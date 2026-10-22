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
from ..schema import Assumption, PolicyRecord, Unclear

CORE_RULES = [Path(__file__).parent / "core.lp"]
# The vocabulary's price variables (02_ontology.md 2.4): CR-9 needs to know whether a change is in a price or a quantity.
PRICE_VARIABLES = ("price_paid", "net_price_received", "wage_rate", "price_substitute", "price_complement", "right_lease_price",
                   "quality_adjusted_price", "full_cost_per_unit", "interest_rate")
Side = Literal["buyer", "seller"]


class Premised(BaseModel):
    premises: list[str] = Field(default=[], max_length=3, description="Assumption ids the fact rests on")
    reading: Optional[str] = Field(default=None, description="A reading label (U1-b): the fact holds only under that reading of an unclear provision")


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
    inverse: bool = Field(default=False, description="The variable falls as the alternative is used more (reformulating to fewer calories, measured by the calorie count)")


class Stake(Premised):
    component: str
    actor: str


class Link(Premised):
    source_actor: str
    source_variable: str
    relation: Literal["complement", "input", "substitute", "output", "yield", "same_act", "cost", "own_price", "currency", "supply_price", "supply",
                      "paid_from", "paid_into", "crowding"]
    actor: str
    variable: str = Field(description="One variable, or several comma-separated for a group (labour as employment,hours_worked)")
    horizon: Optional[Literal["short", "medium", "long"]] = Field(default=None, description="When the link acts; medium if not given")


class Tied(Premised):
    exchange: str
    side: Side
    actor: str


class Charge(BaseModel):
    component: str
    premises: list[str] = Field(default=[], max_length=3, description="That the charge binds and is enforced")
    exchange: str
    payer_side: Side
    receiver: str = Field(description="Who receives it; for a branch paid in kind, the subclass that receives it (workers.at_offering_firms), not the whole side")
    receipt_variable: str = Field(description="tax_revenue for a tax, non_tax_receipts for a fee, non_wage_compensation for a mandated term")
    quantity_premises: list[str] = Field(default=[], max_length=3, description="Premises the fall in trades rests on, where the payment is worth something to its receiver (a mandated term)")
    projection_variable: Optional[str] = Field(default=None, description="tax_revenue_vs_static_projection for a tax")
    branch_premises: list[str] = Field(default=[], max_length=3, description="Where the charge is one branch of a choice the policy gives the payer (pay, or provide in kind): the premise that some payers take it")
    branch_premise_sets: list[list[str]] = Field(default=[], description="Further premise sets, any one of which also opens the branch (new offerers, or upgraders)")
    capped_payers: list[str] = Field(default=[], description="Payers whose total under the charge is capped: they pay a fixed sum at the margin")
    basis: Literal["unit", "operating", "item"] = Field(default="unit", description="operating: a sum fixed per seller (a licence fee); item: a sum fixed per item offered (testing or labelling each item); both not per unit sold (CR-4 0.8)")


class Grant(BaseModel):
    component: str
    premises: list[str] = Field(default=[], max_length=3, description="That the grant is paid as enacted (funded, claimed)")
    exchange: str
    recipient_side: Side
    payer: str = Field(description="Who pays it out (an agency or fund)")
    outlay_variable: Optional[str] = Field(default="subsidy_outlay")
    budget_premises: list[str] = Field(default=[], max_length=3, description="The grant's total is fixed and more would claim it than it covers: it is rationed by waiting or other criteria")


class Threshold(Premised):
    """A line in a measure of size past which the component binds, or past which a grant is lost: crossing it is an option
    made worse for those near it."""
    component: str
    actor: str = Field(description="Those near the line, below it")
    variable: str = Field(description="The measure of size the line is drawn in (employment, quantity_supplied)")
    chooser: Optional[str] = Field(default=None, description="Who decides on crossing, where not the actor itself (employers setting workers' hours)")


class Qualifies(Premised):
    component: str
    actor: str = Field(description="Those who compete to qualify")
    variable: str = Field(description="What the allocation is based on (quantity_supplied, quantity_traded)")


class Capped(Premised):
    component: str
    exchange: str
    holders: list[str] = Field(default=[], description="Those who hold the permission to sell (licences, quota rights)")
    wider_price: bool = Field(default=False, description="The good's price is set in a wider market (CR-6 0.7)")


class Penalty(Premised):
    """CR-8b: a fine due on breaking the rule, from those who break it to those who collect it; its premise is that some
    break the rule and are fined."""
    component: str
    actor: str = Field(description="Those who break the rule and pay")
    collector: str


class Terms(Premised):
    """CR-1 without a payment: the option of trading in an exchange made worse or better for one side (a private rule
    changing the bundle a rule-maker sells its members; a disclosure showing a good worse or better than believed, with
    the premise that beliefs change; a non-price term imposed by rule)."""
    component: str
    exchange: str
    side: Side
    direction: Literal["worse", "better"]


class Banned(Premised):
    component: str
    exchange: str


class Fixed(Premised):
    exchange: str
    side: Side = Field(description="The side whose price cannot move in the period: by a rule already in force (a minimum wage) or a term already set")
    horizon: Optional[Literal["short", "medium", "long"]] = Field(default=None, description="How long it stays fixed (a term set for the year: short); short if not given")


class Reading(BaseModel):
    """A provision the text leaves unclear (02_ontology.md, per-reading signs): which components apply under each reading.
    A component no reading lists applies under all of them; the engine runs once per reading and gives a sign per reading
    where they differ."""
    id: str
    text: str
    readings: list[str] = Field(description='Each "U1-a: what the provision means under it"')
    components: dict[str, list[str]] = Field(description="Reading label -> the components that apply under it")


class Moves(Premised):
    exchange: str
    side: Side
    horizon: Optional[Literal["short", "medium", "long"]] = Field(default=None, description="When the price takes the change (sticky prices: medium); short if not given")


class Incidence(Premised):
    """CR-7b, DM-1: the side whose alternatives are clearly worse bears more of a charge (receives more of a grant)."""
    component: str
    exchange: str
    side: Side = Field(description="The side whose alternatives are clearly worse")


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
    penalties: list[Penalty] = Field(default=[], description="CR-8b: fines due on breaking a component's rule")
    terms: list[Terms] = Field(default=[], description="CR-1 without a payment: trading in an exchange made worse or better for one side")
    banned: list[Banned] = []
    incidence: list[Incidence] = Field(default=[], description="CR-7b: which side's alternatives are clearly worse, for a charge or grant on an exchange")
    fixed: list[Fixed] = Field(default=[], description="A price that cannot move in the period; a charge's payer then adjusts the terms it controls (margins of kind adjust)")
    unclear: list[Reading] = Field(default=[], description="Provisions with more than one reading, and the components each reading applies")
    thresholds: list[Threshold] = Field(default=[], description="CR-4 at a line: the component binds only above a size")
    qualifies: list[Qualifies] = Field(default=[], description="CR-7c: a right the policy creates is allocated by history in a period after it is expected")
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
    out += ['share_var(charge, "tax_share_borne").', 'share_var(grant, "subsidy_share_received").', 'share_var(penalty, "non_tax_receipts").']
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
        if a.inverse and kind == "plain":
            out.append(f"alt_inverse({a.component}, {_q(a.chooser)}, {_q(a.actor)}, {_q(a.variables[0])}).")
    for st in s.stakes:
        out.append(f"stake({st.component}, {_q(st.actor)}, {_p(st.premises)}).")
    for l in s.links:
        out.append(f"link({_q(l.source_actor)}, {_q(l.source_variable)}, {l.relation}, {_q(l.actor)}, {_q(l.variable)}, {_p(l.premises)}).")
        if l.horizon:
            out.append(f"link_horizon({_q(l.source_actor)}, {_q(l.source_variable)}, {l.relation}, {_q(l.actor)}, {_q(l.variable)}, {l.horizon}).")
    for l in s.links:
        if "," in l.variable:
            out.append(f"link_group({_q(l.variable)}).")
    for ch in s.charges:
        out.append(f"charge({ch.component}, {ch.exchange}, {ch.payer_side}, {_q(ch.receiver)}).")
        if ch.premises:
            out.append(f"charge_premise({ch.component}, {_p(ch.premises)}).")
        out.append(f"receipt_var({ch.component}, {_q(ch.receipt_variable)}).")
        if ch.quantity_premises:
            out.append(f"qty_premise({ch.component}, {ch.exchange}, {_p(ch.quantity_premises)}).")
        if ch.projection_variable:
            out.append(f"projection_var({ch.component}, {_q(ch.projection_variable)}).")
        if ch.branch_premises:
            out.append(f"branch({ch.component}, {_p(ch.branch_premises)}).")
        out += [f"branch({ch.component}, {_p(ps)})." for ps in ch.branch_premise_sets]
        out += [f"charge_capped({ch.component}, {_q(a)})." for a in ch.capped_payers]
        if ch.basis == "operating":
            out.append(f"operating({ch.component}).")
        if ch.basis == "item":
            out.append(f"per_item({ch.component}).")
    for f in s.fixed:
        out.append(f"fixed({f.exchange}, {f.side}, {_p(f.premises)}).")
        if f.horizon:
            out.append(f"fixed_horizon({f.exchange}, {f.side}, {f.horizon}).")
    for m in s.moves:
        out.append(f"moves({m.exchange}, {m.side}, {_p(m.premises)}).")
        if m.horizon:
            out.append(f"moves_horizon({m.exchange}, {m.side}, {m.horizon}).")
    for i in s.incidence:
        out.append(f"incidence({i.component}, {i.exchange}, {i.side}, {_p(i.premises)}).")
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
        if g.premises:
            out.append(f"grant_premise({g.component}, {_p(g.premises)}).")
        if g.budget_premises:
            out.append(f"budget({g.component}, {g.exchange}, {_p(g.budget_premises)}).")
        if g.outlay_variable:
            out.append(f"outlay_var({g.component}, {_q(g.outlay_variable)}).")
    for c in s.capped:
        out.append(f"capped({c.component}, {c.exchange}, {_p(c.premises)}).")
        out += [f"holder({c.component}, {c.exchange}, {_q(h)})." for h in c.holders]
        if c.wider_price:
            out.append(f"wider_price({c.exchange}).")
    for pn in s.penalties:
        out.append(f"penalty({pn.component}, {_q(pn.actor)}, {_q(pn.collector)}, {_p(pn.premises)}).")
    for t in s.terms:
        out.append(f"terms({t.component}, {t.exchange}, {t.side}, {t.direction}, {_p(t.premises)}).")
    for b in s.banned:
        out.append(f"banned({b.component}, {b.exchange}, {_p(b.premises)}).")
    for t in s.thresholds:
        out.append(f"threshold({t.component}, {_q(t.actor)}, {_q(t.variable)}, {_p(t.premises)}).")
        if t.chooser:
            out.append(f"threshold_chooser({t.component}, {_q(t.actor)}, {_q(t.chooser)}).")
    for t in s.qualifies:
        out.append(f"qualifies({t.component}, {_q(t.actor)}, {_q(t.variable)}, {_p(t.premises)}).")
    for e in s.expires:
        out.append(f"expires({e['component']}, {_p(e.get('premises', []))}).")
    for d in s.dominance:
        if d.window is None:
            out.append(f"dom({_q(d.actor)}, {_q(d.variable)}, {d.direction}, {_p(d.premises)}).")
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


# The parts that are a component's own operation (CR-1): under an unclear provision they apply only under the readings
# that list their component.
OPERATIONS = ["held", "charges", "terms", "penalties", "grants", "capped", "banned", "thresholds", "qualifies", "backstops", "discretion", "means",
              "compliance", "enforcers", "funded", "fixed_budget", "announced", "expires"]


def _comp(x) -> Optional[str]:
    return x.get("component") if isinstance(x, dict) else getattr(x, "component", None)


def _reading(x) -> Optional[str]:
    return x.get("reading") if isinstance(x, dict) else getattr(x, "reading", None)


def _only(s: Situation, keep, labels=(None,)) -> Situation:
    """The situation with each operation part limited to the components `keep` accepts, and every part to the facts tied
    to one of `labels` (None: the facts tied to no reading)."""
    upd = {p: [x for x in getattr(s, p) if keep(_comp(x))] for p in OPERATIONS}
    for p, f in Situation.model_fields.items():
        items = upd.get(p, getattr(s, p))
        if isinstance(items, list):
            upd[p] = [x for x in items if _reading(x) in labels]
    return s.model_copy(update=upd)


def run(s: Situation):
    """The consequences the core rules alone derive from the situation, with CR-12e applied; once per reading of an unclear
    provision, merged with a sign per reading where they differ (engine.run)."""
    conditional = {c for u in s.unclear for cs in u.components.values() for c in cs}
    labels = lambda u: [r.split(":", 1)[0].strip() for r in u.readings]
    # under a reading: the components it applies, and the facts tied to it (an alternative only that reading opens)
    unclear = [Unclear(id=u.id, text=u.text, readings=u.readings,
                       reading_facts={lab: facts(_only(s, lambda c, cs=set(u.components.get(lab, [])): c in cs, (None, lab)))
                                      + facts(_only(s, lambda c: c not in conditional, (lab,))) for lab in labels(u)})
               for u in s.unclear]
    empty = PolicyRecord(name=s.name, jurisdiction="-", rule_maker="-", enacted="-", effective="-", components=[], unclear=unclear)
    a = assumptions(s)
    with engine.rule_set(CORE_RULES):
        cons = engine.run(empty, a, extra=facts(_only(s, lambda c: c not in conditional)))[0]
    return dominate([_collapse(c) for c in cons], s, a)


def _collapse(c):
    """Signs per combination of readings ("U1-a; U2-b") keep only the provisions the sign depends on: a provision whose
    readings give the same sign whatever the others' readings is dropped from the labels (and a sign no provision changes
    is the one sign)."""
    if not c.sign_by_reading:
        return c
    combos = {tuple(x.strip() for x in k.split(";")): v for k, v in c.sign_by_reading.items()}
    n = len(next(iter(combos)))
    keep = []
    for i in range(n):
        rest = {}
        for k, v in combos.items():
            rest.setdefault(k[:i] + k[i + 1:], set()).add(v)
        if any(len(vs) > 1 for vs in rest.values()):
            keep.append(i)
    if not keep:
        return c.model_copy(update={"sign": next(iter(combos.values())), "sign_by_reading": {}})
    reduced = {"; ".join(k[i] for i in keep): v for k, v in combos.items()}
    return c.model_copy(update={"sign_by_reading": reduced})


def dominate(cons, s: Situation, a: dict[str, Assumption]):
    """CR-12e: where opposite chains made a consequence ambiguous, a dominance premise that holds (p >= cut-off) settles its
    sign; the consequence then rests on the chains' premises and the dominance premise. Not for signs per reading or groups."""
    out = []
    for c in cons:
        d = next((d for d in s.dominance if (d.actor, d.variable, d.window) == (c.actor_class, c.variable, c.window)), None)
        # a dominance premise below the cut-off settles nothing: the consequence stays ambiguous, and reported as such
        if d and c.sign == "ambiguous" and not c.sign_by_reading and not c.group and all(a[x].p >= engine.CUTOFF for x in d.premises):
            used = sorted(set(c.assumptions) | set(d.premises))
            c = c.model_copy(update=dict(sign=d.direction, assumptions=used, assumption_sets=[used],
                                         reported=all(a[x].p >= engine.CUTOFF for x in used)))
        elif d and c.sign_by_reading and "ambiguous" in c.sign_by_reading.values() and not c.group \
                and all(a[x].p >= engine.CUTOFF for x in d.premises):
            # per reading: the dominance premise settles the readings under which the chains clash
            by = {k: (d.direction if v == "ambiguous" else v) for k, v in c.sign_by_reading.items()}
            uniform = len(set(by.values())) == 1
            used = sorted(set(c.assumptions) | set(d.premises))
            c = c.model_copy(update=dict(sign_by_reading={} if uniform else by, sign=next(iter(by.values())) if uniform else "ambiguous",
                                         assumptions=used, assumption_sets=[used], reported=all(a[x].p >= engine.CUTOFF for x in used)))
        out.append(c)
    return out


def load(path: Path) -> Situation:
    return Situation.model_validate_json(path.read_text())
