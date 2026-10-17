# WE-056 / Analysis: Tarrenmoor Insulin Affordability Act (a $35 counter cap on insulin, balance paid by plans or a state fund)

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Tarrenmoor Insulin Affordability Act.** Tarrenmoor is a state of about 4.3 million people; about 120,000 residents use insulin. 48,000 are members of plans regulated by the state insurance code (39,000 fully insured group, 9,000 individual market; average out-of-pocket about $88 per 30-day fill; about 40% in high-deductible plans paying the contracted price of about $290 until the deductible is met; about 70% pay more than $35 in a typical month). 30,000 are in self-funded employer plans governed by national law, which the state cannot reach; 32,000 are in national programs that already cap the payment at $35 or less; 10,000 are uninsured (2,500 in manufacturers' patient-assistance programs, 3,000 buying human insulin without a prescription at about $50 a month, 4,500 buying analog insulin at pharmacy cash prices of about $320, against a wholesale acquisition cost of about $295). In a 2026 survey about 40% of the last group and 15% of high-deductible members had used less insulin than prescribed because of cost.

List prices are set nationally by three manufacturers; the 58,000 users the Act reaches are about 0.7% of national users. Private-label human insulin is sold by national chains at one national price. Manufacturers' assistance programs exclude people whose insulin is paid by "any public program or fund", applied to state funds at their discretion. About 1,050 pharmacies are licensed in the state under §18-4; about 140 out-of-state pharmacies hold nonresident permits under §18-9, and §18-9(3) subjects them to the chapter's dispensing provisions. About 20% of state-plan insulin fills are by mail, three quarters from two PBM-owned mail-order pharmacies in Lisvane; plans may require mail order only with an opt-out to retail. PBM-pharmacy contracts run by calendar year; the 2028 contracts were signed in autumn 2027. State-regulated premiums total about $9.4 billion a year for 1.4 million members and bear a 2% premium tax paid into the general fund. Many individual-market buyers receive national premium credits that cap their net premium as a share of income; about a third do not.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Tarrenmoor. Just outside: Lisvane (the two large mail-order pharmacies; border towns 20 minutes away) and Ardmere. | §1. |
| Announced / enacted / effective / expires | Bill introduced 15 January 2027; signed 12 April 2027; effective 1 January 2028; no expiry. | §9. |
| Enforcement (who, penalties, resources) | Board of Pharmacy: $1,000 fine for each overcharge, paid into the Fund; repeated violation may lead to suspension of a license or permit. The Board is funded by license and permit fees; the Act gives it no new money. The Department of Health runs the Fund through a claims contract (about $3 million a year, paid from the Fund). False attestation is an offence. | §5, §7. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Counter cap | Cap on the buyer's payment (no ontology type) | Insulin dispensed on prescription | Every "pharmacy licensed by the Board of Pharmacy under chapter 18" (U1) | §3: no more than $35 collected from a covered resident for each 30-day supply. Covered resident: uninsured, or enrolled in a plan regulated under the insurance code. | Members of self-funded plans and national programs; non-residents; insulin sold without a prescription. |
| K2 Plans pay the balance | Mandated payment | Insulin fills of state-plan members | State-regulated plans | §4(a): the pharmacy bills the balance to the plan, "which shall pay it on the terms of its pharmacy contract". | — |
| K3 Insulin Access Fund | `purchase_rebate` paid to the pharmacy | Insulin fills of uninsured residents | Fund (Department of Health) | §4(b): the pharmacy's usual and customary price less $35, but not more than wholesale acquisition cost plus 20% less $35. Usual and customary price: the price charged to a cash-paying customer who is not a covered resident. The uninsured resident attests to having no coverage (§5). | — |
| K4 Funding | Appropriation | K3 | General fund | §6: "such sums as are necessary" from general revenue; §7 fines paid into the Fund. Fiscal note: $19 million a year. | — |

Unclear provisions:
- **U1, mail-order pharmacies outside the state.** Reading U1-a: a nonresident permit holder is "licensed under chapter 18", so out-of-state mail-order pharmacies are bound by §3 and may bill the plan or the Fund. Reading U1-b: only §18-4 licensees are bound; out-of-state pharmacies collect ordinary cost sharing (or their cash price) and cannot bill the Fund. No guidance. Readings get no probability; one sign per reading is given where a sign depends on U1.

**Figures (from the record).** State-plan members: average out-of-pocket falls from about $88 to about $34 per fill; plans pay about $54 more per fill, about $34 million a year including ended rationing (about 0.36% of state-regulated premiums); premium tax on that about $0.7 million. Uninsured: with usual prices set at the Fund's limit (about $354), each fill costs the Fund about $319; total about $39 million against the fiscal note's $19 million (current cash buyers about $19 million with the end of rationing; over-the-counter buyers who obtain a prescription about $8 million; assistance-program enrollees about $10 million if dropped; administration $3 million). Fines: at most a few hundred thousand dollars a year.

**Counterfactual law.** Without the Act: pharmacies collect plan cost sharing or their cash price; no Fund; the same premium tax, insurance code, chapter 18 and national rules.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Counter cap | triangular (fixes a term of the exchange between pharmacy and covered resident) | Yes for the about 70% of state-plan members and the uninsured cash buyers who pay more than $35 (record; A-1); not binding for members already paying $35 or less | 3 for bound pharmacies (a fine and a risk of suspension attached to collecting more than $35); 3 for covered residents (the option "fill a prescription" brings a lower payment); per reading for out-of-state mail-order pharmacies (U1-a: op 3; U1-b: none) | CR-4, CR-5c, CR-6 (no price is fixed for the seller, see note), CR-11a |
| K2 Plans pay the balance | binary in effect (a payment compelled from plans, on terms of an existing contract) | Yes wherever K1 binds (A-1) | 4 for plans (they must pay the balance on each fill); 3 for plans (each insulin fill now costs the plan the full contract rate) | CR-5b, CR-5c, CR-7b, CR-8b, CR-9 (contract) |
| K3 Fund payment | binary (state gives) | Yes for uninsured fills (A-1) | 3 for pharmacies (a payment attached to dispensing to an attesting uninsured resident, tied to their own usual price); 2 for the uninsured (a $35 option opens) | CR-4, CR-5c, CR-6 (0.8: a public payer with no fixed quantity), CR-8b |
| K4 Funding | binary (state takes, unnamed payers) | Yes | 4 for taxpayers and recipients of other spending (as a group) | CR-8a, CR-8b, CR-8 (0.7 note: general budget) |
| Fines (§7) | binary | For violators only (A-16) | 3 for pharmacies (fine attached to overcharging); 4 to the Fund (receipts) | CR-4 (x: comply, y: overcharge), CR-8 (1.0 note: receipts into the same budget) |

**Note on CR-6.** K1 fixes what the buyer pays, not what the seller receives: the pharmacy still receives its contract rate (K2) or its usual price (K3). So no gap between planned purchases and sales is created at the pharmacy, and CR-6's displaced-pressure clause does not apply to pharmacies. It applies instead to the payers: a third party now pays for whatever covered residents choose, so the price no longer conveys the cost difference between products to them (CR-11a), and the pressure from payers goes to the margins open to them (utilization management, rate negotiations, the usual price that sets the Fund's payment).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| members.state_plans.over_35 | State-plan insulin users who paid more than $35 per fill (copay, coinsurance, or high-deductible members before the deductible) | Op 3: filling brings a payment of at most $35. |
| members.state_plans.hdhp | High-deductible members (subset of the above) | Op 3 on insulin; through their insurance contract (CR-9), less of their spending counts toward the deductible (A-N2). |
| members.state_plans.at_or_below_35 | State-plan insulin users already paying $35 or less | None from K1 (not binding); premiums through A-12. |
| members.state_plans.mail_order | State-plan members filling by mail from out of state | Per reading: U1-a op 3 as above; U1-b none unless they switch (A-19). |
| members.state_plans.non_insulin | The other members of state-regulated plans | Through premiums (A-12). |
| uninsured.cash_buyers | 4,500 uninsured buying analog insulin at about $320 | Op 2/3: a $35 option on attestation. |
| uninsured.otc_human_insulin | 3,000 uninsured buying human insulin without prescription at about $50 a month | Op 2: a prescription analog at $35 is now open (CR-4, x: OTC human insulin, y: prescription analog). |
| uninsured.pap_enrollees | 2,500 receiving free insulin from manufacturers' programs | Op 2 ($35 at the counter); op 1 if the manufacturers drop them (A-9). |
| non_covered.false_attesters | Self-funded members and Lisvane residents who could attest falsely | Op 3: false attestation brings $35 insulin with a risk of prosecution (A-15). |
| non_residents.cash_buyers | Visitors and non-residents buying insulin for cash at Tarrenmoor pharmacies | Through CR-9: the usual price they pay is now the price that sets the Fund's payment (A-4). |
| pharmacies.in_state | 1,050 §18-4 licensees | Op 3: fine for collecting more than $35; balance billing; Fund claims tied to their usual price. |
| pharmacies.nonresident_mail | 140 permit holders, including two large PBM-owned mail-order pharmacies | Per reading: U1-a as in-state pharmacies; U1-b not bound, cannot bill the Fund. |
| pharmacies.lisvane_border | Pharmacies in Lisvane border towns | Through CR-9 (across_border): resident and non-resident buyers re-sort (A-N1, A-4). |
| insurers.state_regulated | Plans regulated by the insurance code | Op 4/3: pay the balance on every insulin fill; may change utilization management (A-6) and premiums (A-12). |
| pbms | Pharmacy benefit managers that contract with pharmacies for plans | Through CR-9 (contract): plans now bear the cost high-deductible members bore (A-22). |
| premium_payers.insured_employers | Employers buying fully insured group plans | Through CR-9 (contract): premiums (A-12); conversion to self-funding (A-13). |
| employees.insured_employers | Their employees | Through CR-9 (employment contract): terms of employment (A-N3). |
| individual_buyers.without_credits | Individual-market buyers without premium credits | Through premiums (A-12); may drop coverage (A-14). |
| national_government.premium_credits | Payer of national premium credits | Through premiums of credit recipients (A-12). |
| manufacturers | Three national insulin makers | Through CR-9 (input_to): more units sold in Tarrenmoor; assistance programs (A-9); list prices (A-10). |
| sellers.private_label_human_insulin | National chains selling human insulin over the counter | Through CR-9 (substitute): fewer buyers (A-8, A-20). |
| producers.human_insulin | Plants making human insulin | Through CR-9 (input_to): lower output (A-21). |
| buyers.human_insulin_national | Over-the-counter buyers of human insulin anywhere | Through the national price (A-21). |
| buyers.insulin_national | Insulin payers in other states | Through list prices (A-10). |
| sellers.complements | Clinics writing prescriptions; sellers of pen needles and syringes | Through CR-9 (complement). |
| officials.insulin_access_fund | Department of Health and its claims contractor | Op 4: pays K3 out of general revenue; receives fines. |
| officials.board_of_pharmacy | Enforces K1 from a fixed fee-funded budget (A-5) | Op 3: new duties, no new money. |
| general_fund | Receives premium tax; funds K4 | Op 4 out (K4); premium tax base changes (A-12, A-13, A-14). |
| taxpayers, recipients_of_other_spending | Those who fund K4 | Op 4 (as a group). |
| organized_interests | Pharmacies, PBMs, insurers, patient groups (A-17) | CR-4 (x: accept, y: lobby) on questions the Act creates (U1 guidance, the Fund's rate). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 to K4 alter. Each sign is against the same state and time without the Act.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | members.state_plans.over_35 | price_paid (insulin, per 30-day fill at bound pharmacies) | decrease | short; medium; long | CR-1 op 3, CR-5c | A-1 |
| C-2 | members.state_plans.at_or_below_35 | price_paid (insulin, per fill) | no_change | short; medium; long | CR-1 | - |
| C-3 | uninsured.cash_buyers | price_paid (analog insulin, per fill) | decrease | short; medium; long | CR-1 op 2/3, CR-5c | A-1 |
| C-4 | insurers.state_regulated | price_paid (plan's share per insulin fill) | increase | short; medium; long | CR-1 op 4, CR-8b, CR-12b, CR-12e | A-1, A-24 |
| C-5 | officials.insulin_access_fund | subsidy_outlay | increase | short; medium; long | CR-1 op 4, CR-8b | A-1 |
| C-6 | taxpayers, recipients_of_other_spending, future_taxpayers | resources_available_other_uses | at_least_one_decrease | short; medium; long | CR-8a, CR-8b, CR-8 (0.7 general budget) | - |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-5 for compelled and prevented exchanges; CR-10a for timing; CR-8c for resources used up.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | members.state_plans.over_35, uninsured.cash_buyers | quantity_demanded (insulin, units actually used) | increase | short; medium; long | CR-4c | A-3, A-1 |
| C-8 | uninsured.otc_human_insulin | quantity_substitute (over-the-counter human insulin) | decrease | short; medium | CR-4 (x: OTC human insulin, y: prescription analog at $35) | A-8, A-1 |
| C-9 | uninsured.otc_human_insulin, sellers.complements (clinics) | quantity_complement (clinic visits to obtain an insulin prescription) | increase | short; medium | CR-9, LW-10 | A-8 |
| C-10 | members.state_plans.over_35, uninsured.cash_buyers | quantity_demanded (pens and newer analogs, relative to vials and older products) | increase | short; medium | CR-4 (x: vial, y: pen or newer analog), CR-11a | A-7, A-1 |
| C-11 | insurers.state_regulated | term_prevalence (prior authorization or step therapy on costlier insulin products) | increase | short; medium | CR-4 (x: no utilization management, y: add it), CR-6 (pressure to open margins) | A-6, A-7 |
| C-12 | members.state_plans.over_35 | wait_time (prior authorization decisions for insulin) | increase | short; medium | CR-9 (contract), CR-8c | A-6, A-7 |
| C-13 | pharmacies.in_state | net_price_received (insulin fills paid by the Fund) | increase | short; medium; long | CR-4 (x: keep usual price, y: raise it to the Fund's limit), CR-5c | A-4, A-1 |
| C-14 | non_residents.cash_buyers | price_paid (insulin cash price at Tarrenmoor pharmacies) | increase | short; medium; long | CR-9, CR-4 | A-4 |
| C-15 | pharmacies.in_state | compliance_cost | increase | short; medium; long | CR-1 op 3, CR-8c | - |
| C-16 | pharmacies.noncompliant | legal_breach (collecting more than $35 from covered residents) | increase | short; medium | CR-4 (x: comply, y: overcharge) | A-16 |
| C-17 | officials.insulin_access_fund | non_tax_receipts (fines) | increase | short; medium | CR-8b, CR-8e | A-16 |
| C-18 | officials.insulin_access_fund | subsidy_outlay (net of fines) | increase | short; medium; long | CR-8 (1.0: receipts into the same budget), CR-12e | A-1 |
| C-19 | officials.board_of_pharmacy | enforcement_cost | increase | short; medium; long | CR-1 op 3, CR-8c | A-5 |
| C-20 | officials.board_of_pharmacy | resources_available_other_uses (the Board's other licensing and inspection work) | decrease | short; medium; long | CR-8a, CR-3c | A-5 |
| C-21 | officials.insulin_access_fund | enforcement_cost (claims contract) | increase | short; medium; long | CR-1 op 4, CR-8c | - |
| C-22 | non_covered.false_attesters | legal_breach (false attestation of no coverage) | increase | short; medium | CR-4 (x: honest, y: attest falsely) | A-15 |
| C-23 | uninsured.pap_enrollees | price_paid (analog insulin) | increase | short; medium; long | CR-1 op 1 (by manufacturers' choice), CR-4 | A-9 |
| C-24 | uninsured.pap_enrollees | compliance_cost (yearly income-tested re-application) | decrease | short; medium | CR-4, CR-8c | A-9 |
| C-25 | manufacturers | resources_available_other_uses | increase | short; medium | CR-8b, CR-4 | A-9 |
| C-26 | members.state_plans, uninsured | quantity_traded (insulin fills, October to December 2027) | decrease | short (window before 1 January 2028) | CR-10a, CR-4 (x: fill now, y: wait for January) | A-11 |
| C-27 | members.state_plans, uninsured | quantity_traded (insulin fills, January 2028) | increase | short (first weeks of 2028) | CR-10a | A-11 |
| C-28 | members.state_plans.mail_order | quantity_traded (insulin fills from out-of-state mail-order pharmacies) | U1-a: decrease; U1-b: decrease | short; medium | CR-4 (x: stay, y: switch or stop shipping) | A-18, A-19 |
| C-29 | pharmacies.in_state | quantity_traded (insulin fills) | increase | short; medium; long | CR-9, CR-4 | A-3 or A-8 or A-19 |
| C-30 | organized_interests (in-state pharmacies, PBMs, insurers, patient groups) | lobbying_effort (Board guidance on U1; the Fund's payment rule; extension to other plans) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-17 |
| C-31 | residents.near_lisvane_border | cross_border_purchases (insulin filled at Lisvane pharmacies) | decrease | short; medium | CR-4 (x: Lisvane pharmacy, y: Tarrenmoor pharmacy) | A-N1 |
| C-32 | non_residents.cash_buyers | quantity_demanded (insulin at Tarrenmoor pharmacies) | decrease | short; medium | CR-4c | A-4 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Diffuse effects on the customers of employers who pay higher premiums (relation: premiums input_to their goods) are pruned at depth 3 as diffuse bystander effects; so are effects of the national list price on the Fund's cap (WAC plus 20%) beyond C-44. Health effects of more insulin use are out of scope for version 1 and are not traced.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-33 | premium_payers (insured employers, individual buyers) | price_paid (premiums of state-regulated plans) | increase | short; medium; long | CR-9 (contract), CR-5c | insulin outlay input_to premiums (contract) | A-12, A-1 |
| C-34 | members.state_plans.non_insulin | resources_available_other_uses | decrease | short; medium; long | CR-8a, CR-8b, CR-3c | insurance contract | A-12 |
| C-35 | members.state_plans.over_35 (not in high-deductible plans) | resources_available_other_uses | increase | short; medium; long | CR-8b, CR-12e | insurance contract | A-1, A-12 |
| C-36 | members.state_plans.hdhp | price_paid (other covered services before the deductible is met) | increase | short; medium; long | CR-9 (contract) | insurance contract (deductible) | A-N2, A-1 |
| C-37 | members.state_plans.hdhp | resources_available_other_uses | ambiguous | short; medium; long | CR-12b | insurance contract | A-1, A-N2 |
| C-38 | individual_buyers.without_credits | quantity_demanded (individual-market coverage) | decrease | medium | CR-4c | insurance contract | A-14, A-12 |
| C-39 | national_government.premium_credits | subsidy_outlay (national premium credits for Tarrenmoor buyers) | increase | short; medium; long | CR-9, CR-8b | premium credit contract | A-12 |
| C-40 | premium_payers.insured_employers | reclassification (conversion to self-funded plans) | increase | medium; long | CR-4 (x: insured plan, y: self-funded plan) | insurance contract | A-13, A-12 |
| C-41 | employees.insured_employers | wage_rate (-), non_wage_compensation (-), employment (-) | at_least_one_decrease | medium; long | CR-9 (employment contract), CR-5c, CR-7b | premiums input_to employment (contract) | A-12, A-N3 |
| C-42 | general_fund | tax_revenue (premium tax) | increase | short | CR-9, arithmetic | premiums (tax base) | A-12 |
| C-43 | general_fund | tax_revenue (premium tax) | ambiguous | medium; long | CR-12b | premiums (tax base) | A-12, A-13, A-14 |
| C-44 | buyers.insulin_national | price_paid (insulin list prices) | increase | long | CR-9, CR-4, CR-6 (1.0: small effects are signed) | Tarrenmoor insulin same_market_other_segment of national insulin | A-10 |
| C-45 | manufacturers | quantity_traded (insulin sold for Tarrenmoor residents) | increase | short; medium; long | CR-9, LW-10 | input_to | A-3 or A-8 |
| C-46 | sellers.complements (pen needles, syringes, supplies) | quantity_complement (insulin delivery supplies) | increase | short; medium | CR-9, LW-10 | complement | A-3 |
| C-47 | sellers.private_label_human_insulin | inventory_held (human insulin) | increase | short | CR-9, CR-10b | OTC human insulin substitute for prescription analog | A-8, A-20 |
| C-48 | buyers.human_insulin_national | price_paid (private-label human insulin, national price) | ambiguous | medium; long | CR-12b, CR-6, CR-9 | input_to (plants to chains) | A-8, A-21 |
| C-49 | pharmacies.in_state | net_price_received (insulin fills paid by plans) | no_change | short (2028) | CR-6 (0.7: existing contracts), CR-5c | PBM-pharmacy contract | A-2 |
| C-50 | pharmacies.in_state | net_price_received (insulin fills paid by plans) | ambiguous | medium; long (from 2029) | CR-12b, CR-5c, CR-7b | PBM-pharmacy contract | A-22 |
| C-51 | pharmacies.in_state | asset_value (pharmacy businesses) | ambiguous | short (from April 2027); medium | CR-7c, CR-10c, CR-12b | - | A-4, A-23 |
| C-52 | pharmacies.nonresident_mail (PBM-owned) | asset_value | U1-a: ambiguous; U1-b: decrease | short; medium | CR-7c, CR-10c | same_market_other_segment (mail and retail) | A-19 |
| C-53 | self_funded_plan_sponsors | price_paid (plan share of insulin fills of members who attest falsely) | decrease | short; medium | CR-9 (contract), CR-8b | self-funded plan contract | A-15 |
| C-54 | pharmacies.lisvane_border | quantity_traded (insulin fills) | ambiguous | short; medium | CR-9, CR-12b | across_border | A-N1, A-4 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| insurers.state_regulated, price_paid (plan share per fill), all horizons | K2 balance (CR-1, CR-8b); members choose costlier products (C-10, A-7) | plans steer to cheaper products (C-11, A-6) | Arithmetic premise A-24 (CR-12e): rate differences among steerable products are much smaller than the $54 shifted | increase (C-4) |
| officials.insulin_access_fund, subsidy_outlay net of fines | outlay (C-5) | fines (C-17) | Arithmetic on the record (CR-8 1.0 note; CR-12e): fines of a few hundred thousand dollars against $19 to $39 million | increase (C-18) |
| members.state_plans.over_35 (not high-deductible), resources_available_other_uses | cap (C-1) | premium share (C-33) | Arithmetic (CR-12e): about $650 a year against about 0.36% of a premium | increase (C-35) |
| members.state_plans.hdhp, resources_available_other_uses | cap (C-1) | other services paid in full longer (C-36); premium (C-33) | None: the class splits by other spending | ambiguous (C-37) |
| general_fund, tax_revenue (premium tax), short | added premiums (A-12) | — (conversions and drops wait for renewals) | — | increase (C-42) |
| general_fund, tax_revenue (premium tax), medium; long | added premiums (A-12) | conversions (A-13), drops (A-14) | None | ambiguous (C-43) |
| buyers.human_insulin_national, price_paid | rising unit cost (A-21) | lower demand (CR-6) | None | ambiguous (C-48) |
| pharmacies.in_state, net_price_received (plan fills), 2028 | — | — | Contract fixed for 2028 (A-2) | no_change (C-49) |
| pharmacies.in_state, net_price_received (plan fills), from 2029 | compliance cost raises the lowest acceptable rate (CR-5c) | PBM pressure (A-22) | None | ambiguous (C-50) |
| pharmacies.in_state, asset_value | more fills; higher Fund price | compliance; 2029 rates (kind 3) | None | ambiguous (C-51) |
| pharmacies.lisvane_border, quantity_traded | non-residents buying at home (A-4) | residents returning to Tarrenmoor (A-N1) | None | ambiguous (C-54) |
| members.state_plans and uninsured, quantity_traded (fills) by window | January 2028 (C-27) | October to December 2027 (C-26) | Different windows, not combined (CR-12g) | decrease (late 2027); increase (January 2028) |
| members.state_plans.mail_order, quantity_traded out of state | U1-a and U1-b both decrease | — | — | U1-a: decrease; U1-b: decrease (C-28) |

**Checked and not combined.** C-29 (in-state fills) has three same-signed chains and no opposing one: under U1-a the large PBM mail-order pharmacies may keep their members, which leaves the sign unchanged (no chain sends fills from in-state pharmacies out of state). C-45 (manufacturers' units) has no opposing chain: the end of free program supply (C-23) changes who pays, not the units used. C-7 rests on A-3; no chain lowers use because of the Act.

**Final check before the report (workflow).** (1) Uncombined chains: every key reached by chains in sections 4 to 8 is in the table above; the timing chains (C-26, C-27) are per window. (2) Group signs: employees' terms (C-41) and the general-budget payers (C-6) are groups. (3) Baseline: every sign is against Tarrenmoor without the Act, not against the fiscal note (the Fund's outlay above the note is in section 8, not a consequence). (4) Worse off is not poorer: `resources_available_other_uses` is signed only for classes that keep paying (members without insulin, C-34) or receive a transfer (C-35, C-25), and is `ambiguous` where arithmetic splits the class (C-37). (5) Timing shifts: C-26 and C-27. (6) Both sides of every transfer: see section 9. (7) Every class and rule: CR-6 was checked for pharmacies and does not apply at the counter (section 2 note); CR-7c was applied to pharmacies (C-51, C-52); CR-7c for manufacturers' shares, insurers' and PBMs' values was checked and gives no sign without premises on sizes (Tarrenmoor is 0.7% of the market), so nothing is recorded; enforcement costs for the Board and the Fund are recorded (C-19, C-21). (8) Unstated premises: A-N1 to A-N3 added. (9) No patterns were cited.

## 8. Time structure

- **Announcement and enactment.** The bill was introduced on 15 January 2027 and was not expected before (A-23); it was signed on 12 April 2027 and takes effect on 1 January 2028. From signing, the date is known, so covered residents who can store insulin defer purchases from late 2027 into January 2028 (CR-10a; C-26, C-27). High-deductible members who would have stocked up in December after meeting the deductible no longer need to. Pharmacy business values move as the Act becomes expected (CR-7c; C-51), partly from January and fully from April 2027.
- **Contracts.** PBM-pharmacy contracts for 2028 were signed in autumn 2027, after the Act was known, and are not reopened during the year (A-2), so pharmacies' total per plan fill does not change in 2028 (C-49). Rate pressure appears at the 2029 renewals (C-50). Premiums for 2028 were filed in mid-2027 and include the expected outlay (A-12; C-33).
- **Premium base.** Employers' conversions to self-funding (C-40) and individual buyers' drops (C-38) take effect at plan renewals, so they enter the premium tax only from the medium term (C-42, C-43). Each conversion also takes that employer's insulin users out of the cap.
- **The Fund's cost grows into its rules.** In the first months pharmacies learn the usual-price rule; as they set usual prices at the Fund's limit (A-4; C-13) and as over-the-counter buyers obtain prescriptions (C-8) and manufacturers drop program enrollees (C-23), the outlay grows toward the record's $39 million against the fiscal note's $19 million. The Fund has no fixed budget ("such sums as are necessary"), so pressure from claims goes to the general fund (C-6), not to waiting by claimants.
- **List prices.** List prices are set once or twice a year nationally (A-10), so C-44 is a long-run effect.
- **Human insulin supply.** Contracted volumes (A-20) make chains' stocks rise at first (C-47); the effect on the national price (C-48) comes as contracts and plant output adjust.
- Not a repeal: no metamorphic check is needed.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-6 | taxpayers, recipients_of_other_spending, future_taxpayers | resources_available_other_uses | at_least_one_decrease | Other public spending, lower taxes or less borrowing: about $39 million a year on the record's figures | CR-8a, CR-8b, CR-8 (0.7 general budget) |
| C-9 | uninsured.otc_human_insulin, sellers.complements (clinics) | quantity_complement (clinic visits to obtain an insulin prescription) | increase | Clinic fees and time spent obtaining prescriptions that OTC buyers did not need before | CR-9, LW-10 |
| C-12 | members.state_plans.over_35 | wait_time (prior authorization decisions for insulin) | increase | Patients' and prescribers' time spent on authorizations | CR-9 (contract), CR-8c |
| C-15 | pharmacies.in_state | compliance_cost | increase | Staff time and systems spent on balance billing, attestations and Fund claims | CR-1 op 3, CR-8c |
| C-19 | officials.board_of_pharmacy | enforcement_cost | increase | Board staff time on complaints and audits under the Act | CR-1 op 3, CR-8c |
| C-20 | officials.board_of_pharmacy | resources_available_other_uses (the Board's other licensing and inspection work) | decrease | Other inspections and licensing work the Board would have done | CR-8a, CR-3c |
| C-21 | officials.insulin_access_fund | enforcement_cost (claims contract) | increase | About $3 million a year of general revenue | CR-1 op 4, CR-8c |
| C-30 | organized_interests (in-state pharmacies, PBMs, insurers, patient groups) | lobbying_effort (Board guidance on U1; the Fund's payment rule; extension to other plans) | increase | Staff time and money spent seeking guidance or changes | CR-4 (x: accept, y: lobby), CR-8c |
| C-34 | members.state_plans.non_insulin | resources_available_other_uses | decrease | Purchases forgone to pay the added premium share | CR-8a, CR-8b, CR-3c |

CR-8's symmetry is applied throughout: what members and the uninsured no longer pay (C-1, C-3) is paid by plans (C-4) and the Fund (C-5); the plans' outlay is paid through premiums (C-33) by members without insulin (C-34), employers and their employees (C-41) and the national credit payer (C-39); the Fund's outlay by taxpayers or recipients of other spending (C-6); the Fund's payment for program enrollees is received by manufacturers (C-25); false attestations move payment from self-funded plans (C-53) to the Fund. Compliance, enforcement, authorization time and lobbying are used up (C-15, C-19, C-21, C-12, C-30).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Bound pharmacies comply with the $35 cap for most fills, and the payments they receive (contract rate, or the Fund's payment) exceed their acquisition cost, so they keep dispensing. | enforcement | 0.9 | Fines and license suspension; Fund pays at least wholesale cost less $35 plus the $35. | These consequences fail or lose this chain: C-1, C-3, C-4, C-5, C-7, C-8, C-10, C-13, C-18, C-33, C-35, C-36, C-37. |
| A-2 | 2028 PBM contracts with pharmacies are not reopened during the year. | other | 0.75 | Calendar-year contracts, signed in autumn 2027. | These consequences fail or lose this chain: C-49. |
| A-3 | Some covered residents used less insulin than prescribed at the old price. | other | 0.85 | 2026 survey: about 40% of uninsured cash buyers and 15% of high-deductible members. | These consequences fail or lose this chain: C-7, C-29, C-45, C-46. |
| A-4 | Most pharmacies have few cash insulin customers outside the Act, so they set their usual price at or near the Fund's limit. | other | 0.75 | Non-residents and visitors are a small share of insulin cash sales. | These consequences fail or lose this chain: C-13, C-14, C-32, C-51, C-54. |
| A-5 | The Board of Pharmacy does some enforcement work under the Act (complaints, audits of balance billing) from its existing fee-funded budget, which the Act does not raise. | revenue_use | 0.8 | The Act appropriates nothing to the Board; fee schedules are set by statute. | These consequences fail or lose this chain: C-19, C-20. |
| A-6 | Plans may and some do add prior authorization or step therapy for costlier insulin products. | other | 0.6 | The insurance code allows utilization management with 72-hour decisions; plans' practice for other drugs. | These consequences fail or lose this chain: C-11, C-12. |
| A-7 | When the patient's payment is the same for every product, some patients and prescribers choose pens or newer analogs over vials and older products. | substitutability | 0.7 | Vials are chosen now mainly for price; prescriber surveys. | These consequences fail or lose this chain: C-10, C-11, C-12. |
| A-8 | Some over-the-counter human insulin buyers obtain a prescription to buy an analog at $35. | substitutability | 0.75 | The price gap ($50 against $35); community clinic fees of about $40 a visit. | These consequences fail or lose this chain: C-8, C-9, C-29, C-45, C-47, C-48. |
| A-9 | Manufacturers apply their payer-of-last-resort clause to the Fund and drop or restrict program enrollment for Tarrenmoor residents. | other | 0.6 | Their program terms; practice with other states' funds. | These consequences fail or lose this chain: C-23, C-24, C-25. |
| A-10 | Manufacturers' list prices respond at the margin to how many sales a higher list price loses, so a smaller loss in Tarrenmoor moves them, by a small amount. | other | 0.6 | List price changes set once or twice a year; payer mix and list prices in industry studies. Size: 0.7% of national users. | These consequences fail or lose this chain: C-44. |
| A-11 | Some covered residents can defer storable insulin purchases from late 2027 to January 2028. | other | 0.65 | Unopened insulin keeps for months; high-deductible members' December stocking. | These consequences fail or lose this chain: C-26, C-27. |
| A-12 | Insurers include the added outlay in 2028 premiums, and the insurance commissioner approves it. | other | 0.8 | Rate filings in mid-2027 after signing; commissioner's practice with mandated benefits. | These consequences fail or lose this chain: C-33, C-34, C-35, C-38, C-39, C-40, C-41, C-42, C-43. |
| A-13 | Some employers near the line between insured and self-funded plans convert. | other | 0.55 | Mid-sized employers already weigh self-funding; the cap adds about 0.36% to premiums. | These consequences fail or lose this chain: C-40, C-43. |
| A-14 | Some individual-market buyers without premium credits are at the margin of buying coverage at a slightly higher premium. | substitutability | 0.55 | About a third of individual buyers lack credits; past responses to premium changes. | These consequences fail or lose this chain: C-38, C-43. |
| A-15 | Some members of self-funded plans, or residents of Lisvane, attest falsely, and pharmacies cannot easily check. | enforcement | 0.6 | Attestation at the counter; no shared coverage database for self-funded plans. | These consequences fail or lose this chain: C-22, C-53. |
| A-16 | Some pharmacies collect more than $35, and some are fined. | enforcement | 0.6 | Complaint-driven enforcement by a Board with no new staff. | These consequences fail or lose this chain: C-16, C-17. |
| A-17 | Pharmacies, PBMs, insurers and patient groups can organize at a cost below their stakes. | other | 0.85 | Existing associations; the bill's hearings. | These consequences fail or lose this chain: C-30. |
| A-18 | Under U1-a, some nonresident permit holders with few Tarrenmoor insulin patients stop shipping insulin there rather than comply with the billing and usual-price rules. | other | 0.55 | Most of the 140 permit holders ship few insulin fills to Tarrenmoor. | These consequences fail or lose this chain: C-28. |
| A-19 | Under U1-b, most state-plan members using out-of-state mail order can switch to an in-state pharmacy. | mobility | 0.85 | The insurance code's opt-out rule; 1,050 in-state pharmacies. | These consequences fail or lose this chain: C-28, C-29, C-52. |
| A-20 | Private-label human insulin cannot be cut back at once: chains buy it under contracted volumes. | durability | 0.6 | Supply contracts with the producers. | These consequences fail or lose this chain: C-47. |
| A-21 | Human insulin is made in a few plants with large fixed costs, so cost per vial rises as output contracts. | other | 0.6 | Industry structure. | These consequences fail or lose this chain: C-48. |
| A-22 | Some PBMs press insulin reimbursement rates down at the 2029 renewals because plans now bear what high-deductible members paid. | other | 0.55 | PBM practice with drugs whose cost shifts to the plan. | These consequences fail or lose this chain: C-50. |
| A-23 | The Act was not expected before its introduction in January 2027. | expectations | 0.7 | No earlier bill reached a committee. | These consequences fail or lose this chain: C-51. |
| A-24 | The contracted rates of the insulin products a plan can steer between differ by much less than the $54 a fill the cap shifts to plans. | other | 0.75 | Contracted rates of preferred and non-preferred analogs; the case's figures. | These consequences fail or lose this chain: C-4. |
| A-25 | Some individual-market insulin users drop coverage because insulin now costs $35 without it. | substitutability | 0.4 | Most also need insurance for visits, supplies and monitors. Below the cut-off. | No reported consequence rests on it (see Not reported). |
| A-26 | Some insulin users move into Tarrenmoor for the cap. | mobility | 0.2 | Moving costs far exceed the saving for almost everyone. Below the cut-off. | No reported consequence rests on it (see Not reported). |
| A-27 | Under U1-b, a PBM opens an in-state licensed mail-order pharmacy to keep its Tarrenmoor insulin fills. | other | 0.35 | Tarrenmoor is a small market for a national PBM. Below the cut-off. | No reported consequence rests on it (see Not reported). |
| A-N1 | Some Tarrenmoor residents near the border filled insulin at Lisvane pharmacies before the Act. | mobility | 0.6 | NEW. Border towns 20 minutes away; network pharmacies on both sides; commuting into Lisvane. | These consequences fail or lose this chain: C-31, C-54. |
| A-N2 | In high-deductible plans, only the member's own payment counts toward the deductible, so a $35 insulin payment counts $35, not the plan's balance. | other | 0.7 | NEW. Deductibles are defined by member cost sharing in standard plan documents; the Act does not say the balance counts. | These consequences fail or lose this chain: C-36, C-37. |
| A-N3 | Insured employers do not bear the whole premium rise themselves: some pass part of it to employees through wages, benefits or hiring. | other | 0.6 | NEW. Premiums are part of the cost of employing; employers' practice with past premium rises. | These consequences fail or lose this chain: C-41. |

**Not reported** (an assumption below 0.5):
- Individual-market insulin users drop coverage because insulin costs $35 without it (CR-4, x: insured, y: uninsured at $35; this would raise the Fund's outlay and lower premiums collected): needs A-25 (p 0.4).
- Insulin users move into Tarrenmoor for the cap (CR-4, x: here, y: there): needs A-26 (p 0.2).
- Under U1-b, a PBM opens an in-state mail-order pharmacy (CR-4, x: lose fills, y: license in state): needs A-27 (p 0.35). This would partly offset C-28 and C-52 under U1-b.

**Kind (2) chains checked (CR-12, 0.8).** No opposing chain in this analysis needed a premise below 0.5 to exist; A-25 would add a same-signed chain to C-5 and an opposing chain to C-38's premium effect only.

## 11. Report

**The policy:** From 1 January 2028, a pharmacy licensed under Tarrenmoor's pharmacy law may not collect more than $35 for a 30-day supply of insulin from a resident who is uninsured or in a state-regulated plan. Plans pay the rest on their pharmacy contract terms. For the uninsured, a state fund pays the pharmacy its usual cash price less $35, capped at wholesale cost plus 20% less $35, out of general revenue. Self-funded employer plans and national programs are not covered. It is unclear whether out-of-state mail-order pharmacies are bound (U1).

**Visible consequences:** State-plan members who paid more than $35, and uninsured cash buyers, pay $35 or less (C-1, C-3), and insulin use rises among those who rationed (C-7). Plans pay more per fill (C-4), and premiums of state-regulated plans rise (C-33). The fund pays out (C-5). Members already paying $35 or less see no change (C-2).

**Invisible consequences:**
- *Who pays:* members without insulin pay higher premiums (C-34); employees of insured employers bear part through wages, benefits or hiring (C-41); the national credit payer pays the rise for credit recipients (C-39); taxpayers or recipients of other spending fund the fund (C-6). Employers near the line self-fund (C-40), and some individual buyers drop coverage (C-38).
- *High-deductible members:* their insulin counts less toward the deductible, so they pay in full for other care for longer (C-36). Whether they come out ahead depends on their other medical spending (C-37).
- *Products and plans:* patients move to pens and newer analogs once the price no longer shows the difference (C-10). Plans add prior authorization (C-11), which adds delays (C-12).
- *Pharmacies:* they raise their usual cash price toward the fund's limit, so the fund pays more per fill (C-13) and non-resident cash buyers pay more and buy elsewhere (C-14, C-32). They bear billing and claims costs (C-15) and fill more prescriptions (C-29). Some overcharge and are fined (C-16, C-17). Their 2028 plan rates are unchanged (C-49); later rates are ambiguous (C-50).
- *Uninsured groups:* over-the-counter human insulin buyers get prescriptions for analogs (C-8), which means paying for clinic visits (C-9). Manufacturers drop program enrollees, who then pay $35 instead of nothing (C-23); they no longer re-apply (C-24), and the manufacturers gain the payment (C-25).
- *Enforcement:* the Board of Pharmacy enforces from a fixed budget, at the expense of its other work (C-19, C-20). The fund pays a claims contractor (C-21). Some people attest falsely (C-22), which moves payment from self-funded plans to the fund (C-53).
- *Timing:* fills fall in late 2027 and bunch in January 2028 (C-26, C-27).
- *Beyond Tarrenmoor:* national list prices are slightly higher (C-44); human-insulin sellers hold more stock at first (C-47); manufacturers sell more units (C-45); sales of pen needles and supplies rise (C-46). Residents near the border fill at home instead of in Lisvane (C-31). Out-of-state mail-order fills fall under either reading of U1 (C-28).
- *Lobbying:* lobbying over U1 guidance and the fund's payment rule increases (C-30).

**Ambiguous effects:** For the medium term, premium tax revenue (C-43) has the added premiums pushing it up and employer conversions and coverage drops pushing it down. Also ambiguous: pharmacies' plan rates from 2029 (C-50), pharmacy business values (C-51), the PBM mail-order pharmacies' value under U1-a (C-52), the national price of human insulin (C-48), sales at Lisvane border pharmacies (C-54), and high-deductible members' total spending (C-37). Each has chains pushing both ways and no premise in the case that settles which wins.

**Key conditions:** Most pharmacies comply (A-1, 0.9); usual prices are set at the fund's limit (A-4, 0.75); insurers pass the outlay into premiums (A-12, 0.8); steering cannot undo the $54 shift (A-24, 0.75); manufacturers drop program enrollees (A-9, 0.6); employers near the line convert (A-13, 0.55). Three premises were added: some border residents filled in Lisvane (A-N1, 0.6); only the member's payment counts toward the deductible (A-N2, 0.7); employers pass part of premium rises to employees (A-N3, 0.6).

**What this analysis cannot say:** How large any effect is, beyond the record's arithmetic. It cannot say whether the fund will cost nearer $19 or $39 million. It does not weigh the gains to insulin users against the costs to other members, employees and taxpayers, or say whether the Act is good. Health effects of more insulin use, including fewer complications and any resulting change in plans' other claims, are out of scope for version 1 and are not counted.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | members.state_plans.over_35 | price_paid (insulin, per 30-day fill at bound pharmacies) | decrease | short; medium; long | visible | B | CR-1 (op 3: K1 caps what a bound pharmacy may collect at $35); CR-5c (the terms of the exchange move within the range both accept: the pharmacy collects the rest from the plan, K2); A-1: pharmacies comply for most fills | A-1 |
| C-2 | members.state_plans.at_or_below_35 | price_paid (insulin, per fill) | no_change | short; medium; long | invisible | A | CR-1 (the cap is above what they already pay, so no operation is performed on their option of filling) | none |
| C-3 | uninsured.cash_buyers | price_paid (analog insulin, per fill) | decrease | short; medium; long | visible | B | CR-1 (op 2/3: on attestation a bound pharmacy collects $35, against about $320); CR-5c (the Fund pays the rest, K3); A-1: compliance | A-1 |
| C-4 | insurers.state_regulated | price_paid (plan's share per insulin fill) | increase | short; medium; long | visible | B | CR-1 (op 4/3: K2 makes the plan pay the balance, about $54 a fill on average); CR-8b (what members no longer pay, plans pay). Combined under CR-12b with an opposing chain (plans steer to cheaper products, C-11, A-6) and a same-signed one (members choose costlier products, C-10, A-7); CR-12e dominance by arithmetic premise A-24: contracted rates of the products a plan can steer between differ by much less than the $54 shifted, so steering cannot reverse the increase | A-1, A-24 |
| C-5 | officials.insulin_access_fund | subsidy_outlay | increase | short; medium; long | visible | B | CR-1 (op 4: K3 pays each pharmacy its usual price less $35, capped); CR-8b (every payment is a receipt: to pharmacies); the outlay against a counterfactual of none (CR-12, 0.9 note: an activity the policy creates). Sources: current cash buyers (A-1), ended rationing (A-3), OTC switchers (A-8), dropped program enrollees (A-9), false attesters (A-15), usual prices set at the limit (A-4); each raises it, none lowers it | A-1 |
| C-6 | taxpayers, recipients_of_other_spending, future_taxpayers | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | A | CR-8b and the 0.7 note on payers from the general budget (K4 funds the Fund from general revenue, so someone pays, but who is not named: a group); CR-8a (the money paid out is withdrawn from the uses it would otherwise have funded); the Fund's claims administration ($3 million) alone suffices for the sign | none |
| C-7 | members.state_plans.over_35, uninsured.cash_buyers | quantity_demanded (insulin, units actually used) | increase | short; medium; long | visible | B | CR-4c (each unit now costs the user less; the units given up for cost at the old price, valued least, are the first taken up again; LW-3); A-3: some rationed at the old price | A-3, A-1 |
| C-8 | uninsured.otc_human_insulin | quantity_substitute (over-the-counter human insulin) | decrease | short; medium | invisible | B | CR-4 (x: OTC human insulin at about $50 a month; y: a prescription analog at $35 per fill; y made better by K1 and K3, so buyers for whom the gap exceeds the cost of a prescription switch; CR-4a: none switch back because of the Act) | A-8, A-1 |
| C-9 | uninsured.otc_human_insulin, sellers.complements (clinics) | quantity_complement (clinic visits to obtain an insulin prescription) | increase | short; medium | invisible | B | CR-9 (relation: a prescription is a complement of prescription insulin; switchers, C-8, need one); LW-10; CR-8a (clinic fees of about $40 a visit are withdrawn from other uses) | A-8 |
| C-10 | members.state_plans.over_35, uninsured.cash_buyers | quantity_demanded (pens and newer analogs, relative to vials and older products) | increase | short; medium | invisible | B | CR-11a (with the patient's payment fixed at $35 for every product, the price no longer conveys the products' cost difference to the patient); CR-4 (x: a vial chosen mainly for price; y: a pen or newer analog; the price advantage of x disappears, so patients and prescribers for whom x ranked above y only because of price switch) | A-7, A-1 |
| C-11 | insurers.state_regulated | term_prevalence (prior authorization or step therapy on costlier insulin products) | increase | short; medium | invisible | B | CR-4 (x: pay for whatever product is chosen; y: require prior authorization or step therapy; the plan now bears the whole price of the costlier product, so y gains); CR-6 (the price signal removed from patients, C-10, leaves the payer's pressure to the margins still open to it: utilization terms) | A-6, A-7 |
| C-12 | members.state_plans.over_35 | wait_time (prior authorization decisions for insulin) | increase | short; medium | invisible | B | CR-9 (relation: insurance contract; the added terms, C-11, bear on members); decisions take up to 72 hours; CR-8c (time and paperwork used up) | A-6, A-7 |
| C-13 | pharmacies.in_state | net_price_received (insulin fills paid by the Fund) | increase | short; medium; long | invisible | B | CR-4 (x: keep the usual cash price at about $320; y: raise it toward the Fund's limit, about $354; y brings more on every Fund-paid fill and costs only the few cash sales to non-residents, A-4); CR-5c (the pharmacy receives $35 plus the Fund's payment); A-1: the payment covers acquisition cost | A-4, A-1 |
| C-14 | non_residents.cash_buyers | price_paid (insulin cash price at Tarrenmoor pharmacies) | increase | short; medium; long | invisible | B | CR-9 (relation: same_market_other_segment; the usual price charged to non-residents is the base of the Fund's payment); CR-4 for pharmacies as in C-13 | A-4 |
| C-15 | pharmacies.in_state | compliance_cost | increase | short; medium; long | invisible | A | CR-1 (op 3: balance billing to plans, attestation records and Fund claims attached to every covered fill); CR-8c (resources spent on complying are used up) | none |
| C-16 | pharmacies.noncompliant | legal_breach (collecting more than $35 from covered residents) | increase | short; medium | invisible | B | CR-4 (x: comply; y: collect more than $35; the Act creates the rule, so any overcharge is a breach against a counterfactual of none; complaint-driven enforcement leaves y open for some, A-16) | A-16 |
| C-17 | officials.insulin_access_fund | non_tax_receipts (fines) | increase | short; medium | invisible | B | CR-8b (fines paid by pharmacies, C-16, are received by the Fund; §7) | A-16 |
| C-18 | officials.insulin_access_fund | subsidy_outlay (net of fines) | increase | short; medium; long | invisible | B | CR-8 1.0 note (fines and outlay are two items of one budget; the net is a separate consequence); CR-12e dominance by arithmetic on the record: fines of at most a few hundred thousand dollars against an outlay of $19 to $39 million | A-1 |
| C-19 | officials.board_of_pharmacy | enforcement_cost | increase | short; medium; long | invisible | B | CR-1 (op 3: new complaints and audits under the Act); CR-8c (resources spent enforcing are used up) | A-5 |
| C-20 | officials.board_of_pharmacy | resources_available_other_uses (the Board's other licensing and inspection work) | decrease | short; medium; long | invisible | B | CR-8a and CR-3c (the Board's budget is fixed by fee schedules and the Act adds no money, so work under the Act, C-19, is withdrawn from its other work) | A-5 |
| C-21 | officials.insulin_access_fund | enforcement_cost (claims contract) | increase | short; medium; long | invisible | A | CR-1 (op 4: about $3 million a year of the Fund pays a claims contractor); CR-8c | none |
| C-22 | non_covered.false_attesters | legal_breach (false attestation of no coverage) | increase | short; medium | invisible | B | CR-4 (x: pay self-funded plan cost sharing or a cash price; y: attest falsely and pay $35; y made better by K1 and K3; the counter cannot check coverage, A-15) | A-15 |
| C-23 | uninsured.pap_enrollees | price_paid (analog insulin) | increase | short; medium; long | invisible | B | CR-4 for manufacturers (x: keep supplying free; y: apply the payer-of-last-resort clause now that a public fund pays; y made better by K3); CR-1 op 1 for enrollees (free supply removed); they pay $35 instead of nothing | A-9 |
| C-24 | uninsured.pap_enrollees | compliance_cost (yearly income-tested re-application) | decrease | short; medium | invisible | B | Following C-23: enrollees no longer re-apply each year; attestation at the counter replaces it (CR-8c: resources no longer used up) | A-9 |
| C-25 | manufacturers | resources_available_other_uses | increase | short; medium | invisible | B | CR-4 (as in C-23) and CR-8b: insulin they gave free is now paid for by the Fund at up to wholesale cost; the transfer from the Fund reaches them through pharmacies | A-9 |
| C-26 | members.state_plans, uninsured | quantity_traded (insulin fills, October to December 2027) | decrease | short (window before 1 January 2028) | invisible | B | CR-10a (a change expected from a known date alters choices now); CR-4 (x: fill in late 2027 at the old price, or stock up in December after meeting the deductible; y: wait until January at $35; storable insulin makes y open, A-11) | A-11 |
| C-27 | members.state_plans, uninsured | quantity_traded (insulin fills, January 2028) | increase | short (first weeks of 2028) | invisible | B | CR-10a (the deferred fills of C-26 are made in January, in addition to the fills the Act adds, C-7) | A-11 |
| C-28 | members.state_plans.mail_order | quantity_traded (insulin fills from out-of-state mail-order pharmacies) | U1-a: decrease; U1-b: decrease | short; medium | invisible | B | U1-a: CR-4 for small permit holders (x: ship insulin and comply with billing and usual-price rules; y: stop shipping insulin to Tarrenmoor; y gains for those with few patients, A-18), so their members move to other pharmacies. U1-b: CR-4 for members (x: out-of-state mail order at ordinary cost sharing; y: an in-state pharmacy at $35; y made better, and the opt-out rule keeps y open, A-19) | A-18, A-19 |
| C-29 | pharmacies.in_state | quantity_traded (insulin fills) | increase | short; medium; long | invisible | B | CR-9 (more units used, C-7; OTC switchers, C-8; under either reading, members leaving out-of-state mail order, C-28). Independent chains with the same sign (CR-12d): any one suffices | A-3 or A-8 or A-19 |
| C-30 | organized_interests (in-state pharmacies, PBMs, insurers, patient groups) | lobbying_effort (Board guidance on U1; the Fund's payment rule; extension to other plans) | increase | short; medium | invisible | B | CR-4 (x: accept; y: lobby; the Act creates the questions, so the counterfactual contest is none, CR-4 1.0 note); CR-8c (resources spent lobbying are used up) | A-17 |
| C-31 | residents.near_lisvane_border | cross_border_purchases (insulin filled at Lisvane pharmacies) | decrease | short; medium | invisible | B | CR-4 (x: fill at a Lisvane pharmacy at ordinary cost sharing; y: fill at a Tarrenmoor pharmacy at $35; y made better) | A-N1 |
| C-32 | non_residents.cash_buyers | quantity_demanded (insulin at Tarrenmoor pharmacies) | decrease | short; medium | invisible | B | CR-4 (x: buy at a Tarrenmoor pharmacy at the raised usual price, C-14; y: buy at home or in Lisvane) | A-4 |
| C-33 | premium_payers (insured employers, individual buyers) | price_paid (premiums of state-regulated plans) | increase | short; medium; long | visible | B | CR-9 (relation: insurance contract; plans' outlay rises, C-4); CR-5c (the range of acceptable premiums moves up); A-12: insurers file and the commissioner approves | A-12, A-1 |
| C-34 | members.state_plans.non_insulin | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-8b (the higher premium, C-33, funds payments to insulin users); CR-3c (they keep paying the premium: coverage is not given up for a 0.36% rise, except at the margin, C-38) | A-12 |
| C-35 | members.state_plans.over_35 (not in high-deductible plans) | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-8b (the cap transfers to them about $54 a fill); against their share of the premium rise (C-33), CR-12e dominance by arithmetic: about $650 a year saved against about 0.36% of a premium | A-1, A-12 |
| C-36 | members.state_plans.hdhp | price_paid (other covered services before the deductible is met) | increase | short; medium; long | invisible | B | CR-9 (relation: insurance contract; insulin payments of $35 instead of about $290 count toward the deductible, A-N2, so the deductible is met later and more of other services is paid in full) | A-N2, A-1 |
| C-37 | members.state_plans.hdhp | resources_available_other_uses | ambiguous | short; medium; long | invisible | B | CR-12b: (+) insulin paid at $35 instead of about $290 (C-1); (-) other services paid in full for longer (C-36) and the premium rise (C-33). Arithmetic splits the class: a member with no other spending gains; a member whose other spending alone exceeds the deductible pays $35 a fill more in total than before until the out-of-pocket maximum. No premise on the distribution of other spending is in the case | A-1, A-N2 |
| C-38 | individual_buyers.without_credits | quantity_demanded (individual-market coverage) | decrease | medium | invisible | B | CR-4 (x: buy coverage at the higher premium, C-33; y: go without; buyers at the margin switch) | A-14, A-12 |
| C-39 | national_government.premium_credits | subsidy_outlay (national premium credits for Tarrenmoor buyers) | increase | short; medium; long | invisible | B | CR-9 (relation: the credit pays the premium above a share of income; C-33); CR-8b (the national payer bears the rise for credit recipients, whose net premium does not change) | A-12 |
| C-40 | premium_payers.insured_employers | reclassification (conversion to self-funded plans) | increase | medium; long | invisible | B | CR-4 (x: stay fully insured at the higher premium and under the cap; y: self-fund, outside state law; y made relatively better for employers near the line) | A-13, A-12 |
| C-41 | employees.insured_employers | wage_rate (-), non_wage_compensation (-), employment (-) | at_least_one_decrease | medium; long | invisible | B | CR-9 (relation: employment contract; the premium, C-33, is part of the cost of employing); CR-5c (the range of acceptable terms moves); CR-7b (the burden is shared unless employers bear it all; A-N3) | A-12, A-N3 |
| C-42 | general_fund | tax_revenue (premium tax) | increase | short | invisible | B | Arithmetic on the record: 2% of the added premiums (about $0.7 million), A-12; conversions and drops take effect only at renewals, so not in the first year | A-12 |
| C-43 | general_fund | tax_revenue (premium tax) | ambiguous | medium; long | invisible | B | CR-12b: (+) 2% of the added premiums (A-12); (-) whole premiums leave the base when employers self-fund (C-40, A-13) and when individual buyers drop coverage (C-38, A-14). No premise on sizes | A-12, A-13, A-14 |
| C-44 | buyers.insulin_national | price_paid (insulin list prices) | increase | long | invisible | B | CR-4 for manufacturers (x: a lower list price, y: a higher one; fewer Tarrenmoor sales are lost at a higher list price, since covered residents pay $35 whatever it is, so y gains at the margin, A-10); CR-6 1.0 note: small effects are signed (Tarrenmoor is 0.7% of users) | A-10 |
| C-45 | manufacturers | quantity_traded (insulin sold for Tarrenmoor residents) | increase | short; medium; long | invisible | B | CR-9 (relation: insulin from manufacturers input_to pharmacy fills; more units used, C-7, and OTC switchers, C-8). Independent chains (CR-12d) | A-3 or A-8 |
| C-46 | sellers.complements (pen needles, syringes, supplies) | quantity_complement (insulin delivery supplies) | increase | short; medium | invisible | B | CR-9 (relation: needles and syringes are complements of insulin in use; more insulin used, C-7) | A-3 |
| C-47 | sellers.private_label_human_insulin | inventory_held (human insulin) | increase | short | invisible | B | CR-9 (relation: substitute; OTC buyers leave, C-8); CR-10b (contracted volumes cannot be cut at once, A-20, so stocks build) | A-8, A-20 |
| C-48 | buyers.human_insulin_national | price_paid (private-label human insulin, national price) | ambiguous | medium; long | invisible | B | CR-12b: (-) CR-6 (less demand at each price, C-8, moves the price toward a lower level); (+) CR-9 and A-21 (output contracts in plants with large fixed costs, so cost per vial rises, CR-12 1.0 note). Signed though small (Tarrenmoor buyers are a tiny share) | A-8, A-21 |
| C-49 | pharmacies.in_state | net_price_received (insulin fills paid by plans) | no_change | short (2028) | invisible | B | K2 makes plans pay the balance on the terms of the existing contract, so the pharmacy's total per fill is the contract rate; CR-6 0.7 note (terms fixed by contracts count as regulated while they last, A-2) | A-2 |
| C-50 | pharmacies.in_state | net_price_received (insulin fills paid by plans) | ambiguous | medium; long (from 2029) | invisible | B | CR-12b: (-) PBMs press rates down at renewal because plans now bear what members paid (A-22; CR-5c); (+) CR-5c: pharmacies' added cost of balance billing (C-15) raises the lowest rate they accept. No premise on which dominates | A-22 |
| C-51 | pharmacies.in_state | asset_value (pharmacy businesses) | ambiguous | short (from April 2027); medium | invisible | B | CR-10c and CR-7c (expected yields are capitalized when the Act becomes expected, partly from January 2027, A-23). CR-12b: (+) more fills (C-29) and a higher price on Fund fills (C-13); (-) compliance cost (C-15) and the 2029 rate chain (C-50, itself ambiguous: kind 3) | A-4, A-23 |
| C-52 | pharmacies.nonresident_mail (PBM-owned) | asset_value | U1-a: ambiguous; U1-b: decrease | short; medium | invisible | B | U1-b: CR-7c (members switch to in-state pharmacies, C-28, A-19; the expected fall in fills is borne by the owners when the Act becomes expected). U1-a: (+) fills paid at $35 plus balance and more units; (-) compliance cost; CR-12b, no premise | A-19 |
| C-53 | self_funded_plan_sponsors | price_paid (plan share of insulin fills of members who attest falsely) | decrease | short; medium | invisible | B | CR-9 (relation: plan contract; a member who attests falsely, C-22, fills outside the plan, so the plan pays nothing for that fill); CR-8b (the Fund pays instead, C-5) | A-15 |
| C-54 | pharmacies.lisvane_border | quantity_traded (insulin fills) | ambiguous | short; medium | invisible | B | CR-12b: (-) Tarrenmoor residents who filled there return home (C-31, A-N1); (+) non-residents who bought for cash in Tarrenmoor buy there instead (C-32, A-4). No premise on sizes | A-N1, A-4 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-056-C1: Health effects of ended rationing (fewer complications, lower later claims for plans) are out of scope for version 1. These would form an opposing chain to C-4 and C-33 over the long run, which version 1 cannot record. This is a scope limit, not a calculus gap (out of scope).
- No other step lacked a core rule. Every consequence was derived from CR-1 to CR-12, LW-3 and LW-10, and arithmetic on the record's figures.

**(b) Core-rule wording that was hard to apply.**
- CR-1 has no operation for a cap on what the buyer pays while the seller's receipt is set by a third party (K1 with K2 and K3). It is op 3 for both sides, but CR-6's displaced-pressure clause, written for a price "prevented from moving", does not say whether it applies when only the buyer's share is fixed. It was read as applying to the payers' margins (utilization terms, rate renegotiation, the usual price), not to the pharmacy counter.
- CR-6, 0.8 note on a public payer with no fixed quantity: the Fund's payment depends on a price the seller sets (the usual price). The note does not cover a payment indexed to the payee's own posted price. The response (C-13) was derived directly from CR-4.
- CR-3, note on "worse off is not poorer": for high-deductible members the transfer interacts with a nonlinear contract term (the deductible). The arithmetic splits the class by other spending, and the rule does not say whether to split or to record `ambiguous` (both done: C-36 and C-37).
- CR-12d with independent chains: there is no notation for "any one of these premises" in the assumptions column. "A-3 or A-8" was used (C-29, C-45).

**(c) Vocabulary missing from the ontology.**
- No instrument type for a cap on a buyer's payment that leaves the seller's receipt unchanged (a "cost-sharing cap"); nor for a mandated payment by a third party under an existing contract (K2).
- No variable for coverage choice (insured or self-funded; insured or uninsured): `reclassification` and `quantity_demanded (coverage)` were used.
- No variable for the deductible or out-of-pocket position within a contract year.
