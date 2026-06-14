"""API tests using FastAPI's TestClient (test model, no network/data)."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from world4_api.app import app, get_labor
from world4_core import LaborInputs, RegionLabor, save_labor_inputs

client = TestClient(app)


def test_health() -> None:
    assert client.get("/api/health").json() == {"status": "ok"}


def test_model_info() -> None:
    body = client.get("/api/model/info").json()
    assert body["products"] == len(body["regions"]) * len(body["sectors"])
    assert body["extensions"]
    assert body["has_footprints"] is True


def test_impacts_catalog() -> None:
    impacts = client.get("/api/impacts").json()
    assert impacts
    for impact in impacts:
        assert {"key", "label", "extension", "unit", "coverage"} <= impact.keys()


def test_impact_by_region() -> None:
    info = client.get("/api/model/info").json()
    key = client.get("/api/impacts").json()[0]["key"]
    body = client.get(f"/api/impacts/{key}/by-region").json()
    assert set(body["values"]) == set(info["regions"])


def test_impact_by_region_unknown_returns_404() -> None:
    assert client.get("/api/impacts/not-a-key/by-region").status_code == 404


def test_simulate_reduction_only() -> None:
    sector = client.get("/api/model/info").json()["sectors"][0]
    body = client.post(
        "/api/simulate", json={"name": "t", "levers": [{"sector": sector, "reduction": 0.4}]}
    ).json()
    assert body["impacts"]
    assert all(impact["delta"] <= 1e-9 for impact in body["impacts"])


def test_simulate_rejects_increase() -> None:
    response = client.post("/api/simulate", json={"levers": [{"sector": "food", "reduction": 1.5}]})
    assert response.status_code == 422


def test_simulate_unknown_sector_returns_422() -> None:
    response = client.post(
        "/api/simulate", json={"levers": [{"sector": "not-a-sector", "reduction": 0.5}]}
    )
    assert response.status_code == 422


def test_labor_endpoints(tmp_path, monkeypatch) -> None:  # type: ignore[no-untyped-def]
    # No labour artifact configured -> 404.
    monkeypatch.delenv("WORLD4_LABOR_PATH", raising=False)
    get_labor.cache_clear()
    assert client.get("/api/labor").status_code == 404

    # Configure a tiny artifact: production = 4500*52*40 -> 40 h/week at 20..65, n=0.
    inputs = LaborInputs(
        year=2022,
        regions={
            "FR": RegionLabor(production_hours=4500 * 52 * 40.0, population_by_age=[100.0] * 101),
            "WA": RegionLabor(production_hours=1.0, population_by_age=None),
        },
    )
    path = save_labor_inputs(inputs, tmp_path / "labor.json")
    monkeypatch.setenv("WORLD4_LABOR_PATH", str(path))
    get_labor.cache_clear()
    try:
        assert client.get("/api/labor").json()["regions"] == ["FR"]  # WA has no demography

        forward = client.get(
            "/api/labor/FR",
            params={"start_age": 20, "retirement_age": 65, "non_employment_rate": 0.0},
        ).json()
        assert forward["weekly_hours_per_worker"] == pytest.approx(40.0)

        solved = client.get(
            "/api/labor/FR/solve",
            params={
                "target_weekly_hours": 40,
                "solve_for": "retirement_age",
                "start_age": 20,
                "non_employment_rate": 0.0,
            },
        ).json()
        assert solved["feasible"] is True
        assert solved["value"] == pytest.approx(65.0)

        # POST worktime with no levers matches the baseline forward.
        post = client.post(
            "/api/labor/FR/worktime",
            json={"start_age": 20, "retirement_age": 65, "non_employment_rate": 0.0, "levers": []},
        ).json()
        assert post["weekly_hours_per_worker"] == pytest.approx(40.0)
        assert post["production_hours_delta"] == 0.0
        assert post["baseline_production_hours"] == pytest.approx(post["production_hours"])

        # POST solve under (empty) scenario.
        psolve = client.post(
            "/api/labor/FR/solve",
            json={
                "target_weekly_hours": 40,
                "solve_for": "retirement_age",
                "start_age": 20,
                "non_employment_rate": 0.0,
                "levers": [],
            },
        ).json()
        assert psolve["feasible"] is True
        assert psolve["value"] == pytest.approx(65.0)

        # Rest-of-World aggregate has no demography -> 409.
        assert client.get("/api/labor/WA").status_code == 409
    finally:
        get_labor.cache_clear()
