"""Engine unit tests on a hand-built, deterministic MRIO (no pymrio needed)."""

from __future__ import annotations

import numpy as np
import pytest

from world4_core.build import production_hours_multiplier
from world4_core.engine import build_delta_final_demand, leontief_inverse, run_scenario
from world4_core.model import Lever, Scenario
from world4_core.mrio import Extension, MrioModel


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


def test_leontief_inverse_known_values() -> None:
    assert leontief_inverse(np.array([[0.0]]))[0, 0] == pytest.approx(1.0)
    assert leontief_inverse(np.array([[0.5]]))[0, 0] == pytest.approx(2.0)
    # 2x2 sanity check against the textbook identity x = L @ y.
    technical = np.array([[0.2, 0.1], [0.3, 0.4]])
    inverse = leontief_inverse(technical)
    assert inverse @ (np.eye(2) - technical) == pytest.approx(np.eye(2))


def test_leontief_inverse_rejects_non_square() -> None:
    with pytest.raises(ValueError, match="square"):
        leontief_inverse(np.array([[0.1, 0.2]]))


def test_delta_final_demand_is_reduction_only() -> None:
    model = tiny_model()
    delta = build_delta_final_demand(model, Scenario(levers=[Lever(sector="a", reduction=0.5)]))
    assert delta == pytest.approx([-50.0, 0.0])
    assert np.all(delta <= 0.0)


def test_overlapping_levers_clamp_at_full_removal() -> None:
    model = tiny_model()
    delta = build_delta_final_demand(
        model,
        Scenario(levers=[Lever(sector="a", reduction=0.8), Lever(sector="a", reduction=0.8)]),
    )
    # 0.8 + 0.8 clamps to 1.0 -> cannot remove more than the whole demand.
    assert delta == pytest.approx([-100.0, 0.0])


def test_run_scenario_full_cut_equals_negative_baseline() -> None:
    model = tiny_model()
    result = run_scenario(
        model,
        Scenario(levers=[Lever(sector="a", reduction=1.0), Lever(sector="b", reduction=1.0)]),
    )
    (total,) = result.totals
    assert total.delta == pytest.approx(-total.baseline)
    assert total.relative == pytest.approx(-1.0)


def test_production_hours_multiplier() -> None:
    # 1 region, 2 sectors; employment-hours intensity h = [1, 2] M.hr per M.EUR.
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
    p = production_hours_multiplier(model)
    assert p is not None
    assert p.shape == (1, 2)
    # P @ y must equal the baseline production hours: 1e6 * Σ h[p]·x[p], x = L @ y.
    output = model.leontief @ model.final_demand
    expected = 1e6 * (1.0 * output[0] + 2.0 * output[1])
    assert (p @ model.final_demand)[0] == pytest.approx(expected)


def test_production_hours_multiplier_none_without_hours() -> None:
    model = MrioModel(
        regions=["R"],
        sectors=["a"],
        index=[("R", "a")],
        final_demand=np.array([1.0]),
        leontief=np.array([[1.0]]),
        extensions={"co2": Extension("co2", ["c"], ["kg"], np.array([[1.0]]))},
    )
    assert production_hours_multiplier(model) is None


def test_unknown_sector_raises() -> None:
    model = tiny_model()
    with pytest.raises(ValueError, match="unknown sector"):
        run_scenario(model, Scenario(levers=[Lever(sector="nope", reduction=0.5)]))


def test_scenario_result_is_json_serialisable() -> None:
    model = tiny_model()
    result = run_scenario(model, Scenario(name="s", levers=[Lever(sector="a", reduction=0.3)]))
    payload = result.model_dump_json()
    assert '"scenario":"s"' in payload.replace(" ", "")
