# Validation

The seed rule: at each milestone, reproduce a **published / documented** figure
before advancing. Numbers are cited, never invented. Tests live in
[`test_exiobase_validation.py`](../packages/world4-core/tests/test_exiobase_validation.py)
(marked `@pytest.mark.exiobase`, auto-skipped when the dataset is absent).

## Brick 1 — France footprint (EXIOBASE 3, 2022, product-by-product)

Two layers, because "reproduce a published figure" has two distinct meanings:

### 1. Engine correctness (hard gate)

Our `consumption_footprint("FR")` reproduces pymrio's own consumption-based
account (`D_cba`) — the reference EXIOBASE implementation — to machine precision:

| Stressor | Our engine | pymrio `D_cba` | rel. diff |
| --- | --- | --- | --- |
| `CO2 - combustion - air` | 3.414329e11 kg | 3.414329e11 kg | ~3e-15 |

This proves the Leontief propagation and data extraction are correct on the real
9 800 × 9 800 system, independent of any contested external number.

### 2. External published cross-check (plausibility band)

France per-capita consumption-based **fossil CO2** footprint, EXIOBASE 2022 pxp:

- **5.0 tCO2/cap** (341.4 Mt total; population 67.97 M, World Bank 2022).

Anchored against the French ministry figure:

- **SDES** ("L'empreinte carbone de la France de 1995 à 2022"): **9.2 tCO2eq/cap**
  in 2022, of which ~78 % is CO2 → **~7.2 tCO2/cap**.

EXIOBASE (5.0) and SDES (~7.2 CO2) are the **same order of magnitude** but not
identical — expected, because they are **different models** (EXIOBASE MRIO vs the
SDES hybrid method) and because EXIOBASE's non-combustion/process CO2 is unevenly
covered here (those stressors come back as NaN and are honestly excluded rather
than fabricated). The test therefore asserts a **sourced plausibility band**
(4–10 tCO2/cap), not an exact match — the anti-mathwashing stance: we do not give
a cross-model comparison the false rigour of an identity.

> Methodology note: "fossil CO2" = CO2 air stressors excluding biogenic
> (`CO2_bio`, `biogenic`). In EXIOBASE 2022 pxp this reduces to combustion CO2,
> because the non-combustion CO2 stressors are not populated for this footprint.

### Bonus — employment is native

The `employment` extension carries **both** hours (`M.hr`) and people (`1000 p`),
split by skill × gender. Embodied in French final demand (2022): **100.9 billion
hours / ≈ 49.9 M people**. This confirms the hours↔jobs distinction the seed
requires (brick 4 will turn hours into FTE/jobs via sourced sliders).

## Sources

- SDES, *L'empreinte carbone de la France de 1995 à 2022* —
  <https://www.statistiques.developpement-durable.gouv.fr/lempreinte-carbone-de-la-france-de-1995-2022>
- World Bank, *Population, total — France* (2022 ≈ 67.97 M).
- EXIOBASE 3 (2022, pxp) via pymrio — see [data/exiobase.md](data/exiobase.md).
