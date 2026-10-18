"""Context retrieval and enrichment (plan 5.3): date filter, per-question retrieval, related markets from sources with
quotes checked in code. The sources here are test fixtures written for these tests, not evidence about any case."""
import json
import shutil
import subprocess
import sys
from pathlib import Path

from praxeo import parser
from praxeo.context import for_question, retrieve, split
from praxeo.decider import FixtureDecider
from praxeo.pipeline import predict
from praxeo.schema import Related, Source

ROOT = Path(__file__).resolve().parents[1]
WE21 = ROOT / "cases" / "we021_calvera"

SOURCES = [
    Source(id="s1", date="2026-06-01", citation="test fixture",
           text="Electricians in Calvera are fully booked; commercial builders compete with solar installers for licensed electricians."),
    Source(id="s2", date="2026-07-01", citation="test fixture", text="Grid electricity rates rose 3% last year."),
    Source(id="s3", date="2027-03-01", citation="test fixture", text="Electrician wages jumped 15% after the subsidy began."),
]


def _record():
    rec = parser.parse_fixture(WE21 / "record.json")
    return rec.model_copy(update={"enacted": "2026-11-01"})


def test_split_holds_back_sources_on_or_after_enactment():
    kept, held = split(_record(), SOURCES)
    assert [s.id for s in kept] == ["s1", "s2"] and held == ["s3"]


def test_retrieve_ranks_by_shared_rare_words_and_drops_unrelated():
    kept, _ = split(_record(), SOURCES)
    assert [s.id for s in retrieve(kept, "Is the supply of licensed electricians slow to expand?")] == ["s1"]
    assert retrieve(kept, "Will foreign sellers absorb the tariff?") == []
    rec, used = for_question(_record(), kept, "grid electricity rates")
    assert used == ["s2"] and rec.context[-1].startswith("Grid electricity rates rose")


def test_predict_gives_each_question_its_sources_and_never_a_later_one():
    rec = _record()
    pred = predict((WE21 / "policy.txt").read_text(), rec, FixtureDecider(WE21 / "answers.json"), SOURCES)
    assert pred["sources_held_back"] == ["s3"]
    used = {a["question"]["id"]: a.get("sources", []) for a in pred["questions"]}
    assert used["k1.related_slow_r1"] == ["s1"]
    assert not any("s3" in ids for ids in used.values())


def test_source_quotes_are_checked():
    rec = _record()
    kept, _ = split(rec, SOURCES)
    text = (WE21 / "policy.txt").read_text()
    good = Related(kind="input", good="electrical_labour", seller_actor="electricians", price_variable="wage_rate",
                   other_user_actor="builders.commercial", source_id="s1",
                   quote="commercial builders compete with solar installers for licensed electricians.")
    bad_quote = good.model_copy(update={"quote": "builders hoard electricians."})
    late = good.model_copy(update={"source_id": "s3", "quote": "Electrician wages jumped 15% after the subsidy began."})
    for rel, expect in ((good, []), (bad_quote, ["quote not found in source s1"]), (late, ["source s3 is not a source dated before enactment"])):
        rec.components[0].related = [rel]
        problems = parser.check_source_quotes(rec, text, kept)
        assert [p.split(": ", 1)[1] for p in problems] == expect, problems


def test_enrichment_from_a_source_reaches_the_engine(tmp_path):
    """End to end through the command line: an enrichment file adds the electricians' other users from a source; the
    quote is checked; the engine then signs SB-3 with CR-7a for them (the rows WE-021 lists as C-14 and C-20)."""
    case = tmp_path / "case"
    shutil.copytree(WE21, case, ignore=shutil.ignore_patterns("sample_run"))
    rec = json.loads((case / "record.json").read_text())
    rec["enacted"] = "2026-11-01"
    rec["components"][0]["related"] = [r for r in rec["components"][0]["related"] if r["good"] != "electrical_labour"]
    (case / "record.json").write_text(json.dumps(rec))
    (case / "sources.json").write_text(json.dumps([s.model_dump() for s in SOURCES]))
    answers = json.loads((case / "answers.json").read_text())
    for a in answers:   # the electrical labour relation is now the second one listed
        a["question_id"] = {"k1.related_slow_r1": "k1.related_slow_r2", "k1.related_slow_r2": "k1.related_slow_r1"}.get(a["question_id"], a["question_id"])
    (case / "answers.json").write_text(json.dumps(answers))
    enrichment = {"components": [{"id": "k1", "related": [{
        "kind": "input", "good": "electrical_labour", "seller_actor": "electricians", "price_variable": "wage_rate",
        "other_user_actor": "buyers.other_electrical_work", "source_id": "s1",
        "quote": "commercial builders compete with solar installers for licensed electricians."}]}]}
    (tmp_path / "enrichment.json").write_text(json.dumps(enrichment))
    out = tmp_path / "run"
    subprocess.run([sys.executable, "-m", "praxeo", str(case), "--enrichment", str(tmp_path / "enrichment.json"), "--out", str(out)],
                   check=True, cwd=ROOT, capture_output=True)
    pred = json.loads((out / "prediction.json").read_text())
    assert pred["citation_problems"] == [] and pred["sources_held_back"] == ["s3"]
    keys = {(c["actor_class"], c["variable"], c["sign"]) for c in pred["consequences"] if c["reported"]}
    assert {("buyers.other_electrical_work", "price_paid", "increase"), ("buyers.other_electrical_work", "quantity_traded", "decrease"),
            ("electricians", "wage_rate", "increase")} <= keys
