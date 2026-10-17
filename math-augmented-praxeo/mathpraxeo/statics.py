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
from .rules import derives


FIRST_ORDER_LIMIT = 0.15  # beyond a 15% price gap, a constant elasticity is a strong assumption


def _strain(gap: Interval) -> str:
    return (f"First order is strained: the gap reaches {gap.hi:.0%}, beyond {FIRST_ORDER_LIMIT:.0%}; "
            "treat the range as indicative only.") if gap.hi > FIRST_ORDER_LIMIT else ""


def _check(ed: Interval, es: Interval):
    if ed.hi > 0:
        raise ValueError(f"demand elasticity must be <= 0 (law of demand), got {ed}")
    if es.lo < 0:
        raise ValueError(f"supply elasticity must be >= 0, got {es}")


@derives('MR-4')
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


@derives('MR-4')
def ceiling_quantity_supplied(gap, es) -> Result:
    """Fall in quantity supplied when the price sellers get is held a fraction `gap` below clearing."""
    gap, es = Interval.of(gap), Interval.of(es)
    _check(Interval.point(0), es)
    v = corners(lambda g, s: -s * g, gap, es)
    return Result("quantity_supplied_change", v, "M1",
                  [f"price held {gap} below clearing", f"supply elasticity {es} at the relevant horizon"], _strain(gap))


@derives('MR-5')
def tax_incidence(t, ed, es) -> tuple[Result, Result]:
    """A per-unit tax of t (as a share of the price): changes in the buyers' price and the sellers' net price.

    Buyers bear the share es / (es + |ed|), sellers the rest, to first order. The share rises with es and
    with ed (toward zero), so its range comes from the corners (es.lo, ed.lo) and (es.hi, ed.hi). Where the
    ranges allow no quantity response on either side (es can be 0 and ed can be 0), incidence is
    undetermined there, and the share is reported as the full range [0, 1]: no split is assumed.
    """
    t, ed, es = Interval.of(t), Interval.of(ed), Interval.of(es)
    _check(ed, es)
    note = ""
    if es.lo == 0 and ed.hi == 0:
        share = Interval(0.0, 1.0)
        note = ("Incidence undetermined: the ranges allow no quantity response on either side, so the buyers' "
                "share is reported as anything from none to all of the tax.")
    else:
        share = Interval(es.lo / (es.lo + abs(ed.lo)), es.hi / (es.hi + abs(ed.hi)))
    assum = [f"tax {t} of the price", f"demand elasticity {ed}", f"supply elasticity {es}", "first order"]
    buyers = t * share
    sellers = -(t * (1 - share))
    return (Result("buyers_price_change", buyers, "M1", assum, note),
            Result("sellers_net_price_change", sellers, "M1", assum, note))


@derives('MR-5')
def equilibrium_shift(demand_shift, supply_shift, ed, es) -> tuple[Result, Result]:
    """Supply-and-demand intersection, first order. A demand shift `a` and a supply shift `b` are the
    proportional changes in quantity demanded and supplied at the old price. Then

        %dP = (a - b) / (es - ed),     %dQ = (es * a - ed * b) / (es - ed).

    The direction of each is already praxeological (LW-3, LW-4); the annex gives the size.
    """
    a, b, ed, es = (Interval.of(x) for x in (demand_shift, supply_shift, ed, es))
    _check(ed, es)
    if es.lo - ed.hi <= 0:
        raise ValueError("price change undefined when both elasticities are zero")
    assum = [f"demand shift {a} at the old price", f"supply shift {b} at the old price",
             f"demand elasticity {ed}", f"supply elasticity {es}", "first order"]
    dp = corners(lambda a_, b_, d, s: (a_ - b_) / (s - d), a, b, ed, es)
    dq = _extremes(lambda a_, b_, d, s: (s * a_ - d * b_) / (s - d), a, b, ed, es)
    return Result("price_change", dp, "M1", assum), Result("quantity_change", dq, "M1", assum)


def _extremes(f, *args: Interval, steps: int = 6) -> Interval:
    """Range over a grid that includes the corners, for functions not monotone in every argument."""
    import itertools
    grids = [[a.lo + (a.hi - a.lo) * k / steps for k in range(steps + 1)] for a in args]
    vals = [f(*p) for p in itertools.product(*grids)]
    return Interval(min(vals), max(vals))


@derives('MR-4')
def floor_surplus(gap, ed, es) -> Result:
    """Excess supply at a floor a fraction `gap` above the clearing price, as a share of the clearing quantity
    (a minimum wage: unemployment among those whose labor the floor binds on). (|ed| + es) * gap, first order."""
    gap, ed, es = Interval.of(gap), Interval.of(ed), Interval.of(es)
    _check(ed, es)
    v = corners(lambda g, d, s: (abs(d) + s) * g, gap, ed, es)
    return Result("floor_surplus_share", v, "M1",
                  [f"floor {gap} above the clearing price", f"demand elasticity {ed}", f"supply elasticity {es}", "first order"],
                  _strain(gap))


@derives('MR-4', 'MR-5')
def quantity_under_wedge(t, ed, es) -> Result:
    """Fall in quantity traded when a wedge t (a tax, or the cost of complying) separates buyers' and sellers' prices:
    %dQ = - t * es * |ed| / (es + |ed|). The exchanges that no longer happen (CR-5a), counted, not valued."""
    t, ed, es = Interval.of(t), Interval.of(ed), Interval.of(es)
    _check(ed, es)
    v = corners(lambda t_, d, s: 0.0 if abs(d) + s == 0 else -t_ * s * abs(d) / (s + abs(d)), t, ed, es)
    return Result("quantity_traded_change", v, "M1",
                  [f"wedge {t} of the price", f"demand elasticity {ed}", f"supply elasticity {es}", "first order"],
                  "Counts the exchanges forgone. Their value to the parties is ordinal and is not summed in money here.")


@derives('MR-5')
def subsidy_incidence(s, ed, es) -> tuple[Result, Result]:
    """A per-unit subsidy is a negative tax: buyers' price falls by s * es / (es + |ed|), sellers' net price rises
    by the rest. Who gains how much of it, first order."""
    buyers, sellers = tax_incidence(s, ed, es)
    return (Result("buyers_price_change", -buyers.value, "M1", buyers.assumptions, buyers.note),
            Result("sellers_net_price_change", -sellers.value, "M1", sellers.assumptions, sellers.note))


@derives('MR-2', 'MR-4', 'MR-6')
def tariff(t, import_share, ed, es_domestic, pass_through=(1.0, 1.0)) -> dict[str, Result]:
    """Ad valorem tariff t on a good partly imported (import share m of use).

    Domestic price rises by pass_through * t (1 for a small buyer on the world market; less if foreign
    sellers absorb part: a range). Domestic output rises by es * %dP; use falls by |ed| * %dP; imports,
    the difference, fall by (|ed| + es (1 - m)) / m * %dP. First order.
    """
    t, m, ed, es, k = (Interval.of(x) for x in (t, import_share, ed, es_domestic, Interval(*pass_through)))
    _check(ed, es)
    if m.lo <= 0 or m.hi > 1:
        raise ValueError("import share must be in (0, 1]")
    dp = t * k
    assum = [f"tariff {t}", f"import share {m}", f"demand elasticity {ed}", f"domestic supply elasticity {es}",
             f"pass-through to the domestic price {k}", "first order"]
    return {
        "domestic_price": Result("domestic_price_change", dp, "M1", assum),
        "domestic_output": Result("domestic_output_change", es * dp, "M1", assum),
        "use": Result("use_change", ed * dp, "M1", assum),
        "imports": Result("imports_change",
                          _extremes(lambda p_, m_, d, s: -(abs(d) + s * (1 - m_)) / m_ * p_, dp, m, ed, es),
                          "M1", assum, _strain(dp)),
    }


@derives('MR-2')
def quota_rent(price_gap, quota_quantity) -> Result:
    """Yearly value of the right to sell under a binding quota: the gap between the domestic and the world (or
    marginal-cost) price times the quantity allowed. Arithmetic once the gap is known (M0 given the gap)."""
    g, q = Interval.of(price_gap), Interval.of(quota_quantity)
    return Result("quota_rent_per_year", g * q, "M0", [f"price gap {g} per unit", f"quota {q} units a year"],
                  "Capitalize with capital.present_value for the value of a license (CR-7c).")


@derives('MR-2', 'MR-4')
def spending_change(price_change, ed) -> Result:
    """Change in buyers' total spending on a good when its price changes, first order: (1 + ed) * %dP.
    Its sign turns on whether |ed| is above 1: the case CR-4's means exception needs."""
    dp, ed = Interval.of(price_change), Interval.of(ed)
    _check(ed, Interval.point(0))
    v = corners(lambda p_, d: (1 + d) * p_, dp, ed)
    return Result("spending_change", v, "M1", [f"price change {dp}", f"demand elasticity {ed}", "first order"])


@derives('MR-6')
def cost_pass_through(input_price_change, cost_share) -> Result:
    """Upper bound on the output price change from an input price change: cost share * input change.
    The bound holds with full pass-through; less elastic output supply passes through less, so the
    range is [0, share * change] for an increase. Use for RS-14 and PC-12 (costs passed up or down a chain)."""
    dp, s = Interval.of(input_price_change), Interval.of(cost_share)
    if s.lo < 0 or s.hi > 1:
        raise ValueError("cost share outside [0, 1]")
    full = dp * s
    v = Interval(min(0.0, full.lo), max(0.0, full.hi))
    return Result("output_price_change_bound", v, "M1",
                  [f"input price change {dp}", f"cost share {s}", "first order; between no and full pass-through"])


@derives('MR-2', 'MR-4')
def revenue_change(t0, t1, base_elasticity) -> Result:
    """Revenue R = t * B when the rate moves from t0 to t1 and the base responds to the net-of-tax rate (1 - t)
    with elasticity e (a range): %dB = e * %d(1 - t), first order. The revenue side of OC-1 and TX-2."""
    t0, t1, e = Interval.of(t0), Interval.of(t1), Interval.of(base_elasticity)
    if t0.lo <= 0 or t1.hi >= 1:
        raise ValueError("rates must be in (0, 1)")
    v = corners(lambda a, b, e_: (b / a) * (1 + e_ * ((1 - b) / (1 - a) - 1)) - 1, t0, t1, e)
    return Result("revenue_change", v, "M1", [f"rate from {t0} to {t1}", f"base elasticity {e} to the net-of-tax rate", "first order"],
                  _strain(Interval.of(abs((t1.hi - t0.lo)) / max(1 - t0.hi, 1e-9))))
