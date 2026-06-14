"""Consumption-based (footprint) accounting.

A region's footprint attributes to it the *global* upstream pressures embodied in
everything it finally consumes:

    footprint(region) = S @ L @ y_region

where ``y_region`` is that region's final demand over all products, worldwide.
This is the standard consumption-based accounting used for per-capita footprints,
and the basis of the brick-1 binary validation (reproduce a published figure).
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from world4_core.mrio import MrioModel


class FootprintEntry(BaseModel):
    """One stressor's embodied total for a region (its own metric, no aggregation)."""

    extension: str
    stressor: str
    unit: str
    value: float


class RegionFootprint(BaseModel):
    """A region's consumption-based footprint across all stressors."""

    region: str
    model: str
    entries: list[FootprintEntry] = Field(default_factory=list)

    def get(self, extension: str, stressor: str) -> FootprintEntry | None:
        """Return the matching entry, or ``None`` if absent."""
        for entry in self.entries:
            if entry.extension == extension and entry.stressor == stressor:
                return entry
        return None


def consumption_footprint(model: MrioModel, region: str) -> RegionFootprint:
    """Compute the consumption-based footprint of ``region`` for every stressor."""
    demand = model.consuming_demand(region)
    output = model.leontief @ demand
    entries: list[FootprintEntry] = []
    for ext in model.extensions.values():
        embodied = ext.S @ output
        for i, stressor in enumerate(ext.stressors):
            entries.append(
                FootprintEntry(
                    extension=ext.name,
                    stressor=stressor,
                    unit=ext.units[i],
                    value=float(embodied[i]),
                )
            )
    return RegionFootprint(region=region, model=model.name, entries=entries)


def per_capita(value: float, population: float) -> float:
    """Divide a footprint total by a (sourced) population. Raises if population <= 0."""
    if population <= 0:
        raise ValueError(f"population must be positive, got {population}")
    return value / population
