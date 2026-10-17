"""Symbolic engine (Configuration A): clingo over the rule base.

The policy record and the decider's assumption estimates become ASP facts.
The rule base opens a choice over every assumption; enumerating all answer
sets gives, for each conclusion, every assumption set under which it is
derived. Keeping only the minimal sets yields an ATMS-style label
(plan 4.4): "this follows if A and B".
"""
from __future__ import annotations

import itertools
import math
from pathlib import Path

import clingo

from .schema import Assumption, Consequence, HORIZON_ORDER, PolicyRecord, Step

RULES = Path(__file__).parent / "rules" / "price_controls.lp"
CUTOFF = 0.5  # workflow: report a consequence only if each assumption has p >= 0.5


def _atom(name: str) -> str:
    """Snake-case identifier safe as an ASP constant."""
    s = "".join(ch if ch.isalnum() else "_" for ch in name.lower()).strip("_")
    return s if s[:1].isalpha() else "c_" + s


def facts(record: PolicyRecord, assumptions: dict[str, Assumption]) -> str:
    lines = []
    for comp in record.components:
        c = _atom(comp.id)
        if comp.instrument == "price_ceiling":
            lines.append(f"ceiling({c}).")
        lines.append(f'bound({c}, "{comp.bound_actor}").')
        if comp.protected_actor:
            lines.append(f'protected({c}, "{comp.protected_actor}").')
        lines.append(f'excluded({c}, "{comp.excluded_actor or "buyers.prospective"}").')
    for a in assumptions:
        lines.append(f"assumption({a}).")
    return "\n".join(lines) + "\n"


def _models(program: str) -> list[list[clingo.Symbol]]:
    ctl = clingo.Control(["0", "--warn=none"])
    ctl.load(str(RULES))
    ctl.add("base", [], program)
    ctl.ground([("base", [])])
    out: list[list[clingo.Symbol]] = []
    ctl.solve(on_model=lambda m: out.append(list(m.symbols(shown=True))))
    return out


def run(record: PolicyRecord, assumptions: dict[str, Assumption], extra: str = "") -> tuple[list[Consequence], str]:
    """Derive consequences. `assumptions` maps the ASP atom (e.g. 'enforced(c1)') to its estimate;
    `extra` adds facts such as `exception(pc_5, c1).` from context grounding."""
    program = facts(record, assumptions) + extra
    labels: dict[tuple, list[frozenset[str]]] = {}
    steps: dict[str, set[tuple[str, str]]] = {}
    for model in _models(program):
        held = frozenset(str(s.arguments[0]) for s in model if s.name == "holds")
        for s in model:
            if s.name == "fired":
                rule, concl, prem = (str(a) for a in s.arguments)
                steps.setdefault(concl, set()).add((rule, prem))
            elif s.name == "effect":
                concl = str(s.arguments[0])
                key = tuple(a.string if a.type == clingo.SymbolType.String else a.name for a in s.arguments[1:])
                labels.setdefault((concl, *key), []).append(held)

    consequences = []
    for n, (key, sets) in enumerate(sorted(labels.items()), start=1):
        concl, actor, variable, sign, horizon, visibility, tier = key
        minimal = sorted({s for s in sets if not any(o < s for o in sets)}, key=lambda s: (len(s), sorted(s)))
        best = max(minimal, key=lambda s: (math.prod(assumptions[a].p for a in s), -len(s)))
        consequences.append(Consequence(
            id=f"C-{n}",
            actor_class=actor,
            variable=variable,
            sign=sign,
            horizon=[h for h in HORIZON_ORDER if HORIZON_ORDER[h] >= HORIZON_ORDER[horizon]],
            visibility=visibility,
            tier=tier,
            derivation=_derivation(concl, steps),
            assumption_sets=[sorted(s) for s in minimal],
            assumptions=sorted(best),
            reported=all(assumptions[a].p >= CUTOFF for a in best),
        ))
    return consequences, program


def _derivation(concl: str, steps: dict[str, set[tuple[str, str]]]) -> list[Step]:
    """Walk the fired/3 atoms back from a conclusion to the record and the assumptions."""
    order: list[Step] = []
    seen = set()

    def visit(c: str) -> None:
        if c in seen or c not in steps:
            return
        seen.add(c)
        by_rule: dict[str, list[str]] = {}
        for rule, prem in sorted(steps[c]):
            by_rule.setdefault(rule, []).append(prem)
        for prem in itertools.chain.from_iterable(by_rule.values()):
            visit(prem)
        for rule, prems in by_rule.items():
            order.append(Step(rule=rule.upper().replace("_", "-"), conclusion=c, premises=prems))

    visit(concl)
    return order
