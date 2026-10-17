"""Tests for confidence thresholds and escalation (praxeo/escalation.py)."""
import json
import sys
from pathlib import Path

import pytest

from praxeo import parser
from praxeo.__main__ import main
from praxeo.decider import FixtureDecider
from praxeo.escalation import EscalatingDecider, Thresholds, confidence, load_thresholds
from praxeo.pipeline import predict
from praxeo.questions import ceiling_questions
from praxeo.schema import Answer, Question

ROOT = Path(__file__).resolve().parents[1]
SF = ROOT / "cases" / "sf_1994"


class _Never:
    """A fallback that must not be asked."""
    name = "never"

    def answer(self, question, record):
        raise AssertionError(f"fallback asked about {question.id}")


def _record():
    return parser.parse_fixture(SF / "record.json")


def _questions():
    return ceiling_questions(_record().components[0])


def _fixture_with(tmp_path, name, probabilities, default=None):
    """A fixture answers file: the sf_1994 answers with overridden probabilities."""
    rows = json.loads((SF / "answers.json").read_text())
    kept = []
    for r in rows:
        if default is not None:
            r["probability"] = default
        if r["question_id"] in probabilities:
            r["probability"] = probabilities[r["question_id"]]
        kept.append(r)
    path = tmp_path / name
    path.write_text(json.dumps(kept))
    return FixtureDecider(path)


def test_passing_thresholds_change_nothing():
    text = (SF / "policy.txt").read_text()
    plain = predict(text, _record(), FixtureDecider(SF / "answers.json"))
    # 0.55 is the lowest confidence in the fixture (evasion, and exit_process at p = 0.45); 0.54 sits just below it
    wrapped = EscalatingDecider(FixtureDecider(SF / "answers.json"), _Never(),
                                Thresholds(kind={"noul": 0.54}))
    out = predict(text, _record(), wrapped)
    assert wrapped.log == []
    assert out["escalations"] == []
    assert out["consequences"] == plain["consequences"]
    assert out["assumptions"] == plain["assumptions"]
    assert out["questions"] == plain["questions"]
    assert out["explanations"] == plain["explanations"]
    assert "escalations" not in plain  # plain decider: output shape unchanged


def test_high_threshold_escalates_low_confidence_to_fallback(tmp_path):
    primary = _fixture_with(tmp_path, "primary.json", {}, default=0.55)
    fallback = FixtureDecider(SF / "answers.json")
    dec = EscalatingDecider(primary, fallback, Thresholds(kind={"noul": 0.9}))
    rec = _record()
    expected = {r["question_id"]: r["probability"] for r in json.loads((SF / "answers.json").read_text())}
    for q in _questions():
        a = dec.answer(q, rec)
        assert a.decider == "fixture:answers.json"
        assert a.probability == expected[q.id]
    assert [e["question_id"] for e in dec.log] == [q.id for q in _questions()]
    entry = dec.log[0]
    assert entry["kind"] == "noul"
    assert entry["assumption_class"] == "binding"
    assert entry["primary"] == "fixture:primary.json"
    assert entry["primary_p"] == 0.55
    assert entry["primary_confidence"] == pytest.approx(0.55)
    assert entry["threshold"] == 0.9
    assert entry["fallback"] == "fixture:answers.json"
    assert entry["fallback_p"] == 0.75


def test_only_low_confidence_questions_escalate(tmp_path):
    # noul 0.7: lockin_dominates (0.65), keepers_dominate (0.6), quality_adjustable (0.6), evasion (0.55) and
    # exit_process (0.45, confidence 0.55) fall below; the rest pass
    primary = FixtureDecider(SF / "answers.json")
    fallback = _fixture_with(tmp_path, "fallback.json",
                             {"c1.lockin_dominates": 0.3, "c1.keepers_dominate": 0.2})
    dec = EscalatingDecider(primary, fallback, Thresholds(kind={"noul": 0.7}))
    out = predict((SF / "policy.txt").read_text(), _record(), dec)
    assert [e["question_id"] for e in out["escalations"]] == [
        "c1.lockin_dominates", "c1.keepers_dominate", "c1.quality_adjustable", "c1.evasion", "c1.exit_process"]
    used = {q["answer"]["question_id"]: q["answer"] for q in out["questions"]}
    assert used["c1.lockin_dominates"]["probability"] == 0.3
    assert used["c1.lockin_dominates"]["decider"] == "fixture:fallback.json"
    assert used["c1.keepers_dominate"]["probability"] == 0.2
    assert used["c1.binding"]["decider"] == "fixture:answers.json"
    assert out["assumptions"]["lockin_dominates(c1)"]["p"] == 0.3


def test_assumption_class_threshold_overrides_kind(tmp_path):
    fallback = FixtureDecider(SF / "answers.json")
    # kind says 0.5 (nothing escalates), class says 0.8 for binding (0.75 escalates)
    dec = EscalatingDecider(FixtureDecider(SF / "answers.json"), fallback,
                            Thresholds(kind={"noul": 0.5}, assumption_class={"binding": 0.8}))
    dec.answer(_questions()[0], _record())
    assert len(dec.log) == 1 and dec.log[0]["threshold"] == 0.8
    # kind says 0.8 (binding 0.75 would escalate), class says 0.7 for binding (it passes)
    dec = EscalatingDecider(FixtureDecider(SF / "answers.json"), fallback,
                            Thresholds(kind={"noul": 0.8}, assumption_class={"binding": 0.7}))
    dec.answer(_questions()[0], _record())
    assert dec.log == []
    # and a kind threshold still applies to classes without their own threshold
    dec.answer(_questions()[2], _record())  # alternative_uses, p 0.7 -> conf 0.7 < 0.8
    assert dec.log[0]["question_id"] == "c1.alternative_uses" and dec.log[0]["threshold"] == 0.8


def test_confidence_rules():
    noul = Question(id="q", kind="noul", text="?")
    assert confidence(noul, Answer(question_id="q", value="no", probability=0.2, rationale="")) == pytest.approx(0.8)
    choice = Question(id="c", kind="choice", text="?", options=["a", "b"])
    unknown = Answer(question_id="c", value="a", probability=0.9, rationale="")
    assert confidence(choice, unknown) == 0.0
    known = Answer(question_id="c", value="a", probability=0.9, rationale="", confidence=0.6)
    assert confidence(choice, known) == 0.6


def test_choice_without_confidence_escalates_unless_threshold_zero():
    class Stub:
        name = "stub"

        def __init__(self, conf=None):
            self.conf = conf

        def answer(self, question, record):
            return Answer(question_id=question.id, value="a", probability=0.9, rationale="",
                          decider=self.name, confidence=self.conf)

    choice = Question(id="c", kind="choice", text="?", options=["a", "b"])
    rec = _record()
    dec = EscalatingDecider(Stub(), Stub(), Thresholds(kind={"choice": 0.1}))
    dec.answer(choice, rec)
    assert len(dec.log) == 1
    dec = EscalatingDecider(Stub(), Stub(), Thresholds(kind={"choice": 0.0}))
    dec.answer(choice, rec)
    assert dec.log == []


def test_load_example_thresholds():
    t = load_thresholds(SF / "thresholds.example.json")
    assert t.kind == {"noul": 0.7}
    assert t.assumption_class == {"binding": 0.8}
    assert "not calibrated" in t.note


def test_cli_with_thresholds_logs_escalations(tmp_path, monkeypatch, capsys):
    out = tmp_path / "run"
    monkeypatch.setattr(sys, "argv", ["praxeo", str(SF), "--out", str(out),
                                      "--thresholds", str(SF / "thresholds.example.json"),
                                      "--fallback", "fixture",
                                      "--fallback-answers", str(SF / "answers.json")])
    main()
    pred = json.loads((out / "prediction.json").read_text())
    ids = {e["question_id"] for e in pred["escalations"]}
    assert ids == {"c1.binding", "c1.lockin_dominates", "c1.keepers_dominate",
                   "c1.quality_adjustable", "c1.evasion", "c1.exit_process"}
    assert "Escalations: 6 of 20" in (out / "report.md").read_text()
    assert (out / "score.json").exists()


def test_cli_without_thresholds_leaves_prediction_unchanged(tmp_path, monkeypatch):
    out = tmp_path / "run"
    monkeypatch.setattr(sys, "argv", ["praxeo", str(SF), "--out", str(out)])
    main()
    pred = json.loads((out / "prediction.json").read_text())
    assert "escalations" not in pred
    assert "Escalations" not in (out / "report.md").read_text()
