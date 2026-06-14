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

from world4_api.schemas import (
    ImpactInfo,
    LaborCatalog,
    ModelInfo,
    RegionValues,
    SimImpact,
    SimResult,
    SolveRequest,
    SolveResponse,
    WorkTimeRequest,
    WorkTimeResponse,
)
from world4_core import (
    LaborInputs,
    Lever,
    MrioModel,
    Scenario,
    WorkTimeParams,
    load_labor_inputs,
    load_model,
    load_test_model,
    run_scenario,
    solve_non_employment_rate,
    solve_retirement_age,
    solve_start_age,
    work_time,
    working_age_population,
)
from world4_core.engine import build_delta_final_demand
from world4_core.impacts import available_impacts, impact_by_region, impact_value


@lru_cache(maxsize=1)
def get_model() -> MrioModel:
    path = os.getenv("WORLD4_MODEL_PATH")
    if path and Path(path).exists():
        return load_model(path)
    return load_test_model()


@lru_cache(maxsize=1)
def get_labor() -> LaborInputs | None:
    """Load the labour-inputs artifact if configured, else None (no labour view)."""
    path = os.getenv("WORLD4_LABOR_PATH")
    if path and Path(path).exists():
        return load_labor_inputs(path)
    return None


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


def _require_labor() -> LaborInputs:
    labor = get_labor()
    if labor is None:
        raise HTTPException(
            status_code=404, detail="labour data not loaded (set WORLD4_LABOR_PATH)"
        )
    return labor


def _region_population(region: str) -> tuple[float, list[float]]:
    """Return (production_hours, population_by_age) for a region, or raise."""
    region_labor = _require_labor().regions.get(region)
    if region_labor is None:
        raise HTTPException(status_code=404, detail=f"unknown region {region!r}")
    if region_labor.population_by_age is None:
        raise HTTPException(
            status_code=409, detail=f"no demography for region {region!r} (Rest-of-World aggregate)"
        )
    return region_labor.production_hours, region_labor.population_by_age


def _adjust_production_hours(
    region: str, baseline: float, levers: list[Lever]
) -> tuple[float, float]:
    """Apply the scenario's effect on a region's production hours: (adjusted, delta).

    Uses the model's production-hours multiplier ``P``: ``Δhours = (P @ Δy)[region]``.
    Falls back to no change if there are no levers or the model has no ``P``.
    """
    model = get_model()
    multiplier = model.production_hours_multiplier
    if not levers or multiplier is None or region not in model.regions:
        return baseline, 0.0
    delta_y = build_delta_final_demand(model, Scenario(levers=levers))
    delta = float((multiplier @ delta_y)[model.regions.index(region)])
    return baseline + delta, delta


def _solve_value(
    production_hours: float,
    population: list[float],
    target_weekly_hours: float,
    solve_for: str,
    params: WorkTimeParams,
) -> float | None:
    if solve_for == "non_employment_rate":
        wap = working_age_population(population, params.start_age, params.retirement_age)
        return solve_non_employment_rate(
            production_hours, wap, target_weekly_hours, params.weeks_per_year
        )
    if solve_for == "retirement_age":
        return solve_retirement_age(
            production_hours,
            population,
            params.start_age,
            params.non_employment_rate,
            target_weekly_hours,
            params.weeks_per_year,
        )
    if solve_for == "start_age":
        return solve_start_age(
            production_hours,
            population,
            params.retirement_age,
            params.non_employment_rate,
            target_weekly_hours,
            params.weeks_per_year,
        )
    raise HTTPException(
        status_code=422, detail="solve_for must be retirement_age | non_employment_rate | start_age"
    )


def _work_time_response(
    region: str,
    baseline: float,
    adjusted: float,
    delta: float,
    population: list[float],
    params: WorkTimeParams,
) -> WorkTimeResponse:
    result = work_time(region, adjusted, population, params)
    return WorkTimeResponse(
        region=region,
        production_hours=adjusted,
        baseline_production_hours=baseline,
        production_hours_delta=delta,
        working_age_population=result.working_age_population,
        employed=result.employed,
        weekly_hours_per_worker=result.weekly_hours_per_worker,
    )


@api.get("/labor", response_model=LaborCatalog)
def labor_catalog() -> LaborCatalog:
    labor = _require_labor()
    regions = [code for code, r in labor.regions.items() if r.population_by_age is not None]
    return LaborCatalog(year=labor.year, regions=regions)


@api.get("/labor/{region}", response_model=WorkTimeResponse)
def labor_region(
    region: str,
    start_age: int = 20,
    retirement_age: int = 65,
    non_employment_rate: float = 0.20,
    weeks_per_year: float = 52.0,
) -> WorkTimeResponse:
    """Baseline work-time for a region (no scenario)."""
    baseline, population = _region_population(region)
    params = WorkTimeParams(start_age, retirement_age, non_employment_rate, weeks_per_year)
    return _work_time_response(region, baseline, baseline, 0.0, population, params)


@api.post("/labor/{region}/worktime", response_model=WorkTimeResponse)
def labor_worktime(region: str, request: WorkTimeRequest) -> WorkTimeResponse:
    """Work-time for a region under the current scenario (levers reduce hours)."""
    baseline, population = _region_population(region)
    adjusted, delta = _adjust_production_hours(region, baseline, request.levers)
    params = WorkTimeParams(
        request.start_age,
        request.retirement_age,
        request.non_employment_rate,
        request.weeks_per_year,
    )
    return _work_time_response(region, baseline, adjusted, delta, population, params)


@api.get("/labor/{region}/solve", response_model=SolveResponse)
def labor_solve(
    region: str,
    target_weekly_hours: float,
    solve_for: str = "retirement_age",
    start_age: int = 20,
    retirement_age: int = 65,
    non_employment_rate: float = 0.20,
    weeks_per_year: float = 52.0,
) -> SolveResponse:
    """Inverse solve on the baseline (no scenario)."""
    baseline, population = _region_population(region)
    params = WorkTimeParams(start_age, retirement_age, non_employment_rate, weeks_per_year)
    value = _solve_value(baseline, population, target_weekly_hours, solve_for, params)
    return SolveResponse(
        region=region,
        solve_for=solve_for,
        target_weekly_hours=target_weekly_hours,
        value=value,
        feasible=value is not None,
    )


@api.post("/labor/{region}/solve", response_model=SolveResponse)
def labor_solve_scenario(region: str, request: SolveRequest) -> SolveResponse:
    """Inverse solve under the current scenario (adjusted production hours)."""
    baseline, population = _region_population(region)
    adjusted, _ = _adjust_production_hours(region, baseline, request.levers)
    params = WorkTimeParams(
        request.start_age,
        request.retirement_age,
        request.non_employment_rate,
        request.weeks_per_year,
    )
    value = _solve_value(
        adjusted, population, request.target_weekly_hours, request.solve_for, params
    )
    return SolveResponse(
        region=region,
        solve_for=request.solve_for,
        target_weekly_hours=request.target_weekly_hours,
        value=value,
        feasible=value is not None,
    )


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
