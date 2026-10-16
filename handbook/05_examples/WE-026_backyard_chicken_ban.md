# WE-026 Ban on keeping chickens on residential lots, with a 12-month phase-out

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

A stylized policy in a fictional city. It is a gap-probing example: it was chosen because it is an *autistic* intervention (01_foundations.md, intervention typology), which restricts what people do with their own means and coerces no exchange, and none of WE-001 to WE-025 is of that type. The analysis therefore tests CR-1 operation 1 applied to own production, the recording of a loss that has no money counterpart, a phase-out with a common deadline, and effects on neighbors who are linked to the restricted households by place rather than by exchange. Health, animal welfare, noise, odor and other neighborhood amenities are out of scope for version 1 and are not analyzed; where they would enter a chain, this is said. The probabilities are illustrative; the evidence column says what a real analysis would cite.

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
| K1 Keeping ban | `prohibition` (of keeping fowl on one's own lot; see section 2) | Keeping "domestic fowl" on residential lots | All households on residential lots | From 11 May 2028, no fowl may be kept. | Lots zoned agricultural (about 40 lots on the city's edge); school educational programs registered with the district (up to three birds, on school grounds). |
| K2 Acquisition freeze and phase-out | `prohibition` | Acquiring or hatching fowl; registration | Same | From 11 May 2027, no new birds may be acquired or hatched; birds kept on that date may be kept until 11 May 2028. The registry is closed to new entries and becomes the inspection list. | Same as K1. |
| K3 Enforcement | Enforcement | K1, K2 | Animal Services | Fines, reinspection, impoundment (above). No new appropriation. | None |

Unclear provisions:
- **U1.** Which birds are banned. The definitions section defines "fowl" as "chickens, ducks, geese, turkeys, guinea fowl and quail", but the title and preamble speak of "backyard chickens", and the enforcement section refers only to "hens". Reading U1-a: only chickens are banned. Reading U1-b: all listed fowl are banned. About 60 registered households keep ducks or quail, alone or with hens. Readings get no probability; where a sign depends on U1, one sign per reading is given.

The counterfactual law is §6.40: keeping up to six hens with registration, with complaints leading to orders to fix setbacks and sanitation.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Autistic: forbids households to produce eggs (and keep birds) on their own lots. No exchange is forced or forbidden directly; exchanges that depended on the activity (selling or giving surplus eggs, buying feed and coops) stop as a consequence (CR-9). | Yes: about 2,600 households keep hens (A-1 for compliance). | No family covers an autistic ban (2.3 lists `prohibition` only as triangular); derived from CR-1 op 1, CR-3, CR-4, CR-9. RS, OC, EN-7 does not apply (no trade is prohibited). |
| K2 | Autistic, as K1, with an earlier date for acquisition | Yes | RS-8 is checked and found not to apply as worded (section 8); CR-10a. |
| K3 | Binary: fines are forced payments to the city; impoundment is a confiscation (CR-8e). Funded from a fixed budget (OC-3, second funding case, A-17). | Yes, where enforced (A-3, A-18) | OC-3, CR-8 |

**CR-1 operations by actor class.** The counterfactual law is §6.40.

| Actor class | Operations |
|---|---|
| `households.keepers.registered` | Op 1: keeping hens removed (from 11 May 2028), acquiring birds removed (from 11 May 2027). Their lots are on the inspection list, so the removal is enforced. |
| `households.keepers.unregistered` | Op 3 rather than op 1: not on the list, so for them the ban attaches a risk (a fine, if a neighbor complains) to keeping hens (CR-1, Premises). |
| `households.prospective_keepers` | Op 1: starting a flock removed. |
| `neighbors.of_keepers` | Op 2: a complaint now establishes a violation by the birds' presence, a stronger remedy than a setback order (an added option). Op 1 as well, since they too can no longer keep hens. |
| Households keeping ducks or quail | U1-a: no operation. U1-b: op 1, as for hen keepers. |
| Agricultural lots, school programs | None (exempt). |
| `officials.enforcement` | A new duty without new funds (op 3 on their other work, through the fixed budget). |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `households.keepers` (registered and unregistered) | About 2,600 households keeping hens | Must give up their flocks by the deadline and cannot replace birds in the meantime; may comply, keep birds illegally, switch to ducks or quail (U1-a), or board hens outside the city. |
| `households.prospective_keepers` | Households that would have started a flock | Cannot start one. |
| `neighbors.of_keepers` | Households next to a flock | Can have the flock removed by complaining; can no longer keep hens themselves. |
| `buyers.backyard_eggs` | Neighbors, coworkers and friends who bought or were given surplus eggs | Lose that source. |
| `sellers.substitutes` | Grocers, farmers-market vendors, Dunmore farm stands and small egg farms | More egg buyers. |
| `input_suppliers.feed` | The two feed stores, and chick sellers | Fewer customers for poultry feed, bedding, chicks. |
| `coop_builders` | About six small carpentry firms and the feed store's coop line | Less demand for coops. |
| `buyers.neighboring` | Dunmore and county households and farms that buy used coops and adult hens | More used coops and hens offered. |
| `hen_boarding_services` | Dunmore farms that could board hens for city households | A new service is in demand. |
| `officials.enforcement`, residents served by Animal Services | Animal Services and those who rely on its other work | A new task from a fixed budget. |
| `city_budget` | Receives fines | Fine receipts. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `households.keepers` | `capital_stock_target` (flocks and coops in use for home egg production in the city) | decrease | short to medium | CR-1 op 1, CR-10b (the stock runs down through the phase-out and reaches near zero for complying households at the deadline) | A-1 |
| C-2 | `households.keepers` | `quantity_substitute` (eggs bought, from all sellers) | increase | short to medium | RS-1; CR-4 (x: home eggs, y: bought eggs) | A-1, A-2 |

The visible effect is that backyard flocks disappear from residential lots. The supporters' stated aim (fewer complaints about odor, noise and rodents) is an amenity effect, which is out of scope for version 1 and which no core rule carries to the neighbors (GAP-026-1, section 6).

**A loss with no variable.** By CR-3a, every household that chose to keep hens is worse off by its own ranking once that option is removed, whatever happens to its money spending: the eggs, the hobby, the birds as pets, a children's chore, and a hedge against egg shortages were ends it ranked above its alternatives. This conclusion is Tier A (it needs only that the option was chosen and that the ban is enforced against it), and it is the most certain claim in this analysis. But 2.5 requires every consequence to be a signed change in a controlled variable, and no variable records the loss of an activity valued for itself. It is therefore stated here and in the report, and not in the consequence list (Gaps found, (d)). C-1 and C-2 record what can be observed: the stock of flocks falls, and egg purchases rise.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `households.keepers`, `households.prospective_keepers` | `investment_target` (chicks, pullets and new coops bought by city residents; window: after enactment) | decrease | short | CR-1 op 1 (K2: acquiring is barred from 11 May 2027), CR-4 | A-1 |
| C-4 | `households.keepers`, `households.prospective_keepers` | `investment_target` (chicks, pullets and new coops bought by city residents; window: announcement to enactment, 2 March to 11 May 2027) | ambiguous | short | CR-10a with CR-4: purchases planned for later in 2027 are pulled forward before the freeze (+); the expected period over which a new bird or coop can be used falls from years to at most 14 months, so fewer are bought (−); CR-12b | A-13, A-21 |
| C-5 | `households.keepers` (mainly unregistered) | `informal_activity` (keeping fowl after the deadline, against the ban) | increase | medium | RS-3; CR-1 (for households not on the registry the ban attaches a risk rather than removing the option); CR-4 (x: comply, y: keep birds) | A-3 |
| C-6 | `households.keepers` and households keeping ducks or quail | `quantity_substitute` (ducks or quail kept for eggs) | U1-a: increase; U1-b: decrease | medium | U1-a: RS-5 (ducks and quail are the uncovered form); U1-b: CR-1 op 1 applied to existing duck and quail keepers | A-4, A-5 |
| C-7 | `households.keepers` | `cross_border_purchases` (hen boarding or hen shares on Dunmore farms) | increase | medium | RS-4; CR-4 (x: keep hens here, y: keep them there) | A-6 |
| C-8 | `households.keepers` disposing of hens | `search_cost`, `wait_time` (finding a taker for the birds; rescue waiting lists) | at_least_one_increase | short | CR-10a (disposals bunch before the deadline, C-9), CR-6 (takers' capacity is limited, so the scarce side chooses), OC-2 | A-7 |
| C-9 | `households.keepers` | `quantity_supplied` (live hens offered for rehoming or sale; window: phase-out, May 2027 to May 2028) | increase | short | CR-10a, 2.5 timing shift: all hens must go within the window | A-1, A-8 |
| C-10 | `households.keepers` | `quantity_supplied` (live hens offered for rehoming or sale; window: after the deadline) | decrease | medium | CR-10a, 2.5 timing shift: in the counterfactual some spent hens would have been offered in these years; with the ban, there are none left to offer | A-1, A-8 |
| C-11 | `households.keepers`, `input_suppliers.feed` | `lobbying_effort` (for repeal, grandfathering of existing flocks, or reading U1-a) | increase | medium | RS-7 | A-9 |

C-3 and C-4 are the same activity in two windows. K2 bars acquisition from enactment, so after it purchases fall (C-3). In the ten weeks between introduction and enactment, which fall in the spring chick season, two chains conflict (C-4): RS-8's "rush before the rule" applies to purchases that some households had planned for later in 2027 and bring forward, but the ban has no grandfathering, so every bird must go by May 2028 whenever it was bought. A chick bought in March 2027 starts laying in late summer and can be kept for only about eight months of laying, rather than several years. The expected yield of a new bird or coop falls, and by CR-4 fewer are bought. CR-12b gives `ambiguous`.

C-5: complaint-driven enforcement with no list of unregistered keepers leaves keeping hens open to those who are not on the registry, at the risk of a fine if a neighbor complains. Registered keepers face inspection and are expected mostly to comply (A-1); the split follows CR-1's instruction to divide a class where the operation differs.

C-6: under U1-a, ducks and quail are outside the ban, and some keepers switch to them for eggs (RS-5). Under U1-b, households that already keep ducks or quail must give them up too.

C-9 and C-10 are a timing shift (02_ontology.md, 2.5): hens are given up with and without the ban, but at different times. With the ban, every hen still alive at the deadline must go during the phase-out, and households that want eggs as long as possible keep their hens until close to the deadline, so the offers bunch in the last months (A-7, C-8). In the years after, nothing is left to give up.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `sellers.substitutes` (grocers, market vendors, farm stands) | `quantity_traded` (eggs) | increase | short to medium | CR-9 (buyers turn to them), RS-16 (quantity) | home eggs and bought eggs: `substitute`, close | A-1, A-2 |
| C-13 | buyers of local farm eggs (market and farm-stand customers, including former keepers) | `price_substitute` (eggs from local small farms) | increase | short | RS-16 | home eggs and local farm eggs: `substitute`, close | A-1, A-10 |
| C-14 | `sellers.substitutes` (small egg farms in Dunmore) | `investment_target` (laying flocks) | increase | medium | CR-9, CR-7 (yield on local egg production rises with C-13) | as C-13 | A-1, A-10 |
| C-15 | `input_suppliers.feed` | `quantity_complement` (poultry feed, bedding and supplies sold to city residents) | decrease | short to medium | RS-12 | feed and hens: `complement`, close | A-1, A-11 |
| C-16 | `coop_builders` | `number_of_sellers` (firms building coops for city residents) | decrease | medium | RS-6, CR-9 | coops and hens: `complement`, close | A-1, A-12 |
| C-17 | `households.keepers` | `asset_value` (coops and equipment) | decrease | short | CR-7c, CR-10c (the coop's yield in the city ends at the deadline, so its value falls to what it fetches outside the city, net of moving it, from the time the ban becomes expected) | coops and hens: `complement`, close | A-13 |
| C-18 | `buyers.neighboring` | `price_paid` (used coops and adult laying hens in the county) | decrease | short | RS-13 (city supply is added to the county's used market) | city and county used markets: `across_border`, close | A-1, A-7, A-14 |
| C-19 | `buyers.backyard_eggs`, `households.keepers` | `quantity_traded` (surplus backyard eggs sold to neighbors and coworkers) | decrease | short to medium | CR-5a, OC-4 (both parties lose an exchange each expected to gain from); CR-9 | direct exchange between keepers and their buyers (CR-5a; no 2.8 relation needed) | A-1, A-15 |
| C-20 | `households.keepers` (complying) | `resources_available_other_uses` | increase | medium | CR-8a (feed, bedding and vet outlays stop) against CR-4 (eggs now bought); CR-12e dominance by A-16 | — | A-1, A-16 |

**C-20 and the final check, item 4.** Households lose by their own ranking (section 4), yet those that comply may have more money for other things, not less. CR-3's note says when `resources_available_other_uses` falls; here it rises if what a household spent each month on keeping hens (feed alone is about $1.85 per dozen eggs from a young hen, and more from older ones, plus bedding, grit, vet bills and losses to predators) is more than what it now spends on eggs. Many flocks include older hens that lay little, which raises outlays per dozen. A-16 (p = 0.55) is the dominance premise; it is weakest for households that bought farm-stand eggs at $6, and for food-oriented keepers who fed kitchen scraps.

**C-19.** Some exchanges are prevented, although the ordinance forbids no exchange: the surplus eggs that keepers sold to neighbors under the state small-flock rule are no longer produced. CR-5a applies to the exchange that would have taken place. Eggs that were *given* rather than sold are not covered by CR-5, and CR-9 reaches a gift's recipient only through a relation in 2.8, which has no type for gifts. Gifts are therefore described here but not recorded (Gaps found, (b) and (d)).

**Neighbors (GAP-026-1).** The ordinance's purpose concerns neighbors: about 120 complaints a year about odor, noise and rodents. Two chains reach them.
- *Derivable:* CR-1 op 2. A complaint now removes a flock instead of producing a setback order. Neighbors who object to a flock gain an option (CR-3b), and they can use it against the households that keep hens illegally (C-5). This is a gain by their own ranking; it has no variable other than the enforcement work it creates (C-21).
- *Not derivable:* the amenity itself, that a neighbor's yard is quieter and smells less once the flock is gone, and any gain in the value of neighbors' homes from it. The change travels from the keeper's action to the neighbor through physical proximity, not exchange. CR-9 says propagation "follows exchange relations only", and no other core rule says how one actor's change in their own production changes the situation of someone who neither buys from nor sells to them. The amenity is also out of scope (2.4). This step is `GAP-026-1`.

**Residential lot values: not reported.** Two chains reach `asset_value` of residential lots. One is derivable: every residential lot loses an option that some buyers value (keeping hens), so by CR-7c its value can only fall from that chain, given that some buyers value the option (A-19, p = 0.6). The other, a gain in value for lots next to a flock that now leaves, rests on GAP-026-1 and cannot be derived. Reporting `decrease` would ignore a chain known to push the other way; reporting `ambiguous` would combine with a chain that is not derived. CR-12 does not say how to combine a derived chain with an opposing chain that has no derivation, so the consequence is not reported (Gaps found, (b)).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `households.keepers`, `resources_available_other_uses`, medium | Outlays on keeping stop (CR-8a). | Eggs now bought (C-2). Fines, for those who keep birds and are caught (C-23; recorded as their own class). | A-16: outlays exceed the cost of eggs bought, for most keepers (CR-12e, empirical premise). | **increase** (C-20), for complying households. |
| `households.keepers`, `investment_target`, announcement window | Purchases pulled forward before the freeze (A-21). | Shorter expected period of use without grandfathering (A-13). | None | **ambiguous** (C-4). |
| `input_suppliers.feed`, `quantity_complement`, short to medium | Under U1-a, duck and quail keepers still buy feed (C-6). | Hens given up (C-1). | Not needed: under U1-a the switch is partial, so fewer birds are fed in total (A-1). | **decrease** (C-15) under both readings. |
| `sellers.substitutes`, `quantity_traded`, short to medium | Former keepers buy eggs (C-2). | None: keepers who keep birds illegally (C-5) buy fewer than the complying ones, but no fewer than without the ban. | — | **increase** (C-12). |
| Residential lots, `asset_value` | Lots next to a flock lose a nuisance (GAP-026-1, not derived). | Every lot loses the option of keeping hens (CR-7c, A-19). | — | **Not reported** (section 6). |
| Price of grocery eggs, short | Former keepers' added demand (RS-16). | — | — | Not reported: A-20 (p = 0.35), that grocery egg supply cannot expand at an unchanged cost for so small a demand, is below the cut-off. |

## 8. Time structure

Three windows matter.
- **Announcement to enactment (2 March to 11 May 2027).** The chick season. Purchases of chicks and coops are `ambiguous` against the counterfactual (C-4). The value of existing coops falls from when passage becomes likely (C-17, CR-7c); with five of nine sponsors, that is from introduction (A-13). RS-8 as worded ("rush before a tax or cap takes effect") suggests a rush, but the ban has no grandfathering, so the core rules give an ambiguous sign instead (Gaps found, (c), P-026-2).
- **Phase-out (11 May 2027 to 11 May 2028).** No replacements. Flocks shrink as hens die or are culled, and laying falls as they age, so home egg output declines through the year, and egg purchases rise gradually (C-2) and then jump at the deadline. Disposals bunch in the last months (C-8, C-9), which lowers the county prices of used coops and adult hens in that period (C-18). Feed sales fall gradually, then sharply (C-15).
- **After the deadline.** Inspections of registered lots, complaints and fines (C-21 to C-24). Illegal keeping (C-5) concentrates among unregistered households and those whose neighbors do not object. Small local egg farms add laying flocks over about a year (C-14), which reduces the price rise of C-13. Coop building for the city ends (C-16), and no spent hens are offered (C-10).

**Food security.** Some households keep hens as a hedge against egg shortages. The ban removes that hedge: in a shortage, these households would now buy in the market and add to demand. Whether a shortage occurs in the horizon is A-22 (p = 0.3), so the chain is a conditional possibility, not a consequence. The hedge itself is part of the loss by own ranking in section 4, and has no variable.

**Expectations.** If the council is expected to adopt reading U1-a in practice, or to grandfather existing flocks after lobbying (C-11), keepers delay disposal past the deadline, which C-5 partly captures.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-21 | `officials.enforcement` | `enforcement_cost` | increase | Officers' time on inspections of registry lots, complaints and reinspections. | OC-3, CR-8c |
| C-22 | residents served by Animal Services | `wait_time` (responses to other calls: stray dogs, wildlife, cruelty reports) | increase | With no new appropriation, the time spent on fowl comes out of other work (OC-3, second funding case; CR-8a). | OC-3, CR-8a |
| C-23 | `households.keepers` fined for keeping birds | `resources_available_other_uses` | decrease | What the fined households would have bought with the fine. A fine is a sum they cannot avoid once caught (CR-3 note). | CR-8b, CR-3 |
| C-24 | `city_budget` | `tax_revenue` (fine receipts) | increase | The receipt side of C-23 (CR-8b). Fines are not taxes; the controlled list has no variable for other receipts of the state (Gaps found, (d)). | CR-8b |

Impoundment (K3) is a confiscation (CR-8e). Birds transferred to a rescue are a transfer to the rescue; birds euthanized are means used up (CR-8e, last sentence). It is not recorded separately: its value is small, and it concerns the same households as C-23.

The time households spent on their flocks (about 15 minutes a day) is freed. It goes to other uses, but which ones the core rules do not say (CR-4, "a change in means alone"; 06_gaps.md, Q19), so no consequence is recorded.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most keepers give up their hens by the deadline (registered keepers know their lots will be inspected; fines rise on reinspection). | enforcement | 0.75 | §7 inspection of registry lots; the size of the fines against the value of a small flock. | C-1, C-2, C-3, C-9, C-10, C-12 to C-16, C-18 to C-20 shrink to the complying share. |
| A-2 | Households that gave up hens keep eating eggs and buy them. | substitutability | 0.9 | Egg consumption is common in keeper households (registration survey). | C-2, C-12 fail. |
| A-3 | Enforcement leaves some keepers able to continue: complaints are the only route to unregistered keepers, and many neighbors do not complain. | enforcement | 0.7 | 600 to 900 unregistered flocks; about 120 complaints a year. | C-5 fails. |
| A-4 | Under U1-a, some keepers regard ducks or quail as an acceptable source of eggs. | substitutability | 0.55 | Duck and quail eggs are used for cooking; ducks need water and are louder. | C-6 under U1-a fails. |
| A-5 | Some households keep ducks or quail now. | other | 0.9 | About 60 registered households. | C-6 under U1-b fails. |
| A-6 | Some Dunmore farms offer to board hens for city households, and some keepers take it up. | mobility | 0.55 | Farms 5 to 15 km away; hen-boarding is a known arrangement, but none is offered locally yet. | C-7 fails. |
| A-7 | Many keepers delay giving up hens until near the deadline, and regional rescues and small farms can take only limited numbers in a short period. | other | 0.65 | Two small poultry rescues in the county; about 12,000 hens. | C-8 fails; C-18 weakens. |
| A-8 | Without the ban, keepers would have sold or rehomed some spent hens in the years after May 2028. | other | 0.8 | Rehoming listings for hens in the county each year. | C-10 fails. |
| A-9 | The Marrowfield Backyard Poultry Club (about 300 members) and the feed stores can organize to lobby at a cost below their stake. | other | 0.7 | An existing club with a mailing list; the feed store's poultry sales. | C-11 not reported. |
| A-10 | A material share of former keepers buy from local small farms, whose laying flocks cannot expand within months. | durability | 0.55 | Keepers' stated preference for farm-fresh eggs; pullets take about five months to lay. | C-13, C-14 fail. |
| A-11 | Poultry feed and supplies have few uses other than keeping birds. | substitutability | 0.9 | Product lines. | C-15 weakens. |
| A-12 | Coop builders have other carpentry work to move to. | alternative_uses | 0.85 | Coops are a side line for the six firms. | C-16: firms stay but idle. |
| A-13 | From introduction, residents expected the ordinance to pass. | expectations | 0.8 | Five of nine council members as sponsors. | C-17's timing moves to enactment; C-4's (−) chain starts later. |
| A-14 | The county's market for used coops and adult hens is thin, so added offers lower prices. | other | 0.75 | Few listings in a normal month. | C-18 fails. |
| A-15 | Some keepers sold surplus eggs to neighbors and coworkers. | other | 0.8 | State small-flock rule; listings and signs. | C-19 fails. |
| A-16 | For most complying keepers, monthly outlays on keeping hens exceeded what they now spend on eggs. | other | 0.55 | Feed about $1.85 per dozen from young hens and more from older ones, plus bedding, vet and losses; grocery eggs $3.20, farm eggs $6. | C-20 becomes ambiguous. |
| A-17 | Enforcement is funded within existing appropriations, and the budget is not raised. | revenue_use | 0.7 | §8 "within existing appropriations". | C-22 fails; OC-1 applies to taxpayers instead. |
| A-18 | Animal Services does inspect registry lots and fine some violators. | enforcement | 0.85 | §7 mandates inspection of registry lots. | C-21 to C-24 shrink. |
| A-19 | Some buyers of residential lots value the option of keeping hens. | other | 0.6 | Listings that advertise coops. | Only enters a consequence not reported (section 6). |
| A-20 | Grocery egg supply cannot expand at an unchanged cost for this added demand. | durability | 0.35 | The added demand (roughly 2,000 households, two dozen a week) is small against regional supply. | Below cut-off; not reported. |
| A-21 | Some chick and coop purchases planned for later in 2027 are moved before enactment. | other | 0.6 | Chicks are sold mainly in spring; some households planned summer coops. | C-4's (+) chain fails; C-4 becomes decrease. |
| A-22 | A regional egg shortage occurs within the horizon. | other | 0.3 | Frequency of past shortages. | Below cut-off; the food-security chain (section 8) is a conditional possibility. |
| A-23 | Keepers who continue illegally give neighbors eggs or favors so that they do not complain (CR-1 op 2 for neighbors; CR-5). | other | 0.45 | Egg gifts to neighbors are already common. | Below cut-off; `side_payments` not reported. |

**Final check (workflow).**
1. *Uncombined chains.* Feed sales (U1-a ducks against hens given up), keepers' money (outlays against eggs bought), the announcement window (pull-forward against shorter use) and lot values were each combined in section 7. Egg-seller volume has no opposing chain.
2. *Group signs.* C-8 (search or waiting) is a group. C-16 is `number_of_sellers`, not `employment`, so RS-6's group form for labor is not needed.
3. *Baseline.* Every sign is against §6.40, not against the time before §6.40. C-10 is signed against the counterfactual disposal of spent hens, not against the phase-out.
4. *Worse off is not poorer.* C-20 is the case: keepers lose by their own ranking and may have more money. It rests on A-16.
5. *Timing shifts.* Hen disposals (C-9, C-10) and acquisitions (C-3, C-4) are signed per window.
6. *Both sides of every transfer.* Fines: C-23 (payers) and C-24 (city). Confiscation: CR-8e, noted in section 9. Eggs sold: C-19 records both parties. Outlays that keepers no longer make (C-20) are matched by sales that feed stores and coop builders no longer make (C-15, C-16).
7. *Every actor class, every core rule.* CR-7c: coops (C-17) and lots (not reported). CR-6: rescues' capacity (C-8), local farm eggs (C-13). CR-9: feed, coops, egg sellers, county buyers, egg buyers. Enforcement and its funding: C-21, C-22.
8. *Unstated premises.* Lobbying's organizing premise is A-9; "some actors at the margin" is in A-4, A-6, A-21; RS-16's supply premise is A-10 and A-20.

## 11. Report

**The policy.** Marrowfield will no longer let households keep chickens on residential lots. Households may keep the birds they have until 11 May 2028, but from 11 May 2027 they may not acquire new ones. Animal Services enforces the ban with fines of $150 and then $500, and impounds birds after a third violation, from its existing budget. Whether ducks and quail are banned too is unclear (U1). About 2,600 households keep some 12,000 hens; just outside the city, in Dunmore Township, poultry is allowed on larger lots and farms.

**Visible consequences.** Backyard flocks disappear from complying households (C-1), and those households buy their eggs instead (C-2). Every household that kept hens because it wanted to is worse off by its own ranking: it loses the eggs, the hobby, the birds and a hedge against shortages (CR-3a). That loss is certain, but it has no money measure, and this method has no variable for it (section 4).

**Invisible consequences.**
- *Keepers* stop buying chicks and coops once the freeze starts (C-3); in the weeks before it, purchases could go either way (C-4). Coops lose value as soon as the ban is expected (C-17). Hens must all go in the same year, so many owners struggle to find takers near the deadline (C-8), offers of hens bunch in that year and are absent after it (C-9, C-10), and county buyers of used coops and hens pay less (C-18). Some keepers, mostly those not on the registry, keep birds illegally (C-5); some board hens on Dunmore farms (C-7); and some switch to ducks or quail if those are allowed (C-6, U1-a), or must give those up too (U1-b). Keepers who comply probably have more money for other things than they would have, because keeping hens cost them more than the eggs they now buy (C-20, A-16, p = 0.55): they are worse off, not poorer.
- *Egg sellers* sell more eggs (C-12). Local farm eggs cost more for a while (C-13), until small farms add hens (C-14). Neighbors and coworkers who bought surplus backyard eggs lose that exchange (C-19).
- *Feed stores* sell less poultry feed and supplies (C-15), and fewer firms build coops for city residents (C-16).
- *Neighbors* who object to a flock gain a stronger remedy: a complaint now removes the birds (section 6). The relief from odor and noise that the ordinance aims at is out of scope, and the method cannot carry it to neighbors at all (GAP-026-1).
- *Animal Services* spends time on the ban (C-21), and, with no new money, responds more slowly to other calls (C-22). Fined households pay the city (C-23, C-24).
- *Keepers' associations and feed stores* lobby for repeal, grandfathering or the narrow reading of U1 (C-11).

**Ambiguous effects.** Whether chick and coop purchases rose or fell between introduction and enactment (C-4). Whether residential lot values rise or fall is not reported: one chain lowers them, and the opposing chain cannot be derived (section 6).

**Key conditions.** Compliance by registered keepers (A-1, p = 0.75) drives most effects. That complying keepers end up with more money rests on A-16 (p = 0.55), the weakest reported premise. U1 decides whether ducks and quail are a way out.

**What this analysis cannot say.** How large any effect is. Whether the neighbors' gain in amenity outweighs the keepers' loss, or whether either is large, since the method neither measures nor compares people's rankings and has no variable for either. Health, animal welfare, noise, odor and other neighborhood amenities, which are out of scope for version 1. Whether the ordinance is a good idea.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | households.keepers | capital_stock_target (flocks and coops, home egg production) | decrease | short–medium | visible | B | CR-1 op 1, CR-10b | A-1 |
| C-2 | households.keepers | quantity_substitute (eggs bought) | increase | short–medium | visible | B | RS-1, CR-4 | A-1, A-2 |
| C-3 | households.keepers, households.prospective_keepers | investment_target (chicks, pullets, coops; after enactment) | decrease | short | invisible | B | CR-1 op 1, CR-4 | A-1 |
| C-4 | households.keepers, households.prospective_keepers | investment_target (chicks, pullets, coops; announcement window) | ambiguous | short | invisible | B | CR-10a, CR-4; CR-12b | A-13, A-21 |
| C-5 | households.keepers (mainly unregistered) | informal_activity (keeping fowl against the ban) | increase | medium | invisible | B | RS-3, CR-1, CR-4 | A-3 |
| C-6 | households.keepers, duck and quail keepers | quantity_substitute (ducks or quail kept) | U1-a: increase; U1-b: decrease | medium | invisible | B | U1-a: RS-5; U1-b: CR-1 op 1 | A-4, A-5 |
| C-7 | households.keepers | cross_border_purchases (hen boarding in Dunmore) | increase | medium | invisible | B | RS-4, CR-4 | A-6 |
| C-8 | households.keepers (disposing) | search_cost, wait_time | at_least_one_increase | short | invisible | B | CR-10a, CR-6, OC-2 | A-7 |
| C-9 | households.keepers | quantity_supplied (live hens offered; phase-out window) | increase | short | invisible | B | CR-10a | A-1, A-8 |
| C-10 | households.keepers | quantity_supplied (live hens offered; after deadline) | decrease | medium | invisible | B | CR-10a | A-1, A-8 |
| C-11 | households.keepers, input_suppliers.feed | lobbying_effort | increase | medium | invisible | B | RS-7 | A-9 |
| C-12 | sellers.substitutes | quantity_traded (eggs) | increase | short–medium | invisible | B | CR-9, RS-16 | A-1, A-2 |
| C-13 | buyers of local farm eggs | price_substitute (local farm eggs) | increase | short | invisible | B | RS-16 | A-1, A-10 |
| C-14 | sellers.substitutes (Dunmore egg farms) | investment_target (laying flocks) | increase | medium | invisible | B | CR-9, CR-7 | A-1, A-10 |
| C-15 | input_suppliers.feed | quantity_complement (poultry feed and supplies) | decrease | short–medium | invisible | B | RS-12 | A-1, A-11 |
| C-16 | coop_builders | number_of_sellers (coops for city residents) | decrease | medium | invisible | B | RS-6, CR-9 | A-1, A-12 |
| C-17 | households.keepers | asset_value (coops and equipment) | decrease | short | invisible | B | CR-7c, CR-10c | A-13 |
| C-18 | buyers.neighboring | price_paid (used coops and adult hens, county) | decrease | short | invisible | B | RS-13 | A-1, A-7, A-14 |
| C-19 | buyers.backyard_eggs, households.keepers | quantity_traded (surplus backyard eggs sold) | decrease | short–medium | invisible | B | CR-5a, OC-4, CR-9 | A-1, A-15 |
| C-20 | households.keepers (complying) | resources_available_other_uses | increase | medium | invisible | B | CR-8a vs CR-4; CR-12e | A-1, A-16 |
| C-21 | officials.enforcement | enforcement_cost | increase | short–medium | invisible | B | OC-3, CR-8c | A-18 |
| C-22 | residents served by Animal Services | wait_time (other calls) | increase | medium | invisible | B | OC-3, CR-8a | A-17, A-18 |
| C-23 | households.keepers (fined) | resources_available_other_uses | decrease | medium | invisible | B | CR-8b, CR-3 | A-3, A-18 |
| C-24 | city_budget | tax_revenue (fine receipts) | increase | medium | invisible | B | CR-8b | A-3, A-18 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).**
- GAP-026-1 (open). Referred to the experts as Q20 (`06_gaps.md`); catalog 0.7 gives provisional handling. Effects on neighbors through physical proximity. When keepers stop keeping hens, neighbors' situation changes (less odor and noise; possibly the value of their homes), but they neither buy from nor sell to the keepers. CR-9 limits propagation to exchange relations, and no other core rule carries a change in one actor's own production to a non-trading third party. The amenity is also out of scope, but the gap is in the calculus, not only the vocabulary: the same link is needed for in-scope variables (`asset_value` of neighboring lots). Any autistic intervention whose stated purpose is a spillover onto neighbors (noise, burning, building height) will meet it. Question for the experts: should CR-9 admit a non-exchange relation (proximity) with a premise, or is the effect of one person's use of their property on another's outside praxeological analysis?

**(b) Unclear core rules (wording that was hard to apply here).**
- *CR-12 with an underived chain.* Residential lot values have one derived chain (CR-7c, −) and one opposing chain that rests on GAP-026-1. CR-12b combines derived chains; it does not say whether a known but underived opposing chain makes the sign `ambiguous`, is ignored, or blocks reporting. This analysis chose not to report. A rule is needed.
- *CR-3 note and final check, item 4, in the other direction.* The note says when `resources_available_other_uses` falls for a class that is made worse off. It says nothing about when it rises, which is the usual case when an activity that cost money is banned. C-20 applied CR-8a with a dominance premise (CR-12e). The note could say both directions.
- *CR-1 on a phased provision.* K2 removes one option (acquiring) at enactment and another (keeping) a year later. CR-1 has no time index on its operations, and "record every operation that applies" does not say whether to record them per date. They were split into two components (K1, K2).
- *CR-5 and gifts.* CR-5a covers exchanges prevented; gifts of surplus eggs, which are not exchanges, are prevented too. CR-2 covers the giver; the recipient is reached only through CR-9, whose relations have no gift type. Whether a gift is an exchange for CR-5's purposes (the giver ranks the gift above keeping the eggs) is not said.

**(c) Missing patterns (derived here, likely to recur).**
- *P-026-1 Ban on own production (autistic prohibition).* If: a policy forbids actors to produce a good or keep an asset for their own use, and the good can be bought. Then: (i) producers who chose the activity are worse off by their own ranking (CR-3a), whatever happens to their money; (ii) purchases of the good rise (CR-4, x: produce, y: buy) and its sellers sell more (CR-9); (iii) inputs and complements of home production fall (CR-9 with LW-10); (iv) the producers' specific capital loses value at announcement (CR-7c, CR-10c) and is sold across the boundary (RS-13); (v) exchanges and gifts of surplus stop (CR-5a); (vi) their `resources_available_other_uses` is `ambiguous` unless a premise compares the outlays of home production with the price of the bought good (CR-8a against CR-4, CR-12e); (vii) where enforcement depends on a registry, registered and unregistered producers split (CR-1, Recording). Derivation: CR-1 op 1, CR-3a, CR-4, CR-7c, CR-8a, CR-9, CR-12. Recurs for bans on home brewing or distilling, home gardens in front yards, wood stoves, short-term letting of one's own home, and home businesses.
- *P-026-2 Phase-out of a held stock with a common deadline.* If: a policy bans holding a stock (birds, vehicles, equipment) from a common deadline, with no grandfathering, and bans new acquisitions earlier. Then: acquisitions after the freeze fall; acquisitions before it are `ambiguous` (pull-forward against a shorter period of use, CR-10a, CR-4, CR-12b); disposals bunch before the deadline and are signed per window (CR-10a, 2.5); takers' capacity is rationed (CR-6), so search or waiting rises (group sign); prices fall in the market that receives the disposals (RS-13); the stock's value falls at announcement (CR-7c). Derivation: CR-4, CR-6, CR-7c, CR-10a, CR-12. RS-8 should gain an *Unless* clause: where a deadline applies to every unit regardless of when it was acquired, a rush before it is not implied, and the sign before the deadline is `ambiguous`.

**(d) Vocabulary (what the ontology lacks).**
- *Instrument type.* 2.3 lists `prohibition` only as triangular ("of a good or service"). An autistic ban on one's own production or keeping has no instrument type and no rule family. Proposed: `own_use_prohibition` (autistic).
- *Variables.* (1) No variable for production for one's own use or for gifts: `quantity_supplied` and `quantity_traded` are market quantities, so C-1 had to use `capital_stock_target` as a proxy. Proposed: `home_production`. (2) No way to record a loss by the actor's own ranking (CR-3a) of an activity valued for itself; the method's most certain conclusion here is not in the consequence list. Proposed: a field on a consequence (for example `own_ranking: worse`) attached to the observable variable, scored only on the variable. (3) `informal_activity` is defined as trade outside the legal market; keeping banned birds is production, not trade (C-5). (4) Fines and other non-tax receipts of the state have no variable (C-24 used `tax_revenue`). Proposed: `non_tax_receipts`.
- *Relation types.* No `gift` relation (C-19) and no `proximity` relation for neighbors (GAP-026-1).
- *Actor classes.* `neighbors` is not in the generic list in 2.2, although every autistic intervention on property has them.
- *Signs.* C-6 under U1-b could only be signed because existing duck keepers lose their birds; had there been none, there would have been no sign for "this chain does not arise under this reading". See WE-027, Gaps found (d).
