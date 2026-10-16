# WE-026 / Analysis: Ban on keeping chickens on residential lots, with a 12-month phase-out

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Marrowfield Residential Fowl Ordinance (Ordinance 2027-14).** Marrowfield is a city of about 220,000 people. Under the existing code (Municipal Code §6.40) a household on a residential lot may keep up to six hens, no roosters, in a coop at least 10 feet from property lines, after a one-time $25 registration with Animal Services. About 1,900 households are registered; Animal Services estimates another 600 to 900 keep hens without registering. A typical flock is four or five hens, so roughly 12,000 hens are kept in the city. Animal Services receives about 120 complaints a year about backyard flocks; under §6.40 a complaint leads to an order to fix the setback or sanitation problem, not to removal of the birds.

Dunmore Township, an unincorporated part of the county, borders the city on the north and west. Its zoning allows poultry on lots of one acre or more and on farms; several small egg farms and three farm stands are 5 to 15 km from most Marrowfield homes. Inside the city, a weekly farmers' market has about six egg vendors, and one farm-and-feed store sells feed, bedding, chicks in spring and prefabricated coops; a second feed store is in Dunmore. Grocery eggs sell for about $3.20 a dozen; farm-stand and market eggs for about $6. A 50-lb bag of layer feed costs about $22. A hen eats about a quarter pound of feed a day and lays about five eggs a week in her first two years, two or three later; hens live six to eight years, and many keepers keep older hens as pets.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | City of Marrowfield, residential zones. Dunmore Township (poultry allowed on lots of one acre or more and on farms) borders the city on two sides. About 40 agricultural lots in the city are exempt. | §1: "This ordinance applies within all residential zones of the City." |
| Announced / enacted / effective / expires | Introduced 2 March 2027 with five of nine council members as sponsors (announced). Enacted 11 May 2027. Acquisition ban effective on enactment; keeping ban effective 11 May 2028. No expiry. | §5: "Fowl lawfully kept on the date of enactment may be kept until twelve months after that date." |
| Enforcement (who, penalties, resources) | Animal Services. Complaint-driven, plus inspection of any lot on the existing registry after the deadline. $150 for a first violation; $500 for each later violation found at a reinspection 30 days later; after a third violation the birds are impounded and transferred to a rescue or euthanized. Carried out "within existing appropriations". | §7, §8 |
| Existing rules | State small-flock rule: eggs from flocks under 50 birds may be sold ungraded directly to final consumers without a license. §6.40 (repealed and replaced) is the counterfactual law. | State Agriculture Code; §6.40 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Keeping ban | `own_production_ban` (recorded in the policy as a `prohibition` of keeping fowl on one's own lot) | Keeping "domestic fowl" on residential lots | All households on residential lots | From 11 May 2028, no fowl may be kept. | Agricultural lots (about 40); registered school programs (up to three birds, on school grounds). |
| K2 Acquisition freeze and phase-out | `prohibition` | Acquiring or hatching fowl; registration | Same | From 11 May 2027, no new birds may be acquired or hatched; birds kept on that date may be kept until 11 May 2028. The registry is closed to new entries and becomes the inspection list. | Same as K1. |
| K3 Enforcement | Enforcement | K1, K2 | Animal Services | Fines, reinspection, impoundment. No new appropriation. | None |

Unclear provisions:
- **U1.** Which birds are banned. The definitions section defines "fowl" as "chickens, ducks, geese, turkeys, guinea fowl and quail"; the title and preamble speak of "backyard chickens"; the enforcement section refers only to "hens". Reading U1-a: only chickens are banned. Reading U1-b: all listed fowl are banned. About 60 registered households keep ducks or quail. Where a sign depends on U1, one sign per reading is given; elsewhere the sign is the same under both readings.

Counterfactual law (CR-1 recording): §6.40 stays in force: up to six hens with registration; complaints lead to fix orders; registration stays open.

**Horizons used.** Short: from announcement (2 March 2027) to about one year after the keeping deadline (May 2029); this contains the announcement window (2 March to 11 May 2027), the phase-out year (11 May 2027 to 11 May 2028) and the first inspections. Medium: one to five years after the deadline. Long: beyond that, when hens kept on the enactment date would in any case have died.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Keeping ban | autistic (restricts keepers' own production for their own use and for gifts) | Yes for registered keepers, whose lots are inspected (A-1, A-18); for unregistered keepers, a risk rather than a removal (A-3) | 1 (dated 11 May 2028: removes the option "keep hens on one's own lot") where enforced; 3 (attaches risk of fines and impoundment) where not; under U1-b the same for ducks, geese, turkeys, guinea fowl and quail | CR-3a, CR-4, CR-5 (gift clarification), CR-7c, CR-8c, CR-10a |
| K2 Acquisition freeze | triangular (prohibits exchanges between residents and sellers of chicks, pullets and adult birds) and autistic (prohibits hatching) | Yes from enactment for prospective keepers and for keepers replacing birds (A-N7) | 1 (dated 11 May 2027: removes "buy, accept or hatch birds"); 1 for unregistered keepers: "register" removed; 3 on existing birds: their use ends at a known date | CR-4, CR-5a, CR-7c, CR-9, CR-10a |
| K3 Enforcement | binary (fines transfer means to the city; impoundment is a confiscation, CR-8e) | Fines reach some violators (A-18) | 3 (penalty attached to "keep after the deadline"); 4 (fines paid); 4 for Animal Services (tasks added with no added means, A-17) | CR-4 (x: comply, y: violate), CR-8b, CR-8c, CR-8d, CR-8e |

No price is fixed by the policy. CR-6 enters where quantities are fixed in the short run (laying flocks of local farms, rescue capacity) or where a supplier does not raise its price (rescues accept birds without charge).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| keepers.complying | Registered and unregistered keepers who give up their birds by the deadline (A-1) | Op 1 (dated): keeping removed; op 3 on the hens and coop they hold: their use ends at a date. They choose among sell, give to a rescue or farm, board, cull. |
| keepers.complying.egg_sellers | Complying keepers who sold surplus eggs (A-15) | As above, plus their egg sales end. |
| keepers.complying.non_sellers | Complying keepers who did not sell eggs | As keepers.complying. |
| keepers.continuing | Keepers who keep birds after the deadline (A-3), mostly unregistered | Op 3: keeping now carries a risk of fines and impoundment; op 1 on replacement: buying chicks in the city is prohibited. |
| keepers.boarding | Keepers who board hens on Dunmore farms (A-6) | New option chosen because the home option is removed (CR-4, x: here, y: there). |
| households.prospective_keepers | Households who would have started keeping hens after May 2027 (A-N7) | Op 1: acquiring removed. |
| households.ducks_quail | About 60 registered households keeping ducks or quail (A-5) | U1-a: no operation; U1-b: op 1 as for keepers.complying. |
| buyers.keeper_eggs | Neighbors and coworkers who bought keepers' surplus eggs (A-15) | Through CR-9 (exchange): their seller stops selling. |
| neighbors | Households next to flocks | Through CR-9 (proximity and gift): fewer flocks next door; fewer egg gifts (A-N3); the consequence of a complaint changes from a fix order to fines and removal. |
| sellers.local_small_farms | Dunmore egg farms, farm stands and the six market vendors | Through CR-9 (substitute): more buyers at each price (A-10). |
| buyers.farm_eggs.other | Existing buyers of farm and market eggs | Through CR-9 (same market): compete with former keepers for a fixed short-run supply. |
| sellers.grocers | Grocery stores selling eggs | Through CR-9 (substitute): more egg buyers (A-2). |
| sellers.city_feed_store | The farm-and-feed store in the city | Through CR-9 (input_to and complement): fewer flocks to supply; op 1 on its chick sales to residents. |
| sellers.dunmore_feed_store | The feed store in Dunmore | Through CR-9: loses city keepers' purchases, gains boarding farms' and continuing keepers' purchases. |
| sellers.coop_builders | Six firms that build coops as a side line | Through CR-9 (input_to): fewer new coops wanted in the city; used coops offered in the county. |
| buyers.other_carpentry | Buyers of the coop builders' other carpentry | Through CR-9 (same labor input_to other work). |
| buyers.county_hens_coops | County buyers of adult hens and used coops | Through CR-9 (same market): more offers in the phase-out year, fewer later. |
| rescues_and_small_farms | Two county poultry rescues and small farms that take hens | Through CR-9 (gift): more birds offered to them near the deadline. |
| neighboring_jurisdictions.dunmore_farms | Dunmore farms that board hens (A-6) | New buyers for boarding. |
| owners.residential_lots | Owners of residential lots when the ban became expected | CR-7c: the option of keeping hens is removed from the lot. |
| owners.exempt_lots | Owners of Dunmore lots of one acre or more and of the 40 agricultural lots | CR-7c: their lots keep the option others lose. |
| officials.enforcement | Animal Services | Op 3: new inspection and fining tasks; op 4: fines received; no added appropriation (A-17). |
| poultry_club, feed_stores | Marrowfield Backyard Poultry Club and feed stores | Lobbying now worth more (CR-4, x: accept, y: lobby). |
| taxpayers | City taxpayers | No change in the budget (A-17); the enforcement cost falls on other Animal Services work instead. |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1, K2 and K3 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | keepers.complying | home_production (eggs from own hens) | decrease | short; medium; long | CR-1 op 1 (K1, K2), CR-4 (x: keep, y: give up), CR-3a | A-1, A-18 |
| C-2 | households.prospective_keepers | home_production (eggs from own hens) | decrease | short; medium; long | CR-1 op 1 (K2), CR-4 | A-N7 |
| C-3 | households.ducks_quail | home_production (duck and quail eggs) | U1-a: no_change; U1-b: decrease | short; medium; long | CR-1 per reading, CR-4 | A-5, A-18 |
| C-4 | officials.enforcement | enforcement_cost | increase | short | CR-1 op 3, CR-8c | A-18 |
| C-5 | keepers.continuing | resources_available_other_uses | decrease | short; medium | CR-1 op 4 (fines), CR-8b, CR-3c | A-3, A-18 |
| C-6 | officials.enforcement (city receipts) | non_tax_receipts | ambiguous | short; medium | CR-12b: (+) CR-8b fines; (-) CR-1 op 1 registry closed | A-3, A-18, A-N7 |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-5 for prevented exchanges; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | keepers.continuing | legal_breach (keeping fowl after the deadline) | increase | short; medium; long | CR-4 (x: comply, y: violate), CR-1 (unenforced prohibition attaches a risk) | A-3 |
| C-8 | keepers.complying | reclassification (switching to ducks or quail) | U1-a: increase; U1-b: no_change | short; medium | CR-4 (x: covered form, y: uncovered form) | A-4 |
| C-9 | keepers.complying | compliance_cost (rehoming, selling, dismantling) | increase | short | CR-1 op 1, CR-8c | A-1 |
| C-10 | keepers.complying | quantity_substitute (eggs bought) | increase | short; medium; long | CR-4 (x: own eggs, y: bought eggs) | A-1, A-2 |
| C-11 | keepers.complying | travel_time (trips to farm stands and the market for eggs) | increase | short; medium; long | CR-4, CR-8c | A-1, A-2, A-10 |
| C-12 | keepers.boarding | cross_border_purchases (hen boarding in Dunmore) | increase | short; medium | CR-4 (x: keep here, y: board there) | A-6 |
| C-13 | keepers.continuing | quantity_traded (surplus eggs sold) | decrease | short; medium; long | CR-4 (x: sell openly, y: stop selling), CR-11b | A-3, A-15 |
| C-14 | keepers.continuing | cross_border_purchases (chicks and pullets bought outside the city) | increase | medium; long | CR-1 op 1 (K2), CR-4 (x: buy in the city, y: buy outside) | A-3, A-N4 |
| C-15 | keepers.complying | net_price_received (adult hens and used coops, 11 May 2027 to 11 May 2028) | decrease | short | CR-4, CR-6, CR-7c | A-1, A-14 |
| C-16 | keepers.complying | wait_time (placing hens with rescues and farms, last months before the deadline) | increase | short | CR-10a, CR-6 | A-1, A-7 |
| C-17 | keepers.complying, keepers.continuing | asset_value (coops and flocks) | decrease | short (from 2 March 2027) | CR-7c, CR-10c | A-13, A-14 |
| C-18 | poultry_club, feed_stores | lobbying_effort (against passage, then for repeal or amendment) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-9 |
| C-19 | sellers.city_feed_store | quantity_traded (chicks and coops, 2 March to 11 May 2027) | ambiguous | short (announcement window) | CR-10a, CR-4, CR-12b | A-13, A-21 |
| C-20 | sellers.city_feed_store | quantity_traded (chicks and coops sold to residents, after 11 May 2027) | decrease | short; medium; long | CR-1 op 1 (K2), CR-5a, CR-9 | A-N7 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Pruned: effects on the customers of farm stands' other produce (trip complement, no premise that farm stands sell other goods to these buyers; Tier C note only); effects on the rescues' other work (depth 4, diffuse).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-21 | sellers.local_small_farms | net_price_received (eggs) | increase | short | CR-9, CR-6 | home eggs substitute for farm eggs (close) | A-1, A-2, A-10 |
| C-22 | buyers.farm_eggs.other | price_paid (farm and market eggs) | increase | short | CR-9, CR-6 | same market (close) | A-1, A-2, A-10 |
| C-23 | buyers.farm_eggs.other | quantity_traded (farm and market eggs) | decrease | short | CR-4c, CR-8a | same market (close) | A-1, A-2, A-10 |
| C-24 | sellers.local_small_farms | capital_stock_target (laying flocks) | increase | medium; long | CR-7a, CR-10b | as above | A-1, A-2, A-10, A-N2 |
| C-25 | sellers.local_small_farms | quantity_traded (eggs) | increase | medium; long | CR-7a, CR-5 | as above | A-1, A-2, A-10, A-N2 |
| C-26 | sellers.grocers, sellers.local_small_farms | quantity_traded (eggs): grocery (+), farm (+) | at_least_one_increase | short; medium; long | CR-9, CR-5 | home eggs substitute for bought eggs (close) | A-1, A-2 |
| C-27 | sellers.city_feed_store | quantity_traded (layer feed and bedding) | decrease | medium; long | CR-9, LW-10, CR-5a | feed and bedding input_to home egg production (close) | A-1, A-11 |
| C-28 | sellers.dunmore_feed_store | quantity_traded (feed, bedding, chicks) | ambiguous | medium; long | CR-12b | input_to (close); across_border | A-1, A-3, A-6, A-N4 |
| C-29 | sellers.city_feed_store | asset_value (store and its poultry line) | decrease | short (from 2 March 2027) | CR-7c, CR-10c, CR-7b | input_to (close) | A-11, A-13 |
| C-30 | sellers.coop_builders | employment (coop building) | decrease | short; medium | CR-9, LW-10 | coops input_to home egg production (close) | A-N7 |
| C-31 | buyers.other_carpentry | price_paid (other carpentry) | decrease | short; medium | CR-9, CR-7a, CR-6 | same labor input_to other carpentry (partial) | A-12, A-N7 |
| C-32 | buyers.county_hens_coops | price_paid (adult hens and used coops, to 11 May 2028) | decrease | short | CR-9, CR-6 | same market, across_border (county) | A-1, A-14 |
| C-33 | keepers.complying | quantity_supplied (adult hens offered in the county, 11 May 2027 to 11 May 2028) | increase | short | CR-10a, CR-4 | same market | A-1 |
| C-34 | keepers.complying | quantity_supplied (adult hens offered in the county, after 11 May 2028) | decrease | medium | CR-10a, CR-10b | same market | A-1, A-8 |
| C-35 | buyers.county_hens_coops | price_paid (adult hens, after 11 May 2028) | increase | medium | CR-9, CR-6 | same market | A-1, A-8, A-14 |
| C-36 | neighboring_jurisdictions.dunmore_farms | quantity_traded (hen boarding) | increase | short; medium | CR-9, CR-5 | across_border (close) | A-6 |
| C-37 | keepers.complying.non_sellers | resources_available_other_uses | increase | medium; long | CR-8a, CR-3 (note), CR-4 | - | A-1, A-2, A-16 |
| C-38 | keepers.complying.egg_sellers | resources_available_other_uses | ambiguous | medium; long | CR-12b | exchange (egg sales) | A-1, A-2, A-15, A-16 |
| C-39 | buyers.keeper_eggs | quantity_traded (eggs bought from keepers) | decrease | short; medium; long | CR-9, CR-5a | exchange (close) | A-1, A-15 |
| C-40 | buyers.keeper_eggs | quantity_substitute (eggs bought from grocers and farms) | increase | short; medium; long | CR-4 | substitute (close) | A-1, A-15, A-N6 |
| C-41 | officials.enforcement (other Animal Services work) | resources_available_other_uses | decrease | short | CR-8a, CR-8d | shared budget | A-17, A-18 |
| C-42 | officials.enforcement | enforcement_cost | ambiguous | medium; long | CR-12b | - | A-1, A-3, A-18 |
| C-43 | owners.residential_lots | asset_value | ambiguous | short (from 2 March 2027) | CR-7c, CR-10c, CR-9 (proximity), CR-12b | proximity (neighbors' flocks) | A-13, A-19, A-N5 |
| C-44 | owners.exempt_lots | asset_value | increase | short (from 2 March 2027) | CR-7c, CR-7b, CR-10c | substitute (lots where hens may be kept) | A-13, A-19, A-N1 |

**Tier C notes (not consequences).**
- *Gifts.* Keepers who gave eggs to neighbors, friends and family (A-N3) stop when they give up their hens. By CR-5 (gift clarification) and CR-8b the giver loses a gain and the recipient a receipt. The ontology has no variable for gifts received, so no consequence is recorded (see Gaps found).
- *Proximity.* Neighbors of former flocks are no longer exposed to the odor, noise and rodents behind the 120 complaints a year (CR-9 proximity, Tier C pending Q20). These are health and environmental effects with no variable in version 1.
- *Complaints.* For neighbors, the ban changes what a complaint brings: under §6.40 a fix order, now fines and removal (CR-1 op 3 applied to the option "complain"). By CR-4, neighbors who want the flock gone gain from complaining, and neighbors who wanted only a fix and value the keeper's goodwill lose from it, so the direction for neighbors as a class is open. There is no variable for complaints.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| officials.enforcement (city receipts), non_tax_receipts, short; medium | fines from continuing keepers found at inspection (CR-8b; A-3, A-18) | registration fees from new keepers stop (K2 closes the registry; A-N7) | None: the number of fines and of forgone registrations is not known | ambiguous (C-6) |
| sellers.city_feed_store, quantity_traded (chicks and coops), announcement window | purchases moved before enactment (CR-10a; A-21) | buyers who would have bought in spring for several years of keeping drop out, since birds bought now may be kept only one year (CR-4, x made worse; A-13) | None | ambiguous (C-19) |
| sellers.dunmore_feed_store, quantity_traded, medium; long | boarding farms feed boarded hens (A-6); continuing keepers buy chicks outside the city (A-N4) | city keepers who bought there give up their hens (A-1) | None | ambiguous (C-28) |
| keepers.complying.egg_sellers, resources_available_other_uses, medium; long | monthly outlays on hens exceeded egg spending (A-16) | egg-sale receipts end (A-15; CR-5a) | None | ambiguous (C-38) |
| keepers.complying.non_sellers, resources_available_other_uses, medium; long | outlays exceed egg spending (A-16) | none derived | - | increase (C-37) |
| keepers.complying, resources_available_other_uses, short | feed outlays stop at the deadline | rehoming costs (C-9), low sale prices (C-15) | Not combined: rehoming cost is recorded as compliance_cost and sale price as net_price_received (CR-12c); no short-run RAOU sign is claimed | not reported |
| officials.enforcement, enforcement_cost, short | inspection of about 1,900 registry lots and reinspections (A-18) | fewer flocks to receive complaints about | Arithmetic: inspection of every registry lot in the first year is far larger than the counterfactual 120 fix-order complaints a year (CR-12e, arithmetic) | increase (C-4) |
| officials.enforcement, enforcement_cost, medium; long | complaint-driven enforcement against continuing flocks, now with fines and reinspection (A-3, A-18) | fewer flocks, so fewer of the 120 complaints a year that §6.40 would have handled (A-1) | None | ambiguous (C-42) |
| owners.residential_lots, asset_value, short | lower chance of a flock next door, valued by some buyers (A-N5; proximity, Tier C) | option to keep hens removed, valued by some buyers (A-19) | None | ambiguous, Tier C (C-43) |
| sellers.local_small_farms, net_price_received, medium; long | demand stays higher than the counterfactual (A-2, A-10) | added laying flocks (A-N2) bring the price back toward cost | CR-12e (a response cannot reverse its cause) establishes only "not below the counterfactual"; no sign claimed | not reported |
| buyers.county_hens_coops, price_paid, by window | after 11 May 2028: fewer adult hens offered (A-8) | to 11 May 2028: more adult hens and coops offered (A-1, A-14) | Different windows, not combined (CR-12g) | decrease (C-32, to 11 May 2028); increase (C-35, after) |

CR-12f: no chains cancel by construction.

## 8. Time structure

- **Announcement (2 March to 11 May 2027).** With five of nine council members as sponsors, passage was expected (A-13). The value of coops and flocks (C-17), of the feed store (C-29) and of residential lots (C-43) moves as the probability of passage rises, so the change is borne by those who held these assets at that time (CR-7c, CR-10c). Chick and coop purchases in the window move both ways (C-19). Lobbying against passage starts (C-18).
- **Acquisition freeze (from 11 May 2027).** Chick and coop sales to residents stop at once (C-20). Hens that die or are taken by predators during the phase-out year cannot be replaced, so home production falls before the keeping deadline (C-1, short).
- **Phase-out year and bunching.** Keepers delay giving up hens until near the deadline (A-7), when rescues and small farms can take only limited numbers. The giving-up would not happen without the policy, so the bunching is a path note (workflow, timing shifts); its effects are recorded as consequences: waiting to place hens (C-16) and lower prices for adult hens and used coops (C-15, C-32).
- **Timing shift of spent hens.** Without the ban, keepers would have sold or rehomed some spent hens in the years after May 2028 (A-8). The ban moves these offers into the phase-out year: offers increase in that window (C-33) and decrease after it (C-34), with prices moving the other way (C-32, C-35). Signed per window against the counterfactual.
- **Farm supply.** Laying flocks cannot expand within months (A-10; pullets take about five months to lay), so the price of farm eggs rises in the short run (C-21, C-22) and flocks grow later (C-24, C-25).
- **Durability.** Coops are durable and specific; feed-store stock and coop builders' coop work are specific to keeping birds (A-11) or movable (A-12). Coop builders move to other carpentry (C-30, C-31). The stock of hens in Marrowfield is not replaced (CR-10b), so feed sales fall gradually and fully only in the medium and long run (C-27).
- **Persistence.** This is not a repeal, so `persistence` is not recorded on consequences. If the ordinance were later repealed, flocks dispersed, coops sold out of the city, farms' added laying flocks (C-24) and coop builders' move to other work would not reverse at once (CR-10b); the asset-value changes would reverse when repeal became expected (CR-7c).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-1 | keepers.complying | home_production (eggs from own hens) | decrease | Eggs, gifts and the satisfaction of keeping hens that keepers ranked above the alternatives (CR-3a) | CR-1, CR-3a, CR-4 |
| C-4 | officials.enforcement | enforcement_cost | increase | Inspector time that would have served other Animal Services ends | CR-8c |
| C-9 | keepers.complying | compliance_cost (rehoming, selling, dismantling) | increase | Time and money spent disposing of birds and coops | CR-8c |
| C-11 | keepers.complying | travel_time (trips for eggs) | increase | Time that would have served other ends | CR-8c |
| C-16 | keepers.complying | wait_time (placing hens) | increase | Time spent waiting and searching for placements | CR-6, CR-8c |
| C-18 | poultry_club, feed_stores | lobbying_effort | increase | Members' and stores' time and money | CR-8c |
| C-20 | sellers.city_feed_store | quantity_traded (chicks and coops sold to residents) | decrease | Exchanges each party expected to gain from (CR-5a) | CR-5a |
| C-23 | buyers.farm_eggs.other | quantity_traded (farm and market eggs) | decrease | Farm eggs no longer bought at the higher price | CR-4c, CR-8a |
| C-39 | buyers.keeper_eggs | quantity_traded (eggs bought from keepers) | decrease | Exchanges both sides expected to gain from | CR-5a |
| C-41 | officials.enforcement (other Animal Services work) | resources_available_other_uses | decrease | Other Animal Services work not done because the budget is fixed | CR-8a, CR-8d |

CR-8's symmetry is applied throughout: fines paid (C-5) are received by the city (C-6); the budget used for inspections (C-4) is withdrawn from other Animal Services work (C-41); the farm egg sales to former keepers (C-25, C-26) are matched by their purchases (C-10); the lower prices received for adult hens (C-15) are the lower prices paid by county buyers (C-32). Impounded birds transferred to a rescue are a transfer from keeper to rescue (CR-8e, CR-8b); euthanized birds are used up (CR-8e, CR-8a); neither is reported, since no premise estimates how many keepers reach a third violation.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Most keepers give up their hens by the deadline (registered keepers know their lots will be inspected; fines rise on reinspection). | enforcement | 0.75 | §7 inspection of registry lots; fines against the value of a small flock. | These consequences fail or lose this chain: C-1, C-9, C-10, C-11, C-15, C-16, C-21 to C-28, C-32 to C-35, C-37 to C-40, C-42. |
| A-2 | Households that gave up hens keep eating eggs and buy them. | substitutability | 0.9 | Egg consumption is common in keeper households. | C-10, C-11, C-21 to C-26, C-37, C-38. |
| A-3 | Enforcement leaves some keepers able to continue: complaints are the only route to unregistered keepers, and many neighbors do not complain. | enforcement | 0.7 | 600 to 900 unregistered flocks; about 120 complaints a year. | C-5, C-6, C-7, C-13, C-14, C-28, C-42. |
| A-4 | Under U1-a, some keepers regard ducks or quail as an acceptable source of eggs. | substitutability | 0.55 | Duck and quail eggs are used for cooking; ducks need water and are louder. | C-8. |
| A-5 | Some households keep ducks or quail now. | other | 0.9 | About 60 registered households. | C-3. |
| A-6 | Some Dunmore farms offer to board hens for city households, and some keepers take it up. | mobility | 0.55 | Farms 5 to 15 km away; hen-boarding is a known arrangement. | C-12, C-28, C-36. |
| A-7 | Many keepers delay giving up hens until near the deadline, and regional rescues and small farms can take only limited numbers in a short period. | other | 0.65 | Two small poultry rescues; about 12,000 hens. | C-16. |
| A-8 | Without the ban, keepers would have sold or rehomed some spent hens in the years after May 2028. | other | 0.8 | Rehoming listings in the county each year. | C-34, C-35. |
| A-9 | The Poultry Club and the feed stores can organize to lobby at a cost below their stake. | other | 0.7 | Existing club with a mailing list; feed store's poultry sales. | C-18. |
| A-10 | A material share of former keepers buy from local small farms, whose laying flocks cannot expand within months. | durability | 0.55 | Stated preference for farm-fresh eggs; pullets take about five months to lay. | C-11, C-21 to C-25. |
| A-11 | Poultry feed and supplies have few uses other than keeping birds. | substitutability | 0.9 | Product lines. | C-27, C-29. |
| A-12 | Coop builders have other carpentry work to move to. | alternative_uses | 0.85 | Coops are a side line for the six firms. | C-31. |
| A-13 | From introduction, residents expected the ordinance to pass. | expectations | 0.8 | Five of nine council members as sponsors. | C-17, C-19, C-29, C-43, C-44. |
| A-14 | The county's market for used coops and adult hens is thin, so added offers lower prices. | other | 0.75 | Few listings in a normal month. | C-15, C-17, C-32, C-35. |
| A-15 | Some keepers sold surplus eggs to neighbors and coworkers. | other | 0.8 | State small-flock rule; listings and signs. | C-13, C-38, C-39, C-40. |
| A-16 | For most complying keepers, monthly outlays on keeping hens exceeded what they now spend on eggs. | other | 0.55 | Feed about $1.85 per dozen from young hens and more from older ones, plus bedding, vet and losses; grocery eggs $3.20, farm eggs $6. | C-37, C-38. |
| A-17 | Enforcement is funded within existing appropriations, and the budget is not raised. | revenue_use | 0.7 | §8 "within existing appropriations". | C-41 (if false, the payers are taxpayers or recipients of other city spending). |
| A-18 | Animal Services does inspect registry lots and fine some violators. | enforcement | 0.85 | §7 mandates inspection of registry lots. | C-1, C-3, C-4, C-5, C-6, C-41, C-42. |
| A-19 | Some buyers of residential lots value the option of keeping hens. | other | 0.6 | Listings that advertise coops. | C-43, C-44. |
| A-20 | Grocery egg supply cannot expand at an unchanged cost for this added demand. | durability | 0.35 | The added demand is small against regional supply. | No reported consequence rests on it (see Not reported). |
| A-21 | Some chick and coop purchases planned for later in 2027 are moved before enactment. | other | 0.6 | Chicks are sold mainly in spring; some households planned summer coops. | C-19 (the (+) chain). |
| A-22 | A regional egg shortage occurs within the horizon. | other | 0.3 | Frequency of past shortages. | No reported consequence rests on it (see Not reported). |
| A-23 | Keepers who continue illegally give neighbors eggs or favors so that they do not complain. | other | 0.45 | Egg gifts to neighbors are already common. | No reported consequence rests on it (see Not reported). |
| A-N1 | Some households that value keeping hens choose a Dunmore lot of one acre or more, or one of the city's agricultural lots, instead of a residential lot, because of the ban. | mobility | 0.55 | NEW. Dunmore borders the city on two sides and allows poultry on such lots; A-19. | C-44. |
| A-N2 | Local small farms can add laying hens over a year or more. | alternative_uses | 0.7 | NEW. Pullets lay at about five months; Dunmore zoning allows poultry on farms; farm-egg price above grocery price. | C-24, C-25. |
| A-N3 | Some keepers give eggs to neighbors, friends and family. | other | 0.8 | NEW. Evidence recorded with A-23: egg gifts to neighbors are already common. | No consequence; supports the gift note in section 6. |
| A-N4 | Some continuing keepers replace aging hens by acquiring chicks or pullets outside the city. | other | 0.6 | NEW. Dunmore feed store sells chicks; unregistered keepers are outside the inspection list; hens lay little after two years. | C-14, C-28. |
| A-N5 | Some buyers of residential lots value a lower chance of a flock next door. | other | 0.6 | NEW. About 120 complaints a year about odor, noise, rodents and setbacks. | C-43. |
| A-N6 | Buyers of keepers' surplus eggs keep eating eggs and buy them elsewhere. | substitutability | 0.85 | NEW. Same evidence as A-2: egg consumption is common. | C-40. |
| A-N7 | Without the ordinance, some households would have started keeping hens after May 2027 (most registering and buying chicks and coops); with it, some of these refrain. | other | 0.85 | NEW. About 2,500 to 2,800 current flocks; spring chick sales at the feed store; the freeze and fines; birds would have to go by May 2028 anyway. | C-2, C-6, C-20, C-30, C-31. |

**Not reported** (an assumption below 0.5, or no premise):
- Grocery egg prices rise because of former keepers' purchases (CR-9, CR-6): needs A-20 (p 0.35).
- Former keepers are worse placed in a regional egg shortage, paying more for eggs than they would have (CR-6): needs A-22 (p 0.3).
- Continuing keepers give neighbors eggs or favors for their silence (CR-5c applied to neighbors' new leverage; CR-4, x: complain, y: accept a gift): needs A-23 (p 0.45).
- Impoundment after a third violation (confiscation and transfer to a rescue, CR-8e and CR-8b; or euthanasia, CR-8e and CR-8a): no premise estimates whether any keeper reaches a third violation.

**Final check (workflow, before the report).**
1. *Uncombined chains.* Every key with two chains is in section 7: receipts (C-6), the announcement window (C-19), the Dunmore feed store (C-28), egg sellers' means (C-38), enforcement cost by horizon (C-4, C-42), lot values (C-43), hen prices by window (C-32, C-35). The farm egg price after the short run has opposing chains and is not reported.
2. *Group signs.* Former keepers buy at grocers or farms; only A-10 licenses farms specifically, so the sellers' side is a group (C-26). No other "at least one" rule was used.
3. *Baseline.* Every sign is against §6.40 staying in force, including the registry staying open (C-6) and spent hens being sold later (C-34).
4. *Worse off is not poorer.* Complying keepers are worse off by their own ranking (C-1, CR-3a), but their resources for other uses rise in the medium run only on A-16 (C-37), and are ambiguous for egg sellers (C-38). Resources decrease only for fined keepers, who pay a sum they cannot avoid once fined (C-5), and for Animal Services' other work (C-41).
5. *Timing shifts.* Spent-hen offers (C-33, C-34) and chick and coop purchases (C-19, C-20) are signed per window. The bunching before the deadline is a path note, since without the policy the giving-up would not happen.
6. *Both sides of every transfer.* Fines (C-5, C-6); budget (C-4, C-41); hen sale prices (C-15, C-32); boarding (C-12, C-36); keeper egg sales (C-13, C-39); impoundment noted as not reported.
7. *Every actor class, every core rule.* CR-7c applied to coops and flocks (C-17), the feed store (C-29), residential lots (C-43) and exempt lots (C-44); CR-6 to farm eggs, adult hens and rescue placements; CR-9 to inputs, substitutes, the county hen market, carpentry labor, gifts and proximity; enforcement cost and its payer (C-4, C-41).
8. *Unstated premises.* Seven premises were added (A-N1 to A-N7), each with p and evidence.

## 11. Report

**The policy:** From 11 May 2027, no household on a residential lot in Marrowfield may acquire or hatch fowl, and the hen registry is closed. From 11 May 2028, no fowl may be kept on residential lots, except on about 40 agricultural lots and in school programs. Animal Services inspects registered lots after the deadline and fines violators $150, then $500 per reinspection, impounding birds after a third violation, within its existing budget. Whether ducks and quail are covered is unclear (U1).

**Visible consequences:** Households that keep hens stop producing their own eggs (C-1), and households that would have started cannot (C-2). Under the broad reading, duck and quail keepers stop too (C-3). The city feed store sells no more chicks or coops to residents (C-20). Animal Services spends more on enforcement in the first year (C-4), and some continuing keepers are fined (C-5).

**Invisible consequences:**
- *Former keepers:* They spend time and money disposing of birds and coops (C-9), sell hens and coops for less in a thin market (C-15), wait to place hens with rescues near the deadline (C-16), and lose value on coops and flocks from the moment the ordinance was expected (C-17). They buy eggs instead (C-10) and travel for farm eggs (C-11). Those who did not sell eggs have more to spend on other things later, since keeping cost more than buying eggs (C-37). Under the narrow reading, some switch to ducks or quail (C-8). Some board their hens in Dunmore (C-12, C-36).
- *Continuing keepers:* Some keep birds illegally (C-7), stop selling surplus eggs (C-13) and buy replacement chicks outside the city (C-14).
- *Egg markets:* In the short run farm and market egg prices rise, and other buyers of farm eggs pay more and buy fewer (C-21 to C-23); later, farms add laying hens and sell more (C-24, C-25). Grocers or farms sell more eggs (C-26). Neighbors and coworkers who bought keepers' eggs buy fewer of them and more elsewhere (C-39, C-40).
- *Suppliers:* The city feed store sells less feed and bedding (C-27) and loses value from announcement (C-29). Coop builders do less coop work (C-30) and shift to other carpentry, whose buyers pay less (C-31).
- *County hen market:* Adult hens and used coops are cheaper in the phase-out year (C-32, C-33), and adult hens are scarcer and dearer after it, since spent hens that would have been sold later were sold early (C-34, C-35).
- *Land:* Lots where hens may still be kept (Dunmore lots of an acre or more, the city's agricultural lots) gain value (C-44).
- *Other Animal Services work* gets fewer resources, since the budget is not raised (C-41). The poultry club and feed stores lobby (C-18).

**Ambiguous effects:** City receipts (fines up, registration fees down; C-6); chick and coop sales in the announcement window (rush before enactment against buyers deterred by a one-year keeping limit; C-19); the Dunmore feed store's sales (C-28); the means of keepers who sold eggs (C-38); enforcement cost after the first year (fewer flocks against fines and reinspections; C-42); residential lot values (option of keeping hens lost against fewer flocks next door; C-43, Tier C).

**Key conditions:** Most keepers comply (A-1, 0.75) because registry lots are inspected (A-18, 0.85), while unregistered keepers can continue (A-3, 0.7). Former keepers keep buying eggs (A-2, 0.9), partly from farms whose flocks cannot grow quickly (A-10, 0.55). The hen and coop market is thin (A-14, 0.75). Keeping cost more than buying eggs for most keepers (A-16, 0.55). The ordinance was expected from introduction (A-13, 0.8). Seven premises were added: buyers moving to exempt lots (A-N1), farm flocks expanding later (A-N2), egg gifts (A-N3), continuing keepers buying chicks outside the city (A-N4), buyers valuing fewer flocks next door (A-N5), buyers of keeper eggs buying elsewhere (A-N6), and households that would have started keeping hens (A-N7).

**What this analysis cannot say:** How large any effect is; whether the losses to keepers outweigh any gains to neighbors; whether the policy is good. Effects on health, odor, noise, rodents, animal welfare and the environment, including the fate of the roughly 12,000 hens, are out of scope for version 1. Which reading of U1 applies is for the policy text, not the analyst.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | keepers.complying | home_production (eggs from own hens) | decrease | short; medium; long | visible | B | CR-1 (op 1, dated: K2 removes replacement from 11 May 2027, K1 removes keeping from 11 May 2028; enforced on registry lots, A-18); CR-4 (x: keep, y: give up; x made worse by fines, so keepers comply, A-1); CR-3a (worse off by their own ranking) | A-1, A-18 |
| C-2 | households.prospective_keepers | home_production (eggs from own hens) | decrease | short; medium; long | invisible | B | CR-1 (op 1: K2 removes acquiring and hatching); CR-4 (x: start keeping, y: not; some at the margin refrain, A-N7) | A-N7 |
| C-3 | households.ducks_quail | home_production (duck and quail eggs) | U1-a: no_change; U1-b: decrease | short; medium; long | visible | B | CR-1 recorded per reading: U1-a performs no operation on ducks and quail; U1-b performs op 1 as for hens, enforced on registry lots (A-18); CR-4 (x: keep, y: give up) | A-5, A-18 |
| C-4 | officials.enforcement | enforcement_cost | increase | short | visible | B | CR-1 (op 3: K3 adds inspection of every registry lot and reinspections); CR-8c (resources spent enforcing are used up); CR-12e (arithmetic: about 1,900 inspections against 120 complaints a year) | A-18 |
| C-5 | keepers.continuing | resources_available_other_uses | decrease | short; medium | invisible | B | CR-1 (op 4: fines paid by registered keepers found keeping, A-18, A-3); CR-8b (the fine is a receipt to the city); CR-3c and CR-3 note (a sum they cannot avoid once fined) | A-3, A-18 |
| C-6 | officials.enforcement (city receipts) | non_tax_receipts | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-8b (fines received, C-5); (-) CR-1 op 1 (K2 closes the registry, so the $25 fees of new keepers who would have registered are not paid, A-N7). No premise says which dominates | A-3, A-18, A-N7 |
| C-7 | keepers.continuing | legal_breach (keeping fowl after the deadline) | increase | short; medium; long | invisible | B | CR-1 (an unenforced prohibition attaches a risk rather than removing the option: unregistered keepers are reached only by complaint); CR-4 (x: comply, y: violate; for keepers whose expected penalty is below the value of the flock, y ranks first, A-3) | A-3 |
| C-8 | keepers.complying | reclassification (switching to ducks or quail) | U1-a: increase; U1-b: no_change | short; medium | invisible | B | CR-4 (x: chickens, the covered form; y: ducks or quail, uncovered under U1-a; keepers for whom the two were close switch, A-4); under U1-b both forms are covered, so no switch is caused | A-4 |
| C-9 | keepers.complying | compliance_cost (rehoming, selling, dismantling) | increase | short | invisible | B | CR-1 (op 1: birds and coop must go); CR-8c (resources spent complying are used up) | A-1 |
| C-10 | keepers.complying | quantity_substitute (eggs bought) | increase | short; medium; long | invisible | B | CR-4 (x: own eggs, removed; y: bought eggs; they keep eating eggs, A-2); CR-1 | A-1, A-2 |
| C-11 | keepers.complying | travel_time (trips to farm stands and the market for eggs) | increase | short; medium; long | invisible | B | CR-4 (y: farm or market eggs, chosen by a material share, A-10); eggs from one's own yard needed no trip; farm stands are 5 to 15 km away and the market is weekly; CR-8c | A-1, A-2, A-10 |
| C-12 | keepers.boarding | cross_border_purchases (hen boarding in Dunmore) | increase | short; medium | invisible | B | CR-4 (x: keep here, removed; y: board there, A-6); CR-5 (exchanges with Dunmore farms that would not have taken place) | A-6 |
| C-13 | keepers.continuing | quantity_traded (surplus eggs sold) | decrease | short; medium; long | invisible | B | CR-4 (x: sell eggs openly, y: stop; selling reveals an illegal flock to buyers who could complain, so x is made worse); CR-11b (exchanges tied to an illegal activity lose the means by which buyers find sellers) | A-3, A-15 |
| C-14 | keepers.continuing | cross_border_purchases (chicks and pullets bought outside the city) | increase | medium; long | invisible | B | CR-1 (op 1: K2 prohibits acquiring in the city, where the feed store cannot sell to residents); CR-4 (x: buy in the city, y: buy outside; A-N4) | A-3, A-N4 |
| C-15 | keepers.complying | net_price_received (adult hens and used coops, 11 May 2027 to 11 May 2028) | decrease | short | invisible | B | CR-4 (x: keep until the deadline, y: sell; many sell in the same year); CR-6 (more offers at each price in a thin market, A-14, move the price to a lower clearing level); CR-7c (the buyer pays only for the yield outside the city) | A-1, A-14 |
| C-16 | keepers.complying | wait_time (placing hens with rescues and farms, last months before the deadline) | increase | short | invisible | B | CR-10a (the dated removal brings giving-up forward to just before the deadline, A-7); CR-6 (rescues take birds without charge and their capacity is limited, so placements are rationed by waiting) | A-1, A-7 |
| C-17 | keepers.complying, keepers.continuing | asset_value (coops and flocks) | decrease | short (from 2 March 2027) | invisible | B | CR-10c (the value of a durable means reflects expected yields: the coop's use in the city ends in May 2028); CR-7c (borne by whoever holds the coop and flock as passage becomes expected, A-13; the outside market is thin, A-14) | A-13, A-14 |
| C-18 | poultry_club, feed_stores | lobbying_effort (against passage, then for repeal or amendment) | increase | short; medium | visible | B | CR-4 (x: accept, y: lobby; the ban makes x worse for keepers and suppliers, so y gains); CR-8c (lobbying uses up resources) | A-9 |
| C-19 | sellers.city_feed_store | quantity_traded (chicks and coops, 2 March to 11 May 2027) | ambiguous | short (announcement window) | invisible | B | CR-12b: (+) CR-10a and CR-4 (x: buy after enactment, prohibited; y: buy before; A-21); (-) CR-4 (x: buy now for several years of keeping, made worse because birds may be kept only to May 2028; A-13). No premise says which dominates | A-13, A-21 |
| C-20 | sellers.city_feed_store | quantity_traded (chicks and coops sold to residents, after 11 May 2027) | decrease | short; medium; long | visible | B | CR-1 (op 1: K2 removes residents' option to acquire birds); CR-5a (exchanges that would have taken place are prevented; both parties lose an expected gain); CR-9 (coops are complements of birds, LW-10) | A-N7 |
| C-21 | sellers.local_small_farms | net_price_received (eggs) | increase | short | invisible | B | CR-9 (relation: home eggs substitute for farm eggs; former keepers buy farm eggs, A-10); CR-6 (more buyers at each price while laying flocks are fixed, A-10, move the price to a higher clearing level) | A-1, A-2, A-10 |
| C-22 | buyers.farm_eggs.other | price_paid (farm and market eggs) | increase | short | invisible | B | CR-9 (relation: same market; they compete with former keepers for a fixed supply); CR-6 | A-1, A-2, A-10 |
| C-23 | buyers.farm_eggs.other | quantity_traded (farm and market eggs) | decrease | short | invisible | B | CR-4c (at a higher price the last unit, valued least, is given up); CR-8a (eggs going to former keepers are withdrawn from other buyers) | A-1, A-2, A-10 |
| C-24 | sellers.local_small_farms | capital_stock_target (laying flocks) | increase | medium; long | invisible | B | CR-7a (the higher yield draws means into egg production until it is brought back into line, net of the cost of raising pullets); CR-10b (stocks change only through flows, so the response is gradual; A-N2) | A-1, A-2, A-10, A-N2 |
| C-25 | sellers.local_small_farms | quantity_traded (eggs) | increase | medium; long | invisible | B | CR-7a and CR-5 (added flocks, C-24, sell to the added buyers) | A-1, A-2, A-10, A-N2 |
| C-26 | sellers.grocers, sellers.local_small_farms | quantity_traded (eggs): grocery (+), farm (+) | at_least_one_increase | short; medium; long | invisible | B | CR-9 (relation: home eggs substitute for bought eggs); CR-5 (former keepers buy eggs, A-2, from grocers or farms; which ones is not licensed without A-10) | A-1, A-2 |
| C-27 | sellers.city_feed_store | quantity_traded (layer feed and bedding) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: feed and bedding input_to home egg production; demand for an input follows the use of what it produces); CR-5a; with few other uses, A-11; in the short run hens still alive are still fed | A-1, A-11 |
| C-28 | sellers.dunmore_feed_store | quantity_traded (feed, bedding, chicks) | ambiguous | medium; long | invisible | B | CR-12b: (-) CR-9 (input_to: city keepers who bought there give up their hens, A-1); (+) CR-9 (input_to: Dunmore farms feed boarded hens, A-6; across_border: continuing keepers buy chicks outside the city, A-3, A-N4). No premise says which dominates | A-1, A-3, A-6, A-N4 |
| C-29 | sellers.city_feed_store | asset_value (store and its poultry line) | decrease | short (from 2 March 2027) | invisible | B | CR-10c (value reflects expected yields: fewer flocks to supply, C-20, C-27); CR-7c (borne by the owner when passage becomes expected, A-13); CR-7b (the stock and fittings are specific, A-11) | A-11, A-13 |
| C-30 | sellers.coop_builders | employment (coop building) | decrease | short; medium | invisible | B | CR-9 and LW-10 (relation: coops input_to keeping hens; no new keepers, A-N7, and used coops offered in the county, C-32) | A-N7 |
| C-31 | buyers.other_carpentry | price_paid (other carpentry) | decrease | short; medium | invisible | B | CR-7a (coop builders move their labor to other carpentry, A-12); CR-9 (relation: same labor input_to other carpentry); CR-6 (more offered at each price moves the price down). Depth 4: chain stops | A-12, A-N7 |
| C-32 | buyers.county_hens_coops | price_paid (adult hens and used coops, to 11 May 2028) | decrease | short | invisible | B | CR-9 (relation: same market, county-wide); CR-6 (more offers at each price in a thin market, A-14) | A-1, A-14 |
| C-33 | keepers.complying | quantity_supplied (adult hens offered in the county, 11 May 2027 to 11 May 2028) | increase | short | invisible | B | CR-10a (the dated removal brings sales of hens that would have been sold later into this window, and adds hens that would never have been sold); CR-4 | A-1 |
| C-34 | keepers.complying | quantity_supplied (adult hens offered in the county, after 11 May 2028) | decrease | medium | invisible | B | CR-10a (spent hens that would have been sold in these years, A-8, were sold in the phase-out year); CR-10b (no new flocks in the city to produce spent hens) | A-1, A-8 |
| C-35 | buyers.county_hens_coops | price_paid (adult hens, after 11 May 2028) | increase | medium | invisible | B | CR-9 (relation: same market); CR-6 (fewer offers at each price in a thin market, C-34, A-14) | A-1, A-8, A-14 |
| C-36 | neighboring_jurisdictions.dunmore_farms | quantity_traded (hen boarding) | increase | short; medium | invisible | B | CR-9 (relation: across_border; keepers move the activity outside the city, C-12); CR-5 (exchanges that would not have taken place) | A-6 |
| C-37 | keepers.complying.non_sellers | resources_available_other_uses | increase | medium; long | invisible | B | CR-4 (x: keep hens, removed; y: buy eggs, A-2); CR-8a and CR-3 note (outlays on feed, bedding, vet and losses stop and egg purchases cost less, A-16; worse off by their own ranking, C-1, but with more to spend elsewhere) | A-1, A-2, A-16 |
| C-38 | keepers.complying.egg_sellers | resources_available_other_uses | ambiguous | medium; long | invisible | B | CR-12b: (+) as C-37 (A-16); (-) CR-5a (receipts from egg sales end, A-15). No premise says which dominates | A-1, A-2, A-15, A-16 |
| C-39 | buyers.keeper_eggs | quantity_traded (eggs bought from keepers) | decrease | short; medium; long | invisible | B | CR-9 (relation: exchange; their sellers stop keeping hens, C-1); CR-5a (both parties lose an expected gain) | A-1, A-15 |
| C-40 | buyers.keeper_eggs | quantity_substitute (eggs bought from grocers and farms) | increase | short; medium; long | invisible | B | CR-4 (x: keepers' eggs, gone; y: other eggs; A-N6) | A-1, A-15, A-N6 |
| C-41 | officials.enforcement (other Animal Services work) | resources_available_other_uses | decrease | short | invisible | B | CR-8a (resources directed to inspections, C-4, are withdrawn from other Animal Services work since the budget is fixed, A-17); CR-8d (no other spending frees money for it) | A-17, A-18 |
| C-42 | officials.enforcement | enforcement_cost | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-1 op 3 and CR-8c (complaints against continuing flocks now lead to fines and reinspections, A-3, A-18); (-) CR-9 (fewer flocks, A-1, so fewer of the complaints and fix orders §6.40 would have handled). No premise says which dominates | A-1, A-3, A-18 |
| C-43 | owners.residential_lots | asset_value | ambiguous | short (from 2 March 2027) | invisible | C | CR-12b: (-) CR-7c and CR-10c (the option of keeping hens, valued by some buyers, A-19, is removed; borne by owners when passage becomes expected, A-13); (+) CR-9 (proximity, Tier C) and CR-7c (a lower chance of a flock next door, valued by some buyers, A-N5). No premise says which dominates | A-13, A-19, A-N5 |
| C-44 | owners.exempt_lots | asset_value | increase | short (from 2 March 2027) | invisible | B | CR-7c and CR-10c (lots that keep the option gain buyers who value it, A-19, A-N1; captured by owners when passage becomes expected, A-13); CR-7b (the gain settles on land, which is fixed in supply) | A-13, A-19, A-N1 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-026-C1: The fate of a living stock that can neither be replaced nor kept (about 12,000 hens). CR-4, CR-6 and CR-10a give the directions of selling, giving, boarding and the timing of each, and CR-8e covers impoundment, but culling by the keeper (as distinct from euthanasia after impoundment) is a use-up of means that no core rule prompts for, and the ontology has no variable to record it. The step was left as a note in section 9.
- No other step lacked a core rule. Proximity chains (C-43, neighbors' exposure) are covered by CR-9 at Tier C pending Q20, which is already open.

**(b) Core-rule wording that was hard to apply.**
- CR-6 says pressure is displaced when "a rule prevents the price from moving". The rescues accept hens without charge by their own choice, not by any rule; C-16 applies CR-6's displaced-pressure reasoning ("whatever the reason the price is where it is") to a supplier who chooses not to price. The first paragraph supports this; the second, which lists the margins, is worded only for a price held by a rule.
- CR-12d with an ambiguous sign: C-43 combines a Tier B chain with a Tier C proximity chain. CR-12d says a consequence takes the lowest tier in its chain, but does not say whether an ambiguous sign produced by a Tier C opposing chain is Tier C, or whether the Tier B sign should stand with a Tier C note (the 0.7 clarification covers only underivable opposing effects). Recorded as ambiguous, Tier C.
- CR-1 dated operations: K2 removes an option at enactment and K1 another a year later. The clarification covers one dated removal; with two dates, the asset (a flock) loses value in two steps (no replacement from 2027, no keeping from 2028). CR-7c handled it, but the rule does not say how to date a capitalization when the asset's yield is cut at two dates.
- CR-3 note ("worse off is not poorer") was clear for complying keepers, but for keepers who sold eggs the note gives no guidance on combining lost receipts with saved outlays; CR-12b gave ambiguous (C-38).

**(c) Vocabulary missing from the ontology.**
- No variable for gifts received (CR-5's gift clarification names a loss to the recipient that cannot be recorded); only the giver's `home_production` exists.
- No variable for complaints or reports to an enforcement agency, though the policy changes what a complaint brings and enforcement depends on them.
- No variable for animals or other living stock disposed of or culled (`discards` is defined for output thrown away).
- No generic actor class for charities and rescues that take goods without charge; `rescues_and_small_farms` was named ad hoc.
- No timing labels for horizons tied to policy dates; the case's short horizon had to be defined in section 1.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the chicken ban: flocks and home egg output fall, former keepers buy eggs, coops lose value from announcement, some keepers keep birds illegally or board them in Dunmore, purchases in the announcement window are ambiguous, hen disposals bunch in the phase-out year and are signed per window, county buyers pay less for hens and coops in that year, farm egg prices rise in the short run and farms add flocks later, feed and coop suppliers lose, keepers and suppliers lobby, and the enforcement budget is drawn from other Animal Services work. No key is signed in opposite directions. Three keys are signed `increase` in the pattern version and `ambiguous` in the core version. In each case the core version found an opposing chain that the core rules derive and the pattern version left out: lost egg-sale receipts for keepers who sold eggs (pattern C-20), fewer flocks to handle complaints about after the first year (pattern C-21, where OC-3 counts enforcement against zero rather than against the replaced law), and registration fees no longer paid once the registry closes (pattern C-24). The core version also records fourteen consequences the pattern version does not have. Most of them are omissions in the pattern version. Two are errors in the core version: an unpriced carpentry price change (C-31) and an omitted opposing chain on county hen prices after the deadline (C-35). The pattern version was written under catalog 0.6. Several 0.7 clarifications used by the core version were drawn from this example: dated CR-1 operations, `proximity` and `gift` relations under CR-9, the CR-5 gift clarification, the CR-12 rule on opposing chains that cannot be derived, and the variables `home_production`, `non_tax_receipts` and `legal_breach`. These explain the recording differences (class V) and residential lot values (C-43). They explain none of the sign differences.

Counts: M 11, V 12, S 3, OP 14, OC 0.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | V | | The pattern version used `capital_stock_target` (flocks and coops) as a proxy because 0.6 had no variable for own production; the core version uses `home_production`, added in 0.7 from this example's gap (d). The pattern version could not record the CR-3a loss by own ranking as a consequence, so it stated it in section 4. The core version attaches it to C-1. |
| C-2 | C-10 | M | | The core version extends the horizon to long. |
| C-3 | C-20 | V | | The pattern version records the purchases (`investment_target`) and the core version records the feed store's sales (`quantity_traded`, CR-5a). The core version classifies K2 as partly triangular: the acquisition ban prevents purchases of chicks and pullets. That is correct, and the pattern version's statement that the ordinance "forbids no exchange" (its C-19 note and K1/K2 classification) is wrong for K2. |
| C-4 | C-19 | V | | Both are `ambiguous` (CR-10a pull-forward against a shorter period of use, CR-12b), on the same premises (A-13, A-21). The pattern version records this on the buyers' side and the core version on the feed store's side. The RS-8 *Unless* clause the pattern version proposed (P-026-2) has since been added to the catalog. |
| C-5 | C-7 | V | | The pattern version used `informal_activity` and flagged it as a misfit (gap (d)(3)). The core version used `legal_breach`, which 0.7 defines as breach of a rule "within the legal market". It fits keeping birds no better than the other variable, because keeping birds is not trade. The claim and sign are the same. |
| C-6 | C-8, C-3 | V | | The pattern version used one key with per-reading signs (U1-a increase from switching; U1-b decrease from existing duck keepers). The core version splits it into `reclassification` (U1-a increase, U1-b no_change) and the duck and quail keepers' `home_production` (U1-a no_change, U1-b decrease). Each reading gives the same direction in both versions. This also resolves the pattern version's gap (d) on "this chain does not arise under this reading". |
| C-7 | C-12, C-36 | M | | The core version also records the Dunmore farms' side (C-36). |
| C-8 | C-16 | V | | The pattern version gives `search_cost` and `wait_time` as a group with `at_least_one_increase`. The core version signs `wait_time` alone. Only the pattern version's form follows CR-6: rescues that take birds without charge can ration by waiting, by choosing which birds to take, or by sending keepers to search elsewhere, and no premise selects waiting. This is an error in the core version: it narrows a group to one member without a premise for that margin. |
| C-9 | C-33 | M | | Phase-out-window offers of hens. |
| C-10 | C-34 | M | | After-deadline offers. |
| C-11 | C-18 | M | | Same premise (A-9). The core version adds lobbying against passage in the announcement window. |
| C-12 | C-26, C-25 | V | | The pattern version gives one aggregate class (`sellers.substitutes`) with `increase`. The core version gives a group with `at_least_one_increase` over grocers and farms (C-26), plus a separate farm increase in the medium and long run on A-N2 (C-25). Both are valid: the aggregate rises because total purchases rise (C-2), and the per-seller split needs A-10. |
| C-13 | C-21, C-22 | V | | The pattern version gives `price_substitute` for all buyers of farm eggs. The core version splits by side: sellers' `net_price_received` (C-21) and other buyers' `price_paid` (C-22). The premises are the same (A-10). |
| C-14 | C-24 | V | | `investment_target` against `capital_stock_target`. The core version adds A-N2 (farms can add laying hens over a year or more, p 0.7). The pattern version rests C-14 on A-1 and A-10, but A-10 says only that flocks *cannot* expand within months. That some farms do expand later is the CR-4 marginal premise behind CR-7a, and the pattern version leaves it unstated. |
| C-15 | C-27 | V | | The pattern version covers feed and supplies sold to city residents by both stores, short to medium. The core version covers only the city store (C-27, medium and long) and treats the Dunmore store separately (C-28, core-only). The core version omits the short horizon, although its own short horizon runs a year past the deadline, when the feed decrease already holds. It also omits the U1-a chain of duck and quail feed, which the pattern version combined in its section 7: the switch is partial, so fewer birds are fed. Both are minor omissions in the core version. The sign is the same. |
| C-16 | C-30 | V | | The pattern version uses `number_of_sellers` (firms building coops for the city) and the core version uses `employment` in coop building. With A-12 (coops are a side line), labor can respond in hours as well as in heads, so the CR-4 labor margin calls for a group (`employment`, `hours_worked`). Each version signs one member. This is minor. |
| C-17 | C-17 | M | | The core version adds flocks to coops. |
| C-18 | C-32 | M | | Same window and premises (A-1, A-14). |
| C-19 | C-39 | M | | The core version adds continuing keepers who stop selling (C-13, core-only). |
| C-20 (non-sellers) | C-37 | M | | Same dominance premise (A-16, p 0.55). |
| C-20 (keepers who sold eggs) | C-38 | S | E | Pattern: `resources_available_other_uses` increase for all complying keepers. Core: `ambiguous` for keepers who sold eggs. A-16 compares outlays with egg *purchases* only. For sellers, the receipts they lose (CR-5a, recorded by the pattern version itself as C-19) are a second (−) chain that A-16 does not dominate. At $6 a dozen against about $1.85 of feed, the lost receipts can be large. CR-12b gives `ambiguous`. The pattern version omitted the chain: its final check item 6 lists C-19 but does not carry the receipts into C-20. Its candidate pattern P-026-1(vi) has the same omission. |
| C-21 (short) | C-4 | M | | First-year inspection of about 1,900 registry lots against about 120 complaints a year. The core version states the arithmetic dominance (CR-12e). |
| C-21 (medium) | C-42 | S | P | Pattern: `enforcement_cost` increase, short to medium. Core: `ambiguous` in the medium and long run. After the first round of inspections, fines and reinspections against continuing flocks (+) meet fewer flocks for complaints and fix orders that §6.40 would have handled (−). The (−) chain needs no proximity link: a neighbor cannot complain about a flock that is not there (CR-1 on the neighbors' option). The pattern version cited OC-3, which states `enforcement_cost` increase whenever a policy must be enforced and compares against no enforcement rather than against the replaced law. That is the pattern's hidden premise. The analyst also did not look for the opposing chain. |
| C-22 | C-41 | V | | The pattern version gives residents served by Animal Services `wait_time` increase, medium. The core version gives the agency's other work `resources_available_other_uses` decrease, short. The pattern version's actor class follows OC-3 and CR-8a (the cost falls on those whom the displaced work served) better. The core version's medium horizon is consistent with its C-42: once enforcement cost is ambiguous, so is the displacement. The pattern version's medium horizon inherits the problem in its C-21. |
| C-23 | C-5 | M | | Fined keepers. |
| C-24 | C-6 | S | E | Pattern: fine receipts increase, recorded as `tax_revenue` because 0.6 had no variable for other receipts (0.7 adds `non_tax_receipts`). Core: `ambiguous`. Closing the registry (K2) stops the $25 fees that new keepers would have paid (CR-1 op 1, CR-8b, A-N7). Fines of $150 to $500 from an unknown number of violators against $25 from an unknown number of registrants is not arithmetic dominance under CR-12e. The pattern version omitted the forgone fees. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-2 | OP | E | Prospective keepers' `home_production` decreases (CR-1 op 1, CR-4, A-N7). The pattern version recorded their purchases (C-3) but not the production they forgo. This is a pattern-version omission and trivially derivable. |
| C-9 | OP | E | Keepers' `compliance_cost` (rehoming, selling, dismantling) increases (CR-8c). The pattern version's C-8 covers search and waiting, not the work of disposal. This is a pattern-version omission. |
| C-11 | OP | E | `travel_time` for farm and market eggs increases (CR-4, CR-8c, A-10). Eggs from one's own yard need no trip. This is a pattern-version omission. |
| C-13 | OP | E | Continuing keepers sell fewer surplus eggs (CR-4: selling openly reveals an illegal flock). This is valid on A-3 and A-15. The core version's citation of CR-11b is loose, since the egg sales themselves are not illegal. The pattern version's C-19 rests on A-1 (complying keepers) and omits this class. |
| C-14 | OP | E | Continuing keepers buy chicks outside the city (CR-1 op 1 on K2, CR-4, A-N4). This is a pattern-version omission. |
| C-15 | OP | E | Keepers' `net_price_received` for hens and coops falls in the phase-out year. This is the sellers' side of the price the pattern version recorded only for buyers (C-18). The pattern version's final check item 6 (both sides of every transfer) missed it. |
| C-23 | OP | E | Other buyers of farm eggs buy fewer at the higher price (CR-4c). This follows from C-22 and is a pattern-version omission. |
| C-28 | OP | J | The Dunmore feed store's sales are `ambiguous`: city keepers are lost, and boarding farms and continuing keepers' chick purchases are gained (CR-12b). The pattern version's key was sales to city residents across both stores, which excludes the boarding farms' purchases. Choosing to split by store is a matter of scope and depth. |
| C-29 | OP | E | The city feed store's `asset_value` decreases from announcement (CR-7c, CR-10c, A-11). The pattern version applied CR-7c only to coops and lots (final check item 7). This is a pattern-version omission. |
| C-31 | OP | E | Error in the core version. Buyers of other carpentry pay less because coop builders move to other work. CR-6 gives a lower price only if buyers do not absorb the added work at an unchanged price. For six firms with coops as a side line, in the carpentry market of a city of 220,000, that premise is unstated and doubtful. The core version itself declined grocery egg prices for the same reason (A-20, p 0.35). The consequence needs its own premise below the cut-off, or should be dropped. |
| C-35 | OP | E | Error in the core version. County buyers pay more for adult hens after the deadline because fewer spent hens are offered (C-34). The core version omitted an opposing chain derivable by CR-1 op 1 (K2), CR-9 (same market) and CR-6: city residents who would have bought pullets and adult hens in the county market stop buying, so demand there falls too. Without a dominance premise, CR-12b gives `ambiguous`. The same chain strengthens C-32 in the phase-out year, where both push prices down. The pattern version omitted the after-deadline price entirely. |
| C-40 | OP | E | Buyers of keepers' eggs buy elsewhere (CR-4, A-N6). This is a pattern-version omission. |
| C-43 | OP | A | Residential lot values are `ambiguous`, Tier C. The pattern version reported nothing, because under 0.6 the opposing chain (fewer flocks next door) had no derivation (GAP-026-1) and CR-12 had no rule for an underivable opposing chain. 0.7, partly drawn from this example, admits `proximity` chains under CR-9 at Tier C. That makes the chain derivable, so CR-12b and CR-12d give `ambiguous` at Tier C, and the CR-12 clarification on underivable chains does not apply. The core version also adds the premise A-N5. The difference comes from the rule version and the added premise, not from either analyst. |
| C-44 | OP | A | Exempt lots (Dunmore lots of an acre or more, the city's agricultural lots) gain value (CR-7c, CR-7b). This rests on a premise the pattern version did not consider (A-N1, p 0.55: some households that value hens choose an exempt lot because of the ban). It is valid on that premise. |

### Findings

- **Pattern overclaims (OC-3).** OC-3 says `enforcement_cost` increase whenever a policy "must be administered or enforced", with Tier A. Where the policy replaces a law that was itself enforced (here, §6.40 fix orders on about 120 complaints a year) and reduces the activity that law dealt with, the comparison against the counterfactual has an opposing chain. OC-3 should say that the increase is measured against the enforcement the replaced law would have needed, and that the sign is `ambiguous` without a dominance premise where the policy shrinks the enforced activity. This produced the S on pattern C-21 in the medium run, which then carried into C-22.
- **Pattern version hides a premise (C-14).** The farms' expansion of laying flocks rests on an unstated marginal premise: some farms can and do add flocks after the first months. A-10 states only the short-run limit. The core version supplied it as A-N2.
- **Errors in the core version.** C-31 signs a price change in a large market from a small shift in supply, with no premise. This is inconsistent with the core version's own treatment of grocery egg prices (A-20). C-35 omits the withdrawal of city demand from the county hen market, which K2 causes directly, so its `increase` should be `ambiguous`. C-16 signs `wait_time` alone where CR-6 gives only a group with `search_cost` without a premise for each margin. C-27 omits the short horizon and the U1-a duck-feed chain. C-41 names the agency's other work rather than the residents it served. C-13's citation of CR-11b is loose.
- **Errors in the pattern version.** K2 is classified as purely autistic, and the C-19 note says the ordinance "forbids no exchange", but the acquisition freeze prevents purchases of chicks and pullets (CR-5a). C-20 omits the lost egg-sale receipts of keepers who sold eggs, so its `increase` holds only for non-sellers. C-24 omits the registration fees forgone when the registry closes. The pattern version also omits prospective keepers' lost home production, disposal costs, travel for farm eggs, continuing keepers' egg sales and chick purchases outside the city, keepers' lower sale prices for hens and coops, other farm-egg buyers' reduced purchases, the feed store's asset value, and buyers of keepers' eggs turning elsewhere (core C-2, C-9, C-11, C-13, C-14, C-15, C-23, C-29, C-40).
- **Catalog version.** The pattern version's gaps (a) to (d) are largely answered in 0.7: dated operations (CR-1), `proximity` and `gift` relations (CR-9, ontology 2.8), the CR-5 gift clarification, the CR-12 rule on underivable opposing chains, `own_production_ban`, `home_production`, `non_tax_receipts`, `legal_breach`, the `neighbors` actor class, and the RS-8 *Unless* clause (P-026-2). These account for the recording differences (V) and for C-43. They account for none of the S differences, which come from opposing chains derivable under 0.6 as well.
- **Limits of the core rules.** None produced a difference. Every chain behind an S or an OP was checked and is derivable from CR-1 to CR-12 (with the stated premises) or is a core-version error. The core version's own wording notes stand. CR-6's second paragraph is worded for a price held by a rule, not for a private supplier that chooses not to charge (the rescues); the 0.7 public-supply clarification covers only the rule-maker. CR-12d does not say what tier an `ambiguous` sign takes when it is produced by a Tier C opposing chain. CR-7c does not say how to date a capitalization when the asset's yield is cut at two dates. The ontology still has no variable for gifts received, for complaints, or for culled living stock.
