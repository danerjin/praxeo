"""Out-of-sample run of the quota rules (praxeo/rules/licensing.lp, EN-6) on WE-014, the sugar import quota.

The quota rules were written from EN-6's text alone, without any example; this is their first comparison with one. The
run, the classification of every row and the general gaps are in cases/we014_calvar/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE14 = ROOT / "cases" / "we014_calvar"

# The table's name for export industries is a label; the record keeps the engine's default roles (the text names no exporters),
# and the group row C-33 is on their workers.
SHORT = {"exporters.calvar": ["export_industries", "workers.export_industries"]}
WINDOWS = {"announcement window": "announcement"}
EXCEPTIONS = {
    ("importers", "capital_stock_target", "decrease", None):
        "EN-13 (consolidation under tradable rights, added after the first run): the rights are transferable and holders differ; the example does not apply EN-13",
    ("importers", "number_of_sellers", "decrease", None):
        "EN-13 (consolidation under tradable rights, added after the first run): the rights are transferable and holders differ; the example does not apply EN-13",
    ("quota_holders", "right_lease_price", "increase", None):
        "EN-13 (consolidation under tradable rights, added after the first run): the rights are transferable and holders differ; the example does not apply EN-13",
    ("importers", "reclassification", "increase", None):
        "RS-5 through the tariff chain (EN-6 as TX-7, added after the first run): blends at 65% sugar or less (A-8); the table records the reshaping as the trade in blends (C-9)",
    ("buyers.sugar", "reclassification", "increase", None):
        "RS-5, as above (buyers who import blends)",
    ("growers.beet", "lobbying_effort", "increase", None):
        "RS-7 through the tariff chain: the protected domestic sellers lobby for renewal at the five-year review (A-21); the table names the quota holders (C-12)",

    ("importers", "quantity_traded", "decrease", None):
        "EN-6 on the bound role `importers` (all importers, from the text); C-1 names the subclass quota_holders (base-period importers, section 3) and the foreign sellers",
    ("quota_holders", "net_price_received", "increase", None):
        "EN-6: holders of the rights receive the domestic price on the quota tonnes; the table records the same gain as the value of the shares (C-5) and as the division of the gap (section 7, DM-4)",
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-3 with OC-1, general budget and no tax named: the payers are a group (taxpayers, recipients of other spending, future taxpayers); C-29 signs taxpayers alone on A-22",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None): "member of the OC-1 payer group (see above)",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None): "member of the OC-1 payer group (see above)",
}
NOT_PRODUCED = {
    "C-1": "naming and missing role: the bound role is `importers`, not the base-period subclass quota_holders; foreign sellers have no role for a quota (foreign_seller_actor is a tariff field, OC-4 is not encoded for quotas)",
    "C-6": "RS-8 is not encoded for quotas: no bring-forward of imports into the window before an allocation by past imports, and no question for it",
    "C-7": "missing rule: SB-4 with EN-6 for entry under tradable rights (a new seller must buy or lease shares); entry_rate is signed only for a cap on the number of sellers",
    "C-8": "RS-1 is encoded for tariffs and licensing only; the substitute sweeteners and their users have no quota role",
    "C-9": "RS-5 for a quota: `definition_line` is set, but no quota rule uses it and no question follows",
    "C-10": "RS-14 and RS-4 for quotas: `downstream` is not read for quotas (and section 1 names no sweetened-goods makers)",
    "C-11": "RS-4 for quotas: no neighbour or mobile-buyer role for quotas (section 1 gives the 10 kg allowance and Varnholt)",
    "C-13": "RS-1 not encoded for quotas (see C-8)",
    "C-14": "RS-1 with LW-4 not encoded for quotas (see C-8)",
    "C-15": "missing record fact (section 1 names no landowners) and rule: SB-4 for the owners of the domestic sellers' factor, as TX-7 has for tariffs (domestic_seller_owner_actor), is not wired to quotas",
    "C-16": "RS-14 not read for quotas (see C-10); EN-6 gives no price for goods made with the sugar",
    "C-17": "RS-14, RS-6 and RS-4 for quotas (see C-10)",
    "C-18": "CR-9 for the input chain: the refineries' cane is an input_to relation, and `related` and input_supplier_actor are not read for quotas",
    "C-19": "RS-6 for the refineries' workers (see C-18)",
    "C-20": "RS-4 and RS-9 for quotas: no neighbour role (see C-11)",
    "C-21": "same",
    "C-22": "RS-4 for quotas: foreign makers of the sweetened goods have no role",
    "C-26": "OC-1 with LW-4: the crops the land would have grown; no rule for the domestic sellers' expansion drawing resources, no buyers.field_crops role",
    "C-28": "OC-2 is not encoded (also absent in WE-067): the cost of registering and trading shares",
    "C-29": "sign form: the engine signs the OC-1 payer group (at_least_one_decrease over taxpayers, other spending, future taxpayers); the table signs taxpayers alone",
    "C-30": "CR-9 with LW-4: domestic_seller_worker_actor is read by the tariff rules (TX-7) but not by quotas; section 1 names no beet-factory workers",
    "C-31": "RS-6 and TS-1 for the refineries' capacity (see C-18)",
    "C-32": "OC-1 with CR-8c for the cost of reshaping into blends (see C-9)",
}
PRODUCED = {"C-2", "C-3", "C-4", "C-5", "C-12", "C-23", "C-24", "C-25", "C-27", "C-33", "C-34"}


def test_consistent_with_worked_example_we014():
    pred, keys = _engine(WE14)
    rows = _rows("WE-014_sugar_import_quota.md", SHORT, WINDOWS, {})
    assert len(rows) == 34
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
