# ADR 0004 — FastAPI service + web front (over a Python-native UI)

- **Status:** accepted
- **Date:** 2026-06-14

## Context

The spec suggested a Python-native dashboard (NiceGUI/Reflex) for the seed. But
the long-term target is a turn-based game with a likely **Godot** client, and we
want the same engine to serve every client.

## Decision

Expose the headless core through a **FastAPI HTTP service** (`apps/api`), and build
the dashboard as a **web front-end** (`apps/web`) that consumes that API. The JS
framework and globe library are chosen at brick 2, after the engine is validated.

## Consequences

- One stable HTTP contract serves the web dashboard now and a Godot client later
  (Godot can hit the same endpoints) — no second engine.
- Slightly more upfront plumbing than an all-in-Python UI, and the front-end is
  not Python.
- CORS is off by default and opt-in via `WORLD4_CORS_ORIGINS` for security.
- Supersedes the spec's NiceGUI/Reflex suggestion for the seed.
