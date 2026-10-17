"""Effect combiner (CR-12): totals over subclasses whose chains run in opposite directions.

PC-21 (1.4): insiders who keep the unit leave the area less; insiders displaced by
conversion leave it more. The total for the class is a CR-12 comparison: `ambiguous`
unless a dominance premise (estimated like any other assumption) says which chain
is larger. Where only one subclass's consequence is reported, the total takes its sign.
"""
from __future__ import annotations

import math

from .engine import CUTOFF
from .schema import Assumption, Consequence

# (variable, subclass suffix whose chain the dominance premise favours, opposing suffix, dominance atom prefix)
TOTALS = [
    ("relocation_out_of_area", ".keepers", ".displaced", "keepers_dominate"),
]


def combine(consequences: list[Consequence], assumptions: dict[str, Assumption]) -> list[Consequence]:
    out = list(consequences)
    next_id = len(consequences) + 1
    for variable, fav, opp, atom_prefix in TOTALS:
        favs = [c for c in consequences if c.variable == variable and c.actor_class.endswith(fav)]
        for f in favs:
            parent = f.actor_class[: -len(fav)]
            o = next((c for c in consequences if c.variable == variable and c.actor_class == parent + opp), None)
            parts = [c for c in (f, o) if c is not None and c.reported]
            if not parts:
                continue
            dom = next((a for k, a in assumptions.items() if k.startswith(atom_prefix + "(")), None)
            used = sorted({a for c in parts for a in c.assumptions})
            if len(parts) == 1:
                sign = parts[0].sign
            elif parts[0].sign == parts[1].sign:
                sign = parts[0].sign
            elif dom is not None and dom.p >= CUTOFF:
                sign = f.sign
                used = sorted(set(used) | {dom.id})
            else:
                sign = "ambiguous"
            out.append(Consequence(
                id=f"C-{next_id}",
                actor_class=parent,
                variable=variable,
                sign=sign,
                horizon=sorted({h for c in parts for h in c.horizon}, key=["short", "medium", "long"].index),
                visibility="invisible",
                tier="B",
                derivation=[s for c in parts for s in c.derivation],
                assumption_sets=[used],
                assumptions=used,
                reported=all(assumptions[a].p >= CUTOFF for a in used),
                combines=[c.id for c in parts],
            ))
            next_id += 1
    return out
