"""In-memory representation of a Multi-Regional Input-Output (MRIO) model.

This is the engine's *internal* data structure, deliberately decoupled from
``pymrio``: once a model is extracted (see :mod:`world4_core.data.loaders`) the
rest of the engine depends only on plain NumPy arrays and label metadata.

A model can be carried in two equivalent forms:

* **Full** — has the Leontief inverse ``leontief`` and extension intensities
  ``Extension.S``. This is what loaders build from pymrio.
* **Served** — has precomputed multipliers ``M = S @ L`` (one per extension) and
  no ``L`` / ``S``. This is the compact, fast-to-load form used by the API
  (see :mod:`world4_core.build` and :mod:`world4_core.serialize`).

The engine prefers multipliers when present and falls back to ``L`` otherwise, so
both forms behave identically.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

# A "product" is a (region, sector) pair — one column/row of the IO table.
Product = tuple[str, str]


@dataclass(frozen=True)
class Extension:
    """A satellite (environmental / social) account.

    ``S`` holds *direct intensities* (stressor per unit of sector output), shape
    ``(n_stressors, n_products)``. It is ``None`` in served models, which keep
    only the multipliers (in :attr:`MrioModel.multipliers`) plus labels.
    """

    name: str
    stressors: list[str]
    units: list[str]
    S: np.ndarray | None = None  # (n_stressors, n_products) or None in served models

    def __post_init__(self) -> None:
        if len(self.units) != len(self.stressors):
            raise ValueError(
                f"extension {self.name!r}: {len(self.units)} units "
                f"for {len(self.stressors)} stressors"
            )
        if self.S is not None and self.S.shape[0] != len(self.stressors):
            raise ValueError(
                f"extension {self.name!r}: S has {self.S.shape[0]} rows "
                f"but {len(self.stressors)} stressors"
            )


@dataclass(frozen=True)
class MrioModel:
    """A calculated MRIO ready for scenario propagation.

    Attributes:
        regions: ordered unique region codes.
        sectors: ordered unique sector codes.
        index: the ``(region, sector)`` of each product column, length ``n``.
        final_demand: baseline total final demand per product, length ``n``
            (summed over all *consuming* regions). Used by the scenario engine.
        leontief: the Leontief inverse ``L = (I - A)^-1``, shape ``(n, n)``; or
            ``None`` in a served model.
        final_demand_by_region: final demand split by *consuming* region, shape
            ``(n, n_regions)`` with columns aligned to ``regions``. Needed for
            consumption-based (footprint) accounting. ``None`` if not loaded.
        multipliers: precomputed ``M = S @ L`` per extension name (each shape
            ``(n_stressors, n)``); or ``None`` in a full model.
        production_hours_multiplier: ``P`` of shape ``(n_regions, n)`` mapping a
            final-demand vector to production hours worked *in each region*
            (``hours_by_region = P @ y``; ``Δhours = P @ Δy``). Rows align with
            ``regions``. ``None`` if the model has no employment-hours account.
        extensions: satellite accounts keyed by name.
        name: human-readable model identifier.
    """

    regions: list[str]
    sectors: list[str]
    index: list[Product]
    final_demand: np.ndarray
    leontief: np.ndarray | None = None
    final_demand_by_region: np.ndarray | None = None
    multipliers: dict[str, np.ndarray] | None = None
    production_hours_multiplier: np.ndarray | None = None
    extensions: dict[str, Extension] = field(default_factory=dict)
    name: str = "mrio"

    @property
    def n(self) -> int:
        """Number of products (region x sector)."""
        return len(self.index)

    def multiplier(self, extension: str) -> np.ndarray:
        """Return the multiplier matrix ``M = S @ L`` for an extension.

        Uses the precomputed multiplier if available, else derives it from ``L``
        and the extension's ``S``. Raises if neither is available.
        """
        if self.multipliers is not None and extension in self.multipliers:
            return self.multipliers[extension]
        ext = self.extensions[extension]
        if self.leontief is None or ext.S is None:
            raise ValueError(
                f"cannot derive multiplier for {extension!r}: need either a "
                f"precomputed multiplier or both leontief and Extension.S"
            )
        return ext.S @ self.leontief

    def consuming_demand(self, region: str) -> np.ndarray:
        """Final demand consumed by ``region``, as a vector over all products.

        This is the consumption-side slice of final demand (who *uses* the goods),
        as opposed to :attr:`final_demand` which is summed over consumers. Needed
        for consumption-based footprints.
        """
        if self.final_demand_by_region is None:
            raise ValueError("final_demand_by_region not loaded; cannot compute footprints")
        if region not in self.regions:
            raise ValueError(f"unknown region {region!r}; known: {self.regions}")
        return self.final_demand_by_region[:, self.regions.index(region)]

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
