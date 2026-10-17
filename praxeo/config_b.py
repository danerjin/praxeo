"""Configuration B (plan 5.2): typed questions in a loop, with no symbolic engine.

The price-ceiling rules of rules/price_controls.lp, written as steps. A step
names the earlier steps it needs and is asked only if they all held. A step with
an assumption asks its noul question and holds if P(yes) >= 0.5; a step without
one holds as soon as its prerequisites do. A held step with effects gives
consequences, and every question asked goes into the log.

Not covered: exception/2 facts and the facts of unclear readings, which
Configuration A takes as extra input. The CR-12 total is formed by the same
combiner as Configuration A, applied to B's output.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal, Optional

from . import engine
from .combiner import combine
from .decider import Decider
from .questions import ASSUMPTION_TEXT, ceiling_questions
from .schema import HORIZON_ORDER, Assumption, Component, Consequence, PolicyRecord, Step

Role = Literal["bound", "protected", "excluded", "keepers", "displaced"]


@dataclass(frozen=True)
class Effect:
    """One effect/7 line of the rule base: the role it reaches, what moves, which way, when, how visibly."""
    role: Role
    variable: str
    sign: str
    horizon: str
    visibility: str
    tier: str = "B"


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
    BStep("displaced_leave", "PC-21", "displaced_leave", needs=("reclassify", "would_leave"),
          effects=(Effect("displaced", "relocation_out_of_area", "increase", "long", "invisible"),)),
    # CR-12: asked only when both subclass chains held; the combiner needs it to choose a total.
    BStep("keepers_dominate", "CR-12", "keepers_dominate", needs=("stay_in_area", "displaced_leave"),
          assumption="keepers_dominate"),
]


def _actor(comp: Component, role: Role) -> Optional[str]:
    """The actor class a role names in this component, as engine.facts() names it; None if no protected class."""
    if role == "bound":
        return comp.bound_actor
    if role == "excluded":
        return comp.excluded_actor or "buyers.prospective"
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
    by_id = {s.id: s for s in STEPS}
    cons: list[Consequence] = []
    log: list[dict] = []
    for comp in record.components:
        if comp.instrument != "price_ceiling":
            continue
        c = engine._atom(comp.id)
        questions = {q.assumption: q for q in ceiling_questions(comp)}
        held: dict[str, bool] = {}
        for step in STEPS:
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
        for step in STEPS:
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
                    id=f"C-{len(cons) + 1}", actor_class=actor, variable=eff.variable, sign=eff.sign,
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
        for q in ceiling_questions(comp):
            a = decider.answer(q, record)
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            assumptions[atom] = Assumption(id=atom, text=ASSUMPTION_TEXT[q.assumption],
                                           assumption_class=q.assumption_class, p=a.probability)
    cons, _ = engine.run(record, assumptions)
    return combine(cons, assumptions), assumptions


def _key(c: Consequence) -> tuple[str, str, str]:
    return (c.actor_class, c.variable, c.sign)


def compare_a_b(record: PolicyRecord, decider: Decider) -> dict[str, list]:
    """Run both configurations on one record and decider. Compares (actor class, variable, sign) of the
    reported consequences, CR-12 totals included on both sides."""
    a_cons, _ = run_config_a(record, decider)
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
