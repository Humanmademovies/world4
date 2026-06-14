# CLAUDE.md

Guidance for Claude Code (and any AI agent) working in this repository.

## What this is

World4 is a **physical accounting model of world consumption** (the "seed"),
designed to grow — one brick at a time — into a **turn-based simulation game**
(likely a Godot client later) showing worlds from collapse to solarpunk utopia.
The seed: a planner sets demand-reduction sliders and sees physical (carbon,
water, energy, materials, land) and social (hours, jobs) effects propagate through
the global supply chain via the Leontief inverse, vs tunable sustainability targets.

The authoritative spec is `instructions_projet.md` (French). Everything else in
the repo is in English.

## ⚠️ Epistemic guardrails — read `docs/modeling/epistemics.md` before changing modelling code

Non-negotiable. Violating these is the main way to break this project:

- **Physical, not behavioural.** No prices, elasticities, market equilibrium, or
  behaviour prediction. Capital is frozen in its current physical state.
- **Degrowth at constant apparatus.** The seed only ever does *less*. **No positive
  `Δdemand`, ever.** No green substitution, no new capital. Growth/substitution
  hypotheses (fusion, asteroid mining, wind expansion) are a *separate Phase B
  engine*, never a sign flip on the seed.
- **Levers = demand; engine = Leontief.** Propagate reductions upstream with `L`.
  Ghosh (supply side) and sector-country closure are **out of the seed**.
- **No reinjection.** Cutting a sector finances nothing elsewhere.
- **No single aggregate index.** Each limit/stressor is shown with its own metric.
- **Anti-mathwashing.** Any contested assumption is an explicit, **sourced** slider
  with an uncertainty range — never a hidden constant. See
  `docs/modeling/parameters.md`.
- **Honest coverage.** Carbon/water/materials/land map well; biodiversity, novel
  entities, N/P flows are lacunar — show real coverage, never fake uniformity.
- **Binary validation.** Reproduce a *published* figure before advancing a brick.
  **Never invent a number; cite every value.**

The dynamic/ludic layer (year-by-year projection, collapse conditions) is a
*separate* System-Dynamics (World3-lineage) model bolted onto the seed — never an
extension of the accounting core.

## Architecture (see `docs/architecture.md`)

Headless core + thin clients. Simulation logic lives only in `world4-core` (pure
Python, no UI/web deps). Clients talk to it via a serialisable Pydantic contract.

```
packages/world4-core/src/world4_core/
  model.py      Scenario / Lever / ScenarioResult  (the JSON contract)
  mrio.py       MrioModel: NumPy matrices + labels, decoupled from pymrio
  engine.py     leontief_inverse, build_delta_final_demand, run_scenario
  data/         loaders (pymrio -> MrioModel), EXIOBASE download
  validation/   binary checks vs cited published figures
apps/api/       FastAPI over the core
apps/web/       browser dashboard (brick 2 — placeholder)
data/           EXIOBASE cache — gitignored, NEVER commit
```

Engine maths: `Δx = L @ Δy` (Δy ≤ 0), `Δimpact = S @ Δx`. Precompute `L` once,
serve scenarios as cheap matrix-vector products.

## Commands

Use **`uv`** for all Python — never base conda.

```bash
uv sync                         # install workspace + dev deps (fetches Python 3.12)
uv run pytest                   # tests (engine + test-MRIO integration + API)
uv run ruff check .             # lint
uv run ruff format .            # format
uv run mypy -p world4_core -p world4_api          # strict type check
uv run bandit -r packages/world4-core/src apps/api/src   # security static analysis
uv run world4 info|demo         # engine CLI on the test MRIO
uv run world4-api               # FastAPI dev server
```

Real-EXIOBASE tests are marked `@pytest.mark.exiobase` and skipped unless data is
present. The big download must never run in CI; see `docs/data/exiobase.md`.

## Conventions

- **One brick at a time, binary success criterion.** No stacking. The brick list
  and its statuses live in `docs/roadmap.md` — update it when a brick lands.
- **English everywhere** (code, identifiers, commits, docs). ADR 0002.
- **Citations required** before asserting any "documented method"; verify a
  library/UI capability exists before claiming it (firm pushback on unverified
  claims is expected).
- **Code-first, concise.** Give a file's full content when placement is ambiguous.
- **Keep docs in lockstep with code.** A change that alters behaviour updates the
  relevant `docs/` page, `CHANGELOG.md`, and the roadmap in the same commit.
- **Never commit data or secrets.** `data/`, `.env*` are gitignored.
- **Security defaults stay secure** (e.g. CORS off unless `WORLD4_CORS_ORIGINS`
  is set). See `SECURITY.md`.

## Adding a feature / brick

1. Confirm it belongs to the **seed** (not a deferred Phase B/C layer — re-read the
   guardrails).
2. Find the data; record its **source**. New parameters go through
   `docs/modeling/parameters.md` as explicit sliders with ranges.
3. Implement in `world4-core` first (engine stays UI-agnostic). Expose via the
   Pydantic contract, then the API, then the web client — in that order.
4. Add tests with a binary criterion (unit on synthetic MRIO; mark real-data tests
   `exiobase`).
5. Update `docs/`, `CHANGELOG.md`, and `docs/roadmap.md`.

## Key references

`O'Neill et al. 2018` (good life within planetary boundaries), Raworth (Doughnut),
Hot or Cool (1.5° lifestyles), Richardson et al. 2023 (planetary boundaries),
EXIOBASE 3 + pymrio docs. Full list in `instructions_projet.md`.
