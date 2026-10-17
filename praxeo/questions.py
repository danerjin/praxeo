"""Typed questions for the price-ceiling rules (plan 4.4, Configuration A).

Each noul question estimates one assumption the rule base names. The answer's
probability becomes that assumption's p, committed before any scoring.
"""
from __future__ import annotations

from .schema import Component, Question

# (assumption atom, ontology assumption class, question text, assumption text)
CEILING_QUESTIONS = [
    ("binding", "binding",
     "At the dates the rule takes effect and over the following years, is the maximum price below the price the market would otherwise reach for the covered units?",
     "The ceiling binds: it is below the price the market would otherwise reach."),
    ("enforced", "enforcement",
     "Will the ceiling be enforced against most of the bound sellers (a body that hears complaints, penalties larger than the gain from breaking it)?",
     "The ceiling is enforced against most bound sellers."),
    ("alternative_uses", "alternative_uses",
     "Can the bound sellers move the covered resources to uses the ceiling does not reach (sale to owner-occupiers, conversion, redevelopment, keeping units off the market)?",
     "Owners can move covered units to uses the ceiling does not reach."),
    ("nontransferable", "other",
     "Is the right to buy at the controlled price tied to keeping the good (a sitting tenancy), so that the holder cannot sell or assign it?",
     "The protected buyers' right is tied to holding the tenancy and cannot be sold."),
    ("buyouts_limited", "other",
     "Will payments from landlords to sitting tenants for giving up the tenancy (buyouts) move fewer tenants than the cap keeps in place?",
     "Buyouts move fewer tenants than the cap keeps in place."),
    ("would_leave", "mobility",
     "Without the rule, would some of the protected buyers have moved out of the area, priced out by market rents or for opportunities elsewhere, and does the benefit end if they do?",
     "Without the rule some protected buyers would have left the area, and the benefit does not follow them."),
    ("lockin_dominates", "other",
     "For tenants who keep a covered unit, does the lock-in outweigh moves out of the area by tenants who still move and face higher free rents in the city?",
     "The lock-in outweighs moves diverted out of the area by higher free rents."),
    ("substitutes", "substitutability",
     "Do buyers who cannot obtain a covered unit turn to uncovered units in the same market, which are close substitutes?",
     "Uncovered units in the same market are close substitutes for covered ones."),
]


def ceiling_questions(comp: Component) -> list[Question]:
    return [
        Question(
            id=f"{comp.id}.{atom}",
            kind="noul",
            text=text,
            assumption=atom,
            assumption_class=cls,
        )
        for atom, cls, text, _ in CEILING_QUESTIONS
    ]


ASSUMPTION_TEXT = {atom: text for atom, _, _, text in CEILING_QUESTIONS}
