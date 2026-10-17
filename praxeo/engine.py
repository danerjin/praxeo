"""Symbolic engine (Configuration A): clingo over the rule base.

The policy record and the decider's assumption estimates become ASP facts.
The rule base opens a choice over every assumption; enumerating all answer
sets gives, for each conclusion, every assumption set under which it is
derived. Keeping only the minimal sets yields an ATMS-style label
(plan 4.4): "this follows if A and B".

Unclear provisions: the engine runs once per reading (adding that reading's
facts) and merges the results; where the readings disagree, the consequence
carries a sign per reading (02_ontology.md, per-reading signs).
"""
from __future__ import annotations

import itertools
import math
from pathlib import Path

import clingo

from .schema import Assumption, Consequence, HORIZON_ORDER, PolicyRecord, Step

RULES = sorted((Path(__file__).parent / "rules").glob("*.lp"))  # every rule file is loaded
CUTOFF = 0.5  # workflow: report a consequence only if each assumption has p >= 0.5


class _Context:
    """Python functions the rule base calls with @name(...)."""

    @staticmethod
    def keepers(actor: clingo.Symbol) -> clingo.Symbol:
        return clingo.String(actor.string + ".keepers")

    @staticmethod
    def displaced(actor: clingo.Symbol) -> clingo.Symbol:
        return clingo.String(actor.string + ".displaced")


def _atom(name: str) -> str:
    """Snake-case identifier safe as an ASP constant."""
    s = "".join(ch if ch.isalnum() else "_" for ch in name.lower()).strip("_")
    return s if s[:1].isalpha() else "c_" + s


def _tax_facts(c: str, comp) -> list[str]:
    lines = [f"{'tax' if comp.instrument == 'per_unit_tax' else 'tariff'}({c}).",
             f'buyer({c}, "{comp.buyer_actor}").',
             f'seller({c}, "{comp.seller_actor}").',
             f'domestic_seller({c}, "{comp.domestic_seller_actor}").',
             f'importer({c}, "{comp.importer_actor or comp.bound_actor}").',
             f'revenue({c}, "{comp.revenue_actor}").',
             f'exporter({c}, "{comp.exporter_actor}").',
             f'exporter_worker({c}, "{comp.exporter_worker_actor or "workers." + comp.exporter_actor}").']
    for d in comp.downstream:
        lines.append(f'downstream({c}, "{d.actor}", "{d.buyer_actor}", {d.competitors}).')
    return lines


def facts(record: PolicyRecord, assumptions: dict[str, Assumption]) -> str:
    lines = []
    for comp in record.components:
        c = _atom(comp.id)
        if comp.instrument == "price_ceiling":
            lines.append(f"ceiling({c}).")
        if comp.vacancy_decontrol:
            lines.append(f"decontrol({c}).")
        lines.append(f'bound({c}, "{comp.bound_actor}").')
        if comp.protected_actor:
            lines.append(f'protected({c}, "{comp.protected_actor}").')
        lines.append(f'excluded({c}, "{comp.excluded_actor or "buyers.prospective"}").')
        if comp.instrument in ("per_unit_tax", "tariff"):
            lines += _tax_facts(c, comp)
    for a in assumptions:
        lines.append(f"assumption({a}).")
    return "\n".join(lines) + "\n"


def _models(program: str) -> list[list[clingo.Symbol]]:
    ctl = clingo.Control(["0", "--warn=none"])
    for rules in RULES:
        ctl.load(str(rules))
    ctl.add("base", [], program)
    ctl.ground([("base", [])], context=_Context())
    out: list[list[clingo.Symbol]] = []
    ctl.solve(on_model=lambda m: out.append(list(m.symbols(shown=True))))
    return out


def readings(record: PolicyRecord) -> list[tuple[str, str]]:
    """Every combination of readings of the unclear provisions that carry facts: (label, facts)."""
    branching = [u for u in record.unclear if u.reading_facts]
    if not branching:
        return [("", "")]
    out = []
    for combo in itertools.product(*[u.labels() for u in branching]):
        label = "; ".join(combo)
        extra = "\n".join(u.reading_facts.get(lab, "") for u, lab in zip(branching, combo))
        out.append((label, extra + "\n"))
    return out


def _derive(program: str, assumptions: dict[str, Assumption]) -> dict[tuple, dict]:
    """One engine run. Returns {(actor, variable): {sign, horizon, visibility, tier, concl, sets, steps}}."""
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
    out = {}
    for (concl, actor, variable, sign, horizon, visibility, tier), sets in labels.items():
        minimal = sorted({s for s in sets if not any(o < s for o in sets)}, key=lambda s: (len(s), sorted(s)))
        out[(actor, variable, sign)] = dict(concl=concl, actor=actor, variable=variable, sign=sign, horizon=horizon,
                                            visibility=visibility, tier=tier, sets=minimal,
                                            derivation=_derivation(concl, steps))
    return out


def run(record: PolicyRecord, assumptions: dict[str, Assumption], extra: str = "") -> tuple[list[Consequence], str]:
    """Derive consequences. `assumptions` maps the ASP atom (e.g. 'enforced(c1)') to its estimate;
    `extra` adds facts such as `exception(pc_5, c1).` from context grounding."""
    base = facts(record, assumptions) + extra
    runs = [(label, _derive(base + rf, assumptions)) for label, rf in readings(record)]

    # merge across readings on (actor, variable): same sign everywhere, or a sign per reading
    keys = sorted({(a, v) for _, r in runs for (a, v, _s) in r})
    consequences = []
    for n, (actor, variable) in enumerate(keys, start=1):
        per = {}
        for label, r in runs:
            hits = [d for (a, v, _s), d in r.items() if (a, v) == (actor, variable)]
            per[label] = hits[0] if len(hits) == 1 else None if not hits else _clash(hits)
        derived = [d for d in per.values() if d]
        first = derived[0]
        signs = {lab: (d["sign"] if d else "none") for lab, d in per.items()}
        uniform = len(set(signs.values())) == 1
        sets = sorted({tuple(s) for d in derived for s in d["sets"]})
        minimal = [list(s) for s in sets if not any(set(o) < set(s) for o in sets)]
        best = max(minimal, key=lambda s: (math.prod(assumptions[a].p for a in s), -len(s)))
        consequences.append(Consequence(
            id=f"C-{n}",
            actor_class=actor,
            variable=variable,
            sign=first["sign"] if uniform else "ambiguous",
            horizon=[h for h in HORIZON_ORDER if HORIZON_ORDER[h] >= min(HORIZON_ORDER[d["horizon"]] for d in derived)],
            visibility=first["visibility"],
            tier=first["tier"],
            derivation=first["derivation"],
            assumption_sets=[sorted(s) for s in minimal],
            assumptions=sorted(best),
            reported=all(assumptions[a].p >= CUTOFF for a in best),
            sign_by_reading={} if uniform else signs,
        ))
    return consequences, base


def _clash(hits: list[dict]) -> dict:
    """Two rules give opposite signs for one actor and variable in one run: leave it to the combiner
    by keeping the first and flagging the clash in its derivation."""
    d = dict(hits[0])
    d["sign"] = "ambiguous"
    d["derivation"] = [s for h in hits for s in h["derivation"]]
    d["sets"] = [s for h in hits for s in h["sets"]]
    return d


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
