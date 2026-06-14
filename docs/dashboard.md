# Dashboard (brick 2)

The web dashboard turns the engine into something you can *steer*: colour the world
by an impact, pull demand-reduction levers, and watch every impact respond live.

## Data flow

```
EXIOBASE zip ──build-model──▶ served artifact (.npz, multipliers M=S·L)
                                   │  loaded in ~0.04 s
                                   ▼
                         world4-api (FastAPI, /api/*)
                                   │  JSON
                                   ▼
                    world4-web (React + MapLibre)  ◀── same API a Godot client could call
```

The expensive Leontief inversion happens once at build time (see
[ADR 0006](decisions/0006-precomputed-multipliers-and-react-front.md)); the API
serves the compact multipliers, so a slider move is just `M · Δy`.

## API surface (`/api`)

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/health` | Liveness. |
| GET | `/model/info` | Regions, sectors, extensions, `has_footprints`. |
| GET | `/impacts` | Headline impact catalog (key, label, unit, **coverage**). |
| GET | `/impacts/{key}/by-region` | Baseline consumption value per region (map colour). |
| POST | `/simulate` | Headline-impact deltas for a `Scenario` (the panels). |
| POST | `/scenario` | Full per-stressor result (advanced). |

Engine guards (unknown sector/region, reduction out of `[0,1]`) return **422**, never
500. CORS is off unless `WORLD4_CORS_ORIGINS` is set; in production FastAPI serves the
built front at `/` (single origin, no CORS).

## Headline impacts & honest coverage

The ~1500 EXIOBASE stressors are curated into a handful of headline impacts
(`world4_core.impacts`), each aggregating **same-unit** stressors within one
extension and carrying a `coverage` flag:

| Impact | Unit | Coverage | Note |
| --- | --- | --- | --- |
| CO2 — combustion | kg | partial | non-combustion/process CO2 not populated |
| Water — blue | Mm3 | good | |
| Land use | km2 | good | |
| Material extraction | kt | partial | |
| Energy use | TJ | good | |
| Employment — hours | M.hr | good | hours, not jobs (FTE conversion is brick 4) |

There is **no single aggregate index**: each impact is shown side by side with its own
metric, and the coverage flag keeps rigour (the Leontief result) visually distinct from
uncertainty (uneven data coverage). See [epistemics](modeling/epistemics.md).

## Sanity check

Cutting global *Paddy rice* final demand by 50% moves **water −2.2%** (rice is
water-intensive), CO2 −0.29%, land −0.40% — the kind of physically plausible signature
the model should produce.

## Work-time panel (brick 4)

Click a country to open its **Work time** panel (equal billing with the ecology
impacts): sliders for start/retirement age, n% and weeks/year give the weekly hours
per worker; a target box solves the inverse (target hours → required retirement age /
n% / start age). When you pull industry levers, the panel reflects the
**scenario-adjusted** production hours and shows the **hours freed**. See
[work-time](modeling/work-time.md).

## Not yet (later bricks)

- Sustainability **target** lines per impact (brick 3) — targets must be sourced first.
- Attributing scenario Δ to consuming regions on the map (currently the map shows the
  baseline; panels show global Δ).
