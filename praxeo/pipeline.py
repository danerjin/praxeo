"""End-to-end run: text -> record -> typed questions -> engine -> explanations -> frozen log -> score.

The predictions and assumption estimates are written and hashed before the
outcome card is opened (plan 7.3, rule 1).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

from . import RULEBASE_VERSION, engine, parser
from .decider import Decider
from .explainer import explain
from .questions import ASSUMPTION_TEXT, ceiling_questions
from .schema import Assumption, OutcomeCard, PolicyRecord
from .scoring import score


def predict(text: str, record: PolicyRecord, decider: Decider) -> dict:
    citation_problems = parser.check_citations(record, text)
    answers, assumptions = [], {}
    for comp in record.components:
        if comp.instrument != "price_ceiling":
            continue
        for q in ceiling_questions(comp):
            a = decider.answer(q, record)
            answers.append({"question": q.model_dump(), "answer": a.model_dump()})
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            assumptions[atom] = Assumption(id=atom, text=ASSUMPTION_TEXT[q.assumption],
                                           assumption_class=q.assumption_class, p=a.probability)
    consequences, program = engine.run(record, assumptions)
    return {
        "rulebase_version": RULEBASE_VERSION,
        "record": record.model_dump(),
        "citation_problems": citation_problems,
        "unclear": [u.model_dump() for u in record.unclear],
        "questions": answers,
        "assumptions": {k: v.model_dump() for k, v in assumptions.items()},
        "engine_facts": program,
        "consequences": [c.model_dump() for c in consequences],
        "explanations": [explain(c, assumptions, record) for c in consequences],
    }


def run_case(case: Path, record: PolicyRecord, decider: Decider, out: Path) -> dict:
    text = (case / "policy.txt").read_text()
    out.mkdir(parents=True, exist_ok=True)
    prediction = predict(text, record, decider)
    prediction["run_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    prediction["decider"] = decider.name
    frozen = json.dumps(prediction, indent=1, sort_keys=True)
    (out / "prediction.json").write_text(frozen)
    digest = hashlib.sha256(frozen.encode()).hexdigest()

    # only now is the outcome card opened
    from .schema import Consequence
    card = OutcomeCard.model_validate_json((case / "outcome_card.json").read_text())
    consequences = [Consequence(**c) for c in prediction["consequences"]]
    assumptions = {k: Assumption(**v) for k, v in prediction["assumptions"].items()}
    scores = score(consequences, assumptions, card)
    scores["prediction_sha256"] = digest
    (out / "score.json").write_text(json.dumps(scores, indent=1))
    (out / "report.md").write_text(report(prediction, scores, card))
    return {"prediction": prediction, "score": scores}


def _pct(x):
    return "n/a" if x is None else f"{x:.2f}"


def report(pred: dict, scores: dict, card: OutcomeCard) -> str:
    rec = pred["record"]
    lines = [
        f"# Thin-slice run: {rec['name']}",
        "",
        f"Rule base: {pred['rulebase_version']}  |  Decider: {pred['decider']}  |  Run: {pred['run_at']}",
        f"Prediction log sha256 (frozen before the outcome card was opened): `{scores['prediction_sha256'][:16]}…`",
        "",
        "## Policy record",
        "",
        f"- Rule-maker: {rec['rule_maker']}; enacted {rec['enacted']}, effective {rec['effective']}.",
        f"- Stated aim: {rec.get('stated_aim') or 'none stated'}",
    ]
    for c in rec["components"]:
        lines.append(f"- {c['id']}: {c['instrument']} on {c['good']} in {c['market']}; binds {c['bound_actor']}, "
                     f"protects {c.get('protected_actor')}. Source: \"{c['source_sentences'][0]}\"")
    for u in pred["unclear"]:
        lines.append(f"- Unclear {u['id']}: {u['text']} Readings: " + " / ".join(u["readings"]))
    if pred["citation_problems"]:
        lines.append("- Citation check: " + "; ".join(pred["citation_problems"]))
    else:
        lines.append("- Citation check: every quoted source sentence was found in the text.")
    lines += ["", "## Assumptions (estimated before scoring)", "", "| Atom | Class | p | Text |", "|---|---|---|---|"]
    for a in pred["assumptions"].values():
        lines.append(f"| `{a['id']}` | {a['assumption_class']} | {a['p']:.2f} | {a['text']} |")
    lines += ["", "## Consequences", "", "| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |", "|---|---|---|---|---|---|---|---|---|"]
    for c in pred["consequences"]:
        rules = ", ".join(dict.fromkeys(s["rule"] for s in c["derivation"]))
        sets = " or ".join("{" + ", ".join(s) + "}" for s in c["assumption_sets"])
        lines.append(f"| {c['id']} | {c['actor_class']} | {c['variable']} | {c['sign']} | {c['horizon'][0]}+ | {c['tier']} | {rules} | {sets} | {'yes' if c['reported'] else 'no'} |")
    lines += ["", "## Explanations", ""] + [f"- {e}" for e in pred["explanations"]]
    lines += ["", "## Score against the outcome card", "", f"Card: {card.case}. {card.verification}", ""]
    for name in ("headline", "logic"):
        s = scores[name]
        lines.append(f"- **{name.capitalize()}**: precision {_pct(s['precision'])}, recall {_pct(s['recall'])}, F1 {_pct(s['f1'])} "
                     f"({s['predictions']} predictions; {s['verifiable']} verifiable, {s['unverifiable']} unverifiable, {s['ambiguous']} ambiguous; "
                     f"matched {s['matched']}; false positives {s['false_positives']}; missed findings {s['missed_findings']}).")
    b = scores["brier"]
    lines.append(f"- **Assumption Brier score**: {_pct(b['mean'])} over {len(b['items'])} assumption(s) with a recorded status.")
    if scores["low_confidence_findings"]:
        lines.append(f"- Low-confidence findings on the card: {scores['low_confidence_findings']}.")
    lines += ["", "## Card findings", "", "| ID | Actor class | Variable | Type | Sign | Horizon | Magnitude | Confidence |", "|---|---|---|---|---|---|---|---|"]
    for f in card.findings:
        lines.append(f"| {f.id} | {f.actor_class} | {f.variable} | {f.finding_type} | {f.sign} | {', '.join(f.horizon)} | {f.magnitude or ''} | {f.confidence} |")
    lines += ["", "Confounders: " + "; ".join(card.confounders), ""]
    return "\n".join(lines)
