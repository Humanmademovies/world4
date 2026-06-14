# EXIOBASE 3 data

World4's seed runs on **EXIOBASE 3**, a global Multi-Regional Input-Output (MRIO)
database resolving **44 countries + 5 Rest-of-World regions**, with satellite
accounts for greenhouse gases, water, energy, land use, material extraction, and
**employment in hours worked** per country × sector.

We access it through [`pymrio`](https://pymrio.readthedocs.io/).

## Licence — read before redistributing

EXIOBASE is distributed under its own licence (Creative Commons, via its Zenodo
record) — **separate from this repository's AGPL-3.0 code licence**. We therefore:

- **Never commit the data** (it is also multi-GB). `data/` is gitignored.
- Document attribution and let each user download it themselves.

> ⚠️ Verify the exact licence text and required citation on the official EXIOBASE
> Zenodo record for the version you download, and record the version + DOI in the
> commit/PR that introduces a validated figure. (Citations required — see
> [epistemics](../modeling/epistemics.md).)

## Fetching it

The download is large and slow; it must **never** run in CI.

```bash
uv run python -c "from world4_core.data import download_exiobase; download_exiobase(years=[2022], system='pxp')"
```

This caches into `data/exiobase3/` (gitignored). `pxp` = product-by-product;
`ixi` = industry-by-industry. The choice of version/year used for validation is
an [ADR](../decisions/) decision made at brick 1.

## Loading it

```python
from world4_core.data import load_exiobase_model
model = load_exiobase_model("data/exiobase3/IOT_2022_pxp.zip")
```

Memory note: a full EXIOBASE Leontief inverse is ~9800×9800 (hundreds of MB
dense). This is the deliberate "precompute once" cost of the seed.

## Development without the data

The whole engine is developed and unit-tested against pymrio's small synthetic
MRIO (`load_test_model()`), so contributors never need the real download to work
on the code. Real-data validation tests are marked `@pytest.mark.exiobase`.
