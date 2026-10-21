"""Score decider answers on the control cases against their expected directions.

Usage: python3 tools/score_controls.py ANSWERS_ROOT [LABEL]

ANSWERS_ROOT has one subfolder per control case (cases/controls/<case>), each with answers.json.
Reports, separately for questions whose expected answer is "no" and "yes": how many the decider got on the
right side of 0.5, and the mean probability it gave. A decider biased toward "yes" shows up as errors and high
probabilities on the "no" questions.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTROLS = ROOT / "cases" / "controls"


def score(answers_root: Path) -> dict:
    rows, by = [], {"no": [], "yes": []}
    for case in sorted(p for p in CONTROLS.iterdir() if (p / "expected.json").exists()):
        expected = json.loads((case / "expected.json").read_text())
        f = answers_root / case.name / "answers.json"
        if not f.exists():
            continue  # this run did not cover the case
        answers = {a["question_id"]: a for a in json.loads(f.read_text())}
        for qid, want in expected.items():
            a = answers.get(qid)
            p = None if a is None else float(a["probability"])
            right = p is not None and ((p >= 0.5) == (want == "yes"))
            by[want].append((p, right))
            rows.append((case.name, qid, want, p, right, "" if a is None else a.get("rationale", "")))
    summary = {}
    for want, items in by.items():
        ps = [p for p, _ in items if p is not None]
        summary[want] = {"n": len(items), "right": sum(r for _, r in items),
                         "mean_p": sum(ps) / len(ps) if ps else None}
    return {"rows": rows, "summary": summary}


def markdown(label: str, s: dict) -> str:
    out = [f"## {label}", "", "| Case | Question | Expected | p | Right side |", "|---|---|---|---|---|"]
    for case, qid, want, p, right, _ in s["rows"]:
        out.append(f"| {case} | {qid} | {want} | {'missing' if p is None else f'{p:.2f}'} | {'yes' if right else 'NO'} |")
    out.append("")
    for want in ("no", "yes"):
        m = s["summary"][want]
        mean = "n/a" if m["mean_p"] is None else f"{m['mean_p']:.2f}"
        out.append(f"- Expected {want}: {m['right']} of {m['n']} on the right side of 0.5; mean p {mean}.")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    root = Path(sys.argv[1])
    print(markdown(sys.argv[2] if len(sys.argv) > 2 else root.name, score(root)))
