# world4-core

The headless physical-accounting engine of [World4](../../README.md).

Pure Python. **No UI, no web, no I/O beyond data loading.** It turns a *scenario*
(demand-side reductions only) into *impact results* through the Leontief inverse of a
Multi-Regional Input–Output (MRIO) table.

```python
from world4_core import load_test_model, Scenario, Lever, run_scenario

model = load_test_model()                       # small synthetic MRIO from pymrio
scenario = Scenario(levers=[Lever(sector="food", reduction=0.5)])
result = run_scenario(model, scenario)
print(result.totals)                            # Δ per impact, all <= 0
```

See [`docs/architecture.md`](../../docs/architecture.md) and
[`docs/modeling/`](../../docs/modeling/) for the model and its non-negotiable framing.
