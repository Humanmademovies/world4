# Contributing to World4

Thanks for your interest. World4 is built deliberately and incrementally.

## Ground rules

1. **Read [`docs/modeling/epistemics.md`](docs/modeling/epistemics.md) first.** It
   defines what the model *is*. Changes that violate the framing (adding positive
   demand, hidden assumptions, an aggregate index, growth in the seed…) won't be
   accepted.
2. **One brick at a time, binary success criterion.** See
   [`docs/roadmap.md`](docs/roadmap.md). No stacking unrelated changes.
3. **Cite everything.** No value, parameter, or "documented method" enters the
   repo unsourced. Verify a library/UI capability exists before claiming it.
4. **English** for code, commits, and docs.
5. **Docs travel with code.** Behaviour changes update `docs/`, `CHANGELOG.md`, and
   the roadmap in the same PR.

## Local setup

```bash
uv sync
uv run pre-commit install     # optional but recommended
```

## Before opening a PR

```bash
uv run ruff format .
uv run ruff check .
uv run mypy -p world4_core -p world4_api
uv run bandit -r packages/world4-core/src apps/api/src
uv run pytest
```

CI runs all of these. Engine logic belongs in `world4-core` (keep it UI-agnostic);
expose new capability through the Pydantic contract → API → web, in that order.

## Commit messages

Imperative mood, present tense, scoped when useful, e.g.
`engine: clamp overlapping levers at full removal`.

## Data

Never commit EXIOBASE or any large dataset. See
[`docs/data/exiobase.md`](docs/data/exiobase.md).
