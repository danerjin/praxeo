"""Out-of-sample run of the quota rules (praxeo/rules/licensing.lp, EN-6) on WE-015, a cap on transferable taxi licenses.

The quota rules were written from EN-6's text alone (licensing was developed on WE-003). Same shape as
tests/test_licensing.py::test_consistent_with_worked_example_we003: every reported engine consequence is a row of the
example's consequence list or sits in EXCEPTIONS with its reason (a reason that starts with KNOWN WRONG: contradicts the
example); every table row the engine does not produce sits in NOT_PRODUCED with its reason. The record and answers are in
cases/we015_porthalden/, the write-up in cases/we015_porthalden/out_of_sample.md. Nothing under praxeo/ was changed.

The meter fare (R1) is an existing rule, in force in the counterfactual too, so the record has it in `context` only: the
record has no field for existing rules, and the ceiling rules (PC-1 to PC-6) do not run on it.
"""
from test_out_of_sample import ROOT, _check, _engine, _rows

WE15 = ROOT / "cases" / "we015_porthalden"

SHORT = {"taxi operators": "drivers.taxi"}
WINDOWS = {"announcement window": "announcement"}

EXCEPTIONS = {
    ("drivers.taxi", "capital_stock_target", "decrease", None):
        "EN-13 (consolidation under tradable rights, added after the first run): the rights are transferable and holders differ; the example does not apply EN-13",
    ("drivers.taxi", "quantity_supplied", "increase", None):
        "EN-13 (consolidation under tradable rights, added after the first run): the rights are transferable and holders differ; the example does not apply EN-13",
    ("medallion_owners.initial", "right_lease_price", "increase", None):
        "EN-13 (consolidation under tradable rights, added after the first run): the rights are transferable and holders differ; the example does not apply EN-13",

    ("drivers.taxi", "entry_rate", "decrease", None):
        "EN-6 with seller_cap on the bound role; the table has the same fall for the would-be entrants (C-4, drivers.prospective), a class the quota record has no role field for",
    ("drivers.taxi", "informal_activity", "increase", None):
        "RS-3 with evasion, on the bound role; the table has the unlicensed drivers (C-10, drivers.unlicensed), who are outside the licensed class section 3 calls drivers.taxi. The record's bound_actor covers 'anyone offering taxi service', so the rule attaches it there",
    ("drivers.taxi", "quantity_traded", "decrease", None):
        "OC-4 names both sides of the prevented exchanges; C-23 names riders and the would-be drivers (drivers.prospective)",
    ("riders", "search_cost", "increase", None):
        "RS-3 and RS-10 for the unlicensed trade; the table gives it to riders.informal (C-16), a subclass of the record's buyer_actor",
    ("riders", "quality_information", "decrease", None): "same: C-26 is riders.informal",
    ("riders", "disputes_settled_outside_courts", "increase", None): "same: C-27 is riders.informal",
    # OC-3 with OC-1: the table's C-25 is the single class taxpayers (decrease); the engine gives the payer group
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-3 with OC-1 (general_budget, A-16): the payer group, member taxpayers; C-25 signs taxpayers alone as a decrease",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None): "same group, member 2 (OC-1, who pays)",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None): "same group, member 3 (OC-1, who pays)",
    # produced and WRONG by the example
}
NOT_PRODUCED = {
    "C-3": "missing rule: RS-8 for a quota or license cap (licenses taken out in the announcement window); the record sets announcement_window but no EN rule reads it",
    "C-4": "missing role: no field for would-be entrants in a quota (excluded_actor is not read); the rule signs entry_rate on the bound role (an exception above)",
    "C-6": "same: PC-1 and PC-2 on R1 (and A-18, no question)",
    "C-7": "same: PC-2 on R1; no role for outlying riders",
    "C-8": "same: PC-4 and RS-2 on R1; TS-1 for durable vehicles is not encoded for a cap",
    "C-9": "same: PC-6 and RS-3 on R1",
    "C-10": "missing role: the unlicensed drivers (section 3); the rule gives informal_activity to the bound role only (an exception above)",
    "C-11": "missing rule and role: RS-5 for the exempt private-hire segment (definition_line is set, no EN rule reads it); no role for private hire",
    "C-13": "missing rule: EN-2 signs net_price_received only; the holders' earnings from more trips or lease income at a fixed fare (CR-7b) is not encoded",
    "C-14": "missing rule: RS-1 for a quota (the buyer_substitutes premise exists for licensing only), and no role for the substitute's sellers",
    "C-15": "missing rule and role: PC-8 with its Unless clause (CR-4b, RS-13) for the exempt segment; no private-hire role",
    "C-16": "missing role: riders.informal (the engine signs the buyer class, an exception above)",
    "C-26": "same as C-16",
    "C-27": "same as C-16",
    "C-17": "missing role and rule: lenders to medallion buyers (SB-4 chain, CR-12e); no role field",
    "C-18": "missing role and rule: drivers.lessees; EN-2 lease capture (CR-7a) against busier cabs (CR-12b) is not encoded",
    "C-19": "later stage: app services (U1); the parser's readings carry no engine facts and no role, so nothing is signed per reading",
    "C-20": "same as C-19: no app_services role, RS-5 and PC-8 not encoded for quotas",
    "C-21": "missing role: medallion_holders (initial owners and later buyers); the single right_holder_actor is the initial owners (C-2 is produced for them), and the long-run erosion has no rule",
    "C-22": "missing role and rule: medallion_buyers.later; SB-4's decapitalization for a later buyer (GAP-015-1) is not encoded",
    "C-24": "missing role and rule: EN-3 (earnings of those excluded) is encoded for licensing only, and no role for would-be entrants",
    "C-25": "sign form: the engine gives the OC-1 payer group (taxpayers, other spending, future taxpayers) as at_least_one_decrease (exceptions above); the table signs taxpayers alone as a decrease because A-16 names the payer",
    "C-28": "missing record fact: full_cost_per_unit (fare plus side payments plus waiting) needs the PC rules on R1",
    "C-29": "missing rule and role: PC-8 Unless, CR-4b (would-be taxi drivers enter private hire); no private-hire role",
    "C-30": "missing rule: CR-12b over EN-6 (fewer cabs) and CR-7a (more drivers per medallion); employment is signed by EN-3 for licensing only",
    "C-31": "missing record fact and rule: the transfer fee and permit fees (CR-1, CR-8b); the record has no fee field and no role for the city's accounts",
    "C-32": "missing rule: CR-8c for the resources spent on lobbying (EN-5 and RS-7 sign the lobbying only)",
    "C-33": "missing rule: RS-8 with CR-9 for the first-year fleet from window licenses (A-4, A-14 have no question)",
}
PRODUCED = {"C-1", "C-2", "C-5", "C-12", "C-23", "C-34"}


def test_consistent_with_worked_example_we015():
    pred, keys = _engine(WE15)
    rows = _rows("WE-015_taxi_license_cap.md", SHORT, WINDOWS, {})
    assert len(rows) == 34
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    # the window flag adds no timing-window row: no quota rule reads it
    assert not any(c["window"] for c in pred["consequences"])
    # the seller_cap form: the number of sellers falls (C-1) and the cap's holders' asset value rises (C-2, SB-4)
    assert ("drivers.taxi", "number_of_sellers", "decrease", None) in keys
    assert ("medallion_owners.initial", "asset_value", "increase", None) in keys
