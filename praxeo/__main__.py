"""Command line: python -m praxeo CASE_DIR [--engine auto|core|patterns] [--parser fixture|llm] [--proposer fixture|llm]
                                       [--enrichment PATH] [--decider fixture|llm|human] [--out DIR]
                                       [--thresholds PATH --fallback fixture|human|llm [--fallback-answers PATH]]

The core path (praxeo/core) is the default: the seed, the expand loop and the core rules. `auto` uses it whenever the case has
core inputs (loop/seed.json, or a one-shot situation.json) or the parser is the LLM; otherwise it falls back to the pattern
engine."""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from . import parser as P
from .context import load_sources, split
from .decider import FixtureDecider, HumanDecider, LLMDecider
from .escalation import EscalatingDecider, Thresholds, load_thresholds
from .pipeline import run_case


def main() -> None:
    ap = argparse.ArgumentParser(prog="praxeo")
    ap.add_argument("case", type=Path)
    ap.add_argument("--engine", choices=["auto", "core", "patterns"], default="auto")
    ap.add_argument("--proposer", choices=["fixture", "llm"], default="fixture", help="core path: who proposes each node's facts")
    ap.add_argument("--parser", choices=["fixture", "llm"], default="fixture")
    ap.add_argument("--decider", choices=["fixture", "llm", "human"], default="fixture")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--enrichment", type=Path, help="related markets from the context sources as JSON (parser.Enrichment), "
                    "in place of the LLM enrichment step; quotes are checked against sources.json")
    ap.add_argument("--thresholds", type=Path, help="JSON confidence thresholds (praxeo/escalation.py); needs --fallback")
    ap.add_argument("--fallback", choices=["fixture", "human", "llm"], help="decider for questions below threshold")
    ap.add_argument("--fallback-answers", type=Path, help="answers file for --fallback fixture")
    a = ap.parse_args()
    if a.thresholds and not a.fallback:
        ap.error("--thresholds needs --fallback")
    if a.fallback == "fixture" and not a.fallback_answers:
        ap.error("--fallback fixture needs --fallback-answers")
    if a.fallback_answers and a.fallback != "fixture":
        ap.error("--fallback-answers only applies to --fallback fixture")

    if a.engine != "patterns":
        from .core import pipeline as CP
        found = CP.inputs(a.case) if a.parser == "fixture" else None
        if a.engine == "core" or found or a.parser == "llm":
            run_core(a, found)
            return

    text = (a.case / "policy.txt").read_text()
    record = P.parse_fixture(a.case / "record.json") if a.parser == "fixture" else P.parse_llm(text)
    # enrichment (plan 5.3): related markets from the sources dated before enactment, each quote checked in the pipeline
    kept, _ = split(record, load_sources(a.case / "sources.json"))
    if a.enrichment:
        record = P.enrich(record, P.Enrichment.model_validate_json(a.enrichment.read_text()))
    elif a.parser == "llm":
        record = P.enrich_llm(record, kept)
    decider = {"fixture": lambda: FixtureDecider(a.case / "answers.json"),
               "llm": LLMDecider, "human": HumanDecider}[a.decider]()
    if a.fallback:
        fallback = {"fixture": lambda: FixtureDecider(a.fallback_answers),
                    "llm": LLMDecider, "human": HumanDecider}[a.fallback]()
        thresholds = load_thresholds(a.thresholds) if a.thresholds else Thresholds()
        decider = EscalatingDecider(decider, fallback, thresholds)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = a.out or Path("runs") / f"{a.case.name}-{a.parser}-{a.decider}-{stamp}"
    result = run_case(a.case, record, decider, out)
    if result["score"] is None:
        print(json.dumps({"out": str(out), "scored": False, "consequences": len(result["prediction"]["consequences"])}, indent=1))
        return
    s = result["score"]["headline"]
    print(json.dumps({"out": str(out), "precision": s["precision"], "recall": s["recall"], "f1": s["f1"],
                      "brier": result["score"]["brier"]["mean"]}, indent=1))


def run_core(a, found) -> None:
    from .core import expand as X, pipeline as CP
    from .core.seed import parse_seed_llm
    text = (a.case / "policy.txt").read_text()
    if a.parser == "llm":
        seed, proposer, decider = parse_seed_llm(text), None, None
    elif found:
        seed, proposer, decider = found
    else:
        raise SystemExit(f"{a.case}: no core inputs (loop/seed.json or situation.json); use --parser llm or --engine patterns")
    if a.proposer == "llm" or proposer is None:
        proposer = X.LLMProposer()
    if a.decider == "llm" or decider is None:
        decider = LLMDecider()
    elif a.decider == "human":
        decider = HumanDecider()
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = a.out or Path("runs") / f"{a.case.name}-core-{stamp}"
    pred = CP.run_case(a.case, out, seed, proposer, decider)
    print(json.dumps({"out": str(out), "engine": "core", "rounds": pred["loop"]["rounds"],
                      "consequences": sum(1 for c in pred["consequences"] if c["reported"]),
                      "verifier_problems": len(pred["verifier_problems"])}, indent=1))


if __name__ == "__main__":
    main()
