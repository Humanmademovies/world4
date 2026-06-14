"""Cited reference values for binary validation.

Every entry MUST carry a verifiable ``source``. The list starts empty on
purpose: invented or unsourced numbers are forbidden (see the "citations
required" convention). The EXIOBASE brick fills it with cited figures.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceValue:
    """A published figure the engine must be able to reproduce.

    Attributes:
        label: human-readable description (e.g. "France per-capita CO2 footprint").
        region: region code the value pertains to.
        stressor: stressor label as exposed by the model's extensions.
        value: the published quantity.
        unit: its unit.
        tolerance: allowed *relative* deviation (e.g. 0.10 for +/-10%).
        source: citation (author, year, title / DOI / URL). Required.
    """

    label: str
    region: str
    stressor: str
    value: float
    unit: str
    tolerance: float
    source: str


def within_tolerance(computed: float, reference: ReferenceValue) -> bool:
    """Whether ``computed`` matches ``reference`` within its relative tolerance."""
    if reference.value == 0.0:
        return computed == 0.0
    return abs(computed - reference.value) / abs(reference.value) <= reference.tolerance


# Filled at the EXIOBASE brick with cited values. Intentionally empty for now.
REFERENCES: list[ReferenceValue] = []
