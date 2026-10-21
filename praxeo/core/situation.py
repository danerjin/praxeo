"""The situation record of the core-rule pilot: what a policy does, in CR-1's terms, and the facts of the case the core rules
need (who trades, which price is held and which way, which terms are left free, which alternatives and links exist).

It carries no signs: every sign comes from praxeo/core/core.lp. Each empirical fact names the assumptions it rests on
(at most three), by id; `assumptions` gives each id its text and probability. `run` derives the consequences with the
core rules alone (no pattern file is loaded).
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field

from .. import engine
from ..schema import Assumption, PolicyRecord

CORE_RULES = [Path(__file__).parent / "core.lp"]
# The vocabulary's price variables (02_ontology.md 2.4): CR-9 needs to know whether a change is in a price or a quantity.
PRICE_VARIABLES = ("price_paid", "net_price_received", "wage_rate", "price_substitute", "price_complement", "right_lease_price",
                   "quality_adjusted_price", "full_cost_per_unit", "interest_rate")
Side = Literal["buyer", "seller"]


class Premised(BaseModel):
    premises: list[str] = Field(default=[], max_length=3, description="Assumption ids the fact rests on")


class Exchange(BaseModel):
    id: str
    buyer: str
    seller: str
    unsatisfied_buyer: Optional[str] = None
    unsatisfied_seller: Optional[str] = None
    buyer_price_var: Optional[str] = None
    seller_price_var: Optional[str] = None
    criteria_for: Optional[str] = Field(default=None, description="Who the scarce side chooses among (CR-6)")
    criteria: list[str] = Field(default=[], description="The criteria it can choose by: a group")


class Held(Premised):
    component: str
    exchange: str
    direction: Literal["below", "above"]


class Margin(Premised):
    exchange: str
    kind: Literal["criterion", "adjust", "outside"]
    side: Optional[Side] = Field(default=None, description="adjust: the side that controls the term or quantity")
    actor: str
    variables: list[str] = Field(description="One variable, or several for a group (adjust)")


class Alt(Premised):
    component: str
    chooser: str
    actor: str
    variables: list[str]


class Stake(Premised):
    component: str
    actor: str


class Link(Premised):
    source_actor: str
    source_variable: str
    relation: Literal["complement", "input", "substitute", "output", "yield", "same_act", "cost", "own_price", "currency", "supply_price"]
    actor: str
    variable: str = Field(description="One variable, or several comma-separated for a group (labour as employment,hours_worked)")


class Tied(Premised):
    exchange: str
    side: Side
    actor: str


class Charge(BaseModel):
    component: str
    exchange: str
    payer_side: Side
    receiver: str
    receipt_variable: str = Field(description="tax_revenue for a tax, non_tax_receipts for a fee, non_wage_compensation for a mandated term")
    quantity_premises: list[str] = Field(default=[], max_length=3, description="Premises the fall in trades rests on, where the payment is worth something to its receiver (a mandated term)")
    projection_variable: Optional[str] = Field(default=None, description="tax_revenue_vs_static_projection for a tax")


class Grant(BaseModel):
    component: str
    exchange: str
    recipient_side: Side
    payer: str = Field(description="Who pays it out (an agency or fund)")
    outlay_variable: Optional[str] = Field(default="subsidy_outlay")


class Capped(Premised):
    component: str
    exchange: str
    holders: list[str] = Field(default=[], description="Those who hold the permission to sell (licences, quota rights)")
    wider_price: bool = Field(default=False, description="The good's price is set in a wider market (CR-6 0.7)")


class Banned(Premised):
    component: str
    exchange: str


class Moves(Premised):
    exchange: str
    side: Side


class Discretion(Premised):
    component: str
    actor: str


class Means(BaseModel):
    component: str
    actor: str
    direction: Literal["out", "in"]


class Timing(Premised):
    component: str
    actor: str
    variable: str
    mode: Literal["bring_forward", "carry_over"]


class Backstop(Premised):
    component: str
    exchange: str
    buyer: str
    outlay_variable: Optional[str] = Field(default=None, description="e.g. subsidy_outlay")


class Dominance(Premised):
    actor: str
    variable: str
    window: Optional[str] = None
    direction: Literal["increase", "decrease"]
    kind: Literal["empirical", "identity", "arithmetic", "response"] = Field(
        description="CR-12e: what establishes it: an empirical premise, an accounting identity, arithmetic on the case's figures, "
                    "or the argument that a response cannot reverse its cause")


class Situation(BaseModel):
    name: str
    exchanges: list[Exchange]
    held: list[Held] = []
    margins: list[Margin] = []
    alternatives: list[Alt] = []
    stakes: list[Stake] = []
    links: list[Link] = []
    assets: list[Tied] = []
    yields: list[Tied] = []
    transfers: list[dict] = Field(default=[], description="{'exchange': id, 'premises': [...]}: CR-8b")
    compliance: list[dict] = Field(default=[], description="{'component', 'actor'}")
    enforcers: list[dict] = Field(default=[], description="{'component', 'actor'}")
    funded: list[dict] = Field(default=[], description="{'component', 'actor', 'premises'}: who pays the enforcer")
    fixed_budget: list[dict] = Field(default=[], description="{'component', 'actor', 'premises'}: the enforcer's other work gives way")
    charges: list[Charge] = []
    moves: list[Moves] = []
    discretion: list[Discretion] = []
    means: list[Means] = []
    announced: list[dict] = Field(default=[], description="{'component', 'premises'}: CR-10a")
    timing: list[Timing] = []
    early_price: list[dict] = Field(default=[], description="{'exchange', 'premises'}")
    backstops: list[Backstop] = []
    grants: list[Grant] = []
    capped: list[Capped] = []
    banned: list[Banned] = []
    expires: list[dict] = Field(default=[], description="{'component', 'premises'}: the measure ends and is expected to")
    parts: list[dict] = Field(default=[], description="{'part', 'whole'}: CR-12, a class total over its parts")
    dominance: list[Dominance] = []
    assumptions: dict[str, dict] = Field(description="id -> {'text', 'p', 'class'}")


def _q(s: str) -> str:
    return json.dumps(s)


def _p(prem: list[str]) -> str:
    ps = list(prem) + ["none"] * (3 - len(prem))
    return ", ".join(ps)


def facts(s: Situation) -> str:
    out = [f"price_kind({_q(v)})." for v in PRICE_VARIABLES]
    out += ['buy_price("price_paid").', 'sell_price("net_price_received").', 'sell_price("wage_rate").']
    for e in s.exchanges:
        out += [f"party({e.id}, buyer, {_q(e.buyer)}).", f"party({e.id}, seller, {_q(e.seller)})."]
        for side, a in (("buyer", e.unsatisfied_buyer), ("seller", e.unsatisfied_seller)):
            if a:
                out.append(f"unsatisfied({e.id}, {side}, {_q(a)}).")
        for side, v in (("buyer", e.buyer_price_var), ("seller", e.seller_price_var)):
            if v:
                out.append(f"price_var({e.id}, {side}, {_q(v)}).")
        if e.criteria_for and len(e.criteria) > 1:
            out.append(f"criteria({e.id}, {_q(e.criteria_for)}, {_q(','.join(e.criteria))}).")
    for h in s.held:
        out.append(f"held({h.component}, {h.exchange}, {h.direction}, {_p(h.premises)}).")
    for m in s.margins:
        if m.kind == "criterion":
            out.append(f"criterion({m.exchange}, {_q(m.actor)}, {_q(m.variables[0])}, {_p(m.premises)}).")
        elif m.kind == "outside":
            out.append(f"outside({m.exchange}, {_q(m.actor)}, {_q(m.variables[0])}, {_p(m.premises)}).")
        elif len(m.variables) > 1:
            out.append(f"adjust({m.exchange}, {m.side}, {_q(m.actor)}, {_q(','.join(m.variables))}, {_p(m.premises)}).")
        else:
            out.append(f"adjust_one({m.exchange}, {m.side}, {_q(m.actor)}, {_q(m.variables[0])}, {_p(m.premises)}).")
    for a in s.alternatives:
        kind = "group" if len(a.variables) > 1 else "plain"
        out.append(f"alt({a.component}, {_q(a.chooser)}, {_q(a.actor)}, {_q(','.join(a.variables))}, {kind}, {_p(a.premises)}).")
    for st in s.stakes:
        out.append(f"stake({st.component}, {_q(st.actor)}, {_p(st.premises)}).")
    for l in s.links:
        out.append(f"link({_q(l.source_actor)}, {_q(l.source_variable)}, {l.relation}, {_q(l.actor)}, {_q(l.variable)}, {_p(l.premises)}).")
    for l in s.links:
        if "," in l.variable:
            out.append(f"link_group({_q(l.variable)}).")
    for ch in s.charges:
        out.append(f"charge({ch.component}, {ch.exchange}, {ch.payer_side}, {_q(ch.receiver)}).")
        out.append(f"receipt_var({ch.component}, {_q(ch.receipt_variable)}).")
        if ch.quantity_premises:
            out.append(f"qty_premise({ch.component}, {ch.exchange}, {_p(ch.quantity_premises)}).")
        if ch.projection_variable:
            out.append(f"projection_var({ch.component}, {_q(ch.projection_variable)}).")
    for m in s.moves:
        out.append(f"moves({m.exchange}, {m.side}, {_p(m.premises)}).")
    for d in s.discretion:
        out.append(f"discretion({d.component}, {_q(d.actor)}, {_p(d.premises)}).")
    for m in s.means:
        out.append(f"means({m.component}, {_q(m.actor)}, {m.direction}).")
    for a in s.announced:
        out.append(f"announced({a['component']}, {_p(a.get('premises', []))}).")
    for t in s.timing:
        out.append(f"timing({t.component}, {_q(t.actor)}, {_q(t.variable)}, {t.mode}, {_p(t.premises)}).")
    for e in s.early_price:
        out.append(f"early_price({e['exchange']}, {_p(e.get('premises', []))}).")
    for b in s.backstops:
        out.append(f"backstop({b.component}, {b.exchange}, {_q(b.buyer)}, {_p(b.premises)}).")
        if b.outlay_variable:
            out.append(f"outlay_var({b.component}, {_q(b.outlay_variable)}).")
    for g in s.grants:
        out.append(f"grant({g.component}, {g.exchange}, {g.recipient_side}, {_q(g.payer)}).")
        if g.outlay_variable:
            out.append(f"outlay_var({g.component}, {_q(g.outlay_variable)}).")
    for c in s.capped:
        out.append(f"capped({c.component}, {c.exchange}, {_p(c.premises)}).")
        out += [f"holder({c.component}, {c.exchange}, {_q(h)})." for h in c.holders]
        if c.wider_price:
            out.append(f"wider_price({c.exchange}).")
    for b in s.banned:
        out.append(f"banned({b.component}, {b.exchange}, {_p(b.premises)}).")
    for e in s.expires:
        out.append(f"expires({e['component']}, {_p(e.get('premises', []))}).")
    for pt in s.parts:
        out.append(f"part_of({_q(pt['part'])}, {_q(pt['whole'])}).")
    for t in s.assets:
        out.append(f"asset({t.exchange}, {t.side}, {_q(t.actor)}, {_p(t.premises)}).")
    for t in s.yields:
        out.append(f"yield({t.exchange}, {t.side}, {_q(t.actor)}, {_p(t.premises)}).")
    for t in s.transfers:
        out.append(f"transfer({t['exchange']}, {_p(t.get('premises', []))}).")
    for d in s.compliance:
        out.append(f"compliance({d['component']}, {_q(d['actor'])}).")
    for d in s.enforcers:
        out.append(f"enforcer({d['component']}, {_q(d['actor'])}).")
    for d in s.funded:
        out.append(f"funded({d['component']}, {_q(d['actor'])}, {_p(d.get('premises', []))}).")
    for d in s.fixed_budget:
        out.append(f"fixed_budget({d['component']}, {_q(d['actor'])}, {_p(d.get('premises', []))}).")
    return "\n".join(out) + "\n"


def assumptions(s: Situation) -> dict[str, Assumption]:
    return {k: Assumption(id=k, text=v["text"], assumption_class=v.get("class", "other"), p=v["p"]) for k, v in s.assumptions.items()}


def run(s: Situation):
    """The consequences the core rules alone derive from the situation, with CR-12e applied."""
    empty = PolicyRecord(name=s.name, jurisdiction="-", rule_maker="-", enacted="-", effective="-", components=[])
    a = assumptions(s)
    with engine.rule_set(CORE_RULES):
        cons = engine.run(empty, a, extra=facts(s))[0]
    return dominate(cons, s, a)


def dominate(cons, s: Situation, a: dict[str, Assumption]):
    """CR-12e: where opposite chains made a consequence ambiguous, a dominance premise that holds (p >= cut-off) settles its
    sign; the consequence then rests on the chains' premises and the dominance premise. Not for signs per reading or groups."""
    out = []
    for c in cons:
        d = next((d for d in s.dominance if (d.actor, d.variable, d.window) == (c.actor_class, c.variable, c.window)), None)
        if d and c.sign == "ambiguous" and not c.sign_by_reading and not c.group:
            used = sorted(set(c.assumptions) | set(d.premises))
            c = c.model_copy(update=dict(sign=d.direction, assumptions=used, assumption_sets=[used],
                                         reported=all(a[x].p >= engine.CUTOFF for x in used)))
        out.append(c)
    return out


def load(path: Path) -> Situation:
    return Situation.model_validate_json(path.read_text())
