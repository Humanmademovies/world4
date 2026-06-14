"""Headline impact catalog.

EXIOBASE exposes ~1500 raw stressors — far too many for a UI. This module curates
a small set of **headline impacts**, each aggregating same-unit stressors within
one extension, and carries an honest ``coverage`` flag (the impact vector is
unevenly populated; we never fake uniform coverage).

The catalog is *derived from the loaded model*: a curated impact is included only
if it actually matches stressors that share a single unit. On an unknown model
(e.g. the synthetic test MRIO) a generic per-extension fallback is used so the API
always has something to serve.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass

import numpy as np

from world4_core.mrio import MrioModel


@dataclass(frozen=True)
class ImpactSpec:
    """A curated impact definition: which stressors of an extension to aggregate."""

    key: str
    label: str
    extension: str
    match: Callable[[str], bool]
    coverage: str  # "good" | "partial" | "poor"


@dataclass(frozen=True)
class Impact:
    """A resolved impact for a specific model (stressors selected, unit fixed)."""

    key: str
    label: str
    extension: str
    unit: str
    coverage: str
    stressor_indices: tuple[int, ...]


# Curated headline impacts for EXIOBASE 3. Predicates are matched against the
# model's actual stressor labels, so a non-matching spec is simply dropped.
CURATED: list[ImpactSpec] = [
    ImpactSpec(
        "co2_combustion",
        "CO2 — combustion",
        "air_emissions",
        lambda s: s == "CO2 - combustion - air",
        "partial",  # non-combustion/process CO2 is not populated for footprints
    ),
    ImpactSpec("water_blue", "Water — blue", "water", lambda s: "Blue" in s, "good"),
    ImpactSpec("land_use", "Land use", "land", lambda s: True, "good"),
    ImpactSpec("material", "Material extraction", "material", lambda s: True, "partial"),
    ImpactSpec("energy", "Energy use", "energy", lambda s: True, "good"),
    ImpactSpec(
        "employment_hours",
        "Employment — hours",
        "employment",
        lambda s: "hour" in s.lower(),
        "good",
    ),
]


def _resolve(model: MrioModel, spec: ImpactSpec) -> Impact | None:
    ext = model.extensions.get(spec.extension)
    if ext is None:
        return None
    indices = [i for i, stressor in enumerate(ext.stressors) if spec.match(stressor)]
    if not indices:
        return None
    units = {ext.units[i] for i in indices}
    if len(units) != 1:  # cannot aggregate across different units — drop honestly
        return None
    return Impact(spec.key, spec.label, spec.extension, units.pop(), spec.coverage, tuple(indices))


def _generic(model: MrioModel) -> list[Impact]:
    """Fallback for unknown models: one impact per extension, most-common unit."""
    impacts: list[Impact] = []
    for name, ext in model.extensions.items():
        if not ext.stressors:
            continue
        common_unit, _ = Counter(ext.units).most_common(1)[0]
        indices = tuple(i for i, u in enumerate(ext.units) if u == common_unit)
        impacts.append(Impact(name, name, name, common_unit, "unknown", indices))
    return impacts


def available_impacts(model: MrioModel) -> list[Impact]:
    """Resolved headline impacts for ``model`` (curated, with a generic fallback)."""
    curated = [impact for spec in CURATED if (impact := _resolve(model, spec)) is not None]
    return curated if curated else _generic(model)


def _stressor_totals(model: MrioModel, impact: Impact, demand: np.ndarray) -> np.ndarray:
    """Per-selected-stressor embodied totals for a demand vector."""
    multiplier = model.multiplier(impact.extension)
    rows = multiplier[list(impact.stressor_indices), :]
    return np.asarray(rows @ demand, dtype=float)


def impact_value(model: MrioModel, impact: Impact, demand: np.ndarray) -> float:
    """Aggregate an impact for a demand vector (NaN stressors dropped, honestly)."""
    return float(np.nansum(_stressor_totals(model, impact, demand)))


def impact_by_region(model: MrioModel, impact: Impact) -> dict[str, float]:
    """Baseline consumption value of ``impact`` for every region."""
    if model.final_demand_by_region is None:
        raise ValueError("final_demand_by_region not loaded; cannot compute per-region impacts")
    multiplier = model.multiplier(impact.extension)
    rows = multiplier[list(impact.stressor_indices), :]
    per_region = np.nansum(rows @ model.final_demand_by_region, axis=0)
    return {region: float(per_region[j]) for j, region in enumerate(model.regions)}
