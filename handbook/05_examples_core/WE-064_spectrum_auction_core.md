# WE-064 / Analysis: Auction of 2.9 GHz radio licenses with a build-out obligation and a per-bidder cap

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Tarnesse 2.9 GHz Award Regulations.** Tarnesse (about 12 million people, currency the mark, M) has three mobile network operators: Ardel Mobile (about 42% of subscriptions), Nevra Telecom (36%) and Kostel (22%), each holding national licenses in three existing bands that expire in 2035. Mobile data traffic grows about 30% a year and busy-hour capacity in the cities is tight; without new spectrum, operators add capacity by adding cell sites in their existing bands (densification). Linmark Fibre passes about 25% of homes with fibre; Pellow Networks' copper (DSL) lines serve about 1.6 million households, about 700,000 of them outside fibre and cable areas. About 11,000 tower and rooftop sites exist, mostly owned by Selwyn Towers and Haldmoor Sites; new towers need municipal permits taking 4 to 9 months. About 1,400 certified riggers do about 3,000 site installations a year. All radio equipment is imported; Tarnesse buys about 0.4% of world output.

The 2,880 to 3,000 MHz band (120 MHz) has been unused since a defence radar left it in 2024. Under the Radio Act no one may transmit without a license. The TCA consulted in March 2026; the Regulations were made on 1 March 2027; the auction ran in September and October 2027; licenses run from 1 January 2028 to 31 December 2042. Five bidders qualified: the three operators, Linmark Fibre (fixed wireless access outside its fibre footprint) and Ombra Group (a foreign entrant). A financial investor did not qualify by the deposit date under the TCA's provisional reading of reg. 9(3).

**Figures.** Six blocks of 20 MHz, reserve M40 million each (M240 million in all). Consultant's value M100 million to M200 million a block; projected receipts M600 million to M1.2 billion, against a general budget of about M58 billion and annual borrowing of about M2 billion. 90% population coverage takes about 6,500 sites per network; the cities and large towns (about 65%, which operators said they would cover commercially within five years) take about 3,000. Three to four networks at 6,500 sites is 20,000 to 26,000 installations in five years (4,000 to 5,000 a year), beside the existing 3,000 a year. About 2,000 new towers are projected. TCA costs: M9 million for the auction and M2 million a year for monitoring, from its appropriation out of the general budget.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Tarnesse, nationally. Neighboring countries license the same band in their own ways; cross-border coordination limits power near borders. | reg. 2. |
| Announced / enacted / effective / expires | Consultation March 2026; Regulations made (announced) 1 March 2027; auction September to October 2027; licenses effective 1 January 2028; coverage deadline 31 December 2032; licenses expire 31 December 2042. | regs. 1, 8, 9, 12. |
| Enforcement (who, penalties, resources) | The TCA: coverage verified by drive tests and operators' coverage maps; a licensee that has not met the coverage obligation by the deadline has its license revoked, without refund. | reg. 9(2), reg. 10. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Auction | `rights_allocation` (auction) | Six national licenses of 20 MHz in the 2.9 GHz band | Bidders who qualify by deposit | Ascending clock auction; reserve M40 million a block; 15-year term; no right of renewal. | — |
| K2 Build-out obligation | `mandated_contract_term` | Each license | Each licensee | Service in the band to areas containing 90% of the population by 31 December 2032, or revocation without refund. | — |
| K3 Cap | `quota` on holdings | Blocks in the band | Each bidder and later holder, with affiliates (control above 50% or right to appoint a board majority) | No more than two blocks awarded to, or held by, one person and its affiliates. | — |
| K4 Receipts | `revenue_use` | Auction payments | The Treasury | Paid into the Consolidated Fund. | — |
| K5 Administration | Enforcement | K1 to K3 | TCA, funded by its appropriation from the general budget | M9 million for the auction; M2 million a year for monitoring. | — |

Existing rules that stay in the counterfactual: the Radio Act (no transmission without a license); the operators' existing licenses, expiring 2035; tower permits; no regulation of mobile or broadband prices. **Counterfactual law:** the band stays unused; no one may transmit in it (CR-1 recording note).

Unclear provision:
- **U1, resale before the coverage deadline.** Reg. 14 allows transfer with the TCA's consent, the obligations passing with the license; reg. 9(3) says that until the coverage obligation is met the license is held "for the purpose of meeting it". U1-a: transfers are allowed at any time with consent. U1-b: reg. 9(3) bars transfer until the obligation is met or the deadline passes. No probability is given to either reading.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Auction | binary (the state sells a right it creates) | Yes: blocks are bid at or above reserve (A-1) | 2 (adds, for winners, the option of transmitting in the band, which the Radio Act otherwise removes); 4 (winners' payments transferred to the Treasury, by an exchange each winner accepts, CR-5) | CR-5, CR-7c, CR-8b, CR-10c, CR-4 |
| K2 Build-out | triangular in form (a term attached to the license), binary in effect (a burden attached to holding a right from the state) | Yes: licensees would cover only about 65% commercially (A-8), and revocation is credible (A-3) | 3 (attaches to the option "hold the license" the obligation to serve 90% by 2032, with revocation without refund as the penalty); dated: the penalty acts on 31 December 2032, before that through expectations (CR-10a) | CR-4 (x: build, y: forfeit; x: comply, y: overstate), CR-3a, CR-8a, CR-8c, CR-9 |
| K3 Cap | triangular (limits holdings among private bidders) | Yes for any bidder that would have taken more than two blocks (A-17, A-5) | 1 (removes the option of holding a third block, for each bidder and its affiliates, at award and later) | CR-4 (x: covered form, y: stake below the affiliate line), CR-6 (fixed quantity per holder) |
| K4 Receipts | binary | Yes (A-1) | 4 (the Treasury's means rise) | CR-8b, CR-8d |
| K5 Administration | binary | Yes | 4 (general budget to the TCA); 3 (drive tests and coverage reports attached to holding a license) | CR-8b, CR-8c, CR-8 0.7 (payers from the general budget) |
| U1 (reg. 9(3) and 14) | triangular | Under U1-b, binding for licensees that would sell before 2032 (A-10) | U1-a: 2 (adds the option of selling the license before 2032, with consent); U1-b: that option is not added until the obligation is met | CR-1 per reading, CR-4, CR-5 |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| licensees | Winners of blocks (some of the three operators, Linmark, Ombra) | Op 2: may transmit in the band; op 4: pay the auction price; op 3: K2 and K5 obligations; op 1 (K3): no third block. |
| licensees.low_value | Licensees who later value their license less than others would (A-10) | U1-a: may sell (op 2); U1-b: may not until the obligation is met. |
| operators.incumbent | Ardel, Nevra, Kostel, as holders of existing-band licenses and networks | Through CR-9 (substitute): the band substitutes for densification and for their existing spectrum; rivals (including entrants) gain capacity. |
| entrants | Linmark and Ombra | Op 2: entry into mobile or fixed wireless through the band (A-14). |
| investors.financial | Investors without networks | Op 2 under U1-a only, if they bid only to resell (A-12). |
| bidders | All qualifying bidders, with affiliates | Op 1 (K3) on a third block; pressure to hold through stakes below the affiliate line (A-5). |
| mobile_subscribers.cities | Buyers of mobile service where busy-hour capacity is tight | Through CR-9 (licensees' added capacity, same market). |
| residents.beyond_commercial_area | People in the 25% of population between the 65% commercial footprint and the 90% obligation | Through CR-9: K2 makes licensees serve them in the band. |
| dsl_households.outside_fibre | About 700,000 DSL households outside fibre and cable areas | Through CR-9 (substitute): fixed wireless in the band (A-18). |
| pellow_networks | Seller of DSL over sunk copper | Through CR-9 (substitute): rival fixed wireless. |
| tower_companies | Selwyn Towers, Haldmoor Sites | Through CR-9 (input_to): band sites and new rural towers; fewer densification sites. |
| workers.riggers | About 1,400 certified riggers | Through CR-9 (input_to): demand for installations. |
| riggers.prospective | People in related trades who could certify | CR-4 (x: other trade, y: train as rigger). |
| buyers.rigger_services_other | Fibre builders and other buyers of site installation work | Through CR-9 (same labor input_to their projects). |
| permit_applicants | Everyone applying for municipal tower permits | Through CR-9 (shared processing capacity, priced at a fee): more applications for band and rural towers; fewer for densification. |
| equipment_vendors | Foreign suppliers of radio equipment | Through CR-9 (input_to): orders for band equipment; fewer for densification. |
| treasury | Receives auction payments (K4) | Op 4: means rise. |
| taxpayers or recipients of other spending or future taxpayers | Payers and beneficiaries of the general budget | Through CR-8b and CR-8d: receipts free other money; K5 costs take some. |
| officials.tca | Runs the auction and monitors coverage | Op 4 (appropriation); tasks of K5. |
| town_councils | Councils campaigning for coverage | CR-4 (x: accept, y: lobby) on enforcement of K2. |
| borrowers.other | Other borrowers in Tarnesse's loan market | Through CR-9 (loan market): Treasury borrows less (A-26), licensees borrow more (A-27). |
| holders_of_currency | Buyers of foreign exchange | Through CR-9 (currency): equipment imports; foreign finance (A-N1). |
| neighboring_jurisdictions | Users of the same band abroad | Coordination limits power near borders; no operation changes their options beyond the coordination already in place. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | treasury | non_tax_receipts (auction payments) | increase | short | CR-1 op 4, CR-5, CR-8b | A-1 |
| C-2 | licensees | asset_value (2.9 GHz licenses) | increase | short (at award) | CR-1 op 2, CR-7c, CR-10c | A-1 |
| C-3 | licensees | resources_available_other_uses (auction payment) | decrease | short | CR-3c, CR-8a, CR-8b | A-1 |
| C-4 | licensees | investment_target (sites and equipment in the band) | increase | medium | CR-1 op 2, CR-4, CR-1 op 3 (K2) | A-4, A-3 |
| C-5 | residents.beyond_commercial_area | quantity_traded (mobile service in the band) | increase | medium; long | CR-1 op 3 (K2), CR-4, CR-9 | A-3, A-8 |

## 5. Responses

CR-4 for every pair of options each class has; CR-6 where a quantity is fixed; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | operators.incumbent | investment_target (densification in existing bands) | decrease | medium | CR-4 (x: densify, y: add the band), CR-9 | A-7, A-1 |
| C-7 | operators.incumbent | investment_target (densification in existing bands, March 2026 to end 2027) | decrease | short (announcement window) | CR-10a, CR-4 (x: densify now, y: wait for the band) | A-7, A-28 |
| C-8 | entrants | number_of_sellers (mobile and fixed wireless networks) | increase | medium | CR-1 op 2, CR-4 (x: stay out, y: enter) | A-14 |
| C-9 | bidders | reclassification (stakes and joint ventures below the affiliate line) | increase | short; medium | CR-1 op 1 (K3), CR-4 (x: covered form, y: uncovered form), CR-6 | A-5 |
| C-10 | licensees | term_prevalence (network-sharing agreements pooling blocks in the band) | increase | medium | CR-4, CR-12 0.9 (activity only under the policy) | A-6 |
| C-11 | licensees | compliance_cost (coverage maps, drive-test data, reports) | increase | medium | CR-1 op 3, CR-8c | - |
| C-12 | licensees | resources_available_other_uses (sites beyond the commercial footprint) | decrease | medium | CR-1 op 3, CR-3a, CR-3c, CR-8a | A-3, A-8 |
| C-13 | licensees | legal_breach (coverage overstated, met by minimal sites, or missed) | increase | medium | CR-4 (x: comply, y: violate), CR-12 0.9 | A-9 |
| C-14 | licensees | lobbying_effort (to extend or relax the coverage obligation) | increase | medium | CR-4 (x: accept, y: lobby), CR-10a, CR-8c | A-13, A-8 |
| C-15 | town_councils | lobbying_effort (on coverage) | ambiguous | medium | CR-12b over two CR-4 chains | A-13, A-3 |
| C-16 | bidders | lobbying_effort (on the TCA's reading of U1) | increase | short | CR-4, CR-12 0.9, CR-8c | A-13, A-12 |
| C-17 | investors.financial | applications (to qualify as bidders) | U1-a: increase; U1-b: no_change | short | CR-1 per reading, CR-4 (x: stay out, y: bid) | A-12 |
| C-18 | licensees.low_value | quantity_traded (license transfers before end 2032) | U1-a: increase; U1-b: no_change | medium | CR-1 per reading, CR-5, CR-7a | A-10 |
| C-19 | licensees.low_value | reclassification (sales of licensee companies or long capacity leases in place of transfers) | U1-a: no_change; U1-b: increase | medium | CR-4 (x: barred transfer, y: uncovered form), CR-6 | A-10, A-11 |
| C-20 | officials.tca | enforcement_cost | increase | short; medium | CR-1 op 4, CR-8c | - |
| C-21 | riggers.prospective | enrollment (rigger certification) | increase | short; medium | CR-10a, CR-4 (x: other trade, y: train), CR-7a | A-23, A-3, A-28 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-22 | workers.riggers | wage_rate | increase | short; medium | CR-9, LW-10, CR-6, CR-12e (arithmetic) | rigger labor input_to installations (close) | A-3, A-22, A-20 |
| C-23 | workers.riggers | employment | increase | medium | CR-9, CR-7a | as above | A-3, A-23 |
| C-24 | workers.riggers | wage_rate | ambiguous | long (after 2032) | CR-12b, CR-10b, CR-10a | as above | A-23, A-24 |
| C-25 | buyers.rigger_services_other | price_paid (site and fibre installation work) | increase | short; medium | CR-9, CR-7a | same labor input_to other site work (close) | A-3, A-22 |
| C-26 | buyers.rigger_services_other | quantity_traded (other installations, 2028 to 2032) | decrease | medium | CR-4c, CR-8a | as above | A-3, A-22 |
| C-27 | buyers.rigger_services_other | quantity_traded (other installations, after 2032) | increase | long | CR-10a, CR-4 (x: now, y: later) | as above | A-24, A-3, A-22 |
| C-28 | tower_companies | quantity_traded (site tenancies and new towers) | ambiguous | medium | CR-12b, CR-9 | sites input_to band networks and to densification | A-3, A-8, A-7 |
| C-29 | tower_companies | asset_value | ambiguous | short (from announcement) | CR-7c, CR-10c, CR-12b | as above | A-3, A-8, A-7, A-28 |
| C-30 | permit_applicants | wait_time (municipal tower permits) | ambiguous | medium | CR-9, CR-6, CR-12b | permit processing input_to towers (shared) | A-3, A-8, A-7, A-20 |
| C-31 | equipment_vendors | quantity_traded (radio equipment sold into Tarnesse) | increase | medium | CR-9, LW-10 | equipment input_to installations (close) | A-3, A-23 |
| C-32 | mobile_subscribers.cities | price_paid (per unit of data) (−), quality_per_unit (busy-hour speed) (+), quantity_traded (data) (+) | at_least_one_as_stated | medium | CR-9, CR-6 0.9, CR-4c, CR-12e (response argument) | band capacity same market as existing capacity | A-4, A-7, A-15 |
| C-33 | dsl_households.outside_fibre | quantity_traded (DSL lines) | decrease | medium | CR-4 (x: DSL, y: fixed wireless), CR-9 | fixed wireless substitute for DSL (partial) | A-18, A-1 |
| C-34 | pellow_networks | net_price_received (DSL outside fibre areas) | decrease | medium | CR-9, CR-6, CR-7b | as above | A-18, A-19 |
| C-35 | dsl_households.outside_fibre | price_paid (fixed broadband) | decrease | medium | CR-6, CR-4 | as above | A-18, A-19 |
| C-36 | pellow_networks | asset_value (copper network) | decrease | short (from announcement) | CR-7c, CR-10c | as above | A-18, A-19, A-28 |
| C-37 | operators.incumbent | asset_value (existing-band licenses to 2035) | decrease | short (from announcement) | CR-9, CR-7c, CR-10c | band substitute for existing spectrum (close) | A-7, A-28 |
| C-38 | operators.incumbent | asset_value (firms) | ambiguous | short; medium | CR-12b, CR-7c | competitors; substitute | A-17, A-14, A-7, A-3 |
| C-39 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses (from receipts) | at_least_one_increase | short; medium | CR-8b, CR-8d | - | A-1 |
| C-40 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses (TCA appropriation) | at_least_one_decrease | short; medium | CR-8b, CR-8 0.7 | - | - |
| C-41 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses (receipts net of TCA costs) | at_least_one_increase | whole period | CR-8 1.0, CR-12e (arithmetic) | - | A-1 |
| C-42 | borrowers.other | interest_rate | ambiguous | short; medium | CR-9, CR-6, CR-12b, CR-8 0.9 | loan market (same market) | A-26, A-27 |
| C-43 | holders_of_currency | exchange_rate | ambiguous | short; medium | CR-9 (currency), CR-12b | currency | A-3, A-23, A-N1 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| workers.riggers, wage_rate, short; medium | Band installations: 4,000 to 5,000 a year with K2 enforced (A-3) | Fewer densification installations (A-7) | Arithmetic (CR-12e): band installations alone exceed the 3,000 a year done in total without the policy, and densification cannot fall below zero; with capacity fixed at once (A-22) and cost rising (A-20), the pressure goes to price (CR-6 0.9 split premise) | increase (C-22) |
| workers.riggers, wage_rate, long | Projects delayed past 2032 (A-24) | More certified riggers (CR-10b; A-23) and the end of band build-out | None | ambiguous (C-24) |
| tower_companies, quantity_traded and asset_value | Band co-location and new rural towers (A-3, A-8) | Less densification (A-7) | None in the figures (the counterfactual densification count is not given) | ambiguous (C-28, C-29) |
| permit_applicants, wait_time, medium | New rural towers (A-3, A-8) | Fewer densification sites needing permits (A-7) | None | ambiguous (C-30) |
| mobile_subscribers.cities, price per unit / quality / quantity | Band capacity added (A-4) and competition (A-15) | Rigger wages raise the cost of densification (C-22) | Response argument (CR-12e): operators move from densification to the band only where the band gives capacity more cheaply (A-7), so the substitution cannot leave less capacity than without the policy. The license price and K2's rural sites are costs fixed per network (CR-4 0.7), which bear on whether a network operates, not on the unit price; A-15 says none leaves | at_least_one_as_stated (C-32) |
| operators.incumbent, asset_value (firms) | Surplus on blocks won below own value (A-17) | Entry (A-14), lower value of existing licenses (C-37), K2 burden (C-12) | None | ambiguous (C-38) |
| taxpayers group, resources_available_other_uses | Receipts (C-39) | TCA costs (C-40) | Arithmetic: one block at the M40 million reserve exceeds M9 million plus M2 million a year to 2032 (M19 million); CR-8 1.0 two items and the net | items as signed; net at_least_one_increase, whole period (C-41) |
| town_councils, lobbying_effort | Lobbying for enforcement and against extension | K2 delivers coverage they would have campaigned for (counterfactual contest, CR-4 1.0) | None | ambiguous (C-15) |
| borrowers.other, interest_rate | Licensees borrow to pay and build (A-27) | Treasury borrows less (A-26) | None | ambiguous (C-42) |
| holders_of_currency, exchange_rate | Equipment imports (C-31) | Foreign finance brought in for payments and build-out (A-N1) | None | ambiguous (C-43) |
| licensees, resources_available_other_uses | - | Payment (C-3, short); K2 sites (C-12, medium) | Different horizons (CR-12g); both decreases | decrease (short); decrease (medium) |
| licensees, asset_value (licenses) | License created (C-2) | K2 burden lowers the value of the license relative to one without it | That comparison is against another version of the policy, not the counterfactual (final check 3); against no license the value is created from nothing | increase (C-2) |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement.** The award was partly expected from the March 2026 consultation and fully from 1 March 2027 (A-28). Asset values move then (CR-7c, CR-10c): Pellow's copper network (C-36) and the operators' existing licenses (C-37) fall; tower companies' values move in a direction the rules do not settle (C-29). Operators hold back densification in the window (C-7), and some workers start rigger certification (C-21).
- **Auction (September to October 2027).** Payments fall due (C-1, C-3); the Treasury borrows less in that year (A-26), licensees borrow more (A-27).
- **Build-out (2028 to 2032).** Installations exceed rigger capacity (A-20, A-22); wages rise (C-22), other installation work is delayed (C-26) and, where it is delayed rather than cancelled, done after 2032 (C-27). These are per-window signs: the same projects happen at a different time. Building bunches before the 31 December 2032 deadline (CR-10a; path note, no separate consequence because the build-out exists only under the policy).
- **After 2032.** The rigger stock persists (CR-10b), so the long-run wage sign is ambiguous (C-24). Rural service built under K2 persists while it covers its running costs (CR-10b); how much would be withdrawn after 2032 is not signed.
- **Approach to 2042.** With no right of renewal (re-auction or renewal at market value), investment in the band falls as 2042 approaches (CR-10a, CR-7c); beyond the horizon of this analysis, noted only.
- **Revocation.** A revoked license would be re-auctioned (A-30, p 0.3, not reported).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-3 | licensees | resources_available_other_uses (auction payment) | decrease | Other investment or payouts licensees would have made with the payment | CR-3c, CR-8a |
| C-11 | licensees | compliance_cost | increase | Engineering and reporting time | CR-1 op 3, CR-8c |
| C-12 | licensees | resources_available_other_uses (sites beyond the commercial footprint) | decrease | Investment elsewhere displaced by about 3,500 mandated sites per network | CR-3a, CR-8a |
| C-14 | licensees | lobbying_effort | increase | Staff time and money | CR-8c |
| C-20 | officials.tca | enforcement_cost | increase | M9 million and M2 million a year | CR-8c |
| C-26 | buyers.rigger_services_other | quantity_traded (other installations, 2028 to 2032) | decrease | Fibre and other site work not done in the period | CR-4c, CR-8a |
| C-40 | taxpayers group | resources_available_other_uses (TCA appropriation) | at_least_one_decrease | Other spending or lower taxes | CR-8b |

The band itself had no use in the counterfactual (the Radio Act bars transmission and the radar left in 2024), so CR-8a finds no displaced use of the spectrum. CR-8's symmetry: payments by licensees (C-3) are receipts to the Treasury (C-1) and free other budget money (C-39); rigger labor drawn to the band (C-22, C-23) is withdrawn from other work (C-26); compliance, enforcement and lobbying are used up (C-11, C-14, C-16, C-20).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Some blocks are bid at or above the reserve: bidders expect a license to be worth more than M40 million after the build-out cost. | binding | 0.95 | Five qualified bidders; consultant's valuation. | C-1, C-2, C-3, C-6, C-33, C-39, C-41 fail. |
| A-3 | The obligation is enforced: revocation is credible, so licensees build to 90% by the end of 2032. | enforcement | 0.75 | Regulations' text; TCA's record. | C-4 (K2 part), C-5, C-12, C-15, C-21, C-22, C-23, C-25, C-26, C-27, C-31 fail or lose this chain. |
| A-4 | The band is used to add capacity where busy-hour demand presses on existing capacity. | other | 0.85 | Traffic growth; city congestion. | C-4, C-32 fail. |
| A-5 | Some bidders or holders use stakes or joint ventures below the affiliate line. | other | 0.55 | Control-based affiliate test; practice elsewhere. | C-9 fails. |
| A-6 | Some licensees pool blocks by network-sharing agreements. | other | 0.6 | Existing sharing; contiguous spectrum worth more. | C-10 fails. |
| A-7 | Without the band, operators would densify in existing bands; with it, they densify less. | substitutability | 0.75 | Capacity plans; cost per unit of capacity. | C-6, C-7, C-37 fail; C-28, C-29, C-30 lose their (−) chain. |
| A-8 | Licensees would not on their own cover 90% with the band by 2032 (about 65% commercially). | binding | 0.8 | Consultation responses; site counts. | C-5, C-12, C-14 fail. |
| A-9 | Some licensees overstate coverage, meet it by minimal sites, or miss the deadline. | enforcement | 0.55 | Drive-test sampling; cost of last sites. | C-13 fails. |
| A-10 | After the auction some licensees value their licenses less than others would. | other | 0.6 | Entrants' financing; five years is long. | C-18, C-19 fail. |
| A-11 | Under U1-b, sales of licensee companies or long capacity leases are not treated as transfers. | enforcement | 0.55 | Reg. 14 speaks of transfer of the license. | C-19 (U1-b) fails. |
| A-12 | Some investors without networks bid only if they can resell before the deadline. | other | 0.55 | One investor registered interest. | C-16, C-17 fail. |
| A-13 | Licensees, entrants and town councils can organize to lobby at a cost below their stakes. | other | 0.85 | Industry associations; councils' campaigns. | C-14, C-15, C-16 fail. |
| A-14 | At least one of Linmark and Ombra wins blocks and builds a network. | other | 0.6 | Demand of ten blocks for six at reserve; the cap. | C-8 fails; C-38 loses a (−) chain. |
| A-15 | Licensees compete on price; no network leaves the market because of the award in the medium run. | other | 0.7 | Active price competition; entry. | C-32 fails. |
| A-16 | Kostel exits or merges because it wins too little of the band. | other | 0.3 | Kostel's share and finances. | Not reported. |
| A-17 | Some operators win blocks at prices below their own value for them. | other | 0.6 | Auction structure with the cap. | C-38 loses its (+) chain. |
| A-18 | Fixed wireless in the band substitutes for DSL for some households outside fibre areas. | substitutability | 0.7 | 700,000 DSL households outside fibre; Linmark's plans. | C-33 to C-36 fail. |
| A-19 | Pellow's copper network cannot be withdrawn or its costs cut at once. | durability | 0.8 | Sunk copper plant. | C-34, C-35, C-36 fail. |
| A-20 | Sites cannot be added at unchanged cost per site, and cost per site does not fall as building expands. | durability | 0.8 | Permit times; rigger numbers. | C-22, C-30 fail or lose this chain. |
| A-22 | Riggers cannot be added at once (certification 6 to 12 months). | durability | 0.75 | Certification rules. | C-22, C-25, C-26, C-27 fail. |
| A-23 | Some new riggers are trained or move from other work in the medium run. | mobility | 0.8 | Training places; related trades. | C-21, C-23, C-24, C-31 fail. |
| A-24 | Some projects delayed by the shortage are done after 2032 rather than cancelled. | other | 0.6 | Fibre builders' plans. | C-27 fails; C-24 loses its (+) chain. |
| A-25 | Equipment vendors' supply cannot expand at unchanged cost at once. | durability | 0.6 | Order books; lead times. | No reported consequence rests on it (see section 10 notes). |
| A-26 | The Treasury borrows less than it would have, by part of the receipts. | revenue_use | 0.6 | Annual borrowing about M2 billion. | C-42 loses its (−) chain. |
| A-27 | Licensees borrow part of what they pay and build in Tarnesse's loan market. | other | 0.7 | Operators' debt; entrants' financing. | C-42 loses its (+) chain. |
| A-28 | Investors expected the award partly from March 2026 and fully from 1 March 2027. | expectations | 0.8 | Market commentary; share prices. | C-7, C-21, C-29, C-36, C-37 lose their timing; signs from award stand. |
| A-30 | A license is revoked and the band re-auctioned. | other | 0.3 | Licensees' finances; lobbying. | Not reported. |
| A-N1 | Part of what licensees pay and spend on build-out is financed from abroad (the foreign entrant's or foreign shareholders' and lenders' capital). | other | 0.6 | NEW. Ombra is a foreign group; operators' debt markets; all equipment is imported and often vendor-financed. | C-43 loses its (−) chain (sign would be increase). |

**Not reported** (an assumption below 0.5):
- Kostel exits or merges, lowering the number of networks (A-16, p 0.3).
- A license is revoked without refund and re-auctioned, with a second payment to the Treasury and a stranded build-out (A-30, p 0.3).
- Equipment prices paid in Tarnesse rise (CR-6, CR-9; A-25, p 0.6): A-25 clears the cut-off, but the chain also needs total equipment orders to rise in the short run, which A-22 (rigger capacity fixed at once) leaves open since band orders displace densification orders; recorded as a kind (2) chain without a premise, not reported (CR-12, 0.8).

### Final check before the report

1. **Uncombined chains.** Each key reached by opposing chains is in section 7: rigger wages (dominance by arithmetic), tower companies, permits, firm values, councils' lobbying, interest rates, the exchange rate. Announcement-window chains (C-7, C-21, C-36, C-37) have the same sign as the later chains on their keys.
2. **Group signs.** C-32 (price, quality, quantity: CR-6 0.9 gives no split premise), C-39 to C-41 (general budget group, CR-8 0.7).
3. **Baseline.** Every sign is against the band staying unused. Comparisons with an auction without K2 or without the cap (lower receipts under K2; a different allocation without K3) are against another version of the policy and are not signed. U1 signs are against no award, per reading; "U1-b has fewer transfers than U1-a" is not itself a consequence.
4. **Worse off is not poorer.** C-3 and C-12 are signed because licensees pay sums they cannot avoid once they have won (payment) and held the license (K2). Losing bidders are not signed.
5. **Timing shifts.** Densification held back in the announcement window (C-7) and after (C-6); other installations in 2028 to 2032 (C-26) and after (C-27).
6. **Both sides of every transfer.** Auction payment: C-3 and C-1, C-39. TCA costs: C-20 and C-40. Rigger labor: C-22, C-23 against C-25, C-26. License value: created (C-2), captured by winners net of price; the price goes to the Treasury (CR-7c).
7. **Every actor class, every core rule.** CR-4: each class's option pairs (Section 3). CR-6: rigger labor (C-22), permits (C-30), DSL (C-34), mobile data (C-32), K3 holdings (C-9). CR-7: capitalization for licenses (C-2), existing licenses (C-37), copper (C-36), towers (C-29), incumbent firms (C-38); CR-7a for riggers. CR-9: every relation in Section 3, including currency (C-43), loan market (C-42), substitutes (DSL, existing spectrum) and contracts (network sharing, C-10). Gifts and proximity: no relation found.
8. **Unstated premises.** Lobbying needs A-13; responses need the margin premises (A-5, A-6, A-7, A-9, A-12, A-18, A-23); foreign finance added as A-N1.
9. **Pattern baselines.** No patterns used.

## 11. Report

**The policy:** Tarnesse auctions six 20 MHz licenses in an unused band (reserve M40 million each) for 2028 to 2042. Each licensee must serve areas with 90% of the population by the end of 2032 or lose the license without refund; no one may hold more than two blocks with its affiliates; receipts go to the Consolidated Fund; the TCA spends M9 million on the auction and M2 million a year on monitoring.

**Visible consequences:** The Treasury receives the auction payments (C-1); winners pay them (C-3) and hold a newly valuable license (C-2); licensees build networks in the band (C-4); people in the areas between the commercial 65% footprint and 90% get service in the band (C-5); new networks enter (C-8).

**Invisible consequences:**
- *Operators:* they densify less in existing bands, from the announcement (C-6, C-7), and their existing licenses are worth less (C-37); mandated rural sites take means from other uses (C-12); they bear reporting costs (C-11), some overstate or miss coverage (C-13), and they lobby for an extension (C-14).
- *Bidders and holders:* stakes and joint ventures below the affiliate line (C-9) and network-sharing (C-10). U1: under U1-a, licenses change hands before 2032 (C-18) and resale investors bid (C-17); under U1-b, company sales and leases take the place of transfers (C-19). Bidders lobby over the reading (C-16).
- *Riggers and other builders:* riggers' wages and employment rise (C-22, C-23) and more people train (C-21); fibre builders and others pay more for installation work and do less of it until 2032 (C-25, C-26), and some of it afterwards (C-27). Radio equipment orders rise (C-31).
- *Fixed broadband:* DSL households outside fibre areas switch to fixed wireless (C-33) and pay less (C-35); Pellow receives less (C-34) and its copper network loses value from the announcement (C-36).
- *Mobile subscribers in the cities:* lower price per unit of data, better busy-hour speed or more data used, at least one of these as stated (C-32).
- *Budget:* receipts free other money for taxpayers or other spending (C-39); TCA costs take some (C-40); the net is positive over the period (C-41).

**Ambiguous effects:** riggers' wages after 2032 (C-24); tower companies' business and value (C-28, C-29) and permit waits (C-30), where new band and rural towers push one way and less densification the other; incumbents' firm values (C-38); councils' lobbying (C-15); interest rates for other borrowers (C-42); the exchange rate (C-43).

**Key conditions:** K2 enforced (A-3, 0.75) and binding (A-8, 0.8); the band substitutes for densification (A-7, 0.75); rigger supply fixed at once (A-22, 0.75) and costs rising (A-20, 0.8); fixed wireless substitutes for DSL (A-18, 0.7); an entrant builds (A-14, 0.6). One premise was added: foreign finance (A-N1, 0.6).

**What this analysis cannot say:** sizes (how much prices fall, how many households switch, how large receipts are within the projected range), net welfare, whether the policy is good, whether U1-a or U1-b is the right reading. Health, safety and environmental effects (including any effect of new towers on landscapes) are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | treasury | non_tax_receipts (auction payments) | increase | short | visible | B | CR-1 op 4 (payments under K1, paid into the Consolidated Fund by K4); CR-5 (each winner accepts the price, so it is paid only where bids reach the reserve, A-1); CR-8b (every payment is a receipt) | A-1 |
| C-2 | licensees | asset_value (2.9 GHz licenses) | increase | short (at award) | visible | B | CR-1 op 2 (the option of transmitting in the band, which the Radio Act removes in the counterfactual); CR-10c (value reflects expected yields); CR-7c (an asset the policy creates is valued at creation and captured by whoever receives it, here net of the price paid) | A-1 |
| C-3 | licensees | resources_available_other_uses (auction payment) | decrease | short | visible | B | CR-3c and CR-8a (the payment is not available for other uses); CR-8b (it is what the Treasury receives, C-1) | A-1 |
| C-4 | licensees | investment_target (sites and equipment in the band) | increase | medium | visible | B | CR-1 op 2; CR-4 (x: no band network, y: build in the band where busy-hour demand presses, A-4); CR-1 op 3 (K2 attaches revocation to not building to 90%, A-3) | A-4, A-3 |
| C-5 | residents.beyond_commercial_area | quantity_traded (mobile service in the band) | increase | medium; long | visible | B | CR-1 op 3 (K2); CR-4 (x: build beyond 65%, y: forfeit the license without refund; y made worse, so licensees build, A-3, A-8); CR-9 (residents are the buyers of the added service); CR-10b (sites built persist) | A-3, A-8 |
| C-6 | operators.incumbent | investment_target (densification in existing bands) | decrease | medium | invisible | B | CR-4 (x: densify, y: use the band; y made available by K1, so operators for whom the band is cheaper per unit of capacity switch, A-7); CR-9 (relation: band capacity substitute for densification) | A-7, A-1 |
| C-7 | operators.incumbent | investment_target (densification in existing bands, March 2026 to end 2027) | decrease | short (announcement window) | invisible | B | CR-10a (a change expected in the future alters choices now, A-28); CR-4 (x: densify now, y: wait for the band) | A-7, A-28 |
| C-8 | entrants | number_of_sellers (mobile and fixed wireless networks) | increase | medium | visible | B | CR-1 op 2 (spectrum available to an entrant); CR-4 (x: stay out, y: enter; K3 holds enough blocks back from incumbents for an entrant to win, A-14) | A-14 |
| C-9 | bidders | reclassification (stakes and joint ventures below the affiliate line) | increase | short; medium | invisible | B | CR-1 op 1 (K3 removes a third block for a person and its affiliates); CR-6 (a fixed quantity per holder leaves pressure for margins outside the rule); CR-4 (x: covered form, control, y: uncovered form, a stake below 50% without board control, A-5) | A-5 |
| C-10 | licensees | term_prevalence (network-sharing agreements pooling blocks in the band) | increase | medium | invisible | B | CR-4 (x: use own blocks alone, y: pool with another licensee; contiguous spectrum is worth more and K3 limits each holder to two blocks, A-6); CR-12 0.9 (the activity exists only under the policy) | A-6 |
| C-11 | licensees | compliance_cost (coverage maps, drive-test data, reports) | increase | medium | invisible | A | CR-1 op 3 (K2 and K5 attach reporting and verification to holding a license); CR-8c (used up) | none |
| C-12 | licensees | resources_available_other_uses (sites beyond the commercial footprint) | decrease | medium | invisible | B | CR-1 op 3; CR-3a (the obligation burdens the chosen option, holding the license); CR-3c and CR-8a (about 3,500 sites per network that licensees would not have built, A-8, built because revocation is credible, A-3, are withdrawn from other uses) | A-3, A-8 |
| C-13 | licensees | legal_breach (coverage overstated, met by minimal sites, or missed) | increase | medium | invisible | B | CR-4 (x: comply fully, y: overstate or build minimal sites; drive tests are sampled, A-9); CR-12 0.9 (breach exists only under the policy) | A-9 |
| C-14 | licensees | lobbying_effort (to extend or relax the coverage obligation) | increase | medium | invisible | B | CR-4 (x: accept, y: lobby; K2 makes accepting costly where coverage is uncommercial, A-8); CR-10a (the dated deadline); CR-12 0.9 (the question exists only under the policy); CR-8c | A-13, A-8 |
| C-15 | town_councils | lobbying_effort (on coverage) | ambiguous | medium | invisible | B | CR-12b: (+) CR-4 (x: accept, y: lobby for enforcement of K2 and against extension; A-13); (−) CR-4 1.0 (councils campaign for coverage in the counterfactual; K2 delivers coverage, A-3, so part of that campaign is no longer worth its cost). No dominance premise | A-13, A-3 |
| C-16 | bidders | lobbying_effort (on the TCA's reading of U1) | increase | short | invisible | B | CR-4 (x: accept the provisional reading, y: lobby for the reading that favors them; resale investors, A-12); CR-12 0.9 (the question exists only under the policy); CR-8c | A-13, A-12 |
| C-17 | investors.financial | applications (to qualify as bidders) | U1-a: increase; U1-b: no_change | short | invisible | B | CR-1 per reading (U1-a adds the option of resale before 2032; U1-b does not); CR-4 (x: stay out, y: bid; investors who bid only to resell, A-12, bid only under U1-a) | A-12 |
| C-18 | licensees.low_value | quantity_traded (license transfers before end 2032) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-1 per reading (U1-a adds the option of selling); CR-5 (a sale takes place where the buyer values the license more, A-10); CR-7a (means move to the user that yields more); U1-b: no transfer is allowed before the obligation is met | A-10 |
| C-19 | licensees.low_value | reclassification (sales of licensee companies or long capacity leases in place of transfers) | U1-a: no_change; U1-b: increase | medium | invisible | B | U1-b: CR-1 op 1 (transfer barred); CR-6 (the gain from moving the license to a higher-value user seeks an open margin); CR-4 (x: barred transfer, y: sale of the company or a lease, not treated as transfer, A-11). U1-a: the direct transfer is open, so no reshaping is needed for that purpose | A-10, A-11 |
| C-20 | officials.tca | enforcement_cost | increase | short; medium | visible | A | CR-1 op 4 (M9 million for the auction, M2 million a year for monitoring); CR-8c | none |
| C-21 | riggers.prospective | enrollment (rigger certification) | increase | short; medium | invisible | B | CR-10a (the build-out is expected from 2027, A-28); CR-4 (x: stay in another trade, y: train; y made better by higher wages, C-22); CR-7a (labor moves toward the higher yield, A-23) | A-23, A-3, A-28 |
| C-22 | workers.riggers | wage_rate | increase | short; medium | invisible | B | CR-9 and LW-10 (relation: rigger labor input_to installations; demand for installations rises); CR-12e (arithmetic: with K2 enforced, A-3, band installations alone are 4,000 to 5,000 a year against 3,000 a year done in total without the policy, so less densification, A-7, cannot offset them); CR-6 0.9 (riggers cannot be added at once, A-22, and cost per site rises, A-20, so the pressure goes to price) | A-3, A-22, A-20 |
| C-23 | workers.riggers | employment | increase | medium | visible | B | CR-9 (demand for rigger labor rises, C-22); CR-7a (labor moves in from related trades and training, A-23) | A-3, A-23 |
| C-24 | workers.riggers | wage_rate | ambiguous | long (after 2032) | invisible | B | CR-12b: (+) CR-10a (projects delayed past 2032 are done then, A-24); (−) CR-10b (riggers trained for the build-out remain, A-23, while band installation falls back). No dominance premise | A-23, A-24 |
| C-25 | buyers.rigger_services_other | price_paid (site and fibre installation work) | increase | short; medium | invisible | B | CR-9 (relation: same rigger labor input_to their projects); CR-7a (the wage rise, C-22, spreads to every use of the movable labor) | A-3, A-22 |
| C-26 | buyers.rigger_services_other | quantity_traded (other installations, 2028 to 2032) | decrease | medium | invisible | B | CR-4c (at the higher price the least valued projects are given up or deferred); CR-8a (labor drawn to the band is withdrawn from other work) | A-3, A-22 |
| C-27 | buyers.rigger_services_other | quantity_traded (other installations, after 2032) | increase | long | invisible | B | CR-10a and CR-4 (x: build in 2028 to 2032 at the higher price, y: build after; some delayed projects are done later rather than cancelled, A-24); per-window sign against the counterfactual (02_ontology 2.5, timing shifts) | A-24, A-3, A-22 |
| C-28 | tower_companies | quantity_traded (site tenancies and new towers) | ambiguous | medium | invisible | B | CR-12b: (+) CR-9 (relation: sites input_to band networks; co-location and about 2,000 new towers, mostly beyond the commercial footprint, A-3, A-8); (−) CR-9 (relation: sites input_to densification, which falls, A-7). No dominance premise (the counterfactual densification count is not in the figures) | A-3, A-8, A-7 |
| C-29 | tower_companies | asset_value | ambiguous | short (from announcement) | invisible | B | CR-10c and CR-7c (value reflects expected yields, captured from the announcement, A-28); the yields are C-28, a kind (3) chain under CR-12 0.8 | A-3, A-8, A-7, A-28 |
| C-30 | permit_applicants | wait_time (municipal tower permits) | ambiguous | medium | invisible | B | CR-12b: (+) CR-9 and CR-6 (more applications for band and rural towers at a fixed processing capacity, A-20, A-3, A-8); (−) fewer densification sites need permits (A-7). No dominance premise | A-3, A-8, A-7, A-20 |
| C-31 | equipment_vendors | quantity_traded (radio equipment sold into Tarnesse) | increase | medium | invisible | B | CR-9 and LW-10 (relation: equipment input_to installations); total installations rise once riggers are added (C-23, A-23), and new networks need core equipment | A-3, A-23 |
| C-32 | mobile_subscribers.cities | price_paid (per unit of data) (−), quality_per_unit (busy-hour speed) (+), quantity_traded (data) (+) | at_least_one_as_stated | medium | visible | B | CR-9 (relation: band capacity same market as existing capacity, A-4); CR-6 (more capacity offered at each price; with no premise splitting the response, the members are a group, CR-6 0.9 and 0.7); CR-4c; CR-12e (response argument: operators replace densification with the band only where it is cheaper per unit of capacity, A-7, so the substitution does not reduce capacity; license price and K2 sites are costs fixed per network, CR-4 0.7, and no network leaves, A-15) | A-4, A-7, A-15 |
| C-33 | dsl_households.outside_fibre | quantity_traded (DSL lines) | decrease | medium | invisible | B | CR-4 (x: DSL, y: fixed wireless in the band; y newly available, A-18); CR-9 (relation: fixed wireless substitute for DSL) | A-18, A-1 |
| C-34 | pellow_networks | net_price_received (DSL outside fibre areas) | decrease | medium | invisible | B | CR-9 (fewer buyers at each price, C-33); CR-6 0.9 (copper cannot be withdrawn or its costs cut at once, A-19, so the pressure goes to price); CR-7b (the loss settles on the means that cannot move) | A-18, A-19 |
| C-35 | dsl_households.outside_fibre | price_paid (fixed broadband) | decrease | medium | invisible | B | CR-6 (C-34 for those who stay on DSL); CR-4 (those who switch do so only to a cheaper or better offer) | A-18, A-19 |
| C-36 | pellow_networks | asset_value (copper network) | decrease | short (from announcement) | invisible | B | CR-10c and CR-7c (the expected fall in yields, C-34, is borne by the owner when it becomes expected, A-28) | A-18, A-19, A-28 |
| C-37 | operators.incumbent | asset_value (existing-band licenses to 2035) | decrease | short (from announcement) | invisible | B | CR-9 (relation: band spectrum substitute for existing spectrum in supplying capacity, A-7); CR-10c and CR-7c (a lower expected yield is borne by holders when expected, A-28) | A-7, A-28 |
| C-38 | operators.incumbent | asset_value (firms) | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-7c (blocks won at prices below their value to the winner, A-17); (−) CR-9 (entry, A-14; lower value of existing licenses, C-37; K2 burden, C-12, A-3). No dominance premise | A-17, A-14, A-7, A-3 |
| C-39 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses (from receipts) | at_least_one_increase | short; medium | invisible | B | CR-8b (receipts add to the budget, C-1); CR-8d (money paid into the Consolidated Fund frees other money: lower borrowing, lower taxes or more spending, a group under CR-8 0.7) | A-1 |
| C-40 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses (TCA appropriation) | at_least_one_decrease | short; medium | invisible | A | CR-8b and CR-8 0.7 (payers from the general budget, a group) | none |
| C-41 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses (receipts net of TCA costs) | at_least_one_increase | whole period | invisible | B | CR-8 1.0 (receipts and costs in the same budget: two items and the net); CR-12e (arithmetic: at least one block at the M40 million reserve, A-1, against M9 million plus M2 million a year to 2032) | A-1 |
| C-42 | borrowers.other | interest_rate | ambiguous | short; medium | invisible | B | CR-12b: (−) CR-9 and CR-6 (the Treasury borrows less in the loan market, A-26); (+) licensees borrow to pay and build, A-27. CR-8 0.9 (the borrowing baseline). No dominance premise | A-26, A-27 |
| C-43 | holders_of_currency | exchange_rate | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-9 (currency: more imported equipment, C-31, raises demand for foreign currency); (−) CR-9 (currency: finance brought from abroad for payments and build-out, A-N1). No dominance premise | A-3, A-23, A-N1 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-064-C1: The new band's value is created by K1 out of a right the Radio Act withholds. CR-7c says the value is captured by whoever receives the asset at creation, but in an auction it is split between the winner and the Treasury by the price. No core rule says how the split is set (it depends on the auction format and on K3); A-17 had to supply it. A short clause in CR-7c for rights sold at creation would close this.
- GAP-064-C2: Whether equipment orders rise in the short run depends on whether band installations add to or displace densification installations while rigger capacity is fixed. The rules give the direction of each chain but no way to sign a fixed-capacity reallocation between two uses of the same input without a count; left unreported.

**(b) Core-rule wording that was hard to apply.**
- CR-4 1.0 (lobbying against a counterfactual contest) applied to town councils: their coverage campaigns exist without the policy, so the sign of their lobbying under the policy needed both chains and came out ambiguous. The note does not say whether redirected lobbying (same effort, new target) counts as a change.
- CR-12e (arithmetic dominance) for rigger wages needed the counterfactual total of installations (3,000 a year) and the observation that a displaced use cannot fall below zero. The rule allows arithmetic but does not mention bounding by a counterfactual total; this seemed legitimate but is worth stating.
- CR-6 1.0 (scope of the public-supply clause) for municipal permits: the permit is priced at a fee but processing capacity is fixed, which is neither a public supplier at an open quantity nor clearly a fixed-quantity public supply. Treated as a shared input with a direction from CR-6.
- Per-reading signs (U1) against the counterfactual: "no_change" under U1-b for transfers is against no award, which is correct but hides the more informative comparison between readings. The normal form has no place for a between-reading comparison.

**(c) Vocabulary missing from the ontology.**
- No variable for network coverage (share of population served by a network); `quantity_traded (mobile service in the band)` was used for C-5.
- No variable for public borrowing (the Treasury's own borrowing); its effect could only be carried through `interest_rate` for other borrowers.
- No actor class for holders of a right whose obligations travel with it (licensees bound by K2 after transfer); `licensees.low_value` was used.
