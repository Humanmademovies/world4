"""FastAPI application exposing the World4 engine.

Thin by design: it loads a model once and forwards scenarios to
:func:`world4_core.engine.run_scenario`. All modelling lives in the core.
"""

from __future__ import annotations

import os
from functools import lru_cache

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from world4_core import MrioModel, Scenario, ScenarioResult, load_test_model, run_scenario


@lru_cache(maxsize=1)
def get_model() -> MrioModel:
    """Load and cache the active model.

    Seed: the synthetic test MRIO. The EXIOBASE brick swaps this for a real,
    pre-parsed model (selected via configuration), without touching the routes.
    """
    return load_test_model()


def _cors_origins() -> list[str]:
    return [origin for origin in os.getenv("WORLD4_CORS_ORIGINS", "").split(",") if origin]


def create_app() -> FastAPI:
    app = FastAPI(
        title="World4 API",
        version="0.1.0",
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

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/model/info")
    def model_info() -> dict[str, object]:
        model = get_model()
        return {
            "name": model.name,
            "regions": model.regions,
            "sectors": model.sectors,
            "products": model.n,
            "extensions": list(model.extensions),
        }

    @app.post("/scenario", response_model=ScenarioResult)
    def post_scenario(scenario: Scenario) -> ScenarioResult:
        return run_scenario(get_model(), scenario)

    return app


app = create_app()


def run() -> None:  # pragma: no cover - thin uvicorn entrypoint
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("WORLD4_API_HOST", "127.0.0.1"),
        port=int(os.getenv("WORLD4_API_PORT", "8000")),
    )
