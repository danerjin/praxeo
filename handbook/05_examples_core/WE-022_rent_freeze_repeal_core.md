# WE-022 / Analysis: Repeal of the Riverton rent ordinance

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Riverton Rent Stabilization Repeal.** Ten years after the WE-001 ordinance took effect, voters approve a ballot measure to repeal it. The measure qualified for the ballot six months before its effective date, and polls showed it was likely to pass. The starting point, taken from WE-001's analysis and stated here as the situation at repeal rather than as findings: controlled rents were frozen for three years and have risen at most 2% a year since, while rents for comparable exempt units have kept rising faster; some covered buildings have been converted to condominiums through the K3 permit route; maintenance in covered buildings has been below what it would otherwise have been; Eastfield and Northgate remain unregulated.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Decontrol with phase-in | Removal of a `price_ceiling` | Rent on units covered by WE-001's K1 | Landlords and tenants of covered units | Vacancy decontrol from the effective date: a covered unit that becomes vacant may be let at any rent. Sitting tenants: during each of the two years after the effective date, rent may rise by at most 15% at renewal. From the second anniversary, no limit. | None |
| R2 Tenancy rules | Removal of a restriction on contract terms | Leases of covered units (WE-001 K2) | Landlords and tenants | Eviction only for cause, and the ban on assigning a tenancy, stay in force for the two phase-in years and end at the second anniversary. | None |
| R3 Rent board | End of administration | WE-001 K4 | City | The board handles phase-in disputes and overcharge claims for two years, then is dissolved. | None |
| (unchanged) | — | Condominium-conversion permit process (WE-001 K3) | — | Not repealed: the 12-month permit process and relocation payments continue to apply to all rental buildings. | — |

Unclear provisions: whether a unit vacated during the phase-in by a tenant who accepted a payment to leave counts as a vacancy, and is therefore decontrolled at once. Assumed yes; the measure does not regulate such payments.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| R1 Decontrol with phase-in | removal of a triangular intervention | Yes: controlled rents are well below comparable exempt rents (A-1) | 2 for landlords (charging above the cap becomes an option: at once on vacancy, up to 15% a year at renewal, without limit from the second anniversary); 3 for sitting tenants (staying now brings a higher rent); 2 for prospective tenants (covered units become available to anyone willing to pay the market rent) | CR-4, CR-5, CR-6, CR-7c, CR-10a, CR-10b, CR-10c, CR-11a |
| R2 Tenancy rules (end after two years) | removal of a triangular intervention, delayed | Yes from the second anniversary | 2 for landlords (ending a tenancy without cause); 1 for sitting tenants (the option of staying on the same terms indefinitely is removed); 2 for tenants (assigning a tenancy) | CR-4, CR-10a |
| R3 Rent board (dissolved after two years) | end of administration (binary) | Yes | 4 (the board's budget is no longer drawn from the city budget); 3 (overcharge complaints and paperwork end) | CR-8a, CR-8c, CR-8d |
| Unchanged: conversion permit process | existing rule (stays in the counterfactual too) | - | None directly; its relative attractiveness changes because renting now yields more (CR-4) | CR-4, CR-10b |

The counterfactual is that the WE-001 ordinance stays in force: rents capped at 2% a year, eviction only for cause, no assignment, the board in place. Every sign below is relative to that path. The facts about WE-001 used here come from the WE-022 starting point and from the WE-001 input (background only).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| landlords.covered | Owners letting units covered by the ordinance | Op 2: may charge more on vacancy and renewal; from year 2, may end tenancies without cause. |
| owners.covered_buildings | Whoever owns covered buildings when the repeal becomes expected | Expected yield of the asset rises (CR-7c, CR-10c). |
| buyers.covered_buildings | Buyers of covered buildings after the announcement | Pay a price that reflects the higher expected yield. |
| tenants.sitting | Current tenants of covered units | Op 3: staying costs more; op 1 from year 2 (no indefinite stay); op 2 from year 2 (may assign). |
| tenants.sitting.accepting_payment | Sitting tenants who accept a payment to leave (A-13) | Op 2 in effect: the landlord can now offer a payment worth making. |
| tenants.covered_units | Whoever occupies covered units | Through CR-9: quality follows maintenance. |
| prospective_tenants | Seekers of rental housing in Riverton | Op 2: covered units can be rented by anyone who pays the market rent; non-price rationing loses its role. |
| tenants.exempt_units | Tenants of comparable exempt units in Riverton | Through CR-9 (same_market_other_segment). |
| tenants.neighboring_cities | Renters in Eastfield and Northgate | Through CR-9 (across_border). |
| developers | Builders of new rental buildings (exempt under the ordinance) | Through CR-9: the exempt segment's rents may change. |
| buyers.condominiums | Buyers of condominiums produced by conversion | Through CR-9: fewer conversions. |
| input_suppliers.building_trades | Contractors for repair and renovation | Through CR-9 (input_to). |
| officials.rent_board | Board that administers the ordinance | Op 4: dissolved after two years. |
| taxpayers.city | Those who fund the city budget | Op 4 in reverse: the board's budget is no longer needed. |

## 4. Direct effect

CR-1 and CR-2: the immediate change. Persistence is compared with the path on which the ordinance was never imposed (CR-10b).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | landlords.covered | net_price_received (rent on covered units) | increase | short; medium | CR-1 op 2, CR-5c, CR-6 | A-1, A-2 |
| C-2 | tenants.sitting | price_paid (rent) | increase | short; medium | CR-1 op 3, CR-5c, CR-6 | A-1, A-2 |
| C-3 | prospective_tenants | price_paid (covered units let on vacancy) | increase | short | CR-1 op 2, CR-6 | A-1, A-2 |
| C-4 | owners.covered_buildings | asset_value (covered buildings) | increase | short (from announcement) | CR-7c, CR-10c | A-1, A-3 |
| C-5 | buyers.covered_buildings | price_paid (covered buildings) | increase | short; medium | CR-7c, CR-8 | A-1, A-3 |
| C-6 | officials.rent_board | enforcement_cost | decrease | medium (after dissolution) | CR-1 op 4, CR-8c | - |
| C-7 | taxpayers.city | resources_available_other_uses | increase | medium | CR-8a, CR-8d | A-20 |

## 5. Responses

CR-4 for each pair of options; CR-5 for exchanges the ceiling prevented; CR-6 where the price is freed; CR-10a for the announcement window and the phase-in.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-8 | landlords.covered | units_held_vacant | increase | short (six-month announcement window) | CR-10a, CR-4 (x: re-let now under the cap, y: hold empty until decontrol) | A-11 |
| C-9 | landlords.covered | units_held_vacant | decrease | medium; long | CR-4 (x: keep out of use, y: let at market rent), CR-10b | A-N1, A-18 |
| C-10 | landlords.covered | maintenance_spending | increase | short; medium | CR-4c (x: defer, y: maintain), CR-10c | A-2, A-3 |
| C-11 | landlords.covered | investment_target (major renovation of covered buildings) | increase | medium; long | CR-4 (x: no renovation, y: renovate), CR-10c, CR-10b | A-4, A-18 |
| C-12 | tenants.covered_units | quality_per_unit | increase | medium; long | CR-9, CR-10b | A-2, A-3, A-10, A-18 |
| C-13 | landlords.covered | reclassification (conversion of rental buildings to condominiums) | decrease | short; medium | CR-4 (x: convert, y: keep renting), CR-4a | A-15, A-2 |
| C-14 | landlords.covered | capital_stock_target (rental units in formerly covered buildings) | increase | medium; long | CR-10b, CR-4 | A-15, A-N1, A-18 |
| C-15 | tenants.sitting | turnover | increase | short; medium | CR-4 (x: stay at the higher rent, y: move), CR-10a | A-6, A-1 |
| C-16 | landlords.covered | side_payments (payments to sitting tenants to leave) | increase | short (phase-in years) | CR-5, CR-4 (x: wait for the phase-in, y: pay to vacate now) | A-13, A-1 |
| C-17 | tenants.sitting.accepting_payment | resources_available_other_uses | increase | short | CR-5, CR-8b | A-13 |
| C-18 | tenants.sitting | search_cost | increase | short; medium | CR-4, CR-8c | A-6 |
| C-19 | tenants.sitting | job_changes | increase | medium | CR-9, CR-4 (x: keep current job, y: take a job requiring a move) | A-12, A-1 |
| C-20 | prospective_tenants | search_cost | decrease | short; medium | CR-6, CR-11a | A-1 |
| C-21 | prospective_tenants | allocation_by_non_price_criteria | decrease | short; medium | CR-6 | A-1 |
| C-22 | prospective_tenants | side_payments (key money and payments for illegal sublets) | decrease | short; medium | CR-6, CR-4 (x: comply, y: violate) | A-N2, A-1 |
| C-23 | tenants.sitting | informal_activity (illegal sublets) | decrease | short; medium | CR-4 (x: comply, y: violate), CR-6 | A-N2, A-1 |
| C-24 | prospective_tenants | quantity_traded (covered units let to new tenants) | increase | short; medium | CR-5a (reversed), CR-4 | A-6, A-1 |
| C-25 | tenants.sitting | lobbying_effort (to restore controls) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-14 |
| C-26 | owners.covered_buildings | lobbying_effort | ambiguous | short; medium | CR-12b over two CR-4 chains | A-14 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7. Depth limit 4. Effects on movers' new neighborhoods beyond Eastfield and Northgate, and on employers of tenants who change jobs, are diffuse bystander effects pruned at depth 3.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-27 | tenants.exempt_units | price_paid (comparable exempt units) | increase | short (announcement window and first months) | CR-9, CR-4 | covered units same_market_other_segment of exempt units (close) | A-11, A-5 |
| C-28 | tenants.exempt_units | price_paid (comparable exempt units) | ambiguous | medium; long | CR-12b: CR-6 and CR-10b against CR-4 | covered units same_market_other_segment of exempt units (close) | A-5, A-6, A-15 |
| C-29 | tenants.neighboring_cities | price_paid (rents in Eastfield and Northgate) | ambiguous | medium | CR-12b over two CR-4 chains | Riverton rental housing across_border to Eastfield and Northgate rentals (partial, by commuting) | A-6, A-7 |
| C-30 | developers | investment_target (new rental buildings) | ambiguous | medium; long | CR-9, CR-10c, CR-12b | new rental buildings same_market_other_segment of covered units | A-8, A-5, A-6 |
| C-31 | buyers.condominiums | price_paid (condominiums) | increase | medium; long | CR-9, CR-7a, CR-6 | rental buildings input_to condominiums by conversion (alternative use) | A-15, A-2 |
| C-32 | input_suppliers.building_trades | quantity_traded (repair and renovation work) | increase | medium | CR-9, LW-10 | building trades input_to covered rental housing (close) | A-3, A-4 |
| C-33 | tenants.sitting | resources_available_other_uses | decrease | short; medium | CR-8b, CR-3a | - | A-1, A-2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| tenants.exempt_units, price_paid, short | covered units held empty in the window (A-11) | - | - | increase (C-27) |
| tenants.exempt_units, price_paid, medium; long | sitting tenants who move add to demand (CR-4, A-6) | displaced pressure lifted (CR-6); covered stock returns (CR-10b) | None stated (see Gaps (c)) | ambiguous (C-28) |
| tenants.neighboring_cities, price_paid, medium | displaced sitting tenants commute in (A-6, A-7) | rationed seekers return to Riverton (A-7) | None | ambiguous (C-29) |
| developers, investment_target, medium; long | - | - | Follows C-28 | ambiguous (C-30) |
| owners.covered_buildings, lobbying_effort, short; medium | defending the repeal | no longer campaigning to repeal | None | ambiguous (C-26) |
| landlords.covered, units_held_vacant | short window (C-8) | medium; long (C-9) | Different horizons | increase (short); decrease (medium; long) |

Metamorphic check: added in the comparison phase.

## 8. Time structure

- **Announcement window (six months).** When the measure became likely to pass, the expected rise in rents was capitalized into covered buildings at once (CR-7c, CR-10c; C-4). Units that fell vacant in the window were worth holding empty until decontrol (CR-10a; C-8), which pushed demand into exempt units (C-27).
- **Phase-in (two years).** Vacancy decontrol is immediate, while sitting tenants' rents rise at most 15% per renewal. This gap makes vacancy worth paying for, so payments to leave are concentrated in these two years (C-16, C-17). Turnover rises at once and again at the second anniversary, when eviction for cause and the ban on assignment end (CR-10a; C-15).
- **Second anniversary.** Rents for sitting tenants may move freely; the rent board is dissolved (C-6, C-7).
- **Stock adjustment.** Buildings, maintenance and the split between rental and condominium use are stocks that change only through flows (CR-10b). Routine maintenance responds quickly if owners expect decontrol to last a few years (A-3, 0.8); major renovation needs ten to fifteen years of expected decontrol (A-4, 0.6) and several years to carry out (A-18). Quality and the rental stock therefore recover gradually (C-10, C-11, C-12, C-14).
- **What does not reverse (CR-10b).** Buildings converted to condominiums stay converted: they have been sold to separate owners and reversal costs more than the restored rental yield (A-9, 0.9; reconversion, A-16, has p 0.1). Deferred maintenance that became structural damage costs more to repair than ongoing maintenance would have (A-10). Owners who sold under the ordinance do not recover their capital loss (CR-7c). The persistence column records this for each consequence; "n/a" marks effects of the transition itself, which have no counterpart on the never-imposed path.
- **Belief in the repeal.** If owners expected controls to return, short-payback actions would still go ahead and long-payback ones would be held back (CR-10a, CR-10c). The premises for developers' fear of a return (A-19, 0.35) and for a fear that the exemption would be withdrawn (A-17, 0.4) are below the cut-off, so no consequence rests on them.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-18 | tenants.sitting | search_cost | increase | Time and money spent finding and moving to another unit | CR-4, CR-8c |
| C-25 | tenants.sitting | lobbying_effort (to restore controls) | increase | Time and money spent organizing to restore controls | CR-4 (x: accept, y: lobby), CR-8c |
| C-33 | tenants.sitting | resources_available_other_uses | decrease | Spending and saving given up to pay the higher rent | CR-8b, CR-3a |

CR-8's symmetry: the higher rents received by landlords (C-1) are matched by what sitting and new tenants pay (C-2, C-3, C-33); the capital gain to owners at the announcement (C-4) is matched by the higher price later buyers pay (C-5); payments to leave are a transfer from landlords to tenants (C-16, C-17). The board's budget is released (C-7), and resources used up in searching, moving and lobbying are counted (C-18, C-25).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | For most covered units, the controlled rent is now well below the rent of a comparable exempt unit. | binding | 0.95 | Rent board registry against rents of comparable exempt units; ten years of a 2% cap against the market trend. | These consequences fail or lose this chain: C-1, C-2, C-3, C-4, C-5, C-15, C-16, C-19, C-20, C-21, C-22, C-23, C-24, C-33. |
| A-2 | Landlords raise rents toward the market level at renewal and on vacancy, as R1 allows. | other | 0.85 | Ownership structure of covered buildings; landlord behavior in exempt units. | These consequences fail or lose this chain: C-1, C-2, C-3, C-10, C-12, C-13, C-31, C-33. |
| A-3 | Owners expect decontrol to last at least a few years, long enough for routine repairs to pay back. | expectations | 0.8 | Size of the ballot majority; council composition; how hard it would be to put a new ordinance on the ballot. | These consequences fail or lose this chain: C-4, C-5, C-10, C-12, C-32. |
| A-4 | Owners expect decontrol to last ten to fifteen years, long enough for major renovation and new building to pay back. | expectations | 0.6 | As A-3, plus the strength of tenant organizing after the repeal. | These consequences fail or lose this chain: C-11, C-32. |
| A-5 | Covered and exempt units are close substitutes. | substitutability | 0.85 | Similar locations and sizes; same tenant pool (WE-001 A-7). | These consequences fail or lose this chain: C-27, C-28, C-30. |
| A-6 | Some sitting tenants will not pay the higher rent and will move. | mobility | 0.85 | Incomes of sitting tenants against market rents for their units. | These consequences fail or lose this chain: C-15, C-18, C-24, C-28, C-29, C-30. |
| A-7 | Commuting from neighboring cities is practical for many renters. | mobility | 0.7 | Travel times of 15 to 25 minutes; transit links. | These consequences fail or lose this chain: C-29. |
| A-8 | Developers had expected the new-construction exemption to last, so the exempt-segment premium was feeding new building. | expectations | 0.6 | Same evidence as WE-001 A-9. | These consequences fail or lose this chain: C-30. |
| A-9 | Condominium conversions are costly to undo: converted units have been sold to separate owners. | reversal_cost | 0.9 | Condominium registry; number of owners per converted building. | No reported consequence rests on it (see Not reported). |
| A-10 | Some deferred maintenance has become structural damage that costs more to repair than ongoing maintenance would have. | reversal_cost | 0.75 | Inspection records; age of the covered stock. | These consequences fail or lose this chain: C-12. |
| A-11 | Some covered units fall vacant in the announcement window, and landlords can keep them empty until decontrol at small cost. | expectations | 0.7 | Normal vacancy rate; rent forgone for a few months against the gain from decontrol. | These consequences fail or lose this chain: C-8, C-27. |
| A-12 | Some job opportunities for sitting tenants would require moving or a much longer commute. | mobility | 0.75 | Size of the region; where jobs are (WE-001 A-12). | These consequences fail or lose this chain: C-19. |
| A-13 | Payments to leave are legal and some sitting tenants accept them. | other | 0.7 | The measure does not regulate them; practice in comparable markets. | These consequences fail or lose this chain: C-16, C-17. |
| A-14 | Sitting tenants and owners can organize at a cost below their stake. | other | 0.75 | The ballot campaigns on both sides. | These consequences fail or lose this chain: C-25, C-26. |
| A-15 | Some buildings are in the conversion permit process at the effective date, and their owners can withdraw. | other | 0.7 | Pending permit applications. | These consequences fail or lose this chain: C-13, C-14, C-28, C-31. |
| A-16 | Reconverting condominiums to rental is worth its cost for some buildings. | reversal_cost | 0.1 | Number of owners per building; cost of buying out owners. | No reported consequence rests on it (see Not reported). |
| A-17 | Developers had feared that the new-construction exemption would be withdrawn (negation of A-8). | expectations | 0.4 | As A-8. | No reported consequence rests on it (see Not reported). |
| A-18 | Restoring capacity in formerly covered buildings (major renovation, repair of structural damage, bringing units back into use) takes several years of permits, finance and construction. | durability | 0.85 | Permit times for major alterations; construction lead times; the age of the covered stock. | These consequences fail or lose this chain: C-9, C-11, C-12, C-14. |
| A-19 | Developers give a meaningful probability to controls returning, and covering new buildings, within the payback period of a new rental building (ten to fifteen years). | expectations | 0.35 | The original ordinance exempted new construction; size of the repeal majority; strength of tenant organizing after the repeal. | No reported consequence rests on it (see Not reported). |
| A-20 | The city reduces taxes or other borrowing, or funds other spending it would otherwise have cut, by the amount of the board's budget, rather than leaving the saving unused or absorbed by administration elsewhere. | revenue_use | 0.7 | City budget process; whether the board's appropriation is a separate line. | These consequences fail or lose this chain: C-7. |
| A-N1 | Under the ordinance, some covered units were kept out of the rental market (held empty, used by owners or left unrepaired) because letting them at the controlled rent did not pay. | other | 0.6 | NEW. Implied by A-18's 'bringing units back into use' but not stated as a premise; registry vacancy data; WE-001's starting point. | These consequences fail or lose this chain: C-9, C-14. |
| A-N2 | Under the ordinance, some covered units changed hands with key money or were sublet illegally. | enforcement | 0.8 | NEW. Carried from WE-001 A-3 (p 0.8): complaint-driven enforcement and the ban on assignment. | These consequences fail or lose this chain: C-22, C-23. |

**Not reported** (an assumption below 0.5):
- Some condominium buildings are reconverted to rental (CR-4, x: keep as condominiums, y: buy out owners and let): needs A-16 (p 0.1). Without it, past conversions persist in full (CR-10b).
- Developers build more because the fear that the exemption would be withdrawn is gone (CR-10c): needs A-17 (p 0.4).
- Developers hold back because they expect controls to return and cover new buildings (CR-10a, CR-10c): needs A-19 (p 0.35).

## 11. Report

**The policy:** Ten years after Riverton froze and then capped rents on existing units, voters repeal the ordinance. From the effective date, a covered unit that falls vacant may be let at any rent; sitting tenants' rents may rise at most 15% at each renewal for two years and freely after that. Eviction only for cause and the ban on assigning tenancies end at the second anniversary, when the rent board is dissolved. The condominium-conversion permit process stays. The comparison is with the ordinance staying in force.

**Visible consequences:** Landlords of covered units receive higher rents (C-1); sitting tenants pay more, in steps for two years and then at the market level (C-2); new tenants of covered units pay market rents (C-3). The rent board's costs end after two years (C-6).

**Invisible consequences:**
- *Owners and buyers of buildings:* Owners at the time the repeal became expected capture the rise in value (C-4); later buyers pay for it and gain nothing from it (C-5).
- *Landlords:* They hold some units empty in the six months before the effective date (C-8), then bring units back into use (C-9), spend more on maintenance and renovation (C-10, C-11), withdraw pending conversions (C-13), and pay some sitting tenants to leave during the phase-in (C-16). The rental stock in formerly covered buildings grows back, slowly and only in part (C-14).
- *Sitting tenants:* They pay more (C-33); some move, with search and moving costs (C-15, C-18); they take jobs that require moving more readily (C-19); some receive payments to leave (C-17); illegal sublets decline (C-23); they organize to restore controls (C-25).
- *Seekers:* Covered units become available to anyone willing to pay (C-24); search costs, key money and allocation by connections fall (C-20, C-22, C-21).
- *Occupants of covered units:* quality rises over time (C-12).
- *Other markets:* Exempt rents rise in the announcement window (C-27); condominium prices rise as fewer buildings convert (C-31); repair and renovation work increases (C-32); taxpayers can use the board's budget elsewhere (C-7).

**Ambiguous effects:** Rents in comparable exempt units after the window (C-28): lifting the displaced pressure and the return of covered units push them down; sitting tenants who are priced out push them up. Rents in Eastfield and Northgate (C-29): displaced tenants move there, rationed seekers move back. New rental building (C-30) follows the exempt rents. Owners' lobbying (C-26).

**What does not reverse:** Condominium conversions (A-9), structural damage that costs more to repair than maintenance would have (A-10), and the capital loss of owners who sold under the ordinance (CR-7c). Restoring capacity takes years (A-18).

**Key conditions:** The controlled rents are well below the market (A-1, 0.95) and landlords use the room (A-2, 0.85); owners believe the repeal will last a few years (A-3, 0.8) or ten to fifteen (A-4, 0.6); conversions are hard to undo (A-9, 0.9). Two premises were added: some covered units were out of use under the ordinance (A-N1, 0.6) and some units were sublet illegally or let with key money (A-N2, 0.8).

**What this analysis cannot say:** How large any effect is, how much of the stock returns or how fast, and whether exempt-segment and neighboring rents end up higher or lower. It does not weigh the gains of landlords and seekers against the losses of sitting tenants, or say whether the repeal is good. Health, safety and environmental effects are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | landlords.covered | net_price_received (rent on covered units) | increase | short; medium | visible | B | CR-1 (op 2: R1 removes the ceiling, at once on vacancy and in 15% steps at renewal); CR-6 (with the price free to move, it tends toward the level at which planned lettings and rentals are compatible; A-1: that level is well above the controlled rent); CR-5c (the range of acceptable terms moves); A-2: landlords use the room | A-1, A-2 | partial (short: the 15% steps); none (from the second anniversary) |
| C-2 | tenants.sitting | price_paid (rent) | increase | short; medium | visible | B | CR-1 (op 3: staying now brings a higher rent); CR-6 and CR-5c as for C-1; capped at 15% at each renewal for two years, then free | A-1, A-2 | partial (short: the 15% steps); none (from the second anniversary) |
| C-3 | prospective_tenants | price_paid (covered units let on vacancy) | increase | short | visible | B | CR-1 (op 2 for landlords: a vacant unit may be let at any rent); CR-6 (the price moves toward the clearing level, A-1, A-2) | A-1, A-2 | none (vacancy decontrol is immediate) |
| C-4 | owners.covered_buildings | asset_value (covered buildings) | increase | short (from announcement) | invisible | B | CR-10c (the value of a durable means reflects the yields it is expected to bring); CR-7c (the lasting rise in expected yield, C-1, is captured by whoever owns the building when the repeal becomes expected, six months before the effective date; A-3: owners expect decontrol to last) | A-1, A-3 | partial: values recover, but owners who sold under the ordinance at a depressed price do not recover their loss (CR-7c), and converted or damaged buildings do not regain it (A-9, A-10) |
| C-5 | buyers.covered_buildings | price_paid (covered buildings) | increase | short; medium | invisible | B | CR-7c (later buyers pay a price at which they expect to earn what they could elsewhere, so they do not share the gain); CR-8 symmetry (the seller's gain, C-4, is matched by what the buyer pays) | A-1, A-3 | none |
| C-6 | officials.rent_board | enforcement_cost | decrease | medium (after dissolution) | visible | A | CR-1 (op 4: R3 ends the board after two years); CR-8c (resources no longer used up in administering and enforcing) | none | none |
| C-7 | taxpayers.city | resources_available_other_uses | increase | medium | invisible | B | CR-8a (the board's budget is no longer withdrawn from other uses); CR-8d (the saving reaches other uses only if other spending is not fixed; A-20) | A-20 | none |
| C-8 | landlords.covered | units_held_vacant | increase | short (six-month announcement window) | invisible | B | CR-10a (an expected change alters choices now); CR-4 (x: re-let a unit that falls vacant at the capped rent, y: keep it empty until the effective date and let it at the market rent; y made better by the expected repeal) | A-11 | n/a (transition effect) |
| C-9 | landlords.covered | units_held_vacant | decrease | medium; long | invisible | B | CR-4 (x: keep a unit out of use, y: let it; y made better by R1, so owners for whom the two were close let it); CR-10b (units that need repair come back only through investment, A-18) | A-N1, A-18 | partial (units needing major repair return over several years, A-18) |
| C-10 | landlords.covered | maintenance_spending | increase | short; medium | invisible | B | CR-4c (each unit of maintenance now brings a higher rent, so the marginal repair, previously not worth doing, is done; x: defer, y: maintain); CR-10c (repairs pay back only if decontrol is expected to last long enough, A-3) | A-2, A-3 | partial (A-10: deferred maintenance that became structural damage costs more to repair than it would have cost to maintain) |
| C-11 | landlords.covered | investment_target (major renovation of covered buildings) | increase | medium; long | invisible | B | CR-4 (renovation now yields the market rent); CR-10c (major works pay back only over ten to fifteen years, A-4); CR-10b (the stock is restored through flows over several years, A-18) | A-4, A-18 | partial (A-10, A-18) |
| C-12 | tenants.covered_units | quality_per_unit | increase | medium; long | invisible | B | CR-9 (maintenance and renovation are input_to the quality of the housing service, C-10, C-11); CR-10b (quality is a stock that changes only through flows; damage costs more to undo, A-10, and takes years, A-18) | A-2, A-3, A-10, A-18 | partial (A-10, A-18) |
| C-13 | landlords.covered | reclassification (conversion of rental buildings to condominiums) | decrease | short; medium | invisible | B | CR-4 (x: convert to condominiums, y: keep renting; R1 makes y better, so owners in the permit process for whom the two were close withdraw, A-15); CR-4a (no owner who was renting starts converting because of the repeal) | A-15, A-2 | full for buildings already converted (A-9; reconversion needs A-16, p 0.1); none for the flow of new conversions |
| C-14 | landlords.covered | capital_stock_target (rental units in formerly covered buildings) | increase | medium; long | invisible | B | CR-10b (the rental stock changes only through flows: fewer conversions, C-13; units returned to use, C-9; repair, C-11); CR-10b (converted units stay converted: reversal costs more than the restored yield, A-9) | A-15, A-N1, A-18 | partial (A-9: past conversions do not return; A-18: restoration is slow) |
| C-15 | tenants.sitting | turnover | increase | short; medium | invisible | B | CR-4 (x: stay at the higher rent, y: move to a cheaper unit or another city; x made worse, so tenants who ranked staying narrowly above moving move, A-6); from the second anniversary R2 also lets landlords end tenancies without cause (CR-1 op 1 for tenants) | A-6, A-1 | none |
| C-16 | landlords.covered | side_payments (payments to sitting tenants to leave) | increase | short (phase-in years) | invisible | B | CR-4 (x: wait two years for the sitting tenant's rent to reach the market level, y: pay the tenant to leave and let the unit at once at any rent; read with the input's assumed reading of the unclear provision, that such a unit counts as vacant); CR-5 (the payment takes place only where the tenant ranks it above the remaining capped years and the landlord ranks the vacancy above the payment) | A-13, A-1 | n/a (transition effect) |
| C-17 | tenants.sitting.accepting_payment | resources_available_other_uses | increase | short | invisible | B | CR-5 (the tenant accepts only a payment ranked above what is given up); CR-8b (the payment is a receipt to the tenant of what the landlord pays) | A-13 | n/a (transition effect) |
| C-18 | tenants.sitting | search_cost | increase | short; medium | invisible | B | CR-4 (tenants who move, C-15, must search for another unit); CR-8c (time and money spent searching are used up) | A-6 | none |
| C-19 | tenants.sitting | job_changes | increase | medium | invisible | B | CR-9 (relation: a controlled tenancy is a complement, by location, of the tenant's job; while the rent gap lasted, a move to take a job meant losing it); CR-4 (x: keep the current job, y: take a job that requires moving; the repeal removes what moving cost, so y improves; A-12) | A-12, A-1 | none |
| C-20 | prospective_tenants | search_cost | decrease | short; medium | invisible | B | CR-6 (when the price can move, the pressure that went into searching and queuing is no longer displaced there); CR-11a (the rent again conveys scarcity, so seekers learn what is available at what price) | A-1 | none |
| C-21 | prospective_tenants | allocation_by_non_price_criteria | decrease | short; medium | invisible | B | CR-6 (the criteria by which the scarce side chose among seekers, such as connections or preference for some tenants, lose their role when the price can clear the market) | A-1 | none |
| C-22 | prospective_tenants | side_payments (key money and payments for illegal sublets) | decrease | short; medium | invisible | B | CR-6 (exchanges outside the rule took place because the controlled price was below the clearing level; with the price free, that gap closes); CR-4 (x: comply, y: violate; the gain from violating falls) | A-N2, A-1 | none |
| C-23 | tenants.sitting | informal_activity (illegal sublets) | decrease | short; medium | invisible | B | CR-4 (x: occupy or give up the unit, y: sublet it illegally at a higher rent; the margin between the tenant's rent and the market rent shrinks, so y gains less); CR-6 | A-N2, A-1 | none |
| C-24 | prospective_tenants | quantity_traded (covered units let to new tenants) | increase | short; medium | invisible | B | CR-5 (lettings that the ceiling prevented, because units were held by tenants who valued them less or kept out of use, now take place); CR-4 (turnover, C-15, and units returned to use, C-9) | A-6, A-1 | none |
| C-25 | tenants.sitting | lobbying_effort (to restore controls) | increase | short; medium | invisible | B | CR-4 (x: accept the repeal, y: organize to restore controls; R1 makes x worse for sitting tenants, so lobbying gains); CR-8c (resources spent lobbying are used up) | A-14 | n/a (transition effect) |
| C-26 | owners.covered_buildings | lobbying_effort | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-4 (x: accept a possible return of controls, y: lobby to keep the repeal; their gain, C-4, is at stake); (-) in the counterfactual owners would keep spending to repeal the ordinance, which they no longer need to do. No premise says which dominates | A-14 | n/a |
| C-27 | tenants.exempt_units | price_paid (comparable exempt units) | increase | short (announcement window and first months) | invisible | B | CR-9 (relation: covered and exempt units are same_market_other_segment, close substitutes, A-5); units held empty in the window, C-8, are not offered, so seekers turn to exempt units (CR-4, x: covered unit, y: exempt unit) | A-11, A-5 | n/a (transition effect) |
| C-28 | tenants.exempt_units | price_paid (comparable exempt units) | ambiguous | medium; long | invisible | B | CR-12b: (-) CR-6 (with the ceiling gone, unsatisfied demand for covered units is no longer displaced to the exempt segment) and CR-10b (more covered units come back into use, C-14); (+) CR-4 (x: stay in a covered unit at the higher rent, y: move to an exempt unit; sitting tenants who move, A-6, add to demand there). No premise establishes which dominates | A-5, A-6, A-15 | none |
| C-29 | tenants.neighboring_cities | price_paid (rents in Eastfield and Northgate) | ambiguous | medium | invisible | B | CR-12b: (+) CR-4 (x: stay in Riverton at the higher rent, y: move to a neighboring city and commute; A-6, A-7); (-) CR-4 (x: live in a neighboring city and commute, y: rent a Riverton unit now available at the market rent; seekers who were rationed out move back, A-7). No premise says which dominates | A-6, A-7 | none |
| C-30 | developers | investment_target (new rental buildings) | ambiguous | medium; long | invisible | B | CR-9 (relation: new buildings are in the exempt segment); CR-10c (investment follows expected yields); A-8: the exempt-segment premium was feeding new building, so the sign follows exempt rents, C-28, which is ambiguous. The chain through fear of controls returning or of the exemption being withdrawn needs A-19 or A-17 (below 0.5) | A-8, A-5, A-6 | partial (buildings not built under the ordinance are not built retroactively: CR-10b) |
| C-31 | buyers.condominiums | price_paid (condominiums) | increase | medium; long | invisible | B | CR-9 and CR-7a (a building's rental use and condominium use are alternative uses of the same means; fewer conversions, C-13, mean fewer condominiums offered); CR-6 (the price moves to a higher clearing level) | A-15, A-2 | partial (condominiums already converted stay on the market, A-9) |
| C-32 | input_suppliers.building_trades | quantity_traded (repair and renovation work) | increase | medium | invisible | B | CR-9 and LW-10 (relation: repair and renovation work input_to covered housing; demand for the input follows the higher yield of the housing, C-10, C-11) | A-3, A-4 | none |
| C-33 | tenants.sitting | resources_available_other_uses | decrease | short; medium | invisible | B | CR-8b (each extra dollar of rent is the landlord's receipt, C-1; CR-8 symmetry); CR-3a (tenants who stay fall back to an option they ranked lower than staying at the old rent) | A-1, A-2 | partial (short: the 15% steps); none (from the second anniversary) |

## Gaps found

**(a) Calculus gaps.** None. Every step used CR-1 to CR-12, LW-10 or arithmetic. Persistence was derived from CR-10b with the reversal-cost premises A-9, A-10 and A-18.

**(b) New premises.**
- A-N1 (p 0.6): needed for C-9 and part of C-14. CR-4 gives the direction (no owner takes a unit out of use because the ceiling is lifted), but it changes anything only if some units were out of use under the ordinance; A-18 mentions "bringing units back into use" without stating it as a premise.
- A-N2 (p 0.8): needed for C-22 and C-23. CR-6 says the pressure leaves the margins outside the rule when the price can move, but only if trade had moved there; this was a WE-001 assumption (A-3) and is not among WE-022's.

**(c) Unclear core rules.**
- CR-6 with CR-12b on a repeal (C-28): CR-6 read symmetrically says removing the ceiling lifts the pressure displaced to the exempt segment, while CR-4 says sitting tenants priced out move into it. Arithmetic on occupied units (households housed in covered units can only rise if covered units in use rise) could decide the sign, but CR-12b speaks of "a premise" and does not say whether an accounting identity counts as one. Left ambiguous.
- CR-4 for lobbying (C-26): the rule compares x (accept) and y (lobby) for one change, but on a repeal the counterfactual also has lobbying, in the other direction. The rule does not say how to sign the change in effort when both paths have a stake.
- CR-10b and the persistence field: CR-10b says changes that cost something to undo persist, but persistence is measured against the never-imposed path while signs are measured against the policy staying. For transition effects with no counterpart on either path (buyouts, holding units empty in the window) neither "none" nor "full" fits; "n/a" was used.
