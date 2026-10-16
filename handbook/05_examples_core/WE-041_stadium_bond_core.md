# WE-041 / Analysis: Stadium financed by city bonds and leased below market

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Merrowgate Riverside Stadium Agreement.** Merrowgate (about 610,000 people; metro about 1.5 million) has a general fund of about $1.9 billion a year and a 1% local sales tax. Its charter caps general-obligation (GO) debt at 3% of assessed value ($2.4 billion); outstanding GO debt is $1.55 billion, leaving $850 million of headroom, and the five-year capital plan lists $620 million of projects awaiting GO financing in 2027 to 2031 (school roofs, road resurfacing, a branch library). The Herons, a privately owned team in a 20-franchise league (new franchises and relocations need a three-quarters vote of owners), play at the team-owned Halcourt Bowl (35,000 seats, 1978) in the separate town of Halcourt, 14 km from Riverside; about half of home games sold out in the last three seasons. In 2024 the team said the Bowl needed a $210 million renovation and held talks with Selwick (400 km away) that ended without an offer. The Bowl pays Halcourt about $1.6 million a year in property tax. The Riverside site is a 22-acre city-owned former rail yard; in 2025 a developer offered $38 million for it for about 1,100 dwellings, and withdrew when the stadium deal was announced.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | City of Merrowgate. Halcourt, a separate town on its eastern edge, hosts the Bowl; Selwick is 400 km away. | "The Herons play at the Halcourt Bowl ... in Halcourt, a separate town on Merrowgate's eastern edge" |
| Announced / enacted / effective / expires | Announced 14 April 2026; approved 9 September 2026; bonds sold January 2027; construction 2027 to mid-2029; opens August 2029; lease to 2059; bonds to 2056. | "The deal was announced on 14 April 2026 ... The lease runs for 30 years from opening, to 2059." |
| Enforcement (who, penalties, resources) | The lease is a contract enforced in the courts; K4's penalty is the outstanding bond principal plus $50 million; city finance and property departments administer it. | K4, K5 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Bonds | `government_borrowing` | Stadium construction | City | $480 million of 30-year GO bonds at 4.2%; level debt service about $28.4 million a year, 2027 to 2056 (about $853 million), from the general fund; no new tax named | - |
| K2 Construction | `public_supply` of a facility | A 42,000-seat stadium on the Riverside site | City | Built on the city's land, which is not sold | - |
| K3 Lease | `lump_sum_subsidy` (in kind) | The Herons | City and team | Rent $1 million a year, fixed for 30 years (consultant's arm's-length estimate about $19 million); team keeps all revenue; team pays operating costs and routine maintenance (about $4 million a year) and major repairs in lease years 1 to 15 (about $1 million a year); years 16 to 30 per U1 (about $9 million a year) | - |
| K4 Non-relocation | `mandated_contract_term` | Home games | Team | All home games at Riverside for 30 years; relocation costs the outstanding principal plus $50 million | - |
| K5 Administration | Administration | K1 to K4 | City departments | Issuance about $3.1 million; lease administration about $0.4 million a year, from the general fund | - |

Counterfactual: Merrowgate without the agreement. On the evidence the Herons would have stayed at the Bowl and renovated it at their own cost in 2027-28 (A-1, p 0.7), and the city would have sold the site to the developer, who would have built about 1,100 dwellings (A-12, p 0.6). Every sign is against that path.

Horizons: short = 2026 to mid-2029 (announcement and construction); medium = August 2029 to 2043 (lease years 1 to 15); long = 2044 to 2059 (lease years 16 to 30).

Unclear provisions:
- U1, major capital repairs in lease years 16 to 30. Reading U1-a: the city, as owner, pays them. Reading U1-b: the team pays them under its general repair covenant. Readings, not assumptions; no probability is given.
- Not stated: whether the team owes property tax on the city-owned stadium. No sign below depends on it (checked in section 7).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Bonds | binary (the state borrows; taxes or other spending later repay) | Yes; repaid on schedule (A-18) | 4 (means transferred from general-fund payers to bondholders over 30 years, in exchange for $480 million lent now); uses debt headroom (A-15) | CR-8a, CR-8b, CR-8 0.7 note (borrowing), CR-4 0.7 note (means over time), CR-9 |
| K2 Construction | binary (public supply of a facility) | Yes | 2 (adds the option of a new stadium at Riverside); 1 for the developer (the site is not offered for sale, A-12) | CR-5a, CR-8a, CR-9 |
| K3 Lease | binary (in-kind subsidy to the team) | Yes | 2 (option to play at the new stadium at $1 million a year); 4 (value transferred in kind, about $18 million a year against the arm's-length rent); 3 per reading of U1 in years 16 to 30 | CR-3b, CR-7c, CR-8b, CR-10a, CR-10c |
| K4 Non-relocation | triangular in form (a contract term), agreed by the team | Yes for 30 years; binds little in the medium run if the team would have stayed anyway (A-1) | 3 (a penalty attached to the option "relocate") | CR-4, CR-7c, CR-10a |
| K5 Administration | binary | Yes | 4 (general fund to departments) | CR-8c |

The team takes the deal voluntarily (CR-5): it ranks the package above its alternative (A-1), so by CR-3b and CR-5 it is not made worse off by its own ranking at the time of choice. The city is not an actor with its own ranking; its choices are those of officials, and the burden falls on general-fund payers and recipients of other spending (CR-8 0.7 note).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| team.herons (owners) | Lessee | Op 2 and op 4 (new stadium at a rent far below arm's length); avoids the $210 million renovation (A-1); op 3 (relocation penalty) |
| taxpayers.merrowgate, recipients of other general-fund spending | Payers of debt service, administration and, under U1-a, repairs | Op 4 through the general fund for 30 years |
| users.capital_plan | Pupils, road users, library users served by the capital plan | Through CR-8a: projects deferred (A-15) |
| fans | Buyers of Herons tickets | Op 2: a new venue they value more (A-2), with 7,000 more seats |
| sellers.substitutes | Sellers of other outings in the metro (A-6) | Through CR-9 (substitute) |
| businesses.riverside | Bars, restaurants and shops near the new stadium | Through CR-9 (complement, trip): game-day customers (A-8); congestion (A-9, shared_facility); no residents of the forgone dwellings |
| businesses.halcourt | Businesses near the Bowl | Through CR-9 (complement, trip): game-day customers leave from 2029 |
| property_owners.riverside_commercial, property_owners.halcourt_commercial | Owners of commercial property near each stadium | CR-7c, CR-10c (A-10) |
| halcourt.town | Collects the Bowl's property tax | Through CR-9 (the Bowl's use changes) |
| developer | The 2025 bidder for the site | Op 1: the sale is not offered (CR-5a) |
| buyers.prospective (housing) | Would-be residents of the 1,100 dwellings and other Merrowgate renters and buyers | Through CR-9 (fewer dwellings) |
| residents.riverside, residents.halcourt | Neighbors of each stadium | Proximity and shared roads (Tier C) |
| construction_firms | Builders in the metro | Through CR-9 (input_to): stadium instead of renovation and housing |
| lenders, other domestic borrowers | Buyers of the bonds and those who compete for the same saving (A-14) | Through CR-9 and CR-8 0.7 note (borrowing) |
| officials.city_finance | Issue the bonds, administer the lease | K5 |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium | CR-1 op 4, CR-8a, CR-8b, CR-8 0.7 note | A-18, A-12 |
| C-2 | city.general_fund | subsidy_outlay (value of stadium use transferred below arm's-length rent) | increase | medium; long | CR-1 op 4, CR-8b | none |
| C-3 | team.herons | resources_available_other_uses | increase | short | CR-1 op 2, CR-3b, CR-8b | A-1 |
| C-4 | team.herons | asset_value (franchise) | increase | short (from 14 April 2026) | CR-7c, CR-10c, CR-12e | A-1, A-3, A-N1 |
| C-5 | fans | quality_per_unit (venue) | increase | medium; long | CR-1 op 2, CR-2 | A-1, A-2 |
| C-6 | officials.city_finance | enforcement_cost (bond issuance and lease administration) | increase | short; medium; long | CR-1 op 4, CR-8c | none |

## 5. Responses

CR-4 applied to every pair of options each actor class has (substitute, terms, evade, relocate, reclassify, exit, lobby, timing); CR-5 for prevented exchanges; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | fans | quantity_traded (Herons tickets) | increase | medium; long | CR-4, CR-6 | A-1, A-2, A-5, A-6 |
| C-8 | fans | price_paid (Herons tickets) | ambiguous | medium; long | CR-12b | A-1, A-2, A-5 |
| C-9 | team.herons | maintenance_spending (Halcourt Bowl, 2026 to mid-2029) | decrease | short | CR-10a, CR-4 (x: renovate, y: hold until the move) | A-1 |
| C-10 | team.herons | resources_available_other_uses | increase | medium | CR-8b, CR-12a, arithmetic | A-1, A-17, A-2 |
| C-11 | team.herons | resources_available_other_uses | U1-a: increase; U1-b: ambiguous | long | CR-12b per reading, arithmetic | A-1, A-17, A-2 |
| C-12 | team.herons | resources_available_other_uses | increase | whole period (2027 to 2059) | CR-12 0.7 note (whole period), arithmetic | A-1, A-17 |
| C-13 | team.herons | maintenance_spending (major repairs, lease years 11 to 15) | U1-a: decrease; U1-b: no_change | medium (2039 to 2043) | CR-10a, CR-4 (x: repair now at own cost, y: defer to year 16) | A-17 |
| C-14 | city.general_fund | subsidy_outlay (major repairs, lease years 16 to 30) | U1-a: increase; U1-b: no_change | long | CR-1 op 3 per reading, CR-8b | A-17 |
| C-15 | team.herons, city officials | lobbying_effort (dispute over U1) | increase | medium (approaching 2044); long | CR-4 (x: accept the other's reading, y: dispute), CR-8c | A-4 |
| C-16 | team.herons | lobbying_effort (for a further public subsidy as 2059 approaches) | increase | long | CR-10a, CR-4 (x: accept the lease end, y: seek a new deal) | A-N2 |
| C-17 | developer | quantity_traded (Riverside site) | decrease | short | CR-5a | A-12 |
| C-18 | users.capital_plan | quantity_traded (capital-plan projects completed 2027 to 2031) | decrease | medium (2027 to 2031) | CR-8a, arithmetic on the charter cap | A-15 |
| C-19 | users.capital_plan | quantity_traded (deferred capital-plan projects completed after 2031) | increase | long (after 2031) | CR-8a, CR-10a; 2.5 timing shift | A-15 |
| C-20 | city.general_fund | interest_rate (the city's later GO borrowing) | increase | medium; long | CR-11c, CR-5c | A-16 |

## 6. Second-order effects

CR-9 along named relations. Depth limit 4; effects on suppliers of the substitute outings and of Riverside businesses stop at depth 3 (diffuse). Chains through `shared_facility` and `proximity` are Tier C (CR-9 0.7 note).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-21 | sellers.substitutes | quantity_substitute (other outings in the metro) | decrease | medium; long | CR-9, CR-4 | Herons games substitute for other outings (partial) | A-1, A-2, A-6 |
| C-22 | sellers.substitutes | employment (other outings) | decrease | medium; long | CR-9, LW-10 | labor input_to other outings | A-1, A-2, A-6, A-7 |
| C-23 | businesses.riverside | quantity_traded | ambiguous | medium; long | CR-12b over three chains | complement (trip) with games; complement (location) with the forgone dwellings; shared_facility (roads) | A-8, A-9, A-12, A-N3 |
| C-24 | property_owners.riverside_commercial | asset_value | ambiguous | short (from 14 April 2026) | CR-7c, CR-10c, CR-12b | as C-23 | A-8, A-9, A-10, A-12, A-N3 |
| C-25 | businesses.halcourt | quantity_traded | decrease | medium | CR-9 | complement (trip) with games at the Bowl | A-1, A-8, A-11 |
| C-26 | businesses.halcourt | quantity_traded | ambiguous | long | CR-12b | as C-25; complement (location) with redevelopment of the Bowl site | A-1, A-8, A-13 |
| C-27 | businesses.halcourt | employment | decrease | medium | CR-9, LW-10 | labor input_to game-day sales | A-1, A-7, A-8, A-11 |
| C-28 | property_owners.halcourt_commercial | asset_value | ambiguous | short (from 14 April 2026) | CR-7c, CR-10c, CR-12b | as C-26 | A-1, A-8, A-10, A-13 |
| C-29 | halcourt.town | tax_revenue (property tax on the Bowl site) | decrease | medium | CR-9, CR-10b | the Bowl site's use | A-1, A-11 |
| C-30 | halcourt.town | tax_revenue (property tax on the Bowl site) | increase | long | CR-9, CR-7a | the Bowl site's use | A-13 |
| C-31 | buyers.prospective (housing in Merrowgate) | quantity_supplied (dwellings) | decrease | medium; long | CR-9, CR-5a | site input_to dwellings | A-12, A-N4 |
| C-32 | buyers.prospective (housing in Merrowgate) | price_paid (housing) | increase | medium; long | CR-6, CR-9 | dwellings same_market_other_segment of Merrowgate housing | A-12, A-N4 |
| C-33 | city.general_fund | tax_revenue (property tax on the forgone dwellings) | decrease | medium; long | CR-8a, CR-9 | site input_to dwellings | A-12 |
| C-34 | city.general_fund | tax_revenue (sales tax) | ambiguous | medium; long | CR-12b over three chains | complement (trip); substitute; complement (location) | A-6, A-8, A-12, A-19, A-N3 |
| C-35 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | long | CR-8a, CR-8b, CR-12a | - | A-18 |
| C-36 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | whole period (2027 to 2059) | CR-12e (arithmetic), CR-12 0.7 note | - | A-18, A-19, A-N5 |
| C-37 | lenders, other domestic borrowers | interest_rate (other domestic borrowers) | ambiguous | short | CR-8 0.7 note (borrowing), CR-6, CR-12b | the same pool of saving (A-14) | A-1, A-12, A-14 |
| C-38 | construction_firms | quantity_traded (construction in the metro, 2027 to 2029) | ambiguous | short | CR-9, CR-12b | construction input_to the stadium, the renovation and the dwellings | A-1, A-12 |
| C-39 | residents.riverside | travel_time (game days) | increase | medium; long | CR-9 0.7 note (shared facilities) | shared_facility (roads, parking) | A-9 |
| C-40 | residents.halcourt | travel_time (game days) | decrease | medium; long | CR-9 0.7 note (shared facilities) | shared_facility (roads, parking) | A-1, A-N6 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
|---|---|---|---|---|
| team.herons, asset_value (franchise), short | Rent about $18 million a year below arm's length for 30 years; $210 million renovation avoided (A-1); more revenue (A-2, A-5) | K4 removes the option to relocate for 30 years | A-N1 (empirical, p 0.8) | increase (C-4) |
| team.herons, resources_available_other_uses, medium | Outlays on the home venue: rent $1m + routine $4m + repairs $1m = $6m a year against $7m upkeep of the renovated Bowl plus $1.6m property tax to Halcourt (A-17); more revenue (A-2) | None (even if the team owed property tax at Riverside, outlays would be at most equal before revenue) | Same direction | increase (C-10) |
| team.herons, resources_available_other_uses, long | U1-a: outlays $5m against $8.6m; more revenue | U1-b: outlays $14m against $8.6m | U1-a: same direction; U1-b: none stated | U1-a: increase; U1-b: ambiguous (C-11) |
| team.herons, resources_available_other_uses, whole period | $210m renovation avoided; medium-run savings | Under U1-b, about $5.4m a year more in years 16 to 30 (about $81m) | Arithmetic: $210m exceeds $81m even before the medium-run savings and revenue (CR-12e) | increase (C-12) |
| fans, price_paid (tickets) | Fans value the new venue more (A-2) | 7,000 more seats at games that sold out (A-5) | None stated | ambiguous (C-8) |
| businesses.riverside, quantity_traded | Game-day customers (A-8) | Congestion deters regular customers (A-9; shared_facility, Tier C chain); residents of the forgone dwellings would have shopped there (A-12, A-N3) | None stated | ambiguous (C-23) |
| property_owners.riverside_commercial, asset_value | As C-23, capitalized (A-10) | As C-23 | None stated | ambiguous (C-24) |
| businesses.halcourt, quantity_traded, long | Redevelopment of the Bowl site adds customers (A-13) | Game-day customers gone (A-8) | None stated | ambiguous (C-26); medium: decrease (C-25), since redevelopment is slow (A-11) |
| property_owners.halcourt_commercial, asset_value | Expected redevelopment (A-13) | Expected loss of game-day sales (A-8) | None stated | ambiguous (C-28) |
| halcourt.town, tax_revenue | Long: redevelopment (A-13) | Medium: an idle Bowl site against a renovated Bowl (A-1, A-11) | Different horizons, not combined (CR-12g) | decrease (medium, C-29); increase (long, C-30) |
| city.general_fund, tax_revenue (sales tax) | Game-day sales at Riverside, part drawn from Halcourt, outside the city (A-8, A-19) | Fans' spending drawn from other outings inside Merrowgate (A-6); residents of the forgone dwellings (A-12, A-N3) | None stated | ambiguous (C-34) |
| taxpayers.merrowgate, resources_available_other_uses, whole period | Rent about $30m; new sales tax about $2.8m a year (at most about $84m); land and stadium at lease end | Debt service about $853m; forgone sale $38m; administration about $15m; under U1-a repairs about $135m; forgone property tax on dwellings (A-12) | Arithmetic on the case's figures (A-19) and A-N5 (CR-12e) | at_least_one_decrease (C-36) |
| other domestic borrowers, interest_rate, short | $480m of city borrowing from domestic saving (A-14) | Team's $210m renovation (A-1) and the developer's project (A-12) not financed | None stated: the developer's outlay is not in the figures | ambiguous (C-37) |
| construction_firms, quantity_traded, short | The stadium | The renovation (A-1) and the 1,100 dwellings (A-12) not built | None stated | ambiguous (C-38) |
| users.capital_plan, quantity_traded, by window | After 2031: deferred projects done (C-19) | 2027 to 2031: projects deferred (C-18) | Different windows signed separately (2.5 timing shifts) | decrease (2027 to 2031); increase (after 2031) |

CR-12f: no two provisions cancel by construction. K4's penalty (outstanding principal plus $50 million) would return part of the bond cost only if the team relocated; under A-1 and A-N1 it does not, so no chain runs through the payment.

## 8. Time structure

- **Announcement (14 April 2026).** The franchise gains value when the deal becomes expected, rising with its chance of approval through September (CR-7c; C-4); the gain goes to the current owners, not to later buyers of the team. Commercial property near each stadium is revalued then (C-24, C-28). The developer withdrew at once (C-17).
- **Construction (2027 to mid-2029).** The team stops investing in the Bowl (C-9). Debt service starts in 2027, two years before the stadium opens (C-1). Construction demand is shifted from the Bowl and the housing site to the stadium (C-38).
- **Capital plan (2027 to 2031).** The stadium takes $480 million of $850 million headroom, leaving $370 million against a $620 million queue: at least $250 million of projects cannot be GO-financed in the window unless headroom grows (arithmetic; A-15). They are deferred (C-18) and done later as debt amortizes and assessed values grow (C-19): a timing shift, signed per window. Later borrowing costs more (C-20).
- **Lease years 11 to 15 and 16 to 30.** Under U1-a, the team gains by deferring major repairs past year 15 (C-13), and the city pays about $9 million a year from 2044 (C-14). The dispute is expected to start as year 15 approaches (C-15).
- **Bond maturity (2056) and lease end (2059).** Debt service stops in 2056. As 2059 approaches, the team's option to relocate returns and it seeks a further subsidy (C-16; CR-10a).
- **The Bowl and Halcourt.** The Bowl stops hosting games in August 2029; its redevelopment takes years (A-11), so Halcourt's losses come first and any gain comes in the long run (C-25, C-26, C-29, C-30).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-1 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | About $28.4 million a year of purchases or public services, plus the $38 million the site would have fetched | CR-8a, CR-8b |
| C-6 | officials.city_finance | enforcement_cost | increase | Issuance and administration costs | CR-8c |
| C-15 | team.herons, city officials | lobbying_effort (dispute over U1) | increase | Legal and negotiating costs | CR-4, CR-8c |
| C-16 | team.herons | lobbying_effort (further subsidy) | increase | Resources spent seeking a new deal | CR-4, CR-8c |
| C-17 | developer | quantity_traded (Riverside site) | decrease | The sale both sides expected to gain from | CR-5a |
| C-18 | users.capital_plan | quantity_traded (capital-plan projects, 2027 to 2031) | decrease | School roofs, roads and a library done later | CR-8a |
| C-21 | sellers.substitutes | quantity_substitute (other outings) | decrease | Sales of other entertainment | CR-9 |
| C-31 | buyers.prospective (housing in Merrowgate) | quantity_supplied (dwellings) | decrease | About 1,100 dwellings not built | CR-8a, CR-9 |
| C-33 | city.general_fund | tax_revenue (property tax on the forgone dwellings) | decrease | Taxes the dwellings would have paid | CR-8a |
| C-35 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | Debt service and, under U1-a, repairs in the long run | CR-8a, CR-8b |

CR-8b both sides: the general fund's debt service (C-1, C-35) is the bondholders' receipt in exchange for the $480 million they lent, which was withdrawn from other borrowers (C-37); the value of stadium use transferred below the arm's-length rent (C-2) is the team's receipt (C-10, C-12), capitalized into the franchise (C-4). The site is kept by the city, so the $38 million not received is matched by land retained, not by a gain to anyone else; the developer's lost exchange (C-17) is the loss of both parties' expected gains (CR-5a). The renovation the team does not pay for (C-3) is spending not made on Halcourt construction (C-38).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the agreement, the Herons would have stayed at the Bowl and renovated it at their own cost ($210 million in 2027-28). | counterfactual_trend | 0.7 | Talks with Selwick ended without an offer; the league's three-quarters vote on relocation; the team's own renovation plan. | The counterfactual changes; these consequences fail or lose this chain: C-3 to C-5, C-7 to C-12, C-21, C-22, C-25 to C-29, C-37, C-38, C-40. |
| A-2 | Fans value the new stadium above the renovated Bowl. | other | 0.75 | Fan surveys; attendance after comparable moves; transit access. | C-5, C-7, C-8, C-10, C-11, C-21, C-22. |
| A-3 | The number of franchises is fixed by the league, so the expected subsidy is capitalized into the franchise's value. | other | 0.85 | League rules on new franchises. | C-4. |
| A-4 | The parties dispute U1 as lease year 15 approaches. | other | 0.7 | Stake of about $135 million; the clause's wording. | C-15. |
| A-5 | Games at the Bowl often sold out, so added seats go to buyers who were turned away. | other | 0.6 | About half of home games sold out. | C-7 (capacity chain), C-8. |
| A-6 | Some fans are at the margin between a Herons game and other outings in the metro. | substitutability | 0.85 | Entertainment spending surveys. | C-7, C-21, C-22, C-34. |
| A-7 | Sellers adjust their labor to their sales. | alternative_uses | 0.8 | Staffing practice in construction and hospitality. | C-22, C-27. |
| A-8 | Fans eat and drink near the stadium before and after games. | other | 0.85 | Game-day sales near the Bowl. | C-23 to C-28, C-34. |
| A-9 | Game-day congestion on Riverside's roads and parking deters some regular customers and slows residents. | other | 0.65 | Traffic studies around comparable stadiums. | C-39; one (-) chain of C-23, C-24. |
| A-10 | Expected sales near each stadium are capitalized into commercial property values from the announcement. | expectations | 0.75 | Commercial rents near the Bowl. | C-24, C-28. |
| A-11 | The Bowl site is redeveloped only over several years. | other | 0.7 | Size of the site; Halcourt's planning process. | C-25, C-27, C-29. |
| A-12 | Without the agreement, the city would have sold the site to the developer, who would have built about 1,100 dwellings. | counterfactual_trend | 0.6 | The 2025 offer and negotiations. | C-1 (forgone sale), C-17, C-23, C-24, C-31 to C-34, C-37, C-38. |
| A-13 | The team sells the Bowl site, and its redevelopment adds to Halcourt's tax base in the long run. | other | 0.75 | Value of 60 acres of suburban land. | C-26, C-28, C-30. |
| A-14 | The bonds are bought mainly out of domestic saving that would otherwise have been lent to other domestic borrowers. | other | 0.6 | Holders of the city's earlier bonds. | C-37. |
| A-15 | The city uses debt headroom for the stadium that it would otherwise have used for projects in its capital plan, and those projects are deferred, not financed another way. | other | 0.7 | The charter limit; the capital plan's $620 million queue. | C-18, C-19. |
| A-16 | Rating agencies and bond buyers weigh the higher debt ratio, so the city's later borrowing costs more. | other | 0.55 | Rating agencies' published criteria. | C-20. |
| A-17 | The cost figures hold well enough for the comparisons: team routine maintenance $4 million a year; major repairs $1 million a year in lease years 1-15 and $9 million a year after; counterfactual upkeep of the renovated Bowl $7 million a year. | other | 0.75 | City consultant's report; the team's renovation plan. | C-10 to C-14. |
| A-18 | Debt service is paid from the general fund on schedule; the debt is repaid, not rolled over. | revenue_use | 0.9 | K1; the charter. | C-1, C-35, C-36. |
| A-19 | New sales tax on Riverside game-day sales is far smaller than debt service. | other | 0.9 | City projection of $2.8 million a year against $28.4 million. | C-36 (dominance); C-34. |
| A-20 | The league's collective agreement ties player payroll to a share of team revenue, including stadium revenue. | other | 0.45 | League agreement. Below the cut-off. | Not reported. |
| A-N1 | The option to relocate that K4 removes for 30 years is worth less to the owners than the rent below arm's length and the renovation avoided. | other | 0.8 | NEW. Talks with Selwick ended without an offer; relocation needs a three-quarters vote; the rent gap alone is about $18 million a year. | C-4 becomes ambiguous. |
| A-N2 | As the lease end approaches, the team seeks a further public subsidy, using its restored option to relocate. | expectations | 0.6 | NEW. The team's conduct in 2024 (renovation claim and talks with Selwick) when its venue aged. | C-16. |
| A-N3 | Residents of the forgone dwellings would have bought part of their meals and goods from Riverside businesses, inside Merrowgate. | other | 0.8 | NEW. Walking distance; mixed-use plan with ground-floor retail. | One (-) chain of C-23, C-24, C-34. |
| A-N4 | The developer does not build an equivalent project on another Merrowgate site in the same years, so the dwellings are not replaced. | other | 0.6 | NEW. Large sites in the city are scarce; the developer withdrew rather than moving the project. | C-31, C-32. |
| A-N5 | The value to the city of the land and the 30-year-old stadium at lease end, plus rent and new sales tax, is far smaller than the debt service paid. | other | 0.9 | NEW. The Bowl needed a $210 million renovation at 46 years; the land was offered at $38 million; rent totals about $30 million and sales tax at most about $84 million against about $853 million. | C-36 becomes ambiguous over the whole period. |
| A-N6 | Game-day congestion around the Bowl slowed Halcourt residents. | other | 0.65 | NEW. By analogy with A-9; the Bowl's 35,000 seats and suburban roads. | C-40. |

**Not reported** (an assumption below 0.5):
- Players' pay rises with stadium revenue (CR-9, LW-10, through the league's revenue-sharing rule): needs A-20 (p 0.45). The chain is recorded here per the CR-12 0.8 note; it has no opposing role in any reported consequence.
- The team relocates and pays K4's penalty: excluded by A-1 and A-N1.

### Final check before the report

1. *Uncombined chains.* Every (class, variable, horizon) with more than one chain is in section 7: the franchise value against the loss of the relocation option; the team's outlays per reading; Riverside and Halcourt businesses and property; the city's sales tax; interest rates; construction.
2. *Group signs.* General-fund payers are a group (C-1, C-35, C-36).
3. *Baseline.* All signs are against the counterfactual of a renovated Bowl and housing on the site (A-1, A-12), not against the Bowl as it is. Hence construction (C-38) and interest rates (C-37) are ambiguous, not increases.
4. *Worse off is not poorer.* Fans who switch from other outings are better off by their own ranking; their spending elsewhere is not signed (only sellers' sales, C-21). The team's means are signed because its outlays are fixed by the lease and A-17.
5. *Timing shifts.* Capital-plan projects (C-18, C-19) and deferred repairs under U1-a (C-13, C-14) are signed per window.
6. *Both sides of every transfer.* Debt service and bondholders (section 9); the in-kind subsidy (C-2) and the team (C-4, C-10, C-12); the site (C-17 and land retained).
7. *Every class, every core rule.* CR-4 checked for every class's pairs (team: renovate or move, repair now or later, relocate or stay, lobby; fans: game or other outing; developer: this site or another, A-N4; officials: dispute or accept). CR-6: C-8, C-32, C-37. CR-7c: C-4, C-24, C-28. CR-9: section 6, including the currency link (no material foreign payment is in the case, so not followed) and shared facilities (C-39, C-40). Administration (C-6) recorded.
8. *Unstated premises.* Six premises added (A-N1 to A-N6).

## 11. Report

**The policy:** Merrowgate borrows $480 million (debt service about $28.4 million a year for 30 years, from the general fund) to build a 42,000-seat stadium on city land it had been about to sell for housing, and leases it to the Herons from 2029 to 2059 for $1 million a year, against an estimated market rent of about $19 million. The team keeps all stadium revenue, pays operating costs and routine upkeep, and pays major repairs for the first 15 years; who pays them after that is unclear. The team must play all home games there for 30 years or pay off the bonds plus $50 million.

**Visible consequences:** The team gets a new stadium at a rent far below market (C-2) and avoids the $210 million renovation of its old one (C-3). Fans get a venue they value more (C-5) and more of them attend (C-7). General-fund payers or recipients of other city spending bear the debt service (C-1).

**Invisible consequences:**
- *Team owners:* The franchise gains value from the announcement, captured by its current owners (C-4). The team spends less on its venue in lease years 1 to 15 (C-10) and over the whole period (C-12); it stops maintaining the Bowl (C-9). Under reading U1-a it defers major repairs to year 16, when the city pays (C-13, C-14). The parties dispute the repair clause (C-15), and as 2059 nears the team seeks a new subsidy (C-16).
- *City finances and public projects:* At least $250 million of planned school, road and library projects are pushed beyond 2031 (C-18), and done later (C-19); later borrowing costs more (C-20). The city forgoes property tax on the 1,100 dwellings (C-33). Over the whole period, general-fund payers or recipients of other spending are worse off (C-36).
- *Housing:* About 1,100 dwellings are not built (C-31) and housing in Merrowgate costs more than it would have (C-32); the developer's purchase does not happen (C-17).
- *Other markets:* Other outings in the metro sell less and employ fewer people (C-21, C-22). Halcourt businesses near the Bowl lose game-day sales and staff from 2029 (C-25, C-27); Halcourt's property tax from the Bowl site falls in the medium run (C-29) and rises in the long run if the site is redeveloped (C-30).
- *Neighbors (Tier C):* Riverside residents face game-day congestion (C-39); Halcourt residents are relieved of it (C-40).

**Ambiguous effects:** Ticket prices (C-8): fans value the venue more, but there are more seats. Sales and property values near Riverside (C-23, C-24): game-day trade against congestion and the residents who would have lived on the site. Halcourt business and property values in the long run (C-26, C-28): lost game days against redevelopment. The city's sales tax (C-34): game-day sales drawn from outside the city against spending drawn from other outings inside it and the residents who never arrive. The team's means in lease years 16 to 30 under U1-b (C-11). Interest rates for other borrowers and metro construction in 2027-29 (C-37, C-38): the stadium against the renovation and housing it replaces.

**Key conditions:** The counterfactual premises: the team would have stayed and renovated (A-1, 0.7) and the site would have become housing (A-12, 0.6). The franchise gain needs a fixed number of franchises (A-3, 0.85) and a small value on the relocation option (A-N1, 0.8). The public-project deferral needs A-15 (0.7). Fans' response needs A-2 (0.75) and A-6 (0.85). The repair split in years 16 to 30 is a reading of U1, not a probability.

**What this analysis cannot say:** How large any effect is; whether the fans' and the team's gains outweigh the general-fund payers' losses, the deferred public projects and the dwellings not built; whether the policy is good. It cannot say whether ticket prices, sales near Riverside or the city's sales tax rise or fall. Safety and environmental effects (traffic emissions, noise) are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium | visible | B | CR-1 (op 4: debt service of about $28.4 million a year from the general fund from 2027, A-18); CR-8b (every payment is a receipt; the payer is the general fund, so a group, CR-8 0.7 note); CR-8a (the $38 million the site would have fetched is not received, A-12) | A-18, A-12 |
| C-2 | city.general_fund | subsidy_outlay (value of stadium use transferred below arm's-length rent) | increase | medium; long | visible | A | CR-1 (op 4: K3 rent of $1 million against an arm's-length estimate of about $19 million, the stated figures); CR-8b (what the team receives in kind the city gives up) | none |
| C-3 | team.herons | resources_available_other_uses | increase | short | visible | B | CR-1 (op 2: a new venue without the $210 million renovation, A-1); CR-3b (only options added, by the team's own acceptance, CR-5); CR-8b | A-1 |
| C-4 | team.herons | asset_value (franchise) | increase | short (from 14 April 2026) | invisible | B | CR-10c and CR-7c (the expected subsidy, C-2, C-3, raises expected yields and is captured by owners when it becomes expected; the fixed number of franchises keeps it from being competed away, A-3); CR-12b against K4's removal of the relocation option, dominance by A-N1 (CR-12e, empirical) | A-1, A-3, A-N1 |
| C-5 | fans | quality_per_unit (venue) | increase | medium; long | visible | B | CR-1 (op 2: a new venue); CR-2 (fans rank it above the renovated Bowl, A-2) | A-1, A-2 |
| C-6 | officials.city_finance | enforcement_cost (bond issuance and lease administration) | increase | short; medium; long | invisible | A | CR-1 (op 4: about $3.1 million at issuance and $0.4 million a year); CR-8c (resources spent administering are used up) | none |
| C-7 | fans | quantity_traded (Herons tickets) | increase | medium; long | visible | B | CR-4 (x: another outing, y: a Herons game; y improved, A-2, so fans at the margin switch, A-6); CR-6 (7,000 more seats at games that sold out let turned-away buyers in, A-5). Two chains, same sign | A-1, A-2, A-5, A-6 |
| C-8 | fans | price_paid (Herons tickets) | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-6 (more demand at each price, A-2); (-) CR-6 (more seats at sold-out games, A-5). No premise says which dominates | A-1, A-2, A-5 |
| C-9 | team.herons | maintenance_spending (Halcourt Bowl, 2026 to mid-2029) | decrease | short | invisible | B | CR-10a (the move, expected from 2026, alters choices now); CR-4 (x: renovate the Bowl in 2027-28, as in the counterfactual, A-1; y: maintain it only until the move) | A-1 |
| C-10 | team.herons | resources_available_other_uses | increase | medium | invisible | B | CR-8b and arithmetic on A-17 (outlays on the venue $6 million a year against $8.6 million for the renovated Bowl with its property tax); CR-6 and CR-4 (more revenue from a venue fans value more, A-2); same direction (CR-12a) | A-1, A-17, A-2 |
| C-11 | team.herons | resources_available_other_uses | U1-a: increase; U1-b: ambiguous | long | invisible | B | Per reading. U1-a: outlays $5 million against $8.6 million, plus more revenue (CR-12a). U1-b: CR-12b, outlays $14 million against $8.6 million (-) against more revenue (+, A-2); no premise says which dominates | A-1, A-17, A-2 |
| C-12 | team.herons | resources_available_other_uses | increase | whole period (2027 to 2059) | invisible | B | CR-12 0.7 note (a whole-period consequence where a dominance premise sets the sign); CR-12e (arithmetic: the $210 million renovation avoided exceeds the at most about $81 million of extra repairs under U1-b, before the medium-run savings) | A-1, A-17 |
| C-13 | team.herons | maintenance_spending (major repairs, lease years 11 to 15) | U1-a: decrease; U1-b: no_change | medium (2039 to 2043) | invisible | B | CR-10a and CR-4 (x: repair in years 11 to 15 at own cost, y: defer to year 16 when the city pays under U1-a); under U1-b the team pays in both windows, so no change | A-17 |
| C-14 | city.general_fund | subsidy_outlay (major repairs, lease years 16 to 30) | U1-a: increase; U1-b: no_change | long | invisible | B | CR-1 per reading (U1-a: op 4, about $9 million a year from the general fund, plus repairs deferred under C-13); CR-8b | A-17 |
| C-15 | team.herons, city officials | lobbying_effort (dispute over U1) | increase | medium (approaching 2044); long | invisible | B | CR-4 (x: accept the other side's reading, y: dispute it; stake about $135 million, A-4); CR-8c (resources spent in the dispute are used up) | A-4 |
| C-16 | team.herons | lobbying_effort (for a further public subsidy as 2059 approaches) | increase | long | invisible | B | CR-10a (the lease end is expected and alters choices before it); CR-4 (x: accept the end, y: seek a new subsidy using the restored relocation option, A-N2); CR-8c | A-N2 |
| C-17 | developer | quantity_traded (Riverside site) | decrease | short | visible | B | CR-5a (the sale that would otherwise have taken place, A-12, is prevented by K2's use of the site; both parties lose the gain each expected) | A-12 |
| C-18 | users.capital_plan | quantity_traded (capital-plan projects completed 2027 to 2031) | decrease | medium (2027 to 2031) | invisible | B | CR-8a (debt headroom directed to the stadium is withdrawn from other uses); arithmetic ($850m - $480m = $370m against a $620m queue); A-15: deferred, not financed another way | A-15 |
| C-19 | users.capital_plan | quantity_traded (deferred capital-plan projects completed after 2031) | increase | long (after 2031) | invisible | B | CR-10a and 2.5 timing shift (projects deferred, not cancelled, A-15, are done in a later window than in the counterfactual) | A-15 |
| C-20 | city.general_fund | interest_rate (the city's later GO borrowing) | increase | medium; long | invisible | B | CR-11c (a higher debt ratio conveys information to rating agencies and lenders, A-16); CR-5c (lenders' acceptable terms move) | A-16 |
| C-21 | sellers.substitutes | quantity_substitute (other outings in the metro) | decrease | medium; long | invisible | B | CR-9 (relation: substitute; fans switching to games, C-7, buy fewer other outings, A-6); CR-4 | A-1, A-2, A-6 |
| C-22 | sellers.substitutes | employment (other outings) | decrease | medium; long | invisible | B | CR-9 and LW-10 (demand for labor follows sales, A-7). Stops at depth 3 | A-1, A-2, A-6, A-7 |
| C-23 | businesses.riverside | quantity_traded | ambiguous | medium; long | invisible | C | CR-12b: (+) CR-9 (complement, trip: game-day customers, A-8); (-) CR-9 0.7 note (shared_facility: congestion deters regular customers, A-9; Tier C link); (-) CR-9 (complement, location: residents of the forgone dwellings, A-12, A-N3). No premise says which dominates | A-8, A-9, A-12, A-N3 |
| C-24 | property_owners.riverside_commercial | asset_value | ambiguous | short (from 14 April 2026) | invisible | C | CR-7c and CR-10c (expected sales capitalized from the announcement, A-10); chains as C-23 | A-8, A-9, A-10, A-12, A-N3 |
| C-25 | businesses.halcourt | quantity_traded | decrease | medium | invisible | B | CR-9 (complement, trip: game-day customers leave with the team in 2029, A-1, A-8); redevelopment of the Bowl site is slow (A-11), so no offsetting chain in this horizon | A-1, A-8, A-11 |
| C-26 | businesses.halcourt | quantity_traded | ambiguous | long | invisible | B | CR-12b: (-) as C-25; (+) CR-9 (complement, location: redevelopment of the Bowl site adds customers, A-13). No premise says which dominates | A-1, A-8, A-13 |
| C-27 | businesses.halcourt | employment | decrease | medium | invisible | B | CR-9 and LW-10 (labor input_to game-day sales, A-7). Stops at depth 3 | A-1, A-7, A-8, A-11 |
| C-28 | property_owners.halcourt_commercial | asset_value | ambiguous | short (from 14 April 2026) | invisible | B | CR-7c and CR-10c (expected yields capitalized from the announcement, A-10); CR-12b: (-) loss of game-day sales, A-8; (+) expected redevelopment, A-13 | A-1, A-8, A-10, A-13 |
| C-29 | halcourt.town | tax_revenue (property tax on the Bowl site) | decrease | medium | invisible | B | CR-9 (the Bowl is not renovated, C-9, and stands idle while redevelopment is slow, A-11, against a renovated Bowl in the counterfactual, A-1); CR-10b | A-1, A-11 |
| C-30 | halcourt.town | tax_revenue (property tax on the Bowl site) | increase | long | invisible | B | CR-7a (the site moves to a use that yields more once it is no longer needed for games); CR-9 (A-13) | A-13 |
| C-31 | buyers.prospective (housing in Merrowgate) | quantity_supplied (dwellings) | decrease | medium; long | invisible | B | CR-9 (relation: site input_to dwellings); CR-5a (the sale and the building it would have financed do not happen, A-12); not replaced elsewhere, A-N4 | A-12, A-N4 |
| C-32 | buyers.prospective (housing in Merrowgate) | price_paid (housing) | increase | medium; long | invisible | B | CR-6 (with fewer dwellings, C-31, the price moves to a higher clearing level than it would have) ; CR-9 (relation: the dwellings same_market_other_segment of Merrowgate housing) | A-12, A-N4 |
| C-33 | city.general_fund | tax_revenue (property tax on the forgone dwellings) | decrease | medium; long | invisible | B | CR-8a and CR-9 (the dwellings, A-12, would have paid property tax; the city-owned stadium is not stated to pay any) | A-12 |
| C-34 | city.general_fund | tax_revenue (sales tax) | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-9 (game-day sales at Riverside, part drawn from Halcourt outside the city, A-8, A-19); (-) CR-9 (spending drawn from other outings inside the city, A-6); (-) CR-9 (residents of the forgone dwellings, A-12, A-N3). No premise says which dominates | A-6, A-8, A-12, A-19, A-N3 |
| C-35 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | long | invisible | B | CR-8a and CR-8b (debt service to 2056, A-18; under U1-a also repairs, C-14); the group sign per CR-8 0.7 note; all chains same direction for the group, since rent and new sales tax are far smaller (A-19) | A-18 |
| C-36 | taxpayers.merrowgate, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | whole period (2027 to 2059) | invisible | B | CR-12 0.7 note (whole period); CR-12e (arithmetic on the case's figures: about $853m of debt service, $38m forgone, about $15m of administration against about $30m of rent and at most about $84m of new sales tax, A-19; residual value of land and stadium far smaller, A-N5) | A-18, A-19, A-N5 |
| C-37 | lenders, other domestic borrowers | interest_rate (other domestic borrowers) | ambiguous | short | invisible | B | CR-8 0.7 note (the means lent to the city are not available to other borrowers, A-14) and CR-6: (+) $480m of city borrowing; (-) the team's $210m renovation (A-1) and the developer's project (A-12) are not financed. No figure for the developer's outlay, so no dominance | A-1, A-12, A-14 |
| C-38 | construction_firms | quantity_traded (construction in the metro, 2027 to 2029) | ambiguous | short | invisible | B | CR-9 (relation: construction input_to each project); CR-12b: (+) the stadium; (-) the renovation (A-1) and the dwellings (A-12) not built. No premise says which dominates | A-1, A-12 |
| C-39 | residents.riverside | travel_time (game days) | increase | medium; long | invisible | C | CR-9 0.7 note (shared_facility: game-day traffic on Riverside's roads and parking, A-9) | A-9 |
| C-40 | residents.halcourt | travel_time (game days) | decrease | medium; long | invisible | C | CR-9 0.7 note (shared_facility: game-day traffic leaves the Bowl's roads in 2029, A-1, A-N6) | A-1, A-N6 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-041-C1: The city as an actor. CR-1 to CR-12 are stated over individuals; the city's choices (to borrow, to forgo the sale, to defer projects) are made by officials whose ranking the rules do not model, and the burden is traced only through CR-8 to a group of payers. Deciding which capital projects are deferred (A-15) and whether repairs are deferred by the city under U1-b needed premises, not rules.
- GAP-041-C2: Bargaining over a lease clause left to "good faith" (U1). No core rule says how a dispute between two parties to a continuing contract settles; C-15 records only that resources are spent on it (CR-4, CR-8c).

**(b) Core-rule wording that was hard to apply.**
- CR-7c with a contract term that removes an option (K4): the rule speaks of changes in expected yield; the value of a lost relocation option to a franchise owner is a change in yield only in states that A-1 says are unlikely. A-N1 was needed to sign the franchise value.
- CR-12 0.7 note (whole period): the whole-period sign for general-fund payers needed a residual-value premise (A-N5), because the city keeps an asset (land and stadium) at the end. The note does not say whether assets held at the end of the period count in the arithmetic.
- CR-8 0.7 note (borrowing): it records the lenders' side, but here the counterfactual also uses saving (the team's renovation, the developer's project), so the sign on other borrowers' rates is ambiguous. The note reads as if the lenders' side always pushes rates up.
- CR-3b and CR-5: the team accepts the package voluntarily, so it is not worse off by its own ranking; but the package also binds it (K4). The rules handle a voluntary contract with a binding term only by treating the whole contract as one exchange.
- CR-9 0.7 note on shared facilities: the congestion chain enters an ambiguous combination (C-23) at Tier C, which pulls the whole consequence down to Tier C (CR-12d), although its other chains are Tier B.

**(c) Vocabulary missing from the ontology.**
- No variable for public capital projects completed or deferred; recorded as `quantity_traded` with a qualifier (C-18, C-19).
- No variable for debt headroom under a borrowing cap.
- No actor class for a government budget as distinct from its payers; recorded as `city.general_fund`.
- No variable for the in-kind value of a below-market lease; recorded as `subsidy_outlay` with a qualifier (C-2).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on most of the stadium case. Both find the following: the team gains means and its franchise gains value from the announcement, fans get a better venue, ticket prices are `ambiguous`, other outings in the metro sell less, and the repair clause is disputed. Riverside sales and commercial property are `ambiguous` at Tier C, Riverside residents face congestion, and Halcourt loses game-day trade and Bowl property tax in the medium run. The site sale and the dwellings are forgone, the capital plan is deferred within the charter limit, and the city's later borrowing costs more. Construction work is `ambiguous`, and both versions record the general-fund payers per horizon and over the whole period, administration, and the team's whole-period gain. There are three sign differences. Two are pattern-version errors. In the national loan market, the pattern signs other borrowers' rate up and their loans down (C-26, C-27) by OC-8 as written. But the counterfactual also uses saving, for the team's renovation and the developer's project, so the rate is `ambiguous` (core C-37). In lease years 16 to 30 under U1-b, the pattern signs the team's means down on outlays alone (C-32). It leaves out the derived (+) revenue chain from a venue fans value more, so the valid sign is `ambiguous` (core C-11). The third is a core error: Halcourt's long-run property tax is signed up (core C-30) against an idle site rather than against the renovated Bowl of the counterfactual. The pattern's `ambiguous` (C-21) is right. The core version also signs the team's deferral of repairs (C-13) and its late-lease lobbying (C-16) against the wrong baseline. It omits the items that CR-12's 0.8 "two items in one variable" clause asks for (game-day sales at Riverside, regulars deterred, Merrowgate's game-day sales tax), the stadium workers and the payers' Hazlitt's-tailor row. The pattern version omits the housing-price effect, the property tax on the forgone dwellings, the later window of the capital plan, Halcourt residents' relief from congestion, and the city's residual asset in the whole-period arithmetic.

Counts: M 15, V 10, S 3, OP 12, OC 10.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-3 | M | | The team's means rise while the Bowl's renovation is not needed. The horizon labels differ (pattern "medium" 2027 to 2031, core "short"); the window is the same. |
| C-2 | C-5 | M | | |
| C-3 | none (core C-38 records the total) | OC | J | Stadium construction work, `at_least_one_increase`, as an item. The core records only the metro total (`ambiguous`). The item follows from CR-9 and LW-10 for a project that does not exist in the counterfactual. A recording choice. |
| C-4 | C-4 | M | | The franchise's value rises. The core adds an opposing chain: K4 removes the option to relocate for 30 years (CR-3a, CR-7c), dominated by A-N1. The pattern argues that K4 "binds only in the 30% of cases" where the team would have left. That argument is about actions; an option has value to the asset's holder even when it is unlikely to be used. So the pattern's sign has a hidden premise. Both versions miss that the team's acceptance of the package (CR-2, CR-5) is evidence for A-N1 as far as the owners' own ranking goes. |
| C-5 | none | OC | J | `subsidy_share_received`, owners against fans, increase. The rent is a cost fixed per firm (CR-4 0.8 note), so no ticket-price chain runs through it, and the fixed number of franchises (A-3) places the gain with the owners (CR-7b). The core uses the same reasoning in C-4 ("the fixed number of franchises keeps it from being competed away") but does not record the share. |
| C-6 | C-7 | V | | `quantity_demanded` (pattern) against `quantity_traded` (core). The core adds the capacity chain at sold-out games (A-5), with the same sign. |
| C-7 | C-8 | M | | |
| C-8 | C-21 | V | | `quantity_traded` against `quantity_substitute` for other outings. |
| C-9 | C-22 | V | | Pattern: `employment`, `hours_worked` as a group, `at_least_one_decrease`. Core: `employment` decrease alone. CR-9 with LW-10 gives less labor demanded, not which margin moves, so the core's single sign overclaims (final check 2). The pattern's group is the valid record. |
| C-10 | C-15 | M | | |
| C-11 | none | OC | E | Employment at the Riverside stadium increases (CR-9, LW-10: labor `input_to` games played there, a place where they are not played in the counterfactual). Core omission. |
| C-12 | none | OC | E | Employment at the Halcourt Bowl decreases from 2029 (CR-9). The core records Halcourt businesses' staff (C-27) but not the Bowl's own staff. Core omission. |
| C-13 | none (core C-23 records the total) | OC | E | Riverside sales to fans on game days, increase, as an item (Tier B). CR-12's 0.8 "two items in one variable" clause asks for each item and the total to be recorded. The core records only the total. Core error. It is also what keeps the Tier B claim alive when the total drops to Tier C. |
| C-14 | C-25 | V | | Halcourt sales to fans (an item, medium to long) against Halcourt businesses' total sales (medium; the core's long-run total, C-26, is `ambiguous`). |
| C-15 | none | OC | E | Riverside regulars deterred on game days, decrease (Tier C item). The core has it only as a chain of C-23. Same cause as C-13. |
| C-16 | C-23 | M | | Both `ambiguous`, Tier C. The core adds a third chain: residents of the forgone dwellings (A-12, A-N3). |
| C-17 | C-39 | M | | |
| C-18 | C-24 | M | | |
| C-19 | C-28 | V | | Both `ambiguous`; the tiers differ. The pattern's chains are lost trips (B) against less congestion (C), so it records Tier C. The core's chains are lost trips (B) against expected redevelopment of the Bowl site (B, A-13), so it records Tier B. The pattern omitted the redevelopment chain here, though it uses A-13 for C-21. With that chain the sign is `ambiguous` at Tier B whatever the congestion chain does. |
| C-20 | C-29 | M | | Halcourt's revenue decreases in the medium run. The pattern also counts "game-day sales tax" for Halcourt. The record names a sales tax for Merrowgate only, so that part rests on an unstated premise. |
| C-21 | C-30 | S | E | Halcourt's long-run tax revenue. Pattern: `ambiguous` (redevelopment against the loss of the Bowl's tax). Core: property tax on the Bowl site increase. The core's CR-7a step shows only that the owner moves the site to its best use once games leave. It does not show that the redeveloped site is assessed above a renovated, operating stadium, which is the counterfactual (A-1). The comparison the core actually makes is with an idle site, the medium-run state. Core error (baseline); the pattern's sign is the valid one. |
| C-22 | none (core C-34 records the total) | OC | E | Merrowgate's sales tax on Riverside game-day sales increase, as an item. The core records only the total (`ambiguous`), against the CR-12 0.8 items clause, as for C-13. |
| C-23 | C-1 | V | | The forgone $38 million, recorded as the city's `non_tax_receipts` (pattern) or inside the payers' group (core C-1, citing CR-8a). Same premise (A-12). |
| C-24 | C-31 | M | | The core adds A-N4: the developer does not build an equivalent project elsewhere in Merrowgate. The pattern's sign for `buyers.prospective` needs it. Hidden premise. |
| C-25 | none | OC | J | Land in Halcourt supplied for redevelopment in the long run (CR-7a, A-13). The core uses the same chain inside C-26, C-28 and C-30 but does not record it. A recording choice. |
| C-26 | C-37 | S | P | Other borrowers' `interest_rate`. Pattern: increase (OC-8 with A-14). Core: `ambiguous`, because the counterfactual also draws on saving: the team's $210 million renovation (A-1) and the developer's project (A-12) are not financed under the agreement. OC-8 as written has no right-baseline clause for borrowing that the policy itself displaces; OC-3 has one. The analyst applied it as written, though the pattern's own C-30 counted the housing project as displaced. Pattern error, with the cause in the PATTERN as written. |
| C-27 | none | OC | P | Loans to other borrowers decrease (OC-8). Lending to all borrowers other than the city falls whatever the rate does: if the rate falls, saving is no larger; if it rises, the added saving is smaller than the $480 million, by CR-12e's response argument. But part of that fall is the team and developer not borrowing, not crowding out. For third parties, the quantity moves opposite to the rate and is `ambiguous` like C-37. The pattern's sign, derived from a rate rise, fails with C-26. The core omits the key, and nothing scorable is lost. |
| C-28 | C-18 | V | | `quantity_supplied` (pattern) against `quantity_traded` (core) of capital-plan projects, 2027 to 2031. The core adds the arithmetic: at least $250 million cannot be GO-financed in the window. |
| C-29 | C-20 | M | | |
| C-30 | C-38 | V | | Labor (`employment`, `hours_worked`) against construction `quantity_traded`, both `ambiguous`. The pattern's (−) chains omit the renovation not done (A-1), which the core includes; the combined sign is the same. |
| C-31 | C-10 | M | | The team's means rise in lease years 1 to 15. The core puts the Bowl's $1.6 million property tax into the counterfactual outlays ($8.6 million against $7 million) and adds a revenue chain (A-2); the pattern calls the margin thin. Same sign. |
| C-32 | C-11 | S | P | Lease years 16 to 30. U1-a: both increase. U1-b: pattern decrease (outlays $14 million against $7 million), core `ambiguous`. A venue fans value more (A-2), with 7,000 more seats, cannot lower the team's net receipts. It can always sell as before (CR-3b) and, given A-2, earns more. That (+) chain opposes the higher outlays, and no premise ranks them. So CR-12b gives `ambiguous`. The pattern analyst omitted a derived chain (final check 1); no pattern is at fault. |
| C-33 | C-12 | M | | |
| C-34 | C-1, C-35 | V | | Split by horizon. The pattern nets the rent and new sales tax by arithmetic (A-19); the core folds them into the group sign. |
| C-35 | C-14 | V | | Payers' repairs under U1-a (pattern) against the general fund's `subsidy_outlay` (core). Same per-reading split, CR-8 contingent payers. |
| C-36 | C-36 | M | | The core adds A-N5: the land and the stadium the city holds at lease end are worth far less than the debt service. The pattern counts the site's forgone $38 million as a cost while the city keeps the land. Without a residual-value premise its arithmetic is incomplete, though the sign survives. |
| C-37 | C-6 | M | | The pattern applies OC-3's right baseline (the counterfactual sale's administration); the core omits that comparison but the sign is the same. |
| C-38 | none | OC | E | Sellers where the payers would have spent or invested: `employment`, `hours_worked`, `at_least_one_decrease` (CR-8a, CR-9, LW-10, as an unnamed group). The core has the payers' loss (C-1, C-35, C-36) but not its propagation. Core omission. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-2 | OP | J | The general fund's `subsidy_outlay` (the rent below arm's length), Tier A. The pattern records the transfer in its classification and through the payers (C-34). A recording choice. |
| C-9 | OP | E | The team spends less on the Bowl in 2026 to mid-2029, since it does not renovate it (CR-10a, CR-4). Derivable, and the pattern omitted it as a consequence; its C-1 rests on it. |
| C-13 | OP | E | Under U1-a the team defers major repairs from lease years 11 to 15. The CR-4 move is right, but the sign is given against U1-b ("U1-b: no_change"), not against the counterfactual, in which the team repairs a renovated Bowl. The pattern declined to sign it for that reason (section 8; Gaps (b)3). Core error (baseline). With A-17's figures a sign against the counterfactual may be possible. Neither version tries. |
| C-16 | OP | E | The team lobbies for a further subsidy as 2059 approaches (A-N2). In the counterfactual the renovated Bowl ages in the same years, and the team's 2024 conduct, the core's own evidence, suggests it would seek a subsidy then too. Against that baseline the sign needs a comparison premise (RS-7's "Unless" clause, applied to a counterfactual with lobbying). Core error. |
| C-17 | OP | J | The developer's purchase of the site does not happen (CR-5a). The pattern records both sides of the same forgone exchange as C-23 (the city) and C-24 (the dwellings). |
| C-19 | OP | E | Deferred capital-plan projects completed after 2031, increase (timing shift, 2.5). The pattern says that part of C-28 is a delay but signs only the first window (final check 5), so this is a pattern omission. The core's variable is narrow, though. Stadium debt occupies headroom until 2056, so if the cap binds in later years, the deferred projects displace later ones. The total of GO-financed projects after 2031 is not signed. |
| C-26 | OP | J | Halcourt businesses' long-run total, `ambiguous` (redevelopment against lost game days). The pattern records the item (C-14) and Halcourt's tax and property, not this total. Nothing scorable is added. |
| C-27 | OP | E | Halcourt businesses' staff decrease (CR-9, LW-10). The pattern omitted it. The core's single sign should be a group (`employment`, `hours_worked`, `at_least_one_decrease`), as in C-22. |
| C-32 | OP | E | Housing in Merrowgate costs more than it would have (CR-6 on supply withdrawn, given A-12 and A-N4). The direction is derivable even if the effect is small. Pattern omission. |
| C-33 | OP | E | The city forgoes property tax on the 1,100 dwellings (CR-8a, CR-9). Pattern omission. The core assumes, without saying so, that Merrowgate levies a property tax. The record implies assessed values but names no city property tax. |
| C-34 | OP | E | Merrowgate's total sales tax, `ambiguous` (game-day sales partly drawn from Halcourt; outings and the forgone residents drawn from inside the city). The pattern says in prose that the total is "not signed". CR-12's 0.8 items clause asks for the total to be recorded, combined under CR-12b. Minor pattern omission. |
| C-40 | OP | E | Halcourt residents' game-day travel time decreases (Tier C, A-N6). The pattern uses the same chain for Halcourt property (C-19) but does not record it for residents. Pattern omission. |

### Findings

- **Pattern overclaims and hidden premises.**
  - C-26 and C-27 apply OC-8 without asking what the counterfactual borrows. The team's renovation and the housing project would have drawn on the same saving, so the rate is `ambiguous`.
  - C-32 under U1-b signs the team's means from outlays alone and omits the revenue chain from a better, larger venue.
  - C-4 omits the value of the relocation option that K4 removes; it needs a dominance premise (core A-N1).
  - C-24 needs the premise that the dwellings are not built elsewhere (core A-N4).
  - C-36 counts the forgone sale but not the land and stadium the city holds at the end (core A-N5).
  - C-19 omits the redevelopment chain and so drops to Tier C needlessly.
  - C-20 assumes a Halcourt sales tax the record does not name.
- **Errors in the core version.**
  - C-30 (Halcourt's long-run property tax) is signed against an idle site, not the renovated Bowl.
  - C-13 is signed against the other reading of U1, and C-16 against no lobbying, rather than against the counterfactual.
  - C-22 and C-27 give `employment` a single sign where only a group is derivable.
  - It omits the items CR-12's 0.8 clause asks for (C-13, C-15, C-22), stadium workers at both sites (C-11, C-12), the payers' propagation to sellers (C-38) and the owners' share (C-5).
- **Errors in the pattern version (omissions).** It omits the Bowl's lost maintenance spending (core C-9), the later window of the capital plan (C-19), Halcourt businesses' staff (C-27), the housing price (C-32), the property tax on the forgone dwellings (C-33), Merrowgate's total sales tax as a recorded key (C-34) and Halcourt residents' relief (C-40).
- **Problems in patterns as written.**
  - OC-8 needs a right-baseline clause like OC-3's: compare with the borrowing the counterfactual would have done, including borrowing the policy itself displaces. Without one the rate sign is `ambiguous`. This goes beyond the pattern version's own (c)1, which asks for clauses on a small borrower and an existing debt limit, and (c)2, which asks for "no sign" for lenders. Both of those are also confirmed. The CR-8 0.7 note on borrowing reads the same way (core Gaps (b)).
  - OC-5's 0.8 clause on new activities should say "new to the place considered", as the pattern version proposes.
- **Limits of the core rules.**
  - No row has cause K. Every difference traces to an error or a recording choice.
  - The real limits are shared. Residents' valuation of having the team travels through no recorded relation (pattern Gaps (a)). A response on an asset that exists only under the policy (deferral of repairs) has no counterfactual to be signed against (pattern Gaps (b)3; the core's C-13 shows the trap). A change in the probability of an action (the team leaving) can be recorded only as a conditional possibility (pattern Gaps (b)4).
  - The core's GAP-041-C1 (the city as an actor) did not produce a difference: CR-8's note on payers from the general budget carries the burden.
- **Unclear core-rule wording.**
  - CR-12d with a Tier C chain opposing a Tier B chain: both versions raise this independently (pattern Gaps (b)1, core Gaps (b)).
  - CR-12's 0.7 whole-period note should say whether assets held at the end of the period count in the arithmetic (core A-N5).
  - CR-7c should say how a contract term that removes an option enters an asset's value.
  - CR-12's 0.8 "two items in one variable" clause is easy to miss; the final check could name it.
  - The CR-8 0.7 borrowing note needs the baseline point above.
- **Test of 0.8 verdicts.**
  - *OC-8 (needed interpretation):* confirmed on the debt limit (core C-18 derives it directly from CR-8a) and on the lenders' side (the core records interest only as a receipt, under CR-8b). Contradicted in degree: the core version finds that OC-8 as written gives the wrong sign in the national loan market here, so the verdict should be "failed" (C-26 above).
  - *OC-5 0.8, new activities (needed interpretation):* the core version does not record stadium workers, so it neither confirms nor contradicts directly. Its per-location derivations for Halcourt staff (C-27) support applying the clause per place.
  - *CR-9 0.7, a Tier C chain opposing a Tier B one (needed interpretation):* confirmed (core Gaps (b), C-23).
  - *CR-12g 0.7, whole period ("worked as written, and showed its value"):* the whole-period sign for the team holds in both versions. The showcase contrast does not: under U1-b, the long-run window is `ambiguous`, not a decrease (C-32 above).

