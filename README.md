# World4

**A physical accounting model of world consumption — a sandbox for degrowth, on the
way to a turn-based simulation of how the planet evolves.**

World4 lets a planner set activity-level sliders (per product, per country) and
watch the **physical** consequences (carbon, water, energy, materials, land) and
**social** ones (human-hours freed, jobs) propagate through the global supply chain
via the Leontief inverse — compared against tunable, sourced sustainability targets.

It is **not** an economic/behavioural model: no prices, no elasticities, no market
equilibrium. It answers one question mechanically — *"if a sector drops, what
happens, everywhere?"* — with productive capital frozen in its current state. The
seed is deliberately **degrowth at constant apparatus**. Read the
[epistemic framing](docs/modeling/epistemics.md) before anything else.

The long game: iteration by iteration, grow this into a turn-based simulation that
can show worlds heading for collapse **and** solarpunk utopias, calibrated on
serious published projection scenarios. See the [roadmap](docs/roadmap.md).

## Status

🌱 **Brick 0 — engine seed.** The Leontief engine runs on a synthetic test MRIO,
fully tested. Real EXIOBASE 3 wiring and the validation against published
footprints are next (brick 1).

## Quickstart

Requires [`uv`](https://docs.astral.sh/uv/). Python 3.12 is fetched automatically.

```bash
uv sync                                   # create the env, install the workspace
uv run pytest                             # run the test suite
uv run world4 info                        # inspect the test model
uv run world4 demo --sector food --reduction 0.5   # propagate a reduction
uv run world4-api                         # serve the HTTP API at http://127.0.0.1:8000/docs
```

## Layout

| Path | What |
| --- | --- |
| [`packages/world4-core`](packages/world4-core) | The engine — pure Python, no UI/web deps. |
| [`apps/api`](apps/api) | FastAPI service over the engine. |
| [`apps/web`](apps/web) | Browser dashboard (brick 2 — placeholder). |
| [`docs/`](docs/index.md) | Architecture, roadmap, modelling, data, decisions. |

See [docs/architecture.md](docs/architecture.md) for how it fits together.

## Contributing

One brick at a time, with a binary success criterion. Citations required for every
factual claim and parameter. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Licence & data

Code: **AGPL-3.0-or-later** (see [`LICENSE`](LICENSE) and
[ADR 0003](docs/decisions/0003-license-agpl.md)). The **EXIOBASE** dataset has its
own licence and is never committed — see [docs/data/exiobase.md](docs/data/exiobase.md).
