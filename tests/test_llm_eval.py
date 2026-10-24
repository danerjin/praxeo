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
