# In-app wiki (the Guide drawer)

A left **drawer** (the "📖 Guide" button) that makes the dashboard self-explanatory:
what every lever does, what each sector affects and by how much, and a glossary —
**bilingual (FR/EN)** and **live** (sector figures follow the selected country).

## Two content sources (by design)

1. **Narrative pages** — authored Markdown, bundled with the front under
   [`apps/web/src/content/wiki/{en,fr}/`](../apps/web/src/content/wiki):
   `overview`, `levers`, `work-time`, `targets`, `glossary`. Each exists in both
   languages; the drawer's FR/EN toggle switches them. Edit the `.md` files to update.
2. **Computed sector profiles** — *not* hand-written for 200 sectors. For the selected
   country, `world4_core.wiki.sector_profile` derives, per sector: the **share of each
   footprint it drives** (comparable %, ranked) and the **production hours it ties up**.
   Served by `GET /api/wiki/sector/{sector}?region=` and `GET /api/wiki/sectors`. This
   stays honest and never goes stale — it reads the live model.

Sector metadata (code, consumption category) is a small bundled table derived from
the EXIOBASE classification: `world4_core/data/sectors_pxp.json`.

## Honest & up to date

- Sector content is computed from the model, so it can't drift from reality.
- Impact data labels arrive in English from the API; the FR view maps the headline
  impacts via a small table (`apps/web/src/content/wiki.ts`).
- Each panel (levers, work-time, targets) has a `?` that opens the drawer at the
  matching page.

## Adding content

- New narrative page: add `apps/web/src/content/wiki/en/<slug>.md` **and**
  `.../fr/<slug>.md`, then list it in `WIKI_PAGES` in `apps/web/src/content/wiki.ts`.
- Richer sector text: the computed profile is the baseline; hand-written overrides per
  sector can be layered on later (the chosen "auto + overrides" approach).
