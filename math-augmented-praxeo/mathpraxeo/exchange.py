"""The equation of exchange, M V = P Y, used as an identity (rung M0).

In growth factors it holds exactly: (1 + p) = (1 + m)(1 + v) / (1 + y), where m, v, y, p
are the proportional changes in money, velocity (spending per unit of money), real
output and the price level. As an identity it says nothing about causes. The
quantity *theory* adds empirical claims (that v and y do not move with m), which here
enter only as ranges the analyst supplies.

Praxeological caveat (Mises, TMC Part II ch. 8; HA ch. XVII §4): P is an average.
New money reaches some people first, so prices do not rise together and relative
prices change on the way (Cantillon effects). The identity bounds the average; the
praxeological chain says who gains and who loses.
"""
from __future__ import annotations

from .interval import Interval, corners
from .result import Result


def price_level_change(m, v, y) -> Result:
    m, v, y = Interval.of(m), Interval.of(v), Interval.of(y)
    p = corners(lambda m_, v_, y_: (1 + m_) * (1 + v_) / (1 + y_) - 1, m, v, y)
    return Result(
        "price_level_change", p, "M0",
        [f"money grows by {m}", f"velocity changes by {v}", f"real output changes by {y}"],
        "Average over all goods; Cantillon effects mean individual prices move at different times and by different amounts.",
    )


def implied_velocity_change(m, p, y) -> Result:
    """Given observed m, p and y, the v that makes the identity hold (for checking stated ranges)."""
    m, p, y = Interval.of(m), Interval.of(p), Interval.of(y)
    v = corners(lambda m_, p_, y_: (1 + p_) * (1 + y_) / (1 + m_) - 1, m, p, y)
    return Result("implied_velocity_change", v, "M0", [f"m = {m}", f"p = {p}", f"y = {y}"])
