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
    ("keepers_dominate", "other",
     "Taking all protected tenants together, will the fall in moves out of the area among those who keep their units be larger than the rise among those displaced by conversion or withdrawal?",
     "Among all protected tenants, the fall in moves out of the area among keepers outweighs the rise among the displaced."),
    ("substitutes", "substitutability",
     "Do buyers who cannot obtain a covered unit turn to uncovered units in the same market, which are close substitutes?",
     "Uncovered units in the same market are close substitutes for covered ones."),
]


# Per-unit taxes (TX-1, TX-2). The wedge needs one side able to cut its quantity; the incidence premises
# stand in for DM-1 (the rule leaves the split open), so each side's price effect is its own claim.
TAX_QUESTIONS = [
    ("quantity_responds", "substitutability",
     "Can buyers cut back or switch to substitutes, or can sellers move resources to untaxed uses, so that the quantity traded falls once the tax is in place?",
     "At least one side can reduce the quantity it trades in response to the tax."),
    ("buyers_bear", "other",
     "Will part of the tax be passed on to buyers, so that the price they pay rises?",
     "Part of the tax is passed on to buyers: the price they pay rises."),
    ("sellers_bear", "other",
     "Will part of the tax stay with sellers, so that the price they keep after tax falls?",
     "Part of the tax stays with sellers: the price they keep after tax falls."),
]

# Tariffs (TX-7, TX-8).
TARIFF_QUESTIONS = [
    ("binding", "binding",
     "Do imports remain a meaningful share of supply after the tariff, and will foreign sellers fail to absorb most of it (they have many other markets, the country buys a small share of the world's supply)?",
     "Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff."),
    ("domestic_substitutes", "substitutability",
     "Can domestic producers raise output (spare or idle capacity) and make close substitutes for most imports?",
     "Domestic producers can raise output and make close substitutes for most imports."),
    ("no_offset", "other",
     "Is the fall in imports left unoffset by capital flows or other adjustments in the currency market within the medium run?",
     "The fall in imports is not offset by capital flows or other adjustments within the medium run."),
]

# RS-14, asked of any tax or tariff whose record names downstream users of the taxed good as an input.
INPUT_QUESTION = ("input_not_replaceable", "substitutability",
                  "Is the taxed good a material part of the downstream users' costs, and can they not replace it at the old cost in the medium run (other materials, other designs)?",
                  "The taxed good is a material part of downstream costs and cannot be replaced at the old cost.")
EXEMPT_QUESTION = ("competitors_exempt", "other",
                   "Do the downstream users compete with sellers who do not face the higher cost (imported finished goods, untaxed products)?",
                   "Many downstream users compete with sellers who do not face the higher input cost.")


def _specs(comp: Component) -> list[tuple[str, str, str, str]]:
    """The (atom, class, question, assumption text) list for a component, by instrument."""
    if comp.instrument == "price_ceiling":
        return CEILING_QUESTIONS
    if comp.instrument not in ("per_unit_tax", "tariff"):
        return []
    specs = list(TAX_QUESTIONS if comp.instrument == "per_unit_tax" else TARIFF_QUESTIONS)
    if comp.downstream:
        specs.append(INPUT_QUESTION)
        if any(d.competitors == "exempt" for d in comp.downstream):
            specs.append(EXEMPT_QUESTION)
    return specs


def questions_for(comp: Component) -> list[tuple[Question, str]]:
    """Typed questions for a component, each with the text of the assumption it estimates."""
    return [(Question(id=f"{comp.id}.{atom}", kind="noul", text=text, assumption=atom, assumption_class=cls), assumed)
            for atom, cls, text, assumed in _specs(comp)]


def ceiling_questions(comp: Component) -> list[Question]:
    return [q for q, _ in questions_for(comp)] if comp.instrument == "price_ceiling" else []


ASSUMPTION_TEXT = {atom: text for atom, _, _, text in CEILING_QUESTIONS}
