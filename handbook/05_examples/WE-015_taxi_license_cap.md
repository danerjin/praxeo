# WE-015 Cap on transferable taxi licenses (medallions)

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional city. It resembles real medallion systems but is not modeled on any one of them, and it is kept apart from the historical cases reserved for evaluation. App-based ride services, which appear some years after the cap, are treated as a later stage in section 8, not as a separate policy. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Port Halden Taxi Fleet Stabilization Ordinance.** Port Halden is a city of about 900,000 people. Until now, anyone who passed a driver background check and a vehicle inspection could obtain a city taxi license for $400 a year; about 2,400 licenses are in use. Demand for taxi trips has grown about 3% a year with population and tourism. Fares are set by the city council as a meter rate, indexed each year to consumer prices; this rule predates the ordinance and is unchanged by it. The suburbs of Brindlewick and Corvale license their own taxis, which may drop passengers in Port Halden but may not pick up there. The ordinance was introduced by the council five months before it took effect, with passage widely expected.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 License cap | `quota` (on the number of licenses, within the existing `licensing_requirement`) | Taxi service: street hails and taxi ranks | Anyone offering taxi service | The number of licenses is fixed at the number outstanding on the effective date. New licenses only by council vote. Licenses become "medallions" that may be sold or leased, with transfers registered and a 2% transfer fee. Driver and vehicle standards unchanged; vehicles must be no more than 8 years old. | K2 |
| K2 Private-hire exemption | Exemption from K1 | Pre-booked private hire | Private-hire operators | Vehicles that take only bookings made at least 30 minutes ahead, at a fare agreed at booking, may operate with an uncapped private-hire permit ($300 a year). No street hails, no ranks. | — |
| K3 Enforcement | Enforcement | K1, K2 | Taxi and Limousine Office | 12 inspectors. Fine of $1,000 for unlicensed street-hail or rank service; vehicle impounded on a second offense. Funded from the general budget and license fees. | None |

Existing rules (`existing_rules`; not part of the ordinance, and in force in the counterfactual too):

| Rule | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Meter rate | `price_ceiling` (and floor) | Taxi fares | Taxi drivers | Council-set rate, indexed each year to consumer prices. Predates the ordinance and is unchanged by it. | None |

Unclear provisions: U1, whether a booking made through a smartphone app a few minutes before pickup meets the 30-minute rule. The rule was written for phone bookings to dispatch offices, and the office has not ruled. Reading U1-a: app booking counts as pre-booked. Reading U1-b: it does not. This matters only in the later stage, where each reading's sign is reported (section 8); readings get no probability.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges between riders and would-be taxi operators beyond the cap; a grant of privilege to license holders | Not on the effective date, when the cap equals the number of licenses then outstanding. It binds as demand grows past what the fixed fleet can serve at the meter rate, within about two years (A-1). | EN-6, EN-1, EN-2, SB-4, TS-3, RS |
| R1 (existing rule) | Triangular: fixes the fare | Under open entry, not binding as a ceiling: supply adjusts to demand at the meter rate. Once K1 holds supply fixed, the meter rate sits below the fare at which riders and taxis would clear, and works as a binding ceiling (A-1, A-2). | PC-1 to PC-6 |
| K2 | Creates a boundary between covered and uncovered service | Yes | RS-5, PC-8 |
| K3 | Binary: funded from the general budget and license fees; whether the Office's budget rises with the added work is an assumption (A-16) | Yes | OC-3 |

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
| `private_hire` (`sellers.substitutes`) | Pre-booked operators under K2 | More demand; an incentive to operate as close to taxi service as the rules allow; entry stays open at a $300 permit. |
| `drivers.taxi` | Everyone who drives a licensed cab: owner-drivers and lessees | Fewer cabs than under open entry, but each may run more shifts. |
| `government.city` | The city's fee accounts | New transfer fees; more private-hire permits. |
| `drivers.unlicensed` (`intermediaries`) | People offering street-hail service without a medallion, including suburban taxis picking up illegally | Unmet demand to serve, at a risk of fines. |
| `lenders.medallion` (`intermediaries`) | Banks and credit unions that finance medallion purchases | A new loan market. |
| `app_services` (`sellers.substitutes`, later stage) | App-based ride services | See section 8. |
| `officials.enforcement`, `taxpayers` | Taxi and Limousine Office and its funders | More enforcement work. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | taxi operators (legal market) | `number_of_sellers` (taxis in service) | decrease | medium, growing | EN-6, TS-3 | A-1 |
| C-2 | `medallion_owners.initial` | `asset_value` (medallions) | increase | short (from the announcement) | EN-6, EN-2, SB-4 | A-1, A-3 |

C-1 is the visible aim: a stable fleet. Compared with open entry it is a decrease that starts at zero and grows each year that demand grows. C-2 follows at once: buyers will pay for a medallion today what they expect its extra earnings to be worth, so the gain goes to whoever holds a license when the cap becomes expected (SB-4). Medallion values are not usually part of the story when a cap is passed.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `drivers.prospective` | `entry_rate` (licenses taken out in the announcement window) | increase | short | RS-8 | A-4 |
| C-4 | `drivers.prospective` | `entry_rate` (as taxi owner-operators) | decrease | medium | EN-1, EN-6 | A-1 |
| C-5 | `riders` | `excess_demand` (taxi trips at the meter rate) | increase | medium | PC-1 | A-1, A-2 |
| C-6 | `riders` | `wait_time` | increase | medium | PC-2 | A-1, A-2, A-18 |
| C-7 | `riders.outlying` | `allocation_by_non_price_criteria` (drivers pick trips by destination, length and the look of the rider) | increase | medium | PC-2 | A-1, A-2, A-5 |
| C-8 | `riders` | `quality_per_unit` (older and less clean vehicles, refusals of short trips, less help with luggage) | decrease | medium | PC-4, RS-2 | A-1, A-6 |
| C-9 | `riders` | `side_payments` (flat fares haggled at the station and airport ranks; extra "tips" to accept a short trip) | increase | medium | PC-6, RS-3 | A-1, A-7 |
| C-10 | `drivers.unlicensed` | `informal_activity` | increase | medium | RS-3, EN-3 | A-1, A-7 |
| C-11 | `private_hire` | `reclassification` (operating as near to street service as the 30-minute rule allows: waiting near ranks, back-dated bookings) | increase | medium | RS-5 | A-1, A-8 |
| C-12 | `medallion_owners.initial` | `lobbying_effort` (keep the cap, raise the meter rate, more enforcement against unlicensed and private-hire service; later, against app services) | increase | medium to long | RS-7, EN-5 | A-9 |
| C-13 | `medallion_owners.initial` | `earnings` (more paid trips per shift at the meter rate, or lease income) | increase | medium | EN-2 | A-1, A-2 |
| C-29 | `private_hire` | `entry_rate` (new private-hire operators) | increase | medium | PC-8 Unless, CR-4b (x: enter taxi service, now closed or costly; y: enter private hire) | A-1, A-15 |
| C-33 | `riders` | `wait_time` | decrease | short (first year) | RS-8, CR-9 | A-4, A-14 |

C-3: the cap counts licenses outstanding on the effective date, and the ordinance was expected five months ahead. A $400 license that will become a sellable medallion is worth taking out now, even by people who would not otherwise drive, so the fleet on the effective date is larger than it would have been. This delays the date at which the cap binds. Where those window licenses are put into service rather than held idle (A-14), the first-year fleet is larger than under open entry and riders wait less in the first year (C-33). C-3 and C-4 sign the same entry per window: more in the announcement window, less afterwards.

C-29: with taxi entry closed except by buying or leasing a medallion, some would-be drivers take the uncapped private-hire permit instead (A-15). This is the supply chain that PC-8's Unless clause names, and it is what makes private-hire fares ambiguous (C-15, section 7).

C-5 to C-9: the cap does not raise the fare, because the meter rate is fixed (R1). The scarcity shows up instead in waiting, in drivers choosing their riders, in lower service, and in payments outside the meter (LW-6). PC-2 alone licenses only the group (waiting, search, side payments, non-price allocation: at least one increases). Each member is signed here on its own premise that the margin is open and used: waiting because cabs are allocated first come at ranks and by hail (A-18), drivers' choice of riders because refusals are hard to detect (A-5), side payments because off-meter deals go undetected (A-7). Riders who would have been served under open entry are the ones who wait or go without.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-14 | `riders` | `quantity_substitute` (transit, private cars, private hire) | increase | medium | RS-1 | taxis and transit: `substitute`, partial | A-1, A-10 |
| C-15 | `riders` (using private hire) | `price_substitute` (private-hire fares) | ambiguous | medium | PC-8 vs RS-13 (PC-8 Unless); CR-12b | taxis and private hire: `same_market_other_segment`, partial | A-1, A-10, A-15 |
| C-30 | `drivers.taxi` | `employment` (people driving licensed cabs) | ambiguous | medium | EN-6 vs CR-7a; CR-12b | | A-1, A-2 |
| C-31 | `government.city` | `tax_revenue` (2% transfer fees and private-hire permit fees) | increase | medium | CR-1, CR-8b | | A-1, A-3, A-15 |
| C-16 | `riders.informal` | `search_cost` (unlicensed cabs cannot advertise) | increase | medium | RS-10 | | A-7 |
| C-26 | `riders.informal` | `quality_information` (no licensing record, insurance check or Office complaint route) | decrease | medium | RS-10 | | A-7 |
| C-27 | `riders.informal` | `disputes_settled_outside_courts` (fare and damage disputes with unlicensed drivers) | increase | medium | RS-10 | | A-7 |
| C-17 | `lenders.medallion` | `quantity_traded` (medallion loans) | increase | medium | SB-4 | medallion purchases and loans: `complement`, close | A-3 |

C-15: riders turned away by the capped fleet add demand for private hire (PC-8), while would-be taxi drivers shut out by the cap add supply to it (C-29, RS-13). PC-8's Unless clause applies, and without a premise on which chain dominates the fare is `ambiguous` (section 7).

C-30: there are fewer cabs than under open entry (C-1), but the medallion is now the scarce means, so holders run each one for more shifts, with more drivers per medallion (CR-7a). The number of people driving taxis is `ambiguous`. EN-3 covers the excluded entrants (C-24), not the drivers who remain.

C-31: the 2% transfer fee exists only because medallions are tradable, and private-hire permits rise with entry (C-29). If annual license fees are still charged on medallions, the smaller fleet yields less of them, so total city fee revenue is `ambiguous`; only the transfer and permit fees are signed.

C-16, C-26, C-27: RS-10 applies to the unlicensed trade in C-10. Unlicensed cabs cannot advertise, riders cannot check a driver's record or insurance, and a fare dispute cannot go to the Office.

RS-9 (bundled trips) was checked: riders do not change where they buy other goods, so it does not apply. RS-11 (lock-in) was checked: a medallion can be sold, so its holder loses nothing by moving, and it does not apply. RS-12 (complements in use) was checked: the smaller taxi fleet buys less fuel and fewer repairs, but riders' shift to private cars and private hire (C-14) uses more of both, so the combined sign for garages and fuel sellers is ambiguous; the group is diffuse, so the chain is not pursued.

Not reported: higher medallion prices passed on to riders as a higher meter rate. The meter rate is indexed by formula; a council vote to raise it above the index rests on A-13 (p = 0.35), below the cut-off. It is a likely target of C-12.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `riders` (using private hire), `price_substitute`, medium | Riders the capped fleet cannot serve turn to private hire (PC-8). | Would-be taxi drivers enter private hire instead (C-29; RS-13, PC-8 Unless). | None | **ambiguous** (C-15). What would decide it: how many shut-out drivers take private-hire permits, against how much unmet taxi demand turns to pre-booked rides. |
| `drivers.taxi`, `employment`, medium | More shifts per medallion as holders work the scarce asset harder (CR-7a). | Fewer cabs than under open entry (C-1). | None | **ambiguous** (C-30). |
| `riders`, `wait_time`, short and medium | Medium: the fixed fleet falls short of growing demand (C-6). | Short: licenses taken out in the window add cabs in the first year (C-33). | Not combined (CR-12g) | Different horizons: **decrease** in the first year (C-33), **increase** in the medium run (C-6). |
| `drivers.lessees`, `earnings`, medium | Busier cabs: more paid trips per shift at the meter rate (C-5). | Lease fees rise with medallion values and capture the scarcity for the owner (EN-2, SB-4). | None | **ambiguous** (C-18). Decided by competition for leases: with many drivers bidding for a fixed number of medallions, lease fees absorb most of the extra trips' value. |
| `riders`, `full_cost_per_unit` (meter fare plus side payments and the value of waiting), medium | Waiting (C-6), side payments (C-9). | None: the meter fare is the same as in the counterfactual, because R1 stays in place there too. | None needed | **increase** (C-28). Unlike under a ceiling imposed by the policy, the money price does not fall, so nothing offsets the added waiting and side payments. Lower quality (C-8) adds to the loss but is not part of this variable. |
| `riders`, `wait_time`, long (after app services arrive) | The cap (C-6). | Under reading U1-a, app services entering through the private-hire exemption, in greater numbers than under open entry because the cap leaves unmet demand (C-20). | None | **U1-a: ambiguous; U1-b: increase** (C-19). Under U1-a, decided by how close a substitute app rides are for street hails. Under U1-b, app services cannot relieve the cap legally, and only the + chain applies. |
| `medallion_holders`, `asset_value`, long | The cap still limits street-hail and rank service (C-2). | App services take part of the unmet demand that gives medallions their value (C-20). | None needed | **increase** (C-21), but smaller than at its peak. The − chain can bring the value down toward what a license would be worth under open entry; it cannot push it below that. |

## 8. Time structure

**Stage 1: the cap alone (years 0 to about 5).**
- **Announcement (five months).** Licenses are taken out to be converted into medallions (C-3), and medallions gain value as soon as the cap is expected (C-2). Medallions are an asset the ordinance creates, so their value is captured by those who hold licenses when the cap becomes expected (SB-4, CR-7c). If the window licenses are put into service, riders wait less in the first year (C-33).
- **The cap binds gradually.** On the effective date the fleet is no smaller than under open entry. With demand growing about 3% a year, the cap binds within about two years (A-1), and every effect that runs through scarcity (C-5 to C-11, C-13 to C-16, C-26 to C-28) starts small and grows each year. This is TS-3, which since catalog 0.3 covers caps fixed in physical units such as a number of licenses; the expected path of demand is A-1.
- **Durable vehicles.** Owners keep cars up to the 8-year limit rather than replacing them early, since busy cabs fill anyway (C-8, TS-1); the fall in vehicle quality shows after a few years.
- **Capitalization and later buyers.** Every sale after the announcement is at a price that carries the expected rent (SB-4). Later buyers, often borrowing (C-17), earn only an ordinary return on what they paid, and they carry the risk that the rent will not last.

**Stage 2: app-based ride services appear (about year 6 on).** App services would have appeared in the counterfactual too, competing with a larger fleet; what matters here is how the cap changes their entry. The unclear provision decides which path the city takes.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-19 | `riders` | `wait_time` | U1-a: ambiguous; U1-b: increase | long | see section 7 | | A-1 |
| C-20 | `app_services` | `entry_rate` (legal app service) | U1-a: increase; U1-b: decrease | long | U1-a: RS-5, PC-8; U1-b: EN-6, RS-3 | taxis and app rides: `same_market_other_segment`, close | A-1 |
| C-21 | `medallion_holders` | `asset_value` (medallions) | increase under both readings (under U1-a, smaller than at peak) | long | SB-4, see section 7 | | A-1, A-3 |
| C-22 | `medallion_buyers.later` | `earnings` (after loan payments, compared with driving under open entry) | U1-a: decrease; U1-b: ambiguous | long | SB-4, RS-5 | | A-3, A-12 |

- **Reading U1-a: app booking counts as pre-booked.** The private-hire exemption becomes the route by which the cap's unmet demand is served (RS-5). App services enter faster than they would under open entry, because the capped fleet leaves riders waiting (C-20). Waiting, refusals and unlicensed street service lose much of their reason to exist; whether waiting ends up shorter or longer than under open entry is ambiguous (C-19). Medallion values fall from their peak but stay above what a license would be worth under open entry, so long as the cap still reserves hails and ranks (C-21). Buyers who paid the peak price, many with loans, now hold an asset worth less than they paid, and earn less than they would have by driving under open entry (C-22). This is SB-4 as generalized in catalog 0.3: when an expected gain erodes because exempt competitors enter, the value falls on whoever holds the asset then, including recent buyers who paid the capitalized price. Relative to open entry, medallions are still worth more (C-21); the loss is relative to what later buyers paid, and shows in their earnings after loan payments (C-22). Medallion holders lobby to have app rides classified as taxis (C-12). Pressure for a further rule, such as a cap on private-hire permits, is what TS-4 predicts; TS-4 is Tier C in the catalog, so this is a suggestion only.
- **Reading U1-b: app booking does not count.** App rides booked on short notice become unlicensed taxi service (RS-3), so informal activity (C-10) and enforcement costs (C-25) rise further. Legal app service is less than under open entry, where app drivers could have taken out $400 licenses (C-20, decrease). Waiting stays longer than under open entry (C-19, increase), and medallion values hold up longer (C-21). Later buyers then neither gain nor lose from the cap as it stands (SB-4), so C-22 is not signed under this reading.
- **Expectations.** Once app services are seen in other cities, medallion buyers expect erosion, and medallion prices fall before any app operates in Port Halden (SB-4, TS-2). Whoever holds medallions when the erosion becomes expected bears the fall, including buyers who paid near the peak.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | `riders`, `drivers.prospective` | `quantity_traded` (taxi trips) | decrease | Trips that riders would have taken and new drivers would have supplied at the meter rate under open entry. Both sides lose the gain they expected. | OC-4 |
| C-24 | `drivers.prospective` | `earnings` | decrease | The earnings of driving, for those who would have entered with a $400 license and take their next-best work instead, where that work pays less in money (A-17). By their own ranking all of them are worse off (CR-3a). | EN-3, OC-4 |
| C-25 | `taxpayers` | `resources_available_other_uses` | decrease | What the Office's added enforcement budget would otherwise have funded (A-16). | OC-3, OC-1 |
| C-32 | `medallion_owners.initial` | `resources_available_other_uses` | decrease | What the resources spent lobbying (C-12) would otherwise have done. | OC-1, CR-8c |
| C-34 | `officials.enforcement` | `enforcement_cost` | increase | Inspectors' time on unlicensed service and the 30-minute rule; registering transfers. | OC-3 |

Riders' waiting time is already recorded as C-6, so it is not listed again here. OC-3 funding: the Office is funded from the general budget and license fees. A-16 takes its budget to rise with the added work, so the cost falls on taxpayers (C-25); to the extent the new transfer fees pay for it, it reduces what those fees would do elsewhere. If the budget stays fixed at 12 inspectors, other inspections (vehicles, driver checks) fall instead, and the chance that any one unlicensed ride is caught falls, which strengthens C-9 to C-11.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Demand keeps growing about 3% a year, so at the meter rate the fixed fleet falls short of demand within about two years, and more so each year. | binding | 0.8 | Trip records; population and visitor trends; utilization of cabs. | The cap does not bind; almost every consequence fails. |
| A-2 | Drivers cannot simply charge above the meter on metered trips. | enforcement | 0.8 | Sealed meters; receipts; complaint data. | The fare rises instead; C-5 to C-7 weaken. |
| A-3 | Medallion holders and buyers expect the cap to last. | expectations | 0.75 | Council politics; history of comparable caps. | C-2, C-17, C-21 smaller; C-31's transfer fees smaller. |
| A-4 | Applicants know the cap will count licenses outstanding on the effective date, and can get a license within five months. | expectations | 0.8 | Ordinance text; processing times for checks and inspections. | C-3 not reported. |
| A-5 | Refusals of hails and trips are hard to detect and punish. | enforcement | 0.75 | Complaint volumes; 12 inspectors for 2,400 cabs. | C-7 weakens. |
| A-6 | Vehicle and service standards leave room above the legal minimum. | other | 0.8 | 8-year age limit; inspection content. | C-8 weakens. |
| A-7 | Unlicensed service and off-meter deals often go undetected. | enforcement | 0.75 | 12 inspectors; size of the city; pick-up bans on suburban taxis hard to police. | C-9, C-10, C-16 not reported. |
| A-8 | The 30-minute booking rule is loosely enforced. | enforcement | 0.6 | Inspection of booking records; fines issued. | C-11 not reported. |
| A-9 | Medallion holders can organize at a cost below their stake. | other | 0.85 | Existing drivers' association; concentrated, identifiable gain. | C-12, C-32 weaken. |
| A-10 | Transit and private hire are acceptable substitutes for some taxi trips. | substitutability | 0.8 | Transit coverage; private-hire fleet size. | C-14, C-15 weaken. |
| A-12 | App services take enough trips that medallion prices fall below what buyers near the peak paid. | expectations | 0.6 | Experience of cities where app services entered; medallion sale prices. | C-22 not reported. |
| A-13 | The council raises the meter rate above its index in response to medallion holders. | other | 0.35 | Council voting record on fares. | Below cut-off; not reported. |
| A-14 | Most licenses obtained in the window are put into service (driven or leased out) in the first year rather than held idle as medallions. | other | 0.6 | A vehicle must pass inspection to be licensed; cost of holding an idle licensed vehicle; lease demand. | C-33 not reported (first-year waits unchanged). |
| A-15 | Some would-be taxi drivers shut out by the cap can and do operate as private hire instead. | alternative_uses | 0.75 | $300 uncapped permit; same vehicle and driver standards; dispatch offices taking on drivers. | C-29 and C-31's permit fees not reported; C-15 becomes **increase** (PC-8 alone). |
| A-16 | The Office's budget rises with the added enforcement work, rather than the 12 inspectors being moved from other duties. | revenue_use | 0.55 | The ordinance fixes 12 inspectors but says nothing about their other duties; budget documents; use of the new transfer fees. | C-25 not reported; other inspections fall instead (OC-3, fixed budget). |
| A-17 | Would-be taxi drivers' next-best work pays less in money than driving under open entry would have. | other | 0.6 | Earnings of drivers compared with the jobs open to people of similar skills; but private hire (C-29) is open to some of them and may pay as well. | C-24 not reported; excluded entrants are still worse off by their own ranking. |
| A-18 | Taxi trips are allocated first come at ranks and by hail, so fewer cabs relative to riders shows as longer waits. | other | 0.9 | Rank queues and hail practice; no booking system for street service. | C-6 is replaced by the PC-2 group (waiting, search, side payments, non-price allocation: at least one increases). |

A-11 of the catalog 0.2 draft gave a probability to the reading of the 30-minute rule. Readings are not assumptions (workflow step 10), so it is withdrawn; the provision is analyzed as U1, with one sign per reading.

## 11. Report

**The policy.** Port Halden freezes the number of taxi licenses at the number outstanding on the effective date and makes them transferable "medallions". Fares stay at the council-set meter rate. Pre-booked private hire is exempt and uncapped.

**Visible consequences.** The fleet stops growing (C-1).

**Invisible consequences.**
- *License holders on the effective date* receive a sellable asset (C-2) and, as demand grows, more paid trips or lease income (C-13). Some people took out licenses during the announcement window only to hold a medallion (C-3).
- *Riders*, once demand outgrows the fleet, wait longer (C-6), get older cars and more refusals (C-8), pay off-meter at busy ranks (C-9), and use transit, cars and private hire more (C-14). Whether private-hire fares rise is ambiguous, because drivers shut out of taxi service enter private hire too (C-15, C-29). In the first year, if the licenses rushed in the window are put into service, riders wait less (C-33). Riders in outer areas, at night or wanting short trips are the ones drivers pass over (C-7). Taken together, the full cost of a trip (fare, side payments and waiting) rises, since the meter fare is the same as it would have been (C-28). Some take unlicensed cabs, which are harder to find, harder to judge in advance, and offer no recourse in a dispute (C-10, C-16, C-26, C-27).
- *Would-be drivers* can no longer enter for $400 (C-4); some take private-hire permits instead (C-29), others take other work, at lower earnings where it pays less (C-24, A-17). Fewer trips happen than would have (C-23). Whether more or fewer people drive licensed cabs is ambiguous: fewer cabs, but more shifts per cab (C-30).
- *Later buyers of medallions* pay for the expected rent up front, often with loans (C-17).
- *Medallion holders* lobby to protect the cap (C-12), using up resources (C-32). *Taxpayers* fund enforcement (C-25, C-34). The city collects transfer and private-hire permit fees (C-31).
- *When app services arrive*, the result depends on how the city reads the 30-minute rule (U1). If app bookings count as pre-booked, apps enter through the private-hire exemption faster than they would under open entry (C-20), medallion values fall from their peak though they stay above their open-entry level (C-21), and buyers who paid near the peak earn less than they would have by driving under open entry (C-22). If app bookings do not count, short-notice app rides are unlicensed, legal app service is less than under open entry (C-20), waits stay longer (C-19), and medallion values hold up longer (C-21).

**Ambiguous effects.** Whether drivers who lease medallions earn more or less. Whether private-hire fares rise (C-15). Whether more or fewer people drive taxis (C-30). Whether riders' waiting time, once app services arrive, ends up longer or shorter than under open entry, if app bookings count as pre-booked (C-19).

**Key conditions.** That demand keeps growing (A-1, p = 0.8): the cap does nothing until demand outgrows the fleet. How the city reads the 30-minute rule for app bookings (U1) decides the later stage; the analysis reports both readings and does not guess between them.

**What this analysis cannot say.** How long waits get, how much medallions are worth, how the gains of early holders compare with the losses of riders, would-be drivers and late buyers; road safety and congestion (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | taxi operators (legal) | number_of_sellers | decrease | medium | visible | B | EN-6, TS-3 | A-1 |
| C-2 | medallion_owners.initial | asset_value | increase | short | invisible | B | EN-6, EN-2, SB-4 | A-1, A-3 |
| C-3 | drivers.prospective | entry_rate (announcement window) | increase | short | invisible | B | RS-8 | A-4 |
| C-4 | drivers.prospective | entry_rate | decrease | medium | invisible | B | EN-1, EN-6 | A-1 |
| C-5 | riders | excess_demand | increase | medium | invisible | B | EN-6, PC-1 | A-1, A-2 |
| C-6 | riders | wait_time | increase | medium | invisible | B | PC-1, PC-2 | A-1, A-2, A-18 |
| C-7 | riders.outlying | allocation_by_non_price_criteria | increase | medium | invisible | B | PC-1, PC-2 | A-1, A-2, A-5 |
| C-8 | riders | quality_per_unit | decrease | medium | invisible | B | PC-4, RS-2, TS-1 | A-1, A-6 |
| C-9 | riders | side_payments | increase | medium | invisible | B | PC-6, RS-3 | A-1, A-7 |
| C-10 | drivers.unlicensed | informal_activity | increase | medium | invisible | B | RS-3, EN-3 | A-1, A-7 |
| C-11 | private_hire | reclassification | increase | medium | invisible | B | RS-5 | A-1, A-8 |
| C-12 | medallion_owners.initial | lobbying_effort | increase | medium–long | invisible | B | RS-7, EN-5 | A-9 |
| C-13 | medallion_owners.initial | earnings | increase | medium | invisible | B | EN-2 | A-1, A-2 |
| C-14 | riders | quantity_substitute (transit, cars, private hire) | increase | medium | invisible | B | RS-1 | A-1, A-10 |
| C-15 | riders (private hire) | price_substitute | ambiguous | medium | invisible | B | PC-8 vs RS-13 (PC-8 Unless); CR-12b | A-1, A-10, A-15 |
| C-16 | riders.informal | search_cost | increase | medium | invisible | B | RS-3, RS-10 | A-7 |
| C-26 | riders.informal | quality_information | decrease | medium | invisible | B | RS-3, RS-10 | A-7 |
| C-27 | riders.informal | disputes_settled_outside_courts | increase | medium | invisible | B | RS-3, RS-10 | A-7 |
| C-17 | lenders.medallion | quantity_traded (loans) | increase | medium | invisible | B | SB-4 | A-3 |
| C-18 | drivers.lessees | earnings | ambiguous | medium | invisible | B | C-5 vs EN-2, SB-4 | A-1, A-2 |
| C-19 | riders | wait_time | U1-a: ambiguous; U1-b: increase | long | invisible | B | C-6 vs C-20 | A-1 |
| C-20 | app_services | entry_rate (legal) | U1-a: increase; U1-b: decrease | long | invisible | B | U1-a: RS-5, PC-8; U1-b: EN-6, RS-3 | A-1 |
| C-21 | medallion_holders | asset_value | increase | long | invisible | B | SB-4 | A-1, A-3 |
| C-22 | medallion_buyers.later | earnings | U1-a: decrease; U1-b: ambiguous | long | invisible | B | SB-4, RS-5 | A-3, A-12 |
| C-23 | riders, drivers.prospective | quantity_traded (taxi trips) | decrease | medium | invisible | B | OC-4 | A-1, A-2 |
| C-24 | drivers.prospective | earnings | decrease | medium | invisible | B | EN-3, OC-4 | A-1, A-17 |
| C-25 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | OC-3, OC-1 | A-16 |
| C-28 | riders | full_cost_per_unit | increase | medium | invisible | B | PC-1, PC-2, PC-6 | A-1, A-2 |
| C-29 | private_hire | entry_rate | increase | medium | invisible | B | PC-8 Unless, CR-4b | A-1, A-15 |
| C-30 | drivers.taxi | employment | ambiguous | medium | invisible | B | EN-6 vs CR-7a; CR-12b | A-1, A-2 |
| C-31 | government.city | tax_revenue (transfer and permit fees) | increase | medium | invisible | B | CR-1, CR-8b | A-1, A-3, A-15 |
| C-32 | medallion_owners.initial | resources_available_other_uses | decrease | medium | invisible | B | OC-1, CR-8c | A-9 |
| C-33 | riders | wait_time | decrease | short | invisible | B | RS-8, CR-9 | A-4, A-14 |
| C-34 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |

## Gaps found

- GAP-015-1 (closed in catalog 0.3: SB-4 generalized to decapitalization when an expected gain erodes). C-22 is now Tier B under reading U1-a, resting on A-3 and A-12.
- GAP-015-2 (closed in catalog 0.3: TS-3 widened to parameters fixed in physical units). The gradual binding of the license cap is now derived (C-1, section 8), with the demand path in A-1.
- GAP-015-3 (closed in catalog 0.3: `existing_rules` field in the policy record). The meter rate is recorded there as R1 instead of as a component K0.

Review corrections on the update to catalog 0.3: the reading of the 30-minute rule had been given a probability (A-11) and reading B dropped as below the cut-off; it is now the unclear provision U1, with one sign per reading (C-19 to C-22). The RS-10 effects of unlicensed service are split into their own variables (C-16, C-26, C-27); riders' combined cost is recorded as `full_cost_per_unit` (C-28); the complements check now uses RS-12; two real suburb names were replaced with fictional ones.

- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-015_taxi_license_cap_core.md): private-hire fares (C-15) are now ambiguous under PC-8's Unless clause, with private-hire entry added (C-29, A-15); added the ambiguous number of taxi drivers (C-30), transfer and permit fees (C-31), lobbying resources (C-32), first-year waits from the window rush (C-33, A-14) and enforcement cost (C-34); EN-3's earnings premise (A-17), PC-2's per-margin premise for waiting (A-18) and OC-3's funding (A-16) are now stated.
