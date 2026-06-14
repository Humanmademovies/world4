"""CLI for the engine.

    uv run world4 info
    uv run world4 demo --sector food --reduction 0.5
    uv run world4 build-model --exiobase data/exiobase3/IOT_2022_pxp.zip \
        --out data/models/exiobase_2022_pxp.npz
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from world4_core.build import to_served_model
from world4_core.data import load_exiobase_model, load_test_model
from world4_core.data.labor_build import build_labor_inputs
from world4_core.engine import run_scenario
from world4_core.labor import save_labor_inputs
from world4_core.model import Lever, Scenario
from world4_core.serialize import save_model


def _cmd_info() -> int:
    model = load_test_model()
    print(
        json.dumps(
            {
                "name": model.name,
                "regions": model.regions,
                "sectors": model.sectors,
                "products": model.n,
                "extensions": list(model.extensions),
            },
            indent=2,
        )
    )
    return 0


def _cmd_demo(sector: str | None, reduction: float) -> int:
    model = load_test_model()
    target = sector or model.sectors[0]
    result = run_scenario(
        model, Scenario(name="demo", levers=[Lever(sector=target, reduction=reduction)])
    )
    print(result.model_dump_json(indent=2))
    return 0


def _cmd_build_model(exiobase: str | None, use_test: bool, out: str) -> int:
    if use_test:
        model = load_test_model()
    elif exiobase:
        model = load_exiobase_model(exiobase)
    else:
        print("error: provide --exiobase PATH or --test")
        return 2
    served = to_served_model(model)
    path = save_model(served, out)
    print(
        json.dumps(
            {
                "built": str(path),
                "name": served.name,
                "regions": len(served.regions),
                "sectors": len(served.sectors),
                "products": served.n,
                "extensions": list(served.extensions),
            },
            indent=2,
        )
    )
    return 0


def _cmd_build_labor(exiobase: str, wpp: str, year: int, out: str) -> int:
    inputs = build_labor_inputs(exiobase, wpp, year)
    path = save_labor_inputs(inputs, out)
    with_demography = sum(1 for r in inputs.regions.values() if r.population_by_age)
    print(
        json.dumps(
            {
                "built": str(path),
                "year": inputs.year,
                "regions": len(inputs.regions),
                "with_demography": with_demography,
            },
            indent=2,
        )
    )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="world4", description="World4 engine CLI.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("info", help="Print test-model dimensions.")

    demo = sub.add_parser("demo", help="Run a sample reduction scenario on the test MRIO.")
    demo.add_argument("--sector", default=None, help="Sector to reduce (default: first sector).")
    demo.add_argument("--reduction", type=float, default=0.5, help="Reduction fraction (0..1).")

    build = sub.add_parser("build-model", help="Precompute a served model artifact (.npz).")
    source = build.add_mutually_exclusive_group(required=True)
    source.add_argument("--exiobase", default=None, help="Path to an EXIOBASE 3 zip/folder.")
    source.add_argument("--test", action="store_true", help="Build from the synthetic test MRIO.")
    build.add_argument("--out", required=True, help="Output artifact path (.npz).")

    labor = sub.add_parser(
        "build-labor", help="Build the labour-inputs artifact (EXIOBASE hours + UN WPP demography)."
    )
    labor.add_argument("--exiobase", required=True, help="Path to an EXIOBASE 3 zip/folder.")
    labor.add_argument("--wpp", required=True, help="Path to UN WPP single-age CSV (.csv.gz).")
    labor.add_argument("--year", type=int, default=2022, help="Year for demography (default 2022).")
    labor.add_argument("--out", required=True, help="Output artifact path (.json).")

    args = parser.parse_args(argv)

    if args.command == "info":
        return _cmd_info()
    if args.command == "demo":
        return _cmd_demo(args.sector, args.reduction)
    if args.command == "build-model":
        return _cmd_build_model(args.exiobase, args.test, args.out)
    if args.command == "build-labor":
        return _cmd_build_labor(args.exiobase, args.wpp, args.year, args.out)
    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
