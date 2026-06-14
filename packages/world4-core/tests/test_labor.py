"""Work-time identity + inverse solvers (pure, no data)."""

from __future__ import annotations

from pathlib import Path

import pytest

from world4_core.labor import (
    LaborInputs,
    RegionLabor,
    WorkTimeParams,
    load_labor_inputs,
    save_labor_inputs,
    solve_non_employment_rate,
    solve_retirement_age,
    work_time,
    working_age_population,
)

# Uniform population: 100 people at every single age 0..100.
UNIFORM = [100.0] * 101
# Chosen so the forward identity lands on 40.0 h/week for 20->65, n=0, 50 weeks.
PRODUCTION = 4500 * 50 * 40.0  # working_age(20,65)=4500 * 50 weeks * 40 h


def test_working_age_population() -> None:
    assert working_age_population(UNIFORM, 20, 65) == pytest.approx(4500.0)
    assert working_age_population(UNIFORM, 0, 101) == pytest.approx(10100.0)


def test_forward_identity() -> None:
    result = work_time("X", PRODUCTION, UNIFORM, WorkTimeParams(20, 65, 0.0, 50.0))
    assert result.working_age_population == pytest.approx(4500.0)
    assert result.employed == pytest.approx(4500.0)
    assert result.weekly_hours_per_worker == pytest.approx(40.0)


def test_fewer_workers_means_more_hours() -> None:
    base = work_time("X", PRODUCTION, UNIFORM, WorkTimeParams(20, 65, 0.20, 50.0))
    earlier_retirement = work_time("X", PRODUCTION, UNIFORM, WorkTimeParams(20, 60, 0.20, 50.0))
    assert earlier_retirement.weekly_hours_per_worker > base.weekly_hours_per_worker


def test_inverse_non_employment_rate_roundtrip() -> None:
    params = WorkTimeParams(20, 65, 0.20, 50.0)
    forward = work_time("X", PRODUCTION, UNIFORM, params)
    n = solve_non_employment_rate(
        PRODUCTION, forward.working_age_population, forward.weekly_hours_per_worker, 50.0
    )
    assert n == pytest.approx(0.20)


def test_inverse_retirement_age_roundtrip() -> None:
    # Forward at retire=65 gives 40 h/week; solving for the age at 40 h/week recovers 65.
    age = solve_retirement_age(
        PRODUCTION,
        UNIFORM,
        start_age=20,
        non_employment_rate=0.0,
        weekly_hours_target=40.0,
        weeks_per_year=50.0,
    )
    assert age == pytest.approx(65.0)


def test_infeasible_returns_none() -> None:
    # Target so low it would need more workers than exist -> None, not a fake value.
    assert solve_non_employment_rate(PRODUCTION, 4500.0, 5.0, 50.0) is None
    assert solve_retirement_age(PRODUCTION, UNIFORM, 20, 0.0, 1.0, 50.0) is None


def test_params_validation() -> None:
    with pytest.raises(ValueError):
        WorkTimeParams(65, 20, 0.2, 52)  # start >= retire
    with pytest.raises(ValueError):
        WorkTimeParams(20, 65, 1.0, 52)  # n out of range
    with pytest.raises(ValueError):
        WorkTimeParams(20, 65, 0.2, 0)  # weeks <= 0


def test_labor_inputs_roundtrip(tmp_path: Path) -> None:
    inputs = LaborInputs(
        year=2022,
        regions={
            "FR": RegionLabor(production_hours=PRODUCTION, population_by_age=UNIFORM),
            "WA": RegionLabor(production_hours=1.0, population_by_age=None),
        },
    )
    loaded = load_labor_inputs(save_labor_inputs(inputs, tmp_path / "labor.json"))
    assert loaded.year == 2022
    assert loaded.regions["FR"].population_by_age == UNIFORM
    assert loaded.regions["WA"].population_by_age is None
