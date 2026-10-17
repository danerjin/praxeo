"""Command line: python -m praxeo CASE_DIR [--parser fixture|llm] [--decider fixture|llm|human] [--out DIR]"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

from . import parser as P
from .decider import FixtureDecider, HumanDecider, LLMDecider
from .pipeline import run_case


def main() -> None:
    ap = argparse.ArgumentParser(prog="praxeo")
    ap.add_argument("case", type=Path)
    ap.add_argument("--parser", choices=["fixture", "llm"], default="fixture")
    ap.add_argument("--decider", choices=["fixture", "llm", "human"], default="fixture")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()

    text = (a.case / "policy.txt").read_text()
    record = P.parse_fixture(a.case / "record.json") if a.parser == "fixture" else P.parse_llm(text)
    decider = {"fixture": lambda: FixtureDecider(a.case / "answers.json"),
               "llm": LLMDecider, "human": HumanDecider}[a.decider]()
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = a.out or Path("runs") / f"{a.case.name}-{a.parser}-{a.decider}-{stamp}"
    result = run_case(a.case, record, decider, out)
    s = result["score"]["headline"]
    print(json.dumps({"out": str(out), "precision": s["precision"], "recall": s["recall"], "f1": s["f1"],
                      "brier": result["score"]["brier"]["mean"]}, indent=1))


if __name__ == "__main__":
    main()
