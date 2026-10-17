"""Closed intervals: every input and every output of the annex is a range, not a point."""
from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Interval:
    lo: float
    hi: float

    def __post_init__(self):
        if self.lo > self.hi:
            raise ValueError(f"empty interval [{self.lo}, {self.hi}]")

    @classmethod
    def point(cls, x: float) -> "Interval":
        return cls(x, x)

    @classmethod
    def of(cls, x) -> "Interval":
        return x if isinstance(x, Interval) else cls.point(float(x))

    def __add__(self, o):
        o = Interval.of(o)
        return Interval(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.hi, -self.lo)

    def __sub__(self, o):
        return self + (-Interval.of(o))

    def __rsub__(self, o):
        return Interval.of(o) - self

    def __mul__(self, o):
        o = Interval.of(o)
        c = [self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi]
        return Interval(min(c), max(c))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = Interval.of(o)
        if o.lo <= 0 <= o.hi:
            raise ZeroDivisionError(f"divisor interval {o} contains zero")
        return self * Interval(1 / o.hi, 1 / o.lo)

    def __rtruediv__(self, o):
        return Interval.of(o) / self

    def contains(self, x: float) -> bool:
        return self.lo <= x <= self.hi

    @property
    def sign(self) -> str:
        """The sign the whole interval agrees on, in the handbook's vocabulary."""
        if self.lo > 0:
            return "increase"
        if self.hi < 0:
            return "decrease"
        if self.lo == self.hi == 0:
            return "no_change"
        return "ambiguous"

    def __repr__(self):
        return f"[{self.lo:.4g}, {self.hi:.4g}]"


def corners(f: Callable[..., float], *args: Interval) -> Interval:
    """Range of f over a box, for f monotone in each argument separately (checked at the corners only).

    Exact for functions monotone in each argument on the box; the callers below use it only there.
    """
    vals = [f(*c) for c in itertools.product(*[(a.lo, a.hi) for a in args])]
    return Interval(min(vals), max(vals))
