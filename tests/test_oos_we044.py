"""Out-of-sample run of the prohibition rules (praxeo/rules/prohibition.lp) on WE-044, a ban on short-term rentals of whole homes.

The prohibition rules were written from WE-017 only. Same shape as test_consistent_with_worked_example_we017 in
tests/test_prohibition.py: every reported engine consequence is a row of the example's consequence list (key: actor class,
variable, sign, window) or sits in EXCEPTIONS with its reason (prefixed "KNOWN WRONG:" when it contradicts the example);
every table row the engine does not produce sits in NOT_PRODUCED with the reason. The record and answers are in
cases/we044_saltmere/, the write-up in cases/we044_saltmere/out_of_sample.md. Nothing under praxeo/ was changed for this run.

The record has three components: k1 `prohibition` (the ban with its exceptions, K1 and K4's enforcement), k2
`disclosure_mandate` (the platform duty, K2: no rules for it) and k3 `licensing_requirement` (the registry, K3: the licensing
rules fire on it). U1 is recorded without reading_fields: neither reading changes a Component field.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE44 = ROOT / "cases" / "we044_saltmere"

# the table's primary-residence hosts (over and under 90 nights) are the record's k3 bound role; "hosts" in C-15 are the
# record's two host roles; the table's recipients of other general-fund spending are the engine's payer group member
SHORT = {
    "hosts.primary_over90": "hosts.primary",
    "hosts.primary_under90": "hosts.primary",
    "hosts": ["hosts.non_primary", "hosts.primary"],
    "recipients of other general-fund spending": "recipients.other_spending",
}
WINDOWS = {"window bookings": "announcement", "stays before 1 July 2027": "announcement"}
EXCEPTIONS = {
    ("guests.off_platform", "quality_variability", "increase", None):
        "RS-10 with the underground trade: the third member of the triple (C-11, C-12, C-13 list the other three)",
    ("guests.whole_unit", "disputes_settled_outside_courts", "increase", None):
        "RS-3 and RS-10 on K3's unregistered lets (the k3 buyers): the table puts the underground trade on guests.off_platform (C-13)",
    ("guests.whole_unit", "quality_information", "decrease", None):
        "same chain as the row above (K3's unregistered lets); the table has it for guests.off_platform (C-12)",
    ("guests.whole_unit", "price_paid", "increase", None):
        "KNOWN WRONG: EN-7 and CR-7, a risk premium paid by the legal buyers; A-27 and C-14 say hosts in breach screen guests and do not price the risk guest by guest, and the lawful on-platform guests face no such premium",
    ("guests.whole_unit", "quantity_demanded", "decrease", None):
        "sign agrees with C-30 (trips fall, A-11), reached through the risk-price chain of the row above, not through A-11",
    ("guests.whole_unit", "quantity_demanded", "increase", "announcement"):
        "KNOWN WRONG: RS-8 gives the (+) chain of C-18 and C-19 alone; the table signs both ambiguous because owners end lets or time conversions before July (A-16), a second timing chain RS-8 (0.9) combines under CR-12b",
    ("guests.whole_unit", "quantity_substitute", "increase", None):
        "RS-1: guests turn to hotels, rooms and Elsdon (A-8); the table signs the sellers' side (C-23, C-57) and not the guests' own substitute quantity",
    ("guests.whole_unit", "resources_available_other_uses", "decrease", None):
        "EN-1 with CR-8b on K3's fee and proof (the k3 buyers); the table signs the hosts' cost (C-17); the guests' loss from prevented stays is C-2",
    ("guests.whole_unit", "search_cost", "increase", None):
        "OC-2 for the guests who go to Elsdon (RS-4) and from K3's chain; the table has the crossing as travel_time (C-62) and rebooking cost for prebooked guests (C-21)",
    ("hosts.in_breach", "disputes_settled_outside_courts", "increase", None):
        "RS-10, the sellers' side of C-13",
    ("hosts.in_breach", "reclassification", "increase", None):
        "RS-5 on the informal sellers; C-59 has the reclassification on hosts.non_primary, the unsplit class",
    ("hosts.primary", "employment", "decrease", None):
        "KNOWN WRONG: EN-3 on K3 as a licence that excludes entrants from an occupation; K3 is a registration fee and proof of residence on an exempt use (CR-4 fixed cost per outlet, C-17), nobody is excluded from a trade and there is no employment effect",
    ("hosts.primary", "entry_rate", "decrease", None):
        "EN-1 on K3: C-17 says the fixed fee bears on whether a primary-residence host lists at all (some who let a few nights stop); the table does not sign entry for this class",
    ("hosts.primary", "informal_activity", "increase", None):
        "RS-3 on K3: lets without a valid number; C-9 records the same breach as legal_breach",
    ("hosts.primary", "net_price_received", "increase", None):
        "EN-2 licence rents; C-39 signs the lawful hosts' net price up for another reason (less competition, RS-16, A-32, A-35) under hosts.lawful, which the record has no role for",
    ("hosts.primary", "number_of_sellers", "decrease", None):
        "EN-1 on K3: the hosts who stop listing (C-17); the head count is not in the table",
    ("hosts.primary", "quantity_traded", "decrease", None):
        "EN-1 and OC-4 on K3, the nights prevented above the cap; the table has C-3 as quantity_supplied for hosts.primary_over90",
    ("hosts.primary", "share_of_sellers_licensed", "increase", None):
        "EN-1: the registered share rises by definition of the requirement; not in the table",
    ("neighboring_jurisdictions", "quantity_traded", "increase", None):
        "RS-4: the sellers across the boundary gain the guests (C-26); the table signs Elsdon hosts' quantity_supplied (C-27)",
    ("officials.revenue", "tax_revenue", "decrease", None):
        "KNOWN WRONG: TX-10 alone; C-49 is ambiguous because the TOT lost on whole-unit STRs is partly regained from hotels (A-8, A-9) and Elsdon is outside the city (A-10), against A-11",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-1 payer group: the engine's default group has future taxpayers as a third member; C-46 names taxpayers and the recipients of other spending",
}
NOT_PRODUCED = {
    "C-1": "variable: EN-7 signs the lawful hosts' quantity_traded and number_of_sellers, not quantity_supplied (nights offered)",
    "C-3": "missing record fact and variable: the 90-night cap (CR-1 operation 1 above a threshold, operation 3 below) has no field; the k3 key gives quantity_traded for hosts.primary, not the class over 90 nights",
    "C-4": "missing role: two-unit hosts (hosts.duplex); U1 changes a role's coverage, not a Component field, so reading_fields cannot carry it",
    "C-5": "missing role: hosts.duplex (see C-4)",
    "C-6": "missing rule and question: RS-6 and CR-4 (the next-best use, a 12-month lease, A-5) for a prohibition; no role for the converting hosts",
    "C-7": "missing rule and role: the owner's own-use element (units_held_vacant, A-6); no rule for a ban on a use of one's own property",
    "C-9": "missing variable: no rule signs legal_breach; breach of a cap on a lawful use (nights above 90, another unit's number) is not a prohibition form the rules know",
    "C-14": "missing rule and question: RS-20 (complaint-only enforcement) and A-27 (screening by hosts in breach)",
    "C-18": "missing rule: RS-8 (0.9) opposing timing chain (the leasing season, A-16) and the CR-12b combiner; the engine reports the (+) chain alone (see the KNOWN WRONG exception)",
    "C-19": "missing rule: same as C-18, with A-17 for the guests who move trips before July",
    "C-21": "missing role and record fact: guests with bookings cancelled and refunded under the transition clause",
    "C-22": "missing rule, role and question: RS-16 / CR-9 for the substitute market (hotel guests' price, A-9 durability); RS-1 signs only the buyers' quantity_substitute",
    "C-23": "missing role: substitute_seller_actor is the RS-5 line role (hosts.mid_term here), so hotels, the RS-1 substitute sellers, have no field; no rule signs their quantity",
    "C-24": "missing rule and role: CR-7c asset value of the substitute sellers (hotels) with A-9 and A-30",
    "C-25": "missing rule and role: CR-7a long-run investment of the substitute sellers",
    "C-27": "variable and question: RS-4 signs the neighbor sellers' quantity_traded (the engine row), the table quantity_supplied with the durability premise A-39",
    "C-28": "missing rule: CR-7c asset value of the neighbor sellers' homes",
    "C-29": "missing role and rule: RS-13 (spillover from the neighbor's STR to its long-term market, A-29); one neighbor role per component",
    "C-31": "missing rule: CR-9 and RS-9 for related markets (complements) under a prohibition: relations.lp takes target_qty from taxes and subsidies only; section 1 names no complement, so the record has no related entry",
    "C-32": "missing rule: CR-9 for inputs (cleaners, managers) under a prohibition (target_qty); section 1 names the cleaning and management cost but no supplier group",
    "C-33": "missing rule and role: OC-5 for the staff of the substitute sellers (hotels)",
    "C-34": "missing rule and role: RS-13 spillover to the long-term rental market (tenants.prospective); the conversion route is C-6",
    "C-35": "missing rule and role: same",
    "C-36": "missing rule and role: same, landlords.long_term",
    "C-37": "missing rule and role: CR-7c asset value of rental buildings",
    "C-38": "missing rule and role: RS-16 with its Unless clause and RS-13 for the mid-term market (guests.extended); two opposing chains (A-7, A-31)",
    "C-39": "missing role and rule: hosts.lawful and RS-16 (rooms and within-cap lets lose competition, A-32, A-35)",
    "C-40": "missing rule: CR-7c / SB-4 asset value fall of non-primary units is tied to no_other_use (answer no, 0.15, from A-5); the table has it with alternatives that yield less (A-1, A-30)",
    "C-41": "missing role: hosts.duplex (owners)",
    "C-42": "missing rule and role: CR-7c with CR-8b for would-be home buyers (buyers.prospective)",
    "C-43": "missing rule: proximity chain (CR-9, Tier C), CR-12d; no role homeowners.str_districts",
    "C-44": "missing rule: CR-3a and CR-7b return on capital after a ban removes the best use; the rule needs no alternative use at all",
    "C-47": "missing role and rule: a second enforcer (Code Enforcement; K1 and K3 share one enforcer_actor) and OC-3 for complaint-driven work with fixed budget (CR-12b combiner, A-18, A-19)",
    "C-48": "missing role and rule: neighbors as complainants (OC-2, CR-8c)",
    "C-49": "missing combiner: TX-10 signs the lost tax alone (KNOWN WRONG exception); the table nets it against hotel and Elsdon effects (CR-12b); actor classes differ too",
    "C-50": "missing rule: CR-8b fines paid by hosts found in breach go to the general fund (non_tax_receipts); prohibition.lp signs no penalty receipts",
    "C-51": "missing rule and role: CR-8b / CR-3c on the hosts fined (hosts.fined); convicted_actor feeds EN-10 (employment) only",
    "C-52": "missing rule: CR-9, RS-9 and the CR-12b combiner for complements near converted units",
    "C-53": "missing rule: proximity chain, Tier C (see C-43)",
    "C-54": "missing rule and role: CR-1 / CR-7c asset value of beach-district homeowners",
    "C-55": "missing rule: CR-8b / CR-12e fees collected under K3 against the old registration (non_tax_receipts)",
    "C-56": "missing rule: CR-8b fines and fees combined (CR-12b)",
    "C-57": "missing role and rule: RS-16 spillover to rooms in occupied homes (hosts.rooms), A-32, A-36",
    "C-58": "missing role and rule: RS-16 / CR-7a entry of owner-occupiers into room lets",
    "C-59": "role split: RS-5 reshaping is signed on hosts.mid_term and hosts.in_breach (the engine rows), the table puts it on hosts.non_primary; no question for the claim of primary residence on changeable documents",
    "C-60": "missing role and rule: CR-4 (a sale as the next-best use, A-37) and its price in section 6; hosts.selling",
    "C-61": "missing role and rule: investors.home_buyers' quantity_demanded (CR-7c, A-21)",
    "C-62": "variable: RS-4 signs search_cost for the crossing buyers (the engine row); the table's travel_time has no rule",
    "C-63": "missing rule and role: RS-16 with A-9 for hotel guests' own quantity (CR-4c)",
    "C-64": "missing rule and role: RS-16 / RS-13 for the furnished-let market (guests.extended); the sellers' RS-5 row is C-8",
}
PRODUCED = {f"C-{i}" for i in range(1, 65)} - set(NOT_PRODUCED)


def test_consistent_with_worked_example_we044():
    pred, keys = _engine(WE44)
    rows = _rows("WE-044_short_term_rental_ban.md", SHORT, WINDOWS, {})
    assert len(rows) == 64
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
