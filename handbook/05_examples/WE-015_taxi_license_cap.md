# WE-015 Cap on transferable taxi licenses (medallions)

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized policy in a fictional city. It resembles real medallion systems but is not modeled on any one of them, and it is kept apart from the historical cases reserved for evaluation. App-based ride services, which appear some years after the cap, are treated as a later stage in section 8, not as a separate policy. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Port Halden Taxi Fleet Stabilization Ordinance.** Port Halden is a city of about 900,000 people. Until now, anyone who passed a driver background check and a vehicle inspection could obtain a city taxi license for $400 a year; about 2,400 licenses are in use. Demand for taxi trips has grown about 3% a year with population and tourism. Fares are set by the city council as a meter rate, indexed each year to consumer prices; this rule predates the ordinance and is unchanged by it. The suburbs of Ashby and Marlow license their own taxis, which may drop passengers in Port Halden but may not pick up there. The ordinance was introduced by the council five months before it took effect, with passage widely expected.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K0 Meter rate (existing, not part of the ordinance) | `price_ceiling` (and floor) | Taxi fares | Taxi drivers | Council-set rate, indexed to consumer prices. | None |
| K1 License cap | `quota` (on the number of licenses, within the existing `licensing_requirement`) | Taxi service: street hails and taxi ranks | Anyone offering taxi service | The number of licenses is fixed at the number outstanding on the effective date. New licenses only by council vote. Licenses become "medallions" that may be sold or leased, with transfers registered and a 2% transfer fee. Driver and vehicle standards unchanged; vehicles must be no more than 8 years old. | K2 |
| K2 Private-hire exemption | Exemption from K1 | Pre-booked private hire | Private-hire operators | Vehicles that take only bookings made at least 30 minutes ahead, at a fare agreed at booking, may operate with an uncapped private-hire permit ($300 a year). No street hails, no ranks. | — |
| K3 Enforcement | Enforcement | K1, K2 | Taxi and Limousine Office | 12 inspectors. Fine of $1,000 for unlicensed street-hail or rank service; vehicle impounded on a second offense. Funded from the general budget and license fees. | None |

Unclear provisions: whether a booking made through a smartphone app a few minutes before pickup meets the 30-minute rule. The rule was written for phone bookings to dispatch offices, and the office has not ruled. This matters only in the later stage, where both readings are analyzed (section 8).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges between riders and would-be taxi operators beyond the cap; a grant of privilege to license holders | Not on the effective date, when the cap equals the number of licenses then outstanding. It binds as demand grows past what the fixed fleet can serve at the meter rate, within about two years (A-1). | EN-6, EN-1, EN-2, SB-4, RS |
| K0 | Triangular: fixes the fare | Under open entry, not binding as a ceiling: supply adjusts to demand at the meter rate. Once K1 holds supply fixed, the meter rate sits below the fare at which riders and taxis would clear, and works as a binding ceiling (A-1, A-2). | PC-1 to PC-6 |
| K2 | Creates a boundary between covered and uncovered service | Yes | RS-5, PC-8 |
| K3 | Binary: funded by taxpayers and fees | Yes | OC-3 |

The counterfactual is Port Halden with open entry at the same meter rate.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `medallion_owners.initial` | License holders on the effective date | A $400 license becomes a sellable asset; less competition as demand grows. |
| `medallion_buyers.later` (`sellers.prospective`) | People who enter the trade after the cap by buying a medallion | Must pay a price that carries the expected rent. |
| `medallion_holders` | Whoever holds medallions at a later date: initial owners and later buyers together | Bear changes in medallion values after the cap is in place. |
| `drivers.lessees` | Drivers who lease a medallion by the shift or week | Busier cabs, but a lease fee to pay. |
| `drivers.prospective` (`sellers.prospective`) | People who would have entered with a $400 license | Can enter only by buying or leasing. |
| `riders` (`buyers.current`) | Taxi users | At the meter rate, fewer cabs relative to demand. |
| `riders.outlying` | Riders in outer neighborhoods, at night, or wanting short trips | Drivers can choose among hails. |
| `riders.informal` | Riders who use unlicensed cabs | Ride without the protections of the legal market. |
| `private_hire` (`sellers.substitutes`) | Pre-booked operators under K2 | More demand; an incentive to operate as close to taxi service as the rules allow. |
| `drivers.unlicensed` (`intermediaries`) | People offering street-hail service without a medallion, including suburban taxis picking up illegally | Unmet demand to serve, at a risk of fines. |
| `lenders.medallion` (`intermediaries`) | Banks and credit unions that finance medallion purchases | A new loan market. |
| `app_services` (`sellers.substitutes`, later stage) | App-based ride services | See section 8. |
| `officials.enforcement`, `taxpayers` | Taxi and Limousine Office and its funders | More enforcement work. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | taxi operators (legal market) | `number_of_sellers` (taxis in service) | decrease | medium, growing | K1, EN-6 | A-1 |
| C-2 | `medallion_owners.initial` | `asset_value` (medallions) | increase | short (from the announcement) | EN-6, EN-2, SB-4 | A-1, A-3 |

C-1 is the visible aim: a stable fleet. Compared with open entry it is a decrease that starts at zero and grows each year that demand grows. C-2 follows at once: buyers will pay for a medallion today what they expect its extra earnings to be worth, so the gain goes to whoever holds a license when the cap becomes expected (SB-4). Medallion values are not usually part of the story when a cap is passed.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `drivers.prospective` | `entry_rate` (licenses taken out in the announcement window) | increase | short | RS-8 | A-4 |
| C-4 | `drivers.prospective` | `entry_rate` (as taxi owner-operators) | decrease | medium | EN-1, EN-6 | A-1 |
| C-5 | `riders` | `excess_demand` (taxi trips at the meter rate) | increase | medium | PC-1 | A-1, A-2 |
| C-6 | `riders` | `wait_time` | increase | medium | PC-2 | A-1, A-2 |
| C-7 | `riders.outlying` | `allocation_by_non_price_criteria` (drivers pick trips by destination, length and the look of the rider) | increase | medium | PC-2 | A-1, A-2, A-5 |
| C-8 | `riders` | `quality_per_unit` (older and less clean vehicles, refusals of short trips, less help with luggage) | decrease | medium | PC-4, RS-2 | A-1, A-6 |
| C-9 | `riders` | `side_payments` (flat fares haggled at the station and airport ranks; extra "tips" to accept a short trip) | increase | medium | PC-6, RS-3 | A-1, A-7 |
| C-10 | `drivers.unlicensed` | `informal_activity` | increase | medium | RS-3, EN-3 | A-1, A-7 |
| C-11 | `private_hire` | `reclassification` (operating as near to street service as the 30-minute rule allows: waiting near ranks, back-dated bookings) | increase | medium | RS-5 | A-1, A-8 |
| C-12 | `medallion_owners.initial` | `lobbying_effort` (keep the cap, raise the meter rate, more enforcement against unlicensed and private-hire service; later, against app services) | increase | medium to long | RS-7, EN-5 | A-9 |
| C-13 | `medallion_owners.initial` | `earnings` (more paid trips per shift at the meter rate, or lease income) | increase | medium | EN-2 | A-1, A-2 |

C-3: the cap counts licenses outstanding on the effective date, and the ordinance was expected five months ahead. A $400 license that will become a sellable medallion is worth taking out now, even by people who would not otherwise drive, so the fleet on the effective date is larger than it would have been. This delays the date at which the cap binds.

C-5 to C-9: the cap does not raise the fare, because the meter rate is fixed (K0). The scarcity shows up instead in waiting, in drivers choosing their riders, in lower service, and in payments outside the meter (LW-6). Riders who would have been served under open entry are the ones who wait or go without.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-14 | `riders` | `quantity_substitute` (transit, private cars, private hire) | increase | medium | RS-1 | taxis and transit: `substitute`, partial | A-1, A-10 |
| C-15 | `riders` (using private hire) | `price_substitute` (private-hire fares) | increase | medium | PC-8 | taxis and private hire: `same_market_other_segment`, partial | A-1, A-10 |
| C-16 | `riders.informal` | `search_cost` (unlicensed cabs cannot advertise; fares disputed without recourse) | increase | medium | RS-10 | | A-7 |
| C-17 | `lenders.medallion` | `quantity_traded` (medallion loans) | increase | medium | SB-4 | medallion purchases and loans: `complement`, close | A-3 |

C-16: RS-10 applies to the unlicensed trade in C-10. Riders cannot check a driver's record or insurance, and a fare dispute cannot go to the Office.

RS-9 (bundled trips) was checked: riders do not change where they buy other goods, so it does not apply. RS-11 (lock-in) was checked: a medallion can be sold, so its holder loses nothing by moving, and it does not apply. Effects on garages and fuel sellers from a smaller fleet are diffuse at depth 3; stopped.

Not reported: higher medallion prices passed on to riders as a higher meter rate. The meter rate is indexed by formula; a council vote to raise it above the index rests on A-13 (p = 0.35), below the cut-off. It is a likely target of C-12.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `drivers.lessees`, `earnings`, medium | Busier cabs: more paid trips per shift at the meter rate (C-5). | Lease fees rise with medallion values and capture the scarcity for the owner (EN-2, SB-4). | None | **ambiguous** (C-18). Decided by competition for leases: with many drivers bidding for a fixed number of medallions, lease fees absorb most of the extra trips' value. |
| `riders`, total cost per trip (meter fare, side payments, waiting), medium | Waiting (C-6), side payments (C-9), lower quality (C-8). | None. | None needed | **increase**. Every chain that applies pushes the full cost of a trip up; the meter fare itself is unchanged. |
| `riders`, `wait_time`, long (after app services arrive) | The cap (C-6). | App services entering through the private-hire exemption, in greater numbers than under open entry because the cap leaves unmet demand (C-20). | None | **ambiguous** (C-19). Decided by whether app booking qualifies as pre-booked (A-11) and how close a substitute app rides are. |
| `medallion_holders`, `asset_value`, long | The cap still limits street-hail and rank service (C-2). | App services take part of the unmet demand that gives medallions their value (C-20). | None needed | **increase** (C-21), but smaller than at its peak. The − chain can bring the value down toward what a license would be worth under open entry; it cannot push it below that. |

## 8. Time structure

**Stage 1: the cap alone (years 0 to about 5).**
- **Announcement (five months).** Licenses are taken out to be converted into medallions (C-3), and medallions gain value as soon as the cap is expected (C-2).
- **The cap binds gradually.** On the effective date the fleet is no smaller than under open entry. With demand growing about 3% a year, the cap binds within about two years (A-1), and every effect that runs through scarcity (C-5 to C-11, C-13 to C-16) starts small and grows each year. This is the same pattern TS-3 describes for a cap fixed in money terms, but here the cap is fixed in units (see GAP-015-2); in this example it is carried by A-1.
- **Durable vehicles.** Owners keep cars up to the 8-year limit rather than replacing them early, since busy cabs fill anyway (C-8, TS-1); the fall in vehicle quality shows after a few years.
- **Capitalization and later buyers.** Every sale after the announcement is at a price that carries the expected rent (SB-4). Later buyers, often borrowing (C-17), earn only an ordinary return on what they paid, and they carry the risk that the rent will not last.

**Stage 2: app-based ride services appear (about year 6 on).** App services would have appeared in the counterfactual too, competing with a larger fleet; what matters here is how the cap changes their entry. The unclear provision decides which path the city takes.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-19 | `riders` | `wait_time` | ambiguous | long | see section 7 | | A-1, A-11 |
| C-20 | `app_services` | `entry_rate` | increase | long | RS-5, PC-8 | taxis and app rides: `same_market_other_segment`, close | A-1, A-11 |
| C-21 | `medallion_holders` | `asset_value` (medallions) | increase (smaller than at peak) | long | SB-4, see section 7 | | A-1, A-3, A-11 |
| C-22 | `medallion_buyers.later` | `earnings` (after loan payments, compared with driving under open entry) | decrease | long | SB-4, RS-5, GAP-015-1 | | A-11, A-12 |

- **Reading A: app booking counts as pre-booked (A-11, p = 0.6).** The private-hire exemption becomes the route by which the cap's unmet demand is served (RS-5). App services enter faster than they would under open entry, because the capped fleet leaves riders waiting (C-20). Waiting, refusals and unlicensed street service lose much of their reason to exist; whether waiting ends up shorter or longer than under open entry is ambiguous (C-19). Medallion values fall from their peak but stay above what a license would be worth under open entry, so long as the cap still reserves hails and ranks (C-21). Buyers who paid the peak price, many with loans, now hold an asset worth less than they paid, and earn less than they would have by driving under open entry (C-22). No rule in the catalog covers the fall in a capitalized value when the rent erodes, so C-22 is Tier C (GAP-015-1). Medallion holders lobby to have app rides classified as taxis (C-12). Pressure for a further rule, such as a cap on private-hire permits, is what TS-4 predicts; TS-4 is Tier C in the catalog, so this is a suggestion only.
- **Reading B: app booking does not count (p = 0.4).** App rides become unlicensed taxi service, so informal activity and enforcement costs rise further, and medallion values hold up longer. Below the cut-off; not reported.
- **Expectations.** Once app services are seen in other cities, medallion buyers expect erosion, and medallion prices fall before any app operates in Port Halden (TS-2). Buyers who bought earlier bear the fall.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | `riders`, `drivers.prospective` | `quantity_traded` (taxi trips) | decrease | Trips that riders would have taken and new drivers would have supplied at the meter rate under open entry. Both sides lose the gain they expected. | OC-4 |
| C-24 | `drivers.prospective` | `earnings` | decrease | The earnings of driving, for those who would have entered with a $400 license and take their next-best work instead. | EN-3, OC-4 |
| C-25 | `taxpayers` | `resources_available_other_uses` | decrease | What the Office's added enforcement budget would otherwise have funded. | OC-3, OC-1 |

Riders' waiting time is already recorded as C-6, so it is not listed again here.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Demand keeps growing about 3% a year, so at the meter rate the fixed fleet falls short of demand within about two years, and more so each year. | binding | 0.8 | Trip records; population and visitor trends; utilization of cabs. | The cap does not bind; almost every consequence fails. |
| A-2 | Drivers cannot simply charge above the meter on metered trips. | enforcement | 0.8 | Sealed meters; receipts; complaint data. | The fare rises instead; C-5 to C-7 weaken. |
| A-3 | Medallion holders and buyers expect the cap to last. | expectations | 0.75 | Council politics; history of comparable caps. | C-2, C-17, C-21 smaller. |
| A-4 | Applicants know the cap will count licenses outstanding on the effective date, and can get a license within five months. | expectations | 0.8 | Ordinance text; processing times for checks and inspections. | C-3 not reported. |
| A-5 | Refusals of hails and trips are hard to detect and punish. | enforcement | 0.75 | Complaint volumes; 12 inspectors for 2,400 cabs. | C-7 weakens. |
| A-6 | Vehicle and service standards leave room above the legal minimum. | other | 0.8 | 8-year age limit; inspection content. | C-8 weakens. |
| A-7 | Unlicensed service and off-meter deals often go undetected. | enforcement | 0.75 | 12 inspectors; size of the city; pick-up bans on suburban taxis hard to police. | C-9, C-10, C-16 not reported. |
| A-8 | The 30-minute booking rule is loosely enforced. | enforcement | 0.6 | Inspection of booking records; fines issued. | C-11 not reported. |
| A-9 | Medallion holders can organize at a cost below their stake. | other | 0.85 | Existing drivers' association; concentrated, identifiable gain. | C-12 weakens. |
| A-10 | Transit and private hire are acceptable substitutes for some taxi trips. | substitutability | 0.8 | Transit coverage; private-hire fleet size. | C-14, C-15 weaken. |
| A-11 | App booking is treated as pre-booked under K2 (reading A of the unclear provision). | other | 0.6 | Wording of K2; the Office's past rulings on phone bookings; legal opinion. | Reading B applies: C-19 to C-22 not reported. |
| A-12 | App services take enough trips that medallion prices fall below what buyers near the peak paid. | expectations | 0.6 | Experience of cities where app services entered; medallion sale prices. | C-22 not reported. |
| A-13 | The council raises the meter rate above its index in response to medallion holders. | other | 0.35 | Council voting record on fares. | Below cut-off; not reported. |

## 11. Report

**The policy.** Port Halden freezes the number of taxi licenses at the number outstanding on the effective date and makes them transferable "medallions". Fares stay at the council-set meter rate. Pre-booked private hire is exempt and uncapped.

**Visible consequences.** The fleet stops growing (C-1).

**Invisible consequences.**
- *License holders on the effective date* receive a sellable asset (C-2) and, as demand grows, more paid trips or lease income (C-13). Some people took out licenses during the announcement window only to hold a medallion (C-3).
- *Riders*, once demand outgrows the fleet, wait longer (C-6), get older cars and more refusals (C-8), pay off-meter at busy ranks (C-9), and use transit, cars and private hire more (C-14), where fares rise (C-15). Riders in outer areas, at night or wanting short trips are the ones drivers pass over (C-7). Some take unlicensed cabs, which are harder to find and offer no recourse (C-10, C-16).
- *Would-be drivers* can no longer enter for $400 (C-4); some take other work at lower earnings (C-24). Fewer trips happen than would have (C-23).
- *Later buyers of medallions* pay for the expected rent up front, often with loans (C-17).
- *Medallion holders* lobby to protect the cap (C-12). *Taxpayers* fund enforcement (C-25).
- *When app services arrive*, they enter through the private-hire exemption faster than they would under open entry (C-20), medallion values fall from their peak (C-21), and buyers who paid near the peak earn less than they would have by driving under open entry (C-22, Tier C).

**Ambiguous effects.** Whether drivers who lease medallions earn more or less. Whether riders' waiting time, once app services arrive, ends up longer or shorter than under open entry.

**Key conditions.** That demand keeps growing (A-1, p = 0.8): the cap does nothing until demand outgrows the fleet. How the city reads the 30-minute rule for app bookings (A-11, p = 0.6) decides the later stage.

**What this analysis cannot say.** How long waits get, how much medallions are worth, how the gains of early holders compare with the losses of riders, would-be drivers and late buyers; road safety and congestion (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | taxi operators (legal) | number_of_sellers | decrease | medium | visible | B | K1, EN-6 | A-1 |
| C-2 | medallion_owners.initial | asset_value | increase | short | invisible | B | EN-6, EN-2, SB-4 | A-1, A-3 |
| C-3 | drivers.prospective | entry_rate (announcement window) | increase | short | invisible | B | RS-8 | A-4 |
| C-4 | drivers.prospective | entry_rate | decrease | medium | invisible | B | EN-1, EN-6 | A-1 |
| C-5 | riders | excess_demand | increase | medium | invisible | B | EN-6, PC-1 | A-1, A-2 |
| C-6 | riders | wait_time | increase | medium | invisible | B | PC-1, PC-2 | A-1, A-2 |
| C-7 | riders.outlying | allocation_by_non_price_criteria | increase | medium | invisible | B | PC-1, PC-2 | A-1, A-2, A-5 |
| C-8 | riders | quality_per_unit | decrease | medium | invisible | B | PC-4, RS-2, TS-1 | A-1, A-6 |
| C-9 | riders | side_payments | increase | medium | invisible | B | PC-6, RS-3 | A-1, A-7 |
| C-10 | drivers.unlicensed | informal_activity | increase | medium | invisible | B | RS-3, EN-3 | A-1, A-7 |
| C-11 | private_hire | reclassification | increase | medium | invisible | B | RS-5 | A-1, A-8 |
| C-12 | medallion_owners.initial | lobbying_effort | increase | medium–long | invisible | B | RS-7, EN-5 | A-9 |
| C-13 | medallion_owners.initial | earnings | increase | medium | invisible | B | EN-2 | A-1, A-2 |
| C-14 | riders | quantity_substitute (transit, cars, private hire) | increase | medium | invisible | B | RS-1 | A-1, A-10 |
| C-15 | riders (private hire) | price_substitute | increase | medium | invisible | B | PC-8 | A-1, A-10 |
| C-16 | riders.informal | search_cost | increase | medium | invisible | B | RS-3, RS-10 | A-7 |
| C-17 | lenders.medallion | quantity_traded (loans) | increase | medium | invisible | B | SB-4 | A-3 |
| C-18 | drivers.lessees | earnings | ambiguous | medium | invisible | B | C-5 vs EN-2, SB-4 | A-1, A-2 |
| C-19 | riders | wait_time | ambiguous | long | invisible | B | C-6 vs C-20 | A-1, A-11 |
| C-20 | app_services | entry_rate | increase | long | invisible | B | RS-5, PC-8 | A-1, A-11 |
| C-21 | medallion_holders | asset_value | increase | long | invisible | B | SB-4 | A-1, A-3, A-11 |
| C-22 | medallion_buyers.later | earnings | decrease | long | invisible | C | SB-4, RS-5, GAP-015-1 | A-11, A-12 |
| C-23 | riders, drivers.prospective | quantity_traded (taxi trips) | decrease | medium | invisible | B | OC-4 | A-1, A-2 |
| C-24 | drivers.prospective | earnings | decrease | medium | invisible | B | EN-3, OC-4 | A-1 |
| C-25 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |

## Gaps found

- **GAP-015-1** (Tier C: C-22). SB-4 says a lasting restriction is capitalized into the value of a fixed-supply asset when it is created, and that later entrants pay for it. It says nothing about what happens when the rent erodes, through entry by an exemption, a substitute technology or repeal, and who bears the fall. Proposed fix: a companion rule, "SB-4b De-capitalization": when the expected rent from a restriction falls, `asset_value` decreases, and the loss falls on those holding the asset when the erosion becomes expected, including recent buyers who paid the capitalized price; their `earnings` net of financing fall below the counterfactual. Assumes the erosion was not fully expected when they bought.
- **GAP-015-2** (no Tier C consequence; bindingness carried by A-1 as workflow step 2 allows). TS-3 covers parameters fixed in money terms that become more binding as prices move. A cap fixed in physical units (licenses, tonnes) does the same as demand grows. Proposed fix: widen TS-3's If clause to "a cap, floor, rate, threshold or quantity fixed in money or physical units, while the relevant market price or demand moves".
- **GAP-015-3** (no Tier C consequence; record design). The binding ceiling here comes from a pre-existing rule (the meter rate) that the new policy makes binding. The policy record (`02_ontology.md`, 2.1) has no field for existing rules that interact with the policy, so K0 had to be added as a component that the ordinance does not contain. Proposed fix: add a field `existing_rules` to the policy record, with the same sub-fields as a component, so that PC and other rules can be applied to them and the counterfactual keeps them in place.
