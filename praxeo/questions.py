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

# TX-3 with RS-1, asked of every per-unit tax: buyers' untaxed substitutes.
SUBSTITUTES_QUESTION = ("untaxed_substitutes", "substitutability",
                        "Do buyers of the taxed good have acceptable untaxed substitutes (other goods, or other forms of the same good) that they can turn to?",
                        "Buyers have acceptable untaxed substitutes they can turn to.")
# TX-4 with RS-4, asked of a per-unit tax whose record names buyers who can cross a boundary to an untaxed place.
CROSS_BORDER_QUESTION = ("cross_border_feasible", "mobility",
                         "Can enough of the buyers easily buy the taxed good on the other side of the boundary, in a place without the tax, for crossing to be worth its cost to them?",
                         "Enough buyers can easily buy across the boundary, where the tax does not apply.")
# TX-1 (1.1), asked when the measure raises the rate of an existing tax.
BASE_HOLDS_QUESTION = ("revenue_base_holds", "substitutability",
                       "Will the taxed base fall by less than enough to offset the rise in the rate, so that the revenue rises?",
                       "The taxed base falls by less than enough to offset the rise in the rate.")

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


# RS-8, asked only when the record has an announcement window (Component.announcement_window).
WINDOW_REPRICING_QUESTION = ("window_repricing", "expectations",
                             "Can the bound sellers reprice a meaningful share of their contracts in the announcement window, before the rule takes effect?",
                             "Enough contracts come up for repricing in the announcement window, and sellers can raise the price on them.")
CATCHUP_QUESTION = ("counterfactual_catches_up", "counterfactual_trend",
                    "Without the rule, would prices on renewed contracts follow the market path within a year or two, so that the market price soon passes any raise made in the announcement window?",
                    "Without the rule, the market price soon passes any raise made in the announcement window.")
STOCKPILE_QUESTION = ("stockpile_ahead", "expectations",
                      "Can the buyers or importers buy ahead of the effective date, by storing the good or placing orders early?",
                      "Buyers and importers can store the good and order ahead of the effective date.")


# PC-12, asked only for a price ceiling whose record names the suppliers of the input the capped sellers buy (input_supplier_actor).
INPUT_FEW_OUTLETS_QUESTION = ("input_few_outlets", "alternative_uses",
                              "Do the suppliers of the input have few outlets, in the period considered, other than the capped sellers (so that they cannot send their output elsewhere at an uncapped price)?",
                              "The input's suppliers have few uncapped outlets: they receive less for what they sell to the capped sellers.")
INPUT_OTHER_OUTLETS_QUESTION = ("input_other_outlets", "alternative_uses",
                                "Do the suppliers of the input have other buyers, in the period considered, to whom they can send their output at an uncapped price?",
                                "The input's suppliers have other buyers: they send less to the capped sellers.")


# Subsidies (SB-1 to SB-6). SB-1, OC-3 and the claims cost (CR-8c) need no premise; the rest are asked per subsidy, or only
# when the record carries the fact or role the rule needs.
SUBSIDY_QUESTIONS = [
    ("takeup", "other",
     "Will many of those eligible claim the payment, because it is worth more to them than what they must do or give up to qualify?",
     "Many eligible recipients value the payment above the cost of qualifying, and claim it."),
    ("not_fully_captured", "other",
     "Will the recipients keep part of the payment, rather than sellers raising their prices by the whole of it?",
     "Sellers do not capture the whole payment: the recipients' net price falls."),
    ("quantity_expands", "alternative_uses",
     "Will more of the subsidized good change hands than without the payment (because buyers buy more, or sellers can supply more)?",
     "At least one side can expand its quantity: more of the subsidized good is traded."),
    ("seller_supply_slow", "durability",
     "Is the sellers' supply of the subsidized good fixed for a while (stock ordered or built before the payment, long lead times), so that it cannot grow at once to meet the added demand?",
     "The sellers' supply of the subsidized good cannot grow at once."),
    ("sellers_fewer_alternatives", "substitutability",
     "While their supply is fixed, do the sellers have clearly fewer alternatives than the recipients (who can wait, buy something else or not buy at all)?",
     "While supply is fixed, the sellers have clearly fewer alternatives than the recipients."),
]
SB_SUBSTITUTES_QUESTION = ("substitutes_given_up", "substitutability",
                           "Would some recipients otherwise have bought one of the goods the payment does not cover (a non-eligible model, another form of the good)?",
                           "Some recipients would otherwise have bought an unsubsidized good.")
SB_LASTING_QUESTION = ("expected_to_last", "expectations",
                       "Do buyers of the affected assets expect the payment to stay in place long enough to raise what the assets earn over several years?",
                       "Buyers of the affected assets expect the payment to last for several years.")
SB_SLOW_ASSET_QUESTION = ("asset_supply_slow", "durability",
                          "Is the supply of the asset whose return the payment raises (land, homes, licenses, specific plant) fixed or slow to expand?",
                          "The supply of the asset whose return the payment raises is fixed or slowly expandable.")
QUALIFY_QUESTION = ("qualifying_pays", "other",
                    "For some who do not now meet the criteria, will changing what they do or own so as to meet them cost less than the payment is worth to them?",
                    "Some can meet the criteria at a cost below the payment's worth to them.")
SB_ORGANIZE_QUESTION = ("beneficiaries_organize", "other",
                        "Can the sellers who gain from the payment organize to lobby for its extension or renewal at a cost below their stake (an existing trade association, a few large firms)?",
                        "The sellers who gain can organize to lobby for renewal at a cost below their stake.")
OVERSUBSCRIBED_QUESTION = ("oversubscribed", "other",
                           "Will more people want the payment than its budget or number allows at some point while it is offered?",
                           "Demand for the payment exceeds its budget or number at some point.")
DELAY_QUESTION = ("can_delay", "expectations",
                  "Could those who will be eligible put off a purchase they would otherwise make before the payment starts, until it does (the payment was announced in advance)?",
                  "Eligible buyers knew of the payment before it started and could delay purchases.")
PULL_FORWARD_QUESTION = ("pulled_forward", "expectations",
                         "Would many of those who buy during the payment's window have bought the same good within the following few years anyway?",
                         "Many window buyers would have bought within the next few years anyway.")
STAY_IN_USE_QUESTION = ("would_stay_in_use", "durability",
                        "Would the goods scrapped to obtain the payment otherwise have stayed in use for some years?",
                        "The scrapped goods would otherwise have stayed in use for some years.")
USED_SUPPLY_QUESTION = ("used_supply_slow", "mobility",
                        "Is other supply of used goods of this kind (imports, goods kept in use longer) unable to replace the scrapped ones quickly?",
                        "Other supply cannot quickly replace the scrapped used goods.")
SB_MOVE_QUESTION = ("opportunities_need_move", "mobility",
                    "Would some recipients, without the repayment condition, take a job or a home elsewhere within the period in which moving means repaying the payment?",
                    "Some recipients would otherwise move within the repayment period.")


# SB-6 after expiry: the dip needs the payment to end as scheduled; its price side needs a premise about supply at that date.
ENDS_QUESTION = ("ends_as_scheduled", "expectations",
                 "Will the payment end when its window closes, rather than being renewed, extended or repeated soon after?",
                 "The payment ends as scheduled: it is not renewed, extended or repeated soon after.")
EXPIRY_SUPPLY_QUESTION = ("supply_slow_at_expiry", "durability",
                          "When the payment ends, will the sellers still be unable to cut their supply at once (stock already ordered, capacity built for the window)?",
                          "When the payment ends, the sellers cannot cut their supply at once.")
# SB-2 where the recipients are the sellers (a payment to producers per unit sold): which way the capture runs.
SELLER_KEEPS_QUESTION = ("not_fully_captured", "other",
                         "Will the producers who receive the payment keep part of it, rather than passing all of it on to their buyers in lower prices?",
                         "The producers keep part of the payment: the price they receive, including it, rises.")

# PC-20: a cap on the buyer's share, the rest paid by a third party.
SHARE_CAP_QUESTIONS = [
    ("payer_complies", "enforcement",
     "Will the third party (the insurer or fund) pay the sellers the rest of the price as the rule requires?",
     "The third party pays the sellers the rest of the price as required."),
    ("share_demand_responds", "substitutability",
     "Will buyers whose out-of-pocket share falls buy more of the good (fewer skipped or rationed purchases)?",
     "Buyers whose share falls buy more of the good."),
]


# RS-3 with CR-8b, asked when the text sets penalties for false claims (claim_penalties).
FALSE_CLAIMS_QUESTION = ("false_claims", "enforcement",
                         "Given how claims are checked, will some claims for the payment be false or overstated?",
                         "Some claims are false or overstated.")
RECOVERED_QUESTION = ("claims_recovered", "enforcement",
                      "Will the checks find some false claims, so that repayments or fines are collected?",
                      "Some false claims are found, and repayments or fines are collected.")


def _subsidy_specs(comp: Component) -> list[tuple[str, str, str, str]]:
    claims = [FALSE_CLAIMS_QUESTION, RECOVERED_QUESTION] if comp.claim_penalties else []
    if comp.instrument == "lump_sum_subsidy":   # SB-2 to SB-6 need a payment per unit; SB-4 needs only an asset it attaches to
        return ([SB_SLOW_ASSET_QUESTION, SB_LASTING_QUESTION] if comp.asset_owner_actor else []) + claims
    specs = list(SUBSIDY_QUESTIONS) + claims
    if not comp.seller_actor or comp.seller_actor == comp.bound_actor:   # the recipients sell
        specs = [SELLER_KEEPS_QUESTION if s[0] == "not_fully_captured" else s for s in specs]
    if comp.substitute_seller_actor:
        specs.append(SB_SUBSTITUTES_QUESTION)
    if comp.asset_owner_actor:
        specs += [SB_SLOW_ASSET_QUESTION, SB_LASTING_QUESTION]
    if comp.eligibility_criteria:
        specs.append(QUALIFY_QUESTION)
    if comp.renewable:
        specs.append(SB_ORGANIZE_QUESTION)
    if comp.budget_capped:
        specs.append(OVERSUBSCRIBED_QUESTION)
    if comp.announcement_window:
        specs.append(DELAY_QUESTION)
    if comp.temporary:
        specs += [PULL_FORWARD_QUESTION, ENDS_QUESTION, EXPIRY_SUPPLY_QUESTION]
    if comp.scrappage:
        specs += [STAY_IN_USE_QUESTION, USED_SUPPLY_QUESTION]
    if comp.repay_on_move:
        specs.append(SB_MOVE_QUESTION)
    return specs


# RS-7 Unless (1.0, 1.1), asked when the record says the policy field was contested before the measure (field_contested).
CONTESTED_QUESTION = ("contested_otherwise", "other",
                      "Without the measure, would the question it settles (whether and how much to regulate or support this field) still be fought over by the same groups in the period considered?",
                      "Without the measure, the question it settles would still be contested by the same groups.")


# Licensing (EN-1 to EN-3, EN-5, EN-11) and quotas (EN-6).
LICENSE_QUESTIONS = [
    ("binding", "binding",
     "Do the license's conditions (training, exams, fees, waiting periods) go beyond what some current or would-be sellers already meet?",
     "The requirement goes beyond what some current or would-be sellers already meet."),
    ("enforced", "enforcement",
     "Will the requirement be enforced often enough that many sellers comply with it or stop selling?",
     "The requirement is enforced often enough that many sellers comply or stop."),
    ("some_qualify", "alternative_uses",
     "Will some current sellers or new entrants choose to obtain the license?",
     "Some current sellers or new entrants obtain the license."),
    ("evasion", "enforcement",
     "Will some sellers keep selling without a license and not be caught?",
     "Some sellers keep selling without a license and are not caught."),
    ("buyer_substitutes", "substitutability",
     "Can some buyers turn to a substitute for the licensed service (doing it themselves, family or friends, another service)?",
     "Some buyers have a feasible substitute for the licensed service."),
    ("tests_valued_quality", "other",
     "Does the license test something buyers care about but cannot easily judge for themselves (competence, safety, honesty)?",
     "The license tests something buyers value but cannot easily judge."),
    ("can_organize", "other",
     "Can the license holders (or those who train them) organize to lobby for the requirement at a cost below their stake?",
     "The license holders can organize to lobby at a cost below their stake."),
]
QUOTA_QUESTIONS = [
    ("binding", "binding",
     "Is the cap below the quantity that would otherwise be traded, now or within the period considered (for a cap on the number of sellers: does it hold the quantity down)?",
     "The cap holds the quantity below what would otherwise be traded."),
    ("enforced", "enforcement",
     "Will the cap be enforced, so that little trade takes place beyond it?",
     "The cap is enforced."),
    ("evasion", "enforcement",
     "Will some trade take place beyond the cap without being caught?",
     "Some trade takes place beyond the cap without being caught."),
    ("can_organize", "other",
     "Can the holders of the quota rights organize to lobby for keeping or tightening the cap at a cost below their stake?",
     "The holders of the rights can organize to lobby at a cost below their stake."),
]
EN_LASTING_QUESTION = ("expected_to_last", "expectations",
                       "Do holders and buyers of the licenses or quota rights expect the restriction to last for many years?",
                       "Holders and buyers of the rights expect the restriction to last.")
WIDER_PRICE_QUESTION = ("price_effect_material", "other",
                        "Is the capped quantity a large enough part of the wider market for the cap to raise the price buyers pay there?",
                        "The capped quantity matters enough in the wider market to raise the price there.")


ALLOCATION_KNOWN_QUESTION = ("allocation_known", "expectations",
                             "During the base period, will actors know (or expect) that rights will be allocated by their activity in it?",
                             "Actors know the allocation rule during the base period.")
VALUES_DIFFER_QUESTION = ("values_differ", "other",
                          "Do holders of the rights differ in their costs, or in the value they get from the right?",
                          "Holders' costs or values differ.")
TRADE_CHEAP_QUESTION = ("trade_cheap", "mobility",
                        "Can the rights be sold or leased at low cost (a register, few restrictions on who may hold them)?",
                        "Rights can be sold or leased at low cost.")
TRAINING_COMMON_QUESTION = ("training_common", "other",
                            "Before the requirement, did many people already take the training it requires (a degree many would-be sellers already pursued)?",
                            "The required training was already commonly taken before the requirement.")


def _en_specs(comp: Component) -> list[tuple[str, str, str, str]]:
    specs = list(LICENSE_QUESTIONS if comp.instrument == "licensing_requirement" else QUOTA_QUESTIONS)
    if comp.instrument == "licensing_requirement" and comp.trainer_actor:
        specs.append(TRAINING_COMMON_QUESTION)
    if comp.transferable:
        specs.append(EN_LASTING_QUESTION)
    if comp.instrument == "quota" and comp.transferable:
        specs += [VALUES_DIFFER_QUESTION, TRADE_CHEAP_QUESTION]
    if comp.instrument == "quota" and comp.allocation_by_history and comp.base_period_after_announcement:
        specs.append(ALLOCATION_KNOWN_QUESTION)
    if comp.instrument == "quota" and comp.import_quota:
        # the tariff chains apply (EN-6: as under TX-7): their questions, except the tariff's own binding and funding ones
        have = {s[0] for s in specs}
        tariff = _instrument_specs(comp.model_copy(update={"instrument": "tariff", "general_budget": False, "own_revenue_funded": True}))
        specs += [s for s in tariff if s[0] not in have and s[0] != "binding"]
    if comp.instrument == "quota" and comp.wider_market:
        specs.append(WIDER_PRICE_QUESTION)
    if comp.general_budget:
        specs.append(BUDGET_QUESTION)
    return specs


def _related_specs(comp: Component) -> list[tuple[str, str, str, str]]:
    """One question per premise of each related market (CR-9, SB-3, RS-12), named by the relation's index."""
    out = []
    for i, rel in enumerate(comp.related, start=1):
        good = rel.good.replace("_", " ")
        if rel.kind == "complement":
            out.append((f"related_close_r{i}", "substitutability",
                        f"Is {good} used together with the {comp.good.replace('_', ' ')}, with few other uses, so that its sales follow the good's?",
                        f"{good.capitalize()} is a close complement of the good, with few other uses."))
        out.append((f"related_slow_r{i}", "durability",
                    f"Is the supply of {good} slow to expand or contract in the period considered (training, licensing, capacity)?",
                    f"The supply of {good} is slow to adjust."))
    return out


def _specs(comp: Component) -> list[tuple[str, str, str, str]]:
    specs = _instrument_specs(comp) + _related_specs(comp)
    if comp.field_contested:
        specs.append(CONTESTED_QUESTION)
    return specs


def _instrument_specs(comp: Component) -> list[tuple[str, str, str, str]]:
    """The (atom, class, question, assumption text) list for a component, by instrument."""
    if comp.instrument == "price_ceiling" and comp.third_party_payer_actor:
        return list(SHARE_CAP_QUESTIONS)
    if comp.instrument == "price_ceiling":
        specs = list(CEILING_QUESTIONS)
        if comp.announcement_window:
            specs += [WINDOW_REPRICING_QUESTION, CATCHUP_QUESTION]
        if comp.general_budget:
            specs.append(BUDGET_QUESTION)
        if comp.input_supplier_actor:
            specs += [INPUT_FEW_OUTLETS_QUESTION, INPUT_OTHER_OUTLETS_QUESTION]
        return specs
    if comp.instrument in ("per_unit_subsidy", "purchase_rebate", "lump_sum_subsidy"):
        return _subsidy_specs(comp)
    if comp.instrument in ("licensing_requirement", "quota"):
        return _en_specs(comp)
    if comp.instrument not in ("per_unit_tax", "tariff"):
        return []
    specs = list(TAX_QUESTIONS if comp.instrument == "per_unit_tax" else TARIFF_QUESTIONS)
    if comp.instrument == "per_unit_tax":
        specs.append(SUBSTITUTES_QUESTION)
        if comp.mobile_buyer_actor:
            specs.append(CROSS_BORDER_QUESTION)
    if comp.rate_rise:
        specs.append(BASE_HOLDS_QUESTION)
    if comp.downstream:
        specs.append(INPUT_QUESTION)
        if any(d.competitors == "exempt" for d in comp.downstream):
            specs.append(EXEMPT_QUESTION)
    if not comp.own_revenue_funded:  # OC-3, third funding case: the measure's own revenue pays, no budget is raised on taxpayers
        specs.append(BUDGET_QUESTION)
    if comp.announcement_window:
        specs.append(STOCKPILE_QUESTION)
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


def record_questions(record) -> list[tuple[Component, Question, str]]:
    """Typed questions for every component under every reading whose fields change it (Unclear.reading_fields), once each."""
    from .engine import readings
    seen, out = set(), []
    for _label, _facts, variant in readings(record):
        for comp in variant.components:
            for q, assumed in questions_for(comp):
                if q.id not in seen:
                    seen.add(q.id)
                    out.append((comp, q, assumed))
    return out


def ceiling_questions(comp: Component) -> list[Question]:
    return [q for q, _ in questions_for(comp)] if comp.instrument == "price_ceiling" else []


# Configuration B's questions: the ceiling list and the funding question. The window questions are not implemented there.
ASSUMPTION_TEXT = {atom: text for atom, _, _, text in CEILING_QUESTIONS + [BUDGET_QUESTION]}
