"""Verifier: structural checks on every consequence before it is reported.

- the variable is in the shared vocabulary; the actor class has a known role (the ontology's, or one the record names);
- the derivation is not empty, and every premise it uses is a record fact, an
  estimated assumption, or the conclusion of an earlier step;
- every assumption it names was estimated, and `reported` agrees with the cut-off;
- per-reading signs name readings that exist;
- a group consequence has a group sign and at least two members, every one in the vocabulary, and a group sign is
  used only for a group; an announcement-window consequence has horizon ['short'] and its component has an
  announcement window.
"""
from __future__ import annotations

from . import vocabulary
from .engine import CUTOFF
from .schema import GROUP_SIGNS, Assumption, Consequence, PolicyRecord

RECORD_PREDICATES = ("ceiling(", "decontrol(", "bound(", "protected(", "excluded(", "tax(", "tariff(", "neighbor(", "enforcer(",
                     "definition_line(", "renewable(", "announced(", "rolled_back(", "taxpayer(", "protected_concentrated(",
                     "subsidy(", "per_unit_sub(", "share_cap(", "criteria(", "budget_capped(", "temporary(", "scrappage(",
                     "repay_on_move(", "field_contested(", "target_qty(", "claim_penalties(",
                     "licensing(", "quota(", "transferable(", "import_quota(", "seller_cap(", "wider_market(", "general_budget(", "price_fixed(", "allocation_by_history(", "prohibition(", "volume_penalties(", "practice_ban(", "fees_to_budget(", "stocks_destroyed(", "taxed_before(", "mobile_buyer(", "rights_sold(", "holder_cap(", "self_supply(", "domestic_seller(", "downstream(", "importer(", "buyer(",
                     "exporter(", "seller(", "renewable(", "definition_line(", "relief_applicant(",
                     "mandate(", "employment(", "term_ban(", "standard(", "per_head_cap(", "paid_absence(", "forfeit_on_leaving(", "complaint_only(",
                     "size_threshold(", "threshold_staff_split(", "threshold_partial_count(", "margin_covered(", "restrains_mobility(",
                     "voids_existing(", "stock_exempt(", "disclosure(", "fixed_cost_per_item(", "floor(", "fixed_budget(", "state_buys(")


def record_roles(record: PolicyRecord) -> set[str]:
    """Roles of the actor classes the record itself names: the ontology's list is open, so a record may
    introduce roles (steel_users, importers) that the rules then use."""
    roles = set()
    for comp in record.components:
        names = [comp.bound_actor, comp.protected_actor, comp.excluded_actor, comp.buyer_actor, comp.seller_actor,
                 comp.domestic_seller_actor, comp.importer_actor, comp.revenue_actor, comp.exporter_actor,
                 comp.exporter_worker_actor or "workers." + comp.exporter_actor, comp.neighbor_actor, comp.enforcer_actor]
        names += [comp.taxpayer_actor, comp.foreign_seller_actor, comp.input_supplier_actor,
                  comp.domestic_seller_owner_actor, comp.relief_applicant_actor, comp.domestic_seller_worker_actor,
                  comp.mobile_buyer_actor, comp.neighbor_seller_actor]
        names += [comp.outlay_actor, comp.right_holder_actor, comp.trainer_actor, comp.informal_buyer_actor, comp.entrant_actor, comp.worker_actor,
                  comp.informal_seller_actor, comp.prospective_buyer_actor, comp.convicted_actor]
        names += [comp.third_party_payer_actor, comp.qualifier_actor, comp.other_spending_actor, comp.future_taxpayer_actor]
        names += [comp.other_buyer_actor, comp.substitute_seller_actor, comp.asset_owner_actor, comp.claim_handler_actor,
                  comp.used_buyer_actor, comp.used_owner_actor, comp.scrapper_actor]
        names += [comp.recipient_actor, comp.floor_bound_actor, comp.applicant_actor, comp.already_provider_actor,
                  comp.already_recipient_actor, comp.below_cap_actor, comp.above_cap_actor, comp.cover_seller_actor,
                  comp.output_buyer_actor, comp.tradable_actor, comp.outside_actor, comp.complainant_actor, comp.violator_actor,
                  comp.near_threshold_actor, comp.below_threshold_actor, comp.margin_recipient_actor, comp.stock_owner_actor,
                  comp.charge_payer_actor, comp.charge_payer_worker_actor, comp.player_recipient_actor, comp.lower_tier_seller_actor, comp.charge_capped_actor,
                  *comp.rival_actors]
        names += [n for rel in comp.related for n in (rel.seller_actor, rel.other_user_actor)]
        for d in comp.downstream:
            names += [d.actor, d.buyer_actor, d.owner_actor, d.exporter_actor, d.worker_actor]
        roles |= {n.split(".")[0] for n in names if n}
    return roles


def verify(consequences: list[Consequence], assumptions: dict[str, Assumption], record: PolicyRecord) -> list[str]:
    problems = []
    labels = {lab for u in record.unclear for lab in u.labels()}
    from .engine import invalid_reading_facts
    for u in record.unclear:
        bad = invalid_reading_facts(u)
        if bad:
            problems.append(f"{u.id}: reading facts for {bad} are not valid clingo and were ignored")
    from .questions import questions_for
    asked = {comp.id: {q.assumption for q, _ in questions_for(comp)} for comp in record.components}
    for u in record.unclear:
        for lab, by_comp in u.reading_premises.items():
            for cid, atoms in by_comp.items():
                for atom in set(atoms) - asked.get(cid, set()):
                    problems.append(f"{u.id} {lab}: premise `{atom}` is not asked of {cid}, so the reading settles nothing")
    by_id = {c.id: c for c in consequences}
    named = record_roles(record)
    for c in consequences:
        actor_msgs = [None if a.split(".")[0] in named else vocabulary.check_actor(a) for a in c.actors()]
        for msg in [vocabulary.check_variable(v) for v in c.members()] + actor_msgs:
            if msg:
                problems.append(f"{c.id}: {msg}")
        if c.group and (len(c.group) < 2 or c.variable != c.group[0] or c.sign not in GROUP_SIGNS and c.sign != "ambiguous"):
            problems.append(f"{c.id}: a group consequence needs two or more members, a group sign (or ambiguous by reading), and its first member as `variable`")
        if c.actor_group and (len(c.actor_group) < 2 or c.actor_class != c.actor_group[0] or c.group):
            problems.append(f"{c.id}: an actor group needs two or more classes, its first as `actor_class`, and one variable")
        if c.sign in GROUP_SIGNS and not (c.group or c.actor_group):
            problems.append(f"{c.id}: group sign `{c.sign}` on a single variable and class")
        if c.window == "announcement" and c.horizon != ["short"]:
            problems.append(f"{c.id}: an announcement-window consequence has horizon ['short'], not {c.horizon}")
        if c.window == "after_expiry" and not any(comp.temporary for comp in record.components):
            problems.append(f"{c.id}: after-expiry consequence, but the record has no temporary measure")
        if c.window == "announcement" and not any(comp.announcement_window for comp in record.components):
            problems.append(f"{c.id}: announcement-window consequence, but the record has no announcement window")
        if c.combines:
            missing = [i for i in c.combines if i not in by_id]
            if missing:
                problems.append(f"{c.id}: combines unknown consequences {missing}")
        elif not c.derivation:
            problems.append(f"{c.id}: empty derivation")
        concluded = set()
        for step in c.derivation:
            for prem in step.premises:
                if not (prem in assumptions or prem in concluded or prem.startswith(RECORD_PREDICATES)):
                    problems.append(f"{c.id}: {step.rule} uses `{prem}`, which is neither a record fact, an assumption nor an earlier conclusion")
            concluded.add(step.conclusion)
        for a in {a for s in c.assumption_sets for a in s} | set(c.assumptions):
            if a not in assumptions:
                problems.append(f"{c.id}: assumption `{a}` was never estimated")
        if c.assumptions and all(a in assumptions for a in c.assumptions):
            should = all(assumptions[a].p >= CUTOFF for a in c.assumptions)
            if should != c.reported:
                problems.append(f"{c.id}: reported={c.reported} disagrees with the cut-off")
        for lab in c.sign_by_reading:
            for part in filter(None, lab.split("; ")):
                if part not in labels:
                    problems.append(f"{c.id}: sign for unknown reading `{part}`")
    return problems
