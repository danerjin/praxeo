"""Out-of-sample check of the mandate rules (praxeo/rules/mandates.lp: PC-17 developed on WE-029, PC-18 and EN-14 written from
the catalog alone) on WE-059, the right-to-repair act.

Same shape as tests/test_oos_we018.py. The rules were not changed for this example: every engine key is a row of the
example's consequence list or sits in EXCEPTIONS with its reason, classified "defensible" or "KNOWN WRONG", and every
table row the engine does not produce sits in NOT_PRODUCED with its reason category. The run is described in
cases/we059_kestrava/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE59 = ROOT / "cases" / "we059_kestrava"

# the table's "lobbying groups" (C-22) are makers, dealers, farm groups and repair associations; the record's roles are the
# bound makers, the dealers (K2) and the farm owners (the recipients who organize)
SHORT = {"lobbying groups": ["makers.ag", "makers.phone", "dealers.ag", "owners.ag"]}

EXCEPTIONS = {
    ("dealers.ag", "resources_available_other_uses", "decrease", None):
        "defensible: CR-8b, voiding of the dealers' anti-repair terms (K2, voids_existing): what the dealers lose the owners keep (C-39 is the owners' side); after the rule changes",
    ("owners.ag.exempt", "stock_age", "ambiguous", None):
        "defensible: EN-14 with its Unless clause (buyers value repairability, A-22): kept in use longer against drawn to covered units; C-29 signs the same ambiguous for covered units; after the rule changes",
    ("owners.phone.exempt", "stock_age", "ambiguous", None):
        "defensible: same, for phones sold before 2023",
    ("makers.ag", "quantity_supplied", "ambiguous", None):
        "defensible: EN-14's fewer new units against the Unless clause (A-22); C-30 records the same as quantity_traded, ambiguous; after the rule changes",
    ("makers.phone", "quantity_supplied", "ambiguous", None):
        "defensible: same, for phones (C-30)",
    # ---- EN-14 and RS-14 on new units
    ("buyers.prospective", "specification_level", "increase", None):
        "defensible: EN-14, the standard raises what new units must do; the example records the same fact as pairing removed or constrained (C-12) and as buyers valuing repairability (A-22, C-38)",
    # ---- PC-17 / PC-18 groups: the employment variables on buyers
    ("owners.ag", "non_wage_compensation", "increase", None):
        "defensible: the mandated term itself, received by the owners; the example records it as cheaper genuine parts and tools (C-1) and as information (C-37), under other variables",
    ("owners.phone", "non_wage_compensation", "increase", None):
        "defensible: the mandated term received by phone owners (see farm owners)",
    # ---- members of the example's groups signed alone
    ("makers.ag", "term_prevalence", "increase", None):
        "KNOWN WRONG: PC-18 signs the shift to substitute terms alone on substitute_terms; C-10 keeps it in a group with the price (at_least_one_as_stated), 'not netted' and not a price alone (final check 2); A-6 names no member",
    ("makers.phone", "term_prevalence", "increase", None):
        "KNOWN WRONG: same, for phones (C-10)",
    # ---- makers and rivals
    ("makers.ag", "resources_available_other_uses", "decrease", None):
        "defensible: CR-8b, the margin passes to the buyers of parts; the example signs owners' means only under conditions (C-39) and records makers' loss as value and cost",
    ("makers.phone", "resources_available_other_uses", "decrease", None): "defensible: same, for phone makers",
    ("makers.phone.matching", "quantity_supplied", "increase", None):
        "defensible: CR-9, the unbound rival sells more. The chain runs through the PC-17 group (others adjust, at least one), which the example's rule (CR-12 1.1: a group is not a chain) would not allow",
    # ---- lobbying: the Unless item
    ("makers.ag", "lobbying_effort", "ambiguous", None):
        "defensible: RS-7 Unless, item policy_field: lobbying on right to repair as such is signed against the contest of 2023 and 2025; C-22 leaves it unsigned, which is what ambiguous says",
    ("makers.phone", "lobbying_effort", "ambiguous", None): "defensible: same (policy_field item), phone makers",
    ("dealers.ag", "lobbying_effort", "ambiguous", None): "defensible: same (policy_field item), dealers",
    ("owners.ag", "lobbying_effort", "ambiguous", None): "defensible: same (policy_field item), farm groups",
    # ---- the state and complainants
    ("officials.enforcement", "enforcement_cost", "increase", None):
        "defensible: OC-3, Tier A: enforcing the Act costs the Division; with a fixed budget (OC-3 0.9) the example records the same work as other complaints waiting longer (C-41)",
    ("owners.ag", "compliance_cost", "increase", None):
        "defensible: RS-20, recipients spend time on complaints; the example records the complaints themselves (C-44), not their cost",
    ("owners.phone", "compliance_cost", "increase", None): "defensible: same, phone owners",
    # ---- the exempt stock
    ("owners.phone.exempt", "asset_value", "ambiguous", None):
        "defensible: EN-14 with its Unless clause for the phones sold before 2023; the example applies it to tractors only (C-28)",
}
NOT_PRODUCED = {
    "C-1": "missing rule: PC-17 gives the recipients the term (non_wage_compensation), not a fall in the price of the mandated inputs; independents, the third-party recipients, have no role in the record",
    "C-2": "role: independents; missing rule: RS-1 (more repairs outside the makers' network) is not encoded for a mandate",
    "C-3": "missing rule: RS-1 self repair (home_production) for a mandate",
    "C-4": "role: independents; missing rule: RS-16 per unit of quality with CR-12e's response argument is not encoded",
    "C-5": "missing rule: PC-18's direct effect (fewer enforceable anti-repair terms) is not derived; the engine's term_prevalence is the substitute-term increase",
    "C-6": "missing rule: RS-16 mirror (authorized repair loses demand); role: authorized_providers.phone has no component",
    "C-7": "missing rule: RS-16 mirror with waiting as a group member; role: authorized providers",
    "C-8": "role: independents.prospective; missing rule: RS-6 in reverse (entry)",
    "C-9": "missing rule: PC-17's group for a sale (price, warranty, models) is not encoded; the engine's group is wages, hours and jobs; sign form",
    "C-10": "sign form: the engine signs the substitute-term member alone (term_prevalence increase) and has no price member; the example's group is at_least_one_as_stated",
    "C-11": "missing rule: CR-7b across makers, dealers and buyers; the engine's incidence needs wages_adjust and falls on the recipients; role: dealers are not a party to the mandate",
    "C-12": "unsupported form: product_attribute (parts pairing) has no rule; U1's readings change no Component field, so the record carries no per-reading signs",
    "C-13": "role: parts_sellers.third_party; missing rule: RS-1 and CR-4 for non-genuine parts",
    "C-14": "unsupported form: informal trade in parts from stolen phones (RS-3) under a standard; per-reading sign needs a reading field",
    "C-15": "missing rule: RS-8 is not encoded for mandates (announcement_window is read by no mandate rule); role: authorized repairs",
    "C-16": "missing rule: RS-8 first months for mandates",
    "C-17": "missing rule: RS-4 for buyers crossing a line under a mandate (the mandate's boundary rule is for providers selling against rivals); no mobile-buyer role; combiner",
    "C-18": "missing rule: CR-9 for the makers' choice to extend a program nationally; role: Darnholt phone owners",
    "C-21": "missing rule: RS-24 (a cost fixed per model offered); variable variety",
    "C-24": "role: independents; missing rule: CR-7a for the repairers who gain",
    "C-25": "role: independents; combiner: CR-12e's response argument is not encoded",
    "C-27": "missing rule: CR-7c, RS-12 for the value of covered units to their owners (the recipients' asset value)",
    "C-29": "missing rule: CR-10b stock_age of covered units; the engine's stock_age is the exempt stock's and has the wrong sign",
    "C-30": "combiner: the engine has the decrease chain only (RS-14); the buyers' valuation (A-22) is a premise of EN-14's Unless for the stock, not of the new-sales total",
    "C-31": "missing rule: CR-5c for the dealers' parts price (a maker-dealer exchange); no such role",
    "C-32": "missing rule: CR-6 (the queue margin falls with capacity)",
    "C-33": "role: technicians; missing rule: RS-6, CR-9, LW-10 for the labour of the repair shops",
    "C-34": "role: technicians; missing rule: OC-5 (new activities)",
    "C-35": "role: technicians; combiner: opposing demands, no rule",
    "C-36": "role: buyers.used; missing rule: CR-11c, information conveyed by a lock",
    "C-37": "missing rule: EN-15 (disclosure mandate: diagnostic documentation); variable quality_information",
    "C-38": "unsupported form: product_attribute (separately replaceable parts) and TS-3 are not encoded",
    "C-41": "missing rule: OC-3's fixed-budget case (other complaints wait, time per complaint); role: complainants.other",
    "C-42": "role: independents; missing rule: CR-4 and CR-8a for inputs bought to use the access",
    "C-43": "missing rule: CR-9 for the dealers' parts counter",
    "C-44": "missing rule: RS-20 gives the owners a compliance cost and the makers a breach, not the complaints (applications) the example signs",
    "C-45": "missing rule: CR-9, LW-10 for makers' sales of genuine parts; per-reading sign",
    "C-47": "role: independents; missing rule: CR-6 against CR-5c; combiner",
}
PRODUCED = {f"C-{i}" for i in range(1, 48)} - set(NOT_PRODUCED)


def test_consistent_with_worked_example_we059():
    pred, keys = _engine(WE59)
    rows = _rows("WE-059_right_to_repair.md", SHORT, {}, {})
    assert len(rows) == 47
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert all(r.startswith(("defensible:", "KNOWN WRONG:")) for r in EXCEPTIONS.values())
    assert all(r.startswith(("missing rule", "missing record fact", "role", "combiner", "sign form", "unsupported form", "below cut-off"))
               for r in NOT_PRODUCED.values())
    assert len(PRODUCED) == 9  # 8 at the first run; C-39 after the rule changes (CR-8b on both sides of a voided term)
