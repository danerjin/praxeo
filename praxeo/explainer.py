"""Templated explainer: derivation tree -> plain sentences. No free text generation."""
from __future__ import annotations

from .schema import Assumption, Consequence, PolicyRecord

RULE_TEXT = {
    "PC-1": "a ceiling held below the price the market would reach binds sellers; where new contracts are priced freely, fewer vacancies raise their initial price instead of leaving a shortage",
    "PC-3": "those who hold a covered unit pay the controlled price, while those shut out look elsewhere",
    "RS-4": "shut-out buyers turn to uncovered units, which are close substitutes",
    "PC-5": "owners move resources to uses whose yield the ceiling does not cap",
    "RS-5": "owners move units out of the rule's reach",
    "PC-7": "the benefit is tied to staying put and cannot be sold, so holders move less",
    "PC-21": "leaving the area forfeits the benefit, and fewer holders are priced out, so they leave the area less",
    "TX-1": "a tax that is collected takes resources from those who bear it and yields revenue",
    "TX-2": "a tax on each unit opens a wedge between what buyers pay and what sellers keep, and the market shrinks",
    "TX-3": "buyers of a taxed good turn to the untaxed alternatives they have",
    "TX-4": "where an untaxed place is within reach, buyers who can cross the boundary buy there and the sellers across it gain their custom",
    "TX-5": "whoever must record, file or collect a tax bears the cost of doing so",
    "RS-1": "when a good becomes dearer, buyers turn to substitutes",
    "TX-7": "a tariff the foreign sellers do not absorb raises what domestic buyers pay and lets protected domestic producers charge and sell more",
    "TX-8": "foreigners who sell less to the country earn less of its currency and so buy fewer of its exports",
    "RS-8": "a measure announced before it takes effect treats the same action differently by date, so actors move it toward the favourable window",
    "CR-8": "every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses",
    "CR-9": "an owner who leaves the rental market ends the leases of those who live in the building",
    "OC-3": "the measure must be administered, and a raised budget is paid for by taxpayers",
    "RS-6": "sellers whose return falls sell less, and may cut staff or hours",
    "SB-1": "a subsidy is paid by someone: taxes now, or borrowing repaid from taxes later",
    "OC-1": "what the payers give up is what they would otherwise have bought",
    "SB-2": "a payment per unit is a wedge in the other direction: buyers pay less net of it, sellers may receive more, and more is traded",
    "DM-1": "where sellers' supply cannot grow at once, the added demand raises their price, and the side with fewer alternatives receives more of the payment",
    "CR-4": "buyers who face a higher price take fewer units",
    "SB-3": "resources move into the subsidized activity from the uses that would otherwise have had them",
    "SB-4": "a lasting change in the return on an asset in slow supply is capitalized in its value",
    "SB-5": "a payment conditional on criteria draws effort to meet them",
    "RS-7": "a gain concentrated on an identifiable group draws its lobbying to keep or extend it",
    "LW-6": "a good handed out at a fixed price in a fixed number is rationed by other means when more want it",
    "PC-2": "rationing by other means than price shows up as waiting or allocation by connections",
    "SB-6": "a temporary purchase subsidy moves purchases into its window, and a scrappage condition takes used goods out of the stock",
    "CR-6": "sellers facing fewer buyers than they planned for cut their price",
    "OC-4": "exchanges that no longer happen are lost to both sides",
    "RS-11": "a benefit lost on moving ties the holder to staying put",
    "RS-14": "a dearer input is passed down to the output: its price rises where competitors face the same cost, and its sellers sell less where competitors are exempt",
}

SIGN_WORD = {"increase": "rises", "decrease": "falls", "ambiguous": "may move either way", "no_change": "does not change",
             "at_least_one_increase": "rises for at least one of them", "at_least_one_decrease": "falls for at least one of them"}
WINDOW_WORD = {"announcement": "in the announcement window (before the effective date)",
               "first_months": "in the first months after the effective date",
               "after_expiry": "after the temporary measure expires"}


def explain(c: Consequence, assumptions: dict[str, Assumption], record: PolicyRecord) -> str:
    rules = []
    for step in c.derivation:
        if step.rule not in rules:
            rules.append(step.rule)
    chain = "; ".join(f"{r}: {RULE_TEXT.get(r, r)}" for r in rules)
    when = f"from the {c.horizon[0]} run onward" if len(c.horizon) > 1 else f"in the {c.horizon[0]} run"
    if c.window:
        when = WINDOW_WORD[c.window] + ", " + when
    conds = "; ".join(f"{assumptions[a].text.rstrip('.')} (p = {assumptions[a].p:.2f})" for a in c.assumptions) or "no assumption"
    alt = ""
    if len(c.assumption_sets) > 1:
        alt = f" It also follows under {len(c.assumption_sets) - 1} other minimal assumption set(s)."
    status = "Reported." if c.reported else "Not reported: an assumption is below the 0.5 cut-off."
    if c.sign_by_reading:
        status = "Sign per reading: " + "; ".join(f"{k}: {v}" for k, v in c.sign_by_reading.items()) + ". " + status
    if c.combines:
        chain = f"CR-12 total of {', '.join(c.combines)}" + (" (no premise decides which chain is larger)" if c.sign == "ambiguous" else " (a dominance premise decides the sign)" if len(c.combines) > 1 else " (only one subclass's chain is reported)")
    return (
        f"{c.id}. Compared with no {record.name}, {' or '.join(v.replace('_', ' ') for v in c.members())}"
        f"{' (' + c.item.replace('_', ' ') + ')' if c.item else ''} for {' or '.join(c.actors())} "
        f"{SIGN_WORD[c.sign]} {when} (tier {c.tier}, {c.visibility}). "
        f"Why: {chain}. This holds if: {conds}.{alt} {status}"
    )
