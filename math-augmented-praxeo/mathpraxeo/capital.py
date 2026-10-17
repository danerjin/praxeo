"""Arithmetic of price paths and of capitalization (rung M0).

Given growth rates (as ranges), the gap between a capped price and the market path
is arithmetic. Given a discount rate and an expected duration (as ranges), the value
of an asset that earns the capped price falls by the present value of the gaps
(CR-7c in the handbook: a lasting change in income is priced into the asset when
it is expected). Nothing here is estimated; every range is an input.
"""
from __future__ import annotations

from .interval import Interval
from .result import Result


def cap_gap_path(years: int, market_growth, cap_schedule: list[float]) -> list[Result]:
    """Gap between market and capped price in each year, in units of today's price.

    `cap_schedule` gives the allowed growth of the capped price in each year
    (e.g. [0, 0, 0, 0.02, 0.02] for a 3-year freeze then 2%); `market_growth` is a
    range for the counterfactual market growth per year.
    """
    if len(cap_schedule) < years:
        raise ValueError("cap_schedule shorter than years")
    g = Interval.of(market_growth)
    out, cap = [], 1.0
    for k in range(years):
        cap *= 1 + cap_schedule[k]
        gap = Interval((1 + g.lo) ** (k + 1) - cap, (1 + g.hi) ** (k + 1) - cap)
        out.append(Result(f"gap_year_{k + 1}", gap, "M0",
                          [f"market price grows by {g} a year", f"capped growth {cap_schedule[k]:.3g} in year {k + 1}"]))
    return out


def gap_share(gap: Result, market_growth, year: int) -> Interval:
    """The same gap as a share of that year's market price. The share rises with market growth,
    so its bounds are taken at the matching ends of the growth range."""
    g = Interval.of(market_growth)
    return Interval(gap.value.lo / (1 + g.lo) ** year, gap.value.hi / (1 + g.hi) ** year)


def capitalized_loss(gaps: list[Result], rate, duration_years) -> Result:
    """Present value of the yearly gaps, in units of today's annual income, over an expected duration.

    Monotone in every input: larger gaps, a lower discount rate and a longer
    expected duration all raise the loss, so the bounds come from the corners.
    """
    r = Interval.of(rate)
    d = Interval.of(duration_years)
    if r.lo <= -1:
        raise ValueError("discount rate must be above -100%")
    if d.hi > len(gaps):
        raise ValueError("duration longer than the gap path supplied")

    def pv(bound: str, rate_: float, dur: float) -> float:
        return sum(getattr(gaps[k].value, bound) / (1 + rate_) ** (k + 1) for k in range(int(dur)))

    return Result("capitalized_loss", Interval(pv("lo", r.hi, d.lo), pv("hi", r.lo, d.hi)), "M0",
                  [f"discount rate {r}", f"expected duration {d} years", "gaps as given"],
                  "Borne by owners when the policy became expected (CR-7c); later buyers pay the lower price.")


def present_value(stream, rate, years: int) -> Result:
    """Present value of a constant yearly amount (a range) for `years`, discounted at `rate` (a range).
    Gives the value of a license or quota (the yearly rent it earns) or of a lasting tax or subsidy (CR-7c)."""
    a, r = Interval.of(stream), Interval.of(rate)
    if r.lo <= -1:
        raise ValueError("discount rate must be above -100%")
    if a.lo < 0:
        raise ValueError("give the stream as a positive amount; sign it in the caller")

    def annuity(r_):
        return years if r_ == 0 else (1 - (1 + r_) ** -years) / r_

    return Result("present_value", Interval(a.lo * annuity(r.hi), a.hi * annuity(r.lo)), "M0",
                  [f"yearly amount {a}", f"discount rate {r}", f"{years} years"])
