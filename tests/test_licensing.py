"""Licensing and quotas (praxeo/rules/licensing.lp): consistency with the development example WE-003, and the rules one by one.

Same shape as tests/test_subsidies.py. WE-003 was used to write the licensing rules, so this is a development check. The quota
rules were written from EN-6's text alone; their examples are run out of sample (tests/test_oos_we0*.py).
"""
from pathlib import Path

from praxeo import engine, parser
from praxeo.questions import questions_for
from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE3 = ROOT / "cases" / "we003_westmark"

WE003_SHORT = {"braiders.current": "braiders", "licensed braiders": "braiders.licensed", "licensees": "braiders.licensed",
               "schools": "schools.cosmetology", "customers": "customers.braiding"}
WE003_EXCEPTIONS: dict = {}
WE003_NOT_PRODUCED = {
    "C-16": "missing record fact: section 1 does not say how the board's added work is funded (A-8's evidence is the fiscal note); with `general_budget` set, OC-3 and OC-1 sign the payer group",
    "C-18": "missing role: businesses that employ braiders (their unlicensed staff fall, CR-1, CR-4); the record has one bound role",
}
WE003_PRODUCED = {"C-1", "C-2", "C-3", "C-4", "C-5", "C-6", "C-8", "C-9", "C-10", "C-11", "C-12", "C-15", "C-17", "C-19", "C-20", "C-21"}


def _record():
    return parser.parse_fixture(WE3 / "record.json")


def _reported(rec, **p):
    a = {}
    for comp in rec.components:
        for q, text in questions_for(comp):
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            a[atom] = engine.Assumption(id=atom, text=text, assumption_class=q.assumption_class, p=p.get(q.assumption, 0.9))
    return {(c.actor_class, c.variable, c.sign, c.window) for c in engine.run(rec, a)[0] if c.reported}


def test_consistent_with_worked_example_we003():
    pred, keys = _engine(WE3)
    rows = _rows("WE-003_braiding_license.md", WE003_SHORT, {}, {})
    assert len(rows) == 18
    _check(rows, keys, WE003_EXCEPTIONS, WE003_NOT_PRODUCED, WE003_PRODUCED)
    # EN-11: the training is unrelated to braiding quality (A-5), so the license tells buyers nothing (no increase)
    assert ("customers.braiding", "quality_information", "increase", None) not in keys


def test_binding_and_enforcement_gate_every_licensing_row():
    rec = _record()
    assert not _reported(rec, binding=0.3)
    assert _reported(rec, enforced=0.3) == set()


def test_licensing_premises_and_payers():
    rec = _record()
    got = _reported(rec, evasion=0.3, some_qualify=0.3)
    assert not any(k[1] in ("informal_activity", "search_cost", "compliance_cost") for k in got)
    assert ("customers.braiding", "quality_information", "increase", None) in got            # EN-11 when the test is valued
    rec.components[0].general_budget = True                                                   # OC-3 with OC-1, who pays
    got = _reported(rec)
    assert ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None) in got


def test_quota_rules():
    """EN-6 from its text: quantity down, price up for buyers, holders gain; tradable rights capitalized; an import quota
    protects domestic sellers and, through TX-8, lowers exports; in a wider market the lease price rations instead."""
    rec = _record()
    comp = rec.components[0]
    comp.instrument, comp.bound_actor, comp.buyer_actor = "quota", "importers", "buyers.sugar"
    comp.right_holder_actor, comp.trainer_actor, comp.transferable = "quota_holders", None, True
    comp.import_quota, comp.domestic_seller_actor = True, "growers.domestic"
    got = _reported(rec)
    assert {("importers", "quantity_traded", "decrease", None), ("buyers.sugar", "price_paid", "increase", None),
            ("quota_holders", "net_price_received", "increase", None), ("quota_holders", "asset_value", "increase", None),
            ("growers.domestic", "quantity_supplied", "increase", None),
            ("export_industries", "quantity_supplied", "decrease", None)} <= got
    comp.wider_market = True
    got = _reported(rec, price_effect_material=0.3)
    assert ("quota_holders", "right_lease_price", "increase", None) in got
    assert ("buyers.sugar", "price_paid", "increase", None) not in got
    assert ("quota_holders", "net_price_received", "increase", None) not in got
