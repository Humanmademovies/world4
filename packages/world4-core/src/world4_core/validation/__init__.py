"""Binary validation against published figures.

The seed rule: before advancing a milestone, reproduce a *published* number
(e.g. France's per-capita carbon/water footprint). This package holds the
comparison machinery; the cited reference values are added at the EXIOBASE
brick — never invented.
"""

from world4_core.validation.reference import ReferenceValue, within_tolerance

__all__ = ["ReferenceValue", "within_tolerance"]
