"""API smoke tests using FastAPI's TestClient (no network)."""

from __future__ import annotations

from fastapi.testclient import TestClient

from world4_api.app import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_model_info() -> None:
    response = client.get("/model/info")
    assert response.status_code == 200
    body = response.json()
    assert body["products"] == len(body["regions"]) * len(body["sectors"])
    assert body["extensions"]


def test_post_scenario_returns_non_positive_deltas() -> None:
    info = client.get("/model/info").json()
    sector = info["sectors"][0]
    response = client.post(
        "/scenario",
        json={"name": "t", "levers": [{"sector": sector, "reduction": 0.4}]},
    )
    assert response.status_code == 200
    totals = response.json()["totals"]
    assert totals
    assert all(total["delta"] <= 1e-9 for total in totals)


def test_post_scenario_rejects_increase() -> None:
    # reduction > 1 violates the type contract -> 422 (no positive demand ever).
    response = client.post(
        "/scenario",
        json={"levers": [{"sector": "food", "reduction": 1.5}]},
    )
    assert response.status_code == 422
