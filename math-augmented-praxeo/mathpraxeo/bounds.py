"""Bounds: results the annex adopts only as upper or lower limits, never as point estimates.

Each function returns a range whose ends are limits set by arbitrage, by what buyers will pay, or by what
sellers must be compensated for. The range says where the quantity must lie if the stated conditions
hold. It never says where in the range it lies.
"""
from __future__ import annotations

from .capital import present_value
from .interval import Interval, corners
from .result import Result


def black_market_premium(gap, ed, es, seller_penalty, buyer_penalty) -> Result:
    """Price on the illegal market under a binding ceiling, as a premium over the ceiling, in shares of the
    clearing price (PC-6, RS-3).

    - Lower limit: sellers must at least recover their expected penalty per unit (risk-neutral; risk-averse
      sellers ask more, so the true lower limit is if anything higher).
    - Upper limit: what the marginal buyer will pay for the quantity still offered, less the buyer's own
      expected penalty. First order, the quantity offered at the ceiling is Q*(1 - es * gap), and buyers
      value that quantity at p*(1 + es * gap / |ed|).

    If the lower limit is above the upper, no illegal trade pays at the margin; the range is reported empty
    as [0, 0] with a note. That means the premise of imperfect enforcement fails (PC-6's Assumes).
    The ceiling sits at (1 - gap) of the clearing price, so the premium is measured from there.
    """
    g, ed, es, sp, bp = (Interval.of(x) for x in (gap, ed, es, seller_penalty, buyer_penalty))
    if ed.hi >= 0:
        raise ValueError("demand elasticity must be negative here (the buyers' price at the shrunken quantity is undefined at 0)")
    lo = sp  # premium over the ceiling the seller needs
    hi = corners(lambda g_, d, s, b: (1 + s * g_ / abs(d)) - (1 - g_) - b, g, ed, es, bp)
    assum = [f"ceiling {g} below clearing", f"demand elasticity {ed}", f"supply elasticity {es}",
             f"sellers' expected penalty per unit {sp}", f"buyers' expected penalty per unit {bp}",
             "first order; risk-neutral sellers for the lower limit"]
    if lo.lo > hi.hi:
        return Result("black_market_premium", Interval(0.0, 0.0), "M1", assum,
                      "No illegal trade pays at the margin: sellers' expected penalty exceeds what buyers will pay "
                      "above the ceiling. The premise of imperfect enforcement fails under these inputs.")
    return Result("black_market_premium", Interval(max(lo.lo, 0.0), hi.hi), "M1", assum,
                  "Bound only: the illegal premium lies in this range if illegal trade happens at all.")


def hotelling_gap(net_price_growth, rate, tax_growth=0.0, tax_share=0.0) -> Result:
    """No-arbitrage over time for an exhaustible resource: owners leave a unit in the ground only if its
    net-of-tax price is expected to grow at least as fast as the rate of interest.

    Returns (expected growth of the net-of-tax price) - (interest rate). Negative: extraction is brought
    forward, and the stock in the ground falls sooner. Positive: extraction is deferred. A per-unit tax that
    is a share `tax_share` of the net price and grows at `tax_growth` lowers net-of-tax growth by about
    tax_share * (tax_growth - net_price_growth) / (1 - tax_share), first order.

    Bound only. It holds where owners expect to keep the resource (secure property) and can choose when to
    extract. It gives the direction of the timing pressure and its size against r, not an extraction path.
    """
    gn, r, tg, ts = (Interval.of(x) for x in (net_price_growth, rate, tax_growth, tax_share))
    if ts.hi >= 1 or ts.lo < 0:
        raise ValueError("tax share must be in [0, 1)")
    v = corners(lambda g, r_, t_g, t_s: g - t_s * (t_g - g) / (1 - t_s) - r_, gn, r, tg, ts)
    return Result("net_price_growth_minus_rate", v, "M1",
                  [f"expected net price growth {gn}", f"interest rate {r}", f"tax growth {tg}", f"tax share of net price {ts}",
                   "owners expect to keep the resource; first order"],
                  "Negative: extraction brought forward (CR-4, x: extract now, y: later). Positive: deferred.")


def rent_seeking_ceiling(rent_per_year, rate, years: int) -> Result:
    """Upper limit on total spending to obtain or keep a privilege: the present value of the privilege to all
    contenders together (RS-7). Contenders who do not overpay in total spend no more than the prize; how
    much less is not determined. The lower limit is zero."""
    pv = present_value(rent_per_year, rate, years)
    return Result("lobbying_spending_bound", Interval(0.0, pv.value.hi), "M1",
                  pv.assumptions + ["contenders together do not spend more than the prize"],
                  "Bound only: total spending lies between nothing and the value of the privilege.")


def covered_interest_parity(domestic_rate, foreign_rate, cost_band=0.0) -> Result:
    """Arbitrage limit on the forward exchange rate: forward / spot = (1 + i_dom) / (1 + i_for), up to a band
    for transaction costs and capital controls. Returns the forward premium (forward / spot - 1) as a range.
    Relevant where a policy caps interest rates or restricts capital movements (TX-8)."""
    d, f, c = (Interval.of(x) for x in (domestic_rate, foreign_rate, cost_band))
    if c.lo < 0:
        raise ValueError("cost band must be non-negative")
    v = corners(lambda d_, f_, c_: (1 + d_) / (1 + f_) * (1 - c_) - 1, d, f, c)
    w = corners(lambda d_, f_, c_: (1 + d_) / (1 + f_) * (1 + c_) - 1, d, f, c)
    return Result("forward_premium", Interval(min(v.lo, w.lo), max(v.hi, w.hi)), "M1",
                  [f"domestic rate {d}", f"foreign rate {f}", f"cost and control band {c}", "arbitrage open within the band"],
                  "Bound only: outside this range a riskless arbitrage profit would exist.")
