"""World4 headless physical-accounting engine.

Public API:

    from world4_core import load_test_model, Scenario, Lever, run_scenario

The engine is UI-agnostic: it consumes a :class:`Scenario` and returns a
:class:`ScenarioResult`. See ``docs/architecture.md`` for the bigger picture and
``docs/modeling/`` for the model's non-negotiable framing.
"""

from world4_core.build import precompute_multipliers, to_served_model
from world4_core.data import load_exiobase_model, load_test_model
from world4_core.engine import build_delta_final_demand, leontief_inverse, run_scenario
from world4_core.footprint import (
    FootprintEntry,
    RegionFootprint,
    consumption_footprint,
    per_capita,
)
from world4_core.labor import (
    LaborInputs,
    RegionLabor,
    WorkTimeParams,
    WorkTimeResult,
    load_labor_inputs,
    save_labor_inputs,
    solve_non_employment_rate,
    solve_retirement_age,
    solve_start_age,
    work_time,
    working_age_population,
)
from world4_core.model import ImpactTotal, Lever, Scenario, ScenarioResult
from world4_core.mrio import Extension, MrioModel
from world4_core.serialize import load_model, save_model

__version__ = "0.1.0"

__all__ = [
    "Extension",
    "FootprintEntry",
    "ImpactTotal",
    "LaborInputs",
    "Lever",
    "MrioModel",
    "RegionFootprint",
    "RegionLabor",
    "Scenario",
    "ScenarioResult",
    "WorkTimeParams",
    "WorkTimeResult",
    "__version__",
    "build_delta_final_demand",
    "consumption_footprint",
    "leontief_inverse",
    "load_exiobase_model",
    "load_labor_inputs",
    "load_model",
    "load_test_model",
    "per_capita",
    "precompute_multipliers",
    "run_scenario",
    "save_labor_inputs",
    "save_model",
    "solve_non_employment_rate",
    "solve_retirement_age",
    "solve_start_age",
    "to_served_model",
    "work_time",
    "working_age_population",
]
