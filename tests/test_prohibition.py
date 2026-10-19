"""Prohibitions (praxeo/rules/prohibition.lp): consistency with the development example WE-017, and the rules one by one.

Same shape as tests/test_licensing.py. WE-017 was used to write the rules, so this is a development check.
"""
from pathlib import Path

from praxeo import engine, parser
from praxeo.questions import questions_for
from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE17 = ROOT / "cases" / "we017_corrin"

WE017_WINDOWS = {"announcement window": "announcement"}
WE017_EXCEPTIONS: dict = {}
WE017_NOT_PRODUCED = {
    "C-20": "the informal sellers' earnings: C-4's price against the penalties, ambiguous; no rule signs earnings under a ban",
    "C-26": "combiner: all state taxes, the lost sales tax (C-17) against excises on substitutes (A-15); no declared comparison",
    "C-30": "combiner: the legal price in the final weeks, stocking up against the run-down of stocks (CR-12b); no declared comparison",
}
WE017_PRODUCED = {f"C-{i}" for i in range(1, 31)} - set(WE017_NOT_PRODUCED)


def _record():
    return parser.parse_fixture(WE17 / "record.json")


def _reported(rec, **p):
    a = {}
    for comp in rec.components:
        for q, text in questions_for(comp):
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            a[atom] = engine.Assumption(id=atom, text=text, assumption_class=q.assumption_class, p=p.get(q.assumption, 0.9))
    return {(c.actor_class, c.variable, c.sign, c.window) for c in engine.run(rec, a)[0] if c.reported}


def test_consistent_with_worked_example_we017():
    pred, keys = _engine(WE17)
    rows = _rows("WE-017_substance_ban.md", {}, WE017_WINDOWS, {})
    assert len(rows) == 30
    _check(rows, keys, WE017_EXCEPTIONS, WE017_NOT_PRODUCED, WE017_PRODUCED)


def test_premises_gate_their_chains():
    rec = _record()
    got = _reported(rec, evasion=0.3)
    assert not any(k[1] in ("informal_activity", "quality_variability", "share_concentrated_forms") for k in got)
    assert ("users.current", "price_paid", "increase", None) in got                       # the risk price needs no evasion
    got = _reported(rec, enforcement_risk=0.3)
    assert not any(k[1] == "price_paid" or k[0] == "users.convicted" for k in got)
    got = _reported(rec, enforced=0.3)
    assert not any(k[0] == "shops.lirva" and k[1] in ("quantity_traded", "employment", "inventory_held") for k in got)
    assert ("shops.lirva", "resources_available_other_uses", "decrease", None) in got     # stocks destroyed: Tier A
    rec.components[0].volume_penalties = False                                            # EN-8 needs bulk-graded penalties
    assert not any(k[1] == "share_concentrated_forms" for k in _reported(rec))
