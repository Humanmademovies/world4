# Roadmap

Built **one brick at a time, with a binary success criterion**. No stacking: a
brick is "done" only when its check passes. This file is updated as bricks land.

## Phase A — the accounting seed

| # | Brick | Success criterion | Status |
| --- | --- | --- | --- |
| 0 | Scaffold + engine on the test MRIO | `uv run pytest` green; a reduction scenario yields Δimpacts ≤ 0 | ✅ done |
| 1 | Wire real EXIOBASE 3 | Reproduce a published figure (France footprint) within tolerance | ✅ done — see [validation.md](validation.md) |
| 2 | API + web dashboard (globe, sliders) | Move a slider → Δimpacts update on screen in real time | ✅ done — see [dashboard.md](dashboard.md) |
| 3 | Tunable sustainability targets (per limit, sourced) | Each planetary limit shown side by side vs its own target; no aggregate index | ⬜ next |
| 4 | Employment levers (hours → FTE, retirement age, target rate) | Human-hours freed and jobs computed and clearly distinguished | ⬜ |
| 5 | Anti-mathwashing parameters (e.g. advertising-driven demand) | Each contested assumption is an explicit slider with sourced range + uncertainty shown distinctly | ⬜ |

**Phase A exit:** the dashboard + globe deliverable from the spec, validated
against published footprints, with honest impact coverage.

## Phase B — beyond the seed (separate modules, never grafted on the accounting core)

These require an explicit go-ahead and live as their own objects (see
[epistemics](modeling/epistemics.md)):

- **Supply-side / sector-country closure** (Ghosh model, reallocation layer).
- **Growth & substitution hypotheses** — the seed is degrowth-only; exploring
  "fusion invented", "asteroid mining viable", "wind fleet grows" needs a model
  that can *add* capital and capacity. This is a new engine, not a sign flip.
- **Dynamic / System-Dynamics layer** (World3 / Limits-to-Growth lineage):
  year-by-year projection, stocks & flows, feedback loops.

## Phase C — the game

- Turn-based management loop over the Phase B engines: the player varies dozens to
  hundreds of parameters and watches the world evolve, from collapse to solarpunk.
- Calibrated against serious published projection scenarios.
- Likely a **Godot** client driving the same HTTP API (the headless-core boundary
  set in Phase A is what makes this a port, not a rewrite). See
  [decisions/0004](decisions/0004-fastapi-and-web-front.md).

## Working method

Each iteration: pick the next brick → find the missing data (cited) → implement →
prove the binary criterion → update docs + this roadmap + `CHANGELOG.md`.
