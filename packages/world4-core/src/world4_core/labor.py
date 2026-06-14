"""Work-time accounting — the labour-redistribution identity.

Pure functions, no I/O. Given the hours an economy must work (production-based,
from EXIOBASE) and a country's age structure (from UN WPP), this expresses one
accounting identity per country:

    working_age_pop = sum of population with age in [start_age, retirement_age)
    employed        = working_age_pop * (1 - non_employment_rate)   # "full employment minus n%"
    weekly_hours    = production_hours / employed / weeks_per_year

Set the age bounds and n%, read off the weekly hours per worker. It makes the
trade-off visible: retire younger or start later -> fewer workers -> more hours
each; raise n% -> fewer workers -> more hours each. Ecology and labour are read
side by side, with equal weight.
"""

from __future__ import annotations

import math
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, Field

AGES = 101  # single ages 0..100 (100 is the "100+" bucket)


@dataclass(frozen=True)
class WorkTimeParams:
    """User-set policy knobs for the work-time identity."""

    start_age: int
    retirement_age: int
    non_employment_rate: float = 0.20  # n%: share of working-age not in full-time work
    weeks_per_year: float = 52.0

    def __post_init__(self) -> None:
        if not 0 <= self.start_age < self.retirement_age:
            raise ValueError(
                f"need 0 <= start_age < retirement_age, got {self.start_age}/{self.retirement_age}"
            )
        if not 0.0 <= self.non_employment_rate < 1.0:
            raise ValueError(
                f"non_employment_rate must be in [0, 1), got {self.non_employment_rate}"
            )
        if self.weeks_per_year <= 0:
            raise ValueError(f"weeks_per_year must be positive, got {self.weeks_per_year}")


@dataclass(frozen=True)
class WorkTimeResult:
    """The solved identity for one region."""

    region: str
    production_hours: float
    working_age_population: float
    employed: float
    weekly_hours_per_worker: float


def working_age_population(
    population_by_age: Sequence[float], start_age: int, retirement_age: int
) -> float:
    """Sum population for single ages in ``[start_age, retirement_age)``."""
    upper = min(retirement_age, len(population_by_age))
    return float(sum(population_by_age[age] for age in range(start_age, upper)))


def work_time(
    region: str,
    production_hours: float,
    population_by_age: Sequence[float],
    params: WorkTimeParams,
) -> WorkTimeResult:
    """Solve the work-time identity for one region (forward: read off weekly hours).

    ``weekly_hours_per_worker`` is infinite if no one is employed (degenerate
    case: an empty working-age band or n% = 100%), surfaced honestly rather than
    hidden.
    """
    wap = working_age_population(population_by_age, params.start_age, params.retirement_age)
    employed = wap * (1.0 - params.non_employment_rate)
    weekly = production_hours / employed / params.weeks_per_year if employed > 0 else math.inf
    return WorkTimeResult(
        region=region,
        production_hours=production_hours,
        working_age_population=wap,
        employed=employed,
        weekly_hours_per_worker=weekly,
    )


# --- Inverse solvers --------------------------------------------------------
# The identity has one degree of freedom you read off and three you set:
#     production_hours = working_age_pop(start, retire) * (1 - n) * weekly * weeks
# Fix a *target* on any variable and solve for another. Solvers return ``None``
# when the target is not achievable, rather than inventing a value.


def required_employed(production_hours: float, weekly_hours: float, weeks_per_year: float) -> float:
    """Workers needed to deliver ``production_hours`` at a given weekly load."""
    if weekly_hours <= 0 or weeks_per_year <= 0:
        raise ValueError("weekly_hours and weeks_per_year must be positive")
    return production_hours / (weekly_hours * weeks_per_year)


def solve_non_employment_rate(
    production_hours: float,
    working_age_pop: float,
    weekly_hours_target: float,
    weeks_per_year: float = 52.0,
) -> float | None:
    """n% needed to hit a target weekly load, given the working-age population.

    Returns ``None`` if infeasible: target too low (would need more workers than
    exist, n < 0) or too high (would need almost none, n >= 1).
    """
    if working_age_pop <= 0:
        return None
    n = (
        1.0
        - required_employed(production_hours, weekly_hours_target, weeks_per_year) / working_age_pop
    )
    return n if 0.0 <= n < 1.0 else None


def solve_retirement_age(
    production_hours: float,
    population_by_age: Sequence[float],
    start_age: int,
    non_employment_rate: float,
    weekly_hours_target: float,
    weeks_per_year: float = 52.0,
) -> float | None:
    """Retirement age (fractional) needed to hit a target weekly load.

    Walks up the age distribution until the cumulative working-age population
    reaches what's required, interpolating within the final year. ``None`` if
    even retiring at the oldest age cannot supply enough workers.
    """
    if not 0.0 <= non_employment_rate < 1.0:
        return None
    target_wap = required_employed(production_hours, weekly_hours_target, weeks_per_year) / (
        1.0 - non_employment_rate
    )
    cumulative = 0.0
    for age in range(start_age, len(population_by_age)):
        people = population_by_age[age]
        if cumulative + people >= target_wap:
            fraction = (target_wap - cumulative) / people if people > 0 else 0.0
            return age + fraction
        cumulative += people
    return None


def solve_start_age(
    production_hours: float,
    population_by_age: Sequence[float],
    retirement_age: int,
    non_employment_rate: float,
    weekly_hours_target: float,
    weeks_per_year: float = 52.0,
) -> float | None:
    """Start-of-work age (fractional) needed to hit a target weekly load.

    Walks *down* from the retirement age, adding younger cohorts until enough
    workers are available. ``None`` if even starting at age 0 is not enough.
    """
    if not 0.0 <= non_employment_rate < 1.0:
        return None
    target_wap = required_employed(production_hours, weekly_hours_target, weeks_per_year) / (
        1.0 - non_employment_rate
    )
    cumulative = 0.0
    upper = min(retirement_age, len(population_by_age))
    for age in range(upper - 1, -1, -1):
        people = population_by_age[age]
        if cumulative + people >= target_wap:
            fraction = (target_wap - cumulative) / people if people > 0 else 0.0
            return age + 1 - fraction
        cumulative += people
    return None


# --- Serialisable labour inputs (the compact, precomputed per-region data) ---
# production_hours comes from EXIOBASE (production-based hours worked);
# population_by_age comes from UN WPP (single ages). Built once by
# world4_core.data.labor_build and loaded fast at serve time.


class RegionLabor(BaseModel):
    """Labour inputs for one region."""

    production_hours: float = Field(..., description="Hours worked per year for production.")
    population_by_age: list[float] | None = Field(
        None, description="Population by single age 0..100; None if demography unavailable (RoW)."
    )


class LaborInputs(BaseModel):
    """Per-region labour inputs for a given year (EXIOBASE hours + WPP demography)."""

    year: int
    regions: dict[str, RegionLabor] = Field(default_factory=dict)


def save_labor_inputs(inputs: LaborInputs, path: str | Path) -> Path:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(inputs.model_dump_json(), encoding="utf-8")
    return out


def load_labor_inputs(path: str | Path) -> LaborInputs:
    return LaborInputs.model_validate_json(Path(path).read_text(encoding="utf-8"))
