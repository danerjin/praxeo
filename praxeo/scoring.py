"""Scoring against an outcome card (plan 7.3 and 7.4).

- Only reported consequences (every assumption p >= cut-off) are scored: headline accuracy.
- Logic accuracy rescores those whose assumptions the card shows all held.
- Predictions are deduplicated on (actor class, variable, horizon).
- Ambiguous predictions are excluded from precision and count as not recalled.
- Unverifiable predictions (no finding of any type on that actor, variable and horizon)
  are excluded from precision; their rate is reported.
- Actor classes match only when they are the same class. A subclass's sign can differ
  from its class's total (CR-12; PC-21 1.4: keepers against the displaced), so a finding
  on a class neither confirms nor refutes a prediction on one of its subclasses.
- Variables are checked against the shared vocabulary (02_ontology.md, 2.4).
- Assumption estimates are scored with the Brier score where the card records the status.
"""
from __future__ import annotations

from . import vocabulary
from .schema import Assumption, Consequence, Finding, OutcomeCard


def _covers(c: Consequence, f: Finding) -> bool:
    return c.actor_class == f.actor_class and c.variable == f.variable and bool(set(c.horizon) & set(f.horizon))


def _matches(c: Consequence, f: Finding) -> bool:
    return f.finding_type == "effect" and _covers(c, f) and c.sign == f.sign


def dedupe(preds: list[Consequence]) -> list[Consequence]:
    seen, out = set(), []
    for c in preds:
        key = (c.actor_class, c.variable, tuple(c.horizon))
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out


def f1_block(preds: list[Consequence], card: OutcomeCard) -> dict:
    preds = dedupe(preds)
    effects = [f for f in card.findings if f.finding_type == "effect"]
    signed = [c for c in preds if c.sign != "ambiguous"]
    verifiable = [c for c in signed if any(_covers(c, f) for f in card.findings)]
    matched = [c for c in verifiable if any(_matches(c, f) for f in card.findings)]
    recalled = [f for f in effects if any(_matches(c, f) for c in signed)]
    precision = len(matched) / len(verifiable) if verifiable else None
    recall = len(recalled) / len(effects) if effects else None
    if precision is None or recall is None:
        f1 = None
    else:
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {
        "predictions": len(preds),
        "ambiguous": len(preds) - len(signed),
        "verifiable": len(verifiable),
        "unverifiable": len(signed) - len(verifiable),
        "unverifiable_rate": (len(signed) - len(verifiable)) / len(signed) if signed else None,
        "matched": [c.id for c in matched],
        "false_positives": [c.id for c in verifiable if c not in matched],
        "unverifiable_ids": [c.id for c in signed if c not in verifiable],
        "recalled_findings": [f.id for f in recalled],
        "missed_findings": [f.id for f in effects if f not in recalled],
        "precision": precision,
        "recall": recall,
        "f1": f1,
    }


def vocabulary_problems(card: OutcomeCard) -> list[str]:
    return [f"{f.id}: {m}" for f in card.findings if (m := vocabulary.check_variable(f.variable))]


def role_names(card: OutcomeCard, record) -> dict[str, str]:
    """Record actor name -> card actor name, through the role fields the card declares (CR-12 subclass
    suffixes such as .keepers and .displaced follow their parent)."""
    out = {}
    for card_name, role in card.actor_roles.items():
        for comp in record.components:
            name = getattr(comp, role, None)
            if isinstance(name, str) and name and name != card_name:
                out[name] = card_name
                for suffix in (".keepers", ".displaced"):
                    out[name + suffix] = card_name + suffix
    return out


def score(consequences: list[Consequence], assumptions: dict[str, Assumption], card: OutcomeCard, record=None) -> dict:
    if record is not None and card.actor_roles:
        names = role_names(card, record)
        consequences = [c.model_copy(update={"actor_class": names.get(c.actor_class, c.actor_class)}) for c in consequences]
    status = {s.assumption: s.held for s in card.assumption_status}
    reported = [c for c in consequences if c.reported]
    held = [c for c in reported if c.assumptions and all(status.get(_bare(a)) is True for a in c.assumptions)]
    brier = [(a, assumptions[a].p, status[_bare(a)]) for a in assumptions if status.get(_bare(a)) is not None]
    return {
        "headline": f1_block(reported, card),
        "logic": f1_block(held, card),
        "brier": {
            "items": [{"assumption": a, "p": p, "held": h, "score": (p - float(h)) ** 2} for a, p, h in brier],
            "mean": sum((p - float(h)) ** 2 for _, p, h in brier) / len(brier) if brier else None,
        },
        "low_confidence_findings": [f.id for f in card.findings if f.confidence == "low"],
        "card_vocabulary_problems": vocabulary_problems(card),
    }


def _bare(atom: str) -> str:
    """'enforced(c1)' -> 'enforced'; the card records assumption status by type within the case."""
    return atom.split("(", 1)[0]
