# WE-048 Apprenticeship training levy with vouchers that lapse to a small-firm fund

Analyst: draft (Handbook 0.9, held-out test)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized, fictional policy in a fictional country. It resembles real "train or pay" levies but is not modeled on any one of them. It was written as a held-out test of catalog 0.9, which was drawn from WE-036 to WE-045. It probes a charge that is refunded only if the payer later buys a costly service (a `mandate_with_charge`, PC-17's 0.9 buy-out clause, and the deposit-refund candidate in `06_gaps.md`, 6.2e), a payroll threshold with a notch (RS-17, 0.9: the value of firms near it), a levy capped per firm (RS-18, 0.9; CR-1, 0.9: operations that switch at a threshold), refunds paid on a deemed cost per apprentice (CR-3, 0.9: refunds on a standard), named and general-budget payers (OC-1), and training as an asset that cannot be sold (CR-7, 0.9). The probabilities are illustrative; the evidence column says what a real analysis would cite. Effects on health, safety and the environment are outside the scope of version 1.

## 1. Policy record

**The Estrava Apprenticeship Levy Act 2027.** The Republic of Estrava has about 5.2 million employees and 420,000 employers. About 9,500 employers have an annual payroll above 3 million crowns; they employ 3.2 million people (62%) and pay 380 billion crowns in wages a year. Forty-five of them have payrolls above 1 billion crowns (110 billion in total). About 1,100 employers have payrolls between 2.7 and 3.3 million. Employers under common control count as one employer for the threshold, the levy and the cap. To the north, the Republic of Halvard has no levy; cross-border employment is small.

**Training before the Act.** Approved apprenticeship standards already exist (a 12-month minimum, 20% of paid hours off the job, an end test). About 58,000 apprenticeships start each year and about 150,000 people are in training at any time, at an average provider fee of 9,000 crowns per apprentice-year: about 1.35 billion crowns a year, paid by employers. Levy-paying employers pay about 0.74 billion of it; 70% of them bought no approved training in 2026. About 600 large employers run their own (in-house) training units, spending about 2.1 billion crowns a year on in-house programs that are not approved apprenticeships; the Agency estimates that programs at about 400 of them could meet an approved standard.

**Dates.** The Finance Minister announced the levy, with a draft bill, in the budget statement of 1 March 2027. The Act was enacted on 1 November 2027. The levy applies to payroll from 1 April 2028, paid monthly with payroll withholding; vouchers are credited monthly from May 2028. The first vouchers lapse in May 2030, and the Small Firm Training Fund pays out from 1 July 2030. No expiry. The threshold, the cap and the bands are fixed in crowns; bands are reviewed every two years. Nominal wages grow about 3% a year.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Republic of Estrava; Halvard (no levy) to the north | Act s. 1 |
| Announced / enacted / effective / expires | 1 March 2027 / 1 November 2027 / 1 April 2028 (levy); May 2028 (vouchers); 1 July 2030 (Fund) / none | Budget statement; Act s. 2, 16 |
| Enforcement (who, penalties, resources) | Revenue Service collects the levy through payroll withholding, within its existing budget. The National Skills Agency (NSA) keeps voucher accounts, registers providers and audits them (appropriation of 40 million crowns a year from the general budget). Misused vouchers are repaid with a 50% penalty; providers who misuse them are deregistered. | Act s. 11, 18 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Levy | `mandate_with_charge` (with K2) | Payroll | Employers whose payroll in the levy year exceeds 3 million crowns | 0.5% of the whole payroll (a notch: at 3 million the levy jumps from zero to 15,000 crowns), capped at 5 million crowns per employer a year (reached at a payroll of 1 billion). About 1.6 billion crowns a year in total. | Employers with payroll of 3 million or less |
| K2 Vouchers | Refund conditional on a purchase (with K1) | Approved apprenticeship training | Levy payers | Each crown of levy is credited as one crown of vouchers. Vouchers pay an approved provider the funding band for the apprentice's standard (a deemed cost of 4,000 to 24,000 crowns per apprentice-year, set at the median 2026 fee for the standard), whatever the provider's fee; the provider may charge the employer any excess, and may not rebate any part of the band. Up to 25% of a year's vouchers may be transferred to other employers "without payment or other consideration". Vouchers lapse 24 months after credit. | — |
| K3 Small Firm Training Fund | `per_unit_subsidy` | Approved apprenticeship training at small employers | NSA | Receives lapsed vouchers; pays 90% of the band for apprentices at employers with payroll of 3 million or less, first come, first served each quarter, while its balance lasts. No other source. | — |
| K4 Administration | Enforcement | K1 to K3 | NSA, Revenue Service | As above. | — |

Unclear provisions:
- **U1, in-house training.** Section 9(4): "A provider shall be independent of the employers whose apprentices it trains, save as regulations provide for employers training their own apprentices." Section 14(3): "No part of a voucher shall return to the employer that redeemed it." Reading **U1-a**: s. 9(4)'s saving allows an employer's in-house unit, including an existing program that meets an approved standard, to be registered as an employer-provider and paid the band from the employer's own vouchers; the band is payment for training, not a "return". Reading **U1-b**: s. 14(3) bars any payment from an employer's vouchers to its own unit, so in-house programs cannot be funded from the employer's own vouchers (they may train other employers' apprentices).

Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures.** Levy: 0.5% of 270 billion (payrolls under the cap) plus 45 times 5 million, about 1.6 billion crowns a year, against about 0.74 billion that levy payers spent on approved training in 2026. Under the notch, an employer at 3.01 million pays about 15,050 crowns, against zero at 3.0 million. Because each band is the 2026 median fee, about half of providers' 2026 fees were below their band.

The counterfactual is Estrava without the Act: employers buy approved training at their own cost, with no levy, vouchers or Fund.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 + K2 | Binary (a charge on payroll) with a conditional refund; together a "train or pay" `mandate_with_charge`: the employer either spends 0.5% of payroll on approved training or loses that sum to the Fund. By CR-1 (0.9: per range): payroll up to 3 million, no operation; crossing 3 million, operation 3 on the option of growing past the line (a notch); from 3 million to 1 billion, operation 3 on each crown of payroll; above 1 billion, operation 4 (a fixed 5 million that no payroll choice changes). The voucher is operation 3 on the option of training (approved training up to the balance is paid from a sum otherwise lost) for an employer whose training is below its balance, and works as operation 4 (a lump-sum return) for one whose training would exceed its balance anyway. | Yes for employers whose approved training is below their levy (A-2) | PC-17 (0.9: buy-out), TX-1, TX-2, TX-3, TX-5, TX-9, RS-17, RS-18 (0.9), CR-1 (0.9), CR-3 (0.9), CR-7 (0.9), RS-5, RS-8, RS-15, RS-3; deposit-refund candidate (6.2e) |
| K3 | Binary: lapsed levy money pays a subsidy to small employers' training | Yes, from July 2030 (A-2) | SB-1, SB-2, SB-8, CR-6 (0.7: public supply), CR-8b, OC-1 |
| K4 | Binary: NSA from the general budget; Revenue Service from a fixed budget | Yes | OC-3 (0.9: fixed budget), OC-1 (Who pays) |

The charge is paid first and refunded up to 24 months later, so PC-17's buy-out clause fits by economic equivalence, not by form: per employer, the burden is the levy less the vouchers redeemed. Split by response (CR-1, 0.7): `employers.levy.full` redeem all their vouchers; `employers.levy.partial` redeem some or none.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `employers.levy.full` | Levy payers whose approved training uses all their vouchers | Pay the levy and recover it as training; bear holding and claiming costs. |
| `employers.levy.partial` | Levy payers that leave some or all vouchers to lapse | Approved training up to the balance is free at the margin; the rest is a payroll charge. |
| `employers.levy.inhouse` | Levy payers with in-house training units (about 600) | U1-a: may fund in-house programs from their vouchers. U1-b: may not. |
| `employers.levy.capped` | 45 employers with payroll above 1 billion | Levy fixed at 5 million; an extra crown of payroll costs no levy. |
| `employers.near_threshold` | Employers with payroll about 2.7 to 3.3 million | Crossing 3 million costs 15,000 crowns at once. |
| `employers.small` | Employers well below 3 million | Pay nothing; from July 2030 may receive 90% of the band; rivals above the line are burdened. |
| `apprentices` | People in approved apprenticeships, new hires and existing staff | More places; existing staff spend 20% of hours off the job. |
| `providers.external` | Independent approved training providers | Paid the band per voucher-funded apprentice-year whatever their fee. |
| `providers.prospective` | Would-be providers | Band payments and voucher demand. |
| `trainers.inhouse` | Staff of in-house training units | Their units' work depends on U1. |
| `workers.qualified` (`factor_owners.specific`) | Holders of qualifications in trades where apprenticeships expand | More completers enter their trades. |
| `intermediaries` | Labor agencies and contractors | Payroll moved off employers' books. |
| `residual_claimant` | The Small Firm Training Fund | Receives lapsed vouchers. |
| `officials.enforcement` | Revenue Service (collection), NSA (accounts, registration, audits) | New tasks. |
| `taxpayers` | Payers from the general budget | Fund the NSA. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `officials.enforcement` (Revenue Service, voucher accounts) | `tax_revenue` (levy collected) | increase | short to long | CR-1, CR-8b, TX-1 | A-1 |
| C-2 | `employers.levy.partial` | `enrollment` (approved apprenticeships at levy payers) | increase | short to medium (from April 2028) | CR-1 (0.9: the voucher as operation 3 below the balance), CR-4, PC-17 (0.9) | A-2, A-3, A-4 |
| C-3 | `employers.levy.partial` | `resources_available_other_uses` (levy not recovered) | decrease | short to long | TX-1, OC-1, CR-3 (note), CR-8a | A-1, A-2 |

C-2 is the policy's purpose. For an employer with an unspent balance, an extra apprentice-year costs nothing in cash up to the band (the vouchers would otherwise lapse), so those who valued it below the full fee now take it (CR-4; A-4). C-3: an employer that leaves vouchers to lapse keeps paying a sum it does not recover (CR-3 note); which other uses it gives up needs a premise (OC-1, Naming the forgone uses) and is not named.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `employers.levy.full` | `resources_available_other_uses` (holding the levy until redeemed, the cost of claiming, training bought only to recover the levy) | decrease | short to long | CR-3 (note; 0.9), CR-8a, CR-8c | A-1 |
| C-5 | `employers.near_threshold` | `number_of_sellers` (employers with payroll just below 3 million) | increase | short to medium | RS-17, CR-1 (0.9), CR-4 | A-5 |
| C-6 | `employers.near_threshold` | `number_of_sellers` (employers with payroll just above 3 million) | decrease | short to medium | RS-17, CR-4 | A-5 |
| C-7 | `employers.near_threshold`, `employers.levy.partial` | `reclassification` (work moved from payroll to contractors, agency staff or unrelated entities) | increase | short to medium | RS-5, RS-17, CR-4 | A-6 |
| C-8 | `employers.levy.partial` | `price_paid` (labor cost per hour including the levy) (+), `wage_rate` (−) | at_least_one_as_stated | short to medium | PC-17 (0.9: buy-out; TX-2 for those who pay), TX-2, CR-5c, CR-1 (0.9) | A-1, A-7 |
| C-9 | `employers.levy.partial` | `employment`, `hours_worked` (non-apprentice staff) | at_least_one_decrease | medium | TX-2, TX-3, RS-6, CR-4 | A-1, A-8 |
| C-10 | `employers.levy.capped` | `employment`, `hours_worked` (through the cost of an extra unit of payroll; not counting apprentices or the change in means) | no_change | short to long | RS-18 (0.9: caps per firm), CR-1 (0.9), CR-4 (0.8: fixed cost per firm) | A-28 |
| C-11 | `employers.levy.full`, `employers.levy.partial` | `reclassification` (existing staff and existing training relabeled as approved apprenticeships) | increase | short to medium | RS-5, SB-5, CR-4 | A-9 |
| C-12 | `employers.levy.inhouse` | `compliance_cost` (applications and audits to register in-house units as employer-providers) | U1-a: increase; U1-b: no_change | short to medium | RS-15, CR-8c | A-10 |
| C-13 | `employers.levy.inhouse` | `allocation_by_non_price_criteria` (NSA's case-by-case registration of employer-providers) | U1-a: increase; U1-b: no_change | short to medium | RS-15, CR-6 | A-10 |
| C-14 | `employers.levy`, `providers.external`, `employers.small` | `lobbying_effort` (large employers for in-house funding and wider voucher uses; providers for higher bands; small-firm groups for the Fund) | increase | short to medium | RS-7 | A-11 |
| C-15 | `employers.levy.partial` | `enrollment` (apprenticeship starts, March 2027 to March 2028; a flow) | decrease | short | RS-8, CR-10a | A-12 |
| C-16 | `employers.small` | `enrollment` (starts in the months before the Fund opens, early 2030; a flow) | decrease | medium | RS-8, CR-10a | A-13 |
| C-17 | `employers.small` | `enrollment` (approved apprenticeships at small employers, from July 2030) | increase | medium to long | CR-1 (operation 3), CR-4, CR-8b | A-2, A-26 |
| C-18 | `employers.levy.partial` | `quantity_traded` (vouchers transferred to other employers, as gifts) | increase | short to long | CR-5 (0.7: gift), CR-4, CR-12 (0.9: activities that exist only under the policy) | A-14 |
| C-19 | `employers.levy.partial`, transferees | `legal_breach` (consideration given for voucher transfers) | increase | medium | RS-3, CR-4 | A-14, A-15 |

**Train or pay (PC-17, 0.9).** Split by response: those who pay (C-3, C-8, C-9) are under TX-2: the levy is a wedge on each crown of payroll, so labor cost rises or the wage falls (a mixed group, C-8; incidence is not ranked, DM-1 has no clear premise here), and employment or hours fall (C-9). Those who "play" are under PC-17, but its conclusion had to be read differently (Gaps found, c1): the other terms that adjust are those of every contract on which the charge is levied (the whole payroll), not those of the apprentices who receive the term; for apprentices, the term is free at the margin, so demand for them rises (C-2). A full recoverer's marginal crown of payroll creates a voucher it spends on training it buys anyway, so it faces no wedge at the margin; its burden is the holding and claiming cost (C-4, CR-3 note).

**Operations per range (CR-1, 0.9).** Four ranges: none below 3 million; a notch at the line (C-5 to C-7); operation 3 per crown from 3 million to 1 billion (C-8, C-9); operation 4 above 1 billion. Above the cap the levy does not vary with payroll, so it changes no choice of hours or heads (RS-18, 0.9; CR-4, 0.8): C-10 is `no_change` through that channel. Whether the 5 million changes hiring through the firm's means is CR-4's "change in means alone" and is not signed.

**The notch (C-5 to C-7).** Measured on the levy year's payroll, so the response comes in each levy year. Employers just above the line that do not train gain 15,000 crowns or more by staying below it (A-5), and some move work off payroll (C-7, A-6). Common control blocks splitting into related companies.

**Relabeling (C-11).** Vouchers that would otherwise lapse pay for training employers would have done anyway once it is fitted to a standard: existing staff are enrolled, graduate programs converted (RS-5, SB-5; A-9). This is the main way full recoverers recover the levy without training more.

**In-house registration (C-12, C-13).** Under U1-a, the NSA decides case by case which in-house units meet the regulations' conditions; the relief from the levy is worth far more than the application (RS-15; A-10). Under U1-b there is nothing to apply for.

**Timing (C-15 to C-17).** From the March 2027 announcement, levy payers know that from April 2028 apprenticeships will be paid from vouchers; those planning starts in the year before delay them (C-15, RS-8; A-12), and the rise after April 2028 is part of C-2. Small employers know the Fund opens in July 2030; starts planned for early 2030 are delayed (C-16, A-13), then rise (C-17).

**Transfers (C-18, C-19).** A partial user loses unspent vouchers to the Fund; giving them to a supplier or customer costs nothing more (CR-4, A-14). The ban on consideration is hard to enforce where the gift buys goodwill or a price discount (A-15).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-20 | `providers.external` (fees below the band) | `net_price_received` (per voucher-funded apprentice-year) | increase | short to medium | CR-3 (0.9: refunds on a standard), CR-8b | training `input_to` apprenticeships | A-16 |
| C-21 | `providers.external` | `quantity_traded` (approved training sold) | U1-a: ambiguous; U1-b: increase | medium | CR-9, CR-4, CR-12b | as C-20 | A-2, A-4, A-18 |
| C-22 | `providers.external` (fees above the band) | `price_paid` (fee per apprentice-year) | U1-a: ambiguous; U1-b: increase | short to medium | CR-6, CR-12e (0.9: partial response), CR-12 (0.8, kind 3) | as C-20 | A-2, A-4, A-17, A-18 |
| C-23 | `providers.prospective` | `entry_rate` | U1-a: ambiguous; U1-b: increase | medium | CR-4, CR-7a, CR-12b | as C-20 | A-16, A-17, A-18 |
| C-24 | `providers.external` | `asset_value` (provider businesses) | U1-a: ambiguous; U1-b: increase | short (from March 2027) | CR-7c, CR-10c, CR-12b | as C-20 | A-16, A-18 |
| C-25 | `trainers.inhouse` | `employment` (staff of in-house units) | U1-a: increase; U1-b: decrease | medium | CR-4, CR-9, CR-12 (0.8, kind 2 below the cut-off) | in-house training `substitute` for external | A-19, A-20 |
| C-26 | `employers.levy.inhouse` | `asset_value` (in-house training programs; cannot be sold; by the holder's own ranking) | U1-a: ambiguous; U1-b: decrease | short to medium | CR-7 (0.9: assets without a market price), CR-7c, CR-3a, CR-12b | as C-25 | A-18, A-19 |
| C-27 | `workers.qualified` | `wage_rate` | decrease | long | CR-9, RS-13, CR-6 (0.9: splitting a shift) | completers `same_market_other_segment` | A-21 |
| C-28 | `workers.qualified` | `asset_value` (qualifications held; cannot be sold; by holders' own ranking) | decrease | long | CR-7 (0.9), CR-7c, CR-3a | as C-27 | A-21 |
| C-29 | `residual_claimant` (Small Firm Training Fund) | `non_tax_receipts` (lapsed vouchers) | increase | medium to long (from May 2030) | CR-8b, CR-12 (0.9) | — | A-1, A-2 |
| C-30 | `employers.small` (who would have trained anyway) | `resources_available_other_uses` | increase | medium to long | SB-8, CR-8b | — | A-22 |
| C-31 | `employers.small` | `wait_time`, `allocation_by_non_price_criteria` (first-come Fund) | at_least_one_increase | medium to long | CR-6 (0.7: public supply), PC-2 | — | A-23 |
| C-32 | `employers.small` (well below the threshold) | `asset_value` | increase | short (from March 2027) | CR-7c, CR-10c, CR-9 | rivals in the same product markets | A-25 |
| C-33 | `employers.levy.partial` (payroll 3 million to 1 billion) | `asset_value` | decrease | short (from March 2027) | CR-7c, CR-10c, SB-4 | — | A-1, A-2, A-30 |
| C-34 | `employers.near_threshold` | `asset_value` | ambiguous | short (from March 2027) | RS-17 (0.9), CR-7c, CR-12b | — | A-5, A-25 |
| C-35 | `intermediaries` (labor agencies, contractors) | `quantity_traded` (contract and agency labor) | increase | short to medium | CR-9 | agency labor `substitute` for payroll | A-6 |
| C-36 | `officials.enforcement` | `tax_revenue_vs_static_projection` (levy) | decrease | short to medium | TX-9 | — | A-6, A-8 |

**Refunds on a deemed cost (C-20, CR-3 0.9).** The voucher pays the band whatever the fee. Split providers by their position against it: those whose fees were below the band receive more per apprentice-year than they did (C-20; A-16, and by construction about half of 2026 fees were below the median); those above it still charge their fee, the band paid by vouchers and the excess by the employer. The clause's other half ("those who claim on the standard and use less than it receive more than they paid") cannot hold for employers in total, because the vouchers redeemed are capped at the levy paid; it holds per apprentice-year for in-house units under U1-a (Gaps found, b2).

**External providers under each reading (C-21 to C-24).** Under U1-b, voucher demand goes only to independent providers: more training is bought (C-21), and fees above the band rise. CR-12e's response argument: entry of providers is a response to the higher fee and cannot push it below its old level; to report `increase` the response must be partial (CR-12, 0.9), which A-17 states (trainer shortages, registration lags of six to twelve months) for the short to medium run. Under U1-a, a second chain opposes: employers that bought external training and can deliver it in-house below the band move it in-house, since the band then pays their own unit (A-18, p = 0.6). That is a kind 2 chain with p ≥ 0.5, so external quantity is `ambiguous` under U1-a, and fees, entry and provider values, which follow from it, are `ambiguous` too (CR-12, kind 3). The band surplus of C-20 holds under both readings, per apprentice-year sold.

**In-house units (C-25, C-26; CR-7 0.9).** An in-house program is a durable asset that cannot be sold. Its yield to the employer is what it saves against buying training outside. Under U1-b, voucher-funded external training is free at the margin for employers with balances, so the program saves less, and part of it is replaced (A-19): the program is worth less by the holder's own ranking (C-26), and in-house staff fall (C-25). A chain the other way, in-house units training other employers' apprentices for vouchers, needs A-32 (p = 0.3), below the cut-off, so the derived sign stands (CR-12, 0.8, kind 2). Under U1-a, both the program and external training can be paid from vouchers: the program is paid the band, which it keeps in the firm, while the external alternative also became free. Which is larger depends on the band against the external fee, with no premise: `ambiguous` (C-26). Employers expand units to recover the levy (A-20), so in-house staff rise (C-25; an opposing chain, units sending trainees outside, needs A-33, p = 0.3). The program's effect on the employer's money earnings is not signed (CR-7, 0.9).

**Qualified workers (C-27, C-28; CR-7 0.9).** More completers enter some trades from about 2031 (A-21): the wage of those already qualified falls against the counterfactual (CR-6, 0.9: the premise splits the shift toward price), and their qualification, which cannot be sold, yields less (C-28, by their own ranking). Completers themselves chose the apprenticeship (CR-2), so they are better off by their own ranking; a rise in their money earnings needs a premise on their next-best use, which is weak because many are existing staff (A-34, p = 0.45): not reported.

**The Fund (C-29 to C-31).** Lapsed vouchers are the Fund's only receipts, an activity that exists only under the Act (CR-12, 0.9). Unlike a deposit fund, it cannot go negative: it pays only what has lapsed. Its payers are named, the levy payers who do not redeem (C-3); its recipients are small employers. Those who would have trained anyway now pay 10% of the band (C-30, SB-8). With a 90% subsidy, demand is likely to exceed lapses in some quarters, and a first-come rule rations it (C-31, CR-6 0.7 applied to a public payer with a fixed budget; Gaps found, b4).

**Values (C-32 to C-34).** Expected from the March 2027 announcement (CR-7c, CR-10c). Employers that will not recover their levy are worth less (C-33). Small employers well below the line gain from the burden on rivals above it and from the Fund (C-32; A-25). Near the line, RS-17's 0.9 clause applies: rivals' burden and the Fund (+) against the lower value of growing past the line (−): `ambiguous` (C-34).

**Payroll inputs.** RS-14 would pass the levy into output prices, but 0.5% of payroll is not "a material part of the cost" for most outputs (A-27, p = 0.2): not reported. Payroll moved to Halvard: A-31, p = 0.2, not reported. Stopping points: the other spending of levy payers' workers, of providers' staff and of small employers: depth 3, diffuse.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `employers.levy.partial`, `enrollment`, short to medium | Training free at the margin up to the balance (C-2). | Fewer hires where the levy raises labor cost (C-9), if apprentices are among them (A-35, p = 0.2: kind 2 below the cut-off). | None needed | **increase** (C-2) |
| `employers.levy.partial`, `enrollment` (flow), March 2027 to March 2028 | None | Starts delayed to be paid by vouchers (C-15). | None needed | **decrease** (C-15) |
| `providers.external`, `quantity_traded`, medium | New voucher demand (C-2). | U1-a only: employers move external training in-house to be paid the band (A-18). | None | U1-a: **ambiguous**; U1-b: **increase** (C-21) |
| `providers.external` (above the band), `price_paid`, short to medium | Voucher demand. | Entry of providers (a response: CR-12e, with A-17 as the partial premise). U1-a: demand itself ambiguous (kind 3). | CR-12e (response argument) | U1-a: **ambiguous**; U1-b: **increase** (C-22) |
| `trainers.inhouse`, `employment`, medium | U1-a: units expanded to recover the levy (A-20). U1-b: training for other employers (A-32, p = 0.3). | U1-b: in-house training replaced by free external training (A-19). U1-a: trainees sent outside (A-33, p = 0.3). | Kind 2 below the cut-off in each reading | U1-a: **increase**; U1-b: **decrease** (C-25) |
| `employers.levy.inhouse`, `asset_value` (programs), short to medium | U1-a: the band paid to the firm's own unit. | The external alternative is free at the margin (both readings). | None | U1-a: **ambiguous**; U1-b: **decrease** (C-26) |
| `employers.near_threshold`, `asset_value`, short | Rivals above the line burdened; Fund eligibility. | Growing past the line is worth less. | None (RS-17, 0.9) | **ambiguous** (C-34) |
| `employers.small` (well below), `asset_value`, short | Rivals burdened; Fund. | None (growth past the line not in prospect). | None needed | **increase** (C-32) |
| `employers.levy.capped`, `employment`, `hours_worked` | None through the marginal cost of payroll. | None through it. | — | **no_change** (C-10), through that channel only |

## 8. Time structure

- **March 2027 to March 2028: expectation.** Values of employers above and near the line, of small employers and of providers adjust from the announcement (C-24, C-32 to C-34). Starts at levy payers are delayed (C-15). Employers near the line plan payroll for the first levy year (C-5 to C-7).
- **From April 2028.** Levy and vouchers. Enrollment rises (C-2), relabeling is fast (C-11), new training slower: providers need registration and trainers (A-17). Vouchers lapse 24 months after credit, first in, first out, so each employer's redemptions bunch before its oldest vouchers expire. Enrollment is higher in every window than in the counterfactual; the bunching is a path note (CR-12h), not a consequence.
- **May 2030 and after.** First lapses; the Fund pays from July 2030 (C-29 to C-31); small employers' starts dip before and rise after (C-16, C-17).
- **Stocks.** Skills are a durable stock that grows only through completions (CR-10b, TS-1): the first completers from levy-funded starts arrive from 2029, and the supply effect on qualified workers is long-run (C-27, C-28).
- **Erosion (TS-3).** The 3 million threshold, the 5 million cap and the bands are fixed in crowns. With nominal wages up about 3% a year, more employers cross the line each year, more reach the cap, and the bands buy less training until reviewed.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-37 | `officials.enforcement` (NSA) | `enforcement_cost` | increase | Staff for accounts, registration and audits (40 million crowns a year). | OC-3, CR-8c |
| C-38 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` (NSA appropriation) | at_least_one_decrease | Whatever the 40 million would otherwise fund or leave with its payers. | OC-1 (Who pays), OC-3, CR-8 (0.7) |
| C-39 | `officials.enforcement` (Revenue Service) | `wait_time` (other refunds and clearances) (+), `enforcement_cost` (other checks) (−) | at_least_one_as_stated | Other uses of the service's fixed budget. | OC-3 (0.9: fixed budget) |
| C-40 | `employers.levy.full`, `employers.levy.partial` | `compliance_cost` (levy returns, voucher accounts, evidence of off-the-job hours) | increase | Staff time and systems. | TX-5, OC-2, CR-8c |
| C-41 | `apprentices` (existing staff enrolled) | `hours_worked` (in production) | decrease | The output of the 20% of paid hours spent off the job. | OC-1, CR-8a |

**Payers (OC-1).** The levy's payers are named by the Act: levy payers, through their means (C-3, C-4) and, by incidence, their workers or buyers (C-8). They are not a general-budget group. The NSA is funded from the general budget with no tax named, so its payers are a group (C-38). The Revenue Service absorbs collection in a fixed budget (A-29): other work is slower or fewer checks are made (C-39). Both sides of each transfer are recorded: levy (C-3, C-4 / C-1), vouchers (C-2 / C-20, C-21), lapses (C-3 / C-29) and their use (C-29 / C-17, C-30), transfers (C-18).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The levy is collected from most employers above the threshold. | enforcement | 0.95 | Payroll withholding already in place. | Everything that follows from the levy shrinks. |
| A-2 | Many levy payers' vouchers exceed the approved training they would have bought without the Act, so some vouchers go unused and some lapse. | binding | 0.9 | Levy 1.6 billion against 0.74 billion of approved training; 70% of levy payers bought none in 2026. | C-2, C-3, C-17, C-29 and the Fund chains fail. |
| A-3 | Candidates (new hires or existing staff) are available for the added places. | other | 0.8 | Youth unemployment; staff interest in funded qualifications. | C-2 is smaller, and shows in wages for apprentices instead. |
| A-4 | Some levy payers with unspent balances value approved training above zero cash cost. | substitutability | 0.85 | Training surveys; experience of other voucher schemes. | C-2 is not reported. |
| A-5 | For some employers near 3 million that do not train, the 15,000-crown notch exceeds the gain from growing slightly past it. | binding | 0.75 | 1,100 employers between 2.7 and 3.3 million; margins in small firms. | C-5, C-6 are not reported; C-34 loses its (−) chain. |
| A-6 | Some employers can move work to contractors, agency staff or unrelated entities at a cost below the levy saved. | other | 0.6 | Use of contractors in services; common-control rule. | C-7, C-35 are not reported; C-36 rests on A-8 alone. |
| A-7 | At employers that do not recover the levy, labor cost or wages adjust (at least one). | alternative_uses | 0.8 | A wedge of 0.5% on payroll must fall somewhere. | C-8 is not reported. |
| A-8 | Some employment or hours at those employers are at the margin. | alternative_uses | 0.65 | Hiring decisions at low-margin firms. | C-9 is not reported; C-36 rests on A-6. |
| A-9 | Existing staff and existing training can be fitted to approved standards. | other | 0.8 | Standards cover management, care, retail, engineering. | C-11 is not reported. |
| A-10 | Under U1-a, NSA registration of employer-providers is decided case by case under conditions it interprets. | other | 0.6 | No regulations yet; s. 9(4). | C-12, C-13 are smaller and C-13 is not reported. |
| A-11 | Employers' federations, providers and small-firm groups organize at a cost below their stakes. | other | 0.85 | Existing associations. | C-14 is not reported. |
| A-12 | Levy payers know the voucher start date and can delay planned starts. | expectations | 0.7 | Budget statement; HR planning cycles. | C-15 is not reported. |
| A-13 | Small employers know the Fund's opening date and can delay starts by a few months. | expectations | 0.6 | Act s. 16; publicity. | C-16 is not reported. |
| A-14 | Some partial users would rather transfer vouchers than let them lapse. | other | 0.8 | Transfer costs nothing more; supply-chain ties. | C-18, C-19 are not reported. |
| A-15 | Some transfers carry undisclosed consideration. | enforcement | 0.55 | Consideration is hard to detect. | C-19 is not reported. |
| A-16 | Some providers' fees are below the band for their standard. | other | 0.8 | Bands are the 2026 median fees. | C-20 is not reported. |
| A-17 | Approved provision cannot expand fully at the old cost in the short to medium run. | durability | 0.7 | Trainer shortages; registration takes six to twelve months. | C-22 under U1-b is an increase or no change, not reported. |
| A-18 | Under U1-a, some employers that bought external approved training have in-house units that can deliver it below the band. | other | 0.6 | About 400 in-house programs could meet a standard. | C-21 to C-24 are increases under U1-a too. |
| A-19 | Some employers with in-house programs have balances large enough to replace part of in-house training with voucher-funded external training (U1-b). | other | 0.7 | Large employers' levies of 1 to 5 million crowns. | C-25 and C-26 under U1-b are not reported. |
| A-20 | Under U1-a, some employers expand in-house units to recover their levy. | other | 0.6 | Band against in-house cost per trainee. | C-25 under U1-a is not reported. |
| A-21 | Added completers raise the supply of qualified workers in some trades faster than demand. | other | 0.55 | Trades where apprenticeships are a large share of entry. | C-27, C-28 are not reported. |
| A-22 | Some small employers would have bought approved training without the Fund. | other | 0.9 | 0.61 billion of small-employer spending in 2026. | C-30 is not reported. |
| A-23 | Demand for Fund support exceeds its receipts in some quarters. | other | 0.7 | 90% subsidy; 410,000 small employers. | C-31 is not reported. |
| A-24 | Some enrollees are existing staff whose off-the-job hours come out of production. | other | 0.8 | Relabeling (C-11). | C-41 is not reported. |
| A-25 | Small employers compete with levy payers in some product markets, or expect to use the Fund. | other | 0.6 | Sector overlap. | C-32 is not reported; C-34 loses part of its (+) chain. |
| A-26 | Some small employers value approved training above the 10% of the band they pay. | substitutability | 0.85 | Small-employer demand at full price in 2026. | C-17 is not reported. |
| A-27 | The levy is a material part of the cost of some outputs. | other | 0.2 | 0.5% of payroll; payroll about a third of costs. | Below the cut-off: RS-14 pass-through not reported. |
| A-28 | No capped employer is near the 1 billion line. | other | 0.9 | Payroll distribution of the 45. | C-10 applies only to those well above it. |
| A-29 | The Revenue Service's budget is not raised for the levy. | revenue_use | 0.7 | Act gives it no appropriation. | C-39 is replaced by a taxpayer group, as C-38. |
| A-30 | Owners at the announcement expected the levy to last. | expectations | 0.8 | No expiry; cross-party support. | C-33 is smaller. |
| A-31 | Some employers move payroll to Halvard. | mobility | 0.2 | Small cross-border employment. | Below the cut-off: not reported. |
| A-32 | Under U1-b, in-house units register to train other employers' apprentices. | other | 0.3 | Few such units sell training now. | Below the cut-off: C-25 under U1-b stands. |
| A-33 | Under U1-a, employers send in-house trainees to external providers because the band does not cover in-house cost. | other | 0.3 | In-house cost per trainee against bands. | Below the cut-off: C-25 under U1-a stands. |
| A-34 | Additional completers' money earnings rise. | other | 0.45 | Many enrollees are existing staff. | Below the cut-off: not reported. |
| A-35 | Levy payers that cut hiring under the levy cut apprentice places. | other | 0.2 | Apprentice places are free at the margin for partial users. | Below the cut-off: C-2 stands. |

## 11. Report

**The policy.** From April 2028 Estrava charges employers with payroll above 3 million crowns 0.5% of their whole payroll, up to 5 million crowns a year. The levy comes back as vouchers to pay approved providers for apprenticeship training, at a fixed band per apprentice-year. Vouchers unused after 24 months go to a fund that pays 90% of the band for apprentices at small employers. Whether employers can use their vouchers on their own in-house programs is unclear.

**Visible consequences.** The levy is collected (C-1); more approved apprenticeships start at levy payers (C-2); employers that do not train lose the levy (C-3).

**Invisible consequences.**
- *Train or pay.* Employers that train enough recover the levy but bear holding and claiming costs (C-4), largely by relabeling existing staff and training (C-11), whose off-the-job hours cost output (C-41). Those that do not train pay what is in effect a payroll tax: higher labor cost or lower wages (C-8), and fewer jobs or hours (C-9). The largest employers, above the cap, face no levy on an extra crown of payroll (C-10).
- *The threshold.* More employers stay just below 3 million and fewer just above (C-5, C-6), and work moves to contractors and agencies (C-7, C-35). The levy raises less than a static projection (C-36).
- *Values.* Employers that will not recover the levy lose value from the announcement (C-33); small employers gain (C-32); those near the line may gain or lose (C-34).
- *Providers.* Providers whose fees were below the band gain per apprentice (C-20).
- *Small employers.* From 2030 the Fund, paid from lapsed vouchers (C-29), funds more apprenticeships (C-17), frees money for small employers that would have trained anyway (C-30), and is rationed by queue or criteria (C-31). Starts dip before vouchers and before the Fund open (C-15, C-16).
- *Workers.* Existing holders of qualifications in trades where apprenticeships grow face lower wages and a less valuable qualification in the long run (C-27, C-28).
- *Costs.* NSA administration (C-37), paid from the general budget (C-38); collection inside the Revenue Service's fixed budget (C-39); compliance (C-40); lobbying (C-14); voucher transfers (C-18) and illicit consideration for them (C-19).

**Per reading of U1.** If in-house programs can be funded (U1-a), large employers apply for registration (C-12, C-13), in-house training staff grow (C-25), and the effect on independent providers' sales, fees, entry and values is ambiguous (C-21 to C-24). If not (U1-b), independent providers sell more at higher fees (C-21, C-22) and in-house programs lose value and staff (C-25, C-26).

**Ambiguous effects.** Values of employers near the threshold (C-34); of in-house programs under U1-a (C-26); independent providers under U1-a (C-21 to C-24).

**Key conditions.** That vouchers exceed what levy payers would have spent (A-2, p = 0.9); that some employers sit near the notch (A-5, p = 0.75); provider supply (A-17, p = 0.7); the effect on qualified workers (A-21, p = 0.55).

**What this analysis cannot say.** How much training is additional rather than relabeled; whether apprentices or the economy gain in productivity; how large any effect is; whether the levy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | officials.enforcement | tax_revenue (levy) | increase | short–long | visible | B | CR-1, CR-8b, TX-1 | A-1 |
| C-2 | employers.levy.partial | enrollment (approved apprenticeships) | increase | short–medium | visible | B | CR-1, CR-4, PC-17 | A-2, A-3, A-4 |
| C-3 | employers.levy.partial | resources_available_other_uses (levy not recovered) | decrease | short–long | visible | B | TX-1, OC-1, CR-3, CR-8a | A-1, A-2 |
| C-4 | employers.levy.full | resources_available_other_uses (holding, claiming, training bought to recover) | decrease | short–long | invisible | B | CR-3, CR-8a, CR-8c | A-1 |
| C-5 | employers.near_threshold | number_of_sellers (just below 3 million) | increase | short–medium | invisible | B | RS-17, CR-1, CR-4 | A-5 |
| C-6 | employers.near_threshold | number_of_sellers (just above 3 million) | decrease | short–medium | invisible | B | RS-17, CR-4 | A-5 |
| C-7 | employers.near_threshold, employers.levy.partial | reclassification (work moved off payroll) | increase | short–medium | invisible | B | RS-5, RS-17, CR-4 | A-6 |
| C-8 | employers.levy.partial | price_paid (labor cost) (+), wage_rate (−) | at_least_one_as_stated | short–medium | invisible | B | PC-17, TX-2, CR-5c, CR-1 | A-1, A-7 |
| C-9 | employers.levy.partial | employment, hours_worked (non-apprentice staff) | at_least_one_decrease | medium | invisible | B | TX-2, TX-3, RS-6, CR-4 | A-1, A-8 |
| C-10 | employers.levy.capped | employment, hours_worked (via the marginal cost of payroll) | no_change | short–long | invisible | B | RS-18, CR-1, CR-4 | A-28 |
| C-11 | employers.levy.full, employers.levy.partial | reclassification (staff and training relabeled as apprenticeships) | increase | short–medium | invisible | B | RS-5, SB-5, CR-4 | A-9 |
| C-12 | employers.levy.inhouse | compliance_cost (employer-provider registration) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | RS-15, CR-8c | A-10 |
| C-13 | employers.levy.inhouse | allocation_by_non_price_criteria (registration) | U1-a: increase; U1-b: no_change | short–medium | invisible | B | RS-15, CR-6 | A-10 |
| C-14 | employers.levy, providers.external, employers.small | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-11 |
| C-15 | employers.levy.partial | enrollment (starts, March 2027 to March 2028) | decrease | short | invisible | B | RS-8, CR-10a | A-12 |
| C-16 | employers.small | enrollment (starts before the Fund opens, 2030) | decrease | medium | invisible | B | RS-8, CR-10a | A-13 |
| C-17 | employers.small | enrollment (from July 2030) | increase | medium–long | invisible | B | CR-1, CR-4, CR-8b | A-2, A-26 |
| C-18 | employers.levy.partial | quantity_traded (vouchers transferred) | increase | short–long | invisible | B | CR-5, CR-4, CR-12 | A-14 |
| C-19 | employers.levy.partial, transferees | legal_breach (consideration for transfers) | increase | medium | invisible | B | RS-3, CR-4 | A-14, A-15 |
| C-20 | providers.external (fees below band) | net_price_received (per voucher-funded apprentice-year) | increase | short–medium | invisible | B | CR-3, CR-8b | A-16 |
| C-21 | providers.external | quantity_traded (approved training) | U1-a: ambiguous; U1-b: increase | medium | invisible | B | CR-9, CR-4, CR-12b | A-2, A-4, A-18 |
| C-22 | providers.external (fees above band) | price_paid (fee) | U1-a: ambiguous; U1-b: increase | short–medium | invisible | B | CR-6, CR-12e, CR-12 | A-2, A-4, A-17, A-18 |
| C-23 | providers.prospective | entry_rate | U1-a: ambiguous; U1-b: increase | medium | invisible | B | CR-4, CR-7a, CR-12b | A-16, A-17, A-18 |
| C-24 | providers.external | asset_value (provider businesses) | U1-a: ambiguous; U1-b: increase | short | invisible | B | CR-7c, CR-10c, CR-12b | A-16, A-18 |
| C-25 | trainers.inhouse | employment | U1-a: increase; U1-b: decrease | medium | invisible | B | CR-4, CR-9, CR-12 | A-19, A-20 |
| C-26 | employers.levy.inhouse | asset_value (in-house programs; not saleable) | U1-a: ambiguous; U1-b: decrease | short–medium | invisible | B | CR-7, CR-7c, CR-3a, CR-12b | A-18, A-19 |
| C-27 | workers.qualified | wage_rate | decrease | long | invisible | B | CR-9, RS-13, CR-6 | A-21 |
| C-28 | workers.qualified | asset_value (qualifications; not saleable) | decrease | long | invisible | B | CR-7, CR-7c, CR-3a | A-21 |
| C-29 | residual_claimant (Fund) | non_tax_receipts (lapsed vouchers) | increase | medium–long | invisible | B | CR-8b, CR-12 | A-1, A-2 |
| C-30 | employers.small (would have trained) | resources_available_other_uses | increase | medium–long | invisible | B | SB-8, CR-8b | A-22 |
| C-31 | employers.small | wait_time, allocation_by_non_price_criteria | at_least_one_increase | medium–long | invisible | B | CR-6, PC-2 | A-23 |
| C-32 | employers.small (well below threshold) | asset_value | increase | short | invisible | B | CR-7c, CR-10c, CR-9 | A-25 |
| C-33 | employers.levy.partial | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, SB-4 | A-1, A-2, A-30 |
| C-34 | employers.near_threshold | asset_value | ambiguous | short | invisible | B | RS-17, CR-7c, CR-12b | A-5, A-25 |
| C-35 | intermediaries (agencies, contractors) | quantity_traded (contract and agency labor) | increase | short–medium | invisible | B | CR-9 | A-6 |
| C-36 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short–medium | invisible | B | TX-9 | A-6, A-8 |
| C-37 | officials.enforcement (NSA) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-38 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses (NSA appropriation) | at_least_one_decrease | short–long | invisible | A | OC-1, OC-3, CR-8 | none |
| C-39 | officials.enforcement (Revenue Service) | wait_time (+), enforcement_cost (other checks) (−) | at_least_one_as_stated | short–medium | invisible | B | OC-3 | A-29 |
| C-40 | employers.levy.full, employers.levy.partial | compliance_cost | increase | short–long | invisible | A | TX-5, OC-2, CR-8c | none |
| C-41 | apprentices (existing staff) | hours_worked (in production) | decrease | medium | invisible | B | OC-1, CR-8a | A-24 |

**Final check.** (1) Uncombined chains: every key with opposing chains is in section 7; enrollment's window (C-15) and later rise (C-2) are separate windows. (2) Groups: labor cost and wages (C-8), employment and hours (C-9), Fund rationing (C-31), Revenue Service (C-39). (3) Baseline: every sign is against no Act; U1 readings are compared with no Act, not with each other (C-21 under U1-a is ambiguous against no Act, not "smaller than under U1-b"). (4) Worse off is not poorer: `resources_available_other_uses` is signed only for those who keep paying (C-3, C-4) or are paid (C-30); in-house programs and qualifications are signed by the holder's ranking, not in money (C-26, C-28). (5) Timing: per window (C-15, C-16 / C-2, C-17); voucher bunching is a path note. (6) Both sides: section 9. (7) Capitalization checked for every employer class, providers, in-house programs and qualified workers. (8) Premises: every derivation's premises are in section 10, including those below the cut-off.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from patterns whose preconditions held.

**(b) Unclear core rules.**
1. *CR-1 0.9 (operations per range).* Written for a threshold in the policy's parameter (a cap per firm). Here a second "range" is set by the actor's own response: the same voucher is operation 3 for an employer whose training is below its balance and works as operation 4 for one whose training exceeds it anyway. Applied by analogy; the clause could say that the range may be defined by the actor's position against any quantity the provision depends on.
2. *CR-3 0.9 (refunds on a standard).* The standard (the band) is per unit of the refunded act (an apprentice-year), while the refund is capped at the charge paid. "Those who use less than the standard receive more than they paid" then holds per unit, never in total. Applied to providers and to in-house units per apprentice-year (C-20, C-26).
3. *CR-12 0.9 (what the response argument gives).* Worked with A-17 in the short to medium run. In the long run, entry by providers with fixed costs could leave fees below their old level if scale lowers cost per apprentice; the argument establishes equal yields, not an unchanged price (the same issue is found in WE-049). Not used for a long-run sign.
4. *CR-6 0.7 (public supply).* The Fund is a public payer of a fixed subsidy from a fixed budget, not a seller of a fixed quantity. The clause was applied by analogy (C-31).

**(c) Missing or wrong patterns.**
1. *PC-17 0.9 (buy-out), applied as written, gave a wrong conclusion for the "play" side.* Its main clause says the cost to the party providing the term rises and the other terms of "those contracts" adjust against the receiving side. Where the charge is paid first and refunded when the term is provided, providing the term lowers the employer's cost relative to not providing it; the charge falls on every contract on the payroll, while the term's recipients (apprentices) see demand for them rise. Read here as: the other-terms group applies to the whole payroll of those who do not recover the charge (C-8), and the term itself rises (C-2). The clause should say that under a refund the relevant contracts are those that carry the charge.
2. *RS-18 0.9 (caps per firm).* Its If clause ("a cost per worker") is not met: the levy is per crown of payroll, so there is no hours-for-heads shift below the cap either. The per-firm cap clause gave the right `no_change` above the cap (C-10), but it was reached through CR-1 0.9.
3. *RS-17 0.9.* Does not distinguish a notch (the whole payroll charged once over the line) from a kink; and it misses a second (+) chain for firms below the line when the policy also pays them (the Fund). The sign is still `ambiguous`.
4. *RS-14.* Precondition (a material part of cost) failed on the case's premise (A-27); no sign overridden.
5. *Deposit-refund candidate (6.2e, WE-027).* Needed, and fits with changes: the refund is for a costly act by the payer (buying training), not for returning the item; the third-party channel (iv) is the capped gift transfer, and the voucher has no market value because sale is barred (side payments instead, C-19); the residual claimant (v) cannot go negative because it pays only what lapses. Proposed wider form: "a charge refunded, within a period, to a payer who performs a named act, with the rest to a named fund".

**(d) Vocabulary.**
1. No variable for training spending or for training received (only `enrollment`, which counts relabeled places too).
2. No variable for a stock of skills held by workers; `asset_value` used with "not saleable".
3. No instrument for a charge refunded on the payer's own later purchase: `mandate_with_charge` and `deposit_refund` each fit part of it.
4. No actor class for training providers or in-house trainers; `providers.*` and `trainers.inhouse` used.

**(e) Test of 0.9.**
- *PC-17 0.9, a mandate with a buy-out charge (train or pay).* Split by response worked; the conclusion for those who provide the term failed as written (c1): the adjusting contracts are the whole payroll, and the term's recipients gain demand.
- *`mandate_with_charge` (2.3).* Needed interpretation: the charge is paid first and refunded within 24 months, so the instrument fits by economic equivalence, not by form (d3).
- *RS-17 0.9, value of firms near the threshold.* Worked as written: `ambiguous` (C-34). It did not prompt the extra (+) chain from Fund eligibility, nor the notch (c3).
- *RS-18 0.9, caps per firm.* Worked for its conclusion (C-10, `no_change` above the cap) but its If clause did not fit a cost per crown (c2).
- *CR-1 0.9, operations that switch at a threshold.* Worked for the four payroll ranges; needed interpretation for the voucher, where the range is set by the employer's own training (b1).
- *CR-3 0.9, refunds on a standard.* Needed interpretation: per unit only, because the refund is capped at the charge (b2, C-20).
- *CR-7 0.9, assets without a market price (training).* Worked as written: in-house programs and qualifications signed by the holder's ranking (C-26, C-28); money earnings left to a premise, below the cut-off for completers (A-34).
- *OC-1, payers.* The payers clause is a 0.8 change, not 0.9. Worked as written: the levy's payers are named and not recorded as a group; the NSA's general-budget funding is a group (C-38); forgone uses not named without a premise (C-3).
- *OC-3 0.9, fixed budget.* Worked as written (C-39).
- *CR-12 0.9, what the response argument gives.* Worked with the partial premise for the short to medium run (C-22 under U1-b); for the long run it would need a premise that cost per unit does not fall with scale (b3).
- *CR-12 0.9, activities that exist only under the policy.* Worked as written (C-18, C-29).
- *CR-12 0.8 kind 2 below the cut-off.* Worked (C-2, C-25).
- *Candidate patterns.* The deposit-refund candidate (WE-027) was needed. Its use here is valid against the counterfactual (the charge, refunds, lapses and the residual claimant's receipts are each signed against no Act), so this second use promotes it, in the wider form proposed in c5.
