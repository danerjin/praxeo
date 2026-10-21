# WE-050 / Analysis: Ban on sales of new combustion-engine cars from 2035

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Vessmark Clean Cars Act.** Vessmark is a country of about 9 million people with about 4.8 million registered passenger cars, of average age 10 years, scrapped at about 17 years (about 260,000 a year). It has no car assembly: every new car is imported by about 12 brand importers and sold through about 600 dealers; Vessmark buys about 0.4% of the world's new cars. In 2025 about 280,000 new cars were sold: 196,000 combustion-only (70%), 28,000 plug-in hybrids (PHEVs, 10%) and 56,000 battery-electric cars (BEVs, 20%). A new combustion compact costs about $30,000 and a comparable BEV about $36,000 (gap forecast at about $2,000 by 2035). About 650,000 used cars change hands a year; about 25,000 are imported used from Drevland (no ban, about 3.5 million used sales a year) at import parity: Vessmark's used prices sit about $1,800 above Drevland's (transport, a $900 state import inspection, registration). Inspection capacity is about 40,000 cars a year. Vessmark has about 2,100 fuel stations, 9,000 public chargers, about 3,500 independent repair shops with about 14,000 mechanics. Fuel excise ($0.70 a liter, about $600 a year per combustion car) raises about $2.6 billion a year for the general budget.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Vessmark. Drevland, the larger neighbor to the south, has no ban and no announced date; residents may drive a foreign-registered car for at most six months. | "Drevland ... which has no ban and no announced date"; existing rules. |
| Announced / enacted / effective / expires | Introduced 3 March 2026; passed 18 June 2026; enacted 30 June 2026; K1 effective 1 January 2035; K2 PHEV ban 1 January 2038; K5 from 1 January 2035; no expiry. The Minister reports on charging readiness by 30 June 2031 and may postpone the dates in s. 3 and s. 4 by up to three years. | Policy record; s. 9. |
| Enforcement (who, penalties, resources) | Vehicle Registry refuses registration; selling an unregistrable new car as new is an offence (fine $5,000). The Registry's budget is fixed by law; no new funds. | s. 7. |
| Existing rules (both paths) | Fuel excise; import roadworthiness inspection at state test centers; six-month limit on driving a foreign-registered car. | Policy record. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 End of sale (s. 3) | `product_standard` (a new passenger car must have no combustion engine) | First registration of new passenger cars | Vehicle Registry; importers and dealers | From 1 January 2035 the Registry shall not register for the first time a new passenger car fitted with an internal combustion engine; "new" means not previously registered (s. 2). | PHEVs, under K2 |
| K2 Plug-in hybrids (s. 4) | Dated exemption from K1 | New PHEVs with at least 50 km electric range | as K1 | Exempt until 31 December 2037; banned from 1 January 2038. | — |
| K3 Existing cars (s. 5) | Saving clause | Cars registered before the dates | — | Use, sale, transfer and re-registration unaffected. | — |
| K4 Enforcement (s. 7) | Enforcement | K1, K2 | Vehicle Registry | Registration refused; $5,000 fine; fixed budget. | — |
| K5 Road charge (s. 8) | `lump_sum_tax` per car per year (operation 3 on owning a BEV) | Battery-electric passenger cars | Owners of BEVs | $250 a year from 1 January 2035, collected with registration renewal; to the general budget. | PHEVs |

Unclear provisions:
- **U1, "not previously been registered" (s. 2).** U1-a: previously registered in Vessmark, so used combustion cars imported from abroad can no longer be registered after 2035. U1-b: previously registered anywhere, so used combustion cars from Drevland, and new ones first registered in Drevland, can still be imported and registered. No probability is given; signs that depend on it are reported per reading.

**Counterfactual.** Vessmark without the Act: no end-of-sale date, no road charge, the BEV share rising on the forecast trend (about 110,000 new combustion cars plus about 25,000 PHEVs in 2035; about 40,000 combustion in 2045). Counterfactual law: every new car may be registered; BEVs pay no road charge. **Horizons used:** short = 2026 to 2034 (from introduction to the effective date); medium = 2035 to 2040; long = after 2040. Timing consequences name their window in the variable.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations (dated) | Core rules applied |
|---|---|---|---|---|
| K1 End of sale | triangular (prohibits the exchange of a new combustion car between importer or dealer and buyer) | Yes from 2035: about 110,000 counterfactual buyers a year (A-1), enforced through registration (A-2), dates not postponed (A-3) | 1 for buyers, dealers and importers, from 1 January 2035 (option of registering or selling a new combustion car removed). Before the date it acts through expectations (CR-1 0.7 note, CR-10a) and asset values (CR-7c). Under U1-a, op 1 also for buyers of used combustion cars imported from abroad; under U1-b, no operation on them | CR-4, CR-5a, CR-6, CR-7c, CR-9, CR-10a, CR-10c |
| K2 PHEV date | triangular | Yes from 2038 (about 25,000 PHEVs a year, A-1) | Against the no-Act counterfactual: no operation until 2037; op 1 from 1 January 2038 | CR-4, CR-5a, CR-10a |
| K3 Saving clause | none against the counterfactual | — | No operation against the counterfactual law (all cars may be used and resold on both paths). It limits K1's reach and is what makes pre-registration (A-9) and the scarcity value of existing cars possible | CR-7c (through K1) |
| K4 Enforcement | triangular (penalty) and binary (Registry resources) | Yes (A-2); budget fixed (A-28) | 3 for dealers (risk of a $5,000 fine attached to selling an unregistrable new car as new); added tasks for the Registry with no added means | CR-4 (x: comply, y: violate), CR-8a, CR-8c, CR-6 (public supply) |
| K5 Road charge | binary (state takes) | Yes from 2035 (A-2) | 3 for prospective BEV buyers (a charge attached to the option of owning a BEV); for existing BEV owners, a sum they cannot avoid while they keep the car (op 3 on keeping it, unavoidable in effect) | CR-3, CR-4, CR-7c, CR-8b, CR-10c |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1, CR-9) |
|---|---|---|
| buyers.new_combustion | Would-be buyers of new combustion cars (about 110,000 a year in 2035) | Op 1 from 2035; before 2035, buying a combustion car now gains (CR-10a, CR-7c). Split: those who move to a new BEV, a PHEV, a used car, or keep their car (A-4, A-22, A-25, A-27). |
| buyers.new_phev | Would-be buyers of new PHEVs (about 25,000 a year) | Op 1 from 2038; gain displaced combustion buyers as rivals in 2035 to 2037. |
| buyers.new_bev | Buyers of new BEVs | K5 (op 3) from 2035; K5 expected from 2026 (CR-10a). |
| owners.bev | Owners of BEVs | K5: $250 a year from 2035, unavoidable while they keep the car. |
| owners.combustion | Owners of combustion cars registered before the dates (K3) | No operation; their cars' value changes through the used market (CR-9, CR-7c). |
| buyers.used_cars | Buyers of used cars in Vessmark | Through CR-9 (substitute): displaced new-car buyers compete for used cars. |
| importers.brand | About 12 importers of new cars | Op 1 on selling new combustion cars from 2035 (PHEVs from 2038); model decisions before (A-8). |
| dealers | About 600 dealers | Op 1 as above; op 3 (K4 fine); stock decisions before 2035 (A-9). |
| importers.used | Importers of used cars from Drevland and the buyers who use them | U1-a: op 1 on registering imported combustion cars from 2035; U1-b: no operation, and more demand (A-20). |
| sellers.foreign | Drevland used-car sellers; foreign makers selling to Vessmark | Through CR-9 (across_border, input_to). |
| officials.registry | Vehicle Registry | Added tasks (checks, refusals, road-charge collection) with a fixed budget (A-28). |
| users.registry_services | Everyone else who uses the Registry and the state test centers | Through CR-9 (shared_facility of a fixed public supply): compete for the same staff and inspection slots. |
| fuel_retailers | About 2,100 stations | Through CR-9 (complement): fewer combustion vehicle-km after 2035 (A-16). |
| workers.fuel_stations | Station staff | Through CR-9 (input_to fuel retailing). |
| repair_shops | About 3,500 independent shops and 14,000 mechanics | Through CR-9 (complement): more old cars kept running (medium), fewer combustion cars (long). |
| charging_firms | Sellers of public charging | Through CR-9 (complement): more BEVs (A-24). |
| taxpayers, recipients_of_other_spending | Those who make up or receive general-budget money | Through CR-8b: fuel excise falls (A-16); road charge collected (K5). |
| lobby_groups | Dealers, fuel retailers, motoring clubs; BEV importers and charging firms | CR-4 (x: accept, y: lobby) on the 2031 review (A-15). |
| exporters.vessmark | Vessmark's exporters | Through CR-9 (currency): payments for car imports change. |

## 4. Direct effect

CR-1 and CR-2: what K1, K2 and K5 change first, for those whose options they alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | buyers.new_combustion, importers.brand, dealers | quantity_traded (new combustion cars, excluding PHEVs, registered from 2035) | decrease | medium; long | CR-1 op 1, CR-5a | A-1, A-2, A-3 |
| C-2 | buyers.new_phev, importers.brand, dealers | quantity_traded (new PHEVs, from 2038) | decrease | medium; long | CR-1 op 1, CR-5a | A-1, A-2, A-3 |
| C-3 | taxpayers, recipients_of_other_spending | tax_revenue (road charge) | increase | medium; long | CR-1 op 3/4, CR-8b, CR-12 0.9 (activity exists only under the policy) | A-2 |
| C-4 | owners.bev | resources_available_other_uses | decrease | medium; long | CR-8b, CR-3 note (a sum they cannot avoid while they keep the car), CR-3c | A-2 |

## 5. Responses

CR-4 for every pair of options each actor class has; CR-5 for prevented exchanges; CR-10a for timing; CR-7c and CR-10c for durable assets.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | buyers.new_combustion | quantity_demanded (new BEVs) | increase | medium; long | CR-4 (x: new combustion, removed; y: new BEV), CR-12b and CR-12e with A-22 against K5 | A-1, A-2, A-3, A-22 |
| C-6 | buyers.new_bev | price_paid (new BEVs, before the road charge) | no_change | medium; long | CR-6 0.9 (splitting a shift: supply expands at unchanged cost), CR-7a | A-5 |
| C-7 | buyers.new_combustion (those who move to new BEVs) | price_paid (new car bought) | increase | medium | CR-4, CR-3a, arithmetic on A-23 | A-1, A-3, A-22, A-23 |
| C-8 | buyers.new_phev | quantity_traded (new PHEVs, 2035 to 2037) | increase | medium | CR-4 (x: new combustion, removed; y: PHEV), CR-10a | A-25, A-2, A-3 |
| C-9 | buyers.used_cars | quantity_demanded (used combustion cars) | increase | medium | CR-4 (x: new combustion, removed; y: used car or keep present car), CR-9 (substitute) | A-4, A-2, A-3 |
| C-10 | buyers.used_cars | price_paid (used combustion cars) | increase | medium | CR-6, CR-12e response argument with partial import response (case figures, A-12), CR-12b with A-11 against thinning | A-4, A-11, A-12, A-2, A-3 |
| C-11 | owners.combustion (cars registered at enactment) | asset_value (cars) | increase | short (from introduction, March 2026) | CR-7c, CR-10c, CR-10a | A-4, A-11, A-1, A-3 |
| C-12 | owners.combustion (cars still in the fleet after 2040) | asset_value (cars) | ambiguous | long | CR-12b: (+) CR-6 scarcity; (−) CR-9 thinning of fuel and repair (A-10) | A-4, A-10 |
| C-13 | owners.combustion | maintenance_spending (repairs to keep cars running) | increase | medium | CR-4 (x: scrap, y: repair; y made better by the higher value), CR-10b | A-19, A-11, A-4 |
| C-14 | owners.combustion | quantity_traded (cars sold for scrap) | decrease | medium | CR-4, CR-10b | A-19, A-11, A-4 |
| C-15 | buyers.new_combustion | quantity_traded (new combustion cars, 2026 to 2030) | increase | short | CR-10a, CR-7c (a car bought before 2035 carries the scarcity value), CR-4 (K5 expected makes a BEV worse) | A-4, A-11, A-3, A-2 |
| C-16 | buyers.new_combustion | quantity_traded (new combustion cars, 2031 to 2032) | ambiguous | short | CR-12b: (+) as C-15; (−) CR-4 0.7 fixed cost per item offered, model withdrawal (A-8) | A-4, A-11, A-3, A-8 |
| C-17 | buyers.new_combustion | quantity_traded (new combustion cars, 2033 to 2034) | ambiguous | short | CR-12b: (+) CR-10a pull-forward (A-7) and C-15's chain; (−) A-8 withdrawal, A-29 waiting for pre-registered stock | A-7, A-8, A-29, A-3 |
| C-18 | buyers.new_bev | quantity_traded (new BEVs, 2026 to 2034) | ambiguous | short | CR-12b: (−) CR-10a, CR-7c (K5 expected lowers a BEV's value; a combustion car bought now gains); (+) CR-10a, CR-7c (displaced demand raises used-BEV values from 2035, A-27) | A-2, A-3, A-4, A-11, A-27 |
| C-19 | importers.brand, buyers.new_combustion | variety (combustion models offered, 2031 to 2034) | decrease | short | CR-4 0.7 (fixed cost per item offered: x: certify and market a model, y: drop it), CR-10a | A-8, A-3 |
| C-20 | dealers | reclassification (unsold new combustion stock registered before 1 January 2035) | increase | short (late 2034) | CR-4 (x: hold unregistrable stock, y: pre-register under K3), CR-12 0.9 (activity exists only under the policy) | A-9, A-2 |
| C-21 | buyers.pre_registered | price_paid (pre-registered combustion cars, 2035, against their counterfactual new price) | decrease | medium (2035) | CR-5c, CR-6 (stock that cannot be sold as new clears at a lower price) | A-9, A-29 |
| C-22 | dealers | net_price_received (pre-registered combustion stock, 2035) | decrease | medium (2035) | CR-5c, CR-6, CR-7b (stock that cannot move bears the loss) | A-9, A-29 |
| C-23 | importers.used | quantity_traded (used combustion cars imported from Drevland) | U1-a: decrease; U1-b: increase | medium | U1-a: CR-1 op 1, CR-5a; U1-b: CR-7a (import parity), CR-4 | A-2, A-20 |
| C-24 | importers.used | reclassification (new combustion cars first registered in Drevland and imported) | U1-a: no_change; U1-b: increase | medium | CR-4 (x: comply, y: register abroad first), CR-7a | A-21, A-2 |
| C-25 | lobby_groups (dealers, fuel retailers, motoring clubs) | lobbying_effort (for postponement at the 2031 review) | increase | short | CR-4 (x: accept, y: lobby), CR-8c | A-15 |
| C-26 | lobby_groups (BEV importers, charging firms) | lobbying_effort (against postponement) | increase | short | CR-4 (x: accept, y: lobby), CR-8c | A-15 |
| C-27 | officials.registry | enforcement_cost | increase | medium; long | CR-1 (K4), CR-8c | A-2 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Chains through Drevland's wider market stop at depth 3 (C-29); the currency chain stops at depth 3 with no sign (C-46). Rows also listed as opportunity costs appear in section 9.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-28 | users.registry_services | wait_time (+), quality_per_unit (−) (other Registry and inspection services) | at_least_one_as_stated | medium | CR-8a, CR-6 0.7 (public supply, fixed budget) | shared_facility: Registry staff and budget (fixed) | A-28, A-2 |
| C-29 | sellers.foreign (Drevland used-car market) | price_paid (used combustion cars in Drevland) | U1-a: decrease; U1-b: increase | medium | CR-9, CR-6 0.7 (wider market moves by as much as the quantity matters) | across_border: used combustion cars in Drevland and in Vessmark (partial) | A-20, A-2 |
| C-30 | importers.used | wait_time (state import inspection) | U1-a: decrease; U1-b: increase | medium | CR-6 0.7 (public supply at a set fee, fixed capacity) | input_to: inspection input_to registering an import (close) | A-20, A-12 |
| C-31 | fuel_retailers | quantity_traded (motor fuel) | decrease | medium; long | CR-9, LW-10, CR-12e with A-16 | complement: fuel and combustion cars (close) | A-16, A-1, A-3 |
| C-32 | taxpayers, recipients_of_other_spending | tax_revenue (fuel excise) | decrease | medium; long | CR-9, CR-8b, arithmetic ($0.70 per liter) | complement (as C-31) | A-16, A-1, A-3 |
| C-33 | taxpayers, recipients_of_other_spending | tax_revenue (fuel excise plus road charge) | ambiguous | medium; long | CR-12 0.8 (two items in one variable): C-3 (+), C-32 (−) | as C-3, C-32 | A-2, A-16 |
| C-34 | taxpayers, recipients_of_other_spending | resources_available_other_uses | ambiguous | medium; long | CR-8 0.7 (payers from the general budget), CR-12b | as C-33 | A-2, A-16 |
| C-35 | fuel_retailers | asset_value (stations) | decrease | short (from enactment) | CR-7c, CR-10c, CR-4 0.8 (fixed cost per outlet) | complement (as C-31) | A-16, A-1, A-3 |
| C-36 | fuel_retailers | number_of_sellers (stations) | decrease | long | CR-4 0.8 (fixed cost per outlet: x: operate, y: convert the site), CR-7a | complement (as C-31) | A-17, A-16, A-10 |
| C-37 | workers.fuel_stations | employment (fuel retailing) | decrease | medium; long | CR-9, LW-10 | input_to: station labor input_to fuel retailing | A-18, A-16 |
| C-38 | owners.combustion | travel_time (to fuel and repair) | increase | long | CR-9, CR-10b | complement; proximity of stations to drivers | A-10, A-17 |
| C-39 | repair_shops | quantity_traded (combustion repair) | increase | medium | CR-9, LW-10 | complement: repair and combustion cars in use (close) | A-26, A-19, A-4 |
| C-40 | repair_shops | quantity_traded (combustion repair) | decrease | long | CR-9, LW-10, CR-10b | complement (as C-39) | A-10 |
| C-41 | repair_shops (mechanics) | employment (combustion repair) | increase | medium | CR-9, LW-10 | input_to: mechanics' labor input_to repair | A-26, A-19, A-4 |
| C-42 | repair_shops (mechanics) | employment (combustion repair) | decrease | long | CR-9, LW-10 | input_to (as C-41) | A-10 |
| C-43 | repair_shops | asset_value (repair businesses) | ambiguous | short (from enactment) | CR-7c, CR-10c, CR-12b (C-39 +, C-40 −) | complement (as C-39) | A-26, A-19, A-10 |
| C-44 | charging_firms | quantity_traded (public charging) | increase | medium; long | CR-9, LW-10 | complement: charging and BEVs (close) | A-24, A-22, A-5 |
| C-45 | charging_firms | asset_value (charging businesses) | increase | short (from enactment) | CR-7c, CR-10c | complement (as C-44) | A-24, A-22, A-3 |
| C-46 | exporters.vessmark | quantity_traded (exports) | ambiguous | long | CR-9 (currency), CR-12b | currency: payments for car imports (weak) | A-23, A-4 |
| C-47 | owners.bev (at enactment) | asset_value (BEVs) | ambiguous | short (from enactment) | CR-7c, CR-10c, CR-12b: (−) K5 capitalized; (+) displaced demand (A-27) | substitute: used BEVs for new combustion cars (partial) | A-2, A-27, A-3 |
| C-48 | buyers.used_cars | price_paid (used BEVs) | ambiguous | medium | CR-6, CR-12b: (+) displaced demand (A-27); (−) K5 lowers a BEV's yield | substitute (as C-47) | A-2, A-27 |
| C-49 | importers.brand, sellers.foreign | quantity_traded (new combustion cars exported to Vessmark) | decrease | medium; long | CR-9 (input_to: the importer's sales are the foreign maker's sales), CR-5a | input_to (close) | A-1, A-2, A-3 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| buyers.new_bev, quantity_demanded (new BEVs), medium; long | K1 removes the combustion option (CR-4) | K5 attaches $250 a year to owning a BEV (CR-4) | A-22 (empirical, p 0.85): the ban chain dominates; the charge is below the excise a combustion car pays | increase (C-5) |
| buyers.used_cars, price_paid (used combustion), medium | displaced demand (C-9); under U1-a, the import supply also stops (C-23) | under U1-b, more imports (C-23); thinning of fuel and repair (A-10, slight before 2040) | Imports: CR-12e response argument (imports cannot push the price below its old level), partial by the case figures (at most 15,000 more against about 110,000 displaced buyers) and A-12 (inspection capacity not expanded). Thinning: A-11 (empirical) | increase under both readings (C-10) |
| owners.combustion (at enactment), asset_value, short | scarcity value from 2035 (CR-7c) | thinning after 2040 (A-10) | A-11 (empirical, p 0.7): for cars in the fleet at enactment, scarcity dominates (most are scrapped by 2043) | increase (C-11) |
| owners.combustion (in fleet after 2040), asset_value, long | scarcity (no new combustion cars) | thinning (A-10, p 0.6) | none: a kind (2) chain with p ≥ 0.5 | ambiguous (C-12) |
| new combustion purchases, 2026 to 2030 | scarcity value carried by cars bought before 2035 (CR-7c with A-11); K5 expected makes a BEV worse | none derived | — | increase (C-15) |
| new combustion purchases, 2031 to 2032 | as above | model withdrawal (A-8) | none | ambiguous (C-16) |
| new combustion purchases, 2033 to 2034 | pull-forward (A-7); scarcity value | model withdrawal (A-8); waiting for pre-registered stock (A-29) | none | ambiguous (C-17) |
| new combustion purchases, from 2035 | — | K1 (op 1) | — | decrease (C-1); under U1-b, partly replaced by grey imports (C-24), which do not reverse it (A-12 and inspection capacity) |
| new BEV purchases, 2026 to 2034 | expected used-BEV demand from 2035 (A-27) | K5 expected; combustion cars bought before 2035 gain scarcity value | none: kind (2) chain | ambiguous (C-18) |
| fuel_retailers, quantity_traded (fuel), medium; long | owners keep older cars that use more fuel per km (A-19) | fewer combustion cars (fleet 2.9 against 3.4 million in 2040) | A-16 (empirical, p 0.75): older cars' fuel use does not offset | decrease (C-31) |
| taxpayers, tax_revenue (total), medium; long | road charge (C-3) | fuel excise (C-32) | none (per car $250 against $600, but the charge is paid on the whole BEV fleet, whose size is not in the figures) | ambiguous (C-33); items recorded separately (CR-12 0.8) |
| repair_shops, quantity_traded and employment | medium: old cars kept running (C-39, C-41) | long: fewer combustion cars (C-40, C-42) | different horizons, not combined (CR-12g) | increase (medium); decrease (long) |
| repair_shops, asset_value, short | C-39 capitalized | C-40 capitalized | none | ambiguous (C-43) |
| owners.bev, asset_value, short; used BEV price, medium | displaced demand (A-27) | K5 capitalized | none | ambiguous (C-47, C-48) |
| new PHEVs | 2035 to 2037: displaced buyers (C-8) | from 2038: K2 (C-2) | different windows | increase (2035 to 2037); decrease (from 2038) |

## 8. Time structure

- **Announcement (March 2026 to 2034).** K1 performs its operation on 1 January 2035 (CR-1 0.7 note on dated operations). Before then it acts only through expectations (CR-10a) and through the prices of durable assets whose yields depend on it (CR-7c): existing combustion cars (C-11), fuel stations (C-35), charging businesses (C-45), repair businesses (C-43) and BEVs (C-47) change value as the Act becomes expected, from its introduction on 3 March 2026 (cross-party support), more on passage in June 2026. Gains and losses go to those who own the assets then, not to later buyers (CR-7c).
- **The 2031 review.** The Minister may postpone by up to three years. The dates are expected to hold (A-3, p 0.7), so the capitalized changes are partial: they move with the probability that the dates hold (CR-7c, "becomes expected" is a matter of probability). The review gives both sides a stake in lobbying in 2026 to 2031 (C-25, C-26). If postponed, every medium-horizon sign that depends on A-3 shifts later by up to three years.
- **Timing shifts in new combustion purchases (CR-12h).** Signed per window against the counterfactual: 2026 to 2030 increase (C-15); 2031 to 2032 ambiguous (C-16); 2033 to 2034 ambiguous (C-17); from 2035 decrease (C-1). Persistence of the bunching: n/a, it exists only during the transition; but the cars bought early stay in the fleet (CR-10b) and so add to the combustion fleet and to fuel and repair demand into the 2040s.
- **PHEV window.** From 2035 to 2037 PHEVs are the only new cars with an engine; displaced buyers move to them (C-8), and the 2038 date pulls PHEV purchases forward into 2036 and 2037 (CR-10a, same direction as C-8). From 2038 they fall to zero (C-2).
- **Pre-registration.** Dealers register unsold stock in late 2034 (C-20) and sell it in 2035 below the counterfactual new price (C-21, C-22). This exists only during the transition (persistence n/a).
- **Stock dynamics (CR-10b).** The combustion fleet changes only through flows: it is equal on both paths in 2035 (3.9 million) and falls below the counterfactual afterwards (2.9 against 3.4 million in 2040; 1.7 against 2.8 million in 2045). Hence fuel volumes, excise, station numbers and repair demand diverge gradually (C-31, C-32, C-36, C-40). Station closures persist once sites are converted (A-17), even if the dates were later postponed.
- **Medium against long run for used cars and repair.** Scarcity of used combustion cars and more repairs dominate in 2035 to 2040 (A-11, A-26); after about 2040 the thinning of fuel and repair (A-10) works the other way, so long-run values are ambiguous (C-12, C-43).
- **Road charge.** Starts in 2035 and is expected from 2026 (C-47, C-18). As a fixed sum per year it does not change the km a BEV owner drives (CR-4, "a change in means alone").

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-4 | owners.bev | resources_available_other_uses | decrease | $250 a year per BEV that owners would have spent or saved | CR-8b, CR-3c |
| C-7 | buyers.new_combustion (those who move to new BEVs) | price_paid (new car bought) | increase | Part of the higher purchase price withdrawn from other uses (fuel saved works the other way; not netted) | CR-4, CR-3a |
| C-13 | owners.combustion | maintenance_spending (repairs to keep cars running) | increase | Means spent repairing old cars rather than on other ends | CR-4, CR-8a |
| C-25 | lobby_groups (dealers, fuel retailers, motoring clubs) | lobbying_effort (for postponement) | increase | Staff time and money | CR-8c |
| C-26 | lobby_groups (BEV importers, charging firms) | lobbying_effort (against postponement) | increase | Staff time and money | CR-8c |
| C-27 | officials.registry | enforcement_cost | increase | Registry staff time on refusals, checks of prior registration and PHEV range, road-charge collection | CR-8c |
| C-28 | users.registry_services | wait_time (+), quality_per_unit (−) (other Registry services) | at_least_one_as_stated | Services the fixed budget no longer covers | CR-8a |
| C-20 | dealers | reclassification (pre-registration) | increase | Registration fees and paperwork used up to keep stock saleable | CR-8c |
| C-1 | buyers.new_combustion, importers.brand, dealers | quantity_traded (new combustion cars, from 2035) | decrease | The gain each party expected from exchanges that no longer take place | CR-5a |

CR-8's symmetry: the road charge paid by BEV owners (C-4) is received by the general budget (C-3); the excise no longer paid by combustion drivers (C-32) is a receipt the budget no longer has, made up by a group of taxpayers or recipients of other spending (C-34, ambiguous because the two items move in opposite directions). The higher price received for used combustion cars (C-10) is paid by their buyers; the gain to owners at enactment (C-11) is matched by the higher prices later buyers pay.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the Act, a material share of new cars sold from 2035 would have combustion engines (about 110,000 a year in 2035, 40,000 in 2045, plus about 25,000 PHEVs a year). | counterfactual_trend | 0.9 | Importers' association forecast; BEV price gap. | K1 and K2 do not bind: C-1, C-2, C-7, C-11, C-31, C-32, C-35, C-49 fail. |
| A-2 | The Registry refuses first registration of new combustion cars and collects the road charge with renewals. | enforcement | 0.95 | Registration is required to drive legally; existing collection of renewal fees. | Most consequences fail or lose this chain. |
| A-3 | The 2035 and 2038 dates are not postponed at the 2031 review. | expectations | 0.7 | Cross-party majority; the review is limited to charging readiness. | Medium-horizon signs shift up to three years later; capitalized values (C-11, C-35, C-45) move less. |
| A-4 | Some would-be buyers of new combustion cars rank a used car or keeping their present car above a new BEV or PHEV. | substitutability | 0.85 | Price gap; rural drivers' range needs. | C-9 to C-15, C-39, C-41 fail. |
| A-5 | World supply of BEVs to Vessmark expands at about unchanged cost within the planning period. | alternative_uses | 0.8 | Vessmark buys 0.4% of world cars; eight years' notice. | C-6 fails; C-5 and C-44 lose part of their chain. |
| A-6 | In 2035, BEV supply to Vessmark cannot expand at once (allocations fixed). | other | 0.3 | Importers plan allocations years ahead. | Below cut-off (see Not reported). |
| A-7 | Buyers know the date, and some can bring the purchase of a new combustion car forward into 2033 to 2034. | expectations | 0.85 | Publicity; replacement cycles of 6 to 10 years. | C-17 loses its (+) chain. |
| A-8 | Importers stop offering some combustion models in Vessmark from 2031 rather than certify or market them for a short window, and some buyers of those models buy something other than a new combustion car. | other | 0.6 | Model cycles of 5 to 7 years; fixed certification and launch costs per market. | C-19 fails; C-16 becomes increase; C-17 loses a (−) chain. |
| A-9 | Dealers pre-register unsold combustion stock before 1 January 2035. | other | 0.8 | Dealers' practice before past rule changes. | C-20, C-21, C-22 fail. |
| A-10 | After about 2040, as the combustion fleet falls well below its counterfactual size, stations close and combustion repair becomes scarcer, lowering a combustion car's value in use. | other | 0.6 | Fleet figures; station volumes. | C-12 becomes increase; C-36, C-38, C-40, C-42 fail. |
| A-11 | For cars in the fleet at enactment, and for used prices in 2035 to 2040, the scarcity chain dominates the thinning chain. | other | 0.7 | Thinning slight before 2040; most 2026 cars scrapped by 2043. | C-10, C-11 become ambiguous; C-13 to C-16 lose their chain. |
| A-12 | Import inspection capacity is not expanded by 2040 enough for imports to close the gap between Vessmark's and Drevland's used combustion prices. | mobility | 0.6 | State test centers; no budget for expansion in the Act. | Under U1-b, C-10 becomes "increase or no change" (response argument without partiality); C-30 loses its U1-b sign. |
| A-13 | Owners expect further restrictions on using combustion cars within their cars' lives. | expectations | 0.3 | No such proposals; K3 protects use. | Below cut-off (see Not reported). |
| A-14 | Residents evade the ban by keeping combustion cars registered in Drevland. | enforcement | 0.3 | Six-month rule; roadside checks of foreign plates. | Below cut-off (see Not reported). |
| A-15 | Dealers, fuel retailers and motoring clubs, and BEV importers and charging firms, can each organize at a cost below their stake in the review. | other | 0.85 | Existing trade associations. | C-25, C-26 fail. |
| A-16 | Vehicle-km in combustion cars fall with the combustion fleet; older cars' higher fuel use per km does not offset it. | other | 0.75 | Fuel economy by age; km driven by age. | C-31, C-32 become ambiguous; C-35 to C-37 lose their chain. |
| A-17 | Fuel stations' costs are largely fixed per outlet, and their sites have other uses. | other | 0.7 | Station accounts; volumes needed to break even. | C-36, C-38 fail. |
| A-18 | Fuel retailers adjust staff or hours to volume. | alternative_uses | 0.7 | Staffing by volume. | C-37 fails. |
| A-19 | Some owners keep combustion cars longer, repairing them, because the car is now worth more than the repair. | other | 0.8 | Scrap decisions turn on repair cost against value. | C-13, C-14, C-39, C-41 fail. |
| A-20 | Used imports from Drevland are at import parity, and rise when Vessmark's used price rises. | mobility | 0.75 | 25,000 imports a year; the $1,800 gap. | U1-b signs of C-23, C-29, C-30 fail. |
| A-21 | Under U1-b, registering a new combustion car briefly in Drevland and importing it costs less than the premium it earns in Vessmark for some importers. | other | 0.6 | Drevland registration about $500; transport and inspection $1,800. | C-24's U1-b sign fails. |
| A-22 | The ban chain on new BEV registrations dominates the road-charge chain. | substitutability | 0.85 | The charge is below a combustion car's excise; the ban removes the choice of about half of new-car buyers. | C-5 becomes ambiguous; C-7, C-44, C-45 lose their chain. |
| A-23 | A new BEV costs more to buy in 2035 than the comparable combustion car. | other | 0.7 | Forecast gap of about $2,000. | C-7 fails. |
| A-24 | Public charging sales rise with the BEV fleet. | other | 0.8 | Share of charging done publicly. | C-44, C-45 fail. |
| A-25 | Some would-be buyers of combustion cars buy PHEVs in 2035 to 2037. | substitutability | 0.8 | PHEVs are closest to combustion cars in range and refueling. | C-8 fails. |
| A-26 | In 2035 to 2040, the old cars kept in use need more repair a year than the new combustion cars missing from the fleet would have. | other | 0.8 | Repair spending by car age. | C-39, C-41 become ambiguous. |
| A-27 | Some displaced buyers of new combustion cars buy used BEVs. | substitutability | 0.6 | Price of used BEVs against new ones. | C-18, C-47, C-48 lose their (+) chain and take the (−) sign. |
| A-28 | The Registry's budget does not rise with the new checks. | revenue_use | 0.8 | K4: budget fixed by law; no appropriation. | C-28 fails. |
| A-29 | Dealers clear pre-registered stock in 2035 below the new price, and some buyers who would have bought new in late 2034 wait for it. | other | 0.55 | Discounts on pre-registered cars after past rule changes. | C-21, C-22 fail; C-17 loses a (−) chain. |

No new premises (A-N) were needed: every derivation used the case assumptions, the case figures (arithmetic) or the policy text.

**Not reported** (an assumption below 0.5):
- New BEV prices and waiting rise in 2035 because allocations are fixed (CR-6, public-supply-like fixed quantity in the short run): needs A-6 (p 0.3). Under A-5 the price is unchanged (C-6).
- Existing combustion cars lose value from expected further use restrictions (CR-10a, CR-7c): needs A-13 (p 0.3).
- Residents keep combustion cars registered in Drevland (CR-4, x: comply, y: violate; `informal_activity` increase and `cross_border_purchases` increase): needs A-14 (p 0.3). The direction is a priori (CR-4a: no one evades less because of the ban); the scale is not.

### Final check before the report

1. **Uncombined chains.** Every key reached by opposing chains is in section 7. Chains written in section 8 (bunching, pre-registration, the PHEV window, the 2031 review) are signed per window or combined there; none is left uncombined.
2. **Group signs.** The Registry crowding (C-28) is a mixed group. The CR-6 margins for the used market are a free price (C-10), which satisfies the "at least one margin" conclusion by itself (CR-6 0.8 note); no waiting is claimed for used cars.
3. **Baseline.** Every sign is against Vessmark without the Act on the forecast trend, not against 2025. New BEV purchases rise against a counterfactual that already rises.
4. **Worse off is not poorer.** Displaced buyers are worse off by their ranking (CR-3a) but `resources_available_other_uses` is not signed for them: those who buy BEVs pay more up front and less fuel excise later. It is signed only for BEV owners, who pay a sum they cannot avoid (C-4).
5. **Timing shifts.** New combustion purchases (C-15 to C-17, C-1), PHEVs (C-8, C-2), pre-registration (C-20, C-21) are signed per window.
6. **Both sides of every transfer.** Road charge (C-3, C-4); fuel excise (C-32, C-34); capitalized gains on existing cars (C-11) against the higher prices paid by used buyers (C-10); pre-registration discount (C-21, C-22).
7. **Every actor class, every core rule.** CR-4: buyers (substitute, timing, evade: below cut-off), importers (drop models), dealers (reclassify, comply), used importers (relocate under U1-b), lobby groups. CR-6: new BEVs (C-6), used cars (C-10), Registry and inspection queues (C-28, C-30). CR-7c: cars, stations, repair and charging businesses, BEVs. CR-9: fuel, repair, charging, Drevland, foreign makers, currency. CR-11: no information conveyed beyond the dates themselves; expected further restrictions are below cut-off (A-13).
8. **Unstated premises.** Organization for lobbying (A-15), margins (A-4, A-25, A-27), the alternative being worse (A-23) are in the table.

## 11. Report

**The policy:** From 1 January 2035 the Vessmark Registry will not register a new combustion-engine car for the first time; new plug-in hybrids with at least 50 km of electric range may be registered until the end of 2037. Cars registered before those dates can still be used and resold. From 2035 every battery-electric car pays a road charge of $250 a year. The Minister may postpone the dates by up to three years after a 2031 review.

**Visible consequences:** From 2035, no new combustion cars are sold, and from 2038 no new PHEVs (C-1, C-2); importers and foreign makers sell none to Vessmark (C-49). More new BEVs are bought than would have been (C-5), at about the world price (C-6). BEV owners pay the road charge (C-3, C-4). Fuel excise revenue falls as the combustion fleet shrinks below its counterfactual size (C-32).

**Invisible consequences:**
- *Owners of existing combustion cars* gain from the Act's announcement, because used combustion cars become scarcer from 2035 (C-11, C-10); they repair them more and scrap them later (C-13, C-14). After 2040 the value of the remaining cars is ambiguous, as stations close and repair becomes scarcer (C-12, C-38).
- *Buyers:* displaced buyers who move to BEVs pay more for the car (C-7); some buy PHEVs while they can (C-8); buyers of used combustion cars pay more (C-10). Before 2035, more new combustion cars are bought in 2026 to 2030 (C-15), and fewer combustion models are offered from 2031 (C-19). Dealers pre-register unsold stock and sell it at a discount in 2035 (C-20 to C-22).
- *Imports from Drevland* depend on how "previously registered" is read: under U1-a, used combustion imports stop, Drevland's used prices fall and inspection queues shorten; under U1-b, imports and grey imports of new cars registered first in Drevland rise and inspection queues lengthen (C-23, C-24, C-29, C-30).
- *Fuel and repair:* fuel sales, station values, station numbers and station jobs fall (C-31, C-35 to C-37); repair work and mechanics' jobs rise in 2035 to 2040 and fall later (C-39 to C-42); public charging sales and charging businesses' values rise (C-44, C-45).
- *The state:* the Registry spends more on enforcement (C-27) with a fixed budget, so other Registry users wait longer or get worse service (C-28). Both sides lobby over the 2031 review (C-25, C-26).

**Ambiguous effects:** New combustion purchases in 2031 to 2034 (C-16, C-17): the scarcity value of cars bought before the date and the pull-forward push up; model withdrawal and waiting for discounted stock push down. New BEV purchases before 2035 (C-18) and BEV values (C-47, C-48): the expected road charge pushes down; displaced demand for used BEVs pushes up. Total tax revenue and what other taxpayers must make up (C-33, C-34): the charge adds, lost excise subtracts. Long-run value of combustion cars and of repair businesses (C-12, C-43). Exports through the currency link (C-46).

**Key conditions:** The dates hold (A-3, p 0.7); displaced buyers turn partly to used cars (A-4, p 0.85); scarcity dominates thinning until about 2040 (A-11, p 0.7); the ban dominates the road charge for new BEVs (A-22, p 0.85); inspection capacity limits imports (A-12, p 0.6); BEV supply expands at unchanged cost (A-5, p 0.8). Evasion through Drevland registration (A-14), fixed BEV allocations (A-6) and expected further restrictions (A-13) are below the cut-off.

**What this analysis cannot say:** The size of any effect, so not whether total tax revenue rises or falls, or whether owners of existing cars gain more than buyers of used cars lose. It does not weigh gains against losses or say whether the policy is good. Environmental, health and safety effects, including emissions and air quality, are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.new_combustion, importers.brand, dealers | quantity_traded (new combustion cars, excluding PHEVs, registered from 2035) | decrease | medium; long | visible | B | CR-1 (op 1, dated 1 January 2035: K1 removes the option of registering, so of buying or selling, a new combustion car); CR-5a (exchanges that would have taken place, A-1, are prevented; both parties lose a gain each expected) | A-1, A-2, A-3 |
| C-2 | buyers.new_phev, importers.brand, dealers | quantity_traded (new PHEVs, from 2038) | decrease | medium; long | visible | B | CR-1 (op 1 dated 1 January 2038 by K2); CR-5a | A-1, A-2, A-3 |
| C-3 | taxpayers, recipients_of_other_spending | tax_revenue (road charge) | increase | medium; long | visible | B | CR-1 (K5: $250 a year per BEV); CR-8b (what owners pay is received by the general budget); CR-12 0.9 (an activity that exists only under the policy is an increase against none) | A-2 |
| C-4 | owners.bev | resources_available_other_uses | decrease | medium; long | visible | B | CR-8b; CR-3 note (a sum they cannot avoid while they keep the car); CR-3c | A-2 |
| C-5 | buyers.new_combustion | quantity_demanded (new BEVs) | increase | medium; long | visible | B | CR-4 (x: new combustion car, removed; y: new BEV, so displaced buyers for whom y ranks next switch); CR-12b (K5 makes y worse, an opposing chain) and CR-12e with A-22 (empirical: the ban chain dominates) | A-1, A-2, A-3, A-22 |
| C-6 | buyers.new_bev | price_paid (new BEVs, before the road charge) | no_change | medium; long | invisible | B | CR-6 0.9 (splitting a shift: added demand meets supply that expands at unchanged cost, A-5, so it is taken in quantity, not price); CR-7a (world supply moves to Vessmark until yields are equal; Vessmark is 0.4% of world demand) | A-5 |
| C-7 | buyers.new_combustion (those who move to new BEVs) | price_paid (new car bought) | increase | medium | invisible | B | CR-4 (they move from x, removed, to a BEV, C-5); arithmetic on A-23 (a new BEV costs more than the comparable combustion car in 2035); CR-3a (they are worse off by their own ranking) | A-1, A-3, A-22, A-23 |
| C-8 | buyers.new_phev | quantity_traded (new PHEVs, 2035 to 2037) | increase | medium | visible | B | CR-4 (x: new combustion, removed; y: PHEV, the nearest open substitute, A-25); CR-10a (the 2038 date pulls PHEV purchases into 2036 and 2037, same direction) | A-25, A-2, A-3 |
| C-9 | buyers.used_cars | quantity_demanded (used combustion cars) | increase | medium | invisible | B | CR-4 (x: new combustion, removed; y: used combustion car or keeping the present car, A-4); CR-9 (relation: used cars substitute for new cars) | A-4, A-2, A-3 |
| C-10 | buyers.used_cars | price_paid (used combustion cars) | increase | medium | invisible | B | CR-6 (more demand against a used stock that changes only through flows, CR-10b, moves the price to a higher clearing level; a free price satisfies the margin conclusion, CR-6 0.8); U1-a: the import supply stops (C-23), same direction; U1-b: imports rise (A-20) but CR-12e response argument: they cannot push the price below its old level, and CR-12 0.9: the response is partial (case figures: at most 15,000 more imports against about 110,000 displaced buyers; A-12); CR-12b with A-11 (scarcity dominates thinning before 2040) | A-4, A-11, A-12, A-2, A-3 |
| C-11 | owners.combustion (cars registered at enactment) | asset_value (cars) | increase | short (from introduction, March 2026) | invisible | B | CR-10c and CR-7c (the expected rise in the cars' value from 2035, C-10, is captured by those who own them when it becomes expected, partly from introduction and more at passage, in proportion to the probability the dates hold, A-3); CR-12b with A-11 (scarcity dominates thinning for these cars) | A-4, A-11, A-1, A-3 |
| C-12 | owners.combustion (cars still in the fleet after 2040) | asset_value (cars) | ambiguous | long | invisible | B | CR-12b: (+) CR-6 (no new combustion cars, a smaller stock); (−) CR-9 (complement: fewer stations and repair shops lower the value in use, A-10). Kind (2) chain with p ≥ 0.5; no dominance premise | A-4, A-10 |
| C-13 | owners.combustion | maintenance_spending (repairs to keep cars running) | increase | medium | invisible | B | CR-4 (x: scrap, y: repair; the higher value of a running car, C-10, makes y better, A-19); CR-10b (the stock is maintained through flows) | A-19, A-11, A-4 |
| C-14 | owners.combustion | quantity_traded (cars sold for scrap) | decrease | medium | invisible | B | CR-4 (as C-13: owners at the margin keep the car); CR-10b | A-19, A-11, A-4 |
| C-15 | buyers.new_combustion | quantity_traded (new combustion cars, 2026 to 2030) | increase | short | invisible | B | CR-10a (a change expected in 2035 alters choices now); CR-7c (a combustion car bought before 2035 is a durable asset that will carry the scarcity value from 2035, A-11); CR-4 (x: BEV, made worse by the expected K5; y: combustion car, made better); counterfactual: same buyers on the forecast trend | A-4, A-11, A-3, A-2 |
| C-16 | buyers.new_combustion | quantity_traded (new combustion cars, 2031 to 2032) | ambiguous | short | invisible | B | CR-12b: (+) as C-15; (−) CR-4 0.7 (fixed cost per item offered: importers drop models rather than certify them for a short window, and some of their buyers buy something else, A-8). No dominance premise | A-4, A-11, A-3, A-8 |
| C-17 | buyers.new_combustion | quantity_traded (new combustion cars, 2033 to 2034) | ambiguous | short | invisible | B | CR-12b: (+) CR-10a and CR-4 (x: buy in 2035 or later, removed; y: buy in 2033 to 2034, A-7) and C-15's chain; (−) model withdrawal (A-8) and CR-4 (x: buy new in late 2034, y: wait for discounted pre-registered stock, A-29). No dominance premise | A-7, A-8, A-29, A-3 |
| C-18 | buyers.new_bev | quantity_traded (new BEVs, 2026 to 2034) | ambiguous | short | invisible | B | CR-12b: (−) CR-10a and CR-7c (K5, expected, lowers the value of a BEV bought now; a combustion car bought now gains scarcity value, A-11); (+) CR-10a and CR-7c (displaced demand raises used-BEV values from 2035, A-27). Kind (2) chain with p ≥ 0.5 | A-2, A-3, A-4, A-11, A-27 |
| C-19 | importers.brand, buyers.new_combustion | variety (combustion models offered, 2031 to 2034) | decrease | short | invisible | B | CR-4 0.7 (a cost fixed per item offered: x: certify and launch a model for a short window, y: drop it, A-8); CR-10a (the 2035 date shortens each model's selling life) | A-8, A-3 |
| C-20 | dealers | reclassification (unsold new combustion stock registered before 1 January 2035) | increase | short (late 2034) | invisible | B | CR-4 (x: hold stock that cannot be registered from 2035, y: register it before the date so that it is no longer "new", s. 2, and keeps its use under K3, A-9); CR-12 0.9 (an activity that exists only under the policy); CR-8c (registration costs used up) | A-9, A-2 |
| C-21 | buyers.pre_registered | price_paid (pre-registered combustion cars, 2035, against their counterfactual new price) | decrease | medium (2035) | invisible | B | CR-5c (the terms move with what the seller may receive: the car can no longer be sold as new); CR-6 (stock that cannot be replaced clears at a price below the new price, A-29) | A-9, A-29 |
| C-22 | dealers | net_price_received (pre-registered combustion stock, 2035) | decrease | medium (2035) | invisible | B | CR-5c, CR-6 (as C-21); CR-7b (stock already held cannot move to another use, so its holder bears the loss) | A-9, A-29 |
| C-23 | importers.used | quantity_traded (used combustion cars imported from Drevland) | U1-a: decrease; U1-b: increase | medium | invisible | B | U1-a: CR-1 (op 1: an imported used car has not been registered in Vessmark, so it is "new" and cannot be registered); CR-5a. U1-b: CR-7a (cars move between the two markets until prices differ by no more than the cost of moving, A-20); CR-4 (the higher Vessmark used price, C-10, makes importing better); capped by inspection capacity (A-12) | A-2, A-20 |
| C-24 | importers.used | reclassification (new combustion cars first registered in Drevland and imported) | U1-a: no_change; U1-b: increase | medium | invisible | B | U1-a: such a car is still "new" in Vessmark, so the option does not exist. U1-b: CR-4 (x: comply, y: register in Drevland first and import; the premium exceeds the cost, A-21); CR-7a | A-21, A-2 |
| C-25 | lobby_groups (dealers, fuel retailers, motoring clubs) | lobbying_effort (for postponement at the 2031 review) | increase | short | invisible | B | CR-4 (x: accept the dates, y: lobby for the postponement s. 9 allows; their stakes, C-31, C-35, C-1, make y better; A-15: they can organize); CR-8c | A-15 |
| C-26 | lobby_groups (BEV importers, charging firms) | lobbying_effort (against postponement) | increase | short | invisible | B | CR-4 (x: accept a possible postponement, y: lobby against it; their stakes, C-5, C-44, A-15); CR-8c | A-15 |
| C-27 | officials.registry | enforcement_cost | increase | medium; long | invisible | B | CR-1 (K4: refusals, checks of prior registration and of PHEV range, road-charge collection, A-2); CR-8c (resources spent enforcing are used up) | A-2 |
| C-28 | users.registry_services | wait_time (+), quality_per_unit (−) (other Registry and inspection services) | at_least_one_as_stated | medium | invisible | B | CR-8a (staff time directed to the new checks is withdrawn from other tasks, since the budget is fixed, A-28); CR-6 0.7 (public supply with a fixed budget: the pressure goes to waiting or to service quality; which one is not signed) | A-28, A-2 |
| C-29 | sellers.foreign (Drevland used-car market) | price_paid (used combustion cars in Drevland) | U1-a: decrease; U1-b: increase | medium | invisible | B | CR-9 (across_border: Vessmark buyers are part of Drevland's demand); CR-6 0.7 (a wider-market price moves in the CR-6 direction by as much as the quantity matters: U1-a, about 25,000 fewer exports; U1-b, more exports, A-20) | A-20, A-2 |
| C-30 | importers.used | wait_time (state import inspection) | U1-a: decrease; U1-b: increase | medium | invisible | B | CR-6 0.7 (public supply at a set fee, $900, with fixed capacity, A-12: U1-a, combustion imports stop, so fewer cars queue; U1-b, more cars seek the same capacity, A-20, and the pressure goes to waiting) | A-20, A-12 |
| C-31 | fuel_retailers | quantity_traded (motor fuel) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: fuel complement to combustion cars; a smaller combustion fleet, CR-10b, uses less); CR-12e with A-16 (empirical: older cars' higher use per km does not offset) | A-16, A-1, A-3 |
| C-32 | taxpayers, recipients_of_other_spending | tax_revenue (fuel excise) | decrease | medium; long | visible | B | CR-9 (fewer liters, C-31); arithmetic ($0.70 per liter); CR-8b (the receipt falls with the payment) | A-16, A-1, A-3 |
| C-33 | taxpayers, recipients_of_other_spending | tax_revenue (fuel excise plus road charge) | ambiguous | medium; long | invisible | B | CR-12 0.8 (two items in one variable: road charge up, C-3; excise down, C-32); CR-12b, no dominance premise (the BEV fleet size is not in the figures) | A-2, A-16 |
| C-34 | taxpayers, recipients_of_other_spending | resources_available_other_uses | ambiguous | medium; long | invisible | B | CR-8 0.7 (payers from the general budget: whoever makes up a shortfall, or receives a surplus, is a group); CR-12b (the net budget change, C-33, is ambiguous) | A-2, A-16 |
| C-35 | fuel_retailers | asset_value (stations) | decrease | short (from enactment) | invisible | B | CR-10c and CR-7c (the expected fall in volume from 2035, C-31, is borne by those who own stations when it becomes expected); CR-4 0.8 (costs fixed per outlet: the loss falls on the station business, limited by the site's other uses, A-17) | A-16, A-1, A-3 |
| C-36 | fuel_retailers | number_of_sellers (stations) | decrease | long | invisible | B | CR-4 0.8 (a cost fixed per outlet bears on whether the outlet operates: x: operate at lower volume, y: convert the site, A-17); CR-7a; CR-10b (the stock of stations falls through closures as volume falls, A-10) | A-17, A-16, A-10 |
| C-37 | workers.fuel_stations | employment (fuel retailing) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: station labor input_to fuel retailing; demand for it follows fuel volume, C-31, A-18) | A-18, A-16 |
| C-38 | owners.combustion | travel_time (to fuel and repair) | increase | long | invisible | B | CR-9 (complement: fewer stations, C-36, and scarcer combustion repair, A-10, mean longer trips for the remaining owners); CR-10b | A-10, A-17 |
| C-39 | repair_shops | quantity_traded (combustion repair) | increase | medium | invisible | B | CR-9 and LW-10 (relation: repair complement to cars in use; owners keep old cars running, C-13, and the old cars need more repair than the missing new ones would have, A-26) | A-26, A-19, A-4 |
| C-40 | repair_shops | quantity_traded (combustion repair) | decrease | long | invisible | B | CR-9 and LW-10 (a smaller combustion fleet, CR-10b, A-10, needs less combustion repair) | A-10 |
| C-41 | repair_shops (mechanics) | employment (combustion repair) | increase | medium | invisible | B | CR-9 and LW-10 (relation: mechanics' labor input_to repair; follows C-39) | A-26, A-19, A-4 |
| C-42 | repair_shops (mechanics) | employment (combustion repair) | decrease | long | invisible | B | CR-9 and LW-10 (follows C-40) | A-10 |
| C-43 | repair_shops | asset_value (repair businesses) | ambiguous | short (from enactment) | invisible | B | CR-10c and CR-7c (the business value reflects expected yields); CR-12b (more repair in 2035 to 2040, C-39; less after, C-40); no dominance premise | A-26, A-19, A-10 |
| C-44 | charging_firms | quantity_traded (public charging) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: charging complement to BEVs; more BEVs, C-5, A-24) | A-24, A-22, A-5 |
| C-45 | charging_firms | asset_value (charging businesses) | increase | short (from enactment) | invisible | B | CR-10c and CR-7c (the expected rise in charging sales, C-44, is captured by owners when it becomes expected, in proportion to A-3) | A-24, A-22, A-3 |
| C-46 | exporters.vessmark | quantity_traded (exports) | ambiguous | long | invisible | B | CR-9 (currency: payments for imported cars are the means with which foreigners buy Vessmark's exports); CR-12b: (+) each new BEV costs more to import (A-23); (−) fewer new cars are bought as some buyers keep old or used cars (A-4). Stopped at depth 3 | A-23, A-4 |
| C-47 | owners.bev (at enactment) | asset_value (BEVs) | ambiguous | short (from enactment) | invisible | B | CR-10c and CR-7c; CR-12b: (−) K5 lowers each BEV's yield from 2035, capitalized now; (+) displaced buyers of new combustion cars buy used BEVs from 2035 (A-27). Kind (2) chain with p ≥ 0.5 | A-2, A-27, A-3 |
| C-48 | buyers.used_cars | price_paid (used BEVs) | ambiguous | medium | invisible | B | CR-6; CR-12b: (+) more demand from displaced buyers (A-27); (−) K5 makes owning a BEV worse for every buyer (CR-4) | A-2, A-27 |
| C-49 | importers.brand, sellers.foreign | quantity_traded (new combustion cars exported to Vessmark) | decrease | medium; long | invisible | B | CR-9 (input_to: the foreign makers supply the importers whose sales fall, C-1); CR-5a | A-1, A-2, A-3 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-050-C1: The composition of a durable stock by age. K1 changes the age mix of the fleet (old cars kept, new ones missing), and several chains (fuel use per km, repair per car, value in use after 2040) turn on that mix. CR-10b says the stock changes only through flows, but no core rule relates a change in the stock's age mix to the use of its complements; each step needed an empirical premise (A-16, A-26). This may be correct (it is empirical), but the calculus gives no prompt for it.
- GAP-050-C2: Thinning of a complement network. The value of a combustion car falls as fewer others use the same stations and repair shops (A-10). This was derived from CR-9 plus CR-4 0.8 (cost fixed per outlet), but no rule states that a fall in other users of a complement raises its cost to the remaining users; it is assembled each time from two notes.

**(b) Core-rule wording that was hard to apply.**
- CR-12h and the normal form: the signs per window for new combustion purchases (C-15 to C-17) depend on window boundaries the analyst chooses (2030 and 2032, from A-8's 2031 date). The rule does not say how to choose windows when several timing chains start at different dates.
- CR-12e response argument under one reading only: for used prices (C-10), the import response exists under U1-b only, and its partiality comes partly from the case figures and partly from A-12. The 0.9 note does not say whether a capacity figure in the case counts as arithmetic or still needs the premise for a later period.
- CR-7c with a postponement power: "becomes expected is a matter of probability" fits A-3, but it is unclear whether a discretionary power to postpone (s. 9) should be treated as a reading, an assumption, or a probability already inside the capitalized value.
- CR-1 for K5: a lump-sum tax per BEV is op 4 for existing owners in effect but op 3 for prospective buyers; the 0.9 note on thresholds covers ranges, not classes split by date of purchase.
- CR-3 note: for displaced buyers who move to BEVs, the higher price (A-23) and the saved excise move resources in opposite directions; the note forbids a sign but does not say whether to record an ambiguous `resources_available_other_uses` or nothing. Nothing was recorded.

**(c) Vocabulary missing from the ontology.**
- No variable for the size of a household-held durable stock (the fleet) or for its age; `capital_stock_target` is productive capacity.
- No variable for the rate of use of a durable good (vehicle-km); fuel quantity stood in for it.
- No variable for the scrappage rate; `quantity_traded (cars sold for scrap)` stood in for it.
- The horizons short, medium and long have no fixed meaning for a policy whose operative date is nine years after enactment; windows were defined in section 1.
- No actor class for users of a public administrative service crowded by new duties (`users.registry_services` was introduced).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the Vessmark case. No new combustion cars from 2035 and no new PHEVs from 2038. More new BEVs, with the road charge as an opposing chain that A-22 dominates. Buyers who move to BEVs pay more for the car. More PHEVs in 2035 to 2037. Fewer combustion models from 2031, pre-registration of unsold stock, and an ambiguous 2033 to 2034 window. Used imports and grey imports are signed per reading. Cars are repaired and kept longer, and used combustion prices and the value of cars held at enactment rise in 2035 to 2040. The long-run value of the stock is ambiguous as the fuel and repair network thins, and the value of existing BEVs is ambiguous. Fuel sales, excise, station values and station numbers fall, charging rises, total revenue is ambiguous, and the fixed-budget Registry crowds out its other work. Both versions derive the complement-thinning chain and the road charge's effect on the substitute's quantity rather than its price. That confirms the pattern version's verdicts on EN-14 and RS-16 0.9. The differences: the pattern version signs total new-car purchases `decrease` (C-7) by a response argument that does not cover U1-a's removal of imported used cars, a separate change with its own (+) chain. It also leaves Drevland's used price unsigned where CR-6 asks for a sign. It omits several derivable keys: the pre-2033 windows for new combustion and BEV purchases, the pre-registration discount, the inspection queue, repair businesses' value and mechanics' labor, and the used-BEV price. The core version signs labor alone where the derivable form is a group (C-37, C-41, C-42). It signs long-run repair work `decrease` without the age-mix chain that the pattern records (C-40). It signs new combustion purchases in 2026 to 2030 `increase` on A-11 outside that premise's scope (C-15), and charging firms' value `increase` with no premise that charging capacity expands slowly (C-45). It omits total new-car purchases, used imports before 2035 and scrapping after 2040.

Counts: M 24, V 7, S 2, OP 17, OC 4.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | |
| C-2 | C-2 | M | | |
| C-3 | C-4 | M | | |
| C-4 | C-3 | M | | |
| C-5 | C-5 | V | | `quantity_substitute` (BEVs registered) in the pattern; `quantity_demanded` in the core, with the quantity traded implied by C-6 (price unchanged under A-5). Same chains and dominance premise (A-22). |
| C-6 | C-7 | M | | Both sign a change in the good bought (a BEV instead of a combustion car) as `price_paid` increase. 6.2g asks that prices be signed per unit of a given good, so a change in mix is not a price change. Neither version has a variable for "spends more on the car bought". |
| C-7 | none | OC | P | Pattern: total new cars `decrease` (CR-4a, response argument, partial with A-4). The response argument binds the responses of displaced combustion buyers. Under U1-a, the Act also removes the option of an imported used combustion car for about 25,000 buyers a year (CR-1 op 1). That is a separate change, not a response, and some of those buyers move to new cars (CR-4): a (+) chain with p ≥ 0.5 that CR-12e does not bound. A second (+) chain comes from owners who sell at the higher used price and buy new (CR-3: keeping the car costs its sale price). Since entries to the fleet are new cars plus imports, the response argument bounds that sum, and under U1-a it lets new purchases exceed the counterfactual by as much as imports fall. Derivable form: U1-b `decrease` (as the pattern argues); U1-a `ambiguous` without a dominance premise. Analyst misapplication of CR-12e. Core-version omission of the key. |
| C-8 | C-8 | M | | |
| C-9 | C-17 | M | | |
| C-10 | C-19 | M | | |
| C-11 | C-20 | V | | `inventory_held` (pre-registered stock unsold at the date) in the pattern; `reclassification` (stock registered before the date) in the core. Both use CR-12 0.9. |
| C-12 | none | OC | E | Used combustion imports in 2026 to 2034 increase: CR-7c and CR-10c (the premium on cars in use after 2035 is capitalized from enactment, as the core's own C-11 says), then CR-7a across the border (A-20). Holds under both readings. The core signs imports only from 2035 (C-23). Core-version omission. |
| C-13 | C-23 | M | | |
| C-14 | C-24 | M | | |
| C-15 | C-13 | M | | |
| C-16 | C-14 | M | | |
| C-17 | none | OC | E | Scrapping after 2040 `ambiguous`: cars retained are scrapped later (+), and fewer combustion cars reach scrapping age (−). CR-10b, CR-12b and CR-12g give it. The core signs scrapping only for the medium horizon (C-14). Core-version omission. |
| C-18 | C-25, C-26 | V | | Split by side. |
| C-19 | C-11 | M | | |
| C-20 | C-10 | M | | |
| C-21 | C-10 | V | | Sellers' `net_price_received`. The core records it through the CR-8b note in section 9 ("paid by their buyers"), not as a row. |
| C-22 | C-12 | V | | `price_paid` after 2040 in the pattern; `asset_value` of cars in the fleet after 2040 in the core. Same chains (scarcity against thinning, A-10), both `ambiguous`. |
| C-23 | C-47 | M | | |
| C-24 | C-31 | M | | |
| C-25 | C-36 | M | | |
| C-26 | C-35 | M | | |
| C-27 | C-37 | S | E | Pattern: station staff's `employment`, `hours_worked` `at_least_one_decrease`. Core: `employment` `decrease`. A-18 ("adjust staff or hours to volume") does not say which, so `employment` alone needs a further premise. CR-9 and LW-10 give lower demand for the labor, and the derivable form is the group. Core-version error. |
| C-28 | C-44 | M | | |
| C-29 | C-39 | M | | |
| C-30 | C-40 | S | E | Repairs after 2040. Pattern: `ambiguous` (older cars kept against fewer cars). Core: `decrease` from the smaller fleet alone. The core's section 7 treats the two chains as belonging to different horizons (CR-12g). But the age-mix chain continues within the long horizon: after 2035 every combustion car is at least as old as the date, and the fleet stays older than on the counterfactual path, where new combustion cars keep entering. That is a (+) chain on repairs per car, the core's own GAP-050-C1. Core-version error (an uncombined chain). The pattern's `ambiguous` needs A-26 to extend past 2040, and the pattern should state that. |
| C-31 | C-38 | M | | The core adds trips to repair shops. |
| C-32 | C-32 | M | | |
| C-33 | C-33 | M | | |
| C-34 | C-20 | V | | The cost of pre-registration as `compliance_cost` in the pattern; the core records it as what `reclassification` uses up (section 9, CR-8c). |
| C-35 | C-27 | M | | |
| C-36 | C-28 | V | | Both are mixed groups from the fixed Registry budget. The second member is "other Registry checks" (−) in the pattern and `quality_per_unit` (−) in the core. |
| C-37 | none | OC | E | Used importers' total spending on inspections and checks, per reading (CR-8c: it follows the number of imports, C-13). Derivable. Core-version omission; the core records the queue instead (C-30). |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-6 | OP | J | New BEV price `no_change` under A-5 (CR-6 0.9 split). The pattern declined to sign it and noted the lack of a `not_signed` value (Gaps d2). With A-5 ("expands at about unchanged cost") the core's sign is derivable. Recording "not signed" is also defensible if "about" is read as allowing a small rise. |
| C-9 | OP | J | Used combustion `quantity_demanded` increase: a step the pattern states in prose (C-20 discussion) and does not record. |
| C-15 | OP | E | New combustion purchases in 2026 to 2030 `increase`. Two (+) chains: the expected road charge makes a BEV worse (CR-4, CR-10a; needs only A-2), and a car bought before 2035 carries the scarcity value (CR-7c). The second is a kind (3) chain under CR-12 0.8. A car bought in 2026 to 2030 is in use well past 2040, where the core's own C-12 is `ambiguous`. The core cites A-11, which covers cars in the fleet at enactment and used prices in 2035 to 2040, not cars bought later. The `increase` needs A-11 extended to these cars; without that it is `ambiguous`. Core-version error. The window is also a pattern-version omission: its C-12 says the premium is capitalized from 2026, but its timing analysis starts in 2031. |
| C-16 | OP | J | 2031 to 2032 `ambiguous`. The window boundaries are the core's choice (its Gaps b). The pattern starts model withdrawal in 2031 and signs only 2033 to 2034. |
| C-18 | OP | E | New BEV purchases in 2026 to 2034 `ambiguous`: the expected charge and the combustion car's resale value (−), against the expected demand for used BEVs from 2035 (+, A-27). Derivable. Pattern-version omission. |
| C-21 | OP | E | Buyers of pre-registered cars pay less in 2035 than these cars would have fetched new (CR-5c, A-29). The pattern states A-29 and uses it in C-9 but records no row. Pattern-version omission. Caveat: a pre-registered car is not a new car, so this signs a change of good, the issue 6.2g raises for prices. |
| C-22 | OP | E | Dealers receive less for pre-registered stock (CR-5c, CR-7b, A-29). Pattern-version omission, as C-21. |
| C-29 | OP | P | Drevland's used price, per reading. CR-6 (0.7, 0.8): the wider-market price moves in the CR-6 direction; record its sign, with a premise if the effect may be negligible. The pattern noted the effect as negligible and did not record it, "as EN-6's wider-market clause". EN-6 as written allows "or note it as negligible". The pattern as written departs from CR-6, applied here by analogy. |
| C-30 | OP | E | Import inspection queue, per reading (CR-6 0.7: public supply with fixed capacity). Under U1-b the pattern's own A-12 says that capacity limits imports, which implies rationing of inspection slots, so `increase` is derivable. Pattern-version omission. The core's U1-a `decrease` is not derivable: 25,000 imports against 40,000 capacity leaves no queue to shorten unless one exists now, which the record does not say. U1-a should be `no_change`, or `decrease` with a premise. |
| C-34 | OP | J | Payers who make up or receive the net budget change: `ambiguous`, since the total (C-33) is. The pattern records no group because the total is unsigned. Either is defensible. |
| C-41 | OP | E | Mechanics' labor rises in 2035 to 2040 (CR-9, LW-10, A-26). Derivable; pattern-version omission. The core signs `employment` alone; as in C-27, the derivable form is `employment`, `hours_worked` `at_least_one_increase`. |
| C-42 | OP | E | Mechanics' `employment` `decrease` after 2040. Core-version error, as in C-40 (the age-mix chain is not combined) and C-27 (group form). The derivable sign is `ambiguous`. |
| C-43 | OP | E | Repair businesses' value `ambiguous` (CR-7c, CR-10c on C-39 and C-40). The pattern applied CR-7c to stations but not to repair shops. Pattern-version omission. |
| C-45 | OP | E | Charging businesses' value `increase`. By CR-7a, yields on means that can move are brought back into line. A lasting gain settles only on means that cannot move (CR-7b), and chargers can be added at will over eight years. The sign needs a premise that charging capacity, or good sites for it, expands slowly. Core-version error (missing premise). |
| C-46 | OP | J | Exports through the currency link `ambiguous`, stopped at depth 3. A depth choice. |
| C-48 | OP | E | Used BEV price in 2035 to 2040 `ambiguous` (displaced demand, A-27, against the charge). Derivable; the pattern records only the value at enactment (C-23). Pattern-version omission. |
| C-49 | OP | J | Foreign makers' sales to Vessmark fall (CR-9, input_to). The pattern names importers in C-1. Adds a class, not a sign. |

### Findings

- **Pattern overclaims or hidden premises.** Total new-car purchases (C-7) were signed `decrease` by a response argument that does not cover U1-a. There the Act also removes imported used combustion cars, a separate change whose buyers partly move to new cars. Entries to the fleet are new plus imported cars, so the response argument bounds their sum, not new cars alone. The sign should be per reading. The `ambiguous` sign for repairs after 2040 (C-30) needs A-26 extended past 2040, which the pattern did not state. Drevland's used price was noted as negligible rather than signed (core C-29). EN-6's wider-market clause, applied by analogy, permits that; CR-6 does not. Both versions sign a move from combustion cars to BEVs as a rise in `price_paid` (C-6), the change-of-mix problem 6.2g records under RS-16.
- **Errors in the core version.** Labor signed as `employment` alone where A-18 and CR-9 give only the group (C-37, C-41, C-42). Long-run repair work and mechanics' labor signed `decrease` with the age-mix chain left out (C-40, C-42), though that chain is the core's own GAP-050-C1. New combustion purchases in 2026 to 2030 (C-15) signed `increase` on A-11, which does not cover cars bought in that window and used past 2040. Charging firms' value (C-45) signed without a premise on slow expansion, contrary to CR-7a. The U1-a sign of the inspection queue (C-30) assumes an existing queue. Omissions: total new-car purchases (per reading), used imports in 2026 to 2034, scrapping after 2040, and importers' inspection spending.
- **Errors in the pattern version (omissions).** New combustion purchases in 2026 to 2032 (core C-15, C-16) and new BEV purchases in 2026 to 2034 (C-18); the pre-registration discount to buyers and dealers (C-21, C-22, on its own A-29); the inspection queue under U1-b (C-30); repair businesses' value (C-43); mechanics' labor in 2035 to 2040 (C-41); the used-BEV price (C-48).
- **Test of 0.9 verdicts.** *EN-14 (needed interpretation; listed as a failure in 6.2g):* confirmed. Without EN-14, the core version derived the thinning of fuel and repair from CR-9 and CR-4 0.8 (its GAP-050-C2), found the long-run value of the stock `ambiguous` (C-12), needed A-11 for the 2035 to 2040 rise and signed scrapping per window. It also shows that EN-14's "kept in use longer" reaches complements through the age mix (GAP-050-C1), which the core version itself then failed to combine after 2040 (C-40). *CR-7 0.9, persistence follows the stock (needed interpretation):* not tested. The core version analyzed no repeal or postponement scenario, so it neither confirms nor contradicts the reading that the stock includes new supply that can return at once. Its one statement on persistence (station closures persist once sites are converted) is consistent with the clause read on the stock. *RS-16 0.9, costs on the substitute (failed for new BEVs):* confirmed. The core version combined the road charge with the quantity of new BEVs (C-5, A-22), signed their price `no_change` from CR-6 0.9 and A-5 (C-6), and took the charge's other effect on the value of existing BEVs (C-47). Nothing pointed at sellers' net price. *CR-12 0.9, response argument (worked as written, with the U1-a point in b2):* the core version raised the same uncertainty in its Gaps (b): whether a capacity figure counts as arithmetic. C-7 adds a further point: the clause does not say which aggregate the response bounds.
- **Limits of the core rules.** None produced a difference: no S, OP or OC row has cause K. Unclear core-rule wording: (1) CR-12e and its 0.9 note do not say which aggregate the response argument bounds (here, entries to the fleet, new plus imported, rather than new cars alone) (C-7). (2) CR-12h gives no guidance on window boundaries when timing chains start at different dates (the core's Gaps b; C-15, C-16 against the pattern's C-9). (3) CR-12 0.8, kind (2): what to do when a dominance or chain premise is stated for one horizon only (A-26 for 2035 to 2040) and the chain continues into the next (C-30, C-40). (4) CR-6 0.7, public supply: it does not say that a queue exists only where capacity binds, which made the U1-a sign of C-30 easy to overstate. (5) CR-7c with CR-7a: a rise in expected yield is captured as `asset_value` only by means that cannot expand. The core version applied it symmetrically to stations (sunk, falling) and to charging (expandable, rising) (C-45). (6) No variable or rule for the age mix of a durable stock (GAP-050-C1).
