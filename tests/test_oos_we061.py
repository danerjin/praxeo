"""Out-of-sample check of the mandate rules (praxeo/rules/mandates.lp, PC-17 developed on WE-029) on WE-061, app-based drivers
deemed employees with a per-trip buy-out.

Same shape as test_oos_we018.py. The rules were not changed for this example: every engine consequence is a row of the
example's consequence list or sits in EXCEPTIONS with its reason (each classified "defensible" or "KNOWN WRONG"), and every
table row the engine does not produce sits in NOT_PRODUCED with its reason. The run is described in
cases/we061_lanvik/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE61 = ROOT / "cases" / "we061_lanvik"

# the table's "lobbying groups" (C-22) are the platforms (bound) and the workers' side (recipients); the payer group's
# members are named in words
SHORT = {"lobbying groups": ["platforms", "drivers.employee"],
         "recipients of other spending": "recipients.other_spending",
         "future taxpayers": "taxpayers.future"}
EXCEPTIONS = {
    ("platforms", "asset_value", "decrease", None):
        "defensible: CR-7c on the bound actor; the table puts the fall on the platforms' shareholders, owners.platforms (C-27)",
    ("platforms", "return_on_capital", "decrease", None):
        "defensible: CR-7b, the cost stays with the platforms while fare shares hold (A-29); C-27 rests on the same fall in expected yield",
    ("platforms", "resources_available_other_uses", "decrease", None):
        "defensible: CR-8b, the platforms' means fall with the cost they bear. The final check (item 4) signs this variable only for "
        "riders whose trips do not fall (C-38); it does not say the platforms' means do not fall",
    ("sellers.small_platform", "quantity_supplied", "increase", None):
        "defensible: CR-9, exempt rivals gain sales where the cost stays (worth_less); the table has the exempt services' number rise (C-21), not their sales",
    ("sellers.small_platform", "asset_value", "increase", None):
        "defensible: CR-7c on the exempt rivals, with the same premise (valued_on_earnings); not in the table",
    ("sellers.substitutes", "quantity_supplied", "increase", None):
        "defensible: CR-9 for the taxis as unbound rivals; the table records the same gain as quantity_substitute (C-25, RS-1)",
    ("sellers.substitutes", "asset_value", "increase", None):
        "defensible: CR-7c for the unbound rivals; the table puts the gain on the medallion owners (C-26)",
}
NOT_PRODUCED = {
    "C-1": "missing rule: the floor's direct effect on the pay per hour of workers below it (PC-10); K2 is a price_floor, which has no rules, and the engine signs wage_rate the other way",
    "C-2": "unsupported form: K5 is a mandate_with_charge, which has no rules",
    "C-4": "missing record fact: K4 (contributions, a per_unit_tax on wages with a notch) is not recorded; the tax family is not the mandate rules",
    "C-10": "missing rule: RS-23's selection of low-fare workers into employee status (term_prevalence); the rule signs only the providers' choice among applicants",
    "C-12": "unsupported form: K5 has no rules (CR-6 free terms, an add-on undone through the fare share)",
    "C-13": "unsupported form: K5 has no rules (two items of net_price_received, CR-12)",
    "C-14": "unsupported form: K5 has no rules",
    "C-17": "missing rule: RS-3 (legal_breach by platforms and workers) is not in mandates.lp; RS-20's breach chain needs complaint_only, and enforcement here is by audit as well",
    "C-18": "unsupported form: RS-17's size threshold only; no hours kink (the 40-hour line of K3) and K3 is not recorded",
    "C-19": "unsupported form: same, hours split across companies at a line on hours",
    "C-20": "unsupported form: same, a notch in weekly wages (K4)",
    "C-23": "missing record fact: RS-4 needs providers selling against unbound rivals across the boundary; here it is the workers' hours that move (CR-7a), and no such rival is named",
    "C-24": "combiner and missing rule: riders' wait_time, CR-12e's response argument, no rule",
    "C-25": "missing rule: RS-1 (riders leaving the apps take taxi trips, quantity_substitute); the engine's CR-9 rival gain is quantity_supplied",
    "C-26": "role: CR-7c on the rivals signs their own asset_value; the medallion owners have no role field",
    "C-27": "role: CR-7c puts the fall on the bound actor (platforms), the table on owners.platforms; no owner role for bound providers",
    "C-28": "missing rule: RS-12 (delivery as a complement to restaurant meals)",
    "C-29": "missing rule: RS-1 with CR-6 labor demand (in-house couriers) for a restaurant substitute",
    "C-30": "missing record fact: the insurance fund and its benefits (K4's receipts); CR-8b",
    "C-31": "combiner: the fund's contributions against benefits; no K4 and no declared comparison",
    "C-33": "combiner: the engine reports the earnings-down chain alone, as decrease (an engine row classed KNOWN WRONG); the floor chain that would make it ambiguous is not encoded without a paid absence",
    "C-34": "combiner and missing rule: contractors' wait_time (CR-12e, a second chain); K5 has no rules",
    "C-35": "combiner and missing rule: contractors' hourly earnings (CR-12e); K5 has no rules",
    "C-38": "missing rule: OC-1 for riders who keep paying the higher fare (CR-3's note); the mandate rules sign the providers' means only",
    "C-40": "missing rule: paid waiting outside shifts under U1-b; U1 changes no record field, so the readings are not told apart",
    "C-41": "combiner: cover (+) against flexibility (-) as two items of non_wage_compensation (CR-12, 0.8); the rules sign only the cover, and the key's sign is given per reading",
    "C-42": "unsupported form: K5 has no rules (term_prevalence of contractor agreements)",
    "C-43": "missing rule: entry_rate of new contractors (CR-4, ambiguous); no rule signs entry",
    "C-44": "missing rule: RS-1, home production as a substitute for delivery",
    "C-45": "missing rule: CR-6 for the price of a legal right (a taxi medallion's lease price)",
}
PRODUCED = {"C-3", "C-5", "C-6", "C-7", "C-8", "C-9", "C-11", "C-15", "C-16", "C-21", "C-22", "C-36", "C-37"}


def test_consistent_with_worked_example_we061():
    pred, keys = _engine(WE61)
    rows = _rows("WE-061_gig_worker_reclassification.md", SHORT, {}, {})
    assert len(rows) == 43
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert PRODUCED | set(NOT_PRODUCED) == set(rows)
    known_wrong = {k for k, v in EXCEPTIONS.items() if v.startswith("KNOWN WRONG")}
    assert known_wrong == set()  # 2 at the first run: no wage-down chain where a floor holds the recipients (fix after the run)
    assert all(v.startswith(("defensible", "KNOWN WRONG")) for v in EXCEPTIONS.values())
