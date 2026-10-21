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
