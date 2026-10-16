# WE-025 / Analysis: Housing bill with a rent cap, a vacancy tax and a construction subsidy

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Harrowmere Housing Stability and Supply Act.** Harrowmere is a city of about 700,000 people with about 300,000 homes, 55% of them rented. Market rents have risen about 5% a year for several years. The suburbs of Alden County, 20 to 30 minutes away, have no comparable rules. About 12,000 homes (4% of the stock) are not anyone's principal residence for more than six months a year: roughly 5,000 second homes and city apartments of people who live elsewhere, 3,000 short-term rentals, 2,500 units held empty by landlords, and 1,500 estates and renovations. Converting a rental building to separately owned condominiums requires a subdivision permit that takes about nine months.

The bill was introduced on 1 February of Year 1 with a council majority behind it. It passed on 1 May and takes effect on 1 September of Year 1. The vacancy tax is first assessed on occupancy during calendar Year 2. The subsidy applies to units completed from 1 September of Year 1 to 31 August of Year 6. The rent cap has no end date.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rent cap | `price_ceiling` | Rent on residential units in buildings of two or more units that were first occupied before 1 September of Year 1 | Landlords of those units | Rent increases for a sitting tenant capped at 3% a year from the rent in force on 1 September. Between tenancies the rent may be reset to any level. Eviction only for cause, including owner move-in, demolition, or withdrawal for conversion with six months' notice and a relocation payment of three months' rent. | Single-family homes; condominium units owned separately; units first occupied on or after 1 September of Year 1, for 15 years from first occupancy. |
| K2 Vacancy tax | `capital_tax` (annual tax on holding an unused unit) | Residential units not occupied as anyone's principal residence for more than six months in a calendar year | Owners | 2% of assessed value a year (about $10,000 for a typical unit). Annual self-declaration; audits using water and electricity records; unpaid tax plus 50% penalty. | Units under an active building permit (up to 24 months); owners in hospital or care; estates, for 12 months after death. Units listed for sale or rent are **not** exempt. |
| K3 Construction subsidy | `per_unit_subsidy` | New rental units completed from 1 September of Year 1 to 31 August of Year 6 that add to the city's housing stock | Developers who claim | $30,000 per unit, paid on completion. The developer records a covenant keeping the unit as a long-term rental (12-month leases to principal residents) for 15 years. No cap on the number of units. | — |
| K4 Funding of K3 | Funding | — | City | K3 is paid first from K2 revenue, held in a Housing Fund; any shortfall comes from the general budget. Unspent K2 revenue stays in the fund for future K3 payments. | — |
| K5 Administration | Enforcement | K1 to K3 | City Housing Department | Rent registry; complaint-driven enforcement of K1 with fines; K2 declarations and audits; K3 claims. Funded from the general budget. | — |

Unclear provisions:
- **U1.** Whether a newly completed unit that is still being leased up counts as vacant under K2. Reading U1-a: not counted (or always leased within six months). Reading U1-b: counted like any other unit. Both readings are analyzed (section 7).
- **U2.** Whether a later council will remove the exemption of new units from K1 before 15 years. The exemption is in the same ordinance and can be amended by a simple majority. Treated as an expectation (A-17).
- **U3.** Whether a unit rented as a short-term rental is "occupied as a principal residence". By the text, no: short-term rentals count as vacant.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Rent cap | triangular | Yes within tenancies: market rents rise faster than 3% (A-1), enforced (A-2) | 1 for covered landlords (raising a sitting tenant's rent above 3% is removed); 3 (eviction only for cause; conversion requires notice and three months' relocation payment); for sitting tenants, staying at a capped rent is a new option worth more each year | CR-4, CR-5, CR-6, CR-7c, CR-9, CR-10a, CR-10b, CR-11a |
| K2 Vacancy tax | binary | Yes for owners of the about 12,000 units not used as a principal residence (A-10); U1 decides whether new units in lease-up are covered | 3 (a 2% annual payment attached to the option 'keep the unit unused, as a second home or as a short-term rental'); 4 (means transferred from those who keep that option to the Housing Fund) | CR-4, CR-7c, CR-8b, CR-9, CR-10a |
| K3 Construction subsidy | binary | Yes for marginal projects (A-13) | 3 (a $30,000 payment attached to completing a new rental unit); 1 for those who claim (selling the unit or letting it short-term is removed for 15 years by the covenant); 4 (means transferred from the fund or the general budget) | CR-4, CR-4c, CR-7b, CR-7c, CR-8, CR-9, CR-10a |
| K4 Funding of K3 | binary (earmark) | Yes | 4: K2 revenue is directed to K3; any shortfall is taken from the general budget | CR-8b, CR-8d |
| K5 Administration | binary (spending) | Yes | 4 (general budget to the Housing Department); 3 (registry, declarations, audits and claims attached to the options of landlords, owners and developers) | CR-8c |

The counterfactual is Harrowmere with none of the five components. Each consequence records the components its chain runs through.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| tenants.sitting | Tenants of covered units on 1 September of Year 1 | K1: staying at a capped rent; moving loses it (A-4). |
| landlords.covered | Landlords of units in pre-September buildings of two or more units | K1 op 1 and op 3; vacancy reset remains open. |
| owners.covered_buildings | Owners of covered buildings when K1 becomes expected | Expected yield falls (CR-7c). |
| prospective_tenants | Seekers of rental housing in Harrowmere | Through K1 (starting rents, vacancies), K2 (more units), K3 (new units). |
| tenants.exempt_units | Tenants of single-family homes, separately owned condominiums and new units | Through CR-9 (same_market_other_segment). |
| owners.non_principal_units | Owners of second homes, short-term rentals, landlord-held empty units, estates and renovations | K2 op 3 and op 4 on keeping a unit unused; exemptions for permits, care and estates. |
| operators.short_term_rental | Operators of the about 3,000 short-term rentals (U3: counted as vacant) | K2 op 3. |
| guests.short_stay | Visitors who rent short-term | Through CR-9: hotels are the substitute (A-11). |
| sellers.substitutes.hotels | Hotels | Through CR-9 (substitute). |
| buyers.homes | Buyers of condominiums and homes for sale | Through CR-9: units sold under K2, conversions under K1, projects diverted by K3. |
| developers | Builders of new housing | K3 op 3 and op 1 (covenant); K1 exempts their new units for 15 years; K2 may tax lease-up (U1-b). |
| landowners.apartment_zoned | Owners of land zoned for apartments (A-15) | Through CR-9 and CR-7b (input_to new rentals). |
| workers.construction | Owners of construction labor (A-16) | Through CR-9 (input_to). |
| buyers.other_construction | Buyers of non-subsidized building and renovation | Through CR-9: compete for the same labor and land. |
| renters.alden_county | Renters in the suburbs 20 to 30 minutes away | Through CR-9 (across_border, A-N1). |
| taxpayers.city | Those who fund the general budget | K5 op 4; K4 shortfall (A-N2). |
| officials.housing_department | Runs the registry, K2 audits and K3 claims; holds the Housing Fund | K5 op 4. |

## 4. Direct effect

CR-1 and CR-2: the immediate change for each component.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | tenants.sitting | price_paid (rent) | increase | short (renewals 1 February to 31 August of Year 1) | CR-10a, CR-4 (x: renew after 1 September, y: renew before) | A-9 |
| C-2 | tenants.sitting | price_paid (rent) | decrease | short (after 1 September); medium; long | CR-1 op 1, CR-6 | A-1, A-2 |
| C-3 | landlords.covered | net_price_received (rent from sitting tenants) | decrease | short (after 1 September); medium; long | CR-1 op 1, CR-8b | A-1, A-2 |
| C-4 | owners.non_principal_units | resources_available_other_uses | decrease | medium (from Year 2) | CR-1 op 4, CR-3a, CR-8b | - |
| C-5 | officials.housing_department (Housing Fund) | tax_revenue (vacancy tax) | increase | medium (from Year 2) | CR-1 op 4, CR-8b | - |
| C-6 | officials.housing_department (Housing Fund) | tax_revenue_vs_static_projection | decrease | medium | CR-4 (x: keep unused, y: rent, sell or occupy) | A-10 |
| C-7 | developers | net_price_received (new rental units, including subsidy) | increase | medium; long | CR-1 op 3, CR-5c | A-13 |

## 5. Responses

CR-4 for each pair of options each actor class has; CR-6 where K1 fixes the sitting tenant's rent; CR-5 for prevented and new exchanges; CR-10a for the effective date, the first K2 assessment year and the subsidy window.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-8 | prospective_tenants | price_paid (starting rents, covered units) | ambiguous | short; medium | CR-12b over CR-10a and CR-9 chains | A-3, A-10 |
| C-9 | prospective_tenants | search_cost | ambiguous | medium; long | CR-12b over CR-4 and CR-9 chains | A-4, A-10 |
| C-10 | tenants.sitting | turnover | ambiguous | medium; long | CR-12b over two CR-4 chains | A-4, A-7, A-8 |
| C-11 | tenants.sitting | job_changes | decrease | medium; long | CR-9, CR-4 (x: keep current job, y: take a job requiring a move) | A-4, A-5, A-1 |
| C-12 | landlords.covered | side_payments (payments to sitting tenants to leave) | increase | medium; long | CR-4 (x: keep the tenant, y: pay to vacate), CR-5 | A-7, A-1 |
| C-13 | landlords.covered | maintenance_spending | decrease | medium; long | CR-6, CR-4c (x: maintain, y: defer) | A-6, A-1, A-2 |
| C-14 | tenants.sitting | quality_per_unit | decrease | long | CR-9, CR-10b | A-6, A-1 |
| C-15 | tenants.sitting | informal_activity (sublets at market rent) | increase | medium | CR-4 (x: comply, y: violate), CR-6 | A-18, A-1 |
| C-16 | landlords.covered | reclassification (conversion to separately owned condominiums) | ambiguous | medium; long | CR-12b: CR-4 (K1) against CR-9 (K2) | A-8, A-1, A-10, A-N4 |
| C-17 | owners.covered_buildings | asset_value (covered buildings) | decrease | short (from introduction) | CR-7c, CR-10c | A-1, A-24 |
| C-18 | owners.non_principal_units | units_held_vacant | decrease | short (late Year 1); medium | CR-4 (x: keep unused, y: rent, sell or occupy), CR-10a | A-10 |
| C-19 | operators.short_term_rental | quantity_supplied (short-term rentals) | decrease | medium | CR-4 (x: short-term rental, y: long-term rental or sale) | A-11 |
| C-20 | owners.non_principal_units | quantity_supplied (long-term rentals) | increase | medium | CR-4, CR-1 (K1 on let units) | A-10, A-11 |
| C-21 | owners.non_principal_units | quantity_supplied (homes offered for sale) | increase | short; medium | CR-4 (x: keep, y: sell), CR-1 (K1 on let units) | A-10 |
| C-22 | owners.non_principal_units | reclassification (building permits and occupancy arrangements to fall into exemptions) | increase | medium | CR-4 (x: pay, y: reshape into an exemption) | A-12 |
| C-23 | owners.non_principal_units | asset_value | decrease | short (from introduction) | CR-7c, CR-10c | A-24, A-10 |
| C-24 | developers | investment_target (new rental buildings) | U1-a: increase; U1-b: increase | medium; long | CR-4 (x: other project or none, y: subsidized rental), CR-10c, CR-6, arithmetic | A-13, A-17, A-N3 |
| C-25 | developers | quantity_supplied (new rental units) | increase | long | CR-10b, CR-4 | A-13, A-17 |
| C-26 | developers | quality_per_unit (floor area per unit) | decrease | medium; long | CR-4c (x: fewer larger units, y: more smaller units) | A-14 |
| C-27 | developers | quantity_traded (new units first occupied before 1 September of Year 1) | decrease | short (to 31 August of Year 1) | CR-10a, CR-4 (x: first occupancy before 1 September, y: after) | A-21 |
| C-28 | developers | quantity_traded (new units first occupied in the months after 1 September of Year 1) | increase | short (September to December of Year 1) | CR-10a, CR-4 | A-21 |
| C-29 | developers | quantity_traded (new units completed in the months after 31 August of Year 6) | decrease | long (months after the subsidy ends) | CR-10a, CR-4 (x: complete after the end, y: before) | A-21 |
| C-30 | landlords.covered, owners.non_principal_units, developers, tenants.sitting | lobbying_effort | increase | medium | CR-4 (x: accept, y: lobby), CR-8c | A-19 |
| C-31 | landlords.covered, owners.non_principal_units, developers | compliance_cost | increase | short; medium | CR-1 op 3, CR-8c | - |
| C-32 | officials.housing_department | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | - |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7. Depth limit 4. Effects on employers of tenants who do not move, on businesses near converted buildings and on hotel suppliers are diffuse bystander effects pruned at depth 3.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-33 | guests.short_stay | price_substitute (hotel rooms) | increase | medium | CR-9, CR-6 | hotel rooms substitute for short-term rentals (close) | A-11 |
| C-34 | sellers.substitutes.hotels | quantity_traded (hotel stays) | increase | medium | CR-9, CR-4 | hotel rooms substitute for short-term rentals (close) | A-11 |
| C-35 | buyers.homes | price_paid (homes and condominiums for sale) | decrease | short | CR-9, CR-6 | non-principal units same_market_other_segment of homes for sale (close) | A-10 |
| C-36 | buyers.homes | price_paid (homes and condominiums for sale) | ambiguous | medium; long | CR-12b over CR-9 chains | homes for sale same_market_other_segment of rental housing; land input_to both | A-10, A-13, A-15, A-N4 |
| C-37 | tenants.exempt_units | price_paid (single-family homes, condominiums and new units let) | ambiguous | medium | CR-12b over CR-6 and CR-9 chains | covered units same_market_other_segment of exempt units (close) | A-3, A-4, A-10, A-13 |
| C-38 | landlords.covered, developers, owners.non_principal_units | capital_stock_target (rental housing in the city) | ambiguous | long | CR-12b over CR-10b chains | covered, unused and new units are segments of the same rental market | A-8, A-10, A-13, A-25 |
| C-39 | renters.alden_county | price_paid (rents in Alden County) | ambiguous | medium | CR-12b over two CR-9 chains | Harrowmere rentals across_border to Alden County rentals (partial, by commuting) | A-N1, A-3, A-4, A-10 |
| C-40 | landowners.apartment_zoned | asset_value (land zoned for apartments) | increase | short; medium (from introduction) | CR-9, CR-7b, CR-7c | zoned land input_to new rental buildings (close) | A-15, A-13 |
| C-41 | landowners.apartment_zoned | subsidy_share_received | increase | medium | CR-7b | zoned land input_to new rental buildings (close) | A-15, A-13 |
| C-42 | workers.construction | wage_rate | increase | medium | CR-9, LW-10, CR-7a | construction labor input_to new buildings (close) | A-16, A-13 |
| C-43 | buyers.other_construction | quantity_traded (non-subsidized building and renovation) | decrease | medium | CR-8a, CR-7a, CR-4c | same labor input_to other construction (close) | A-16, A-13 |
| C-44 | developers | units_held_vacant (newly completed units in lease-up) | U1-a: increase; U1-b: ambiguous | medium; long | arithmetic, CR-4 (x: hold out for a higher starting rent, y: lease faster) | - | A-13, A-20 |
| C-45 | taxpayers.city | resources_available_other_uses | decrease | short; medium; long | CR-8a, CR-8c, CR-8b, CR-8d | - | - |
| C-46 | officials.housing_department (Housing Fund) | resources_available_other_uses | decrease | medium | CR-8d | - | - |

**Pairwise component check** (workflow step 6). For each pair: does one close or open an exit route from the other, change who is bound by it, fund it, or tax or restrict its intended output?

| Pair | Interaction | Consequences |
| --- | --- | --- |
| K1 and K2 | K2 taxes keeping a unit unused, closing that exit from K1 for landlords; it does not close conversion to condominiums sold to owner-occupiers. K2 lowers condominium prices, which weakens the conversion route that K1 opens. K1 makes letting worse for units it would cover, so owners leaving K2's taxed use lean toward sale. K2's added rental supply works against K1's upward push on starting and exempt rents | C-16, C-20, C-21, C-8, C-37, C-9, C-39, C-36, C-38 |
| K1 and K3 | K1 exempts K3's new units for 15 years, and the pressure K1 displaces raises their expected rents, so K1 adds to K3's incentive (if the exemption is expected to last, A-17). Units first occupied before 1 September are covered by K1 and get no K3 payment, so completions are timed after it | C-24, C-25, C-27, C-28, C-37, C-38 |
| K2 and K3 | Under U1-b, K2 taxes new units in lease-up, part of K3's intended output; by arithmetic this lowers but does not reverse K3's incentive (A-N3). K3 adds supply that works with K2's added supply on rents | C-24, C-44, C-37, C-38 |
| K2, K3 and K4 | K4 funds K3 from K2 revenue; K2 revenue falls below projection as owners respond while K3 claims are uncapped, so a shortfall falls on the general budget (A-N2); unspent K2 revenue sits in the fund | C-6, C-45, C-46 |
| K5 and the others | K5 changes no one's bound status; its cost falls on the general budget | C-32, C-31, C-45 |
| K1 and K4 or K5 | No interaction beyond administration | - |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| prospective_tenants, price_paid (starting rents), short; medium | K1 anticipation (A-3) | K2 supply (A-10); K3 supply (A-13) | None | ambiguous (C-8) |
| prospective_tenants, search_cost, medium; long | K1 lock-in (A-4) | K2 supply (A-10) | None | ambiguous (C-9) |
| tenants.sitting, turnover, medium; long | buyouts and withdrawals (A-7, A-8) | lock-in (A-4) | None | ambiguous (C-10) |
| landlords.covered, reclassification (conversion), medium; long | K1 (A-8) | K2 lowers condominium prices (A-10, A-N4) | None | ambiguous (C-16) |
| tenants.exempt_units, price_paid, medium | K1 displaced pressure (A-3, A-4) | K2 and K3 supply (A-10, A-13) | None | ambiguous (C-37) |
| buyers.homes, price_paid, short | - | K2 sales (A-10) | - | decrease (C-35) |
| buyers.homes, price_paid, medium; long | K3 diversion and land (A-13, A-15) | K2 sales and less second-home demand (A-10, A-N4) | None | ambiguous (C-36) |
| rental stock, capital_stock_target, long | K2 (A-10); K3 (A-13) | K1 conversions and withdrawals (A-8) | None | ambiguous (C-38) |
| renters.alden_county, price_paid, medium | K1 (A-N1, A-3, A-4) | K2 (A-10) | None | ambiguous (C-39) |
| developers, investment_target, medium; long | K3 (A-13); K1 exemption (A-17) | K2 on lease-up, U1-b only (A-20) | Arithmetic: $30,000 against at most about $10,000 a year for a slow unit, with lease-up rarely near three years (A-N3) | U1-a: increase; U1-b: increase (C-24) |
| developers, units_held_vacant (lease-up), medium; long | more completions (A-13) | U1-b only: K2 on slow lease-up (A-20) | None under U1-b | U1-a: increase; U1-b: ambiguous (C-44) |
| taxpayers.city, resources_available_other_uses | - | K5 (CR-8a, CR-8c); K4 shortfall (A-N2) | Same direction | decrease (C-45) |

## 8. Time structure

- **Introduction to effective date (1 February to 31 August of Year 1).** K1 became expected on 1 February. Landlords raise rents at renewals before 1 September (A-9; C-1), and covered building values fall from the introduction (CR-7c; C-17). Developers hold back first occupancy until after 1 September to be exempt from K1 and eligible for K3 (A-21; C-27, C-28). Land zoned for apartments gains value as soon as K3 is expected (C-40).
- **K2 timing.** K2 is first assessed on occupancy during Year 2, so owners must have a principal resident in a unit for more than six months of Year 2. They act in late Year 1 and early Year 2 (CR-10a; C-18, C-21, C-35); revenue arrives from Year 2.
- **K1 over time.** The cap applies within tenancies with no end date, so the gap between capped and market rents grows each year that market rents rise faster than 3% (A-1). Lock-in, buyouts, subletting and lower maintenance grow with the gap (C-11, C-12, C-15, C-13); quality falls as a stock (CR-10b; C-14).
- **K3 over time.** Buildings take years to plan and build (A-25), so added units arrive in the long run (C-25). The subsidy ends for units completed after 31 August of Year 6: completions are rushed before and dip just after (CR-10a; C-29). New units stay exempt from K1 for 15 years from first occupancy, if the exemption is believed (A-17, 0.55); its removal by a later majority (U2) is the main risk to developers' expectations.
- **Expectations.** Owners and buyers expect K1 and K2 to last (A-24, 0.75), so their capitalized effects (C-17, C-23) arrive at once.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-4 | owners.non_principal_units | resources_available_other_uses | decrease | Spending and saving of owners who pay about $10,000 a unit a year | CR-1 op 4, CR-3a, CR-8b |
| C-11 | tenants.sitting | job_changes | decrease | Jobs not taken because taking them means losing the capped rent | CR-9, CR-4 (x: keep current job, y: take a job requiring a move) |
| C-30 | landlords.covered, owners.non_principal_units, developers, tenants.sitting | lobbying_effort | increase | Resources spent seeking to change or keep the components | CR-4 (x: accept, y: lobby), CR-8c |
| C-31 | landlords.covered, owners.non_principal_units, developers | compliance_cost | increase | Time and money spent on registration, declarations, audits and claims | CR-1 op 3, CR-8c |
| C-32 | officials.housing_department | enforcement_cost | increase | Staff and budget for the registry, audits and claims | CR-1 op 4, CR-8c |
| C-43 | buyers.other_construction | quantity_traded (non-subsidized building and renovation) | decrease | Buildings and renovations not done because labor and land went to subsidized rentals | CR-8a, CR-7a, CR-4c |
| C-45 | taxpayers.city | resources_available_other_uses | decrease | Other public spending or lower taxes given up for administration and any K3 shortfall | CR-8a, CR-8c, CR-8b, CR-8d |

CR-8's symmetry: what sitting tenants do not pay (C-2) landlords do not receive (C-3); what owners pay under K2 (C-4) the fund receives (C-5) and passes to developers (C-7) and, in part, to landowners (C-41); any shortfall and the administration fall on taxpayers (C-45). Labor and land drawn into subsidized building are withdrawn from other building (C-43). Resources spent on compliance, enforcement and lobbying are used up (C-31, C-32, C-30).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Market rents keep rising faster than 3% a year, so the cap binds within tenancies. | binding | 0.85 | Rent trend; vacancy rate; pipeline of new supply. | These consequences fail or lose this chain: C-2, C-3, C-11, C-12, C-13, C-14, C-15, C-16, C-17. |
| A-2 | The rent registry enforces the cap against most landlords. | enforcement | 0.75 | Registry budget; complaint volumes; size of fines. | These consequences fail or lose this chain: C-2, C-3, C-13. |
| A-3 | Landlords raise starting rents in anticipation of capped increases. | expectations | 0.75 | Starting rents in covered and exempt units after enactment; landlord surveys. | These consequences fail or lose this chain: C-8, C-37, C-39. |
| A-4 | Sitting tenants lose the capped rent if they move; tenancies cannot be transferred. | other | 0.95 | Ordinance text. | These consequences fail or lose this chain: C-9, C-10, C-11, C-37, C-39. |
| A-5 | Some job opportunities for sitting tenants require moving or a much longer commute. | mobility | 0.7 | Size of the region; job locations. | These consequences fail or lose this chain: C-11. |
| A-6 | Housing codes leave room to reduce maintenance. | other | 0.8 | Habitability code; inspection frequency. | These consequences fail or lose this chain: C-13, C-14. |
| A-7 | Landlords offer buyouts where the rent gap is large. | other | 0.6 | Buyout disclosures where they are required; tenant surveys. | These consequences fail or lose this chain: C-10, C-12. |
| A-8 | The conversion route is usable for many buildings. | alternative_uses | 0.7 | Subdivision permit approvals; relocation costs; condominium demand. | These consequences fail or lose this chain: C-10, C-16, C-38. |
| A-9 | Enough leases renew before 1 September, and landlords can raise rents at renewal. | expectations | 0.7 | Share of leases renewing in the window. | These consequences fail or lose this chain: C-1. |
| A-10 | Many owners of empty units prefer to rent, sell or occupy them rather than pay 2% a year. | alternative_uses | 0.75 | Vacancy reasons by type (second homes, short-term, landlord-held); sale and rental demand. | These consequences fail or lose this chain: C-6, C-8, C-9, C-16, C-18, C-20, C-21, C-23, C-35, C-36, C-37, C-38, C-39. |
| A-11 | Short-term rental is less profitable than other uses after the tax, and guests have hotel alternatives. | alternative_uses | 0.7 | Short-term rental revenue per unit against $10,000 tax; hotel occupancy. | These consequences fail or lose this chain: C-19, C-20, C-33, C-34. |
| A-12 | Owners can use building permits or occupancy arrangements to fall into exemptions. | other | 0.65 | Permit requirements; audit design. | These consequences fail or lose this chain: C-22. |
| A-13 | The subsidy is large relative to developers' margins, and land and approvals are available. | alternative_uses | 0.75 | Development cost per unit; approval rates; zoned capacity. | These consequences fail or lose this chain: C-7, C-24, C-25, C-36, C-37, C-38, C-40, C-41, C-42, C-43, C-44. |
| A-14 | The per-unit subsidy makes smaller units more attractive, and zoning allows them. | other | 0.7 | Minimum unit sizes; unit-mix data. | These consequences fail or lose this chain: C-26. |
| A-15 | Land zoned for apartments is scarce. | other | 0.75 | Zoned capacity; land prices. | These consequences fail or lose this chain: C-36, C-40, C-41. |
| A-16 | Construction land and labor are scarce and in use elsewhere. | other | 0.8 | Construction employment; project pipeline. | These consequences fail or lose this chain: C-42, C-43. |
| A-17 | Developers expect new units to stay exempt from K1 for the full 15 years. | expectations | 0.55 | Whether the exemption is in the charter or an ordinance; council politics; history of extending controls. | These consequences fail or lose this chain: C-24, C-25. |
| A-18 | Some sitting tenants sublet at market rent without being caught. | enforcement | 0.6 | Lease terms; complaint-driven enforcement. | These consequences fail or lose this chain: C-15. |
| A-19 | Tenants, landlords, owners and developers can organize to lobby. | other | 0.85 | Existing associations. | These consequences fail or lose this chain: C-30. |
| A-20 | Under reading U1-b, some newly completed units stay unleased for more than six months. | other | 0.8 | Lease-up times for new buildings. | These consequences fail or lose this chain: C-44. |
| A-21 | Developers can time certificates of occupancy around 1 September. | expectations | 0.8 | Completion schedules; inspection process. | These consequences fail or lose this chain: C-27, C-28, C-29. |
| A-22 | Owners make false occupancy declarations on a meaningful scale. | enforcement | 0.35 | Utility-record audits; penalties. | No reported consequence rests on it (see Not reported). |
| A-23 | Short-term rental operators move to Alden County on a meaningful scale. | mobility | 0.35 | Location of short-stay demand. | No reported consequence rests on it (see Not reported). |
| A-24 | Owners and buyers expect K1 and K2 to stay in force for many years. | expectations | 0.75 | Neither has an end date; council majority; history of rent rules in the region once enacted. | These consequences fail or lose this chain: C-17, C-23. |
| A-25 | The housing stock grows slowly relative to its size, so existing units are in slowly expandable supply. | durability | 0.9 | Completions against the stock of 300,000; permit and building times. | These consequences fail or lose this chain: C-38. |
| A-N1 | Commuting from Alden County is practical for some Harrowmere renters. | mobility | 0.7 | NEW. Travel times of 20 to 30 minutes stated in the policy record; no case assumption covers renters' mobility across the boundary. | These consequences fail or lose this chain: C-39. |
| A-N2 | In at least some years, K3 claims exceed the K2 revenue available in the fund, so the general budget pays part of K3. | revenue_use | 0.6 | NEW. Static K2 base of about 12,000 units at $10,000 falls as owners respond (A-10); K3 is uncapped at $30,000 a unit and induces building (A-13). Used only as a reinforcing chain; no reported sign depends on it. | No reported consequence rests on it (see Not reported). |
| A-N3 | Lease-up of a new unit rarely takes anywhere near three years, so under U1-b the vacancy tax on a slow unit stays well below the $30,000 payment. | other | 0.9 | NEW. Typical lease-up times for new buildings (months, A-20 says some exceed six); the tax is 2% of assessed value, about $10,000, a year. | These consequences fail or lose this chain: C-24. |
| A-N4 | Some buyers of condominiums in Harrowmere buy them as second homes or to let short-term, and K2 lowers what they will pay. | other | 0.85 | NEW. About 5,000 second homes and city apartments of people who live elsewhere and 3,000 short-term rentals in the record; K2 taxes both uses. | These consequences fail or lose this chain: C-16, C-36. |

**Not reported** (an assumption below 0.5):
- Widespread false occupancy declarations, with lower K2 revenue and more audit cost (CR-4, x: declare truthfully, y: declare falsely): needs A-22 (p 0.35).
- Short-term rental operators move to Alden County, raising short-stay supply there (CR-4, x: here, y: there): needs A-23 (p 0.35).
- Developers expect the K1 exemption to be removed before 15 years and hold back (CR-10a, CR-10c): needs the negation of A-17 (p 0.45). With A-17 at 0.55, the K1 chain in C-24 is reported; it is the most fragile premise in the bill.

**Readings.** U1 is reported as two readings in C-24 and C-44, without probabilities. U2 is treated as the expectation A-17, as the input specifies. U3 follows the text: short-term rentals count as vacant (C-19).

## 11. Report

**The policy:** Harrowmere caps rent increases for sitting tenants in existing buildings of two or more units at 3% a year (rents reset freely between tenancies; eviction only for cause), taxes homes not used as anyone's principal residence for more than six months a year at 2% of value, and pays developers $30,000 for each new rental unit completed in five years, kept as a long-term rental for 15 years. The tax revenue pays the subsidy first; the general budget covers any shortfall and the administration.

**Visible consequences:** Sitting tenants pay less than they would have (C-2) and landlords receive less from them (C-3). Owners of unused homes pay the tax or put their units to use (C-4, C-18), and the fund collects it (C-5). Developers receive the subsidy (C-7) and, in the long run, complete more rental units (C-25).

**Invisible consequences:**
- *Before 1 September:* rents are raised at renewals (C-1); covered building values and values of unused homes fall (C-17, C-23); land zoned for apartments gains value (C-40); first occupancy of new units is moved past 1 September (C-27, C-28).
- *Sitting tenants:* take fewer jobs that require moving (C-11); some sublet (C-15); some are paid to leave (C-12); maintenance and quality fall over time (C-13, C-14).
- *Owners of unused homes:* sell or let them (C-21, C-20); short-term rentals shrink (C-19) and hotels gain (C-33, C-34); some reshape their units into exemptions (C-22), so revenue falls short of the static projection (C-6). Home prices fall in the short run (C-35).
- *Developers and building:* build smaller units (C-26); rush completions before the subsidy ends (C-29); part of the subsidy goes to owners of scarce land (C-41); construction wages rise and other building is crowded out (C-42, C-43).
- *Public budget:* administration and any shortfall in the fund fall on taxpayers (C-45, C-32); fund balances are tied up (C-46); everyone bound spends on compliance (C-31); every group lobbies (C-30).

**Ambiguous effects:** Because the components push rents and supply in opposite directions, several signs cannot be given without a premise about sizes: starting rents (C-8), exempt-unit rents (C-37), seekers' search costs (C-9), sitting tenants' turnover (C-10), conversions to condominiums (C-16), home prices after the short run (C-36), the citywide rental stock (C-38) and Alden County rents (C-39). The rent cap pushes toward higher starting and exempt rents and fewer rental units; the vacancy tax and the subsidy push toward more units and lower rents. What would decide each is the relative size of these flows. Under reading U1-b, the number of new units waiting to be leased is ambiguous (C-44); under either reading, developers invest more (C-24).

**Key conditions:** The cap binds (A-1, 0.85) and is enforced (A-2, 0.75); many owners respond to the tax (A-10, 0.75); the subsidy matters to margins (A-13, 0.75); developers believe the exemption of new units will last (A-17, 0.55, the weakest premise); land and labor are scarce (A-15, A-16). Four premises were added: commuting from Alden County (A-N1, 0.7), a K3 shortfall in some years (A-N2, 0.6), short lease-up times (A-N3, 0.9) and second-home demand for condominiums (A-N4, 0.85).

**What this analysis cannot say:** The size of any effect, and therefore whether the bill on balance raises or lowers rents, the rental stock, home prices or rents in Alden County. It does not weigh sitting tenants' gains against seekers', landlords' and owners' losses, or developers' and landowners' gains against taxpayers' costs, or say whether the bill is good. Health, safety and environmental effects are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Components |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | tenants.sitting | price_paid (rent) | increase | short (renewals 1 February to 31 August of Year 1) | invisible | B | CR-10a (an expected cap alters choices now); CR-4 (for landlords, x: raise the rent after 1 September under the cap, y: raise it at renewal before; the cap is applied to the rent in force on 1 September, so y gains, A-9) | A-9 | K1 |
| C-2 | tenants.sitting | price_paid (rent) | decrease | short (after 1 September); medium; long | visible | B | CR-1 (op 1: increases above 3% a year are removed for sitting tenants); CR-6 (the market rent rises faster, A-1, so the capped rent falls further below it each year; enforced, A-2) | A-1, A-2 | K1 |
| C-3 | landlords.covered | net_price_received (rent from sitting tenants) | decrease | short (after 1 September); medium; long | visible | B | CR-1 (op 1); CR-8b and CR-8's symmetry (what sitting tenants do not pay, C-2, landlords do not receive) | A-1, A-2 | K1 |
| C-4 | owners.non_principal_units | resources_available_other_uses | decrease | medium (from Year 2) | visible | A | CR-1 (op 4: owners who keep a unit unused pay 2% of its value a year); CR-3a (owners who instead rent, sell or occupy fall back to an option they ranked lower); CR-8b (the payment is the fund's receipt) | none | K2 |
| C-5 | officials.housing_department (Housing Fund) | tax_revenue (vacancy tax) | increase | medium (from Year 2) | visible | A | CR-1 (op 4); CR-8b (the fund receives what owners pay) | none | K2, K4 |
| C-6 | officials.housing_department (Housing Fund) | tax_revenue_vs_static_projection | decrease | medium | invisible | B | CR-4 (owners for whom keeping the unit unused ranked narrowly above renting, selling or occupying switch, A-10, so fewer units pay than the 12,000 times $10,000 projection assumes); avoidance through exemptions adds to the gap (C-22) | A-10 | K2, K4 |
| C-7 | developers | net_price_received (new rental units, including subsidy) | increase | medium; long | visible | B | CR-1 (op 3: $30,000 is attached to completing a new rental unit); CR-5c (what one party may receive moves the range of terms); A-13: the payment is large relative to margins | A-13 | K3 |
| C-8 | prospective_tenants | price_paid (starting rents, covered units) | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-10a and CR-4 (landlords set starting rents higher to allow for capped increases later, A-3; K1); (-) CR-9 (relation: same market; units brought into long-term rental by K2 add to supply, A-10, A-11; K2); (-) later, new units under K3 (A-13; K3). No premise says which dominates | A-3, A-10 | K1, K2, K3 |
| C-9 | prospective_tenants | search_cost | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-4 (sitting tenants move less, A-4, so fewer covered units fall vacant; K1); (-) CR-9 (more units offered for rent and sale under K2, A-10; K2). No premise says which dominates | A-4, A-10 | K1, K2 |
| C-10 | tenants.sitting | turnover | ambiguous | medium; long | invisible | B | CR-12b: (-) CR-4 (x: move, y: stay; staying at a capped rent is lost on moving, A-4, so tenants for whom moving ranked narrowly above staying stay); (+) CR-4 and CR-5 for landlords (x: keep a capped tenant, y: pay the tenant to leave and reset the rent, A-7; or withdraw for owner move-in or conversion, A-8). No premise says which dominates | A-4, A-7, A-8 | K1 |
| C-11 | tenants.sitting | job_changes | decrease | medium; long | invisible | B | CR-9 (relation: the capped tenancy is a complement, by location, of jobs within reach); CR-4 (x: take a job that requires moving, y: keep the current one; x now costs the capped rent, A-4, so tenants for whom the two were close stay, A-5) | A-4, A-5, A-1 | K1 |
| C-12 | landlords.covered | side_payments (payments to sitting tenants to leave) | increase | medium; long | invisible | B | CR-4 (vacancy resets the rent, so a vacancy is worth paying for once the gap is large, A-7); CR-5 (the payment is made only where both rank it above the alternative) | A-7, A-1 | K1 |
| C-13 | landlords.covered | maintenance_spending | decrease | medium; long | invisible | B | CR-6 (with the rent held below the clearing level, landlords keep sitting tenants without competing on quality, so pressure moves to the unregulated term, quality); CR-4c (each unit of maintenance no longer raises the rent a sitting tenant pays; codes leave room, A-6) | A-6, A-1, A-2 | K1 |
| C-14 | tenants.sitting | quality_per_unit | decrease | long | invisible | B | CR-9 (relation: maintenance input_to the housing service, C-13); CR-10b (quality is a stock that changes through flows, so the fall builds up) | A-6, A-1 | K1 |
| C-15 | tenants.sitting | informal_activity (sublets at market rent) | increase | medium | invisible | B | CR-6 (exchanges outside the rule where the expected gain exceeds the expected penalty); CR-4 (x: give up or occupy the unit, y: sublet it at the market rent; the gap grows each year, A-1; not caught, A-18) | A-18, A-1 | K1 |
| C-16 | landlords.covered | reclassification (conversion to separately owned condominiums) | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-4 (x: keep renting under the cap, y: convert to condominiums, which K1 exempts; A-8; nine-month permit, CR-10b; K1); (-) CR-9 (relation: condominiums are the converted product; K2 taxes condominiums bought as second homes or short-term rentals, A-N4, and K2 puts unused units on the market, A-10, which lowers condominium prices and the return to converting; K2). K2 does not close the route for sale to owner-occupiers. No premise says which dominates | A-8, A-1, A-10, A-N4 | K1, K2 |
| C-17 | owners.covered_buildings | asset_value (covered buildings) | decrease | short (from introduction) | invisible | B | CR-10c (value reflects expected yields); CR-7c (the expected fall in rents, C-3, is borne by whoever owns the building when K1 becomes expected, from 1 February of Year 1; owners expect K1 to last, A-24) | A-1, A-24 | K1 |
| C-18 | owners.non_principal_units | units_held_vacant | decrease | short (late Year 1); medium | visible | B | CR-4 (x: keep the unit unused, y: let it, sell it or live in it; x now costs 2% a year); CR-10a (owners act before Year 2, the first year assessed); A-10 | A-10 | K2 |
| C-19 | operators.short_term_rental | quantity_supplied (short-term rentals) | decrease | medium | invisible | B | CR-4 (U3: a short-term rental counts as vacant, so it carries the tax; it is less profitable than other uses after the tax, A-11) | A-11 | K2 |
| C-20 | owners.non_principal_units | quantity_supplied (long-term rentals) | increase | medium | invisible | B | CR-4 (owners who stop keeping units unused, C-18, and short-term operators, C-19, let some of them long-term, A-10, A-11); K1 interaction: a unit in a pre-September building of two or more units, once let, is covered by K1, which makes letting worse relative to selling for those owners, so part of the move goes to sale (C-21) instead; the sign of this consequence is unchanged | A-10, A-11 | K2, K1 |
| C-21 | owners.non_principal_units | quantity_supplied (homes offered for sale) | increase | short; medium | invisible | B | CR-4 (x: keep the unit unused, y: sell it; A-10); K1 makes the other exit, letting, worse for units it would cover, so more owners choose sale (CR-4 with x: let under K1, y: sell) | A-10 | K2, K1 |
| C-22 | owners.non_principal_units | reclassification (building permits and occupancy arrangements to fall into exemptions) | increase | medium | invisible | B | CR-4 (x: pay the tax, y: obtain a building permit or arrange occupancy so the unit falls into an exemption; y made better relative to x, A-12) | A-12 | K2 |
| C-23 | owners.non_principal_units | asset_value | decrease | short (from introduction) | invisible | B | CR-10c and CR-7c (the expected tax, or the lower-ranked use owners turn to, lowers the expected yield of these units; borne by whoever owns them when K2 becomes expected; A-24: expected to stay) | A-24, A-10 | K2 |
| C-24 | developers | investment_target (new rental buildings) | U1-a: increase; U1-b: increase | medium; long | invisible | B | CR-4 (x: another project or none, y: a new rental building; the $30,000 payment makes y better, A-13; K3); CR-6 and CR-10c (K1 holds covered rents down, so displaced demand raises expected rents in exempt new units, which developers expect to stay exempt for 15 years, A-17; K1); under U1-b, K2 also taxes units unleased for more than six months (A-20), but by arithmetic the tax, about $10,000 a year for a slow unit, is below the $30,000 payment unless lease-up takes about three years, which is rare (A-N3), so the net change to the option is still an improvement | A-13, A-17, A-N3 | K3, K1, K2 |
| C-25 | developers | quantity_supplied (new rental units) | increase | long | visible | B | CR-10b (the stock grows only through completions, with a lag after investment, C-24, A-25); CR-4 | A-13, A-17 | K3, K1 |
| C-26 | developers | quality_per_unit (floor area per unit) | decrease | medium; long | invisible | B | CR-4c (the payment is per unit, so each added unit on a site brings $30,000; the last unit of floor area per unit is the first given up; zoning allows smaller units, A-14) | A-14 | K3 |
| C-27 | developers | quantity_traded (new units first occupied before 1 September of Year 1) | decrease | short (to 31 August of Year 1) | invisible | B | CR-10a; CR-4 (x: first occupancy before 1 September, when the unit is covered by K1 and gets no K3 payment; y: after, when it is exempt from K1 for 15 years and receives $30,000; A-21: completions can be timed) | A-21 | K1, K3 |
| C-28 | developers | quantity_traded (new units first occupied in the months after 1 September of Year 1) | increase | short (September to December of Year 1) | invisible | B | CR-10a; CR-4 (the units held back, C-27, are completed just after the date) | A-21 | K1, K3 |
| C-29 | developers | quantity_traded (new units completed in the months after 31 August of Year 6) | decrease | long (months after the subsidy ends) | invisible | B | CR-10a; CR-4 (x: complete after 31 August of Year 6 without the payment, y: rush to complete before it; A-21), so completions that would have fallen just after the end are brought forward | A-21 | K3 |
| C-30 | landlords.covered, owners.non_principal_units, developers, tenants.sitting | lobbying_effort | increase | medium | invisible | B | CR-4 (each component creates a concentrated stake: landlords in loosening K1, owners in narrowing K2, developers in extending K3 and keeping the K1 exemption, sitting tenants in extending K1 to new units, U2); CR-8c (resources used up) | A-19 | K1, K2, K3 |
| C-31 | landlords.covered, owners.non_principal_units, developers | compliance_cost | increase | short; medium | invisible | A | CR-1 (op 3: rent registry, annual declarations, audits, claims and covenants); CR-8c (resources spent complying are used up) | none | K1, K2, K3, K5 |
| C-32 | officials.housing_department | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 4: K5 is funded from the general budget); CR-8c (resources spent on administering and enforcing are used up) | none | K5 |
| C-33 | guests.short_stay | price_substitute (hotel rooms) | increase | medium | invisible | B | CR-9 (relation: hotel rooms substitute for short-term rentals, A-11); CR-6 (more demand at each price moves the price to a higher clearing level) | A-11 | K2 |
| C-34 | sellers.substitutes.hotels | quantity_traded (hotel stays) | increase | medium | invisible | B | CR-9 (same relation); CR-4 (guests, x: short-term rental, y: hotel; x is scarcer and dearer) | A-11 | K2 |
| C-35 | buyers.homes | price_paid (homes and condominiums for sale) | decrease | short | invisible | B | CR-9 (relation: units sold under K2 are same_market_other_segment of homes for sale, C-21); CR-6 (more offered at each price). K1 conversions take nine months and K3 projects years, so neither acts in the short run | A-10 | K2 |
| C-36 | buyers.homes | price_paid (homes and condominiums for sale) | ambiguous | medium; long | invisible | B | CR-12b: (-) K2 sales (A-10) and less demand from second-home buyers (A-N4); (+ or -) K1 conversions, C-16, themselves ambiguous; (+) K3 covenant diverts projects from building for sale to subsidized rental (CR-4, x: build for sale, y: build rental; A-13) and bids up land (A-15). No premise says which dominates | A-10, A-13, A-15, A-N4 | K1, K2, K3 |
| C-37 | tenants.exempt_units | price_paid (single-family homes, condominiums and new units let) | ambiguous | medium | invisible | B | CR-12b: (+) CR-6 (pressure displaced from capped covered units: fewer vacancies, A-4, higher starting rents, A-3, push seekers to exempt units; K1); (-) CR-9 (units brought into long-term rental under K2, A-10, and new units under K3, A-13, add to supply in the same market). No premise says which dominates | A-3, A-4, A-10, A-13 | K1, K2, K3 |
| C-38 | landlords.covered, developers, owners.non_principal_units | capital_stock_target (rental housing in the city) | ambiguous | long | invisible | B | CR-12b: (-) K1 conversions and owner move-in withdraw covered units from rental (A-8); (+) K2 brings unused units into long-term rental (A-10); (+) K3 adds new rental units (A-13). CR-10b: each acts through flows. No premise says which dominates | A-8, A-10, A-13, A-25 | K1, K2, K3 |
| C-39 | renters.alden_county | price_paid (rents in Alden County) | ambiguous | medium | invisible | B | CR-12b: (+) CR-9 (relation: across_border by commuting, A-N1; fewer covered vacancies and higher starting rents push some seekers to Alden County, A-3, A-4; K1); (-) CR-9 (more units in Harrowmere under K2 keep some seekers in the city, A-10; K2). No premise says which dominates | A-N1, A-3, A-4, A-10 | K1, K2 |
| C-40 | landowners.apartment_zoned | asset_value (land zoned for apartments) | increase | short; medium (from introduction) | invisible | B | CR-9 (relation: land input_to new rental buildings); CR-7b (the lasting gain from the subsidy settles on the means that cannot move: scarce zoned land, A-15); CR-7c (captured by whoever owns the land when K3 becomes expected) | A-15, A-13 | K3 |
| C-41 | landowners.apartment_zoned | subsidy_share_received | increase | medium | invisible | B | CR-7b (part of the $30,000 per unit settles on scarce land, A-15, rather than on developers or tenants) | A-15, A-13 | K3 |
| C-42 | workers.construction | wage_rate | increase | medium | invisible | B | CR-9 and LW-10 (relation: construction labor input_to new rental buildings); CR-7a (scarce labor in use elsewhere, A-16, is bid away, raising its wage in every use) | A-16, A-13 | K3 |
| C-43 | buyers.other_construction | quantity_traded (non-subsidized building and renovation) | decrease | medium | invisible | B | CR-8a (labor and land directed to subsidized rentals are withdrawn from the uses their owners would otherwise have chosen); CR-7a and CR-4c (higher costs, C-42, mean the last projects elsewhere are not done). Depth 4 from K3: chain stops here | A-16, A-13 | K3 |
| C-44 | developers | units_held_vacant (newly completed units in lease-up) | U1-a: increase; U1-b: ambiguous | medium; long | invisible | B | U1-a: arithmetic (more completions under K3, C-25, mean more units in lease-up at any time). U1-b: the same (+) against CR-4 (x: hold a unit for a higher starting rent, y: lease it faster at a lower one; K2 taxes x once a unit is unleased for more than six months, A-20) (-); CR-12b: ambiguous | A-13, A-20 | K3, K2 |
| C-45 | taxpayers.city | resources_available_other_uses | decrease | short; medium; long | invisible | A | CR-8a and CR-8c (K5 is funded from the general budget and used up in administration); a second chain in the same direction: K4 pays K3 from K2 revenue first and from the general budget for any shortfall (CR-8b), and K2 revenue falls below projection as owners respond, C-6, while K3 claims are uncapped (A-N2). The sign rests on the first chain alone | none | K5, K4, K3, K2 |
| C-46 | officials.housing_department (Housing Fund) | resources_available_other_uses | decrease | medium | invisible | A | CR-8d (K2 revenue is earmarked for K3; where it is not yet spent it stays in the fund and is not available for other uses, unless other spending adjusts) | none | K2, K4 |

## Gaps found

**(a) Calculus gaps.** None. Every step used CR-1 to CR-12, LW-10 or arithmetic. One vocabulary limit, not a rule gap: the controlled list has no variable for unit size, so the shift to smaller units (C-26) is recorded as `quality_per_unit` with "(floor area per unit)".

**(b) New premises.**
- A-N1 (p 0.7): needed for C-39. CR-9 follows effects across the boundary only along a recorded relation; the case assumptions cover short-term operators moving (A-23) but not renters commuting.
- A-N2 (p 0.6): needed for the K4 chain in C-45. CR-8b and CR-8d say who pays only once it is known whether K3 claims exceed K2 revenue; no case assumption says so. The reported sign does not rest on it.
- A-N3 (p 0.9): needed to sign C-24 under U1-b. Two components act on the same option (K3 pays, K2 taxes a slow lease-up); CR-12b needs a dominance premise, which here is arithmetic plus a premise about lease-up times.
- A-N4 (p 0.85): needed for the K2 chain in C-16 and C-36. The pairwise check shows K2 can weaken the conversion route that K1 opens, but only if some condominium buyers are second-home or short-term buyers.

**(c) Unclear core rules.**
- CR-12b in a multi-component bill: most combined rent and supply signs come out ambiguous because K1 pushes one way and K2 and K3 the other. CR-12b allows no dominance without a premise, and the case assumptions contain none comparing components. Whether a component that changes a price (K1) and components that change a quantity (K2, K3) "reach the same variable" or should be kept apart under CR-12c is not stated; they were treated as reaching the same price.
- CR-12b and arithmetic: for C-24, the K2 and K3 payments attach to the same option (building), and arithmetic on their sizes was treated as a dominance premise (A-N3). The rule does not say whether summing money attached to one option is "combining chains" at all, or simply CR-4 applied to the net change.
- CR-12d: for C-45, one chain needs no premise and a second, reinforcing chain needs A-N2. The rule says a consequence holds only if all its premises hold, but does not say whether the premises of a redundant chain count. Treated as not counting; A-N2 is named in the derivation only.
- CR-6 with vacancy reset: K1 caps rents within tenancies but frees them between tenancies, so the controlled price is the sitting tenant's, and the starting rent is free. CR-6 applies to the sitting tenancy, while the starting-rent response comes from CR-10a. The rule's wording ("if a rule prevents the price from moving") does not cover a price that is free at one point of a contract and fixed later.
