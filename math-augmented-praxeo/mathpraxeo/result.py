"""What every annex computation returns: a range, the assumptions it took, and its rung."""
from __future__ import annotations

from dataclasses import dataclass, field

from .interval import Interval

RUNGS = {
    "M0": "identity or arithmetic: exact given its inputs",
    "M1": "first-order, local: exact for small changes, given elasticity ranges",
}


@dataclass
class Result:
    name: str
    value: Interval
    rung: str
    assumptions: list[str] = field(default_factory=list)
    note: str = ""

    def __post_init__(self):
        if self.rung not in RUNGS:
            raise ValueError(f"unknown rung {self.rung}")


def check_sign(praxeological_sign: str, r: Result) -> str:
    """Compare the annex's range with the sign the praxeological analysis gave.

    The annex never overrides a sign. A contradiction means an input range is wrong
    (or the praxeological premise failed) and must be reported, not resolved here.
    """
    s = r.value.sign
    if praxeological_sign in ("ambiguous", "as_stated") or s == "ambiguous":
        return "indeterminate"
    return "agrees" if s == praxeological_sign else "contradicts"
