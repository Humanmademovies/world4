# Demand levers — what a slider does

A **lever** reduces the **final demand** of one sector (optionally in one region).
"Final demand" = what is ultimately consumed (households, government, investment,
exports) — not the intermediate sales between industries.

## When you drag a slider

Setting a sector to **−30%** removes 30% of its final demand. The engine then:

1. propagates the cut **upstream** through the whole supply chain (`Δoutput = L · Δdemand`);
2. recomputes every **environmental impact** (`Δimpact = intensity · Δoutput`);
3. recomputes the **production hours** each country needs (which feeds the Work-time panel).

So reducing one sector touches many others, in many countries — that's the point.

## Rules of the seed (honest by design)

- **Reductions only.** You can never *add* demand here; the model only explores doing less.
- **No reinjection.** Money or labour "freed" by a cut is not magically spent elsewhere.
- **Constant technology.** Intensities don't improve; the seed isn't a green-transition model.

## Reading a sector

Open the **Sectors** tab and pick any sector to see, for the selected country, the
**share of each footprint it drives** and the **labour it ties up** — i.e. exactly
what its lever would move, and by how much.
