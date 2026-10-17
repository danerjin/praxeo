# WE-060 / Analysis: A basic payment to every adult, funded by a higher VAT, with means-tested benefits offset

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Korsland Basic Payment and Value Added Tax Act 2027.** Korsland has 6.0 million people, about 4.8 million of them adults habitually resident; the currency is the crown (kr). The border town of Kessa (about 40,000 people) is 8 km from Varrin in Dornholt, which has a retail park; Dornholt's standard VAT rate is 21%.

Existing rules that stay in the counterfactual: Schedule 2 benefits ("income support": 750 kr a month for a single adult with no other income, withdrawn at 65 öre per crown of earnings above 100 kr, nil at about 1,254 kr; about 520,000 recipients, of whom about 400,000 receive 300 kr or more and about 120,000 less than 300 kr, about 95,000 of them less than 240 kr); housing support (up to 70% of rent, at most 550 kr, full where "counted income", which is "income from all sources, including any benefit", is 900 kr or less, withdrawn at 40 öre per crown above that; about 380,000 recipients, 210,000 of them also on income support, of whom about 30,000 receiving 300 kr or more of income support are in the taper; 170,000 not on income support, about 120,000 of them in the taper); April price indexation of Schedule 2 benefits and the state pension (average 1,400 kr, about 1.1 million pensioners) by the September CPI; VAT at 20% standard, 6% reduced (food, books, public transport), exempt (rent, financial services, health, education), registration threshold 80,000 kr. The standard-rated base that bears unrecoverable VAT is about 360 billion kr a year net of tax (households 245 billion, about 4,250 kr a month per adult; government 35 billion; inputs of exempt businesses 80 billion). Net national income is about 420 billion kr. Standard-rated goods weigh about 55% in the CPI.

**Figures.** The payment costs 17.28 billion kr a year. The offset saves about 1.66 billion. Four VAT points on the base is 14.4 billion static; the Treasury projects 13.6 billion with responses, of which about 1.3 billion is paid by the government itself. The Payments Agency costs about 140 million a year and 90 million to set up. Tax per crown of net price rises by 4 öre (tax-inclusive price at most about 3.3% higher), so the payment covers the price rise for anyone buying less than 7,500 kr a month of standard-rated goods. If the tax is borne by sellers' net prices instead, 14.4 billion is about 3.4% of net national income. Housing support: U1-a saves about 0.18 billion a year; U1-b costs about 0.04 billion more. The Consolidated Fund is short by about 1.2 billion (U1-a) or 1.4 billion (U1-b) a year on static VAT, and about 3.3 or 3.5 billion on the Treasury's projection net of the government's own VAT.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Korsland. Just outside: Dornholt (standard VAT 21%); Varrin, 8 km from Kessa. | §1. |
| Announced / enacted / effective / expires | Announced 15 January 2027; enacted 1 April 2027; effective 1 January 2028; no expiry. | §1, §20. |
| Enforcement (who, penalties, resources) | The Payments Agency (new) pays and checks residence against the population register; false claims: repayment plus up to 5,000 kr. The Tax Office collects VAT as now. | §6, §14. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Basic payment | `lump_sum_subsidy` | Adults habitually resident | The Payments Agency pays; every adult resident for 24 of the last 36 months is entitled | 300 kr a month, not taxable, not indexed; funded from the Consolidated Fund (§11). | Adults resident for less than 24 of the last 36 months. |
| K2 Offset | Benefit reduction | Schedule 2 benefits | Recipients | Each Schedule 2 benefit reduced by the payment, not below nil (§5(1)); a nil-rate entitlement keeps passported help (§5(3)). | — |
| K3 VAT rise | `ad_valorem_tax` | Standard-rated supplies | VAT-registered sellers | 20% to 24%. Reduced rate and exemptions unchanged. Added revenue "applied to the cost of the payment" (§12); no provision for any shortfall. | Reduced-rate and exempt supplies; sellers under the 80,000 kr threshold. |
| K4 Payments Agency | Administration | K1 | The Agency, general budget | About 140 million a year; 90 million set-up in 2027. | — |

Unclear provisions:
- **U1, the payment in the housing means test.** U1-a: the payment is "income from all sources" and is counted; §9 keeps it out only of rules that refer to benefits as such. U1-b: §9 keeps it out of every means test; it is not counted. Readings get no probability; signs that depend on U1 are given per reading.

Counterfactual law: the same Schedule 2, housing support, indexation and VAT rules, with no payment, no offset and a 20% standard rate.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Basic payment | binary (state gives) | Yes, paid to every eligible adult (A-4) | 4 (means transferred to every eligible adult, no choice avoids it except residence); 3 (a payment attached to the option of staying or becoming resident for 24 months, CR-1 0.7) | CR-3b, CR-4 (change in means alone), CR-8b, CR-9, CR-10a |
| K2 Offset | binary (state takes back part of K1 from recipients) | Yes, mechanical | 4 (for recipients of 300 kr or more, a transfer equal and opposite to K1; for recipients below 300 kr, a transfer of their whole benefit); 3 (changes what earning above about 792 kr brings: the 65% withdrawal no longer applies between about 792 and 1,254 kr) | CR-1 1.0 (ranges), CR-3, CR-4, CR-8b |
| K3 VAT rise | binary | Yes, on every standard-rated sale by a registered seller (A-1) | 3 (a charge attached to each standard-rated purchase and sale); 4 for no one (a charge avoided by not buying, CR-1 0.7) | CR-4, CR-4c, CR-5c, CR-6, CR-7b, CR-7c, CR-9, CR-10a |
| K4 Payments Agency | binary (means used up) | Yes | 4 (means to the Agency from the general budget); 3 (penalty risk attached to false claims) | CR-8c, CR-4 (x: claim truly, y: claim falsely) |

Interactions between components: K2 recovers part of K1 from recipients; K3 is earmarked to K1 but does not cover it (CR-8d: the earmark frees nothing, since the shortfall must be met from other money); K3 raises the CPI, which raises Schedule 2 benefits and pensions through the existing indexation rule (A-24); K1 interacts with housing support through U1.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| adults.eligible | All adults resident 24 of 36 months | Op 4: +300 kr a month (K1). |
| income_support.300_or_more (about 400,000) | Recipients receiving at least 300 kr | Op 4: +300 (K1), −300 (K2): net nil; op 3: VAT on standard-rated purchases (A-30). Earnings above about 792 kr no longer lose 65 öre per crown. |
| income_support.300_or_more.housing_taper (about 30,000) | As above, and in the housing taper | U1-a: counted income unchanged (benefit −300, payment +300 counted); U1-b: counted income −300, housing support +120. |
| income_support.below_300 (about 120,000; 95,000 below 240 kr) | Recipients receiving less than 300 kr | Op 4: lose the whole benefit, gain 300; the 65% withdrawal ends for them. Under U1-a, counted income rises by 300 minus the benefit. |
| adults.no_income_support | Adults not on Schedule 2 benefits, including pensioners | Op 4: +300; op 3: VAT on standard-rated purchases. Split by purchases below or above 7,500 kr a month. |
| housing_support.taper_no_income_support (about 120,000) | Not on income support, in the housing taper | U1-a: counted income +300, housing support −120; U1-b: no change. |
| adults.resident_under_24_months | New residents | Op 3 (VAT); no payment until 24 months; op 3 on staying (the payment later). |
| pensioners (about 1.1 million) | Receive the payment and an indexed pension | Op 4: +300; VAT; pension uplift from April 2029 (A-24). |
| buyers.standard_rated_goods | Households, government, exempt businesses | Op 3: VAT 4 points higher. |
| sellers.standard_rated | VAT-registered sellers | Op 3: tax on each sale; options to reclassify, evade, stay under threshold. |
| businesses.near_registration_threshold | Turnover near 80,000 kr | Registering now costs 24% rather than 20% on all sales (a notch, CR-1 1.0). |
| exempt_sellers (banks, insurers, private landlords) | Buy standard-rated inputs they cannot reclaim | Op 3: input costs up 4 öre per crown (A-19). |
| buyers.financial_services | Customers of banks and insurers | Through CR-9 (input_to). |
| tenants.low_cost_rentals, landlords.private | Low-cost rental market | Through CR-9: tenants' means change; landlords' input costs rise. |
| factor_owners | Workers and owners of capital | Bear any part of the VAT not passed into prices (A-3). |
| income_support.earning_400_to_792, income_support.earning_792_to_1254 | Recipients who can change hours | Op 3 on earning above about 792 kr. |
| kessa_residents, sellers.kessa_retailers, sellers.kessa_grocers, owners.kessa_retail_property | Border town | Through CR-9 (across_border, trip complement). |
| neighboring_jurisdictions.varrin_retailers, neighboring_jurisdictions.varrin_grocers, owners.varrin_retail_park | Just across the border | Through CR-9 (across_border). |
| buyers.foreign (Dornholt) | Currency link | Through CR-9 (currency). |
| residents.would_emigrate, dornholt_workers | Potential movers | Op 3: payment attached to residence (A-15, A-16). |
| claimants.false | False residence claimants | Op 3: payment attached to a false claim, with penalty risk (A-17). |
| officials.payments_agency, officials.tax_office, officials.benefits, officials.housing_support | Administration | Op 4: budget outlays; tasks. |
| consolidated_fund; taxpayers or recipients of other spending or future taxpayers | Pay the shortfall | CR-8b, CR-8 0.7. |
| recipients_groups, pensioners_associations, retailers' associations | Lobbies | CR-4 (x: accept, y: lobby). |
| buyers.durables | Households planning car or furniture purchases | CR-10a: rate rise dated 1 January 2028. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | adults.eligible | subsidy_outlay (basic payment) | increase | short; medium; long | CR-1 op 4, CR-8b | A-4 |
| C-2 | buyers.standard_rated_goods | price_paid (standard-rated goods, tax-inclusive) | increase | short; medium | CR-1 op 3, CR-5c, CR-7b | A-1, A-2 |
| C-3 | officials.tax_office | tax_revenue (VAT) | increase | short; medium; long | CR-1 op 3, CR-8b | A-N3 |
| C-4 | officials.benefits | subsidy_outlay (Schedule 2 benefits) | decrease | short; medium; long | CR-1 op 4 (K2), arithmetic | none |
| C-16 | consolidated_fund | fund_balance | decrease | short; medium; long | CR-8b, CR-8 0.8 (capped budgets), arithmetic | none |

## 5. Responses

CR-4 for every pair of options each class has; CR-10a for timing; CR-6 where a quantity is fixed.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-25 | sellers.standard_rated | net_price_received | decrease | short; medium | CR-5c, CR-7b | A-1, A-2 |
| C-27 | households.net_gainers | quantity_demanded (standard-rated goods) | ambiguous | short; medium | CR-4c, CR-4 (change in means), CR-12b | A-1, A-7, A-N1 |
| C-28 | income_support.300_or_more | quantity_demanded (standard-rated goods) | decrease | short | CR-4c, CR-4 (change in means) | A-1, A-7, A-30 |
| C-29 | households.net_gainers | quantity_demanded (reduced-rate goods) | increase | short; medium | CR-4 (change in means), CR-4 (x: standard-rated, y: reduced-rate) | A-7, A-N1 |
| C-30 | income_support.300_or_more | quantity_demanded (reduced-rate goods) | ambiguous | short; medium | CR-12b | A-7, A-N5 |
| C-31 | kessa_residents | cross_border_purchases (standard-rated goods in Varrin) | increase | short; medium; long | CR-4 (x: buy in Kessa, y: buy in Varrin) | A-8 |
| C-40 | sellers.standard_rated | reclassification (supplies reshaped into reduced-rate or exempt categories) | increase | short; medium | CR-4 (x: covered form, y: uncovered form) | A-10 |
| C-41 | sellers.standard_rated | lobbying_effort (for reduced-rate or exempt status) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-18, A-20 |
| C-42 | sellers.standard_rated | informal_activity (unrecorded sales) | increase | short; medium | CR-4 (x: comply, y: violate) | A-11 |
| C-43 | businesses.near_registration_threshold | quantity_supplied (−), reclassification (business splitting) (+) | at_least_one_as_stated | short; medium | CR-1 1.0 (notch), CR-4 | A-12 |
| C-46 | sellers.standard_rated | compliance_cost (repricing, systems) | increase | short | CR-1 op 3, CR-8c | none |
| C-47 | buyers.durables | quantity_traded (durables, 15 January to 31 December 2027) | increase | short (announcement window) | CR-10a, CR-4 (x: buy after 1 January 2028, y: buy before) | A-13 |
| C-48 | buyers.durables | quantity_traded (durables, first months of 2028) | ambiguous | short | CR-10a, CR-12b | A-13, A-14 |
| C-49 | income_support.earning_400_to_792 | hours_worked | increase | short; medium | CR-4 (x: earn below 792, y: earn above), CR-12e (arithmetic) | A-5 |
| C-50 | income_support.earning_792_to_1254 | hours_worked | ambiguous | short; medium | CR-4 and its exception, CR-12b | A-6, A-29 |
| C-51 | adults.net_gainers.choosing_hours | hours_worked | decrease | short; medium | CR-4 (change in means), CR-4 (x: work, y: not work) | A-6, A-29, A-N1 |
| C-52 | residents.would_emigrate | job_changes (moves to Dornholt) | decrease | medium; long | CR-4 (x: move, y: stay) | A-15 |
| C-53 | dornholt_workers | job_changes (moves to Korsland) | increase | medium; long | CR-4 (x: stay in Dornholt, y: move), CR-10a | A-16 |
| C-54 | claimants.false | legal_breach (false residence claims) | increase | short; medium | CR-4 (x: no claim, y: false claim) | A-17 |
| C-55 | recipients_groups, pensioners_associations | lobbying_effort (to index or raise the payment) | increase | medium; long | CR-4 (x: accept, y: lobby), CR-12 0.9 (activity only under the policy), CR-8c | A-18 |

## 6. Second-order effects

Depth limit 4; diffuse effects on the customers of every business that pays VAT on inputs are pruned at depth 3, except for the exempt sellers named in the case. Relation named per row.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-19 | tenants.low_cost_rentals | price_paid (rent) | increase | short; medium | CR-4 (change in means), CR-6, CR-9 | low-cost housing among uses of added means; standard-rated inputs input_to letting (medium) | A-N1, A-N4, A-21 |
| C-20 | landlords.private | asset_value (rental property) | ambiguous | short; medium | CR-7c, CR-10c, CR-12b | as above | A-19, A-21, A-22, A-N4 |
| C-18 | officials.housing_support | subsidy_outlay (housing support) | U1-a: ambiguous; U1-b: increase | short; medium | CR-1, arithmetic, CR-9, CR-12b | rent input to the housing support formula (70% of rent) | A-21, A-N1, A-N4 |
| C-22 | buyers.financial_services | price_paid (financial services) | increase | short; medium | CR-9, CR-7b, LW-10 | standard-rated inputs input_to financial services | A-19 |
| C-23 | exempt_sellers.financial | return_on_capital | decrease | short | CR-7b | as above | A-19 |
| C-26 | factor_owners | earnings (factor incomes) | decrease | short; medium | CR-7b, CR-9, LW-10 | factors input_to standard-rated goods | A-1, A-3 |
| C-32 | neighboring_jurisdictions.varrin_retailers | quantity_traded (standard-rated goods) | increase | short; medium; long | CR-9, CR-5 | across_border (close at 8 km) | A-8 |
| C-33 | neighboring_jurisdictions.varrin_grocers | quantity_traded (groceries) | increase | short; medium; long | CR-9 | complement (trip) | A-8, A-9 |
| C-34 | sellers.kessa_retailers | quantity_traded (sales to Dornholt shoppers) | decrease | short; medium; long | CR-9, CR-4 | across_border | A-8 |
| C-35 | sellers.kessa_retailers | quantity_traded (all standard-rated sales) | ambiguous | short; medium | CR-9, CR-12b | across_border; Kessa residents' means | A-7, A-8, A-N1 |
| C-36 | sellers.kessa_grocers | quantity_traded (groceries) | ambiguous | short; medium | CR-9, CR-12b | complement (trip); Kessa residents' means | A-7, A-8, A-9, A-N1 |
| C-37 | owners.varrin_retail_park | asset_value | increase | short (from 2027); medium | CR-7c, CR-10c | across_border | A-8, A-22 |
| C-38 | owners.kessa_retail_property | asset_value | ambiguous | short; medium | CR-7c, CR-10c, CR-12b | across_border | A-7, A-8, A-22, A-N1 |
| C-39 | buyers.foreign | exchange_rate (+), quantity_traded (Korsland exports and assets bought from Dornholt) (+) | at_least_one_increase | medium | CR-9 0.7 (currency), CR-6 | currency | A-8 |
| C-44 | officials.tax_office | tax_revenue_vs_static_projection | decrease | short; medium | CR-4, CR-4c, CR-12e | - | A-N3 |
| C-45 | officials.tax_office | enforcement_cost | increase | short; medium | CR-8c, CR-4 | - | A-10, A-11 |
| C-13 | pensioners | subsidy_outlay (state pension, indexation uplift) | increase | medium; long (from April 2029) | CR-9, existing rule applied (A-24) | VAT input to the CPI, CPI input to indexation | A-1, A-24 |

## 7. Combined effects

Distributional consequences (resources available for other uses) and the budget are combined here; each row lists every chain found anywhere in the analysis.

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| income_support.300_or_more, resources_available_other_uses, short | none (K1 and K2 cancel by construction, CR-12f) | VAT on purchases kept (A-30, A-1); higher rent for renters not in the taper (C-19, 70% covered by housing support up to the cap) | not needed | decrease (C-5) |
| income_support.300_or_more.housing_taper, same, short | U1-b: housing support +120 kr | VAT (A-30); rent (C-19) | none | U1-a: decrease; U1-b: ambiguous (C-6) |
| income_support.300_or_more, same, medium (from April 2029) | indexation uplift on the benefit (A-24), about 1.8% of 750 kr; U1-b housing gain for the taper | VAT; rent | none (both small, of similar size) | ambiguous (C-7) |
| income_support.below_240, same, short; medium | net receipt of 300 kr less a benefit below 240 kr (at least 60 kr) | VAT; rent; U1-a: housing support falls by 40% of the net receipt for those in the taper | A-N1 (empirical) | increase (C-8) |
| income_support.240_to_300, same | net receipt below 60 kr | VAT; rent | none | ambiguous (C-9) |
| adults.no_income_support.purchases_below_7500, same, short; medium | +300 kr | VAT through prices (at most 0.04 S, below 300 by arithmetic); VAT through exempt sellers' costs and through factor incomes (A-3); U1-a: housing support −120 kr for the 120,000 in the taper; rent | A-N1 (empirical; the price chain alone is settled by arithmetic); the rent chain is covered by the response argument for the class as a whole (CR-12e 0.8: tenants bidding up a fixed stock with part of their added means cannot, as a class, pay more in added rent than the added means they choose to spend on housing) | increase (C-10) |
| adults.purchases_7500_or_more, same | +300 kr | VAT 0.04 S ≥ 300; factor incomes (A-3) | none | ambiguous (C-11) |
| adults.resident_under_24_months, same | none | VAT; rent | not needed | decrease (C-12) |
| sellers.standard_rated, net_price_received | none (aggregate demand change from the redistribution among households is a kind 3 chain, CR-12 0.8) | part of the tax not passed on (A-1) | A-2 (tax-inclusive prices rise by no more than the tax) covers the kind 3 chain in both directions: the net price cannot rise | decrease (C-25) |
| households.net_gainers, quantity_demanded (standard-rated goods) | added means (A-7) | higher price (CR-4c) | none | ambiguous (C-27) |
| income_support.300_or_more, quantity_demanded (reduced-rate goods) | substitution from standard-rated goods (A-N5) | lower means (A-7) | none | ambiguous (C-30) |
| sellers.kessa_retailers, quantity_traded (all sales) | Kessa residents' added means (A-N1, A-7) | cross-border shopping (A-8); fewer Dornholt shoppers | none | ambiguous (C-35) |
| officials.housing_support, subsidy_outlay | U1-b: counted income falls for the taper (+0.04 bn); both readings: higher rents raise the 70% share (C-19) | U1-a: counted income rises (−0.18 bn) | none | U1-a: ambiguous; U1-b: increase (C-18) |
| officials.benefits, subsidy_outlay (Schedule 2), medium | indexation uplift (A-24), about 1.8% of the remaining outlay | offset saving 1.66 bn | arithmetic (CR-12e): the uplift is a small fraction of the saving | decrease (C-4) |
| officials.tax_office, tax_revenue | 4 points on the base | base responses (C-31, C-40, C-42, C-43, C-27/C-28) | A-N3 (Treasury projection: responses remove about 0.8 bn of 14.4 bn) | increase (C-3) |
| officials.tax_office, tax_revenue_vs_static_projection | spending of net gainers' added means on standard-rated goods (kind 3 at aggregate) | cross-border, reclassification, evasion, threshold, price response | A-N3 | decrease (C-44) |
| consolidated_fund, fund_balance | VAT 13.6 to 14.4 bn; offset 1.66 bn; U1-a housing saving | payment 17.28 bn; Agency 0.14 bn; indexation uplift on pensions and benefits (from 2029); U1-b housing cost; government's own VAT is a receipt and an outlay of the same budget (CR-8 1.0) | arithmetic: short by 1.2 to 3.5 bn under both readings | decrease (C-16) |
| income_support.earning_400_to_792, hours_worked | return on earning above 792 kr rises from 35 to 100 öre per crown (A-5) | VAT lowers the goods value of a crown by at most 3.3% | arithmetic (CR-12e) | increase (C-49) |
| income_support.earning_792_to_1254, hours_worked | marginal withdrawal ends (substitution) | added means (A-6) | none | ambiguous (C-50) |
| adults.net_gainers.choosing_hours, hours_worked | VAT lowers net means (A-6), CR-4 exception | added net means (A-6, A-N1); VAT lowers the goods value of earnings (CR-4) | A-N1 (the net means change is a rise, so the means chains combine to one) | decrease (C-51) |
| buyers.durables, quantity_traded, first months of 2028 | net gainers buying durables with the payment (A-14) | purchases moved into 2027 (A-13) | none | ambiguous (C-48) |
| landlords.private, asset_value | rent rises (C-19) | input VAT (A-19) | none | ambiguous (C-20) |

Cancellation by construction (CR-12f): for recipients of 300 kr or more, K1 and K2 cancel exactly, and passported help is preserved by §5(3); no consequence is reported for that pair. Different variables (hours, prices, resources) are not netted (CR-12c).

## 8. Time structure

- **Announcement (15 January 2027) to effect (1 January 2028).** The rate rise is dated and was expected for almost a year. Purchases of durables are moved into 2027 (CR-10a; C-47), and early-2028 purchases are lower on that chain but higher on the chain of net gainers spending the first payments on durables (A-14), so C-48 is ambiguous. Property values move when the change becomes expected (CR-7c, CR-10c): the Varrin retail park from January 2027, part of the way until enactment (C-37), as buyers expect the rate and the payment to last (A-22).
- **Indexation (April 2029).** The VAT rise enters the September 2028 CPI, so Schedule 2 benefits and pensions rise in April 2029 (A-24). This is a second, later chain for recipients (C-7) and for the fund (C-16, C-13). It is a one-time level shift that persists.
- **The payment is not indexed.** Its real value falls each year relative to indexed benefits and pensions, while the VAT revenue grows with nominal spending. The Consolidated Fund's shortfall therefore narrows over time in real terms (arithmetic); its sign is unchanged in the long run on the case's figures. Recipients of 300 kr or more who keep a positive benefit are unaffected by erosion while the offset equals the payment.
- **Housing.** The low-cost rental stock cannot grow within a year (A-21), so the added demand raises rents first (C-19); in later years supply may expand, and the rent effect may narrow. No long-run sign is given.
- **Migration.** The 24-month wait delays both the gain to movers (C-53) and the payment outlay on them; emigrants who stay (C-52) act from 2027 on the expectation (CR-10a).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-15 | officials.payments_agency | enforcement_cost | increase | About 140 million a year and 90 million set-up that would have served other public or private uses | CR-1 op 4, CR-8c |
| C-17 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses | at_least_one_decrease | The 1.2 to 3.5 billion kr a year shortfall, met by taxes, cuts or borrowing | CR-8b, CR-8 0.7 |
| C-45 | officials.tax_office | enforcement_cost | increase | Audit and dispute work over reclassification and evasion | CR-8c |
| C-46 | sellers.standard_rated | compliance_cost (repricing, systems) | increase | Staff time and systems changes | CR-8c |
| C-41 | sellers.standard_rated | lobbying_effort (for reduced-rate or exempt status) | increase | Means spent seeking reduced-rate status | CR-8c |
| C-55 | recipients_groups, pensioners_associations | lobbying_effort (to index or raise the payment) | increase | Members' time and dues | CR-8c |
| C-5 | income_support.300_or_more | resources_available_other_uses | decrease | 12 to 24 kr a month of other purchases (0.04 × 300 to 600 kr) | CR-3c, CR-8a |
| C-12 | adults.resident_under_24_months | resources_available_other_uses | decrease | Other purchases, while no payment is received | CR-3c, CR-8a |

CR-8b symmetry: the payment (C-1) is matched by the offset (C-4), VAT paid (C-2, C-26) and the shortfall payers (C-17); the VAT revenue (C-3) is matched by buyers' and factor owners' payments; the government's own VAT (about 1.3 bn) is a receipt and an outlay of the same budget (CR-8 1.0) and adds nothing to the fund's balance.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Most of the VAT rise passes into standard-rated shelf prices within a year. | other | 0.75 | Past VAT changes in Korsland and Dornholt; retailers' statements. | C-2, C-5, C-6, C-12, C-13, C-25, C-26, C-27, C-28 lose this chain. |
| A-2 | Tax-inclusive prices rise by no more than the tax (4 öre per crown of net price). | other | 0.85 | Past VAT changes; competition in retail. | C-2, C-25 lose their bound. |
| A-3 | Whatever part of the VAT is not passed into prices falls on factor incomes roughly in proportion to them (about 3.4%). | other | 0.6 | Standard incidence of a broad consumption tax. | C-26 fails. |
| A-4 | The payment is paid and residence is checked against the population register. | enforcement | 0.9 | The Agency's budget; register quality. | C-1, C-8, C-10 fail. |
| A-5 | Some recipients earning 400 to 792 kr can find work or extra hours that take them above 792 kr. | substitutability | 0.7 | Part-time job openings; current earnings spread. | C-49 fails. |
| A-6 | Fewer hours of work is among the uses on which adults spend part of a rise in means, and which they give up first when means fall. | other | 0.65 | Hours after earlier benefit changes. | C-50 loses its opposing chain; C-51 fails. |
| A-7 | Both standard-rated and reduced-rate goods are among the uses on which these classes' spending rises when their means rise, and falls when they fall. | other | 0.7 | Household budget surveys. | C-27 to C-30, C-35, C-36, C-38 change. |
| A-8 | Some Kessa shoppers buy in Varrin when standard-rated goods there are about 2.5% cheaper; some Dornholt shoppers stop coming to Kessa. | mobility | 0.8 | 8 km; Varrin retail park; trip surveys. | C-31 to C-39 fail. |
| A-9 | Shoppers who go to Varrin buy groceries on the same trip. | other | 0.7 | Trip surveys; Varrin supermarket. | C-33, C-36 fail. |
| A-10 | Some sellers can reshape supplies into reduced-rate or exempt categories at a cost below the four points. | other | 0.6 | Disputes over catering and bundles. | C-40, C-45 lose this chain. |
| A-11 | VAT enforcement is imperfect; some sales go unrecorded. | enforcement | 0.75 | Tax Office gap estimates. | C-42 fails. |
| A-12 | Some businesses near 80,000 kr of turnover can stay below the threshold or split. | other | 0.7 | Bunching below the threshold now. | C-43 fails. |
| A-13 | Some purchases of durables can be moved before 1 January 2028. | other | 0.8 | Car and furniture sales before earlier rate rises. | C-47 fails; C-48 becomes increase. |
| A-14 | Some net gainers spend part of the payment on durables in its first months. | other | 0.55 | Spending after earlier rebates. | C-48 becomes decrease. |
| A-15 | Some residents who would have moved abroad value 3,600 kr a year enough to stay. | mobility | 0.6 | Emigration to Dornholt; wage gaps. | C-52 fails. |
| A-16 | Some Dornholt workers move to Korsland, waiting 24 months for the payment. | mobility | 0.5 | Cross-border commuting; housing costs. | C-53 fails. |
| A-17 | Some false residence claims are made. | enforcement | 0.6 | Residence-based benefits elsewhere. | C-54 fails. |
| A-18 | Recipients' groups, pensioners' associations and retailers can organize at a cost below their stakes. | other | 0.85 | Existing associations; hearings. | C-41, C-55 fail. |
| A-19 | Exempt sellers cannot replace standard-rated inputs at the old cost. | substitutability | 0.8 | Input structure of banks and landlords. | C-20, C-22, C-23 fail or change. |
| A-20 | The higher stake in reduced-rate status raises the effort spent seeking it. | other | 0.8 | Past budget reviews. | C-41 fails. |
| A-21 | The low-cost rental stock cannot grow within a year. | durability | 0.8 | Construction times. | C-18, C-19, C-20 fail in the short run. |
| A-22 | Buyers of property expect the VAT rate and the payment to last. | expectations | 0.75 | No expiry; cross-party support. | C-20, C-37, C-38 are smaller and slower. |
| A-24 | The indexation rule is applied as now, so the VAT rise raises benefits and pensions from April 2029. | other | 0.85 | Applied every year for twenty years. | C-7 becomes decrease; C-13 fails. |
| A-26 | The supply of reduced-rate goods (mostly food) cannot expand at an unchanged cost within the period. | durability | 0.35 | Food is widely traded and imported. | Not reported (below 0.5). |
| A-29 | Some adults in work can choose their hours. | other | 0.75 | Labor force survey. | C-50, C-51 fail. |
| A-30 | Benefit recipients keep buying some standard-rated goods (clothing, household goods, energy). | other | 0.95 | Household budget survey. | C-5, C-6, C-28 fail. |
| A-31 | Workers with more means accept jobs with unpleasant conditions less readily, so the wage in such jobs rises. | other | 0.4 | No direct evidence. | Not reported (below 0.5). |
| A-N1 | For adults not on income support whose standard-rated purchases are below 7,500 kr a month, and for income-support recipients receiving less than 240 kr, the added VAT they bear through prices, through exempt sellers' costs (rent, financial services) and through factor incomes, together with any loss of housing support under U1-a, is less than their net receipt from K1 and K2. | other | 0.65 | NEW. The static VAT is about 250 kr a month per adult on average (14.4 bn / 4.8 m / 12) against 300 kr; the price chain alone is below 300 kr by arithmetic for purchases below 7,500 kr; low earners' purchases are small; U1-a costs at most 40% of the net receipt. Flagged: needed for C-8, C-10, C-29, C-51 and the means chains of C-19, C-35, C-36, C-38. | C-8, C-10 become ambiguous; C-29, C-51 fail. |
| A-N3 | The Treasury's projection is right in direction: VAT revenue rises, by less than the static 14.4 billion. | other | 0.7 | NEW. Treasury projection of 13.6 billion with responses; a fall would need responses to remove a sixth of the base. Flagged: needed for C-3 and C-44. | C-3 or C-44 fail. |
| A-N4 | Renting more or better low-cost housing is among the uses on which low-income adults spend part of a rise in means. | other | 0.6 | NEW. Crowding and household formation among low-income adults; housing is a large budget share. Flagged: needed for C-18 to C-20. | C-19 fails; C-18 under U1-a becomes decrease; C-20 becomes decrease. |
| A-N5 | Some buyers substitute reduced-rate goods for standard-rated ones when the latter rise by about 3.3% (groceries for prepared food and catering). | substitutability | 0.6 | NEW. Catering disputes; grocery against restaurant spending after earlier rate changes. Flagged: the opposing chain in C-30 and a second chain in C-29. | C-30 becomes decrease. |
| A-N6 | Financial services are among the uses on which households' spending moves with their means, enough to move their price. | other | 0.4 | NEW. No evidence in the case. | Not reported (below 0.5); C-22 keeps its sign. |

**Not reported** (an assumption below 0.5):
- Food prices rise as net gainers buy more reduced-rate goods (CR-6, CR-9): needs A-26 (p 0.35). The CR-6 0.9 note requires a premise on whether supply can expand to split the shift; without it, the price is not signed.
- Wages in jobs with unpleasant conditions rise (CR-7a, CR-4 with the change in means): needs A-31 (p 0.4).
- A demand chain on financial services opposing the cost chain in C-22: needs A-N6 (p 0.4); under CR-12 0.8 (kind 2 below 0.5) C-22 keeps its derived sign and the chain is recorded here.

### Final check before the report

1. Uncombined chains: every resources, hours, quantity and budget key was listed in section 7 with chains from all sections, including indexation (section 8) and U1 (sections 1 and 6). C-7, C-18, C-48 were changed to ambiguous or per-reading signs on this check.
2. Group signs: C-17 (payers of the shortfall), C-39 (currency link) and C-43 (threshold) are group signs.
3. Baseline: every sign is against Korsland in 2028 onward with a 20% rate and no payment; C-4 is against Schedule 2 outlay without the offset, not against 2027.
4. Worse off is not poorer: resources are signed only where the class keeps paying (A-30) or receives an unavoidable sum (K1, K2).
5. Timing: durables are signed per window (C-47, C-48).
6. Both sides: K1 against K2, K3 and C-17; VAT against buyers and factor owners; housing support outlay against tenants and landlords.
7. Every class, every rule: CR-7c applied to rental property, Kessa and Varrin retail property; CR-6 to rentals and food (food not reported); CR-9 along across_border, trip, input_to, currency; CR-4 (x: comply, y: violate) to VAT sellers and claimants.
8. Unstated premises: A-N1 to A-N6 added and flagged.
9. No pattern is cited.

## 11. Report

**The policy:** From 1 January 2028 every adult resident in Korsland for 24 of the last 36 months receives 300 kr a month, tax-free and not indexed. Schedule 2 benefits are cut by the same amount, but not below nil. The standard VAT rate rises from 20% to 24%, and the revenue is earmarked for the payment, but it does not cover it. It is unclear whether the payment counts as income for housing support (U1).

**Visible consequences:** Every eligible adult receives 300 kr a month (C-1). Standard-rated prices rise (C-2). VAT revenue rises (C-3). Schedule 2 spending falls by about 1.66 billion (C-4). The Consolidated Fund is short by 1.2 to 3.5 billion a year under both readings (C-16).

**Invisible consequences:**
- *Who gains and who pays:* Most adults not on income support, and income-support recipients receiving less than 240 kr, gain on balance (C-8, C-10, under A-N1). Recipients of 300 kr or more get nothing from the payment and pay the higher VAT, so they are slightly worse off in 2028 (C-5, C-6). New residents pay VAT and receive nothing (C-12). Whoever meets the shortfall has less (C-17). Factor owners bear the part of the VAT not passed on (C-26), and sellers receive less per sale (C-25).
- *Work:* Recipients earning 400 to 792 kr work more, because earnings above 792 kr are no longer withdrawn at 65% (C-49). Adults whose net means rise and who can choose their hours work less (C-51).
- *Spending:* Recipients of 300 kr or more buy fewer standard-rated goods (C-28). Net gainers buy more reduced-rate goods (C-29). Durables are bought before the rate rise (C-47).
- *Border:* Kessa residents shop more in Varrin (C-31). Varrin retailers and grocers sell more (C-32, C-33), and the Varrin retail park gains value (C-37). Kessa sells less to Dornholt shoppers (C-34). Through the currency link, either the crown falls against Dornholt's currency or Dornholt buys more Korsland exports or assets (C-39).
- *Avoidance:* Sellers reclassify supplies (C-40), lobby for reduced-rate status (C-41) and leave more sales unrecorded (C-42). Businesses near the threshold stay below it or split (C-43). Revenue falls short of the static projection (C-44), and enforcement costs rise (C-45).
- *Housing and finance:* Low-cost rents rise (C-19). Financial services cost more (C-22), and returns at exempt financial firms fall (C-23).
- *Migration and claims:* Fewer residents emigrate (C-52), and some Dornholt workers move in (C-53). False residence claims are made (C-54). Recipients' groups lobby to index the payment (C-55). Pensions rise through indexation from 2029 (C-13).

**Ambiguous effects:** Resources of recipients of 300 kr or more from April 2029 (C-7: indexation against VAT and rent). Recipients receiving 240 to 300 kr (C-9). Heavy spenders (C-11). Net gainers' purchases of standard-rated goods (C-27). Hours of recipients earning 792 to 1,254 kr (C-50). Kessa shops' total sales and property values (C-35, C-36, C-38). Rental property values (C-20). Durables in early 2028 (C-48). Housing support spending under U1-a (C-18). What would decide each is listed in section 7.

**Key conditions:** Most of the VAT reaches prices (A-1, 0.75) and prices rise by no more than the tax (A-2, 0.85); net gainers' total VAT burden is below their net receipt (A-N1, 0.65, added); the Treasury projection is right in direction (A-N3, 0.7, added); the cross-border margin exists (A-8, 0.8); indexation runs as usual (A-24, 0.85).

**What this analysis cannot say:** Sizes, apart from the case's own arithmetic. Whether the gains outweigh the losses, or whether the policy is good. Whether food prices rise (A-26 below the cut-off). Long-run rents after the stock adjusts. Health and other out-of-scope effects are not analyzed.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | adults.eligible | subsidy_outlay (basic payment) | increase | short; medium; long | visible | B | CR-1 (op 4: K1 transfers 300 kr a month to each eligible adult); CR-8b (every payment is a receipt: 17.28 bn a year) | A-4 |
| C-2 | buyers.standard_rated_goods | price_paid (standard-rated goods, tax-inclusive) | increase | short; medium | visible | B | CR-1 (op 3: K3 attaches 4 more points to each standard-rated purchase); CR-5c (the charge moves the range of acceptable terms); CR-7b (most of it is passed into prices, A-1; by no more than the tax, A-2) | A-1, A-2 |
| C-3 | officials.tax_office | tax_revenue (VAT) | increase | short; medium; long | visible | B | CR-1 (op 3); CR-8b (what buyers and sellers pay is received by the Tax Office); responses do not remove a sixth of the base (A-N3) | A-N3 |
| C-4 | officials.benefits | subsidy_outlay (Schedule 2 benefits) | decrease | short; medium; long | visible | A | CR-1 (op 4: K2 reduces each benefit by 300 kr, not below nil); arithmetic: about 1.66 bn a year saved; medium: the indexation uplift (about 1.8% of the remaining outlay) is far smaller than the saving (CR-12e, arithmetic) | none |
| C-5 | income_support.300_or_more (outside the housing taper) | resources_available_other_uses | decrease | short | invisible | B | K1 and K2 cancel by construction (CR-12f); CR-3 note and CR-3c (they keep buying standard-rated goods, A-30, at prices higher by up to 4 öre per crown, A-1); renters also pay part of higher rents (C-19), the same direction | A-1, A-30 |
| C-6 | income_support.300_or_more.housing_taper | resources_available_other_uses | U1-a: decrease; U1-b: ambiguous | short | invisible | B | U1-a: counted income unchanged, so only the VAT chain and the rent chain (CR-3c; A-30, A-1); U1-b: counted income falls by 300 kr, housing support rises by about 120 kr (CR-1 op 4, arithmetic) against VAT and higher rent (CR-12b; no dominance premise covers the rent chain) | A-1, A-30, A-21, A-N4 |
| C-7 | income_support.300_or_more | resources_available_other_uses | ambiguous | medium (from April 2029) | invisible | B | CR-12b: (+) indexation raises the benefit by about 1.8% of 750 kr (A-24); (−) VAT on 300 to 600 kr of purchases, 12 to 24 kr (A-30, A-1); (−) rent (C-19). No dominance premise | A-1, A-24, A-30 |
| C-8 | income_support.below_240 | resources_available_other_uses | increase | short; medium | invisible | B | CR-1 (op 4: lose a benefit below 240 kr, gain 300 kr); CR-12b with A-N1 as dominance premise over VAT, rent and, under U1-a, lower housing support (CR-12e, empirical) | A-4, A-N1 |
| C-9 | income_support.240_to_300 | resources_available_other_uses | ambiguous | short; medium | invisible | B | CR-12b: (+) net receipt below 60 kr; (−) VAT (A-1, A-30) and rent | A-1, A-30 |
| C-10 | adults.no_income_support.purchases_below_7500 | resources_available_other_uses | increase | short; medium | invisible | B | CR-1 (op 4: +300 kr); CR-12b: VAT through prices is at most 0.04 S, below 300 kr (arithmetic); VAT through exempt sellers' costs and factor incomes, and U1-a housing loss, dominated by A-N1; rent chain bounded for the class by the response argument (CR-12e 0.8) | A-4, A-N1 |
| C-11 | adults.purchases_7500_or_more | resources_available_other_uses | ambiguous | short; medium | invisible | B | CR-12b: (+) 300 kr; (−) 0.04 S of at least 300 kr (A-1), factor incomes (A-3) | A-1, A-3 |
| C-12 | adults.resident_under_24_months | resources_available_other_uses | decrease | short; medium | invisible | B | CR-3c (they keep buying standard-rated goods at higher prices, A-1, and receive nothing until 24 months); rent chain the same direction | A-1 |
| C-13 | pensioners | subsidy_outlay (state pension, indexation uplift) | increase | medium; long (from April 2029) | invisible | B | CR-9 (the VAT rise enters the CPI with weight 0.55, A-1; the existing rule passes it to pensions, A-24); about 1.8% of 1,400 kr a month | A-1, A-24 |
| C-15 | officials.payments_agency | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 4: 140 m a year, 90 m set-up); CR-8c (means used up in administration) | none |
| C-16 | consolidated_fund | fund_balance | decrease | short; medium; long | visible | A | CR-8b and CR-8 0.8 (a law that promises more than its revenue pays): payment 17.28 bn against VAT 13.6 to 14.4 bn and offset 1.66 bn; short by 1.2 to 3.5 bn under both readings (arithmetic); government's own VAT is a receipt and an outlay of the same budget (CR-8 1.0); indexation and the Agency widen the gap | none |
| C-17 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | A | CR-8b and CR-8 0.7 (payers from the general budget): someone meets the shortfall (C-16), the Act does not say who | none |
| C-18 | officials.housing_support | subsidy_outlay (housing support) | U1-a: ambiguous; U1-b: increase | short; medium | invisible | B | U1-a: (−) counted income rises by 300 kr for those in the taper, saving about 0.18 bn (arithmetic); (+) higher rents raise the 70% share (C-19; CR-9); CR-12b. U1-b: (+) counted income falls for the 30,000 (about +0.04 bn) and (+) rents: increase | A-21, A-N1, A-N4 |
| C-19 | tenants.low_cost_rentals | price_paid (rent) | increase | short; medium | invisible | B | CR-4 (change in means: net gainers spend part of the rise on housing, A-N1, A-N4); CR-6 (more bids for a stock that cannot grow within a year, A-21, raise the clearing rent); medium: CR-9 (input_to: landlords' standard-rated inputs cost more, A-19), the same direction | A-N1, A-N4, A-21 |
| C-20 | landlords.private | asset_value (rental property) | ambiguous | short; medium | invisible | B | CR-7c and CR-10c: (+) expected rents rise (C-19, A-22); (−) unrecoverable input VAT (A-19); CR-12b, no dominance premise | A-19, A-21, A-22, A-N4 |
| C-22 | buyers.financial_services | price_paid (financial services) | increase | short; medium | invisible | B | CR-9 and LW-10 (relation: standard-rated inputs input_to financial services; inputs cost more and cannot be replaced at the old cost, A-19); CR-7b (each side's price moves in its direction; shares not ranked) | A-19 |
| C-23 | exempt_sellers.financial | return_on_capital | decrease | short | invisible | B | CR-7b (part of the input cost is borne by the sellers, who cannot reclaim it, A-19) | A-19 |
| C-25 | sellers.standard_rated | net_price_received | decrease | short; medium | invisible | B | CR-5c and CR-7b (the tax moves the range; part not passed on, A-1); A-2 bounds the tax-inclusive price, so the redistribution chain (kind 3) cannot raise the net price (CR-12e, empirical) | A-1, A-2 |
| C-26 | factor_owners | earnings (factor incomes) | decrease | short; medium | invisible | B | CR-9 and LW-10 (the part of the tax not passed into prices, A-1, lowers what sellers can pay their factors); CR-7b (borne roughly in proportion, A-3) | A-1, A-3 |
| C-27 | households.net_gainers | quantity_demanded (standard-rated goods) | ambiguous | short; medium | invisible | B | CR-12b: (−) CR-4c (higher price, A-1); (+) CR-4 change in means (A-7, A-N1) | A-1, A-7, A-N1 |
| C-28 | income_support.300_or_more | quantity_demanded (standard-rated goods) | decrease | short | invisible | B | CR-4c (higher price, A-1) and CR-4 change in means (lower means, A-7, A-30), the same direction | A-1, A-7, A-30 |
| C-29 | households.net_gainers | quantity_demanded (reduced-rate goods) | increase | short; medium | invisible | B | CR-4 change in means (A-7, A-N1); independent chain: CR-4 (x: standard-rated, y: reduced-rate, A-N5); CR-12d | A-7, A-N1 |
| C-30 | income_support.300_or_more | quantity_demanded (reduced-rate goods) | ambiguous | short; medium | invisible | B | CR-12b: (+) substitution from standard-rated goods (A-N5); (−) lower means (A-7) | A-7, A-N5 |
| C-31 | kessa_residents | cross_border_purchases (standard-rated goods in Varrin) | increase | short; medium; long | visible | B | CR-4 (x: buy in Kessa, y: buy in Varrin; x made worse by about 2.5% relative, A-8); CR-4a (no one moves the other way) | A-8 |
| C-32 | neighboring_jurisdictions.varrin_retailers | quantity_traded (standard-rated goods) | increase | short; medium; long | invisible | B | CR-9 (across_border: Kessa shoppers come, Dornholt shoppers stay home, A-8); CR-5 | A-8 |
| C-33 | neighboring_jurisdictions.varrin_grocers | quantity_traded (groceries) | increase | short; medium; long | invisible | B | CR-9 (complement, trip: groceries bought on the same trip, A-9) | A-8, A-9 |
| C-34 | sellers.kessa_retailers | quantity_traded (sales to Dornholt shoppers) | decrease | short; medium; long | invisible | B | CR-9 (across_border); CR-4 (Dornholt shoppers: x: Kessa, y: Varrin, A-8) | A-8 |
| C-35 | sellers.kessa_retailers | quantity_traded (all standard-rated sales) | ambiguous | short; medium | invisible | B | CR-12b: (−) C-31, C-34; (+) Kessa residents' added means (A-N1, A-7) | A-7, A-8, A-N1 |
| C-36 | sellers.kessa_grocers | quantity_traded (groceries) | ambiguous | short; medium | invisible | B | CR-12b: (−) trip complement to Varrin (A-8, A-9); (+) added means (A-7, A-N1) | A-7, A-8, A-9, A-N1 |
| C-37 | owners.varrin_retail_park | asset_value | increase | short (from 2027); medium | invisible | B | CR-7c and CR-10c (expected yields rise with C-32, C-33; captured by owners when the rate rise becomes expected, partly from January 2027; A-22) | A-8, A-22 |
| C-38 | owners.kessa_retail_property | asset_value | ambiguous | short; medium | invisible | B | CR-7c, CR-10c on C-35, which is ambiguous; CR-12b | A-7, A-8, A-22, A-N1 |
| C-39 | buyers.foreign | exchange_rate (+), quantity_traded (Korsland exports and assets bought from Dornholt) (+) | at_least_one_increase | medium | invisible | B | CR-9 0.7 (currency: more crowns paid for Varrin goods are means for Dornholt residents to buy Korsland exports or assets); CR-6 (the pressure goes to the price of the currency or to the quantity of exports) | A-8 |
| C-40 | sellers.standard_rated | reclassification (supplies reshaped into reduced-rate or exempt categories) | increase | short; medium | invisible | B | CR-4 (x: standard-rated form, y: reduced-rate or exempt form; the gain from y rises by 4 points, A-10) | A-10 |
| C-41 | sellers.standard_rated | lobbying_effort (for reduced-rate or exempt status) | increase | short; medium; long | invisible | B | CR-4 (x: accept, y: lobby; stake raised by 4 points, A-20, A-18); CR-4 1.0 (signed against the counterfactual contest over reduced-rate status at 20%, which A-20 compares); CR-8c | A-18, A-20 |
| C-42 | sellers.standard_rated | informal_activity (unrecorded sales) | increase | short; medium | invisible | B | CR-4 (x: comply, y: violate; the gain from not recording a sale rises, enforcement unchanged, A-11) | A-11 |
| C-43 | businesses.near_registration_threshold | quantity_supplied (−), reclassification (business splitting) (+) | at_least_one_as_stated | short; medium | invisible | B | CR-1 1.0 (the threshold is a notch: crossing it now costs 24% of all sales, not 20%); CR-4 (x: cross, y: stay below or split, A-12) | A-12 |
| C-44 | officials.tax_office | tax_revenue_vs_static_projection | decrease | short; medium | invisible | B | CR-4 and CR-4c (cross-border, reclassification, evasion, threshold, lower purchases: C-31, C-40, C-42, C-43, C-28); CR-12e with A-N3 against the kind 3 redistribution chain | A-N3 |
| C-45 | officials.tax_office | enforcement_cost | increase | short; medium | invisible | B | CR-4 (more reclassification and evasion to police, A-10, A-11); CR-8c | A-10, A-11 |
| C-46 | sellers.standard_rated | compliance_cost (repricing, systems) | increase | short | invisible | A | CR-1 (op 3: every registered seller must charge the new rate); CR-8c | none |
| C-47 | buyers.durables | quantity_traded (durables, 15 January to 31 December 2027) | increase | short (announcement window) | invisible | B | CR-10a (the dated rate rise alters choices now); CR-4 (x: buy after 1 January 2028, y: buy before, A-13) | A-13 |
| C-48 | buyers.durables | quantity_traded (durables, first months of 2028) | ambiguous | short | invisible | B | CR-12b: (−) purchases moved into 2027 (A-13); (+) payment spent on durables (A-14) | A-13, A-14 |
| C-49 | income_support.earning_400_to_792 | hours_worked | increase | short; medium | invisible | B | CR-1 1.0 (ranges): earnings above about 792 kr no longer lose 65 öre per crown; CR-4 (x: earn below 792, y: earn above; y improved, A-5); CR-12e (arithmetic: the return per crown above 792 rises from 35 to 100 öre against a VAT effect of at most 3.3%) | A-5 |
| C-50 | income_support.earning_792_to_1254 | hours_worked | ambiguous | short; medium | invisible | B | CR-4 (withdrawal ends: more hours) against CR-4's exception (means rise by 300 kr less the lost benefit: fewer hours, A-6); CR-12b | A-6, A-29 |
| C-51 | adults.net_gainers.choosing_hours | hours_worked | decrease | short; medium | invisible | B | CR-4 change in means (net means rise, A-N1; fewer hours is among the uses, A-6); CR-4 (VAT lowers the goods value of earnings: x: work, y: not work); same direction | A-6, A-29, A-N1 |
| C-52 | residents.would_emigrate | job_changes (moves to Dornholt) | decrease | medium; long | invisible | B | CR-1 op 3 (the payment is attached to staying resident); CR-4 (x: move, y: stay, A-15) | A-15 |
| C-53 | dornholt_workers | job_changes (moves to Korsland) | increase | medium; long | invisible | B | CR-4 (x: stay, y: move; the payment after 24 months, A-16); CR-10a (expected payment acts now) | A-16 |
| C-54 | claimants.false | legal_breach (false residence claims) | increase | short; medium | invisible | B | CR-4 (x: no claim, y: false claim; a payment now attaches to y, against repayment and a penalty of up to 5,000 kr, A-17); CR-12 0.9 (an activity that exists only under the policy) | A-17 |
| C-55 | recipients_groups, pensioners_associations | lobbying_effort (to index or raise the payment) | increase | medium; long | invisible | B | CR-4 (x: accept a fixed 300 kr, y: lobby; the payment's real value falls each year while benefits and pensions are indexed); CR-12 0.9 (no such payment to lobby over without the policy); CR-8c | A-18 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-060-C1: Indexation is an existing rule applied mechanically (CPI rise passed to benefits and pensions). CR-9 covers it only by treating the CPI as an `input_to` relation, which is not an exchange; no core rule says how a policy propagates through a formula in another statute (indexation, means tests). It was handled as arithmetic on an existing rule.
- GAP-060-C2: The redistribution among households (net gainers against payers of VAT and the shortfall) leaves the aggregate change in demand for every good as a kind 3 chain. No core rule gives a sign for aggregate demand when means are moved between classes with unknown rankings (CR-4, "a change in means alone"). Wherever a market-level sign was needed (C-25, C-44), it had to come from an empirical bound (A-2, A-N3).

**(b) Core-rule wording that was hard to apply.**
- CR-12e 0.8 (response argument "binds the response as a whole"): used to keep the rent chain from overturning the gain to net gainers as a class (C-10). The rule speaks of a response that cannot reverse the change that causes it; applying it to a rent rise caused by the same class's added means was a stretch, and it does not cover renters who are in the class but gain little.
- CR-3 note ("worse off is not poorer") with a lump sum and a tax on purchases at once: the class splits by purchases relative to 7,500 kr, but the indirect channels (exempt sellers' costs, factor incomes) are not attributable per person from the case's figures, which forced the broad premise A-N1.
- CR-1 1.0 (ranges and notches) for a benefit offset: K2 performs a transfer for some recipients and also removes a withdrawal range for others; the rule's wording on ranges assumes a charge, not the end of a withdrawal rate.
- CR-12f (cancellation by construction) is clear for K1 against K2 but the record cannot show a class for which the net is zero while other components still act on it (VAT); the rows were written as VAT-only effects.
- CR-4 1.0 (lobbying signed against the counterfactual contest): for lobbying over reduced-rate status, the contest also exists at 20%; the sign rests on the raised stake (A-20).

**(c) Vocabulary missing from the ontology.**
- No variable for population or residence (migration was recorded as `job_changes`).
- No variable for benefit income or for the withdrawal rate faced by recipients (effective marginal rate); the work-incentive change could be recorded only through `hours_worked`.
- No variable for factor incomes as a whole (used `earnings`), nor for fraudulent claims on the state (used `legal_breach`).
- No generic actor class for benefit recipients, pensioners or a general-budget fund (`consolidated_fund` was used).
