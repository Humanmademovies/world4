# world4-web

The browser dashboard: a choropleth of the world (2D or globe) coloured by a chosen
impact, with demand-reduction sliders whose effects update live. It is a thin client
over the [`world4-api`](../api/) HTTP service — the same API a future Godot client
would use.

Stack: **React + TypeScript + Vite**, map via **MapLibre GL JS** (2D + globe).

## Run it

```bash
# 1. (once) build a served model artifact so the API has real data, fast:
uv run world4 build-model --exiobase data/exiobase3/IOT_2022_pxp.zip \
    --out data/models/exiobase_2022_pxp.npz

# 2. start the API (serves the artifact if WORLD4_MODEL_PATH is set, else test model):
WORLD4_MODEL_PATH=data/models/exiobase_2022_pxp.npz uv run world4-api

# 3a. dev (hot reload; Vite proxies /api to the API):
cd apps/web && npm install && npm run dev

# 3b. or build + let FastAPI serve it at the API origin:
cd apps/web && npm install && npm run build   # emits dist/, served by world4-api at /
```

> Note: port 8000 is reserved on some Windows setups — set `WORLD4_API_PORT` (and
> update `vite.config.ts`'s proxy) if needed.

## What it shows

- **Map**: each region coloured by its baseline *consumption* footprint for the
  selected impact. The 5 Rest-of-World aggregates and Malta have no geometry.
- **Levers**: pick a sector (searchable), optionally scope to a region, set how much
  of its final demand to remove. Reductions only — the seed never adds demand.
- **Impact panels**: every headline impact side by side with its own unit and an
  explicit **coverage** flag (no single aggregate index; rigour vs uncertainty stays
  visible).

Design constraints carried from the seed live in [`docs/dashboard.md`](../../docs/dashboard.md).
