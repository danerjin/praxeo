"""Step 4 of the core layer: the expand-as-you-go loop (praxeo/core/expand.py). Given the same facts, the loop must give the
one-shot result while asking only about actors the reasoning reaches; a file-driven run stops and lists what it needs."""
import json
from pathlib import Path

import pytest

from praxeo.core import expand as X
from praxeo.core import situation as S

ROOT = Path(__file__).resolve().parents[1]


def _key(cons):
    return {(c.actor_class, c.variable, c.sign, c.window, tuple(c.group)) for c in cons if c.reported}


@pytest.mark.parametrize("case", ["we001_riverton", "we009_larrow", "we013_halvern"])
def test_the_loop_reproduces_the_one_shot_record(case, tmp_path):
    full = S.load(ROOT / "cases" / case / "situation.json")
    seed, props = X.split(full)
    (tmp_path / "p.json").write_text(json.dumps(props))
    run = X.expand(seed, X.FixtureProposer(tmp_path / "p.json"), X.TextDecider({v["text"]: v["p"] for v in full.assumptions.values()}))
    assert _key(S.run(run.situation)) == _key(S.run(full))
    asked = {e["node"] for e in run.log}
    assert set(props) <= asked                       # every proposing actor was reached
    assert run.rounds <= X.MAX_DEPTH


def test_a_file_driven_run_lists_what_it_needs(tmp_path):
    full = S.load(ROOT / "cases" / "we009_larrow" / "situation.json")
    seed, props = X.split(full)
    prop, dec = X.FileProposer(tmp_path / "none.json"), X.FileDecider(tmp_path / "none.json")
    X.expand(seed, prop, dec)
    assert {n.actor for n in prop.missing} >= {"employers.low_wage", "workers.adult_low_wage"}   # the first round's nodes
    assert all(n.depth == 1 for n in prop.missing)   # nothing deeper is reached without their facts


def _loop_score(case, example, short):
    from test_out_of_sample import _rows
    cons = S.run(S.load(ROOT / "cases" / case / "loop" / "situation.json"))
    keys = {(a, v, c.sign, c.window) for c in cons if c.reported for a in (c.actor_group or [c.actor_class]) for v in (c.group or [c.variable])}
    rows = _rows(example, short, {}, {})
    return {r for r, ks in rows.items() if ks & keys}, len(rows)


def test_blind_loop_runs():
    """Blind: a stand-in for the LLM proposer and the decider wrote the seed and answered the loop node by node from the
    policy section and the assumption statements only (cases/<case>/loop/notes.md). Names mapped only where the class is
    the same."""
    produced, n = _loop_score("we006_coralia", "WE-006_price_gouging_law.md",
                              {"buyers.served": "buyers.local", "residents.declared": ["buyers.unserved", "guests.unserved"],
                               "hotels.declared": "sellers.lodging", "evacuees.in_rooms": "guests.local",
                               "repair_contractors.outside": "sellers.repair_outside"})
    assert (len(produced), n) == (17, 26)          # pattern engine: 15 after its fixes
    produced, n = _loop_score("we062_saldria", "WE-062_plastic_packaging_tax.md",
                              {"state budget": "officials.enforcement", "converters": "converters.domestic",
                               "sellers.foreign": ["converters.foreign", "sellers.foreign.packaged_goods"],
                               "recyclers": "recyclers.domestic", "buyers.packaged_goods": "consumers.packaged_goods",
                               "exporters": "exporters.packaged_goods", "converter_workers": "workers.converters",
                               "recycler_workers": "workers.recyclers", "workers of sellers.substitutes": "workers.substitute_makers",
                               "sellers.substitutes": "sellers.substitute_packaging", "converters.owners": "owners.converters",
                               "importers.packaged_goods": "importers.goods",
                               "small_importers": ["importers.small_goods", "importers.small_packaging"], "taxpayers.other": "taxpayers"})
    assert (len(produced), n) == (26, 68)          # pattern engine: 12 after its fixes; 23 before r2 and the response argument
