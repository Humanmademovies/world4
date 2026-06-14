"""FastAPI application exposing the World4 engine.

Thin by design: it loads a model once and forwards work to ``world4_core``. All
modelling lives in the core.

Model selection: if ``WORLD4_MODEL_PATH`` points to a served artifact it is loaded
(fast); otherwise the synthetic test model is used — so CI and a fresh clone work
offline, while a machine with the EXIOBASE artifact gets the real dashboard.

Routing: the JSON API lives under ``/api``; in production the built web client
(``apps/web/dist``) is served as static files at ``/`` (single origin, no CORS).
"""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from world4_api.schemas import ImpactInfo, ModelInfo, RegionValues, SimImpact, SimResult
from world4_core import MrioModel, Scenario, load_model, load_test_model, run_scenario
from world4_core.engine import build_delta_final_demand
from world4_core.impacts import available_impacts, impact_by_region, impact_value


@lru_cache(maxsize=1)
def get_model() -> MrioModel:
    path = os.getenv("WORLD4_MODEL_PATH")
    if path and Path(path).exists():
        return load_model(path)
    return load_test_model()


def _cors_origins() -> list[str]:
    return [origin for origin in os.getenv("WORLD4_CORS_ORIGINS", "").split(",") if origin]


def _web_dist() -> Path:
    override = os.getenv("WORLD4_WEB_DIST")
    if override:
        return Path(override)
    return Path(__file__).resolve().parents[3] / "web" / "dist"


api = APIRouter(prefix="/api")


@api.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@api.get("/model/info", response_model=ModelInfo)
def model_info() -> ModelInfo:
    model = get_model()
    return ModelInfo(
        name=model.name,
        regions=model.regions,
        sectors=model.sectors,
        products=model.n,
        extensions=list(model.extensions),
        has_footprints=model.final_demand_by_region is not None,
    )


@api.get("/impacts", response_model=list[ImpactInfo])
def list_impacts() -> list[ImpactInfo]:
    model = get_model()
    return [
        ImpactInfo(
            key=i.key, label=i.label, extension=i.extension, unit=i.unit, coverage=i.coverage
        )
        for i in available_impacts(model)
    ]


@api.get("/impacts/{key}/by-region", response_model=RegionValues)
def impact_region_values(key: str) -> RegionValues:
    model = get_model()
    impact = next((i for i in available_impacts(model) if i.key == key), None)
    if impact is None:
        raise HTTPException(status_code=404, detail=f"unknown impact {key!r}")
    if model.final_demand_by_region is None:
        raise HTTPException(status_code=409, detail="model has no per-region footprints")
    return RegionValues(
        impact=impact.key,
        unit=impact.unit,
        coverage=impact.coverage,
        values=impact_by_region(model, impact),
    )


@api.post("/simulate", response_model=SimResult)
def simulate(scenario: Scenario) -> SimResult:
    model = get_model()
    delta_y = build_delta_final_demand(model, scenario)
    impacts: list[SimImpact] = []
    for impact in available_impacts(model):
        baseline = impact_value(model, impact, model.final_demand)
        delta = impact_value(model, impact, delta_y)
        relative = delta / baseline if baseline else 0.0
        impacts.append(
            SimImpact(
                key=impact.key,
                label=impact.label,
                unit=impact.unit,
                coverage=impact.coverage,
                baseline=baseline,
                delta=delta,
                relative=relative,
            )
        )
    return SimResult(scenario=scenario.name, model=model.name, impacts=impacts)


@api.post("/scenario")
def post_scenario(scenario: Scenario) -> dict[str, object]:
    """Full per-stressor result (every extension/stressor), for advanced use."""
    return run_scenario(get_model(), scenario).model_dump()


def create_app() -> FastAPI:
    app = FastAPI(
        title="World4 API",
        version="0.2.0",
        summary="Physical accounting of world consumption — degrowth-at-constant-apparatus seed.",
    )

    origins = _cors_origins()
    if origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_methods=["GET", "POST"],
            allow_headers=["*"],
        )

    @app.exception_handler(ValueError)
    async def _value_error(request: Request, exc: ValueError) -> JSONResponse:
        # Engine guards (unknown sector/region, etc.) surface as 422, not 500.
        return JSONResponse(status_code=422, content={"detail": str(exc)})

    app.include_router(api)

    dist = _web_dist()
    if dist.is_dir():
        app.mount("/", StaticFiles(directory=str(dist), html=True), name="web")

    return app


app = create_app()


def run() -> None:  # pragma: no cover - thin uvicorn entrypoint
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("WORLD4_API_HOST", "127.0.0.1"),
        port=int(os.getenv("WORLD4_API_PORT", "8000")),
    )
