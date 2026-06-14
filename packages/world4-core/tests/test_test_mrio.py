"""Integration tests against pymrio's small synthetic MRIO.

These exercise the real data-loading path (pymrio -> MrioModel) without any
download, so they are safe to run in CI.
"""

from __future__ import annotations

import numpy as np
import pytest

from world4_core.data import load_test_model
from world4_core.engine import run_scenario
from world4_core.model import Lever, Scenario


def test_load_test_model_shapes() -> None:
    model = load_test_model()
    assert model.n == len(model.regions) * len(model.sectors)
    assert model.leontief.shape == (model.n, model.n)
    assert model.final_demand.shape == (model.n,)
    assert model.extensions, "test MRIO should expose at least one extension"


def test_reduction_only_yields_non_positive_deltas() -> None:
    model = load_test_model()
    sector = model.sectors[0]
    result = run_scenario(model, Scenario(levers=[Lever(sector=sector, reduction=0.3)]))
    assert result.totals
    for total in result.totals:
        assert total.delta <= 1e-9, f"{total.stressor} delta should be <= 0"
        assert np.isfinite(total.delta)
        assert -1.0 - 1e-9 <= total.relative <= 1e-9


def test_full_global_cut_zeroes_every_footprint() -> None:
    model = load_test_model()
    levers = [Lever(sector=sector, reduction=1.0) for sector in model.sectors]
    result = run_scenario(model, Scenario(levers=levers))
    for total in result.totals:
        if total.baseline != 0.0:
            assert total.relative == pytest.approx(-1.0, abs=1e-6)
