"""The annex pass: attach sizes to a praxeological run without changing it.

Dependency runs one way: this module reads `praxeo` output; nothing in `praxeo`
or `handbook` imports the annex.

Three operations, each with a guard:

- `annex_pass` attaches an annex `Result` and its sign check to every reported
  consequence whose variable has a handler. It never changes a consequence: it
  returns new records beside the prediction and checks that the prediction is
  unchanged.
- `premise_evidence` turns an annex result into evidence for a CR-12 dominance
  premise. It proposes a probability with its source. It never writes the premise's
  p; a decider (LLM, human or Jev) must accept it, and the source is logged.
- `settle_by_arithmetic` lets a result settle a CR-12 comparison directly, as
  CR-12e (0.8) allows for "arithmetic where the case gives the figures". Only
  rung M0 results computed from the case's own figures may do this. An M1 result,
  or an M0 result on illustrative or external ranges, raises `GuardError`.
"""
from __future__ import annotations

import copy
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable

from .capital import cap_gap_path, gap_share
from .interval import Interval
from .result import Result, check_sign
from .statics import ceiling_quantity_supplied, ceiling_shortage


class GuardError(Exception):
    """An annex result tried to do what only praxeology (or the case's own arithmetic) may do."""


@dataclass
class AnnexInputs:
    """Ranges for one case. Every range names its source; `from_case` is True only for figures in the
    case record itself (not illustrative, not from outside studies)."""
    values: dict[str, Interval]
    sources: dict[str, str]
    from_case: dict[str, bool]

    @classmethod
    def load(cls, path: Path) -> "AnnexInputs":
        raw = json.loads(Path(path).read_text())
        vals, srcs, fc = {}, {}, {}
        for k, v in raw.items():
            if k.startswith("_"):
                continue
            vals[k] = Interval.of(v["value"])
            srcs[k] = v["source"]
            fc[k] = bool(v.get("from_case", False))
        return cls(vals, srcs, fc)

    def all_from_case(self, keys: list[str]) -> bool:
        return all(self.from_case.get(k, False) for k in keys)


@dataclass
class Attachment:
    consequence_id: str
    actor_class: str
    variable: str
    praxeological_sign: str
    result: dict
    sign_check: str
    inputs_used: list[str]
    sources: list[str]


def _gap(inp: AnnexInputs) -> Interval:
    """Gap between market and capped price in `gap_year`, as a share of the market price. The cap's growth
    is a range too: the smallest gap uses its fastest growth, the largest its slowest."""
    year = int(inp.values["gap_year"].lo)
    cap = inp.values["cap_growth"]
    m = inp.values["market_growth"]
    small = gap_share(cap_gap_path(year, m, [cap.hi] * year)[year - 1], m, year)
    large = gap_share(cap_gap_path(year, m, [cap.lo] * year)[year - 1], m, year)
    return Interval(min(small.lo, large.lo), max(small.hi, large.hi))


# variable -> (handler, input keys it uses). A handler returns a Result whose sign is comparable
# with the consequence's sign.
HANDLERS: dict[str, tuple[Callable[[AnnexInputs], Result], list[str]]] = {
    "quantity_supplied": (lambda i: ceiling_quantity_supplied(_gap(i), i.values["supply_elasticity"]),
                          ["market_growth", "cap_growth", "gap_year", "supply_elasticity"]),
    "excess_demand": (lambda i: ceiling_shortage(_gap(i), i.values["demand_elasticity"], i.values["supply_elasticity"]),
                      ["market_growth", "cap_growth", "gap_year", "demand_elasticity", "supply_elasticity"]),
}


def _price_paid_insiders(i: AnnexInputs) -> Result:
    g = _gap(i)
    return Result("insiders_price_vs_market", -g, "M0",
                  [f"market growth {i.values['market_growth']}", f"cap growth {i.values['cap_growth']}",
                   f"year {int(i.values['gap_year'].lo)}"],
                  "Sitting tenants' rent against the market path, as a share of the market rent.")


def annex_pass(prediction: dict, inputs: AnnexInputs, protected_actor: str | None = None) -> list[Attachment]:
    """Attach annex results to reported consequences. The prediction is not modified (checked)."""
    before = copy.deepcopy(prediction)
    out = []
    for c in prediction["consequences"]:
        if not c["reported"]:
            continue
        handler = HANDLERS.get(c["variable"])
        keys = handler[1] if handler else []
        if c["variable"] == "price_paid" and protected_actor and c["actor_class"] == protected_actor:
            handler = (_price_paid_insiders, ["market_growth", "cap_growth", "gap_year"])
            keys = handler[1]
        if handler is None or not all(k in inputs.values for k in keys):
            continue
        r = handler[0](inputs)
        out.append(Attachment(c["id"], c["actor_class"], c["variable"], c["sign"],
                              {"name": r.name, "range": [r.value.lo, r.value.hi], "rung": r.rung,
                               "assumptions": r.assumptions, "note": r.note},
                              check_sign(c["sign"], r), keys, [f"{k}: {inputs.sources[k]}" for k in keys]))
    if prediction != before:
        raise GuardError("the annex pass changed the prediction")
    return out


@dataclass
class PremiseEvidence:
    premise: str
    current_p: float
    proposed_p: float
    rung: str
    basis: str
    accepted: bool = False


def premise_evidence(premise: str, current_p: float, favoured: Result, opposed: Result) -> PremiseEvidence:
    """Evidence for a dominance premise ('the favoured chain is larger than the opposed one').

    If the favoured range's smallest size exceeds the opposed range's largest, propose p = 0.9; if the
    reverse, 0.1; if the ranges overlap, leave p where it is. The proposal is never applied here.
    """
    f = Interval(min(abs(favoured.value.lo), abs(favoured.value.hi)), max(abs(favoured.value.lo), abs(favoured.value.hi)))
    o = Interval(min(abs(opposed.value.lo), abs(opposed.value.hi)), max(abs(opposed.value.lo), abs(opposed.value.hi)))
    rung = "M1" if "M1" in (favoured.rung, opposed.rung) else "M0"
    if f.lo > o.hi:
        p, why = 0.9, f"favoured size {f} exceeds opposed size {o} everywhere"
    elif o.lo > f.hi:
        p, why = 0.1, f"opposed size {o} exceeds favoured size {f} everywhere"
    else:
        p, why = current_p, f"ranges overlap ({f} against {o}); no change proposed"
    return PremiseEvidence(premise, current_p, p, rung, f"annex {rung}: {why}")


def settle_by_arithmetic(total: dict, favoured: Result, opposed: Result, inputs: AnnexInputs, keys: list[str]) -> str:
    """Settle a CR-12 total by arithmetic (CR-12e, 0.8). Allowed only for M0 results on the case's own figures.

    Returns the sign the arithmetic gives ('ambiguous' if the ranges overlap). Does not write it anywhere:
    the caller records it as a CR-12e step with this function's result as the arithmetic.
    """
    if favoured.rung != "M0" or opposed.rung != "M0":
        raise GuardError("only M0 arithmetic may settle a CR-12 comparison; M1 results can only be evidence for a premise")
    if not inputs.all_from_case(keys):
        raise GuardError("the arithmetic uses ranges not given by the case record; use premise_evidence instead")
    ev = premise_evidence("arithmetic", 0.5, favoured, opposed)
    if ev.proposed_p == 0.9:
        return total["favoured_sign"]
    if ev.proposed_p == 0.1:
        return {"increase": "decrease", "decrease": "increase"}.get(total["favoured_sign"], "ambiguous")
    return "ambiguous"


def to_markdown(case: str, atts: list[Attachment]) -> str:
    out = [f"# Annex pass: {case}", "",
           "Sizes attached to reported consequences by `mathpraxeo.bridge.annex_pass`. No consequence was changed.", "",
           "| Consequence | Actor class | Variable | Sign | Annex range | Rung | Sign check |", "|---|---|---|---|---|---|---|"]
    for a in atts:
        lo, hi = a.result["range"]
        out.append(f"| {a.consequence_id} | {a.actor_class} | {a.variable} | {a.praxeological_sign} | "
                   f"[{lo:.3g}, {hi:.3g}] | {a.result['rung']} | {a.sign_check} |")
    out += ["", "Sources of the ranges:", ""]
    seen = set()
    for a in atts:
        for s in a.sources:
            if s not in seen:
                seen.add(s)
                out.append(f"- {s}")
    notes = [f"- {a.consequence_id}: {a.result['note']}" for a in atts if a.result["note"]]
    if notes:
        out += ["", "Notes:", ""] + notes
    return "\n".join(out) + "\n"


def dump(atts: list[Attachment]) -> str:
    return json.dumps([asdict(a) for a in atts], indent=1)
