"""Out-of-sample check of the mandate rules (praxeo/rules/mandates.lp: PC-17 developed on WE-029; PC-18 and EN-14 written from
the catalog alone) on WE-031, the building energy code, a product_standard (EN-14).

Same shape as test_oos_we018.py. The rules were not changed for this example: every engine consequence is a row of the
example's consequence list or sits in EXCEPTIONS with its reason (each classified "defensible" or "KNOWN WRONG"), and every
table row the engine does not produce sits in NOT_PRODUCED with its reason. The run is described in
cases/we031_westmere/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE31 = ROOT / "cases" / "we031_westmere"

EXCEPTIONS = {
    ("buyers.new_homes", "specification_level", "increase", None):
        "defensible: EN-14 puts specification_level on the buyers of the new units (the homes they get); the table puts it on the builders (C-2), whose designs it constrains",
    ("owners.existing_homes", "stock_age", "increase", None):
        "defensible: section 5 says the existing stock is kept in use longer; the example folds it into C-5 and C-11 and lists no row (Gaps found, item 4: no variable then)",
}
NOT_PRODUCED = {
    "C-2": "role: EN-14 signs specification_level on the buyers, the table on the builders; the engine's row is in EXCEPTIONS",
    "C-6": "missing rule and record fact: fixed per-plan costs of compliance (CR-4 note on lumpy costs) are not in EN-14; no small-builders role or question for A-8",
    "C-7": "missing rule and record fact: RS-8 with a dated schedule of later steps; the record has no field for the steps, and RS-8 is encoded for a single announced measure",
    "C-8": "missing rule: the quarter after each step (RS-8), as for C-7",
    "C-9": "missing rule and role: OC-3's fixed-budget case (review staff fixed, A-10) and a permit-applicants role; EN-14 asks no question for it",
    "C-10": "missing rule: RS-5 is encoded for a mandated term (mc_reshaped); the record carries definition_line and outside_actor (homeowners.renovating) but EN-14 does not read them",
    "C-11": "missing rule: RS-1 and RS-16 for the exempt substitutes (renovation) are not in EN-14; the stock effect is signed on the stock's owners only",
    "C-12": "missing rule and record fact: CR-4c on unit size under a per-square-foot index; U1 changes no Component field, so no reading can differ",
    "C-13": "missing record fact and rule: exempt new substitutes (manufactured homes) have no role; EN-14 reads only the exempt existing stock",
    "C-14": "missing rule: RS-4 is not in EN-14 (the record's neighbor_seller_actor is read only for mandated terms); no neighbours' role recorded",
    "C-15": "missing rule and record fact: price of the rating service under capacity limits (CR-6, CR-9, A-14); raters are not a role of EN-14",
    "C-16": "missing rule and role: entry of raters (CR-4, CR-7a)",
    "C-17": "missing rule and role: RS-3 for false certification by builders and raters; the breach rule (RS-20) is for complaint-only mandates",
    "C-19": "role: RS-7 is encoded for the bound party and, for a mandated term, its recipients; the beneficiaries of a standard (efficiency-product makers) have no role",
    "C-20": "unsupported form: an existing rule (the rebate's threshold) moved by the Act; no instrument or rule for that",
    "C-22": "missing rule and role: RS-16 on the price of the exempt stock to its buyers (buyers.existing_homes); EN-14 signs the owners' asset value only",
    "C-23": "missing rule and role: CR-7b and CR-7c for the owners of the factor specific to new units (buildable lots)",
    "C-24": "missing rule and role: the standard raises the demand for compliance inputs per home; CR-9 through target_qty would give the opposite sign (see out_of_sample.md)",
    "C-25": "missing record fact: the policy text names no suppliers of other inputs; the variable is quantity_demanded, relations.lp writes quantity_traded; signs differ by reading of U1",
    "C-26": "combiner and missing rule: employment and hours of construction labor (CR-9, CR-12b), ambiguous by two chains",
    "C-27": "missing rule and role: RS-16 and CR-9 to rents (renters)",
    "C-28": "combiner and missing rule: DM-3, CR-12b: the price against lower energy spending (A-24); no rule signs buyers' means under a standard",
    "C-29": "missing rule: OC-4 and CR-5a, the prevented exchanges of homes below the standard, are not derived from EN-14",
    "C-31": "missing rule: OC-3's fixed-budget case (CR-8a), less other inspection work; EN-14 signs enforcement_cost increase only (C-3)",
    "C-32": "unsupported form: the existing rebate rule moved by the Act (see C-20)",
    "C-33": "unsupported form: RS-8 around the first step, per reading of U2, which is about the rebate rule, not a Component field",
    "C-34": "unsupported form: as C-33",
    "C-35": "combiner and unsupported form: price in Years 1 to 3 sets the compliance chain against the looser rebate (existing rule); the engine gives increase over short to long (C-4)",
    "C-36": "combiner and unsupported form: as C-35, for quantity",
    "C-37": "missing rule and role: CR-1 and CR-9 for the rating service K3 requires on every home; derived demand through target_qty would give the opposite sign (see out_of_sample.md)",
    "C-38": "missing rule and role: CR-7c and CR-10c for raters' certifications",
    "C-39": "missing rule and role: CR-4 on variety (plans offered) by small builders",
    "C-40": "missing rule and role: CR-7b pair incidence between lot owners and builders",
    "C-41": "missing rule and role: CR-7c and CR-10c for makers of efficiency products",
    "C-42": "missing rule and role: CR-6, CR-9 on auditors drawn into rating (buyers.home_energy_audits)",
    "C-43": "unsupported form: the existing rebate's outlay (utilities.rebate_program) under a moved threshold",
    "C-44": "unsupported form: as C-43",
    "C-45": "unsupported form and sign form: the rebate budget's other side (ratepayers) as an at_least_one group, from the existing rule",
    "C-46": "unsupported form and sign form: as C-45",
    "C-47": "missing rule and sign form: RS-6, resources moving to commercial building; a mixed group (price_paid -, quantity_traded +) that no sign encodes",
}
PRODUCED = {"C-1", "C-3", "C-4", "C-5", "C-18", "C-21", "C-30"}


def test_consistent_with_worked_example_we031():
    pred, keys = _engine(WE31)
    rows = _rows("WE-031_building_energy_code.md", {}, {}, {})
    assert len(rows) == 47
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert len(PRODUCED) == 7 and len(NOT_PRODUCED) == 40
    # nothing is below the cut-off: the engine reports every consequence it derives
    assert all(c["reported"] for c in pred["consequences"]) and len(pred["consequences"]) == 9
