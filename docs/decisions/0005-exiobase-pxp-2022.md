# ADR 0005 — EXIOBASE 3, 2022, product-by-product (pxp) as the reference dataset

- **Status:** accepted
- **Date:** 2026-06-14

## Context

EXIOBASE 3 ships two symmetric table types — **pxp** (product × product, ~200
products) and **ixi** (industry × industry, ~163 industries) — across many years.
We need one reference dataset to validate the seed (brick 1).

## Decision

Use **EXIOBASE 3, year 2022, pxp** as the reference for the accounting seed:

- **pxp**, because consumption footprints (and the published per-capita figures we
  validate against) are naturally expressed in *products*, and final demand is a
  product vector. This is the conventional choice for footprint accounting.
- **2022**, the most recent year in the current release.

The engine's `MrioModel` is **system-agnostic** (it does not care whether sectors
are products or industries), so adding **ixi** later is free where it matters:
employment levers and industry-level policy targeting (brick 4), since jobs and
"throttle this industry" are industry concepts. The game phase will likely lean on
ixi for industry-based decisions.

## Consequences

- Validation (brick 1) uses 49 regions × 200 products; France = `FR`.
- A second `ixi` download is deferred until employment/industry targeting needs it.
- Dataset is ~224 MB compressed, never committed (see
  [docs/data/exiobase.md](../data/exiobase.md)).
