"""Templated explainer: derivation tree -> plain sentences. No free text generation."""
from __future__ import annotations

from .schema import Assumption, Consequence, PolicyRecord

RULE_TEXT = {
    "PC-1": "a ceiling held below the price the market would reach leaves more buyers wanting units than sellers offer",
    "PC-3": "those who hold a covered unit pay the controlled price, while those shut out look elsewhere",
    "RS-4": "shut-out buyers turn to uncovered units, which are close substitutes",
    "PC-5": "owners move resources to uses whose yield the ceiling does not cap",
    "RS-5": "owners move units out of the rule's reach",
    "PC-7": "the benefit is tied to staying put and cannot be sold, so holders move less",
    "PC-21": "leaving the area forfeits the benefit, and fewer holders are priced out, so they leave the area less",
}

SIGN_WORD = {"increase": "rises", "decrease": "falls", "ambiguous": "may move either way", "no_change": "does not change"}


def explain(c: Consequence, assumptions: dict[str, Assumption], record: PolicyRecord) -> str:
    rules = []
    for step in c.derivation:
        if step.rule not in rules:
            rules.append(step.rule)
    chain = "; ".join(f"{r}: {RULE_TEXT.get(r, r)}" for r in rules)
    when = f"from the {c.horizon[0]} run onward" if len(c.horizon) > 1 else f"in the {c.horizon[0]} run"
    conds = "; ".join(f"{assumptions[a].text.rstrip('.')} (p = {assumptions[a].p:.2f})" for a in c.assumptions) or "no assumption"
    alt = ""
    if len(c.assumption_sets) > 1:
        alt = f" It also follows under {len(c.assumption_sets) - 1} other minimal assumption set(s)."
    status = "Reported." if c.reported else "Not reported: an assumption is below the 0.5 cut-off."
    return (
        f"{c.id}. Compared with no {record.name}, {c.variable.replace('_', ' ')} for {c.actor_class} "
        f"{SIGN_WORD[c.sign]} {when} (tier {c.tier}, {c.visibility}). "
        f"Why: {chain}. This holds if: {conds}.{alt} {status}"
    )
