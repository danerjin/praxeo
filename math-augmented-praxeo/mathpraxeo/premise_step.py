"""The premise step: put annex evidence for dominance premises to a decider.

For each dominance premise in a praxeo prediction that the annex inputs can size
(`bridge.dominance_evidence`), and whose proposed probability differs from the
current one, a typed noul question goes to a `praxeo` Decider (fixture, LLM, human,
or later Jev). The decider's answer is its probability for the premise itself. The
proposal is never applied on its own.

The step writes:
- a log of every proposal, the decider's answer, and whether it changed the premise;
- an annex-informed prediction, re-derived by the `praxeo` engine, combiner and
  verifier with the accepted probabilities. It sits beside the frozen original and
  never replaces it. Every consequence whose reported status or sign differs from
  the original is listed and labelled, with the evidence behind it.

Signs still come only from the praxeological rules: the step changes a premise's
probability, which can move a consequence across the 0.5 cut-off or decide a CR-12
total through its dominance premise, exactly as any other evidence for a premise would.
"""
from __future__ import annotations

import copy
from dataclasses import asdict, dataclass

from praxeo import engine
from praxeo.combiner import combine
from praxeo.explainer import explain
from praxeo.schema import Assumption, PolicyRecord, Question
from praxeo.verifier import verify

from .bridge import AnnexInputs, PremiseEvidence, dominance_evidence

DOMINANCE_PREFIXES = ("keepers_dominate", "lockin_dominates")


@dataclass
class StepRecord:
    evidence: PremiseEvidence
    question: dict
    answer: dict | None
    new_p: float


def question_for(ev: PremiseEvidence, text: str) -> Question:
    return Question(
        id=f"annex_premise.{ev.premise}",
        kind="noul",
        text=(f"Premise `{ev.premise}`: \"{text}\" Its current probability is {ev.current_p:.2f}. "
              f"Evidence from the mathematical annex ({ev.rung}, not praxeological): {ev.basis}. "
              f"The annex proposes p = {ev.proposed_p:.2f}. Taking this evidence into account with everything "
              f"else you know about the case as it stood at enactment, what is your probability that the premise holds?"),
        assumption=ev.premise,
        assumption_class="other",
    )


def run(prediction: dict, inputs: AnnexInputs, decider) -> tuple[list[StepRecord], dict]:
    """Return the step log and the annex-informed prediction (the original dict is not modified)."""
    original = copy.deepcopy(prediction)
    record = PolicyRecord.model_validate(prediction["record"])
    assumptions = {k: Assumption(**v) for k, v in prediction["assumptions"].items()}

    log: list[StepRecord] = []
    for atom, a in assumptions.items():
        if not atom.startswith(DOMINANCE_PREFIXES):
            continue
        ev = dominance_evidence(inputs, atom, a.p)
        if ev is None or ev.proposed_p == ev.current_p:
            if ev is not None:
                log.append(StepRecord(ev, {}, None, a.p))
            continue
        q = question_for(ev, a.text)
        ans = decider.answer(q, record)
        ev.accepted = abs(ans.probability - a.p) > 1e-9
        log.append(StepRecord(ev, q.model_dump(), ans.model_dump(), ans.probability))

    updated = {k: v.model_copy(update={"p": next((r.new_p for r in log if r.evidence.premise == k), v.p)})
               for k, v in assumptions.items()}
    cons, _ = engine.run(record, updated)
    cons = combine(cons, updated)
    informed = copy.deepcopy(prediction)
    informed["assumptions"] = {k: v.model_dump() for k, v in updated.items()}
    informed["consequences"] = [c.model_dump() for c in cons]
    informed["explanations"] = [explain(c, updated, record) for c in cons]
    informed["verifier_problems"] = verify(cons, updated, record)
    informed["annex_informed"] = {
        "premises_changed": [r.evidence.premise for r in log if r.evidence.accepted],
        "differences": _differences(prediction["consequences"], informed["consequences"], log),
        "note": "Annex-informed variant. The frozen original prediction is the one scored; this one is reported beside it.",
    }
    if prediction != original:
        raise RuntimeError("the premise step changed the original prediction")
    return log, informed


def _differences(before: list[dict], after: list[dict], log: list[StepRecord]) -> list[dict]:
    # a window, an item or a group makes a different consequence of the same actor and variable
    key = lambda c: (c["actor_class"], c["variable"], c.get("window"), c.get("item"), tuple(c.get("group", [])))  # noqa: E731
    b = {key(c): c for c in before}
    basis = "; ".join(r.evidence.basis for r in log if r.evidence.accepted)
    out = []
    for c in after:
        o = b.get(key(c))
        if o is None or o["sign"] != c["sign"] or o["reported"] != c["reported"]:
            out.append({"actor_class": c["actor_class"], "variable": c["variable"],
                        "before": None if o is None else {"sign": o["sign"], "reported": o["reported"]},
                        "after": {"sign": c["sign"], "reported": c["reported"]},
                        "label": "annex-informed (premise probability changed on annex evidence)",
                        "evidence": basis})
    return out


def log_markdown(case: str, log: list[StepRecord], informed: dict) -> str:
    out = [f"# Premise step: {case}", "",
           "Annex evidence for dominance premises, put to a decider. The decider's answer is the premise's new "
           "probability; a proposal is never applied on its own. The frozen original prediction is unchanged.", "",
           "| Premise | Current p | Annex rung | Proposed p | Decider | Decider's p | Changed |", "|---|---|---|---|---|---|---|"]
    for r in log:
        dec = r.answer["decider"] if r.answer else "(not asked: no change proposed)"
        out.append(f"| `{r.evidence.premise}` | {r.evidence.current_p:.2f} | {r.evidence.rung} | {r.evidence.proposed_p:.2f} | "
                   f"{dec} | {r.new_p:.2f} | {'yes' if r.evidence.accepted else 'no'} |")
    out += ["", "Evidence:", ""] + [f"- `{r.evidence.premise}`: {r.evidence.basis}" for r in log]
    diffs = informed["annex_informed"]["differences"]
    out += ["", "Consequences that differ in the annex-informed variant:", ""]
    out += [f"- {d['actor_class']}, {d['variable']}: {d['before']} -> {d['after']} ({d['label']})" for d in diffs] or ["- none"]
    return "\n".join(out) + "\n"


def dump_log(log: list[StepRecord]) -> list[dict]:
    return [asdict(r) for r in log]
