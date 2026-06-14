"""Precompute the compact, serve-ready form of a model.

The full model (from pymrio) carries the Leontief inverse ``L`` and per-extension
intensities ``S``. For serving we only ever need the multipliers ``M = S @ L``
(plus the demand vectors and labels), which are far smaller than ``L`` and make
scenario evaluation a single ``M @ Δy``. This module does that one-off transform.
"""

from __future__ import annotations

import numpy as np

from world4_core.mrio import Extension, MrioModel


def precompute_multipliers(model: MrioModel) -> dict[str, np.ndarray]:
    """Compute ``M = S @ L`` for every extension. Requires a full model."""
    if model.leontief is None:
        raise ValueError("model has no Leontief inverse; cannot precompute multipliers")
    result: dict[str, np.ndarray] = {}
    for name, ext in model.extensions.items():
        if ext.S is None:
            raise ValueError(f"extension {name!r} has no S; cannot precompute multipliers")
        result[name] = np.ascontiguousarray(ext.S @ model.leontief)
    return result


def to_served_model(model: MrioModel) -> MrioModel:
    """Return a compact serve-ready copy: multipliers set, ``L`` and ``S`` dropped."""
    multipliers = precompute_multipliers(model)
    extensions = {
        name: Extension(name=name, stressors=ext.stressors, units=ext.units, S=None)
        for name, ext in model.extensions.items()
    }
    return MrioModel(
        regions=model.regions,
        sectors=model.sectors,
        index=model.index,
        final_demand=model.final_demand,
        leontief=None,
        final_demand_by_region=model.final_demand_by_region,
        multipliers=multipliers,
        extensions=extensions,
        name=model.name,
    )
