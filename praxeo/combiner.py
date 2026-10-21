"""Effect combiner (CR-12): a declared table of comparisons between chains that run in opposite directions.

CR-12b: when chains reach the same actor class, variable and horizon in opposite directions, the combined sign is
`ambiguous` unless a premise establishes that one chain dominates (CR-12e). Each entry of COMPARISONS names

- the total's variable (and window, if it is signed for a timing window);
- the favoured chain and the opposed chain, each picked out by a subclass suffix of the total's actor (".keepers"),
  or by variable, window or item (the qualifier of one item of a variable, CR-12 0.8), or by "inverts" where the chain
  moves the total the other way (a fall in quality raises the price per unit of quality);
- the dominance premise: the atom of an estimated assumption that settles the sign for the favoured chain, or None
  where the handbook gives no premise, so that the total is `ambiguous` whenever both chains are reported.

A total is `ambiguous` unless the dominance premise has p >= 0.5. Only reported chains count: a chain that rests on an
assumption below the cut-off is not a chain here (CR-12 0.8, kind 2), so with one chain reported the total takes its
sign. Where the opposed chain's own sign is `ambiguous` (kind 3, or a sign that differs by reading), the total is
`ambiguous` unless the dominance premise covers it, which the premise is taken to do. A group consequence
(`at_least_one_*`) is never a chain (CR-12 1.1).

Two modes. `new` forms a separate total consequence (PC-21's keepers against the displaced, formed for their parent
class; the first months after the effective date; the landlords' resources; the quality-adjusted price). `in_place`
settles the favoured consequence itself against an opposing chain in another window: the capped price against the
announcement-window rush, which needs the dominance premise that the counterfactual price passes the raised base.

Every entry cites the handbook line it comes from. Where the handbook leaves a total ambiguous and gives no premise
(`dominance=None`) the combiner says so rather than inventing one.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

from .engine import CUTOFF
from .schema import Assumption, Consequence, HORIZON_ORDER


@dataclass(frozen=True)
class Chain:
    suffix: str = ""                  # appended to the total's actor class: ".keepers"
    variable: Optional[str] = None    # default: the comparison's variable
    window: Optional[str] = None
    item: Optional[str] = None
    inverts: bool = False             # the chain moves the total's variable the other way


@dataclass(frozen=True)
class Comparison:
    id: str
    variable: str                     # the total's variable
    favoured: Chain
    opposed: Chain
    dominance: Optional[str]          # assumption atom (without the component); None: the handbook gives no premise
    source: str                       # the handbook line the comparison comes from
    mode: str = "new"                 # "new" or "in_place"
    window: Optional[str] = None      # the total's window ("new" mode)
    horizon: Optional[tuple[str, ...]] = None  # the total's horizons; default: the union of the parts'


# The declared comparisons. The first four are formed as separate totals, the last two settle a capped price in place.
COMPARISONS: list[Comparison] = [
    Comparison("pc_21_relocation", "relocation_out_of_area",
               Chain(suffix=".keepers"), Chain(suffix=".displaced"), "keepers_dominate",
               "PC-21 (1.4): insiders who keep the unit leave the area less, those displaced leave more; the class total needs a premise on the share displaced"),
    Comparison("quality_adjusted_price", "quality_adjusted_price",
               Chain(variable="price_paid"), Chain(variable="quality_per_unit", inverts=True), None,
               "WE-001 section 7, tenants.controlled quality_adjusted_price: lower rent against lower quality; the handbook gives no dominance rule, so it is ambiguous",
               horizon=("medium", "long")),
    Comparison("landlords_resources", "resources_available_other_uses",
               Chain(item="rent_forgone"), Chain(item="key_money"), "enforced",
               "WE-001 section 7, landlords.controlled resources_available_other_uses (C-28): rent forgone against key money, dominance by A-2 (the cap is enforced against most landlords, so key money is confined to a minority)",
               horizon=("medium", "long")),
    Comparison("first_months_price", "price_paid",
               Chain(window=None), Chain(window="announcement"), None,
               "WE-001 C-21: the first months after the effective date; PC-3 (a fall) against RS-8 (the raised base), and the handbook gives no premise at this horizon (the size of the raises is a magnitude)",
               window="first_months", horizon=("short",)),
    Comparison("capped_price_vs_rush", "price_paid",
               Chain(window=None), Chain(window="announcement"), "counterfactual_catches_up",
               "WE-001 C-1: from the medium horizon the cap chain dominates the announcement-window raises by A-14 (the counterfactual price passes any raise within a lease cycle or two; CR-12e, empirical premise)",
               mode="in_place"),
    Comparison("sellers_price_vs_rush", "net_price_received",
               Chain(window=None), Chain(window="announcement"), "counterfactual_catches_up",
               "WE-001 C-27: the mirror of C-1 for the sellers, with the same premise A-14",
               mode="in_place"),
]


def _comp_of(c: Consequence) -> Optional[str]:
    """The component an assumption atom belongs to: 'enforced(c1)' -> 'c1'."""
    for a in c.assumptions:
        m = re.search(r"\((\w+)\)$", a)
        if m:
            return m.group(1)
    return None


def _find(consequences: list[Consequence], chain: Chain, actor: str, variable: str) -> list[Consequence]:
    want_var = chain.variable or variable
    return [c for c in consequences
            if not c.group and c.variable == want_var and c.actor_class == actor + chain.suffix
            and c.window == chain.window and c.item == chain.item]


def _push(c: Consequence, chain: Chain) -> str:
    if chain.inverts and c.sign in ("increase", "decrease"):
        return "decrease" if c.sign == "increase" else "increase"
    return c.sign


def _dominance(comp: Comparison, ref: Consequence, assumptions: dict[str, Assumption]) -> Optional[Assumption]:
    if comp.dominance is None:
        return None
    key = f"{comp.dominance}({_comp_of(ref)})"
    if key in assumptions:
        return assumptions[key]
    return next((a for k, a in assumptions.items() if k.startswith(comp.dominance + "(")), None)


def _settle(comp: Comparison, fav: Consequence, opp: Optional[Consequence], assumptions: dict[str, Assumption]):
    """The total's sign and the assumptions it rests on, for a favoured chain and the opposed chain if it is reported."""
    parts = [c for c in (fav, opp) if c is not None and c.reported]
    if not parts:
        return None
    used = sorted({a for c in parts for a in c.assumptions})
    if len(parts) == 1:
        return parts[0], parts, parts[0].sign, used
    f_sign, o_sign = _push(fav, comp.favoured), _push(opp, comp.opposed)
    dom = _dominance(comp, fav, assumptions)
    if f_sign == o_sign and f_sign != "ambiguous":
        return parts[0], parts, f_sign, used
    if dom is not None and dom.p >= CUTOFF:
        return parts[0], parts, f_sign, sorted(set(used) | {dom.id})
    return parts[0], parts, "ambiguous", used


def _parents(consequences: list[Consequence], comp: Comparison) -> list[str]:
    """The actor classes a comparison forms a total for: those with a consequence on the favoured chain."""
    chain = comp.favoured
    out: list[str] = []
    for c in consequences:
        if c.group or c.window != chain.window or c.item != chain.item or c.variable != (chain.variable or comp.variable):
            continue
        if chain.suffix and not c.actor_class.endswith(chain.suffix):
            continue
        parent = c.actor_class[: -len(chain.suffix)] if chain.suffix else c.actor_class
        if parent not in out:
            out.append(parent)
    return out


def combine(consequences: list[Consequence], assumptions: dict[str, Assumption]) -> list[Consequence]:
    out = list(consequences)
    next_id = len(consequences) + 1
    for comp in (c for c in COMPARISONS if c.mode == "new"):
        for parent in _parents(consequences, comp):
            fs = _find(consequences, comp.favoured, parent, comp.variable)
            os_ = _find(consequences, comp.opposed, parent, comp.variable)
            f = fs[0] if fs else None
            o = os_[0] if os_ else None
            # a subclass total (PC-21) may be formed from one subclass's chain; any other comparison needs both chains to exist
            if f is None or (o is None and not comp.favoured.suffix):
                continue
            settled = _settle(comp, f, o, assumptions)
            if settled is None:
                continue
            _, parts, sign, used = settled
            if len(parts) == 1:
                sign = _push(parts[0], comp.favoured if parts[0] is f else comp.opposed)
            horizon = list(comp.horizon) if comp.horizon else sorted({h for c in parts for h in c.horizon}, key=HORIZON_ORDER.get)
            out.append(Consequence(
                id=f"C-{next_id}",
                actor_class=parent,
                variable=comp.variable,
                window=comp.window,
                sign=sign,
                horizon=horizon,
                visibility="invisible",
                tier="B",
                derivation=[s for c in parts for s in c.derivation],
                assumption_sets=[used],
                assumptions=used,
                reported=all(assumptions[a].p >= CUTOFF for a in used),
                combines=[c.id for c in parts],
                comparison=comp.id,
            ))
            next_id += 1
    # in_place: settle the favoured consequence against its opposing chain in another window
    for comp in (c for c in COMPARISONS if c.mode == "in_place"):
        for i, f in enumerate(out):
            if f.window != comp.favoured.window or f.item != comp.favoured.item or f.group or f.comparison:
                continue
            if f.variable != comp.variable or not f.reported:
                continue
            opposed = _find(consequences, comp.opposed, f.actor_class, comp.variable)
            if not opposed or not opposed[0].reported:
                continue
            o = opposed[0]
            _, parts, sign, used = _settle(comp, f, o, assumptions)
            extra = set(used) - set(f.assumptions) - set(o.assumptions)  # the dominance premise, if it decided the sign
            if sign != "ambiguous" and extra:
                # the dominance premise settles the sign for the favoured chain: it rests on that chain and the premise,
                # not on the premises of the chain it dominates (WE-001 C-1: A-1, A-2, A-14)
                used = sorted(set(f.assumptions) | extra)
            sets = [used] if sign == "ambiguous" else [sorted(set(x) | extra) for x in f.assumption_sets]
            out[i] = f.model_copy(update=dict(
                sign=sign, assumptions=used, assumption_sets=sets,
                reported=all(assumptions[a].p >= CUTOFF for a in used),
                combines=[o.id], comparison=comp.id))
    return out
