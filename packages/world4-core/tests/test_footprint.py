"""Consumption-based footprint tests on the synthetic MRIO (no download)."""

from __future__ import annotations

import numpy as np
import pytest

from world4_core.data import load_test_model
from world4_core.footprint import consumption_footprint, per_capita


def test_final_demand_by_region_sums_to_total() -> None:
    model = load_test_model()
    assert model.final_demand_by_region is not None
    assert model.final_demand_by_region.shape == (model.n, len(model.regions))
    # Summing over consuming regions must recover the total final demand.
    assert model.final_demand_by_region.sum(axis=1) == pytest.approx(model.final_demand)


def test_consumption_footprint_entries_are_finite() -> None:
    model = load_test_model()
    footprint = consumption_footprint(model, model.regions[0])
    assert footprint.entries
    for entry in footprint.entries:
        assert np.isfinite(entry.value)


def test_regional_footprints_sum_to_global_total() -> None:
    """sum_r (S @ L @ y_r) == S @ L @ y_total — consumption- and production-based
    totals coincide for the whole system."""
    model = load_test_model()
    global_output = model.leontief @ model.final_demand

    per_region_sum: dict[tuple[str, str], float] = {}
    for region in model.regions:
        for entry in consumption_footprint(model, region).entries:
            key = (entry.extension, entry.stressor)
            per_region_sum[key] = per_region_sum.get(key, 0.0) + entry.value

    for ext in model.extensions.values():
        global_impact = ext.S @ global_output
        for i, stressor in enumerate(ext.stressors):
            assert per_region_sum[(ext.name, stressor)] == pytest.approx(
                float(global_impact[i]), rel=1e-9
            )


def test_consuming_demand_unknown_region_raises() -> None:
    model = load_test_model()
    with pytest.raises(ValueError, match="unknown region"):
        model.consuming_demand("not-a-region")


def test_per_capita() -> None:
    assert per_capita(10.0, 2.0) == pytest.approx(5.0)
    with pytest.raises(ValueError, match="population must be positive"):
        per_capita(10.0, 0.0)
