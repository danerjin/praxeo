"""Run the annex pass on a praxeo prediction.

Usage: python3 math-augmented-praxeo/annex_run.py PREDICTION_JSON ANNEX_INPUTS_JSON OUT_DIR

Reads a frozen `prediction.json` written by `python3 -m praxeo`, attaches annex sizes to its reported
consequences, and writes annex.json and annex.md to OUT_DIR. The prediction file is not modified.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from mathpraxeo.bridge import AnnexInputs, annex_pass, dump, to_markdown  # noqa: E402


def main(pred_path: str, inputs_path: str, out_dir: str) -> None:
    pred = json.loads(Path(pred_path).read_text())
    protected = next((c.get("protected_actor") for c in pred["record"]["components"]), None)
    atts = annex_pass(pred, AnnexInputs.load(Path(inputs_path)), protected)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    (out / "annex.json").write_text(dump(atts))
    (out / "annex.md").write_text(to_markdown(pred["record"]["name"], atts))
    print((out / "annex.md").read_text())


if __name__ == "__main__":
    main(*sys.argv[1:4])
