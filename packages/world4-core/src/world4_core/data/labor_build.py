"""Build the compact labour-inputs artifact from EXIOBASE + UN WPP.

* production hours per region: EXIOBASE employment account (direct hours worked
  for production), summed over each region's industries — available for all 49
  regions (the 5 Rest-of-World aggregates included).
* population by single age: UN WPP, matched by ISO-2 code — available for the 44
  named countries. RoW aggregates get ``population_by_age = None`` (no single
  demography), which the work-time view surfaces honestly rather than faking.

Heavy and one-off (like ``build-model``); never run in CI.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pymrio

from world4_core.labor import AGES, LaborInputs, RegionLabor

# EXIOBASE Rest-of-World aggregate codes. These are NOT countries — and some
# collide with real ISO-2 codes (e.g. "WF" = Wallis & Futuna), so we must never
# attach a single country's demography to them.
ROW_REGIONS = frozenset({"WA", "WL", "WE", "WF", "WM"})


def _production_hours_by_region(exiobase_path: str | Path) -> dict[str, float]:
    """Total production hours worked per region (EXIOBASE employment, hours rows)."""
    io = pymrio.parse_exiobase3(path=str(exiobase_path))
    flows = io.employment.F  # stressors x (region, sector)
    hour_rows = [s for s in flows.index if "hour" in str(s).lower()]
    # EXIOBASE employment hours are in millions of hours (M.hr) -> convert to hours.
    by_region = flows.loc[hour_rows].sum(axis=0).groupby(level=0).sum() * 1e6
    return {str(region): float(value) for region, value in by_region.items()}


def _population_by_age(wpp_path: str | Path, year: int) -> dict[str, list[float]]:
    """Population by single age (persons) per ISO-2 country, for ``year``, from WPP."""
    dtypes = {
        "ISO2_code": "object",
        "Time": "int32",
        "AgeGrpStart": "int16",
        "PopTotal": "float64",
        "LocTypeName": "object",
    }
    rows: list[pd.DataFrame] = []
    for chunk in pd.read_csv(
        wpp_path,
        compression="gzip",
        usecols=list(dtypes),
        dtype=dtypes,
        chunksize=400_000,
        encoding="utf-8-sig",
    ):
        chunk = chunk[(chunk["Time"] == year) & (chunk["LocTypeName"] == "Country/Area")]
        if len(chunk):
            rows.append(chunk[["ISO2_code", "AgeGrpStart", "PopTotal"]])
    table = pd.concat(rows, ignore_index=True)

    by_country: dict[str, list[float]] = {}
    for iso, group in table.groupby("ISO2_code"):
        if not isinstance(iso, str):
            continue
        ages = [0.0] * AGES
        for age, pop_thousands in zip(group["AgeGrpStart"], group["PopTotal"], strict=False):
            index = int(age)
            if 0 <= index < AGES:
                ages[index] += float(pop_thousands) * 1000.0
        by_country[iso] = ages
    return by_country


def build_labor_inputs(
    exiobase_path: str | Path, wpp_path: str | Path, year: int = 2022
) -> LaborInputs:
    """Assemble per-region labour inputs (production hours + demography)."""
    production = _production_hours_by_region(exiobase_path)
    demography = _population_by_age(wpp_path, year)

    regions: dict[str, RegionLabor] = {}
    for region, hours in production.items():
        pop = None if region in ROW_REGIONS else demography.get(region)
        regions[region] = RegionLabor(production_hours=hours, population_by_age=pop)
    return LaborInputs(year=year, regions=regions)
