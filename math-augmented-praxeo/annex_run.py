"""Run the annex pass, and optionally the premise step, on a praxeo prediction.

Usage:
  python3 math-augmented-praxeo/annex_run.py PREDICTION_JSON ANNEX_INPUTS_JSON OUT_DIR
      [--premise-step --decider fixture|llm|human [--answers ANSWERS_JSON]]

Reads a frozen `prediction.json` written by `python3 -m praxeo` and writes, to OUT_DIR:
- annex.json, annex.md: sizes attached to reported consequences;
- with --premise-step: premise_step.json, premise_step.md (each proposal and the decider's answer) and
  prediction_annex_informed.json (re-derived with the accepted probabilities, beside the original).
The prediction file is never modified.
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))  # praxeo

from mathpraxeo import premise_step  # noqa: E402
from mathpraxeo.bridge import AnnexInputs, annex_pass, dump, to_markdown  # noqa: E402


def main(argv=None) -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("prediction", type=Path)
    ap.add_argument("inputs", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--premise-step", action="store_true")
    ap.add_argument("--decider", choices=["fixture", "llm", "human"], default="fixture")
    ap.add_argument("--answers", type=Path)
    a = ap.parse_args(argv)

    pred = json.loads(a.prediction.read_text())
    inputs = AnnexInputs.load(a.inputs)
    a.out.mkdir(parents=True, exist_ok=True)
    atts = annex_pass(pred, inputs)
    (a.out / "annex.json").write_text(dump(atts))
    (a.out / "annex.md").write_text(to_markdown(pred["record"]["name"], atts))
    print((a.out / "annex.md").read_text())

    if a.premise_step:
        from praxeo.decider import FixtureDecider, HumanDecider, LLMDecider
        if a.decider == "fixture" and not a.answers:
            ap.error("--decider fixture needs --answers")
        decider = {"fixture": lambda: FixtureDecider(a.answers), "llm": LLMDecider, "human": HumanDecider}[a.decider]()
        log, informed = premise_step.run(pred, inputs, decider)
        (a.out / "premise_step.json").write_text(json.dumps(premise_step.dump_log(log), indent=1))
        (a.out / "premise_step.md").write_text(premise_step.log_markdown(pred["record"]["name"], log, informed))
        (a.out / "prediction_annex_informed.json").write_text(json.dumps(informed, indent=1, sort_keys=True))
        print((a.out / "premise_step.md").read_text())


if __name__ == "__main__":
    main()
