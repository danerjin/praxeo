"""The core path end to end (step 5): policy text -> seed (CR-1) -> expand loop (proposer, decider) -> core rules -> CR-12e
-> verifier -> explanations -> frozen log. The pattern engine (praxeo/pipeline.py) is the fallback for cases without core
inputs; the patterns themselves are kept as checks that the core rules re-derive them (tests/test_core_derives_patterns.py).
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import tempfile
from pathlib import Path
from typing import Optional

from .. import vocabulary
from ..engine import CUTOFF
from ..schema import Assumption, Consequence, PolicyRecord
from . import expand as X
from . import situation as S

CORE_VERSION = "core-" + hashlib.sha256(S.CORE_RULES[0].read_bytes()).hexdigest()[:12]

# One sentence per core rule, for the templated explanations (no free text generation).
CR_TEXT = {
    "CR-1": "the policy removes, adds or attaches a cost to an option, or transfers means",
    "CR-4": "an option made worse is taken less and its alternatives more; an option made better, the reverse",
    "CR-5": "trades that would have taken place beyond the line do not, and both sides lose them",
    "CR-6": "a price held off the level that clears the market leaves one side wanting more; the pressure moves to the terms "
            "left free and to choosing by other criteria",
    "CR-7": "returns and asset values follow the change in what a use yields",
    "CR-8": "every payment is a receipt, and resources spent on complying or enforcing serve no other end",
    "CR-9": "a change in one actor's dealings reaches those who trade or compete with it",
    "CR-10": "a change expected in the future alters choices now",
    "CR-11": "information conveyed by the policy changes choices only where it changes beliefs",
    "CR-12": "chains that reach the same actor and variable are combined: the same direction stands, opposite directions are "
             "ambiguous unless a premise settles them",
}


def explain(c: Consequence, assumptions: dict[str, Assumption]) -> str:
    rules = list(dict.fromkeys(s.rule for s in c.derivation))
    who = " or ".join(c.actor_group) if c.actor_group else c.actor_class
    what = " or ".join(c.group) if c.group else c.variable
    when = f" in the {c.window.replace('_', ' ')} window" if c.window else ""
    because = "; ".join(CR_TEXT.get(r, r) for r in rules)
    given = "; ".join(f"{assumptions[a].text} (p {assumptions[a].p:.2f})" for a in c.assumptions if a in assumptions)
    return f"{who}: {what} {c.sign.replace('_', ' ')}{when}, because {because}" + (f", given that {given}" if given else "") + "."


def verify(cons: list[Consequence], assumptions: dict[str, Assumption], situation: S.Situation) -> list[str]:
    """Structural checks on the core output: vocabulary, derivations, estimated premises, the cut-off."""
    problems = []
    for c in cons:
        for v in (c.group or [c.variable]):
            if (msg := vocabulary.check_variable(v)):
                problems.append(f"{c.actor_class}: {msg}")
        if not c.derivation:
            problems.append(f"{c.actor_class} {c.variable}: empty derivation")
        missing = [a for s in c.assumption_sets for a in s if a not in assumptions]
        if missing:
            problems.append(f"{c.actor_class} {c.variable}: premises never estimated {sorted(set(missing))}")
        elif c.assumptions and c.reported != all(assumptions[a].p >= CUTOFF for a in c.assumptions):
            problems.append(f"{c.actor_class} {c.variable}: reported disagrees with the cut-off")
    return problems


def predict(text: str, seed: S.Situation, proposer, decider, record: Optional[PolicyRecord] = None) -> dict:
    """The core path. `record` is only what the decider is shown besides the question (the policy text as context)."""
    record = record or PolicyRecord(name=seed.name, jurisdiction="-", rule_maker="-", enacted="-", effective="-",
                                    components=[], context=[text])
    run = X.expand(seed, proposer, decider, text, record=record)
    a = S.assumptions(run.situation)
    cons = S.run(run.situation)
    return {
        "engine": "core",
        "rulebase_version": CORE_VERSION,
        "seed": seed.model_dump(),
        "situation": run.situation.model_dump(),
        "loop": {"rounds": run.rounds, "log": run.log, "proposer": proposer.name, "decider": getattr(decider, "name", "")},
        "assumptions": {k: v.model_dump() for k, v in a.items()},
        "engine_facts": S.facts(run.situation),
        "consequences": [c.model_dump() for c in cons],
        "verifier_problems": verify(cons, a, run.situation),
        "explanations": [explain(c, a) for c in cons if c.reported],
    }


def inputs(case: Path):
    """The core inputs a case has: (seed, proposer, decider), or None (then the pattern engine is the fallback).
    A loop run (loop/seed.json with proposals and answers) is replayed; a one-shot situation.json is split into a seed and
    the proposals each node makes (expand.split), which the loop reproduces."""
    loop = case / "loop"
    if (loop / "seed.json").exists():
        answers = json.loads((loop / "answers.json").read_text()) if (loop / "answers.json").exists() else {}
        seed = S.load(loop / "seed.json")
        table = {**{v["text"]: v["p"] for v in seed.assumptions.values()}, **answers}
        return seed, X.FixtureProposer(loop / "proposals.json"), X.TextDecider(table, name=f"file:{loop.name}/answers.json")
    if (case / "situation.json").exists():
        full = S.load(case / "situation.json")
        seed, props = X.split(full)
        path = Path(tempfile.mkdtemp()) / "proposals.json"
        path.write_text(json.dumps(props))
        return seed, X.FixtureProposer(path), X.TextDecider({v["text"]: v["p"] for v in full.assumptions.values()}, name="file:situation.json")
    return None


def run_case(case: Path, out: Path, seed: S.Situation, proposer, decider) -> dict:
    text = (case / "policy.txt").read_text() if (case / "policy.txt").exists() else ""
    out.mkdir(parents=True, exist_ok=True)
    pred = predict(text, seed, proposer, decider)
    pred["run_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    frozen = json.dumps(pred, indent=1, sort_keys=True, default=str)
    (out / "prediction.json").write_text(frozen)
    digest = hashlib.sha256(frozen.encode()).hexdigest()
    (out / "report.md").write_text(report(pred, digest))
    return pred


def report(pred: dict, digest: str) -> str:
    lines = [f"# Core-rule run: {pred['seed']['name']}", "",
             f"Rule base: {pred['rulebase_version']}  |  Proposer: {pred['loop']['proposer']}  |  Decider: {pred['loop']['decider']}"
             f"  |  Run: {pred['run_at']}",
             f"Prediction log sha256: `{digest[:16]}…`", "",
             f"- Expand loop: {pred['loop']['rounds']} rounds, {sum(1 for e in pred['loop']['log'] if 'question' in e)} premise questions.",
             "- Verifier: " + ("; ".join(pred["verifier_problems"]) if pred["verifier_problems"] else "no problems."), "",
             "## Assumptions", "", "| Atom | p | Text |", "|---|---|---|"]
    lines += [f"| `{a['id']}` | {a['p']:.2f} | {a['text']} |" for a in pred["assumptions"].values()]
    lines += ["", "## Consequences (reported)", "", "| Actor class | Variable | Sign | Window | Core rules | Assumptions |", "|---|---|---|---|---|---|"]
    for c in pred["consequences"]:
        if not c["reported"]:
            continue
        who = " or ".join(c["actor_group"]) if c.get("actor_group") else c["actor_class"]
        what = " or ".join(c["group"]) if c.get("group") else c["variable"]
        rules = ", ".join(dict.fromkeys(s["rule"] for s in c["derivation"]))
        lines.append(f"| {who} | {what} | {c['sign']} | {c.get('window') or ''} | {rules} | {', '.join(c['assumptions'])} |")
    lines += ["", "## Explanations", ""] + [f"- {e}" for e in pred["explanations"]]
    return "\n".join(lines) + "\n"
