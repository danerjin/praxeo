"""Configuration B (plan 5.2): typed questions in a loop, with no symbolic engine.

The price-ceiling rules of rules/price_controls.lp, written as steps. A step
names the earlier steps it needs and is asked only if they all held. A step with
an assumption asks its noul question and holds if P(yes) >= 0.5; a step without
one holds as soon as its prerequisites do. A held step with effects gives
consequences, and every question asked goes into the log.

Not covered: exception/2 facts and the facts of unclear readings, which
Configuration A takes as extra input. The CR-12 totals are formed by the same
combiner as Configuration A, applied to B's output.

Not implemented in B (the capabilities added to Configuration A after B was built):
- per-window timing (RS-8: the announcement-window rush and the "first months" total, and the questions
  window_repricing and counterfactual_catches_up that they rest on);
- group signs (at_least_one_increase / at_least_one_decrease), which only the tax and tariff rules use;
- the in-place CR-12 comparisons that settle the capped price against the announcement-window rush.
`compare_a_b` therefore restricts the agreement check to rows without a window and without a group sign. B
does implement the ordinary rows added with them (the displaced holders' turnover, the two items of the sellers'
resources and their CR-12 total, the buyers' resources, the quality-adjusted price total, and taxpayers' funding of
a board paid from the general budget).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal, Optional

from . import engine
from .combiner import combine
from .decider import Decider
from .questions import ASSUMPTION_TEXT, ceiling_questions, questions_for
from .schema import HORIZON_ORDER, Assumption, Component, Consequence, PolicyRecord, Step

Role = Literal["bound", "protected", "excluded", "keepers", "displaced", "neighbor", "enforcer", "taxpayer"]


@dataclass(frozen=True)
class Effect:
    """One effect/7 line of the rule base: the role it reaches, what moves, which way, when, how visibly."""
    role: Role
    variable: str
    sign: str
    horizon: str
    visibility: str
    tier: str = "B"
    item: Optional[str] = None  # one item of a variable that opposite chains move (CR-12 0.8)


@dataclass(frozen=True)
class BStep:
    """One step of the chain. `assumption` is the atom its question estimates; `concl` names it in derivations."""
    id: str
    rule: str
    concl: str
    needs: tuple[str, ...] = ()
    assumption: Optional[str] = None
    effects: tuple[Effect, ...] = ()
    guard: Callable[[Component], bool] = lambda comp: True  # record condition, e.g. "not decontrol"


# The price-ceiling rules, in an order where every step comes after the steps it needs.
STEPS: list[BStep] = [
    BStep("binding", "PC-1", "binding", assumption="binding"),
    BStep("enforced", "PC-1", "enforced", needs=("binding",), assumption="enforced"),
    BStep("cap", "PC-1", "binding_cap", needs=("binding", "enforced")),
    BStep("excess_demand", "PC-1", "excess_demand", needs=("cap",),
          guard=lambda c: not c.vacancy_decontrol,
          effects=(Effect("excluded", "excess_demand", "increase", "short", "invisible"),)),
    BStep("insider_gain", "PC-3", "insider_gain", needs=("cap",),
          effects=(Effect("protected", "price_paid", "decrease", "medium", "visible"),)),
    BStep("substitutes", "RS-4", "substitutes", needs=("cap",), assumption="substitutes"),
    BStep("outsider_price", "PC-3", "outsider_price", needs=("cap", "substitutes"),
          effects=(Effect("excluded", "price_substitute", "increase", "long", "invisible"),)),
    BStep("alternative_uses", "PC-5", "alternative_uses", needs=("cap",), assumption="alternative_uses"),
    BStep("supply_falls", "PC-5", "supply_falls", needs=("cap", "alternative_uses"),
          effects=(Effect("bound", "quantity_supplied", "decrease", "long", "invisible"),)),
    BStep("reclassify", "RS-5", "reclassify", needs=("cap", "alternative_uses"),
          effects=(Effect("bound", "reclassification", "increase", "long", "invisible"),)),
    BStep("nontransferable", "PC-7", "nontransferable", needs=("cap",), assumption="nontransferable"),
    BStep("displaced_move", "CR-9", "displaced_move", needs=("reclassify", "nontransferable"),
          effects=(Effect("displaced", "turnover", "increase", "medium", "invisible"),)),
    BStep("buyouts_limited", "PC-7", "buyouts_limited", needs=("cap",), assumption="buyouts_limited"),
    BStep("turnover", "PC-7", "turnover_falls", needs=("cap", "nontransferable", "buyouts_limited"),
          effects=(Effect("protected", "turnover", "decrease", "medium", "invisible"),)),
    BStep("initial_price", "PC-1", "initial_price", needs=("turnover",),
          guard=lambda c: c.vacancy_decontrol,
          effects=(Effect("excluded", "price_paid", "increase", "medium", "invisible"),)),
    BStep("would_leave", "PC-21", "would_leave", needs=("cap",), assumption="would_leave"),
    BStep("lockin_dominates", "PC-21", "lockin_dominates", needs=("turnover",), assumption="lockin_dominates"),
    BStep("stay_in_area", "PC-21", "stay_in_area", needs=("turnover", "would_leave", "lockin_dominates"),
          effects=(Effect("keepers", "relocation_out_of_area", "decrease", "medium", "invisible"),)),
    BStep("displaced_leave", "PC-21", "displaced_leave", needs=("reclassify", "nontransferable", "would_leave"),
          effects=(Effect("displaced", "relocation_out_of_area", "increase", "long", "invisible"),)),
    # CR-12: asked only when both subclass chains held; the combiner needs it to choose a total.
    BStep("keepers_dominate", "CR-12", "keepers_dominate", needs=("stay_in_area", "displaced_leave"),
          assumption="keepers_dominate"),
    # PC-2 (1.4): rationing members, only where there is excess demand (so not under vacancy decontrol)
    BStep("search_open", "PC-2", "search_open", needs=("excess_demand",), assumption="search_open"),
    BStep("search_rationing", "PC-2", "search_rationing", needs=("excess_demand", "search_open"),
          effects=(Effect("excluded", "search_cost", "increase", "short", "invisible"),)),
    BStep("selection_open", "PC-2", "selection_open", needs=("excess_demand",), assumption="selection_open"),
    BStep("selection_rationing", "PC-2", "selection_rationing", needs=("excess_demand", "selection_open"),
          effects=(Effect("excluded", "allocation_by_non_price_criteria", "increase", "short", "invisible"),)),
    # PC-4 with RS-2
    BStep("quality_adjustable", "RS-2", "quality_adjustable", needs=("cap",), assumption="quality_adjustable"),
    BStep("quality_falls", "PC-4", "quality_falls", needs=("cap", "quality_adjustable"),
          effects=(Effect("protected", "quality_per_unit", "decrease", "short", "invisible"),
                   Effect("bound", "maintenance_spending", "decrease", "short", "invisible"))),
    # PC-6 with RS-3, then RS-10
    BStep("evasion", "RS-3", "evasion", needs=("cap",), assumption="evasion"),
    BStep("informal", "PC-6", "informal", needs=("cap", "evasion")),
    BStep("seeker_side_payments", "PC-6", "seeker_side_payments", needs=("informal",),
          effects=(Effect("excluded", "side_payments", "increase", "short", "invisible"),),
          guard=lambda c: not c.vacancy_decontrol),
    BStep("sublet", "PC-6", "sublet", needs=("informal", "nontransferable"),
          effects=(Effect("protected", "informal_activity", "increase", "short", "invisible"),)),
    BStep("no_recourse", "RS-10", "no_recourse", needs=("informal",),
          effects=(Effect("excluded", "disputes_settled_outside_courts", "increase", "short", "invisible"),)),
    # RS-11 (with PC-7)
    BStep("opportunities_need_move", "RS-11", "opportunities_need_move", needs=("turnover",),
          assumption="opportunities_need_move"),
    BStep("job_lock", "RS-11", "job_lock", needs=("turnover", "opportunities_need_move"),
          effects=(Effect("protected", "job_changes", "decrease", "medium", "invisible"),)),
    # RS-7
    BStep("can_organize", "RS-7", "can_organize", needs=("cap",), assumption="can_organize"),
    BStep("lobbying", "RS-7", "lobbying", needs=("cap", "can_organize"),
          effects=(Effect("bound", "lobbying_effort", "increase", "medium", "invisible"),)),
    BStep("lobbying_protected", "RS-7", "lobbying_protected", needs=("lobbying",),
          guard=lambda c: c.protected_concentrated,
          effects=(Effect("protected", "lobbying_effort", "increase", "medium", "invisible"),)),
    # PC-16 and OC-4
    BStep("transfer", "PC-16", "transfer", needs=("insider_gain",),
          effects=(Effect("bound", "net_price_received", "decrease", "medium", "invisible"),)),
    BStep("rent_forgone", "CR-8", "rent_forgone", needs=("transfer",),
          effects=(Effect("bound", "resources_available_other_uses", "decrease", "medium", "invisible", item="rent_forgone"),)),
    BStep("rent_kept", "CR-8", "rent_kept", needs=("insider_gain",),
          effects=(Effect("protected", "resources_available_other_uses", "increase", "medium", "visible"),)),
    BStep("key_money", "CR-8", "key_money", needs=("informal",),
          effects=(Effect("bound", "resources_available_other_uses", "increase", "medium", "invisible", item="key_money"),),
          guard=lambda c: not c.evasion_by_resellers),
    BStep("prevented", "OC-4", "prevented", needs=("supply_falls",),
          effects=(Effect("excluded", "quantity_traded", "decrease", "medium", "invisible"),
                   Effect("bound", "quantity_traded", "decrease", "medium", "invisible"))),
    # SB-4
    BStep("durable_assets", "SB-4", "durable_assets", needs=("cap",), assumption="durable_assets"),
    BStep("expected_to_last", "SB-4", "expected_to_last", needs=("cap",), assumption="expected_to_last"),
    BStep("capitalized", "SB-4", "capitalized", needs=("cap", "durable_assets", "expected_to_last"),
          effects=(Effect("bound", "asset_value", "decrease", "short", "invisible"),)),
    # OC-3
    BStep("administered", "OC-3", "administered", needs=("cap",),
          effects=(Effect("enforcer", "enforcement_cost", "increase", "short", "invisible", "A"),)),
    # OC-3 with OC-1: taxpayers fund a board paid from the general budget, if the budget rises with the task
    BStep("enforcement_budget_raised", "OC-3", "enforcement_budget_raised", needs=("administered",),
          assumption="enforcement_budget_raised", guard=lambda c: c.general_budget),
    BStep("ceiling_funded", "OC-3", "ceiling_funded", needs=("administered", "enforcement_budget_raised"),
          guard=lambda c: c.general_budget,
          effects=(Effect("taxpayer", "resources_available_other_uses", "decrease", "short", "invisible"),)),
    # RS-4 with PC-3, only when the record names a neighbouring market
    BStep("commutable", "RS-4", "commutable", needs=("cap",), assumption="commutable",
          guard=lambda c: c.neighbor_actor is not None),
    BStep("cross_boundary", "RS-4", "cross_boundary", needs=("cap", "commutable"),
          guard=lambda c: c.neighbor_actor is not None,
          effects=(Effect("neighbor", "price_paid", "increase", "medium", "invisible"),)),
    # PC-5 with RS-5 and CR-4; OC-2
    BStep("relet_obstructs", "PC-5", "relet_obstructs", needs=("reclassify",), assumption="relet_obstructs"),
    BStep("held_vacant", "PC-5", "held_vacant", needs=("reclassify", "relet_obstructs"),
          effects=(Effect("bound", "units_held_vacant", "increase", "medium", "invisible"),)),
    BStep("exit_process", "OC-2", "exit_process", needs=("reclassify",), assumption="exit_process"),
    BStep("process_cost", "OC-2", "process_cost", needs=("reclassify", "exit_process"),
          effects=(Effect("bound", "compliance_cost", "increase", "medium", "invisible"),)),
]


# Patterns of rules/ceiling_extensions.lp that Configuration A and B both carry (added after the out-of-sample runs on
# WE-005, WE-006 and WE-067). Kept apart from STEPS, which mirrors rules/price_controls.lp (test_config_b checks that).
# Not mirrored in B: the group form of PC-2 (B has no group signs) and PC-12 (it needs a record field and two further questions).
EXTENSION_STEPS: list[BStep] = [
    BStep("demand_rises", "LW-3", "demand_rises", needs=("excess_demand",),
          effects=(Effect("excluded", "quantity_demanded", "increase", "short", "invisible"),)),
    BStep("informal_buyers", "PC-6", "informal_buyers", needs=("informal",),
          guard=lambda c: not c.vacancy_decontrol,
          effects=(Effect("excluded", "informal_activity", "increase", "short", "invisible"),)),
]


def _actor(comp: Component, role: Role) -> Optional[str]:
    """The actor class a role names in this component, as engine.facts() names it; None if no protected class."""
    if role == "bound":
        return comp.bound_actor
    if role == "excluded":
        return comp.excluded_actor or "buyers.prospective"
    if role == "neighbor":
        return comp.neighbor_actor
    if role == "enforcer":
        return comp.enforcer_actor
    if role == "taxpayer":
        return comp.taxpayer_actor
    if comp.protected_actor is None:
        return None
    return comp.protected_actor if role == "protected" else f"{comp.protected_actor}.{role}"


def _ancestors(step_id: str, by_id: dict[str, BStep]) -> list[str]:
    """The steps a step rests on, earlier ones first, then the step itself."""
    out: list[str] = []

    def visit(sid: str) -> None:
        if sid in out:
            return
        for n in by_id[sid].needs:
            visit(n)
        out.append(sid)

    visit(step_id)
    return out


def run_config_b(record: PolicyRecord, decider: Decider) -> tuple[list[Consequence], list[dict]]:
    """Walk the steps for each price ceiling. Returns the consequences of the held chains and a log of every question asked."""
    all_steps = STEPS + EXTENSION_STEPS
    by_id = {s.id: s for s in all_steps}
    cons: list[Consequence] = []
    log: list[dict] = []
    for comp in record.components:
        if comp.instrument != "price_ceiling":
            continue
        c = engine._atom(comp.id)
        questions = {q.assumption: q for q in ceiling_questions(comp)}
        held: dict[str, bool] = {}
        for step in all_steps:
            if not step.guard(comp) or not all(held.get(n, False) for n in step.needs):
                held[step.id] = False
                continue
            if step.assumption is None:
                held[step.id] = True
                continue
            q = questions[step.assumption]
            ans = decider.answer(q, record)
            held[step.id] = ans.probability >= engine.CUTOFF
            log.append({"component": comp.id, "step": step.id, "question": q.model_dump(),
                        "answer": ans.model_dump(), "held": held[step.id]})
        for step in all_steps:
            if not held[step.id] or not step.effects:
                continue
            chain = _ancestors(step.id, by_id)
            derivation = [Step(rule=by_id[s].rule, conclusion=f"{by_id[s].concl}({c})",
                               premises=[f"{by_id[n].concl}({c})" for n in by_id[s].needs])
                          for s in chain if by_id[s].assumption is None]
            assumed = sorted(f"{by_id[s].assumption}({c})" for s in chain if by_id[s].assumption)
            for eff in step.effects:
                actor = _actor(comp, eff.role)
                if actor is None:
                    continue
                cons.append(Consequence(
                    id=f"C-{len(cons) + 1}", actor_class=actor, variable=eff.variable, sign=eff.sign, item=eff.item,
                    horizon=[h for h in HORIZON_ORDER if HORIZON_ORDER[h] >= HORIZON_ORDER[eff.horizon]],
                    # plan 5.2: Configuration B yields a decision trail, not a proof, so its results are Tier J
                    visibility=eff.visibility, tier="J", derivation=derivation,
                    assumption_sets=[assumed], assumptions=assumed, reported=True,
                ))
    return cons, log


def assumptions_from_log(log: list[dict]) -> dict[str, Assumption]:
    """The assumptions the logged answers estimate, keyed as the engine keys them: atom(component)."""
    out: dict[str, Assumption] = {}
    for e in log:
        q, a = e["question"], e["answer"]
        atom = f"{q['assumption']}({engine._atom(e['component'])})"
        out[atom] = Assumption(id=atom, text=ASSUMPTION_TEXT[q["assumption"]],
                               assumption_class=q["assumption_class"], p=a["probability"])
    return out


def run_config_a(record: PolicyRecord, decider: Decider) -> tuple[list[Consequence], dict[str, Assumption]]:
    """Configuration A on the same questions: every ceiling question answered, the engine run, then the CR-12 combiner."""
    assumptions: dict[str, Assumption] = {}
    for comp in record.components:
        if comp.instrument != "price_ceiling":
            continue
        for q, assumed in questions_for(comp):
            a = decider.answer(q, record)
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            assumptions[atom] = Assumption(id=atom, text=assumed, assumption_class=q.assumption_class, p=a.probability)
    cons, _ = engine.run(record, assumptions)
    return combine(cons, assumptions), assumptions


def _key(c: Consequence) -> tuple[str, str, str]:
    return (c.actor_class, c.variable, c.sign)


def _comparable(c: Consequence) -> bool:
    """Rows both configurations can produce: B has no per-window timing and no group signs (see the module docstring)."""
    return c.window is None and not c.group


def compare_a_b(record: PolicyRecord, decider: Decider) -> dict[str, list]:
    """Run both configurations on one record and decider. Compares (actor class, variable, sign) of the
    reported consequences, CR-12 totals included on both sides. Rows with a window or a group sign are left out
    of the comparison: Configuration B does not implement them."""
    a_cons, _ = run_config_a(record, decider)
    a_cons = [c for c in a_cons if _comparable(c)]
    b_cons, log = run_config_b(record, decider)
    b_cons = combine(b_cons, assumptions_from_log(log))
    a = {_key(c) for c in a_cons if c.reported}
    b = {_key(c) for c in b_cons if c.reported}
    return {
        "agree": sorted(a & b),
        "only_a": sorted(a - b),
        "only_b": sorted(b - a),
        "a_unreported": sorted(_key(c) for c in a_cons if not c.reported),
    }
