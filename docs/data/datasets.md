# Data catalog — everything World4 has at its disposal

A plain-language inventory of every dataset World4 ingests: what's in it, at what
granularity, in what units, **all of it — not just the parts currently used** — and
exactly where it comes from (source + URL + how it was acquired).

All raw data lives under `data/` and is **gitignored** (never committed): it is
large and carries its own licence (separate from this repo's AGPL-3.0 code).

| Dataset | Role in World4 | Lives in |
| --- | --- | --- |
| EXIOBASE 3 | The world economy + its physical/social pressures | `data/exiobase3/` |
| UN World Population Prospects 2024 | Demography (population by age) | `data/demography/` |
| Natural Earth | Country shapes for the map | `apps/web/public/countries.geojson` |
| *(derived)* model & labour artifacts | Precomputed, fast-to-serve | `data/models/`, `data/labor/` |

---

## 1. EXIOBASE 3 — global Multi-Regional Input–Output (MRIO) database

**What it is.** A *monetary* picture of the entire world economy for one year: who
buys what from whom, across every sector and country, **plus** satellite accounts
that attach physical and social pressures (emissions, water, land, materials,
energy, jobs…) to each sector. It's the backbone of World4.

**Source & acquisition.**
- Publisher: the EXIOBASE consortium, hosted on Zenodo.
- Concept DOI: **10.5281/zenodo.3583070** — <https://doi.org/10.5281/zenodo.3583070>
- Exact file we downloaded: `IOT_2022_pxp.zip` from
  <https://zenodo.org/records/20051562/files/IOT_2022_pxp.zip>
- How: programmatically via **pymrio 0.6.3** (`pymrio.download_exiobase3`), wrapped
  in [`world4_core.data.download.download_exiobase`](../../packages/world4-core/src/world4_core/data/download.py).
  Parsed with `pymrio.parse_exiobase3`. pymrio docs: <https://pymrio.readthedocs.io/>
- Licence: Creative Commons (CC BY-SA) — confirm the exact terms on the Zenodo
  record before redistributing.

**Granularity.**
- **49 regions** = 44 individual countries (ISO-2 codes: `FR`, `DE`, `US`, `CN`,
  `GB`, …) + **5 Rest-of-World aggregates**: `WA` (Asia-Pacific), `WL` (America),
  `WE` (Europe), `WF` (Africa), `WM` (Middle East).
- **200 products** (this is the *product-by-product*, "pxp", build). EXIOBASE also
  ships an *industry-by-industry* ("ixi") build with **163 industries** — same data,
  different symmetric form (see [ADR 0005](../decisions/0005-exiobase-pxp-2022.md)).
  **Full lists of all products and industries** (with codes & ISIC):
  [exiobase-sectors.md](exiobase-sectors.md).
- **Year 2022** (the series runs 1995–2022; one file per year).

**The monetary core tables** (unit: **million euros, M.EUR**, basic prices):

| Symbol | Name | Shape | Meaning |
| --- | --- | --- | --- |
| `Z` | Inter-industry flows | 9800 × 9800 | sales from each product to each product |
| `Y` | Final demand | 9800 × (49×7) | sales to final users (see categories below) |
| `x` | Total output | 9800 | total production per product |
| `A` | Technical coefficients | 9800 × 9800 | input per unit output (`Z` ÷ `x`) |
| `L` | Leontief inverse | 9800 × 9800 | total (direct+indirect) requirements `(I−A)⁻¹` |

(9800 = 49 regions × 200 products.)

**Final-demand categories** (the 7 columns of `Y` per consuming region):
Household final consumption · NPISH (non-profits serving households) · Government
final consumption · Gross fixed capital formation · Changes in inventories ·
Changes in valuables · Exports (fob).

**Satellite accounts (the "extensions") — the full inventory.** Each attaches a
pressure to every region×product. Counts and units are read directly from the 2022
pxp file:

| Extension | # indicators | Unit(s) | What's inside |
| --- | --- | --- | --- |
| **employment** | 12 | `1000 p` (6) + `M.hr` (6) | jobs **and** hours worked, split by skill (low/medium/high) × sex (male/female) |
| **air_emissions** | 420 | `kg` (418) + `kg CO2-eq` (2) | pollutants & GHGs by substance × source (combustion / non-combustion / agriculture / waste): CO2, CO2-bio, CH4, N2O, NOx, SOx, NH3, NMVOC, CO, PM2.5/PM10, heavy metals (As, Cd, Hg, Pb, Zn…), PAHs, HFC/PFC/SF6… The 2 `kg CO2-eq` rows are GWP-weighted GHG totals |
| **energy** | 4 | `TJ` | energy use: Emission-relevant / Final / Gross / Net |
| **material** | 62 | `kt` (kilotonnes) | Domestic Extraction Used: primary crops, crop residues, grazing, wood, fish, minerals, metal ores, fossil fuels |
| **water** | 194 | `Mm3` (million m³) | Consumption (green & blue) and Withdrawal (blue), by use: agriculture per crop, livestock, electricity cooling per technology, domestic, manufacturing… |
| **land** | 26 | `km2` | land use by type: artificial surfaces, cropland per crop, pasture, forest… |
| **nutrients** | 6 | `kg` | nitrogen (N) and phosphorus (P) releases to soil and water (agriculture) |
| **factor_inputs** | 9 | `M.EUR` | value added: taxes less subsidies on products, other net taxes, compensation of employees (by skill), operating surplus & mixed income |

Full per-stressor lists: [all products & industries](exiobase-sectors.md) ·
[all 420 air + 194 water stressors](exiobase-stressors-air-water.md).

For each extension pymrio also derives, after computation: `S` (intensity per unit
output), `M` (multipliers `S·L`), and `D_pba`/`D_cba` (production- and
consumption-based accounts).

**Honest coverage note.** Carbon, water, materials, land map well to the economy.
Biodiversity, novel entities (most chemistry), and some N/P flows are sparse or
absent — and some individual stressors come back as `NaN` (e.g. non-combustion CO2
in the consumption footprint). World4 shows real coverage and never fakes a uniform
one (see [epistemics](../modeling/epistemics.md)).

**What World4 uses today vs. what's available.** Available: *everything above.*
Used so far: a curated handful of "headline impacts" (combustion CO2, blue water,
land, material, energy, employment hours — see [dashboard.md](../dashboard.md)),
the employment **hours** for the work-time model, and the monetary tables for the
Leontief engine. The other ~1500 stressors are present and can be surfaced as the
project grows.

---

## 2. UN World Population Prospects 2024 — demography

**What it is.** The UN's official estimates and projections of population, by
single year of age and sex, for every country and many aggregates. World4 uses it to
turn a retirement/start-of-work age into a *number of people of working age*.

**Source & acquisition.**
- Publisher: United Nations, Dept. of Economic and Social Affairs, Population
  Division — *World Population Prospects 2024*.
- Portal & methodology: <https://population.un.org/wpp/> (see "Methodology" and
  "Definition of Projection Variants" there).
- Exact file we downloaded: `WPP2024_PopulationBySingleAgeSex_Medium_1950-2023.csv.gz`
  from `https://population.un.org/wpp/assets/Excel Files/1_Indicator (Standard)/CSV_FILES/`
- How: a documented `curl` download into `data/demography/`, then parsed by
  [`world4_core.data.labor_build`](../../packages/world4-core/src/world4_core/data/labor_build.py).
- Licence: CC BY 3.0 IGO — confirm on the WPP site.

**Granularity & columns.** One row per (location, year, single age, variant); unit
is **thousands of persons**.

| Column | Meaning |
| --- | --- |
| `Location`, `ISO3_code`, `ISO2_code`, `LocID` | the place (country or aggregate) |
| `LocTypeName` | "Country/Area" vs region/income-group aggregates |
| `Time` | calendar year |
| `AgeGrpStart` (`AgeGrp`) | single age, **0 to 100** (100 = "100+") |
| `PopMale`, `PopFemale`, `PopTotal` | population (thousands) |
| `Variant` | here "Medium" |

**Coverage.** This file: **1950–2023** estimates, single ages, *Medium* variant.

**Also available from WPP (not downloaded yet).** A companion file extends single-age
population to **2024–2100** (projections) — directly useful for the future/game phase.
WPP also publishes 5-year age groups, and many other indicators: births, deaths,
fertility, life expectancy, mortality, migration, median age, sex ratios; and other
projection variants (Low / High / Constant-fertility, etc.).

**What World4 uses today.** `PopTotal` by single age, **year 2022**, for the 44
named EXIOBASE countries. The 5 Rest-of-World aggregates get no demography (they're
multi-country; their ISO codes aren't real countries — note `WF` even collides with
Wallis-&-Futuna's ISO-2, which the builder explicitly guards against).

---

## 3. Natural Earth — country boundaries (for the map only)

**What it is.** Free vector map data. World4 uses the country polygons to draw the
choropleth.

**Source & acquisition.**
- Publisher: Natural Earth (public domain).
- File: `ne_110m_admin_0_countries.geojson` (1:110m, low detail) from the
  Natural Earth vector repo: <https://github.com/nvkelso/natural-earth-vector>
- How: fetched, then trimmed to the 43 EXIOBASE countries with geometry (keeping
  only `iso` = ISO-2 and `name`), saved to `apps/web/public/countries.geojson`
  (~99 KB, the one data file small enough to commit).
- Licence: public domain.

**Granularity.** 1:110m resolution (coarse, fine for a world choropleth). Malta is
too small to appear at this resolution; the 5 Rest-of-World aggregates have no single
geometry.

---

## 4. Derived artifacts (what World4 precomputes from the above)

Not external data — these are compact files World4 builds once so the API starts
fast. Both gitignored.

| Artifact | Built by | Contains | From |
| --- | --- | --- | --- |
| `data/models/exiobase_2022_pxp.npz` | `world4 build-model` | multipliers `M = S·L` per extension + demand vectors | EXIOBASE |
| `data/labor/labor_inputs_2022.json` | `world4 build-labor` | production hours per region + population by single age | EXIOBASE + WPP |

See [ADR 0006](../decisions/0006-precomputed-multipliers-and-react-front.md) for why,
and the [dashboard doc](../dashboard.md) for how they're served.

---

## Licence summary

| Dataset | Licence (verify at source) | Committed to git? |
| --- | --- | --- |
| EXIOBASE 3 | CC BY-SA (Zenodo) | No |
| UN WPP 2024 | CC BY 3.0 IGO | No |
| Natural Earth | Public domain | Yes (trimmed, ~99 KB) |
| World4 code | AGPL-3.0-or-later | Yes |
