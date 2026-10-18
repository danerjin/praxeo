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
- Group consequences (at_least_one_increase / at_least_one_decrease over several variables, plan 7.4): a group
  prediction is verifiable if the card has a finding of any type on any member for that actor and horizon. It matches if an
  `effect` finding on a member has the group's direction. It is a false positive only if every member has a finding for
  that actor and horizon and each is null or opposite; a verifiable group prediction that is neither is unresolved (some
  members have no finding, none has the direction), and is left out of precision. It recalls the effect findings on its
  members that have its direction.
- Announcement-window consequences carry horizon ["short"] and are scored as short-horizon predictions; they are kept
  apart from the ordinary consequence of the same actor and variable when deduplicating. Items (the parts of a CR-12 total
  over two items of one variable) are not scored: the total is. An item of a variable with no total (SB-3's unsubsidized
  goods) is scored as it stands.
- Variables are checked against the shared vocabulary (02_ontology.md, 2.4).
- Assumption estimates are scored with the Brier score where the card records the status.
"""
from __future__ import annotations

from . import vocabulary
from .schema import GROUP_SIGNS, Assumption, Consequence, Finding, OutcomeCard


def _covers(c: Consequence, f: Finding) -> bool:
    """The finding is about this prediction's actor and horizon, and about its variable (any member, for a group)."""
    return f.actor_class in c.actors() and f.variable in c.members() and bool(set(c.horizon) & set(f.horizon))


def _direction(c: Consequence) -> str:
    return GROUP_SIGNS.get(c.sign, c.sign)


def _matches(c: Consequence, f: Finding) -> bool:
    return f.finding_type == "effect" and _covers(c, f) and _direction(c) == f.sign


def _refuted(c: Consequence, card: OutcomeCard) -> bool:
    """A verifiable prediction is a false positive. An ordinary one is when no finding matches. A group prediction is
    only when every member has a finding for the actor and horizon, and each is a null or the opposite direction."""
    findings = [f for f in card.findings if _covers(c, f)]
    if not (c.group or c.actor_group):
        return not any(_matches(c, f) for f in findings)
    return (not any(_matches(c, f) for f in findings)
            and all(any((f.actor_class, f.variable) == (a, m) for f in findings) for a in c.actors() for m in c.members()))


def dedupe(preds: list[Consequence]) -> list[Consequence]:
    seen, out = set(), []
    for c in preds:
        key = (tuple(c.actors()), tuple(c.members()), tuple(c.horizon), c.window, c.item)
        if key not in seen:
            seen.add(key)
            out.append(c)
    return out


def f1_block(preds: list[Consequence], card: OutcomeCard, every: list[Consequence] | None = None) -> dict:
    """`every` is the whole prediction, of which `preds` may be a subset (the logic score): an item is left out wherever
    the prediction has a total over its variable, whether or not the total is in the subset."""
    totals = {(c.actor_class, c.variable, c.window) for c in (every or preds) if c.item is None and c.combines}
    preds = dedupe([c for c in preds if c.item is None or (c.actor_class, c.variable, c.window) not in totals])
    effects = [f for f in card.findings if f.finding_type == "effect"]
    signed = [c for c in preds if c.sign != "ambiguous"]
    verifiable = [c for c in signed if any(_covers(c, f) for f in card.findings)]
    matched = [c for c in verifiable if any(_matches(c, f) for f in card.findings)]
    false_pos = [c for c in verifiable if c not in matched and _refuted(c, card)]
    unresolved = [c for c in verifiable if c not in matched and c not in false_pos]
    recalled = [f for f in effects if any(_matches(c, f) for c in signed)]
    judged = len(matched) + len(false_pos)  # = verifiable, less the unresolved group predictions
    precision = len(matched) / judged if judged else None
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
        "false_positives": [c.id for c in false_pos],
        "unresolved_group_ids": [c.id for c in unresolved],
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
        consequences = [c.model_copy(update={"actor_class": names.get(c.actor_class, c.actor_class),
                                             "actor_group": [names.get(a, a) for a in c.actor_group]}) for c in consequences]
    status = {s.assumption: s.held for s in card.assumption_status}
    reported = [c for c in consequences if c.reported]
    held = [c for c in reported if c.assumptions and all(status.get(_bare(a)) is True for a in c.assumptions)]
    brier = [(a, assumptions[a].p, status[_bare(a)]) for a in assumptions if status.get(_bare(a)) is not None]
    return {
        "headline": f1_block(reported, card, consequences),
        "logic": f1_block(held, card, consequences),
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
