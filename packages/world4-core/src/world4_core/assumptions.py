"""Anti-mathwashing assumptions — sourced, tunable hypotheses (brick 5).

Two kinds of number live in World4 (see ``docs/modeling/parameters.md``):
**accounting results** (Leontief identities over data) and **tunable
assumptions** (contested hypotheses such as "how much of final demand is
advertising-driven?"). The rule: any assumption that could hide in the engine
must be an explicit slider with a sourced default and an uncertainty range —
never a hidden constant, and never displayed with the false rigour of an
accounting figure.

This module is the registry of those assumptions plus the pure helpers that
turn them into scenario variants. Seed invariant preserved: an assumption only
ever *removes* final demand.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from world4_core.model import Scenario


class Assumption(BaseModel):
    """A contested, sourced hypothesis exposed as an explicit slider.

    ``default``, ``low`` and ``high`` are fractions of final demand in
    ``[0, 1]``; every one of them must come from a published source (``source``
    is the citation, including how the published figure was converted, if at
    all). ``low``/``high`` bound the *published disagreement*, not the slider's
    mechanical travel.
    """

    key: str
    label: str
    description: str
    unit: str = Field(..., description="What the fraction applies to, e.g. 'of final demand'.")
    default: float = Field(..., ge=0.0, le=1.0)
    low: float = Field(..., ge=0.0, le=1.0, description="Low end of the sourced range.")
    high: float = Field(..., ge=0.0, le=1.0, description="High end of the sourced range.")
    source: str = Field(..., description="Citation for default/low/high. Required.")
    note: str = ""


# Sourced registry. Every value cited; conversions documented in the citation.
ASSUMPTIONS: dict[str, Assumption] = {
    "advertising_demand_share": Assumption(
        key="advertising_demand_share",
        label="Advertising-driven demand",
        description=(
            "Share of observed final demand that would not exist without brand "
            "advertising. Enabling it removes that share of final demand uniformly, "
            "on top of any levers (multiplicative composition)."
        ),
        unit="fraction of final demand",
        default=0.0636,
        low=0.0042,
        high=0.1475,
        source=(
            "Molinari & Turino (2018), 'Advertising and Aggregate Consumption: A "
            "Bayesian DSGE Assessment', Economic Journal 128(613), 2106-2130, "
            "doi:10.1111/ecoj.12514, Table 4 panel A: long-run consumption +6.79% "
            "(90% credible interval [+0.42%, +17.3%]) vs a counterfactual US economy "
            "without advertising. Converted to a share of observed demand via "
            "x/(1+x): 6.36% [0.42%, 14.75%]. The low end is consistent with Ashley, "
            "Granger & Schmalensee (1980), Econometrica 48(5), 1149-1167, who find "
            "no evidence that advertising Granger-causes aggregate consumption."
        ),
        note=(
            "US estimate (1976-2006) applied uniformly to all products and regions; "
            "the paper models household consumption, we apply it to total final "
            "demand. Both extrapolations are honesty limits, not data."
        ),
    ),
}


def available_assumptions() -> list[Assumption]:
    """The full sourced catalog, for clients to render as explicit sliders."""
    return list(ASSUMPTIONS.values())


def get_assumption(key: str) -> Assumption:
    """Look up one assumption; unknown keys are an error, never a silent 0."""
    try:
        return ASSUMPTIONS[key]
    except KeyError:
        raise ValueError(f"unknown assumption {key!r}") from None


def band_scenarios(scenario: Scenario) -> tuple[Scenario, Scenario] | None:
    """Scenario variants with every active assumption at its sourced low/high.

    Returns ``None`` when the scenario carries no assumptions (pure accounting —
    no uncertainty band to show). The band reflects the *published* range, not
    the user's slider position.
    """
    if not scenario.assumptions:
        return None
    low = scenario.model_copy(
        update={"assumptions": {k: get_assumption(k).low for k in scenario.assumptions}}
    )
    high = scenario.model_copy(
        update={"assumptions": {k: get_assumption(k).high for k in scenario.assumptions}}
    )
    return low, high
