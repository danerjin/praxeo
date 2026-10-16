# WE-044 / Analysis: Ban on short-term rentals of whole homes, with a primary-residence exception

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Saltmere Housing Preservation Ordinance (Ordinance 2026-31).** Saltmere is a coastal city of about 310,000 people and about 128,000 dwellings. About 60,000 of them are rented long-term (median rent $1,850 a month, vacancy about 3%). The 2026 platform report counts about 4,300 active short-term rental (STR) listings: 1,250 rooms in homes where the owner is present (not covered); 2,150 whole units that are not the owner's primary residence (about 1,700 investor units and about 450 second homes, about 70% in the three beach districts); 550 whole units that are the owner's primary residence, let while the owner is away (about 140 let more than 90 nights a year); and 350 whole units in two-unit buildings whose owner lives in the other unit (about 120 let more than 90 nights; subject to U1). A whole-unit STR earns about $30,000 a year net, against about $20,000 net on a 12-month lease. Hotels: about 7,400 rooms, occupancy 79% (94% in July and August), $180 a night, about 2.1 million room-nights a year against about 0.67 million whole-unit STR nights; new hotels take three to five years. Furnished lets of 30 nights or more: about 900 units at about $3,200 a month. About 6% of a year's whole-unit STR nights are booked more than nine months ahead. About 30% of 2023–2025 home purchases in the beach districts were by non-occupants. Elsdon, 12 km from the Harbor district, has about 420 STR listings and no STR rules.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | City of Saltmere, all zones. Elsdon (no STR restriction) 12 km away. | §1: "This ordinance applies to every dwelling unit within the City." |
| Announced / enacted / effective / expires | Introduced 3 November 2026 by six of nine council members (announced). Enacted 8 December 2026. Effective 1 July 2027; stays booked and confirmed before 1 July 2027 may be completed if they end by 30 September 2027. No expiry. | §9 |
| Enforcement (who, penalties, resources) | K2 against platforms: Registry Unit notices, $1,000 per listing per day after 10 days. K4 against hosts: Code Enforcement, on complaint only, $2,500 first violation, $5,000 each later one, within existing appropriations; fines to the general fund. K3: Registry Unit, five staff, $520,000 a year, new general-fund appropriation. | §6, §7, §8 |
| Existing rules (stay in the counterfactual) | R1 STR registration ($150 a year; about 65% of hosts registered). R2 Transient occupancy tax (TOT) 12% on stays under 30 nights, hotels and STRs; about $18.7 million a year from whole-unit STRs and $46 million from hotels. R3 Noise and nuisance ordinance, on complaint: about 1,500 of 9,600 complaints in 2025 about STR units, about 2.5 staff hours each. Code Enforcement budget fixed at $6.1 million (48 staff). | Municipal Code §5.12, §3.30, §8.04 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Ban | `prohibition` (letting a whole unit for under 30 consecutive nights) | Whole-unit STR | Owners and anyone letting a unit | From 1 July 2027, only the owner's primary residence (resides at least 270 days a year), registered under K3, for at most 90 nights a year (45 for July–December 2027). Stays booked before 1 July 2027 may be completed if they end by 30 September 2027; all other later bookings cancelled and refunded in full. | Rooms in the owner's primary residence while the owner is present; lets of 30 nights or more. |
| K2 Platform duty | Rule on intermediaries | Listings | Booking platforms | Display a K3 number on every whole-unit listing; remove a listing within 10 days of notice; report nights per registration number each quarter. $1,000 per listing per day. | — |
| K3 Registry | `licensing_requirement` for the exempt use | Primary-residence lets | Owners who let their primary residence | $250 a year, proof of residence. Replaces R1 for whole units. | — |
| K4 Host enforcement | Enforcement | K1 | Code Enforcement | On complaint only; fines as above; no new appropriation. | — |

Unclear provisions:
- **U1, two-unit buildings.** U1-a: "the dwelling" is the building, so the second unit may be let up to 90 nights a year. U1-b: "the dwelling" is the unit, so the second unit may not be let for under 30 nights. About 350 listings, 120 of them above 90 nights. The Registry Unit will decide when it issues or refuses numbers. No probability; one sign per reading.

Counterfactual: Saltmere without the ordinance, with R1 to R3 in force.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Ban | triangular (prohibits exchanges between owners and guests) | Yes for most non-primary units (A-1); enforced through platforms (A-2) and, off-platform, only by complaint (A-3, A-19) | 1 (removes the option of letting a non-primary whole unit for under 30 nights, where enforced); 3 (attaches a fine risk where not enforced); 1 (removes nights above 90 for primary-residence hosts); per U1 for two-unit buildings: U1-a op 1 on nights above 90, U1-b op 1 on all short nights; 1 (removes booked future stays after 30 September 2027, A-24) | CR-2, CR-3a, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10a, CR-10c, CR-11b |
| K2 Platform duty | triangular (condition on intermediaries' exchanges) | Yes (A-2) | 3 (compliance duties and fines attached to listing whole units) | CR-1, CR-8c, CR-4 (x: comply, y: violate) |
| K3 Registry | triangular (licence for the exempt use) | Yes for primary-residence hosts who list on platforms (A-2) | 3 ($250 fee and proof attached to the exempt use; replaces R1's $150); 4 (general-fund appropriation to the Registry Unit) | CR-3a, CR-4 (fixed cost per outlet), CR-8b, CR-8c |
| K4 Host enforcement | binary (state time used) and part of K1 | Partly: on complaint only (A-19) | 3 (fine risk attached to unlawful lets, scaled by neighbors' choice to complain) | CR-4 (x: comply, y: violate), CR-6 (fixed Code Enforcement budget), CR-8b, CR-8c |

The law in the counterfactual lets any owner let a whole unit for any number of nights, so K1 removes an option (CR-1 recording note). The ordinance fixes no price; CR-6 enters where it fixes quantities (no non-primary STR nights, at most 90 for the exempt use) and where a budget fixes Code Enforcement's capacity.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| owners.non_primary_units | About 1,700 investor units and 450 second homes let whole | Op 1 (short lets removed where enforced); op 3 (fine risk off-platform). Next-best options: 12-month lease, mid-term let, sale, own use and vacancy, evasion, reclassification (CR-4 for each pair). |
| owners.second_homes | Subset of the above who use the home some weeks | As above, plus the option of keeping it for own use and leaving it empty (A-6). |
| owners.primary_residence_hosts | 550 whole-unit lets of the owner's home | Op 3 (K3 fee and proof); op 1 on nights above 90 (about 140 hosts). |
| owners.two_unit | 350 second units in owner-occupied two-unit buildings | U1-a: as primary-residence hosts; U1-b: as non-primary units. |
| owners.room_hosts | 1,250 rooms in occupied homes (exempt) | No operation; through CR-9 (substitute) more guests. |
| sellers.prospective (room and primary-residence lets) | Residents who could start letting a room or their home | Through CR-9: entry pays more (CR-4, x: stay out, y: enter). |
| guests.whole_unit | Visitors who book whole units | Op 1 on their chosen exchange; must choose among hotels, rooms, primary-residence lets, 30-night lets, Elsdon, off-platform lets, or no trip. |
| guests.booked_after_30_Sep_2027 | Guests holding bookings for stays after 30 September 2027 | Op 1: bookings cancelled and refunded (A-24). |
| platforms | Booking intermediaries | Op 3: K2 duties and fines; lose whole-unit bookings in Saltmere. |
| hotels | Sellers of the closest commercial substitute | Through CR-9 (substitute): more demand with fixed rooms (A-9). |
| buyers.substitutes (hotel guests) | Guests who would stay in hotels anyway | Through CR-9: compete with displaced guests for fixed rooms. |
| sellers.substitutes (mid-term lets) | Landlords of furnished lets of 30 nights or more | Through CR-9: more supply (A-7) and more demand (A-31). |
| tenants.long_term | Current and prospective long-term tenants in Saltmere | Through CR-9 (same_market_other_segment): more units offered (A-5). |
| landlords.long_term | Existing long-term landlords | Through CR-9: more competing units. |
| investors.home_buyers | Non-occupant buyers of homes in the beach districts | Op 1 on the STR use of any home they would buy (A-21). |
| buyers.prospective (owner-occupiers) | Buyers of homes to live in, beach districts | Through CR-9 (same market): fewer competing investors; proximity chain (A-23). |
| neighbors | Residents near STR units | Through `proximity` (CR-9, Tier C): fewer transient neighbors; K4 makes their complaints the trigger of enforcement. |
| neighboring_jurisdictions (Elsdon hosts, owners, tenants, businesses) | Across the border | Through `across_border` (A-10): more visitor demand; owners move units from long-term to STR (A-29). |
| sellers.complements (beach-district shops and restaurants) | Sell meals and goods near lodging | Through CR-9 (`complement`, location, A-12): fewer visitors, more residents. |
| input_suppliers (cleaning and management firms) | Service STR units | Through CR-9 (`input_to`): fewer nights serviced (A-26). |
| officials.registry | Registry Unit | Op 4: $520,000 a year; decides U1. |
| officials.code_enforcement | Enforces K4 and R3 on a fixed budget | More complaints about unlawful lets (A-19); fewer nuisance complaints about operating STR units (A-18). |
| city.general_fund | Receives TOT and fines; pays the Registry Unit | Through CR-8b: TOT base changes; fines received. |
| taxpayers | Fund the general fund | Op 4 via the appropriation (A-20). |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 to K3 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | owners.non_primary_units | quantity_supplied (whole-unit STR nights, legal market) | decrease | short; medium; long | CR-1 op 1, CR-2, CR-4a | A-2 |
| C-2 | guests.whole_unit, platforms | quantity_traded (whole-unit STR nights booked on platforms, Saltmere) | decrease | short; medium; long | CR-1 op 1, CR-5a | A-2 |
| C-3 | owners.non_primary_units | return_on_capital (units formerly let short) | decrease | short; medium; long | CR-3a, CR-4b, CR-5a | A-1, A-2 |
| C-4 | owners.non_primary_units | asset_value (units used as whole-unit STR) | decrease | short (from 3 November 2026) | CR-7c, CR-10c | A-1, A-30 |
| C-5 | owners.primary_residence_hosts | compliance_cost (K3 fee and proof of residence) | increase | short; medium; long | CR-1 op 3, CR-8c | A-2 |
| C-6 | owners.primary_residence_hosts (about 140 above 90 nights) | quantity_supplied (STR nights above 90 a year) | decrease | short; medium; long | CR-1 op 1, CR-4a | A-2 |

## 5. Responses

CR-4 for every pair of options each class has; CR-5 for prevented exchanges; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | owners.non_primary_units | quantity_supplied (12-month leases) | increase | medium; long | CR-4 (x: short let, y: 12-month lease), CR-7a | A-5, A-2 |
| C-8 | owners.non_primary_units | quantity_supplied (furnished lets of 30 nights or more) | increase | short; medium; long | CR-4 (x: short let, y: mid-term let) | A-7, A-2 |
| C-9 | owners.second_homes | units_held_vacant | increase | short; medium; long | CR-4 (x: let, y: own weeks only, empty otherwise) | A-6, A-2 |
| C-10 | owners.non_primary_units (in breach) | informal_activity (whole-unit short lets booked directly, off-platform) | increase | short; medium; long | CR-4 (x: comply, y: violate), CR-6 | A-3, A-4 |
| C-11 | owners.primary_residence_hosts, owners.two_unit | legal_breach (nights above 90 spread over several platforms) | increase | short; medium; long | CR-4 (x: comply, y: violate) | A-22 |
| C-12 | owners.non_primary_units | reclassification (nominal 30-night contracts for shorter stays; claims of primary residence) | increase | short; medium; long | CR-4 (x: covered form, y: uncovered form) | A-N1 |
| C-13 | owners.non_primary_units | quantity_supplied (homes offered for sale, beach districts) | increase | short; medium | CR-4 (x: hold, y: sell) | A-N2 |
| C-14 | investors.home_buyers | quantity_demanded (homes in the beach districts) | decrease | short; medium; long | CR-1 op 1, CR-4, CR-7c | A-21, A-1 |
| C-15 | owners.two_unit | quantity_supplied (whole-unit STR nights in two-unit buildings) | U1-a: ambiguous; U1-b: decrease | short; medium; long | CR-1 op 1, CR-4, CR-12b | A-2, A-32 |
| C-16 | owners.two_unit | asset_value (second units) | U1-a: ambiguous; U1-b: decrease | short (from 3 November 2026) | CR-7c, CR-10c, CR-12b | A-1, A-30, A-32 |
| C-17 | owners.room_hosts, owners.primary_residence_hosts, their guests | price_paid (room lets and primary-residence lets) | increase | short; medium; long | CR-9 (substitute), CR-6 | A-32, A-2 |
| C-18 | owners.room_hosts | quantity_supplied (room-nights) | increase | short; medium; long | CR-4c, CR-9 | A-32, A-2 |
| C-19 | owners.primary_residence_hosts | quantity_supplied (STR nights, all hosts) | ambiguous | short; medium; long | CR-12b (cap −; higher price +) | A-2, A-32 |
| C-20 | sellers.prospective (room and primary-residence lets) | entry_rate | increase | medium | CR-4 (x: stay out, y: enter), CR-7a | A-32, A-2 |
| C-21 | guests.whole_unit | full_cost_per_unit (lodging for a Saltmere stay) | increase | short; medium; long | CR-3a, CR-6, CR-9 | A-2, A-8 |
| C-22 | guests.whole_unit | quantity_demanded (trips to Saltmere) | decrease | short; medium; long | CR-4 (x: trip, y: no trip or another place) | A-11, A-2 |
| C-23 | guests.whole_unit | cross_border_purchases (lodging in Elsdon) | increase | short; medium; long | CR-4 (x: here, y: there) | A-10, A-2 |
| C-24 | guests.whole_unit | travel_time | increase | short; medium; long | CR-4, CR-3a | A-10, A-2 |
| C-25 | guests.whole_unit (off-platform) | quality_information | decrease | short; medium; long | CR-11b | A-3, A-4 |
| C-26 | owners.non_primary_units (in breach) | allocation_by_non_price_criteria (guest screening) | increase | short; medium; long | CR-4, CR-6 | A-3, A-4, A-19, A-27 |
| C-27 | guests.booked_after_30_Sep_2027 | quantity_traded (stays booked before 3 November 2026) | decrease | short | CR-1 op 1, CR-5a | A-24, A-2 |
| C-28 | guests.booked_after_30_Sep_2027 | search_cost | increase | short | CR-3a, CR-8c | A-24, A-2 |
| C-29 | owners.non_primary_units, platforms | lobbying_effort (to repeal or relax K1) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-14, A-1 |
| C-30 | hotels, neighbors (associations) | lobbying_effort (to keep or tighten K1) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-14, A-8 |
| C-31 | platforms | compliance_cost (numbers, removals, quarterly reports) | increase | short; medium; long | CR-1 op 3, CR-8c | A-2 |
| C-32 | guests.whole_unit | quantity_traded (whole-unit STR nights, 3 Nov 2026 to 30 Jun 2027) | increase | short (announcement window) | CR-10a, CR-4 (x: trip after 1 July, y: before) | A-17 |
| C-33 | guests.whole_unit | quantity_traded (whole-unit STR nights, 1 Jul to 30 Sep 2027) | decrease | short (transition window) | CR-1 op 1, CR-10a, CR-4 | A-2 |
| C-34 | guests.whole_unit | quantity_traded (bookings made 3 Nov 2026 to 30 Jun 2027 for stays 1 Jul to 30 Sep 2027) | increase | short (announcement window) | CR-10a, CR-4 (x: book later, y: book before 1 July) | A-15 |
| C-35 | guests.whole_unit | quantity_traded (bookings made 1 Jul to 30 Sep 2027 for stays in that window) | decrease | short (transition window) | CR-1 op 1, CR-10a | A-2, A-15 |
| C-36 | owners.non_primary_units | quantity_supplied (12-month leases starting August–September 2027) | increase | short (transition) | CR-10a, CR-4 (x: summer lets, y: free unit for leasing season or sale) | A-16, A-5 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Effects on customers of hotels' and shops' suppliers are pruned at depth 3 as diffuse bystander effects.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-37 | tenants.long_term | price_paid (long-term rent, Saltmere) | decrease | medium; long | CR-9, CR-6 | former STR units same_market_other_segment of long-term rentals (close) | A-5, A-13, A-2 |
| C-38 | tenants.long_term | quantity_traded (long-term leases, Saltmere) | increase | medium; long | CR-9, CR-5, CR-6 | as above | A-5, A-13, A-2 |
| C-39 | landlords.long_term | net_price_received (long-term rent) | decrease | medium; long | CR-9, CR-6, CR-7a | as above | A-5, A-13, A-2 |
| C-40 | landlords.long_term | asset_value (rental buildings) | decrease | short (from 3 November 2026) | CR-7c, CR-10c | as above | A-5, A-13, A-30 |
| C-41 | hotels, buyers.substitutes | price_paid (hotel rooms) | increase | short; medium; long | CR-9, CR-6, CR-12e | whole-unit STR substitute for hotel rooms (partial) | A-8, A-2 |
| C-42 | hotels | quantity_traded (hotel room-nights) | increase | short; medium; long | CR-9, CR-5 | as above | A-8, A-2 |
| C-43 | hotels | asset_value (hotels) | increase | short (from 3 November 2026) | CR-7c, CR-10c | as above | A-8, A-9, A-30 |
| C-44 | hotels | investment_target (hotel rooms) | increase | long | CR-4 (x: stay out, y: build), CR-7a | as above | A-8, A-25 |
| C-45 | buyers.substitutes (guests who would stay in hotels anyway) | quantity_traded (their hotel room-nights) | decrease | short; medium | CR-4c, CR-6 | as above; shared fixed room stock | A-8, A-9, A-2 |
| C-46 | sellers.substitutes (mid-term lets) | quantity_traded (furnished lets of 30 nights or more) | increase | short; medium; long | CR-4, CR-5, CR-12d | short let substitute for mid-term let (partial) | A-7 or A-31 (independent chains) |
| C-47 | sellers.substitutes (mid-term lets) | price_paid (furnished lets of 30 nights or more) | ambiguous | short; medium; long | CR-6, CR-12b | as above | A-7, A-31 |
| C-48 | neighboring_jurisdictions (Elsdon hosts) | net_price_received (Elsdon STR nights) | increase | short; medium; long | CR-9, CR-6 | Saltmere STR across_border Elsdon STR | A-10, A-2 |
| C-49 | neighboring_jurisdictions (Elsdon owners) | asset_value (homes suitable for STR, Elsdon) | increase | short (from 3 November 2026) | CR-7c, CR-10c | as above | A-10, A-30 |
| C-50 | neighboring_jurisdictions (Elsdon tenants) | price_paid (long-term rent, Elsdon) | increase | medium; long | CR-7a, CR-9, CR-6 | Elsdon STR same_market_other_segment of Elsdon long-term rentals | A-10, A-29 |
| C-51 | sellers.complements (beach districts) | quantity_complement (visitors' purchases near lodging) | decrease | short; medium; long | CR-9, LW-10, CR-12d | visitor lodging complement (location) of nearby meals and goods | A-12, A-2, and A-10 or A-11 |
| C-52 | sellers.complements (beach districts) | quantity_complement (all purchases near lodging, visitors and residents) | ambiguous | medium; long | CR-9, CR-12b | as above; plus residents of re-let units | A-12, A-N3, A-5 |
| C-53 | neighboring_jurisdictions (Elsdon businesses) | quantity_complement (visitors' purchases) | increase | short; medium; long | CR-9, LW-10 | as above, across_border | A-10, A-12 |
| C-54 | input_suppliers (cleaning and management firms) | employment (STR cleaning and management) | decrease | short; medium; long | CR-9, LW-10, CR-7a | cleaning and management input_to STR nights | A-26, A-2 |
| C-55 | city.general_fund | tax_revenue (TOT) | ambiguous | short; medium; long | CR-8b, CR-9, CR-12b | STR and hotel nights both in the TOT base | A-2, A-8, A-9 |
| C-56 | city.general_fund | non_tax_receipts (K4 fines) | increase | short; medium; long | CR-8b | — | A-19, A-3 |
| C-57 | owners.non_primary_units (in breach, fined) | resources_available_other_uses | decrease | short; medium; long | CR-8b, CR-3 note | — | A-19, A-3 |
| C-58 | officials.registry | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | — | none |
| C-59 | taxpayers or recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | CR-8a, CR-8b (0.7: payers from the general budget) | — | A-20 |
| C-60 | residents filing other complaints with Code Enforcement | wait_time (handling of other complaints) | ambiguous | short; medium; long | CR-6 (0.7 public supply), CR-12b | shared_facility (fixed Code Enforcement staff) | A-19, A-18 |
| C-61 | buyers.prospective (owner-occupiers) | price_paid (homes, beach districts) | ambiguous | short; medium; long | CR-9, CR-6, CR-7a, CR-12b | investor and owner-occupier demand same_market; proximity | A-21, A-N2, A-23 |
| C-62 | neighbors (owner-occupiers, beach districts) | asset_value (owner-occupied homes) | ambiguous | short; medium; long | CR-7c, CR-9, CR-12b | same_market; proximity | A-21, A-23, A-30 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| owners.primary_residence_hosts, quantity_supplied (all STR nights) | Higher nightly price from displaced guests draws hosts under 90 nights toward 90 (CR-9, CR-4c, A-32) | Nights above 90 removed for about 140 hosts (CR-1 op 1, A-2); K3 fee is a fixed cost per outlet, which can end lets for the lightest users (CR-4, 0.8 note) | None | ambiguous (C-19) |
| owners.two_unit, quantity_supplied, U1-a | Same as the row above (A-32) | Nights above 90 removed for about 120 (A-2) | None | U1-a: ambiguous; U1-b: decrease (C-15) |
| owners.two_unit, asset_value, U1-a | Higher nightly rate on up to 90 nights (A-32) | Nights above 90 removed (A-1, A-2) | None | U1-a: ambiguous; U1-b: decrease (C-16) |
| sellers.substitutes (mid-term), price_paid | Guests extend stays to 30 nights (A-31) | Owners move units into mid-term lets (A-7) | None | ambiguous (C-47); quantity traded: both chains push up, increase (C-46) |
| hotels, price_paid, long | Displaced demand (A-8) | New hotel rooms (A-25) | CR-12e response argument: entry is drawn by the higher yield and stops once yields are equal, so it cannot push the price below the counterfactual | increase (C-41) |
| sellers.complements (beach districts), quantity_complement, total | Residents of units moved to 12-month leases buy near home (A-N3, A-5) | Fewer visitors buy near lodging (A-12, with A-10 or A-11) | None | ambiguous (C-52). The visitors' item alone is decrease (C-51), recorded separately under CR-12 (0.8, two items in one variable) |
| city.general_fund, tax_revenue (TOT) | Hotel nights and hotel prices rise (C-41, C-42) | Whole-unit STR nights fall (C-2); off-platform lets pay no TOT (C-10) | None: the case figures do not let hotel gains be compared with the $18.7 million STR base, since peak capacity limits hotel gains (A-9) | ambiguous (C-55) |
| residents with other complaints, wait_time | Complaints about unlawful lets added to a fixed staff (A-19) | Fewer nuisance complaints as fewer STR units operate (A-18, C-1) | None: hours per K4 complaint are not in the case | ambiguous (C-60) |
| buyers.prospective (owner-occupiers), price_paid (homes) | Some buyers value fewer transient neighbors (A-23, proximity, Tier C) | Fewer investor bids (A-21) and more homes offered (A-N2) | None | ambiguous, Tier C (C-61) |
| neighbors, asset_value (owner-occupied homes) | Proximity (A-23, Tier C) | Lower demand in the same market (A-21) | None | ambiguous, Tier C (C-62) |
| guests.whole_unit, quantity_traded, 3 Nov 2026 to 30 Jun 2027 | Trips moved before 1 July (A-17) | Owners who sell or stop letting before 1 July (A-N4, p 0.4: below the cut-off) | CR-12 (0.8, kind 2): the opposing chain needs a premise below 0.5, so the derived sign is reported and the chain is listed in section 10 | increase (C-32) |
| owners.non_primary_units, quantity_supplied (12-month leases) | C-7, C-36 | none | — | increase |
| tenants.long_term, price_paid | — | Added units (A-5, A-13); no derived chain raises long-term demand in Saltmere | — | decrease (C-37) |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement (3 November 2026).** Six of nine members sponsored the bill, so passage was likely from introduction (A-30). Asset values move then, not on 1 July 2027: STR units fall (C-4), two-unit second units fall under U1-b (C-16), long-term rental buildings fall (C-40), hotels and Elsdon homes rise (C-43, C-49) (CR-7c, CR-10c). The loss falls on whoever owns an STR unit on or after introduction, partly before enactment as the probability rose.
- **Before 1 July 2027.** Guests who want whole units move trips before the ban (C-32, A-17) and book summer stays before 1 July so that they qualify for the transition (C-34, A-15). Both are timing shifts, signed per window against the counterfactual. Bookings made after 1 July for July to September stays fall to those of exempt units (C-35).
- **1 July to 30 September 2027.** Only stays booked before 1 July may be completed. Nights in this window fall (C-33). Some owners end or refuse summer lets to have the unit free for the August–September leasing season or a sale (A-16), so leases starting then rise (C-36). These are transition effects; no lasting stock is involved in them, but the leases that start then persist (CR-10b).
- **Bookings for later stays.** About 6% of a year's nights are booked more than nine months ahead (A-24), so some bookings made before introduction are cancelled and refunded (C-27, C-28). The refund returns what the guest paid (CR-8b: no net transfer), but the expected gain from the stay is lost on both sides (CR-5a).
- **Medium and long run.** Units move to 12-month leases as current guests' stays end and leases are signed (C-7, CR-10b); once let long-term on a lease, they stay in the long-term market for the lease term even if expectations change. Hotels cannot add rooms for three to five years (A-9); after that, rooms are added if sites are available (C-44, A-25), which limits but does not reverse the hotel price rise (C-41). Evasion grows or shrinks with what owners learn about the complaint rate (A-3, A-19).
- **U1 resolution.** Until the Registry Unit decides U1, owners of two-unit buildings face uncertainty about which reading applies. Values move part of the way toward each reading's value, weighted by what owners expect (CR-7c), which the analysis does not estimate.
- **Expectations of repeal.** Owners and platforms lobby to relax the ordinance (C-29). If they expect success, owners keep furniture and listings and choose mid-term lets or vacancy over 12-month leases (CR-10a); that would slow C-7. No premise in the case bears on this, so no sign is given.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-2 | guests.whole_unit, platforms | quantity_traded (whole-unit STR nights) | decrease | Stays guests preferred to every alternative; owners' and platforms' receipts from them | CR-5a |
| C-3 | owners.non_primary_units | return_on_capital | decrease | About $10,000 a year of net yield per unit over the next-best use (A-1) | CR-3a, CR-5a |
| C-5 | owners.primary_residence_hosts | compliance_cost | increase | $250 a year and the time to prove residence | CR-1 op 3, CR-8c |
| C-22 | guests.whole_unit | quantity_demanded (trips to Saltmere) | decrease | Trips not taken by visitors with no close substitute | CR-4, CR-5a |
| C-24 | guests.whole_unit | travel_time | increase | Time traveling from Elsdon | CR-3a |
| C-27 | guests.booked_after_30_Sep_2027 | quantity_traded | decrease | Stays already arranged | CR-5a |
| C-28 | guests.booked_after_30_Sep_2027 | search_cost | increase | Time spent rebooking | CR-8c |
| C-29, C-30 | owners, platforms, hotels, neighbors | lobbying_effort | increase | Time and money spent seeking to change or keep the ordinance | CR-8c |
| C-31 | platforms | compliance_cost | increase | Staff time on numbers, removals and reports | CR-8c |
| C-45 | buyers.substitutes | quantity_traded (hotel nights) | decrease | Hotel stays priced out by displaced guests | CR-4c, CR-5a |
| C-57 | owners in breach, fined | resources_available_other_uses | decrease | Fines paid | CR-8b |
| C-58 | officials.registry | enforcement_cost | increase | $520,000 a year of staff and systems | CR-8c |
| C-59 | taxpayers or recipients of other spending | resources_available_other_uses | at_least_one_decrease | What the $520,000 would otherwise have paid for | CR-8a, CR-8b |
| C-60 | residents with other complaints | wait_time | ambiguous | Code Enforcement hours diverted to K4 complaints (or freed from STR nuisance complaints) | CR-6, CR-8a |

CR-8b check (both sides of every transfer): fines paid by owners (C-57) are received by the general fund (C-56); the Registry's appropriation (C-58) is paid by taxpayers or recipients of other spending (C-59); refunds of cancelled bookings pass from owners and platforms back to guests (no net change; section 8); TOT lost on STR nights and gained on hotel nights both reach the general fund (C-55). K3 replaces R1 for whole units: fees paid by registrants are received by the city; the change in total registration fees cannot be signed from the case figures (fewer whole-unit registrants at a higher fee), so it is not reported.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | For most non-primary units, short lets yield more than any lawful alternative (about $30,000 net against about $20,000). | binding | 0.9 | Platform revenue data; long-term rents. | C-3, C-4, C-14, C-16, C-29 fail or lose this chain. |
| A-2 | Platforms comply with K2. | enforcement | 0.85 | Fine exceeds a platform's fee per listing; compliance elsewhere. | Most consequences lose their chain: K1 then attaches only a complaint-driven risk. |
| A-3 | For some units complaints are unlikely, so the expected fine is below the gain from breach. | enforcement | 0.75 | Detached homes; complaint rates by building type. | C-10, C-25, C-26, C-56, C-57 fail. |
| A-4 | Some guests keep wanting whole units in Saltmere enough to book directly. | substitutability | 0.7 | Repeat guests; direct-booking sites. | C-10, C-25, C-26 fail. |
| A-5 | Most non-primary units can be let on 12-month leases, and some owners choose that. | alternative_uses | 0.85 | Unit types; condominium rules; demand. | C-7, C-36, C-37 to C-40, C-52 fail. |
| A-6 | Some second-home owners keep the home and leave it empty the rest of the year. | other | 0.7 | Blocked calendar weeks. | C-9 fails. |
| A-7 | Some owners can let for 30 nights or more. | substitutability | 0.75 | Mid-term listings; hospital and university demand. | C-8 fails; C-46 keeps the A-31 chain; C-47 becomes increase. |
| A-8 | Hotels are a substitute for whole units for some guests. | substitutability | 0.8 | Guest surveys; group sizes. | C-21, C-30, C-41 to C-45, C-55 fail or lose this chain. |
| A-9 | Hotel rooms cannot be added in the short to medium run; peak occupancy near capacity. | durability | 0.85 | Occupancy; planning times. | C-43, C-45 lose this chain; C-55 depends on it for the limit on hotel gains. |
| A-10 | Elsdon is near enough for some guests. | mobility | 0.7 | Travel times. | C-23, C-24, C-48 to C-50, C-53 fail; C-51 keeps the A-11 chain. |
| A-11 | Some visitors with no close substitute shorten or skip trips. | substitutability | 0.65 | Group sizes; suites available. | C-22 fails; C-51 keeps the A-10 chain. |
| A-12 | Visitors buy meals and goods near their lodging. | other | 0.7 | Card-spending data by district. | C-51 to C-53 fail. |
| A-13 | Units added to the long-term market are not offset by withdrawals elsewhere. | substitutability | 0.75 | No other policy change. | C-37 to C-40 fail. |
| A-14 | Hosts, platforms, hotels and neighborhood associations can organize at a cost below their stake. | other | 0.85 | Their activity on the ordinance. | C-29, C-30 fail. |
| A-15 | Guests can book summer stays earlier than they otherwise would. | expectations | 0.7 | Booking lead times. | C-34 fails. |
| A-16 | Some owners planning to convert or sell end or refuse summer lets to free the unit for the leasing season or a sale. | other | 0.6 | Leasing-season timing; sale listings. | C-36 fails; C-33 keeps the A-2 chain. |
| A-17 | Some guests move a later trip to before 1 July 2027. | other | 0.55 | Flexible trip dates. | C-32 fails. |
| A-18 | Nuisance complaints per operating STR unit stay near the 2025 rate. | other | 0.75 | R3 records 2022–2025. | C-60 loses its (−) chain and becomes increase. |
| A-19 | Neighbors file complaints about unlawful lets in meaningful numbers; some lead to fines. | enforcement | 0.8 | City projection of 400 to 1,200 a year. | C-26, C-56, C-57 fail; C-60 loses its (+) chain. |
| A-20 | The $520,000 is new general-fund money. | revenue_use | 0.9 | §8. | C-59 fails as stated (the payers would then be within an existing budget). |
| A-21 | Investors are a material part of demand for homes in the beach districts. | other | 0.8 | About 30% of purchases by non-occupants. | C-14 fails; C-61, C-62 lose their (−) chain. |
| A-22 | Hosts on several platforms can exceed 90 nights without the per-platform reports revealing it. | enforcement | 0.6 | Reports are per platform; no aggregation planned. | C-11 fails. |
| A-23 | Some buyers value fewer transient neighbors (proximity chain). | other | 0.6 | Associations' support; R3 complaints. | C-61, C-62 lose their (+) chain and become decrease. |
| A-24 | Bookings exist for stays after 30 September 2027 made before the introduction. | other | 0.9 | 6% of nights booked more than nine months ahead. | C-27, C-28 fail. |
| A-25 | Hotels can obtain sites and permits to add rooms in the long run. | alternative_uses | 0.55 | Zoning for hotels. | C-44 fails. |
| A-26 | Cleaning and management firms adjust labor to the nights they service. | alternative_uses | 0.8 | Staffing practice. | C-54 fails. |
| A-27 | Hosts in breach can screen guests on traits that predict complaints, and do not price the risk guest by guest. | other | 0.6 | Off-platform practice; house rules. | C-26 fails. |
| A-28 | Rivals file complaints against lawful hosts to raise their costs. | other | 0.3 | No evidence in complaint records. | Not reported (see below). |
| A-29 | Some Elsdon owners move units from long-term leases into STR. | alternative_uses | 0.6 | Elsdon's STR to long-term returns. | C-50 fails. |
| A-30 | Values of STR units, hotels and Elsdon homes rest on expected yields, and passage was likely from introduction. | expectations | 0.8 | Sale prices as multiples of earnings; sponsors. | C-4, C-16, C-40, C-43, C-49, C-62 move at enactment or later instead, or fail. |
| A-31 | Some guests on stays of two to four weeks can extend to 30 nights. | substitutability | 0.6 | Stay lengths; guest types. | C-46 keeps the A-7 chain; C-47 becomes decrease. |
| A-32 | Rooms in occupied homes and primary-residence lets are a substitute for whole units for some guests. | substitutability | 0.75 | Guest overlap on platforms. | C-17, C-18, C-20 fail; C-15 (U1-a), C-16 (U1-a) and C-19 lose their (+) chain and become decrease. |
| A-N1 | Some owners reshape short stays into nominal 30-night contracts, or claim primary residence on documents they can obtain. | substitutability | 0.6 | NEW. K1 defines the ban by contract length and residence; K3's proofs (driver's license, voter registration) can be changed at low cost; K4 enforces only on complaint. | C-12 fails. |
| A-N2 | Some owners of non-primary units sell rather than lease, let mid-term or hold. | alternative_uses | 0.7 | NEW. A-16's evidence names listings for sale; investor share of purchases (A-21); the fall in yield (A-1). | C-13 fails; C-61 loses part of its (−) chain. |
| A-N3 | Residents of units moved to 12-month leases buy some meals and goods near home. | other | 0.8 | NEW. Residents shop locally; card-spending data by district (A-12) covers residents too. | C-52 loses its (+) chain and becomes decrease. |
| A-N4 | Some owners sell, or stop letting short, before 1 July 2027. | other | 0.4 | NEW. A buyer can still let until 1 July, so a sale need not end lets; leasing season is August–September. | Below cut-off: not used. |

**Not reported** (an assumption below 0.5):
- Rivals file complaints against lawful hosts, raising lawful hosts' expected fines and lowering their nights (CR-4, x: let, y: stop; CR-8c on the complaints): needs A-28 (p 0.3).
- Fewer whole-unit nights in the announcement window, from owners who sell or stop letting before 1 July (CR-10a, CR-4): needs A-N4 (p 0.4). This is the opposing chain to C-32 under CR-12 (0.8, kind 2); C-32 keeps its derived sign.

### Final check before the report

1. *Uncombined chains.* Every key with chains of opposite sign is in section 7. Hotel price in the long run uses a CR-12e response argument; all others with opposing chains are ambiguous. Whole-unit nights in the July–September window: early booking (C-34) moves the booking date, not the stay, so it cannot raise nights in the window above the counterfactual; decrease (C-33) stands.
2. *Single signs for a group.* The general-fund payers (C-59) are a group sign. The CR-6 margins for guests are recorded as `full_cost_per_unit` (C-21) with each priced substitute signed separately (C-17, C-41, C-47, C-48), not as one unlicensed margin.
3. *Baseline.* All signs are against Saltmere without the ordinance, with R1 to R3 in force.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for fines paid (C-57) and the appropriation (C-59). Owners' loss is recorded as `return_on_capital` and `asset_value`, not as spending power.
5. *Timing shifts.* Trips and bookings moved before 1 July are signed per window (C-32 to C-35).
6. *Both sides of every transfer.* Checked in section 9.
7. *Every class, every rule.* CR-4 was applied to each owner class for each pair (lease, mid-term, sale, vacancy, evasion, reclassification, lobbying, timing); CR-6 to hotels, mid-term lets, rooms, Elsdon, long-term rentals and Code Enforcement's fixed staff; CR-7c to STR units, two-unit buildings, rental buildings, hotels, Elsdon homes and owner-occupied homes; CR-9 along substitute, same-segment, across-border, complement (location), input_to, shared_facility and proximity relations. No `contract`, `currency` or `gift` relation carries a chain here beyond the cancelled bookings (C-27), which are contracts voided by K1.
8. *Unstated premises.* A-N1 to A-N4 added.

## 11. Report

**The policy:** From 1 July 2027, no whole dwelling in Saltmere may be let for under 30 nights unless it is the owner's registered primary residence, and then for at most 90 nights a year. Platforms must show a registration number on every whole-unit listing and remove listings on notice; hosts are fined only after a complaint. Bookings for stays after 30 September 2027 are cancelled. Owners pay $250 a year to register; a new Registry Unit costs $520,000 a year from the general fund. Whether the second unit of an owner-occupied two-unit building counts as the owner's residence is unclear (U1).

**Visible consequences:** Fewer whole-unit short lets in Saltmere (C-1, C-2); owners of non-primary units earn less on them (C-3); primary-residence hosts pay to register and lose nights above 90 (C-5, C-6). Some units move to 12-month leases (C-7), so long-term rents are lower and more leases are signed than without the ordinance (C-37, C-38).

**Invisible consequences:**
- *Owners:* STR units lose value from the day the bill was introduced (C-4). Owners also let mid-term (C-8), leave second homes empty (C-9), sell (C-13), let off-platform in breach where complaints are unlikely (C-10), screen guests (C-26), reshape contracts or claim residence (C-12), and lobby (C-29). Fined owners have less to spend (C-57).
- *Guests:* They pay more in full for lodging (C-21), travel further from Elsdon (C-24), take fewer trips (C-22), know less about off-platform lets (C-25), and lose and rebook stays already booked (C-27, C-28). Before the ban, trips and bookings are moved earlier (C-32, C-34); in the transition window, nights and new bookings fall (C-33, C-35).
- *Other lodging:* Hotel prices, nights and values rise (C-41 to C-43), and hotels build more in the long run (C-44); guests who would have used hotels anyway get fewer nights (C-45). Room hosts and primary-residence hosts charge more (C-17), room hosts let more (C-18) and new hosts enter (C-20). More mid-term lets are traded (C-46).
- *Housing:* Long-term landlords receive lower rents and their buildings lose value (C-39, C-40). Investors buy fewer beach-district homes (C-14).
- *Elsdon:* Higher STR prices and home values (C-48, C-49), more visitor spending (C-53), and higher long-term rents for its tenants (C-50).
- *Others:* Beach-district businesses sell less to visitors (C-51); cleaning and management firms employ fewer people in STR work (C-54); platforms bear compliance costs (C-31); the general fund receives fines (C-56) and pays for the Registry (C-58), at the expense of taxpayers or other spending (C-59); hotels and neighborhood groups lobby to keep the ban (C-30).

**Ambiguous effects:** Total nights let by primary-residence hosts (C-19) and, under U1-a, by two-unit owners (C-15, C-16): the 90-night cap pushes down, higher nightly prices push up. Mid-term rents (C-47): more supply against more demand. Total sales of beach-district businesses (C-52): fewer visitors against more residents. TOT revenue (C-55): fewer STR nights against more and dearer hotel nights. Waiting for other Code Enforcement complaints (C-60): new complaints about unlawful lets against fewer nuisance complaints. Beach-district home prices and owner-occupiers' home values (C-61, C-62, Tier C): fewer investor bids against buyers who value fewer transient neighbors.

**Key conditions:** Platforms comply (A-2, 0.85), which is what makes the ban bind; short lets yield more than leases (A-1, 0.9); most units can be leased (A-5, 0.85) and are not offset (A-13, 0.75), which decide the rent effect; hotels are a substitute (A-8, 0.8) with fixed rooms (A-9, 0.85); complaints are unlikely for some units (A-3, 0.75), which decides evasion. Four premises were added: reshaping contracts or residence claims (A-N1, 0.6), sales (A-N2, 0.7), residents buying locally (A-N3, 0.8), and early sales before 1 July (A-N4, 0.4, not used).

**What this analysis cannot say:** How many units move to each use, how far rents fall, whether TOT revenue rises or falls, or whether the gains to tenants, hotels and neighbors outweigh the losses to owners, guests, platforms and visitor businesses. Nuisance, noise, safety and neighborhood character are out of scope (no variable); the proximity chain enters only through home prices, at Tier C. It does not say whether the policy is good.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | owners.non_primary_units | quantity_supplied (whole-unit STR nights, legal market) | decrease | short; medium; long | visible | B | CR-1 (op 1: K1 removes the option where platforms enforce K2); CR-2; CR-4a (no owner moves toward the removed option) | A-2 |
| C-2 | guests.whole_unit, platforms | quantity_traded (whole-unit STR nights booked on platforms, Saltmere) | decrease | short; medium; long | visible | B | CR-1 (op 1); CR-5a (exchanges that would have taken place are prevented; both parties and the intermediary lose the expected gain) | A-2 |
| C-3 | owners.non_primary_units | return_on_capital (units formerly let short) | decrease | short; medium; long | visible | B | CR-3a (chosen option removed; next-best yields about $20,000 against $30,000, A-1); CR-4b; CR-5a (lost receipts combined with saved outlays by A-1's net figures) | A-1, A-2 |
| C-4 | owners.non_primary_units | asset_value (units used as whole-unit STR) | decrease | short (from 3 November 2026) | invisible | B | CR-10c (value reflects expected yields); CR-7c (borne by whoever owns the unit as the ban becomes expected, part of the way from introduction as passage became likely, A-30) | A-1, A-30 |
| C-5 | owners.primary_residence_hosts | compliance_cost (K3 fee and proof of residence) | increase | short; medium; long | visible | B | CR-1 (op 3: $250 and proof attached to the exempt use, replacing R1's $150, which about a third did not pay); CR-8c; platforms require the number (A-2) | A-2 |
| C-6 | owners.primary_residence_hosts (above 90 nights) | quantity_supplied (STR nights above 90 a year) | decrease | short; medium; long | visible | B | CR-1 (op 1 on nights above 90); CR-4a (no host moves toward more nights because of the cap; evasion, C-11, limits the fall but cannot reverse it, CR-12e) | A-2 |
| C-7 | owners.non_primary_units | quantity_supplied (12-month leases) | increase | medium; long | visible | B | CR-4 (x: short let, now removed; y: 12-month lease, next-best for some, A-5); CR-7a (the unit moves to the use that now yields most) | A-5, A-2 |
| C-8 | owners.non_primary_units | quantity_supplied (furnished lets of 30 nights or more) | increase | short; medium; long | invisible | B | CR-4 (x: short let, y: mid-term let, exempt by length) | A-7, A-2 |
| C-9 | owners.second_homes | units_held_vacant | increase | short; medium; long | invisible | B | CR-4 (x: let short between own weeks, removed; y: keep for own weeks and leave empty, since a lease would block own use, A-6) | A-6, A-2 |
| C-10 | owners.non_primary_units (in breach) | informal_activity (whole-unit short lets booked directly, off-platform) | increase | short; medium; long | invisible | B | CR-4 (x: comply, y: violate; enforcement off-platform only by complaint, so expected fine below gain for some units, A-3); CR-6 (displaced guests' pressure seeks the margin outside the rule, A-4) | A-3, A-4 |
| C-11 | owners.primary_residence_hosts, owners.two_unit | legal_breach (nights above 90 spread over several platforms) | increase | short; medium; long | invisible | B | CR-4 (x: comply with the cap, y: exceed it on several platforms; per-platform reports do not reveal it, A-22) | A-22 |
| C-12 | owners.non_primary_units | reclassification (nominal 30-night contracts for shorter stays; claims of primary residence) | increase | short; medium; long | invisible | B | CR-4 (x: the covered form, y: a form outside K1's definitions; y made relatively better; A-N1: some have it open) | A-N1 |
| C-13 | owners.non_primary_units | quantity_supplied (homes offered for sale, beach districts) | increase | short; medium | invisible | B | CR-4 (x: hold, y: sell; holding yields less, C-3) | A-N2 |
| C-14 | investors.home_buyers | quantity_demanded (homes in the beach districts) | decrease | short; medium; long | invisible | B | CR-1 (op 1 on the STR use of any home bought); CR-4 (x: buy here, y: invest elsewhere); CR-7c | A-21, A-1 |
| C-15 | owners.two_unit | quantity_supplied (whole-unit STR nights in two-unit buildings) | U1-a: ambiguous; U1-b: decrease | short; medium; long | invisible | B | U1-a: CR-12b over CR-1 op 1 on nights above 90 (−) and CR-9, CR-4c via higher nightly prices (+, A-32). U1-b: CR-1 op 1 on all short nights, CR-4a | A-2, A-32 |
| C-16 | owners.two_unit | asset_value (second units) | U1-a: ambiguous; U1-b: decrease | short (from 3 November 2026) | invisible | B | CR-10c, CR-7c (A-30). U1-a: CR-12b over lost nights above 90 (−, A-1) and higher nightly rate (+, A-32). U1-b: yield falls to the next-best use (A-1) | A-1, A-30, A-32 |
| C-17 | owners.room_hosts, owners.primary_residence_hosts, their guests | price_paid (room lets and primary-residence lets) | increase | short; medium; long | invisible | B | CR-9 (substitute: displaced whole-unit guests bid for rooms and primary-residence lets, A-32); CR-6 (with more buyers at each price, and primary-residence nights capped, the price rises) | A-32, A-2 |
| C-18 | owners.room_hosts | quantity_supplied (room-nights) | increase | short; medium; long | invisible | B | CR-9 (substitute); CR-4c (at a higher price, rooms not let before are let) | A-32, A-2 |
| C-19 | owners.primary_residence_hosts | quantity_supplied (STR nights, all hosts) | ambiguous | short; medium; long | invisible | B | CR-12b: (−) CR-1 op 1 on nights above 90 and CR-4 (0.8: fixed cost per outlet, K3 fee); (+) CR-9, CR-4c via higher prices (A-32). No dominance premise | A-2, A-32 |
| C-20 | sellers.prospective (room and primary-residence lets) | entry_rate | increase | medium | invisible | B | CR-4 (x: stay out, y: enter; y made better by higher prices, C-17); CR-7a | A-32, A-2 |
| C-21 | guests.whole_unit | full_cost_per_unit (lodging for a Saltmere stay) | increase | short; medium; long | invisible | B | CR-3a (their chosen option is removed, so they fall back to a lower-ranked one); CR-6 and CR-9 (the substitutes they turn to rise in price, C-17, C-41) | A-2, A-8 |
| C-22 | guests.whole_unit | quantity_demanded (trips to Saltmere) | decrease | short; medium; long | invisible | B | CR-4 (x: a trip with the next-best lodging, y: no trip or another place; for groups with no close substitute y now ranks higher, A-11) | A-11, A-2 |
| C-23 | guests.whole_unit | cross_border_purchases (lodging in Elsdon) | increase | short; medium; long | invisible | B | CR-4 (x: here, y: there; Elsdon has no restriction, A-10) | A-10, A-2 |
| C-24 | guests.whole_unit | travel_time | increase | short; medium; long | invisible | B | CR-4 (guests who stay in Elsdon travel 12 km to the beach districts); CR-3a | A-10, A-2 |
| C-25 | guests.whole_unit (off-platform) | quality_information | decrease | short; medium; long | invisible | B | CR-11b (exchanges moved outside the legal market lose reviews, platform guarantees and recourse) | A-3, A-4 |
| C-26 | owners.non_primary_units (in breach) | allocation_by_non_price_criteria (guest screening) | increase | short; medium; long | invisible | B | CR-4 (x: accept any guest, y: screen; a complaint brings a fine, A-19, and screening lowers its chance, A-27); CR-6 (the scarce side chooses among buyers by criteria, not only price) | A-3, A-4, A-19, A-27 |
| C-27 | guests.booked_after_30_Sep_2027 | quantity_traded (stays booked before 3 November 2026) | decrease | short | invisible | B | CR-1 (op 1: K1 voids bookings for later dates); CR-5a (both parties lose the gain each expected; the refund returns the price, CR-8b) | A-24, A-2 |
| C-28 | guests.booked_after_30_Sep_2027 | search_cost | increase | short | invisible | B | CR-3a; CR-8c (time spent rebooking is used up) | A-24, A-2 |
| C-29 | owners.non_primary_units, platforms | lobbying_effort (to repeal or relax K1) | increase | short; medium; long | invisible | B | CR-4 (x: accept, y: lobby; their loss, C-3, makes y gain); CR-8c | A-14, A-1 |
| C-30 | hotels, neighbors (associations) | lobbying_effort (to keep or tighten K1) | increase | short; medium; long | invisible | B | CR-4 (x: accept a relaxation, y: lobby to keep the ban; hotels gain from it, C-41); CR-8c | A-14, A-8 |
| C-31 | platforms | compliance_cost (numbers, removals, quarterly reports) | increase | short; medium; long | invisible | B | CR-1 (op 3: K2 duties); CR-4 (x: comply, y: pay $1,000 per listing per day; A-2: they comply); CR-8c | A-2 |
| C-32 | guests.whole_unit | quantity_traded (whole-unit STR nights, 3 Nov 2026 to 30 Jun 2027) | increase | short (announcement window) | invisible | B | CR-10a (a change expected in future alters choices now); CR-4 (x: a trip after 1 July without a whole unit, y: the trip before 1 July with one; A-17). Opposing chain via early sales needs A-N4 (p 0.4): derived sign kept (CR-12, 0.8 kind 2) | A-17 |
| C-33 | guests.whole_unit | quantity_traded (whole-unit STR nights, 1 Jul to 30 Sep 2027) | decrease | short (transition window) | invisible | B | CR-1 (op 1: only stays booked before 1 July may be completed); CR-10a; early booking (C-34) moves the booking date, not the stay, so it cannot raise nights above the counterfactual (CR-12e); also A-16 (owners end summer lets), an independent chain (CR-12d) | A-2 |
| C-34 | guests.whole_unit | quantity_traded (bookings made 3 Nov 2026 to 30 Jun 2027 for stays 1 Jul to 30 Sep 2027) | increase | short (announcement window) | invisible | B | CR-10a; CR-4 (x: book after 1 July, now void, y: book before; A-15) | A-15 |
| C-35 | guests.whole_unit | quantity_traded (bookings made 1 Jul to 30 Sep 2027 for stays in that window) | decrease | short (transition window) | invisible | B | CR-1 (op 1: bookings made after 1 July for non-primary units are unlawful); CR-10a (some that would have been made then were made earlier, A-15) | A-2, A-15 |
| C-36 | owners.non_primary_units | quantity_supplied (12-month leases starting August–September 2027) | increase | short (transition) | invisible | B | CR-10a; CR-4 (x: complete summer lets, y: free the unit for the August–September leasing season or a sale, A-16); A-5 for the lease | A-16, A-5 |
| C-37 | tenants.long_term | price_paid (long-term rent, Saltmere) | decrease | medium; long | visible | B | CR-9 (same_market_other_segment: former STR units enter the long-term market, C-7); CR-6 (with more units offered at each rent, the rent moves to a lower clearing level; A-13: not offset) | A-5, A-13, A-2 |
| C-38 | tenants.long_term | quantity_traded (long-term leases, Saltmere) | increase | medium; long | visible | B | CR-9; CR-5 (leases agreed that would not have been); CR-6 | A-5, A-13, A-2 |
| C-39 | landlords.long_term | net_price_received (long-term rent) | decrease | medium; long | invisible | B | CR-9 (those who compete for the same customers face a changed situation); CR-6; CR-7a | A-5, A-13, A-2 |
| C-40 | landlords.long_term | asset_value (rental buildings) | decrease | short (from 3 November 2026) | invisible | B | CR-10c, CR-7c (the expected fall in rents, C-39, is borne by owners when it becomes expected, A-30) | A-5, A-13, A-30 |
| C-41 | hotels, buyers.substitutes | price_paid (hotel rooms) | increase | short; medium; long | invisible | B | CR-9 (substitute, A-8); CR-6 (more buyers for a fixed stock of rooms, A-9 short and medium); long: CR-12e (new rooms, C-44, are drawn by the higher yield and cannot push the price below the counterfactual) | A-8, A-2 |
| C-42 | hotels | quantity_traded (hotel room-nights) | increase | short; medium; long | invisible | B | CR-9 (substitute); CR-5 (stays that would not have taken place); off-peak rooms are free, peak rooms near capacity (A-9 limits but does not reverse) | A-8, A-2 |
| C-43 | hotels | asset_value (hotels) | increase | short (from 3 November 2026) | invisible | B | CR-10c, CR-7c (higher expected yields, C-41, captured by owners when the ban becomes expected; capacity fixed, A-9) | A-8, A-9, A-30 |
| C-44 | hotels | investment_target (hotel rooms) | increase | long | invisible | B | CR-4 (x: stay out, y: build; y made better by C-41); CR-7a; sites available (A-25) | A-8, A-25 |
| C-45 | buyers.substitutes (guests who would stay in hotels anyway) | quantity_traded (their hotel room-nights) | decrease | short; medium | invisible | B | CR-4c (at a higher price their last nights, valued least, are given up); CR-6 (shared fixed stock of rooms, A-9) | A-8, A-9, A-2 |
| C-46 | sellers.substitutes (mid-term lets) | quantity_traded (furnished lets of 30 nights or more) | increase | short; medium; long | invisible | B | CR-12d, two independent chains with the same sign: CR-4 for owners (x: short let, y: mid-term let, A-7) and CR-4 for guests (x: shorter stay, y: extend to 30 nights, A-31); CR-5 | A-7 or A-31 (independent chains) |
| C-47 | sellers.substitutes (mid-term lets) | price_paid (furnished lets of 30 nights or more) | ambiguous | short; medium; long | invisible | B | CR-12b: (−) CR-6 with more units offered (A-7); (+) CR-6 with more guests extending to 30 nights (A-31). No dominance premise | A-7, A-31 |
| C-48 | neighboring_jurisdictions (Elsdon hosts) | net_price_received (Elsdon STR nights) | increase | short; medium; long | invisible | B | CR-9 (across_border, A-10); CR-6 | A-10, A-2 |
| C-49 | neighboring_jurisdictions (Elsdon owners) | asset_value (homes suitable for STR, Elsdon) | increase | short (from 3 November 2026) | invisible | B | CR-10c, CR-7c (higher expected STR yields, C-48, A-30) | A-10, A-30 |
| C-50 | neighboring_jurisdictions (Elsdon tenants) | price_paid (long-term rent, Elsdon) | increase | medium; long | invisible | B | CR-7a (Elsdon owners move units to the higher-yielding STR use, A-29); CR-9 (same_market_other_segment); CR-6 (fewer long-term units at each rent) | A-10, A-29 |
| C-51 | sellers.complements (beach districts) | quantity_complement (visitors' purchases near lodging) | decrease | short; medium; long | invisible | B | CR-9 (complement, location: visitors buy near lodging, A-12); LW-10; fewer visitor nights in Saltmere by either of two independent chains (CR-12d): guests move to Elsdon (A-10) or skip trips (A-11); no derived chain adds visitor nights in Saltmere | A-12, A-2, and A-10 or A-11 |
| C-52 | sellers.complements (beach districts) | quantity_complement (all purchases near lodging, visitors and residents) | ambiguous | medium; long | invisible | B | CR-12b and CR-12 (0.8, two items in one variable): (−) C-51; (+) CR-9 (complement, location: residents of units moved to 12-month leases buy near home, A-N3, A-5). No dominance premise | A-12, A-N3, A-5 |
| C-53 | neighboring_jurisdictions (Elsdon businesses) | quantity_complement (visitors' purchases) | increase | short; medium; long | invisible | B | CR-9 (complement, location; across_border); LW-10 | A-10, A-12 |
| C-54 | input_suppliers (cleaning and management firms) | employment (STR cleaning and management) | decrease | short; medium; long | invisible | B | CR-9 (input_to: fewer nights serviced, C-1); LW-10 (demand for an input follows demand for what it produces); CR-7a (labor moves to other uses, A-26) | A-26, A-2 |
| C-55 | city.general_fund | tax_revenue (TOT) | ambiguous | short; medium; long | visible | B | CR-12b: (−) CR-8b on fewer STR nights (C-2) and untaxed off-platform lets (C-10); (+) CR-8b on more and dearer hotel nights (C-41, C-42), limited by peak capacity (A-9). No dominance premise | A-2, A-8, A-9 |
| C-56 | city.general_fund | non_tax_receipts (K4 fines) | increase | short; medium; long | invisible | B | CR-8b (fines paid are received by the general fund; complaints lead to fines, A-19, on lets in breach, A-3) | A-19, A-3 |
| C-57 | owners.non_primary_units (in breach, fined) | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-8b (the other side of C-56); CR-3 note (a sum paid that the fined owner cannot avoid once fined) | A-19, A-3 |
| C-58 | officials.registry | enforcement_cost | increase | short; medium; long | visible | A | CR-1 (op 4: $520,000 a year to the Registry Unit); CR-8c (resources spent administering are used up) | none |
| C-59 | taxpayers or recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | B | CR-8a, CR-8b (0.7: payers from the general budget are a group; the money is new, A-20) | A-20 |
| C-60 | residents filing other complaints with Code Enforcement | wait_time (handling of other complaints) | ambiguous | short; medium; long | invisible | B | CR-6 (0.7 public supply: fixed staff, so added work is rationed by waiting); CR-12b: (+) K4 complaints about unlawful lets (A-19); (−) fewer nuisance complaints as fewer STR units operate (A-18, C-1). No dominance premise | A-19, A-18 |
| C-61 | buyers.prospective (owner-occupiers) | price_paid (homes, beach districts) | ambiguous | short; medium; long | invisible | C | CR-12b: (−) CR-9 and CR-6 (fewer investor bids, A-21; more homes offered, A-N2); (+) CR-9 (proximity: some buyers value fewer transient neighbors, A-23), Tier C under CR-9 (0.7). CR-12 (0.8 kind 2): derived chain with p at least 0.5, so ambiguous | A-21, A-N2, A-23 |
| C-62 | neighbors (owner-occupiers, beach districts) | asset_value (owner-occupied homes) | ambiguous | short; medium; long | invisible | C | CR-7c, CR-10c; CR-12b over the same two chains as C-61 (A-21; A-23, Tier C) | A-21, A-23, A-30 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-044-C1: Nuisance itself. The chain from fewer operating STR units to less noise for neighbors is derivable as a `proximity` relation (CR-9, 0.7), but it has no variable, so it can be recorded only through home prices (C-61, C-62) at Tier C. The rules cover the step; the vocabulary does not (see (c)). No other step lacked a core rule.

**(b) Core-rule wording that was hard to apply.**
- CR-12e, response argument for timing: whether early booking (C-34) can raise nights in the July–September window (C-33) needed the argument that a booking shift moves the booking date, not the stay. CR-12e is worded for responses to a price, not for timing shifts within a transition window.
- CR-3 note on lost receipts: owners lose receipts but save cleaning and management outlays. The note says to combine them under CR-12b; A-1's net figures settle the sign of `return_on_capital`, but the note does not say whether an owner whose net yield falls should also be signed on `resources_available_other_uses`. Not signed here (final check 4).
- CR-9 (0.7) with CR-12d: a combined consequence with one Tier C chain (proximity) takes Tier C, though its ambiguity comes from both chains. Whether the Tier C chain should be able to make a Tier B chain ambiguous at all is not stated.
- CR-7c with an undecided reading (U1): an asset's value moves toward a weighted mix of the readings' values while the Registry decides. Readings get no probability, so the price path cannot be signed; only each reading's end state is.
- CR-6 with enforcement by complaint: the expected fine depends on neighbors' choice to complain, which is itself a CR-4 choice by a third party. CR-4 covers it, but the rules do not say how to record a penalty whose probability is set by another actor class.

**(c) Vocabulary missing from the ontology.**
- No variable for nuisance or complaints filed (noise, disturbance), even as a count, so the proximity relation cannot be signed directly.
- No variable that separates the date an exchange is agreed from the date it is performed (a booking versus a stay); `quantity_traded` with a window qualifier was used.
- No standard actor class for intermediaries' platforms as a role distinct from `intermediaries`, or for visitors and guests (used `guests.whole_unit`).
- No variable for registrations or registered sellers in a non-licensing registry (only `share_of_sellers_licensed`).
- No variable for visitor numbers or trips; `quantity_demanded (trips)` was used.
