# ADR 0001 — Headless core with thin clients

- **Status:** accepted
- **Date:** 2026-06-14

## Context

World4 must travel from an accounting *seed* to a turn-based simulation *game*
(likely Godot), while staying modular, scalable and maintainable.

## Decision

All simulation logic lives in a single pure-Python package, `world4-core`, with
**no UI or web dependency**. Clients (FastAPI service, web dashboard, future Godot
client, CLI) communicate with it only through a serialisable Pydantic contract
(`Scenario` → `ScenarioResult`). The MRIO data is extracted from `pymrio` once
into an internal NumPy structure (`MrioModel`); the engine does not depend on
pymrio at runtime.

## Consequences

- The engine is unit-testable on a tiny synthetic MRIO; no heavy deps in hot paths.
- Adding/replacing a front-end never touches the model.
- The Godot game becomes a *client port*, not a rewrite.
- Cost: a serialisation boundary to maintain, and one extraction step at load time.
