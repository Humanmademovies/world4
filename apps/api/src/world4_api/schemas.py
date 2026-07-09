"""Response schemas for the World4 API (the typed contract the web client uses)."""

from __future__ import annotations

from pydantic import BaseModel, Field

from world4_core import Lever


class ModelInfo(BaseModel):
    name: str
    regions: list[str]
    sectors: list[str]
    products: int
    extensions: list[str]
    has_footprints: bool = Field(..., description="Whether per-region footprints are available.")


class ImpactInfo(BaseModel):
    key: str
    label: str
    extension: str
    unit: str
    coverage: str = Field(..., description='Honesty flag: "good" | "partial" | "poor" | "unknown".')


class RegionValues(BaseModel):
    impact: str
    unit: str
    coverage: str
    values: dict[str, float] = Field(..., description="Baseline consumption value per region code.")


class SimImpact(BaseModel):
    key: str
    label: str
    unit: str
    coverage: str
    baseline: float
    delta: float = Field(..., description="Change vs baseline; <= 0 in the degrowth seed.")
    relative: float
    # Uncertainty band — only set when the scenario carries sourced assumptions.
    # The band spans the *published* range of the active assumptions, so clients
    # can render assumption-dependent results distinctly from accounting ones.
    delta_low: float | None = Field(
        None, description="Delta with every active assumption at the low end of its sourced range."
    )
    delta_high: float | None = Field(
        None, description="Delta with every active assumption at the high end of its sourced range."
    )
    relative_low: float | None = None
    relative_high: float | None = None


class SimResult(BaseModel):
    scenario: str
    model: str
    impacts: list[SimImpact] = Field(default_factory=list)


class AssumptionInfo(BaseModel):
    """A sourced, contested hypothesis exposed as an explicit slider (brick 5)."""

    key: str
    label: str
    description: str
    unit: str
    default: float
    low: float = Field(..., description="Low end of the published range.")
    high: float = Field(..., description="High end of the published range.")
    source: str = Field(..., description="Citation for default/low/high.")
    note: str


class LaborCatalog(BaseModel):
    year: int
    regions: list[str] = Field(..., description="Region codes that have demography (labour view).")


class WorkTimeResponse(BaseModel):
    region: str
    production_hours: float = Field(
        ..., description="Hours/year to produce (scenario-adjusted if levers are set)."
    )
    baseline_production_hours: float = Field(..., description="Hours before any scenario.")
    production_hours_delta: float = Field(..., description="Change from the scenario (<= 0).")
    working_age_population: float
    employed: float
    weekly_hours_per_worker: float


class SolveResponse(BaseModel):
    region: str
    solve_for: str
    target_weekly_hours: float
    value: float | None = Field(
        ..., description="Solved value, or null if the target is infeasible."
    )
    feasible: bool


class WorkTimeRequest(BaseModel):
    """Work-time query carrying the current demand-reduction levers, so the result
    reflects the scenario (production hours fall as industries shrink)."""

    start_age: int = 20
    retirement_age: int = 65
    non_employment_rate: float = 0.20
    weeks_per_year: float = 52.0
    levers: list[Lever] = Field(default_factory=list)


class SolveRequest(WorkTimeRequest):
    target_weekly_hours: float
    solve_for: str = "retirement_age"


class TargetInfo(BaseModel):
    impact_key: str
    label: str
    unit: str
    allocation: str
    source: str
    note: str
    presets: list[str]
    default_preset: str


class RegionTargetItem(BaseModel):
    impact_key: str
    label: str
    unit: str
    preset: str
    boundary: float
    per_capita_footprint: float
    overshoot_ratio: float = Field(..., description="footprint / boundary (>1 means over).")
    overshoot_day: float | None = None
    source: str
    note: str


class RegionTargets(BaseModel):
    region: str
    items: list[RegionTargetItem] = Field(default_factory=list)


class SectorInfo(BaseModel):
    sector: str
    code: str
    category: str
