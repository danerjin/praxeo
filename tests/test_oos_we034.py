"""Out-of-sample check of the mandate rules (praxeo/rules/mandates.lp: PC-18 term_prohibition, written from the catalog alone)
on WE-034, the non-compete ban.

Same shape as test_oos_we018.py. The rules were not changed for this example: every engine consequence is a row of the
example's consequence list or sits in EXCEPTIONS with its reason (each classed "defensible" or "KNOWN WRONG"), and every
table row the engine does not produce sits in NOT_PRODUCED with its reason. The run is described in
cases/we034_teravel/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE34 = ROOT / "cases" / "we034_teravel"

# No table name is mapped to a record role: the record's bound role is employers.restraining (all employers holding
# non-competes), and the table's employers.net_trainers is a subclass of it.
EXCEPTIONS = {
    ("employers.restraining", "asset_value", "decrease", None):
        "defensible: CR-8 voiding of the employers' right, on the whole class; the table signs it for the net trainers (C-16) and gives the class the resources fall (C-38); nothing in the example says the other restraining employers keep the value",
    ("employers.restraining", "lobbying_effort", "increase", None):
        "defensible: RS-7 on the bound class; the table has the net trainers and the worker and start-up associations (C-13)",
    ("employers.restraining", "term_prevalence", "increase", None):
        "defensible: the substitute terms of the preserved forms, on the whole class; the table has the net trainers (C-4), whose substitutes the example derives the same way (A-4)",
}
NOT_PRODUCED = {
    "C-2": "unsupported form: K4 is a disclosure_mandate, which has no rules; PC-18 adds no compliance cost for the bound employers",
    "C-3": "missing record fact and rule: no founders role (a term ban has no entrant field); CR-4b entry by the freed party is not encoded",
    "C-4": "role: the engine signs the bound class employers.restraining; the table's net_trainers is a subclass",
    "C-5": "unsupported form: a sign per reading of a term the Act's exemption may or may not preserve; the reading changes no Component field and the rule has no paid-notice term",
    "C-6": "unsupported form: a sign per reading for training repayment; same",
    "C-9": "missing rule: CR-4a and RS-11 (fewer moves out of the field); only moves to rivals are derived",
    "C-10": "combiner: job_changes (all) needs a declared comparison of the (+) and (-) chains",
    "C-11": "missing rule: RS-8 timing around the effective date and the pending-cases clause; PC-18 has no window",
    "C-12": "missing record fact and rule: the exemptions (K2, K3) have no field, and RS-5 is not applied to a term ban",
    "C-13": "role: employers.restraining against the table's net_trainers; the associations have no role",
    "C-14": "missing rule: RS-1 (trade-secret and non-solicitation claims as substitutes for the voided term)",
    "C-15": "missing record fact and rule: no rival-employer role; CR-9 for hiring firms is not encoded in PC-18",
    "C-16": "role: the engine signs employers.restraining; the table's net_trainers is a subclass",
    "C-17": "missing record fact and combiner: no rival-employer role; a comparison of the (+) and (-) chains on its asset_value",
    "C-18": "missing record fact and rule: no customers role; CR-9 for the old employer's clients",
    "C-19": "combiner: RS-13 against RS-14 on customers' price, and no customers role",
    "C-20": "missing record fact and rule: no intermediaries role; CR-9 for recruiters",
    "C-21": "missing rule: RS-4 and CR-7a for training-intensive investment; no net-trainer or neighbour role in a term ban",
    "C-22": "combiner and role: the courts have no role (the record's enforcer is the Bureau); a comparison of C-33 and C-34",
    "C-24": "missing rule: OC-3 fixed-budget case (the Bureau's other work falls, CR-8a); PC-18 signs the extra task and stops",
    "C-25": "missing rule: OC-4 and CR-5a for the prevented training-for-restraint exchange; the exchange's two classes have no roles",
    "C-26": "missing rule and question: the retention devices that replace the restraint (A-10) raise the freed workers' non_wage_compensation; the rule signs the employers' term_prevalence only",
    "C-27": "missing record fact and rule: buy-outs of bound workers (CR-10a, CR-8b); no buy-out term in the rules",
    "C-28": "missing record fact and rule: the buying side of the same buy-outs; no rival-employer role",
    "C-29": "missing rule: CR-9, CR-4 for the old employer's client accounts",
    "C-30": "missing record fact and rule: no lawyers role; CR-9 on enforcement work",
    "C-31": "missing record fact and rule: no lawyers role; CR-9 on redrafting work",
    "C-32": "combiner and role: a comparison of C-30 and C-31; no lawyers role",
    "C-33": "missing record fact and rule: no courts role; OC-3 for the courts' caseload",
    "C-34": "missing record fact and rule: no courts role; OC-3 for the new disputes",
    "C-35": "missing record fact and rule: no hiring-intensive firms role; CR-4 and CR-7a for location",
    "C-36": "missing record fact and rule: neighbouring jurisdiction's gain (RS-4, CR-4); a term ban has no neighbour field",
    "C-37": "missing record fact and rule: the mirror of C-36 for entry; no neighbour field",
}
PRODUCED = {f"C-{i}" for i in range(1, 40)} - set(NOT_PRODUCED)


def test_consistent_with_worked_example_we034():
    pred, keys = _engine(WE34)
    rows = _rows("WE-034_noncompete_ban.md", {}, {}, {})
    assert len(rows) == 39
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert PRODUCED == {"C-1", "C-7", "C-8", "C-23", "C-38", "C-39"}  # C-1 and C-23 at the first run; the rest after the rule changes
    wrong = {k for k, v in EXCEPTIONS.items() if v.startswith("KNOWN WRONG")}
    assert wrong == set()  # the group on workers.bound (2 keys at the first run) moved to workers.trainees (PC-18 fix)
    assert all(v.startswith(("defensible:", "KNOWN WRONG:")) for v in EXCEPTIONS.values())
