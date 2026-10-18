"""Consistency tests for the out-of-sample worked examples WE-005, WE-006 and WE-067 (price ceilings).

Same shape as test_consistent_with_worked_example_we001: every engine consequence is a row of the example's
consequence list (key: actor class, variable, sign, window; a group gives one key per member), or sits in a dict of
exceptions with its reason; every table row the engine does not produce sits in a dict with the reason. The first runs
of the rules on these examples, before any rule change, are in cases/<case>/out_of_sample.md.
"""
import re
from pathlib import Path

from praxeo import parser
from praxeo.decider import FixtureDecider
from praxeo.pipeline import predict
from test_slice import _split_top

ROOT = Path(__file__).resolve().parents[1]
WE5 = ROOT / "cases" / "we005_corvane"
WE6 = ROOT / "cases" / "we006_coralia"
WE67 = ROOT / "cases" / "we067_tessford"


def _rows(example: str, short: dict, windows: dict, subclasses: dict) -> dict[str, set]:
    """The example's normal-form table as {row id: {(actor class, variable, sign, window)}}. `short` maps the table's actor
    name to one or more record role names; `windows` maps a cell qualifier to a timing window; `subclasses` maps a cell
    qualifier to the suffix of the engine's subclass name. A bracketed qualifier is otherwise dropped."""
    md = (ROOT / "handbook" / "05_examples" / example).read_text()
    table = md.split("## Consequence list (normal form)")[1].split("## Gaps found")[0]
    rows: dict[str, set] = {}
    for line in table.splitlines():
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) > 4 and re.match(r"C-\d+$", cells[0]):
            actor_cell, var_cell = cells[1], cells[2]
            window = next((w for q, w in windows.items() if q in actor_cell or q in var_cell), None)
            keys = set()
            for a in _split_top(actor_cell):
                name = re.sub(r"\s*\(.*", "", a).strip()
                suffix = next((s for q, s in subclasses.items() if q in a), "")
                names = short.get(name, name)
                for n in ([names] if isinstance(names, str) else names):
                    for v in _split_top(var_cell):
                        keys.add((n + suffix, re.sub(r"\s*\(.*", "", v).strip(), cells[3], window))
            rows[cells[0]] = keys
    return rows


def _engine(case: Path):
    record = parser.parse_fixture(case / "record.json")
    pred = predict((case / "policy.txt").read_text(), record, FixtureDecider(case / "answers.json"))
    assert pred["citation_problems"] == [] and pred["verifier_problems"] == []
    keys = {(c["actor_class"], v, c["sign"], c["window"]) for c in pred["consequences"] if c["reported"]
            for v in (c["group"] or [c["variable"]])}
    return pred, keys


def _check(rows, keys, exceptions, not_produced, produced_rows):
    table = set().union(*rows.values())
    for key in keys:
        assert key in table or key in exceptions, key
    assert keys & set(exceptions) == set(exceptions)  # an exception that no longer occurs is removed
    got = {rid for rid, ks in rows.items() if ks & keys}
    assert set(rows) - got == set(not_produced)
    assert got == set(produced_rows)
    assert len(got) + len(not_produced) == len(rows)


# ---------------------------------------------------------------- WE-005

WE005_EXCEPTIONS = {
    ("stations", "maintenance_spending", "decrease", None): "PC-4 pairs it with quality_per_unit; C-8 describes closed restrooms and air pumps (maintenance), the table lists the quality row only",
    ("drivers.served", "quality_per_unit", "decrease", None): "PC-4 puts the cut on the protected buyers; the table records the same cut on the stations' side (C-8)",
    ("drivers.served", "resources_available_other_uses", "increase", None): "CR-8b, what the buyers keep (mirror of C-2); the table does not list it",
    ("stations", "resources_available_other_uses", "decrease", None): "CR-8b, the sellers' side of C-1 and C-2",
    ("drivers.served", "quality_adjusted_price", "ambiguous", None): "price against quality, ambiguous by the handbook's own treatment (WE-001); WE-005 records full_cost_per_unit instead (C-23)",
    ("drivers.served", "price_paid", "decrease", "first_months"): "same sign as C-1: the combiner forms the first-months row from the cap chain when window_repricing is unreported, as WE-001 A-11 says (C-21 becomes a decrease)",
    ("drivers", "disputes_settled_outside_courts", "increase", None): "RS-10 for the informal trade in cans (C-9, C-22); the variable is not in the table",
    ("drivers", "side_payments", "increase", None): "PC-6 with RS-3: the table records the same trade as informal_activity (C-9) and as premiums in C-23",
    ("drivers", "quantity_traded", "decrease", None): "OC-4 names both sides of prevented exchanges; C-20 names the unserved drivers, a subclass of the record's excluded role `drivers`",
    # the PC-2 group (PC-2 Then): the table lists the members one by one with their own premises (C-5 to C-7, C-9), not the group
    ("drivers", "wait_time", "at_least_one_increase", None): "member of the PC-2 group, implied by C-5, C-6, C-7 and C-9",
    ("drivers", "search_cost", "at_least_one_increase", None): "member of the PC-2 group (see above)",
    ("drivers", "side_payments", "at_least_one_increase", None): "member of the PC-2 group (see above)",
    ("drivers", "allocation_by_non_price_criteria", "at_least_one_increase", None): "member of the PC-2 group (see above)",
    # produced and WRONG by the handbook: see WE005_KNOWN_WRONG
    ("drivers.brennick", "price_paid", "increase", None): "KNOWN WRONG: RS-4 alone",
    ("stations", "resources_available_other_uses", "increase", None): "KNOWN WRONG: the key-money item",
}
# Engine consequences that contradict the handbook and have not been fixed (a fix needs more than a general pattern).
WE005_KNOWN_WRONG = {
    ("drivers.brennick", "price_paid", "increase", None):
        "the handbook prunes the Brennick price because it combines the diversion of supply with the ambiguous crossing (C-17); the engine has the buyers-arrive chain only",
    ("stations", "resources_available_other_uses", "increase", None):
        "the item key_money gives the above-cap receipt to the stations; WE-005's K2 bans surcharges and the informal sales are resales of fuel in cans by individuals (C-9)",
}
WE005_NOT_PRODUCED = {
    "C-5": "PC-2's wait_time member has no question (no queue premise)",
    "C-8": "the rules sign quality_per_unit on the protected buyers, not on the bound sellers",
    "C-12": "RS-8 is encoded for sellers' repricing only; buyers waiting for the lower price is not",
    "C-13": "same, with TS-7 for the stations' wholesale purchases",
    "C-14": "needs PC-12 with RS-6 and a role for the refiner (a second input-supplier role)",
    "C-16": "RS-1 for a ceiling is not encoded (tariffs only); the subclass drivers.unserved is not a record role",
    "C-17": "RS-4 signs the neighbours' price, not the buyers' crossing; no combiner entry; no drivers.border role",
    "C-18": "RS-9 is not encoded; the station subclasses (out of fuel, with fuel) are not record facts",
    "C-19": "same",
    "C-22": "RS-10 is encoded for disputes_settled_outside_courts only",
    "C-23": "no rule or combiner entry for full_cost_per_unit",
    "C-24": "needs PC-12, RS-6 and RS-8 around the expiry date",
    "C-25": "RS-8 with TS-7 around the expiry date is not encoded",
}
WE005_PRODUCED = {"C-1", "C-2", "C-3", "C-4", "C-6", "C-7", "C-9", "C-10", "C-11", "C-15", "C-20", "C-21", "C-26"}


def test_consistent_with_worked_example_we005():
    pred, keys = _engine(WE5)
    rows = _rows("WE-005_gasoline_price_cap.md", {}, {"Days 3–5": "announcement"}, {})
    assert len(rows) == 26
    _check(rows, keys, WE005_EXCEPTIONS, WE005_NOT_PRODUCED, WE005_PRODUCED)
    assert set(WE005_KNOWN_WRONG) <= set(WE005_EXCEPTIONS) and len(WE005_PRODUCED) == 13
    # C-20 names the unserved drivers and the suppliers; only the suppliers' side is produced (PC-12 quantity branch with OC-4)
    assert ("suppliers", "quantity_traded", "decrease", None) in keys
    # PC-12: the price branch (C-11) and the quantity branch (C-10) both hold, at A-7 and A-6
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"]}
    assert by[("suppliers", "net_price_received")]["assumptions"] == ["binding(k1)", "enforced(k1)", "input_few_outlets(k1)"]
    assert by[("suppliers", "quantity_supplied")]["assumptions"] == ["binding(k1)", "enforced(k1)", "input_other_outlets(k1)"]
    # the group form of PC-2 is one consequence with four members
    assert [c["group"] for c in pred["consequences"] if c["group"]] == [["wait_time", "search_cost", "side_payments", "allocation_by_non_price_criteria"]]
    # the 6 million drivers are not a concentrated group (RS-7): the stations lobby, the drivers do not
    assert ("drivers.served", "lobbying_effort", "increase", None) not in keys and ("stations", "lobbying_effort", "increase", None) in keys


# ---------------------------------------------------------------- WE-006

WE006_EXCEPTIONS = {
    ("buyers.served", "quality_per_unit", "decrease", None): "PC-4 puts the cut on the protected buyers; the table has it on hotels.declared (C-10)",
    ("evacuees.in_rooms", "quality_per_unit", "decrease", None): "same, for the guests in rooms",
    ("sellers.local", "maintenance_spending", "decrease", None): "PC-4 pairs it with quality_per_unit; the table omits it",
    ("sellers.outside", "maintenance_spending", "decrease", None): "same, for the outside sellers",
    ("hotels.declared", "maintenance_spending", "decrease", None): "same, for the hotels",
    ("buyers.served", "resources_available_other_uses", "increase", None): "CR-8b, what the buyers keep (mirror of C-24)",
    ("evacuees.in_rooms", "resources_available_other_uses", "increase", None): "CR-8b, what the guests keep (mirror of C-24)",
    ("evacuees.in_rooms", "price_paid", "decrease", None): "C-1 for the rooms (the table names buyers.served for goods and rooms together)",
    ("sellers.local", "resources_available_other_uses", "decrease", None): "CR-8b, the sellers' side of C-1 (total of the CR-12 comparison and its item rent_forgone)",
    ("sellers.outside", "resources_available_other_uses", "decrease", None): "same, for the outside sellers",
    ("hotels.declared", "resources_available_other_uses", "decrease", None): "same, for the hotels",
    ("sellers.local", "resources_available_other_uses", "increase", None): "key-money item of the CR-12 comparison: C-14's informal sales above the cap are receipts of sellers",
    ("sellers.outside", "resources_available_other_uses", "increase", None): "key-money item (see above)",
    ("hotels.declared", "resources_available_other_uses", "increase", None): "key-money item (see above)",
    ("buyers.served", "quality_adjusted_price", "ambiguous", None): "the handbook's price-against-quality comparison (WE-001); not in WE-006's table",
    ("evacuees.in_rooms", "quality_adjusted_price", "ambiguous", None): "same",
    ("evacuees.in_rooms", "informal_activity", "increase", None): "PC-6 sublet form (nontransferable from A-8); A-8 itself says a guest cannot pass the room on, so the route is doubtful; the sign is C-14's",
    ("residents.declared", "disputes_settled_outside_courts", "increase", None): "RS-10 for the informal trade (C-14, C-25); the variable is not in the table",
    ("residents.declared", "price_substitute", "increase", None): "PC-8 with A-13; the table signs the quantity (C-17) and RS-1 leaves the price to RS-16",
    ("residents.declared", "quantity_traded", "decrease", None): "OC-4: C-22 names buyers.unserved, a subclass of the record's excluded role",
    ("residents.declared", "side_payments", "increase", None): "PC-6 with RS-3; a member of the C-4 group, signed on its own premise (A-10)",
    ("sellers.local", "quantity_traded", "decrease", None): "OC-4 names both sides of a prevented exchange; the table names the outside sellers (C-22)",
    ("buyers.inland", "price_paid", "increase", None): "RS-4 (inland stores take the extra demand, A-12); the table records the crossing (C-18), not the inland price",
}
WE006_NOT_PRODUCED = {
    "C-7": "PC-13 (documented costs) is not encoded",
    "C-9": "RS-8 release of stock after the cap lapses; no such window in the engine",
    "C-10": "the rules sign quality_per_unit on the protected buyers, not on the hotels",
    "C-13": "PC-13 (the cost of documenting under K2) is not encoded",
    "C-17": "RS-1 for a ceiling is not encoded",
    "C-18": "RS-4 signs the neighbours' price, not the buyers' crossing; no combiner entry",
    "C-19": "a depth-4 chain through C-11 to a role the record lacks",
    "C-20": "TS-7 (expected caps reduce stocks held) is not encoded",
    "C-21": "standing-law RS-8 before the season is not encoded",
    "C-23": "OC-3's fixed-budget case is not encoded",
    "C-25": "RS-10 is encoded for disputes_settled_outside_courts only",
}
WE006_PRODUCED = {"C-1", "C-2", "C-3", "C-4", "C-5", "C-6", "C-8", "C-11", "C-12", "C-14", "C-15", "C-16", "C-22", "C-24", "C-26"}


def test_consistent_with_worked_example_we006():
    pred, keys = _engine(WE6)
    rows = _rows("WE-006_price_gouging_law.md", {}, {}, {})
    assert len(rows) == 26
    _check(rows, keys, WE006_EXCEPTIONS, WE006_NOT_PRODUCED, WE006_PRODUCED)
    assert len(WE006_PRODUCED) == 15
    # C-4 is produced as a group over the four rationing variables
    assert ("residents.declared", "wait_time", "at_least_one_increase", None) in keys
    # the record has three components (goods sold by local sellers, goods brought in, rooms) so that the outside sellers and
    # the hotels have a role; the diffuse buying public does not lobby (RS-7)
    assert ("buyers.served", "lobbying_effort", "increase", None) not in keys
    assert ("sellers.outside", "quantity_supplied", "decrease", None) in keys   # C-6
    assert ("evacuees.in_rooms", "turnover", "decrease", None) in keys           # C-11
    # no 'displaced' holders where nothing is held (PC-7): the goods are not a tenancy
    assert not any(k[0].endswith(".displaced") for k in keys)


# ---------------------------------------------------------------- WE-067

WE067_SHORT = {"sitting tenants": ["tenants.covered.other", "tenants.covered.senior"],
               "sitting tenants renewing before 1 October 2027": ["tenants.covered.other", "tenants.covered.senior"],
               "landlords": "landlords.covered", "tenant unions": "tenants.covered.other",
               "tenants.displaced.other": "tenants.covered.other.displaced"}
WE067_WINDOWS = {"first months": "first_months", "announcement window": "announcement", "(announcement)": "announcement",
                 "rents set before": "announcement", "renewing before": "announcement", "March–September 2027": "announcement"}
WE067_SUBCLASSES = {"(keep the unit)": ".keepers"}

WE067_EXCEPTIONS = {
    ("landlords.covered", "resources_available_other_uses", "increase", None):
        "the key-money item of C-44's CR-12 comparison: section 7 lists 'rents above the cap taken by landlords who evade' as a (+) chain",
    ("tenants.prospective", "disputes_settled_outside_courts", "increase", None):
        "RS-10 for the sublet trade (A-11): the subtenants are households seeking a home; WE-001 C-23 has the same row",
}
WE067_KNOWN_WRONG: dict = {}   # the seekers' side payments under vacancy decontrol: fixed in PC-6 (1.4 decontrol note)
WE067_NOT_PRODUCED = {
    "C-4": "unsupported form: the Portable Senior Credit (K4) is a payment attached to renting elsewhere",
    "C-5": "unsupported form (K4): no subsidy rule",
    "C-10": "needs the senior class and the credit's portable range (PC-21 1.4 per destination)",
    "C-11": "same",
    "C-13": "missing record fact (no-cause terminations under state law, the class tenants.window_terminated) and a question for A-8",
    "C-14": "senior class and credit",
    "C-15": "credit; RS-8 delay to qualify",
    "C-23": "senior class, credit and the reading U1 (the parser's readings carry no engine facts)",
    "C-24": "same",
    "C-25": "same as C-13",
    "C-27": "RS-7's Unless clause is not encoded (the counterfactual is contested, A-19)",
    "C-28": "OC-2 for registration and the fee needs a record fact and a rule; the engine's compliance cost is the exit-process form",
    "C-30": "one neighbour role per component (Durnside)",
    "C-32": "PC-21's population caveat (shut-out residents leave more) is not encoded",
    "C-33": "the rental to owner-occupied relation is a record fact (as in WE-001 C-14)",
    "C-35": "no landlords.exempt role; SB-4 is applied to the bound sellers only",
    "C-36": "no role or exemption fact (as in WE-001 C-13)",
    "C-37": "no landlords.county role",
    "C-40": "unsupported form (K4, paid from the general fund)",
    "C-41": "unsupported form (K4)",
    "C-43": "unsupported form (K6)",
    "C-46": "case-specific provision (relocation payment, K3), as in WE-001 C-30",
    "C-47": "OC-3's own-revenue funding case with CR-8b is not encoded",
    "C-50": "needs a per-horizon sign (TS-3); the engine's decrease holds from the medium horizon onward",
    "C-51": "the total across kept, displaced and senior classes; no senior class",
    "C-52": "senior class, credit",
    "C-55": "the combiner declares the first-months total for the buyers' price only",
    "C-56": "CR-8b mirror of C-12 in the window is not encoded",
    "C-58": "RS-8 for landlords' no-cause terminations: missing record fact and rule",
    "C-61": "PC-6 buyout form (A-29) is not encoded",
    "C-62": "credit",
    "C-63": "unsupported form (K6)",
    "C-64": "no rule for commuting by shut-out seekers",
    "C-65": "no landlords.county role",
    "C-66": "unsupported form (K4)",
    "C-67": "no rule for moving cost (CR-1 and CR-8c)",
    "C-68": "no rule",
    "C-69": "no variable rule (fund_balance)",
    "C-70": "the combiner forms no turnover total (README)",
    "C-71": "destination (out of the county) not represented",
    "C-72": "senior classes",
    "C-73": "the landlords' side of C-53 (CR-8b mirror) is not encoded",
}
WE067_PRODUCED = {"C-1", "C-2", "C-3", "C-8", "C-9", "C-12", "C-16", "C-17", "C-18", "C-19", "C-20", "C-21", "C-22", "C-26",
                  "C-29", "C-31", "C-34", "C-38", "C-39", "C-42", "C-44", "C-45", "C-48", "C-49", "C-53", "C-54", "C-57",
                  "C-59", "C-60"}


def test_consistent_with_worked_example_we067():
    pred, keys = _engine(WE67)
    rows = _rows("WE-067_rent_cap_senior_credit.md", WE067_SHORT, WE067_WINDOWS, WE067_SUBCLASSES)
    assert len(rows) == 71  # C-1 to C-73 without the removed C-6 and C-7
    _check(rows, keys, WE067_EXCEPTIONS, WE067_NOT_PRODUCED, WE067_PRODUCED)
    assert set(WE067_KNOWN_WRONG) <= set(WE067_EXCEPTIONS) and len(WE067_PRODUCED) == 29
    # vacancy decontrol: no excess demand for new contracts, so none of the PC-2 group or LW-3 rows (PC-1 1.4)
    assert not any(k[1] in ("excess_demand", "quantity_demanded", "wait_time") for k in keys)
    by = {(c["actor_class"], c["variable"], c["window"]): c for c in pred["consequences"]}
    assert by[("tenants.covered.other", "price_paid", "first_months")]["sign"] == "ambiguous"                   # C-2
    assert by[("tenants.covered.other", "price_paid", None)]["comparison"] == "capped_price_vs_rush"           # C-1 with A-5
    assert by[("tenants.covered.other", "relocation_out_of_area", None)]["comparison"] == "pc_21_relocation"   # C-49 with A-26
    # the displaced holders exist here (nontransferable, A-3), unlike WE-006's goods
    assert ("tenants.covered.other.displaced", "turnover", "increase", None) in keys
