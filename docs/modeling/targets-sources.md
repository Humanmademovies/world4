# Sustainability targets — sources, compatibility & scope (brick 3)

Brick 3 shows, for each limit, the current footprint **vs a sourced target**, per
capita, with ambition presets — **never an aggregate index**: each limit stands
beside its own metric. This page is the *sourcing contract*: where every target
number comes from, how well it matches our EXIOBASE metric, and what we therefore
choose to show (and not show).

> Epistemic stance ([epistemics](epistemics.md)): a target is a **sourced, contestable
> parameter**, not a fact. We make the allocation rule and ambition explicit, we keep
> the rigorous footprint visually distinct from the uncertain target, and where no
> defensible per-capita boundary exists we **show no target** rather than invent one.

## Primary source — O'Neill et al. 2018

*A good life for all within planetary boundaries*, Nature Sustainability 1, 88–95,
[doi:10.1038/s41893-018-0021-4](https://doi.org/10.1038/s41893-018-0021-4); dataset:
[goodlife.leeds.ac.uk](https://goodlife.leeds.ac.uk).

Why it is the right backbone: its boundaries are **per capita**, **consumption-based**
(Eora MRIO), at **national** resolution, allocated **equally per person** — the same
shape as World4's footprints. Reference data: year 2011, population 7 billion.

Per-capita boundaries (Table 1):

| Indicator | Planetary boundary (global) | **Per capita / yr** | % of countries within |
| --- | --- | --- | --- |
| CO₂ | 2 °C warming | **1.61 t CO₂** | 34% |
| Phosphorus | 6.2 Tg P | **0.89 kg P** | 44% |
| Nitrogen | 62 Tg N | **8.9 kg N** | 45% |
| Blue water | 4000 km³ | **574 m³** | 84% |
| eHANPP (land) | 18.2 Gt C | **2.62 t C** | 44% |
| Ecological footprint | — | **1.72 gha** | 43% |
| Material footprint | — | **7.2 t** | 44% |

## Ambition layer (carbon) — Hot or Cool Institute

*1.5-Degree Lifestyles* ([hotorcool.org](https://hotorcool.org/projects/1-5-degree-lifestyles/)):
per-capita **lifestyle** carbon footprint targets of **2.5 / 1.4 / 0.7 tCO₂e** for
**2030 / 2040 / 2050** (global average today ≈ 4.6 tCO₂e). These are CO₂**eq** (all
GHG), so they are an *ambition reference*, not a like-for-like with our CO₂-only metric.

## Caveat — Richardson et al. 2023 (planetary boundaries update)

[doi:10.1126/sciadv.adh2458](https://doi.org/10.1126/sciadv.adh2458). The 2023 freshwater
boundary is expressed as the **% of land area** with altered streamflow / soil moisture
— **not** a per-capita water volume. It therefore does **not** map onto our blue-water
*volume* footprint; for a per-capita water target we use O'Neill's 574 m³ instead, and
note the difference.

## Compatibility with our EXIOBASE metrics

Our headline impacts are consumption-based footprints (see
[dashboard](../dashboard.md)). Match of each to a sourced target:

| Our impact (EXIOBASE, consumption) | Candidate target | Verdict |
| --- | --- | --- |
| **CO₂ — combustion** (kg) | O'Neill **1.61 tCO₂** (2 °C) + Hot or Cool **1.5°** presets | 🟢 good (same consumption/cap basis). Caveats: O'Neill is total CO₂, ours is combustion-only; Hot or Cool is CO₂eq. |
| **Water — blue** (Mm³) | O'Neill **574 m³** | 🟢 good — cleanest match (Richardson 2023 unusable as a volume). |
| **Material** (kt) | O'Neill **7.2 t** | 🟡 to confirm: our footprint propagates Domestic Extraction Used through `L` ⇒ a consumption-based material footprint ≈ RMC; check unit kt→t/cap. |
| **Land use** (km²) | O'Neill uses **eHANPP (tC)**, not km² | 🔴 mismatch (biomass appropriation ≠ land area). No clean km²/cap boundary. |
| **Energy** (TJ) | — | 🔴 no planetary boundary (CO₂ is the bounded quantity); only sufficiency floors exist. |
| *(N / P — not yet a headline impact)* | O'Neill **8.9 kg N**, **0.89 kg P** | 🟡 clean boundaries exist; would need adding to the impact catalog. |

## Normative knobs (made explicit, anti-mathwashing)

- **Allocation rule:** equal per capita (O'Neill's choice). Alternatives (historical
  responsibility, need-based) are out of scope but the rule is stated, not hidden.
- **Reference population:** O'Neill used 7 bn (2011); with ~8 bn today the equal share
  shrinks. We compare each country's *per-capita footprint* to the *per-capita
  boundary* directly (no re-downscaling), and note the year of the boundary.
- **Ambition preset:** `2C` (O'Neill 1.61) · `1.5C-2030` (2.5) · `1.5C-2050` (0.7).

## Scope retained for brick 3

1. **Ship first, with targets:** **CO₂** (presets 2 °C + 1.5° 2030/2050) and **blue
   water** (574 m³) — the two clean matches. Binary criterion: a country's per-capita
   footprint vs its equal-share boundary, with the overshoot ratio, sources visible.
2. **Next:** material (confirm RMC equivalence), then N / P (add to the catalog).
3. **Land & energy:** shown **without a numeric target**, explicitly labelled
   *"no per-capita planetary boundary"* — honest coverage, no invented line.

## How it will be implemented

- `world4_core.targets`: a sourced registry (per impact → unit, per-preset per-capita
  boundary, native→target unit factor, allocation, source, note) + an `assess()` that
  compares a region's per-capita footprint to the boundary (overshoot ratio + overshoot
  day). Population comes from the labour artifact (UN WPP). No aggregate index.
- API: `/api/targets` (catalog) and per-impact per-region assessment.
- UI: a region **Targets** panel — each impact's per-capita footprint vs its target
  line + overshoot, an ambition selector, and honest "no target" rows for land/energy;
  rigour (footprint) and uncertainty (target) kept visually distinct.
