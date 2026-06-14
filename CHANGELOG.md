# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project uses
[Semantic Versioning](https://semver.org/).

## [Unreleased]

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
