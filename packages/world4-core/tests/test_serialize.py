"""Served-model build + serialization round-trip, validated against the L path."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from world4_core import (
    consumption_footprint,
    leontief_inverse,
    load_model,
    load_test_model,
    run_scenario,
    save_model,
    to_served_model,
)
from world4_core.model import Lever, Scenario
from world4_core.mrio import Extension, MrioModel


def test_served_roundtrip_matches_full_model(tmp_path: Path) -> None:
    full = load_test_model()
    served = to_served_model(full)
    loaded = load_model(save_model(served, tmp_path / "model.npz"))

    assert loaded.regions == full.regions
    assert loaded.sectors == full.sectors
    assert loaded.n == full.n
    assert loaded.leontief is None
    assert loaded.multipliers is not None

    scenario = Scenario(levers=[Lever(sector=full.sectors[0], reduction=0.4)])
    full_totals = {(t.extension, t.stressor): t.delta for t in run_scenario(full, scenario).totals}
    loaded_totals = {
        (t.extension, t.stressor): t.delta for t in run_scenario(loaded, scenario).totals
    }
    assert full_totals.keys() == loaded_totals.keys()
    for key, value in full_totals.items():
        assert loaded_totals[key] == pytest.approx(value, rel=1e-9, abs=1e-9)

    region = full.regions[0]
    full_fp = {
        (e.extension, e.stressor): e.value for e in consumption_footprint(full, region).entries
    }
    loaded_fp = {
        (e.extension, e.stressor): e.value for e in consumption_footprint(loaded, region).entries
    }
    for key, value in full_fp.items():
        assert loaded_fp[key] == pytest.approx(value, rel=1e-9, abs=1e-9)


def test_production_hours_multiplier_survives_roundtrip(tmp_path: Path) -> None:
    model = MrioModel(
        regions=["R"],
        sectors=["a", "b"],
        index=[("R", "a"), ("R", "b")],
        final_demand=np.array([100.0, 50.0]),
        leontief=leontief_inverse(np.array([[0.1, 0.2], [0.0, 0.1]])),
        extensions={
            "employment": Extension("employment", ["hrs"], ["M.hr"], np.array([[1.0, 2.0]]))
        },
    )
    served = to_served_model(model)
    assert served.production_hours_multiplier is not None
    loaded = load_model(save_model(served, tmp_path / "m.npz"))
    assert loaded.production_hours_multiplier is not None
    assert loaded.production_hours_multiplier == pytest.approx(served.production_hours_multiplier)
