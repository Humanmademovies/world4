# Work-time model (brick 4)

How much human work does an economy require, and how can a society **share** it?
This is the labour half of World4 — equal in standing with the ecological half.

## The accounting identity

For a country, one identity ties together the work to be done and the people to do
it:

```
hours_required  = production hours the country must work (from EXIOBASE)
working_age_pop = Σ population with age in [start_age, retirement_age)   (from UN WPP)
employed        = working_age_pop × (1 − n)        # "full employment minus n%"
weekly_hours    = hours_required / employed / weeks_per_year
```

Set the policy knobs, read off the weekly hours. It makes the trade-off explicit:
**retire younger or start later → fewer workers → more hours each**; **raise n →
fewer workers → more hours each**.

## Both directions (bidirectional)

The same identity is solved either way (see
[`labor.py`](../../packages/world4-core/src/world4_core/labor.py)):

- **Forward** — given the knobs, compute weekly hours.
- **Inverse** — fix a *target* weekly load and solve for the **retirement age**, the
  **start age**, or **n%** required to reach it. When a target can't be met (e.g. you'd
  need more workers than exist), the solver returns "not achievable" rather than
  inventing a number.

Example (France 2022, n = 20%, 52 weeks): 20→65 gives ≈ 35.7 h/week; to reach 32
h/week you'd retire at ≈ 70.6 **or** drop n to ≈ 10.7%; 28 h/week is not reachable by
n alone (it would need retirement at ≈ 80).

## Coupling: act on an industry → see the work move

Reducing an industry (a demand-reduction lever) shrinks production, so a country's
production hours fall by `Δhours = (P · Δy)[country]`, where **P** is a precomputed
"production hours per region ← final demand" matrix (`P = 1e6 · R·diag(h)·L`, with
`h` the direct employment-hours intensity). The work-time panel then recomputes on
the **scenario-adjusted** hours. Example: cutting French motor-vehicle final demand
by 50% frees ≈ 846 M·hr/yr (−1.55% of French work), nudging 35.7 → 35.2 h/week.

This is the **production** view (hours worked *in* the country), confirmed as the
project's axis — not the consumption/footprint view.

## Data & sources

- **Production hours**: EXIOBASE 3 `employment` account (hours worked, by country ×
  industry). See the [data catalog](../data/datasets.md).
- **Demography**: UN World Population Prospects 2024, population by single age.
- The 5 Rest-of-World aggregates have no single demography → no work-time view for
  them (shown honestly, not faked).

## Tunable, sourced parameters (anti-mathwashing)

- **n%** (share of working-age not in full-time work — unemployment + inactivity):
  a single slider, default 20%.
- **weeks per year**: a slider (default 52), lower it to model leave/holidays.

Both are explicit controls, not hidden constants — consistent with
[parameters.md](parameters.md) and the [epistemics](epistemics.md).

## Scope limits

- **Constant apparatus**: production-hour intensities are fixed (no productivity
  change); the seed only does *less*.
- One country's required hours respond to *global* demand changes via the supply
  chain (the `P` row captures that country's domestic share).
