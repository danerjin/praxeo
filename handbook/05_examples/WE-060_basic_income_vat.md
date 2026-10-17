# WE-060 A basic payment to every adult, funded by a higher VAT, with means-tested benefits offset

Analyst: draft (Handbook 1.0, held-out test)  |  Rule catalog version: 1.0  |  Status: awaiting expert review

A stylized policy in a fictional country. Several real proposals pay every adult a fixed sum and fund it from a consumption tax; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a case none of the 1.0 changes were drawn from. It probes how the method handles a transfer that is a change in means alone for some adults (CR-4, "a change in means alone"; `06_gaps.md`, Q19) while the tax that funds it changes relative prices for everyone, and the payment and the benefit offset together change the return to work for some benefit recipients (CR-4 proper, and CR-4's exception where means and relative prices move together). It also tests OC-1 as widened in 1.0 (who pays, saving is a use, receipts into the same budget), TX-1 and TX-2 incidence of a VAT with DM-1, CR-12's 0.8 note on two items in one variable (the payment up, the benefit down) against CR-12f, RS-11 (a payment lost by leaving the country), RS-22 (whether a compensating differential arises when labor supply changes), RS-17's 1.0 notch clause (the VAT registration threshold) and CR-12's 1.0 notes on the baseline of patterns and on tiers and dominance. The unclear provision is whether the payment counts as income in the means test for housing support. The counterfactual throughout is **Korsland without the Act**: the same benefits, housing support, VAT at 20% and price indexation of benefits and pensions. Effects on health and well-being are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Korsland Basic Payment and Value Added Tax Act 2027.** Korsland is a country of 6.0 million people, about 4.8 million of them adults (18 and over) habitually resident. Its currency is the crown (kr). To the south lies Dornholt, whose standard VAT rate is 21%; the Korsland border town of Kessa (about 40,000 people) is 8 km from the Dornholt town of Varrin, which has a retail park.

Existing rules that stay in the counterfactual:
- **Schedule 2 benefits** (income support, jobseeker's allowance, disability income supplement; together "income support" below). A single adult with no other income receives 750 kr a month. Earnings above 100 kr a month reduce the benefit by 65 öre per crown, so it falls to nil at earnings of about 1,254 kr. About 520,000 adults receive it: about 400,000 receive 300 kr or more (earnings below about 792 kr), of whom about 110,000 earn between 400 and 792 kr; about 120,000 receive less than 300 kr (earnings 792 to 1,254 kr), of whom about 95,000 receive less than 240 kr (earnings above about 885 kr). A household survey puts the standard-rated spending of adults receiving 300 kr or more at 300 to 600 kr a month each.
- **Housing support** (Housing Support Act). Up to 70% of rent, at most 550 kr a month, paid in full where "counted income" is 900 kr a month or less, and reduced by 40 öre per crown of counted income above 900 kr (so it ends at about 2,275 kr). Counted income is "income from all sources, including any benefit". About 380,000 adults receive it: 210,000 also receive income support (of whom about 30,000 receiving 300 kr or more of income support have counted income above 900 kr, in the taper), and 170,000 do not (about 120,000 in the taper, about 35,000 with counted income between 600 and 900 kr, and 15,000 below 600 kr).
- **Price indexation.** Schedule 2 benefits and the state pension (average 1,400 kr a month, about 1.1 million pensioners) are raised each April by the rise in the consumer price index to the previous September.
- **VAT.** Standard rate 20%; reduced rate 6% (food, books, public transport); exempt: residential rent, financial services, health and education. Businesses with turnover under 80,000 kr a year need not register; once registered, VAT is due on all sales. The standard-rated purchases that bear VAT which no one can reclaim total about 360 billion kr a year net of tax: household purchases about 245 billion (about 4,250 kr a month per adult), government purchases about 35 billion, and inputs bought by exempt businesses (banks, insurers, private landlords) about 80 billion. Net national income is about 420 billion kr. Standard-rated goods weigh about 55% in the consumer price index.

**Figures for arithmetic.** The payment costs 4.8 million × 300 kr × 12 = 17.28 billion kr a year. The offset saves about 1.44 billion (400,000 × 300 × 12) plus about 0.22 billion (120,000 × about 150 × 12) = 1.66 billion. Four points of VAT on the standard-rated base is 4% of 360 billion = 14.4 billion before any response; the Treasury projects 13.6 billion with responses, of which about 1.3 billion is paid by the government on its own purchases. The Payments Agency costs about 140 million a year, and 90 million to set up. The tax per crown of net price rises by 4 öre (a tax-inclusive price rises by at most 1.24/1.20 − 1, about 3.3%): an adult who buys S kr a month of standard-rated goods (net of tax) pays at most 0.04 × S kr more, so the 300 kr payment covers the full rise for anyone buying less than 7,500 kr a month. If instead the tax is borne by sellers' net prices, and so by factor incomes, 14.4 billion is about 3.4% of net national income. Housing support under U1-a saves roughly 0.18 billion a year (the payment is counted and pushes counted income up by 300 kr); under U1-b it costs roughly 0.04 billion more (income support falls by 300 kr and the payment is not counted, so counted income falls for the 30,000 in the taper). With the full static VAT and the government's own VAT counted as revenue, the Consolidated Fund is short by about 1.2 billion a year under U1-a and 1.4 billion under U1-b; on the Treasury's projection, net of the government's own VAT, about 3.3 and 3.5 billion.

The bill was published on 15 January 2027 and enacted on 1 April 2027. The VAT rise and the first payment take effect on 1 January 2028. No expiry. The payment is fixed at 300 kr and is not indexed.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Korsland. Just outside: Dornholt (standard VAT 21%); Varrin, 8 km from Kessa. | §1. |
| Announced / enacted / effective / expires | Announced 15 January 2027; enacted 1 April 2027; effective 1 January 2028; no expiry. | §1, §20. |
| Enforcement (who, penalties, resources) | The Payments Agency (new) pays the payment and checks residence by matching the population register; false claims are an offence (repayment plus a penalty of up to 5,000 kr). The Tax Office collects VAT as now. | §6, §14. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Basic payment | `lump_sum_subsidy` | Adults habitually resident | The Payments Agency pays; every adult resident for 24 of the last 36 months is entitled | 300 kr a month, not taxable (§8), not indexed. Funded from the Consolidated Fund (§11). | Adults resident for less than 24 of the last 36 months. |
| K2 Offset | Benefit reduction | Schedule 2 benefits | Recipients | "Any Schedule 2 benefit shall be reduced by the amount of the payment, but not below nil." (§5(1)) A person whose benefit is reduced to nil keeps a nil-rate entitlement for the purposes of other enactments (§5(3)), so free prescriptions and other passported help are unchanged. | — |
| K3 VAT rise | `ad_valorem_tax` | Standard-rated supplies | VAT-registered sellers | Standard rate 20% to 24%. Reduced rate and exemptions unchanged. "The additional revenue shall be applied to the cost of the payment" (§12). No provision for any shortfall. | Reduced-rate and exempt supplies; businesses under the 80,000 kr registration threshold. |
| K4 Payments Agency | Administration | K1 | The Agency, funded from the general budget | About 140 million kr a year; 90 million to set up in 2027. | — |

Unclear provision:
- **U1, the payment in the housing means test.** §9: "The payment is not a benefit for the purposes of any other enactment." The Housing Support Act counts "income from all sources, including any benefit". Reading U1-a: the payment is still income from a source, so it is counted; §9 only keeps it out of rules that refer to benefits as such (the benefit cap). Reading U1-b: §9 was meant to keep the payment out of every means test, so it is not counted. The Housing Ministry has issued no guidance and the explanatory notes are silent.

Readings get no probability; where a sign depends on U1, one sign per reading is given.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Binary: a transfer from the state. For an adult who will stay resident, it is a transfer no choice avoids (CR-1, operation 4: a change in means alone, CR-4). Because it is lost by leaving the country, it is also operation 3 on the option of emigrating (CR-1, 0.7). | Yes, given payment (A-4). | SB-1, OC-1 (1.0), CR-4 (means alone), CR-8b, RS-11, TS-3 |
| K2 | Binary: for those receiving 300 kr or more, K1 and K2 together do nothing at their present earnings (the payment replaces 300 kr of benefit), but they change what earning more brings: above about 792 kr of earnings the 65% withdrawal no longer applies. That is operation 3 on earning above the line, and nothing below it (CR-1, 0.9: operation per range). For those receiving less than 300 kr, the two together are a transfer of 300 kr less the benefit (operation 4) and remove the withdrawal on their earnings (operation 3). | Yes (A-5 for a response). | CR-1 (0.9), CR-4, CR-4 exception, CR-12 (0.8: two items) |
| K3 | Binary: a tax on the option of buying standard-rated goods (CR-1, operation 3), which changes their price relative to reduced-rate goods, exempt goods, leisure, home production, untaxed informal supply and purchases in Dornholt. | Yes (A-1). | TX-1, TX-2, TX-4, TX-5, TX-9, DM-1, RS-1, RS-3, RS-4, RS-5, RS-8, RS-9, RS-14, RS-17 (1.0), CR-7c |
| K4 | Binary: administration from the general budget. | Yes | OC-3, OC-1 (who pays) |
| Existing: housing support | Interacts with K1 and K2 through counted income, per reading of U1. | Yes | CR-1, CR-8b, CR-4 |
| Existing: price indexation | Interacts with K3: the VAT rise raises the index and so the benefits and pensions paid from April 2029. | Yes (A-24) | CR-1, CR-8b |

**Which classes face a change in means alone.** Taken component by component, K1 is a change in means alone for every resident adult who will stay, and K3 is a relative-price change for every buyer. No class faces K1 alone: every adult also buys standard-rated goods. The method is applied in two steps. First, the money amounts of the two changes in means (the payment, less what K3 takes from the class) are combined by arithmetic where the case's figures allow (CR-12e), giving each class's net change in means. Second, CR-4 is applied to the relative-price changes, and CR-4's exception to the net change in means, with a premise wherever a named use is claimed (CR-4, "a change in means alone"; Q19).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `adults.resident` | Every adult entitled to the payment | Receive 300 kr a month; lose it by leaving the country. |
| `recipients.full_offset` | About 400,000 adults receiving 300 kr or more of income support (earnings below about 792 kr) | Payment and offset cancel at present earnings; earnings above 792 kr are no longer withdrawn at 65%. Pay more for standard-rated goods. Sub-class `recipients.full_offset.near`: about 110,000 earning 400 to 792 kr. |
| `recipients.taper_exit` | About 120,000 adults receiving less than 300 kr (earnings 792 to 1,254 kr) | Gain 300 kr less their benefit; keep all of any extra earnings. Split `.low` (benefit under 240 kr, about 95,000) and `.high` (240 to 300 kr, about 25,000). |
| `adults.lower` | About 3.3 million adults not on income support whose income and standard-rated spending are both under 7,000 kr a month (including about 1.1 million pensioners) | Gain 300 kr; pay at most 280 kr more in VAT however it is shared. |
| `adults.middle` | About 730,000 adults not in either group | Gain 300 kr; may pay more or less than that. |
| `adults.higher` | About 250,000 adults whose income and standard-rated spending both exceed 10,000 kr a month | Gain 300 kr; bear at least about 340 kr however the VAT is shared (A-3). |
| `households.housing_taper` | About 120,000 adults on housing support, in its taper, not on income support | U1-a: support falls by up to 120 kr. U1-b: no change. |
| `households.near_threshold` | About 35,000 adults on full housing support with counted income 600 to 900 kr, not on income support | U1-a: the payment pushes them into the taper, so 40 öre of each further crown earned is withdrawn. |
| `households.both_taper` | About 30,000 adults on income support (300 kr or more) and in the housing taper | U1-a: counted income unchanged (300 kr of benefit replaced by 300 kr of payment). U1-b: counted income falls by 300 kr, so support rises by up to 120 kr. |
| `buyers.current`, `sellers.current` | Buyers and VAT-registered sellers of standard-rated goods | The tax wedge rises by 4 öre per crown of net price. |
| `sellers.small_unregistered` | Businesses under the 80,000 kr registration threshold | Their untaxed price is now further below registered rivals'; crossing the line now costs 24% of all sales. |
| `sellers.exempt` | Banks, insurers, private landlords | Pay more VAT on inputs and cannot reclaim it. |
| `renters.low_cost` | Tenants in the market low-cost rental segment | Rent is exempt; demand and landlords' costs change. |
| `buyers.border` | Shoppers in Kessa and other border towns | Standard-rated goods now cheaper in Varrin (21%) than at home (24%). |
| `sellers.border`, `owners.border_retail` | Kessa retailers and owners of their premises | Lose border shoppers; Dornholt shoppers stop coming. |
| `neighboring_jurisdictions` | Varrin retailers, and Dornholt shoppers who came to Kessa | Gain Korsland shoppers; Dornholt shoppers no longer gain by crossing. Owners of Varrin retail premises: `owners.border_retail.varrin`. |
| `workers.low_wage` | Workers in jobs paying under about 1,500 kr a month for part-time work | Labor supplied by recipients and by `adults.lower` changes. |
| `emigrants.prospective` | Residents who would move abroad | Leaving now forfeits 3,600 kr a year. |
| `immigrants.prospective` | Dornholt workers who might move to Korsland | Moving in now brings the payment after 24 months. |
| `claimants` | Those who might claim the payment falsely | A new payment to claim. |
| `pensioners` | State pensioners | Part of `adults.lower`; their pension is indexed. |
| `treasury` | The Consolidated Fund | Pays K1, saves on K2 and (U1-a) housing support, collects K3. |
| `officials.enforcement` (`payments_agency`) | The Payments Agency | New task. |
| `taxpayers`, recipients of other spending, future taxpayers | Whoever makes up the shortfall | §11 and §12 say nothing about it. |
| `lobbying groups` | Recipients' groups, pensioners, retailers, sellers seeking the reduced rate | Concentrated stakes in the payment level, indexation, U1 and the rate lists. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `adults.resident` | `resources_available_other_uses` (the payment: item 1) | increase | short (from January 2028) | CR-1, CR-8b, SB-1 | none |
| C-2 | `treasury` | `subsidy_outlay` (the payment) | increase | short | SB-1, CR-8b | none |
| C-3 | `recipients.full_offset`, `recipients.taper_exit` | `resources_available_other_uses` (Schedule 2 benefit: item 2) | decrease | short | CR-1, CR-8b | none |
| C-4 | `treasury` | `subsidy_outlay` (Schedule 2 benefits) | decrease | short | CR-8b | none |
| C-5 | `buyers.current` | `price_paid` (standard-rated goods, tax-inclusive) | increase | short | TX-2, CR-5c | A-1 |
| C-6 | `treasury` | `tax_revenue` (VAT) | increase | short | TX-1 | none |
| C-7 | `households.housing_taper`, `households.near_threshold` | `resources_available_other_uses` (housing support: item 3) | U1-a: decrease; U1-b: no_change | short | CR-1, CR-8b | none |
| C-8 | `households.both_taper` | `resources_available_other_uses` (housing support: item 3) | U1-a: no_change; U1-b: increase | short | CR-1, CR-8b | none |
| C-9 | `treasury` | `subsidy_outlay` (housing support) | U1-a: decrease; U1-b: increase | short | CR-8b | none |

C-1 to C-6 are what the Act's supporters point to: every adult is paid, those on income support have their benefit reduced by the same amount, and VAT goes up to pay for it. Each payment is recorded on both sides (CR-8b).

**Housing support and U1 (C-7 to C-9).** Housing support is reduced by 40 öre per crown of counted income above 900 kr. Under U1-a the payment is counted. For an adult not on income support it adds 300 kr to counted income, so support in the taper falls by up to 120 kr (C-7, U1-a: decrease). For an adult on income support of 300 kr or more, the payment replaces 300 kr of benefit, which was itself counted, so counted income is unchanged (C-8, U1-a: no_change). Under U1-b the payment is not counted. Adults not on income support see no change (C-7, U1-b: no_change); adults on income support lose 300 kr of counted benefit and gain uncounted payment, so their counted income falls and support in the taper rises by up to 120 kr (C-8, U1-b: increase). The reading thus decides which of two groups gains: under U1-a the low-paid workers on housing support lose part of the payment; under U1-b those on income support gain housing support they did not have. The Treasury's housing outlay moves the opposite way to the households' receipts under each reading (C-9). These are signs by construction on the provisions, so they need no assumption. (Adults with less than 300 kr of income support in the taper gain 300 kr less their benefit in counted income under U1-a, and lose their benefit from it under U1-b; they are few and are left in the text.)

**Who pays the VAT (C-5).** TX-2 gives `price_paid` up and/or `net_price_received` down, at least one. A-1 (the rise passes largely into shelf prices within a year) is needed to sign C-5. Without it, part of the tax falls on sellers' net prices and so on the incomes of those who supply labor and capital to them. The split matters for who is a net gainer: a class whose income is a benefit fixed in money (income support, pensions) bears the tax only through prices. Rothbard's first law of incidence (DM-1, dispute; Q3) would put the burden on factor incomes; under that view `recipients.full_offset` bear none of it. The totals in section 7 are signed so that they hold under any split where they can be (A-3), and per class where they cannot.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-10 | `buyers.current`, `sellers.current` | `tax_share_borne` (VAT rise, buyers against sellers) | ambiguous | short to medium | DM-1, CR-7b | A-1 |
| C-11 | `recipients.full_offset.near` | `employment` (+), `hours_worked` (+) | at_least_one_increase | short to medium | CR-1 (0.9), CR-4b, CR-12e (arithmetic), CR-12a | A-5 |
| C-12 | `recipients.taper_exit` | `hours_worked` | ambiguous | short to medium | CR-4b, CR-4 exception, CR-12b | A-6 |
| C-13 | `adults.lower` (in work) | `hours_worked` | decrease | medium | CR-4b (x: work for taxed goods, y: leisure), CR-4 exception with A-6, CR-12a, CR-12d | A-1, A-29 |
| C-14 | `households.near_threshold` (in work) | `hours_worked` | U1-a: decrease; U1-b: decrease | medium | CR-4b, CR-1 (0.9), CR-12a, CR-12d | A-1, A-29 |
| C-15 | `adults.higher` (in work) | `hours_worked` | ambiguous | medium | CR-4b, CR-4 exception, CR-12b | A-1, A-3, A-6 |
| C-16 | `recipients.full_offset` | `quantity_traded` (standard-rated goods) | decrease | short | TX-2, RS-1, CR-4c, CR-4 exception, CR-12a | A-1, A-7, A-30 |
| C-17 | `recipients.full_offset` | `quantity_substitute` (reduced-rate goods) | ambiguous | short | RS-1, CR-4 exception, CR-12b | A-1, A-7 |
| C-18 | `adults.lower` | `quantity_traded` (standard-rated goods) | ambiguous | short to medium | TX-2, CR-4c, CR-4 (means alone), CR-12b | A-1, A-7 |
| C-19 | `adults.lower` | `quantity_substitute` (reduced-rate and exempt goods) | increase | short to medium | RS-1, CR-4 (means alone), CR-12a | A-1, A-7 |
| C-20 | `adults.higher` | `quantity_traded` (standard-rated goods) | decrease | short to medium | TX-2, CR-4c, CR-4 exception, CR-12a | A-1, A-3, A-7 |
| C-21 | `buyers.current` (all buyers) | `quantity_traded` (standard-rated goods, total) | ambiguous | short to medium | TX-2, CR-4 (means alone), CR-12b | A-1, A-7 |
| C-22 | `buyers.border` | `cross_border_purchases` (standard-rated goods bought in Dornholt) | increase | short | RS-4, TX-4 | A-1, A-8 |
| C-23 | `neighboring_jurisdictions` (Dornholt shoppers) | `cross_border_purchases` (standard-rated goods bought in Korsland) | decrease | short | RS-4, TX-4 | A-1, A-8 |
| C-24 | `sellers.current` | `reclassification` (goods and bundles reshaped into reduced-rate or exempt categories) | increase | short to medium | RS-5, TX-4 | A-10 |
| C-25 | `sellers.current`, `buyers.current` | `informal_activity` (unrecorded cash sales and services) | increase | short | RS-3, TX-4, CR-4 (x: comply, y: evade) | A-11 |
| C-26 | `sellers.small_unregistered` | `number_of_sellers` (just below the 80,000 kr threshold) | increase | short to medium | RS-17 (1.0: notch), CR-1 (1.0: notch), CR-4 | A-12 |
| C-27 | `sellers.small_unregistered` | `reclassification` (businesses split to stay under the threshold) | increase | medium | RS-17, RS-5 | A-12 |
| C-28 | `buyers.current` | `quantity_traded` (durable standard-rated goods, 1 April to 31 December 2027) | increase | short | RS-8, CR-10a | A-13 |
| C-29 | `buyers.current` | `quantity_traded` (durable standard-rated goods, January to June 2028) | ambiguous | short | RS-8 (0.9: more timing chains), CR-4 (means alone), CR-12b | A-13, A-14 |
| C-30 | `emigrants.prospective` | `job_changes` (moves abroad) | decrease | medium | RS-11, CR-3 | A-4, A-15 |
| C-31 | `immigrants.prospective` | `job_changes` (moves from Dornholt into Korsland) | increase | medium to long | CR-4 (x: stay in Dornholt, y: move), CR-10a | A-16 |
| C-32 | `claimants` | `legal_breach` (false residence claims) | increase | short | RS-3, CR-4 | A-17 |
| C-33 | `lobbying groups` | `lobbying_effort` (on questions that exist only under the Act: payment level, indexation, U1, the offset) | increase | short to medium | RS-7 (1.0), CR-4 (1.0), CR-12 (0.9: activities that exist only under the policy) | A-18 |
| C-34 | `sellers.current` | `lobbying_effort` (for reduced-rate status) | increase | medium | RS-7 (1.0), CR-4 (1.0) | A-18, A-20 |

**Recipients near the old exit point (C-11).** For an adult on 300 kr or more of income support, earning less than about 792 kr, the payment and the offset cancel at present earnings (CR-1, 0.9: no operation below the line). Above about 792 kr, though, the benefit would have been under 300 kr, so it is now nil and every further crown earned is kept: the 65% withdrawal disappears over the band from 792 to 1,254 kr. The option of earning above 792 kr has become better and nothing else about their situation has changed except the VAT (CR-4b; A-5: some of them can find work or more hours that take them over the line). The VAT pushes the other way for every hour, since each crown earned buys about 3% fewer standard-rated goods (CR-4b, x: work, y: leisure). On the hours above 792 kr, what the recipient keeps rises from 35 öre to about 97 öre per crown (net of the VAT); on hours below, it falls from 35 öre to about 34. That is a dominance premise by arithmetic on the case's figures (CR-12e) for the option of working past the line. The VAT also leaves these recipients poorer (C-45), which under A-6 pushes toward more work, the same direction. Some take a job, some add hours: recorded as a group (C-11). Recipients far below the line (no earnings and no prospect of earnings above 792 kr) are not in `.near`: for them only the VAT chains act, opposing each other, and nothing is recorded.

**Recipients in the old taper (C-12).** For adults with less than 300 kr of benefit, extra earnings are now kept in full (the return to work rises, CR-4b) and their means rise by 300 kr less their benefit. CR-4's exception applies: the rise in means can move them toward fewer hours. With A-6 (fewer hours is among the uses on which a rise in means is spent) the two chains oppose: `ambiguous` (CR-12b).

**Everyone else in work (C-13 to C-15).** The payment is, for an adult not on income support, a change in means alone (CR-4): it tells us that spending on some uses rises by 300 kr, not which. The VAT is both a relative-price change (each hour of work buys fewer taxed goods, so x: work for goods, y: leisure or untaxed home production, and CR-4b gives fewer hours at the margin) and a change in means. Combining the two money amounts by arithmetic first: for `adults.lower`, the net change in means is positive (C-49). With A-6, a rise in means goes partly to fewer hours, which is the same direction as the relative-price chain: `decrease` (C-13; CR-12a). Without A-6, the means chain has no sign and the relative-price chain alone gives `decrease`; the two chains have the same sign, so the consequence holds if either chain's premises hold (CR-12d), and only A-1 and A-29 are listed. For `adults.higher`, the net change in means is negative (C-51); with A-6 that pushes toward more hours, against the relative-price chain: `ambiguous` (C-15). Adults near the housing threshold (C-14) add a third chain under U1-a: the payment pushes their counted income into the taper, so 40 öre of each further crown earned is withdrawn (CR-1, 0.9; CR-4b), the same direction. Under U1-b they are in the position of C-13. Both readings: `decrease`.

**What people buy (C-16 to C-21).** The VAT raises the price of standard-rated goods relative to reduced-rate food, exempt rent and services, and untaxed home production (RS-1, CR-4c: the substitution chain moves purchases away from standard-rated goods). The change in means moves purchases of every kind in the direction of the means, with A-7 (both kinds of goods are among the uses on which spending rises when means rise, and falls when they fall). CR-4's exception decides the rest per class:
- `recipients.full_offset` are poorer (C-45) and face dearer taxed goods. Standard-rated goods: both chains down (C-16). Reduced-rate goods: substitution up, means down: `ambiguous` (C-17). This is CR-4's exception where it bites: a price rise on something they spend much of their means on changes their total means, and the effect on the untaxed goods is opposite to substitution.
- `adults.lower` gain on net. Standard-rated goods: substitution down, means up: `ambiguous` (C-18). Reduced-rate and exempt goods: both up (C-19).
- `adults.higher` lose on net: standard-rated goods both down (C-20).
- All buyers together (C-21): the classes move in different directions and one class's own sign is ambiguous (C-18, kind 3), so the total is `ambiguous`. TX-2's `quantity_traded` decrease is the K3 chain alone; combined with K1, which returns the revenue (and more) to the same buyers, no sign follows (CR-12b). This is a combination across components, not a fault in TX-2 (TX-1 says the spending of the revenue is to be analyzed as a separate component and combined).

**The border (C-22, C-23).** With Korsland at 24% and Dornholt at 21%, standard-rated goods in Varrin are now cheaper than in Kessa by about 2.5% of the price, where they were dearer by about 0.8% (RS-4, TX-4; A-8). Some Kessa shoppers buy in Varrin (C-22), and Dornholt shoppers who bought in Kessa no longer gain by doing so (C-23). Both are signed against the 20% counterfactual.

**Reshaping, evasion and the threshold (C-24 to C-27).** The gap between the standard and reduced rates widens from 14 to 18 points, so reshaping a supply to fall under the reduced rate (food sold for consumption off the premises, books bundled with materials) pays more (C-24; RS-5; A-10). Evasion pays more as the rate rises (C-25; RS-3; A-11). The registration threshold is a notch: once a business's turnover passes 80,000 kr, VAT is due on all its sales (CR-1, 1.0; RS-17, 1.0). The cost of crossing rises from 20% to 24% of sales (for sales to households, who cannot reclaim it), so some businesses that would have grown past the line stay below it (C-26) or split (C-27). RS-17 states its first conclusion as "just below the threshold increases relative to just above"; re-signed against Korsland without the Act (CR-12, 1.0), it is the count just below the line that rises, from those who would have crossed (A-12).

**Timing (C-28, C-29).** The VAT rise is known from 1 April 2027 and starts on 1 January 2028, so purchases of durable standard-rated goods (cars, furniture, appliances) are brought forward into the window (C-28; RS-8; A-13). The expected payment, starting on the same date, adds to net gainers' means from then on: some buy durables they would not have bought, and some who can borrow bring purchases forward to before January (CR-10a). In January to June 2028 the dip from purchases brought forward is opposed by purchases funded by the payment (A-14): two timing chains, `ambiguous` (C-29; RS-8, 0.9: more timing chains; CR-12b). In the window before January both push up.

**Leaving and arriving (C-30, C-31).** The payment is lost by ceasing to reside. A resident who would have moved abroad (to work in Dornholt, say) now gives up 3,600 kr a year by going, so some stay (RS-11; CR-3; A-15). The mirror for arrivals: a Dornholt worker who moves to Korsland gains the payment after 24 months (CR-4, CR-10a; A-16). Note that arrivals pay the higher VAT from the day they come, and the payment only after two years.

**Claims and lobbying (C-32 to C-34).** A new payment conditional on residence invites some false claims (C-32; RS-3; A-17). By CR-4's 1.0 note, lobbying is signed against what would have been contested without the Act: the payment's level and indexation, the reading of U1 and the offset exist only under the Act, so lobbying on them rises against none (C-33). Reduced-rate status was contested without the Act too (the 6% list is reviewed every budget); the Act raises the stake in it by four points, so sellers spend more seeking it (C-34; RS-7, 1.0; A-20: the stake raises effort).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-35 | `sellers.border` (Kessa) | `quantity_traded` (all goods bought on border shopping trips, including reduced-rate food) | decrease | short | RS-9, CR-9 | food at Kessa shops: `complement` (note `trip`) to standard-rated goods bought on the same trip | A-8, A-9 |
| C-36 | `neighboring_jurisdictions` (Varrin sellers) | `quantity_traded` (sales to Korsland shoppers) | increase | short | RS-9, CR-9 | as C-35, `across_border` | A-8, A-9 |
| C-37 | `owners.border_retail` (Kessa) | `asset_value` (retail premises) | decrease | short (from 1 April 2027) | CR-7c, CR-10c, SB-4 | follows C-35 | A-8, A-22 |
| C-38 | `owners.border_retail.varrin` | `asset_value` (retail premises) | increase | short (from 1 April 2027) | CR-7c, CR-10c, SB-4 | follows C-36 | A-8, A-22 |
| C-39 | `sellers.exempt` (banks, insurers, private landlords) | `price_paid` (their services) (+), `quantity_supplied` (−) | at_least_one_as_stated | medium | RS-14, CR-9 | standard-rated inputs `input_to` exempt services | A-1, A-19 |
| C-40 | `renters.low_cost` | `price_paid` (market rents, low-cost segment) | ambiguous | medium | CR-6 (0.9: splitting a shift), CR-4, RS-14, CR-12b | rent and standard-rated goods: `substitute`; landlords' inputs `input_to` rental | A-7, A-19, A-21 |
| C-41 | `workers.low_wage` | `wage_rate` (low-wage part-time jobs) | ambiguous | medium | CR-6, CR-7a, CR-12b | labor: same market, recipients and others | A-5, A-6 |
| C-42 | `sellers.small_unregistered` (near the threshold) | `asset_value` | ambiguous | short | RS-17 (0.9: value of firms near the line), CR-7c, CR-12b | rivals above the line: `same_market_other_segment` | A-12, A-22 |
| C-43 | `recipients.full_offset`, `pensioners` | `resources_available_other_uses` (extra indexation from April 2029: item 4) | increase | medium | CR-1 (existing rule), CR-9 | indexation rule: `contract` (statutory) | A-1, A-24 |
| C-44 | `treasury` | `subsidy_outlay` (extra indexation of benefits and pensions) | increase | medium | CR-8b | as C-43 | A-1, A-24 |

**Border trips (C-35 to C-38).** A Kessa shopper who drives to Varrin for clothes or appliances buys groceries there on the same trip (RS-9; A-9), so Kessa shops lose reduced-rate sales too, and Varrin's gain them. Retail premises in Kessa lose part of their expected yield and those in Varrin gain; values move when the rise becomes expected (CR-7c, CR-10c; A-22), from the bill's publication in January 2027 by part and fully at enactment on 1 April 2027. Owners at that time bear or capture the change.

**Exempt sellers (C-39).** Banks, insurers and private landlords cannot reclaim VAT on what they buy, so the cost of their inputs rises by about 3% of the standard-rated part (RS-14). Their prices rise and/or their supply falls (at least one). All of them face the same rise, so by RS-14 the price rise dominates where their competitors are also exempt Korsland firms; but the pattern's group is what CR-6 licenses without a premise on supply, and is recorded as such.

**Rents (C-40).** Three chains reach market rents in the low-cost segment, where the stock is fixed in the short run (A-21), so a shift in demand goes to price (CR-6, 0.9). Rent is exempt, so it is now cheaper relative to taxed goods (CR-4: demand up for everyone); `adults.lower` have more means (demand up, A-7); landlords' input costs rise (C-39: up). Against these, `recipients.full_offset` who rent in the market are poorer, and with A-7 demand less (down). Their own chain is ambiguous (substitution up, means down: kind 3), so the combined sign is `ambiguous`. Housing support moves rents too, per reading (support falls for some tenants under U1-a and rises for others under U1-b); that does not change the sign.

**Low-wage jobs (C-41).** Recipients near the old exit point offer more labor (C-11); `adults.lower` in work offer fewer hours (C-13); those in the old taper may offer more or less (C-12). In the low-wage labor market these push the wage in opposite directions, and one is ambiguous: `ambiguous` (CR-12b, kind 3). **RS-22 does not apply.** Its precondition is a change in a term of some jobs other than the wage; nothing here changes any term of any job. What changes is workers' means and the return they keep from work. The effect of that on wages is CR-6 and CR-7a directly. A premise that workers with more means accept unpleasant jobs less readily (so that the wage in such jobs rises) is a premise on their rankings that the case does not support (A-31, p = 0.4, below the cut-off).

**Firms near the threshold (C-42).** RS-17's 0.9 clause: against the counterfactual, a business just below the line loses the value of growing past it, and gains from the higher tax on its registered rivals. No premise ranks the two: `ambiguous`.

**Indexation (C-43, C-44).** The VAT rise raises the consumer price index by about 1.8% (55% weight times 3.3%), so under the existing indexation rule benefits and pensions are raised by that much more from April 2029 than they would have been (A-24). The guarantee of 750 kr rises by about 13.5 kr more, the average pension by about 25 kr. This is the existing rule working on a higher index: the recipients' receipt and the Treasury's outlay are both recorded.

Stopping points. The suppliers of Kessa shops and the spending of their workers (depth 3, diffuse); the goods and services on which net gainers spend more and net losers less, beyond the classes above (CR-4, means alone: unnamed without a premise); the Dornholt budget's VAT receipts. The VAT is charged on imports and refunded on exports, so the rise does not change the relative price of Korsland goods abroad, and TX-8 is not used.

## 7. Combined effects

**Totals of several items in one variable.** Under CR-12's 0.8 note, where a policy moves named items of one variable in opposite directions, each item is recorded and the total is recorded separately. For each class the items of `resources_available_other_uses` are: the payment (C-1), the benefit offset (C-3), the VAT the class pays through prices or factor incomes (C-5, A-1 and A-3), housing support per reading (C-7, C-8), and from April 2029 extra indexation (C-43). For `recipients.full_offset`, the payment and the offset cancel exactly by construction (§5(1) reduces the benefit "by the amount of the payment"), so under CR-12f that pair is not reported as a consequence of its own; the total is reported because the VAT item remains.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-45 | `recipients.full_offset` | `resources_available_other_uses` (total: payment, offset, VAT) | decrease | short (to April 2029) | CR-12 (0.8: two items), CR-12f, TX-1, CR-3 (note) | A-1, A-30 |
| C-46 | `recipients.full_offset` | `resources_available_other_uses` (total, with extra indexation) | ambiguous | medium to long | CR-12b, CR-12g | A-1, A-24, A-30 |
| C-47 | `recipients.taper_exit.low` | `resources_available_other_uses` (total) | increase | short to medium | CR-12 (0.8), CR-12e (arithmetic) | A-2, A-3 |
| C-48 | `recipients.taper_exit.high` | `resources_available_other_uses` (total) | ambiguous | short to medium | CR-12 (0.8), CR-12b | A-1 |
| C-49 | `adults.lower` | `resources_available_other_uses` (total: payment, VAT, housing support) | U1-a: increase; U1-b: increase | short to medium | CR-12 (0.8), CR-12e (arithmetic), OC-1 | A-2, A-3 |
| C-50 | `adults.lower` | `resources_available_other_uses` (total) | ambiguous | long | CR-12b, CR-12g, TS-3 | A-1, A-3 |
| C-51 | `adults.higher` | `resources_available_other_uses` (total: payment, VAT) | decrease | short to long | CR-12 (0.8), CR-12e (arithmetic), TX-1 | A-3 |
| C-52 | `adults.middle` | `resources_available_other_uses` (total) | ambiguous | short to medium | CR-12b | A-1, A-3 |
| C-53 | `adults.lower` | `consumption` (+), `saving` (+), at constant prices | at_least_one_increase | short to medium | CR-4 (a change in means alone; 0.7: saving is a use), OC-1 (saving is a use), CR-8b | A-2, A-3 |
| C-54 | `adults.higher` | `consumption` (−), `saving` (−), at constant prices | at_least_one_decrease | short to long | CR-4 (means alone; 0.7: saving is a use), OC-1, CR-8b | A-3 |

**The arithmetic.**
- *C-45.* At present earnings the payment (+300 kr) and the offset (−300 kr) cancel; these recipients' income is a benefit fixed in money, so they bear the VAT only through prices, about 4 öre per crown of the 300 to 600 kr a month of standard-rated goods they buy (12 to 24 kr). With A-1 (the rise reaches prices) and A-30 (they keep buying some standard-rated goods: clothing, household goods, energy), the total is a decrease. Under a pure first-law incidence (no price rise), it would be no change. This is the class the Act's title most suggests is helped, and it is the one class made poorer with certainty given A-1.
- *C-46.* From April 2029 the guarantee is raised by about 13.5 kr more than without the Act (C-43). Against a VAT burden of 12 to 24 kr, some are over-compensated and some not: `ambiguous` for the class (CR-12g keeps this horizon separate from C-45).
- *C-47.* Benefit under 240 kr; earnings at most 1,254 kr; standard-rated spending at most about 900 kr. The burden is at most 0.04 × 900 = 36 kr through prices, or about 3.4% × 1,254 = 43 kr through factor incomes, or a mix. 300 − 240 − 43 > 0: an increase under any split (A-3, and A-2: prices do not rise by more than the tax).
- *C-48.* With benefits between 240 and 300 kr, the total runs from slightly negative to about 60 kr: `ambiguous` for the class.
- *C-49.* Income and standard-rated spending under 7,000 kr: the burden is at most 0.04 × 7,000 = 280 kr through prices or 3.4% × 7,000 = 240 kr through incomes, so the total is positive. Under U1-a, those in the housing taper also lose up to 120 kr; their counted income is under 2,275 kr, so their VAT burden is at most about 112 kr, and 300 − 120 − 112 > 0. Increase under both readings.
- *C-50.* The payment is fixed in money; the VAT is a share of prices. As prices rise, the payment's real value falls while the burden keeps its share (TS-3), so for the upper part of the class the total can turn negative within a decade: `ambiguous` in the long run.
- *C-51.* Income and spending above 10,000 kr: the burden is at least 0.04 × 10,000 = 400 kr through prices or 340 kr through incomes, more than 300 kr under any split (A-3). Decrease, and more so as the payment erodes.
- *C-53, C-54.* Means rise for `adults.lower` and fall for `adults.higher`. Which uses gain or lose is not said by CR-4 (a change in means alone), but saving is one of them (CR-4, 0.7; OC-1, 1.0): the claim is the group, at constant prices. A claim about any named good needs A-7 (C-16 to C-20). In money terms, `adults.higher` may spend more on consumption (prices are higher) while saving less; at constant prices, at least one falls.

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `recipients.full_offset`, `resources_available_other_uses`, short | Payment (C-1) | Offset (C-3, cancels the payment by construction); VAT (A-1) | CR-12f for the pair; nothing opposes the VAT item | **decrease** (C-45) |
| same, medium to long | Extra indexation (C-43) | VAT | None (figures straddle) | **ambiguous** (C-46) |
| `recipients.taper_exit.low`, total, short to medium | Payment | Offset (< 240 kr); VAT (≤ 43 kr) | Arithmetic (CR-12e) | **increase** (C-47) |
| `adults.lower`, total, short to medium | Payment | VAT (≤ 280 kr); U1-a: housing support (≤ 120 kr, only where VAT ≤ 112 kr) | Arithmetic | **increase** under both readings (C-49) |
| `adults.higher`, total | Payment | VAT (≥ 340 kr) | Arithmetic, A-3 | **decrease** (C-51) |
| `recipients.full_offset.near`, employment and hours | Return above 792 kr (65% withdrawal removed); poorer (A-6) | VAT lowers what each hour buys | Arithmetic on retention above the line (CR-12e) | **at_least_one_increase** (C-11) |
| `recipients.taper_exit`, hours | Withdrawal removed | Richer (A-6); VAT relative price | None | **ambiguous** (C-12) |
| `adults.lower`, hours, medium | — | VAT relative price; richer (A-6) | None needed | **decrease** (C-13) |
| `adults.higher`, hours, medium | Poorer (A-6) | VAT relative price | None | **ambiguous** (C-15) |
| `buyers.current`, standard-rated quantity (total) | Net gainers' means (A-7) | Substitution (TX-2); net losers' means | None; one class's chain is itself ambiguous (kind 3) | **ambiguous** (C-21) |
| `buyers.current`, durables, January to June 2028 | Purchases funded by the payment (A-14) | Purchases brought forward into 2027 (A-13) | None | **ambiguous** (C-29) |
| `renters.low_cost`, rents, medium | Rent relatively cheaper; gainers' means; landlords' costs | Losers' means (kind 3 for `recipients.full_offset`) | None | **ambiguous** (C-40) |
| `workers.low_wage`, wage, medium | Fewer hours from `adults.lower` | More labor from `recipients.full_offset.near` | None; C-12 is kind 3 | **ambiguous** (C-41) |
| `treasury`, `fund_balance`, short to medium | VAT (C-6); offset savings (C-4); U1-a housing savings | Payment (C-2); U1-b housing cost; agency (C-59); from 2029 indexation (C-44) | Arithmetic: shortfall of 1.2 to 3.5 billion kr under either reading | **decrease** under both readings (C-56) |
| `treasury`, `tax_revenue_vs_static_projection` | Net gainers buy more taxed goods (A-7) | Avoidance (C-22, C-24, C-25); substitution | None | **ambiguous** (C-58) |

**Final check** (`03_workflow.md`).
1. Uncombined chains: every class's money items are combined in one total (C-45 to C-52), and hours, purchases, rents and wages each combine the relative-price chain with the change in means. The timing chain from the payment is combined with the pull-forward (C-29). The Treasury's items are netted in C-56, and indexation is included in its medium-run sign.
2. Group signs: hours or jobs (C-11), consumption or saving (C-53, C-54), exempt sellers' price or supply (C-39), payers of the shortfall (C-55).
3. Baseline: every sign is against Korsland without the Act, with VAT at 20% and indexation in force. The border signs are against a counterfactual in which Dornholt shoppers crossed into Kessa. RS-17's "below relative to above" is re-signed (C-26). The housing support signs per reading are against the support each class would have received without the payment.
4. Worse off is not poorer: `resources_available_other_uses` is signed only on money received or on VAT paid by classes that keep buying taxed goods (A-30 for `recipients.full_offset`). Those who stop buying a taxed good are worse off by their own ranking but not signed poorer.
5. Timing shifts: durables per window (C-28, C-29). The payment and the VAT start on the same date, so there is no window in which one applies without the other.
6. Both sides of every transfer: payment (C-1, C-2), offset (C-3, C-4), VAT (C-5, C-6, payers in C-45 to C-52), housing support (C-7 to C-9), indexation (C-43, C-44), the shortfall (C-55, C-56), border trade (C-35, C-36), border property (C-37, C-38).
7. Every actor class, every core rule: CR-7c for border property and for firms near the threshold; CR-6 for rents (with a premise on the fixed stock) and in the labor market; enforcement costs for the Payments Agency (C-59) and its payers (C-55). CR-6 for reduced-rate goods: their price would rise only if their supply could not expand (A-26, p = 0.35, below the cut-off; not reported).
8. Unstated premises: the ranking premises A-6 and A-7 are stated for every named use; the incidence premises A-1 to A-3 for every total.
9. Baseline of every pattern: TX-1, TX-2, TX-4, RS-1, RS-3, RS-4, RS-5, RS-8, RS-9, RS-11, RS-14, SB-1, SB-4 and OC-1 conclude against no Act. RS-17's first clause compared below with above and is re-signed. DM-1 and TX-9 compare by definition (shares; a static projection). RS-22 and RS-23 are not used.

## 8. Time structure

- **15 January to 31 March 2027: the bill.** Retail property in Kessa and Varrin starts to move as passage becomes likely (C-37, C-38; CR-7c, probability). Lobbying on the payment, U1 and the rate lists begins (C-33, C-34).
- **1 April to 31 December 2027: enacted, not yet in force.** Durable purchases are brought forward (C-28). The Payments Agency is set up (90 million kr) and adults register (C-61). Small businesses near the threshold plan to stay below it (C-26).
- **January 2028 to March 2029: first period.** Payments start and VAT rises together. Benefit recipients with 300 kr or more are poorer by the VAT on what they buy (C-45). Border shopping moves to Varrin (C-22, C-35). The dip in durables is offset in part by purchases funded by the payment (C-29). Labor supply responses grow as people learn the new rules (TS-8).
- **From April 2029.** Benefits and pensions are raised by the higher index (C-43, C-44), so recipients' totals become ambiguous (C-46).
- **Long run.** The payment is fixed at 300 kr in money (TS-3). As prices rise, its real value falls, while the VAT keeps its share of prices: net gains shrink for every class (C-50) and the Consolidated Fund's shortfall shrinks or turns (C-57). Moves abroad avoided (C-30) and arrivals (C-31) accumulate.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-55 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` | at_least_one_decrease | The shortfall of 1.2 to 3.5 billion kr a year, and the Payments Agency's cost, are met from the Consolidated Fund with no tax named: other taxes, other spending or borrowing. | OC-1 (who pays), OC-3, CR-8 (0.7: payers from the general budget), TX-1 |
| C-56 | `treasury` | `fund_balance` (Consolidated Fund: VAT, offset and housing savings, less payment, indexation and agency) | U1-a: decrease; U1-b: decrease | Net of K1 to K4; signed by arithmetic. | CR-8 (1.0: receipts into the same budget), OC-1 (1.0) |
| C-57 | `treasury` | `fund_balance` (long run) | ambiguous | The fixed payment erodes while VAT grows with prices. | TS-3, CR-12g |
| C-58 | `treasury` | `tax_revenue_vs_static_projection` (VAT) | ambiguous | Avoidance shrinks the base; net gainers' purchases may enlarge it. | TX-9, TX-4, CR-12b |
| C-59 | `officials.enforcement` (Payments Agency) | `enforcement_cost` | increase | About 140 million kr a year and 90 million to set up. | OC-3, CR-8c |
| C-60 | `sellers.current` | `compliance_cost` (repricing, tills, systems, rate disputes) | increase | Time and money spent changing prices and systems. | TX-5, CR-8c |
| C-61 | `adults.resident` | `compliance_cost` (registering and proving residence) | increase | Time spent registering. | OC-2, CR-8c |

**Receipts into the same budget (OC-1, 1.0; CR-8, 1.0).** §12 applies the extra VAT "to the cost of the payment", but both flow through the Consolidated Fund, and the Act does not say what happens if they differ. The VAT receipt (C-6) and the payment outlay (C-2) are recorded as two items, and the net separately (C-56). The arithmetic in section 1 gives a shortfall under both readings, even counting the full static VAT and the VAT the government pays on its own purchases. That last part (about 1.4 billion kr) is the budget paying itself: it takes no means from anyone (CR-8b), so the shortfall on the Treasury's own projection is larger. Who meets the shortfall is not named, so the payers are a group (C-55; OC-1, who pays).

**What the VAT payers give up.** OC-1 says resources taken leave less for other uses; which uses, CR-4 (a change in means alone) does not say, and saving is one of them (OC-1, 1.0). The signs in C-53 and C-54 are therefore groups, and named goods appear only with A-7.

**TX-9 (C-58).** Applied as written, TX-9 gives `decrease`: TX-4's avoidance shrinks the base. But the same Act gives most buyers more means, and with A-7 some of that is spent on standard-rated goods, which enlarges the base. That chain is derived with a premise at p ≥ 0.5, so the combined sign is `ambiguous` (CR-12, 0.8, kind 2). TX-9's Unless clause covers a tax that pushes up the price it is levied on; it does not cover a tax whose revenue is returned to the buyers (Gaps found, c).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most of the VAT rise passes into standard-rated shelf prices within a year. | other | 0.75 | Past VAT changes in Korsland and Dornholt; retailers' statements. | C-5 not reported; C-45 becomes no change for benefit recipients; the totals rest on A-3. |
| A-2 | Tax-inclusive prices rise by no more than the tax (4 öre per crown of net price). | other | 0.85 | Past VAT changes; competition in retail. | C-47 and C-49 need wider margins; some members leave the classes. |
| A-3 | Whatever part of the VAT is not passed into prices falls on factor incomes roughly in proportion to them (about 3.4%). | other | 0.6 | Standard incidence of a broad consumption tax; Rothbard's first law as a limiting case (Q3). | C-47, C-49, C-51, C-53 and C-54 need the price-side figures alone; C-51 and C-54 rest on A-1. |
| A-4 | The payment is paid and residence is checked against the population register. | enforcement | 0.9 | The Agency's budget; register quality. | C-30 weakens; C-32 grows. |
| A-5 | Some recipients earning 400 to 792 kr can find work or extra hours that take them above 792 kr. | substitutability | 0.7 | Part-time job openings; current earnings spread. | C-11 not reported. |
| A-6 | Fewer hours of work is among the uses on which adults spend part of a rise in means, and which they give up first when means fall. | other | 0.65 | Hours of second earners and part-timers after earlier benefit changes. | C-13 and C-14 rest on the relative-price chains alone (still `decrease`); C-12 and C-15 become `increase` and `decrease` respectively. |
| A-7 | Both standard-rated and reduced-rate goods are among the uses on which these classes' spending rises when their means rise, and falls when they fall. | other | 0.7 | Household budget surveys by income. | C-16, C-17, C-19, C-20 lose their means chains; C-18 becomes `decrease`; C-58 becomes `decrease`. |
| A-8 | Some Kessa shoppers buy in Varrin when standard-rated goods there are about 2.5% cheaper; some Dornholt shoppers stop coming to Kessa. | mobility | 0.8 | 8 km; Varrin retail park; surveys of current cross-border trips. | C-22, C-23 and C-35 to C-38 not reported. |
| A-9 | Shoppers who go to Varrin buy groceries on the same trip. | other | 0.7 | Trip surveys; Varrin supermarket. | C-35 and C-36 cover only standard-rated goods. |
| A-10 | Some sellers can reshape supplies into reduced-rate or exempt categories at a cost below the four points. | other | 0.6 | Earlier disputes over catering and bundles. | C-24 not reported. |
| A-11 | VAT enforcement is imperfect; some sales go unrecorded. | enforcement | 0.75 | Tax Office gap estimates. | C-25 not reported. |
| A-12 | Some businesses near 80,000 kr of turnover can stay below the threshold or split. | other | 0.7 | Bunching below the threshold now. | C-26, C-27, C-42 not reported. |
| A-13 | Some purchases of durables can be moved before 1 January 2028. | other | 0.8 | Car and furniture sales before earlier rate rises. | C-28 not reported; C-29 becomes `increase`. |
| A-14 | Some net gainers spend part of the payment on durables in its first months. | other | 0.55 | Spending after earlier one-off rebates. | C-29 becomes `decrease`. |
| A-15 | Some residents who would have moved abroad value 3,600 kr a year enough to stay. | mobility | 0.6 | Emigration to Dornholt for work; wage gaps. | C-30 not reported. |
| A-16 | Some Dornholt workers move to Korsland, waiting 24 months for the payment. | mobility | 0.5 | Cross-border commuting; housing costs. | C-31 not reported. |
| A-17 | Some false residence claims are made. | enforcement | 0.6 | Experience with residence-based benefits. | C-32 not reported. |
| A-18 | Recipients' groups, pensioners' associations and retailers can organize at a cost below their stakes. | other | 0.85 | Existing associations; hearings on the bill. | C-33, C-34 not reported. |
| A-19 | Exempt sellers cannot replace standard-rated inputs at the old cost. | substitutability | 0.8 | Input structure of banks and landlords. | C-39 not reported; C-40 loses a (+) chain. |
| A-20 | The higher stake in reduced-rate status raises the effort spent seeking it. | other | 0.8 | Submissions at past budget reviews. | C-34 not reported. |
| A-21 | The low-cost rental stock cannot grow within a year. | durability | 0.8 | Construction times. | C-40 unchanged (`ambiguous`). |
| A-22 | Buyers of property expect the VAT rate and the payment to last. | expectations | 0.75 | No expiry; cross-party support. | C-37, C-38, C-42 shrink. |
| A-24 | The indexation rule is applied as now, so the VAT rise raises benefits and pensions from April 2029. | other | 0.85 | The rule has been applied every year for twenty years. | C-43, C-44 not reported; C-46 becomes `decrease`. |
| A-26 | The supply of reduced-rate goods (mostly food) cannot expand at an unchanged cost within the period. | durability | 0.35 | Food is widely traded and imported. | Below the cut-off: the price of reduced-rate goods is not signed. |
| A-29 | Some adults in work can choose their hours (part-time, second earners, the self-employed). | other | 0.75 | Labor force survey. | C-13 and C-14 not reported. |
| A-30 | Benefit recipients keep buying some standard-rated goods (clothing, household goods, energy). | other | 0.95 | Household budget survey. | C-45 not reported. |
| A-31 | Workers with more means accept jobs with unpleasant conditions less readily, so the wage in such jobs rises. | other | 0.4 | No direct evidence; depends on rankings. | Below the cut-off: no compensating-differential claim is reported (RS-22 does not apply in any case). |

## 11. Report

**The policy.** From January 2028 every adult who has lived in Korsland for two of the last three years receives 300 kr a month, untaxed and not indexed. Income support is reduced by the same amount, not below nil. The standard VAT rate rises from 20% to 24% to pay for it. It is unclear whether the payment counts as income in the means test for housing support.

**Visible consequences.** Adults are paid (C-1); income support is cut by the payment (C-3); standard-rated prices rise (C-5); the Treasury pays out and collects (C-2, C-4, C-6).

**Invisible consequences.**
- *Who gains and who loses in money.* Adults who are not on income support and whose income and taxed spending are under about 7,000 kr a month gain on net (C-49), and spend or save more (C-53). Adults above about 10,000 kr lose on net (C-51) and spend or save less (C-54). Recipients of income support of 300 kr or more gain nothing from the payment, which replaces their benefit, and pay the higher VAT on what they buy: they are poorer until indexation catches up in April 2029, after which some are and some are not (C-45, C-46). Recipients near the old exit point gain (C-47).
- *Work.* Recipients who earn close to 792 kr a month can now keep almost all of what they earn above it, and some work more (C-11). Most other adults in lower-income groups work fewer hours (C-13, C-14). For recipients in the old taper and for higher-income adults the direction is open (C-12, C-15), and so is the low wage (C-41).
- *What people buy.* Purchases move from standard-rated toward reduced-rate and exempt goods (C-16, C-19, C-20); for some classes the direction depends on how means changed (C-17, C-18, C-21). Durables are bought before January 2028 (C-28).
- *The border.* Kessa shoppers buy in Varrin, taking grocery spending with them; Kessa retail property loses value and Varrin's gains (C-22, C-23, C-35 to C-38).
- *Business.* More reshaping into reduced-rate categories, more unrecorded sales, more businesses staying under the registration threshold (C-24 to C-27); exempt sellers charge more or supply less (C-39); more lobbying (C-33, C-34).
- *Moving.* Fewer residents move abroad (C-30); some Dornholt workers move in (C-31).
- *The budget.* The VAT does not cover the payment under either reading; the shortfall falls on other taxpayers, other spending or borrowing (C-55, C-56). Indexation adds to the cost from 2029 (C-44).

**Per reading of U1.** If the payment counts for housing support (U1-a), low-paid workers on housing support lose up to 120 kr of it, and those near the threshold now lose 40 öre of each further crown they earn (C-7, C-14). If it does not (U1-b), they keep their support, and those on both income support and housing support gain up to 120 kr (C-8). The Treasury saves under U1-a and pays more under U1-b (C-9). Either way, the lower-income adults still gain on net (C-49).

**Ambiguous effects.** Total purchases of standard-rated goods (C-21), VAT revenue against the static projection (C-58), rents (C-40), the low wage (C-41), hours of recipients in the old taper and of higher-income adults (C-12, C-15), the net position of income-support recipients after 2029 (C-46) and of the middle group (C-52), and the long-run net for lower-income adults and the budget as the payment erodes (C-50, C-57).

**Key conditions.** That the VAT rise reaches shelf prices (A-1, p = 0.75): if it does not, income-support recipients lose nothing, and the burden falls on incomes (A-3). That more means are spent partly on fewer hours and on both kinds of goods (A-6, A-7), the premises the method requires before naming any use.

**What this analysis cannot say.** Whether the policy reduces poverty or raises welfare; how large any effect is; whether total hours worked rise or fall; health and well-being (out of scope for version 1).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | adults.resident | resources_available_other_uses (payment) | increase | short | visible | A | CR-1, CR-8b, SB-1 | none |
| C-2 | treasury | subsidy_outlay (payment) | increase | short | visible | A | SB-1, CR-8b | none |
| C-3 | recipients.full_offset, recipients.taper_exit | resources_available_other_uses (Schedule 2 benefit) | decrease | short | visible | A | CR-1, CR-8b | none |
| C-4 | treasury | subsidy_outlay (Schedule 2 benefits) | decrease | short | visible | A | CR-8b | none |
| C-5 | buyers.current | price_paid (standard-rated goods) | increase | short | visible | B | TX-2, CR-5c | A-1 |
| C-6 | treasury | tax_revenue (VAT) | increase | short | visible | A | TX-1 | none |
| C-7 | households.housing_taper, households.near_threshold | resources_available_other_uses (housing support) | U1-a: decrease; U1-b: no_change | short | invisible | A | CR-1, CR-8b | none |
| C-8 | households.both_taper | resources_available_other_uses (housing support) | U1-a: no_change; U1-b: increase | short | invisible | A | CR-1, CR-8b | none |
| C-9 | treasury | subsidy_outlay (housing support) | U1-a: decrease; U1-b: increase | short | invisible | A | CR-8b | none |
| C-10 | buyers.current, sellers.current | tax_share_borne (VAT rise) | ambiguous | short–medium | invisible | B | DM-1, CR-7b | A-1 |
| C-11 | recipients.full_offset.near | employment (+), hours_worked (+) | at_least_one_increase | short–medium | invisible | B | CR-1, CR-4b, CR-12e, CR-12a | A-5 |
| C-12 | recipients.taper_exit | hours_worked | ambiguous | short–medium | invisible | B | CR-4b, CR-4, CR-12b | A-6 |
| C-13 | adults.lower (in work) | hours_worked | decrease | medium | invisible | B | CR-4b, CR-4, CR-12a, CR-12d | A-1, A-29 |
| C-14 | households.near_threshold (in work) | hours_worked | U1-a: decrease; U1-b: decrease | medium | invisible | B | CR-4b, CR-1, CR-12a, CR-12d | A-1, A-29 |
| C-15 | adults.higher (in work) | hours_worked | ambiguous | medium | invisible | B | CR-4b, CR-4, CR-12b | A-1, A-3, A-6 |
| C-16 | recipients.full_offset | quantity_traded (standard-rated goods) | decrease | short | invisible | B | TX-2, RS-1, CR-4c, CR-12a | A-1, A-7, A-30 |
| C-17 | recipients.full_offset | quantity_substitute (reduced-rate goods) | ambiguous | short | invisible | B | RS-1, CR-4, CR-12b | A-1, A-7 |
| C-18 | adults.lower | quantity_traded (standard-rated goods) | ambiguous | short–medium | invisible | B | TX-2, CR-4c, CR-4, CR-12b | A-1, A-7 |
| C-19 | adults.lower | quantity_substitute (reduced-rate and exempt goods) | increase | short–medium | invisible | B | RS-1, CR-4, CR-12a | A-1, A-7 |
| C-20 | adults.higher | quantity_traded (standard-rated goods) | decrease | short–medium | invisible | B | TX-2, CR-4c, CR-4, CR-12a | A-1, A-3, A-7 |
| C-21 | buyers.current | quantity_traded (standard-rated goods, total) | ambiguous | short–medium | invisible | B | TX-2, CR-4, CR-12b | A-1, A-7 |
| C-22 | buyers.border | cross_border_purchases (in Dornholt) | increase | short | invisible | B | RS-4, TX-4 | A-1, A-8 |
| C-23 | neighboring_jurisdictions (Dornholt shoppers) | cross_border_purchases (in Korsland) | decrease | short | invisible | B | RS-4, TX-4 | A-1, A-8 |
| C-24 | sellers.current | reclassification (into reduced-rate or exempt categories) | increase | short–medium | invisible | B | RS-5, TX-4 | A-10 |
| C-25 | sellers.current, buyers.current | informal_activity (unrecorded sales) | increase | short | invisible | B | RS-3, TX-4, CR-4 | A-11 |
| C-26 | sellers.small_unregistered | number_of_sellers (just below the threshold) | increase | short–medium | invisible | B | RS-17, CR-1, CR-4 | A-12 |
| C-27 | sellers.small_unregistered | reclassification (splitting) | increase | medium | invisible | B | RS-17, RS-5 | A-12 |
| C-28 | buyers.current | quantity_traded (durables, April to December 2027) | increase | short | invisible | B | RS-8, CR-10a | A-13 |
| C-29 | buyers.current | quantity_traded (durables, January to June 2028) | ambiguous | short | invisible | B | RS-8, CR-4, CR-12b | A-13, A-14 |
| C-30 | emigrants.prospective | job_changes (moves abroad) | decrease | medium | invisible | B | RS-11, CR-3 | A-4, A-15 |
| C-31 | immigrants.prospective | job_changes (moves into Korsland) | increase | medium–long | invisible | B | CR-4, CR-10a | A-16 |
| C-32 | claimants | legal_breach (false residence claims) | increase | short | invisible | B | RS-3, CR-4 | A-17 |
| C-33 | lobbying groups | lobbying_effort (questions that exist only under the Act) | increase | short–medium | invisible | B | RS-7, CR-4, CR-12 | A-18 |
| C-34 | sellers.current | lobbying_effort (reduced-rate status) | increase | medium | invisible | B | RS-7, CR-4 | A-18, A-20 |
| C-35 | sellers.border (Kessa) | quantity_traded (goods on border trips) | decrease | short | invisible | B | RS-9, CR-9 | A-8, A-9 |
| C-36 | neighboring_jurisdictions (Varrin sellers) | quantity_traded (sales to Korsland shoppers) | increase | short | invisible | B | RS-9, CR-9 | A-8, A-9 |
| C-37 | owners.border_retail (Kessa) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, SB-4 | A-8, A-22 |
| C-38 | owners.border_retail.varrin | asset_value | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-8, A-22 |
| C-39 | sellers.exempt | price_paid (+), quantity_supplied (−) | at_least_one_as_stated | medium | invisible | B | RS-14, CR-9 | A-1, A-19 |
| C-40 | renters.low_cost | price_paid (market rents) | ambiguous | medium | invisible | B | CR-6, CR-4, RS-14, CR-12b | A-7, A-19, A-21 |
| C-41 | workers.low_wage | wage_rate | ambiguous | medium | invisible | B | CR-6, CR-7a, CR-12b | A-5, A-6 |
| C-42 | sellers.small_unregistered (near the threshold) | asset_value | ambiguous | short | invisible | B | RS-17, CR-7c, CR-12b | A-12, A-22 |
| C-43 | recipients.full_offset, pensioners | resources_available_other_uses (extra indexation) | increase | medium | invisible | B | CR-1, CR-9 | A-1, A-24 |
| C-44 | treasury | subsidy_outlay (extra indexation) | increase | medium | invisible | B | CR-8b | A-1, A-24 |
| C-45 | recipients.full_offset | resources_available_other_uses (total) | decrease | short | invisible | B | CR-12, CR-12f, TX-1, CR-3 | A-1, A-30 |
| C-46 | recipients.full_offset | resources_available_other_uses (total, with indexation) | ambiguous | medium–long | invisible | B | CR-12b, CR-12g | A-1, A-24, A-30 |
| C-47 | recipients.taper_exit.low | resources_available_other_uses (total) | increase | short–medium | invisible | B | CR-12, CR-12e | A-2, A-3 |
| C-48 | recipients.taper_exit.high | resources_available_other_uses (total) | ambiguous | short–medium | invisible | B | CR-12, CR-12b | A-1 |
| C-49 | adults.lower | resources_available_other_uses (total) | U1-a: increase; U1-b: increase | short–medium | invisible | B | CR-12, CR-12e, OC-1 | A-2, A-3 |
| C-50 | adults.lower | resources_available_other_uses (total) | ambiguous | long | invisible | B | CR-12b, CR-12g, TS-3 | A-1, A-3 |
| C-51 | adults.higher | resources_available_other_uses (total) | decrease | short–long | invisible | B | CR-12, CR-12e, TX-1 | A-3 |
| C-52 | adults.middle | resources_available_other_uses (total) | ambiguous | short–medium | invisible | B | CR-12b | A-1, A-3 |
| C-53 | adults.lower | consumption (+), saving (+) (constant prices) | at_least_one_increase | short–medium | invisible | B | CR-4, OC-1, CR-8b | A-2, A-3 |
| C-54 | adults.higher | consumption (−), saving (−) (constant prices) | at_least_one_decrease | short–long | invisible | B | CR-4, OC-1, CR-8b | A-3 |
| C-55 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses | at_least_one_decrease | short–medium | invisible | A | OC-1, OC-3, CR-8, TX-1 | none |
| C-56 | treasury | fund_balance (Consolidated Fund, net of K1 to K4) | U1-a: decrease; U1-b: decrease | short–medium | invisible | A | CR-8, OC-1 | none |
| C-57 | treasury | fund_balance (long run) | ambiguous | long | invisible | B | TS-3, CR-12g | A-1 |
| C-58 | treasury | tax_revenue_vs_static_projection (VAT) | ambiguous | short | invisible | B | TX-9, TX-4, CR-12b | A-1, A-7 |
| C-59 | officials.enforcement (Payments Agency) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-60 | sellers.current | compliance_cost (repricing, systems) | increase | short | invisible | A | TX-5, CR-8c | none |
| C-61 | adults.resident | compliance_cost (registering residence) | increase | short | invisible | A | OC-2, CR-8c | none |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12. The places where the method stops (which goods a rise in means is spent on) are not gaps: CR-4 says a premise is needed there, and A-6 and A-7 supply it.

**(b) Unclear core rules.**
1. *CR-4, "a change in means alone", when two components change means at once.* The rule is stated for a policy that changes means without changing relative costs. Here K1 does that, but K3 changes means and relative prices together, and no class faces K1 alone. The analysis netted the money amounts of the two first (arithmetic, CR-12e), then applied the rule to the net change in means, and CR-4 proper to the relative-price change. The rule does not say whether to net two changes in means before applying it; applying it to each separately would give two unsigned chains on every use and no result. A sentence saying "net the changes in means by arithmetic where the figures allow, then apply the rule to the net" would settle it.
2. *CR-4's exception: "opposite direction".* The exception says a change in means "can shift their ranking among other options in the opposite direction". Whether the means effect opposes the relative-price effect depends on whether means rose or fell and on a premise about the use (A-6, A-7). For `adults.lower` (richer, and taxed goods dearer) the means effect on reduced-rate goods and on hours runs the same way as substitution, so there is no ambiguity (C-13, C-19); for `recipients.full_offset` (poorer) it runs opposite (C-17). The exception's wording implies it always opposes; it should say "can shift their ranking in either direction, depending on whether means rise or fall, and opposes the price effect where it runs the other way".
3. *CR-12's 0.8 note on two items against CR-12f.* The payment and the offset cancel exactly by construction for `recipients.full_offset`. CR-12f says such a consequence "is not reported, and section 7 says so"; the 0.8 note says to record each item and "record the total separately". Here a third item (the VAT) kept the total from cancelling, so the total was reported. Where only the two items exist, the two clauses conflict: (f) says not to report, the 0.8 note says to report the total (which would be `no_change`). The 0.8 note should say that where the items cancel by construction, (f) governs the total.
4. *CR-1 for a payment that is avoided only by leaving.* CR-1 0.7 says operation 4 is "a transfer that no choice avoids". A residence-based payment is avoided only by emigrating. It was recorded as operation 4 for stayers and operation 3 on the option of leaving (RS-11). CR-1 could say that a transfer conditional on a status is operation 3 on the option of changing the status, and operation 4 for those who keep it.

**(c) Missing or wrong patterns.**
1. *TX-9, applied as written, gave a sign I had to override.* Its preconditions hold (TX-4 avoidance shrinks the base), and it concludes `decrease` against the static projection. But the revenue funds a transfer to the same buyers, most of whom gain on net; with A-7 they buy more taxed goods, which enlarges the base. Combined: `ambiguous` (C-58). TX-9's Unless clause covers a tax that raises the price of its own base; it should also cover a tax whose revenue is returned to the payers (directly or through a transfer funded by it).
2. *TX-2's quantity conclusion within a tax-and-transfer.* TX-2 gives `quantity_traded` decrease for the tax component. TX-1 already says the spending of the revenue is analyzed separately, so combining them is ordinary CR-12 work, not a fault. But nothing in TX-2 warns that where the revenue is returned as a transfer, the total quantity is `ambiguous` and only per-class signs survive (C-16 to C-21). A note under TX-2 would help.
3. *RS-22 did not apply, and should not.* The brief anticipated a compensating differential if labor supply changes. RS-22's precondition (a change in a non-wage term of some jobs) is not met: no term of any job changes. The effect of a change in labor supply on wages is CR-6 and CR-7a directly, and here `ambiguous` (C-41). A means-driven reluctance to take unpleasant jobs would need a premise on rankings (A-31, below the cut-off).
4. *RS-17's first conclusion compares below with above.* "`number_of_sellers` just below the threshold increases relative to just above" is a comparison between segments, not against the counterfactual. Re-signed under CR-12 1.0 (C-26). The pattern's own 0.9 clause on value already re-bases; its first clause should be re-based too.
5. *DM-1 for a broad consumption tax.* DM-1 compares buyers' and sellers' alternatives in one market. For a VAT on most consumption, the "sellers" are the owners of all labor and capital, and their alternative (exporting, which is zero-rated) is not the kind DM-1 names. DM-1 gave no sign (C-10), correctly, but for a tax this broad the incidence question is Q3 itself (Rothbard's first law). Which totals survive any split had to be worked out class by class (A-3).
6. *No pattern for a benefit offset that removes a withdrawal rate over a band.* The move in C-11 (a transfer that replaces a benefit one for one, so that the benefit's taper disappears over the band where it would have been less than the transfer) was derived from CR-1 (0.9: operation per range) and CR-4. It is a candidate pattern: "offsetting a flat payment against a tapered benefit".

**(d) Vocabulary.**
1. No variable for migration; `job_changes` was used for moves abroad and moves in (C-30, C-31), though not every move is for a job.
2. No actor class for the state budget as a whole; `treasury` was coined, as `residual_claimant` does not fit a general fund.
3. `consumption` and `saving` are defined in money; the group in C-53 and C-54 had to be stated at constant prices because the tax raises prices. A note in 2.4 that these may be stated at constant prices would help.
4. No variable for a withdrawal rate or the share of extra earnings kept; it is the variable that K2 changes, and it was described in the text only.

**(e) Test of 1.0.**
- *CR-4, "a change in means alone" (and Q19).* Needed interpretation: no class faces a change in means alone once the VAT is counted; the money changes were netted first ((b) 1). Once netted, the rule worked as written: every named use needed a premise (A-6, A-7), and the claims without one were stated as groups including saving (C-53, C-54). On Q19 the case adds one observation: with a tax and a transfer together, more can be said than for a transfer alone, because the tax supplies a relative-price chain whose direction is a priori; but which goods gain from the net change in means still needs a premise.
- *CR-4's exception.* Worked, with interpretation of "opposite" ((b) 2): it made reduced-rate purchases by income-support recipients `ambiguous` (C-17) and hours of `adults.higher` and `recipients.taper_exit` `ambiguous` (C-12, C-15); it did not bite where means and relative price push the same way (C-13, C-19).
- *OC-1 1.0, receipts into the same budget.* Worked as written: VAT and payment as two items, net by arithmetic (C-56), shortfall under both readings.
- *OC-1, who pays (0.8) and saving is a use (0.7).* Worked as written (C-55 as a group; C-53, C-54 include saving).
- *TX-1.* Worked as written (C-6, the payers in C-45 to C-52).
- *TX-2 and DM-1, VAT incidence.* TX-2 needed a premise (A-1) to sign `price_paid` (C-5); DM-1 gave no split (C-10). For totals, signs were found that hold under any split (A-3), which TX-2 and DM-1 do not prompt for ((c) 5). The incidence premise decides whether income-support recipients lose at all (C-45).
- *CR-12 0.8, two items in one variable.* Needed interpretation: payment up and benefit down cancel by construction, which brings in CR-12f; the total was reported only because a third item (VAT) remained ((b) 3).
- *CR-12 1.0, the baseline of patterns.* Worked as written: RS-17's first clause re-signed (C-26); TX-9 and DM-1 compare by definition; no other pattern compared with another policy.
- *CR-12 1.0, tiers and dominance.* Worked as written: arithmetic settled C-11, C-47, C-49, C-51 and C-56 without changing their tiers (Tier B where an assumption is used, Tier A for C-55 and C-56).
- *CR-12 1.0, what the response argument needs.* Not exercised: no response argument was used.
- *CR-1 0.9, operation per range.* Worked as written for the offset (C-11): no operation below about 792 kr of earnings, operation 3 above it.
- *CR-1 1.0 and RS-17 1.0, notches.* Worked as written for the VAT registration threshold (C-26, C-27; C-42 under RS-17's 0.9 value clause).
- *RS-11.* Worked as written: the payment is a non-transferable benefit lost by moving (C-30). The mirror (arrivals, C-31) was derived from CR-4.
- *RS-22.* Not applicable; its precondition was not met ((c) 3). This is a result: a change in labor supply does not by itself trigger RS-22.
- *RS-8 0.9, more timing chains.* Worked as written: the payment starting on the same date as the VAT gives an opposing chain in the window after it (C-29).
- *TS-3.* Worked as written: a payment fixed in money against a tax that keeps its share makes long-run totals `ambiguous` (C-50, C-57).
- *TX-9.* Failed as written here: its conclusion was wrong although its preconditions held ((c) 1).
- *Candidates from 06_gaps.md, 6.2e.* "A claim payable inside a boundary draws items from outside" (WE-027) resembles C-31: a payment to residents draws people across the border to qualify. The derivation is the same (CR-4, CR-7a across the boundary), and it is signed against no payment, so the use is valid against the counterfactual. But the candidate speaks of items (containers), and here people move home and wait 24 months; whether that is the same move is for the re-run to judge. Not claimed as a second use. New candidate: "offsetting a flat payment against a tapered benefit" ((c) 6).
