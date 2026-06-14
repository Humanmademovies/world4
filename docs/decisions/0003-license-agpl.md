# ADR 0003 — AGPL-3.0 licence

- **Status:** accepted
- **Date:** 2026-06-14

## Context

World4 is a transparency-driven model (anti-mathwashing) that may later be served
as a hosted web app or online game. We want downstream openness preserved even
when the software is only ever *used over a network* (not distributed).

## Decision

License the repository's code under **AGPL-3.0-or-later**. The EXIOBASE dataset
keeps its own (Creative Commons) licence, documented separately in
[`docs/data/exiobase.md`](../data/exiobase.md) and never committed.

## Consequences

- A hosted version (dashboard, online game) must make its source available — the
  network clause closes the SaaS loophole, matching the project's ethos.
- May deter purely proprietary reuse; acceptable trade-off given the goals.
- Game assets and any future Godot client carry their own licence considerations,
  to be addressed when that phase starts.
