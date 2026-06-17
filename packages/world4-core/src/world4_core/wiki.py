"""Computed, data-driven documentation for the in-app wiki.

Rather than hand-writing 200 sector paragraphs, we derive each sector's profile
from the model itself — honest and always up to date. A profile answers, for a
chosen region: *if you pull this sector's lever, what does it affect, and how much?*

- **Impact drivers**: the share of the region's footprint (per impact) that is
  embodied in that region's final demand of the sector — comparable across impacts
  because it's a percentage.
- **Labour**: the production hours in the region tied to that consumption (i.e.
  what a full reduction would free).

Sector metadata (code, consumption category) comes from a small bundled table
derived from the EXIOBASE classification (see ``data/sectors_pxp.json``).
"""

from __future__ import annotations

import json
from importlib.resources import files

import numpy as np
from pydantic import BaseModel, Field

from world4_core.impacts import available_impacts
from world4_core.mrio import MrioModel

_SECTORS: dict[str, dict[str, object]] = json.loads(
    (files("world4_core.data") / "sectors_pxp.json").read_text(encoding="utf-8")
)["sectors"]


def sector_metadata(sector: str) -> dict[str, object]:
    """Bundled metadata (code, number, consumption category) for a sector, or {}."""
    return _SECTORS.get(sector, {})


class SectorDriver(BaseModel):
    key: str
    label: str
    unit: str
    share: float = Field(
        ..., description="Fraction of the region's footprint driven by this sector."
    )


class SectorProfile(BaseModel):
    sector: str
    region: str
    code: str = ""
    category: str = ""
    drivers: list[SectorDriver] = Field(default_factory=list)
    labour_hours_in_region: float | None = Field(
        None, description="Production hours in the region tied to this sector's final demand."
    )


def sector_profile(model: MrioModel, sector: str, region: str) -> SectorProfile:
    """Compute a region-contextual profile for one sector (drivers + labour)."""
    if sector not in model.sectors:
        raise ValueError(f"unknown sector {sector!r}")
    if model.final_demand_by_region is None:
        raise ValueError("final_demand_by_region not loaded")
    if region not in model.regions:
        raise ValueError(f"unknown region {region!r}")

    region_idx = model.regions.index(region)
    pos = model.index.index((region, sector))
    demand_region = model.final_demand_by_region[:, region_idx]
    demand_p = float(demand_region[pos])

    drivers: list[SectorDriver] = []
    for impact in available_impacts(model):
        multiplier = model.multiplier(impact.extension)
        rows = list(impact.stressor_indices)
        contribution = float(np.nansum(multiplier[rows, pos])) * demand_p
        total = float(np.nansum(multiplier[rows] @ demand_region))
        share = contribution / total if total else 0.0
        drivers.append(
            SectorDriver(key=impact.key, label=impact.label, unit=impact.unit, share=share)
        )
    drivers.sort(key=lambda d: d.share, reverse=True)

    labour = None
    if model.production_hours_multiplier is not None:
        labour = float(model.production_hours_multiplier[region_idx, pos]) * demand_p

    meta = sector_metadata(sector)
    return SectorProfile(
        sector=sector,
        region=region,
        code=str(meta.get("code", "")),
        category=str(meta.get("category", "")),
        drivers=drivers,
        labour_hours_in_region=labour,
    )
