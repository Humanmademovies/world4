"""Save / load a served model artifact (``.npz``).

The artifact stores numeric arrays plus a JSON metadata blob, all inside a single
NumPy ``.npz``. It is loaded with ``allow_pickle=False`` — **no pickle**, so
loading an artifact can never execute code (a deliberate security choice for a
file that may be distributed alongside the app).
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np

from world4_core.mrio import Extension, MrioModel

FORMAT_VERSION = 1


def save_model(model: MrioModel, path: str | Path) -> Path:
    """Serialise a *served* model (one with multipliers) to ``path`` (.npz)."""
    if model.multipliers is None:
        raise ValueError("save_model expects a served model; run build.to_served_model first")

    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)

    arrays: dict[str, np.ndarray] = {"final_demand": np.asarray(model.final_demand, dtype=float)}
    if model.final_demand_by_region is not None:
        arrays["final_demand_by_region"] = np.asarray(model.final_demand_by_region, dtype=float)

    ext_meta: list[dict[str, Any]] = []
    for i, (name, ext) in enumerate(model.extensions.items()):
        arrays[f"mult_{i}"] = np.asarray(model.multipliers[name], dtype=float)
        ext_meta.append({"name": name, "stressors": ext.stressors, "units": ext.units})

    meta = {
        "format_version": FORMAT_VERSION,
        "name": model.name,
        "regions": model.regions,
        "sectors": model.sectors,
        "index": [list(product) for product in model.index],
        "extensions": ext_meta,
        "has_final_demand_by_region": model.final_demand_by_region is not None,
    }
    arrays["__meta__"] = np.asarray(json.dumps(meta))

    with out.open("wb") as handle:
        np.savez(handle, **arrays)  # type: ignore[arg-type]  # numpy stub quirk with **kwargs
    return out


def load_model(path: str | Path) -> MrioModel:
    """Load a served model artifact written by :func:`save_model`."""
    with np.load(Path(path), allow_pickle=False) as data:
        meta = json.loads(str(data["__meta__"]))
        if meta.get("format_version") != FORMAT_VERSION:
            raise ValueError(f"unsupported artifact format_version {meta.get('format_version')}")

        multipliers: dict[str, np.ndarray] = {}
        extensions: dict[str, Extension] = {}
        for i, ext_meta in enumerate(meta["extensions"]):
            name = ext_meta["name"]
            multipliers[name] = np.ascontiguousarray(data[f"mult_{i}"])
            extensions[name] = Extension(
                name=name, stressors=ext_meta["stressors"], units=ext_meta["units"], S=None
            )

        final_demand = np.ascontiguousarray(data["final_demand"])
        fdbr = (
            np.ascontiguousarray(data["final_demand_by_region"])
            if meta["has_final_demand_by_region"]
            else None
        )

    return MrioModel(
        regions=list(meta["regions"]),
        sectors=list(meta["sectors"]),
        index=[(str(r), str(s)) for r, s in meta["index"]],
        final_demand=final_demand,
        leontief=None,
        final_demand_by_region=fdbr,
        multipliers=multipliers,
        extensions=extensions,
        name=meta["name"],
    )
