# world4-api

FastAPI service that exposes the [`world4-core`](../../packages/world4-core/) engine
over HTTP, so the web dashboard (and later a Godot client) can drive the same model.

```bash
uv run world4-api          # serves on http://127.0.0.1:8000  (docs at /docs)
```

Endpoints:

| Method | Path           | Purpose                                          |
| ------ | -------------- | ------------------------------------------------ |
| GET    | `/health`      | Liveness probe.                                  |
| GET    | `/model/info`  | Model dimensions (regions, sectors, extensions). |
| POST   | `/scenario`    | Run a `Scenario`, get a `ScenarioResult`.        |

CORS is **off by default**. To allow a browser front-end, set
`WORLD4_CORS_ORIGINS` (comma-separated origins), e.g.
`WORLD4_CORS_ORIGINS=http://localhost:5173`.
