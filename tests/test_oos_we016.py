"""Out-of-sample run of the licensing rules (praxeo/rules/licensing.lp) on WE-016 (Arvane interior designers).

The licensing rules were written from WE-003 only; WE-016 was not seen when they were written. The record is
cases/we016_arvane/record.json (one licensing_requirement component, K1; K2 grandfathering, K3 stamped plans and K4
enforcement have no instrument of their own and enter through the right-holder, enforcer and general-budget roles). Same
shape as tests/test_licensing.py::test_consistent_with_worked_example_we003. The write-up is cases/we016_arvane/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE16 = ROOT / "cases" / "we016_arvane"

# The record has one seller role (`designers`) and one buyer role (`clients`); the table's recent, prospective and all designers,
# and its commercial and residential clients, are matched to them.
SHORT = {"designers": "designers", "designers.recent": "designers", "designers.prospective": "designers",
         "clients.commercial": "clients", "clients.residential": "clients", "clients": "clients",
         "schools": "schools.design", "retailers": "retailers.furniture"}
WINDOWS = {"announcement window": "announcement", "first months": "first_months"}
EXCEPTIONS = {

    ("clients", "quality_information", "ambiguous", None):
        "the row exists in the table only as C-28 (decrease, for clients who use unlicensed designers); the engine adds EN-11's "
        "increase for the licensed designers' buyers (A-13 high) and combines them in the one buyer role the record has",
    ("clients", "resources_available_other_uses", "decrease", None):
        "CR-8b, what the buyers pay above the old price is lost to their other uses (mirror of C-11, C-12); not in the table",
    ("designers", "employment", "decrease", None):
        "EN-3 with OC-4 for the bound role; the table has the recent designers' earnings (C-26, needs A-19) and sellers (C-2), not employment",
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-3 with OC-1: the payers of the general-budget share as a group, because the record names no tax; C-27 gives taxpayers alone",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None):
        "member of the OC-1 payer group (see above)",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None):
        "member of the OC-1 payer group (see above)",
}
NOT_PRODUCED = {
    "C-4": "role: compliance_cost (fees, documentation, continuing education) falls on holders by OC-2; the engine puts it on the "
           "bound role for those who qualify (some_qualify), not on the right holder `designers.grandfathered`",
    "C-8": "missing rule: RS-5 for the exemptions of a licensing_requirement (retail staff); no definition_line use in licensing.lp",
    "C-9": "missing rule: RS-8 (announcement window) is not encoded for licensing, and no question for A-8 is asked",
    "C-16": "missing role and rule: RS-5/RS-9 complements (furniture stores); no related market for licensing",
    "C-17": "same (trade showrooms)",
    "C-19": "missing rule: EN-4 and DM-2 (quality per unit, with stamped plans as the decisive pattern) are not encoded",
    "C-20": "missing rule: EN-4 (ambiguous without DM-2) is not encoded",
    "C-21": "missing rule: EN-9 (supervised hours) and a role for the apprentices",
    "C-22": "missing rule: RS-11 for a benefit lost by a change of status (grandfathered license); no question for A-16",
    "C-23": "missing rule: DM-3 combination of the degree route's gains and costs",
    "C-24": "missing rule: EN-2 gives net_price_received (C-13); earnings of the holders with CR-9 and the CR-12c separation are not encoded",
    "C-26": "missing rule: EN-3's premise that the next-best work pays less (A-19) is noted in licensing.lp as not encoded",
    "C-27": "combiner / sign form: the engine's OC-1 group is `at_least_one_decrease` over three payer classes; the table has `decrease` "
            "for taxpayers (Tier A, no premise) because the text says the Board is funded from the general budget",
    "C-28": "role: one buyer role; the buyers who use unlicensed designers are a subclass, and EN-11 for the licensed buyers combines "
            "with RS-10 to `ambiguous` (see EXCEPTIONS)",
    "C-30": "unsupported form: the reading U1 is about which good is covered (styling alone); it changes no Component field, and U1-b "
            "needs RS-5 (reshaping the service to the uncovered form)",
    "C-31": "missing rule and role: EN-9 with CR-1 and CR-6 for the apprentices' wait",
    "C-32": "missing rule: RS-11 and OC-2 for fees kept up while inactive",
    "C-33": "missing rule: RS-8 and CR-10a for the dip after the window (same as C-9)",
    "C-34": "missing role and rule: CR-9 and CR-6 for the architects' fees (no substitute-seller role for licensing)",
    "C-36": "missing record fact: K3 (stamped plans) has no component, so no building-department role; OC-3 is applied to the enforcer only",
}
PRODUCED = {"C-1", "C-2", "C-3", "C-5", "C-6", "C-7", "C-10", "C-11", "C-12", "C-13", "C-14", "C-15", "C-18", "C-25", "C-29", "C-35"}


def test_consistent_with_worked_example_we016():
    pred, keys = _engine(WE16)
    rows = _rows("WE-016_interior_designer_license.md", SHORT, WINDOWS, {})
    assert len(rows) == 36
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert set(NOT_PRODUCED) | PRODUCED == set(rows) and len(PRODUCED) == 16
    # the readings of U1 change no Component field, so the engine runs once and carries no per-reading signs
    assert not any(c["sign_by_reading"] for c in pred["consequences"])
