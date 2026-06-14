"""Tiny CLI for poking at the engine without a UI.

uv run world4 info
uv run world4 demo --sector food --reduction 0.5
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence

from world4_core.data import load_test_model
from world4_core.engine import run_scenario
from world4_core.model import Lever, Scenario


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="world4", description="World4 engine CLI (test MRIO).")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("info", help="Print model dimensions.")

    demo = sub.add_parser("demo", help="Run a sample reduction scenario.")
    demo.add_argument("--sector", default=None, help="Sector to reduce (default: first sector).")
    demo.add_argument("--reduction", type=float, default=0.5, help="Reduction fraction (0..1).")

    args = parser.parse_args(argv)
    model = load_test_model()

    if args.command == "info":
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

    if args.command == "demo":
        sector = args.sector or model.sectors[0]
        scenario = Scenario(name="demo", levers=[Lever(sector=sector, reduction=args.reduction)])
        result = run_scenario(model, scenario)
        print(result.model_dump_json(indent=2))
        return 0

    return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
