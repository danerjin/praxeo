"""Mandates (praxeo/rules/mandates.lp): consistency with the development example WE-029, and the rules one by one.

Same shape as tests/test_prohibition.py. WE-029 was used to write PC-17's rules, so this is a development check; PC-18 and
EN-14 are written from the catalog and checked here on small records only.
"""
from pathlib import Path

from praxeo import engine, parser
from praxeo.questions import questions_for
from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE29 = ROOT / "cases" / "we029_varrow"

# the table names employer associations and unions; the record's roles are the bound employers and the recipients
WE029_SHORT = {"associations": "employers.uncovered", "unions": "workers.uncovered",
               "recipients of other general-fund spending": "recipients.other_spending"}
WE029_EXCEPTIONS: dict = {}
WE029_NOT_PRODUCED = {
    "C-25": "combiner: the total of non-wage compensation sets C-1 against the groups of C-4, C-6 and C-7, and a group is never a chain (CR-12 1.1)",
    "C-36": "breach by letting 2027 balances lapse, per reading of U1: the record has no field for a term whose start of enforcement is unclear, and its key is C-15's",
}
WE029_PRODUCED = {f"C-{i}" for i in range(1, 43)} - set(WE029_NOT_PRODUCED)


def _record():
    return parser.parse_fixture(WE29 / "record.json")


def _reported(rec, **p):
    a = {}
    for comp in rec.components:
        for q, text in questions_for(comp):
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            a[atom] = engine.Assumption(id=atom, text=text, assumption_class=q.assumption_class, p=p.get(q.assumption, 0.9))
    return {(c.actor_class, c.variable, c.sign, c.item) for c in engine.run(rec, a)[0] if c.reported}


def test_consistent_with_worked_example_we029():
    pred, keys = _engine(WE29)
    rows = _rows("WE-029_paid_sick_leave_mandate.md", WE029_SHORT, {}, {})
    assert len(rows) == 42
    _check(rows, keys, WE029_EXCEPTIONS, WE029_NOT_PRODUCED, WE029_PRODUCED)


def test_premises_gate_their_chains():
    rec = _record()
    got = _reported(rec, worth_less=0.3)
    # without A-6 the medium-run group, relocation and rivals' sales go; the short-run group and the cost stay (A-3)
    assert ("workers.uncovered", "employment", "at_least_one_decrease", None) in got
    assert not any(k[0] in ("employers.tradable", "neighboring_jurisdictions") for k in got)
    assert ("workers.full_time", "hours_worked", "increase", None) in got        # RS-18's shift alone
    got = _reported(rec, wages_sticky=0.3, worth_less=0.3)
    assert ("employers.uncovered", "price_paid", "increase", None) not in got
    assert ("workers.uncovered", "employment", "at_least_one_decrease", None) not in got
    assert ("workers.uncovered", "wage_rate", "decrease", None) in got           # both sides push the wage down (PC-17)
    got = _reported(rec, unpaid_absence_before=0.3)
    assert ("workers.uncovered", "earnings", "decrease", None) in got            # A-26 false: earnings fall (WE-029 A-26)
    got = _reported(rec, complaint_unlikely=0.3)
    assert not any(k[1] == "legal_breach" or k[0] in ("workers.complainants", "employers.violating") for k in got)


def test_threshold_items_by_reading():
    rec = _record()
    a = {f"{q.assumption}(k1)": engine.Assumption(id=f"{q.assumption}(k1)", text=t, assumption_class=q.assumption_class, p=0.9)
         for comp in rec.components for q, t in questions_for(comp)}
    cons = engine.run(rec, a)[0]
    other = [c for c in cons if c.actor_class == "employers.near_threshold" and c.item == "other_staff"]
    assert [c.sign_by_reading for c in other] == [{"U2-a": "decrease", "U2-b": "increase"}]
    counted = [c for c in cons if c.actor_class == "employers.near_threshold" and c.item == "counted_staff"]
    assert [c.sign for c in counted] == ["decrease"]


def test_term_prohibition_and_standard_from_the_catalog():
    from praxeo.schema import Component, PolicyRecord
    ban = Component(id="k1", instrument="term_prohibition", good="noncompete", market="m", bound_actor="employers",
                    recipient_actor="workers", applicant_actor="workers.prospective", restrains_mobility=True,
                    voids_existing=True, source_sentences=["x"])
    rec = PolicyRecord(name="n", jurisdiction="j", rule_maker="r", enacted="e", effective="f", components=[ban])
    got = _reported(rec)
    # holders of voided contracts move and are bid up; the other terms of new contracts fall on prospective counterparties
    assert {("workers", "job_changes", "increase", None), ("workers", "wage_rate", "increase", None),
            ("employers", "term_prevalence", "increase", None), ("workers.prospective", "wage_rate", "at_least_one_decrease", None),
            ("employers", "resources_available_other_uses", "decrease", None),
            ("workers", "resources_available_other_uses", "increase", None)} <= got
    assert not any(k[0] == "workers" and k[2] == "at_least_one_decrease" for k in got)
    std = Component(id="k1", instrument="product_standard", good="homes", market="m", bound_actor="builders",
                    buyer_actor="buyers.new_homes", stock_exempt=True, stock_owner_actor="owners.existing", source_sentences=["x"])
    rec = PolicyRecord(name="n", jurisdiction="j", rule_maker="r", enacted="e", effective="f", components=[std])
    got = _reported(rec, buyers_value_standard=0.3)
    assert {("buyers.new_homes", "price_paid", "increase", None), ("builders", "quantity_supplied", "decrease", None),
            ("owners.existing", "asset_value", "increase", None), ("owners.existing", "stock_age", "increase", None)} <= got
    got = _reported(rec)                                                          # EN-14 Unless: buyers value the standard
    assert {("owners.existing", "asset_value", "ambiguous", None), ("owners.existing", "stock_age", "ambiguous", None),
            ("builders", "quantity_supplied", "ambiguous", None)} <= got
    # a sale contract: no wage, hours or jobs chains (PC-17 1.1)
    sale = Component(id="k1", instrument="mandated_contract_term", good="repair_parts", market="m", bound_actor="makers",
                     recipient_actor="owners", contract_kind="sale", source_sentences=["x"])
    rec = PolicyRecord(name="n", jurisdiction="j", rule_maker="r", enacted="e", effective="f", components=[sale])
    assert not any(k[1] in ("wage_rate", "employment", "hours_worked", "earnings", "price_paid") for k in _reported(rec))
