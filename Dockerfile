# syntax=docker/dockerfile:1
# Single-origin production image: the FastAPI service serves both the JSON API
# (/api) and the built web dashboard (/), as designed (see apps/api/app.py).
# WORLD4_WEB_BASE lets a reverse proxy mount the app under a sub-path
# (e.g. /world4/) without any global asset routes on the proxy side.

FROM node:22-alpine AS web
WORKDIR /build
COPY apps/web/package.json apps/web/package-lock.json ./
RUN npm ci
COPY apps/web/ ./
ARG WORLD4_WEB_BASE=/
RUN npm run build -- --base=${WORLD4_WEB_BASE}

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
COPY pyproject.toml uv.lock README.md ./
COPY packages ./packages
COPY apps/api ./apps/api
RUN uv sync --frozen --no-dev
COPY --from=web /build/dist ./apps/web/dist

# Artifacts (data/models, data/labor) are mounted at /app/data — never baked in.
ENV WORLD4_API_HOST=0.0.0.0
EXPOSE 8537
CMD ["/app/.venv/bin/world4-api"]
