# WE-016 Arvane expand loop, blind run notes

Read: handbook/04a_core_rules.md, praxeo/core/{core.lp,situation.py,expand.py}, the we001/we009/we013 records, and only section 1
and the ID/Statement/Type/p columns of the assumption table of WE-016. cases/we016_arvane/ already held other files; none was read.
`policy.txt` is section 1 verbatim (from the bold policy name to the unclear-provisions paragraph).

## Seed (CR-1 facts only)
- e_design: clients.design buy from designers.licensed; designers.unlicensed are the unsatisfied sellers (shut out). Free price, so no
  criteria. e_plan: applicants.permit buy stamps from designers.licensed (K3), same unsatisfied sellers.
- capped k1 on e_design (holders: licensed, grandfathered; premises A-1 binding, A-2 enforcement): K1 fixes who may sell, price free.
  capped k3 on e_plan (holders: licensed, grandfathered, architects; premise A-5 "building departments reject plans without a stamp").
- charge k1_fee on e_design, paid by sellers to officials.board (non_tax_receipts): the $250 annual fee. No `moves` (it is a fixed
  annual cost, CR-4 0.8, not a per-trade wedge; no premise in the table says who bears it) and no quantity_premises (money, not in kind).
- outside margin on e_design for designers.unlicensed (A-3): kept in the seed because it belongs to the exchange (enforcement of the cap).
- announced k1, k3 (passed ten months before it took effect; no premise needed). compliance k1 designers.licensed, k3 applicants.permit.
  enforcers k1, k3: officials.board (K4). funded k1: taxpayers (K4 "general budget"); fees are the charge.
- Not seeded, deliberately: held (no price line), banned (the cap covers it; a ban on e_design would double the same effects),
  grants, backstops, expires, means, discretion, early_price, transfers, fixed_budget (nothing in section 1 says the Board's budget is fixed).
- K2 is expressed only as the extra holder class designers.grandfathered. Assumptions in the seed: a1, a2, a3, a5 (table p).

First run: 8 nodes (applicants.permit, architects, clients.design, designers.grandfathered, designers.licensed, designers.unlicensed,
officials.board, taxpayers).

## Round 1 (depth 1), proposals
- applicants.permit: alt to architects for stamping (A-11, K3 text); timing bring_forward permit_applications (A-8, ten-month window).
- architects: link supply_price commercial_interior_work -> net_price_received (A-18); stake (A-9).
- clients.design: alts to store design help at retailers.furnishings (A-10, A-7; exemption list), a group of own_design_work/online_service_use
  (A-10), architects (A-11), designers.velmark (A-17; Corvan is 20 km from the border); timing bring_forward commercial_projects_started (A-8).
- designers.grandfathered: alt temporary_exits_from_trade (A-16; K2 lapse clause makes leave-and-return worse, so it falls); stake (A-9).
- designers.licensed: stake (A-9).
- designers.unlicensed: alts to retailers (A-7), Velmark (A-17), exits_from_trade (A-19), degree program enrolment (judged premise,
  "Some practitioners and would-be entrants without the degree earn it to gain a license", from the 300 graduates a year sentence).
- officials.board, taxpayers: empty (their effects reach no one else; nothing in the table to say what they do about it).

Answers (table): A-11 0.7, A-8 0.6, A-18 0.7, A-9 0.8, A-10 0.85, A-7 0.75, A-17 0.4, A-16 0.65, A-19 0.65.
Judged: "Some practitioners and would-be entrants without the degree earn it to gain a license." 0.7 (A-1 says many would not; some do).
Effect of the answers: A-17 at 0.4 keeps every Velmark chain below the cut-off (designers.velmark arvane_clients_served is listed with "-").

## Round 2 (depth 2): retailers.furnishings, students.interior_design
- retailers.furnishings: complement link design_help_provided -> furnishings_sales (A-12); stake (A-9).
- students.interior_design: same_act link enrolment -> schools.design_programs (no premise: the same act seen from the school);
  supply_price link enrolment -> wait_for_supervised_position (A-15, "supplied" scarcity of supervised positions; the source variable
  is enrolment as a proxy for graduates seeking supervised hours).
Answers (table): A-12 0.75, A-15 0.6.

## Round 3 (depth 3): schools.design_programs
- stake (A-9). Nothing else: no table statement or sentence gives the schools another margin.

Totals: 3 rounds, 11 nodes proposed for (8 + 2 + 1), 12 questions: 11 answered from the table (A-7, A-8, A-9, A-10, A-11, A-12, A-15, A-16,
A-17, A-18, A-19) and 1 judged. Final engine output (engine_output.txt): 36 effect lines, all reported (R) except
designers.velmark arvane_clients_served (A-17 at 0.4).

## What the format could not hold (or held badly)
1. Quality. A-13, A-14, A-20 (training related to commercial needs, unrelated for homes; substitutes give lower quality) are about
   what clients get for the price. The only variable the vocabulary lists for it is quality_adjusted_price (a price) and the link
   relations carry no "lower quality" sign; any link would have been a hack, so none was written. CR-11c (a license as a signal) has no fact type.
2. Stock decay over time. A-4 (grandfathered leave at 3 to 5% a year) and A-16's persistence: no fact says the count of holders falls, so the
   asset value of the grandfathered license cannot fall later. Horizons other than the announcement window do not exist in the format.
3. A scarce unpriced input as an exchange. Supervised hours (K1, A-15) are an exchange (trainees and supervisors, a queue) but exchanges are seed-only
   and nothing is held or capped there, so it is reached only as a link (supply_price on enrolment) and the wait is attached to the students.
4. Fixed costs per firm. The annual fee and CE are fixed costs of operating (CR-4 0.8, bearing on entry and exit, not unit price). The charge
   fact models a per-trade wedge, so it reports quantity_traded down for parties and only the engine's own reading; no way to say "exit margin only".
5. Grandfathering as an exemption. K2 appears only as a second holder class on the capped fact, not as a dated, lapsing operation
   (CR-1 dated operations; the lapse rule). The licensed/grandfathered split of the seller side leaves designers.licensed as the exchange party.
6. Exempt competitors as sellers. Architects and retail employees are exempt sellers in the same market; they are reached as alternatives of the
   buyers, not as a second seller class of e_design, so e.g. a price effect on them comes only via a supply_price link.
7. Windows. Timing facts hold bring_forward; the matching after-expiry dip needs `expires` and the Act does not expire. The paired
   fall in projects after the effective date (carry-over) is not derivable.
8. Class totals. No `parts` were proposed: nothing in the table needed a total over unlicensed, licensed and grandfathered.
9. Dominance. None proposed: no opposed chains appeared, so there was nothing for a dominance premise to settle.
10. Commercial vs residential split of clients. Section 1 gives a 50/50 revenue split; clients.design is one class in e_design. K3 reaches only
    commercial permits, which is why e_plan has its own buyer class, but the residential/commercial difference in A-10 vs A-11 is carried by
    which alternatives are premised, not by a split of the class.
