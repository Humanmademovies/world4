"""Load MRIO data into the engine's internal representation.

Two entry points:

* :func:`load_test_model` — pymrio's tiny synthetic MRIO. No download, fast,
  deterministic. Everything in the engine is developed and unit-tested against
  this so CI never needs the multi-GB real dataset.
* :func:`load_exiobase_model` — a real, previously downloaded EXIOBASE 3 table
  (see :func:`world4_core.data.download.download_exiobase`).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import numpy as np
import pymrio

from world4_core.mrio import Extension, MrioModel


def _flatten_label(label: Any) -> str:
    """Render an index entry (possibly a MultiIndex tuple) as a readable string."""
    if isinstance(label, tuple):
        return " | ".join(str(part) for part in label)
    return str(label)


def _extract_units(extension: Any, stressor_index: Any) -> list[str]:
    """Best-effort per-stressor unit list, aligned to ``stressor_index``."""
    unit = getattr(extension, "unit", None)
    if unit is None:
        return [""] * len(stressor_index)
    aligned = unit.reindex(stressor_index)
    column = aligned.iloc[:, 0] if aligned.shape[1] else aligned
    return ["" if value is None else str(value) for value in column.tolist()]


def _from_iosystem(io: Any, name: str) -> MrioModel:
    """Extract NumPy matrices and labels from a (calculated) pymrio IOSystem.

    ``calc_all`` is idempotent; calling it guarantees ``A``, ``L`` and the
    extension intensity matrices ``S`` exist regardless of how ``io`` was built.
    """
    io.calc_all()

    product_index = io.A.index  # MultiIndex of (region, sector)
    leontief = io.L.reindex(index=product_index, columns=product_index).to_numpy(dtype=float)
    final_demand = io.Y.sum(axis=1).reindex(product_index).to_numpy(dtype=float)

    index = [(str(region), str(sector)) for region, sector in product_index]
    regions = list(dict.fromkeys(region for region, _ in index))
    sectors = list(dict.fromkeys(sector for _, sector in index))

    # Final demand split by *consuming* region (Y columns are (region, category)).
    by_region = io.Y.T.groupby(level=0).sum().T.reindex(index=product_index, columns=regions)
    final_demand_by_region = by_region.to_numpy(dtype=float)

    extensions: dict[str, Extension] = {}
    for ext_name in io.get_extensions(data=False):
        ext = getattr(io, ext_name)
        if getattr(ext, "S", None) is None:
            continue
        intensity = ext.S.reindex(columns=product_index)
        extensions[ext_name] = Extension(
            name=ext_name,
            stressors=[_flatten_label(label) for label in intensity.index],
            units=_extract_units(ext, intensity.index),
            S=intensity.to_numpy(dtype=float),
        )

    return MrioModel(
        regions=regions,
        sectors=sectors,
        index=index,
        leontief=np.ascontiguousarray(leontief),
        final_demand=np.ascontiguousarray(final_demand),
        final_demand_by_region=np.ascontiguousarray(final_demand_by_region),
        extensions=extensions,
        name=name,
    )


def load_test_model() -> MrioModel:
    """Load pymrio's small synthetic MRIO. No network, no large files."""
    return _from_iosystem(pymrio.load_test(), name="test-mrio")


def load_exiobase_model(path: str | Path, name: str | None = None) -> MrioModel:
    """Parse a downloaded EXIOBASE 3 table (zip or extracted folder).

    Memory note: a full EXIOBASE Leontief inverse is ~9800x9800 (hundreds of MB
    dense). This is the deliberate "precompute once" cost of the seed.
    """
    path = Path(path)
    io = pymrio.parse_exiobase3(path=str(path))
    return _from_iosystem(io, name=name or f"exiobase3:{path.name}")
