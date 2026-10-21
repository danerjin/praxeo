"""Price floors (praxeo/rules/floors.lp): consistency with the development example WE-009, and the rules one by one.

Same shape as tests/test_mandates.py. WE-009 was used to write the rules, so this is a development check.
"""
from pathlib import Path

from praxeo import engine, parser
from praxeo.questions import questions_for
from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE9 = ROOT / "cases" / "we009_larrow"

# the table's "unions" are the organized sellers the floor raises
WE009_SHORT = {"unions": "workers.adult_low_wage"}
WE009_EXCEPTIONS = {
    ("workers.adult_low_wage", "lobbying_effort", "increase", None):
        "RS-7 for the sellers the floor raises; C-11 names their unions, mapped to this role (see WE009_SHORT)",
    ("workers.youth", "lobbying_effort", "increase", None):
        "RS-7 on the youth floor's sellers (k2): the same premise A-15 as the unions; the table names the unions once (C-11)",
}
WE009_NOT_PRODUCED: dict = {}
WE009_PRODUCED = {f"C-{i}" for i in range(1, 21)} - {"C-12"} - set(WE009_NOT_PRODUCED)   # C-12 was withdrawn (catalog 0.5)


def _reported(rec, **p):
    a = {}
    for comp in rec.components:
        for q, text in questions_for(comp):
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            a[atom] = engine.Assumption(id=atom, text=text, assumption_class=q.assumption_class, p=p.get(q.assumption, 0.9))
    return {(c.actor_class, c.variable, c.sign, c.item) for c in engine.run(rec, a)[0] if c.reported}


def test_consistent_with_worked_example_we009():
    pred, keys = _engine(WE9)
    rows = _rows("WE-009_minimum_wage_youth_rate.md", WE009_SHORT, {}, {})
    assert len(rows) == 19
    _check(rows, keys, WE009_EXCEPTIONS, WE009_NOT_PRODUCED, WE009_PRODUCED)


def test_premises_gate_their_chains():
    rec = parser.parse_fixture(WE9 / "record.json")
    got = _reported(rec, cost_not_offset=0.3)
    # without A-14 only the wage rise, evasion, reshaping, lobbying and the Tier A costs stay
    assert ("workers.adult_low_wage", "wage_rate", "increase", None) in got
    assert not any(k[1] in ("excess_supply", "return_on_capital", "price_paid", "employment") for k in got)
    got = _reported(rec, tiers_substitute=0.3)
    # without A-13 the youth group has its own PC-10 chain only
    assert ("workers.youth", "employment", "at_least_one_decrease", None) in got
    got = _reported(rec, budget_fixed=0.3)
    assert ("officials.enforcement", "enforcement_cost", "decrease", "other_work") not in got


def test_a_floor_on_a_good_and_the_state_buying_the_surplus():
    from praxeo.schema import Component, PolicyRecord
    base = dict(id="k1", instrument="price_floor", good="milk", market="m", bound_actor="processors",
                seller_actor="farmers", contract_kind="sale", source_sentences=["x"])
    rec = PolicyRecord(name="n", jurisdiction="j", rule_maker="r", enacted="e", effective="f", components=[Component(**base)])
    got = _reported(rec)
    assert {("farmers", "net_price_received", "increase", None), ("processors", "price_paid", "increase", None),
            ("farmers", "excess_supply", "increase", None), ("processors", "quantity_traded", "decrease", None)} <= got
    assert not any(k[1] in ("wage_rate", "employment") for k in got)
    rec = PolicyRecord(name="n", jurisdiction="j", rule_maker="r", enacted="e", effective="f",
                       components=[Component(**base, state_buys_surplus=True, outlay_actor="board", general_budget=True)])
    got = _reported(rec)
    assert {("board", "inventory_held", "increase", None), ("board", "subsidy_outlay", "increase", None)} <= got
    assert not any(k[1] in ("excess_supply", "quantity_traded") for k in got)   # PC-9 Unless
