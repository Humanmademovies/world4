"""Download EXIOBASE 3 from its public archive (Zenodo) via pymrio.

Kept separate from loading on purpose: downloads are large and slow, must never
run in CI, and the resulting data is **never committed** (see the repo
``.gitignore`` and ``docs/data/exiobase.md`` for the data licence).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pymrio

# Default target directory for cached datasets (gitignored at the repo root).
DEFAULT_STORAGE = Path("data/exiobase3")


def download_exiobase(
    storage_folder: str | Path = DEFAULT_STORAGE,
    years: list[int] | None = None,
    system: str = "pxp",
) -> Any:
    """Download EXIOBASE 3 into ``storage_folder``.

    Args:
        storage_folder: where to cache the dataset (created if missing).
        years: list of years to fetch; ``None`` lets pymrio pick the default.
        system: ``"pxp"`` (product-by-product) or ``"ixi"`` (industry-by-industry).

    Returns:
        The pymrio metadata object describing what was downloaded.
    """
    folder = Path(storage_folder)
    folder.mkdir(parents=True, exist_ok=True)
    return pymrio.download_exiobase3(
        storage_folder=str(folder),
        years=years,
        system=system,
    )
