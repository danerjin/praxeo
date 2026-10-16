# WE-052 / Analysis: Repeal of a cap on retail liquor licenses

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Merrowind Retail Liquor Licensing Reform Act.** Merrowind (6.0 million people, 290 towns) has since 1949 allowed one off-premises ("package store") license per 2,500 residents of each town, at least one per town, recounted at each census. Licenses may be sold or leased within the town with routine Board approval (about 90 transfers a year). There are 2,380 licenses, selling for about $400,000 on average ($150,000 to $750,000); about 560 are leased by non-operating holders for $26,000 to $34,000 a year; about 140 are held by supermarket chains (Merrowind has 1,150 supermarkets and 2,600 convenience stores); about 830 (35%) are pledged as collateral, with about $210 million outstanding with three regional banks lending up to 60% of appraised value. The renewal fee is $1,000. A package store sells about $1.6 million a year and holds about six weeks of stock; package stores employ about 13,500. Since 2012 section 12(4) allows licensees to sell on Sunday from noon to 6 p.m. (about 9% of package-store revenue). Liquor excise (per gallon) raises about $310 million a year; the 6% sales tax also applies.

Just outside: Ashcombe issues licenses to any qualified applicant for $3,000 a year, lets supermarkets sell wine and spirits and allows Sunday sales. About 1.1 million Merrowind residents live within 30 minutes of the line; a 50-item basket costs 11% more in Merrowind after allowing for excise; about 7% of Merrowind residents' wine and spirits is bought in Ashcombe. Small retail units in commercial zones rent at about $26 a sq ft with 5% vacancy; rezoning takes 12 to 24 months. The Board's licensing staff of 18 is funded by an $8.5 million appropriation; fees go to the general fund. A 1987 supreme court ruling holds that a license is a privilege, not property: holders have no claim when the legislature changes the rules.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Merrowind; Ashcombe next door with free entry, supermarket sales and Sunday sales | Policy record |
| Announced / enacted / effective / expires | Introduced 2 February 2027; passed 20 May 2027 (41-9, 112-38); signed 1 June 2027; applications from 1 June 2028; effective 1 December 2028; no expiry; no referendum petition | Policy record |
| Enforcement (who, penalties, resources) | Alcohol Control Board; 18 licensing staff on an $8.5 million appropriation, not raised by the Act; compliance checks on underage sales continue | Policy record; K1 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Repeal of the cap | Removal of a `quota` on the number of licensed sellers | Off-premises retail licenses | Alcohol Control Board | Section 12 repealed; section 12A: the Board "shall issue" a license to any qualified applicant (age 21, no felony in ten years, commercial zone, 500 feet from schools and places of worship). Licenses tied to holder and premises; not transferable. Applications from 1 June 2028; licenses effective 1 December 2028. | None |
| K2 Annual fee | Fee for a license | Every off-premises license, old or new | Licensees | $5,000 a year from 1 December 2028 (counterfactual: $1,000). To the general fund. | None |
| K3 Hours of new licenses | Hours rule | Licenses under 12A | Licensees | 8 a.m. to 10 p.m., Monday to Saturday | — |
| K4 Transition | Saving clause | Licenses in force on 1 December 2028 | — | Continue in force and are renewed under 12A | — |
| K5 No compensation | — | Holders | — | "No person shall have any claim against the State by reason of this Act." | — |

Existing rules on both paths: three-tier system (12 licensed wholesalers), excise and sales tax, the 500-foot rule, zoning, underage-sale rules with Board compliance checks.

Unclear provisions:
- **U1, Sunday sales of licenses already in force.** U1-a: old licenses keep the Sunday privilege of 12(4) for as long as they are renewed; only new licenses lack it. U1-b: from their first renewal under 12A (1 December), old licenses carry 12A's hours, so no off-premises license may sell on Sunday. The Board has not said, no court has ruled; no probability is given.

**Counterfactual.** The cap stays in force (a repeal: the counterfactual is the old rule, `03_workflow.md`, "Analyzing a repeal"): 2,380 transferable licenses recounted at the 2030 census, a $1,000 fee, Sunday sales for every licensee, and a contested cap with holders and grocers lobbying (A-9). Signs below are against that path. `persistence` compares the repeal path with the path on which the cap was never imposed.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Repeal | triangular (removes a restriction on exchanges between buyers and would-be sellers) | Yes: the cap binds on the counterfactual path (A-1) | 2 for qualified would-be sellers (the option to sell is added); 1 for holders (the option to sell or lease the license, and the scarcity that gave it value, are removed from 1 December 2028); 2 for buyers (new sellers to buy from) | CR-4, CR-5, CR-6, CR-7a, CR-7b, CR-7c, CR-9, CR-10a, CR-10c |
| K2 Fee | binary (state takes from each licensee) | Yes (paid by every outlet) | 3 on the option of holding a license (a charge paid only by those who take the option, CR-1 0.7); a cost fixed per outlet (CR-4 0.8 note) | CR-3a, CR-4, CR-8b |
| K3 Hours | triangular | Binds on Sunday for new licenses (where an entrant would have opened Sunday) | 3 on the option K1 adds: the new option comes without Sunday | CR-1, CR-3b, CR-4 |
| K4 Transition | per reading | — | U1-a: no operation on old licenses' hours; U1-b: op 1 (Sunday sales removed from old licenses at first renewal) | CR-1 per reading |
| K5 No compensation | — | Not binding | None: the counterfactual law (the 1987 ruling) already denies a claim, so K5 changes no one's situation (CR-1, recording note: state the counterfactual law) | — |

The repeal ends a fixed number of sellers with a free price. Under CR-6 the license's price and lease price were what rationed the fixed count; that pressure ends with the count.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| license_holders.operating | Package stores that own their license | Op 1: license no longer saleable or leasable; op 3: fee $5,000; face entry; U1-b: op 1 on Sunday |
| license_holders.lessors | About 560 non-operating holders | Op 1: no one will lease a license after 1 December 2028 |
| lessees.operators | Package stores operating on a leased license | Op 2: can hold their own license for $5,000 instead of a lease |
| license_holders.supermarkets | Chains holding about 140 licenses | Op 1 on license value; op 2: may license every store |
| license_holders.borrowing | Holders with about $210 million of license-secured loans | Collateral loses value (CR-9, contract) |
| sellers.prospective | Supermarkets, convenience stores, standalone entrants | Op 2: may enter for the fee (CR-4, x: stay out, y: enter) |
| prospective_license_buyers | Those who would have bought one of about 90 licenses a year | Op 2: enter without buying a license |
| buyers.current | Merrowind buyers of wine and spirits | More, nearer sellers (CR-9); U1-b: no Sunday off-premises sales |
| buyers.border | Residents within 30 minutes of Ashcombe | CR-4 (x: buy in Ashcombe, y: buy at home) |
| sellers.ashcombe | Ashcombe stores selling to Merrowind residents | CR-9 (across_border) |
| sellers.on_premises | Bars and restaurants | CR-9 (substitute, A-19) |
| sellers.complements | Sellers of mixers, snacks, ice, groceries | CR-9 (trip complement, A-20) |
| wholesalers | The 12 licensed wholesalers | CR-9 (input_to) |
| landlords.small_retail_units | Owners of small units in commercial zones | CR-9 (input_to: premises for new outlets) |
| tenants.other_small_retail | Other businesses renting small units | CR-9 (compete for the same units) |
| banks.license_lenders | Three regional banks | CR-9 (contract: loans secured by licenses) |
| workers.package_stores, workers.entrants | Employees | CR-9, LW-10 (input_to) |
| officials.enforcement | Alcohol Control Board | Op 3: must process applications from 1 June 2028 with an unchanged appropriation (A-17) |
| state.general_fund | Receives fees, excise, sales tax | CR-8b |
| neighbors.new_outlets | Owners next to new outlets | CR-9 (proximity, Tier C) |
| home_buyers.near_outlets | Buyers of homes near outlets | CR-9 (complement, location) |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | sellers.prospective | entry_rate (off-premises liquor retail) | increase | short (first year from Dec 2028); medium | CR-1 op 2, CR-4, CR-7a | A-1, A-3 |
| C-2 | sellers.off_premises (all) | number_of_sellers | increase | medium; long | CR-4, CR-7a, CR-6 | A-1, A-3 |
| C-3 | license_holders (operating, lessors, supermarkets) | asset_value (licenses) | decrease | short (from Feb 2027, mostly at passage) | CR-7c, CR-10c, CR-6 | A-1, A-2 |
| C-4 | state.general_fund | non_tax_receipts (license fees) | increase | medium | CR-1 op 3, CR-8b | A-3 |
| C-5 | license_holders.continuing | resources_available_other_uses | decrease | medium | CR-1 op 3, CR-3c, CR-8b | none |

## 5. Responses

CR-4 for every pair of options of each class; CR-6 for the end of the fixed count; CR-10a for the 18-month window.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | buyers.current | price_paid (wine and spirits, off-premises) | decrease | medium; long | CR-6, CR-7a, CR-12e | A-1, A-3, A-4, A-13 |
| C-7 | buyers.current | price_paid (window Jun 2027 to Nov 2028) | decrease | short (window) | CR-10a, CR-6 | A-16 |
| C-8 | buyers.current | travel_time | decrease | medium; long | CR-4, CR-9 | A-3, A-5 |
| C-9 | buyers.current | quantity_traded (off-premises wine and spirits bought in Merrowind) | U1-a: increase; U1-b: ambiguous | medium; long | CR-4c, CR-12b | A-4, A-5, A-6, A-18 |
| C-10 | buyers.current | quantity_traded (storable purchases in the window before 1 Dec 2028) | decrease | short (window) | CR-10a, CR-4 | A-15 |
| C-11 | buyers.current | quantity_traded (purchases deferred from the window, made after 1 Dec 2028) | increase | short (first months after Dec 2028) | CR-10a, CR-4 | A-15 |
| C-12 | buyers.border | cross_border_purchases | U1-a: decrease; U1-b: ambiguous | medium; long | CR-4, CR-12b | A-6, A-25 |
| C-13 | buyers.current | quantity_traded (Sunday off-premises sales in Merrowind) | U1-a: ambiguous; U1-b: decrease | medium; long | CR-1 op 1 (U1-b), CR-12b (U1-a) | A-7, A-21 |
| C-14 | license_holders.operating | net_price_received | decrease | medium; long | CR-6, CR-7a, CR-7b | A-1, A-3, A-4 |
| C-15 | license_holders.operating | quantity_traded (sales per package store) | decrease | medium; long | CR-4, CR-9 | A-3, A-5 |
| C-16 | license_holders.operating | number_of_sellers (package stores) | decrease | medium | CR-4, CR-4 0.8 note | A-7 |
| C-17 | license_holders.operating (stores that stay) | quality_per_unit (service, selection, hours) | increase | medium; long | CR-4 | A-14 |
| C-18 | license_holders.operating | inventory_held (into Dec 2028) | decrease | short (window) | CR-10a, CR-10b | A-16 |
| C-19 | license_holders.lessors | right_lease_price (use after 1 Dec 2028) | decrease | short (from passage) | CR-6, CR-7c | A-1, A-2 |
| C-20 | license_holders.lessors | resources_available_other_uses | decrease | medium | CR-8b | A-1 |
| C-21 | lessees.operators | resources_available_other_uses | ambiguous | medium | CR-8b, CR-12b | A-1, A-3, A-4 |
| C-22 | prospective_license_buyers | resources_available_other_uses | increase | medium; long | CR-8a, CR-8b | A-1, A-3 |
| C-23 | license_holders (all) | lobbying_effort (for compensation or restoration of the cap) | ambiguous | short; medium | CR-4 0.9 note, CR-12b | A-8, A-9 |
| C-24 | sellers.prospective (grocers' association) | lobbying_effort (over the cap) | ambiguous | short; medium | CR-4 0.9 note, CR-12b | A-9, A-N4 |
| C-25 | license_holders.old, sellers.new | lobbying_effort (Sunday sales) | U1-a: increase; U1-b: increase | medium | CR-4, CR-8c | A-26, A-8, A-N3 |
| C-26 | applicants (sellers.prospective) | wait_time (license applications) | increase | short (Jun 2028 to 2029) | CR-6 0.7 public supply, CR-8a | A-3, A-17 |
| C-27 | sellers.off_premises (all) | legal_breach (underage sales) | increase | short | CR-4 | A-17, A-N1 |
| C-28 | sellers.prospective | investment_target (premises and fit-out for new outlets) | increase | short (from Jun 2028); medium | CR-10a, CR-4 | A-2, A-3 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7. Depth limit 4. Effects on customers of businesses displaced from small retail units are pruned at depth 3 as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-29 | landlords.small_retail_units | price_paid (rent of small retail units in commercial zones) | increase | short; medium | CR-9, CR-6 0.9 | units input_to new outlets (close) | A-3, A-13 |
| C-30 | tenants.other_small_retail | quantity_traded (small units rented for other uses) | decrease | short; medium | CR-9, CR-4c, CR-8a | other tenants compete for the same units | A-3, A-13 |
| C-31 | wholesalers | quantity_traded (deliveries to Merrowind retailers) | U1-a: increase; U1-b: ambiguous | medium; long | CR-9, LW-10 | wholesale input_to retail (close; three-tier rule) | A-4, A-5, A-6, A-18 |
| C-32 | wholesalers | quantity_traded (deliveries, autumn 2028) | decrease | short (window) | CR-9, CR-10a | input_to | A-16 |
| C-33 | sellers.ashcombe | quantity_traded (sales to Merrowind residents) | U1-a: decrease; U1-b: ambiguous | medium; long | CR-9, CR-12b | across_border (close within 30 minutes) | A-6, A-25 |
| C-34 | sellers.ashcombe | quantity_complement (groceries bought on liquor trips) | U1-a: decrease; U1-b: ambiguous | medium; long | CR-9, CR-12b | complement (trip) | A-6, A-20, A-25 |
| C-35 | sellers.prospective (supermarkets, convenience stores) | quantity_complement (mixers, snacks, ice, groceries) | increase | medium | CR-9 | complement (trip) | A-3, A-5, A-20 |
| C-36 | license_holders.operating | quantity_complement (mixers, snacks, ice) | decrease | medium | CR-9 | complement (trip) | A-5, A-20 |
| C-37 | sellers.on_premises | quantity_substitute (drinks served in bars) | U1-a: decrease; U1-b: ambiguous | medium; long | CR-9, CR-12b | substitute (partial) | A-4, A-19 |
| C-38 | workers.package_stores | employment (package stores) | decrease | medium | CR-9, LW-10 | labor input_to package stores | A-7 |
| C-39 | workers.entrants | employment (liquor departments and new stores) | increase | medium | CR-9, LW-10 | labor input_to new outlets | A-3, A-23 |
| C-40 | workers.off_premises_retail | employment (off-premises wine and spirits retail, total) | ambiguous | medium | CR-12b | as above | A-3, A-7, A-23 |
| C-41 | banks.license_lenders | asset_value (license-secured loans) | decrease | short; medium | CR-9, CR-7c | contract (loans secured by licenses) | A-1, A-10 |
| C-42 | license_holders.borrowing | interest_rate (+), transaction_size (−) | at_least_one_as_stated | short; medium | CR-9, CR-5c | contract | A-1, A-N2 |
| C-43 | banks.license_lenders | quantity_traded (new loans to buy licenses) | decrease | medium; long | CR-9, LW-10 | loans input_to license purchases | A-1 |
| C-44 | state.general_fund | tax_revenue (liquor excise) | U1-a: increase; U1-b: ambiguous | medium; long | CR-9, CR-8b | excise per gallon on Merrowind sales | A-4, A-5, A-6, A-18 |
| C-45 | state.general_fund | tax_revenue (liquor excise, autumn 2028) | decrease | short (window) | CR-10a, CR-8b | as above | A-16 |
| C-46 | state.general_fund | tax_revenue (sales tax on wine and spirits) | ambiguous | medium; long | CR-12b | as above | A-4, A-6 |
| C-47 | home_buyers.near_outlets | asset_value (homes near new outlets), not counting effects through proximity | increase | medium; long | CR-9, CR-7c | complement (location) | A-3, A-11 |
| C-48 | neighbors.new_outlets | asset_value (homes next to new outlets), combined with proximity effects | ambiguous | medium; long | CR-9 0.7, CR-12 0.9 | proximity (Tier C) and complement (location) | A-11, A-12 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| buyers.current, price_paid, medium; long | K2 raises a per-outlet fixed cost (bears on whether outlets operate, not on the unit price, CR-4 0.8 note; signed only with an entry premise) | End of the fixed count and entry (CR-6, CR-7a; A-1, A-3, A-4) | Response argument (CR-12e): exit of package stores (A-7) is a response to the lower price and cannot reverse it; entry is partial in the medium run (A-13), so prices fall but not to the never-capped level at once | decrease (C-6) |
| buyers.current, quantity_traded, medium; long | Lower price, nearer outlets, purchases brought home (A-4, A-5, A-6) | U1-a: Sunday purchases lost where old-license stores close (A-7); U1-b: all Sunday off-premises sales removed (CR-1 op 1) | U1-a: A-18 (p 0.7) states the Sunday loss is few against the gains; U1-b: none | U1-a: increase; U1-b: ambiguous (C-9) |
| buyers.border, cross_border_purchases | U1-b: Sunday trips to Ashcombe (A-25) | Lower prices and grocery sales at home (A-6) | None | U1-a: decrease; U1-b: ambiguous (C-12). Mirrored in C-33, C-34 |
| buyers.current, Sunday quantity | U1-a: uniform daily pricing lets Sunday prices fall with weekday competition (A-21, A-4) | U1-a: old-license stores close (A-7) | None | U1-a: ambiguous; U1-b: decrease (C-13) |
| sellers.on_premises, quantity_substitute | U1-b: Sunday drinkers move to bars (A-19) | Cheaper off-premises drinks (A-4, A-19) | None under U1-b | U1-a: decrease; U1-b: ambiguous (C-37) |
| lessees.operators, resources_available_other_uses | Lease of about $30,000 replaced by a $5,000 fee (arithmetic, A-1) | Lower margins and sales (C-14, C-15) | None | ambiguous (C-21) |
| license_holders, lobbying_effort | Compensation, restoration and Sunday campaigns (A-8) | No longer defending the cap against initiatives, as on the counterfactual path (A-9) | None (CR-4 0.9 note) | ambiguous (C-23) |
| grocers, lobbying_effort | Defending the repeal (A-N4) | Twenty-year campaign against the cap ends (A-9) | None | ambiguous (C-24) |
| workers, employment (total) | Entrants staff up (A-23) | Package stores close (A-7) | None | ambiguous (C-40) |
| state, sales tax on wine and spirits | More units taxed at home (A-6) | Lower price per unit (A-4) | None | ambiguous (C-46) |
| neighbors, asset_value of homes | Location complement (A-11, Tier B) | Traffic, litter (A-12, proximity, Tier C) | None | Tier B: increase, not counting proximity (C-47); combined at Tier C: ambiguous (C-48) |
| license_holders.operating, net_price_received | — | Entry (CR-6, CR-7a); K2 fee | — | decrease (C-14). Under U1-a the Sunday exclusivity keeps a part of the rent; it does not raise the price above the counterfactual, where the same holders already had Sunday and every other day |

Not combined (CR-12g): C-10 (window, decrease) and C-11 (after 1 December 2028, increase) are one timing shift signed per window; C-7 (window) and C-6 (medium) likewise.

## 8. Time structure

- **Expectation.** The bill became expected on introduction (2 February 2027) and near-certain on passage and signing (May to June 2027) by large margins with no referendum petition (A-2). License values fall in steps as passage becomes more likely (CR-7c, "becomes expected" is a matter of probability), so the loss is shared among those who held licenses as the probability rose; most of it falls on holders at passage (C-3). Leases for use after 1 December 2028 lose their value at the same time (C-19).
- **Window, June 2027 to November 2028.** The cap still binds. Buyers who expect lower prices defer storable purchases (A-15; C-10), and incumbents run down stock into December 2028, selling some off (A-16; C-18, C-7, C-32, C-45). Applications open 1 June 2028 and fixed staff process them (A-17; C-26). Entrants rent and fit out premises before the effective date (C-28), which bids up small units (C-29).
- **After 1 December 2028.** Deferred purchases are made (C-11). Entry proceeds as fast as premises allow: small units are limited for one to two years (A-13), so prices fall partly at first and further as units and rezonings arrive (C-6). Package stores that cannot cover costs at lower margins and the higher fee exit over the following years (C-16), as leases and stock run off (CR-10b).
- **Sunday.** Under U1-b, Sunday off-premises sales end for old licenses at their first renewal on 1 December 2028 (C-13). Under U1-a, Sunday sales remain only at old-license stores; as some close (A-7), the set of Sunday sellers shrinks and cannot be replenished: a fixed, declining group with an exclusive right, which is a remnant of the cap that persists in full.
- **Belief in the repeal.** Standalone entrants' fear of the cap's return (A-22, p 0.25) is below the cut-off, so long-payback entry is not reported as held back. The lobbying contest continues in another form (C-23, C-24, C-25).
- **Persistence (habits and siting).** Habits of buying in Ashcombe and stores sited where licenses could be had cost something to change (A-24), so the cap's effects on cross-border buying and store locations persist partly in the medium run.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-5 | license_holders.continuing | resources_available_other_uses | decrease | $4,000 a year more per license that holders keep paying | CR-3c, CR-8b |
| C-20 | license_holders.lessors | resources_available_other_uses | decrease | Lease income of $26,000 to $34,000 a year per license | CR-8b |
| C-22 | prospective_license_buyers | resources_available_other_uses | increase | The ~$400,000 per license (about 90 a year) no longer paid to a holder: the means stay with the entrant | CR-8a, CR-8b |
| C-23, C-24, C-25 | holders, grocers, entrants | lobbying_effort | as signed | Resources spent lobbying are used up | CR-8c |
| C-26 | applicants | wait_time | increase | Time before a new outlet can open | CR-6, CR-8a |
| C-30 | tenants.other_small_retail | quantity_traded (small units rented for other uses) | decrease | Other shops not opened in units taken by liquor outlets | CR-8a |
| C-41 | banks.license_lenders | asset_value (loans) | decrease | Loan repayments not received | CR-8b |

Both sides of each transfer: the fee raised (C-5) is received by the general fund (C-4); the lease payments lessors lose (C-20) are kept by lessees (C-21's (+) chain); the license price that holders can no longer receive (C-3) is kept by prospective buyers (C-22). The general fund's total receipts are not signed: fees rise (C-4), excise depends on the reading (C-44) and sales tax is ambiguous (C-46), so the group of taxpayers and recipients of other spending gets no sign (CR-12b, kind 3). Buyers' `resources_available_other_uses` is not signed: a lower price leaves more for other uses only if quantity does not rise to absorb it (CR-3 note, CR-4 exception). The Board's appropriation is unchanged in year 1 (A-17), so its money spending does not change; its staff time is redirected from compliance checks to applications (CR-8a; C-26, C-27).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The cap binds: more outlets would operate without it. | binding | 0.95 | Licenses sell for about $400,000 and lease for about $30,000 a year. | C-1, C-2, C-3, C-6, C-14, C-19 to C-22, C-41 to C-43 fail. |
| A-2 | Holders, buyers of licenses and entrants expect the repeal to last. | expectations | 0.8 | Votes of 41 to 9 and 112 to 38; no referendum petition. | C-3, C-19, C-28 weaken. |
| A-3 | Entry pays for some supermarkets, convenience stores and standalone stores at a $5,000 fee. | alternative_uses | 0.85 | Ashcombe's licenses at $3,000; Board projects 2,000 to 3,000 applications. | C-1, C-2, C-4, C-6, C-8, C-15, C-26, C-28 to C-30, C-35, C-39, C-47 fail. |
| A-4 | Part of the cap's rent is in the money price. | other | 0.7 | The 11% basket gap after excise. | C-6, C-9, C-14, C-37, C-44 fail. |
| A-5 | New outlets are nearer to some buyers. | other | 0.85 | 3,750 supermarkets and convenience stores against 2,380 package stores. | C-8, C-9, C-15, C-35, C-36 fail. |
| A-6 | Some border residents bought in Ashcombe for price or grocery sales, and some now buy at home. | mobility | 0.75 | Revenue department's 7%; 1.1 million within 30 minutes. | C-9, C-12, C-33, C-34, C-44 fail. |
| A-7 | Some package stores do not cover costs at lower margins and sales and the higher fee. | alternative_uses | 0.7 | Small stores near supermarkets; Ashcombe's outlet mix. | C-16, C-38, C-40, C-13 (U1-a chain) fail. |
| A-8 | Holders can organize to seek compensation and Sunday rights at a cost below their stake. | other | 0.8 | Holders' association's campaigns. | C-23, C-25 fail. |
| A-9 | On the counterfactual path the cap stays contested, with holders and grocers lobbying. | other | 0.8 | Twenty years of campaigns; initiatives 2019 and 2023. | C-23, C-24 become increases. |
| A-10 | Some license-secured loans exceed the license's value after the repeal, and some borrowers cannot cover the shortfall. | other | 0.7 | Loans up to 60% of value; recent purchases. | C-41 fails. |
| A-11 | Some home buyers bid more for homes near an off-premises outlet. | other | 0.55 | Listings mentioning walking distance to shops. | C-47 fails; C-48 loses its (+) chain. |
| A-12 | Owners next to new outlets rank less traffic, litter and late activity above their absence. | other | 0.6 | Objections at Ashcombe hearings. | C-48 loses its (−) chain. |
| A-13 | Small retail units cannot be fully expanded at the old cost within a year or two. | durability | 0.75 | 5% vacancy; rezonings of 12 to 24 months. | C-29, C-30 fail; C-6's persistence becomes none. |
| A-14 | Incumbents who stay invest in service, selection and hours. | other | 0.6 | Package stores' responses in Ashcombe. | C-17 fails. |
| A-15 | Some buyers expect lower prices and delay storable purchases. | expectations | 0.6 | Press coverage; wine and spirits keep. | C-10, C-11 fail. |
| A-16 | Some incumbents cut stock into December 2028 and sell some off at lower prices. | expectations | 0.6 | Six weeks of stock; lower expected margins. | C-7, C-18, C-32, C-45 fail. |
| A-17 | The Board's appropriation is not raised with its workload in the first year. | revenue_use | 0.75 | No appropriation in the Act. | C-26, C-27 fail. |
| A-18 | Under U1-a, Sunday purchases lost where old-license stores close are few against purchases added. | other | 0.7 | Sunday is 9% of package-store revenue; only some stores close. | C-9, C-31, C-44 become ambiguous under U1-a. |
| A-19 | Off-premises drinks and drinks in bars are substitutes for some buyers. | substitutability | 0.6 | Ashcombe spending after supermarket sales began. | C-37 fails. |
| A-20 | Some buyers buy mixers, snacks, ice and groceries on the same trip. | other | 0.8 | Package stores' sales mix. | C-34 to C-36 fail. |
| A-21 | Old-license stores price the same every day of the week. | other | 0.6 | Shelf pricing practice. | C-13's U1-a (+) chain fails, giving decrease under U1-a. |
| A-22 | Standalone entrants fear the cap's return within their payback period. | expectations | 0.25 | Holders' lobbying; against it, the Act's margins and no petition. | Below the cut-off: see Not reported. |
| A-23 | Entrants staff liquor departments and new stores with added employees. | alternative_uses | 0.7 | Ashcombe supermarkets' staffing. | C-39 fails; C-40 becomes decrease. |
| A-24 | Habits of buying in Ashcombe, and stores sited where licenses could be had, cost something to change. | reversal_cost | 0.8 | Commuting and shopping patterns; store leases. | Persistence of C-6, C-8, C-12 becomes none in the medium run. |
| A-25 | Under U1-b, some residents near the line buy on Sunday in Ashcombe. | mobility | 0.7 | Ashcombe Sunday sales; 30-minute trips. | C-12, C-33, C-34 become decrease under U1-b. |
| A-26 | On the counterfactual path nobody lobbies over Sunday off-premises sales. | other | 0.8 | No Sunday bill since 2012. | C-25 becomes ambiguous. |
| A-N1 | With licensing staff fixed (A-17) and more outlets, compliance checks per outlet fall, and some sellers at the margin sell to underage buyers more often. | enforcement | 0.55 | NEW. 18 staff; 2,000 to 3,000 applications; compliance checks are the Board's enforcement means. | C-27 fails. |
| A-N2 | Lenders size or price loans by collateral, so borrowers whose license collateral falls pay more or borrow less on renewal. | other | 0.8 | NEW. Banks lend up to 60% of appraised license value. | C-42 fails. |
| A-N3 | Entrants (through the grocers' association) can organize to seek Sunday hours for new licenses at a cost below their stake. | other | 0.75 | NEW. The association's twenty-year campaign; K3 denies Sunday to every new license. | C-25 rests on A-8 only (U1-b) and on holders defending (U1-a). |
| A-N4 | The grocers' association spends on defending the repeal against holders' efforts to restore the cap or win compensation. | other | 0.55 | NEW. Holders' organized campaign (A-8); grocers' existing organization. | C-24 becomes decrease. |

**Not reported** (an assumption below 0.5):
- Standalone entry held back by fear of the cap's return (CR-10a; CR-4, x: enter now, y: wait): needs A-22 (p 0.25).
- Informal or unlicensed trade: the case records none on the counterfactual path, so no chain through CR-11b is derived.

## 11. Report

**The policy:** From 1 December 2028 Merrowind ends its 1949 cap of one package-store license per 2,500 residents. The Board must license any qualified applicant in a commercial zone; licenses are no longer transferable; every license pays $5,000 a year instead of $1,000; new licenses may sell Monday to Saturday only. Whether old licenses keep Sunday sales is unclear (U1). Holders get no compensation, which they could not have claimed anyway.

**Visible consequences:** Supermarkets, convenience stores and new stores enter (C-1, C-2). License holders lose the sale value of their licenses, mostly at passage in 2027 (C-3). The state collects more in license fees (C-4), paid by holders who keep operating (C-5). Prices fall (C-6) and, under U1-a, Merrowind residents buy more wine and spirits at home (C-9).

**Invisible consequences:**
- *Buyers:* shorter trips (C-8); lower prices in the window as stock is run down (C-7); purchases deferred into December 2028 (C-10, C-11); fewer purchases in Ashcombe under U1-a (C-12); Sunday buying falls under U1-b (C-13).
- *Package stores:* lower prices and sales per store (C-14, C-15), with some closing (C-16) and the others improving service (C-17); less stock before the effective date (C-18). Lessors lose lease income (C-19, C-20). License-secured loans lose value (C-41) and borrowers face tighter terms (C-42). Package-store employment falls (C-38), while entrants hire (C-39).
- *Entrants and other businesses:* license buyers who would have paid a holder keep the money (C-22); entrants invest in premises (C-28), wait for licenses (C-26) and bid up small retail units (C-29), crowding out other tenants (C-30). Supermarkets sell more mixers and groceries on liquor trips (C-35), package stores fewer (C-36). Banks make fewer loans to buy licenses (C-43).
- *Outside the state and other markets:* Ashcombe stores lose Merrowind sales and grocery trips under U1-a (C-33, C-34); bars sell fewer drinks under U1-a (C-37); wholesalers deliver more under U1-a (C-31) but less in autumn 2028 (C-32).
- *State:* excise rises under U1-a (C-44), falls in autumn 2028 (C-45); the Board's fixed staff checks outlets less often, and underage sales rise (C-27). Sunday sales become a new lobbying issue (C-25).

**Ambiguous effects:** Total wine and spirits bought in Merrowind, purchases in Ashcombe, bar sales, wholesaler deliveries and excise under U1-b (C-9, C-12, C-31, C-33, C-37, C-44): the end of Sunday sales pushes against the effects of entry. Sunday sales under U1-a (C-13): store closures against lower uniform prices. Lessees' means (C-21): lease saved against lower margins. Total liquor retail employment (C-40). Sales-tax revenue (C-46). Lobbying by holders and grocers (C-23, C-24), compared with a counterfactual where the cap stays contested. Home values next to new outlets at Tier C (C-48).

**Key conditions:** The cap binds (A-1, 0.95) and entry pays at $5,000 (A-3, 0.85); part of the rent is in the price (A-4, 0.7); small units cannot expand quickly (A-13, 0.75), which decides how fast prices fall; the reading of U1 decides the sign of six consequences. Added premises: fewer compliance checks per outlet (A-N1, 0.55), lenders price by collateral (A-N2, 0.8), entrants organize on Sunday hours (A-N3, 0.75), grocers defend the repeal (A-N4, 0.55).

**What this analysis cannot say:** Sizes, including how far prices fall, how many package stores close and whether total employment rises; whether holders, whose loss was a windfall to earlier holders, deserve compensation; net welfare. Health and safety effects of more outlets and more drinking (including underage drinking) are out of scope for version 1; C-27 records only the change in breaches of the underage-sale rule.

### Metamorphic check (repeal against the original rule)

No earlier analysis of the 1949 cap is used; its effects are derived first from the core rules, against the path with no cap.

| Original effect of the cap (derived) | Core rules | Under the repeal | Consequence |
| --- | --- | --- | --- |
| Fewer outlets (op 1 for would-be sellers) | CR-1, CR-4, CR-7a | Reverses; partly in the medium run (A-13, A-24) | C-1, C-2 |
| License value created and captured by holders when the cap and each census count became expected | CR-6, CR-7c, CR-10c | The value goes, but the loss falls on current holders, not on those who captured the windfall: not a reversal of who gained | C-3 |
| Higher prices to buyers (A-4) | CR-6, CR-7b | Reverses, partly in the medium run | C-6, C-14 |
| Longer trips to fewer stores | CR-4, CR-9 | Reverses, partly while siting persists (A-24) | C-8 |
| More cross-border buying in Ashcombe | CR-4 (x: here, y: there) | U1-a: reverses, partly in the medium run (habits, A-24); U1-b: ambiguous because of Sunday | C-12, C-33 |
| A lease market and lending against licenses | CR-6, CR-9 | Reverses (lease price and new license loans fall to nothing); existing loans' losses persist as realized losses | C-19, C-41, C-43 |
| Supermarkets kept out of liquor; package stores' trip sales | CR-1, CR-9 | Reverses | C-35, C-36 |
| Package-store employment above the uncapped level | CR-9, LW-10 | Reverses as stores close | C-38 |
| Lobbying to defend and to end the cap | CR-4 | Neither reverses nor persists unchanged: it changes object (compensation, Sunday) | C-23 to C-25 |
| Sunday sales for every licensee (2012) | CR-1 op 2 | Not a cap effect. U1-a: kept by old licenses only, a fixed and shrinking privileged group (persists in full); U1-b: ended, a new restriction the original path never had | C-13, C-25 |
| Excise collected on fewer Merrowind gallons | CR-8b, CR-9 | U1-a: reverses; U1-b: ambiguous | C-44 |

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | sellers.prospective | entry_rate (off-premises liquor retail) | increase | short (first year from Dec 2028); medium | visible | B | CR-1 (op 2: K1 adds the option of a license for any qualified applicant); CR-4 (x: stay out, y: enter; y newly open, and by CR-3b adding an option, even with K2's fee attached, cannot make an entrant worse off); CR-7a (means move toward the yield the cap held up) | A-1, A-3 | partial (short); none (medium, long) |
| C-2 | sellers.off_premises (all) | number_of_sellers | increase | medium; long | visible | B | CR-4 and CR-7a (entry, C-1, exceeds exit, C-16: entrants come in because yields exceed costs, and exit is limited to stores that cannot cover costs); CR-6 (the fixed count no longer holds; pressure moves to entry) | A-1, A-3 | partial (medium, A-13, A-24); none (long) |
| C-3 | license_holders (operating, lessors, supermarkets) | asset_value (licenses) | decrease | short (from Feb 2027, mostly at passage) | visible | B | CR-6 (under a cap on the number of sellers the license price rations the count; with the count gone, so is the rationing value); CR-7c (the change is borne by whoever holds the license when it becomes expected, in steps as passage became likely); CR-10c; K1: no sale after Dec 2028. Under U1-a the Sunday privilege keeps some value by the holder's own ranking (CR-7 0.9), but not a sale value | A-1, A-2 | U1-a: partial (Sunday privilege); U1-b: none |
| C-4 | state.general_fund | non_tax_receipts (license fees) | increase | medium | visible | B | CR-1 (op 3: K2 attaches $5,000 to holding a license); CR-8b (the fund receives what licensees pay); arithmetic: receipts exceed the counterfactual $2.38 million once 476 licenses pay, and entry (A-3) adds to the incumbents who renew | A-3 | n/a (new effect) |
| C-5 | license_holders.continuing | resources_available_other_uses | decrease | medium | visible | A | CR-1 (op 3: $4,000 more per license); CR-3 note (they keep paying the burdened option); CR-3c, CR-8b | none | n/a (new effect) |
| C-6 | buyers.current | price_paid (wine and spirits, off-premises) | decrease | medium; long | visible | B | CR-6 (the rent held in the price, A-4, was the pressure of a fixed count; entry, C-1, removes it); CR-7a; CR-12e (response argument: exit of package stores responds to the lower price and cannot reverse it); CR-12 0.9 (partial: units cannot be added fully at the old cost in one to two years, A-13, so the fall is gradual). K2 is a cost per outlet and bears on entry, not on the unit price (CR-4 0.8 note) | A-1, A-3, A-4, A-13 | partial (medium); none (long) |
| C-7 | buyers.current | price_paid (window Jun 2027 to Nov 2028) | decrease | short (window) | invisible | B | CR-10a (incumbents expecting lower margins run down stock and sell some off, A-16); CR-6 (more offered at each price in the window) | A-16 | n/a |
| C-8 | buyers.current | travel_time | decrease | medium; long | invisible | B | CR-4 (x: travel to a package store, y: buy at a nearer new outlet, A-5); CR-9 (more sellers, C-2) | A-3, A-5 | partial (medium, A-24); none (long) |
| C-9 | buyers.current | quantity_traded (off-premises wine and spirits bought in Merrowind) | U1-a: increase; U1-b: ambiguous | medium; long | visible | B | CR-4c (lower price, C-6, and nearer outlets: the last unit is now worth buying); CR-4 (x: Ashcombe, y: home, A-6). Against it: U1-a, Sunday purchases lost where old-license stores close (A-7), dominated by A-18 (CR-12e, empirical premise); U1-b, all Sunday off-premises sales removed (CR-1 op 1), no dominance premise (CR-12b) | A-4, A-5, A-6, A-18 | partial (medium); none (long) |
| C-10 | buyers.current | quantity_traded (storable purchases in the window before 1 Dec 2028) | decrease | short (window) | invisible | B | CR-10a; CR-4 (x: buy now, y: buy after the effective date at an expected lower price; wine and spirits keep, A-15) | A-15 | n/a |
| C-11 | buyers.current | quantity_traded (purchases deferred from the window, made after 1 Dec 2028) | increase | short (first months after Dec 2028) | invisible | B | CR-10a (the deferred purchases, C-10, are made after the date; a timing shift signed per window, `02_ontology.md` 2.5) | A-15 | n/a |
| C-12 | buyers.border | cross_border_purchases | U1-a: decrease; U1-b: ambiguous | medium; long | invisible | B | CR-4 (x: buy in Ashcombe, y: buy at home; y made better by lower prices and grocery sales at home, A-6); U1-b: CR-1 op 1 removes Sunday at home, so CR-4 (x: home, y: Ashcombe on Sunday) pushes the other way (A-25), no dominance premise (CR-12b) | A-6, A-25 | U1-a: partial (medium, A-24); none (long) |
| C-13 | buyers.current | quantity_traded (Sunday off-premises sales in Merrowind) | U1-a: ambiguous; U1-b: decrease | medium; long | invisible | B | U1-b: CR-1 (op 1: no license may sell on Sunday). U1-a: (−) CR-4 and CR-9: old-license stores that close (A-7) take their Sunday sales with them, and no new license may replace them; (+) CR-4c: uniform daily pricing (A-21) lowers Sunday prices with weekday competition; CR-12b | A-7, A-21 | n/a (not an effect of the cap) |
| C-14 | license_holders.operating | net_price_received | decrease | medium; long | invisible | B | CR-6 (the price no longer rations a fixed count); CR-7a (entry brings yields into line); CR-7b (the rent that settled on the immobile license is gone) | A-1, A-3, A-4 | none (long) |
| C-15 | license_holders.operating | quantity_traded (sales per package store) | decrease | medium; long | invisible | B | CR-4 (buyers' x: package store, y: nearer supermarket or convenience store, A-5); CR-9 (rivals compete for the same customers) | A-3, A-5 | none (long) |
| C-16 | license_holders.operating | number_of_sellers (package stores) | decrease | medium | invisible | B | CR-4 (x: operate, y: exit; lower margins and sales and the $5,000 fixed cost per outlet, CR-4 0.8 note, reverse the ranking for some, A-7) | A-7 | none |
| C-17 | license_holders.operating (stores that stay) | quality_per_unit (service, selection, hours) | increase | medium; long | invisible | B | CR-4 (x: keep terms, y: invest in service to keep customers; competition makes x worse); CR-6 (with the count gone, competition moves to non-price terms as well) | A-14 | none (long) |
| C-18 | license_holders.operating | inventory_held (into Dec 2028) | decrease | short (window) | invisible | B | CR-10a (expected lower margins after the date make holding stock across it less valuable); CR-10b (stock adjusts through purchases, six weeks' turnover) | A-16 | n/a |
| C-19 | license_holders.lessors | right_lease_price (use after 1 Dec 2028) | decrease | short (from passage) | invisible | B | CR-6 (the lease price rationed the fixed count); CR-7c (a lessee will not pay for use after the date of a right anyone may have for the fee) | A-1, A-2 | none |
| C-20 | license_holders.lessors | resources_available_other_uses | decrease | medium | invisible | B | CR-8b (lease payments of $26,000 to $34,000 a year cease: what lessees no longer pay, lessors no longer receive) | A-1 | none |
| C-21 | lessees.operators | resources_available_other_uses | ambiguous | medium | invisible | B | CR-12b: (+) CR-8b, arithmetic: the lease is replaced by a $5,000 fee; (−) CR-6, CR-7a: lower margins and sales (C-14, C-15). No dominance premise | A-1, A-3, A-4 | none (long) |
| C-22 | prospective_license_buyers | resources_available_other_uses | increase | medium; long | invisible | B | CR-8a and CR-8b (on the counterfactual about 90 buyers a year pay about $400,000 each to a holder; now they enter for the fee, and the means stay with them) | A-1, A-3 | none |
| C-23 | license_holders (all) | lobbying_effort (for compensation or restoration of the cap) | ambiguous | short; medium | invisible | B | CR-4 0.9 note (signed against a counterfactual in which holders defend a contested cap, A-9); (+) CR-4 (x: accept, y: lobby for compensation or restoration; stake made concrete by C-3, A-8); (−) no initiatives to defend against; CR-12b; CR-8c | A-8, A-9 | n/a |
| C-24 | sellers.prospective (grocers' association) | lobbying_effort (over the cap) | ambiguous | short; medium | invisible | B | CR-4 0.9 note; (−) the campaign against the cap ends (A-9); (+) CR-4 (x: accept holders' campaign, y: defend the repeal, A-N4); CR-12 0.8 kind 2 with p ≥ 0.5, so ambiguous | A-9, A-N4 | n/a |
| C-25 | license_holders.old, sellers.new | lobbying_effort (Sunday sales) | U1-a: increase; U1-b: increase | medium | invisible | B | Counterfactual: none (A-26), so CR-12 0.9 (an activity the policy creates). U1-a: new licenses lack Sunday while old ones keep it: CR-4 (x: accept, y: lobby for Sunday hours, A-N3) for entrants, and holders defend the privilege (A-8). U1-b: holders lobby to restore Sunday (A-8), entrants too (A-N3). CR-8c | A-26, A-8, A-N3 | n/a (new effect) |
| C-26 | applicants (sellers.prospective) | wait_time (license applications) | increase | short (Jun 2028 to 2029) | invisible | B | CR-6 0.7 (a public supplier with fixed capacity at a set price: the Board processes with fixed staff, A-17, and the pressure of 2,000 or more applications, A-3, goes to waiting); CR-8a | A-3, A-17 | n/a |
| C-27 | sellers.off_premises (all) | legal_breach (underage sales) | increase | short | invisible | B | CR-8a (fixed staff, A-17, redirected to applications and spread over more outlets: fewer checks per outlet); CR-4 (x: comply, y: violate; lower expected penalty, so sellers at the margin move to y, A-N1; CR-4a: none move the other way) | A-17, A-N1 | n/a |
| C-28 | sellers.prospective | investment_target (premises and fit-out for new outlets) | increase | short (from Jun 2028); medium | invisible | B | CR-10a (licenses become available on a known date, so premises are prepared before it); CR-4 (x: stay out, y: invest to enter) | A-2, A-3 | none (long) |
| C-29 | landlords.small_retail_units | price_paid (rent of small retail units in commercial zones) | increase | short; medium | invisible | B | CR-9 (relation: units input_to new outlets; entrants bid for them, LW-10); CR-6 0.9 (the split goes to price as well as quantity because units cannot be added fully within one to two years, A-13) | A-3, A-13 | n/a (new effect) |
| C-30 | tenants.other_small_retail | quantity_traded (small units rented for other uses) | decrease | short; medium | invisible | B | CR-9 (other tenants compete for the same units); CR-4c (at a higher rent the marginal tenant drops out); CR-8a (units taken by liquor outlets are withdrawn from other uses). Depth 3; further effects on those tenants' customers pruned as diffuse | A-3, A-13 | n/a |
| C-31 | wholesalers | quantity_traded (deliveries to Merrowind retailers) | U1-a: increase; U1-b: ambiguous | medium; long | invisible | B | CR-9 and LW-10 (relation: wholesale input_to retail under the three-tier rule; deliveries follow C-9, including the reading split); gallons moving from bars to stores (C-37) stay with the same wholesalers | A-4, A-5, A-6, A-18 | none (long) |
| C-32 | wholesalers | quantity_traded (deliveries, autumn 2028) | decrease | short (window) | invisible | B | CR-9 (input_to; retailers run down stock, C-18); CR-10a | A-16 | n/a |
| C-33 | sellers.ashcombe | quantity_traded (sales to Merrowind residents) | U1-a: decrease; U1-b: ambiguous | medium; long | invisible | B | CR-9 (relation: across_border; mirror of C-12, with the same opposing Sunday chain under U1-b, A-25) | A-6, A-25 | U1-a: partial (medium, A-24); none (long) |
| C-34 | sellers.ashcombe | quantity_complement (groceries bought on liquor trips) | U1-a: decrease; U1-b: ambiguous | medium; long | invisible | B | CR-9 (relation: complement, trip: groceries bought on the trip go with the trip, A-20; follows C-33) | A-6, A-20, A-25 | U1-a: partial (medium); none (long) |
| C-35 | sellers.prospective (supermarkets, convenience stores) | quantity_complement (mixers, snacks, ice, groceries) | increase | medium | invisible | B | CR-9 (relation: complement, trip; liquor buyers who now buy at supermarkets and convenience stores add trip items there, A-5, A-20) | A-3, A-5, A-20 | none |
| C-36 | license_holders.operating | quantity_complement (mixers, snacks, ice) | decrease | medium | invisible | B | CR-9 (complement, trip; follows C-15) | A-5, A-20 | none |
| C-37 | sellers.on_premises | quantity_substitute (drinks served in bars) | U1-a: decrease; U1-b: ambiguous | medium; long | invisible | B | CR-9 (relation: substitute, A-19); CR-4 (x: bar, y: buy to drink at home; y cheaper, C-6). U1-b: (+) Sunday buyers move to bars (CR-4, A-19); CR-12b | A-4, A-19 | none (long) |
| C-38 | workers.package_stores | employment (package stores) | decrease | medium | invisible | B | CR-9 and LW-10 (labor input_to package stores; stores close and sell less, C-16, C-15) | A-7 | none |
| C-39 | workers.entrants | employment (liquor departments and new stores) | increase | medium | invisible | B | CR-9 and LW-10 (labor input_to new outlets, A-23) | A-3, A-23 | none |
| C-40 | workers.off_premises_retail | employment (off-premises wine and spirits retail, total) | ambiguous | medium | invisible | B | CR-12b: C-39 (+) against C-38 (−); no premise on which is larger | A-3, A-7, A-23 | n/a |
| C-41 | banks.license_lenders | asset_value (license-secured loans) | decrease | short; medium | invisible | B | CR-9 (relation: contract, loans secured by licenses); CR-7c (collateral value falls, C-3, so loans that exceed it and whose borrowers cannot cover the shortfall lose value when the repeal becomes expected, A-10) | A-1, A-10 | n/a (realized once) |
| C-42 | license_holders.borrowing | interest_rate (+), transaction_size (−) | at_least_one_as_stated | short; medium | invisible | B | CR-9 (contract); CR-5c (the lender's acceptable terms move when collateral falls, A-N2); CR-6 group: price or size | A-1, A-N2 | n/a |
| C-43 | banks.license_lenders | quantity_traded (new loans to buy licenses) | decrease | medium; long | invisible | B | CR-9 and LW-10 (loans input_to license purchases; purchases end, C-22) | A-1 | none |
| C-44 | state.general_fund | tax_revenue (liquor excise) | U1-a: increase; U1-b: ambiguous | medium; long | invisible | B | CR-8b and CR-9 (excise per gallon follows gallons sold in Merrowind, C-9 and C-31, with the same reading split; cross-border gallons, C-12, come back into the base) | A-4, A-5, A-6, A-18 | none (long) |
| C-45 | state.general_fund | tax_revenue (liquor excise, autumn 2028) | decrease | short (window) | invisible | B | CR-9 (excise follows deliveries, C-32); CR-10a | A-16 | n/a |
| C-46 | state.general_fund | tax_revenue (sales tax on wine and spirits) | ambiguous | medium; long | invisible | B | CR-12b: (+) more units sold at home (A-6); (−) lower price per unit on an ad valorem tax (A-4) | A-4, A-6 | n/a |
| C-47 | home_buyers.near_outlets | asset_value (homes near new outlets), not counting effects through proximity | increase | medium; long | invisible | B | CR-9 (relation: complement, location: nearness to an outlet is bought with the home, A-11); CR-7c and CR-10c (the expected yield of nearness is capitalized for owners when outlets become expected) | A-3, A-11 | n/a (new effect) |
| C-48 | neighbors.new_outlets | asset_value (homes next to new outlets), combined with proximity effects | ambiguous | medium; long | invisible | C | CR-12 0.9 (Tier C against Tier B): C-47's chain (+) against CR-9 0.7 through proximity (traffic, litter, late activity, A-12) (−); no dominance premise | A-11, A-12 | n/a |

## Gaps found

**(a) Calculus gaps.**
- GAP-052-C1: Persistence of a privilege created by the transition clause. Under U1-a, old licenses keep Sunday sales while no new license can get them: the repeal creates a fixed, shrinking set of privileged sellers. CR-7c and CR-10b let the analyst say it persists, but `persistence` is defined against the never-imposed path, and this effect has no counterpart on either the counterfactual or the never-imposed path. No rule says how to record a repeal effect that is neither a reversal nor a remnant; recorded as "n/a (not an effect of the cap)".
- GAP-052-C2: Who captured the cap's value and who loses it are different people. The metamorphic check asks whether an effect "reverses"; for capitalized assets the value disappears (reverses) but the gain went to earlier holders and the loss falls on current ones. CR-7c covers both events, but the check's vocabulary (reverses, partly, persists) has no entry for a reversal borne by different actors.

**(b) Core-rule wording that was hard to apply.**
- CR-4 0.9 note (lobbying in repeals): it says the sign needs a premise where the old rule was contested, but gives no way to compare lobbying on one issue (defending the cap) with lobbying on a new one (compensation, Sunday). Holders' and grocers' lobbying both came out ambiguous; Sunday lobbying could be signed only because a separate premise said nobody lobbied over it on the counterfactual path (A-26).
- CR-12e response argument for prices after entry: the 0.9 note is written for an increase that a response cannot reverse; for a fall in price caused by entry, the mirror (exit cannot push the price back above the counterfactual) had to be inferred by symmetry.
- CR-6 0.7 public supply clause, applied to an agency's processing capacity (applications), fits only loosely: licenses are not "supplied" in a fixed quantity; the fixed quantity is staff time.
- CR-3 note on refunds and unavoidable sums: whether a lost income stream (lease income) counts as a sum the class "cannot avoid" for `resources_available_other_uses` is not stated; signed under CR-8b as the other side of a payment no longer made.

**(c) Vocabulary missing from the ontology.**
- No variable for the hours or days a seller may open (Sunday trading); recorded through `quantity_traded` with a Sunday qualifier.
- No actor class for lenders whose collateral is the target asset; `banks.license_lenders` was coined.
- `asset_value` covers both a sale value and a value by the holder's own ranking for an asset that cannot be sold (CR-7 0.9); a qualifier was needed for the Sunday privilege under U1-a.
- No variable for enforcement intensity per bound party (checks per outlet); expressed through `legal_breach` with a premise.
