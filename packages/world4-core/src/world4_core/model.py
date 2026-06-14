"""Serialisable contract between the engine and any client.

These Pydantic models are the *public language* of World4: a client sends a
:class:`Scenario`, the engine returns a :class:`ScenarioResult`. They are pure
data (no NumPy, no pymrio) so they round-trip cleanly to JSON and are stable
across the Python dashboard and a future Godot client.

Seed invariant: levers express **reductions only**. ``reduction`` is bounded to
``[0, 1]`` at the type level; the engine never adds positive final demand.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class Lever(BaseModel):
    """A demand-side reduction of one sector's final use.

    Reduces the baseline final demand of every matching product by ``reduction``
    (a fraction). With ``region=None`` the lever applies in every region.
    """

    sector: str = Field(..., description="Sector code to reduce (must exist in the model).")
    region: str | None = Field(
        None, description="Restrict to one region; None applies to all regions."
    )
    reduction: float = Field(
        ..., ge=0.0, le=1.0, description="Fraction of baseline final demand to remove (0..1)."
    )


class Scenario(BaseModel):
    """A set of demand-side reductions to propagate through the supply chain."""

    name: str = "scenario"
    levers: list[Lever] = Field(default_factory=list)


class ImpactTotal(BaseModel):
    """Change in one stressor relative to the baseline, with its own metric.

    Per the anti-mathwashing rule there is **no single aggregate index**: each
    stressor is reported side by side with its own unit.
    """

    extension: str
    stressor: str
    unit: str
    baseline: float = Field(..., description="Baseline (footprint) level for this stressor.")
    delta: float = Field(..., description="Change vs baseline; <= 0 in the degrowth seed.")
    relative: float = Field(..., description="delta / baseline (0 when baseline is 0).")


class ScenarioResult(BaseModel):
    """The propagated physical/social consequences of a scenario."""

    scenario: str
    model: str
    totals: list[ImpactTotal] = Field(default_factory=list)
