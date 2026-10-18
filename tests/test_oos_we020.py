"""Out-of-sample run of the subsidy rules (praxeo/rules/subsidies.lp) on WE-020, an example they were not written from.

Same shape as tests/test_subsidies.py::test_consistent_with_worked_example_we019: every reported engine consequence is a row
of the example's consequence list (key: actor class, variable, sign, window; a group gives one key per member) or sits in
a dict of exceptions with its reason; every table row the engine does not produce sits in a dict with the reason. The
rules, schema and questions were not changed for this run. Report: cases/we020_tamberlay/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE20 = ROOT / "cases" / "we020_tamberlay"

SHORT = {"owners": "owners.entry_level"}
# C-10 is the rush before the end of the window: its key would otherwise equal C-2's, so it gets a window no engine
# consequence has (the engine has no deadline rule)
WINDOWS = {"March to June": "announcement", "before end of Year 4": "deadline"}
EXCEPTIONS = {
    ("owners.entry_level", "net_price_received", "increase", None):
        "SB-2 with DM-1: the sellers' side of the capitalization (C-11, C-28); the table records the asset value and the share",
    ("owners.entry_level", "quantity_traded", "increase", None):
        "SB-2: the sellers' side of C-2 (an exchange has two sides); the table signs the buyers' side only",
    ("taxpayers", "resources_available_other_uses", "at_least_one_decrease", None):
        "OC-1, who pays (catalog 1.4): no tax is named, so the payers are a group over taxpayers, recipients of other spending and future taxpayers (at_least_one_decrease); WE-020, written before the clause, signs taxpayers alone (C-24)",
    ("recipients.other_spending", "resources_available_other_uses", "at_least_one_decrease", None): "member of the OC-1 group (see above)",
    ("taxpayers.future", "resources_available_other_uses", "at_least_one_decrease", None): "member of the OC-1 group (see above)",
}
NOT_PRODUCED = {
    "C-4": "RS-8 is encoded for the recipients' delay only; the sellers holding back listings (TS-2) has no rule and no question",
    "C-6": "SB-5 with RS-5 signs the recipients' reclassification only; value moved outside the price by sellers just above a price cap has no rule, and the record has no field for a price threshold",
    "C-10": "RS-8's deadline form (buyers sign earlier because renewal is uncertain, A-16) is not encoded; the engine has the announcement delay and the after-expiry dip only",
    "C-14": "no rule and no role: the new-supply response of builders (LW-4, TS-1); the record has one seller role and the owners already fill it",
    "C-15": "same (RS-5 for builders pricing just under the cap); no role",
    "C-16": "SB-3 needs `substitute_seller_actor`, and the buyers of above-cap building are not named in the text; the relation (entry-level and other building compete for builders) is a market-relation fact the record cannot hold",
    "C-17": "SB-4 is applied to one asset-owner role; land as an input to new homes (`input_to`) is a market-relation fact with no field and no role (`landowners.developable` is not in the text)",
    "C-18": "RS-1 against SB-3 for the rental substitute: no renters role and no relation fact; the combiner has no declared comparison for it",
    "C-19": "no intermediaries role and no rule for agents' fees (SB-2, SB-4, CR-9)",
    "C-20": "RS-4 for subsidies: the schema has `neighbor_actor` for price ceilings only; nothing records the border city",
    "C-21": "CR-12b: needs C-20 and C-29, and a neighbour role; the combiner declares no such comparison",
    "C-22": "OC-7 (what owners do with the gain) is not encoded",
    "C-24": "sign form: the engine signs the OC-1 payer group (see EXCEPTIONS); the table signs taxpayers alone, a plain decrease",
    "C-25": "CR-8b mirror of C-12 for the other buyers (what they pay is lost to other uses): no rule for subsidies",
    "C-26": "combiner: a CR-12 comparison of two chains on builders' total not declared (C-14 against C-16), and neither chain is produced",
    "C-27": "OC-7 (see C-22)",
    "C-29": "RS-4 for subsidies (see C-20), with the other buyers' capitalized price",
    "C-30": "no landlords role and no rule (SB-3, CR-4, CR-7a through the rental market)",
    "C-31": "no renters role; RS-1 and CR-12a for rental units let are not encoded",
    "C-32": "no construction labor role; CR-9 and CR-7a for the price of a resource drawn in are not encoded for subsidies",
}
PRODUCED = {"C-1", "C-2", "C-3", "C-5", "C-7", "C-8", "C-9", "C-11", "C-12", "C-13", "C-23", "C-28", "C-33"}


def test_consistent_with_worked_example_we020():
    pred, keys = _engine(WE20)
    rows = _rows("WE-020_first_time_buyer_grant.md", SHORT, WINDOWS, {})
    assert len(rows) == 33
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert len([c for c in pred["consequences"] if c["reported"]]) == 16
    # SB-6's dip after Year 4 needs the grant to end as scheduled (A-15, p = 0.4): not reported (the first run's WRONG rows)
    assert not any(c["window"] == "after_expiry" and c["reported"] for c in pred["consequences"])
