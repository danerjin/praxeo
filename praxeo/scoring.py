"""Scoring against an outcome card (plan 7.3 and 7.4).

- Only reported consequences (every assumption p >= cut-off) are scored: headline accuracy.
- Logic accuracy rescores those whose assumptions the card shows all held.
- Predictions are deduplicated on (actor class, variable, horizon).
- Ambiguous predictions are excluded from precision and count as not recalled.
- Unverifiable predictions (no finding of any type on that actor, variable and horizon)
  are excluded from precision; their rate is reported.
- Assumption estimates are scored with the Brier score where the card records the status.
"""
from __future__ import annotations

from .schema import Assumption, Consequence, Finding, OutcomeCard


def actors_overlap(a: str, b: str) -> bool:
    """Same class, or one is a subclass of the other (tenants vs tenants.controlled)."""
    return a == b or a.startswith(b + ".") or b.startswith(a + ".")


def _covers(c: Consequence, f: Finding) -> bool:
    return actors_overlap(c.actor_class, f.actor_class) and c.variable == f.variable and bool(set(c.horizon) & set(f.horizon))


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


def score(consequences: list[Consequence], assumptions: dict[str, Assumption], card: OutcomeCard) -> dict:
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
    }


def _bare(atom: str) -> str:
    """'enforced(c1)' -> 'enforced'; the card records assumption status by type within the case."""
    return atom.split("(", 1)[0]
