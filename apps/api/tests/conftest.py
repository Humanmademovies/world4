"""Test isolation: force the synthetic test model and no labour data by default.

The API now defaults to the local EXIOBASE/labour artifacts when present. Tests must
not depend on whether those artifacts exist on the machine, so this autouse fixture
points the env vars at non-existent paths (→ test model, no labour) and clears the
cached loaders before/after each test. Individual tests may override the env vars.
"""

from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import pytest

from world4_api.app import get_labor, get_model


@pytest.fixture(autouse=True)
def _isolate_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    monkeypatch.setenv("WORLD4_MODEL_PATH", str(tmp_path / "no-model.npz"))
    monkeypatch.setenv("WORLD4_LABOR_PATH", str(tmp_path / "no-labor.json"))
    get_model.cache_clear()
    get_labor.cache_clear()
    yield
    get_model.cache_clear()
    get_labor.cache_clear()
