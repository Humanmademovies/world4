# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added — Brick 3: sourced sustainability targets
- `world4_core.targets`: a sourced per-capita boundary registry (CO2 with 2 °C +
  1.5° presets, blue water 574 m³, material 7.2 t — O'Neill et al. 2018 + Hot or
  Cool) and `assess()` (overshoot ratio + overshoot day). No aggregate index; land
  and energy intentionally have no target.
- API: `GET /api/targets` (catalog) and `GET /api/targets/region/{region}` (per-capita
  footprint vs boundary, with CO2 ambition preset).
- Dashboard: a **Targets** panel per region — each limit vs its fair-share boundary,
  overshoot ratio/day, ambition selector, honest "no boundary" rows; footprint and
  target kept visually distinct.
- Docs: `docs/modeling/targets-sources.md` (sources, EXIOBASE compatibility, scope).
- Verified on real data: France CO2 ×3.2 (vs 2 °C), blue water ×0.65 (under), material ×2.4.

### Added — Brick 4: work-time / labour redistribution
- `world4_core.labor`: the labour accounting identity (forward) and inverse solvers
  (target weekly hours → retirement age / n% / start age) with honest infeasibility.
- Labour data pipeline: `LaborInputs`/`RegionLabor`, `build_labor_inputs` (EXIOBASE
  production hours + UN WPP single-age demography; RoW guarded), `world4 build-labor`.
- Industry→labour coupling: a precomputed production-hours multiplier `P`
  (`Δhours = P·Δy`) stored in the model artifact; reducing an industry shrinks a
  country's production hours and the work-time view updates.
- API: `/api/labor` catalog, GET + POST `/labor/{region}` and `/labor/{region}/solve`
  (POST variants carry the levers → scenario-adjusted hours).
- Dashboard: a **Work time** panel (bidirectional sliders + target solve) shown next
  to the ecology impacts; pulling industry levers shows the hours freed.
- Data docs: `docs/data/datasets.md` (full catalog), `exiobase-sectors.md` (200 pxp +
  163 ixi), `exiobase-stressors.md` (all 733), `docs/modeling/work-time.md`.
- Demography source: UN WPP 2024.

### Added — Brick 2: API + web dashboard
- Precomputed-multiplier serving: `MrioModel` now supports `multipliers` (M=S·L)
  with optional `leontief`/`Extension.S`; `build.to_served_model`,
  `serialize.save_model`/`load_model` (npz, no pickle), and `world4 build-model`
  produce/load a compact artifact the API loads in ~0.04 s.
- Headline impact catalog (`world4_core.impacts`): curated same-unit aggregates
  with honest coverage flags, generic fallback for unknown models.
- Expanded FastAPI under `/api`: `model/info`, `impacts`, `impacts/{key}/by-region`,
  `simulate`, `scenario`; engine errors → 422; serves the built web client at `/`.
- `apps/web`: React + TypeScript + Vite dashboard with a MapLibre choropleth
  (2D + globe), region selection, searchable sector levers, and side-by-side impact
  panels (no aggregate index; coverage shown). Bundled countries GeoJSON (Natural
  Earth 110m, 43 EXIOBASE countries).
- Docs: `docs/dashboard.md`, ADR 0006; web build added to CI.

### Added — Brick 1: real EXIOBASE wiring + France validation
- Consumption-based footprint accounting: `consumption_footprint`, `per_capita`,
  `FootprintEntry`, `RegionFootprint`.
- `MrioModel.final_demand_by_region` (final demand by consuming region) and
  `MrioModel.consuming_demand`, populated by the loader from EXIOBASE `Y`.
- Binary validation on real EXIOBASE 3 (2022, pxp): engine reproduces pymrio's
  `D_cba` to machine precision; France fossil-CO2 footprint (5.0 tCO2/cap) within
  a sourced plausibility band anchored on SDES (9.2 tCO2eq/cap). Marked
  `@pytest.mark.exiobase`, auto-skipped without data.
- Docs: `docs/validation.md`, ADR 0005 (EXIOBASE 2022 pxp), EXIOBASE structure
  notes (49 regions, 200 products, FR, extensions incl. employment hours+people).

### Added — Brick 0: engine seed
- uv workspace (monorepo): `world4-core` engine + `world4-api` service + `apps/web`
  placeholder.
- Leontief engine: `leontief_inverse`, `build_delta_final_demand`, `run_scenario`
  with a reductions-only (`Δy ≤ 0`) guarantee.
- Serialisable Pydantic contract: `Scenario`, `Lever`, `ScenarioResult`.
- `MrioModel` internal representation, decoupled from pymrio.
- Data loaders: `load_test_model` (synthetic MRIO) and `load_exiobase_model`;
  `download_exiobase` helper (never run in CI).
- Validation scaffold (`ReferenceValue`, `within_tolerance`) — cited values added
  at brick 1.
- FastAPI service (`/health`, `/model/info`, `/scenario`); CORS off by default.
- CLI: `world4 info` / `world4 demo`.
- Tests: engine on a hand-built MRIO, integration on the pymrio test system, API
  smoke tests.
- Docs: epistemic framing, architecture, roadmap, Leontief, parameters, EXIOBASE,
  and ADRs 0001–0004. Tooling: ruff, mypy (strict), bandit, pre-commit, CI,
  Dependabot. Licence: AGPL-3.0-or-later.
