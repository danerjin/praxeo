"""Out-of-sample run of the prohibition rules (praxeo/rules/prohibition.lp) on WE-053, a data localization requirement.

The prohibition rules were written from WE-017 only; WE-053 was not used for any rule. Same shape as
tests/test_prohibition.py: every reported engine consequence is a row of the example's consequence list (key: actor class,
variable, sign, window) or sits in EXCEPTIONS with its reason (prefixed "KNOWN WRONG:" when it contradicts the example); every
table row the engine does not produce sits in NOT_PRODUCED with the reason. The record and answers are in
cases/we053_corvany/, the write-up in cases/we053_corvany/out_of_sample.md. Nothing under praxeo/ was changed.

K1 is a `prohibition` (hosting abroad, the buyers being the covered controllers and the bound sellers the foreign providers),
K3 a `licensing_requirement`; K2 (officer and statement) has no instrument in the ontology and is not in the record.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE53 = ROOT / "cases" / "we053_corvany"

SHORT = {
    "recipients of other spending": "recipients.other_spending",
    "future taxpayers": "taxpayers.future",
}
WINDOWS = {"migration services, window": "announcement"}
EXCEPTIONS = {
    ("sellers.foreign", "legal_breach", "increase", None):
        "RS-3 for a ban on a practice (practice_ban, added after the first run): C-13 signs it for sellers.foreign.online, a subclass the record has no role for",
    ("firms.covered", "lobbying_effort", "increase", None):
        "RS-7 on the buyers (K1); section 5 (lobbying) names covered controllers beside the operators and providers (A-13), but C-14 lists only the operators, providers and controllers near the line",
    ("firms.covered", "price_paid", "increase", None):
        "from K3 through the licensing rules (buyers pay more where sellers are restricted), not from CR-1 and CR-6 on the cost of local hosting; C-4 is the subclass firms.covered.abroad, which has no role in the record, so C-4 is not credited",
    ("firms.covered", "quantity_substitute", "increase", None):
        "RS-1: covered controllers turn to local hosting; the table has it as the sellers' side (C-2) and as the price of the substitute (C-17), not this row",
    ("firms.covered", "quantity_traded", "decrease", None):
        "OC-4, the buyers' side of C-6 (hosting bought from abroad falls); C-7 is only backup storage, with the sign per reading",
    ("sellers.substitutes", "employment", "decrease", None):
        "KNOWN WRONG: EN-1 and EN-3 on K3 alone (the certificate drives some operators out); the table has operators' demand rising under K1 (C-2) and staff at data centers rising (C-38, workers.data_centers)",
    ("sellers.substitutes", "entry_rate", "decrease", None):
        "KNOWN WRONG: EN-1 on K3 alone; C-22 has entry of new data centers (sellers.prospective) increasing, because K1 raises the demand for local hosting",
    ("sellers.substitutes", "number_of_sellers", "decrease", None):
        "KNOWN WRONG: EN-1 and EN-3 on K3 alone; C-20 is ambiguous: the fixed cost per facility (A-18) against entry and expansion drawn by the shifted demand (A-3, CR-12b)",
    ("sellers.substitutes", "quantity_traded", "decrease", None):
        "KNOWN WRONG: OC-4 with EN-1 on K3 alone (exchanges the certificate prevents); C-2 has the operators' quantity supplied increasing",
    ("sellers.substitutes", "share_of_sellers_licensed", "increase", None):
        "EN-1 with some_qualify: more of the operators are licensed; not in the table (C-20 speaks of the number of facilities hosting covered data)",
}
NOT_PRODUCED = {
    "C-1": "K2 (officer, statement) has no instrument in the ontology, so no compliance cost per controller; the prohibition rules give no cost to the buyers (CR-4 0.8, a cost fixed per firm)",
    "C-2": "no rule shifts demand to the local sellers of the substitute (CR-9, CR-6 under a prohibition); the engine has the opposite sign from K3 (KNOWN WRONG)",
    "C-3": "no rule for providers that comply by investing in Corvany (CR-4 0.8, per outlet); investment_target is not derived",
    "C-4": "the subclass firms.covered.abroad is not a role; the engine's firms.covered price_paid rise comes from K3, not from the dearer local hosting (CR-6)",
    "C-5": "no rule gives the buyers fewer sellers to use; EN-7 signs number_of_sellers on the bound sellers only (exception)",
    "C-7": "backup storage per reading (U1 changes no record field and the readings carry no engine facts); the engine has a plain decrease on hosting bought abroad",
    "C-8": "subclass firms.covered.local and the reading U1-b; no rule",
    "C-10": "RS-17 (bunching below a notch) is not encoded; no number_of_sellers rule for a line in a definition",
    "C-11": "RS-17 0.9 and CR-12b for firms just below the line are not encoded; no role",
    "C-12": "CR-4 (0.8, per outlet) and RS-6 for foreign services that cap sign-ups or withdraw are not encoded; no quantity_supplied rule for the buyers who breach",
    "C-13": "legal_breach is not derived (RS-4 0.9, reach of enforcement, is not encoded); the engine's rows on the class are KNOWN WRONG",
    "C-15": "RS-8 with CR-12 (0.9) for activities that exist only under the policy is not encoded; no intermediaries role",
    "C-16": "CR-12b opposing chains on quality are not encoded for a prohibition",
    "C-17": "no RS-16 or CR-6 rule for the price of the substitute under a prohibition",
    "C-18": "same, with CR-12e and RS-13",
    "C-20": "the engine signs it decrease (KNOWN WRONG); the (+) chain of entry is not encoded",
    "C-21": "CR-7c for the substitute sellers' assets under a prohibition is not encoded",
    "C-22": "no sellers.prospective (entrant) role for a prohibition; the engine signs entry decrease (KNOWN WRONG)",
    "C-23": "CR-9 to the owners of an input to the substitute sellers is not encoded for a prohibition (related markets are tax and subsidy only)",
    "C-24": "same (CR-9 input suppliers)",
    "C-25": "same (OC-5, CR-9 construction labor)",
    "C-26": "RS-14 downstream users of the banned input is not encoded for a prohibition",
    "C-27": "CR-9 and CR-4 (0.8) on variety for users of the foreign services are not encoded",
    "C-28": "no domestic-rival role for a prohibition; CR-9 and CR-6 on rivals are not encoded",
    "C-29": "TX-8 (0.9) on the currency link for an import ban is not encoded for a prohibition",
    "C-30": "the neighbor_seller role signs the neighbours' gain from crossing buyers (RS-4); the Esterland data centers' loss is a fall in the bound sellers' sales abroad, with no separate role",
    "C-32": "the engine signs it at_least_one_decrease (KNOWN WRONG); the receipts into the same budget are not a declared comparison",
    "C-33": "licensing fees paid into the general budget (CR-8b) have no rule or variable in the licensing rules",
    "C-36": "no rule for users of the services that cap or withdraw (CR-5a, OC-4)",
    "C-37": "CR-7c, CR-10c and RS-17 for domestic rivals' value are not encoded; no role",
    "C-38": "CR-9 and LW-10 to labor in the substitute sellers' industry are not encoded for a prohibition",
    "C-39": "CR-8a on the providers' investment drawn from elsewhere is not encoded",
    "C-40": "the engine's net_price_received increase is C-19's sign by key; the medium-run ambiguity (CR-12e, RS-13, CR-12b) is not encoded",
    "C-41": "CR-9 and CR-6 on the Esterland regions' price are not encoded",
}
PRODUCED = {"C-6", "C-9", "C-14", "C-19", "C-31", "C-34", "C-35"}


def test_consistent_with_worked_example_we053():
    pred, keys = _engine(WE53)
    rows = _rows("WE-053_data_localization.md", SHORT, WINDOWS, {})
    assert len(rows) == 41
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
