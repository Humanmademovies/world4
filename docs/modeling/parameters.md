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

## Implemented — brick 5: the assumptions registry

Contested hypotheses live in
[`world4_core.assumptions`](../../packages/world4-core/src/world4_core/assumptions.py)
(`Assumption`, `ASSUMPTIONS`): each entry carries a sourced `default`, `low`,
`high` and a mandatory citation. A `Scenario` activates them via its
`assumptions` field; the engine removes the given fraction of final demand
**multiplicatively** with the levers (`remaining = (1 − levers) · Π(1 − assumption)`),
preserving the negative-only invariant. `GET /api/assumptions` serves the
catalog; `POST /api/simulate` returns, for every impact, the point value at the
slider setting **and** a `delta_low`/`delta_high` band computed at the published
range ends. The dashboard renders assumptions in a dedicated amber, dash-bordered
panel, and every assumption-touched impact card switches to a banded, flagged
display — a hypothesis never looks like accounting.

### advertising_demand_share

Share of observed final demand that would not exist without brand advertising.

| | value | derivation |
| --- | --- | --- |
| default | **6.36%** | Molinari & Turino (2018), Table 4 panel A: long-run consumption **+6.79%** (median) vs a counterfactual US economy without advertising; share of observed demand = x/(1+x). |
| low | **0.42%** | Same table, low end of the 90% credible interval (+0.42%). Consistent with Ashley, Granger & Schmalensee (1980), who find no evidence advertising Granger-causes aggregate consumption. |
| high | **14.75%** | Same table, high end of the 90% credible interval (+17.3%). |

Sources: Molinari, B. & Turino, F. (2018). *Advertising and Aggregate
Consumption: A Bayesian DSGE Assessment*. Economic Journal 128(613), 2106–2130.
doi:10.1111/ecoj.12514 (open manuscript: RUA, Universidad de Alicante,
hdl:10045/79511). Ashley, R., Granger, C.W.J. & Schmalensee, R. (1980).
*Advertising and Aggregate Consumption: An Analysis of Causality*. Econometrica
48(5), 1149–1167.

Honesty limits (shown as `note` in the catalog): the estimate is US-only
(1976–2006) and concerns household consumption; we apply it uniformly to all
products, regions and total final demand. Both extrapolations are assumptions
in their own right — which is exactly why this is a slider and not a constant.
