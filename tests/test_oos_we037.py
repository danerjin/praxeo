"""Out-of-sample run of the prohibition and price-ceiling rules on WE-037 (Selvar Fair Ticket Act).

WE-037 was not used to write the rules. The record has a price ceiling (the resale cap, K1) and a prohibition (the bot ban,
K2). Every engine consequence is a row of the example's table or sits in EXCEPTIONS with its reason; every table row the
engine does not produce sits in NOT_PRODUCED with its reason. The write-up is cases/we037_selvar/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE37 = ROOT / "cases" / "we037_selvar"

# the table's names for record roles; "resale market" is the market the engine's excess demand sits on (the excluded buyers)
SHORT = {
    "brokers": "resellers.brokers",
    "resale market": "buyers.outsiders",
}
WINDOWS = {"Feb–Aug 2027": "announcement"}

EXCEPTIONS = {
    ("buyers.insiders", "price_paid", "decrease", "first_months"): "same sign as C-1: the combiner forms the first-months total from the cap chain when no repricing in the window is reported",
    ("buyers.insiders", "quality_adjusted_price", "decrease", None): "price against quality with quality_adjustable unreported: the price fall alone (PC-4); the table lists price_paid only",
    ("buyers.insiders", "resources_available_other_uses", "increase", None): "CR-8b, what the buyers keep (mirror of C-1); the table does not list it",
    ("buyers.outsiders", "allocation_by_non_price_criteria", "at_least_one_increase", None): "member of the PC-2 group; the table writes this member as 'allocation_by_non_price_criteria; under U1-b also price_paid' (C-5)",
    ("buyers.outsiders", "allocation_by_non_price_criteria", "increase", None): "member of the PC-2 group, implied by C-5 (selection_open)",
    ("buyers.outsiders", "search_cost", "increase", None): "member of the PC-2 group, implied by C-5",
    ("buyers.outsiders", "informal_activity", "increase", None): "RS-3 for the informal trade (C-9), put on the excluded buyers because the price-ceiling record has no informal-seller role; the table names the sellers",
    ("buyers.outsiders", "price_substitute", "increase", None): "RS-4 with PC-3: shut-out buyers raise the price of the substitutes (primary demand-priced seats, C-28); the table names the sellers of those seats, and the engine has no role for them",
    ("buyers.outsiders", "quantity_demanded", "increase", None): "PC-3: at the cap buyers want more than is supplied (the other side of C-4 and C-6); the table lists the traded quantity only",
    ("resellers.brokers", "resources_available_other_uses", "decrease", None): "CR-8b, the sellers' side of C-1 and C-2",
    ("resellers.brokers", "resources_available_other_uses", "increase", None): "CR-8b: the premiums brokers take above the cap where they evade (C-9, C-10)",
    ("neighboring_jurisdictions", "price_paid", "increase", None):
        "KNOWN WRONG: C-39 is ambiguous (A-20: brokers shift buying to Brackmere City, an opposing chain with A-19); the engine has the shut-out fans' chain alone",
    ("resellers.brokers", "disputes_settled_outside_courts", "increase", None):
        "KNOWN WRONG: EN-7 and RS-10 for the bot ban presuppose that legal trade stops (enforced) and moves underground; K2 only backs a term already in R1 (A-13, 0.45, below the cut-off) and the rule does not require enforced",
    ("resellers.brokers", "quality_information", "decrease", None): "KNOWN WRONG: same, the bot users' black market (K2)",
    ("resellers.brokers", "quality_variability", "increase", None): "KNOWN WRONG: same",
    ("resellers.brokers", "search_cost", "increase", None): "KNOWN WRONG: same",
    ("resellers.brokers", "quantity_substitute", "increase", None): "KNOWN WRONG: RS-1 for the bot ban turns the bot users to substitutes although the ban is not enforced enough to change what they buy (A-13); the example has no such row",
}

NOT_PRODUCED = {
    "C-7": "PC-12 needs an input supplier (the primary sellers) and the capped sellers as its main buyers; the record has no such role and the text does not say brokers are the main buyers",
    "C-8": "no rule for the exit of capped sellers (RS-6) under a ceiling",
    "C-9": "RS-3 puts the informal trade on the excluded buyers (see EXCEPTIONS); there is no informal-seller role for a price ceiling",
    "C-12": "RS-4 for the reach of enforcement (offshore platforms outside the jurisdiction) is not encoded: the engine's RS-4 is the neighbouring market's price",
    "C-13": "no role for platforms and no jurisdiction-reach question on a price ceiling",
    "C-14": "same, offshore platforms",
    "C-15": "the K2 chain on bot vendors needs enforced (A-13, 0.45, unreported); the K1 chain through brokers' fall in demand for primary tickets is not encoded (CR-12d across components)",
    "C-16": "no rule or variable for purchases in breach of a private term (LW-10)",
    "C-17": "platform fees: the unclear provision U1 changes no record field and the record has no platform role or fee fact; the engine gives no sign per reading",
    "C-18": "same, seller fee",
    "C-19": "same: the engine signs insiders' price_paid without readings, so the key 'U1-a: decrease; U1-b: ambiguous' is not matched",
    "C-21": "RS-8 is encoded for repricing only, not for sellers moving sales into the window; the question A-8 would answer does not match",
    "C-22": "same, buyers waiting",
    "C-23": "same: the window price falls because supply is pulled forward; the engine's window row is the repricing rise (unreported at 0.2)",
    "C-24": "same, no combiner for the window quantity",
    "C-26": "no role for primary-sale buyers; the unregulated primary segment next to a capped one (PC-8, CR-9) is not encoded",
    "C-27": "same",
    "C-28": "no role for demand-pricing primary sellers (PC-8)",
    "C-29": "same",
    "C-30": "no combiner for the offshore and informal price (RS-16, RS-13, CR-12b)",
    "C-31": "same, all channels",
    "C-32": "RS-10 for a price ceiling is encoded for disputes only, not quality information",
    "C-34": "same, quality variability",
    "C-35": "no season-ticket-holder role; seat rights are an asset of a related market (CR-7c)",
    "C-36": "no waiting-list role (CR-4, CR-9 across a related market)",
    "C-37": "CR-7c for the resellers' business value needs durable_assets (asked of the covered assets, answered 0.15); A-18 is a different statement",
    "C-38": "RS-1 and RS-4 sign the neighbours' price only, not the Selvar residents' crossing",
    "C-39": "produced with the wrong sign: see EXCEPTIONS (KNOWN WRONG)",
    "C-41": "OC-3 fixed-budget case (no new appropriation) is not encoded: the record's general_budget is false and no row gives the displaced work",
    "C-42": "OC-2 compliance cost for platforms: no platform role; the engine's compliance cost is the exit-process form (unreported)",
    "C-44": "brokers shifting purchases to the neighbouring market: no rule for resellers following the cap (RS-4, CR-7a)",
    "C-45": "no travel_time rule for fans going to the neighbouring market",
    "C-46": "the charity-auction exemption has no record field; CR-1 operation 4 is not encoded for exemptions",
    "C-48": "no role for the football club; the net of two chains (CR-12e) is not encoded",
    "C-49": "no platform role; CR-7c and CR-10c for platform owners",
}
PRODUCED = {"C-1", "C-2", "C-3", "C-4", "C-5", "C-6", "C-10", "C-11", "C-25", "C-33", "C-40", "C-47"}


def test_out_of_sample_we037():
    pred, keys = _engine(WE37)
    rows = _rows("WE-037_ticket_resale_cap.md", SHORT, WINDOWS, {})
    assert len(rows) == 47
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert len(keys) == 31
