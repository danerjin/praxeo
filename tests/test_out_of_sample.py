"""Out-of-sample consistency tests: five handbook worked examples with per-unit taxes or tariffs (WE-002, WE-010, WE-042,
WE-046, WE-062), encoded after the rules were built from WE-013.

Each test is the analogue of `test_consistent_with_worked_example_we013` (tests/test_slice.py):
- every reported engine consequence appears in the example's normal-form table (actor, variable, sign, window), except the
  listed exceptions, each with its reason (an exception marked WRONG contradicts the handbook and is a known open problem);
- every table row is produced or listed, with its reason, in the NOT_PRODUCED groups.
The record of the run before any rule was changed is cases/<case>/out_of_sample.md.
"""
from pathlib import Path

from praxeo import parser
from praxeo.decider import FixtureDecider
from praxeo.pipeline import predict

import test_slice as TS

ROOT = Path(__file__).resolve().parents[1]
TS.WINDOW_QUALIFIERS.update({"Oct–Dec": "announcement", "February–August 2027": "announcement", "October to December 2027": "announcement"})


def _flat(groups):
    out = {}
    for reason, ids in groups:
        for rid in ids:
            assert rid not in out, rid
            out[rid] = reason
    return out


def _check(case, example, exceptions, groups, produced_expected, fixes=None, false_hits=()):
    """Run a case and compare it with its example's table. Returns (prediction, rows, produced row ids)."""
    d = ROOT / "cases" / case
    record = parser.parse_fixture(d / "record.json")
    pred = predict((d / "policy.txt").read_text(), record, FixtureDecider(d / "answers.json"))
    assert pred["citation_problems"] == [] and pred["verifier_problems"] == []
    rows = {rid: keys for rid, keys in TS._normal_form_rows(example).items() if rid != "—"}
    rows.update(fixes or {})  # rows whose cells the generic parser cannot split (prose actors, one sign per reading)
    table = set().union(*rows.values())
    got = TS._engine_keys(pred)
    assert got
    for key in got:
        assert key in table or key in exceptions, key
    assert got & set(exceptions) == set(exceptions)  # an exception that no longer occurs is removed
    not_produced = _flat(groups)
    produced = {rid for rid, keys in rows.items() if keys & got} - set(false_hits)  # false hits: the key is produced, for another meaning
    assert set(rows) - produced == set(not_produced)
    assert produced == set(produced_expected)
    return pred, rows, produced


WE002_NOT_PRODUCED = [
    ('SB-2, SB-3, SB-7, SB-8 and CR-9/CR-12: the spending of the earmark. The record has no subsidy component and the rule base has no SB rules (missing rules).',
     ['C-3', 'C-8', 'C-20', 'C-22', 'C-26', 'C-27']),
    ("OC-2 / RS-4: the search cost of the mobile buyers' trips. Not encoded (missing rule).",
     ['C-16']),
    ('RS-4 / RS-9: other groceries bought on the same trip. Missing rule. The key (retailers.lakeport, quantity_traded, decrease) is produced, but by OC-4 for the drinks, so the row is not counted.',
     ['C-11']),
    ("Actor: `producers` is not a role in the record; the engine's RS-5 row names the bound distributors and the buyers (missing record fact: the producers).",
     ['C-6']),
    ('RS-7 / SB-5: lobbying. The lobbying rules cover a tariff that is renewable or has relief applicants; nothing for a tax (missing rule).',
     ['C-9']),
    ('TX-3 / OC-5: employment and hours of the sellers as a group (and of those funded by the revenue). The labour group is encoded for a tariff only (missing rule).',
     ['C-12', 'C-23', 'C-24']),
    ('DM-1: `tax_share_borne` for subclasses (mobile and immobile buyers). Not encoded, and the record has no such subclasses (missing rule and record fact).',
     ['C-13']),
    ('SB-3, RS-6, CR-1 and CR-12b under U1: needs subsidy rules and reading facts (missing rule).',
     ['C-14']),
    ('Actor name: the engine produces tax_revenue increase, but for `officials.enforcement` (see the engine rows), not for the `town budget`.',
     ['C-25']),
    ('Variable: quantity_demanded of taxed drinks from all sources (TX-2 with RS-1 across the line). The tax rules sign quantity_traded only (missing rule).',
     ['C-28']),
]

WE010_NOT_PRODUCED = [
    ("RS-4: the tax revenue of the neighbouring jurisdictions. The record has no field for the authority across the line, and whether that authority taxes the good is a record fact (WE-002's neighbours do not) (missing record fact).",
     ['C-19']),
    ('RS-3: informal activity (bootlegging, smuggling) and its investment (TS-2). No evasion rule for taxes (missing rule).',
     ['C-4', 'C-5']),
    ("Actor: `producers` is not a role in the record; the engine's RS-5 rows name the agents and the smokers (missing record fact).",
     ['C-7']),
    ('RS-7: lobbying by border retailers, health groups and producers. No lobbying rule for a tax (missing rule).',
     ['C-10']),
    ("RS-9 / TX-3: untaxed trip goods and the border retailers' labour. Not encoded (missing rule), and the border subclass is not a role in the record.",
     ['C-12', 'C-13']),
    ('Actor: the border subclass `retailers.marren.border` is not a role in the record; the class-level row appears under `retailers.marren` (see the engine rows).',
     ['C-14']),
    ('DM-1: `tax_share_borne` for smokers and their subclasses. Not encoded (missing rule).',
     ['C-15', 'C-16', 'C-30']),
    ("RS-10: informal buyers' search cost, quality and information. Not encoded (missing rule).",
     ['C-17', 'C-18', 'C-28']),
    ("TX-10: other taxes' base (sales tax on trip goods, the tax on other tobacco). Not encoded (missing rule). The key (officials.enforcement, tax_revenue, increase) is produced for the cigarette tax, so C-29 is not counted.",
     ['C-20', 'C-29']),
    ("SB-7: the earmark's effect on the quit program. No SB rules (missing rule).",
     ['C-22']),
    ("OC-2: search cost of the border smokers' trips. Not encoded (missing rule).",
     ['C-26']),
    ("CR-8b / CR-12e: the general fund's recipients gain from the net revenue. Not encoded: the encoded OC-3 case names the payers, not the recipients (missing rule).",
     ['C-27']),
    ("SB-4: asset values of the retail sites on both sides of the line. The SB-4 rule covers a tariff's owners (missing rule for a tax; no owner role).",
     ['C-33', 'C-34']),
]

WE042_NOT_PRODUCED = [
    ("The drawback (K2) and the re-import rule (K3): a refund conditional on export is not an instrument the rule base has (SB-10, CR-1, CR-3, CR-8b/c, RS-19; missing rule and missing record fact). Includes every row on exporters' net cost, claims, the outlay and round trips.",
     ['C-4', 'C-13', 'C-14', 'C-15', 'C-16', 'C-17', 'C-18', 'C-23', 'C-46', 'C-47', 'C-49', 'C-50', 'C-51', 'C-52', 'C-57']),
    ("fabricators.mixed and total exports: need the drawback's shift from home to export sales (CR-4, CR-7a, CR-12e) and a class the record has no field for (missing record fact and rule).",
     ['C-19', 'C-20', 'C-36', 'C-56']),
    ('RS-8 / CR-10a: inventory_held. RS-8 signs quantity_traded only (missing rule).',
     ['C-10']),
    ('RS-1 / RS-16 / CR-6 / CR-9: the market for scrap and secondary aluminum (users turn to it, remelters supply it, its price). No substitute-market rule for a tariff and no remelter or scrap role (missing rules and record facts).',
     ['C-11', 'C-27', 'C-28', 'C-29', 'C-53']),
    ("Actor name: produced under workers.users_home_finished / owners.users_home_finished (see the engine rows); the table's actor is the prose `users.home.finished (workers)` / `(owners)`.",
     ['C-22', 'C-32']),
    ("RS-14 / RS-16 / CR-9: the foreign sellers' side of the switch to untaxed finished goods. The rule base signs the buyers' quantity_substitute only (missing rule).",
     ['C-25']),
    ("RS-4 for a tariff: Ostrel's fabricators supply Vessland buyers. No neighbour role and no rule (missing rule and record fact); the capital-move rule signs capital_stock_target instead.",
     ['C-26']),
    ("Variable: C-30 states the smelters' electricity as quantity_traded; the engine's CR-9 rule gives quantity_demanded (the same claim; see the engine rows).",
     ['C-30']),
    ("RS-14 for goods with no close imported substitute: the buyers' price rises only where competitors face the same cost, but the record's one downstream group has competitors exempt; the second group (A-16) needs a second Downstream entry that I did not write because the table's classes `users.home` and `buyers.aluminum_goods` coincide (missing record fact).",
     ['C-33']),
    ('CR-9 / CR-6: foreign buyers and regional parts makers on the other side of the export shift. Not encoded (missing rule).',
     ['C-34', 'C-55']),
    ('TX-8 with the 0.9 clause on a change in the form of imports: the engine produces a decrease, the table says ambiguous. Counted as not produced; the engine row is WRONG.',
     ['C-35']),
    ('DM-1: `tax_share_borne`. Not encoded (missing rule).',
     ['C-38', 'C-39']),
    ("CR-8b / CR-8d: the general fund's net receipts and their recipients (a group). Not encoded; the encoded OC-3 case names the payers (missing rule).",
     ['C-42']),
    ("OC-3, fixed-budget case with CR-6/CR-8a: customs users' waiting times as a group. The rule base derives nothing for a fixed budget (missing rule).",
     ['C-44']),
    ('CR-7c / CR-10c: the asset value of holders of stocks at the effective date. No rule and no holder role (missing rule and record fact).',
     ['C-48']),
]

WE046_NOT_PRODUCED = [
    ("The residents' discount (K2) and the goods operators as bound classes: the record has one bound class (missing record fact: a second tax component and its classes, or a role per bound class).",
     ['C-2', 'C-20', 'C-62', 'C-65', 'C-66', 'C-67']),
    ('CR-9 `shared_facility` (Tier C): speeds, crowding and travel times through the roads, and what follows from them. No such rule (missing rule).',
     ['C-5', 'C-16', 'C-30', 'C-32', 'C-38', 'C-39', 'C-41', 'C-45', 'C-49', 'C-51', 'C-53', 'C-60', 'C-63', 'C-68']),
    ("RS-1 / RS-16 / CR-4: switching to bus, Ringside parking, ride-hail or the ring road, and the substitutes' prices and supply. No substitute-market rule for a tax (missing rule).",
     ['C-7', 'C-8', 'C-9', 'C-10', 'C-11', 'C-12', 'C-61']),
    ('RS-8 as retiming: trips move to evenings and weekends. RS-8 as encoded brings purchases forward before the start only (missing rule).',
     ['C-13', 'C-14']),
    ('CR-3a / CR-4: travel_time of the diverted and the switching drivers. Variable not derived (missing rule).',
     ['C-15', 'C-50']),
    ('RS-3: legal_breach (evasion, false short-visit claims). No evasion rule for taxes (missing rule).',
     ['C-18', 'C-24']),
    ('RS-7: lobbying on questions that exist only under the ordinance. No lobbying rule for a tax (missing rule).',
     ['C-19']),
    ('U1 (short visits): reclassification, quantity and compliance of delivery visits, and the full cost of a van-day. Needs reading facts and a rule on reshaping rounds (missing rule and reading facts).',
     ['C-21', 'C-22', 'C-23', 'C-44', 'C-47']),
    ('RS-4 / RS-6 / RS-9 / CR-7a: shoppers, zone businesses and Ringside businesses. No cross-border or location rule for a tax (missing rule).',
     ['C-25', 'C-26', 'C-27', 'C-28', 'C-29', 'C-31', 'C-33', 'C-34']),
    ("RS-12 / CR-7c: the parking garages' prices and values. Not encoded (missing rule).",
     ['C-35', 'C-36', 'C-37']),
    ('K3 earmark to bus services: SB-7, CR-8d and what follows (service, employment, headways, input orders). No SB rules and no earmark component (missing rule and record fact).',
     ['C-40', 'C-42', 'C-43', 'C-54', 'C-70']),
    ('Variable `full_cost_per_unit` (CR-1, CR-3): not derived by the tax rules (missing rule).',
     ['C-48']),
    ("RS-22: wage_rate and employment of the zone's employers. Not encoded (missing rule).",
     ['C-52']),
    ('TX-1 for the classes that keep paying (drivers.keep, residents.zone, goods operators). The engine signs the whole class drivers.nonresident instead (see the engine rows); the subclasses are not roles in the record.',
     ['C-55']),
    ('OC-3 for the Adjudication Office, fixed budget: waiting times as a group. Nothing derived for a fixed budget (missing rule).',
     ['C-58']),
    ('CR-4c: transaction_size (drops per charged van-day). Variable not derived (missing rule).',
     ['C-64']),
    ('CR-8a / CR-12g: the city reserves tied up by the set-up advance. Not encoded (missing rule and record fact).',
     ['C-69']),
    ('CR-9 / CR-4b: non-tax receipts (zone parking fines) fall. Not encoded (missing rule).',
     ['C-71']),
]

WE062_NOT_PRODUCED = [
    ("Actor name: the announcement-window purchases (C-15) are produced for `packaging_users`, not for the table's `liable firms well above 10 t`, a class the record does not have.",
     ['C-15']),
    ("TX-5 / OC-2: compliance cost. Produced for `converters` (an exception), not for the table's `liable firms`; the redesign cost of C-51 is not encoded (missing rule).",
     ['C-20', 'C-51']),
    ("K2 and U1 (recycled content): product_attribute, the cut-back above 30%, combining output to average content, the single-product film makers' share, the documented converters' sales. RS-5 and CR-12 over a notch; needs reading facts and rules (missing rule).",
     ['C-4', 'C-6', 'C-7', 'C-57', 'C-65']),
    ('RS-21: weight per component. Not encoded (missing rule).',
     ['C-8']),
    ('RS-1 / RS-16: board, glass and loose produce as substitutes, their prices and capacity, and other buyers of them. No substitute-market rule for a tax and no substitute roles in the record (missing rule and record fact).',
     ['C-10', 'C-11', 'C-43', 'C-62', 'C-63', 'C-66', 'C-45']),
    ('K3 (threshold): RS-17 notch effects on firms near 10 t, small importers and direct importing. No rule (missing rule).',
     ['C-12', 'C-13', 'C-14', 'C-18', 'C-37', 'C-55']),
    ("RS-8 with its second window and inventory: January to March fall, inventory held, converters' labour in the late-2027 window. RS-8 as encoded gives the rush only (missing rule).",
     ['C-16', 'C-17', 'C-59']),
    ('RS-3: legal_breach and penalty receipts (misdeclared content or weight). No evasion rule for taxes (missing rule).',
     ['C-19', 'C-58']),
    ('RS-7: lobbying on U1 and the rules. No lobbying rule for a tax without renewal (missing rule).',
     ['C-21']),
    ('TS-2 / CR-7a / CR-10a: investment targets of converters, recyclers and substitute makers. Not encoded for these roles (missing rule and record fact).',
     ['C-22', 'C-23', 'C-24', 'C-25']),
    ('CR-9 / CR-6: the recycled-resin and virgin-resin markets, bales and municipalities, and the certifiers. No input-market rules, no such roles (missing rules and record facts).',
     ['C-26', 'C-27', 'C-28', 'C-29', 'C-30', 'C-31', 'C-32', 'C-33', 'C-34', 'C-46']),
    ("SB-4 / CR-7c: asset values of converters' owners, recyclers' owners, substitute owners and the other plants. SB-4 is encoded for a tariff's owners only (missing rule and record fact).",
     ['C-41', 'C-42', 'C-68']),
    ('RS-6 / RS-14 / TX-8 / RS-4: the exporters and the currency chain. The exporter rules are encoded for a tariff; a tax on packaging has no exporter role in the record (missing rule and record fact).',
     ['C-38', 'C-39', 'C-40', 'C-60', 'C-61']),
    ('TX-3 / OC-5: labour of the converters (ambiguous) and of recyclers and substitute makers. Not encoded for these roles (missing rule and record fact).',
     ['C-44']),
    ('DM-1: `tax_share_borne`. Not encoded (missing rule).',
     ['C-52']),
    ('CR-12b: imported packaged goods, ambiguous. No rule forms it (missing rule).',
     ['C-53']),
    ("TX-2 on the other sellers: foreign converters' price before tax and the volume of empty imports (importers, foreign sellers). The record has one seller class and the tax rules sign the bound actor and the OC-4 sellers only (missing record fact).",
     ['C-54', 'C-64']),
    ("CR-8 / CR-12e: the net receipt's recipients as a group (C-67). Not encoded (missing rule).",
     ['C-67']),
]


# ---------------------------------------------------------------- WE-002

WE002_EXCEPTIONS = {
    ("buyers.lakeport", "reclassification", "increase", None):
        "TX-4 with RS-5: the buyers' side of the switch to exempt formulations; C-6 puts it with `producers`, C-5 as quantity_substitute",
    ("distributors", "reclassification", "increase", None):
        "RS-5 for the bound actor; C-6 names `producers`, a role the record does not have",
    ("distributors", "quantity_traded", "decrease", None):
        "TX-2: the bound distributors deliver less taxed drink; the table lists the buyers' side (C-2, C-28)",
    ("officials.enforcement", "tax_revenue", "increase", None):
        "TX-1: C-25 gives it to the `town budget`; the record's revenue_actor is `officials.enforcement`",
}


def test_consistent_with_worked_example_we002():
    pred, rows, produced = _check(
        "we002_lakeport", "WE-002_drinks_excise.md", WE002_EXCEPTIONS, WE002_NOT_PRODUCED,
        produced_expected={"C-1", "C-2", "C-4", "C-5", "C-7", "C-10", "C-15", "C-18", "C-21"},
        false_hits={"C-11"})  # (retailers.lakeport, quantity_traded, decrease) is OC-4's drinks, not C-11's other groceries
    assert len(rows) == 26
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"] if c["reported"]}
    # changes made after the first out-of-sample run: TX-3 (substitutes), TX-4 (crossing), TX-5 (compliance), OC-3 split
    assert {s["rule"] for s in by[("buyers.lakeport", "quantity_substitute")]["derivation"]} >= {"TX-3", "RS-1"}
    assert {s["rule"] for s in by[("buyers.lakeport.mobile", "cross_border_purchases")]["derivation"]} >= {"TX-4"}
    assert by[("distributors", "compliance_cost")]["tier"] == "A"
    assert not any(c["actor_class"] == "taxpayers" and c["reported"] for c in pred["consequences"])  # own revenue pays (OC-3)


# ---------------------------------------------------------------- WE-010

WE010_EXCEPTIONS = {
    ("retailers.marren", "net_price_received", "decrease", None):
        "TX-2 with sellers_bear (A-3): the handbook signs it for the border retailers only (C-14); interior retailers are not contradicted",
    ("retailers.marren", "resources_available_other_uses", "decrease", None):
        "TX-1 for the side that bears part of the tax; follows from the row above",
    ("smokers", "reclassification", "increase", None):
        "RS-5 for the buyer side of the definition line; C-6 records the switch as quantity_substitute, C-7 as the producers' reclassification",
    ("stamping_agents", "quantity_traded", "decrease", None):
        "TX-2: the bound agents stamp fewer packs; the table lists the retailers (C-2) and the smokers (C-25)",
    ("stamping_agents", "reclassification", "increase", None):
        "RS-5 for the bound actor; C-7 names `producers`, a role the record does not have",
}


def test_consistent_with_worked_example_we010():
    pred, rows, produced = _check(
        "we010_marren", "WE-010_cigarette_tax_border.md", WE010_EXCEPTIONS, WE010_NOT_PRODUCED,
        produced_expected={"C-1", "C-2", "C-3", "C-6", "C-8", "C-9", "C-11", "C-21", "C-24", "C-25", "C-31", "C-32"},
        false_hits={"C-29"})  # (officials.enforcement, tax_revenue, increase) is the cigarette tax (C-31), not the other tobacco (C-29)
    assert len(rows) == 33
    by = {(c["actor_class"], c["variable"], c["window"]): c for c in pred["consequences"] if c["reported"]}
    # TX-1 (1.1): a rise in the rate of an existing tax yields more revenue only if the base holds: Tier B with that premise (A-16)
    rev = by[("officials.enforcement", "tax_revenue", None)]
    assert rev["tier"] == "B" and rev["assumptions"] == ["revenue_base_holds(k1)"]
    assert by[("smokers", "quantity_traded", "announcement")]["horizon"] == ["short"]  # C-8, the same RS-8 rule as WE-013 C-8
    assert by[("stamping_agents", "compliance_cost", None)]["tier"] == "A"


# ---------------------------------------------------------------- WE-042

WE042_EXCEPTIONS = {
    ("buyers.aluminum_goods", "quantity_substitute", "increase", None):
        "RS-1 with substitute_supply_expands: buyers turn to the tariff-free imported finished goods; the table has the sellers' side (C-25)",
    ("importers", "resources_available_other_uses", "decrease", None):
        "TX-1 for a tariff, as WE-013 C-26 signs it; WE-042 signs the variable only for the classes that keep paying (C-41)",
    ("input_suppliers", "quantity_demanded", "increase", None):
        "CR-9 derived demand; C-30 states the same claim under quantity_traded",
    ("owners.users_home_finished", "asset_value", "decrease", None):
        "SB-4; C-32's actor is the prose `users.home.finished (owners)`",
    ("users.home.finished", "capital_stock_target", "decrease", None):
        "RS-4 / TS-1: squeezed users move capital out (A-23); the table has the Ostrel side of the shift (C-26)",
    ("users.home.finished", "lobbying_effort", "increase", None):
        "RS-7 for the harmed users; C-24 lists `users.home`, of which these are the squeezed part",
    ("workers.users_home_finished", "employment", "at_least_one_decrease", None):
        "RS-6 labour group; C-22's actor is the prose `users.home.finished (workers)`",
    ("workers.users_home_finished", "hours_worked", "at_least_one_decrease", None):
        "RS-6 labour group (second member); see above",
    # WRONG: contradict the handbook. C-35 signs the exports `ambiguous` (TX-8, 0.9: a change in the form of imports makes the
    # currency chain ambiguous unless a premise says which dominates). WE-013 C-19, built under the earlier catalog, signs the
    # same chain a decrease with the same pattern present (reshaping, imported finished goods), so TX-8 is not changed here.
    ("export_industries.other", "quantity_supplied", "decrease", None):
        "WRONG: C-35 says ambiguous (TX-8 0.9 clause on a change in the form of imports); TX-8 as encoded has no such clause",
    ("workers.export_industries.other", "employment", "at_least_one_decrease", None):
        "WRONG: the labour group of the same TX-8 chain, ambiguous for the same reason",
    ("workers.export_industries.other", "hours_worked", "at_least_one_decrease", None):
        "WRONG: as above (second member)",
}


def test_consistent_with_worked_example_we042():
    fixes = {"C-24": {("smelters", "lobbying_effort", "increase", None), ("users.home", "lobbying_effort", "increase", None),
                      ("exporters", "lobbying_effort", "increase", None)}}
    pred, rows, produced = _check(
        "we042_vessland", "WE-042_aluminum_tariff_drawback.md", WE042_EXCEPTIONS, WE042_NOT_PRODUCED,
        produced_expected={"C-1", "C-2", "C-3", "C-5", "C-6", "C-7", "C-8", "C-9", "C-12", "C-21", "C-24", "C-31", "C-37", "C-40",
                           "C-41", "C-43", "C-45", "C-54"},
        fixes=fixes)
    assert len(rows) == 57
    wrong = [k for k, why in WE042_EXCEPTIONS.items() if why.startswith("WRONG")]
    assert len(wrong) == 3
    by = {(c["actor_class"], c["variable"], c["window"]): c for c in pred["consequences"] if c["reported"]}
    assert by[("users.home", "quantity_traded", "announcement")]["horizon"] == ["short"]  # C-9, RS-8 as in WE-013 C-8
    assert by[("importers", "compliance_cost", None)]["tier"] == "A"  # C-45 (TX-5)


# ---------------------------------------------------------------- WE-046

WE046_EXCEPTIONS = {
    ("businesses.zone", "quantity_demanded", "decrease", None):
        "CR-4c with RS-14: businesses whose delivery price rises take fewer deliveries; the table has their sales (C-27, C-28)",
    ("drivers.nonresident", "quantity_substitute", "increase", None):
        "TX-3 with RS-1 for the class; the table has its parts, drivers.switch (C-7, C-10) and drivers.through (C-61)",
    ("drivers.nonresident", "resources_available_other_uses", "decrease", None):
        "TX-1 for the class that pays; C-55 signs it for the subclasses that keep paying (the record does not split the class by response)",
}


def test_consistent_with_worked_example_we046():
    pred, rows, produced = _check(
        "we046_calderford", "WE-046_congestion_charge.md", WE046_EXCEPTIONS, WE046_NOT_PRODUCED,
        produced_expected={"C-1", "C-3", "C-4", "C-6", "C-17", "C-46", "C-56", "C-57", "C-59"},
        fixes={"C-46": {("businesses.zone", "price_paid", "increase", None)}})  # one sign under both readings of U1
    assert len(rows) == 71
    # a road charge has no private seller (seller_actor null): no sellers.current row, which the first run wrongly produced
    assert not any(c["actor_class"] == "sellers.current" for c in pred["consequences"])
    assert "\nseller(k1" not in pred["engine_facts"]


# ---------------------------------------------------------------- WE-062

WE062_EXCEPTIONS = {
    ("converters", "compliance_cost", "increase", None):
        "TX-5: C-20's actor is `liable firms`, the converters and importers of the record",
    ("converters", "resources_available_other_uses", "decrease", None):
        "TX-1 for the side that bears part of the tax (sellers_bear); WE-062 signs the variable only for those who keep paying (C-47)",
    ("packaging_users", "quantity_traded", "increase", "announcement"):
        "RS-8: C-15's actor is `liable firms well above 10 t`, who buy and import packaging",
}


def test_consistent_with_worked_example_we062():
    fixes = {"C-47": {("packaging_users", "resources_available_other_uses", "decrease", None),
                      ("importers.packaging", "resources_available_other_uses", "decrease", None)}}
    pred, rows, produced = _check(
        "we062_saldria", "WE-062_plastic_packaging_tax.md", WE062_EXCEPTIONS, WE062_NOT_PRODUCED,
        produced_expected={"C-1", "C-2", "C-3", "C-5", "C-9", "C-35", "C-36", "C-47", "C-48", "C-49", "C-50", "C-56"},
        # (converters, quantity_traded, decrease) is the packaging, not C-32's virgin resin; (converters, compliance_cost) is TX-5,
        # not C-51's redesign and qualification cost. C-49 is produced as the gross revenue: the table's is net of the appropriation.
        fixes=fixes, false_hits={"C-32", "C-51"})
    assert len(rows) == 68
    # OC-3, third funding case: the Act's unit is paid from the general budget that receives the tax, so no row names the taxpayers
    # as payers (the first run did, against C-67); the budget (revenue) and the Revenue Service (cost) are different actors
    assert not any(c["actor_class"] == "taxpayers" for c in pred["consequences"])
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"] if c["reported"]}
    assert ("state budget", "tax_revenue") in by and ("officials.enforcement", "enforcement_cost") in by
    assert ("state budget", "enforcement_cost") not in by


def test_open_problem_rows_are_not_hidden():
    """The rows of the five examples the engine still gets wrong (WE-042's TX-8 chain) stay listed; when a rule change fixes
    them the exception is removed and this count goes down."""
    assert sum(why.startswith("WRONG") for why in WE042_EXCEPTIONS.values()) == 3
    for ex in (WE002_EXCEPTIONS, WE010_EXCEPTIONS, WE046_EXCEPTIONS, WE062_EXCEPTIONS):
        assert not any(why.startswith("WRONG") for why in ex.values())
