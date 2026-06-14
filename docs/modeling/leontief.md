# The Leontief engine

## Notation

For an MRIO with `n = regions × sectors` products:

- `Z` — inter-industry flows (`n × n`).
- `x` — total output per product (`n`).
- `A = Z x̂⁻¹` — technical coefficients: input of `i` per unit output of `j`.
- `y` — final demand per product (`n`).
- `L = (I − A)⁻¹` — the **Leontief inverse** (total requirements matrix).
- `S` — direct intensity of a stressor per unit output (`stressors × n`), one
  matrix per satellite account (carbon, water, materials, land, employment hours…).

The accounting identity: `x = A x + y = L y`.

## Propagation

A scenario perturbs **final demand** with reductions only:

```
Δy ≤ 0                       # built from the levers; clamped so |Δy| ≤ y
Δx = L @ Δy                  # change in total output, propagated upstream worldwide
Δimpact = S @ Δx             # change per stressor, in its own physical unit
```

The baseline is `x = L @ y` and `impact = S @ x`; we report `Δimpact`, `impact`
(baseline) and `relative = Δimpact / impact` per stressor.

## Why "precompute then serve"

`L` is computed **once** per model (an `O(n³)` inverse). Afterwards every slider
move is a single `O(n²)` matrix-vector product — fast enough for an interactive
dashboard. This is the entire performance story of the seed.

## Invariants the engine guarantees

- **Reductions only.** `reduction ∈ [0, 1]` at the type level; overlapping levers
  on the same product clamp cumulatively to 1. `Δy ≤ 0` always, so `Δimpact ≤ 0`
  for non-negative `S`. There is no path that adds positive demand.
- **No reinjection.** Freed output is not redirected anywhere — consistent with
  the physical, no-reinjected-income framing.

## Scope boundaries (from the framing)

- **Demand-driven only.** We push `Δy` and read effects through `L`. The Ghosh
  supply-side model and direct sector-country closure are *not* part of this engine
  — see [epistemics](epistemics.md) and the roadmap's Phase B.
- **Constant apparatus.** `A` and `S` are fixed (current physical capital); the
  seed never changes technology coefficients.

## Implementation

See [`engine.py`](../../packages/world4-core/src/world4_core/engine.py):
`leontief_inverse`, `build_delta_final_demand`, `run_scenario`. Data extraction
from pymrio into the engine's `MrioModel` is in
[`data/loaders.py`](../../packages/world4-core/src/world4_core/data/loaders.py).
