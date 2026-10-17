# WE-056 A cap on what patients pay for insulin at the pharmacy counter, with the balance paid by insurers or a state fund

Analyst: draft (Handbook 1.0, held-out test)  |  Rule catalog version: 1.0  |  Status: awaiting expert review

A stylized policy in a fictional state. Several real states cap patients' out-of-pocket cost for insulin; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a case none of the 1.0 changes were drawn from. It probes PC-1 and PC-16 where the cap falls on what the buyer pays, not on what the seller receives, because a third party pays the balance; CR-6's 1.0 note that small effects in a wider market are signed (national list prices, private-label human insulin, manufacturers' shares); RS-16's 1.0 clause on prices per unit of quality (patients move to pens and newer analogs, and from over-the-counter human insulin); OC-1's and CR-8's 1.0 clauses on payers and on receipts into the same budget (a fund paid from general revenue, which also receives premium tax on the higher premiums and the fines); RS-4 for mail-order pharmacies outside the state; and CR-12's 1.0 notes on what the response argument needs and on the baseline of patterns. The unclear provision is whether out-of-state mail-order pharmacies that ship to residents are bound. The counterfactual throughout is **Tarrenmoor without the Act**: the same plans, pharmacies, manufacturers' programs and list prices as they would otherwise have been. Health effects (fewer missed doses, fewer emergency admissions) are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Tarrenmoor Insulin Affordability Act.** Tarrenmoor is a state of about 4.3 million people. About 120,000 residents use insulin. By source of coverage:

| Group | Insulin users | What they pay now for a 30-day supply |
|---|---|---|
| Members of plans regulated by the state insurance code (fully insured group plans, 39,000; individual-market plans, 9,000) | 48,000 | Average $88. Members of high-deductible plans (about 40%) pay the plan's contracted price, about $290 for an analog insulin, until the deductible is met; others pay copays of $25 to $75 or coinsurance. About 70% pay more than $35 in a typical month. |
| Members of self-funded employer plans, governed by the national Employee Benefit Plans Act, which overrides state insurance law | 30,000 | Plan terms; not reachable by the state. |
| National old-age and low-income programs | 32,000 | Already $35 or less under national rules. |
| Uninsured | 10,000 | 2,500 receive analog insulin free through manufacturers' patient-assistance programs (income test, yearly re-application, shipped by the program's pharmacy); 3,000 buy human insulin without a prescription at about $25 a vial (about $50 a month); 4,500 buy analog insulin on prescription at pharmacy cash prices, about $320 (wholesale acquisition cost about $295 plus a markup of about $25). In a 2026 state survey, about 40% of the last group and 15% of high-deductible members said they had used less insulin than prescribed because of cost. |

List prices (wholesale acquisition costs) are set nationally by three manufacturers; about 8 million people in the country use insulin, so the 58,000 users the Act reaches are about 0.7% of the national total. Private-label human insulin is sold by national pharmacy chains at one national price. The manufacturers' assistance programs exclude people whose insulin is paid for by "any public program or fund" (their standard payer-of-last-resort clause), but apply it to state funds only at their discretion.

Tarrenmoor has about 1,050 pharmacies licensed under chapter 18, §18-4 of the pharmacy law (pharmacies located in the state). Under §18-9 the Board of Pharmacy issues about 140 "nonresident pharmacy permits" to pharmacies outside the state that ship prescriptions to residents; §18-9(3) says "a holder of a nonresident permit is subject to the provisions of this chapter governing dispensing". About 20% of insulin fills for state-plan members are by mail, three quarters of them from two mail-order pharmacies owned by pharmacy benefit managers in Lisvane, the neighboring state. Plans may require mail order for maintenance drugs only if members may opt out to a retail pharmacy. Contracts between pharmacy benefit managers (PBMs) and pharmacies run by calendar year and were signed for 2028 in the autumn of 2027.

Premiums of state-regulated plans total about $9.4 billion a year for about 1.4 million members. The state levies a 2% premium tax on them, paid into the general fund. Prescription drugs are exempt from sales tax. Many individual-market buyers receive national premium credits that cap their net premium as a share of income; about a third do not.

The Act was signed on 12 April 2027 and takes effect on 1 January 2028. No expiry.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Tarrenmoor. Just outside: Lisvane (the two large mail-order pharmacies; border towns 20 minutes away) and Ardmere. | §1. |
| Announced / enacted / effective / expires | Bill introduced 15 January 2027; signed 12 April 2027; effective 1 January 2028; no expiry. | §9. |
| Enforcement (who, penalties, resources) | Board of Pharmacy: $1,000 fine for each overcharge, paid into the Fund; repeated violation may lead to suspension of a license or permit. The Board is funded by license and permit fees; the Act gives it no new money. The Department of Health runs the Fund through a claims contract (about $3 million a year, paid from the Fund). False attestation is an offence. | §5, §7. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Counter cap | Cap on the buyer's payment (no ontology type; see section 2) | Insulin dispensed on prescription | Every "pharmacy licensed by the Board of Pharmacy under chapter 18" (U1) | §3: "A pharmacy shall not collect from a covered resident more than $35 for each 30-day supply of insulin." A covered resident is a resident who is uninsured or enrolled in a plan regulated under the insurance code. | Members of self-funded plans and of national programs; non-residents; insulin sold without a prescription. |
| K2 Plans pay the balance | Mandated payment | Insulin fills of state-plan members | State-regulated plans | §4(a): the pharmacy bills the balance to the plan, "which shall pay it on the terms of its pharmacy contract". | — |
| K3 Insulin Access Fund | `purchase_rebate` paid to the pharmacy | Insulin fills of uninsured residents | Fund (Department of Health) | §4(b): the Fund pays "the pharmacy's usual and customary price, less $35, but not more than the wholesale acquisition cost plus 20 percent, less $35". The usual and customary price is "the price the pharmacy charges a cash-paying customer who is not a covered resident". The uninsured resident attests at the pharmacy to having no coverage (§5). | — |
| K4 Funding | Appropriation | K3 | General fund | §6: "such sums as are necessary", from general revenue; fines under §7 are paid into the Fund. The fiscal note projects $19 million a year. | — |

Unclear provision:
- **U1, mail-order pharmacies outside the state.** §3 binds "a pharmacy licensed by the Board of Pharmacy under chapter 18". Chapter 18 "licenses" in-state pharmacies under §18-4 and issues "permits" to nonresident pharmacies under §18-9, while §18-9(3) subjects permit holders to the chapter's dispensing provisions. Reading U1-a: a nonresident permit holder is a pharmacy licensed under chapter 18; out-of-state mail-order pharmacies shipping to residents are bound by §3 and may bill the plan or the Fund for the balance. Reading U1-b: only §18-4 licensees are bound; out-of-state pharmacies collect the plan's ordinary cost sharing (or their cash price from the uninsured) and cannot bill the Fund. The Board has issued no guidance. Readings get no probability; where a sign depends on U1, one sign per reading is given.

**Figures.** State-plan members: the cap lowers average out-of-pocket cost from about $88 to about $34 per fill, so plans pay about $54 more per fill: about 48,000 × 12 × $54 ≈ $31 million a year, plus the extra fills of members who rationed, about $34 million in all, or about 0.36% of state-regulated premiums. Premium tax on that: about $0.7 million. Uninsured: if pharmacies set the usual and customary price at the Fund's limit (about $354 on a $295 acquisition cost), each fill costs the Fund about $319. The 4,500 current cash buyers cost about $17 million, or about $19 million with the end of rationing; 2,000 over-the-counter buyers who obtain a prescription would add about $8 million, and the 2,500 program enrollees about $10 million if the manufacturers drop them; claims administration adds $3 million: about $39 million against the fiscal note's $19 million (4,500 buyers at the current $320 price less $35, plus administration). Fines: at most a few hundred thousand dollars a year.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Triangular in form (it fixes what the buyer may be asked to pay in a private exchange), but what the seller receives is not capped: the balance is paid by a third party (K2, K3). For the buyer it is operation 3 (the option of buying insulin is made cheaper, CR-1); for the pharmacy it removes the option of collecting more than $35 from the patient (operation 1) and adds a claim on a payer (operation 2). | Yes, for about 70% of state-plan members and for uninsured cash buyers (A-1). Not for those already paying $35 or less. | CR-1, CR-4, CR-6, CR-8b; PC-1 and PC-16 considered and not applied (below); SB-2, SB-8, RS-1, RS-3, RS-4, RS-8, RS-16, RS-12 |
| K2 | Binary in substance: a payment the state compels a regulated plan to make, passed by the plan to its premium payers (CR-9, `contract`). | Yes (A-1). | CR-1, CR-7b, CR-8b, CR-9, RS-5 |
| K3 | Binary: a per-unit payment from the state to the pharmacy on behalf of the buyer (`purchase_rebate`), at a price the pharmacy sets up to a limit. | Yes. | SB-1, SB-2, SB-8, CR-4, CR-6 |
| K4 | Binary: funding from a general budget, which also receives the premium tax and the fines. | Yes. | OC-1 (1.0), CR-8 (0.7, 1.0), OC-3 |

**Why PC-1 and PC-16 are not applied.** If K1 is recorded as a `price_ceiling` on insulin (the money price paid at the counter is fixed below what it would be), PC-1's If clause is met and gives `excess_demand`; PC-2 would then give rationing by waiting or favoritism, and PC-16 says the buyer pays less and the seller receives less, "by the same amount". Derived from the core rules, none of this follows. CR-6's pressure exists only where the quantity buyers wish to buy differs from what sellers wish to sell at the price *sellers receive*. Here the pharmacy receives its contract rate from patient and plan together (K2) or its own usual and customary price up to a limit from patient and Fund together (K3): the cap moves who pays, not what the seller gets. At what pharmacies receive, they wish to sell every fill demanded (insulin is stocked by every pharmacy, and the payment exceeds acquisition cost, A-1), so no shortage forms and no rationing follows. The transfer runs from plans and the Fund (and through them from premium payers and the general budget) to patients, not from sellers to buyers (CR-8b). The component is analyzed as a purchase subsidy with a mandated payer: SB-2 for the buyer's price and quantity, SB-1 and OC-1 for who pays. The one place where a price is capped for the seller is the Fund's limit on the usual and customary price (wholesale cost plus 20%). It lies above the price pharmacies charge today, so it does not bind against the counterfactual; it binds only against the higher price pharmacies would set for a payer that does not respond to price (C-6). Gaps found, (c) 1.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `covered_residents` (`buyers.current`) | State-plan members and uninsured residents who use insulin | Pay at most $35 a 30-day supply at a bound pharmacy. Split by response and position: `covered_residents.paying_above_cap` (state-plan members paying more than $35, uninsured cash buyers), `covered_residents.uninsured`, `covered_residents.state_plans`, `covered_residents.mail_order_users`. |
| `buyers.otc_human_insulin` (`buyers.substitutes`) | Covered residents who now buy human insulin without a prescription (about 3,000 uninsured and some high-deductible members) | Analog insulin on prescription now costs them $35. |
| `program_enrollees` | Uninsured residents enrolled in manufacturers' assistance programs | Receive insulin free; the program may drop them now that a fund pays. |
| `pharmacies.in_state` (`sellers.current`) | The 1,050 pharmacies licensed under §18-4 | Collect $35 and bill the balance; set the usual and customary price the Fund pays; verify status; wait for payment. |
| `pharmacies.nonresident` (`sellers.current`, `neighboring_jurisdictions`) | The 140 nonresident permit holders, chiefly two PBM-owned mail-order pharmacies in Lisvane | Bound under U1-a; not under U1-b. |
| `plans.state_regulated` | Insurers of fully insured and individual-market plans | Pay the balance of each fill; set formularies and utilization rules. |
| `buyers.plan_premiums` | Employers and individuals who buy state-regulated plans | Premiums carry the plans' added cost. |
| `employers.fully_insured` | Employers buying fully insured group plans | May self-fund to leave the state's reach. |
| `buyers.individual_market` | Buyers of individual-market plans | Premiums rise. |
| `buyers.noncovered_cash` | Cash buyers of insulin at in-state pharmacies who are not covered residents (non-residents, visitors) | Pay the usual and customary price. |
| `manufacturers` (`sellers.current` upstream) | The three insulin manufacturers | More paid units; their assistance programs may be displaced by the Fund; list prices are unregulated. |
| `buyers.other_states` | Insulin buyers and payers elsewhere in the country | Face the national list price. |
| `sellers.substitutes` | National chains selling private-label human insulin | Lose some Tarrenmoor buyers. |
| `sellers.complements` | Clinics and prescribers; sellers of pen needles and syringes | More prescriptions and more insulin used. |
| `insulin_fund` | The Insulin Access Fund (Department of Health) | Pays balances for the uninsured; receives fines. |
| `general_fund` | The state's general fund | Appropriates the Fund; receives premium tax. |
| `taxpayers`, recipients of other state spending, future taxpayers | Those who fund the general budget | Pay for the Fund (OC-1, who pays). |
| `officials.enforcement` | Board of Pharmacy; Department of Health | Enforce the cap on a fixed budget (Board); run claims (Department). |
| `residents.self_funded`, `nonresidents.border` | Members of self-funded plans; Lisvane residents near the line | Not covered; may claim to be. |
| `lobbying groups` | Pharmacies' association, PBMs, insurers, patient groups, the treasury | Concentrated stakes in U1, the Fund's limit and the scope of the cap. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `covered_residents.paying_above_cap` | `price_paid` (insulin, per 30-day supply at the counter of a bound pharmacy) | decrease | short (from 1 January 2028) | CR-1, CR-8b, SB-2 | A-1 |
| C-2 | `plans.state_regulated` | `subsidy_outlay` (balances paid to pharmacies for insulin fills) | increase | short | CR-1, CR-8b, CR-12e (dominance, A-24) | A-1, A-24 |
| C-3 | `insulin_fund` | `subsidy_outlay` (balances paid for uninsured residents) | increase | short | CR-1, CR-8b, SB-1, CR-12 (0.9: activities that exist only under the policy) | none |
| C-4 | `pharmacies.in_state` | `net_price_received` (per fill of a state-plan member, 2028) | no_change | short | CR-8b, CR-6 (0.7: existing contracts) | A-2 |
| C-5 | `covered_residents` | `quantity_traded` (30-day supplies of insulin dispensed) | increase | short–medium | CR-4c, SB-2, LW-3 | A-1, A-3 |

C-1 to C-3 are what the Act's supporters expect: patients pay $35, and plans and the Fund pay the rest. C-3 is an outlay that exists only under the Act, an increase against none (CR-12, 0.9); its size is in section 1. Members of self-funded plans, of national programs and non-residents are not covered and are not in C-1.

**What the pharmacy receives (C-4).** For a state-plan member, §4(a) has the plan pay the balance "on the terms of its pharmacy contract": the pharmacy receives the contract rate, from patient and plan together, as it would without the Act. The 2028 contracts were signed in the autumn of 2027 and fix the rate for the year (CR-6, 0.7: terms fixed by existing contracts count as regulated while they last; A-2). So the pharmacy's price per insured fill does not change in 2028. That is the sign PC-16 gets wrong: the buyer pays less, and the seller does not receive less (section 2). Renewals from 2029 are C-33.

**More insulin bought (C-5).** At $35, those who used less than prescribed because of cost buy more (CR-4c: the last units, given up at the old price, are now worth their cost to the buyer; A-3, from the 2026 survey). Two other responses touch the quantity and do not oppose it: prior authorization (C-9) changes which product a member receives, not whether a month's supply is filled (A-6), and members who drop individual coverage (C-21) still buy insulin, as uninsured residents at $35.

**Plans' outlay (C-2).** The cap shifts to plans what members paid above $35, about $54 a fill on average (+). Plans respond by steering members to cheaper preferred products (C-9), which lowers the rate per fill (−). The response argument does not settle this: the plans' steering is a response to the share of each dollar of the rate they now bear, which steering does not undo (CR-12e, 0.8). A-24 is the dominance premise (arithmetic on the case's figures with an empirical premise): the contracted rates of the analog insulins a formulary can steer between differ by much less than the $54 shifted. So C-2 is an `increase`.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | `pharmacies.in_state` | `net_price_received` (per Fund-paid fill: the usual and customary price) | increase | short | CR-4 (x: keep the usual price, y: raise it to the Fund's limit), CR-8b, CR-6 | A-4 |
| C-7 | `buyers.noncovered_cash` | `price_paid` (insulin bought for cash by buyers the Act does not cover) | increase | short | CR-4, CR-9 (same price list) | A-4 |
| C-8 | `pharmacies.in_state` | `quality_per_unit` (service to Fund-paid customers: delivery, reminders), `side_payments` (inducements to choose the pharmacy) | at_least_one_increase | short–medium | CR-6 (a price held above what sellers would accept: pressure from sellers), RS-2 | A-4 |
| C-9 | `plans.state_regulated` | `term_prevalence` (prior authorization and step therapy for insulin) | increase | medium | CR-4 (x: open formulary, y: restrict it), RS-2 | A-6 |
| C-10 | `covered_residents.uninsured` | `quality_per_unit` (insulin product per 30-day supply: pens and newer analogs rather than vials and older products) | increase | short–medium | CR-4 (the price difference between products to the patient is removed), RS-16 (1.0: a change in mix is not a price change) | A-7 |
| C-11 | `covered_residents.state_plans` | `quality_per_unit` (insulin product per 30-day supply) | ambiguous | medium | CR-4, CR-12b | A-6, A-7 |
| C-12 | `buyers.otc_human_insulin` | `quantity_substitute` (human insulin bought without a prescription) | decrease | short–medium | RS-1, RS-16 (mirror case), CR-4 | A-8 |
| C-13 | `program_enrollees` | `price_paid` (insulin, per 30-day supply) | increase | short (from 2028) | CR-4 (manufacturers: x: keep giving, y: let the Fund pay), CR-9, CR-3a | A-9 |
| C-14 | `manufacturers` | `quantity_traded` (paid 30-day supplies for Tarrenmoor residents) | increase | short–medium | CR-9, CR-4, CR-8b, CR-12a, CR-12d | A-3 or A-9 |
| C-15 | `manufacturers` | `net_price_received` (national list price of analog insulin) | increase | short–medium | CR-4 (x: a list price, y: a higher one; fewer sales lost in Tarrenmoor at the higher price), CR-6 (1.0: small effects are signed) | A-10 |
| C-16 | `buyers.other_states` | `price_paid` (analog insulin, national) | increase | short–medium | CR-9, CR-6 (1.0: small effects are signed) | A-10 |
| C-17 | `covered_residents` | `quantity_traded` (insulin fills, November–December 2027) | decrease | short (window) | RS-8, CR-10a, CR-4 | A-11 |
| C-18 | `covered_residents` | `quantity_traded` (insulin fills, January–February 2028) | increase | short | RS-8, CR-4c, CR-12a, CR-12d | A-3 or A-11 |
| C-19 | `buyers.plan_premiums` | `price_paid` (premiums of state-regulated plans, 2028 on) | increase | short–medium | CR-9 (`contract`), CR-7b, CR-6 (0.7: existing contracts), CR-12 (0.8: kind 2 below the cut-off) | A-12, A-24 |
| C-20 | `employers.fully_insured` | `reclassification` (group plans converted to self-funding) | increase | medium | RS-5, CR-4 | A-13 |
| C-21 | `buyers.individual_market` | `quantity_traded` (individual-market coverage bought) | decrease | medium | CR-4c | A-14 |
| C-22 | `residents.self_funded`, `nonresidents.border` | `legal_breach` (false attestations of no coverage or of residence) | increase | short–medium | RS-3, CR-4 (x: pay the plan's cost sharing or the cash price, y: attest falsely) | A-15 |
| C-23 | `pharmacies.in_state` | `legal_breach` (collecting more than $35) | increase | short | RS-3, CR-12 (0.9) | A-16 |
| C-24 | `lobbying groups` | `lobbying_effort` (on questions that exist only under the Act: U1, the Fund's limit, the $35 level, extension to other drugs) | increase | short–medium | RS-7 (1.0), CR-4 (1.0), CR-12 (0.9) | A-17 |
| C-25 | `covered_residents.mail_order_users`, `pharmacies.nonresident` | `cross_border_purchases` (insulin fills for covered residents from out-of-state pharmacies) | U1-a: ambiguous; U1-b: decrease | short–medium | RS-4 (0.9: reach of enforcement), CR-4, CR-12b | A-3, A-18, A-19 |
| C-26 | `pharmacies.in_state` | `quantity_traded` (insulin fills) | U1-a: increase; U1-b: increase | short–medium | RS-4, CR-4c, CR-12a | A-3, A-19 |
| C-27 | `pharmacies.nonresident` | `compliance_cost` (billing the Fund and plans for balances; usual and customary price rules) | U1-a: increase; U1-b: no_change | short | CR-8c, OC-2, CR-1 | none |
| C-28 | `covered_residents.mail_order_users` | `travel_time` (to obtain insulin) | U1-a: no_change; U1-b: increase | short–medium | CR-3a, CR-4 | A-19 |

**The price the Fund pays (C-6 to C-8).** The Fund pays the pharmacy's own usual and customary price, less $35, up to wholesale cost plus 20%. The uninsured patient pays $35 whatever that price is, so a higher usual price loses the pharmacy no Fund-paid sale. Its only cost is to cash customers who are not covered residents, who pay that price (CR-4: x: keep the usual price at about $320, y: raise it toward about $354). Most pharmacies have few such customers (A-4), so the usual price rises toward the limit (C-6), and so does the price those few customers pay (C-7). This is the mirror of PC-16: the seller receives more, not less, and the payer that does not respond to price (the Fund) pays it. The Fund's payment is then above what pharmacies would accept for a fill. That is CR-6's pressure from the sellers' side: pharmacies compete for Fund-paid customers on the margins still open, better service or inducements, which state pharmacy rules forbid but cannot fully police (C-8, a group; CR-6 gives at least one margin). The Fund pays any product prescribed, so the gap is largest on the costliest products.

**Which insulin (C-9 to C-11).** With the patient's payment fixed at $35 for every product, the patient's (and prescriber's) cost of choosing a pen over a vial, or a newer analog over an older one, falls to zero (CR-4). For the uninsured, the Fund pays for any insulin prescribed, so the mix moves toward the products patients rank higher (C-10; A-7). For state-plan members the plan now bears the whole difference in rate between products, so plans restrict the costlier ones by prior authorization and step therapy, which the insurance code allows (C-9; A-6). The two pushes oppose, and no premise ranks them: C-11 is `ambiguous`. By RS-16's 1.0 clause, prices are signed per product: as the mix moves toward pens and newer analogs, the average amount paid per fill rises, but that is a change in mix, not a price change, and it is not recorded as one. RS-21 was considered for C-10 and not cited: K1 is a cap on a payment per 30-day supply, not a cap or right counted in physical units; CR-4 gives the move directly.

**Human insulin without a prescription (C-12).** An uninsured buyer of over-the-counter human insulin pays about $50 a month; with a prescription, an analog insulin costs $35 (RS-1 in reverse; RS-16, mirror case). The Act covers only insulin dispensed on prescription, so the switch needs a clinic visit (C-31); some make it (A-8). Some high-deductible members who bought human insulin to avoid the deductible switch too.

**Assistance programs (C-13, C-14).** The manufacturers' programs give insulin free to uninsured residents below an income line. Once the Fund pays wholesale cost plus 20% for the same patient, a manufacturer compares giving a unit free with selling it to a pharmacy that the Fund pays (CR-4); its payer-of-last-resort clause lets it drop Tarrenmoor residents (A-9). Enrollees then pay $35 where they paid nothing (C-13): they are worse off by their own ranking and in money (CR-3a), and they are the class the Act's supporters least expect to lose. The manufacturers' paid units rise (C-14), through this chain and through the end of rationing (C-5); the chains push the same way, and either suffices (CR-12a, CR-12d).

**List prices (C-15, C-16).** List prices are not regulated. A manufacturer that raises its list price loses some sales to patients and payers who respond to price. In Tarrenmoor, covered patients pay $35 whatever the list price, and the Fund's limit moves with the wholesale cost, so a higher list price loses fewer sales there than it would have (CR-4: x: a list price, y: a higher one; the Act makes y better). The direction is a priori; that a manufacturer's choice is close enough to the margin for this to move it is A-10. The 58,000 users are about 0.7% of national users, so the effect is small; CR-6's 1.0 note says to sign it, not to leave it unsigned as negligible. It falls on buyers and payers in other states (C-16). No opposing chain is derivable; pressure on manufacturers from the Act's cost to the state is a Tier C note only (TS-4 is not derivable).

**Timing (C-17, C-18).** Between signing (April 2027) and 1 January 2028, a fill bought in December costs the patient the old price and the same fill in January costs $35. Insulin keeps for months unopened, so patients who can, buy only what they need in December and fill again in January (RS-8; CR-10a; A-11). High-deductible members who would have stocked up in December after meeting the deductible have less reason to. Fills in November and December 2027 fall (C-17); in January and February 2028 they rise, from the deferred fills and from the lasting increase (C-18; either chain suffices). Each window is signed against the counterfactual (02_ontology.md, 2.5), on the flow of fills.

**Premiums and the plans' members (C-19 to C-21).** Plans pass their added outlay (C-2) to their premium payers when 2028 rates are filed in mid-2027, after the Act was signed (CR-9, the insurance contract; CR-6 0.7: premiums are fixed for the plan year; A-12). A member who uses insulin pays less at the counter; every member pays a little more in premium: both sides of the transfer are recorded (C-1, C-19). A second chain could oppose C-19 in the individual market: insulin users for whom insurance was worth buying mainly for insulin now get it for $35 uninsured, and if some drop coverage the pool loses high-cost members. Its premise (A-25) has p = 0.4, below the cut-off, so C-19 is reported as an `increase` and the chain is recorded in section 10 (CR-12, 0.8, kind 2). An employer near the line between buying a fully insured plan and self-funding finds the insured plan a little dearer (C-20; RS-5; A-13). Individual-market buyers without premium credits face a dearer plan; some at the margin go without (C-21; CR-4c; A-14).

**Evasion (C-22, C-23).** A member of a self-funded high-deductible plan pays about $290 a fill; by attesting to having no coverage, she pays $35 and the Fund pays the rest. A Lisvane resident who gives a Tarrenmoor address does the same. Pharmacies cannot easily check (RS-3; A-15). Some pharmacies collect more than $35 (C-23): a breach that exists only under the Act, an increase against none (CR-12, 0.9; A-16).

**Lobbying (C-24).** Insulin prices were contested before the Act, and would have stayed so (CR-4 1.0, RS-7 1.0); lobbying on that general question is not signed. The questions C-24 names exist only under the Act and are an increase against none: the reading of U1 (in-state pharmacies against PBM-owned mail order), the Fund's limit (pharmacies against the treasury), the $35 level, and extension to self-funded plans' members or other drugs (A-17).

**Mail order outside the state, by reading (C-25 to C-28).** RS-4 asks which side of the boundary the policy favors.
- *U1-b.* Only in-state pharmacies are bound. A state-plan member who fills by mail from Lisvane pays the plan's ordinary cost sharing (about $88 on average), and at an in-state pharmacy pays $35. Plans that require mail order must let members opt out to a retail pharmacy, where the cap applies (A-19). So members paying more than $35 move their fills inside the state, and uninsured buyers, who can use the Fund only at an in-state pharmacy, do the same: cross-border fills fall (C-25) and in-state fills rise (C-26). Members who move give up home delivery and travel to a pharmacy (C-28; CR-3a: the option they chose is now dearer, so they take one ranked lower before). The Board's reach does not matter under U1-b, since nothing binds the out-of-state pharmacy.
- *U1-a.* Out-of-state permit holders are bound and may bill plans and the Fund like in-state pharmacies. The patient's payment is then the same on either side of the line, so CR-4 gives the patient no reason to move. Two chains reach the out-of-state fills. More insulin is bought overall (C-5), some by mail (+). Complying with Tarrenmoor's balance billing, Fund claims and usual-price rule is a cost fixed per pharmacy for the state's patients (CR-4, 0.8: it bears on whether to serve them), and some nonresident permit holders with few Tarrenmoor insulin patients stop shipping insulin there (A-18) (−). No premise ranks them: `ambiguous`. RS-4's 0.9 clause on the reach of enforcement applies: the Board's power over the out-of-state pharmacy runs through the nonresident permit it can suspend, so under U1-a the boundary that matters is the permit, not the state line, and it is enforced (A-1). C-27 is the nonresident pharmacies' added compliance work under U1-a (none under U1-b); C-26 is an increase under both readings, from C-5 alone under U1-a.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-29 | `sellers.substitutes` | `price_substitute` (private-label human insulin, per vial, national) | decrease | short | RS-16 (mirror case; 1.0: per unit of quality), CR-9, CR-6 (1.0: small effects are signed) | human insulin and analog insulin: `substitute`, partial | A-8, A-20 |
| C-30 | `sellers.substitutes` | `price_substitute` (private-label human insulin, per vial, national) | ambiguous | long | CR-12e (1.0: what the response argument needs), CR-12b, CR-7a | as C-29 | A-8, A-21 |
| C-31 | `sellers.complements` (clinics) | `quantity_complement` (prescriber visits by uninsured insulin users) | increase | short–medium | RS-12, CR-9, CR-1 (the cap requires a prescription) | prescription: `complement` to prescribed insulin | A-8 |
| C-32 | `sellers.complements` | `quantity_complement` (pen needles and syringes) | increase | short–medium | RS-12, CR-9, LW-10 | `complement` in use | A-3 |
| C-33 | `pharmacies.in_state` | `net_price_received` (per fill of a state-plan member, contracts from 2029) | decrease | medium | CR-4 (PBMs: the plan now bears what high-deductible members paid, so each dollar off the rate is the plan's), CR-9 (`contract`), CR-5c | pharmacy contract with PBM: `contract` | A-22 |
| C-34 | `manufacturers` | `asset_value` (shares) | increase | short (from April 2027) | CR-7c, CR-10c, CR-6 (1.0: small effects are signed), CR-12a | follows C-14, C-15 | A-3 or A-9; A-23 |
| C-35 | `general_fund` | `tax_revenue` (premium tax) | increase | short–medium | CR-9, CR-8b, OC-1 (1.0: receipts into the same budget) | premium tax follows premiums | A-12 |
| C-36 | `insulin_fund` | `non_tax_receipts` (fines for overcharging) | increase | short–medium | CR-8b, CR-12 (0.9), OC-1 (1.0) | — | A-16 |

**Human insulin (C-29, C-30).** Some buyers leave private-label human insulin for an analog at $35 (C-12). Human insulin is sold nationally at one price, and Tarrenmoor's buyers are a small part of that market. In the short run the chains' contracted volumes cannot be cut at once (A-20), so the price moves down (RS-16, mirror case; CR-6). The effect may be very small; CR-6's 1.0 note says it is signed, with its size in the evidence column. The price is per vial of a given product (RS-16, 1.0), not an average over a changing mix. In the long run, producers contract. CR-12's response argument says the contraction cannot push the price above its old level, but its 1.0 note says what that needs: a premise that cost per unit does not rise as the activity contracts. Human insulin is made in a few plants with large fixed costs, so cost per vial rises as output falls (A-21), and equal yields can be restored at a price above the old one. Without the constant-cost premise the long-run price is `ambiguous` (C-30). The argument bounds the national price of private-label human insulin, all brands together.

**Complements (C-31, C-32).** The cap applies only to insulin dispensed on prescription, so uninsured buyers who switch from over-the-counter human insulin need a prescriber's visit (C-31; RS-12, `complement`; A-8). More insulin used means more pen needles and syringes (C-32; RS-12; A-3).

**Pharmacy contracts after 2028 (C-33).** Before the Act, a high-deductible member in the deductible paid the whole contract rate, so a lower rate saved the member, not the plan. Now the plan pays all but $35 of it. A PBM negotiating 2029 rates for insulin therefore gains more from each dollar off the rate (CR-4; CR-5c: the bargaining range moves). Some PBMs press insulin rates down at renewal (A-22). The 2028 rate is C-4.

**Manufacturers' value (C-34).** Their paid units rise (C-14) and the list price may rise (C-15); both raise expected yields, capitalized when the Act became expected (CR-7c, CR-10c; A-23: the Act was not expected before its introduction in January 2027). The effect on a national firm's shares is small and signed (CR-6, 1.0).

**Receipts into the same budget (C-35, C-36).** The Fund is appropriated from the general fund. The general fund receives 2% of the higher premiums (C-35; A-12), and the Fund receives the fines (C-36; A-16). By OC-1's and CR-8's 1.0 clauses these receipts and the outlay (C-3) are recorded as items of one budget, and the net separately (C-37, section 9). Arithmetic on the case's figures settles the net: about $39 million out against about $0.7 million of premium tax and fines of a few hundred thousand dollars.

Stopping points. Premium increases borne by employers pass, through employment contracts, to wages and benefits of employees in fully insured groups (CR-7b, DM-1's horizon note on factor markets): depth 3 and diffuse across 1.4 million members; stopped. The spending of patients who pay less (C-39) and of premium payers who pay more (C-38): depth 3, diffuse; stopped. Lisvane's mail-order staff under U1-b: depth 3; stopped.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `plans.state_regulated`, `subsidy_outlay`, short | The cap shifts what members paid above $35 to the plan (about $54 a fill). | Steering to cheaper preferred products (C-9). | CR-12e, empirical with arithmetic (A-24): rate differences between steerable products are much smaller than $54. The response argument does not apply (the plans respond to their share per dollar, which steering does not undo). | **increase** (C-2) |
| `covered_residents.state_plans`, `quality_per_unit`, medium | Patients' choice at a fixed $35 (A-7). | Plans' prior authorization (A-6). | None | **ambiguous** (C-11) |
| `manufacturers`, `quantity_traded`, short–medium | End of rationing (A-3); programs displaced by the Fund (A-9). | — | Same direction (CR-12a); either chain suffices (CR-12d). | **increase** (C-14) |
| `buyers.plan_premiums`, `price_paid`, short–medium | Plans' added outlay (C-2, A-12). | Insulin users leaving the individual market (A-25, p = 0.4). | Opposing chain below the cut-off (CR-12, 0.8, kind 2). | **increase** (C-19) |
| `covered_residents`, `quantity_traded`, January–February 2028 | Deferred fills (A-11); the lasting increase (A-3). | — | Same direction. | **increase** (C-18) |
| `cross_border_purchases`, short–medium | U1-a: more fills overall (A-3). | U1-a: some nonresident pharmacies stop shipping (A-18). U1-b: members move in-state (A-19). | None under U1-a. | U1-a: **ambiguous**; U1-b: **decrease** (C-25) |
| `sellers.substitutes`, `price_substitute`, long | Contraction with rising cost per vial (A-21). | Lower demand (A-8). | Response argument fails without the constant-cost premise (CR-12, 1.0). | **ambiguous** (C-30) |
| General budget, net, short–medium | Premium tax (C-35); fines (C-36). | Fund outlay (C-3). | Arithmetic on the case's figures (CR-8, 1.0). | Payers: **at_least_one_decrease** (C-37) |
| `pharmacies.in_state`, `net_price_received` per insured fill | — | 2029 renewals (A-22). | Different horizons (CR-12g). | short: **no_change** (C-4); medium: **decrease** (C-33) |

**Final check** (`03_workflow.md`).
1. Uncombined chains: plans' outlay (C-2) combines the cap with the steering response; premiums (C-19) with the individual-market selection chain; quality (C-11) with formulary tightening; quantity (C-5) was checked against prior authorization and against members dropping coverage, neither of which reduces fills; cross-border fills per reading (C-25). The timing chains (C-17, C-18) and the lasting increase (C-5) are on different windows.
2. Group signs: pharmacies' competition for Fund-paid customers (C-8), the general budget's payers (C-37) and the Board's other work (C-42) are groups.
3. Baseline: every sign is against Tarrenmoor without the Act. C-13 (enrollees pay $35 against $0) and C-6 (pharmacies receive more than their current cash price) are against the counterfactual, not against the cap. C-25 under U1-b compares the out-of-state fills with those without the Act, not with U1-a.
4. Worse off is not poorer: `resources_available_other_uses` is signed for premium payers who keep paying (C-38) and for patients who keep buying (C-39); enrollees dropped by the programs (C-13) pay a sum they cannot avoid if they keep using insulin, but their means are recorded only through `price_paid`.
5. Timing shifts: fills signed per window (C-17, C-18); manufacturers' values at announcement (C-34).
6. Both sides of every transfer: patients (C-1) against plans (C-2) and the Fund (C-3); plans against premium payers (C-19, C-38); the Fund against the general budget's payers (C-37) with its receipts (C-35, C-36); pharmacies' higher usual price (C-6) against the Fund (C-3) and cash buyers (C-7); manufacturers' displaced programs (C-14) against enrollees (C-13) and the Fund.
7. Every actor class, every core rule: CR-7c for manufacturers (C-34); pharmacies' value is pushed both ways (fills and usual price up, compliance and 2029 rates down) and is not recorded; CR-6 for the Fund-paid segment (C-8) and the human insulin market (C-29); enforcement costs and their payers (C-41, C-42).
8. Unstated premises: A-24 (the plans' dominance premise), A-20 and A-21 (the human insulin market), A-23 (when the Act became expected).
9. Baseline of every pattern: PC-1 and PC-16 were not applied, and their conclusions would have been wrong against the counterfactual (section 2); SB-2, SB-8, RS-1, RS-3, RS-4, RS-5, RS-8, RS-12 and RS-16 are signed against no Act. RS-7 is re-signed against the counterfactual contest (C-24). DM-1 is not used. RS-20, EN-11 and EN-13 are not used.

## 8. Time structure

- **15 January to 12 April 2027: introduction to signing.** Manufacturers' shares move as passage becomes likely (C-34; CR-7c's probability clause). Insurers begin to price the cap into 2028 rate filings.
- **12 April to 31 December 2027: the window.** 2028 premiums are filed and approved with the added outlay (C-19). PBM contracts with pharmacies for 2028 are signed in the autumn with the Act known, but the 2028 rate structure is set before the first year's experience (C-4, A-2). Patients defer storable purchases to January (C-17). Manufacturers decide on their programs for 2028 (C-13). Employers renewing for 2028 consider self-funding (C-20).
- **2028.** Fills rise at once and are bunched in January (C-5, C-18); pharmacies raise their usual price for Fund claims (C-6); plans tighten formularies over the year (C-9); the Fund's outlay is about double its fiscal note.
- **2029 onward.** PBM contracts are renewed with the plans bearing the insulin cost (C-33). The $35 cap is fixed in money: as list prices and pharmacy costs rise, the gap between what patients pay and the price widens, and the plans' and the Fund's share grows (TS-3). Producers of human insulin contract (C-30).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-37 | `taxpayers`, recipients of other state spending, future taxpayers | `resources_available_other_uses` | at_least_one_decrease | The general budget's net cost of the Fund: about $39 million a year out, against about $0.7 million of premium tax and small fines in. The record names no tax, so the payers are a group. | OC-1 (1.0: who pays; receipts into the same budget), CR-8 (0.7, 1.0), CR-8b |
| C-38 | `buyers.plan_premiums` | `resources_available_other_uses` | decrease | What the higher premiums (about 0.36%) would have bought; counted only for those who keep their coverage (CR-3, note). | OC-1, CR-3, CR-8a |
| C-39 | `covered_residents.paying_above_cap` | `resources_available_other_uses` | increase | Patients who would have bought anyway now spend less on insulin and have the difference for other uses. | SB-8, CR-8b |
| C-40 | `pharmacies.in_state` | `compliance_cost` (billing balances, verifying status and residence, holding the balance until paid) | increase | Staff time; money held until the Fund pays. | OC-2, TX-5, CR-8c, CR-3 (note: the time money is held) |
| C-41 | `officials.enforcement` (Department of Health) | `enforcement_cost` (claims administration) | increase | About $3 million a year from the Fund, so from the general budget (part of C-37). | OC-3, CR-8c |
| C-42 | `officials.enforcement` (Board of Pharmacy) | `wait_time` (other licensing and inspection work) (+), `enforcement_cost` (other inspections) (−) | at_least_one_as_stated | The Board enforces the cap from a budget funded by fees that the Act does not raise. | OC-3 (0.9: fixed budget), CR-8a |

**OC-1 and CR-8, 1.0.** The Fund is paid from general revenue; the record names no tax, so the payers are a group (taxpayers, recipients of other state spending, future taxpayers through borrowing), `at_least_one_decrease` (OC-1, who pays). Receipts reach the same budget in two ways: the premium tax on the higher premiums, into the general fund that appropriates the Fund (C-35), and fines, into the Fund itself (C-36). They are recorded as items, and the net (C-37) is signed by arithmetic on the case's figures. The plans' payments (C-2) are a separate transfer, from premium payers (C-19, C-38) to patients, through the insurance contract.

**Prevented exchanges.** The Act prevents no exchange; it adds fills. The exchanges that fall are human insulin bought over the counter (C-12) and some individual coverage (C-21): these are buyers taking a better offer the Act creates, or leaving a dearer one, so only the sellers who lose the sale lose (OC-4 Unless; CR-5, 0.7).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Bound pharmacies comply with the $35 cap for most fills, and the payments they receive (contract rate, or the Fund's payment) exceed their acquisition cost, so they keep dispensing. | enforcement | 0.9 | Fines and license suspension; Fund pays at least wholesale cost less $35 plus the $35. | C-1, C-2, C-5 and what follows shrink; C-23 grows. |
| A-2 | 2028 PBM contracts with pharmacies are not reopened during the year. | other | 0.75 | Calendar-year contracts, signed in autumn 2027. | C-4 is not `no_change`; it becomes C-33 earlier. |
| A-3 | Some covered residents used less insulin than prescribed at the old price. | other | 0.85 | 2026 survey: about 40% of uninsured cash buyers and 15% of high-deductible members. | C-5, C-32 are not reported; C-14, C-18, C-26 rest on their other chains. |
| A-4 | Most pharmacies have few cash insulin customers outside the Act, so they set their usual price at or near the Fund's limit. | other | 0.75 | Non-residents and visitors are a small share of insulin cash sales. | C-6, C-7, C-8 are not reported; the Fund pays about $285 a fill rather than about $319. |
| A-5 | The Board of Pharmacy does some enforcement work under the Act (complaints, audits of balance billing) from its existing fee-funded budget, which the Act does not raise. | revenue_use | 0.8 | The Act appropriates nothing to the Board; fee schedules are set by statute. | C-42 is replaced by OC-3's rising-budget case. |
| A-6 | Plans may and some do add prior authorization or step therapy for costlier insulin products. | other | 0.6 | The insurance code allows utilization management with 72-hour decisions; plans' practice for other drugs. | C-9 is not reported; C-11 becomes `increase`. |
| A-7 | When the patient's payment is the same for every product, some patients and prescribers choose pens or newer analogs over vials and older products. | substitutability | 0.7 | Vials are chosen now mainly for price; prescriber surveys. | C-10 is not reported; C-11 becomes `decrease` or `no_change` from the plans' side. |
| A-8 | Some over-the-counter human insulin buyers obtain a prescription to buy an analog at $35. | substitutability | 0.75 | The price gap ($50 against $35); community clinic fees of about $40 a visit. | C-12, C-29, C-31 are not reported. |
| A-9 | Manufacturers apply their payer-of-last-resort clause to the Fund and drop or restrict program enrollment for Tarrenmoor residents. | other | 0.6 | Their program terms; practice with other states' funds. | C-13 is not reported; C-14 rests on A-3. |
| A-10 | Manufacturers' list prices respond at the margin to how many sales a higher list price loses, so a smaller loss in Tarrenmoor moves them, by a small amount. | other | 0.6 | List price changes are set once or twice a year; the effect of payer mix on list prices in industry studies. Size: Tarrenmoor's users are 0.7% of national users. | C-15 and C-16 are not reported. |
| A-11 | Some covered residents can defer storable insulin purchases from late 2027 to January 2028. | other | 0.65 | Unopened insulin keeps for months; high-deductible members' December stocking. | C-17 is not reported; C-18 rests on A-3. |
| A-12 | Insurers include the added outlay in 2028 premiums, and the insurance commissioner approves it. | other | 0.8 | Rate filings in mid-2027 after signing; commissioner's practice with mandated benefits. | C-19, C-35, C-38 are not reported; insurers bear the cost in 2028. |
| A-13 | Some employers near the line between insured and self-funded plans convert. | other | 0.55 | Mid-sized employers already weigh self-funding; the cap adds about 0.36% to premiums. | C-20 is not reported. |
| A-14 | Some individual-market buyers without premium credits are at the margin of buying coverage at a slightly higher premium. | substitutability | 0.55 | About a third of individual buyers lack credits; past responses to premium changes. | C-21 is not reported. |
| A-15 | Some members of self-funded plans, or residents of Lisvane, attest falsely, and pharmacies cannot easily check. | enforcement | 0.6 | Attestation at the counter; no shared coverage database for self-funded plans. | C-22 is not reported. |
| A-16 | Some pharmacies collect more than $35, and some are fined. | enforcement | 0.6 | Complaint-driven enforcement by a Board with no new staff. | C-23 and C-36 are not reported. |
| A-17 | Pharmacies, PBMs, insurers and patient groups can organize at a cost below their stakes. | other | 0.85 | Existing associations; the bill's hearings. | C-24 is not reported. |
| A-18 | Under U1-a, some nonresident permit holders with few Tarrenmoor insulin patients stop shipping insulin there rather than comply with the billing and usual-price rules. | other | 0.55 | Most of the 140 permit holders ship few insulin fills to Tarrenmoor. | C-25 under U1-a becomes `increase`. |
| A-19 | Under U1-b, most state-plan members using out-of-state mail order can switch to an in-state pharmacy. | mobility | 0.85 | The insurance code's opt-out rule; 1,050 in-state pharmacies. | C-25 and C-28 under U1-b are not reported. |
| A-20 | Private-label human insulin cannot be cut back at once: chains buy it under contracted volumes. | durability | 0.6 | Supply contracts with the producers. | C-29 is not reported (the shift goes to quantity). |
| A-21 | Human insulin is made in a few plants with large fixed costs, so cost per vial rises as output contracts. | other | 0.6 | Industry structure. | C-30 becomes "decrease or no change" by the response argument; `decrease` with a partial-response premise. |
| A-22 | Some PBMs press insulin reimbursement rates down at the 2029 renewals because plans now bear what high-deductible members paid. | other | 0.55 | PBM practice with drugs whose cost shifts to the plan. | C-33 is not reported. |
| A-23 | The Act was not expected before its introduction in January 2027. | expectations | 0.7 | No earlier bill reached a committee. | C-34's timing moves earlier. |
| A-24 | The contracted rates of the insulin products a plan can steer between differ by much less than the $54 a fill the cap shifts to plans. | other | 0.75 | Contracted rates of preferred and non-preferred analogs; the case's figures. | C-2 and C-19 become `ambiguous`. |
| A-25 | Some individual-market insulin users drop coverage because insulin now costs $35 without it. | substitutability | 0.4 | Most also need insurance for visits, supplies and monitors. Below the cut-off. | If above 0.5: C-19 is `ambiguous` for the individual market, and the Fund's outlay rises. |
| A-26 | Some insulin users move into Tarrenmoor for the cap. | mobility | 0.2 | Moving costs far exceed the saving for almost everyone. Below the cut-off. | — (conditional possibility only) |
| A-27 | Under U1-b, a PBM opens an in-state licensed mail-order pharmacy to keep its Tarrenmoor insulin fills. | other | 0.35 | Tarrenmoor is a small market for a national PBM. Below the cut-off. | — (conditional possibility only) |

**Conditional possibilities** (an assumption below 0.5): insulin users leaving the individual market (A-25: the Fund's outlay rises and individual premiums could fall); people moving into the state for the cap (A-26); an in-state mail-order pharmacy under U1-b (A-27: C-28 would shrink).

## 11. Report

**The policy.** From 1 January 2028, a pharmacy in Tarrenmoor may not collect more than $35 for a month's insulin from a resident who is uninsured or covered by a state-regulated plan. The pharmacy bills the rest to the plan, or for the uninsured to a state fund paid from general revenue, which pays the pharmacy's own usual cash price up to wholesale cost plus 20%. Manufacturers' list prices are not regulated. It is unclear whether out-of-state mail-order pharmacies are bound.

**Visible consequences.** Patients who paid more than $35 pay $35 (C-1) and buy more insulin (C-5). Plans and the Fund pay the balance (C-2, C-3).

**Invisible consequences.**
- *Who pays.* Premiums of state-regulated plans rise (C-19), and premium payers have less for other things (C-38); some employers self-fund (C-20) and some individual buyers drop coverage (C-21). The Fund costs the general budget about twice its fiscal note, a little offset by premium tax and fines (C-35, C-36, C-37).
- *Pharmacies.* They receive the same contract rate for insured fills in 2028 (C-4), but more for uninsured fills, since they raise the cash price the Fund pays (C-6), which non-covered cash buyers then pay too (C-7); they compete for Fund-paid customers on service (C-8). From 2029, PBMs press their insulin rates down (C-33). Their paperwork rises (C-40).
- *Manufacturers.* They sell more paid insulin (C-14) and may drop their free programs for residents (C-13), whose enrollees then pay $35 where they paid nothing. List prices rise slightly, for buyers in every state (C-15, C-16), and manufacturers' shares gain a little (C-34).
- *Which insulin.* The uninsured move to pens and newer analogs (C-10); plans add prior authorization (C-9), so for insured members the mix may go either way (C-11). Over-the-counter human insulin loses buyers (C-12), its price dips slightly (C-29), and clinics see more prescription visits (C-31); pen needle and syringe sales rise (C-32).
- *Timing.* Fills fall in late 2027 and bunch in early 2028 (C-17, C-18).
- *Evasion and politics.* Some self-funded members and non-residents claim to be covered residents (C-22); some pharmacies overcharge (C-23). Lobbying over the Act's terms rises (C-24). The Board of Pharmacy's other work slows (C-42).

**Per reading of U1.** If out-of-state mail-order pharmacies are bound (U1-a), they take on billing and compliance work (C-27), and whether out-of-state fills rise or fall is open (C-25). If they are not (U1-b), members move their fills to in-state pharmacies (C-25, C-26) and give up home delivery (C-28).

**Ambiguous effects.** The insulin mix for insured members (C-11); out-of-state fills under U1-a (C-25); the long-run price of human insulin (C-30).

**Key conditions.** Compliance by pharmacies (A-1); that pharmacies raise their cash price to the Fund's limit (A-4, p = 0.75); that manufacturers drop residents from their programs (A-9, p = 0.6); that plans pass the cost to premiums (A-12, p = 0.8).

**What this analysis cannot say.** How large any effect is; whether patients' health improves (out of scope for version 1); whether the transfer from premium payers and taxpayers to insulin users is worth it; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | covered_residents.paying_above_cap | price_paid (insulin per 30-day supply at the counter) | decrease | short | visible | B | CR-1, CR-8b, SB-2 | A-1 |
| C-2 | plans.state_regulated | subsidy_outlay (balances for insulin fills) | increase | short | visible | B | CR-1, CR-8b, CR-12e | A-1, A-24 |
| C-3 | insulin_fund | subsidy_outlay (balances for the uninsured) | increase | short | visible | A | CR-1, CR-8b, SB-1, CR-12 | none |
| C-4 | pharmacies.in_state | net_price_received (per insured fill, 2028) | no_change | short | invisible | B | CR-8b, CR-6 | A-2 |
| C-5 | covered_residents | quantity_traded (30-day supplies dispensed) | increase | short–medium | visible | B | CR-4c, SB-2, LW-3 | A-1, A-3 |
| C-6 | pharmacies.in_state | net_price_received (per Fund-paid fill) | increase | short | invisible | B | CR-4, CR-8b, CR-6 | A-4 |
| C-7 | buyers.noncovered_cash | price_paid (insulin bought for cash) | increase | short | invisible | B | CR-4, CR-9 | A-4 |
| C-8 | pharmacies.in_state | quality_per_unit (service to Fund-paid customers), side_payments (inducements) | at_least_one_increase | short–medium | invisible | B | CR-6, RS-2 | A-4 |
| C-9 | plans.state_regulated | term_prevalence (prior authorization, step therapy for insulin) | increase | medium | invisible | B | CR-4, RS-2 | A-6 |
| C-10 | covered_residents.uninsured | quality_per_unit (insulin product per 30-day supply) | increase | short–medium | invisible | B | CR-4, RS-16 | A-7 |
| C-11 | covered_residents.state_plans | quality_per_unit (insulin product per 30-day supply) | ambiguous | medium | invisible | B | CR-4, CR-12b | A-6, A-7 |
| C-12 | buyers.otc_human_insulin | quantity_substitute (human insulin without prescription) | decrease | short–medium | invisible | B | RS-1, RS-16, CR-4 | A-8 |
| C-13 | program_enrollees | price_paid (insulin per 30-day supply) | increase | short | invisible | B | CR-4, CR-9, CR-3a | A-9 |
| C-14 | manufacturers | quantity_traded (paid 30-day supplies for residents) | increase | short–medium | invisible | B | CR-9, CR-4, CR-8b, CR-12a, CR-12d | A-3, A-9 |
| C-15 | manufacturers | net_price_received (national list price) | increase | short–medium | invisible | B | CR-4, CR-6 | A-10 |
| C-16 | buyers.other_states | price_paid (analog insulin, national) | increase | short–medium | invisible | B | CR-9, CR-6 | A-10 |
| C-17 | covered_residents | quantity_traded (fills, Nov–Dec 2027) | decrease | short | invisible | B | RS-8, CR-10a, CR-4 | A-11 |
| C-18 | covered_residents | quantity_traded (fills, Jan–Feb 2028) | increase | short | invisible | B | RS-8, CR-4c, CR-12a, CR-12d | A-3, A-11 |
| C-19 | buyers.plan_premiums | price_paid (premiums of state-regulated plans) | increase | short–medium | invisible | B | CR-9, CR-7b, CR-6, CR-12 | A-12, A-24 |
| C-20 | employers.fully_insured | reclassification (conversion to self-funding) | increase | medium | invisible | B | RS-5, CR-4 | A-13 |
| C-21 | buyers.individual_market | quantity_traded (individual coverage) | decrease | medium | invisible | B | CR-4c | A-14 |
| C-22 | residents.self_funded, nonresidents.border | legal_breach (false attestations) | increase | short–medium | invisible | B | RS-3, CR-4 | A-15 |
| C-23 | pharmacies.in_state | legal_breach (collecting more than $35) | increase | short | invisible | B | RS-3, CR-12 | A-16 |
| C-24 | lobbying groups | lobbying_effort (questions that exist only under the Act) | increase | short–medium | invisible | B | RS-7, CR-4, CR-12 | A-17 |
| C-25 | covered_residents.mail_order_users, pharmacies.nonresident | cross_border_purchases (insulin fills from out-of-state pharmacies) | U1-a: ambiguous; U1-b: decrease | short–medium | invisible | B | RS-4, CR-4, CR-12b | A-3, A-18, A-19 |
| C-26 | pharmacies.in_state | quantity_traded (insulin fills) | U1-a: increase; U1-b: increase | short–medium | invisible | B | RS-4, CR-4c, CR-12a | A-3, A-19 |
| C-27 | pharmacies.nonresident | compliance_cost (balance billing, usual-price rules) | U1-a: increase; U1-b: no_change | short | invisible | A | CR-8c, OC-2, CR-1 | none |
| C-28 | covered_residents.mail_order_users | travel_time (to obtain insulin) | U1-a: no_change; U1-b: increase | short–medium | invisible | B | CR-3a, CR-4 | A-19 |
| C-29 | sellers.substitutes | price_substitute (private-label human insulin per vial) | decrease | short | invisible | B | RS-16, CR-9, CR-6 | A-8, A-20 |
| C-30 | sellers.substitutes | price_substitute (private-label human insulin per vial) | ambiguous | long | invisible | B | CR-12e, CR-12b, CR-7a | A-8, A-21 |
| C-31 | sellers.complements (clinics) | quantity_complement (prescriber visits by uninsured insulin users) | increase | short–medium | invisible | B | RS-12, CR-9, CR-1 | A-8 |
| C-32 | sellers.complements | quantity_complement (pen needles, syringes) | increase | short–medium | invisible | B | RS-12, CR-9, LW-10 | A-3 |
| C-33 | pharmacies.in_state | net_price_received (per insured fill, from 2029) | decrease | medium | invisible | B | CR-4, CR-9, CR-5c | A-22 |
| C-34 | manufacturers | asset_value (shares) | increase | short | invisible | B | CR-7c, CR-10c, CR-6, CR-12a | A-3, A-9, A-23 |
| C-35 | general_fund | tax_revenue (premium tax) | increase | short–medium | invisible | B | CR-9, CR-8b, OC-1 | A-12 |
| C-36 | insulin_fund | non_tax_receipts (fines) | increase | short–medium | invisible | B | CR-8b, CR-12, OC-1 | A-16 |
| C-37 | taxpayers, recipients of other state spending, future taxpayers | resources_available_other_uses | at_least_one_decrease | short–medium | invisible | A | OC-1, CR-8, CR-8b | none |
| C-38 | buyers.plan_premiums | resources_available_other_uses | decrease | short–medium | invisible | B | OC-1, CR-3, CR-8a | A-12 |
| C-39 | covered_residents.paying_above_cap | resources_available_other_uses | increase | short–medium | invisible | B | SB-8, CR-8b | A-1 |
| C-40 | pharmacies.in_state | compliance_cost (balance billing, verification, money held) | increase | short | invisible | A | OC-2, TX-5, CR-8c, CR-3 | none |
| C-41 | officials.enforcement (Department of Health) | enforcement_cost (claims administration) | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-42 | officials.enforcement (Board of Pharmacy) | wait_time (other work) (+), enforcement_cost (other inspections) (−) | at_least_one_as_stated | short–medium | invisible | B | OC-3, CR-8a | A-5 |

C-14, C-18 and C-34 hold if either of their listed chains' premises holds (CR-12d): C-14 and C-34 on A-3 or A-9 (C-34 also on A-23 for timing), C-18 on A-3 or A-11. C-42 depends on A-5.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. The list-price chain (C-15) is a seller's own choice of price, derived from CR-4 with the price as the option; it needs no rule about market power. Every other step was derived from CR-1 to CR-12.

**(b) Unclear core rules.**
1. *CR-6 and a payer that does not respond to price.* CR-6 is stated over "the quantity buyers wish to buy" and "sellers wish to sell" at a price. Here the price the seller receives and the price the buyer pays are different numbers, with a third party paying the gap. CR-6 had to be read as applying at the price the seller receives (no shortage; C-4) and, for the Fund-paid segment, as pressure from sellers where the payer's price is above what sellers would accept (C-8). A sentence saying "where a third party pays part of the price, apply CR-6 at the price received by the seller and CR-4 to the buyer at the price paid" would help.
2. *CR-6 1.0, small effects are signed, for a seller's own price.* The clause speaks of "a chain that moves a price in a wider market". The national list price (C-15) is set by each manufacturer, not cleared by CR-6; the small-effects rule was applied to it by analogy (CR-4 for the direction, CR-6 1.0 for signing what may be tiny). The clause could say it covers any small effect, whatever rule gives its direction.
3. *CR-8 1.0, receipts into the same budget.* The premium tax goes into the general fund, which appropriates the Fund, and the fines go into the Fund itself. The clause was read as covering both (one budget for the purpose of the net). Whether a receipt to the general fund counts as "the budget that funds the policy" when the policy has its own fund is not said.
4. *CR-12e and a response that does not erode its own cause.* For the plans' outlay (C-2), the plans' steering responds to the share of the rate they bear per dollar, which steering does not undo, so the response argument does not apply and a dominance premise was needed (A-24). The 0.8 note (a response driven partly by a second change) came closest; the case is a response to the same change that leaves its cause intact. A sentence on this would help.

**(c) Missing or wrong patterns.**
1. *PC-1 and PC-16 when the cap falls on the buyer's payment.* If K1 is recorded as a `price_ceiling` (the money price paid at the counter is held below its level without the Act), PC-1's If clause is met and gives `excess_demand`, and PC-16 says the seller receives less "by the same amount" as the buyer pays less. Both conclusions are wrong here: the pharmacy receives the same (C-4) or more (C-6), no shortage forms, and the transfer comes from plans and a fund. Applied as written, the patterns would have given signs that had to be overridden; they were not applied. Their If clauses should require that the cap bind on the price the seller receives, and a pattern is needed for a cap on the buyer's share with the balance paid by a third party (candidate below).
2. *SB-2 where the subsidy is "the seller's price less $35, up to a limit".* SB-2 gives `price_paid` down and/or `net_price_received` up. It does not say that when the subsidy pays the seller's own price, the seller's price rises toward the payer's limit (C-6). This was derived from CR-4; a clause would help.
3. *PC-19 and SB-8.* SB-8 applied as written to patients who would have bought anyway (C-39).
4. *RS-21* was considered for the move to pens (C-10) and not used: its If clause needs a cap or right counted in physical units.
5. *RS-4* worked as written for the mail-order boundary; under U1-a the boundary gave no patient-side reason to move, and the only chains were total demand and a cost fixed per pharmacy for serving the state (C-25), which RS-4 does not prompt.

**(d) Vocabulary.**
1. No instrument type for a cap on the buyer's payment with the balance billed to a third party; recorded as a mandated payment (K2) and a `purchase_rebate` (K3).
2. `subsidy_outlay` was used for the balances paid by private plans under a mandate (C-2), which are not a subsidy in the ontology's sense.
3. No variable for a subsidy outlay against its static projection (the Fund's $39 million against a fiscal note of $19 million), the mirror of `tax_revenue_vs_static_projection`.
4. `quality_per_unit` was used for the product mix chosen per 30-day supply (C-10, C-11); the ontology's definition speaks of the quality of each unit sold, not the buyer's choice among products.

**(e) Test of 1.0.**
- *PC-1, PC-16 with a cap on the buyer's payment.* Failed as written, if the cap is classed as a price ceiling: preconditions met, conclusions (shortage; seller receives less by the same amount) wrong ((c) 1). Re-derived from CR-6 at the seller's price and CR-8b.
- *CR-6 1.0, small effects are signed.* Worked for the human insulin price (C-29), other states' buyers (C-16) and manufacturers' shares (C-34). Needed interpretation for the list price (C-15), which a seller sets rather than a market clears ((b) 2).
- *RS-16 1.0, per unit of quality.* Worked as written: prices are signed per vial of a given product (C-29), and the move toward pens and newer analogs is recorded as a change in mix (C-10, C-11), not as a price rise.
- *OC-1 1.0 and CR-8 1.0, payers and receipts into the same budget.* Worked: the Fund's payers are a group (C-37); premium tax and fines are recorded as items (C-35, C-36) and the net is signed by arithmetic. Needed interpretation on whether the general fund and the Fund are one budget ((b) 3).
- *RS-4 (with 0.9, reach of enforcement).* Worked as written under U1-b (C-25, C-26, C-28). Under U1-a, the reach clause worked (the permit is the boundary), and the sign was `ambiguous` from chains RS-4 does not prompt ((c) 5).
- *CR-12 1.0, what the response argument needs.* Worked as written: for the long-run price of human insulin, fixed costs per plant deny the constant-cost premise, so the sign is `ambiguous` (C-30); the total bounded is the national private-label price, all brands. For plans' outlay the argument did not apply at all ((b) 4).
- *CR-12 1.0, the baseline of patterns.* Worked: every pattern used was checked against Tarrenmoor without the Act. PC-16's error is in its conclusion, not its baseline. RS-7 was re-signed against the counterfactual contest (C-24).
- *CR-6 0.7, existing contracts.* Worked as written for 2028 pharmacy contracts (C-4) and premiums fixed for the plan year (C-19).
- *CR-12 0.8, kind 2 below the cut-off.* Worked as written for the individual-market selection chain on premiums (A-25, C-19).
- *Candidate patterns from 06_gaps.md, 6.2e.* None was needed. "A claim payable inside a boundary draws items from outside" (WE-027) was considered for U1-b and does not fit: the Act draws fills inside, but through the buyer's lower payment, not a claim on items crossing. Proposed new candidates: "a cap on the buyer's share with the balance paid by a third party" (CR-1, CR-6 at the seller's price, CR-8b) and "a payer that pays the seller's own price up to a limit draws the price to the limit" (CR-4, CR-6 from the sellers' side).
