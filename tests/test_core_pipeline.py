"""Step 5: the core path is the default. A case with core inputs runs seed -> expand loop -> core rules -> verifier ->
explanations -> frozen log; a case without them falls back to the pattern engine."""
import json
from pathlib import Path

from praxeo.core import pipeline as CP

ROOT = Path(__file__).resolve().parents[1]


def test_core_path_end_to_end(tmp_path):
    for case in ("we001_riverton", "we006_coralia"):
        seed, proposer, decider = CP.inputs(ROOT / "cases" / case)
        pred = CP.run_case(ROOT / "cases" / case, tmp_path / case, seed, proposer, decider)
        assert pred["engine"] == "core" and pred["verifier_problems"] == []
        assert pred["explanations"] and all("because" in e for e in pred["explanations"])
        frozen = json.loads((tmp_path / case / "prediction.json").read_text())
        assert frozen["rulebase_version"] == CP.CORE_VERSION and frozen["loop"]["rounds"] >= 1
        assert (tmp_path / case / "report.md").read_text().startswith("# Core-rule run")


def test_fallback_to_patterns_without_core_inputs():
    assert CP.inputs(ROOT / "cases" / "controls" / "ceiling_clear_yes") is None
