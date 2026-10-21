"""Out-of-sample run of the licensing rules (praxeo/rules/licensing.lp) on WE-055, home inspector licensing with grandfathering.

The licensing rules were developed on WE-003 only. Same shape as tests/test_licensing.py::test_consistent_with_worked_example_we003:
every reported engine consequence is a row of the example's consequence list or sits in EXCEPTIONS with its reason (a reason that
starts with KNOWN WRONG: marks a row that contradicts the example); every table row the engine does not produce sits in
NOT_PRODUCED with its reason. The record and answers are in cases/we055_aldenmoor/, the write-up in
cases/we055_aldenmoor/out_of_sample.md. Nothing under praxeo/ was changed for this run.

The table gives some signs by reading of the unclear provision U1 (C-3, C-24, C-25). U1 changes no Component field, so the
record carries no reading_fields and the engine's signs are the same under both readings; the table's per-reading cells
are therefore compared as they stand and match no engine key.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE55 = ROOT / "cases" / "we055_aldenmoor"

# the table's "unlicensed inspectors" are the bound inspectors who keep selling without a license (RS-3, as WE-003's C-17)
SHORT = {"unlicensed inspectors": "inspectors"}
# the table's qualifiers in the actor and variable cells are windows of the example's own calendar (January 2026 to June 2027,
# 2027, from 2028), which the engine's short/medium/long windows do not carry; no engine row has a window
WINDOWS = {}

EXCEPTIONS = {
    ("buyers.current", "quality_information", "increase", None):
        "EN-11 (the license tests what buyers value): C-3 under U1-a; its U1-b sign (ambiguous) needs a reading fact the record cannot state",
    ("buyers.unlicensed", "search_cost", "increase", None):
        "RS-10 for the buyers of unlicensed inspections (`informal_buyer_actor`, added after the first run); the table records their quality information only (C-34)",
    ("buyers.unlicensed", "disputes_settled_outside_courts", "increase", None):
        "RS-10, as above",

    ("buyers.current", "quantity_substitute", "increase", None):
        "defensible: EN-3 with RS-1 (A-9, A-19): buyers priced out turn to engineers or to unlicensed inspectors; the example "
        "signs the engineers' side (C-20), not the buyers' substitution",
    ("inspectors", "compliance_cost", "increase", None):
        "defensible: the bound class as a whole; C-1 and C-15 sign the three classes the grandfathering line makes "
        "(grandfathered, new_requirement, prospective), none of which the record can name",
    ("inspectors", "employment", "decrease", None):
        "defensible: EN-3 for those who do not qualify (C-5, C-36 give the exit and the trainees); the example leaves "
        "employment in the trade unsigned and the earnings of the excluded below the cut-off (A-11)",
    ("inspectors", "entry_rate", "decrease", None):
        "defensible: C-4 signs inspectors.prospective entry short run `decrease`; the engine puts it on the bound role (the "
        "record has no would-be entrants role) and has one sign where C-32 and C-33 give three horizons",
    ("inspectors", "quantity_traded", "decrease", None):
        "defensible: OC-4's sellers' side of C-7; the example signs only the buyers' side",
    ("inspectors.licensed", "lobbying_effort", "increase", None):
        "defensible: lobbying over the provisions that exist only under the Act (EN-5; CR-4 1.1: an increase against none), "
        "beside the contested-field row (the item policy_field, C-19). WE-067 (C-26, C-27) and WE-065 (C-15, C-36) sign both; "
        "WE-055 lists only the contested one. The first run counted this row WRONG",
    ("inspectors.licensed", "lobbying_effort", "ambiguous", None):
        "defensible: C-19 (RS-7 Unless, A-18) on the license holders rather than on inspectors.grandfathered, which the record "
        "cannot name; reported with the policy_field qualifier",
    ("inspectors.licensed", "net_price_received", "increase", None):
        "defensible: EN-2 for the license holders; C-8 signs it for the grandfathered and for the new_requirement who qualify",
    ("training_schools", "quantity_demanded", "increase", None):
        "defensible: CR-8c, the schools' receipts from those who train (A-2); C-13 signs the trainees' enrollment in 2027 and "
        "C-14 the schools' enrollment from 2028 `ambiguous`, so the short-run increase does not contradict it",
}

NOT_PRODUCED = {
    "C-1": "missing record fact: the compliance cost falls on three classes the grandfathering line makes (grandfathered, new_requirement, prospective); the engine signs it on the one bound role",
    "C-3": "combiner and missing record fact: the engine reports `ambiguous` (see EXCEPTIONS); the table has U1-a `increase`, U1-b `ambiguous`; no buyers.unlicensed role, and U1 sets no Component field",
    "C-4": "missing record fact: no would-be entrants role (inspectors.prospective); the engine's entry_rate row is on the bound role",
    "C-8": "missing record fact: the gain settles on grandfathered and new_requirement who qualify; the engine signs it on the right_holder role",
    "C-9": "missing rule: CR-7 earnings of holders (money earnings need a premise, A-10); the licensing rules sign net_price_received only",
    "C-10": "case-specific provision and missing rule: RS-8 and RS-17 (rush to reach the grandfathering line, K2); no field for a grandfathering line and no near_line role; announcement_window has no licensing rule",
    "C-11": "case-specific provision and missing rule: as C-10 (near-line inspectors cut fees to win extra jobs, CR-4, CR-5c)",
    "C-12": "case-specific provision and missing rule: as C-10 (rivals lose the inspections the rush takes, RS-8 rivals form)",
    "C-13": "missing rule: RS-8 for training enrollment in the window before the deadline; announcement_window is set but only the receipts of the schools (quantity_demanded) are derived",
    "C-14": "missing rule: CR-9 and CR-12b for the schools' enrollment after the bunch (ambiguous); no horizon rows in licensing.lp",
    "C-15": "unsupported form: grandfather applications (K2) as an exemption with an application cost; OC-2 compliance cost is not derived for an exemption",
    "C-16": "unsupported form: RS-11 with the 12-month lapse clause (a status lost on leaving); no field for a forfeiture condition",
    "C-18": "missing record fact: no role for real-estate agents (intermediaries) and no rule that signs the schools' lobbying; EN-5 and RS-7 are derived for the holders only",
    "C-19": "missing record fact: the engine's `ambiguous` row is on inspectors.licensed (right_holder_actor); the table names inspectors.grandfathered, a class the record has no field for",
    "C-20": "missing record fact: the exempt engineers (engineers.exempt, sellers.substitutes) are a role with no licensing field; EN-3 with RS-1 gives the buyers' substitution only",
    "C-21": "missing record fact and rule: exempt engineers' fee (RS-16 1.0, CR-6); no role for them",
    "C-22": "missing record fact and rule: CR-11 for engineers who now tell buyers of their license; no role for the exempt",
    "C-23": "missing record fact: Linmouth inspectors (neighboring_jurisdictions); neighbor_seller_actor exists for per-unit taxes only",
    "C-24": "unsupported form: CR-7c asset value of sellable firms with U1 readings; no firms role and no reading field",
    "C-25": "unsupported form: U1 reading (agents' recommendations, K4); no encodable instrument for a rule on agents' conduct and no role for referral users; the engine's search_cost is the RS-3 row, not this one",
    "C-26": "missing rule: EN-4 (quality received by buyers, ambiguous) is not encoded",
    "C-27": "missing record fact and rule: insurers (input_suppliers) of the required cover; no input_supplier_actor for licensing, CR-1 and CR-9",
    "C-28": "missing rule: RS-20 (complaint-only enforcement) and CR-8c; the complaint-based enforcement of K3 is not a field",
    "C-31": "missing rule: CR-1 and CR-8b receipts of the Board (fees, fines); licensing.lp derives enforcement_cost only",
    "C-32": "missing rule: EN-1 1.0 entry by horizon (CR-4, CR-7a, CR-12b); the engine has entry_rate short only",
    "C-33": "missing rule: EN-1 1.0 long-run entry (CR-10b, A-32); as C-32",
    "C-35": "missing record fact and rule: engineers' other clients (CR-9, CR-7a, CR-6); no role",
    "C-36": "missing record fact: the new_requirement inspectors who train and stay; CR-3 and CR-8b for trainees have no role",
    "C-37": "missing rule: CR-8b (1.0) with OC-1 for the Board's fund balance (fees and fines less costs, ambiguous); no receipts side",
}
PRODUCED = {"C-2", "C-5", "C-6", "C-7", "C-17", "C-29", "C-30", "C-34"}


def test_consistent_with_worked_example_we055():
    pred, keys = _engine(WE55)
    rows = _rows("WE-055_home_inspector_licensing.md", SHORT, WINDOWS, {})
    assert len(rows) == 37
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
