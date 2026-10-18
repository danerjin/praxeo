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
                     "definition_line(", "renewable(", "announced(", "rolled_back(", "taxpayer(")


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
    by_id = {c.id: c for c in consequences}
    named = record_roles(record)
    for c in consequences:
        known = c.actor_class.split(".")[0] in named
        for msg in [vocabulary.check_variable(v) for v in c.members()] + [None if known else vocabulary.check_actor(c.actor_class)]:
            if msg:
                problems.append(f"{c.id}: {msg}")
        if c.group and (len(c.group) < 2 or c.variable != c.group[0] or c.sign not in GROUP_SIGNS and c.sign != "ambiguous"):
            problems.append(f"{c.id}: a group consequence needs two or more members, a group sign (or ambiguous by reading), and its first member as `variable`")
        if c.sign in GROUP_SIGNS and not c.group:
            problems.append(f"{c.id}: group sign `{c.sign}` on a single variable")
        if c.window == "announcement" and c.horizon != ["short"]:
            problems.append(f"{c.id}: an announcement-window consequence has horizon ['short'], not {c.horizon}")
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
