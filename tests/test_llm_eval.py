"""The LLM runs see only what the blind stand-in writers saw: section 1 and the four allowed assumption columns. No API call."""
from praxeo.core import expand as X
from praxeo.core.llm_eval import blind_inputs


def test_blind_inputs_hold_only_section_1_and_four_columns():
    section1, table = blind_inputs("WE-036")
    assert section1.startswith("## 1") and "## 2" not in section1 and "Consequence list" not in section1
    rows = table.splitlines()
    assert rows and all(len(r.split(" | ")) == 4 and r.startswith("A-") for r in rows)


def test_proposals_from_the_llm_are_checked_against_their_part():
    good = X.ProposalOut(part="links", fact_json='{"source_actor": "a", "source_variable": "price_paid", "relation": "cost", '
                                                  '"actor": "b", "variable": "price_paid"}', premises=["p"])
    assert X._check(good)[0] is not None
    assert X._check(X.ProposalOut(part="links", fact_json="{not json"))[0] is None
    assert X._check(X.ProposalOut(part="exchanges", fact_json='{"id": "e2"}'))[0] is None


def test_identifiers_a_writer_capitalises_are_made_asp_constants():
    """The first live seed named exchanges `E1` and premises by the table's `A-1`, which clingo reads as variables."""
    import json
    import re
    from pathlib import Path

    from praxeo.core import situation as S

    raw = (Path(__file__).resolve().parents[1] / "cases" / "we036_quenby" / "loop" / "seed.json").read_text()
    orig = S.Situation.model_validate_json(raw)
    caps = S.Situation.model_validate_json(re.sub(r'"a(\d+)"', r'"A-\1"', re.sub(r'"e(\d+)"', r'"E\1"', raw)))
    assert S.safe_ids(orig) == orig
    safe = S.safe_ids(caps)
    assert [e.id for e in safe.exchanges] == [e.id for e in orig.exchanges] and "a_1" in safe.assumptions
    dump = lambda cs: sorted(re.sub(r"\ba_(\d+)\b", r"a\1", json.dumps(c.model_dump(), sort_keys=True, default=str)) for c in cs)
    assert dump(S.run(safe)) == dump(S.run(orig))
    assert X.S.safe_ids({"component": "C1", "premises": ["A-2", "q3_x"], "actor": "Workers.Bound"}) == \
        {"component": "c1", "premises": ["a_2", "q3_x"], "actor": "Workers.Bound"}
    assert X.S.safe_ids({"component": "k1_offer", "branch_premises": ["A-4"], "branch_premise_sets": [["A-5"], ["A-6", "q7_y"]]}) == \
        {"component": "k1_offer", "branch_premises": ["a_4"], "branch_premise_sets": [["a_5"], ["a_6", "q7_y"]]}


def test_no_identifier_in_any_case_reaches_the_program_as_a_variable():
    """Every case's identifiers, capitalised as a writer might, give a program with no unquoted capital (a variable)."""
    import re
    from pathlib import Path

    from praxeo.core import situation as S

    def ids(v, out):
        if isinstance(v, dict):
            for k, w in v.items():
                if k in S.ID_FIELDS and isinstance(w, str):
                    out.add(w)
                ids(w, out)
        elif isinstance(v, list):
            for w in v:
                ids(w, out)
        return out

    root, n = Path(__file__).resolve().parents[1] / "cases", 0
    for f in sorted(root.glob("*/**/*.json")):
        try:
            s = S.Situation.model_validate_json(f.read_text())
        except Exception:
            continue
        n += 1
        raw = s.model_dump_json()
        for i in sorted(ids(s.model_dump(), set(s.assumptions)) - {"", "none"}, key=len, reverse=True):
            raw = raw.replace(f'"{i}"', f'"{i.upper()}-X"')
        program = re.sub(r'"(?:[^"\\]|\\.)*"', '""', S.facts(S.safe_ids(S.Situation.model_validate_json(raw))))
        assert not re.findall(r"\b[A-Z]\w*", program), f.name
    assert n > 100
