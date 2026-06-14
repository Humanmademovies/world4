# Parameters & anti-mathwashing

## The rule

> Any assumption that could hide in the engine must become an **explicit, sourced
> slider with an uncertainty range.**

A result that depends on a contested assumption must **never** be presented with
the false rigour of an accounting calculation. Two kinds of number live in World4
and must stay visually and structurally distinct:

| Kind | Example | Status in the UI |
| --- | --- | --- |
| **Accounting result** | `Δimpact = S @ L @ Δy` | High rigour. Derived from data + the Leontief identity. |
| **Tunable assumption** | "fraction of final demand that is unnecessary / advertising-driven" | A slider with a cited range and an explicit uncertainty band. Never silently baked in. |

## Parameter families (to be implemented brick by brick)

These are recorded here so they are designed as parameters from the start, not
discovered as hidden constants later. None are hardcoded in the engine.

- **Sustainability targets** (brick 3): carbon budget, planetary-boundary
  thresholds, per-capita downscaling, overshoot day. Ambition presets: 1.5 °C /
  2 °C / impact-neutral / regenerative. **No aggregate index** — each limit keeps
  its own metric, shown side by side.
- **Employment conversion** (brick 4): hours-per-FTE, retirement age, target
  employment rate. `jobs = hours / hours-per-FTE`. The hours↔jobs distinction is
  native, not derived after the fact.
- **Demand-composition assumptions** (brick 5): e.g. unnecessary / advertising-
  driven fraction of final demand. Canonical anti-mathwashing slider.

## Requirements for every parameter

1. A **default** and an **uncertainty range**.
2. A **citation** (`source`) — no value enters the model unsourced (see
   [`validation/reference.py`](../../packages/world4-core/src/world4_core/validation/reference.py)
   for the same rule applied to validation targets).
3. Surfaced to the client through the serialisable contract so the UI can render
   it as a control with its provenance and uncertainty visible.
