# WE-060 / Analysis: A basic payment to every adult, funded by a higher VAT, with means-tested benefits offset

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

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

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the structure of the Korsland case. Every eligible adult is paid, standard-rated prices and VAT revenue rise, Schedule 2 outlay falls, and the Consolidated Fund is short under both readings, with the shortfall met by a group of payers. Recipients of 300 kr or more are poorer in the first period and `ambiguous` after indexation; recipients with small benefits and lower-spending adults gain on net. Recipients near the old exit point work more, lower-income adults in work work less, and the old taper's hours are `ambiguous`. Purchase responses, border shopping, reshaping, evasion, the registration notch, timing, migration, false claims and lobbying match. There are seven S rows. Four are errors in the pattern version. On Kessa sellers' sales and Kessa property (pattern C-35, C-37), the pattern omits the opposing chain from Kessa residents' net gain in means. On recipients of 300 kr or more in the housing taper (C-45), the pattern's total leaves out the housing item that gives them up to 120 kr under U1-b. On the Treasury's housing outlay (C-9), the pattern omits the rent chain through the 70%-of-rent formula. Two are errors in the core version. Low-cost rents (core C-19) are signed `increase` without the opposing chain from net losers who rent, and the fund's long-run balance (C-16) is signed `decrease` although the fixed payment erodes against a VAT that grows with prices. One is a difference of premises: on VAT revenue against the static projection (C-58 against C-44), the core version uses the Treasury's projection as a dominance premise. The core version omits the item-level records the 0.8 note on two items asks for. It also omits hours and purchases of higher-income adults (its split at 7,500 kr leaves no sure net-loser class), the low wage, firms near the threshold, the consumption-or-saving groups and the long-run household totals. The pattern version omits new residents, who pay VAT and receive nothing, as well as factor owners' earnings, landlords' asset values, the currency link and the Tax Office's enforcement cost.

Counts: M 29, V 12, S 7, OP 6, OC 14.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | V | | The core records the receipt as `subsidy_outlay` on adults.eligible rather than `resources_available_other_uses`. |
| C-2 | C-1, C-16 | V | | The core folds the Treasury's outlay into C-1 (both sides, CR-8b) and C-16. |
| C-3 | none | OC | E | Schedule 2 benefit item down for recipients. CR-12 0.8 asks for each item where two items move in opposite directions, and for `recipients.taper_exit` they do not cancel. Core-version omission: it recorded only totals (C-8, C-9). For the 300-kr-or-more class, CR-12f and the 0.8 note conflict (see Findings). |
| C-4 | C-4 | M | | Core adds the medium-run indexation uplift, netted by arithmetic. |
| C-5 | C-2 | M | | |
| C-6 | C-3 | M | | The core adds A-N3. TX-1 is written for a tax imposed; for a rate rise, revenue rising is not Tier A without a premise, since the base response also cuts the yield of the old 20%. Pattern hidden premise. |
| C-7 | none | OC | E | Housing support item per reading for tenants not on income support (U1-a decrease; U1-b no_change). By construction on the provisions. The core folded it into C-10 and C-18 and did not record the item. Core-version omission. |
| C-8 | none | OC | E | Housing support item for the 30,000 in both tapers (U1-a no_change; U1-b increase). The core folded it into the total C-6. Core-version omission. |
| C-9 | C-18 | S | E | Pattern: U1-a decrease, U1-b increase (by construction). Core: U1-a ambiguous, U1-b increase. Housing support is 70% of rent, so the rent chain reaches the outlay (CR-9). Pattern-version omission: it records rents as `ambiguous` (C-40) but does not carry them into the formula. The core's sign is right for the wrong reason, since its rent chain comes from C-19, whose `increase` is itself wrong. With rents a kind 3 chain, both readings should be `ambiguous` unless a dominance premise covers the rent chain. The horizon "short, before leases reset" would rescue the pattern's signs only with a premise on lease terms (CR-6 0.7). |
| C-10 | none | OC | J | `tax_share_borne` ambiguous. The core signs each side's price instead (C-2, C-25) and records no share. Nothing scorable lost. |
| C-11 | C-49 | V | | Pattern: group (employment, hours). Core: `hours_worked` alone. A-5 says "work or extra hours", so the group is the safer record. |
| C-12 | C-50 | M | | |
| C-13 | C-51 | M | | The pattern lists A-1 and A-29 only, holding that the relative-price chain signs the result if A-6 fails (CR-12d). The core requires A-6 and A-N1 as well. Both are defensible. Without A-6 the means chain is unsigned rather than opposed. |
| C-14 | C-51 | V | | The core covers the class within net gainers, but not the third chain under U1-a: the payment pushes counted income into the housing taper. |
| C-15 | none | OC | E | `adults.higher` hours `ambiguous`: relative price against a fall in means with A-6. The core did not examine hours of net losers. Core-version omission. |
| C-16 | C-28 | M | | |
| C-17 | C-30 | M | | |
| C-18 | C-27 | M | | |
| C-19 | C-29 | M | | The core covers reduced-rate goods only, not exempt goods. |
| C-20 | none | OC | E | `adults.higher` standard-rated purchases decrease (substitution, and lower means with A-7). Valid. The core split classes at 7,500 kr of purchases (C-11 ambiguous) and so had no sure net-loser class above it. Core-version omission. |
| C-21 | none | OC | J | Total standard-rated quantity `ambiguous`. The core states it as a kind 3 chain (GAP-060-C2) but records no key. Nothing scorable lost. |
| C-22 | C-31 | M | | |
| C-23 | C-34 | V | | The core records it on Kessa sellers' sales to Dornholt shoppers. |
| C-24 | C-40 | M | | |
| C-25 | C-42 | M | | |
| C-26 | C-43 | V | | The core gives a group (`quantity_supplied` −, `reclassification` +). A-12 says businesses "can stay below the threshold or split", a disjunction. It supports the group, not C-26 and C-27 each signed alone. Pattern overclaims slightly. |
| C-27 | C-43 | V | | As C-26. |
| C-28 | C-47 | M | | The core's window starts at publication (15 January) rather than enactment. |
| C-29 | C-48 | M | | |
| C-30 | C-52 | M | | |
| C-31 | C-53 | M | | |
| C-32 | C-54 | M | | |
| C-33 | C-55 | M | | The core's key is narrower: indexing or raising the payment. |
| C-34 | C-41 | M | | |
| C-35 | C-35, C-36 | S | E | Pattern: Kessa sellers' sales decrease. Core: total standard-rated sales and grocery sales `ambiguous`. Kessa residents are mostly net gainers, and with A-7 (which the pattern uses in C-19) they buy more at home: a kind 2 chain at p ≥ 0.5. Pattern-version omission in section 7. The pattern's sign holds only for the narrow item "sales diverted to Varrin", which is C-22 seen from the seller. |
| C-36 | C-32, C-33 | V | | Split into standard-rated goods and groceries. |
| C-37 | C-38 | S | E | Pattern: Kessa retail property decrease. Core: `ambiguous` (CR-7c on an ambiguous yield). Follows from C-35: pattern-version error. |
| C-38 | C-37 | M | | |
| C-39 | C-22, C-23 | V | | Pattern: group (exempt sellers' price +, supply −). Core: buyers' price of financial services increase, and exempt financial firms' return decreases, by CR-7b ("each side's price moves in its direction"). The core's stronger sign leans on a reading of CR-7b (see Findings). Landlords are handled under rents (C-19, C-20). |
| C-40 | C-19 | S | E | Pattern: low-cost rents `ambiguous`. Core: `increase`. The core's chains are net gainers' added means (A-N1, A-N4) on a fixed stock (A-21) and, in the medium run, landlords' input VAT. It omits the opposing chain from renters whose means fall: recipients of 300 kr or more (C-5, a kind 3 chain since rent also becomes relatively cheaper) and new residents (C-12). It also omits, under U1-a, the 120,000 taper tenants who lose up to 120 kr. No figure in the case gives the composition of the segment's tenants, so CR-12e arithmetic is not available. Core-version error. |
| C-41 | none | OC | E | Low-wage `wage_rate` `ambiguous` (CR-6 and CR-7a on the labor-supply changes C-49 to C-51). Core-version omission: the core changed labor supply in three classes but did not follow it into the labor market. |
| C-42 | none | OC | E | Value of firms near the threshold `ambiguous` (CR-7c: the value of growing past the line falls; registered rivals are burdened). Core-version omission. |
| C-43 | C-13, C-7 | V | | Pensioners' uplift is recorded as `subsidy_outlay` on pensioners (C-13); recipients' uplift is folded into the total C-7. |
| C-44 | C-13, C-4 | V | | The Treasury side is recorded within C-13 and netted into the medium-run C-4. |
| C-45 | C-5 | M | | Recipients of 300 kr or more outside the housing taper, short. The core adds a rent chain, which is unnecessary and rests on C-19. |
| C-45 (subclass in the housing taper) | C-6 | S | E | The pattern's class includes the 30,000 in `households.both_taper`, and its total lists only payment, offset and VAT. Under U1-b their housing support rises by up to 120 kr (pattern C-8) against 12 to 24 kr of VAT, so their total is not a decrease. Core C-6 gives U1-a decrease, U1-b `ambiguous` (the gain depends on where each member sits in the taper; no distribution in the figures). Pattern-version error: the section 7 text lists housing among the items, but the row omits it. |
| C-46 | C-7 | M | | |
| C-47 | C-8 | M | | The pattern settles the sign by arithmetic (300 − 240 − 43 > 0). That leaves out the U1-a housing loss for members in the housing taper (40% of the net receipt, at least 24 kr at the margin), which the pattern sets aside as "few", and the VAT reaching them through exempt sellers' prices. At the boundary these can exhaust the margin, so an empirical premise (core A-N1) is needed. Pattern overclaims the kind of dominance, not the sign. |
| C-48 | C-9 | M | | |
| C-49 | C-10 | M | | Same point as C-47: the bound "≤ 280 kr through prices" omits VAT on exempt sellers' inputs passed to rents and financial services (about 3.2 billion kr, about 56 kr a month per adult on average). The class's upper edge has a margin of 20 kr. The core's A-N1 is the honest premise. The core's own use of CR-12e's response argument for the rent chain in C-10 is a stretch, as it says. |
| C-50 | none | OC | E | `adults.lower` long-run total `ambiguous` (TS-3: the fixed payment erodes). Core-version omission: its time structure notes the erosion but records no long-run household sign. The pattern does not state the price-path premise TS-3 assumes. |
| C-51 | none | OC | E | `adults.higher` (income and spending over 10,000 kr) total decrease, by arithmetic under any split with A-3 (burden at least 340 kr). Valid. The core's class split (C-11, 7,500 kr or more, `ambiguous`) misses it. Core-version omission. |
| C-52 | C-11 | V | | Overlapping middle classes, both `ambiguous`. |
| C-53 | none | OC | E | `adults.lower` consumption or saving, `at_least_one_increase` at constant prices (CR-4 "a change in means alone" with its 0.7 note on saving; CR-8b). Derivable. Core-version omission. |
| C-54 | none | OC | E | `adults.higher` consumption or saving, `at_least_one_decrease`. As C-53. |
| C-55 | C-17 | M | | |
| C-56 | C-16 | M | | |
| C-57 | C-16 | S | E | Pattern: the fund's long-run balance `ambiguous`. Core: C-16 `decrease` in the long run, "unchanged on the case's figures". The payment (17.28 billion) is fixed in money, while the VAT increment (13.6 billion) grows with nominal spending, and the indexation cost only with prices. Under any positive inflation the gap closes after roughly an 18% rise in prices (about 13.25 g ≈ 15.6) and then reverses. The core's long-run `decrease` has no premise for it. Core-version error. The pattern should state the price-path premise TS-3 assumes. |
| C-58 | C-44 | S | A | Pattern: VAT against the static projection `ambiguous` (it overrode TX-9 with an opposing chain from net gainers' purchases, A-7). Core: `decrease`, with A-N3 (the Treasury's projection, 13.6 against 14.4 billion) as an empirical dominance premise under CR-12e. The core also treats the redistribution chain as kind 3, which is more accurate: net losers buy less. The difference is the premise. The Treasury figure is in the case, so the core's reading is the better supported. |
| C-59 | C-15 | M | | |
| C-60 | C-46 | M | | |
| C-61 | none | OC | E | Adults' `compliance_cost` of registering, Tier A with no assumption. The record says the Agency checks residence "by matching the population register". Whether adults must register or prove anything is not in the record. Pattern hidden premise: it needs an assumption, or should be dropped. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-12 | OP | E | Adults resident under 24 months pay the higher VAT (through prices, A-1, or factor incomes) and receive nothing: `resources_available_other_uses` decrease. Valid. Pattern-version omission: it notes arrivals pay VAT before the payment, but records no key for existing new residents. |
| C-20 | OP | E | Private landlords' rental property value `ambiguous` (CR-7c: rents against unrecoverable input VAT). Pattern-version omission. Its sign stands even with rents `ambiguous`. |
| C-25 | OP | J | Sellers' `net_price_received` decrease (CR-5c, CR-7b, A-1, A-2). The pattern left the seller side as TX-2's "and/or" with a share `ambiguous` (C-10). Defensible if A-1 ("most", not all, passes into prices) is read as partial pass-through. Otherwise the core's sign is "decrease or no change". |
| C-26 | OP | E | Factor owners' `earnings` decrease for the part not passed into prices (A-1, A-3; CR-7b, CR-9). The pattern uses A-3 in every total but records no key. Pattern-version omission. Same caveat on partial pass-through as C-25. |
| C-39 | OP | E | Currency link: more crowns spent in Varrin are means for Dornholt residents to buy Korsland exports or assets (CR-9 0.7), as a group with `exchange_rate`. The pattern dismissed TX-8 because the VAT is border-adjusted, but cross-border shopping is an import by residents. Pattern-version omission (CR-6 1.0: small effects are signed). |
| C-45 | OP | E | Tax Office `enforcement_cost` increase from more reshaping and evasion (CR-8c, A-10, A-11). Pattern-version omission. |

### Findings

- **Pattern overclaims or hidden premises.** *TX-9* applied as written gives `decrease` against the static projection, with no clause for a tax whose revenue goes back to the payers. The pattern version overrode it to `ambiguous`. The core version reached `decrease` only by adding the Treasury's projection as a dominance premise (A-N3), against a redistribution chain it recognized as kind 3. *TX-1* gives `tax_revenue` increase at Tier A for a tax imposed. Applied to a rate rise (C-6), it hides the premise that the base response does not remove the gain. *RS-17*'s first clause compares below with above; the pattern re-signed it. The core signed the threshold group against no Act directly (C-43). *TS-3* assumes a price path, and the pattern used it (C-50, C-57) without stating one. The pattern's arithmetic dominance in C-47 and C-49 omits two items it names elsewhere: the VAT on exempt sellers' inputs, and (C-47) the U1-a housing loss. Signs C-26 and C-27 rest on one disjunctive premise (A-12). C-61 assumes a registration step the record does not contain.
- **Errors in the core version.** Low-cost rents (C-19) are signed `increase` without the opposing chain from net losers who rent, nor (U1-a) the taper tenants who lose support. The housing outlay (C-18) inherits it. The fund's balance (C-16) is signed `decrease` for the long run against the erosion of a fixed payment. Omissions: the item-level records the CR-12 0.8 note asks for (benefit and housing support per class, pattern C-3, C-7, C-8); hours and purchases of a sure net-loser class (pattern C-15, C-20, C-51, C-54); the low-wage labor market (C-41); firms near the threshold (C-42); consumption-or-saving groups (C-53, C-54); long-run household totals (C-50). C-49 signs `hours_worked` alone where A-5 supports only a group with employment. The rent chain is bounded in C-10 by a response argument that, as the core itself notes, does not fit a rise caused by the class's own spending.
- **Errors in the pattern version.** The Kessa sellers' and property signs (C-35, C-37) omit residents' net gain in means. The total for recipients of 300 kr or more (C-45) leaves out the housing item for the 30,000 in both tapers under U1-b. The housing outlay (C-9) omits the rent chain through the 70%-of-rent formula. Omissions: new residents (core C-12), factor owners (C-26), landlords' asset values (C-20), the currency link (C-39), the Tax Office's enforcement cost (C-45).
- **Test of 1.0 verdicts.** *CR-4, "a change in means alone" (needed interpretation: net the money changes first):* confirmed. The core had to net them too, by an empirical premise (A-N1) rather than arithmetic (C-10, C-51), and recorded the aggregate-demand question as GAP-060-C2. *CR-4's exception, "opposite direction" (worked with interpretation):* confirmed. The core applied the means effect in the same direction as substitution for net gainers (C-29, C-51) and in the opposite direction for recipients (C-30), without comment. *CR-12 0.8, two items, against CR-12f (needed interpretation):* confirmed. The core flagged the same conflict in its (b) and resolved it by recording no items at all, which loses items the 0.8 note requires. *TX-9 (failed as written):* partly confirmed. TX-9's unconditional `decrease` is not derivable where the revenue is returned to the payers, so its Unless clause is incomplete. On this case's figures, though, the core reached TX-9's sign with the Treasury's projection as a premise, so the pattern's override to `ambiguous` was not needed. *RS-17's first clause (re-signed):* confirmed by core C-43.
- **Limits of the core rules.** None produced a difference: no row has cause K. GAP-060-C1 (propagation through a formula in another statute: indexation, means tests) is not a gap. CR-1's recording note covers it: state the counterfactual law, and the existing rule applied to the changed price or income is an operation on the recipients. GAP-060-C2 is Q19 and is a correct stop, not a gap. Unclear core-rule wording: (1) CR-4, "a change in means alone", does not say to net several changes in means before applying it. (2) CR-4's exception says the means effect runs "in the opposite direction"; it can run either way. (3) CR-12f and the CR-12 0.8 note on two items conflict where items cancel by construction and a third item remains. (4) CR-7b's "only the direction of each side's price is signed" can be read as signing both sides (core C-22, C-25) or only the at-least-one group (pattern C-39, C-10). (5) CR-12e's response argument (0.8 note) does not say whether it bounds a price rise caused by the class's own added spending (core C-10). (6) CR-1 0.7 calls operation 4 a transfer "no choice avoids", which leaves unclear how to classify a transfer avoided only by giving up a status such as residence.
