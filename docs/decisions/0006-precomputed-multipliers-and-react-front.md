# ADR 0006 — Precomputed multipliers artifact + React/MapLibre dashboard

- **Status:** accepted
- **Date:** 2026-06-14

## Context

Brick 2 needs an interactive dashboard over **real** EXIOBASE data. But parsing
EXIOBASE and inverting the 9 800 × 9 800 system takes ~2.7 min and ~GB of RAM —
unacceptable as an API startup cost. Front-end stack chosen: React + TS + Vite;
map: MapLibre (2D + globe); served by FastAPI in prod (single origin).

## Decision

**1. Precomputed multipliers artifact.** A build step computes, once, the
multiplier matrices `M_ext = S_ext · L` per extension and serialises them with the
demand vectors and labels into a compact artifact (`data/models/*.w4m.npz`,
gitignored). At serve time the API loads the artifact in seconds and never touches
`L`:

- global scenario impact: `Δimpact = M · Δy`
- per-region baseline footprint: `footprint(r) = M · y_region`

`MrioModel` gains optional `multipliers` and makes `leontief` / `Extension.S`
optional, so one model type serves both the full (L-based) and served (M-based)
paths. `world4 build-model` produces the artifact.

**2. Model selection by config.** The API loads `WORLD4_MODEL_PATH` if set, else
falls back to the synthetic test model — so CI and a fresh clone work offline,
while a local machine with the artifact gets the real dashboard.

**3. React + MapLibre front**, dev via Vite (proxy to the API), prod served as
static files by FastAPI.

## Consequences

- Artifact is ~100–150 MB (M matrices, float64), local only, never committed.
- Serve-time memory and latency drop dramatically; slider moves are `M · Δy`.
- Two code paths (M vs L) in engine/footprint, guarded and tested.
- Map colours regions by **baseline consumption footprint**; scenario panels show
  **global Δimpacts** (attributing Δ to consuming regions is deferred — honest).
- No single aggregate index; each impact keeps its own unit and coverage flag.
