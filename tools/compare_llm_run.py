"""Compare an LLM-produced record and answers with a case's hand-written fixtures, and run the pipeline on them.

Usage: python3 tools/compare_llm_run.py CASE_DIR LLM_DIR OUT_DIR

LLM_DIR holds record.json (parser stage) and answers.json (decider stage) produced by an LLM working only
from the policy text and the stage instructions (for example a subagent standing in for the API). The script
writes OUT_DIR/comparison.md and runs:
  (a) the fixture record with the LLM's answers   -> isolates the decider;
  (b) the LLM's record with the LLM's answers     -> parser and decider together.
The fixture run is the baseline. Outcome cards, where present, score every run the same way.
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from praxeo import parser  # noqa: E402
from praxeo.decider import FixtureDecider  # noqa: E402
from praxeo.pipeline import run_case  # noqa: E402
from praxeo.questions import questions_for  # noqa: E402
from praxeo.schema import PolicyRecord  # noqa: E402

ROLE_FIELDS = ("instrument", "bound_actor", "protected_actor", "excluded_actor", "vacancy_decontrol")


def _rows(result: dict) -> set:
    return {(c["actor_class"], c["variable"], c["sign"]) for c in result["prediction"]["consequences"] if c["reported"]}


def _remap_answers(answers: list[dict], record: PolicyRecord, out: Path) -> Path:
    """Re-key answers by the LLM record's component ids (question ids are '<component>.<atom>')."""
    by_atom = {a["question_id"].split(".", 1)[1]: a for a in answers}
    keyed = []
    for comp in record.components:
        for q, _ in questions_for(comp):
            atom = q.id.split(".", 1)[1]
            if atom in by_atom:
                keyed.append({**by_atom[atom], "question_id": q.id})
    out.write_text(json.dumps(keyed, indent=1))
    return out


def main(case: Path, llm: Path, out: Path) -> None:
    out.mkdir(parents=True, exist_ok=True)
    text = (case / "policy.txt").read_text()
    fixture_record = parser.parse_fixture(case / "record.json")
    lines = [f"# LLM stages against fixtures: {case.name}", "",
             f"LLM outputs from `{llm}`. The fixtures are hand-written; the LLM worked only from the policy text and the stage instructions.", ""]

    # parser stage
    lines += ["## Parser", ""]
    try:
        llm_record = PolicyRecord.model_validate_json((llm / "record.json").read_text())
        problems = parser.check_citations(llm_record, text)
        lines.append(f"- Valid record: yes. Components: {len(llm_record.components)} (fixture {len(fixture_record.components)}). "
                     f"Unclear provisions: {len(llm_record.unclear)} (fixture {len(fixture_record.unclear)}).")
        lines.append("- Citation check: " + ("every quoted sentence found in the text." if not problems else "; ".join(problems)))
        for i, (fc, lc) in enumerate(zip(fixture_record.components, llm_record.components)):
            for f in ROLE_FIELDS:
                fv, lv = getattr(fc, f), getattr(lc, f)
                mark = "same" if fv == lv else "DIFFERS"
                lines.append(f"- Component {i + 1} `{f}`: fixture `{fv}`, LLM `{lv}` ({mark})")
        shutil.copy(llm / "record.json", out / "record.json")
    except Exception as e:  # report, do not hide
        llm_record = None
        lines.append(f"- Record did not validate: {e}")

    # decider stage
    fixture_answers = {a["question_id"]: a for a in json.loads((case / "answers.json").read_text())}
    llm_answers = json.loads((llm / "answers.json").read_text())
    shutil.copy(llm / "answers.json", out / "answers.json")
    lines += ["", "## Decider", "", "| Question | Fixture p | LLM p | Difference | Same side of 0.5 |", "|---|---|---|---|---|"]
    diffs, flips = [], 0
    for a in llm_answers:
        f = fixture_answers.get(a["question_id"])
        if f is None:
            lines.append(f"| {a['question_id']} | (none) | {a['probability']:.2f} | | |")
            continue
        d = a["probability"] - f["probability"]
        same = (a["probability"] >= 0.5) == (f["probability"] >= 0.5)
        flips += not same
        diffs.append(abs(d))
        lines.append(f"| {a['question_id']} | {f['probability']:.2f} | {a['probability']:.2f} | {d:+.2f} | {'yes' if same else 'NO'} |")
    if diffs:
        lines.append(f"\nMean absolute difference {sum(diffs) / len(diffs):.2f}; answers on the other side of the cut-off: {flips}.")

    # pipeline runs
    base = run_case(case, fixture_record, FixtureDecider(case / "answers.json"), out / "run_fixture")
    run_a = run_case(case, fixture_record, FixtureDecider(out / "answers.json"), out / "run_llm_decider")
    runs = [("fixtures (baseline)", base), ("fixture record + LLM answers", run_a)]
    if llm_record is not None:
        remapped = _remap_answers(llm_answers, llm_record, out / "answers_remapped.json")
        try:
            runs.append(("LLM record + LLM answers", run_case(case, llm_record, FixtureDecider(remapped), out / "run_llm_both")))
        except Exception as e:
            lines.append(f"\nThe run on the LLM record failed: {e}")
    lines += ["", "## Pipeline runs", "", "| Run | Reported | Only in this run | Missing vs baseline | F1 | Brier |", "|---|---|---|---|---|---|"]
    b = _rows(base)
    for name, r in runs:
        rows = _rows(r)
        s = r.get("score") or {}
        f1 = s.get("headline", {}).get("f1") if s else None
        brier = s.get("brier", {}).get("mean") if s else None
        lines.append(f"| {name} | {len(rows)} | {sorted(rows - b) or '-'} | {sorted(b - rows) or '-'} | "
                     f"{'n/a' if f1 is None else f'{f1:.2f}'} | {'n/a' if brier is None else f'{brier:.2f}'} |")
    (out / "comparison.md").write_text("\n".join(lines) + "\n")
    print((out / "comparison.md").read_text())


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
