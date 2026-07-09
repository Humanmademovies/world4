"""Assumption registry + engine composition tests (brick 5, anti-mathwashing)."""

from __future__ import annotations

import numpy as np
import pytest

from world4_core.assumptions import (
    ASSUMPTIONS,
    available_assumptions,
    band_scenarios,
    get_assumption,
)
from world4_core.engine import build_delta_final_demand, leontief_inverse, run_scenario
from world4_core.model import Lever, Scenario
from world4_core.mrio import Extension, MrioModel

AD = "advertising_demand_share"


def tiny_model() -> MrioModel:
    technical = np.array([[0.1, 0.2], [0.0, 0.1]])
    return MrioModel(
        regions=["R"],
        sectors=["a", "b"],
        index=[("R", "a"), ("R", "b")],
        leontief=leontief_inverse(technical),
        final_demand=np.array([100.0, 50.0]),
        extensions={"co2": Extension("co2", ["co2"], ["kg"], np.array([[1.0, 2.0]]))},
        name="tiny",
    )


def test_every_assumption_is_sourced_and_ordered() -> None:
    assert available_assumptions()
    for a in available_assumptions():
        # No value enters the model unsourced: the citation must be substantive.
        assert len(a.source) > 30, f"{a.key} lacks a citation"
        assert any(ch.isdigit() for ch in a.source), f"{a.key} citation has no year/doi"
        assert 0.0 <= a.low <= a.default <= a.high <= 1.0


def test_unknown_assumption_key_raises() -> None:
    with pytest.raises(ValueError, match="unknown assumption"):
        get_assumption("nope")
    with pytest.raises(ValueError, match="unknown assumption"):
        build_delta_final_demand(tiny_model(), Scenario(assumptions={"nope": 0.1}))


def test_out_of_range_assumption_value_raises() -> None:
    with pytest.raises(ValueError, match="must be in"):
        build_delta_final_demand(tiny_model(), Scenario(assumptions={AD: 1.5}))


def test_assumption_alone_removes_a_uniform_share() -> None:
    delta = build_delta_final_demand(tiny_model(), Scenario(assumptions={AD: 0.1}))
    assert delta == pytest.approx([-10.0, -5.0])
    assert np.all(delta <= 0.0)


def test_assumption_composes_multiplicatively_with_levers() -> None:
    delta = build_delta_final_demand(
        tiny_model(),
        Scenario(levers=[Lever(sector="a", reduction=0.5)], assumptions={AD: 0.1}),
    )
    # Sector a: 1 - (1 - 0.5)(1 - 0.1) = 0.55 removed; sector b: 0.1 removed.
    assert delta == pytest.approx([-55.0, -5.0])


def test_full_lever_plus_assumption_stays_clamped() -> None:
    delta = build_delta_final_demand(
        tiny_model(),
        Scenario(levers=[Lever(sector="a", reduction=1.0)], assumptions={AD: 0.5}),
    )
    # You still cannot remove more than the whole demand.
    assert delta == pytest.approx([-100.0, -25.0])


def test_band_scenarios_none_without_assumptions() -> None:
    assert band_scenarios(Scenario()) is None


def test_band_scenarios_span_the_published_range() -> None:
    spec = ASSUMPTIONS[AD]
    band = band_scenarios(Scenario(assumptions={AD: spec.default}))
    assert band is not None
    low, high = band
    assert low.assumptions[AD] == spec.low
    assert high.assumptions[AD] == spec.high
    # The band reflects the published range, not the slider position.
    band2 = band_scenarios(Scenario(assumptions={AD: spec.low}))
    assert band2 is not None
    assert band2[1].assumptions[AD] == spec.high


def test_band_is_monotonic_on_impacts() -> None:
    model = tiny_model()
    spec = ASSUMPTIONS[AD]

    def co2_delta(value: float) -> float:
        result = run_scenario(model, Scenario(assumptions={AD: value}))
        return result.totals[0].delta

    assert co2_delta(spec.high) <= co2_delta(spec.default) <= co2_delta(spec.low) <= 0.0
