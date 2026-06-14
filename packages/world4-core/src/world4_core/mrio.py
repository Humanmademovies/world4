"""In-memory representation of a Multi-Regional Input-Output (MRIO) model.

This is the engine's *internal* data structure, deliberately decoupled from
``pymrio``: once a model is extracted (see :mod:`world4_core.data.loaders`) the
rest of the engine depends only on plain NumPy arrays and label metadata. That
keeps the core testable with a tiny synthetic MRIO and serialisable for future
clients (web dashboard today, Godot tomorrow).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

# A "product" is a (region, sector) pair — one column/row of the IO table.
Product = tuple[str, str]


@dataclass(frozen=True)
class Extension:
    """A satellite (environmental / social) account.

    ``S`` holds *direct intensities*: stressor emitted/used per unit of sector
    output. Shape is ``(n_stressors, n_products)``.
    """

    name: str
    stressors: list[str]
    units: list[str]
    S: np.ndarray  # (n_stressors, n_products)

    def __post_init__(self) -> None:
        if self.S.shape[0] != len(self.stressors):
            raise ValueError(
                f"extension {self.name!r}: S has {self.S.shape[0]} rows "
                f"but {len(self.stressors)} stressors"
            )
        if len(self.units) != len(self.stressors):
            raise ValueError(
                f"extension {self.name!r}: {len(self.units)} units "
                f"for {len(self.stressors)} stressors"
            )


@dataclass(frozen=True)
class MrioModel:
    """A calculated MRIO ready for scenario propagation.

    Attributes:
        regions: ordered unique region codes.
        sectors: ordered unique sector codes.
        index: the ``(region, sector)`` of each product column, length ``n``.
        leontief: the Leontief inverse ``L = (I - A)^-1``, shape ``(n, n)``.
        final_demand: baseline total final demand per product, length ``n``.
        extensions: satellite accounts keyed by name.
        name: human-readable model identifier.
    """

    regions: list[str]
    sectors: list[str]
    index: list[Product]
    leontief: np.ndarray
    final_demand: np.ndarray
    extensions: dict[str, Extension] = field(default_factory=dict)
    name: str = "mrio"

    @property
    def n(self) -> int:
        """Number of products (region x sector)."""
        return len(self.index)

    def match_indices(self, sector: str, region: str | None = None) -> np.ndarray:
        """Return the integer positions matching a sector (and optional region).

        Raises ``ValueError`` on an unknown sector/region rather than silently
        matching nothing — a silent no-op would be a form of mathwashing.
        """
        if sector not in self.sectors:
            raise ValueError(f"unknown sector {sector!r}; known: {self.sectors}")
        if region is not None and region not in self.regions:
            raise ValueError(f"unknown region {region!r}; known: {self.regions}")
        positions = [
            i
            for i, (reg, sec) in enumerate(self.index)
            if sec == sector and (region is None or reg == region)
        ]
        return np.asarray(positions, dtype=np.intp)
