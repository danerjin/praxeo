# WE-015 / Analysis: Port Halden Taxi Fleet Stabilization Ordinance (cap on transferable taxi licenses)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Every derivation below cites only the core rules (CR-1 to CR-12, with clause), the foundations (AX-1, LW-1 to LW-10) and arithmetic. Assumptions A-1 to A-13 (there is no A-11) are the case assumptions as given; A-N1 is a premise this re-run had to add.

## 1. Policy record

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Port Halden, a city of about 900,000. The suburbs of Brindlewick and Corvale license their own taxis, which may drop passengers in Port Halden but may not pick up there. | Policy record preamble. |
| Announced / enacted / effective / expires | Introduced by the council five months before it took effect, with passage widely expected; no expiry; new licenses only by council vote. | "The ordinance was introduced by the council five months before it took effect, with passage widely expected." |
| Enforcement (who, penalties, resources) | Taxi and Limousine Office: 12 inspectors; $1,000 fine for unlicensed street-hail or rank service; vehicle impounded on a second offense; funded from the general budget and license fees. | K3. |
| Starting conditions | Until now, anyone passing a driver background check and a vehicle inspection could obtain a taxi license for $400 a year; about 2,400 licenses in use. Demand for taxi trips has grown about 3% a year. | Policy record preamble. |

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

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 | Triangular (prohibits exchanges between riders and would-be new taxi operators); together with R1, fixes both the quantity of cabs and the price per trip | Binds within about two years and more each year, as demand grows against a fixed fleet at the meter rate (A-1, A-2) | CR-1 op 1, op 2, op 4; CR-4; CR-5a; CR-6; CR-7b, CR-7c; CR-10a, CR-10c |
| K2 | Adds an option: an uncapped, cheaper permit for pre-booked service at a fare agreed at booking, outside the meter | Binds on how private hire may operate; its reach depends on U1 | CR-1 op 2, op 3; CR-4 (x: covered form, y: uncovered form) |
| K3 | Enforcement | Weak: 12 inspectors for a city of 900,000 (A-5, A-7, A-8) | CR-1 (an unenforced prohibition attaches a risk, op 3); CR-4 (x: comply, y: violate) |
| R1 (existing) | Price ceiling and floor | Becomes binding as a ceiling once K1 makes the fleet fall short (A-1, A-2) | CR-6 |

**CR-1 operations by component and actor class.** Operations: (1) remove an option, (2) add an option, (3) change what an option brings, (4) transfer means.

| Actor class | K1 | K2 | K3 |
|---|---|---|---|
| `holders.incumbent` (license holders on the effective date) | 2 (they may now sell or lease the license); 4 (a transferable right in fixed supply, granted free, is a transfer of means); 3 (a 2% fee attached to selling) | none | none |
| `sellers.prospective` (would-be taxi operators after the effective date) | 1 (getting a new license is removed); 3 (entry now requires buying or leasing a medallion) | 2 (they may enter private hire instead) | 3 (fine and impound risk on unlicensed service) |
| `applicants.window` (those who apply in the five months before the effective date) | 3, relative: a license obtained now becomes a medallion | none | none |
| `drivers.leasing` | 3 (driving a cab requires leasing a medallion at a market rate) | none | none |
| `riders.taxi` | none directly; the fleet and the price are fixed (CR-6, CR-9) | 2 (an unmetered pre-booked option at a $300 permit; wider under U1-a) | none |
| `sellers.private_hire` | none | 2 (a cheaper, uncapped permit with fares agreed at booking); 3 (30-minute rule; no hails, no ranks) | 3 (enforcement risk on short-notice bookings) |
| `sellers.unlicensed` (unlicensed drivers and suburban taxis picking up in the city) | 1 (no new licenses) | none | 3 ($1,000 fine; impound on second offense) |
| `officials.enforcement` | 3 (registering transfers) | 3 (checking booking records) | 3 (inspection with 12 inspectors) |
| `government.city` | 4 (2% transfer fees) | 4 (permit fees) | none |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `holders.incumbent` | Holders of the about 2,400 licenses (plus window entrants) on the effective date | Receive a transferable medallion |
| `applicants.window` | Would-be operators who can apply during the five-month window | A license obtained now becomes a valuable medallion (A-4) |
| `sellers.prospective` | Would-be operators after the cap | Must buy or lease a medallion |
| `sellers.taxi` | All active licensed taxis | Fleet fixed at the effective-date number |
| `drivers.leasing` | Drivers who lease medallions | Pay a lease that reflects the scarcity of medallions |
| `drivers.taxi` | All taxi drivers | Fewer cabs than otherwise, possibly more shifts per cab |
| `riders.taxi` | Street-hail and rank riders | Face a fixed fleet at a fixed fare as demand grows |
| `riders.informal` | Riders who use unlicensed service | Cannot rely on the ordinary means of judging and enforcing quality (CR-11b) |
| `sellers.private_hire` | Pre-booked operators | Cheaper, uncapped permit; fares agreed at booking |
| `sellers.unlicensed` | Unlicensed drivers; suburban taxis picking up illegally | Excess demand makes violation pay (A-7) |
| `sellers.substitutes` | Transit and private hire | Gain riders (A-10) |
| `lobby.medallion` | Medallion holders, organized (A-9) | Stake in keeping the cap and in U1-b |
| `officials.enforcement` | Taxi and Limousine Office | More violations to police with 12 inspectors |
| `government.city` | City budget | Transfer and permit fees |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | holders.incumbent | asset_value (licenses, now medallions) | increase | short | CR-1 op 2, op 4; CR-7c and CR-10c (the expected stream of scarcity returns is capitalized when the cap becomes expected, at introduction, and captured by those who hold licenses then) | A-1, A-3 |
| C-2 | sellers.prospective | entry_rate (new taxi licenses after the effective date) | decrease | medium | CR-1 op 1; arithmetic (without the cap, new licenses would track about 3% a year demand growth) | A-1 |
| C-3 | sellers.taxi | number_of_sellers (licensed taxis) | decrease | medium | CR-1 op 1; arithmetic (fleet fixed while the counterfactual fleet grows with demand) | A-1 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | applicants.window | entry_rate (new licenses in the five months before the effective date) | increase | short | CR-10a (a license obtained before the deadline becomes a medallion); CR-4b (x: enter later, y: enter now) | A-3, A-4 |
| C-5 | sellers.taxi | number_of_sellers (licensed taxis in the first year) | increase | short | CR-10a; arithmetic (window entry brought forward from later years) | A-3, A-4 |
| C-6 | riders.taxi | wait_time | decrease | short | CR-9 (more cabs in service in the first year than otherwise, from C-5) | A-4, A-N1 |
| C-7 | riders.taxi | wait_time | increase | medium | CR-6 (fare fixed by R1 and fleet fixed by K1: the gap between trips wanted and cabs available is closed by queuing) | A-1, A-2 |
| C-8 | riders.taxi | excess_demand | increase | medium | CR-6; arithmetic (demand up about 3% a year against a fixed fleet) | A-1, A-2 |
| C-9 | riders.taxi | allocation_by_non_price_criteria (drivers choose fares: refusals of short or out-of-the-way trips) | increase | medium | CR-6 (the scarce side chooses among the other side by criteria other than price) | A-1, A-2, A-5 |
| C-10 | riders.taxi | quality_per_unit (vehicle condition and service above the legal minimum) | decrease | medium | CR-6 (pressure moves to unregulated terms: with excess demand, drivers lose riders by poor quality less than before) | A-1, A-2, A-6 |
| C-11 | riders.taxi | side_payments (off-meter flat fares, demanded tips) | increase | medium | CR-6 (exchanges outside the rule); CR-4b (x: comply, y: violate) | A-1, A-7 |
| C-12 | sellers.unlicensed | informal_activity (unlicensed street-hail service; suburban taxis picking up in the city) | increase | medium | CR-6; CR-4b (x: comply, y: violate); CR-1 (weak enforcement attaches a risk, not a removal) | A-1, A-7 |
| C-13 | sellers.private_hire | entry_rate | increase | medium | CR-4b (x: enter taxi service, now closed or costly, y: enter private hire); CR-1 op 2 (cheaper uncapped permit, fare agreed at booking); CR-7a | A-1, A-10 |
| C-14 | sellers.private_hire | informal_activity (taking bookings under 30 minutes or street hails) | increase | medium | CR-6; CR-4b (x: comply, y: violate) | A-1, A-8 |
| C-15 | lobby.medallion | lobbying_effort (against new licenses and for reading U1-b) | increase | medium | CR-4b (x: accept, y: lobby) | A-3, A-9 |
| C-16 | drivers.taxi | employment | ambiguous | medium | (−) CR-1 op 1, arithmetic: fewer cabs than otherwise; (+) CR-7a: the medallion is the scarce means, so holders move it into more hours of use (more shifts per cab, more drivers per medallion); CR-12b | A-1, A-2 |

## 6. Second-order effects

Market relations: `taxi_street_hail` and `private_hire`: `substitute`, partial (close under U1-a). `taxi_street_hail` and `transit`: `substitute`, partial (A-10). `medallions` and `taxi_service`: `input_to` (the medallion is a required input). `licensed_taxi_service` and `unlicensed_service`: `same_market_other_segment` (A-7). `port_halden_taxis` and `suburban_taxis`: `across_border` (A-7).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | drivers.leasing | price_paid (medallion lease rate) | increase | medium | CR-7b (the scarcity return settles on the fixed means, the medallion, not on drivers, who can move to other work); CR-9 (input_to) | input_to; depth 2 | A-1, A-2 |
| C-18 | sellers.prospective | price_paid (cost of entry: medallion purchase price) | increase | medium | CR-7c (later buyers pay the capitalized value, so they earn no more than elsewhere); CR-1 op 3 | input_to; depth 2 | A-1, A-3 |
| C-19 | riders.taxi | quantity_traded (taxi trips) | decrease | medium | CR-5a (trips riders and would-be operators would have made are prevented); CR-6 | same market; depth 2 | A-1, A-2 |
| C-20 | sellers.substitutes | quantity_substitute (private-hire and transit trips) | increase | medium | CR-9 (substitute); CR-4b for riders (x: hail a taxi, y: book or take transit) | substitute; depth 2 | A-1, A-10 |
| C-21 | riders.informal | quality_information | decrease | medium | CR-11b (unlicensed rides lack the ordinary means of judging and enforcing quality: licensing, meters, complaints) | same_market_other_segment; depth 3 | A-1, A-7 |
| C-22 | riders.taxi | wait_time | U1-a: ambiguous; U1-b: increase | long | U1-b: CR-6 as in C-7, more so each year (A-1). U1-a: (+) CR-6 as in C-7; (−) CR-9, CR-4b: app-based private hire at agreed fares, uncapped, draws riders away from the taxi queue (A-12); CR-12b | substitute; depth 3 | A-1, A-2, A-12 |
| C-23 | riders.taxi | excess_demand | U1-a: ambiguous; U1-b: increase | long | Same chains as C-22 | substitute; depth 3 | A-1, A-2, A-12 |
| C-24 | holders.incumbent | asset_value (medallions) | increase | long | CR-7c; CR-10c. Under U1-a, app competition (A-12) lowers the value from its peak (path note, section 8), but the value stays above the counterfactual, in which licenses were not transferable at all | input_to; depth 2 | A-1, A-3 |
| C-25 | government.city | tax_revenue (2% transfer fees and private-hire permit fees) | increase | medium | CR-1 op 4; CR-8b | input_to; depth 2 | A-1, A-3, A-10 |

Interaction of components. K2 opens an exit from K1: riders and would-be operators can move to pre-booked private hire, outside both the cap and the meter. U1 decides how wide that exit is. K3's weak staffing turns both K1's ban on new street-hail service and K2's 30-minute rule into risks rather than removals (C-12, C-14). R1, an existing rule, is what makes K1's fixed fleet produce queues rather than higher fares (C-7).

Stopping points. The private-hire chain stops at C-22 and C-23 (depth 3). Effects on vehicle dealers and repair shops through a smaller fleet are not followed: the fleet is smaller but each cab is used more (C-16), so the direction for them is unclear and the effect is diffuse.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| riders.taxi, wait_time, short | none | Window entrants add cabs in the first year (C-6) | Fleet shortfall arrives only within about two years (A-1) | decrease (C-6) |
| riders.taxi, wait_time, medium | Fixed fleet and fare (C-7) | none | — | increase (C-7) |
| riders.taxi, wait_time and excess_demand, long | Fixed fleet and fare | U1-a only: uncapped app-based private hire | U1-b: no opposing chain. U1-a: no premise says which dominates; CR-12b | U1-a: ambiguous; U1-b: increase (C-22, C-23) |
| drivers.taxi, employment, medium | More shifts per medallion (CR-7a) | Fewer cabs (K1) | None stated; CR-12b | ambiguous (C-16) |
| sellers.taxi, number_of_sellers | Short: window rush (C-5) | Medium: fixed fleet (C-3) | Different horizons; signed separately | C-5 increase (short); C-3 decrease (medium) |

## 8. Time structure

Horizons: short = from the ordinance's introduction to the end of the first year after the effective date; medium = years 2 to 5; long = beyond 5 years (the stage at which app-based services matter and U1 decides signs).

- **Window rush (CR-10a).** Because the cap counts licenses outstanding on the effective date and passage was expected five months ahead (A-4), would-be operators who would have entered over the next years get licenses now (C-4, C-5). If they put them into service (A-N1), riders wait less in the first year (C-6).
- **Capitalization (CR-7c, CR-10c).** The medallion's value appears when the cap becomes expected, at introduction, and goes to those who hold licenses on the effective date (C-1). Buyers after that pay the capitalized value and earn no more than elsewhere (C-18).
- **Growing bite (CR-6, arithmetic).** Demand grows about 3% a year; the fleet is fixed; the meter is indexed to consumer prices, not to the shortage. Excess demand and waits grow each year (C-7, C-8).
- **Path of medallion prices under U1-a.** If app bookings count as pre-booked (U1-a) and app services take enough trips (A-12, p 0.6), medallion prices fall below what buyers near the peak paid. Those buyers lose against their purchase price; relative to the counterfactual (no transferable licenses), medallions still have value (C-24). This is a note on the path, not a separate consequence.
- **Durable fleet (CR-10b).** The 8-year vehicle limit sets how long a cab can be kept; with excess demand, holders have less reason to replace vehicles before the limit (part of C-10).
- **Fare rises.** The council raising the meter rate above its index in response to holders (A-13, p 0.35) is not reported.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-7 | riders.taxi | wait_time (in section 5) | increase | Time spent waiting for cabs that would otherwise have been on the street | CR-6; CR-8c |
| C-19 | riders.taxi | quantity_traded (in section 6) | decrease | Trips that would have been made, and the gains riders and operators expected from them | CR-5a |
| C-26 | sellers.prospective | resources_available_other_uses | decrease | The capitalized medallion price, which buys no more than a $400 license would have; the sum is a transfer to incumbents | CR-8a, CR-8b; CR-7c |
| C-27 | lobby.medallion | resources_available_other_uses | decrease | Resources spent lobbying (C-15) | CR-8c |
| C-28 | officials.enforcement | enforcement_cost | increase | Inspectors' time moved to unlicensed service and the 30-minute rule; registering transfers | CR-1 op 3; CR-8c |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Demand keeps growing about 3% a year, so at the meter rate the fixed fleet falls short of demand within about two years, and more so each year. | binding | 0.8 | Trip records; population and visitor trends; utilization of cabs. | Most medium and long consequences fail; medallions have little value. |
| A-2 | Drivers cannot simply charge above the meter on metered trips. | enforcement | 0.8 | Sealed meters; receipts; complaint data. | C-7 to C-10, C-16, C-17, C-19, C-22, C-23: the gap closes partly through higher fares instead of waits. |
| A-3 | Medallion holders and buyers expect the cap to last. | expectations | 0.75 | Council politics; history of comparable caps. | C-1, C-4, C-5, C-15, C-18, C-24, C-25 weaken. |
| A-4 | Applicants know the cap will count licenses outstanding on the effective date, and can get a license within five months. | expectations | 0.8 | Ordinance text; processing times for checks and inspections. | C-4 to C-6 fail. |
| A-5 | Refusals of hails and trips are hard to detect and punish. | enforcement | 0.75 | Complaint volumes; 12 inspectors for 2,400 cabs. | C-9 fails. |
| A-6 | Vehicle and service standards leave room above the legal minimum. | other | 0.8 | 8-year age limit; inspection content. | C-10 fails. |
| A-7 | Unlicensed service and off-meter deals often go undetected. | enforcement | 0.75 | 12 inspectors; size of the city; pick-up bans on suburban taxis hard to police. | C-11, C-12, C-21 fail. |
| A-8 | The 30-minute booking rule is loosely enforced. | enforcement | 0.6 | Inspection of booking records; fines issued. | C-14 fails. |
| A-9 | Medallion holders can organize at a cost below their stake. | other | 0.85 | Existing drivers' association; concentrated, identifiable gain. | C-15, C-27 fail. |
| A-10 | Transit and private hire are acceptable substitutes for some taxi trips. | substitutability | 0.8 | Transit coverage; private-hire fleet size. | C-13, C-20, C-25 weaken. |
| A-12 | App services take enough trips that medallion prices fall below what buyers near the peak paid. | expectations | 0.6 | Experience of cities where app services entered; medallion sale prices. | Under U1-a, C-22 and C-23 become increase. |
| A-13 | The council raises the meter rate above its index in response to medallion holders. | other | 0.35 | Council voting record on fares. | Below cut-off; not used. |
| A-N1 | Most licenses obtained in the window are put into service (driven or leased out) in the first year rather than held idle as medallions. | other | 0.6 | Vehicle inspection required for a license (a vehicle must exist); cost of holding an idle licensed vehicle; lease demand. | C-6 fails (first-year waits unchanged). |

## 11. Report

**The policy:** From the effective date, Port Halden fixes the number of taxi licenses at the number then outstanding. Licenses become medallions that can be sold or leased, with a 2% transfer fee. Fares stay at the council's meter rate, as before. Pre-booked private hire (booked at least 30 minutes ahead, fare agreed at booking) may operate with an uncapped $300 permit, but not from street hails or ranks. Twelve inspectors enforce it. Whether an app booking a few minutes ahead counts as pre-booked is undecided (U1).

**Visible consequences:** License holders on the effective date receive a valuable asset (C-1), which stays valuable in the long run (C-24). New taxi licenses stop (C-2), so the fleet is smaller than it would have been (C-3). Holders lobby to keep the cap (C-15). The city collects transfer and permit fees (C-25).

**Invisible consequences:**
- *Before the cap.* Would-be operators rush to get licenses in the five-month window (C-4), so the first-year fleet is larger than otherwise (C-5) and, if those cabs are put into service, riders wait less at first (C-6, new premise A-N1).
- *Riders.* From about the second year, riders wait longer (C-7) because more trips are wanted than cabs can serve at the meter rate (C-8). Drivers pick which fares to take (C-9), quality above the minimum declines (C-10), off-meter payments rise (C-11), and fewer taxi trips take place (C-19).
- *Unlicensed service.* More unlicensed drivers and suburban taxis pick up in the city (C-12), and riders who use them have less ability to judge and enforce quality (C-21). Private-hire operators take bookings that break the 30-minute rule (C-14).
- *Private hire and transit.* More operators enter private hire (C-13), and riders shift to private hire and transit (C-20).
- *Drivers and new entrants.* Drivers who lease pay more for the medallion (C-17). New entrants pay the medallion's price, which buys no more than a $400 license used to (C-18, C-26). Whether the number of taxi drivers falls is ambiguous (C-16): fewer cabs, but each cab may run more shifts.
- *Enforcement and lobbying.* Inspectors' time goes to new violations (C-28); lobbying uses resources (C-27).

**Ambiguous effects:** Long-run waits and the long-run shortage (C-22, C-23) depend on U1: if app bookings count as pre-booked (U1-a), app-based private hire draws riders from the taxi queue and the direction is ambiguous; if they do not (U1-b), both rise. The policy text, not this analysis, decides between the readings. Driver employment (C-16): fewer cabs against more shifts per cab; what would decide it is how far holders lease medallions for extra shifts.

**Key conditions:** The shortage chains rest on A-1 (demand outgrows the fixed fleet, 0.8) and A-2 (fares cannot rise above the meter, 0.8). Medallion values rest on A-3 (the cap is expected to last, 0.75). Evasion chains rest on A-5, A-7 (0.75) and A-8 (0.6). The first-year fall in waits needs a new premise, A-N1 (0.6).

**What this analysis cannot say:** How long waits become, how much medallions are worth, how many trips are lost, whether app services will enter at scale, or whether the policy is good. It does not weigh the gain to incumbent holders against the losses to riders and entrants. Safety effects (unlicensed rides, vehicle age) and environmental effects are not analyzed. Not reported (assumption below 0.5): a council fare rise above the index in response to holders (A-13, p 0.35).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | holders.incumbent | asset_value (medallions) | increase | short | visible | B | CR-1 op 2, op 4; CR-7c; CR-10c | A-1, A-3 |
| C-2 | sellers.prospective | entry_rate (new taxi licenses after the effective date) | decrease | medium | visible | B | CR-1 op 1; arithmetic | A-1 |
| C-3 | sellers.taxi | number_of_sellers (licensed taxis) | decrease | medium | visible | B | CR-1 op 1; arithmetic | A-1 |
| C-4 | applicants.window | entry_rate (new licenses in the five-month window) | increase | short | invisible | B | CR-10a; CR-4b (x: enter later, y: enter now) | A-3, A-4 |
| C-5 | sellers.taxi | number_of_sellers (licensed taxis in the first year) | increase | short | invisible | B | CR-10a; arithmetic | A-3, A-4 |
| C-6 | riders.taxi | wait_time | decrease | short | invisible | B | CR-9 (same market: more cabs in service) | A-4, A-N1 |
| C-7 | riders.taxi | wait_time | increase | medium | invisible | B | CR-6 (price and quantity fixed: pressure to queues) | A-1, A-2 |
| C-8 | riders.taxi | excess_demand | increase | medium | invisible | B | CR-6; arithmetic | A-1, A-2 |
| C-9 | riders.taxi | allocation_by_non_price_criteria (refusals, choice of fares) | increase | medium | invisible | B | CR-6 (criteria by which the scarce side chooses) | A-1, A-2, A-5 |
| C-10 | riders.taxi | quality_per_unit | decrease | medium | invisible | B | CR-6 (unregulated terms) | A-1, A-2, A-6 |
| C-11 | riders.taxi | side_payments (off-meter fares, demanded tips) | increase | medium | invisible | B | CR-6 (exchanges outside the rule); CR-4b (x: comply, y: violate) | A-1, A-7 |
| C-12 | sellers.unlicensed | informal_activity (unlicensed hails; suburban pickups) | increase | medium | invisible | B | CR-6; CR-1 (enforcement premise); CR-4b (x: comply, y: violate) | A-1, A-7 |
| C-13 | sellers.private_hire | entry_rate | increase | medium | invisible | B | CR-1 op 2; CR-4b (x: enter taxi service, y: enter private hire); CR-7a | A-1, A-10 |
| C-14 | sellers.private_hire | informal_activity (bookings under 30 minutes, hails) | increase | medium | invisible | B | CR-6; CR-4b (x: comply, y: violate) | A-1, A-8 |
| C-15 | lobby.medallion | lobbying_effort | increase | medium | visible | B | CR-4b (x: accept, y: lobby) | A-3, A-9 |
| C-16 | drivers.taxi | employment | ambiguous | medium | invisible | B | (−) CR-1 op 1, arithmetic; (+) CR-7a (more shifts per medallion); CR-12b | A-1, A-2 |
| C-17 | drivers.leasing | price_paid (medallion lease rate) | increase | medium | invisible | B | CR-9 (input_to); CR-7b (gain settles on the fixed means) | A-1, A-2 |
| C-18 | sellers.prospective | price_paid (medallion purchase price) | increase | medium | invisible | B | CR-9 (input_to); CR-7c; CR-1 op 3 | A-1, A-3 |
| C-19 | riders.taxi | quantity_traded (taxi trips) | decrease | medium | invisible | B | CR-5a; CR-6 | A-1, A-2 |
| C-20 | sellers.substitutes | quantity_substitute (private-hire and transit trips) | increase | medium | invisible | B | CR-9 (substitute); CR-4b (x: hail, y: book or take transit) | A-1, A-10 |
| C-21 | riders.informal | quality_information | decrease | medium | invisible | B | CR-9 (same_market_other_segment); CR-11b | A-1, A-7 |
| C-22 | riders.taxi | wait_time | U1-a: ambiguous; U1-b: increase | long | invisible | B | CR-6; U1-a: CR-9, CR-4b (app-based private hire), CR-12b | A-1, A-2, A-12 |
| C-23 | riders.taxi | excess_demand | U1-a: ambiguous; U1-b: increase | long | invisible | B | CR-6; U1-a: CR-9, CR-4b, CR-12b | A-1, A-2, A-12 |
| C-24 | holders.incumbent | asset_value (medallions) | increase | long | visible | B | CR-7c; CR-10c | A-1, A-3 |
| C-25 | government.city | tax_revenue (transfer and permit fees) | increase | medium | invisible | B | CR-1 op 4; CR-8b | A-1, A-3, A-10 |
| C-26 | sellers.prospective | resources_available_other_uses | decrease | medium | invisible | B | CR-8a, CR-8b; CR-7c | A-1, A-3 |
| C-27 | lobby.medallion | resources_available_other_uses | decrease | medium | invisible | B | CR-8c | A-3, A-9 |
| C-28 | officials.enforcement | enforcement_cost | increase | medium | invisible | B | CR-1 op 3; CR-8c | A-1, A-7 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, the foundations and arithmetic. The joint effect of a fixed quantity (K1) and an existing fixed price (R1) was handled by CR-6.

**(b) New premises.**
- A-N1 (p 0.6): C-6. CR-10a gives the rush for licenses in the window (C-4), but whether it shortens first-year waits depends on whether window licenses are put into service or held idle as medallions for their value. No case assumption covers this.

**(c) Unclear core rules.**
- CR-6 is stated for a rule that prevents the price from moving. Here the price is held by an existing rule (R1) and the policy fixes the quantity (K1). CR-6 applies on the reading that the price rule may be one already in force, which the policy makes bind; the rule does not say so.
- CR-7c ("borne or captured by whoever owns it when the change becomes expected") presupposes that the asset already exists. Medallions are created by the ordinance; the rule had to be read as "whoever is granted the asset when the change becomes expected", which here includes window entrants.
- CR-1: the conversion of an existing license into a transferable medallion is both op 2 (the option to sell or lease) and op 4 (a transfer of means). The rule does not say whether one provision may be recorded under two operations.
- CR-7a and CR-7b both bear on driver employment (C-16): CR-7b says the scarcity return settles on medallions, and CR-7a says the medallion is moved into more hours of use. The rules give no way to sign the net effect on the number of drivers; reported as ambiguous under CR-12b.
- CR-12b refers to "a dominance pattern" for a dominance claim. The short-horizon wait (C-6) used A-1's timing ("within about two years") as the reason no opposing chain applies in year one; the core rules do not say whether a timing premise counts as a dominance premise.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure. The cap together with the existing meter rate produces a shortage, not a higher fare, and the shortage grows as demand grows. It shows up as waiting, drivers choosing their fares, lower quality, off-meter payments and unlicensed service. Medallions gain value at announcement, and the gain goes to holders on the effective date. Licenses are rushed in the window. Entry falls. Private hire stretches the 30-minute rule. Long-run waits depend on U1: ambiguous under U1-a, increase under U1-b, in both versions. There are no opposite signs. The most substantive difference is one the pattern version gets wrong: it signs private-hire fares as an increase (PC-8), ignoring the opposing chain that PC-8's own note names. Would-be taxi entrants shut out by the cap flow into the uncapped private-hire segment and add supply there. The core version records that entry (C-13) and the demand shift (C-20), and by CR-12b their combination leaves `price_substitute` ambiguous. The core version in turn omits several consequences that the core rules derive without difficulty: informal riders' search costs and disputes, the medallion-loan market, excluded entrants' earnings, riders' full cost, app-service entry, and later buyers' losses under U1-a, which it wrongly treats as a path note. It also adds a defensible first-year fall in waits from the window rush, on a new premise (A-N1).

**Counts.** M 15, V 4, S 0, OP 6, OC 9. Causes over S, OP and OC (15 items): P 1, K 0, A 1, E 11, J 2.

**Pattern version → core version**

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
|---|---|---|---|---|
| C-1 | C-3 | M | | |
| C-2 | C-1, C-18 | M | | The core version adds the buyer side (C-18: later entrants pay the capitalized price). |
| C-3 | C-4, C-5 | M | | |
| C-4 | C-2 | M | | |
| C-5 | C-8 | M | | |
| C-6 | C-7 | M | | |
| C-7 | C-9 | M | | |
| C-8 | C-10 | M | | |
| C-9 | C-11 | M | | |
| C-10 | C-12 | M | | |
| C-11 | C-14 | V | | Back-dated and short-notice bookings: `reclassification` in the pattern version, `informal_activity` in the core version. Back-dating breaks the rule, so the core version's variable is the more exact. |
| C-12 | C-15 | M | | |
| C-13 | C-17 | V | | The holders' lease income and the lessees' higher lease rate: the same transfer, seen from the two sides. |
| C-14 | C-20 | V | | Actor class `riders` vs `sellers.substitutes`. |
| C-15 | none | OC | P | Pattern: `price_substitute` (private-hire fares) increase, by PC-8. **Overclaim.** PC-8's note names the opposing chain: resources shut out of the capped segment reappear in the uncapped one (RS-13). Here would-be taxi entrants move into uncapped private hire at a $300 permit (core C-13), adding supply as riders add demand (core C-20). By CR-12b, private-hire fares are `ambiguous`. The core version is right not to sign them, although it should have recorded the ambiguous row explicitly. |
| C-16 | none | OC | E (core) | Unlicensed cabs cannot advertise (CR-11b). The core version records only `quality_information`. |
| C-26 | C-21 | M | | |
| C-27 | none | OC | E (core) | Disputes with unlicensed drivers settled without courts (CR-11b names courts explicitly). |
| C-17 | none | OC | E (core) | Medallion loans rise. CR-9 (`complement`) with the core version's own C-18 derives it. |
| C-18 | (C-17, lease rate) | OC | J | Lessees' earnings ambiguous. The core version records the lease rate rising and, by CR-7b, the scarcity return settling on the medallion, which implies lessees earn no lasting premium. That is consistent with the pattern version's "lease fees absorb most". Not recording lessees' earnings is a defensible choice. |
| C-19 | C-22, C-23 | M | | Same per-reading signs. |
| C-20 | none | OC | E (core) | App services' legal entry: U1-a increase, U1-b decrease, against an open-entry counterfactual in which they could take $400 licenses. CR-4b derives it under each reading. The core version uses app services only as a chain inside C-22 and C-23. |
| C-21 | C-24 | M | | |
| C-22 | (section 8 note) | OC | E (core) | Later buyers' earnings after loan payments, compared with driving under open entry: U1-a decrease. The core version calls it "a note on the path", but the comparison is with the counterfactual, so it is a consequence. CR-7c (the buyer paid the capitalized value) with erosion under U1-a gives the sign. |
| C-23 | C-19 | M | | |
| C-24 | none | OC | E (core) | Would-be entrants take next-best work at lower earnings. CR-3a and CR-4 derive it from the core version's own C-2. |
| C-25 | C-28 | V | | Funding side vs spending side. |
| C-28 | none | OC | E (core) | Riders' full cost per trip rises: waiting and side payments rise, and the meter fare is unchanged against the counterfactual, so no chain opposes. Arithmetic on the core version's own C-7 and C-11. |

**Core-only consequences**

| Core ID | Class | Cause | Note |
|---|---|---|---|
| C-6 | OP | A | First-year waits fall because window licenses add cabs. Needs A-N1 (window licenses are put into service, p 0.6). The chain is valid: CR-10a, and a vehicle must pass inspection to be licensed. The pattern version noted the larger initial fleet but signed nothing for riders in the short run. |
| C-13 | OP | E (pattern) | Entry into private hire rises (CR-4b: taxi entry closed, private hire open). This is the chain the pattern version needed to see that its C-15 is ambiguous. |
| C-16 | OP | E (pattern) | Number of taxi drivers ambiguous: fewer cabs, but holders run each medallion for more shifts (CR-7a). A valid point the pattern version missed; EN-3 covers only excluded entrants. |
| C-25 | OP | E (pattern) | Transfer and permit fees rise. The pattern version omitted city fee revenue. Caveat: the variable is defined narrowly. If annual license fees are still charged, the smaller fleet yields less of them, so total fee revenue would be `ambiguous` (CR-12b). The core version should have said so. |
| C-26 | OP | J | Later entrants' `resources_available_other_uses` decrease (the medallion price is a transfer to incumbents, CR-8b). Defensible as the buyer side of a capitalized asset (OC-7 in its 0.4 form says to record it). The core version's gloss ("buys no more than a $400 license would have") overstates it, though: by CR-7c the price buys the rent stream, so later buyers neither gain nor lose by their own ranking. |
| C-27 | OP | E (pattern) | Resources used up in lobbying (CR-8c). A minor omission. |

**Findings**
- Pattern misapplied, with a design weakness in the pattern: PC-8 is applied to private-hire fares as an unconditional increase, although its own note names the opposing supply chain (RS-13), which is active here because the cap itself pushes entrants into the uncapped segment. PC-8's Then clause should carry this as an Unless clause, or as a condition for using RS-13 together with it: "where the cap excludes sellers who can enter the uncontrolled segment, the price there is `ambiguous`".
- Errors in the pattern version: besides C-15, it omits private-hire entry (C-13), the ambiguous count of taxi drivers (C-16), fee revenue (C-25) and the cost of lobbying.
- Errors in the core version: it omits RS-10-type effects that CR-11b derives (search cost, disputes), medallion loans, excluded entrants' earnings, full cost per trip and app-service entry. It treats later buyers' losses under U1-a as a path note, misreading 2.5. Its fee-revenue sign (C-25) holds only under a narrow variable. Its gloss on C-26 conflicts with its own CR-7c reading in C-18.
- Limits of the core rules: none. The joint effect of a cap and an existing price rule was handled by CR-6, and the core version's note that CR-6 should say it covers an existing price rule which the policy makes bind is a fair request to clarify the wording.
