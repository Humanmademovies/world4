"""Computed sector profiles for the wiki (on the synthetic test MRIO)."""

from __future__ import annotations

import math

import pytest

from world4_core.data import load_test_model
from world4_core.wiki import sector_profile


def test_sector_profile_has_ranked_finite_drivers() -> None:
    model = load_test_model()
    region = model.regions[0]
    profile = sector_profile(model, model.sectors[0], region)
    assert profile.region == region
    assert profile.drivers, "expected at least one impact driver"
    shares = [d.share for d in profile.drivers]
    assert all(math.isfinite(s) for s in shares)
    assert shares == sorted(shares, reverse=True)  # ranked by share desc


def test_sector_profile_unknown_sector_raises() -> None:
    model = load_test_model()
    with pytest.raises(ValueError, match="unknown sector"):
        sector_profile(model, "not-a-sector", model.regions[0])
