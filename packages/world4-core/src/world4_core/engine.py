"""The Leontief propagation engine.

One precomputed Leontief inverse ``L`` serves every scenario: a scenario is just
the matrix-vector product ``S @ (L @ Δy)`` with ``Δy`` containing reductions only
(``<= 0``). That is the whole "precompute-then-serve" architecture.
"""

from __future__ import annotations

import numpy as np

from world4_core.model import ImpactTotal, Scenario, ScenarioResult
from world4_core.mrio import MrioModel


def leontief_inverse(technical_coefficients: np.ndarray) -> np.ndarray:
    """Return ``L = (I - A)^-1`` for a technical-coefficient matrix ``A``."""
    a = np.asarray(technical_coefficients, dtype=float)
    if a.ndim != 2 or a.shape[0] != a.shape[1]:
        raise ValueError(f"A must be square, got shape {a.shape}")
    identity = np.eye(a.shape[0])
    return np.linalg.inv(identity - a)


def build_delta_final_demand(model: MrioModel, scenario: Scenario) -> np.ndarray:
    """Build the ``Δy`` vector from a scenario's levers.

    Reductions accumulate per product and are clamped so the cumulative removed
    fraction never exceeds 1 (you cannot remove more than 100% of a demand).
    The result is ``<= 0`` everywhere, enforcing the seed's negative-only rule.
    """
    fraction = np.zeros(model.n, dtype=float)
    for lever in scenario.levers:
        positions = model.match_indices(sector=lever.sector, region=lever.region)
        fraction[positions] += lever.reduction
    np.clip(fraction, 0.0, 1.0, out=fraction)
    return -fraction * model.final_demand


def run_scenario(model: MrioModel, scenario: Scenario) -> ScenarioResult:
    """Propagate a scenario and return per-stressor deltas vs the baseline.

    Uses precomputed multipliers (``M @ Δy``) when available, otherwise derives
    them from ``L`` and ``S`` — both via :meth:`MrioModel.multiplier`.
    """
    delta_y = build_delta_final_demand(model, scenario)

    totals: list[ImpactTotal] = []
    for ext in model.extensions.values():
        multiplier = model.multiplier(ext.name)
        baseline_impact = multiplier @ model.final_demand
        delta_impact = multiplier @ delta_y
        for i, stressor in enumerate(ext.stressors):
            base = float(baseline_impact[i])
            delta = float(delta_impact[i])
            relative = delta / base if base != 0.0 else 0.0
            totals.append(
                ImpactTotal(
                    extension=ext.name,
                    stressor=stressor,
                    unit=ext.units[i],
                    baseline=base,
                    delta=delta,
                    relative=relative,
                )
            )
    return ScenarioResult(scenario=scenario.name, model=model.name, totals=totals)
