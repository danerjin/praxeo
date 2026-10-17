"""Accounting identities and plain arithmetic (rung M0).

Each holds by definition or by counting; the only inputs are ranges the analyst
supplies. None of them says what causes what: that is the praxeological chain's job.
"""
from __future__ import annotations

from .interval import Interval, corners
from .result import Result
from .rules import derives


@derives('MR-2')
def wait_time(queue_length, throughput) -> Result:
    """Little's law, L = lambda * W: average wait = people waiting / people served per unit time.

    Holds for any stable queue, whatever the order of service. Use for PC-2 (rationing by waiting).
    """
    L, lam = Interval.of(queue_length), Interval.of(throughput)
    if lam.lo <= 0:
        raise ValueError("throughput must be positive")
    return Result("wait_time", L / lam, "M0",
                  [f"queue length {L}", f"served per period {lam}", "queue stable (arrivals equal departures on average)"])


@derives('MR-2')
def expected_penalty(p_detect, fine) -> Result:
    """Expected cost of breaking a rule: probability of detection times the penalty.

    Compare with the gain from evasion to judge the enforcement premise (an input to `enforcement` assumptions);
    risk attitudes differ, so it informs a premise and does not decide one.
    """
    p, f = Interval.of(p_detect), Interval.of(fine)
    if p.lo < 0 or p.hi > 1:
        raise ValueError("probability outside [0, 1]")
    return Result("expected_penalty", p * f, "M0", [f"detection probability {p}", f"penalty {f}"],
                  "Informs the enforcement premise; whether actors evade depends on their own ranking (CR-4).")


@derives('MR-2')
def inflation_tax(inflation, real_balances) -> Result:
    """Purchasing power lost by holders of money balances when prices rise by `inflation`:
    balances * inflation / (1 + inflation). Pairs with the equation of exchange and with Cantillon effects:
    the loss falls on holders, the gain on the first receivers of new money."""
    pi, b = Interval.of(inflation), Interval.of(real_balances)
    v = corners(lambda p_, b_: b_ * p_ / (1 + p_), pi, b)
    return Result("inflation_tax_on_holders", v, "M0", [f"price level rises by {pi}", f"money balances held {b}"])


@derives('MR-3')
def real_rate(nominal, inflation) -> Result:
    """Fisher relation as a definition: (1 + nominal) = (1 + real)(1 + inflation). Exact, not the approximation."""
    i, pi = Interval.of(nominal), Interval.of(inflation)
    v = corners(lambda i_, p_: (1 + i_) / (1 + p_) - 1, i, pi)
    return Result("real_rate", v, "M0", [f"nominal rate {i}", f"inflation {pi}"])


@derives('MR-2', 'MR-3')
def debt_path(debt_ratio, rate, growth, primary_balance, years: int) -> Result:
    """Government debt arithmetic: d' = d (1 + r) / (1 + g) - s, with d debt / income, s the primary surplus
    as a share of income. An identity of the budget; r, g and s are ranges. Relevant to OC-8 and OC-9."""
    d, r, g, s = (Interval.of(x) for x in (debt_ratio, rate, growth, primary_balance))

    def step(d_, r_, g_, s_):
        for _ in range(years):
            d_ = d_ * (1 + r_) / (1 + g_) - s_
        return d_

    v = corners(step, d, r, g, s)
    return Result(f"debt_ratio_after_{years}_years", v, "M0",
                  [f"initial debt/income {d}", f"interest rate {r}", f"income growth {g}", f"primary surplus/income {s}"])


@derives('MR-2', 'MR-3')
def stock_path(stock, depreciation, additions, years: int) -> Result:
    """Stock-flow arithmetic: K' = K (1 - depreciation) + additions. For TS-1 and PC-5: with new building
    stopped, a durable stock shrinks only at the depreciation rate."""
    k, dep, add = Interval.of(stock), Interval.of(depreciation), Interval.of(additions)

    def step(k_, d_, a_):
        for _ in range(years):
            k_ = k_ * (1 - d_) + a_
        return k_

    v = corners(step, k, dep, add)
    return Result(f"stock_after_{years}_years", v, "M0",
                  [f"initial stock {k}", f"depreciation {dep} a year", f"additions {add} a year"])


@derives('MR-2')
def sectoral_balance(private_surplus=None, government_surplus=None, foreign_surplus=None) -> Result:
    """National accounts identity: private (S - I) + government (T - G) + rest of world (M - X) = 0.
    Give any two (as shares of income); returns the third. Says nothing about which one adjusts."""
    given = {"private": private_surplus, "government": government_surplus, "foreign": foreign_surplus}
    missing = [k for k, v in given.items() if v is None]
    if len(missing) != 1:
        raise ValueError("give exactly two of the three balances")
    known = [Interval.of(v) for v in given.values() if v is not None]
    return Result(f"{missing[0]}_balance", -(known[0] + known[1]), "M0",
                  [f"{k} balance {Interval.of(v)}" for k, v in given.items() if v is not None],
                  "Identity only: which balance moves when another changes is a praxeological (or empirical) question.")


@derives('MR-3')
def doubling_time(growth) -> Result:
    """Years for a quantity to double at a constant growth rate: ln 2 / ln(1 + g)."""
    import math
    g = Interval.of(growth)
    if g.lo <= 0:
        raise ValueError("growth must be positive")
    v = corners(lambda g_: math.log(2) / math.log(1 + g_), g)
    return Result("doubling_time_years", v, "M0", [f"growth {g} a year"])
