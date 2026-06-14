# World4 documentation

World4 is a **physical accounting model of world consumption**: a sandbox where a
planner sets activity-level sliders and watches the *physical* (carbon, water,
energy, materials, land) and *social* (human-hours, jobs) consequences propagate
through the global supply chain, compared against tunable sustainability targets.

It is built **seed → game**: a rigorous accounting seed first, then, iteration by
iteration, a turn-based simulation that can show worlds heading for collapse as
well as solarpunk utopias — calibrated on serious projection scenarios.

## Read this first

- [Epistemic framing](modeling/epistemics.md) — the non-negotiable rules. **Start here.**
- [Architecture](architecture.md) — how the code is laid out and why.
- [Roadmap](roadmap.md) — the brick-by-brick plan.

## Modelling

- [Leontief engine](modeling/leontief.md) — the maths of propagation.
- [Parameters & anti-mathwashing](modeling/parameters.md) — every assumption is a sourced slider.
- [Validation](validation.md) — binary checks against published figures (brick 1: France footprint).
- [Dashboard](dashboard.md) — the web client, the API surface, and headline impacts (brick 2).

## Data

- [Data catalog](data/datasets.md) — **everything** in every dataset (granularity, units, all indicators), with sources.
- [EXIOBASE sector lists](data/exiobase-sectors.md) — all 200 products (pxp) + 163 industries (ixi), with codes & ISIC.
- [EXIOBASE 3](data/exiobase.md) — how to fetch the MRIO + its structure.

## Decisions

- [Architecture Decision Records](decisions/) — why we chose what we chose.
