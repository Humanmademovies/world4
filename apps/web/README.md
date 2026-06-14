# world4-web (placeholder — brick 2)

The browser dashboard: a 44-country globe coloured by impact type, with per-country
policy sliders, driven entirely by the [`world4-api`](../api/) HTTP service.

**Not implemented yet.** It is scaffolded as a directory so the architecture
(core → API → web client) is visible from day one. The JS framework and globe
library are chosen at brick 2 (see [`docs/roadmap.md`](../../docs/roadmap.md)),
deliberately *after* the engine is validated, to avoid coupling presentation to a
half-built model.

Design constraints carried from the seed:

- **No single aggregate index.** Each planetary limit is shown side by side with
  its own metric.
- **Rigour vs uncertainty must be visually distinct** — Leontief results and
  tunable assumption sliders should not look equally authoritative.
