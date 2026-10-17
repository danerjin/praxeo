"""The annex pass: attach sizes to a praxeological run without changing it.

Dependency runs one way: this module reads `praxeo` output; nothing in `praxeo`
or `handbook` imports the annex.

Operations, each with a guard:

- `annex_pass` attaches an annex `Result` and its sign check to every reported
  consequence that a handler covers. It never changes a consequence: it returns
  new records beside the prediction and checks that the prediction is unchanged.
- `dominance_evidence` sizes the two chains behind a CR-12 dominance premise, from
  counts the inputs supply, and `premise_evidence` turns the sizes into a proposed
  probability. Neither writes the premise's p: the premise step
  (`premise_step.py`) puts the proposal to a decider, which must accept it.
- `settle_by_arithmetic` lets a result settle a CR-12 comparison directly, as
  CR-12e (0.8) allows for "arithmetic where the case gives the figures". Only
  rung M0 results computed from the case's own figures may do this; anything
  else raises `GuardError`.
"""
from __future__ import annotations

import copy
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Callable

from .bounds import black_market_premium, hotelling_gap, rent_seeking_ceiling
from .capital import cap_gap_path, capitalized_loss, gap_share, present_value
from .identities import wait_time
from .interval import Interval, corners
from .result import Result, check_sign
from .statics import (ceiling_quantity_supplied, ceiling_shortage, cost_pass_through, equilibrium_shift,
                      floor_surplus, quantity_under_wedge, quota_rent, subsidy_incidence, tariff, tax_incidence)


class GuardError(Exception):
    """An annex result tried to do what only praxeology (or the case's own arithmetic) may do."""


@dataclass
class AnnexInputs:
    """Ranges for one case. Every range names its source; `from_case` is True only for figures in the
    case record itself (not illustrative, not from outside studies). `actors` names the actor classes
    the handlers look for (e.g. {"buyers": "steel_users"}); `dominance` names, for each dominance premise,
    the counts that size its favoured and opposed chains."""
    values: dict[str, Interval]
    sources: dict[str, str]
    from_case: dict[str, bool]
    actors: dict[str, str] = field(default_factory=dict)
    dominance: dict[str, dict] = field(default_factory=dict)

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
        return cls(vals, srcs, fc, raw.get("_actors", {}), raw.get("_dominance", {}))

    def has(self, keys: list[str]) -> bool:
        return all(k in self.values for k in keys)

    def all_from_case(self, keys: list[str]) -> bool:
        return all(self.from_case.get(k, False) for k in keys)


@dataclass
class Attachment:
    consequence_id: str
    actor_class: str
    variable: str
    praxeological_sign: str
    handler: str
    result: dict
    sign_check: str
    inputs_used: list[str]
    sources: list[str]
    diagnosis: str = ""


# ---------------------------------------------------------------- helpers

GAP_KEYS = ["market_growth", "cap_growth", "gap_year"]


def _gap(i: AnnexInputs) -> Interval:
    """Gap between market and capped price in `gap_year`, as a share of the market price. The cap's growth
    is a range too: the smallest gap uses its fastest growth, the largest its slowest."""
    year = int(i.values["gap_year"].lo)
    cap, m = i.values["cap_growth"], i.values["market_growth"]
    small = gap_share(cap_gap_path(year, m, [cap.hi] * year)[year - 1], m, year)
    large = gap_share(cap_gap_path(year, m, [cap.lo] * year)[year - 1], m, year)
    return Interval(min(small.lo, large.lo), max(small.hi, large.hi))


def _capitalized(i: AnnexInputs) -> Result:
    """Fall in an asset's value at announcement, in years of today's income: minus the present value of the
    gaps over the expected duration. Uses the cap's slowest growth for the upper bound, fastest for the lower."""
    years = int(i.values["expected_duration"].hi)
    cap, m = i.values["cap_growth"], i.values["market_growth"]
    hi = capitalized_loss(cap_gap_path(years, m, [cap.lo] * years), i.values["discount_rate"], i.values["expected_duration"])
    lo = capitalized_loss(cap_gap_path(years, m, [cap.hi] * years), i.values["discount_rate"], i.values["expected_duration"])
    loss = Interval(min(lo.value.lo, hi.value.lo), max(lo.value.hi, hi.value.hi))
    return Result("asset_value_change", -loss, "M0", hi.assumptions + [f"cap growth {cap}"], hi.note)


def _insiders_price(i: AnnexInputs) -> Result:
    return Result("insiders_price_vs_market", -_gap(i), "M0",
                  [f"market growth {i.values['market_growth']}", f"cap growth {i.values['cap_growth']}",
                   f"year {int(i.values['gap_year'].lo)}"],
                  "Sitting tenants' price against the market path, as a share of the market price.")


def _floor_quantity(i: AnnexInputs) -> Result:
    g, ed = i.values["floor_gap"], i.values["demand_elasticity"]
    return Result("quantity_demanded_change", corners(lambda g_, d: d * g_, g, ed), "M1",
                  [f"floor {g} above clearing", f"demand elasticity {ed}", "first order"])


def _tariff_part(part: str) -> Callable[[AnnexInputs], Result]:
    def f(i: AnnexInputs) -> Result:
        return tariff(i.values["tax_rate"], i.values["import_share"], i.values["demand_elasticity"],
                      i.values["supply_elasticity"], (i.values["pass_through"].lo, i.values["pass_through"].hi))[part]
    return f


TARIFF_KEYS = ["tax_rate", "import_share", "demand_elasticity", "supply_elasticity", "pass_through"]
TAX_KEYS = ["tax_rate", "demand_elasticity", "supply_elasticity"]


@dataclass
class Handler:
    """Covers consequences on `variable` for components of `instruments`, for the actor in `role`.

    role: "bound", "protected" or "excluded" (fields of the record's component), "any", or a key of
    AnnexInputs.actors (e.g. "buyers", "importers", "downstream").
    """
    name: str
    instruments: tuple[str, ...]
    variable: str
    role: str
    fn: Callable[[AnnexInputs], Result]
    keys: list[str]


# What a "contradicts" means for each kind of handler: the praxeological premise (an assumption atom prefix)
# that has most likely failed under the annex's inputs, or an input error. Keyed by handler name.
DIAGNOSES: dict[str, tuple[list[str], str]] = {
    **{n: (["binding"], "the market path does not rise above the capped path over the input ranges, so the ceiling "
                        "does not bind: the premise `binding` fails under these inputs, or the market-growth range is wrong")
       for n in ("ceiling_quantity_supplied", "ceiling_shortage", "insiders_price", "capitalized_value")},
    "substitute_price": (["substitutes"], "no demand is diverted to uncovered units under these inputs: the premise "
                                          "`substitutes` fails, or the diverted-demand range is wrong"),
    **{n: (["binding"], "the floor is not above the clearing price under these inputs: the floor does not bind, "
                        "or the floor-gap range is wrong")
       for n in ("floor_surplus", "floor_quantity")},
    **{n: ([], "the rate range has the wrong sign: an input error, not a failed premise")
       for n in ("tax_buyers_price", "tax_sellers_price", "tax_quantity", "tax_revenue_shortfall",
                 "tariff_domestic_price", "tariff_domestic_output", "tariff_imports", "tariff_use",
                 "tariff_revenue_shortfall", "subsidy_buyers_price", "subsidy_sellers_price")},
    **{n: (["binding"], "the domestic price is not above the world or marginal-cost price under these inputs: the "
                        "quota or licence does not bind, or the price-gap range is wrong")
       for n in ("right_value", "right_lease_price")},
    "cost_pass_through": ([], "the upstream price change has the opposite sign to the one this chain assumes: check the "
                              "upstream consequence and the input-price range"),
    "wait_time": ([], "a wait time cannot be negative: an input error"),
    "black_market_premium": (["enforced"], "no illegal trade pays at the margin under these inputs: the expected penalty "
                                           "exceeds what buyers will pay above the ceiling, so the premise of imperfect "
                                           "enforcement (PC-6) fails, or the ceiling does not bind"),
    "hotelling_timing": ([], "the net-of-tax price is expected to grow at the other side of the interest rate from the one "
                             "the timing chain assumes: check the expected price and tax paths, and whether owners expect "
                             "to keep the resource"),
    "rent_seeking_ceiling": ([], "a ceiling on spending cannot contradict a sign; check the rent and rate inputs"),
}


def diagnose(handler: str, prediction: dict) -> str:
    """Name the premise a contradiction points to, with its estimated probability in this run."""
    prefixes, text = DIAGNOSES.get(handler, ([], "no diagnosis recorded for this handler"))
    atoms = [f"`{k}` (p = {v['p']:.2f})" for k, v in prediction.get("assumptions", {}).items()
             if k.split("(", 1)[0] in prefixes]
    return text + (f". Premise in this run: {', '.join(atoms)}" if atoms else "")


CEILING = ("price_ceiling",)
TAXES = ("per_unit_tax",)
TARIFF = ("tariff",)
SUBSIDY = ("per_unit_subsidy", "export_subsidy")
QUOTA = ("quota", "licensing_requirement", "rights_allocation")
ANY = ("*",)

HANDLERS: list[Handler] = [
    # price ceilings (PC-1, PC-3, PC-5, SB-4 / CR-7c, PC-2, RS-4)
    Handler("ceiling_quantity_supplied", CEILING, "quantity_supplied", "bound",
            lambda i: ceiling_quantity_supplied(_gap(i), i.values["supply_elasticity"]), GAP_KEYS + ["supply_elasticity"]),
    Handler("ceiling_shortage", CEILING, "excess_demand", "excluded",
            lambda i: ceiling_shortage(_gap(i), i.values["demand_elasticity"], i.values["supply_elasticity"]),
            GAP_KEYS + ["demand_elasticity", "supply_elasticity"]),
    Handler("insiders_price", CEILING, "price_paid", "protected", _insiders_price, GAP_KEYS),
    Handler("capitalized_value", CEILING, "asset_value", "bound", _capitalized,
            GAP_KEYS + ["discount_rate", "expected_duration"]),
    Handler("substitute_price", CEILING, "price_substitute", "excluded",
            lambda i: equilibrium_shift(i.values["diverted_demand"], 0.0, i.values["substitute_demand_elasticity"],
                                        i.values["substitute_supply_elasticity"])[0],
            ["diverted_demand", "substitute_demand_elasticity", "substitute_supply_elasticity"]),
    Handler("wait_time", ANY, "wait_time", "any",
            lambda i: wait_time(i.values["queue_length"], i.values["throughput"]), ["queue_length", "throughput"]),
    # price floors (PC-9, PC-10)
    Handler("floor_surplus", ("price_floor",), "excess_supply", "any",
            lambda i: floor_surplus(i.values["floor_gap"], i.values["demand_elasticity"], i.values["supply_elasticity"]),
            ["floor_gap", "demand_elasticity", "supply_elasticity"]),
    Handler("floor_quantity", ("price_floor",), "employment", "any", _floor_quantity, ["floor_gap", "demand_elasticity"]),
    Handler("floor_quantity", ("price_floor",), "quantity_demanded", "any", _floor_quantity, ["floor_gap", "demand_elasticity"]),
    # per-unit taxes (TX-1, TX-2, CR-5a)
    Handler("tax_buyers_price", TAXES, "price_paid", "buyers",
            lambda i: tax_incidence(i.values["tax_rate"], i.values["demand_elasticity"], i.values["supply_elasticity"])[0], TAX_KEYS),
    Handler("tax_sellers_price", TAXES, "net_price_received", "sellers",
            lambda i: tax_incidence(i.values["tax_rate"], i.values["demand_elasticity"], i.values["supply_elasticity"])[1], TAX_KEYS),
    Handler("tax_quantity", TAXES, "quantity_traded", "any",
            lambda i: quantity_under_wedge(i.values["tax_rate"], i.values["demand_elasticity"], i.values["supply_elasticity"]), TAX_KEYS),
    Handler("tax_revenue_shortfall", TAXES, "tax_revenue_vs_static_projection", "any",
            lambda i: quantity_under_wedge(i.values["tax_rate"], i.values["demand_elasticity"], i.values["supply_elasticity"]), TAX_KEYS),
    # tariffs (TX-7, TX-8)
    Handler("tariff_domestic_price", TARIFF, "price_paid", "buyers", _tariff_part("domestic_price"), TARIFF_KEYS),
    Handler("tariff_domestic_price", TARIFF, "net_price_received", "domestic_sellers", _tariff_part("domestic_price"), TARIFF_KEYS),
    Handler("tariff_domestic_output", TARIFF, "quantity_supplied", "domestic_sellers", _tariff_part("domestic_output"), TARIFF_KEYS),
    Handler("tariff_imports", TARIFF, "quantity_traded", "importers", _tariff_part("imports"), TARIFF_KEYS),
    Handler("tariff_use", TARIFF, "quantity_traded", "buyers", _tariff_part("use"), TARIFF_KEYS),
    Handler("tariff_revenue_shortfall", TARIFF, "tax_revenue_vs_static_projection", "any", _tariff_part("imports"), TARIFF_KEYS),
    # subsidies (SB-1, SB-2)
    Handler("subsidy_buyers_price", SUBSIDY, "price_paid", "buyers",
            lambda i: subsidy_incidence(i.values["subsidy_rate"], i.values["demand_elasticity"], i.values["supply_elasticity"])[0],
            ["subsidy_rate", "demand_elasticity", "supply_elasticity"]),
    Handler("subsidy_sellers_price", SUBSIDY, "net_price_received", "sellers",
            lambda i: subsidy_incidence(i.values["subsidy_rate"], i.values["demand_elasticity"], i.values["supply_elasticity"])[1],
            ["subsidy_rate", "demand_elasticity", "supply_elasticity"]),
    # quotas, licences, allocated rights (EN-1, EN-6, EN-12, CR-7c)
    Handler("right_value", QUOTA, "asset_value", "holders",
            lambda i: present_value(quota_rent(i.values["price_gap"], i.values["units_per_right"]).value,
                                    i.values["discount_rate"], int(i.values["expected_duration"].lo)),
            ["price_gap", "units_per_right", "discount_rate", "expected_duration"]),
    Handler("right_lease_price", QUOTA, "right_lease_price", "any",
            lambda i: quota_rent(i.values["price_gap"], i.values["units_per_right"]), ["price_gap", "units_per_right"]),
    # bounds (SURVEY.md): illegal premium under a ceiling (PC-6), timing of extraction (Hotelling),
    # ceiling on lobbying spending (RS-7)
    Handler("black_market_premium", CEILING, "side_payments", "any",
            lambda i: black_market_premium(_gap(i), i.values["demand_elasticity"], i.values["supply_elasticity"],
                                           i.values["seller_penalty"], i.values["buyer_penalty"]),
            GAP_KEYS + ["demand_elasticity", "supply_elasticity", "seller_penalty", "buyer_penalty"]),
    Handler("hotelling_timing", TAXES + QUOTA, "resource_stock", "any",
            lambda i: hotelling_gap(i.values["net_price_growth"], i.values["discount_rate"],
                                    i.values.get("tax_growth", Interval.point(0.0)), i.values.get("tax_share", Interval.point(0.0))),
            ["net_price_growth", "discount_rate"]),
    Handler("rent_seeking_ceiling", ANY, "lobbying_effort", "any",
            lambda i: rent_seeking_ceiling(i.values["rent_per_year"], i.values["discount_rate"], int(i.values["expected_duration"].hi)),
            ["rent_per_year", "discount_rate", "expected_duration"]),
    # costs passed down a chain (RS-14, PC-12): any instrument, for the actor named `downstream`
    Handler("cost_pass_through", ANY, "price_paid", "downstream",
            lambda i: cost_pass_through(i.values["input_price_change"], i.values["cost_share"]),
            ["input_price_change", "cost_share"]),
]


def _role_actor(role: str, comp: dict, inputs: AnnexInputs) -> str | None:
    if role in ("bound", "protected", "excluded"):
        return comp.get(f"{role}_actor")
    return inputs.actors.get(role)


def _match(c: dict, comps: list[dict], inputs: AnnexInputs) -> Handler | None:
    for h in HANDLERS:
        if h.variable != c["variable"] or not inputs.has(h.keys):
            continue
        for comp in comps:
            if h.instruments != ANY and comp["instrument"] not in h.instruments:
                continue
            if h.role == "any" or _role_actor(h.role, comp, inputs) == c["actor_class"]:
                return h
    return None


def annex_pass(prediction: dict, inputs: AnnexInputs) -> list[Attachment]:
    """Attach annex results to reported consequences. The prediction is not modified (checked)."""
    before = copy.deepcopy(prediction)
    comps = prediction["record"]["components"]
    out = []
    for c in prediction["consequences"]:
        if not c["reported"]:
            continue
        h = _match(c, comps, inputs)
        if h is None:
            continue
        r = h.fn(inputs)
        verdict = check_sign(c["sign"], r)
        out.append(Attachment(c["id"], c["actor_class"], c["variable"], c["sign"], h.name,
                              {"name": r.name, "range": [r.value.lo, r.value.hi], "rung": r.rung,
                               "assumptions": r.assumptions, "note": r.note},
                              verdict, h.keys, [f"{k}: {inputs.sources[k]}" for k in h.keys],
                              diagnose(h.name, prediction) if verdict == "contradicts" else ""))
    if prediction != before:
        raise GuardError("the annex pass changed the prediction")
    return out


# ---------------------------------------------------------------- CR-12 evidence and its guard

@dataclass
class PremiseEvidence:
    premise: str
    current_p: float
    proposed_p: float
    rung: str
    basis: str
    inputs_used: list[str] = field(default_factory=list)
    accepted: bool = False


def _product(i: AnnexInputs, keys: list[str]) -> Interval:
    v = Interval.point(1.0)
    for k in keys:
        v = v * i.values[k]
    return v


def dominance_evidence(inputs: AnnexInputs, premise: str, current_p: float) -> PremiseEvidence | None:
    """Size both chains behind a dominance premise from counts and compare them.

    `inputs.dominance[name]` gives {"favoured": [keys], "opposed": [keys], "rung": "M0"|"M1"}; each chain's
    size is the product of its keys' ranges (e.g. covered units x exit rate x share deterred). The rung is
    M1 unless the spec says M0 and every input is a case figure.
    """
    name = premise.split("(", 1)[0]
    spec = inputs.dominance.get(name)
    if not spec or not inputs.has(spec["favoured"] + spec["opposed"]):
        return None
    keys = spec["favoured"] + spec["opposed"]
    rung = "M0" if spec.get("rung") == "M0" and inputs.all_from_case(keys) else "M1"
    fav = Result("favoured_chain", _product(inputs, spec["favoured"]), rung)
    opp = Result("opposed_chain", _product(inputs, spec["opposed"]), rung)
    ev = premise_evidence(premise, current_p, fav, opp)
    ev.inputs_used = keys
    return ev


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


# ---------------------------------------------------------------- output

def to_markdown(case: str, atts: list[Attachment]) -> str:
    out = [f"# Annex pass: {case}", "",
           "Sizes attached to reported consequences by `mathpraxeo.bridge.annex_pass`. No consequence was changed.", "",
           "| Consequence | Actor class | Variable | Sign | Handler | Annex range | Rung | Sign check |",
           "|---|---|---|---|---|---|---|---|"]
    for a in atts:
        lo, hi = a.result["range"]
        out.append(f"| {a.consequence_id} | {a.actor_class} | {a.variable} | {a.praxeological_sign} | {a.handler} | "
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
    diag = [f"- {a.consequence_id} contradicts its praxeological sign: {a.diagnosis}. The sign is not changed; "
            f"the contradiction is reported for review." for a in atts if a.diagnosis]
    if diag:
        out += ["", "Contradictions:", ""] + diag
    return "\n".join(out) + "\n"


def dump(items) -> str:
    return json.dumps([asdict(a) for a in items], indent=1)
