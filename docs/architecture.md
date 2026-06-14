# Architecture

## Principle: a headless core with thin clients

```
                 Scenario (JSON)                ScenarioResult (JSON)
   client  ───────────────────────▶   engine   ───────────────────────▶  client
 (web / Godot / CLI)                (world4-core)
```

The simulation logic lives in **one place** — `world4-core`, pure Python, with no
UI or web dependency. Everything else is a client that speaks the same
serialisable contract ([`world4_core.model`](../packages/world4-core/src/world4_core/model.py)).
That is what makes the seed → game trajectory possible: today a FastAPI service and
a web dashboard, tomorrow a Godot client, all driving the identical engine.

## Repository layout (uv workspace / monorepo)

```
world4/
├── packages/
│   └── world4-core/         # the engine — pure Python, no UI/web deps
│       └── src/world4_core/
│           ├── model.py     # Scenario / Lever / ScenarioResult (Pydantic contract)
│           ├── mrio.py      # MrioModel: NumPy matrices + labels, decoupled from pymrio
│           ├── engine.py    # leontief_inverse, build_delta_final_demand, run_scenario
│           ├── data/        # loaders (pymrio -> MrioModel) + EXIOBASE download
│           ├── validation/  # binary checks vs cited published figures
│           └── cli.py       # `uv run world4 ...`
├── apps/
│   ├── api/                 # FastAPI service over the core (`uv run world4-api`)
│   └── web/                 # browser dashboard (brick 2 — placeholder)
├── docs/                    # this documentation, kept up to date with the code
└── data/                    # downloaded EXIOBASE cache — gitignored, never committed
```

## The precompute-then-serve engine

The Leontief inverse `L = (I - A)^-1` is computed **once** per model. A scenario is
then just a matrix-vector product:

```
Δoutput  = L @ Δy            # Δy holds reductions only  (<= 0)
Δimpact  = S @ Δoutput       # per satellite account (carbon, water, hours, ...)
```

So moving a slider is one cheap `O(n²)` product → real-time. See
[modeling/leontief.md](modeling/leontief.md).

## Why these boundaries

| Boundary | Reason |
| --- | --- |
| `MrioModel` (NumPy) vs pymrio | The engine never imports pymrio at runtime; data is extracted once. Keeps the core testable on a tiny synthetic MRIO and free of a heavy dependency in hot paths. |
| Pydantic contract (`model.py`) | Stable JSON language shared by every client (web, Godot, CLI). |
| `apps/*` depend on `world4-core`, never the reverse | Presentation can be swapped/added without touching the model. |
| Deferred layers (Ghosh, dynamics) as **separate modules** | Protects the accounting seed from false precision (see [epistemics](modeling/epistemics.md)). |

## Quality & security gates

- **Tests**: `uv run pytest` — engine on a hand-built MRIO + integration on the
  pymrio test system + API smoke tests. Real-EXIOBASE checks are marked
  `@pytest.mark.exiobase` and skipped unless data is present.
- **Lint/format**: `ruff` (config in root `pyproject.toml`).
- **Types**: `mypy --strict`.
- **Security**: `bandit` (static analysis), pre-commit secret/large-file hooks,
  Dependabot, CORS off by default. See [`SECURITY.md`](../SECURITY.md).
- **CI** runs all of the above on every push/PR.
