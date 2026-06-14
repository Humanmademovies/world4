# Security policy

World4 is a research/simulation tool, but we keep secure defaults from day one.

## Reporting a vulnerability

Please report suspected vulnerabilities privately via GitHub Security Advisories
("Report a vulnerability" on the repository's *Security* tab) rather than a public
issue. We aim to acknowledge within a few days.

## Secure-by-default posture

- **No secrets in the repo.** `.env*` files are gitignored; pre-commit hooks block
  private keys and large files.
- **CORS is off by default** in the API; enable specific origins via
  `WORLD4_CORS_ORIGINS`.
- **Input validation** at the contract boundary: scenarios are validated by
  Pydantic (e.g. `reduction ∈ [0, 1]`), rejecting out-of-range input with HTTP 422.
- **Dependency hygiene:** dependencies are pinned via `uv.lock`; Dependabot opens
  update PRs; CI runs `bandit` static analysis.
- **No data exfiltration:** the engine reads local MRIO data only; the EXIOBASE
  download is explicit and user-initiated.

## Scope notes

The API ships without authentication — it is intended for local/dev use behind
your own access control in the seed phase. Do not expose it publicly without adding
authentication and rate limiting.
