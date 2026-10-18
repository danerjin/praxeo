"""Subsidies (praxeo/rules/subsidies.lp): consistency with the development example WE-019, and the rules one by one.

Same shape as tests/test_out_of_sample.py: every reported engine consequence is a row of the example's consequence list
(key: actor class, variable, sign, window; a group gives one key per member), or sits in a dict of exceptions with its
reason; every table row the engine does not produce sits in a dict with the reason. WE-019 was used to write the rules,
so this is a development check, not evidence that the rules generalize.
"""
from pathlib import Path

from praxeo import engine, parser
from praxeo.questions import questions_for
from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE19 = ROOT / "cases" / "we019_vestria"

WE019_SHORT = {"owners of failing old cars": "buyers.new_cars.scrapping", "dismantlers (used-parts sales)": "dismantlers"}
# C-22 is the cumulative total over the surge and the dips (DM-5); its key would otherwise equal C-2's, so it gets a window
# of its own that no engine consequence has
WE019_WINDOWS = {"March to June": "announcement", "after the window": "after_expiry", "year after the window": "after_expiry",
                 "cumulative": "cumulative"}
WE019_EXCEPTIONS = {
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-1, who pays (catalog 1.4): no tax is named, so the payers are a group over taxpayers, recipients of other spending and future taxpayers (at_least_one_decrease); WE-019, written before the clause, signs taxpayers alone (C-20)",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None): "member of the OC-1 group (see above)",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None): "member of the OC-1 group (see above)",
    ("buyers.new_cars.scrapping", "quantity_traded", "increase", None):
        "SB-2: the buyers' side of C-2 (an exchange has two sides); the table signs the sellers' side only",
    ("buyers.new_cars.other", "quantity_traded", "decrease", None):
        "CR-4c after C-9: buyers without the rebate who face a higher price take fewer of the eligible models; not in the table",
}
WE019_NOT_PRODUCED = {
    "C-15": "RS-1 for repairs of the used-car buyers' own cars: no rule for a substitute reached through the used-goods price",
    "C-16": "RS-12 (complements in use) is not encoded; the ambiguous total needs it",
    "C-17": "same (RS-12 through repairs)",
    "C-18": "same (RS-12 against LW-3 for fuel)",
    "C-22": "DM-5 (the cumulative total over the surge and the dips) is not a declared comparison in the combiner",
    "C-20": "sign form: the engine signs the OC-1 payer group (see WE019_EXCEPTIONS); the table signs taxpayers alone, a plain decrease",
    "C-26": "CR-10b for used parts that crushed cars would later have yielded: no rule",
}
WE019_PRODUCED = {"C-1", "C-2", "C-3", "C-4", "C-5", "C-6", "C-7", "C-8", "C-9", "C-10", "C-11", "C-12", "C-13", "C-14",
                  "C-19", "C-21", "C-23", "C-24", "C-25"}


def _record():
    return parser.parse_fixture(WE19 / "record.json")


def test_consistent_with_worked_example_we019():
    pred, keys = _engine(WE19)
    rows = _rows("WE-019_car_scrappage_subsidy.md", WE019_SHORT, WE019_WINDOWS, {})
    assert len(rows) == 26
    _check(rows, keys, WE019_EXCEPTIONS, WE019_NOT_PRODUCED, WE019_PRODUCED)
    by = {(c["actor_class"], c["variable"], c["window"], c["item"]): c for c in pred["consequences"]}
    # SB-3's unsubsidized goods are another item than the subsidized good: no ambiguous merge with SB-2's increase (C-2, C-12)
    assert by[("sellers.new_cars", "quantity_traded", None, None)]["sign"] == "increase"
    assert by[("sellers.new_cars", "quantity_traded", None, "unsubsidized_goods")]["sign"] == "decrease"
    # SB-1 with borrowing: Tier A, from the medium horizon (C-20); OC-3 and the claims cost are Tier A (C-19, C-24)
    payers = by[("taxpayers", "resources_available_other_uses", None, None)]
    assert payers["actor_group"] == ["taxpayers", "recipients.other_spending", "taxpayers.future"]
    assert payers["sign"] == "at_least_one_decrease" and payers["horizon"] == ["medium", "long"]
    assert {by[k]["tier"] for k in [("taxpayers", "resources_available_other_uses", None, None),
                                    ("officials.enforcement", "enforcement_cost", None, None),
                                    ("sellers.new_cars", "compliance_cost", None, None)]} == {"A"}
    # the timing windows: the delay before the start (C-5) and the dip after expiry (C-6, C-25)
    assert by[("buyers.new_cars.scrapping", "quantity_traded", "announcement", None)]["horizon"] == ["short"]
    assert by[("sellers.new_cars", "net_price_received", "after_expiry", None)]["sign"] == "decrease"


def _reported(rec, **p):
    a = {}
    for comp in rec.components:
        for q, text in questions_for(comp):
            atom = f"{q.assumption}({engine._atom(comp.id)})"
            a[atom] = engine.Assumption(id=atom, text=text, assumption_class=q.assumption_class, p=p.get(q.assumption, 0.9))
    return {(c.actor_class, c.variable, c.sign, c.window) for c in engine.run(rec, a)[0] if c.reported}


def test_no_quantity_rules_for_a_lump_sum_subsidy():
    """SB-2 needs a payment per unit; a lump sum cannot be increased by buying more. SB-1, OC-3 and the claims cost remain."""
    rec = _record()
    rec.components[0].instrument = "lump_sum_subsidy"
    got = _reported(rec)
    assert got == {("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None),
                   ("officials.enforcement", "enforcement_cost", "increase", None),
                   ("sellers.new_cars", "compliance_cost", "increase", None)}


def test_flags_gate_their_rules():
    rec = _record()
    comp = rec.components[0]
    comp.temporary = comp.scrappage = comp.budget_capped = comp.announcement_window = comp.renewable = False
    comp.debt_funded = False
    got = _reported(rec)
    assert not any(k[3] for k in got)                                                     # no windows
    assert not any(k[0] in ("dismantlers", "buyers.used_cars", "owners.old_cars.keeping") for k in got)
    assert ("buyers.new_cars.scrapping", "wait_time", "at_least_one_increase", None) not in got
    assert ("sellers.new_cars", "lobbying_effort", "increase", None) not in got
    assert ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None) in got     # OC-1: the payer group
    comp.tax_named = True                                                                  # OC-1: the named tax's payers
    assert ("taxpayers", "resources_available_other_uses", "decrease", None) in _reported(rec)
    comp.own_revenue_funded = True                                                         # SB-1: no general taxpayers
    assert not any(k[0] == "taxpayers" for k in _reported(rec))


def test_premises_below_the_cut_off_stop_their_chains():
    rec = _record()
    got = _reported(rec, not_fully_captured=0.3, seller_supply_slow=0.3)
    assert ("buyers.new_cars.scrapping", "price_paid", "decrease", None) not in got        # A-1
    assert not any(k[1] in ("net_price_received", "subsidy_share_received") and k[3] is None for k in got)  # A-7: C-8, C-23
    # the price after expiry rests on its own premise about supply at that date (C-25)
    assert ("sellers.new_cars", "net_price_received", "decrease", "after_expiry") in got
    got = _reported(rec, supply_slow_at_expiry=0.3)
    assert ("sellers.new_cars", "net_price_received", "decrease", "after_expiry") not in got
    assert ("sellers.new_cars", "quantity_traded", "decrease", "after_expiry") in got        # the dip itself stays (C-6)
    got = _reported(rec, ends_as_scheduled=0.4)                                             # a renewal moves purchases on
    assert not any(k[3] == "after_expiry" for k in got)
    got = _reported(rec, not_fully_captured=0.3, seller_supply_slow=0.3)
    assert ("buyers.new_cars.other", "price_paid", "increase", None) not in got            # C-9
    got = _reported(rec, takeup=0.3)                                                       # A-2: nothing is claimed
    assert {k[0] for k in got} == {"taxpayers", "officials.enforcement", "sellers.new_cars"}


def test_a_payment_to_producers_signs_the_sellers_side():
    """SB-2 for recipients who sell (found out of sample on WE-065): their price received and supply rise; nothing about
    buying (no price_paid, no delay before the start, no dip after expiry), and they are the sellers who lobby (RS-7)."""
    rec = _record()
    comp = rec.components[0]
    comp.bound_actor, comp.seller_actor = "growers", None
    comp.other_buyer_actor = comp.substitute_seller_actor = comp.claim_handler_actor = None
    comp.scrappage = False
    got = _reported(rec)
    assert {("growers", "net_price_received", "increase", None), ("growers", "quantity_supplied", "increase", None),
            ("growers", "lobbying_effort", "increase", None)} <= got
    assert not any(k[0] == "growers" and k[1] in ("price_paid", "quantity_traded") for k in got)
    assert not any(k[3] for k in got)


def test_a_cap_on_the_buyers_share_is_not_a_price_ceiling():
    """PC-20 (found out of sample on WE-056): with a third party paying the rest, no shortage and no ceiling rows."""
    from test_slice import _record as sf_record
    rec = sf_record()
    rec.unclear = []
    rec.components[0].third_party_payer_actor = "insurers"
    got = _reported(rec)
    assert got == {("tenants.controlled", "price_paid", "decrease", None), ("insurers", "subsidy_outlay", "increase", None),
                   ("tenants.controlled", "quantity_traded", "increase", None),
                   ("tenants.controlled", "resources_available_other_uses", "increase", None)}
