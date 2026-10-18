"""Symbolic engine (Configuration A): clingo over the rule base.

The policy record and the decider's assumption estimates become ASP facts.
The rule base opens a choice over every assumption; enumerating all answer
sets gives, for each conclusion, every assumption set under which it is
derived. Keeping only the minimal sets yields an ATMS-style label
(plan 4.4): "this follows if A and B".

Rule-base conventions beyond effect/7 (all optional, all documented in rules/*.lp):
- group_effect(Concl, Actor, "member1,member2", Sign, Horizon, Visibility, Tier): a group consequence; Sign is
  at_least_one_increase or at_least_one_decrease and the members are comma-separated variable names.
- window(Concl, announcement|first_months|after_expiry): the conclusion is signed for a timing window (RS-8, SB-6);
  an announcement-window conclusion has horizon short.
- item(Concl, "name"): the conclusion is one named item of a variable that opposite chains move (CR-12 0.8).
Consequences are keyed by (actor, variable, window, item). The rules stay monotone in holds/1 (only plain facts
such as exception/2 and announced/1 are negated), which the minimal-set search relies on.

Unclear provisions: the engine runs once per reading (adding that reading's
facts) and merges the results; where the readings disagree, the consequence
carries a sign per reading (02_ontology.md, per-reading signs).
"""
from __future__ import annotations

import itertools
import math
from pathlib import Path

import clingo
import clingo.ast

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


SUBSIDIES = ("per_unit_subsidy", "purchase_rebate", "lump_sum_subsidy")


def _subsidy_facts(c: str, comp) -> list[str]:
    lines = [f"subsidy({c}).", f'sb_recipient({c}, "{comp.bound_actor}").',
             f'enforcer({c}, "{comp.enforcer_actor}").', f'taxpayer({c}, "{comp.taxpayer_actor}").',
             f'sb_claim_handler({c}, "{comp.claim_handler_actor or comp.bound_actor}").']
    if comp.instrument != "lump_sum_subsidy":
        lines.append(f"per_unit_sub({c}).")
    if comp.seller_actor and comp.seller_actor != comp.bound_actor:
        lines.append(f'sb_seller({c}, "{comp.seller_actor}").')
    else:
        lines.append(f"sb_recipients_sell({c}).")
    lines.append(f'sb_qualifier({c}, "{comp.qualifier_actor or comp.bound_actor}").')
    if comp.tax_named:
        lines.append(f"tax_named({c}).")
    payers = [comp.taxpayer_actor, comp.other_spending_actor, comp.future_taxpayer_actor]
    lines.append(f'sb_payer_group({c}, "{",".join(dict.fromkeys(p for p in payers if p))}").')
    for pred, actor in (("sb_other_buyer", comp.other_buyer_actor), ("sb_substitute_seller", comp.substitute_seller_actor),
                        ("sb_asset_owner", comp.asset_owner_actor), ("sb_used_buyer", comp.used_buyer_actor),
                        ("sb_used_owner", comp.used_owner_actor), ("sb_scrapper", comp.scrapper_actor)):
        if actor:
            lines.append(f'{pred}({c}, "{actor}").')
    for pred, flag in (("own_revenue", comp.own_revenue_funded), ("debt_funded", comp.debt_funded),
                       ("criteria", comp.eligibility_criteria), ("renewable", comp.renewable),
                       ("budget_capped", comp.budget_capped), ("temporary", comp.temporary),
                       ("scrappage", comp.scrappage), ("repay_on_move", comp.repay_on_move)):
        if flag:
            lines.append(f"{pred}({c}).")
    return lines


def _tax_facts(c: str, comp) -> list[str]:
    lines = [f"{'tax' if comp.instrument == 'per_unit_tax' else 'tariff'}({c}).",
             f'buyer({c}, "{comp.buyer_actor}").',
             f'domestic_seller({c}, "{comp.domestic_seller_actor}").',
             f'importer({c}, "{comp.importer_actor or comp.bound_actor}").',
             f'revenue({c}, "{comp.revenue_actor}").',
             f'exporter({c}, "{comp.exporter_actor}").',
             f'exporter_worker({c}, "{comp.exporter_worker_actor or "workers." + comp.exporter_actor}").']
    if comp.seller_actor:
        lines.append(f'seller({c}, "{comp.seller_actor}").')
    lines.append(f'enforcer({c}, "{comp.enforcer_actor}").')
    lines.append(f'taxpayer({c}, "{comp.taxpayer_actor}").')
    if comp.domestic_seller_worker_actor:
        lines.append(f'domestic_seller_worker({c}, "{comp.domestic_seller_worker_actor}").')
    lines.append(f'foreign_seller({c}, "{comp.foreign_seller_actor}").')
    for pred, actor in (("input_supplier", comp.input_supplier_actor), ("seller_owner", comp.domestic_seller_owner_actor),
                        ("relief_applicant", comp.relief_applicant_actor)):
        if actor:
            lines.append(f'{pred}({c}, "{actor}").')
    for pred, actor in (("mobile_buyer", comp.mobile_buyer_actor), ("neighbor_seller", comp.neighbor_seller_actor)):
        if actor:
            lines.append(f'{pred}({c}, "{actor}").')
    for pred, flag in (("renewable", comp.renewable), ("definition_line", comp.definition_line),
                       ("rate_rise", comp.rate_rise), ("own_revenue", comp.own_revenue_funded)):
        if flag:
            lines.append(f"{pred}({c}).")
    for d in comp.downstream:
        lines.append(f'downstream({c}, "{d.actor}", "{d.buyer_actor}", {d.competitors}).')
        if d.owner_actor:
            lines.append(f'downstream_owner({c}, "{d.actor}", "{d.owner_actor}").')
        if d.exporter_actor:
            lines.append(f'downstream_exporter({c}, "{d.actor}", "{d.exporter_actor}").')
        if d.worker_actor:
            lines.append(f'downstream_worker({c}, "{d.actor}", "{d.worker_actor}").')
    return lines


def facts(record: PolicyRecord, assumptions: dict[str, Assumption]) -> str:
    lines = []
    for comp in record.components:
        c = _atom(comp.id)
        if comp.instrument == "price_ceiling" and comp.third_party_payer_actor:
            # PC-20: a cap on the buyer's share, the rest paid by a third party; the seller's price is not capped
            lines += [f"share_cap({c}).", f'share_payer({c}, "{comp.third_party_payer_actor}").']
        elif comp.instrument == "price_ceiling":
            lines.append(f"ceiling({c}).")
        if comp.vacancy_decontrol:
            lines.append(f"decontrol({c}).")
        if comp.evasion_by_resellers:
            lines.append(f"resale_evasion({c}).")
        lines.append(f'bound({c}, "{comp.bound_actor}").')
        if comp.protected_actor:
            lines.append(f'protected({c}, "{comp.protected_actor}").')
        lines.append(f'excluded({c}, "{comp.excluded_actor or "buyers.prospective"}").')
        if comp.announcement_window:
            lines.append(f"announced({c}).")
        if comp.field_contested:
            lines.append(f"field_contested({c}).")
        if comp.instrument == "price_ceiling":
            lines.append(f'enforcer({c}, "{comp.enforcer_actor}").')
            if comp.general_budget:
                lines.append(f'taxpayer({c}, "{comp.taxpayer_actor}").')
            if comp.neighbor_actor:
                lines.append(f'neighbor({c}, "{comp.neighbor_actor}").')
            if comp.input_supplier_actor:
                lines.append(f'input_supplier({c}, "{comp.input_supplier_actor}").')
            if comp.protected_concentrated:
                lines.append(f"protected_concentrated({c}).")
        if comp.instrument in ("per_unit_tax", "tariff"):
            lines += _tax_facts(c, comp)
        if comp.instrument in SUBSIDIES:
            lines += _subsidy_facts(c, comp)
    for a in assumptions:
        lines.append(f"assumption({a}).")
    return "\n".join(lines) + "\n"


def _solve(program: str, args: list[str], extra: str = "") -> list[list[clingo.Symbol]]:
    ctl = clingo.Control(["0", "--warn=none", *args])
    for rules in RULES:
        ctl.load(str(rules))
    ctl.add("base", [], program + extra)
    ctl.ground([("base", [])], context=_Context())
    out: list[list[clingo.Symbol]] = []
    ctl.solve(on_model=lambda m: out.append(list(m.symbols(shown=True))))
    return out


def _minimal_sets(program: str, concl: str) -> list[frozenset[str]]:
    """Every subset-minimal set of assumptions under which `concl` is derived (the ATMS label).

    Enumerating all 2^n choices of assumptions does not scale past a dozen assumptions, so each conclusion
    is asked for separately: the rules are monotone in `holds`, and clingo's domain-heuristic mode
    (`domRec`, with every `holds` preferred false) enumerates the subset-minimal models that derive it."""
    models = _solve(program, ["--heuristic=Domain", "--enum-mode=domRec"],
                    f"\n#heuristic holds(A) : assumption(A). [1, false]\n:- not {concl}.\n")
    sets = {frozenset(str(s.arguments[0]) for s in m if s.name == "holds") for m in models}
    return sorted({s for s in sets if not any(o < s for o in sets)}, key=lambda s: (len(s), sorted(s)))


def invalid_reading_facts(unclear) -> list[str]:
    """Labels whose reading facts are not valid clingo (e.g. prose a parser wrote). Such readings are skipped."""
    bad = []
    for label, text in unclear.reading_facts.items():
        try:
            clingo.ast.parse_string(text, lambda _stmt: None)
        except RuntimeError:
            bad.append(label)
    return bad


def readings(record: PolicyRecord) -> list[tuple[str, str]]:
    """Every combination of readings of the unclear provisions that carry facts: (label, facts)."""
    branching = [u for u in record.unclear if u.reading_facts and not invalid_reading_facts(u)]
    if not branching:
        return [("", "")]
    out = []
    for combo in itertools.product(*[u.labels() for u in branching]):
        label = "; ".join(combo)
        extra = "\n".join(u.reading_facts.get(lab, "") for u, lab in zip(branching, combo))
        out.append((label, extra + "\n"))
    return out


def _name(sym: clingo.Symbol) -> str:
    return sym.string if sym.type == clingo.SymbolType.String else sym.name


def _derive(program: str, assumptions: dict[str, Assumption]) -> dict[tuple, dict]:
    """One engine run. Returns {(actor, variable, window, item, sign): {horizon, visibility, tier, concl, sets, derivation}}.
    For a group consequence `variable` is the comma-separated member list.

    The model with every assumption held gives all derivable steps and effects (the rules are monotone in
    `holds`); the assumption sets of each conclusion are then found one conclusion at a time."""
    steps: dict[str, set[tuple[str, str]]] = {}
    effects: list[tuple[str, tuple]] = []
    windows: dict[str, str] = {}
    items: dict[str, str] = {}
    for model in _solve(program, [], "\n:- assumption(A), not holds(A).\n"):
        for s in model:
            if s.name == "fired":
                rule, concl, prem = (str(a) for a in s.arguments)
                steps.setdefault(concl, set()).add((rule, prem))
            elif s.name in ("effect", "group_effect"):
                effects.append((str(s.arguments[0]), tuple(_name(a) for a in s.arguments[1:])))
            elif s.name == "window":
                windows[str(s.arguments[0])] = _name(s.arguments[1])
            elif s.name == "item":
                items[str(s.arguments[0])] = _name(s.arguments[1])
    minimal_by_concl = {c: _minimal_sets(program, c) for c in sorted({c for c, _ in effects})}
    out = {}
    for concl, (actor, variable, sign, horizon, visibility, tier) in effects:
        window, item = windows.get(concl), items.get(concl)
        key = (actor, variable, window, item, sign)
        row = dict(
            concl=concl, actor=actor, variable=variable, sign=sign, horizon=horizon, window=window, item=item,
            visibility=visibility, tier=tier, sets=minimal_by_concl[concl], derivation=_derivation(concl, steps))
        if key in out:
            # two components (or two rules) reach the same row: it follows under either support, so the label is the
            # union of the minimal sets and the derivation keeps both chains
            row["sets"] = out[key]["sets"] + row["sets"]
            row["derivation"] = out[key]["derivation"] + [st for st in row["derivation"] if st not in out[key]["derivation"]]
            row["horizon"] = min(horizon, out[key]["horizon"], key=HORIZON_ORDER.get)
        out[key] = row
    return out


def run(record: PolicyRecord, assumptions: dict[str, Assumption], extra: str = "") -> tuple[list[Consequence], str]:
    """Derive consequences. `assumptions` maps the ASP atom (e.g. 'enforced(c1)') to its estimate;
    `extra` adds facts such as `exception(pc_5, c1).` from context grounding."""
    base = facts(record, assumptions) + extra
    runs = [(label, _derive(base + rf, assumptions)) for label, rf in readings(record)]

    # merge across readings on (actor, variable, window, item): same sign everywhere, or a sign per reading
    keys = sorted({(a, v, w, i) for _, r in runs for (a, v, w, i, _s) in r}, key=lambda k: tuple(x or "" for x in k))
    consequences = []
    for n, (actor, variable, window, item) in enumerate(keys, start=1):
        per = {}
        for label, r in runs:
            hits = [d for (a, v, w, i, _s), d in r.items() if (a, v, w, i) == (actor, variable, window, item)]
            per[label] = hits[0] if len(hits) == 1 else None if not hits else _resolve(hits, assumptions)
        derived = [d for d in per.values() if d]
        first = derived[0]
        signs = {lab: (d["sign"] if d else "none") for lab, d in per.items()}
        uniform = len(set(signs.values())) == 1
        sets = sorted({tuple(s) for d in derived for s in d["sets"]})
        minimal = [list(s) for s in sets if not any(set(o) < set(s) for o in sets)]
        best = max(minimal, key=lambda s: (math.prod(assumptions[a].p for a in s), -len(s)))
        members = variable.split(",") if "," in variable else []
        # a group_effect over actor classes names them as one comma-separated string (OC-1, who pays)
        actors = actor.split(",") if "," in actor else []
        # an announcement-window response is a short-horizon prediction; other effects hold from their first horizon on
        first_h = min(HORIZON_ORDER[d["horizon"]] for d in derived)
        horizon = ["short"] if window == "announcement" else [h for h in HORIZON_ORDER if HORIZON_ORDER[h] >= first_h]
        consequences.append(Consequence(
            id=f"C-{n}",
            actor_class=actors[0] if actors else actor,
            actor_group=actors,
            variable=members[0] if members else variable,
            group=members,
            window=window,
            item=item,
            sign=first["sign"] if uniform else "ambiguous",
            horizon=horizon,
            visibility=first["visibility"],
            tier=first["tier"],
            derivation=first["derivation"],
            assumption_sets=[sorted(s) for s in minimal],
            assumptions=sorted(best),
            reported=all(assumptions[a].p >= CUTOFF for a in best),
            sign_by_reading={} if uniform else signs,
        ))
    return consequences, base


def _resolve(hits: list[dict], assumptions: dict[str, Assumption]) -> dict:
    """Rules give opposite signs for one actor and variable in one run. The sign comes from the chains that are reported:
    where exactly one sign has a minimal set with every p >= cut-off, it is that sign (an opposing chain below the cut-off
    is not reported, so it cannot make the row ambiguous); otherwise the clash stands."""
    def reportable(h):
        return any(all(assumptions[a].p >= CUTOFF for a in s) for s in h["sets"])
    signs = {h["sign"] for h in hits if reportable(h)}
    if len(signs) == 1:
        keep = [h for h in hits if h["sign"] in signs]
        return keep[0] if len(keep) == 1 else _clash(keep)
    return _clash(hits)


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
