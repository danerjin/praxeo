# WE-026 Ban on keeping chickens on residential lots, with a 12-month phase-out

Analyst: draft (Handbook 0.6, corrected under 0.8)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional city. It is a gap-probing example: it was chosen because it is mainly an *autistic* intervention (01_foundations.md, intervention typology), which restricts what people do with their own means, and none of WE-001 to WE-025 is of that type. The keeping ban (K1) coerces no exchange; the acquisition freeze (K2) also forbids buying chicks and pullets, so it is partly triangular. The analysis therefore tests CR-1 operation 1 applied to own production, the recording of a loss that has no money counterpart, a phase-out with a common deadline, and effects on neighbors who are linked to the restricted households by place rather than by exchange. Health, animal welfare, noise, odor and other neighborhood amenities are out of scope for version 1 and are not analyzed; where they would enter a chain, this is said. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Marrowfield Residential Fowl Ordinance (Ordinance 2027-14).** Marrowfield is a city of about 220,000 people. Under the existing code (Municipal Code §6.40) a household on a residential lot may keep up to six hens, no roosters, in a coop at least 10 feet from property lines, after a one-time $25 registration with Animal Services. About 1,900 households are registered; Animal Services estimates another 600 to 900 keep hens without registering. A typical flock is four or five hens, so roughly 12,000 hens are kept in the city. Animal Services receives about 120 complaints a year about backyard flocks (odor, noise, rodents, coops built too close to the line); under §6.40 a complaint leads to an order to fix the setback or sanitation problem, not to removal of the birds.

Outside the city: Dunmore Township, an unincorporated part of the county, borders Marrowfield on the north and west. Its zoning allows poultry on lots of one acre or more and on farms; several small egg farms and three farm stands are 5 to 15 km from most Marrowfield homes. Inside the city, a weekly farmers' market has about six egg vendors, and one farm-and-feed store sells poultry feed, bedding, chicks in spring and prefabricated coops; a second feed store is in Dunmore. Grocery eggs sell for about $3.20 a dozen; farm-stand and market eggs for about $6. A 50-lb bag of layer feed costs about $22. A hen eats about a quarter pound of feed a day and, in her first two years, lays about five eggs a week, falling to two or three in later years; hens commonly live six to eight years, and many keepers keep older, rarely laying hens as pets.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | City of Marrowfield, residential zones. Dunmore Township (poultry allowed on lots of one acre or more and on farms) borders the city on two sides. | §1: "This ordinance applies within all residential zones of the City." |
| Announced / enacted / effective / expires | Introduced 2 March 2027 with five of nine council members as sponsors (announced). Enacted 11 May 2027. Acquisition ban effective on enactment; keeping ban effective 11 May 2028. No expiry. | §5: "Fowl lawfully kept on the date of enactment may be kept until twelve months after that date." |
| Enforcement (who, penalties, resources) | Animal Services. Complaint-driven, plus inspection of any lot on the existing registry after the deadline. Fine of $150 for a first violation; $500 for each later violation found at a reinspection 30 days later; after a third violation, the birds are impounded and transferred to a rescue or euthanized. To be carried out "within existing appropriations". | §7, §8 |
| Existing rules | State small-flock rule: eggs from flocks under 50 birds may be sold ungraded directly to final consumers without a license. Municipal Code §6.40 (repealed and replaced by this ordinance) is the counterfactual law. | State Agriculture Code; §6.40 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Keeping ban | `own_production_ban` (keeping fowl on one's own lot) | Keeping "domestic fowl" on residential lots | All households on residential lots | From 11 May 2028, no fowl may be kept. | Lots zoned agricultural (about 40 lots on the city's edge); school educational programs registered with the district (up to three birds, on school grounds). |
| K2 Acquisition freeze and phase-out | `own_production_ban` (hatching) and `prohibition` (acquiring fowl, including buying chicks and pullets) | Acquiring or hatching fowl; registration | Same | From 11 May 2027, no new birds may be acquired or hatched; birds kept on that date may be kept until 11 May 2028. The registry is closed to new entries and becomes the inspection list. | Same as K1. |
| K3 Enforcement | Enforcement | K1, K2 | Animal Services | Fines, reinspection, impoundment (above). No new appropriation. | None |

Unclear provisions:
- **U1.** Which birds are banned. The definitions section defines "fowl" as "chickens, ducks, geese, turkeys, guinea fowl and quail", but the title and preamble speak of "backyard chickens", and the enforcement section refers only to "hens". Reading U1-a: only chickens are banned. Reading U1-b: all listed fowl are banned. About 60 registered households keep ducks or quail, alone or with hens. Readings get no probability; where a sign depends on U1, one sign per reading is given.

The counterfactual law is §6.40: keeping up to six hens with registration ($25 for each new keeper), with complaints leading to orders to fix setbacks and sanitation.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Autistic: forbids households to produce eggs (and keep birds) on their own lots. No exchange is forced or forbidden directly; exchanges that depended on the activity (selling or giving surplus eggs, buying feed and coops) stop as a consequence (CR-9). | Yes: about 2,600 households keep hens (A-1 for compliance). | `own_production_ban` has no pattern family (2.3); derived from CR-1 op 1, CR-3, CR-4, CR-9. RS, OC. EN-7 does not apply (K1 prohibits no trade). |
| K2 | Autistic in its ban on hatching; triangular in its ban on acquiring, which prevents purchases of chicks and pullets from the feed stores and county sellers that would otherwise have taken place (CR-5a, OC-4). | Yes | RS-8 with its *Unless* clause for a phase-out to a common deadline (0.7); CR-10a; OC-4. |
| K3 | Binary: fines are forced payments to the city; impoundment is a confiscation (CR-8e). Funded from a fixed budget (OC-3, second funding case, A-17). | Yes, where enforced (A-3, A-18) | OC-3 (0.8: against the enforcement §6.40 would have needed), CR-8 |

**CR-1 operations by actor class.** The counterfactual law is §6.40. Operations are dated (CR-1, 0.7): acquiring is removed from 11 May 2027, keeping from 11 May 2028; before each date the removal acts through expectations (CR-10a) and asset values (CR-7c).

| Actor class | Operations |
|---|---|
| `households.keepers.registered` | Op 1: keeping hens removed (from 11 May 2028), acquiring birds removed (from 11 May 2027). Their lots are on the inspection list, so the removal is enforced. |
| `households.keepers.unregistered` | Op 3 rather than op 1: not on the list, so for them the ban attaches a risk (a fine, if a neighbor complains) to keeping hens (CR-1, Premises). |
| `households.prospective_keepers` | Op 1: starting a flock removed (from 11 May 2027), and with it registering. |
| `input_suppliers.feed` and county sellers of chicks and pullets | Op 1: selling chicks and pullets to city residents removed (from 11 May 2027). |
| `neighbors.of_keepers` | Op 3 on the option of complaining: a complaint now establishes a violation by the birds' presence and leads to fines and removal, not a setback order. Op 1 as well, since they too can no longer keep hens. |
| Households keeping ducks or quail | U1-a: no operation. U1-b: op 1, as for hen keepers. |
| Agricultural lots, school programs | None (exempt). |
| `officials.enforcement` | A new duty without new funds (op 3 on their other work, through the fixed budget). |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `households.keepers` (registered and unregistered; split by response into complying and continuing keepers, and complying keepers into those who sold eggs and those who did not) | About 2,600 households keeping hens | Must give up their flocks by the deadline and cannot replace birds in the meantime; may comply, keep birds illegally, switch to ducks or quail (U1-a), or board hens outside the city. |
| `households.prospective_keepers` | Households that would have started a flock | Cannot start one. |
| Households keeping ducks or quail | About 60 registered households | Under U1-b, must give up their birds. |
| `neighbors.of_keepers` | Households next to a flock | A complaint now removes the flock; can no longer keep hens themselves. |
| `buyers.backyard_eggs` | Neighbors, coworkers and friends who bought or were given surplus eggs | Lose that source. |
| `sellers.substitutes` | Grocers, farmers-market vendors, Dunmore farm stands and small egg farms | More egg buyers. |
| `buyers.farm_eggs.other` | Existing buyers of farm-stand and market eggs | Compete with former keepers for farm eggs. |
| `input_suppliers.feed` | The two feed stores, and chick sellers | Fewer customers for poultry feed, bedding, chicks. |
| `coop_builders` | About six small carpentry firms and the feed store's coop line | Less demand for coops. |
| `buyers.neighboring` | Dunmore and county households and farms that buy used coops and adult hens | More used coops and hens offered in the phase-out year, fewer later; fewer city buyers competing. |
| `hen_boarding_services` | Dunmore farms that could board hens for city households | A new service is in demand. |
| `owners.residential_lots` | Owners of residential lots in the city | Their lots lose the option of keeping hens; fewer flocks next door. |
| `officials.enforcement`, residents served by Animal Services | Animal Services and those who rely on its other work | A new task from a fixed budget. |
| `city_budget` | Receives fines and registration fees | Fine receipts; registration fees end. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `households.keepers` | `home_production` (eggs from own hens) | decrease | short to medium | CR-1 op 1 (dated: K2 removes replacement from 11 May 2027, K1 removes keeping from 11 May 2028), CR-10b (the flock runs down through the phase-out and reaches near zero for complying households at the deadline), CR-3a (worse off by their own ranking) | A-1 |
| C-2 | `households.keepers` | `quantity_substitute` (eggs bought, from all sellers) | increase | short to medium | RS-1; CR-4 (x: home eggs, y: bought eggs) | A-1, A-2 |
| C-25 | `households.prospective_keepers` | `home_production` (eggs from own hens) | decrease | short to long | CR-1 op 1 (K2: starting a flock is barred from 11 May 2027), CR-4 | A-24 |
| C-36 | Households keeping ducks or quail | `home_production` (duck and quail eggs) | U1-a: no_change; U1-b: decrease | short to medium | CR-1 recorded per reading: U1-a performs no operation on ducks and quail; U1-b performs op 1 as for hens; CR-4 | A-5, A-18 |

The visible effect is that backyard flocks disappear from residential lots. The supporters' stated aim (fewer complaints about odor, noise and rodents) is an amenity effect, which is out of scope for version 1; the relation that would carry it to neighbors (`proximity`) is admitted by CR-9 only at Tier C (GAP-026-1, Q20; section 6).

**A loss with no variable of its own.** By CR-3a, every household that chose to keep hens is worse off by its own ranking once that option is removed, whatever happens to its money spending: the eggs, the hobby, the birds as pets, a children's chore, and a hedge against egg shortages were ends it ranked above its alternatives. This conclusion is Tier A (it needs only that the option was chosen and that the ban is enforced against it), and it is the most certain claim in this analysis. Under 0.6 it had no observable variable to attach to. Since 0.7, `home_production` records the observable side (C-1, C-25, C-36), and CR-3a is cited in C-1's derivation. The loss of an activity valued for itself is still not a variable; it is stated here and in the report. C-1 and C-2 record what can be observed: home egg output falls, and egg purchases rise.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `households.keepers`, `households.prospective_keepers` | `investment_target` (chicks, pullets and new coops bought by city residents; window: after enactment) | decrease | short | CR-1 op 1 (K2: acquiring is barred from 11 May 2027), CR-5a, CR-4 | A-1, A-24 |
| C-4 | `households.keepers`, `households.prospective_keepers` | `investment_target` (chicks, pullets and new coops bought by city residents; window: announcement to enactment, 2 March to 11 May 2027) | ambiguous | short | RS-8 (*Unless*: phase-out to a common deadline); CR-10a with CR-4: purchases planned for later in 2027 are pulled forward before the freeze (+); the expected period over which a new bird or coop can be used falls from years to at most 14 months, so fewer are bought (−); CR-12b | A-13, A-21 |
| C-5 | `households.keepers` (mainly unregistered) | `legal_breach` (keeping fowl after the deadline, against the ban) | increase | medium | RS-3; CR-1 (for households not on the registry the ban attaches a risk rather than removing the option); CR-4 (x: comply, y: keep birds) | A-3 |
| C-6 | `households.keepers` | `reclassification` (switching from hens to ducks or quail for eggs) | U1-a: increase; U1-b: no_change | medium | U1-a: RS-5 (ducks and quail are the uncovered form), CR-4; U1-b: both forms are covered, so no switch is caused | A-4 |
| C-7 | `households.keepers` | `cross_border_purchases` (hen boarding or hen shares on Dunmore farms) | increase | medium | RS-4; CR-4 (x: keep hens here, y: keep them there) | A-6 |
| C-8 | `households.keepers` disposing of hens | `search_cost`, `wait_time` (finding a taker for the birds; rescue waiting lists) | at_least_one_increase | short | CR-10a (disposals bunch before the deadline, C-9), CR-6 (0.8: a private supplier that chooses not to charge rations by its own choice; the margins are a group), OC-2 | A-7 |
| C-9 | `households.keepers` | `quantity_supplied` (live hens offered for rehoming or sale; window: phase-out, May 2027 to May 2028) | increase | short | CR-10a, 2.5 timing shift: all hens must go within the window | A-1, A-8 |
| C-10 | `households.keepers` | `quantity_supplied` (live hens offered for rehoming or sale; window: after the deadline) | decrease | medium | CR-10a, 2.5 timing shift: in the counterfactual some spent hens would have been offered in these years; with the ban, there are none left to offer | A-1, A-8 |
| C-11 | `households.keepers`, `input_suppliers.feed` | `lobbying_effort` (against passage, then for repeal, grandfathering of existing flocks, or reading U1-a) | increase | short to medium | RS-7 | A-9 |
| C-26 | `households.keepers` (complying) | `compliance_cost` (rehoming, selling, dismantling coops) | increase | short | CR-1 op 1, CR-8c, OC-2 | A-1 |
| C-27 | `households.keepers` (complying) | `travel_time` (trips to farm stands and the market for eggs) | increase | short to medium | CR-4 (y: farm or market eggs, chosen by a material share; eggs from one's own yard needed no trip), CR-8c | A-1, A-2, A-10 |
| C-28 | `households.keepers` (continuing) | `quantity_traded` (surplus eggs sold) | decrease | medium | CR-4 (x: sell eggs openly, y: stop; selling reveals an illegal flock to buyers who could complain, and complaints are the route to enforcement) | A-3, A-15 |
| C-29 | `households.keepers` (continuing) | `cross_border_purchases` (chicks and pullets bought outside the city) | increase | medium | CR-1 op 1 (K2 bars acquiring in the city), RS-4, CR-4 (x: buy in the city, y: buy outside) | A-3, A-29 |

C-3 and C-4 are the same activity in two windows. K2 bars acquisition from enactment, so after it purchases fall (C-3); these are exchanges prevented (CR-5a), not only a change in own production. In the ten weeks between introduction and enactment, which fall in the spring chick season, two chains conflict (C-4): purchases that some households had planned for later in 2027 are brought forward, but the ban has no grandfathering, so every bird must go by May 2028 whenever it was bought. A chick bought in March 2027 starts laying in late summer and can be kept for only about eight months of laying, rather than several years. The expected yield of a new bird or coop falls, and by CR-4 fewer are bought. RS-8's *Unless* clause (added in 0.7 from this example) and CR-12b give `ambiguous`.

C-5: complaint-driven enforcement with no list of unregistered keepers leaves keeping hens open to those who are not on the registry, at the risk of a fine if a neighbor complains. Registered keepers face inspection and are expected mostly to comply (A-1); the split follows CR-1's instruction to divide a class where the operation differs. The variable is `legal_breach` (breach of a rule, not trade outside the legal market); keeping birds is neither trade nor in a market, so the fit is imperfect (Gaps found, (d)).

C-6 and C-36: under U1-a, ducks and quail are outside the ban, and some keepers switch to them for eggs (RS-5); existing duck and quail keepers are unaffected. Under U1-b, no switch is caused, and households that already keep ducks or quail must give them up too.

C-9 and C-10 are a timing shift (02_ontology.md, 2.5): hens are given up with and without the ban, but at different times. With the ban, every hen still alive at the deadline must go during the phase-out, and households that want eggs as long as possible keep their hens until close to the deadline, so the offers bunch in the last months (A-7, C-8). In the years after, nothing is left to give up.

C-28 and C-29 concern keepers who continue illegally (C-5): selling eggs openly would advertise the flock, and replacement birds can no longer be bought in the city.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `sellers.substitutes` (grocers, market vendors, farm stands) | `quantity_traded` (eggs) | increase | short to medium | CR-9 (buyers turn to them), RS-1 (0.8: a traded quantity needs a supply premise), RS-16 (quantity) | home eggs and bought eggs: `substitute`, close | A-1, A-2, A-25 |
| C-13 | buyers of local farm eggs (market and farm-stand customers, including former keepers) | `price_substitute` (eggs from local small farms) | increase | short | RS-16 | home eggs and local farm eggs: `substitute`, close | A-1, A-10 |
| C-14 | `sellers.substitutes` (small egg farms in Dunmore) | `investment_target` (laying flocks) | increase | medium | CR-9, CR-7a (yield on local egg production rises with C-13), CR-10b | as C-13 | A-1, A-10, A-28 |
| C-15 | `input_suppliers.feed` | `quantity_complement` (poultry feed, bedding and supplies sold to city residents) | decrease | short to medium | RS-12 | feed and hens: `complement`, close | A-1, A-11 |
| C-16 | `coop_builders` | `number_of_sellers` (firms building coops for city residents) | decrease | medium | RS-6, CR-9 | coops and hens: `complement`, close | A-1, A-12 |
| C-17 | `households.keepers` | `asset_value` (coops and equipment) | decrease | short | CR-7c, CR-10c (the coop's yield in the city ends at the deadline, so its value falls to what it fetches outside the city, net of moving it, from the time the ban becomes expected) | coops and hens: `complement`, close | A-13 |
| C-18 | `buyers.neighboring` | `price_paid` (used coops and adult laying hens in the county; window: phase-out) | decrease | short | RS-13 (city supply is added to the county's used market); CR-1 op 1 (K2) with CR-9 and CR-6 (city residents who would have bought pullets and hens in the county stop buying); both chains push the same way (CR-12a) | city and county used markets: `across_border`, close | A-1, A-7, A-14, A-26 |
| C-19 | `buyers.backyard_eggs`, `households.keepers` | `quantity_traded` (surplus backyard eggs sold to neighbors and coworkers) | decrease | short to medium | CR-5a, OC-4 (both parties lose an exchange each expected to gain from); CR-9 | direct exchange between keepers and their buyers (CR-5a; no 2.8 relation needed) | A-1, A-15 |
| C-20 | `households.keepers` (complying, did not sell eggs) | `resources_available_other_uses` | increase | medium | CR-8a (feed, bedding and vet outlays stop) against CR-4 (eggs now bought); CR-3 note; CR-12e dominance by A-16 | — | A-1, A-16 |
| C-30 | `households.keepers` (complying) | `net_price_received` (adult hens and used coops; window: phase-out) | decrease | short | RS-13 and CR-6 (the sellers' side of C-18), CR-7c (the buyer pays only for the yield outside the city) | as C-18 | A-1, A-14 |
| C-31 | `buyers.farm_eggs.other` | `quantity_traded` (farm and market eggs) | decrease | short | CR-4c (at the higher price of C-13, the last unit is given up), CR-8a (farm eggs going to former keepers are withdrawn from other buyers) | same market, close | A-1, A-2, A-10 |
| C-32 | `input_suppliers.feed` (city store) | `asset_value` (store and its poultry line) | decrease | short (from 2 March 2027) | CR-7c, CR-10c (fewer flocks to supply, C-3, C-15, from when passage is expected), CR-7b (the stock and fittings are specific) | feed and hens: `complement`, close | A-11, A-13 |
| C-33 | `buyers.backyard_eggs` | `quantity_substitute` (eggs bought from grocers and farms) | increase | short to medium | RS-1, CR-4 (x: keepers' eggs, gone; y: other eggs) | `substitute`, close | A-1, A-15, A-30 |
| C-34 | `buyers.neighboring` | `price_paid` (adult hens in the county; window: after the deadline) | ambiguous | medium | CR-12b: (+) RS-13 mirror and CR-6 (fewer spent hens offered, C-10); (−) CR-1 op 1 (K2), CR-9, CR-6 (city residents who would have bought pullets and hens in the county no longer do); CR-12 (0.8, kind 2: the opposing chain's premise A-26 has p ≥ 0.5) | as C-18 | A-1, A-8, A-14, A-26 |
| C-35 | `owners.residential_lots` | `asset_value` | ambiguous | short (from 2 March 2027) | CR-12b: (−) CR-7c, CR-10c (every lot loses the option of keeping hens, valued by some buyers); (+) CR-9 (`proximity`, Tier C) with CR-7c (a lower chance of a flock next door, valued by some buyers); CR-12d (Tier C) | `proximity` (neighbors' flocks), Tier C | A-13, A-19, A-27 |
| C-37 | `households.keepers` (complying, sold eggs) | `resources_available_other_uses` | ambiguous | medium | CR-12b: (+) as C-20 (A-16); (−) CR-5a and CR-3 note (0.8: receipts from egg sales end); no dominance premise | direct exchange with buyers of their eggs | A-1, A-15, A-16 |

**C-20, C-37 and the final check, item 4.** Households lose by their own ranking (section 4), yet those that comply may have more money for other things, not less. CR-3's note says when `resources_available_other_uses` falls; here it rises if what a household spent each month on keeping hens (feed alone is about $1.85 per dozen eggs from a young hen, and more from older ones, plus bedding, grit, vet bills and losses to predators) is more than what it now spends on eggs. Many flocks include older hens that lay little, which raises outlays per dozen. A-16 (p = 0.55) is the dominance premise; it is weakest for households that bought farm-stand eggs at $6, and for food-oriented keepers who fed kitchen scraps. A-16 compares outlays with egg purchases only. Keepers who also sold surplus eggs lose those receipts (C-19, CR-5a); at $6 a dozen against about $1.85 of feed, the lost receipts can be large. The CR-3 note (0.8) combines them with the saved outlays under CR-12b, and no premise establishes dominance, so for sellers the sign is `ambiguous` (C-37). The `increase` holds only for keepers who did not sell (C-20).

**C-19 and gifts.** The surplus eggs that keepers sold to neighbors under the state small-flock rule are no longer produced, so those exchanges are prevented (CR-5a). Eggs that were *given* rather than sold are covered since 0.7 by CR-5's gift clarification and the `gift` relation (2.8): the giver loses a gain and the recipient a receipt (CR-8b). The giver's side is in `home_production` (C-1, which includes output given away); no variable records gifts received, so the recipients' side is described here and not recorded (Gaps found, (d)).

**Neighbors (GAP-026-1).** The ordinance's purpose concerns neighbors: about 120 complaints a year about odor, noise and rodents. Two chains reach them.
- *Through exchange rules:* CR-1 op 3 on the option of complaining. A complaint now removes a flock instead of producing a setback order. Neighbors who want a flock gone gain from complaining, including against households that keep hens illegally (C-5); neighbors who wanted only a fix and value the keeper's goodwill may lose from it. There is no variable for complaints, and the direction for neighbors as a class is open; the enforcement work it creates is in C-21 and C-38.
- *Through proximity:* the amenity itself, that a neighbor's yard is quieter and smells less once the flock is gone, and any gain in the value of neighbors' homes from it. The change travels from the keeper's action to the neighbor through physical proximity, not exchange. Since 0.7, CR-9 records this as a `proximity` relation and reports chains through it at Tier C, pending Q20 (GAP-026-1, still open). The amenity is out of scope (2.4); the in-scope chain, lot values, is C-35.

**Residential lot values (C-35).** Two chains reach `asset_value` of residential lots. One: every residential lot loses an option that some buyers value (keeping hens), so by CR-7c its value falls from that chain (A-19, p = 0.6). The other: a lot whose neighbor would have kept a flock gains value with some buyers who value a lower chance of a flock next door (A-27, p = 0.6), a `proximity` chain at Tier C. Under 0.6 the second chain had no derivation and the consequence was not reported. Under 0.7 it is derivable at Tier C, and under CR-12 (0.8, kind 2) a derived chain whose premise has p ≥ 0.5 makes the sign `ambiguous` without a dominance premise. The consequence takes Tier C (CR-12d).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `households.keepers` (complying, did not sell eggs), `resources_available_other_uses`, medium | Outlays on keeping stop (CR-8a). | Eggs now bought (C-2). | A-16: outlays exceed the cost of eggs bought, for most keepers (CR-12e, empirical premise). | **increase** (C-20). |
| `households.keepers` (complying, sold eggs), `resources_available_other_uses`, medium | Outlays on keeping exceed eggs bought (A-16). | Receipts from egg sales end (C-19; CR-5a; A-15). | None | **ambiguous** (C-37). |
| `households.keepers` (fined), `resources_available_other_uses`, medium | — | Fines (C-23). | — | **decrease** (C-23); recorded as its own class. |
| `households.keepers`, `investment_target`, announcement window | Purchases pulled forward before the freeze (A-21). | Shorter expected period of use without grandfathering (A-13). | None | **ambiguous** (C-4). |
| `input_suppliers.feed`, `quantity_complement`, short to medium | Under U1-a, duck and quail keepers still buy feed (C-6). | Hens given up (C-1). | Not needed: under U1-a the switch is partial, so fewer birds are fed in total (A-1). | **decrease** (C-15) under both readings. |
| `sellers.substitutes`, `quantity_traded`, short to medium | Former keepers buy eggs (C-2); buyers of keepers' eggs buy elsewhere (C-33). | None: keepers who keep birds illegally (C-5) buy fewer than the complying ones, but no fewer than without the ban; other buyers of farm eggs buy fewer (C-31), but within the same market as the added buyers, so they cannot reverse the rise that causes it (CR-12e, response argument). | — | **increase** (C-12). |
| `buyers.neighboring`, `price_paid`, phase-out window | — | City hens and coops added to the county market (RS-13); city buyers of pullets and hens withdrawn (K2). | — | **decrease** (C-18). |
| `buyers.neighboring`, `price_paid` (adult hens), after the deadline | Fewer spent hens offered (C-10, A-8). | City buyers of pullets and hens withdrawn (K2, A-26). | None | **ambiguous** (C-34). Different windows from C-18, not combined (CR-12g). |
| `officials.enforcement`, `enforcement_cost`, short | Inspection of about 1,900 registry lots and reinspections (A-18). | Fewer flocks to receive complaints about. | Arithmetic: some 1,900 inspections in the first year against about 120 counterfactual complaints a year (CR-12e, arithmetic on the case's figures; OC-3, 0.8). | **increase** (C-21). |
| `officials.enforcement`, `enforcement_cost`, medium to long | Complaints against continuing flocks now lead to fines and reinspections (A-3, A-18). | Fewer flocks, so fewer of the complaints and fix orders §6.40 would have handled (A-1). | None (OC-3, 0.8: against the right baseline) | **ambiguous** (C-38). |
| `city_budget`, `non_tax_receipts`, short to medium | Fines (CR-8b; A-3, A-18). | $25 registration fees of new keepers end with the registry (K2; A-24). | None: the number of fines and of forgone registrations is not in the case's figures (CR-12e: a count is arithmetic only if in the figures). | **ambiguous** (C-24). |
| `owners.residential_lots`, `asset_value`, short | Lower chance of a flock next door (A-27; `proximity`, Tier C). | Every lot loses the option of keeping hens (CR-7c, A-19). | None | **ambiguous**, Tier C (C-35). |
| Price of grocery eggs, short | Former keepers' added demand (RS-16). | — | — | Not reported: A-20 (p = 0.35), that grocery egg supply cannot expand at an unchanged cost for so small a demand, is below the cut-off. |

## 8. Time structure

Three windows matter.
- **Announcement to enactment (2 March to 11 May 2027).** The chick season. Purchases of chicks and coops are `ambiguous` against the counterfactual (C-4). The value of existing coops (C-17), of the city feed store (C-32) and of residential lots (C-35) moves from when passage becomes likely (CR-7c); with five of nine sponsors, that is from introduction (A-13). RS-8's *Unless* clause (0.7) covers this case: the ban has no grandfathering, so the sign before the freeze is `ambiguous` rather than a rush. Lobbying against passage starts (C-11).
- **Phase-out (11 May 2027 to 11 May 2028).** No replacements, and no purchases of chicks or pullets by city residents (C-3). Flocks shrink as hens die or are culled, and laying falls as they age, so home egg output declines through the year (C-1), and egg purchases rise gradually (C-2) and then jump at the deadline. Disposals bunch in the last months (C-8, C-9; disposal costs C-26), which lowers the county prices of used coops and adult hens in that period (C-18, C-30). Feed sales fall gradually, then sharply (C-15).
- **After the deadline.** Inspections of registered lots, complaints and fines (C-21, C-23, C-24; C-38 after the first year). Illegal keeping (C-5) concentrates among unregistered households and those whose neighbors do not object; these keepers stop selling eggs openly (C-28) and buy replacement birds outside the city (C-29). Small local egg farms add laying flocks over about a year (C-14, A-28), which reduces the price rise of C-13. Coop building for the city ends (C-16), and no spent hens are offered (C-10), while city buyers are also gone from the county market (C-34).

**Food security.** Some households keep hens as a hedge against egg shortages. The ban removes that hedge: in a shortage, these households would now buy in the market and add to demand. Whether a shortage occurs in the horizon is A-22 (p = 0.3), so the chain is a conditional possibility, not a consequence. The hedge itself is part of the loss by own ranking in section 4.

**Expectations.** If the council is expected to adopt reading U1-a in practice, or to grandfather existing flocks after lobbying (C-11), keepers delay disposal past the deadline, which C-5 partly captures.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-21 | `officials.enforcement` | `enforcement_cost` (first year after the deadline) | increase | Officers' time on inspections of registry lots, complaints and reinspections, net of the §6.40 fix orders no longer needed (far fewer). | OC-3, CR-8c, CR-12e |
| C-38 | `officials.enforcement` | `enforcement_cost` (after the first year) | ambiguous | Fines and reinspections against continuing flocks, against the §6.40 complaints and fix orders that fewer flocks no longer generate. | OC-3 (0.8), CR-8c, CR-12b |
| C-22 | residents served by Animal Services | `wait_time` (responses to other calls: stray dogs, wildlife, cruelty reports) | increase | With no new appropriation, the time spent on fowl in the first year comes out of other work (OC-3, second funding case; CR-8a). After it, the sign follows C-38 and is not claimed. | OC-3, CR-8a |
| C-23 | `households.keepers` fined for keeping birds | `resources_available_other_uses` | decrease | What the fined households would have bought with the fine. A fine is a sum they cannot avoid once caught (CR-3 note). | CR-8b, CR-3 |
| C-24 | `city_budget` | `non_tax_receipts` (fines and registration fees) | ambiguous | The receipt side of C-23 (CR-8b), against the $25 fees new keepers would have paid under §6.40 (CR-1 op 1 on registering). | CR-8b, CR-1, CR-12b |

Impoundment (K3) is a confiscation (CR-8e). Birds transferred to a rescue are a transfer to the rescue; birds euthanized are means used up (CR-8e, last sentence). It is not recorded separately: no premise estimates how many keepers reach a third violation, and it concerns the same households as C-23.

The time households spent on their flocks (about 15 minutes a day) is freed. It goes to other uses, but which ones the core rules do not say (CR-4, "a change in means alone"; 06_gaps.md, Q19), so no consequence is recorded. Part of it is taken up by trips for farm eggs (C-27).

If the enforcement budget were raised instead (A-17 false), the payers would be a group of city taxpayers and recipients of other city spending with `at_least_one_decrease` (OC-1 and OC-3, 0.8), not taxpayers alone.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most keepers give up their hens by the deadline (registered keepers know their lots will be inspected; fines rise on reinspection). | enforcement | 0.75 | §7 inspection of registry lots; the size of the fines against the value of a small flock. | C-1, C-2, C-3, C-9, C-10, C-12 to C-16, C-18 to C-20, C-26, C-27, C-30, C-31, C-33, C-34, C-37, C-38 shrink to the complying share or lose this chain. |
| A-2 | Households that gave up hens keep eating eggs and buy them. | substitutability | 0.9 | Egg consumption is common in keeper households (registration survey). | C-2, C-12, C-27, C-31 fail. |
| A-3 | Enforcement leaves some keepers able to continue: complaints are the only route to unregistered keepers, and many neighbors do not complain. | enforcement | 0.7 | 600 to 900 unregistered flocks; about 120 complaints a year. | C-5, C-28, C-29 fail; C-24 and C-38 lose their (+) chain. |
| A-4 | Under U1-a, some keepers regard ducks or quail as an acceptable source of eggs. | substitutability | 0.55 | Duck and quail eggs are used for cooking; ducks need water and are louder. | C-6 under U1-a becomes no_change. |
| A-5 | Some households keep ducks or quail now. | other | 0.9 | About 60 registered households. | C-36 under U1-b fails. |
| A-6 | Some Dunmore farms offer to board hens for city households, and some keepers take it up. | mobility | 0.55 | Farms 5 to 15 km away; hen-boarding is a known arrangement, but none is offered locally yet. | C-7 fails. |
| A-7 | Many keepers delay giving up hens until near the deadline, and regional rescues and small farms can take only limited numbers in a short period. | other | 0.65 | Two small poultry rescues in the county; about 12,000 hens. | C-8 fails; C-18 weakens. |
| A-8 | Without the ban, keepers would have sold or rehomed some spent hens in the years after May 2028. | other | 0.8 | Rehoming listings for hens in the county each year. | C-10 fails; C-34 loses its (+) chain and becomes decrease. |
| A-9 | The Marrowfield Backyard Poultry Club (about 300 members) and the feed stores can organize to lobby at a cost below their stake. | other | 0.7 | An existing club with a mailing list; the feed store's poultry sales. | C-11 not reported. |
| A-10 | A material share of former keepers buy from local small farms, whose laying flocks cannot expand within months. | durability | 0.55 | Keepers' stated preference for farm-fresh eggs; pullets take about five months to lay. | C-13, C-14, C-27, C-31 fail. |
| A-11 | Poultry feed and supplies have few uses other than keeping birds. | substitutability | 0.9 | Product lines. | C-15 weakens; C-32 fails. |
| A-12 | Coop builders have other carpentry work to move to. | alternative_uses | 0.85 | Coops are a side line for the six firms. | C-16: firms stay but idle. |
| A-13 | From introduction, residents expected the ordinance to pass. | expectations | 0.8 | Five of nine council members as sponsors. | C-17's, C-32's and C-35's timing moves to enactment; C-4's (−) chain starts later. |
| A-14 | The county's market for used coops and adult hens is thin, so added offers lower prices. | other | 0.75 | Few listings in a normal month. | C-18, C-30 fail; C-34 loses its (+) chain. |
| A-15 | Some keepers sold surplus eggs to neighbors and coworkers. | other | 0.8 | State small-flock rule; listings and signs. | C-19, C-28, C-33 fail; C-37's class is empty. |
| A-16 | For most complying keepers, monthly outlays on keeping hens exceeded what they now spend on eggs. | other | 0.55 | Feed about $1.85 per dozen from young hens and more from older ones, plus bedding, vet and losses; grocery eggs $3.20, farm eggs $6. | C-20 becomes ambiguous; C-37 stays ambiguous. |
| A-17 | Enforcement is funded within existing appropriations, and the budget is not raised. | revenue_use | 0.7 | §8 "within existing appropriations". | C-22 fails; the payers are a group of city taxpayers and recipients of other city spending, `at_least_one_decrease` (OC-1, OC-3). |
| A-18 | Animal Services does inspect registry lots and fine some violators. | enforcement | 0.85 | §7 mandates inspection of registry lots. | C-21 to C-24, C-38 shrink; C-36 under U1-b weakens. |
| A-19 | Some buyers of residential lots value the option of keeping hens. | other | 0.6 | Listings that advertise coops. | C-35 loses its (−) chain and becomes increase, Tier C. |
| A-20 | Grocery egg supply cannot expand at an unchanged cost for this added demand. | durability | 0.35 | The added demand (roughly 2,000 households, two dozen a week) is small against regional supply. | Below cut-off; not reported. |
| A-21 | Some chick and coop purchases planned for later in 2027 are moved before enactment. | other | 0.6 | Chicks are sold mainly in spring; some households planned summer coops. | C-4's (+) chain fails; C-4 becomes decrease. |
| A-22 | A regional egg shortage occurs within the horizon. | other | 0.3 | Frequency of past shortages. | Below cut-off; the food-security chain (section 8) is a conditional possibility. |
| A-23 | Keepers who continue illegally give neighbors eggs or favors so that they do not complain (CR-1 op 3 for neighbors; CR-5). | other | 0.45 | Egg gifts to neighbors are already common. | Below cut-off; `side_payments` not reported. |
| A-24 | Without the ordinance, some households would have started keeping hens after May 2027, most registering and buying chicks and coops; with it, they refrain. | other | 0.85 | About 2,500 to 2,800 current flocks; spring chick sales at the feed store. | C-25 fails; C-3 loses prospective keepers; C-24 loses its (−) chain and becomes increase. |
| A-25 | Regional egg supply to grocers and farm stands can expand to meet former keepers' added purchases (RS-1 supply premise). | durability | 0.9 | Grocery eggs come from a regional supply far larger than the added demand; farm flocks expand later (A-28). | C-12 holds only as a shift between buyers; not reported. |
| A-26 | Without the ordinance, city residents would have bought pullets and adult hens in the county market (replacements and new flocks). | other | 0.75 | Pullets and point-of-lay hens are commonly bought from county farms; flocks are replaced every few years. | C-18 rests on RS-13 alone; C-34 becomes increase. |
| A-27 | Some buyers of residential lots value a lower chance of a flock next door. | other | 0.6 | About 120 complaints a year about odor, noise, rodents and setbacks. | C-35 becomes decrease. |
| A-28 | Local small farms can and do add laying hens over a year or more. | alternative_uses | 0.7 | Pullets lay at about five months; Dunmore zoning allows poultry on farms; farm-egg price above grocery price. | C-14 fails. |
| A-29 | Some continuing keepers replace aging hens by buying chicks or pullets outside the city. | other | 0.6 | The Dunmore feed store sells chicks; unregistered keepers are outside the inspection list; hens lay little after two years. | C-29 fails. |
| A-30 | Buyers of keepers' surplus eggs keep eating eggs and buy them elsewhere. | substitutability | 0.85 | Same evidence as A-2. | C-33 fails. |

**Final check (workflow).**
1. *Uncombined chains.* Keepers' money (outlays against eggs bought, and for egg sellers against lost receipts), the announcement window (pull-forward against shorter use), feed sales (U1-a ducks against hens given up), enforcement cost by horizon (C-21, C-38), city receipts (fines against forgone fees, C-24), county hen prices by window (C-18, C-34) and lot values (C-35) were each combined in section 7. Egg-seller volume has no opposing chain that can reverse it.
2. *Group signs.* C-8 (search or waiting) is a group, as CR-6 (0.8) gives for a private supplier that chooses not to charge. C-16 is `number_of_sellers`, not labor, so RS-6's group form for labor is not used.
3. *Baseline.* Every sign is against §6.40, not against the time before §6.40 and not against no enforcement: C-21 and C-38 count the §6.40 complaint work that the ban makes unnecessary (OC-3, 0.8), and C-24 counts the registry fees §6.40 would have collected. C-10 is signed against the counterfactual disposal of spent hens, not against the phase-out.
4. *Worse off is not poorer.* C-20 is the case: keepers who did not sell eggs lose by their own ranking and may have more money (A-16). For egg sellers the lost receipts make it ambiguous (C-37).
5. *Timing shifts.* Hen disposals (C-9, C-10), county hen prices (C-18, C-34) and acquisitions (C-3, C-4) are signed per window.
6. *Both sides of every transfer.* Fines: C-23 (payers) and C-24 (city). Confiscation: CR-8e, noted in section 9. Eggs sold: C-19 records both parties; the sellers' lost receipts enter C-37. Hen and coop sales in the phase-out: C-30 (sellers) and C-18 (buyers). Boarding: C-7. Outlays that keepers no longer make (C-20) are matched by sales that feed stores and coop builders no longer make (C-15, C-16).
7. *Every actor class, every core rule.* CR-7c: coops (C-17), the city feed store (C-32), residential lots (C-35). CR-6: rescues' capacity (C-8), local farm eggs (C-13, C-31), county hens (C-18, C-30, C-34). CR-9: feed, coops, egg sellers, county buyers, egg buyers (C-19, C-33), proximity (C-35, Tier C). Enforcement and its funding: C-21, C-22, C-38.
8. *Unstated premises.* Lobbying's organizing premise is A-9; "some actors at the margin" is in A-4, A-6, A-21, A-24, A-29; RS-1's and RS-16's supply premises are A-25, A-10 and A-20; farms' later expansion is A-28.

## 11. Report

**The policy.** Marrowfield will no longer let households keep chickens on residential lots. Households may keep the birds they have until 11 May 2028, but from 11 May 2027 they may not acquire new ones, and the hen registry is closed. Animal Services enforces the ban with fines of $150 and then $500, and impounds birds after a third violation, from its existing budget. Whether ducks and quail are banned too is unclear (U1). About 2,600 households keep some 12,000 hens; just outside the city, in Dunmore Township, poultry is allowed on larger lots and farms.

**Visible consequences.** Complying households stop producing their own eggs (C-1), and households that would have started a flock cannot (C-25); under the broad reading, duck and quail keepers stop too (C-36). Those households buy their eggs instead (C-2). Every household that kept hens because it wanted to is worse off by its own ranking: it loses the eggs, the hobby, the birds and a hedge against shortages (CR-3a). That loss is certain, but it has no money measure, and the method records only its observable side (section 4).

**Invisible consequences.**
- *Keepers* stop buying chicks and coops once the freeze starts (C-3); in the weeks before it, purchases could go either way (C-4). Coops lose value as soon as the ban is expected (C-17). Hens must all go in the same year, so owners spend time and money disposing of them (C-26), many struggle to find takers near the deadline (C-8), offers of hens bunch in that year and are absent after it (C-9, C-10), and keepers get less for hens and coops (C-30) while county buyers pay less (C-18). Former keepers travel for farm eggs (C-27). Some keepers, mostly those not on the registry, keep birds illegally (C-5); they stop selling eggs openly (C-28) and buy replacement birds outside the city (C-29). Some board hens on Dunmore farms (C-7), and some switch to ducks or quail if those are allowed (C-6, U1-a). Complying keepers who did not sell eggs probably have more money for other things than they would have, because keeping hens cost them more than the eggs they now buy (C-20, A-16, p = 0.55): they are worse off, not poorer. For keepers who sold eggs, the lost receipts make this ambiguous (C-37).
- *Egg buyers and sellers.* Egg sellers sell more eggs (C-12). Local farm eggs cost more for a while (C-13), so their other buyers buy fewer (C-31), until small farms add hens (C-14). Neighbors and coworkers who bought surplus backyard eggs lose that exchange (C-19) and buy eggs elsewhere (C-33).
- *Feed stores and coop builders.* Feed stores sell less poultry feed and supplies (C-15), and the city store loses value from the announcement (C-32). Fewer firms build coops for city residents (C-16).
- *County hen market.* In the phase-out year adult hens and used coops are cheaper (C-18); after it, fewer spent hens are offered but city buyers are gone too, so the price could go either way (C-34).
- *Neighbors* who object to a flock gain a stronger remedy: a complaint now removes the birds (section 6). The relief from odor and noise that the ordinance aims at is out of scope; the method carries it to neighbors only at Tier C (GAP-026-1).
- *Animal Services* spends more on enforcement in the first year (C-21), and, with no new money, responds more slowly to other calls in that year (C-22). Fined households pay the city (C-23).
- *Keepers' associations and feed stores* lobby against passage, then for repeal, grandfathering or the narrow reading of U1 (C-11).

**Ambiguous effects.** Chick and coop purchases between introduction and enactment (C-4). The means of keepers who sold eggs (saved outlays against lost receipts; C-37). Enforcement cost after the first year (fines and reinspections against fewer complaints; C-38). City receipts (fines against the registration fees no longer paid; C-24). County prices of adult hens after the deadline (fewer offered against fewer city buyers; C-34). Residential lot values (the option of keeping hens lost against fewer flocks next door; C-35, Tier C).

**Key conditions.** Compliance by registered keepers (A-1, p = 0.75) drives most effects. That complying non-sellers end up with more money rests on A-16 (p = 0.55), the weakest reported premise. U1 decides whether ducks and quail are a way out.

**What this analysis cannot say.** How large any effect is. Whether the neighbors' gain in amenity outweighs the keepers' loss, or whether either is large, since the method neither measures nor compares people's rankings. Health, animal welfare, noise, odor and other neighborhood amenities, which are out of scope for version 1, including the fate of the roughly 12,000 hens. Whether the ordinance is a good idea.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | households.keepers | home_production (eggs from own hens) | decrease | short–medium | visible | B | CR-1 op 1 (dated), CR-10b, CR-3a | A-1 |
| C-2 | households.keepers | quantity_substitute (eggs bought) | increase | short–medium | visible | B | RS-1, CR-4 | A-1, A-2 |
| C-3 | households.keepers, households.prospective_keepers | investment_target (chicks, pullets, coops; after enactment) | decrease | short | invisible | B | CR-1 op 1, CR-5a, CR-4 | A-1, A-24 |
| C-4 | households.keepers, households.prospective_keepers | investment_target (chicks, pullets, coops; announcement window) | ambiguous | short | invisible | B | RS-8 (Unless), CR-10a, CR-4; CR-12b | A-13, A-21 |
| C-5 | households.keepers (mainly unregistered) | legal_breach (keeping fowl against the ban) | increase | medium | invisible | B | RS-3, CR-1, CR-4 | A-3 |
| C-6 | households.keepers | reclassification (switch from hens to ducks or quail) | U1-a: increase; U1-b: no_change | medium | invisible | B | U1-a: RS-5, CR-4; U1-b: no switch caused | A-4 |
| C-7 | households.keepers | cross_border_purchases (hen boarding in Dunmore) | increase | medium | invisible | B | RS-4, CR-4 | A-6 |
| C-8 | households.keepers (disposing) | search_cost, wait_time | at_least_one_increase | short | invisible | B | CR-10a, CR-6, OC-2 | A-7 |
| C-9 | households.keepers | quantity_supplied (live hens offered; phase-out window) | increase | short | invisible | B | CR-10a | A-1, A-8 |
| C-10 | households.keepers | quantity_supplied (live hens offered; after deadline) | decrease | medium | invisible | B | CR-10a | A-1, A-8 |
| C-11 | households.keepers, input_suppliers.feed | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-9 |
| C-12 | sellers.substitutes | quantity_traded (eggs) | increase | short–medium | invisible | B | CR-9, RS-1, RS-16 | A-1, A-2, A-25 |
| C-13 | buyers of local farm eggs | price_substitute (local farm eggs) | increase | short | invisible | B | RS-16 | A-1, A-10 |
| C-14 | sellers.substitutes (Dunmore egg farms) | investment_target (laying flocks) | increase | medium | invisible | B | CR-9, CR-7a, CR-10b | A-1, A-10, A-28 |
| C-15 | input_suppliers.feed | quantity_complement (poultry feed and supplies) | decrease | short–medium | invisible | B | RS-12 | A-1, A-11 |
| C-16 | coop_builders | number_of_sellers (coops for city residents) | decrease | medium | invisible | B | RS-6, CR-9 | A-1, A-12 |
| C-17 | households.keepers | asset_value (coops and equipment) | decrease | short | invisible | B | CR-7c, CR-10c | A-13 |
| C-18 | buyers.neighboring | price_paid (used coops and adult hens, county; phase-out window) | decrease | short | invisible | B | RS-13; CR-1 op 1, CR-9, CR-6; CR-12a | A-1, A-7, A-14, A-26 |
| C-19 | buyers.backyard_eggs, households.keepers | quantity_traded (surplus backyard eggs sold) | decrease | short–medium | invisible | B | CR-5a, OC-4, CR-9 | A-1, A-15 |
| C-20 | households.keepers (complying, did not sell eggs) | resources_available_other_uses | increase | medium | invisible | B | CR-8a vs CR-4; CR-3 note; CR-12e | A-1, A-16 |
| C-21 | officials.enforcement | enforcement_cost (first year after the deadline) | increase | short | invisible | B | OC-3, CR-8c, CR-12e (arithmetic) | A-18 |
| C-22 | residents served by Animal Services | wait_time (other calls) | increase | short | invisible | B | OC-3, CR-8a | A-17, A-18 |
| C-23 | households.keepers (fined) | resources_available_other_uses | decrease | medium | invisible | B | CR-8b, CR-3 | A-3, A-18 |
| C-24 | city_budget | non_tax_receipts (fines; registration fees) | ambiguous | short–medium | invisible | B | CR-8b, CR-1 op 1, CR-12b | A-3, A-18, A-24 |
| C-25 | households.prospective_keepers | home_production (eggs from own hens) | decrease | short–long | invisible | B | CR-1 op 1, CR-4 | A-24 |
| C-26 | households.keepers (complying) | compliance_cost (rehoming, selling, dismantling) | increase | short | invisible | B | CR-1 op 1, CR-8c, OC-2 | A-1 |
| C-27 | households.keepers (complying) | travel_time (trips for farm and market eggs) | increase | short–medium | invisible | B | CR-4, CR-8c | A-1, A-2, A-10 |
| C-28 | households.keepers (continuing) | quantity_traded (surplus eggs sold) | decrease | medium | invisible | B | CR-4 | A-3, A-15 |
| C-29 | households.keepers (continuing) | cross_border_purchases (chicks and pullets bought outside the city) | increase | medium | invisible | B | CR-1 op 1, RS-4, CR-4 | A-3, A-29 |
| C-30 | households.keepers (complying) | net_price_received (adult hens and used coops; phase-out window) | decrease | short | invisible | B | RS-13, CR-6, CR-7c | A-1, A-14 |
| C-31 | buyers.farm_eggs.other | quantity_traded (farm and market eggs) | decrease | short | invisible | B | CR-4c, CR-8a | A-1, A-2, A-10 |
| C-32 | input_suppliers.feed (city store) | asset_value (store and its poultry line) | decrease | short | invisible | B | CR-7c, CR-10c, CR-7b | A-11, A-13 |
| C-33 | buyers.backyard_eggs | quantity_substitute (eggs bought from grocers and farms) | increase | short–medium | invisible | B | RS-1, CR-4 | A-1, A-15, A-30 |
| C-34 | buyers.neighboring | price_paid (adult hens, county; after deadline) | ambiguous | medium | invisible | B | CR-6, CR-9, CR-1 op 1; CR-12b | A-1, A-8, A-14, A-26 |
| C-35 | owners.residential_lots | asset_value | ambiguous | short | invisible | C | CR-7c, CR-10c, CR-9 (proximity); CR-12b, CR-12d | A-13, A-19, A-27 |
| C-36 | households keeping ducks or quail | home_production (duck and quail eggs) | U1-a: no_change; U1-b: decrease | short–medium | visible | B | CR-1 per reading, CR-4 | A-5, A-18 |
| C-37 | households.keepers (complying, sold eggs) | resources_available_other_uses | ambiguous | medium | invisible | B | CR-8a vs CR-4; CR-5a, CR-3 note; CR-12b | A-1, A-15, A-16 |
| C-38 | officials.enforcement | enforcement_cost (after the first year) | ambiguous | medium–long | invisible | B | OC-3, CR-8c, CR-9; CR-12b | A-1, A-3, A-18 |

## Corrections after the core-only comparison

Changed under catalog 0.8, after checking each comparison row against the core rules:
- **C-20 split; C-37 added.** The `increase` now holds only for keepers who did not sell eggs. For sellers, lost egg receipts (CR-5a) are a second chain that A-16 does not dominate, so C-37 is `ambiguous` (CR-3 note, 0.8; CR-12b).
- **C-21 narrowed; C-38 added; C-22 short.** Under the revised OC-3, enforcement is measured against what §6.40 would have needed. In the first year the increase holds by arithmetic on the case's figures (C-21). After that, fewer flocks to complain about oppose the fines and reinspections, so C-38 is `ambiguous`. C-22 is now short only, because the displacement after the first year follows C-38.
- **C-24.** The variable is now `non_tax_receipts`. The sign is now `ambiguous`, because closing the registry ends the $25 fees new keepers would have paid (A-24) and no premise compares that with the fines.
- **Vocabulary and recording.** C-1 now uses `home_production` and cites CR-3a. C-5 uses `legal_breach`. C-6 is split into keepers' `reclassification` (C-6, with per-reading `no_change`) and duck and quail keepers' `home_production` (C-36). K1 and K2 are now `own_production_ban`. K2 is also classified as triangular, because it prevents purchases of chicks and pullets, which corrects the 0.6 statement that the ordinance "forbids no exchange". C-4 now cites RS-8's *Unless* clause.
- **Hidden premises made explicit.** C-14 now rests on A-28 (farms add flocks later). C-12 now rests on A-25 (the supply premise that RS-1 requires since 0.8).
- **C-18.** It now includes the withdrawal of city buyers from the county market (K2, A-26), which pushes in the same direction.
- **Omissions added:** C-25 (prospective keepers' home production), C-26 (disposal costs), C-27 (travel for farm eggs), C-28 and C-29 (continuing keepers' egg sales and chick purchases outside the city), C-30 (sellers' side of the hen and coop price), C-31 (other farm-egg buyers), C-32 (feed store's asset value), C-33 (buyers of keepers' eggs turning elsewhere), and C-34 (county hen price after the deadline). C-34 is recorded as `ambiguous`, not as the core version's `increase`, because K2 also withdraws city demand.
- **C-35 now reported.** Residential lot values are now reported as `ambiguous`, Tier C. Since 0.7 the `proximity` chain is derivable at Tier C (CR-9), and under CR-12 (0.8, kind 2) a derived opposing chain with p ≥ 0.5 (A-27) gives `ambiguous`.

Comparison conclusions rejected or not applied:
- **Core C-31 (carpentry prices fall): rejected.** It signs a price in a large market from a small supply shift with no premise. The same reasoning was already declined for grocery eggs (A-20).
- **Core C-16 (`wait_time` alone): rejected.** C-8 keeps the group, because CR-6 (0.8) signs a private supplier's rationing margins as a group.
- **Core C-41 (the agency's other work as the class): not applied.** OC-3 places the cost on those whom the displaced work served, so C-22 keeps that class.
- **Core C-28 (Dunmore feed store split): not applied.** It is a J row and a scope choice that 0.8 does not settle.
- **Core C-44 (exempt lots gain value): not applied.** It is an A row resting on a premise (A-N1) that the record does not support and that 0.8 does not settle.
- **C-16 (coop builders as `number_of_sellers`): kept.** The comparison calls the difference minor.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).**
- GAP-026-1 (open). Referred to the experts as Q20 (`06_gaps.md`); catalog 0.7 gives provisional handling: `proximity` relations under CR-9, with chains at Tier C (used in C-35). Effects on neighbors through physical proximity. When keepers stop keeping hens, neighbors' situation changes (less odor and noise; possibly the value of their homes), but they neither buy from nor sell to the keepers. The amenity is out of scope, but the gap is in the calculus, not only the vocabulary: the same link is needed for in-scope variables (`asset_value` of neighboring lots). Any autistic intervention whose stated purpose is a spillover onto neighbors (noise, burning, building height) will meet it. Question for the experts: may chains through proximity be signed at Tier B under stated premises, or is the effect of one person's use of their property on another's outside praxeological analysis?

**(b) Unclear core rules (wording that was hard to apply here).**
- *CR-12 with an underived chain* (closed in 0.7 and 0.8: CR-12's clarifications distinguish an underivable chain, which is a Tier C note, from a derived chain that needs a premise, which gives `ambiguous` at p ≥ 0.5; lot values are now C-35).
- *CR-3 note in the other direction* (closed in 0.8: the CR-3 note now says that lost receipts from selling part of the banned output are combined with the saved outlays under CR-12b; C-20 and C-37).
- *CR-1 on a phased provision* (closed in 0.7: CR-1 operations carry the date they take effect). Still open: CR-7c does not say how to date a capitalization when the asset's yield is cut at two dates (no replacement from 2027, no keeping from 2028); C-17 dates it from announcement.
- *CR-5 and gifts* (closed in 0.7: CR-5's gift clarification and the `gift` relation).
- *CR-12d with an ambiguous sign from a Tier C chain.* C-35 combines a Tier B chain with a Tier C proximity chain. CR-12d gives the lowest tier, so C-35 is Tier C; whether the derived Tier B direction should instead stand with a Tier C note is not said.

**(c) Missing patterns (derived here, likely to recur).**
- *P-026-1 Ban on own production (autistic prohibition).* If: a policy forbids actors to produce a good or keep an asset for their own use, and the good can be bought. Then: (i) producers who chose the activity are worse off by their own ranking (CR-3a), whatever happens to their money, and their `home_production` falls; (ii) purchases of the good rise (CR-4, x: produce, y: buy) and its sellers sell more, given a supply premise (CR-9); (iii) inputs and complements of home production fall (CR-9 with LW-10), and their suppliers' specific assets lose value (CR-7c); (iv) the producers' specific capital loses value at announcement (CR-7c, CR-10c) and is sold across the boundary (RS-13); (v) exchanges and gifts of surplus stop (CR-5a, CR-5 gift clarification); (vi) their `resources_available_other_uses` is `ambiguous` unless a premise compares the outlays of home production with the price of the bought good, and, for those who sold part of the output, also with the lost receipts (CR-8a against CR-4 and CR-5a, CR-12e); (vii) where enforcement depends on a registry, registered and unregistered producers split (CR-1, Recording); (viii) enforcement is measured against the rule replaced (OC-3). Derivation: CR-1 op 1, CR-3a, CR-4, CR-5a, CR-7c, CR-8a, CR-9, CR-12. Recurs for bans on home brewing or distilling, home gardens in front yards, wood stoves, short-term letting of one's own home, and home businesses. Instrument `own_production_ban` was added in 0.7; the pattern remains a candidate.
- *P-026-2 Phase-out of a held stock with a common deadline* (closed in 0.7: RS-8's *Unless* clause). Not covered by that clause: disposals bunch before the deadline and are signed per window (CR-10a, 2.5); takers' capacity is rationed (CR-6), so search or waiting rises (group sign); prices fall in the market that receives the disposals in that window (RS-13) and are `ambiguous` after it where the freeze also withdraws buyers from that market.

**(d) Vocabulary (what the ontology lacks).**
- *Instrument type* (closed in 0.7: `own_production_ban`).
- *Variables.* (1) Production for one's own use (closed in 0.7: `home_production`). (2) No way to record a loss by the actor's own ranking (CR-3a) of an activity valued for itself; C-1 cites CR-3a in its derivation, but the loss is not scored. Proposed: a field on a consequence (for example `own_ranking: worse`). Still open. (3) Keeping banned birds (C-5) is a breach of a rule but not trade or a market activity. `legal_breach` (0.7) is used, but it is defined "within the legal market", so the fit is imperfect. (4) Fines and other non-tax receipts (closed in 0.7: `non_tax_receipts`). (5) No variable for gifts received, for complaints, or for living stock culled or disposed of. Still open.
- *Relation types* (closed in 0.7: `gift`, `proximity`).
- *Actor classes* (closed in 0.7: `neighbors`). No generic class yet for charities and rescues that take goods without charge.
- *Signs* (closed in 0.7: `no_change`, used in C-6 and C-36).
