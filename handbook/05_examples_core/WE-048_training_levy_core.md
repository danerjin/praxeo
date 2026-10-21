# WE-048 / Analysis: Apprenticeship training levy with vouchers that lapse to a small-firm fund

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**The Estrava Apprenticeship Levy Act 2027.** Estrava has about 5.2 million employees and 420,000 employers. About 9,500 employers have an annual payroll above 3 million crowns (62% of employees, 380 billion crowns of wages); 45 have payrolls above 1 billion (110 billion in total); about 1,100 have payrolls between 2.7 and 3.3 million. Employers under common control count as one. Halvard, to the north, has no levy; cross-border employment is small. Before the Act about 58,000 approved apprenticeships started a year, 150,000 were in training, at an average provider fee of 9,000 crowns per apprentice-year (about 1.35 billion a year, paid by employers; levy payers about 0.74 billion of it; 70% of levy payers bought none in 2026). About 600 large employers run in-house training units (about 2.1 billion a year on programs that are not approved apprenticeships); about 400 of the programs could meet an approved standard.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Republic of Estrava; Halvard (no levy) to the north | Act s. 1 |
| Announced / enacted / effective / expires | 1 March 2027 (budget statement and draft bill) / 1 November 2027 / levy on payroll from 1 April 2028, vouchers credited monthly from May 2028, first lapse May 2030, Fund pays from 1 July 2030 / none | Budget statement; Act s. 2, 16 |
| Enforcement (who, penalties, resources) | Revenue Service collects through payroll withholding within its existing budget. National Skills Agency (NSA) keeps voucher accounts, registers and audits providers (40 million crowns a year from the general budget). Misused vouchers repaid with a 50% penalty; misusing providers deregistered. | Act s. 11, 18 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Levy | `mandate_with_charge` (with K2) | Payroll | Employers whose payroll in the levy year exceeds 3 million crowns | 0.5% of the whole payroll (a notch: 15,000 crowns at 3 million), capped at 5 million crowns per employer a year (reached at 1 billion of payroll). About 1.6 billion a year. Threshold and cap fixed in crowns. | Payroll of 3 million or less |
| K2 Vouchers | refund conditional on a purchase (with K1) | Approved apprenticeship training | Levy payers | One crown of voucher per crown of levy. A voucher pays an approved provider the funding band for the standard (4,000 to 24,000 crowns per apprentice-year, set at the 2026 median fee), whatever the provider's fee; the provider may charge the employer any excess and may not rebate any part of the band. Up to 25% of a year's vouchers may be transferred to other employers "without payment or other consideration". Vouchers lapse 24 months after credit. Bands reviewed every two years. | - |
| K3 Small Firm Training Fund | `per_unit_subsidy` | Approved apprenticeship training at small employers | NSA | Receives lapsed vouchers only; pays 90% of the band for apprentices at employers with payroll of 3 million or less, first come, first served each quarter, while its balance lasts. | - |
| K4 Administration | Enforcement | K1 to K3 | NSA, Revenue Service | As above. | - |

**Existing rules.** Approved apprenticeship standards (12-month minimum, 20% of paid hours off the job, an end test). They stay in place in the counterfactual.

**Counterfactual.** Estrava without the Act: employers buy approved training at their own cost; no levy, vouchers or Fund.

Unclear provisions:
- **U1, in-house training.** s. 9(4) (providers independent of the employers whose apprentices they train, "save as regulations provide for employers training their own apprentices") against s. 14(3) ("No part of a voucher shall return to the employer that redeemed it"). **U1-a:** an employer's in-house unit, including an existing program that meets a standard, can register as an employer-provider and be paid the band from the employer's own vouchers. **U1-b:** no payment from an employer's vouchers to its own unit; in-house units may train only other employers' apprentices. Readings get no probability.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Levy | binary (state takes) | Yes, collected through withholding (A-1) | Per range (CR-1, 0.9): between 3 million and 1 billion of payroll, op 3 (a charge of 0.5% attached to each crown of payroll, and a jump of 15,000 crowns attached to crossing 3 million); above 1 billion, op 4 (a fixed 5 million that no payroll choice changes, A-28) | CR-3, CR-4, CR-7b, CR-7c, CR-8, CR-10 |
| K2 Vouchers | binary (state gives back, conditional) | Yes for levy payers whose vouchers exceed the approved training they would have bought (A-2) | Op 3 on the option 'buy approved training' (paid from vouchers up to the band); op 3 on 'transfer vouchers' (allowed up to 25%, without consideration); op 1 (no rebate of the band, no consideration for transfers) | CR-3 (refund note, 0.9 standard note), CR-4, CR-5c, CR-6, CR-7, CR-9 |
| K1 + K2 together | per class: a charge refunded in full to those who buy at least the levy in approved training anyway (full users); a net charge on payroll for the rest | A-2 | For full users only the cost of claiming and the time the money is held remain (CR-3 note) | CR-3, CR-12 |
| K3 Fund | binary (state gives, budget fixed by receipts) | Yes once lapses occur (A-2); demand may exceed receipts (A-23) | Op 3 on 'buy approved training' for small employers, 90% of the band | CR-4, CR-6 (0.7 public supply), CR-8 (0.7 residual claimant; 0.8 capped budget) |
| K4 Administration | binary | Yes | Op 4 (40 million from the general budget); op 3 (audits and penalties attached to misuse) | CR-8b, CR-8c, CR-4 (x: comply, y: violate) |

U1 changes the operation for employers with in-house units: under U1-a, op 2 (the option 'pay own unit from own vouchers', granted case by case, A-10); under U1-b, no such option.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| employers.levy.full_users | Levy payers whose approved training without the Act would have cost at least their levy | Levy refunded as vouchers they spend on training they would have bought; bear claiming and the time money is held |
| employers.levy.with_unspent_balance | Levy payers whose vouchers exceed the approved training they would have bought (partial users and non-users, A-2) | Approved training up to the band now costs no cash out of vouchers that would otherwise lapse (op 3); transfer is open (op 3) |
| employers.levy.non_recovering | Levy payers that do not recover all of their levy (vouchers lapse or are transferred) | Net charge on payroll (op 3 below the cap, op 4 above) |
| employers.levy.capped | The 45 employers above 1 billion of payroll | Op 4: fixed 5 million, no marginal charge on payroll (A-28) |
| employers.near_threshold.non_training | Employers near 3 million that do not train | Crossing 3 million brings 15,000 crowns of levy and ends Fund eligibility |
| employers.in_house | About 600 employers with in-house units | U1-a: own unit paid from own vouchers; U1-b: own unit not payable from own vouchers |
| employers.transfer_recipients | Employers that receive transferred vouchers | Approved training without cash outlay, up to the band (gift, CR-5 0.7) |
| employers.small | Employers with payroll of 3 million or less | Through CR-9 (same_market_other_segment): compete for provider capacity; from July 2030, op 3: 90% of the band paid by the Fund while it lasts |
| workers.levy_employers | Employees of levy payers | Through CR-5c and CR-7b: training received as a term; share of the levy wedge |
| candidates.apprenticeship | New hires and existing staff who may enroll | More places offered (CR-9, contract) |
| workers.qualified_trades | Holders of qualifications in trades where apprenticeships are a large share of entry | Through CR-9: more completers compete for the same jobs |
| providers.approved | Registered approved providers | Paid the band whatever their fee (op 3); may not rebate (op 1); more buyers |
| providers.prospective | Would-be providers | Entry brings voucher-funded demand (CR-4, x: stay out, y: register) |
| workers.trainers | Owners of the labor providers need | Through CR-9 (input_to) |
| buyers.unapproved_training | Buyers of other training that uses the same trainers | Through CR-9 (input_to, same means) |
| sellers.contract_agency_labor | Contractors and agencies | Through CR-9 (substitute for payroll) |
| residual_claimant (Small Firm Training Fund) | Receives lapsed vouchers | Receipts from 2030 |
| officials.nsa, officials.revenue_service | Administer and collect | Op 4 (appropriation), op 3 (collection duty without new budget, A-29) |
| taxpayers | Fund the NSA appropriation | Op 4 via the general budget |
| neighboring_jurisdictions (Halvard employers) | Possible destination of payroll | A-31 (p 0.2): not reported |
| buyers.current (of levy payers' output) | Through CR-9 (input_to) | A-27 (p 0.2): not reported |
| employers' federations, providers' and small-firm associations | Political action | CR-4 (x: accept, y: lobby) |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | officials.revenue_service (levy collected) | tax_revenue | increase | medium; long | CR-1 op 3/op 4, CR-8b | A-1 |
| C-2 | employers.levy.non_recovering | resources_available_other_uses | decrease | medium; long | CR-1, CR-3 (note), CR-8a | A-1, A-2 |
| C-3 | employers.levy.with_unspent_balance | price_paid (cash outlay per approved apprentice-year, up to the band) | decrease | medium; long | CR-1 op 3 | A-2 |
| C-4 | employers.levy (all bound) | compliance_cost | increase | medium; long | CR-1 op 3, CR-3 (refund note), CR-8c | A-1 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | employers.levy.with_unspent_balance | quantity_demanded (approved apprenticeship training) | increase | medium; long | CR-4, CR-4c | A-2, A-4 |
| C-6 | candidates.apprenticeship | enrollment (approved apprenticeships) | increase | medium; long | CR-4, CR-5, CR-9 | A-2, A-3, A-4 |
| C-7 | employers.levy.with_unspent_balance | reclassification (existing staff and training fitted to approved standards) | increase | medium; long | CR-4 | A-2, A-9, A-24 |
| C-8 | employers.levy.with_unspent_balance | hours_worked (production hours of enrolled existing staff) | decrease | medium; long | CR-1 op 3 (existing rule), CR-8a | A-2, A-4, A-24 |
| C-9 | workers.levy_employers | non_wage_compensation (approved training received) | increase | medium; long | CR-5c | A-2, A-3, A-4 |
| C-10 | employers.transfer_recipients | resources_available_other_uses | increase | medium; long | CR-4, CR-5 (gift), CR-8b | A-2, A-14 |
| C-11 | employers.transfer_recipients | quantity_demanded (approved apprenticeship training) | increase | medium; long | CR-4, CR-4c | A-2, A-14, A-26 |
| C-12 | employers.levy.with_unspent_balance, employers.transfer_recipients | legal_breach (transfers with undisclosed consideration) | increase | medium; long | CR-6, CR-4 (x: comply, y: violate) | A-2, A-14, A-15 |
| C-13 | employers.near_threshold.non_training | earnings (payroll held at or below 3 million) (−), reclassification (+) | at_least_one_as_stated | medium; long | CR-1 (0.9 per range), CR-4 | A-5 |
| C-14 | employers.levy (all bound) | reclassification (work moved to contractors, agency staff or unrelated entities) | increase | medium; long | CR-4 | A-6 |
| C-16 | workers.levy_employers, employers.levy.non_recovering | wage_rate (−) [workers]; return_on_capital (−) [employers] | at_least_one_decrease | medium; long | CR-1 op 3, CR-7b | A-2, A-7 |
| C-17 | workers.levy_employers (at non-recovering employers) | employment (other than apprentices) (−), hours_worked (−) | at_least_one_decrease | medium; long | CR-4c, CR-7b | A-2, A-7, A-8 |
| C-18 | workers.levy_employers | employment (apprentices) | increase | medium; long | CR-4, CR-5 | A-2, A-3, A-4 |
| C-19 | workers.levy_employers (at non-recovering employers) | employment (total) | ambiguous | medium; long | CR-12b (two items) | A-2, A-3, A-4, A-7, A-8 |
| C-20 | employers.levy.capped | employment (through the levy wedge) | no_change | medium; long | CR-1 (0.9, op 4 above the cap), CR-4 (change in means alone) | A-28 |
| C-23 | providers.prospective | entry_rate | increase | medium; long | CR-4, CR-7a | A-2, A-4, A-30 |
| C-28 | employers.levy.with_unspent_balance | quantity_traded (approved starts, 1 Mar 2027 to Apr 2028) | decrease | short | CR-10a, CR-4 | A-2, A-12 |
| C-29 | employers.levy.with_unspent_balance | quantity_traded (approved starts, May to Dec 2028) | increase | medium | CR-10a, CR-4 | A-2, A-4, A-12 |
| C-30 | workers.levy_employers | earnings (discretionary pay dated March 2028) | increase | short | CR-10a, CR-4 | A-N2 |
| C-31 | workers.levy_employers | earnings (discretionary pay dated April 2028 to March 2029) | decrease | medium | CR-10a, CR-4 | A-N2 |
| C-41 | employers.levy (federations) | lobbying_effort (against the levy, or for a higher threshold) | increase | short; medium; long | CR-4, CR-8c | A-2, A-11 |
| C-42 | providers.approved, employers.small (associations) | lobbying_effort (to keep or widen vouchers, bands and the Fund) | increase | medium; long | CR-4, CR-8c | A-11, A-25 |
| C-43 | employers.in_house | lobbying_effort (on the employer-provider regulations) | increase | short; medium | CR-4, CR-8c, CR-10a | A-11 |
| C-44 | employers.in_house | reclassification (in-house programs registered and paid from own vouchers) | U1-a: increase; U1-b: no_change | medium; long | CR-1 op 2 (U1-a), CR-4 | A-9, A-10 |
| C-45 | employers.in_house | quantity_substitute (in-house training) | U1-a: increase; U1-b: decrease | medium; long | CR-4 | A-18, A-20, A-19 |
| C-46 | employers.in_house | compliance_cost (applications for employer-provider registration) | U1-a: increase; U1-b: no_change | short; medium | CR-1 op 2 (case by case), CR-4, CR-8c | A-10, A-20 |
| C-47 | officials.nsa | enforcement_cost | increase | medium; long | CR-1 op 4, CR-8c | - |
| C-49 | officials.revenue_service | enforcement_cost (collecting the levy) | increase | medium; long | CR-1 op 3, CR-8c | A-1 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Chains to buyers of levy payers' output (input_to) need A-27 (p 0.2) and stop; payroll moved to Halvard (across_border) needs A-31 (p 0.2) and stops.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-15 | sellers.contract_agency_labor | quantity_substitute (contract and agency services sold to levy payers) | increase | medium; long | CR-9, CR-4 | contract labor substitute for payroll (partial) | A-6 |
| C-21 | providers.approved | net_price_received (per apprentice-year) | increase | medium; long | CR-1, CR-6, CR-12d | voucher-funded training is the providers' output | A-16 (or A-2, A-4, A-17) |
| C-22 | providers.approved | quantity_traded (approved training) | U1-a: ambiguous; U1-b: increase | medium; long | CR-9, CR-4, CR-6, CR-12b | in-house training substitute for external approved training (close) | A-2, A-4, A-17, A-18, A-19, A-26 |
| C-24 | providers.approved | asset_value (provider businesses) | increase | short (from announcement) | CR-7c, CR-10c | - | A-2, A-4, A-17, A-30 |
| C-25 | workers.trainers | wage_rate | increase | medium | CR-9, LW-10, CR-7a | trainers' labor input_to approved training (close) | A-2, A-4, A-17 |
| C-26 | employers.small | price_paid (provider fee per apprentice-year, before the Fund) | increase | medium | CR-9, CR-6 | small employers' training same_market_other_segment of levy payers' (close) | A-2, A-4, A-17 |
| C-27 | employers.small | quantity_traded (approved training, before July 2030) | decrease | medium | CR-4c, CR-8a, CR-10a | as above | A-2, A-4, A-17 (or A-13) |
| C-32 | residual_claimant (Small Firm Training Fund) | non_tax_receipts (lapsed vouchers) | increase | long | CR-1, CR-8b | - | A-2 |
| C-33 | employers.small (funded starts) | price_paid (approved training) | decrease | long | CR-1 op 3, CR-5c, CR-12b | - | A-2, A-N1 |
| C-34 | employers.small | quantity_demanded (approved training) | increase | long | CR-4, CR-4c | - | A-2, A-26 |
| C-35 | employers.small | wait_time (for Fund support) | increase | long | CR-6 (0.7), CR-8 (0.8) | - | A-2, A-23 |
| C-36 | employers.small (unfunded starts) | price_paid (provider fee per apprentice-year) | increase | long | CR-9, CR-6 | as C-26 | A-2, A-17, A-23 |
| C-37 | employers.small | quantity_traded (approved training) | ambiguous | long | CR-12b | as C-26 | A-2, A-17, A-23, A-26 |
| C-38 | employers.small (inframarginal) | resources_available_other_uses | increase | long | CR-8b | - | A-2, A-22 |
| C-48 | taxpayers, recipients of other spending | resources_available_other_uses | at_least_one_decrease | medium; long | CR-8b, CR-8 (0.7) | - | - |
| C-50 | employers.levy.non_recovering (owners) | asset_value | decrease | short (from announcement) | CR-7c, CR-10c | - | A-1, A-2, A-30 |
| C-51 | workers.qualified_trades | wage_rate | decrease | long | CR-9, CR-6 | completers substitute for qualified workers (close in some trades) | A-2, A-3, A-4, A-21 |
| C-52 | buyers.unapproved_training | price_paid | increase | medium | CR-9, CR-7a | trainers' labor input_to other training (partial) | A-2, A-4, A-17 |
| C-53 | officials.revenue_service | resources_available_other_uses (other collection work) | decrease | medium; long | CR-8a | - | A-1, A-29 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| workers.levy_employers at non-recovering employers, employment (total), medium; long | apprentice places funded by vouchers (CR-4, CR-5; A-2, A-3, A-4) | levy wedge on payroll (CR-1 op 3, CR-4c; A-7, A-8) | None: both chains have premises at p ≥ 0.5 (kind 2) | ambiguous (C-19); the two items are recorded separately (C-17, C-18) |
| providers.approved, quantity_traded, medium; long | voucher demand (A-2, A-4); Fund demand, long (A-26); U1-b: in-house employers buy external (A-19) | U1-a: employers move external training in-house (A-18) | None under U1-a | U1-a: ambiguous; U1-b: increase (C-22) |
| providers.approved, net_price_received | band above fee (A-16); more demand at limited capacity (A-17) | below-band providers barred from rebating cannot cut price (no chain down); bands fixed in crowns (no chain down against the counterfactual) | Not needed: no derived opposing chain | increase (C-21) |
| employers.small, quantity_traded, long | Fund pays 90% of the band (A-26) | higher fees for starts the Fund cannot cover (A-17, A-23) | None | ambiguous (C-37) |
| employers.small, price_paid, long (funded starts) | fees pushed up by voucher and Fund demand (A-17) | 90% of the band paid by the Fund | A-N1: the fee rise is smaller than 90% of the band (empirical, p 0.8) | decrease (C-33) |
| employers.levy.with_unspent_balance, approved starts | from May 2028 (C-29) | announcement window (C-28) | Different windows, not combined (CR-12g) | decrease (short window); increase (medium) |
| workers.levy_employers, earnings (discretionary pay) | March 2028 (C-30) | levy year 2028-29 (C-31) | Different windows | increase (short); decrease (medium) |
| workers.levy_employers, non_wage_compensation | training received (C-9) | possible cut in other non-wage terms as part of the wedge (CR-7b) | The wedge is recorded as a group over wage_rate and return_on_capital (C-16); a cut in other non-wage terms would need its own premise, which the case lacks (kind 1 note) | increase for the training item only (C-9); no total signed |
| employers.levy.capped, employment | - | - | Levy is op 4 above the cap; no marginal chain | no_change (C-20) |

CR-12f: for full users the levy and the vouchers cancel by construction except for claiming and the time the money is held; no resources_available_other_uses consequence is reported for them (C-4 records the claiming cost).

## 8. Time structure

Horizons: **short** = 1 March 2027 (announcement) to March 2028; **medium** = April 2028 (levy, vouchers from May) to June 2030; **long** = from July 2030 (Fund paying; first lapses May 2030).

- **Announcement.** The levy became expected on 1 March 2027 and was expected to last (A-30). Owners of levy payers that will not recover it bear the capitalized cost then (C-50), and providers' businesses gain (C-24) (CR-7c, CR-10c). Levy payers with unspent balances to come hold back planned starts until vouchers can pay for them (C-28, C-29); discretionary pay may be dated before the first levy month (C-30, C-31).
- **First lapse and the Fund.** Lapses begin in May 2030, so the Fund has no receipts before then; small employers who know the opening date delay starts to July 2030 (A-13; same direction as C-27, then the long-run chains C-33 to C-37). The Fund's receipts depend on how much levy payers fail to spend or transfer; as levy payers learn to use or transfer their balances (CR-10b: training capacity and in-house registrations are stocks built over time), receipts may fall over time; no sign is given for that path.
- **Fixed crowns.** The threshold, cap and bands are fixed in crowns while nominal wages grow about 3% a year. More employers cross 3 million each year (the levy base and C-1 grow; more employers face the notch); the cap is reached by more employers over time (A-28 holds only now). Bands fall behind fees between two-yearly reviews, so the cash excess employers pay over the band, and the 10% plus excess small employers pay, rise between reviews (arithmetic on the case figures).
- **Durability.** Provider capacity, trainers and in-house registrations are stocks that change only through flows (CR-10b), so C-21 and C-26 are largest in the medium run, and entry (C-23) narrows them later; no long-run price sign is claimed beyond the band floor.
- **Qualified workers.** Added completers enter the labor market only after at least 12 months of training; C-51 is long-run.
- **Levy timing.** Levy is paid monthly from April 2028 and vouchers are credited the month after; full users bear the time the money is held (CR-3 note), recorded within C-4.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-2 | employers.levy.non_recovering | resources_available_other_uses | decrease | Purchases, investment or saving forgone out of levy not recovered | CR-3 (note), CR-8a |
| C-4 | employers.levy (all bound) | compliance_cost | increase | Payroll and voucher-account work, claims, time money is held | CR-1, CR-3, CR-8c |
| C-8 | employers.levy.with_unspent_balance | hours_worked (production hours of enrolled existing staff) | decrease | Output not produced during off-the-job hours | CR-1, CR-8a |
| C-27 | employers.small | quantity_traded (approved training, before July 2030) | decrease | Training not bought while levy payers draw on provider capacity | CR-4c, CR-8a |
| C-47 | officials.nsa | enforcement_cost | increase | 40 million crowns a year | CR-8c |
| C-48 | taxpayers, recipients of other spending | resources_available_other_uses | at_least_one_decrease | Other spending or private uses of the 40 million | CR-8b |
| C-49 | officials.revenue_service | enforcement_cost (collecting the levy) | increase | Staff time of the Revenue Service | CR-8c |
| C-53 | officials.revenue_service | resources_available_other_uses (other collection work) | decrease | Other collection work not done | CR-8a |
| C-41, C-42, C-43 | federations, providers, small-firm groups, in-house employers | lobbying_effort | increase | Staff time and money spent on political action | CR-8c |
| C-46 | employers.in_house | compliance_cost (applications) | U1-a: increase; U1-b: no_change | Effort spent seeking registration | CR-8c |
| C-52 | buyers.unapproved_training | price_paid | increase | Trainers' time drawn from other training | CR-8a, CR-9 |

CR-8b, both sides of each transfer: the levy taken from payers (C-1, C-2) returns as vouchers to full users (cancels, CR-12f), as training bought by those with balances (C-3, C-5) and paid to providers (C-21), as gifts to transfer recipients (C-10), and as Fund receipts (C-32) paid to small employers (C-33, C-38) and providers. Levy payers that buy training they valued below its cost only because the vouchers would otherwise lapse use the provider's and the trainee's time on it (C-8, C-25, C-52, CR-8a).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The levy is collected from most employers above the threshold. | enforcement | 0.95 | Payroll withholding already in place. | C-1, C-2, C-4, C-49, C-50, C-53 fail |
| A-2 | Many levy payers' vouchers exceed the approved training they would have bought without the Act, so some vouchers go unused and some lapse. | binding | 0.9 | Levy 1.6 billion against 0.74 billion; 70% bought none in 2026. | Most chains through unspent balances, lapses and the Fund fail |
| A-3 | Candidates are available for the added places. | other | 0.8 | Youth unemployment; staff interest. | C-6, C-9, C-18, C-19, C-51 fail |
| A-4 | Some levy payers with unspent balances value approved training above zero cash cost. | substitutability | 0.85 | Training surveys; other voucher schemes. | C-5, C-6, C-8, C-9, C-18 and the demand chains to providers fail |
| A-5 | For some employers near 3 million that do not train, the notch exceeds the gain from growing past it. | binding | 0.75 | 1,100 employers between 2.7 and 3.3 million. | C-13 fails |
| A-6 | Some employers can move work to contractors, agency staff or unrelated entities at a cost below the levy saved. | other | 0.6 | Contractor use; common-control rule. | C-14, C-15 fail |
| A-7 | At employers that do not recover the levy, labor cost or wages adjust (at least one). | alternative_uses | 0.8 | A 0.5% wedge must fall somewhere. | C-16, C-17, C-19 fail |
| A-8 | Some employment or hours at those employers are at the margin. | alternative_uses | 0.65 | Hiring at low-margin firms. | C-17, C-19 lose the (−) chain |
| A-9 | Existing staff and training can be fitted to approved standards. | other | 0.8 | Breadth of standards. | C-7, C-44 fail |
| A-10 | Under U1-a, NSA registration of employer-providers is decided case by case. | other | 0.6 | No regulations yet; s. 9(4). | C-44, C-46 fail under U1-a |
| A-11 | Federations, providers and small-firm groups organize at a cost below their stakes. | other | 0.85 | Existing associations. | C-41, C-42, C-43 fail |
| A-12 | Levy payers know the voucher start date and can delay planned starts. | expectations | 0.7 | Budget statement; HR cycles. | C-28 fails; C-29 loses a chain |
| A-13 | Small employers know the Fund's opening date and can delay starts by a few months. | expectations | 0.6 | Act s. 16. | C-27 loses one chain |
| A-14 | Some partial users would rather transfer vouchers than let them lapse. | other | 0.8 | No added cost; supply-chain ties. | C-10, C-11, C-12 fail |
| A-15 | Some transfers carry undisclosed consideration. | enforcement | 0.55 | Consideration is hard to detect. | C-12 fails |
| A-16 | Some providers' fees are below the band for their standard. | other | 0.8 | Bands are 2026 medians. | C-21 loses one chain |
| A-17 | Approved provision cannot expand fully at the old cost in the short to medium run. | durability | 0.7 | Trainer shortages; registration takes 6-12 months. | C-21 loses one chain; C-24, C-25, C-26, C-36, C-52 fail; C-27 loses one chain |
| A-18 | Under U1-a, some employers that bought external approved training have in-house units that can deliver it below the band. | other | 0.6 | About 400 programs could meet a standard. | C-22 becomes increase under U1-a; C-45 loses one chain |
| A-19 | Some employers with in-house programs have balances large enough to replace part of in-house training with voucher-funded external training (U1-b). | other | 0.7 | Levies of 1 to 5 million. | C-45 U1-b sign fails |
| A-20 | Under U1-a, some employers expand in-house units to recover their levy. | other | 0.6 | Band against in-house cost. | C-45 U1-a loses one chain; C-46 fails |
| A-21 | Added completers raise the supply of qualified workers in some trades faster than demand. | other | 0.55 | Trades where apprenticeships are a large share of entry. | C-51 fails |
| A-22 | Some small employers would have bought approved training without the Fund. | other | 0.9 | 0.61 billion of small-employer spending in 2026. | C-38 fails |
| A-23 | Demand for Fund support exceeds its receipts in some quarters. | other | 0.7 | 90% subsidy; 410,000 small employers. | C-35, C-36 fail; C-37 becomes increase |
| A-24 | Some enrollees are existing staff whose off-the-job hours come out of production. | other | 0.8 | Relabeling. | C-7, C-8 fail |
| A-25 | Small employers compete with levy payers in some product markets, or expect to use the Fund. | other | 0.6 | Sector overlap. | C-42 loses the small-firm part |
| A-26 | Some small employers value approved training above the 10% of the band they pay. | substitutability | 0.85 | Demand at full price in 2026. | C-11, C-34, C-37 fail or lose a chain |
| A-27 | The levy is a material part of the cost of some outputs. | other | 0.2 | 0.5% of payroll. | Not reported (see below) |
| A-28 | No capped employer is near the 1 billion line. | other | 0.9 | Payroll distribution of the 45. | C-20 becomes a decrease chain for capped employers near the line |
| A-29 | The Revenue Service's budget is not raised for the levy. | revenue_use | 0.7 | No appropriation. | C-53 becomes a group over taxpayers |
| A-30 | Owners at the announcement expected the levy to last. | expectations | 0.8 | No expiry; cross-party support. | C-23, C-24, C-50 fail or shrink |
| A-31 | Some employers move payroll to Halvard. | mobility | 0.2 | Small cross-border employment. | Not reported |
| A-32 | Under U1-b, in-house units register to train other employers' apprentices. | other | 0.3 | Few sell training now. | Not reported |
| A-33 | Under U1-a, employers send in-house trainees to external providers because the band does not cover in-house cost. | other | 0.3 | In-house cost against bands. | Not reported |
| A-34 | Additional completers' money earnings rise. | other | 0.45 | Many enrollees are existing staff. | Not reported |
| A-35 | Levy payers that cut hiring under the levy cut apprentice places. | other | 0.2 | Apprentice places are free at the margin for partial users. | Not reported |
| A-N1 | For starts the Fund pays, the rise in provider fees caused by voucher and Fund demand is smaller than 90% of the band. | other | 0.8 | NEW. The Fund pays 90% of a band set at the 2026 median fee; a fee rise of that size would require near-doubling of fees, against trainer shortages that are partial (A-17). | C-33 becomes ambiguous |
| A-N2 | Some levy payers that will not recover the levy can date discretionary pay (bonuses) in March 2028 rather than in the first levy year. | expectations | 0.55 | NEW. Levy assessed on payroll in the levy year from 1 April 2028; withholding is monthly; bonus timing is discretionary at many large employers. | C-30, C-31 fail |
| A-N3 | Below-band providers face voucher demand at the band smaller than they would supply at it, so the bar on rebates holds their price above the level that would clear their market. | binding | 0.45 | NEW. A-16 makes the band exceed some fees; A-17 pushes demand up against capacity, which works the other way. | Not reported (see below) |

**Not reported** (an assumption below 0.5):
- Prices of levy payers' outputs rise (CR-9, input_to): needs A-27 (p 0.2).
- Payroll moved to Halvard (CR-4, x: here, y: there): needs A-31 (p 0.2).
- In-house units under U1-b sell training to other employers: needs A-32 (p 0.3).
- Under U1-a, in-house trainees sent to external providers: needs A-33 (p 0.3).
- Completers' money earnings rise (CR-7c 0.9: a change in money earnings from training needs a premise on the holder's next-best use): needs A-34 (p 0.45).
- Apprentice places cut where hiring is cut: needs A-35 (p 0.2); not counted as a chain in C-19 (CR-12 0.8, kind 2 below 0.5).
- Below-band providers compete on non-price terms (CR-6: the bar on rebates holds the price; pressure to quality, service or inducements, as a group): needs A-N3 (p 0.45).

## 11. Report

**The policy:** From April 2028, Estravan employers with payroll above 3 million crowns pay 0.5% of their whole payroll (capped at 5 million crowns), about 1.6 billion crowns a year, against about 0.74 billion they spent on approved apprenticeships in 2026. Each crown comes back as a voucher that pays an approved provider a fixed band per apprentice-year; up to a quarter may be given to other employers; unused vouchers lapse after two years into a Fund that pays 90% of the band for small employers' apprentices, first come, first served.

**Visible consequences:** The state collects about 1.6 billion a year (C-1). Levy payers with unspent balances face no cash cost for approved training up to the band (C-3) and buy more of it (C-5); enrollment rises (C-6) and more apprentices are employed (C-18). The Fund receives lapsed vouchers from 2030 (C-32) and small employers whose starts it funds pay less (C-33) and want more training (C-34).

**Invisible consequences:**
- *Levy payers that do not recover the levy:* have less to spend on other things (C-2); their owners bear the capitalized cost from the March 2027 announcement (C-50); the wedge falls on wages or returns (C-16) and on employment or hours other than apprentices (C-17). Employers near 3 million hold payroll down or reclassify (C-13); work moves to contractors and agencies (C-14, C-15). Discretionary pay is brought into March 2028 (C-30, C-31).
- *Levy payers with balances:* fit existing staff and training to standards (C-7), losing production hours (C-8); hold back starts until vouchers arrive (C-28, C-29); transfer vouchers to other employers (C-10, C-11), some for hidden consideration (C-12).
- *Workers:* receive more training as a term of employment (C-9); qualified workers in some trades face lower wages as completers enter (C-51); trainers' wages rise (C-25).
- *Providers:* receive more per apprentice-year (C-21), gain value from the announcement (C-24), and new providers enter (C-23). Buyers of other training pay more (C-52).
- *Small employers:* pay more and buy less approved training before the Fund opens (C-26, C-27); afterwards they wait for Fund support (C-35), those not funded in a quarter pay more (C-36), and those who would have trained anyway receive a transfer (C-38).
- *Administration:* the NSA's 40 million comes from taxpayers or other spending (C-47, C-48); the Revenue Service collects without new money, at the expense of other work (C-49, C-53). Federations, providers, small-firm groups and in-house employers lobby (C-41 to C-43).

**Ambiguous effects:** Total employment at levy payers that do not recover the levy (C-19): apprentice places rise, the payroll wedge pushes other employment or hours down. Small employers' approved training after 2030 (C-37): the Fund pushes it up; higher fees in quarters the Fund cannot cover push it down. External providers' volume under U1-a (C-22): new voucher demand against employers moving training in-house.

**Key conditions:** Most levy payers have more vouchers than they would have spent (A-2, 0.9) and value training above zero cash cost (A-4, 0.85); provision cannot expand fully at the old cost (A-17, 0.7); the levy was expected to last (A-30, 0.8). Two premises were added: the fee rise for Fund-paid starts is less than 90% of the band (A-N1, 0.8) and discretionary pay can be re-dated (A-N2, 0.55). U1 decides whether in-house programs are paid from own vouchers: under U1-a in-house training expands (C-45) and registration is sought (C-44, C-46); under U1-b employers with in-house units buy more external training.

**What this analysis cannot say:** Sizes; whether added training raises productivity or completers' earnings (A-34 below cut-off); whether the training bought is worth its cost to society; net welfare or whether the policy is good. Health and safety are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | officials.revenue_service (levy collected) | tax_revenue | increase | medium; long | visible | B | CR-1 (op 3 on each crown of payroll below the cap, op 4 above it); CR-8b (what payers pay is received) | A-1 |
| C-2 | employers.levy.non_recovering | resources_available_other_uses | decrease | medium; long | invisible | B | CR-1 (op 3/op 4); CR-3 note (a charge refunded only on a purchase burdens those who do not claim it; they pay a sum they can avoid only by cutting payroll); CR-8a | A-1, A-2 |
| C-3 | employers.levy.with_unspent_balance | price_paid (cash outlay per approved apprentice-year, up to the band) | decrease | medium; long | visible | B | CR-1 op 3 (vouchers that would otherwise lapse or be given away pay the band; the levy is paid whether or not they train, so the cash cost of the next unit of training is zero up to the band) | A-2 |
| C-4 | employers.levy (all bound) | compliance_cost | increase | medium; long | invisible | B | CR-1 op 3 (withholding, voucher accounts, claims); CR-3 note (full users bear the cost of claiming and the time the money is held); CR-8c | A-1 |
| C-5 | employers.levy.with_unspent_balance | quantity_demanded (approved apprenticeship training) | increase | medium; long | visible | B | CR-4 (x: no approved training, y: voucher-paid approved training; y made better); CR-4c (more units as the next unit costs no cash) | A-2, A-4 |
| C-6 | candidates.apprenticeship | enrollment (approved apprenticeships) | increase | medium; long | visible | B | CR-9 (contract: employment with training); CR-4 (candidates offered a funded place, x: decline, y: enroll); CR-5 (exchanges take place that would not have) | A-2, A-3, A-4 |
| C-7 | employers.levy.with_unspent_balance | reclassification (existing staff and training fitted to approved standards) | increase | medium; long | invisible | B | CR-4 (x: existing unapproved training paid in cash, y: the same training fitted to a standard and paid from vouchers) | A-2, A-9, A-24 |
| C-8 | employers.levy.with_unspent_balance | hours_worked (production hours of enrolled existing staff) | decrease | medium; long | invisible | B | CR-1 op 3 (the existing standard takes 20% of paid hours off the job); CR-8a (those hours are withdrawn from production) | A-2, A-4, A-24 |
| C-9 | workers.levy_employers | non_wage_compensation (approved training received) | increase | medium; long | invisible | B | CR-5c (training is a term of the employment exchange; vouchers make offering it cost the employer no cash) | A-2, A-3, A-4 |
| C-10 | employers.transfer_recipients | resources_available_other_uses | increase | medium; long | invisible | B | CR-4 (x: let vouchers lapse, y: give them away; y not worse for the giver); CR-5 (0.7 gift); CR-8b (the recipient gains what the levy payer gave) | A-2, A-14 |
| C-11 | employers.transfer_recipients | quantity_demanded (approved apprenticeship training) | increase | medium; long | invisible | B | CR-4, CR-4c (training paid by transferred vouchers costs no cash) | A-2, A-14, A-26 |
| C-12 | employers.levy.with_unspent_balance, employers.transfer_recipients | legal_breach (transfers with undisclosed consideration) | increase | medium; long | invisible | B | CR-6 (the rule holds the price of a transferred voucher at zero although recipients value it above zero; the pressure seeks the illegal margin); CR-4 (x: comply, y: violate, against penalties of 50%) | A-2, A-14, A-15 |
| C-13 | employers.near_threshold.non_training | earnings (payroll held at or below 3 million) (−), reclassification (+) | at_least_one_as_stated | medium; long | invisible | B | CR-1 (0.9: the provision attaches 15,000 crowns to crossing 3 million); CR-4 (x: grow past 3 million, y: stay at or below it, by smaller payroll or by moving work outside payroll) | A-5 |
| C-14 | employers.levy (all bound) | reclassification (work moved to contractors, agency staff or unrelated entities) | increase | medium; long | invisible | B | CR-4 (x: covered form, payroll; y: uncovered form, contract) | A-6 |
| C-15 | sellers.contract_agency_labor | quantity_substitute (contract and agency services sold to levy payers) | increase | medium; long | invisible | B | CR-9 (relation: contract labor substitute for payroll); CR-4 (C-14) | A-6 |
| C-16 | workers.levy_employers, employers.levy.non_recovering | wage_rate (−) [workers]; return_on_capital (−) [employers] | at_least_one_decrease | medium; long | invisible | B | CR-1 op 3 (a charge per crown of payroll not refunded); CR-7b (the burden settles on whichever side has fewer alternatives; no premise ranks them, so only the group is signed) | A-2, A-7 |
| C-17 | workers.levy_employers (at non-recovering employers) | employment (other than apprentices) (−), hours_worked (−) | at_least_one_decrease | medium; long | invisible | B | CR-4c (the last hour or worker, valued least, is the first given up when it costs more); CR-7b | A-2, A-7, A-8 |
| C-18 | workers.levy_employers | employment (apprentices) | increase | medium; long | visible | B | CR-4 and CR-5 (places paid from vouchers are filled, C-5, C-6) | A-2, A-3, A-4 |
| C-19 | workers.levy_employers (at non-recovering employers) | employment (total) | ambiguous | medium; long | invisible | B | CR-12b (0.8, two items): (+) C-18; (−) C-17; no dominance premise | A-2, A-3, A-4, A-7, A-8 |
| C-20 | employers.levy.capped | employment (through the levy wedge) | no_change | medium; long | invisible | B | CR-1 (0.9: above the cap the levy is op 4, fixed at 5 million); CR-4 (a change in means alone changes no relative cost of hiring) | A-28 |
| C-21 | providers.approved | net_price_received (per apprentice-year) | increase | medium; long | invisible | B | Two independent chains (CR-12d): (1) CR-1 op 3 and op 1 (the voucher pays the band whatever the fee; no rebate), so providers with fees below the band receive more (A-16); (2) CR-6 (more buyers while provision cannot fully expand, 0.9 split premise A-17) | A-16 (or A-2, A-4, A-17) |
| C-22 | providers.approved | quantity_traded (approved training) | U1-a: ambiguous; U1-b: increase | medium; long | visible | B | CR-9 (relation: in-house training substitute for external); (+) C-5, C-11, C-34 with partial expansion (A-17); U1-b (+) CR-4 (x: in-house paid in cash, y: external paid from vouchers, A-19); U1-a (−) CR-4 (x: external, y: own unit paid the band, A-18); CR-12b | A-2, A-4, A-17, A-18, A-19, A-26 |
| C-23 | providers.prospective | entry_rate | increase | medium; long | invisible | B | CR-4 (x: stay out, y: register); CR-7a (means move toward the higher yield, C-21) | A-2, A-4, A-30 |
| C-24 | providers.approved | asset_value (provider businesses) | increase | short (from announcement) | invisible | B | CR-10c and CR-7c (the expected rise in yield, C-21, is captured by owners when the levy becomes expected, 1 March 2027) | A-2, A-4, A-17, A-30 |
| C-25 | workers.trainers | wage_rate | increase | medium | invisible | B | CR-9 and LW-10 (relation: trainers' labor input_to approved training); CR-7a (pulled up in every use while scarce) | A-2, A-4, A-17 |
| C-26 | employers.small | price_paid (provider fee per apprentice-year, before the Fund) | increase | medium | invisible | B | CR-9 (relation: same_market_other_segment, shared provider capacity); CR-6 (more demand at limited capacity raises the fee) | A-2, A-4, A-17 |
| C-27 | employers.small | quantity_traded (approved training, before July 2030) | decrease | medium | invisible | B | Two chains (CR-12d): (1) CR-4c (higher fee, C-26), CR-8a (capacity drawn to voucher buyers); (2) CR-10a (starts delayed to the Fund's opening, A-13) | A-2, A-4, A-17 (or A-13) |
| C-28 | employers.levy.with_unspent_balance | quantity_traded (approved starts, 1 Mar 2027 to Apr 2028) | decrease | short | invisible | B | CR-10a; CR-4 (x: start now, paid in cash; y: start from May 2028, paid from vouchers that would otherwise go unused) | A-2, A-12 |
| C-29 | employers.levy.with_unspent_balance | quantity_traded (approved starts, May to Dec 2028) | increase | medium | invisible | B | CR-10a (deferred starts arrive); CR-4 (C-5) | A-2, A-4, A-12 |
| C-30 | workers.levy_employers | earnings (discretionary pay dated March 2028) | increase | short | invisible | B | CR-10a; CR-4 (x: pay in the levy year, y: pay before it) | A-N2 |
| C-31 | workers.levy_employers | earnings (discretionary pay dated April 2028 to March 2029) | decrease | medium | invisible | B | CR-10a; CR-4 (the same pay moved earlier) | A-N2 |
| C-32 | residual_claimant (Small Firm Training Fund) | non_tax_receipts (lapsed vouchers) | increase | long | visible | B | CR-1; CR-8b (lapsed vouchers are received by the Fund; against no Fund) | A-2 |
| C-33 | employers.small (funded starts) | price_paid (approved training) | decrease | long | visible | B | CR-1 op 3 (90% of the band paid); CR-5c; CR-12b with dominance premise A-N1 against the fee rise (C-36 chain) | A-2, A-N1 |
| C-34 | employers.small | quantity_demanded (approved training) | increase | long | visible | B | CR-4, CR-4c (the next unit costs 10% of the band plus any excess) | A-2, A-26 |
| C-35 | employers.small | wait_time (for Fund support) | increase | long | invisible | B | CR-6 (0.7: a fixed budget at a set rate; unsatisfied buyers' pressure goes to queuing, first come, first served); CR-8 (0.8: claimants paid later when the budget runs short) | A-2, A-23 |
| C-36 | employers.small (unfunded starts) | price_paid (provider fee per apprentice-year) | increase | long | invisible | B | CR-9 (shared provider capacity); CR-6 (voucher and Fund demand raise the fee) | A-2, A-17, A-23 |
| C-37 | employers.small | quantity_traded (approved training) | ambiguous | long | invisible | B | CR-12b: (+) C-34; (−) CR-4c on C-36 | A-2, A-17, A-23, A-26 |
| C-38 | employers.small (inframarginal) | resources_available_other_uses | increase | long | invisible | B | CR-8b (the Fund pays for training they would have bought) | A-2, A-22 |
| C-41 | employers.levy (federations) | lobbying_effort (against the levy, or for a higher threshold) | increase | short; medium; long | invisible | B | CR-4 (x: accept, y: lobby); CR-8c | A-2, A-11 |
| C-42 | providers.approved, employers.small (associations) | lobbying_effort (to keep or widen vouchers, bands and the Fund) | increase | medium; long | invisible | B | CR-4 (x: accept, y: lobby); CR-8c | A-11, A-25 |
| C-43 | employers.in_house | lobbying_effort (on the employer-provider regulations) | increase | short; medium | invisible | B | CR-4 (regulations under s. 9(4) decide whether own units are paid); CR-10a; CR-8c | A-11 |
| C-44 | employers.in_house | reclassification (in-house programs registered and paid from own vouchers) | U1-a: increase; U1-b: no_change | medium; long | invisible | B | U1-a: CR-1 op 2, CR-4 (x: unapproved program paid in cash, y: registered program paid the band); U1-b: the option does not exist | A-9, A-10 |
| C-45 | employers.in_house | quantity_substitute (in-house training) | U1-a: increase; U1-b: decrease | medium; long | invisible | B | U1-a: CR-4 (x: buy external, y: own unit paid from own vouchers, A-18, A-20); U1-b: CR-4 (x: in-house paid in cash, y: external paid from vouchers, A-19) | A-18, A-20, A-19 |
| C-46 | employers.in_house | compliance_cost (applications for employer-provider registration) | U1-a: increase; U1-b: no_change | short; medium | invisible | B | CR-1 op 2 granted case by case; CR-4 (x: no application, y: apply); CR-8c | A-10, A-20 |
| C-47 | officials.nsa | enforcement_cost | increase | medium; long | invisible | A | CR-1 op 4 (40 million a year); CR-8c | none |
| C-48 | taxpayers, recipients of other spending | resources_available_other_uses | at_least_one_decrease | medium; long | invisible | A | CR-8b; CR-8 (0.7: payers from the general budget recorded as a group) | none |
| C-49 | officials.revenue_service | enforcement_cost (collecting the levy) | increase | medium; long | invisible | B | CR-1 op 3; CR-8c | A-1 |
| C-50 | employers.levy.non_recovering (owners) | asset_value | decrease | short (from announcement) | invisible | B | CR-10c and CR-7c (the expected cost, C-2, is borne by owners when the levy becomes expected, 1 March 2027, partly before enactment) | A-1, A-2, A-30 |
| C-51 | workers.qualified_trades | wage_rate | decrease | long | invisible | B | CR-9 (relation: completers substitute for qualified workers); CR-6 (more sellers of the qualified labor at each wage) | A-2, A-3, A-4, A-21 |
| C-52 | buyers.unapproved_training | price_paid | increase | medium | invisible | B | CR-9 (relation: trainers input_to other training); CR-7a (C-25 spreads to every use of trainers). Depth 4: chain stops | A-2, A-4, A-17 |
| C-53 | officials.revenue_service | resources_available_other_uses (other collection work) | decrease | medium; long | invisible | B | CR-8a (staff directed to the levy are withdrawn from other work when the budget is not raised) | A-1, A-29 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-048-C1: A conditional refund that the payer can also give away (25% transfer) turns part of the levy into a gift chosen by the payer. CR-5 (0.7, gift) and CR-8b cover each side, but no core rule says whether a payer who would otherwise let the vouchers lapse "gives" anything by its own ranking (the alternative was the Fund). Derived here with CR-4 and CR-8b; the giver's own sign is not recorded.
- GAP-048-C2: The effect of training on productivity and completers' earnings has no derivation without a premise (CR-7c 0.9 on assets without a market price, and CR-8 0.7 on non-rival knowledge). This is not a gap in the calculus so much as a limit; recorded because the policy's stated purpose rests on it.

**(b) Core-rule wording that was hard to apply.**
- CR-3 (refund note, 0.9 standard note): the voucher pays a standard (the band) rather than the cost; the note says to split by position against the standard, but here the position belongs to the provider (fee below or above band), not to the claimant. The split was applied to providers (C-21) and to buyers' cash excess.
- CR-1 (0.9, per range) covers the cap; the notch at 3 million is a different kind of range (a jump on crossing), which had to be read as op 3 attached to the option of crossing. The wording could name notches.
- CR-6 for a price floor created only for voucher-paid sales (no rebate below the band) while cash sales are free: whether the floor binds depends on A-17 pushing the other way; the rule gave no guidance for a floor that may or may not bind, so it was handled as a premise (A-N3, below cut-off).
- CR-12f: full users' levy and vouchers cancel by construction except for claiming and timing; the note says not to report, yet the residue is real. Recorded under compliance_cost.

**(c) Vocabulary missing from the ontology.**
- No variable for a firm's payroll or labor cost (used `earnings` for payroll and a group with `return_on_capital` for the wedge).
- No variable for training received by workers (used `non_wage_compensation` with a qualifier) or for the share of a refundable charge recovered.
- No instrument type for a refund conditional on a purchase with transfer rights and lapse to a third party.
- No actor class for recipients of a transferable entitlement (used `employers.transfer_recipients`).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the training levy. Both find the following: the levy is collected, and employers that do not recover it lose means and owners lose value from the March 2027 announcement. Training costs no cash at the margin up to the band for employers with unspent balances, so approved enrollment rises after a dip in the announcement window. Existing staff and training are relabeled, and their off-the-job hours cost output. On non-recovering payroll the wedge falls on a group of wage and cost or return terms, and employment or hours fall as a group. Capped employers see `no_change` through the marginal cost of payroll. Near the notch, firms stay under the line, and work moves to contractors and agencies. Vouchers are transferred, some for hidden consideration, and providers whose fees are below the band receive more. Under each reading of U1, in-house training and external volume move in the same directions in both versions. The Fund receives lapses, small employers who would have trained anyway gain, Fund support is rationed by queue, qualified workers' wages fall, and both versions record lobbying, NSA administration and its general-budget payers. Four keys are signed differently. Three are core-version errors: provider entry, provider values and the provider fee are signed `increase` without the reading split that the core's own volume consequence (C-22, `ambiguous` under U1-a) requires. The fourth, small employers' training after 2030, is a judgment call on how long provider capacity stays short. The pattern version's one wrong sign is small employers' value (C-32), which misses the (−) chain from higher provider fees before the Fund opens. The core version omits more than the pattern version does: in-house programs, qualifications, near-threshold firms and small firms are not capitalized, and it omits the revenue shortfall against a static projection and NSA case-by-case registration. The pattern version omits the cash price to employers with balances, training received by workers, total employment at non-recovering employers, trainers' wages, and the fee and price chains for small employers.

Counts: M 18, V 13, S 4, OP 10, OC 6.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | |
| C-2 | C-5, C-6, C-18, C-29 | V | | Enrollment at levy payers. The core splits it into employers' demand (C-5), candidates' enrollment (C-6), apprentice employment (C-18) and the May to December 2028 window (C-29), which the pattern folds into C-2. |
| C-3 | C-2 | M | | |
| C-4 | C-4 | V | | Pattern: full recoverers' `resources_available_other_uses` decrease (holding, claiming, training bought only to recover the levy). Core: holding and claiming recorded as `compliance_cost` (C-4), and no means consequence for full users (CR-12f). The pattern's class is defined by response (redeem everything), so it includes employers that buy training only to use up their vouchers. They pay a levy they cannot avoid and so lose L − T of means (CR-3 note). The core's class is defined by counterfactual spending (training ≥ levy anyway), and it records that loss for nobody: core omission. CR-12f does not apply to a residue the core itself calls real. |
| C-5 | C-13 | V | | The core records a group: payroll held down (−) or reclassification (+). Either response leaves payroll under 3 million, so the pattern's separate count signs are valid on A-5. The core's group is weaker than derivable, and `earnings` for a firm's payroll stretches the variable. |
| C-6 | C-13 | V | | As C-5. |
| C-7 | C-14, C-13 | V | | The core applies it to all bound employers. |
| C-8 | C-16 | V | | Pattern group: labor cost (+), wage (−). Core group: wage (−), return on capital (−). Both are CR-7b groups with no ranking premise, and they say the same thing from different sides. |
| C-9 | C-17 | M | | |
| C-10 | C-20 | M | | |
| C-11 | C-7 | M | | |
| C-12 | C-46 | M | | |
| C-13 | none | OC | E | `allocation_by_non_price_criteria` under U1-a: increase. The core writes "CR-1 op 2 granted case by case" in C-46, and registration exists only under the Act (CR-12, 0.9), so the key is derivable. Core omission. |
| C-14 | C-41, C-42, C-43 | V | | Split by lobbying group. |
| C-15 | C-28 | M | | |
| C-16 | C-27 | V | | The core reaches the same decrease by two chains (higher fees and capacity drawn to voucher buyers; delay to the Fund's opening) over a wider window. |
| C-17 | C-34, C-37 | S | J | Pattern: small employers' enrollment from July 2030 `increase`. Core: demand increases (C-34), but quantity traded is `ambiguous` (C-37) because unfunded starts face fees pushed up by voucher and Fund demand (C-36). The core's (−) chain uses A-17, which is stated for the short to medium run, at the long horizon. A new demand shift when the Fund opens could keep capacity short for a time, so a premise to that effect is plausible. The pattern never derived the fee chain at all. Each version needs a fix: the core should state a long-run capacity premise in place of A-17, and the pattern should record the chain and combine it. |
| C-18 | C-10, C-11 | V | | The pattern records the transfers. The core records them through recipients' means (C-10) and recipients' demand (C-11). C-10 needs a premise that some recipients would have bought approved training anyway, like A-22, which the core does not state. Without it, vouchers spent on training a recipient would not otherwise buy free no means. |
| C-19 | C-12 | M | | |
| C-20 | C-21 | M | | The core adds a second, independent chain: more demand against limited capacity (A-17). |
| C-21 | C-22 | M | | |
| C-22 | C-26 | S | E | Fee per apprentice-year. Pattern: U1-a `ambiguous`; U1-b `increase`. Core: `increase` with no reading split. Under U1-a the core's own C-22 makes demand for external providers `ambiguous`, so a fee pushed up by that demand is `ambiguous` too (CR-12, 0.8, kind 3). Core error. |
| C-23 | C-23 | S | E | Provider entry. As C-22: the core signs `increase` from a demand chain that it records as `ambiguous` under U1-a. The band surplus (A-16) raises the margin per unit but cannot sign entry while volume is ambiguous. Core error. |
| C-24 | C-24 | S | E | Provider values. As C-23. The core cites the demand premises (A-2, A-4, A-17), not the band, and makes no reading split. Core error. |
| C-25 | C-45 | V | | Pattern: in-house trainers' `employment`. Core: in-house training as `quantity_substitute`. Same signs per reading. |
| C-26 | none | OC | E | In-house programs' `asset_value`: U1-a `ambiguous`, U1-b `decrease`. Derivable from CR-7c with its 0.9 clause (an asset that cannot be sold, valued by the holder's own ranking) and CR-3a, on A-19. Core omission (final check 7). |
| C-27 | C-51 | M | | |
| C-28 | none | OC | E | Qualifications' `asset_value` decrease, by holders' own ranking. Follows from C-51 by CR-7c (0.9), CR-3a. Core omission. |
| C-29 | C-32 | M | | |
| C-30 | C-38 | M | | |
| C-31 | C-35 | V | | The pattern records a group (waiting, allocation by criteria). The core signs `wait_time` alone. The statute names the rationing rule (first come, first served each quarter), so naming that margin is defensible. |
| C-32 | none | OC | P | Small employers' `asset_value` `increase`. Analyst error, not a pattern: an uncombined chain (final check 1). Higher provider fees for small employers before the Fund, and for unfunded starts after it (core C-26, C-36; A-17, p 0.7), are a kind 2 (−) chain on the yield of small firms that train. Against it stand the Fund and rivals' burden. The rivals chain is itself weak, since A-27 (p 0.2) denies pass-through of the levy into output prices. The sign should be `ambiguous`, or the class split into Fund users and others. The core omits small employers' value altogether. |
| C-33 | C-50 | M | | |
| C-34 | none | OC | E | Near-threshold firms' `asset_value` `ambiguous`. CR-7c gives (+) from rivals above the line and Fund eligibility, against (−) from the value of growing past the line. The core even lists the loss of Fund eligibility in its class definition. Core omission. |
| C-35 | C-15 | V | | Recorded as `quantity_substitute`. |
| C-36 | none | OC | E | `tax_revenue_vs_static_projection` decrease: arithmetic on a base the core itself shrinks (C-13, C-14, C-17). Core omission. |
| C-37 | C-47 | M | | |
| C-38 | C-48 | M | | |
| C-39 | C-49, C-53 | V | | Pattern: group of slower refunds and fewer checks (fixed budget). Core: collection cost (C-49) and less of other collection work (C-53). |
| C-40 | C-4 | M | | |
| C-41 | C-8 | M | | Recorded for the employer, not for the apprentices. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-3 | OP | E | `price_paid` (cash outlay per approved apprentice-year, up to the band) decrease for employers with balances. This is the direct op 3 effect. The pattern states it in prose under C-2 but does not record it. Pattern-version omission. |
| C-9 | OP | E | Workers' `non_wage_compensation` (training received) increase (CR-5c). Pattern-version omission. The key also shows how PC-17 fails for a refund: the term itself rises. |
| C-19 | OP | E | Total employment at non-recovering employers `ambiguous` (apprentices up, other staff or hours down). CR-12 (0.8, two items) asks for the total. Pattern-version omission. Caveat: the (+) chain on total employment needs a premise that some added apprentices are new hires rather than enrolled staff, and A-3 does not say so. |
| C-25 | OP | E | Trainers' `wage_rate` increase (CR-9 with LW-10, CR-7a; A-17). Total approved training rises under both readings (in-house units hire trainers too), so no reading split is needed. Pattern-version omission. |
| C-30 | OP | A | Discretionary pay moved into March 2028 (increase). Rests on a new premise, A-N2 (p 0.55). |
| C-31 | OP | A | The matching decrease in the first levy year. As C-30. |
| C-33 | OP | E | Small employers' price for Fund-paid starts decreases, with the dominance premise A-N1 against the fee rise. The pattern has the op 3 subsidy (C-17) but records no price, because it never derived the fee chain. Pattern-version omission. |
| C-36 | OP | E | Fee for small employers' unfunded starts increases at the long horizon. The pattern omits fees to small employers altogether. The core's sign, however, rests on A-17 beyond its stated horizon and has no U1 split (as C-26). Valid only with a long-run capacity premise, and under U1-b. |
| C-44 | OP | J | In-house programs registered and paid from own vouchers under U1-a (`reclassification`). This overlaps the pattern's relabeling (C-11) and in-house registration (C-12); it splits by class and adds no new sign. |
| C-52 | OP | J | Buyers of unapproved training pay more (trainers drawn away). Depth 4; the pattern stopped at depth 3. A depth choice. |

### Findings

- **Pattern overclaims or hidden premises.** Small employers' value `increase` (C-32) leaves out the fee chain and rests partly on a rivals chain that the pattern's own A-27 (p 0.2) undercuts. It is not a pattern error: CR-7c was applied without listing all chains. C-17 has the same blind spot. None of the patterns used, applied as written, produced a wrong sign here. PC-17's failure (below) was caught and corrected by the analyst.
- **Errors in the core version.** Sign errors: provider fees (C-26), entry (C-23) and values (C-24) are signed `increase` under both readings, although the core's own C-22 makes external demand `ambiguous` under U1-a (kind 3). C-36 and C-37 carry A-17 into the long run. C-10 lacks an inframarginal premise for recipients of transferred vouchers. CR-12f is misapplied to full users, whose residue is real (the core's own Gaps b), and employers that spend their whole balance on training they would not otherwise buy are recorded nowhere as losing means. Omissions: capitalization of in-house programs, qualifications, near-threshold firms and small firms (final check 7); `tax_revenue_vs_static_projection`; registration as `allocation_by_non_price_criteria` under U1-a. Minor: the notch is recorded as a group with `earnings` where separate count signs are derivable.
- **Errors in the pattern version (omissions).** The cash price to employers with balances (core C-3); training received by workers (C-9); transferees' demand (C-11); total employment at non-recovering employers (C-19); trainers' wages (C-25); small employers' fees and the price of Fund-paid starts (C-26, C-33, C-36); the timing of discretionary pay (C-30, C-31, on a new premise).
- **Test of 0.9 verdicts.** *PC-17 0.9, buy-out (failed):* confirmed. Without PC-17 the core version derived, from CR-1 op 3, CR-4 and CR-5c, that the term itself rises for employers with balances (C-5, C-9, training received), while the wedge falls on non-recovering employers' whole payroll (C-16, C-17). That is the reverse of PC-17's adjustment of "those contracts" against the receiving side. *`mandate_with_charge` (needed interpretation):* confirmed. The core version used the same label "with K2" and lists in its Gaps (c) that no instrument covers a refund conditional on a purchase, with transfer and lapse to a third party. *CR-1 0.9, per range (needed interpretation for the voucher):* partly contradicted. The core did not need a "range" for the voucher. It split the class by counterfactual position (full users, employers with unspent balance, non-recovering) under CR-1's 0.7 splitting note. Its own trouble with CR-1 0.9 was the notch, which it had to read as op 3 on the option of crossing. That confirms the pattern's separate notch point (c3). *CR-3 0.9, refunds on a standard (needed interpretation):* confirmed. The core version found independently that the position against the standard belongs to the provider, not the claimant, and applied the split to providers. *RS-17 0.9 (worked, but missed the notch and the Fund chain)* and *RS-18 0.9 (worked, If clause not met):* the core version derived the capped `no_change` from CR-1 0.9 and CR-4 directly, confirming RS-18's conclusion. It did not record near-threshold values, so it neither confirms nor contradicts RS-17's `ambiguous`. It did note the loss of Fund eligibility as a further cost of crossing, which RS-17 does not prompt.
- **Candidate pattern used a second time (deposit-refund, 6.2e).** Valid against the no-policy counterfactual: the charge, the refund through training, the lapses and the residual claimant's receipts are each signed against no Act (pattern C-3, C-2, C-29; core C-2, C-5, C-32). The core version reached the same structure from CR-1, the CR-3 note, CR-4 and CR-8b without the candidate. It fits only in the wider form the pattern version proposes (a refund for a costly act by the payer, capped at the charge, with a gift channel and a residual claimant that cannot go negative), not in the WE-027 form (refund for returning an item, to whoever holds it).
- **Limits of the core rules.** None produced a difference: no S, OP or OC row has cause K. Unclear core-rule wording: (1) CR-1 0.9 names thresholds in a parameter (a cap) but not notches (a jump on crossing), nor ranges set by the actor's own position against a quantity the provision depends on. (2) CR-3 0.9's split by position against a standard: when the standard is paid to a third party (a provider) and the refund is capped at the charge, whose position is meant? (3) CR-12f says not to report chains that cancel by construction, yet a residue (claiming, time the money is held) remains, and the core then misread full users. (4) CR-6 has no guidance for a floor that binds only on voucher-paid sales (the ban on rebates) while cash sales are free (core A-N3). (5) CR-6 0.7 public supply is written for a seller of a fixed quantity, and both versions applied it by analogy to a public payer with a fixed budget (Fund rationing). (6) CR-5's gift clause does not say whether a payer whose alternative was a lapse to the Fund gives anything by its own ranking (core GAP-048-C1).
