"""API tests using FastAPI's TestClient (test model, no network/data)."""

from __future__ import annotations

from fastapi.testclient import TestClient

from world4_api.app import app

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
