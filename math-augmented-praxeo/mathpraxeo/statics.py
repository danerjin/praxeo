"""First-order comparative statics with elasticity ranges (rung M1).

Only local linearity is assumed: for changes small enough that the elasticity is
roughly constant over them, %dQ = elasticity * %dP. No curve is fitted, no functional
form is chosen, and the elasticities are ranges the analyst must source. Signs come
from the laws of demand and supply (already praxeological: LW-3, LW-4); the annex
adds only the size, as a range.
"""
from __future__ import annotations

from .interval import Interval, corners
from .result import Result


FIRST_ORDER_LIMIT = 0.15  # beyond a 15% price gap, a constant elasticity is a strong assumption


def _strain(gap: Interval) -> str:
    return (f"First order is strained: the gap reaches {gap.hi:.0%}, beyond {FIRST_ORDER_LIMIT:.0%}; "
            "treat the range as indicative only.") if gap.hi > FIRST_ORDER_LIMIT else ""


def _check(ed: Interval, es: Interval):
    if ed.hi > 0:
        raise ValueError(f"demand elasticity must be <= 0 (law of demand), got {ed}")
    if es.lo < 0:
        raise ValueError(f"supply elasticity must be >= 0, got {es}")


def ceiling_shortage(gap, ed, es) -> Result:
    """Excess demand at a ceiling a fraction `gap` below the clearing price, as a share of the clearing quantity.

    shortage / Q* ~ (|ed| + es) * gap, for small gap.
    """
    gap, ed, es = Interval.of(gap), Interval.of(ed), Interval.of(es)
    _check(ed, es)
    v = corners(lambda g, d, s: (abs(d) + s) * g, gap, ed, es)
    return Result("ceiling_shortage_share", v, "M1",
                  [f"ceiling {gap} below the clearing price", f"demand elasticity {ed}", f"supply elasticity {es}",
                   "elasticities roughly constant over the gap (first order)"], _strain(gap))


def ceiling_quantity_supplied(gap, es) -> Result:
    """Fall in quantity supplied when the price sellers get is held a fraction `gap` below clearing."""
    gap, es = Interval.of(gap), Interval.of(es)
    _check(Interval.point(0), es)
    v = corners(lambda g, s: -s * g, gap, es)
    return Result("quantity_supplied_change", v, "M1",
                  [f"price held {gap} below clearing", f"supply elasticity {es} at the relevant horizon"], _strain(gap))


def tax_incidence(t, ed, es) -> tuple[Result, Result]:
    """A per-unit tax of t (as a share of the price): changes in the buyers' price and the sellers' net price.

    Buyers bear es / (es + |ed|) of it, sellers |ed| / (es + |ed|), to first order.
    Undefined when both elasticities are zero (no quantity response on either side).
    """
    t, ed, es = Interval.of(t), Interval.of(ed), Interval.of(es)
    _check(ed, es)
    if es.hi + abs(ed.hi) == 0 and es.lo + abs(ed.lo) == 0:
        raise ValueError("incidence undefined when both elasticities are zero")

    def share_buyers(d, s):
        tot = abs(d) + s
        return 0.5 if tot == 0 else s / tot

    assum = [f"tax {t} of the price", f"demand elasticity {ed}", f"supply elasticity {es}", "first order"]
    buyers = corners(lambda t_, d, s: t_ * share_buyers(d, s), t, ed, es)
    sellers = corners(lambda t_, d, s: -t_ * (1 - share_buyers(d, s)), t, ed, es)
    return (Result("buyers_price_change", buyers, "M1", assum),
            Result("sellers_net_price_change", sellers, "M1", assum))
