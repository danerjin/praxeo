"""Typed questions (plan 4.4) for the rules in praxeo/rules/.

Each noul question estimates one assumption the rule base names. The answer's
probability becomes that assumption's p, committed before any scoring.

Question-schema rules (plan 6.2): one concept per question; no "and" joining two
claims; examples in brackets illustrate, they are not extra conditions; say which
way a mechanism runs when it is easy to misread (TX-8). Revised after the first
LLM-stage run, where double-barrelled questions produced the largest disagreements.
"""
from __future__ import annotations

from .schema import Component, Question

# (assumption atom, ontology assumption class, question text, assumption text)
CEILING_QUESTIONS = [
    ("binding", "binding",
     "At the dates the rule takes effect and over the following years, is the maximum price below the price the market would otherwise reach for the covered units?",
     "The ceiling binds: it is below the price the market would otherwise reach."),
    ("enforced", "enforcement",
     "Will most of the bound sellers comply with the ceiling in practice (given whatever body enforces it, its powers, and how violations come to light)?",
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
     "Without the rule, would some of the protected buyers have moved out of the area (priced out by market rents, or for opportunities elsewhere)?",
     "Without the rule some protected buyers would have left the area."),
    ("lockin_dominates", "other",
     "For tenants who keep a covered unit, does the lock-in outweigh moves out of the area by tenants who still move and face higher free rents in the city?",
     "The lock-in outweighs moves diverted out of the area by higher free rents."),
    ("keepers_dominate", "other",
     "Taking all protected tenants together, will the fall in moves out of the area among those who keep their units be larger than the rise among those displaced by conversion or withdrawal?",
     "Among all protected tenants, the fall in moves out of the area among keepers outweighs the rise among the displaced."),
    ("substitutes", "substitutability",
     "Are uncovered units in the same market close substitutes for covered units, for buyers who cannot obtain a covered one?",
     "Uncovered units in the same market are close substitutes for covered ones."),
    # PC-2 (one question per member of the rationing group: each margin needs its own premise)
    ("search_open", "other",
     "Is there no public list or allocation rule that assigns the covered good to buyers, so that buyers have to find sellers by their own search?",
     "Seekers find covered units by their own search: no public list or allocation rule assigns them."),
    ("selection_open", "other",
     "Are sellers free to choose among applicants for the covered good by criteria of their own (income, credit, references, connections)?",
     "Sellers may choose among applicants by criteria of their own."),
    # PC-4, RS-2
    ("quality_adjustable", "other",
     "Can the bound sellers cut quality or maintenance below what they now supply without breaking a rule that is enforced (a code, a contract term)?",
     "Sellers have room to cut quality or maintenance above any enforced minimum."),
    # PC-6, RS-3
    ("evasion", "enforcement",
     "Will some exchanges of the covered good take place above the ceiling, disguised or illegal (key money, tie-in sales, sublets at market rent), without being caught?",
     "Some exchanges take place above the ceiling without being caught."),
    # RS-11
    ("opportunities_need_move", "mobility",
     "Would some valued opportunities for the protected buyers (a job, a better home) require them to give up the covered unit?",
     "Some valued opportunities for the protected buyers would require giving up the covered unit."),
    # RS-7
    ("can_organize", "other",
     "Can the groups with a concentrated stake in the rule (those it helps, those it burdens) organize and spend to keep or change it at a cost below their stakes?",
     "The groups with a concentrated stake can organize and spend to keep or change the rule."),
    # SB-4
    ("durable_assets", "durability",
     "Are the assets the bound sellers use to supply the covered good durable, so that the supply of them expands only slowly?",
     "The covered assets are durable and their supply expands slowly."),
    ("expected_to_last", "expectations",
     "Do buyers of the covered assets expect the rule to stay in force for many years?",
     "Buyers of the covered assets expect the rule to last for many years."),
    # RS-4
    ("commutable", "mobility",
     "Can buyers who cannot obtain a covered unit buy in a neighbouring market outside the rule's reach at a cost (travel, time) they are willing to bear?",
     "Shut-out buyers can buy in a neighbouring market outside the rule's reach at a bearable cost."),
    # PC-5, RS-5, CR-4
    ("relet_obstructs", "other",
     "Does letting a vacated covered unit to a new tenant make it harder for the owner to move the unit to an alternative use later (eviction only for cause, relocation payments)?",
     "Re-letting a vacated unit obstructs the owner's later move to an alternative use."),
    # OC-2
    ("exit_process", "other",
     "Does moving covered units to an alternative use require passing a permit or board process?",
     "Moving covered units to an alternative use requires a permit or board process."),
]


# Per-unit taxes (TX-1, TX-2). The wedge needs one side able to cut its quantity; the incidence premises
# stand in for DM-1 (the rule leaves the split open), so each side's price effect is its own claim.
TAX_QUESTIONS = [
    ("quantity_responds", "substitutability",
     "Will the quantity traded fall once the tax is in place (because buyers cut back or switch, or sellers move resources to untaxed uses)?",
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
     "Will the price domestic buyers pay for the covered goods rise by a substantial part of the tariff, rather than foreign sellers absorbing most of it?",
     "The domestic price rises by a substantial part of the tariff; foreign sellers do not absorb most of it."),
    ("domestic_substitutes", "substitutability",
     "Do domestic producers make goods that buyers can use in place of the covered imports, so that dearer imports send buyers to them?",
     "Domestic producers make close substitutes for the covered imports."),
    ("no_offset", "other",
     ("When the country buys fewer imports, foreigners earn less of its currency. Through the exchange rate (the currency "
      "rises against what it would otherwise be) this makes the country's exports dearer abroad, so export industries sell "
      "less: that is the mechanism, not an offset to it. Over the medium run, will this chain operate, rather than being "
      "cancelled by foreigners investing or lending more in the country?"),
     "Lower imports reduce foreigners' purchases of the country's exports in the medium run; capital flows do not cancel it."),
]

# RS-14, asked of any tax or tariff whose record names downstream users of the taxed good as an input.
INPUT_QUESTION = ("input_not_replaceable", "substitutability",
                  "Will the downstream users' costs rise materially because of the higher price of the taxed good (given how much of it they use and whether they can switch to other materials or designs in the medium run)?",
                  "The taxed good is a material part of downstream costs and cannot be replaced at the old cost.")
EXEMPT_QUESTION = ("competitors_exempt", "other",
                   "Do the downstream users compete with sellers who do not face the higher cost (imported finished goods, untaxed products)?",
                   "Many downstream users compete with sellers who do not face the higher input cost.")

# OC-3: asked of every tax or tariff.
BUDGET_QUESTION = ("enforcement_budget_raised", "revenue_use",
                   "Will the budget of the agency that administers the measure be raised to cover the new work, rather than the work being absorbed within its existing budget?",
                   "The administering agency's budget is raised to cover the new work, so taxpayers fund it.")

# Asked only when the record carries the fact the rule needs (definition_line, relief_applicant_actor, renewable,
# owner and exporter actors, downstream groups), so that no question is posed about a role the record leaves empty.
RESHAPING_QUESTION = ("reshaping_pays", "other",
                      "For some of the actors bound by the measure, will reshaping goods so that they fall outside the measure's definitions cost less than the measure would cost them?",
                      "Reshaping goods to fall outside the definitions costs some actors less than the burden.")
DISCRETIONARY_QUESTION = ("relief_discretionary", "other",
                          "Will the officials who grant exclusions, waivers or exemptions decide case by case, with room to weigh who the applicant is or what others say against it, rather than by a fixed published test?",
                          "Relief is granted case by case at officials' discretion.")
VALUABLE_QUESTION = ("relief_valuable", "other",
                     "Is an exclusion, waiver or exemption worth more to those who apply than the fee for applying?",
                     "Relief is worth more to applicants than its fee.")
BENEFICIARIES_ORGANIZE = ("beneficiaries_organize", "other",
                          "Can the protected domestic producers organize to influence the renewal or extension decision at a cost lower than what they stand to gain?",
                          "The protected producers can organize to influence renewal at a cost below their stake.")
HARMED_ORGANIZE = ("harmed_organize", "other",
                   "Can the downstream users who cannot pass the higher cost on organize to seek repeal, exemption or non-renewal at a cost lower than what they stand to lose?",
                   "The harmed users can organize to seek repeal or exemption at a cost below their stake.")
EXTENSION_QUESTION = ("expects_extension", "expectations",
                      "Do the protected domestic producers expect the measure to be renewed or extended when it comes up for review?",
                      "The protected producers expect the measure to be renewed or extended.")
LASTING_QUESTION = ("expected_to_last", "expectations",
                    "Do investors expect the measure to stay in force for at least its stated term?",
                    "Investors expect the measure to stay in force for at least its stated term.")
SLOW_SUPPLY_QUESTION = ("asset_supply_slow", "durability",
                        "Is the supply of the affected firms' productive assets (plants, equipment, the shares that claim their returns) slow to expand or to replace?",
                        "The supply of the affected firms' assets is fixed or slowly expandable.")
RELOCATE_QUESTION = ("can_relocate_capital", "mobility",
                     "Do some downstream users have the option of producing abroad when they next replace their plants?",
                     "Some downstream users can move production abroad when they replace plant.")
SUBSTITUTE_SUPPLY_QUESTION = ("substitute_supply_expands", "substitutability",
                              "Can the sellers of the uncovered substitutes (imported finished goods) supply more at roughly their present prices?",
                              "Sellers of the uncovered substitutes can expand their supply.")
PRICE_TAKER_QUESTION = ("exporters_price_takers", "substitutability",
                        "Do the downstream users who export sell at prices set in world markets, so that they cannot pass a higher input cost on to foreign buyers?",
                        "The exporting users sell at world prices and cannot pass the higher cost on.")


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
    specs.append(BUDGET_QUESTION)
    exempt = [d for d in comp.downstream if d.competitors == "exempt"]
    if comp.definition_line:
        specs.append(RESHAPING_QUESTION)
    if comp.relief_applicant_actor:
        specs += [DISCRETIONARY_QUESTION, VALUABLE_QUESTION]
    if comp.instrument == "tariff":
        if comp.renewable:
            specs.append(BENEFICIARIES_ORGANIZE)
            if exempt:
                specs.append(HARMED_ORGANIZE)
            specs.append(EXTENSION_QUESTION)
        if comp.domestic_seller_owner_actor or any(d.owner_actor for d in exempt):
            specs += [LASTING_QUESTION, SLOW_SUPPLY_QUESTION]
        if exempt:
            specs.append(RELOCATE_QUESTION)
            if any(d.buyer_actor for d in exempt):
                specs.append(SUBSTITUTE_SUPPLY_QUESTION)
        if any(d.exporter_actor for d in comp.downstream):
            specs.append(PRICE_TAKER_QUESTION)
    return specs


def questions_for(comp: Component) -> list[tuple[Question, str]]:
    """Typed questions for a component, each with the text of the assumption it estimates."""
    return [(Question(id=f"{comp.id}.{atom}", kind="noul", text=text, assumption=atom, assumption_class=cls), assumed)
            for atom, cls, text, assumed in _specs(comp)]


def ceiling_questions(comp: Component) -> list[Question]:
    return [q for q, _ in questions_for(comp)] if comp.instrument == "price_ceiling" else []


ASSUMPTION_TEXT = {atom: text for atom, _, _, text in CEILING_QUESTIONS}
