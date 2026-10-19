"""Out-of-sample check of the mandate rules (praxeo/rules/mandates.lp, PC-17 developed on WE-029, PC-18 and EN-14 written from the
catalog) on WE-036, the employer health cover mandate ("play or pay").

Same shape as test_oos_we018.py. The rules were not changed for this example: every engine consequence is a row of the
example's consequence list or sits in EXCEPTIONS with its reason (each classified "defensible:" or "KNOWN WRONG:"), and every
table row the engine does not produce sits in NOT_PRODUCED with a reason category. The run is described in
cases/we036_quenby/out_of_sample.md.
"""
from pathlib import Path

from test_out_of_sample import _check, _engine, _rows

ROOT = Path(__file__).resolve().parents[1]
WE36 = ROOT / "cases" / "we036_quenby"

# the table's "insurers" (C-23) are the K2 makers, its "unions" the recipients' organization, and the "recipients of other
# general-fund spending" the OC-1 group's second member
SHORT = {"insurers": "insurers.group", "unions": "workers.uncovered",
         "recipients of other general-fund spending": "recipients.other_spending"}
EXCEPTIONS = {
    ("employers.bound", "lobbying_effort", "increase", None):
        "defensible: RS-7 signs the bound role; C-23 lists its subclasses (mid-size payers, capped firms) and the firms near 50",
    ("employers.bound", "reclassification", "increase", None):
        "defensible: RS-5 signs the bound role when reshaping pays (A-17); the table puts it on the mid-size payers (C-56, agency labor) and the firms near 50 (C-18)",
    ("employers.bound", "resources_available_other_uses", "decrease", None):
        "defensible: CR-8b, the cost paid by the bound role; the table gives it to its subclasses, the capped firms, the players and the mid-size payers (C-14, C-43, C-46)",
    ("employers.lean_plans", "compliance_cost", "increase", None):
        "defensible: CR-8c, firms with plans short of K1 rewrite them (A-5, C-25); the table has compliance cost on all bound firms (C-42)",
    ("employers.players", "specification_level", "increase", None):
        "defensible: EN-14 signs the buyers of covered plans; the table puts the same fact on the insurers who sell them (C-25)",
    ("sellers.contract_services", "reclassification", "increase", None):
        "defensible: RS-5 signs the actor outside the definitions; the table records the agencies' sales (C-60, quantity_traded)",
    ("workers.near_30", "employment", "at_least_one_decrease", None):
        "defensible: member of RS-18's group below the line, true given C-11 (hours fall); the table signs the members one by one (C-11, C-50)",
    ("workers.near_30", "hours_worked", "at_least_one_decrease", None):
        "defensible: member of RS-18's group below the line (see above); the same fact as C-11",
    ("workers.uncovered", "earnings", "decrease", None):
        "defensible: CR-12, the wage falls (C-7) and hours or jobs fall (C-8, C-9); the table does not list earnings",
    ("workers.seasonal", "non_wage_compensation", "U1-a: increase; U1-b: no_change", None):
        "defensible: the seasonal firms are bound under U1-a only (C-19, C-61); the row gives all their workers cover, which holds only for those at firms that play",
    # produced and contradicted by the example
    ("workers.uncovered", "non_wage_compensation", "increase", None):
        "KNOWN WRONG: the class is full-timers at bound firms in both branches; the example gives cover only to those at players (C-1, workers.at_players) and says nothing is added for workers at payers, and it signs the total ambiguous (C-44)",
    ("employers.compliant", "asset_value", "increase", None):
        "KNOWN WRONG: the example signs the value of compliant firms ambiguous (C-48): their rivals' costs (A-22) against their own quarterly offer reporting (C-42); the engine counts the first only",
    ("workers.full_time", "hours_worked", "ambiguous", None):
        "KNOWN WRONG: the example signs it increase (C-12); the opposing scale chain is a suspected effect the rules do not derive (CR-12 kind 1, Tier C note in section 7), not a chain of equal standing",
    ("workers.uncovered", "job_changes", "decrease", None):
        "KNOWN WRONG: RS-11 lock-in is signed at the medium horizon for the whole class; the example signs it decrease in the short run only, at players (C-57), and ambiguous once wages adjust (C-58)",
    ("insurers.group", "quantity_supplied", "decrease", None):
        "KNOWN WRONG: EN-14 has the standard cut the makers' output; the example has group plans meeting K2 sold in greater number (C-24) and lean plans still sold to payers (section 6)",
}
NOT_PRODUCED = {
    "C-1": "role: the cover is signed on the whole recipient class (workers.uncovered), not on the workers at firms that play; the record has one recipient role",
    "C-3": "missing record fact: no field for a buy-out charge or the split of the bound firms into players and payers; the engine signs price_paid on employers.bound only (C-45)",
    "C-4": "missing record fact and rule: the charge paid to the state under a mandate with a buy-out; nothing signs the fund's receipts",
    "C-11": "sign form: the engine signs RS-18's group below the line, at_least_one_decrease over employment and hours_worked, not hours_worked alone",
    "C-12": "combiner: the engine reports ambiguous (RS-18's shift against the cost chain mc_cap_cost); the example signs increase",
    "C-13": "missing rule and record fact: caps per firm (RS-18 0.9, CR-4 fixed cost), the capped firms' sales won from mid-size payers (CR-9, OC-5); no capped role",
    "C-14": "role: the cost is signed on employers.bound; the record has no capped-firm class and no cap per firm",
    "C-17": "missing rule: RS-17's value of firms near the line (capitalization, rivals' burden) is not in mc_threshold",
    "C-18": "role: RS-5 signs the bound role and the outside actor; the firms near 50 are not bound",
    "C-19": "missing record fact: the 380 seasonal firms are not a role; the margin reading is read on recipients (workers.seasonal) only",
    "C-21": "missing rule: RS-8 timing chains around a threshold (flow of crossings); mandates have no announcement window field",
    "C-22": "missing rule: breach under self-reported compliance checked by audit; mc_breach is for enforcement on complaint only",
    "C-24": "missing rule: CR-9 (plans input_to the players' compensation); mandates have no related markets, and EN-14 signs the opposite on quantity_supplied",
    "C-25": "role: EN-14 signs specification_level on the buyers of the standard's units (employers.players), not on the makers",
    "C-26": "missing rule: RS-1 substitutes for a mandate; no individual-plan role",
    "C-31": "missing rule: RS-14's branch with exempt rivals (the bound sellers lose sales); mc_pass is the price branch and is below the cut-off at A-24 (0.4)",
    "C-35": "missing rule: RS-12 complements for a mandate (care billed to insurers); no provider role",
    "C-36": "missing rule: CR-9 along the insurance contract (ICP outlays); no fund role",
    "C-37": "missing rule: TX-10 income tax lost as wages turn into excluded premiums; no fund role",
    "C-39": "missing record fact and rule: the charges received by the fund (CR-8b, CR-8d); the record has no charge",
    "C-40": "missing rule and combiner: charges against the appropriation, CR-12e arithmetic with a premise; OC-1 is signed on the appropriation side only",
    "C-43": "role: the outlay is signed on employers.bound; no players class",
    "C-44": "combiner: cover increase (mc_binds) and the group of other terms (mc_others_short) are both reported on workers.uncovered without a total; no players class",
    "C-46": "role: the outlay is signed on employers.bound; no payers class",
    "C-47": "role and missing rule: no capped class; the fixed charge against sales won has no chain",
    "C-48": "combiner: the engine reports the rivals' gain only (the WRONG row); compliant firms' own reporting cost is not signed, so there is no opposing chain",
    "C-49": "combiner: the receipts side (C-39) is missing, so the group of C-38 has no opposing chain",
    "C-50": "missing rule: the other half of RS-17 on an hours line, positions under the line (CR-4 switch); mc_cap_shift signs a group below the line",
    "C-51": "missing rule: RS-18's second member, full-time heads fall (CR-4 switch); mc_cap_shift signs hours above the line only",
    "C-52": "combiner: total heads need C-50 and C-51 (CR-12, two items in one variable)",
    "C-55": "unsupported form: a group over employment at three different classes of employer (small firms, part-time, Tarnley); no rule moves workers to unbound work",
    "C-56": "role and missing record fact: reshaping is signed on employers.bound and the agencies; the cap per firm that makes agency labor an arbitrage (A-34) is not a record fact",
    "C-57": "role: the lock-in is signed on workers.uncovered and at the medium horizon (the WRONG row); no players class",
    "C-58": "combiner and missing rule: no chain opposes RS-11's decrease (the lower wage at players, C-7, pushes job changes up)",
    "C-59": "missing rule: CR-9 and CR-7a for workers at unbound firms, with opposing chains; no unbound role",
    "C-60": "missing rule: CR-9 for the agencies' sales (quantity_traded); RS-5 signs reclassification only",
    "C-61": "missing record fact: the seasonal firms' owners have no role; only the workers' margin is read per reading",
}
PRODUCED = {f"C-{i}" for i in range(1, 62) if i != 6} - set(NOT_PRODUCED)


def test_consistent_with_worked_example_we036():
    pred, keys = _engine(WE36)
    rows = _rows("WE-036_employer_health_cover_mandate.md", SHORT, {}, {})
    assert len(rows) == 60
    _check(rows, keys, EXCEPTIONS, NOT_PRODUCED, PRODUCED)
    assert all(r.startswith(("defensible:", "KNOWN WRONG:")) for r in EXCEPTIONS.values())
    assert sum(r.startswith("KNOWN WRONG:") for r in EXCEPTIONS.values()) == 5
    assert all(r.split(":")[0] in ("role", "missing rule", "missing record fact", "missing rule and record fact",
                                   "missing record fact and rule", "missing rule and combiner", "combiner", "sign form",
                                   "unsupported form", "below cut-off", "role and missing rule",
                                   "role and missing record fact", "combiner and missing rule", "missing rule and record fact")
               for r in NOT_PRODUCED.values())
