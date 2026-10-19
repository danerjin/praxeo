"""Out-of-sample run of the quota rules (praxeo/rules/licensing.lp: EN-6, EN-12, EN-13) on WE-047, a tariff-rate quota.

EN-6 was written from the catalog text, EN-12 and EN-13 from WE-028 only; the tariff chains (taxes.lp, spillovers.lp) from
the tariff examples. Same shape as tests/test_oos_we028.py: every reported engine consequence is a row of the example's
consequence list (key: actor class, variable, sign, window) or sits in EXCEPTIONS with its reason (prefixed "KNOWN WRONG:"
when it contradicts the example); every table row the engine does not produce sits in NOT_PRODUCED with the reason. The
record and answers are in cases/we047_kestrany/, the write-up in cases/we047_kestrany/out_of_sample.md. Nothing under
praxeo/ was changed for this run.

The record has three components: k1 `tariff` (the 60% out-of-quota rate), k2 `quota` (`import_quota`, the 400,000 t at 2%,
transferable, allocated by history before the announcement) and k3 `rights_allocation` (no rules). U1 is recorded with
`reading_fields` on k2 (U1-a: `relief_applicant_actor`, the applicants for surrendered tonnes).
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE47 = ROOT / "cases" / "we047_kestrany"

# the table's "applicants" are the registered importers who apply under U1-a (the record's relief applicants, importers.new);
# its bare "importers" are the licence holders; "lobbying groups" are the four groups the row names, as the record's roles
SHORT = {
    "applicants": "importers.new",
    "importers": "importers.history",
    "lobbying groups": ["importers.history", "mills.domestic", "buyers.industrial", "importers.new"],
    "recipients of other spending": "recipients.other_spending",
    "future taxpayers": "taxpayers.future",
}
WINDOWS = {"March–December 2026": "announcement", "31 December 2026": "announcement"}
EXCEPTIONS = {
    ("buyers.household", "quantity_traded", "increase", "announcement"):
        "RS-8 (stockpile_ahead) on the record's one buyer role; C-18 and C-19 put the 2026 stocking on importers and food manufacturers (buyers.industrial)",
    ("buyers.household", "reclassification", "increase", None):
        "RS-5 on the tariff's buyer role; C-23 puts the reclassification of sugar mixtures on importers",
    ("export_industries", "quantity_supplied", "decrease", None):
        "KNOWN WRONG: TX-8 alone; C-31 is ambiguous because a further (+) chain runs through the currency (CR-9, CR-12) and A-21 and A-8 decide the net",
    ("workers.export_industries", "employment", "at_least_one_decrease", None):
        "KNOWN WRONG: the workers of C-31's industries; follows the export fall of TX-8, where C-31 is ambiguous",
    ("workers.export_industries", "hours_worked", "at_least_one_decrease", None):
        "KNOWN WRONG: as above",
    ("importers.history", "capital_stock_target", "decrease", None):
        "EN-13 (consolidation, long run): fewer importing firms, less import capital; the table counts importers (C-10) and does not sign their capital",
    ("importers.history", "net_price_received", "increase", None):
        "EN-6 for holders when the price is not set in a wider market: the importers sell at the higher domestic price (the quota rent, C-8's other side); the table signs the lease price and the share value, not the importers' selling price",
    ("importers.history", "resources_available_other_uses", "decrease", None):
        "TX-1 puts the 60% on the tariff's bound importers (CR-8b); under TX-7 at the marginal rate the buyers bear it (C-5) and the holders gain the rent (C-3, C-35, C-46 ambiguous for refiners); defensible only for the importers above their licence (C-2)",
    ("importers.new", "lobbying_effort", "U1-a: increase; U1-b: no_change", None):
        "RS-7 for the applicants for surrendered tonnes under U1-a (per reading: U1-a increase, U1-b none); C-26 signs would-be importers' lobbying without readings",
    ("input_suppliers", "quantity_demanded", "increase", None):
        "CR-9 on the domestic sellers' inputs; C-36 has the same content under quantity_traded (beet inputs)",
    ("officials.enforcement", "tax_revenue_vs_static_projection", "decrease", None):
        "TX-9 on the 60% rate; the table's C-40 signs tax_revenue itself, which needs the base to fall below 200,000 t (A-25)",
    ("taxpayers", "resources_available_other_uses", "decrease", None):
        "OC-3 with OC-1 as a single payer: the record sets no general budget (the licence office's funding is not stated), so no group of taxpayers, recipients of other spending and future taxpayers is formed (C-41, C-43, C-51)",
}
NOT_PRODUCED = {
    "C-1": "missing record fact and rule: the in-quota rate (2% in place of 25%) has no field and TX-2 is applied to the rise only; no rule for a cut at the inframarginal rate (CR-1 operation 3 either side of a threshold)",
    "C-2": "missing rule and role: the out-of-quota landed cost (60%) as price_paid of the importers; TX-1 puts the tariff on the bound role as resources_available, not price_paid",
    "C-9": "missing rule and role: EN-13's lessors (small holders) quantity_traded; EN-13 signs the remaining importers' quantity_supplied, not the licences leased or sold",
    "C-11": "missing rule: CR-4 entry_rate under a quota that is allocated to history and tradable (EN-6 signs entry only for seller_cap); no question for A-25",
    "C-12": "missing rule: EN-12 (newcomers, U1-a) has no entry_rate row; only the RS-15 relief rows fire",
    "C-15": "missing record fact and rule: K4 (surrender of licences unused by 30 September) has no component or instrument; RS-8 inventory_held before a dated removal of an option (CR-10a) is not encoded",
    "C-17": "missing record fact and rule: as C-15 (RS-8 with CR-12b for January to September imports)",
    "C-18": "missing rule: RS-8 for the importers' purchases before the effective date is encoded for the buyers only (the engine's row is on buyers.household); no importers role in the window",
    "C-19": "missing rule: RS-8 inventory_held (stocks on 31 December 2026) is not encoded",
    "C-20": "missing rule: CR-4c / TX-2 signs quantity_traded and OC-4's purchases not made, not quantity_demanded of the buyers",
    "C-21": "missing rule: RS-1 / RS-16 for sweeteners as substitutes of an input (A-12); the substitute question exists for the goods of exempt competitors only",
    "C-22": "missing rule and role: RS-16 for the price of glucose syrup; no sellers.substitutes role in the record",
    "C-24": "missing rule: RS-21 (high-grading under a cap in physical units) is not encoded for import quotas; no product_attribute variable",
    "C-25": "missing rule and role: CR-9 / RS-21 for the refiners; no refiners.port role in the record",
    "C-31": "missing rule and combiner: TX-8 gives the decrease only, and the further (+) chain through the currency (CR-9, CR-12) is not encoded; the engine's row is KNOWN WRONG",
    "C-32": "missing record fact and rule: owners of beet land as asset owners (SB-4) exist for subsidies only (`asset_owner_actor`); `domestic_seller_owner_actor` is the mills' owners",
    "C-35": "missing role and rule: no owner role for the importing firms (CR-7c claims before creation); the holders' asset_value is the shares (C-3)",
    "C-36": "missing variable: CR-9 signs quantity_demanded of the inputs; the table's quantity_traded (beet inputs) is the same content under another name",
    "C-40": "missing variable: TX-9 gives tax_revenue_vs_static_projection; tax_revenue itself needs A-25 (out-of-quota imports below 200,000 t) as a premise",
    "C-41": "missing record fact: the payer group (taxpayers, recipients of other spending, future taxpayers) needs general_budget, which the text does not state; the engine has taxpayers alone",
    "C-43": "same as C-41 (licence office funding, A-27)",
    "C-46": "missing role and rule: no owners.importers role; CR-7c / CR-12b for the firms as a whole",
    "C-47": "missing rule: RS-8 for tariff revenue in the window (higher imports at 25%) is not encoded",
    "C-50": "missing rule: CR-8b for the registration and transfer fees as the licence office's receipts (OC-1) is not encoded for quotas",
    "C-51": "same as C-41, with the fees (A-32)",
    "C-52": "missing rule and role: CR-6 / CR-9 for the world price (fewer imports lower foreign demand); no foreign net_price_received row for a tariff or import quota",
    "C-53": "missing rule: RS-8 with CR-6 for the world price in the window",
    "C-54": "missing record fact and rule: port warehouses as complements (RS-12, CR-9) are not in section 1; `related` is read for taxes and subsidies on the good's own complements",
}
PRODUCED = {"C-3", "C-4", "C-5", "C-6", "C-7", "C-8", "C-10", "C-13", "C-14", "C-16", "C-23", "C-26", "C-27", "C-28", "C-29", "C-30", "C-33", "C-34", "C-37", "C-38", "C-39", "C-42", "C-44", "C-45", "C-48", "C-49"}


def test_consistent_with_worked_example_we047():
    pred, keys = _engine(WE47)
    rows = _rows("WE-047_sugar_tariff_rate_quota.md", SHORT, WINDOWS, {})
    assert len(rows) == 54
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    # a quota rate and a tariff rate both run: the price rows come from the import quota taking the tariff chains (EN-6) and from k1
    assert ("buyers.household", "price_paid", "increase", None) in keys
    # EN-12: the base period (2023 to 2025) ended before the bill was published, so a windfall, not a race
    assert ("importers.history", "investment_target", "increase", "announcement") not in keys
    assert ("importers.history", "asset_value", "increase", None) in keys
    # EN-6: the price is not set in a wider market here, so the holders' lease price is not signed by EN-6 itself (C-8 comes from EN-13)
    by = {(c["actor_class"], c["variable"]): c for c in pred["consequences"]}
    lease = by[("importers.history", "right_lease_price")]
    assert any(d["rule"] == "EN-13" for d in lease["derivation"])
    # U1 is per reading only where U1-a adds the applicants (reading_fields); the rows for them differ by reading
    assert by[("importers.new", "compliance_cost")]["sign_by_reading"] == {"U1-a": "increase", "U1-b": "none"}
