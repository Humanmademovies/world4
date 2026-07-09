"""API tests for the assumptions catalog and uncertainty bands (brick 5)."""

from __future__ import annotations

from fastapi.testclient import TestClient

from world4_api.app import app

client = TestClient(app)

AD = "advertising_demand_share"


def test_assumptions_catalog_is_sourced() -> None:
    catalog = client.get("/api/assumptions").json()
    assert catalog
    for item in catalog:
        assert {"key", "label", "description", "unit", "default", "low", "high", "source"} <= (
            item.keys()
        )
        assert len(item["source"]) > 30
        assert 0.0 <= item["low"] <= item["default"] <= item["high"] <= 1.0


def test_simulate_without_assumptions_has_no_band() -> None:
    sector = client.get("/api/model/info").json()["sectors"][0]
    body = client.post(
        "/api/simulate", json={"levers": [{"sector": sector, "reduction": 0.4}]}
    ).json()
    for impact in body["impacts"]:
        assert impact["delta_low"] is None
        assert impact["delta_high"] is None


def test_simulate_with_assumption_returns_published_band() -> None:
    spec = next(a for a in client.get("/api/assumptions").json() if a["key"] == AD)
    body = client.post("/api/simulate", json={"assumptions": {AD: spec["default"]}}).json()
    assert body["impacts"]
    for impact in body["impacts"]:
        low, mid, high = impact["delta_low"], impact["delta"], impact["delta_high"]
        assert low is not None and high is not None
        # Deltas are <= 0: the high end of the range removes the most.
        assert high <= mid <= low <= 1e-9


def test_simulate_with_unknown_assumption_returns_422() -> None:
    response = client.post("/api/simulate", json={"assumptions": {"not-a-key": 0.1}})
    assert response.status_code == 422


def test_simulate_with_out_of_range_assumption_returns_422() -> None:
    response = client.post("/api/simulate", json={"assumptions": {AD: 2.0}})
    assert response.status_code == 422
