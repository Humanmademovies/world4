"""Sustainability-target assessment (pure)."""

from __future__ import annotations

import pytest

from world4_core.targets import assess, available_targets, get_target


def test_registry_has_clean_matches_only() -> None:
    keys = {t.impact_key for t in available_targets()}
    assert {"co2_combustion", "water_blue", "material"} <= keys
    # Land and energy intentionally have no per-capita boundary.
    assert get_target("land_use") is None
    assert get_target("energy") is None


def test_assess_at_boundary_gives_ratio_one() -> None:
    target = get_target("co2_combustion")
    assert target is not None
    population = 1_000_000.0
    # native kg chosen so per-capita == 1.61 tCO2 (the 2C boundary): 1.61 t * 1e3 kg/t * pop.
    footprint_kg = 1.61 * 1e3 * population
    result = assess(target, "2C", footprint_kg, population)
    assert result.per_capita_footprint == pytest.approx(1.61)
    assert result.overshoot_ratio == pytest.approx(1.0)
    assert result.overshoot_day == pytest.approx(365.0)


def test_assess_overshoot() -> None:
    target = get_target("water_blue")
    assert target is not None
    population = 2_000_000.0
    # per-capita = 1148 m3 == 2x the 574 boundary -> ratio 2, overshoot day ~182.5.
    footprint_mm3 = (1148.0 * population) / 1e6
    result = assess(target, "planetary-boundary", footprint_mm3, population)
    assert result.overshoot_ratio == pytest.approx(2.0)
    assert result.overshoot_day == pytest.approx(182.5)


def test_assess_unknown_preset_and_bad_population() -> None:
    target = get_target("material")
    assert target is not None
    with pytest.raises(ValueError, match="unknown preset"):
        assess(target, "nope", 1.0, 1.0)
    with pytest.raises(ValueError, match="population"):
        assess(target, "oneill", 1.0, 0.0)
