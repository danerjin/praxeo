"""The math core rules (MATH_CORE_RULES.md) as data, and the decorator that records each function's derivation.

Every public function in the annex and every annex handler names the rules it is derived from, as every
handbook pattern names its core rules. A method that cannot name them does not belong in the annex.
"""
from __future__ import annotations

from typing import Callable

MATH_RULES = {
    "MR-1": "Ranges: every quantity is a set of possible values; results are the full set the inputs allow",
    "MR-2": "Identities and conservation: over a closed set of accounts, flows balance and definitions hold",
    "MR-3": "Compounding and discounting: values over time multiply by growth factors; future amounts are discounted",
    "MR-4": "First-order response: for small changes, %dQ = elasticity x %dP, elasticity signed by LW-3/LW-4, sized by a sourced range",
    "MR-5": "Clearing as a tendency: the price move that would remove an excess created by shifts, sized by the elasticities",
    "MR-6": "No arbitrage: where actors can switch between options, the gap in yield cannot stay above the cost of switching",
    "MR-7": "Composition of magnitudes: opposing chains are ranked only when their ranges are disjoint; only M0 on case figures settles",
}

# the praxeological core rule each math rule is the quantitative counterpart of (None: governs the method itself)
COUNTERPART = {"MR-1": None, "MR-2": "CR-8", "MR-3": "CR-10, CR-7c", "MR-4": "CR-4", "MR-5": "CR-6",
               "MR-6": "CR-7, CR-4", "MR-7": "CR-12"}


def derives(*rules: str) -> Callable:
    """Record the math rules a function is derived from (MR-1 is implied everywhere and need not be named)."""
    unknown = [r for r in rules if r not in MATH_RULES]
    if unknown or not rules:
        raise ValueError(f"unknown or missing math rules: {unknown or 'none given'}")

    def mark(fn: Callable) -> Callable:
        fn.__math_rules__ = tuple(rules)
        return fn
    return mark
