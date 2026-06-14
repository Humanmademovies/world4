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


def production_hours_multiplier(model: MrioModel, hours_unit: str = "M.hr") -> np.ndarray | None:
    """Build ``P`` (n_regions x n) mapping final demand to production hours per region.

    ``hours_by_region = P @ y`` (and ``Δhours = P @ Δy``). Derived from the direct
    employment-hours intensity ``h`` (the satellite rows whose unit is ``hours_unit``)
    and the Leontief inverse: ``P[r] = 1e6 · Σ_{p in r} h[p] · L[p, :]`` — i.e. the
    hours worked *in region r* to satisfy a unit of each product's final demand.
    Returns ``None`` if the model carries no hours account. The ``1e6`` converts
    EXIOBASE's ``M.hr`` (million hours) to hours.
    """
    if model.leontief is None:
        return None
    intensity: np.ndarray | None = None
    for ext in model.extensions.values():
        if ext.S is None:
            continue
        rows = [i for i, unit in enumerate(ext.units) if unit == hours_unit]
        if rows:
            intensity = ext.S[rows, :].sum(axis=0)  # (n,) hours-million per M.EUR
            break
    if intensity is None:
        return None

    region_index = {region: i for i, region in enumerate(model.regions)}
    scaled = np.zeros((len(model.regions), model.n), dtype=float)
    for product, (region, _) in enumerate(model.index):
        scaled[region_index[region], product] = intensity[product]
    return 1e6 * np.ascontiguousarray(scaled @ model.leontief)


def to_served_model(model: MrioModel) -> MrioModel:
    """Return a compact serve-ready copy: multipliers set, ``L`` and ``S`` dropped."""
    multipliers = precompute_multipliers(model)
    production_hours = production_hours_multiplier(model)
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
        production_hours_multiplier=production_hours,
        extensions=extensions,
        name=model.name,
    )
