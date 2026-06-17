"""Sustainability targets — sourced per-capita boundaries, per limit.

Each target compares a region's **per-capita consumption footprint** to a
**sourced equal-per-capita boundary**, giving an overshoot ratio (and an
"overshoot day"). There is **no aggregate index**: every limit keeps its own
metric. Where no defensible per-capita boundary exists (land, energy) there is
simply no target — see ``docs/modeling/targets-sources.md``.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class Target(BaseModel):
    """A sourced per-capita boundary for one impact, with ambition presets."""

    impact_key: str
    label: str
    unit: str = Field(..., description="Per-capita unit of the boundary, e.g. 'tCO2/cap'.")
    factor: float = Field(
        ..., description="Multiply the footprint's native total by this to reach the target unit."
    )
    allocation: str = "equal per capita"
    source: str
    note: str = ""
    presets: dict[str, float] = Field(..., description="Ambition name -> per-capita boundary.")
    default_preset: str


class TargetAssessment(BaseModel):
    """A region's footprint judged against a target."""

    impact_key: str
    preset: str
    unit: str
    boundary: float
    per_capita_footprint: float
    overshoot_ratio: float = Field(..., description="footprint / boundary (>1 means over).")
    overshoot_day: float | None = Field(
        None, description="Day-of-year the annual budget is used up (365/ratio); None if ratio<=0."
    )


# Sourced registry. Impacts absent here (land, energy, employment) have no target.
TARGETS: dict[str, Target] = {
    "co2_combustion": Target(
        impact_key="co2_combustion",
        label="CO2 — combustion",
        unit="tCO2/cap",
        factor=1e-3,  # kg -> t
        source=(
            "O'Neill et al. 2018 (2C, 1.61 tCO2/cap, doi:10.1038/s41893-018-0021-4); "
            "Hot or Cool 1.5-Degree Lifestyles (2.5/0.7 tCO2e for 2030/2050)."
        ),
        note="Boundary is total/eq CO2; our footprint is combustion CO2 only — order-of-magnitude.",
        presets={"2C": 1.61, "1.5C-2030": 2.5, "1.5C-2050": 0.7},
        default_preset="2C",
    ),
    "water_blue": Target(
        impact_key="water_blue",
        label="Water — blue",
        unit="m3/cap",
        factor=1e6,  # Mm3 -> m3
        source="O'Neill et al. 2018 (574 m3/cap; planetary boundary 4000 km3/yr).",
        presets={"planetary-boundary": 574.0},
        default_preset="planetary-boundary",
    ),
    "material": Target(
        impact_key="material",
        label="Material extraction",
        unit="t/cap",
        factor=1e3,  # kt -> t
        source="O'Neill et al. 2018 (7.2 t/cap material footprint).",
        note="Equivalence of our extraction-based footprint to RMC to be confirmed.",
        presets={"oneill": 7.2},
        default_preset="oneill",
    ),
}


def available_targets() -> list[Target]:
    return list(TARGETS.values())


def get_target(impact_key: str) -> Target | None:
    return TARGETS.get(impact_key)


def assess(
    target: Target, preset: str, footprint_native_total: float, population: float
) -> TargetAssessment:
    """Compare a region's footprint to the boundary for a given ambition preset."""
    if preset not in target.presets:
        raise ValueError(
            f"unknown preset {preset!r} for {target.impact_key}; have {list(target.presets)}"
        )
    if population <= 0:
        raise ValueError(f"population must be positive, got {population}")
    boundary = target.presets[preset]
    per_capita = footprint_native_total * target.factor / population
    ratio = per_capita / boundary if boundary > 0 else 0.0
    return TargetAssessment(
        impact_key=target.impact_key,
        preset=preset,
        unit=target.unit,
        boundary=boundary,
        per_capita_footprint=per_capita,
        overshoot_ratio=ratio,
        overshoot_day=365.0 / ratio if ratio > 0 else None,
    )
