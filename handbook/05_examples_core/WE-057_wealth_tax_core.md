# WE-057 / Analysis: Ostrevian Net Wealth Tax Act (1% above M 10 million, formula valuation of unlisted shares, exit charge)

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Ostrevian Net Wealth Tax Act.** Ostrevia has about 9.2 million people in 4.0 million households; its currency is the mark (M). About 11,000 households have net worth above M 10 million at market values, about M 290 billion in all, of which about M 180 billion lies above the threshold. Their assets: listed shares M 87 bn (taxed households own about 8% of the domestic listed market; foreign investors 55%, pension funds and insurers 30%); unlisted business shares M 110 bn (book equity about M 50 bn, about 45% of estimated market value; unlisted firms are bought mostly by companies and private equity, families buying about a third by value); real estate M 49 bn (main homes M 18 bn; taxed households buy about 45% by value of homes above M 3 million, foreign buyers about 15%); pension rights M 20 bn; cash and bonds M 17 bn; art and other M 7 bn. About 6,000 further households have M 8 to 10 million as the Act measures it. About 120 households above M 10 million leave each year without the tax, each paying about M 0.9 million a year in income and gains taxes.

Existing taxes, unchanged on both paths: capital gains tax of 28% on realization, with gains untaxed at death; gift and inheritance tax of 20% above M 1 million per recipient over a lifetime, gifts and bequests taxed alike. Tax Code art. 44: assets transferred to a company the transferor controls are not treated as sold. Small companies may carry investments at cost. Personal pension accounts take up to M 300,000 a year (M 50,000 deductible), locked until 62; defined-benefit rights cannot be assigned or borrowed against but can be transferred at a cash-equivalent value to another scheme. Valtria, two hours away, shares the language, has free movement, no wealth tax and no tax on gains on shares held over a year. Quellin taxes wealth at 0.5% above a higher threshold.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Households resident in Ostrevia, on worldwide assets. Just outside: Valtria (no wealth tax, free movement, same language); Quellin (wealth tax at 0.5%). | §2, §3. |
| Announced / enacted / effective / expires | Announced 1 November 2026; enacted 18 March 2027; first valuation date 31 December 2027; exit charge for departures on or after 1 January 2028; no expiry. | §1, §15. |
| Enforcement (who, penalties, resources) | Ostrevian Tax Agency: self-assessment; a new valuation unit costing about M 45 million a year from the general budget; audits of about 10% of returns a year. Penalty: 50% of the tax understated. Information exchange with 110 countries. | §10, §11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Annual tax | `capital_tax` | Household net worth on 31 December each year | Resident households | 1% of net worth above M 10 million (a kink: only the excess is taxed); threshold fixed in marks. | Household goods up to M 100,000. §5(2): rights the holder cannot assign, surrender or borrow against valued at nil (U1). |
| K2 Valuation rules | Part of K1 | — | — | Listed securities at closing price; real estate and art at market value as assessed by the taxpayer, subject to audit; unlisted shares at the holder's proportion of net assets in the latest audited balance sheet. Debts deductible. | — |
| K3 Exit charge | `capital_tax` (on unrealized gains) | Persons ceasing to be resident on or after 1 January 2028 | Members of a household liable under K1 on any of the three valuation dates before departure | 28% on gains as if all assets were sold at market value the day before departure, in five yearly installments with interest. | Departures before 1 January 2028. |
| K4 Revenue | Revenue use | K1, K3 | — | General budget; no earmark. | — |

Unclear provisions:
- **U1, pension rights.** Reading U1-a: a transfer to another scheme is a surrender, so pension rights count at transfer value. Reading U1-b: a transfer is not a surrender, so pension rights are valued at nil. The Agency has not ruled; readings get no probability, and one sign per reading is given where a sign depends on U1.

**Figures (from the record).** Static base under the Act's own rules: about M 120 billion above the threshold (U1-a) or M 110 billion (U1-b), so M 1.2 or M 1.1 billion a year; the fiscal note uses M 1.1 billion. Book valuation removes about M 60 billion: the effective rate on unlisted holdings is about 0.45% of market value, against 1% on listed shares and cash and, under U1-b, 0% on pensions. A listed portfolio bought for M 4 million and worth M 10 million, moved into a holding company, is taxed on M 4 million. A household with M 30 million that gives M 10 million to each of two adult children's households pays about M 3.6 million gift tax (which a later bequest would have paid) and moves from M 200,000 a year to zero. Exit charge: about M 1.7 million on M 6 million of gains; about M 0.2 billion a year at the counterfactual departure rate if most were liable. The Agency projects about 300 additional departures in the 14 months before the first valuation date.

**Counterfactual law.** Without the Act: no wealth tax, no exit charge; existing capital gains, gift and inheritance taxes, art. 44 and pension rules as above.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Annual tax | binary (state takes) | Yes above the threshold (A-1); not binding below it | 4 for inframarginal holders (a sum due each year whatever they do, given their wealth); 3 for every household near or above the line, on the options of holding wealth in market-valued forms, holding it at all (rather than consuming or giving it), and residing in Ostrevia on 31 December; recorded per range (CR-1, 0.9 note): no operation below M 10 million, op 3 and 4 above it; the kink is a range, not a notch (only the excess is taxed) | CR-3c, CR-4, CR-7b, CR-7c, CR-8b, CR-10a, CR-10c |
| K2 Valuation | part of K1 | Yes | 3: the burden attached to holding each form differs by form (1% of market on listed shares and cash; about 0.45% of market on unlisted shares; self-assessed values on property and art; per reading on pensions: U1-a 1% of transfer value, U1-b nil) | CR-4 (x: taxed form, y: formula-favored form), CR-7a |
| K3 Exit charge | binary (state takes, on an option) | Yes for liable households leaving from 1 January 2028 (A-26) | 3: a charge attached to the option of leaving, dated from 1 January 2028 (CR-1, 0.7 note: before that date it acts only through expectations); the option "leave before 2028" is untouched | CR-4 (x: leave, y: stay; x: leave later, y: leave before 2028), CR-10a |
| K4 Revenue | binary (state gives, unnamed recipients) | — | 4 to the general budget | CR-8b, CR-8d |

The tax was announced 14 months before its first valuation date and was not expected before (A-29), so every response that can be completed before 31 December 2027 (gifts, holding companies, departures without the exit charge) is open in that window (CR-10a).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| households.taxed | About 11,000 households above M 10 million | Op 4 and 3 (K1); valuation differences by form (K2); exit charge (K3). |
| households.taxed.listed_portfolios | Taxed households with large listed portfolios carrying unrealized gains | CR-4 (x: hold directly, y: hold through a controlled company carried at cost, A-2). |
| households.near_line | Households just above M 10 million, and the 6,000 at M 8 to 10 million | Op 3 at the margin of the line (A-8). |
| households.taxed.with_heirs | Taxed households with adult children they planned to leave wealth to (A-5) | CR-4 (x: bequest later, y: gift now). |
| adult_children | Recipients of gifts | Through CR-9 (gift). |
| households.taxed.at_margin_of_leaving | Taxed households for whom living in Valtria ranks close to staying (A-9) | CR-4 (x: stay, y: leave), and by date (leave before 2028 free of K3). |
| households.taxed.departing_after_2028 | Liable households that leave from 2028 for other reasons (A-26) | Op 3: K3 attaches about 28% of unrealized gains to leaving. |
| households.taxed.would_leave_later | Liable households that would have left after 2028 for other reasons (A-11) | CR-4 (x: leave and pay K3, y: stay). |
| households.taxed.db_pension_holders | Executives with defined-benefit rights | Per reading: U1-a rights count at transfer value; U1-b nil. |
| households.taxed.with_pension_room | Taxed households below the yearly contribution limit (A-24) | Per reading: U1-b a nil-valued form is open. |
| foreigners.prospective_residents | Wealthy foreigners who would have moved to Ostrevia (A-12) | Op 3 on the option of moving in. |
| owners.unlisted_firms | Taxed households owning unlisted firms | K2 values their holding at book; CR-4 on accounting and investment mix (A-4), dividends (A-17), listing (A-3). |
| unlisted_firms | The firms themselves | Through CR-9 (ownership): retained earnings, investment, listing choice. |
| holders.listed_shares | Foreign investors, pension funds, insurers and remaining holders of Ostrevian listed shares | Through CR-9 (same market): taxed households sell or hold through companies (A-16). |
| buyers.unlisted_firms | Companies, private equity and families who buy unlisted firms | Through CR-9 (A-18). |
| owners.high_end_homes_ostrevia | Owners of Ostrevian homes above M 3 million | Through CR-9 (A-13); capitalization (CR-7c). |
| buyers.high_end_homes_ostrevia.untaxed | Foreign and other untaxed buyers of such homes | Through CR-9. |
| builders.high_end_ostrevia | Builders of such homes | Through CR-9 (input_to). |
| neighboring_jurisdictions.valtria_home_market | Buyers, owners and builders of high-end homes in Valtria's border cities | Through CR-9 (across_border): emigrants buy there (A-23). |
| sellers.art_collectibles | Dealers and auction houses | Through CR-9 (substitute): A-20. |
| pension_providers | Personal pension providers | Through CR-9 (contract), per reading (A-24). |
| intermediaries.advisers | Valuers, lawyers, tax advisers, company formation agents | Through CR-9 (complement of compliance and avoidance). |
| officials.tax_agency | Administers and enforces K1 to K3 | Op 4: M 45 million a year for a valuation unit; audits. |
| general_budget | Receives K1 and K3; loses other taxes on departures | Op 4. |
| taxpayers, recipients_of_other_spending | Those who gain if net receipts are positive (A-22) | Through K4 (as a group). |
| organized_interests | Family-business federations, advisers, pension providers, campaigners (A-21) | CR-4 (x: accept, y: lobby) on the Act's rules (valuation, U1). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 to K4 alter. Each sign is against Ostrevia at the same dates without the Act.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | households.taxed | resources_available_other_uses | decrease | short; medium; long | CR-1 op 4, CR-3c, CR-8b | A-1 |
| C-2 | general_budget | tax_revenue (net wealth tax) | increase | short; medium; long | CR-1 op 4, CR-8b | A-1 |
| C-3 | officials.tax_agency | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | - |
| C-4 | households.taxed, households.near_line | compliance_cost | increase | short; medium; long | CR-1 op 3, CR-8c | - |
| C-5 | households.taxed.db_pension_holders | resources_available_other_uses | U1-a: decrease; U1-b: no_change | short; medium; long | CR-1 op 4 (per reading), CR-3c | A-25 |

## 5. Responses

CR-4 applied to every pair of options each actor class has (form of holding, holding or consuming or giving, staying or leaving, now or later, accept or lobby, comply or misreport); CR-10a for the 14-month window; CR-8c for resources used up.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | households.taxed.listed_portfolios | reclassification (portfolios moved into controlled holding companies carried at cost) | increase | short (before 31 December 2027); medium | CR-4 (x: hold directly, y: holding company), CR-10a | A-2 |
| C-7 | households.near_line | reclassification (measured net worth brought or kept below M 10 million) | increase | short; medium; long | CR-4 (x: above the line, y: below it) | A-8 |
| C-8 | general_budget | tax_revenue_vs_static_projection (net wealth tax) | decrease | short; medium; long | CR-4, CR-12d | A-2 or A-8 or A-7 or A-3 or A-9 or A-19 |
| C-9 | households.taxed.with_heirs | resources_available_other_uses | decrease | short (2027); medium | CR-4 (x: bequest later, y: gift now), CR-10a, CR-8b | A-5, A-8 |
| C-10 | adult_children | resources_available_other_uses | increase | short; medium | CR-8b, CR-9 (gift) | A-5, A-8 |
| C-11 | general_budget | tax_revenue (gift and inheritance tax, gifts brought forward) | increase | short; medium | CR-10a, CR-8b | A-5, A-8 |
| C-12 | general_budget | tax_revenue (gift and inheritance tax, later bequests) | decrease | long | CR-10a | A-5, A-8 |
| C-13 | general_budget | tax_revenue (income and gains taxes) | decrease | short (2027 to 2028) | CR-4 (x: stay, y: leave), CR-10a, CR-8b | A-9, A-10 |
| C-14 | households.taxed.departing_after_2028 | resources_available_other_uses | decrease | medium; long | CR-1 op 3, CR-3c, CR-8b | A-26 |
| C-15 | households.taxed.would_leave_later | tax_revenue (income and gains taxes paid in Ostrevia by households that stay because of the exit charge) | increase | medium; long | CR-4 (x: leave and pay K3, y: stay) | A-11 |
| C-16 | general_budget | tax_revenue (exit charge) | increase | medium; long | CR-1 op 3, CR-8b | A-26 |
| C-17 | households.taxed | saving (in market-valued forms) | ambiguous | short; medium; long | CR-4 and its exception, CR-12b | A-7, A-6 |
| C-18 | households.taxed | consumption | ambiguous | short; medium; long | CR-4 and its exception, CR-12b | A-7, A-6, A-1 |
| C-19 | households.taxed | legal_breach (under-declared self-assessed property and art values) | increase | short; medium; long | CR-4 (x: declare fully, y: under-declare) | A-19 |
| C-20 | households.taxed | quantity_demanded (art and collectibles) | increase | short; medium | CR-4 (x: market-valued financial assets, y: self-valued art) | A-20 |
| C-21 | households.taxed.with_pension_room | saving (personal pension accounts) | U1-a: ambiguous; U1-b: increase | short; medium; long | CR-4 (x: taxed form, y: pension account), CR-12b | A-24 |
| C-22 | owners.unlisted_firms | reclassification (firms kept private or taken private to be valued at book) | increase | medium; long | CR-4 (x: list, y: stay private) | A-3 |
| C-23 | unlisted_firms | investment_target (expensed intangibles relative to capitalized assets) | increase | medium; long | CR-4 (x: capitalized investment, y: expensed intangibles) | A-4 |
| C-24 | unlisted_firms | saving (retained earnings of firms whose owners pay the tax from dividends) | decrease | short; medium; long | CR-4, CR-3c | A-17 |
| C-25 | general_budget | non_tax_receipts (penalties on understated tax) | increase | medium; long | CR-8b | A-N1, A-19 |
| C-26 | organized_interests | lobbying_effort (valuation rules, the U1 ruling, the threshold) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-21 |
| C-27 | unlisted_firms | capital_stock_target (unlisted firms) | ambiguous | long | CR-12b, CR-7a, CR-10b | A-17, A-7 |
| C-28 | intermediaries.advisers | quantity_traded (valuation, tax-planning and company-formation services) | increase | short; medium; long | CR-9, LW-10 | A-2 or A-8 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Effects on employees and suppliers of unlisted firms follow from C-27, which is ambiguous, and are not traced further (they would be kind 3 chains with no sign). Effects on Quellin are not traced: no case assumption says emigrants go there, and its 0.5% tax makes it a weaker destination than Valtria.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-29 | neighboring_jurisdictions.valtria_home_market (buyers) | price_paid (high-end homes in Valtria's border cities) | increase | short; medium | CR-9, CR-6 | Ostrevian residence across_border Valtrian housing | A-9, A-23, A-14 |
| C-30 | neighboring_jurisdictions.valtria_home_market (owners) | asset_value (high-end homes in Valtria's border cities) | increase | short; medium | CR-7c, CR-10c | across_border | A-9, A-23, A-14 |
| C-31 | neighboring_jurisdictions.valtria_home_market (builders) | investment_target (high-end homes in Valtria's border cities) | increase | medium; long | CR-7a, CR-4 (x: stay out, y: build) | input_to | A-9, A-23, A-15 |
| C-32 | owners.high_end_homes_ostrevia | asset_value (homes above M 3 million) | decrease | short (from announcement); medium | CR-9, CR-7c, CR-10c | taxed households' demand same_market high-end homes | A-13, A-29 |
| C-33 | buyers.high_end_homes_ostrevia.untaxed | quantity_traded (purchases of homes above M 3 million) | increase | short; medium | CR-4c, CR-9 | same_market_other_segment | A-13 |
| C-34 | builders.high_end_ostrevia | investment_target (homes above M 3 million) | decrease | medium; long | CR-9, LW-10, CR-7a | input_to | A-13 |
| C-35 | holders.listed_shares | price_paid (Ostrevian listed shares) | ambiguous | short; medium | CR-12b, CR-6, CR-9 | same market | A-16, A-3, A-N2 |
| C-36 | buyers.unlisted_firms | price_paid (sale value of unlisted firms) | ambiguous | medium; long | CR-12b, CR-7c | same market | A-18, A-7, A-17 |
| C-37 | sellers.art_collectibles | price_substitute (+), quantity_substitute (+) (art and collectibles) | at_least_one_increase | short; medium | CR-9, CR-6 (0.9: splitting a shift) | substitute (store of wealth) | A-20 |
| C-38 | pension_providers | quantity_traded (personal pension contributions) | U1-a: ambiguous; U1-b: increase | short; medium; long | CR-9 (contract) | contract | A-24 |
| C-39 | general_budget | tax_revenue (income and gains taxes) | ambiguous | medium; long | CR-12b | - | A-9, A-10, A-11, A-12 |
| C-40 | general_budget | tax_revenue (all receipts net of lost taxes and administration) | increase | medium; long | CR-8b, CR-12e | - | A-22 |
| C-41 | taxpayers, recipients_of_other_spending, future_taxpayers | resources_available_other_uses | at_least_one_increase | medium; long | CR-8b, CR-8d, CR-8 (0.7 general budget) | - | A-22 |
| C-42 | households.taxed | resources_available_other_uses (holding-company and advisory costs) | decrease | short; medium | CR-8c | - | A-2 or A-8 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| households.taxed, saving | fixed-target saving (CR-4 exception, A-6) | substitution to consumption, gifts and favored forms (A-7) | A-27 (p 0.45) is below the cut-off | ambiguous (C-17) |
| households.taxed, consumption | relatively cheaper than holding wealth (A-7) | tax paid; fixed-target saving (A-6) | None | ambiguous (C-18) |
| general_budget, tax_revenue (income and gains), short (2027 to 2028) | — (stayers matter only after 2028) | window departures (A-9, A-10) | — | decrease (C-13) |
| general_budget, tax_revenue (income and gains), medium; long | stayers because of the exit charge (A-11) | window and later departures (A-9, A-10); foreigners not moving in (A-12) | None | ambiguous (C-39) |
| general_budget, gift and inheritance tax, by window | gifts brought forward (short; medium) | bequests not made later (long) | Different windows, not combined (CR-12g) | increase (C-11); decrease (C-12) |
| general_budget, all receipts net | wealth tax, exit charge, penalties | lost income and gains taxes, administration | A-22 (p 0.7), empirical (CR-12e) | increase (C-40) |
| unlisted_firms, capital_stock_target | inflow into the favored form (A-7) | dividends drawn to pay the tax (A-17) | None | ambiguous (C-27) |
| holders.listed_shares, price_paid | take-private bids (A-3, A-N2) | taxed marginal holders sell (A-16) | None | ambiguous (C-35) |
| buyers.unlisted_firms, price_paid | favored form (A-7, A-18) | taxed at all; lower retained earnings (A-17) | None | ambiguous (C-36) |
| owners.high_end_homes_ostrevia, asset_value | — (under-declaration lowers the burden but cannot reverse it) | yearly charge on holding; departures add sellers | Response argument (CR-12e) | decrease (C-32) |
| Valtria high-end homes, price_paid, long | inflow | new building (A-15) | Response argument gives "not below the old level" only; with building able to expand fully in the long run, no sign | not recorded (see C-31) |

**Final check before the report (workflow).** (1) Uncombined chains: income and gains taxes were combined across the window and later chains (C-13, C-39); saving and consumption carry both the substitution and the fixed-target chain; listed-share and unlisted-firm prices carry both directions. (2) Group signs: art prices and quantities (C-37) and the gainers from net receipts (C-41) are groups. (3) Baseline: every sign is against Ostrevia without the Act; the revenue shortfall is signed against the static projection only in the variable built for it (C-8). (4) Worse off is not poorer: `resources_available_other_uses` is signed for those who keep paying the tax (C-1), pay the exit charge (C-14), give (C-9) or receive (C-10); not for households that respond by restructuring alone, beyond the costs used up (C-42). (5) Timing shifts: gifts (C-11, C-12) and departures (C-13, then C-39). (6) Both sides of every transfer: tax and budget (C-1, C-2), exit charge (C-14, C-16), gifts (C-9, C-10, C-11), net receipts and their recipients (C-40, C-41). (7) Every class and rule: CR-7c applied to Ostrevian and Valtrian homes, listed shares and unlisted firms; CR-6 to the Valtrian housing market and art; enforcement costs and penalties (C-3, C-25). (8) Unstated premises: A-N1 and A-N2 added. (9) No patterns cited.

## 8. Time structure

- **Announcement window (1 November 2026 to 31 December 2027).** The tax was announced 14 months before the first valuation date and was not expected before (A-29). In the window: households at the margin of leaving leave before the exit charge starts on 1 January 2028 (CR-10a; C-13; the Agency projects about 300 additional departures); gifts are brought forward (C-9, C-11); portfolios are moved into holding companies (C-6); measured wealth is brought below the line before the first valuation date (C-7). Home values and other asset prices move from the announcement (CR-7c; C-32, C-30). The emigration count itself has no variable in the ontology (see Gaps); it is signed through its effects on receipts (C-13, C-39) and on Valtrian housing (C-29).
- **After 2028.** The exit charge makes leaving costly for liable households: some who would have left stay (C-15), and those who leave anyway pay it (C-14, C-16). The charge applies to members of households liable on any of the three valuation dates before departure, so a household that falls below the line can leave free of the charge only three years later; that lengthens the effect of C-7 on later departures (a path note: no sign is claimed on the timing of departures, for lack of a variable).
- **Gifts and bequests.** Gifts made now replace bequests later (A-5), so gift tax receipts rise early and inheritance tax receipts fall later (C-11, C-12).
- **Durable stocks.** High-end homes in Ostrevia and Valtria change only through building (CR-10b): Valtrian prices rise in the short and medium term while building takes two to three years (A-14), and building responds later (C-31); Ostrevian high-end building falls gradually (C-34). Firms' capital (C-27) responds slowly.
- **Fixed threshold.** The threshold is fixed in marks, so as nominal wealth grows, more households cross it each year and the tax binds on more of their wealth (arithmetic on the policy text). Households near the line (C-7) are a growing class.
- Not a repeal: no metamorphic check is needed.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-3 | officials.tax_agency | enforcement_cost | increase | About M 45 million a year of general-budget resources | CR-1 op 4, CR-8c |
| C-4 | households.taxed, households.near_line | compliance_cost | increase | Time and fees spent on valuations and returns | CR-1 op 3, CR-8c |
| C-26 | organized_interests | lobbying_effort (valuation rules, the U1 ruling, the threshold) | increase | Resources spent seeking rulings and changes | CR-4 (x: accept, y: lobby), CR-8c |
| C-42 | households.taxed | resources_available_other_uses (holding-company and advisory costs) | decrease | Formation costs, accounts and fees that serve only to reduce the tax | CR-8c |

CR-8's symmetry: the tax paid (C-1) is received by the budget (C-2); the exit charge paid (C-14) is received (C-16); gifts given (C-9) are received by children (C-10), with the tax brought forward (C-11); net receipts (C-40) are matched by gains to taxpayers or recipients of other spending (C-41). Valuation, compliance, holding-company, advisory and lobbying costs are used up (C-3, C-4, C-42, C-26).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Most taxed households file and pay. | enforcement | 0.9 | Self-assessment with audits of about 10% of returns; penalties of 50%; information exchange with 110 countries. | These consequences fail or lose this chain: C-1, C-2, C-18. |
| A-2 | A portfolio contributed to a controlled company is not treated as sold, and the company may carry it at cost; for large portfolios the cost of a holding company is below the tax saved. | other | 0.75 | Tax Code art. 44; small-company accounting rules; formation costs of a few thousand marks. | These consequences fail or lose this chain: C-6, C-8, C-28, C-42. |
| A-3 | Some owners close to a listing decision keep their firms private, or take listed firms private, to be taxed on book value. | other | 0.6 | Listing costs and benefits are close for mid-sized family firms; the gap between 1% of market and about 0.45% of market. | These consequences fail or lose this chain: C-8, C-22, C-35. |
| A-4 | Some owners of unlisted firms can shift investment toward expensed intangibles. | other | 0.55 | Firms already choose between capital and research, training and marketing; accounting rules expense these. | These consequences fail or lose this chain: C-23. |
| A-5 | Some taxed households have adult children and planned to leave them wealth, so that a gift mainly brings forward a tax a bequest would have paid. | other | 0.75 | Most households above M 10 million are headed by people over 55; gifts and bequests are taxed alike. | These consequences fail or lose this chain: C-9, C-10, C-11, C-12. |
| A-6 | A material part of taxed households save toward a fixed sum (a bequest of a set size, a target income). | other | 0.6 | Surveys of saving motives among the wealthy. | These consequences fail or lose this chain: C-17, C-18. |
| A-7 | Taxed households have untaxed or lightly taxed alternatives to saving in market-valued forms: the formula-favored forms, gifts, consumption. | substitutability | 0.85 | K2's valuation rules; art. 44; gift rules. | These consequences fail or lose this chain: C-8, C-17, C-18, C-27, C-36. |
| A-8 | Some households near the line can bring their measured net worth below it, at a cost below the kink's tax or, for those that may leave, the exit charge. | other | 0.75 | Self-assessed property values; gifts; holding companies. | These consequences fail or lose this chain: C-7, C-8, C-9, C-10, C-11, C-12, C-28, C-42. |
| A-9 | Some taxed households are at the margin of leaving Ostrevia. | mobility | 0.7 | Valtria: two hours away, same language, free movement, no wealth tax; 120 such households leave each year without the tax. | These consequences fail or lose this chain: C-8, C-13, C-29, C-30, C-31, C-39. |
| A-10 | Households that left in the window would otherwise have stayed resident and paid income and gains taxes for some years. | counterfactual_trend | 0.8 | Departures before the announcement ran at about 120 a year. | These consequences fail or lose this chain: C-13, C-39. |
| A-11 | Some liable households that would have left after 2028 for other reasons stay because of the exit charge. | mobility | 0.6 | Retirement abroad is common among the wealthy; the charge is about M 1.7 million on typical gains. | These consequences fail or lose this chain: C-15, C-39. |
| A-12 | Some wealthy foreigners would otherwise have moved to Ostrevia. | mobility | 0.6 | Recent arrivals of executives and investors. | These consequences fail or lose this chain: C-39. |
| A-13 | Taxed households are a material share of buyers of homes above M 3 million. | other | 0.7 | About 45% by value of recent purchases. | These consequences fail or lose this chain: C-32, C-33, C-34. |
| A-14 | High-end building in Valtria's border cities expands only gradually (planning and building times). | durability | 0.7 | Valtrian permit and building times of two to three years. | These consequences fail or lose this chain: C-29, C-30. |
| A-15 | The cost per unit of high-end building in Valtria does not fall as more is built. | other | 0.7 | Building costs set region-wide; no scale economies in one-off homes. | These consequences fail or lose this chain: C-31. |
| A-16 | Taxed households are among the marginal holders of Ostrevian listed shares. | other | 0.6 | They hold about 8% of the market. | These consequences fail or lose this chain: C-35. |
| A-17 | Some owners of unlisted firms pay the tax from dividends, and their firms cannot replace the retained earnings by borrowing on the same terms. | other | 0.55 | Family firms' reliance on retained earnings; bank lending terms. | These consequences fail or lose this chain: C-24, C-27, C-36. |
| A-18 | Taxed households are among the buyers who set the sale value of some unlisted firms. | other | 0.55 | Families buy about a third of unlisted firms by value. | These consequences fail or lose this chain: C-36. |
| A-19 | Audits of self-assessed property and art values are infrequent, and some under-declaration is not detected. | enforcement | 0.65 | Audit plan of about 10%; valuation disputes are costly. | These consequences fail or lose this chain: C-8, C-19, C-25. |
| A-20 | Some taxed households move wealth into art and collectibles. | substitutability | 0.55 | Insurance values are not binding for tax; experience of other wealth taxes. | These consequences fail or lose this chain: C-20, C-37. |
| A-21 | Family-business federations, advisers, pension providers and campaigners can organize at a cost below their stakes. | other | 0.85 | Existing associations; the hearings on the bill. | These consequences fail or lose this chain: C-26. |
| A-22 | The Act's net receipts to the general budget are positive: the wealth tax and exit charge exceed lost income and gains taxes and the Agency's cost. | revenue_use | 0.7 | Fiscal note M 1.1 billion; about 300 extra departures (about M 0.27 billion a year of lost taxes); M 45 million administration. | These consequences fail or lose this chain: C-40, C-41. |
| A-23 | Emigrants buy high-end homes in Valtria's border cities, where supply cannot expand at once. | durability | 0.6 | Where recent emigrants have settled; Valtrian building times. | These consequences fail or lose this chain: C-29, C-30, C-31. |
| A-24 | Under U1-b, some taxed households have room within the M 300,000 yearly contribution limit and accept the lock until 62. | other | 0.8 | Most such households contribute less than the limit now. | These consequences fail or lose this chain: C-21, C-38. |
| A-25 | Under U1-a, some households are carried over the line by their pension rights. | other | 0.8 | Executives' defined-benefit rights of M 2 to 6 million. | These consequences fail or lose this chain: C-5. |
| A-26 | Some liable households leave on or after 1 January 2028. | mobility | 0.9 | About 120 departures a year without the tax, for reasons other than tax. | These consequences fail or lose this chain: C-14, C-16. |
| A-27 | For taxed households as a group, the substitution response outweighs the response of fixed-target savers. | other | 0.45 | No direct evidence. Below the cut-off. | No reported consequence rests on it (see Not reported). |
| A-28 | Emigrants move their firms' management and operations abroad. | mobility | 0.35 | Most family firms' customers and staff are in Ostrevia. Below the cut-off. | No reported consequence rests on it (see Not reported). |
| A-29 | The tax was not expected before the announcement of 1 November 2026. | expectations | 0.6 | It was in the governing parties' manifestos, but with no rate, threshold or date. | These consequences fail or lose this chain: C-32. |
| A-N1 | Audits detect some understatement, and penalties are assessed on it. | enforcement | 0.7 | NEW. Audits of about 10% of returns; listed and bank assets reported through information exchange; A-19 says only that some under-declaration is not detected. | These consequences fail or lose this chain: C-25. |
| A-N2 | Take-private bids for listed firms are made at prices above the prevailing market price of their shares. | other | 0.7 | NEW. Bids must induce outside holders (55% foreign, 30% institutions) to sell; usual practice of bid premiums. | These consequences fail or lose this chain: C-35. |

**Not reported** (an assumption below 0.5):
- Taxed households as a group save less (substitution dominates fixed-target saving): needs A-27 (p 0.45). Under CR-12 0.8, kind (2), C-17 and C-18 are therefore `ambiguous`, not signed.
- Emigrants move their firms' management and operations abroad, lowering employment and profit taxes in Ostrevia (CR-4, x: run the firm here, y: abroad; CR-9): needs A-28 (p 0.35). The chain would add a further negative item to C-39 and C-40.

**Not recorded for lack of a premise.** Effects of capital flows on interest rates or the mark (no premise on size; Ostrevian taxed households hold about 8% of listed shares, and foreign investors are the main holders); employees of unlisted firms (C-27 is ambiguous).

## 11. Report

**The policy:** From the valuation date of 31 December 2027, households resident in Ostrevia pay 1% a year on net worth above M 10 million, on worldwide assets. Listed securities are valued at market, unlisted shares at book equity, and property and art at values the taxpayer assesses. Persons who leave from 1 January 2028, if their household was liable on any of the three previous valuation dates, pay 28% capital gains tax on unrealized gains. Revenue goes to the general budget. It is unclear whether pension rights count (U1).

**Visible consequences:** About 11,000 households pay the tax (C-1), and the budget collects it (C-2).

**Invisible consequences:**
- *Avoidance:* portfolios move into holding companies carried at cost (C-6); households near the line keep measured wealth below it (C-7); some under-declare property and art (C-19) and buy more art (C-20); under U1-b, households put more into pension accounts (C-21, C-38). Firms stay or go private (C-22) and shift investment toward expensed intangibles (C-23). Collections fall short of the static projection (C-8). The resources spent on all this are used up (C-4, C-42), and advisers sell more services (C-28).
- *Gifts:* the wealthy give to adult children sooner (C-9, C-10). Gift tax receipts rise now and inheritance tax receipts fall later (C-11, C-12).
- *Departures:* households at the margin leave before the exit charge starts. That lowers income and gains tax receipts in 2027 to 2028 (C-13) and raises the price and value of high-end homes in Valtria's border cities (C-29, C-30), where building expands later (C-31). After 2028 the exit charge is paid by those who leave anyway (C-14, C-16), and some who would have left stay (C-15).
- *Ostrevian property:* homes above M 3 million lose value from the announcement (C-32). Foreign and other untaxed buyers buy more of them (C-33), and less of that kind of home is built (C-34).
- *Other effects:* some unlisted firms retain less because owners draw dividends to pay the tax (C-24); art prices or quantities rise (C-37). The Agency spends M 45 million a year (C-3) and collects penalties (C-25). Lobbying over valuation rules and the pension ruling increases (C-26). Net receipts are positive (C-40), so taxpayers or recipients of other spending gain as a group (C-41). Under U1-a, executives with defined-benefit rights pay from other means (C-5).

**Ambiguous effects:** For taxed households, saving and consumption are ambiguous (C-17, C-18): the tax pushes them away from saving, while saving toward a fixed sum pushes them toward it. Also ambiguous: income and gains tax receipts after 2028 (C-39), with departures and missing arrivals pushing them down and households held by the exit charge pushing them up; the capital stock of unlisted firms (C-27), with tax-funding dividends pushing it down and inflows into the book-valued form pushing it up; listed share prices (C-35), with taxed holders selling and take-private bids pushing opposite ways; and the sale value of unlisted firms (C-36).

**Key conditions:** Most households file and pay (A-1, 0.9); holding companies pay for large portfolios (A-2, 0.75); households near the line can get below it (A-8, 0.75); some are at the margin of leaving (A-9, 0.7); net receipts are positive (A-22, 0.7); the tax was not expected before November 2026 (A-29, 0.6). Two premises were added: audits detect some understatement (A-N1, 0.7), and take-private bids carry a premium (A-N2, 0.7).

**What this analysis cannot say:** How much the tax will raise, how many households will leave, or whether saving and investment in Ostrevia rise or fall. It does not weigh the gains to other taxpayers against the losses to taxed households, property owners and others, or say whether the policy is good. Effects through emigrants moving their firms abroad are below the cut-off (A-28).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | households.taxed | resources_available_other_uses | decrease | short; medium; long | visible | B | CR-1 (op 4: K1 takes 1% of measured net worth above M 10 million each year from households that remain above the line); CR-3c and CR-8b (what is paid is not available for other uses); signed for those who keep paying (CR-3 note), A-1 | A-1 |
| C-2 | general_budget | tax_revenue (net wealth tax) | increase | short; medium; long | visible | B | CR-1 (op 4) and CR-8b (the payments are receipts of the general budget), against a counterfactual of none; A-1 | A-1 |
| C-3 | officials.tax_agency | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 4: about M 45 million a year for the valuation unit); CR-8c | none |
| C-4 | households.taxed, households.near_line | compliance_cost | increase | short; medium; long | invisible | A | CR-1 (op 3: returns, self-assessed valuations of property and art, audit responses); CR-8c; households near the line must value their assets to know whether they are liable | none |
| C-5 | households.taxed.db_pension_holders | resources_available_other_uses | U1-a: decrease; U1-b: no_change | short; medium; long | invisible | B | U1-a: CR-1 (op 4: rights count at transfer value; some households are carried over the line or further above it by them, A-25), and since the rights cannot be assigned or borrowed against, the tax is paid from other means (CR-3c). U1-b: rights valued at nil, so K1 performs no operation on them | A-25 |
| C-6 | households.taxed.listed_portfolios | reclassification (portfolios moved into controlled holding companies carried at cost) | increase | short (before 31 December 2027); medium | invisible | B | CR-4 (x: hold the portfolio directly, taxed at market; y: move it into a controlled company under art. 44, carried at cost, so a M 10 million portfolio bought for M 4 million is taxed on M 4 million; the cost of y is below the tax saved for large portfolios, A-2); CR-10a (done before the first valuation date) | A-2 |
| C-7 | households.near_line | reclassification (measured net worth brought or kept below M 10 million) | increase | short; medium; long | invisible | B | CR-4 (x: measured net worth above the line; y: below it, through gifts, holding companies, or lower self-assessed values; the kink makes the tax saved per mark constant above the line, so households for whom the cost of y is below the tax switch, A-8) | A-8 |
| C-8 | general_budget | tax_revenue_vs_static_projection (net wealth tax) | decrease | short; medium; long | invisible | B | CR-4 applied to every pair of forms (CR-12d: independent chains, any one suffices): holding companies (C-6, A-2), bringing measured wealth below the line (C-7, A-8), moving into formula-favored forms (C-17, A-7; C-20, A-20), firms kept private (C-22, A-3), departures before the first valuation date (A-9), undetected under-declaration (C-19, A-19). None raises the base above the static projection (CR-4a: no one moves into a more heavily taxed form because of the Act) | A-2 or A-8 or A-7 or A-3 or A-9 or A-19 |
| C-9 | households.taxed.with_heirs | resources_available_other_uses | decrease | short (2027); medium | invisible | B | CR-4 (x: hold and bequeath later; y: give to adult children now, paying the gift tax a bequest would have paid, and avoid K1 on the amount given; y made better for those whose plans already included the transfer, A-5, and for whom it brings wealth below or further toward the line, A-8); CR-10a (gifts before the first valuation date); CR-8b (what is given leaves the giver) | A-5, A-8 |
| C-10 | adult_children | resources_available_other_uses | increase | short; medium | invisible | B | CR-8b (the gift adds to the recipient what it takes from the giver, less the tax); CR-9 (relation: gift) | A-5, A-8 |
| C-11 | general_budget | tax_revenue (gift and inheritance tax, gifts brought forward) | increase | short; medium | invisible | B | CR-10a (a transfer that would have been taxed as a bequest later is taxed as a gift now; same 20% rate); signed per window (02_ontology 2.5, timing shifts) | A-5, A-8 |
| C-12 | general_budget | tax_revenue (gift and inheritance tax, later bequests) | decrease | long | invisible | B | CR-10a (the part given now is not bequeathed later, so later inheritance tax on it is not paid); per window, against the counterfactual | A-5, A-8 |
| C-13 | general_budget | tax_revenue (income and gains taxes) | decrease | short (2027 to 2028) | invisible | B | CR-4 (x: stay and pay K1 from 2027 and K3 on any later departure; y: leave before 1 January 2028, free of both; y made better for households at the margin, A-9; CR-10a: the dated charge pulls departures into the window); A-10: they would otherwise have stayed and paid about M 0.9 million a year each. The stayers of C-15 affect only later years | A-9, A-10 |
| C-14 | households.taxed.departing_after_2028 | resources_available_other_uses | decrease | medium; long | invisible | B | CR-1 (op 3: K3 takes 28% of unrealized gains from households that leave, which on the counterfactual path would never have been taxed if held to death); CR-3c; A-26: some liable households leave for other reasons | A-26 |
| C-15 | households.taxed.would_leave_later | tax_revenue (income and gains taxes paid in Ostrevia by households that stay because of the exit charge) | increase | medium; long | invisible | B | CR-4 (x: leave after 2028, paying about M 1.7 million on typical gains; y: stay; y made relatively better, A-11); they pay income and gains taxes that they would have paid abroad (CR-8b) | A-11 |
| C-16 | general_budget | tax_revenue (exit charge) | increase | medium; long | invisible | B | CR-8b (C-14's payments are received by the budget, in five installments with interest), against a counterfactual of none | A-26 |
| C-17 | households.taxed | saving (in market-valued forms) | ambiguous | short; medium; long | invisible | B | CR-12b, kind (2) chain: (-) CR-4 (x: save in market-valued forms taxed at 1% a year; y: formula-favored forms, gifts or consumption, open by A-7); (+) CR-4 exception (a lower return on saving toward a fixed sum calls for more saving to reach it, A-6). The premise that the substitution response dominates (A-27) has p 0.45, below the cut-off | A-7, A-6 |
| C-18 | households.taxed | consumption | ambiguous | short; medium; long | invisible | B | CR-12b: (+) consumption becomes relatively cheaper than holding wealth (A-7); (-) the tax paid (C-1) and fixed-target saving (A-6) reduce what is left to consume. No dominance premise above the cut-off (A-27, p 0.45) | A-7, A-6, A-1 |
| C-19 | households.taxed | legal_breach (under-declared self-assessed property and art values) | increase | short; medium; long | invisible | B | CR-4 (x: declare market value; y: declare less; the expected penalty, 50% of the tax understated times a low chance of detection, A-19, is below the tax saved for some); against a counterfactual of no such declaration | A-19 |
| C-20 | households.taxed | quantity_demanded (art and collectibles) | increase | short; medium | invisible | B | CR-4 (x: hold listed shares or cash taxed at market; y: art and collectibles, valued by the holder and rarely audited; y made relatively better, A-20, A-19) | A-20 |
| C-21 | households.taxed.with_pension_room | saving (personal pension accounts) | U1-a: ambiguous; U1-b: increase | short; medium; long | invisible | B | U1-b: CR-4 (x: hold savings in a taxed form; y: contribute to a pension account valued at nil, accepting the lock until 62; y made better, A-24). U1-a: pension accounts are taxed like other forms, so only the general saving chains of C-17 apply (kind 3: ambiguous) | A-24 |
| C-22 | owners.unlisted_firms | reclassification (firms kept private or taken private to be valued at book) | increase | medium; long | invisible | B | CR-4 (x: list, taxed at 1% of market; y: stay private or delist, taxed at about 0.45% of market; owners for whom listing ranked narrowly above staying private switch, A-3) | A-3 |
| C-23 | unlisted_firms | investment_target (expensed intangibles relative to capitalized assets) | increase | medium; long | invisible | B | CR-4 (x: invest in assets that raise book equity, and so the owner's tax; y: research, training and marketing, expensed and so not in book equity; y made relatively better, A-4) | A-4 |
| C-24 | unlisted_firms | saving (retained earnings of firms whose owners pay the tax from dividends) | decrease | short; medium; long | invisible | B | CR-4 for owners (x: leave earnings in the firm; y: pay a dividend to fund K1; owners without other liquid means choose y, A-17); CR-8a (earnings paid out are withdrawn from the firm) | A-17 |
| C-25 | general_budget | non_tax_receipts (penalties on understated tax) | increase | medium; long | invisible | B | CR-8b (penalties of 50% of the tax understated, on understatement found in audits of about 10% of returns, A-N1); against a counterfactual of none | A-N1, A-19 |
| C-26 | organized_interests | lobbying_effort (valuation rules, the U1 ruling, the threshold) | increase | short; medium; long | invisible | B | CR-4 (x: accept; y: lobby; the U1 ruling and the valuation rules are questions only the Act creates, so the counterfactual contest over them is none; the tax itself was contested on the counterfactual path too, being in manifestos, so lobbying over whether to have it is not signed, CR-4 1.0 note); CR-8c | A-21 |
| C-27 | unlisted_firms | capital_stock_target (unlisted firms) | ambiguous | long | invisible | B | CR-12b: (-) retained earnings paid out to fund the tax and not replaced on the same terms (C-24, A-17); (+) CR-7a: wealth moves into unlisted firms valued at book, about 0.45% of market against 1% elsewhere (A-7). No dominance premise | A-17, A-7 |
| C-28 | intermediaries.advisers | quantity_traded (valuation, tax-planning and company-formation services) | increase | short; medium; long | invisible | B | CR-9 (relation: these services are complements of compliance, C-4, and of the responses in C-6 and C-7) | A-2 or A-8 |
| C-29 | neighboring_jurisdictions.valtria_home_market (buyers) | price_paid (high-end homes in Valtria's border cities) | increase | short; medium | invisible | B | CR-9 (relation: across_border; emigrants, C-13, buy homes there, A-23); CR-6 (more buyers at each price while building takes two to three years, A-14, so the price moves up: the supply side cannot expand in the period, CR-6 0.9 note) | A-9, A-23, A-14 |
| C-30 | neighboring_jurisdictions.valtria_home_market (owners) | asset_value (high-end homes in Valtria's border cities) | increase | short; medium | invisible | B | CR-10c and CR-7c (the higher expected rents and sale prices, C-29, are captured by owners when the inflow becomes expected, from the announcement, A-29) | A-9, A-23, A-14 |
| C-31 | neighboring_jurisdictions.valtria_home_market (builders) | investment_target (high-end homes in Valtria's border cities) | increase | medium; long | invisible | B | CR-7a (building moves toward the higher yield, C-29); A-15: costs do not fall as more is built. By the response argument (CR-12e, 1.0 note), new building cannot push the price below its old level; with constant cost (A-15) and building that can fully expand in the long run, no long-run price sign is given | A-9, A-23, A-15 |
| C-32 | owners.high_end_homes_ostrevia | asset_value (homes above M 3 million) | decrease | short (from announcement); medium | invisible | B | CR-9 (relation: taxed households are about 45% by value of buyers of such homes, A-13; K1 attaches a yearly charge to holding them and departures add sellers); CR-10c and CR-7c (the fall in expected value is borne by owners when the tax becomes expected, A-29); self-assessed values (A-19) lower the burden but cannot reverse its direction (CR-12e, response argument) | A-13, A-29 |
| C-33 | buyers.high_end_homes_ostrevia.untaxed | quantity_traded (purchases of homes above M 3 million) | increase | short; medium | invisible | B | CR-9 (relation: same market; the price falls, C-32); CR-4c (at a lower price foreign and other untaxed buyers buy more) | A-13 |
| C-34 | builders.high_end_ostrevia | investment_target (homes above M 3 million) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: building input_to the stock of such homes; their value falls, C-32); CR-7a (building moves to other uses); CR-10b (the stock responds only through new building) | A-13 |
| C-35 | holders.listed_shares | price_paid (Ostrevian listed shares) | ambiguous | short; medium | invisible | B | CR-12b, kind (2): (-) CR-6 and CR-9: taxed households are among the marginal holders (A-16) and hold less directly, so the price moves down (signed though small, CR-6 1.0 note); holding companies (A-2) keep part of the demand but cannot reverse the direction; (+) take-private bids by owners avoiding listed valuation (C-22, A-3) are made above market (A-N2). No dominance premise | A-16, A-3, A-N2 |
| C-36 | buyers.unlisted_firms | price_paid (sale value of unlisted firms) | ambiguous | medium; long | invisible | B | CR-12b: (+) unlisted firms are a formula-favored form, so taxed households bid more for them (A-7, A-18); (-) K1 taxes taxed buyers' holdings of them at all, at about 0.45% of market, and lower retained earnings lower expected yields (A-17); CR-7c. No dominance premise | A-18, A-7, A-17 |
| C-37 | sellers.art_collectibles | price_substitute (+), quantity_substitute (+) (art and collectibles) | at_least_one_increase | short; medium | invisible | B | CR-9 (relation: art as a substitute store of wealth, C-20); CR-6 0.9 note (the shift in demand gives the direction; how it divides between price and quantity needs a premise on supply, which the case lacks, so a group) | A-20 |
| C-38 | pension_providers | quantity_traded (personal pension contributions) | U1-a: ambiguous; U1-b: increase | short; medium; long | invisible | B | CR-9 (relation: pension contract; C-21) | A-24 |
| C-39 | general_budget | tax_revenue (income and gains taxes) | ambiguous | medium; long | invisible | B | CR-12b: (-) households that left in the window (C-13, A-9, A-10) and later tax-driven departures (A-9); (-) wealthy foreigners who do not move in (CR-4, x: move in, y: stay away; A-12); (+) households that stay because of the exit charge (C-15, A-11). No dominance premise | A-9, A-10, A-11, A-12 |
| C-40 | general_budget | tax_revenue (all receipts net of lost taxes and administration) | increase | medium; long | invisible | B | CR-12e: empirical dominance premise A-22 (wealth tax and exit charge, C-2, C-16, exceed lost income and gains taxes, C-39, and the Agency's cost, C-3) | A-22 |
| C-41 | taxpayers, recipients_of_other_spending, future_taxpayers | resources_available_other_uses | at_least_one_increase | medium; long | invisible | B | CR-8b and CR-8d (net receipts, C-40, are paid into the general budget with no earmark, so other taxes are lower, other spending higher, or borrowing lower; who gains is not named: a group) | A-22 |
| C-42 | households.taxed | resources_available_other_uses (holding-company and advisory costs) | decrease | short; medium | invisible | B | CR-8c (company formation, accounts and advice for C-6 and C-7 are used up); listed in section 9 | A-2 or A-8 |

## Gaps found

**(a) Steps no core rule covers.**
- None. Every step was derived from CR-1 to CR-12, LW-10 and arithmetic on the record. The choice of residence is CR-4 (x: stay, y: leave), and its timing is CR-10a.

**(b) Core-rule wording that was hard to apply.**
- CR-1 and the kink: K1 is operation 4 for a household whose measured wealth does not respond, and operation 3 for one that can change its measured wealth, its form of holding or its residence. The 0.9 note on ranges ("op 3 below the cap, op 4 above") does not fit a burden that is op 3 and op 4 at once for the same household. It was recorded as both.
- CR-4's exception (a lower return on saving toward a fixed sum) gives a kind (2) opposing chain for saving. The rule does not say whether the exception also bears on the choice between forms (it does not, since the exception concerns total means, not relative yields), so it was applied to saving and consumption only.
- CR-12e's response argument (1.0 note) for Valtrian housing: with constant cost (A-15), the argument shows only that the price does not fall below its old level. No long-run sign follows, and the rule does not say whether to record "no long-run sign" as a consequence; it was recorded as a note under C-31 and in section 7.
- CR-4 1.0 note on lobbying: the tax itself was contested on the counterfactual path (manifestos), but its valuation rules and U1 were not. The note does not say how to split lobbying on one Act into questions contested and not contested on the counterfactual path; only the latter were signed (C-26).
- CR-10a with a dated charge on an option (K3): departures are pulled into the window and held back after it. This is a timing shift by the ontology's definition, but without a variable for departures it could only be signed through receipts.

**(c) Vocabulary missing from the ontology.**
- No variable for changes of residence (emigration and immigration counts). `job_changes` covers only moves tied to jobs. Departures were signed through `tax_revenue` (C-13, C-39) and Valtrian housing (C-29).
- No variable for gifts and bequests as flows. `resources_available_other_uses` (giver, recipient) and `tax_revenue` were used.
- No variable for listing status or the number of listed firms; `reclassification` was used (C-22).
- No variable for the portfolio mix (share of wealth in each form); `reclassification` and `quantity_demanded` were used.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on most of the Ostrevian case. Taxed households pay and the budget collects. Revenue falls short of the static projection through any of several responses. Portfolios move into holding companies carried at cost, firms stay private, investment inside them shifts toward expensed intangibles, and under U1-b savings move into pension accounts. Gifts to adult children are brought forward, and households near the line keep measured wealth below it. Departures rise in the window before the exit charge, the income and gains taxes of those who leave are lost, and liable households that leave later pay the charge. Some under-declare and buy art. High-end homes in Valtria's border cities rise in value. Listed share prices and the sale value of unlisted firms are `ambiguous`, compliance and enforcement costs rise, lobbying on the Act's own questions rises, and net receipts are positive on A-22. There are three S rows. The main one is the value of Ostrevian high-end homes, where the pattern version reports that SB-4, applied as written, gave `decrease` and was overridden to `ambiguous`. The core version, using CR-7c without SB-4, reached `decrease` (C-32). Checked against the core rules, the core version is wrong and the pattern version's override stands. The tax falls on most of what a taxed buyer would hold instead of a home, and self-assessed home values draw wealth into homes from cash and listed shares. That is a chain driven by the tax on those other forms, a second change that CR-12e's response argument does not cover (0.8 note). The core version's derivation repeats SB-4's error from CR-7c itself, which supports the pattern version's request for a note under CR-7c. The second S row is capital in unlisted firms, where the core's opposing chain does not hold. The third, saving in taxed forms, is a judgment on how far TX-6's firm clause reaches. The core version adds gift and inheritance tax receipts by window, penalties, Valtrian building and pension providers' sales. The pattern version adds gifts after 2028, total saving, arrivals, the pension valuation cost and the capital stock.

Counts: M 20, V 8, S 3, OP 9, OC 5.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-2 | M | | |
| C-2 | C-1 | M | | |
| C-3 | C-8 | M | | The core lists more independent chains (CR-12d). |
| C-4 | C-6 | M | | |
| C-5 | C-22 | M | | |
| C-6 | C-23 | V | | `reclassification` against `investment_target` (expensed relative to capitalized). Same premise A-4. |
| C-7 | C-21 | V | | `reclassification` into pension accounts (U1-a `no_change`, U1-b `increase`) against `saving` in pension accounts (U1-a `ambiguous`, U1-b `increase`). Under U1-a no line is drawn, so the move caused by the formula is nil, while saving in the accounts follows total saving. Both hold on their own variables. |
| C-8 | C-9, C-10, C-11 | V | | The pattern records gifts as `reclassification` in the window. The core records the giver's means (C-9), the recipient's (C-10) and the gift tax brought forward (C-11). |
| C-9 | none | OC | E | Gifts from 2028 `ambiguous` (later splitting against gifts pulled into the window). The core version did not record gifts after the window. It also signs gift-tax receipts `increase` into the medium term (C-11), which ignores the pulled-forward chain this row combines. Core-version omission. Nothing scorable lost on this row itself. |
| C-10 | C-7 | M | | The core derives only the kink chain; it misses the notch, where the exit charge makes staying below the line worth all of a prospective leaver's gains. Same sign. |
| C-11 | C-17 | S | J | Saving in taxed, market-valued forms: pattern `decrease` (TX-6's firm clause with A-7), core `ambiguous` (CR-4's exception with A-6 against substitution, A-27 below the cut-off). The pattern's sign holds if fixed-target savers place their added saving in the untaxed or lightly taxed forms. Here those forms are capped (pension contributions), costly (holding companies, gift tax) or only partly favored, so CR-4's exception can reach the taxed forms. The core's gap note says the exception "concerns total means, not relative yields", which contradicts its own use of it in C-17. Both signs are defensible; neither version states the premise that decides it. |
| C-12 | none | OC | E | Total saving `ambiguous`. The core has no total-saving key; its total-saving chains appear under C-17's form-specific label. Core-version omission. Nothing scorable lost. |
| C-13 | C-13 | V | | Departures in the window: the pattern signs them as `turnover`; the core, having no residence variable, signs their effect on income and gains tax receipts (C-13) and on Valtrian housing (C-29). |
| C-14 | C-15, C-39 | V | | Departures from 2028 `ambiguous` (pattern, `turnover`) against the core's receipts: stayers held by the exit charge (C-15, an item) and income and gains taxes overall (C-39, `ambiguous`). Same chains. |
| C-15 | none | OC | E | Fewer wealthy foreigners arrive (`turnover` decrease; CR-4; A-12). The core uses A-12 only as a chain inside C-39. A missing residence variable does not excuse leaving the consequence unrecorded; the pattern recorded it as `turnover`. Core-version omission. |
| C-16 | C-19 | M | | The core omits undeclared foreign accounts. |
| C-17 | C-20 | V | | `quantity_substitute` against `quantity_demanded`. |
| C-18 | C-26 | M | | Both sign only the questions the Act creates, against the counterfactual contest. |
| C-19 | C-5 | M | | |
| C-20 | none | OC | E | Valuing pension rights each year, U1-a `increase`, U1-b `no_change`, Tier A (CR-8c). The core's C-4 covers compliance in general but not this cost per reading. Core-version omission. |
| C-21 | C-32 | S | E | Ostrevian high-end homes: pattern `ambiguous`, core `decrease`. By CR-7c the price adjusts until a buyer expects to earn on the home what it could earn elsewhere. For a taxed buyer, cash, bonds and listed shares held directly bear the same 1%, so against them the home loses nothing. Against the formula-favored forms and consumption it loses, and departures add sellers (−). Self-assessed values, rarely audited (A-19), make the home bear less per mark than cash or listed shares, so wealth moves from those into homes (+). The core dismissed the (+) chain by the response argument ("lowers the burden but cannot reverse its direction"). But that chain is not a response to the burden on homes. It is driven by the tax on cash and listed shares, a second change the policy causes, which CR-12e's 0.8 note excludes. Without a dominance premise the sign is `ambiguous`. Core-version error. It is the error the pattern version attributes to SB-4, here reached from CR-7c directly. |
| C-22 | C-30 | M | | Medium run. The pattern uses the response argument with A-15 and A-14; the core has the price from A-14 (C-29) and owners' values (C-30). |
| C-23 | C-35 | M | | Both `ambiguous`, by different (+) chains. The pattern's (+) chain is shares held through holding companies at cost, against bonds and cash. The core's is take-private bids at a premium (A-N2). The core dismissed the holding-company chain with the same misuse of the response argument as in C-32; the sign is unaffected. |
| C-24 | C-36 | M | | |
| C-25 | C-24, C-27 | S | E | Pattern: booked investment in taxed households' unlisted firms `decrease`, medium (A-4 or A-17). Core: the dividend chain as its own item (C-24, retained earnings `decrease`) and the firms' capital stock `ambiguous`, long (C-27), with a (+) chain "wealth moves into unlisted firms valued at book". That chain does not hold for capital added: cash put into a firm raises its book equity mark for mark, and booked investment stays in book equity (the pattern's point). The formula favors only the gap between market and book value on existing firms, which bears on the price at which firms change hands (C-36), not on capital added. Core-version error. The keys differ slightly (an investment flow in the medium run against a stock in the long run), but the core gives no valid (+) chain for either. |
| C-26 | C-37 | V | | The pattern signs the world price of art `increase`; the core records price and quantity as a group (`at_least_one_increase`). CR-6's 0.9 note on splitting a shift asks for a supply premise before the price is signed alone. The pattern gives none (A-19, A-20 bear on demand only), though most art is in fixed supply. The core's record is the stricter one. |
| C-27 | C-29, C-30 | M | | Short run. |
| C-28 | C-13, C-39 | V | | The pattern signs one item, the income and gains taxes of window emigrants, `decrease` over the medium and long run. The core signs the window's loss in the short run (C-13) and the total over the medium and long run (C-39, `ambiguous`). Under CR-12's 0.8 note on two items in one variable, each version records half: the pattern the item without the total, the core the total without the item beyond 2028. |
| C-29 | C-16 | M | | |
| C-30 | C-28 | M | | |
| C-31 | none | OC | J | The economy's capital stock `ambiguous` (kind 3). The core declined capital flows for lack of a premise on size. Nothing scorable lost. |
| C-32 | C-41 | M | | |
| C-33 | C-40 | M | | Both on A-22. The pattern's horizon includes the short run, when the budget has lost taxes from window departures and pays the Agency but has no wealth-tax receipts until June 2028. Its short-run sign in the 2027 window is wrong (CR-12g). The core's horizon (medium, long) is right, but it records no short-run net. |
| C-34 | C-4 | M | | |
| C-35 | C-3 | M | | |
| C-36 | C-14 | M | | |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-11 | OP | E | Gift tax receipts brought forward (CR-10a; A-5, A-8). Valid in the short run. Its "medium" horizon overreaches: from 2028 later splitting and gifts already made oppose (pattern C-9). Pattern-version omission of the receipt. |
| C-12 | OP | E | Inheritance tax receipts `decrease` in the long run: what is given now is not bequeathed later (CR-10a). Pattern-version omission; its CR-8 1.0 list of budget items leaves out both gift-tax chains. |
| C-18 | OP | J | Consumption `ambiguous` (substitution against the tax paid and fixed-target saving). Nothing scorable lost. |
| C-25 | OP | E | Penalties on understated tax (CR-8b; A-N1, A-19). Receipts into the same budget that the pattern's net (C-33) omits. Pattern-version omission. |
| C-31 | OP | E | Valtrian builders build more (CR-7a; A-15). The pattern's text names this response (C-22) but does not record it. Pattern-version omission. |
| C-33 | OP | E | Untaxed buyers buy more Ostrevian high-end homes. It rests on the price fall of C-32, which does not hold (see C-21 above). Core-version error. |
| C-34 | OP | E | Less high-end building in Ostrevia. It rests on C-32 too. Core-version error. |
| C-38 | OP | E | Pension providers' contributions, U1-b `increase` (CR-9; A-24). It follows from the pattern's C-7, and the pattern lists pension providers as an actor class. Pattern-version omission. |
| C-42 | OP | J | Taxed households' means fall by the holding-company and advisory costs they use up (CR-8c). The pattern records the costs (C-34) and declined to sign the means of households that reshape. The core's sign holds for those who keep paying any tax or fee. Defensible either way. |

### Findings

- **Pattern overclaims or hidden premises.** *SB-4.* Applied as written, it gives `decrease` for high-end homes, listed shares and unlisted firms, since a wealth tax lowers each asset's net return. The core rules give `ambiguous` for all three, because the same tax reaches the alternatives that set the price for taxed buyers (CR-7c, "what they could earn elsewhere"). SB-4 compares with alternatives the policy leaves untaxed. It is wrong as written for a tax on wealth in general, and should measure the change in return against the buyer's alternatives as the policy leaves them. *TX-6.* Its Unless clause states the sign "firmly" for saving in taxed forms by savers with untaxed alternatives. That holds only if fixed-target savers place their added saving in those alternatives. Where the favored forms are capped or costly, CR-4's exception can reach the taxed forms (C-11, J). *RS-17.* Its 1.0 clause names notch and kink without saying what differs. The core, without RS-17, derived "stay below" from the kink by CR-4 and missed the notch chain entirely, so neither the pattern nor the core rules prompt it. *RS-11* fits a charge on moving only through its derivation, not its If clause.
- **Errors in the core version.** High-end home values (C-32), from a misuse of the response argument against a chain driven by a second change, carried into C-33 and C-34. The same misuse appears in C-35, without changing the sign. Capital in unlisted firms (C-27) has a (+) chain that does not hold for capital added. Gift-tax receipts are signed `increase` into the medium term (C-11). Omissions: gifts after 2028, total saving, fewer arrivals, the pension valuation cost under U1-a, the notch chain in C-7, and the short-run net of the budget. C-17 is labeled for market-valued forms but carries total-saving chains, against the core's own gap note.
- **Errors in the pattern version.** Net receipts (C-33) carry a short-run horizon that includes the 2027 window, when only losses fall on the budget. The art price (C-26) is signed without a supply premise. Omissions: gift-tax receipts brought forward and later inheritance tax, penalties in the budget's net, Valtrian building and pension providers' contributions under U1-b. The emigrants' lost taxes (C-28) are recorded as an item with no total per horizon.
- **Test of 1.0 verdicts.** *SB-4 (failed: preconditions met, conclusion wrong):* confirmed. For listed shares and unlisted firms the core reached `ambiguous` without SB-4. For homes it reached `decrease`, but only by treating a chain driven by the tax on the buyers' alternatives as a response bounded by the tax on homes. Corrected, the core rules give `ambiguous`, and the core version's error shows that CR-7c read alone invites the same mistake as SB-4, as the pattern version's (b) 5 says. *RS-17 1.0, notch against kink (needed interpretation):* confirmed. The core derived the kink response from CR-4 alone and, with no notch clause to prompt it, missed the notch. *CR-1 1.0, notches (worked with interpretation):* confirmed that the clause needs reading. The core did not record K3 as a notch at the line but as op 3 on leaving. It found a different unclear point: K1 is op 3 and op 4 at once for one household. *CR-7 0.9 and valuation formulas (needed interpretation):* confirmed. The core derived the formula responses from CR-4 and CR-7a without the 0.9 clause (C-6, C-22, C-23), but misread CR-7c for homes. *CR-12 1.0, response argument in mirror form for an expansion (worked, with interpretation):* confirmed. The core used the same mirror premise (A-15) for Valtrian building (C-31) and found that it gives no long-run price sign. It also misapplied the argument in Ostrevia (C-32), which the pattern version had withdrawn there. *OC-1 1.0 and CR-8 1.0 for lost receipts (needed interpretation):* confirmed. The core did not use the 1.0 clause and netted the lost taxes under CR-12e with A-22 (C-40).
- **Candidate patterns.** The pattern version claims no second use of a 6.2e candidate. The nearest, "a standard per unit of a chosen attribute shifts the attribute" (WE-031), resembles the shift to expensed intangibles (C-6). But its If clause is a product standard, not a tax base, so this is not a second use. The pattern version's proposed candidate ("a tax base set by formula draws wealth to the forms it undervalues") is supported by the core's C-6, C-22 and C-23, derived from CR-4 alone.
- **Limits of the core rules.** None produced a difference: no S, OP or OC row has cause K. Unclear core-rule wording: (1) CR-7c's "elsewhere" does not say that where the policy also taxes the alternatives, the comparison is with the alternatives as taxed; the core version erred here. (2) CR-12e's 0.8 note on a second change is easy to miss when the second change is the same tax on another form; an example would help. (3) CR-4's exception does not say whether it bears on the choice between forms of saving or only on total saving (C-11/C-17). (4) CR-1 has no wording for a burden that is op 3 and op 4 at once for one household, or for a notch that binds only on those who later choose to leave. (5) CR-12's 1.0 note on what the response argument needs is written for a contraction only. (6) CR-8's 1.0 note does not mention lost receipts. (7) CR-4's 1.0 note on lobbying does not say how to split one Act into questions contested and uncontested on the counterfactual path. (8) CR-6's 0.9 note on splitting a shift and its 1.0 note on small effects do not say which governs a small shift in a market with fixed supply (art).
