"""Brick-1 binary validation against real EXIOBASE 3 (2022, pxp).

Two layers:

1. **Engine correctness (hard gate):** our consumption_footprint reproduces
   pymrio's own consumption-based account (``D_cba``) to machine precision. This
   is the "reproduce a documented method" check — pymrio + EXIOBASE is the
   reference implementation.
2. **External published cross-check (plausibility band):** France's per-capita
   consumption-based fossil-CO2 footprint lands in a band anchored on the French
   ministry (SDES) figure. EXIOBASE and SDES use *different* models, so we assert
   a sourced band, not an exact match (honest about methodology variance).

Skipped automatically when the dataset is absent (so CI stays fast and offline).
"""

from __future__ import annotations

import math
from pathlib import Path

import pymrio
import pytest

from world4_core.data.loaders import _from_iosystem
from world4_core.footprint import consumption_footprint, per_capita

pytestmark = pytest.mark.exiobase

EXIOBASE_ZIP = Path("data/exiobase3/IOT_2022_pxp.zip")

# --- Sourced reference values (citations required) ---------------------------
# France population 2022: ~67.97 M (World Bank, "Population, total - France").
FR_POPULATION_2022 = 67_970_000
# SDES (Service des données et études statistiques), "L'empreinte carbone de la
# France de 1995 à 2022": 9.2 tCO2eq/cap in 2022, of which ~78% is CO2 -> ~7.2
# tCO2/cap. EXIOBASE (a different MRIO model) is expected in the same band, not
# identical; hence a deliberately wide plausibility band.
FR_FOSSIL_CO2_TCAP_BAND = (4.0, 10.0)


@pytest.fixture(scope="module")
def exiobase_system() -> pymrio.IOSystem:
    if not EXIOBASE_ZIP.exists():
        pytest.skip(f"EXIOBASE not downloaded at {EXIOBASE_ZIP}")
    system = pymrio.parse_exiobase3(path=str(EXIOBASE_ZIP))
    system.calc_all()
    return system


def test_engine_matches_pymrio_consumption_account(exiobase_system: pymrio.IOSystem) -> None:
    model = _from_iosystem(exiobase_system, "exiobase3:IOT_2022_pxp")
    footprint = consumption_footprint(model, "FR")
    stressor = "CO2 - combustion - air"
    entry = footprint.get("air_emissions", stressor)
    assert entry is not None
    reference = float(exiobase_system.air_emissions.D_cba.loc[stressor, "FR"].sum())
    assert entry.value == pytest.approx(reference, rel=1e-6)


def test_france_fossil_co2_footprint_in_published_band(
    exiobase_system: pymrio.IOSystem,
) -> None:
    model = _from_iosystem(exiobase_system, "exiobase3:IOT_2022_pxp")
    footprint = consumption_footprint(model, "FR")
    # Fossil CO2 = CO2 air stressors excluding biogenic; skip NaN stressors
    # (EXIOBASE coverage is honestly uneven — we do not fabricate missing data).
    fossil_co2_kg = sum(
        e.value
        for e in footprint.entries
        if e.extension == "air_emissions"
        and "CO2" in e.stressor
        and "bio" not in e.stressor.lower()
        and math.isfinite(e.value)
    )
    tonnes_per_capita = per_capita(fossil_co2_kg, FR_POPULATION_2022) / 1000.0
    low, high = FR_FOSSIL_CO2_TCAP_BAND
    assert low <= tonnes_per_capita <= high, (
        f"{tonnes_per_capita:.2f} tCO2/cap outside {low}-{high}"
    )
