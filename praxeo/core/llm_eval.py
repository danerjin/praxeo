"""Blind runs of the core path with the LLM in every open role: the seed parser, the proposer and the decider.

Each run sees only what the stand-in writers saw: section 1 of the worked example (the policy record) and its assumption
table's ID, Statement, Type and p columns. The decider is shown the table as context and answers each premise question from
it where a statement matches, else judges. The proposer is given the controlled names with the example excluded from the
count. Output goes to cases/<case>/llm/run_<k>/ (seed, situation, log, rejected proposals, call counts), for scoring with
the same-class mapping the stand-in runs use.

    python -m praxeo.core.llm_eval WE-036 we036_quenby --runs 3
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from .. import llm
from ..schema import PolicyRecord
from . import expand as X

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / "handbook" / "05_examples"

TABLE_NOTE = ("Assumption table of this analysis (ID | Statement | Type | p). Where a question states the same thing as a row, "
              "answer with that row's p; otherwise judge from the policy record.")


def blind_inputs(eid: str) -> tuple[str, str]:
    """Section 1 of the example and its assumption table's four allowed columns, as the blind writers read them."""
    path = next(EXAMPLES.glob(f"{eid}_*.md"))
    md = path.read_text()
    m = re.search(r"^## 1[ .].*?(?=^## 2[ .])", md, re.S | re.M)
    section1 = m.group(0) if m else ""
    rows = []
    for line in md.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and re.fullmatch(r"A-\d+", cells[0]):
            rows.append(" | ".join(cells[:4]))
    return section1, "\n".join(rows)


def run_once(eid: str, case: str, k: int, model: str = "claude-opus-5-5", proposer_effort: str = "high") -> Path:
    from ..decider import LLMDecider
    from .seed import parse_seed_llm

    llm.USAGE.clear()
    section1, table = blind_inputs(eid)
    out = ROOT / "cases" / case / "llm" / f"run_{k}"
    out.mkdir(parents=True, exist_ok=True)
    seed = parse_seed_llm(section1 + "\n\n" + TABLE_NOTE + "\n" + table, model=model, exclude=(eid,))
    (out / "seed.json").write_text(seed.model_dump_json(indent=1))
    proposer = X.LLMProposer(model=model, effort=proposer_effort, exclude=(eid,))
    decider = LLMDecider(model=model)
    record = PolicyRecord(name=seed.name, jurisdiction="-", rule_maker="-", enacted="-", effective="-", components=[],
                          context=[section1, TABLE_NOTE + "\n" + table])
    run = X.expand(seed, proposer, decider, section1, record=record)
    (out / "situation.json").write_text(run.situation.model_dump_json(indent=1))
    (out / "log.json").write_text(json.dumps(run.log, indent=1, default=str))
    (out / "meta.json").write_text(json.dumps({"example": eid, "model": model, "proposer_effort": proposer_effort, "rounds": run.rounds,
                                               "proposer_calls": proposer.calls, "rejected": proposer.rejected,
                                               "questions": sum(1 for e in run.log if "question" in e),
                                               "usage": llm.usage_report(model)}, indent=1))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("example", help="worked example id, e.g. WE-036")
    ap.add_argument("case", help="case folder, e.g. we036_quenby")
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--proposer-effort", default="high", choices=["low", "medium", "high", "xhigh", "max"])
    a = ap.parse_args()
    for k in range(a.start, a.start + a.runs):
        print(run_once(a.example, a.case, k, a.model, a.proposer_effort))


if __name__ == "__main__":
    main()
