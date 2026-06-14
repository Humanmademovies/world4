"""Response schemas for the World4 API (the typed contract the web client uses)."""

from __future__ import annotations

from pydantic import BaseModel, Field


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


class SimResult(BaseModel):
    scenario: str
    model: str
    impacts: list[SimImpact] = Field(default_factory=list)


class LaborCatalog(BaseModel):
    year: int
    regions: list[str] = Field(..., description="Region codes that have demography (labour view).")


class WorkTimeResponse(BaseModel):
    region: str
    production_hours: float = Field(
        ..., description="Hours/year the region must work (production)."
    )
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
