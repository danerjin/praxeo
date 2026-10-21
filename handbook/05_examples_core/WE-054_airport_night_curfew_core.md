# WE-054 / Analysis: Airport night curfew with a daytime slot cap and slots allocated by history

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Wexcombe Airport Night Curfew and Slot Order.** Wexcombe International Airport (WXI) is run by the Wexcombe Airport Authority (WAA), a public authority that sets the airport's operating rules and cost-recovery charges. In summer 2025 WXI handled about 420 movements a day: about 380 between 06:00 and 23:00 and about 40 between 23:00 and 06:00 (about 22 an express parcel carrier's night sort, the "integrator"; about 6 other cargo; about 12 passenger flights, 8 late arrivals scheduled 23:00 to 00:30 and 4 early departures 05:15 to 05:55). About 6 further movements a night are daytime flights running late into 23:00 to 00:00, and about 1 after midnight. Declared runway capacity is 34 movements an hour (existing rule); the peaks run at 30 to 34, 06:00 to 07:00 at about 10 and 22:00 to 23:00 at about 12. Daytime movements have grown about 3% a year, night cargo about 5%. Fourteen airlines operate by day; the three largest operate about 60% of daytime movements. Aircraft average about 150 seats; fleets turn over in two to four years; three gates take wide-bodied aircraft. About 11,000 people work on site (about 900 in the integrator's night sort); about 30% live within 8 km. About 9,000 homes (median $310,000) lie inside the WAA's night-noise contour. WAA charges average about $2,000 per movement (about $13 per seat) and are set each year to recover mostly fixed costs. The noise office costs about $0.5 million a year; the slot unit and curfew monitoring about $2.8 million. Pellham Regional Airport (70 km, 55 minutes by motorway) has no curfew and uses about 45% of its runway capacity; about 1,200 homes would fall in a Pellham night contour if night cargo moved there, within a commuting area of about 40,000 homes. Wexcombe's region is about 4% of a national overnight parcel market.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | WXI only. Pellham Regional (70 km) has no curfew and spare capacity. | "This Order applies to aircraft movements at Wexcombe International Airport." |
| Announced / enacted / effective / expires | Draft with base seasons 2 March 2026 (after a residents' campaign since 2023); adopted 15 September 2026; slots issued 1 September 2027; curfew and cap from 31 October 2027; review 2032; no expiry. | Order, art. 1 and 12. |
| Enforcement (who, penalties, resources) | WAA, from air traffic control's movement log. $50,000 per curfew movement without a dispensation; $10,000 per daytime movement without a slot; slots of a holder fined three times in a season may be withdrawn. Funded from airport charges. | Order, art. 9 to 11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Curfew | `prohibition` | Takeoffs and landings 23:00 to 06:00 | All operators at WXI | None permitted, subject to U1. | Emergencies, medical and state flights. |
| K2 Daytime cap | `quota` | Movements 06:00 to 23:00 | All operators at WXI | 380 a day (the summer 2025 number); the hourly limit of 34 stays. | As K1. |
| K3 Allocation by history | `rights_allocation` | The 380 daily slots | WAA | Issued free in proportion to daytime movements operated in summer 2026 and winter 2026/27, each slot in the hour of the movement that earned it. | - |
| K4 Trading | Rule on transfers | Slots | Slot holders | Slots may be sold, leased and retimed to another daytime hour where the hourly limit leaves room. | - |
| K5 Freed slots | `rights_allocation` | Slots returned to the WAA | WAA | Slots of a holder that ceases to operate, or uses a slot on fewer than 80% of a season's days, return and are reissued free, first to night operators in proportion to their winter 2026/27 night movements, then to new entrants. | - |
| K6 Enforcement and funding | Enforcement | K1 to K5 | WAA | Penalties as above; costs recovered through the annual charges. | - |

Existing rules, kept in the counterfactual: the hourly limit of 34; the WAA's cost-recovery charge method.

Counterfactual: WXI without the order: no curfew, no cap, no slots; daytime movements growing to about 409 a day by winter 2027/28 and about 440 by 2030 (A-1); night movements growing; the residents' campaign continuing.

Unclear provisions:
- U1, late-running flights. K1 permits "a flight scheduled to operate before 23:00 and delayed by circumstances beyond the operator's control" to operate at the duty manager's discretion; the explanatory note says "until midnight". U1-a: a delayed flight scheduled before 23:00 may operate until 00:00 as of right. U1-b: no dispensation for ordinary delays; a late flight diverts (in practice to Pellham) or is cancelled.

Horizons used: short = from the draft (2 March 2026) to the start of the order (31 October 2027), including the base seasons; medium = the first seasons under the order, to about 2030; long = after 2030.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Curfew | triangular (prohibits exchanges between operators and their night customers, and between operators and the WAA for night runway use) | Yes: removes about 40 scheduled night movements (A-2); for operators who would pay the penalty, a risk (A-14) | 1 (night movements removed where enforced); 3 ($50,000 penalty attached to the option where an operator would pay it) | CR-3a, CR-4, CR-5a, CR-6, CR-7c, CR-9, CR-10a |
| K2 Daytime cap | triangular (limits daytime exchanges at WXI) | Binding from winter 2027/28 because counterfactual movements exceed 380 (A-1) | 1 (movements beyond 380 removed); 3 ($10,000 penalty attached to unslotted movements) | CR-4, CR-6 (fixed quantity clause), CR-7, CR-9 |
| K3 Allocation by history | binary (the state gives a created right) | Yes (A-1: the right has value only because K2 binds) | 4 (a valuable right transferred free to airlines with base-season history); 3 before the base seasons (an extra daytime movement in a base season brings a share of slots) | CR-7c (asset created by the policy; claims before creation), CR-8b, CR-8c, CR-10a |
| K4 Trading | triangular (permits exchanges of slots) | Yes where a slot market forms (A-4) | 2 (option to sell, lease, buy and retime slots) | CR-5, CR-6, CR-7a |
| K5 Freed slots | binary (contingent free reissue) | Yes as far as slots are freed (A-N1) | 4 (a contingent claim to freed slots transferred to night operators); 3 (loss of a slot attached to under-use or ceasing for holders) | CR-7c, CR-8b, CR-4 |
| K6 Enforcement and funding | binary (costs recovered from charge payers) | Yes | 4 (costs passed to all charge payers through the existing charge method) | CR-8a, CR-8c |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| operators.night | The integrator, two other cargo carriers, and airlines with night passenger flights | Op 1 (K1); op 3 where they would pay the penalty (A-14); op 4 (K5 claim). |
| operators.night.integrator | Express parcel carrier running the night sort | Op 1 on night movements; its WXI sort hall loses its use (A-16). |
| airlines.slot_holders | Airlines with base-season daytime history | Op 4 (K3 free slots); op 1 (no growth beyond their slots); op 2 (K4 sell or lease); op 3 (K5 loss on under-use). |
| airlines.daytime | All airlines operating by day at WXI | Op 1 above 380; op 3 penalty on unslotted movements; compliance with slot rules. |
| airlines.prospective | Would-be entrants | Op 1: no free capacity; must buy or lease slots, and come after night operators under K5. |
| travelers.wxi | Passengers flying from WXI | Through CR-9: fewer seats than the counterfactual, at higher fares. |
| travelers.wxi.night | Passengers on night passenger flights | Op 1 for their night flights, through CR-9. |
| travelers.wxi.late | Passengers on daytime flights running late | U1-a: none; U1-b: their late flight diverts or is cancelled. |
| travelers.pellham | Passengers using Pellham, including those who move there | Through CR-9 (substitute): more demand at Pellham. |
| shippers.wexcombe | Senders of overnight parcels in the Wexcombe region | Through CR-9 (input_to): the sort moves 70 km away. |
| haulage.wexcombe_pellham | Road hauliers | Through CR-9 (input_to): trucking between Wexcombe and Pellham. |
| workers.wxi | Airport and airline staff at WXI, including the 900 night-sort workers | Through CR-9 (input_to): fewer movements and no night sort. |
| workers.pellham | Staff at Pellham | Through CR-9: added movements and the sort. |
| airport.pellham | Pellham's authority and operators there | Through CR-9 (substitute): more movements. |
| sellers.concessions_wxi | Shops, food and parking at WXI | Through CR-9 (complement, trip): fewer passengers. |
| homeowners.near_wxi | Owners of homes near WXI, including the 9,000 in the night contour | Through CR-9: proximity (quieter nights; Tier C) and location complement (fewer airport workers). |
| homeowners.pellham | Owners in Pellham's commuting area, including the 1,200 under a new night path | Through CR-9: proximity (night noise; Tier C) and location complement (hub workers). |
| officials.waa | Administers K1 to K6; sets charges | Op 3: tasks; receives penalties; charges reset under the existing method. |
| residents.wxi_associations | The residents' campaign | Their campaign's goal is met; the order may be reviewed in 2032 and U1 is disputed. |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1 to K3 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | operators.night | quantity_supplied (scheduled movements 23:00 to 06:00 at WXI) | decrease | medium; long | CR-1 op 1, CR-4b | A-2 |
| C-2 | airlines.daytime | quantity_traded (daytime movements at WXI) | decrease | medium; long | CR-1 op 1, CR-6 | A-1, A-2 |
| C-3 | airlines.slot_holders | asset_value (WXI slots) | increase | short (from the draft); medium; long | CR-1 op 4, CR-7c, CR-10c | A-1, A-3 |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-6 for the fixed quantity; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-4 | airlines.daytime | quantity_supplied (off-peak daytime movements in summer 2026 and winter 2026/27) | increase | short (base seasons) | CR-10a, CR-7c, CR-4 | A-5 |
| C-5 | airlines.slot_holders | right_lease_price (WXI slots) | increase | medium; long | CR-6, CR-12 | A-1, A-4 |
| C-6 | airlines.slot_holders | quantity_traded (slot sales and leases) | increase | medium; long | CR-1 op 2, CR-5, CR-7a, CR-12 | A-4, A-10 |
| C-7 | airlines.daytime | unit_size (seats per movement at WXI) | increase | medium; long | CR-4, CR-10b | A-8, A-1 |
| C-8 | operators.night | quantity_supplied (movements 06:00 to 07:00) | increase | medium; long | CR-4, CR-1 op 2 | A-7, A-4 |
| C-9 | operators.night, airlines.daytime | quantity_supplied (movements 22:00 to 23:00) | U1-a: increase; U1-b: ambiguous | medium; long | CR-4, CR-12b | A-7, A-4, A-24, A-23 |
| C-10 | airlines.daytime | quantity_supplied (late-running movements 23:00 to 00:00) | U1-a: increase; U1-b: decrease | medium; long | CR-1, CR-4 | A-24, A-2 |
| C-11 | operators.night.integrator | quantity_supplied (night sort and cargo movements at Pellham) | increase | medium; long | CR-4 (x: here, y: there), CR-7a | A-6 |
| C-12 | operators.night.integrator | asset_value (WXI sort facility) | decrease | short; medium | CR-7c, CR-10c, CR-7b | A-6, A-16 |
| C-13 | operators.night | asset_value (claim to freed slots under K5) | increase | short; medium | CR-1 op 4, CR-7c, CR-10c | A-N1 |
| C-14 | operators.night | asset_value (WXI night businesses, total) | ambiguous | short; medium | CR-12b (two items, 0.8) | A-6, A-16, A-N1 |
| C-15 | operators.night | legal_breach (curfew movements without dispensation) | increase | medium; long | CR-4 (x: comply, y: violate), CR-12 | A-14, A-2 |
| C-16 | airlines.prospective | entry_rate (new airlines at WXI) | decrease | medium; long | CR-1 op 1, CR-4 (x: stay out, y: enter), CR-6 | A-1, A-4 |
| C-17 | operators.night, airlines.slot_holders, airlines.prospective | lobbying_effort (on the curfew, U1, slot rules and the 2032 review) | increase | medium; long | CR-4 (x: accept, y: lobby), CR-10a, CR-8c | A-15, A-3 |
| C-18 | residents.wxi_associations | lobbying_effort | ambiguous | medium; long | CR-4, CR-12b | A-15 |
| C-19 | officials.waa | enforcement_cost | increase | medium; long | CR-1 op 3, CR-8c | - |
| C-20 | airlines.daytime, operators.night | compliance_cost (slot coordination, records) | increase | short; medium | CR-1 op 3, CR-8c | - |
| C-21 | officials.waa | non_tax_receipts (penalties) | increase | medium; long | CR-8b | A-14, A-2 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Effects on the national parcel price (A-18, p 0.15) and on Pellham fares through a cost increase (A-19, p 0.35) are not reported. Effects on firms that buy from WXI concessions, and on customers of shippers, are pruned at depth 3 as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-22 | airlines.daytime, operators.night | price_paid (WAA charges per movement) | increase | medium; long | CR-9, CR-8b, CR-12b, CR-12e | WAA runway and terminals shared_facility; existing cost-recovery rule | A-13, A-1, A-N2 |
| C-23 | airlines.slot_holders | net_price_received (per seat, net of charges) | increase | medium; long | CR-6, CR-7b, CR-12b, CR-12e | - | A-1, A-9, A-26, A-13 |
| C-24 | travelers.wxi | price_paid (fares at WXI) | increase | medium; long | CR-6, CR-9, CR-12e | slot input_to seats sold (close) | A-1, A-9 |
| C-25 | travelers.wxi | quantity_traded (seats flown at WXI) | decrease | medium; long | CR-4c, CR-6 | as above | A-1, A-9 |
| C-26 | travelers.wxi | price_paid (off-peak fares in the base seasons) | decrease | short (base seasons) | CR-9, CR-6 | added off-peak flights same market | A-5 |
| C-27 | travelers.pellham | price_substitute (+), quantity_substitute (+) (flights from Pellham) | at_least_one_increase | medium; long | CR-9, CR-6 (splitting a shift) | Pellham flights substitute for WXI flights (partial) | A-11, A-1, A-9 |
| C-28 | travelers.wxi | travel_time (Wexcombe-area travelers who use Pellham) | increase | medium; long | CR-4 (x: WXI, y: Pellham), CR-9 | as above | A-11, A-1, A-9 |
| C-29 | travelers.wxi.late | travel_time (late flights diverted to Pellham) | U1-a: no_change; U1-b: increase | medium; long | CR-1 op 1 (U1-b), CR-4 | across_border (Pellham) | A-2 |
| C-30 | travelers.wxi.night | quantity_traded (night passenger flights from WXI) | decrease | medium; long | CR-5a, CR-1 op 1 | - | A-27, A-2 |
| C-31 | airport.pellham | quantity_traded (movements at Pellham) | increase | medium; long | CR-9, CR-6 | Pellham substitute for WXI (partial) | A-6, A-11 |
| C-32 | shippers.wexcombe | quality_per_unit (overnight parcel service: collection cut-off) | decrease | medium; long | CR-9, CR-6 | sort location input_to overnight delivery (close) | A-6, A-17 |
| C-33 | haulage.wexcombe_pellham | quantity_traded (road haulage Wexcombe to Pellham) | increase | medium; long | CR-9, LW-10 | road haulage input_to the relocated sort (close) | A-6 |
| C-34 | workers.wxi | employment (night sort at WXI) | decrease | medium; long | CR-9, LW-10 | labor input_to the sort (close) | A-6, A-25 |
| C-35 | workers.wxi | employment (WXI, all movements) | decrease | medium; long | CR-9, LW-10 | labor input_to movements (close) | A-1, A-25 |
| C-36 | workers.pellham | employment (Pellham sort and movements) | increase | medium; long | CR-9, LW-10, CR-7a | labor input_to the sort (close) | A-6 |
| C-37 | sellers.concessions_wxi | quantity_traded (concession sales) | decrease | medium; long | CR-9 | concessions complement (trip) of flights | A-21, A-1, A-9 |
| C-38 | homeowners.near_wxi | asset_value (homes), not counting effects through proximity | decrease | medium; long | CR-9, CR-7c, CR-10c | homes complement (location) of WXI jobs | A-12, A-6, A-25 |
| C-39 | homeowners.near_wxi | asset_value (homes in the night contour), combined | ambiguous | short; medium; long | CR-9, CR-7c, CR-12 (0.9, Tier C against Tier B) | proximity; complement (location) | A-22, A-12, A-6 |
| C-40 | homeowners.pellham | asset_value (homes), not counting effects through proximity | increase | medium; long | CR-9, CR-7c, CR-10c | homes complement (location) of Pellham jobs | A-12, A-6 |
| C-41 | homeowners.pellham | asset_value (homes in the prospective night contour), combined | decrease | short; medium; long | CR-9, CR-7c, CR-12 (0.9), CR-12e | proximity; complement (location) | A-20, A-6, A-12 |
| C-42 | travelers.wxi | resources_available_other_uses (travelers who keep flying from WXI) | decrease | medium; long | CR-3, CR-8a | - | A-1, A-9 |
| C-43 | airlines.slot_holders | resources_available_other_uses | increase | medium; long | CR-8b, CR-7b | - | A-1, A-9, A-26 |
| C-44 | airlines.daytime | resources_available_other_uses (airlines that added base-season movements) | decrease | short (base seasons) | CR-7c (0.7, claims before creation), CR-8c | - | A-5 |
| C-45 | operators.night.integrator | resources_available_other_uses | decrease | medium; long | CR-3c, CR-8a | - | A-6, A-17 |
| C-46 | operators.night | resources_available_other_uses (operators that pay penalties) | decrease | medium; long | CR-8b, CR-3c | - | A-14, A-2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| airlines.daytime, quantity of daytime movements, short against medium | base seasons: extra off-peak movements to earn history (C-4) | from 31 October 2027: cap below counterfactual growth (C-2) | Different windows: not combined (CR-12g) | increase (base seasons); decrease (medium; long) |
| travelers.wxi, price_paid, medium; long | scarcity under the cap (CR-6); higher WAA charges (C-22) | larger aircraft lower cost per seat (C-7); some demand moves to Pellham (C-27) | CR-12e response argument: larger aircraft and Pellham are responses to the scarcity and cannot reverse it; A-9 states they are partial (0.9 note) | increase (C-24) |
| airlines.slot_holders, net_price_received, medium; long | scarcity premium per seat (CR-6, CR-7b) | higher WAA charges per seat (C-22) | A-26 (p 0.75): the premium exceeds the charge rise (about $2 per seat by 2030) | increase (C-23) |
| airlines and operators, price_paid (WAA charges), medium; long | fixed costs over fewer movements (A-13, A-1); K6 costs (C-19) | penalty receipts credited to costs (C-21) | A-N2 (p 0.8): penalty receipts are far smaller than the shortfall from fewer movements (arithmetic on the record: about $300 more per movement on about 140,000 movements a year against $50,000 per occasional violation) | increase (C-22) |
| movements 22:00 to 23:00, medium; long | night operators buy or lease slots into the shoulder (A-7); U1-a: flights scheduled just before 23:00 (A-24) | U1-b: airlines move 22:00 flights earlier as a buffer (A-23) | None | U1-a: increase; U1-b: ambiguous (C-9) |
| operators.night, asset_value, short; medium | K5 claim to freed slots (C-13) | WXI night business and sort hall lose their use (C-12) | None | ambiguous (C-14); the two items are reported separately (CR-12, 0.8 note) |
| homeowners.near_wxi (night contour), asset_value | quieter nights (proximity, Tier C, A-22) | fewer airport workers seeking homes nearby (Tier B, A-12, A-6, A-25) | None | Tier B: decrease, not counting proximity (C-38); Tier C combined: ambiguous (C-39) |
| homeowners.pellham (night contour), asset_value | more hub workers seeking homes (Tier B, A-12, A-6) | night noise (proximity, Tier C) | A-20 (p 0.6): the noise discount exceeds the added demand in the contour | Tier B: increase, not counting proximity (C-40); Tier C combined: decrease (C-41) |
| residents.wxi_associations, lobbying_effort | defending the curfew at the 2032 review and on U1 | the campaign's goal is met | None (the counterfactual campaign continues) | ambiguous (C-18) |
| workers.wxi, employment, medium; long | none derived | fewer movements than the counterfactual and no night sort (C-34, C-35) | - | decrease. Larger aircraft may need more staff per movement; no case premise supports that chain, so it is a Tier C note (CR-12, 0.7 note) |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement and base seasons (2 March 2026 to spring 2027).** The draft named the base seasons, so an extra daytime movement in summer 2026 or winter 2026/27 brought a share of future slots (CR-10a; CR-7c, claims before creation). Airlines for whom that share was worth more than the cost of the flight added off-peak movements (C-4, A-5), off-peak fares fell in those seasons (C-26), and part of the slots' value was used up in the race (C-44, CR-8c). Night operators could have added daytime movements to earn history too; that needs A-28 (p 0.35) and is not reported.
- **Capitalization.** Slot values (C-3) were capitalized as the order became expected: in part from the draft, more at adoption on 15 September 2026, with the full value on issue on 1 September 2027 (CR-7c, probability clause). A-3 (holders expect slots to last past 2032) supports the value; a reallocation at the review would lower it. The integrator's sort hall (C-12) loses value on the same path. Home values near the two airports (C-38 to C-41) move as the curfew and the move of the sort become expected, before the night flights stop.
- **Durability.** Larger aircraft arrive only as fleets turn over (two to four years) and wide-body gates are few (C-7, A-8), so the scarcity premium (C-5, C-23, C-24) is largest in the first seasons. The cap is fixed at 380 while counterfactual demand grows about 3% a year (A-1), so the cap binds more each year: about 7% below the counterfactual in winter 2027/28 and about 13% by 2030.
- **Use rule.** K5's 80% use rule attaches the loss of a slot to under-use (CR-1 op 3), so holders lease out slots they would leave idle (C-6) or fly them on thin routes. Against a counterfactual without slots this has no variable to sign; it is a note.
- **Review.** The 2032 review keeps lobbying alive (C-17, C-18) and makes the slot value depend on expectations about it (CR-10a).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-17 | operators.night, airlines.slot_holders, airlines.prospective | lobbying_effort | increase | Staff time and money spent on the curfew, U1, the slot rules and the review | CR-4, CR-8c |
| C-19 | officials.waa | enforcement_cost | increase | About $2.8 million a year of slot coordination and monitoring, recovered from charge payers | CR-1 op 3, CR-8c |
| C-20 | airlines.daytime, operators.night | compliance_cost (slot coordination, records) | increase | Staff time spent on slot records and filings | CR-1 op 3, CR-8c |
| C-25 | travelers.wxi | quantity_traded (seats flown at WXI) | decrease | Trips not taken from WXI that travelers and airlines each expected to gain from | CR-5a, CR-4c |
| C-30 | travelers.wxi.night | quantity_traded (night passenger flights from WXI) | decrease | Night trips that would have been taken | CR-5a |
| C-42 | travelers.wxi | resources_available_other_uses | decrease | Purchases forgone by travelers who keep flying at higher fares | CR-3, CR-8a |
| C-44 | airlines.daytime | resources_available_other_uses | decrease | Costs of flights added only to earn slot history | CR-7c, CR-8c |
| C-45 | operators.night.integrator | resources_available_other_uses | decrease | Trucking and the second facility needed to run the sort from Pellham | CR-3c, CR-8a |
| C-46 | operators.night | resources_available_other_uses | decrease | Penalties paid for curfew movements | CR-8b, CR-3c |

CR-8 symmetry: the free slots (C-3) are a transfer to holders whose payers are travelers who keep flying at the scarcity fares (C-24, C-42) and airlines that buy or lease slots (C-5); the penalties (C-46) are received by the WAA (C-21); the WAA's costs (C-19) are paid by charge payers (C-22).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Without the order, daytime movements would grow above 380 a day (about 3% a year), and off-peak runway capacity allows it. | counterfactual_trend | 0.85 | Growth 2015 to 2025; airlines' published plans; hourly use. | C-2, C-3, C-5, C-7, C-16, C-22 to C-25, C-27, C-28, C-35, C-37, C-42, C-43 fail. |
| A-2 | The WAA detects every movement from air traffic control's log and imposes penalties. | enforcement | 0.9 | Movement logs are complete; penalties are administrative. | C-1, C-2, C-10, C-15, C-21, C-29, C-30, C-46 fail. |
| A-3 | Holders expect slots to last past the 2032 review without reallocation. | expectations | 0.7 | Order art. 12; practice at other slot-controlled airports. | C-3 smaller; C-17 loses the holders' stake. |
| A-4 | A slot market forms: slots are sold, leased and retimed at low transaction cost. | other | 0.75 | K4; slot markets at other capped airports. | C-5, C-6, C-8, C-9, C-16 fail. |
| A-5 | Airlines expected base-season history to set their share, and some could add off-peak daytime movements at a cost below the expected value of the extra slots. | expectations | 0.8 | The draft named the base seasons; off-peak capacity; expected slot values. | C-4, C-26, C-44 fail. |
| A-6 | The integrator moves most of its night sort to Pellham, and other night cargo follows. | mobility | 0.7 | Pellham's spare capacity, no curfew; the sort needs night hours. | C-11, C-12, C-31 to C-34, C-36, C-38 to C-41, C-45 fail. |
| A-7 | Some night operators buy or lease daytime slots and fly in the shoulder hours. | substitutability | 0.7 | Passenger night flights' timing needs; shoulder capacity. | C-8, C-9 fail. |
| A-8 | Airlines can move to larger aircraft on some WXI routes within the medium horizon. | other | 0.7 | Fleet plans; three wide-body gates. | C-7 fails. |
| A-9 | Larger aircraft and Pellham together cannot carry all of the counterfactual growth at the old cost (the responses are partial). | other | 0.8 | Fleet lead times; gate limits; 55 minutes to Pellham. | C-23 to C-25, C-27, C-28, C-37, C-42, C-43: price could return to its old level. |
| A-10 | Airlines differ in the value they get from a WXI slot. | other | 0.8 | Network and point-to-point carriers; aircraft sizes. | C-6 fails. |
| A-11 | Some travelers find Pellham a substitute. | substitutability | 0.7 | Motorway access; catchment surveys. | C-27, C-28, C-31 fail. |
| A-12 | Airport workers' housing demand is a material part of demand for homes near each airport, including the contours. | other | 0.6 | 30% of WXI workers live within 8 km; commuting patterns at Pellham. | C-38 to C-41 fail. |
| A-13 | The WAA sets charges to recover costs that are largely fixed. | other | 0.75 | Charging policy and accounts. | C-22, C-23 fail. |
| A-14 | Some operators sometimes operate after the permitted time and pay the penalty. | enforcement | 0.55 | Penalty against a stranded aircraft or missed sort; other curfews. | C-15, C-21, C-46 fail. |
| A-15 | Night operators, slot holders, would-be entrants and residents' associations can organize at a cost below their stake. | other | 0.85 | Hearing records 2026; residents' campaign since 2023. | C-17, C-18 fail. |
| A-16 | The integrator's WXI sort facility has no equally valuable other use. | alternative_uses | 0.7 | Purpose-built airside hall. | C-12, C-14 fail. |
| A-17 | With the sort 70 km away, collection cut-offs in Wexcombe move earlier. | other | 0.65 | Trucking time to Pellham; network times. | C-32, C-45 fail. |
| A-18 | The move of Wexcombe's sort raises the national price of overnight parcel delivery by more than a negligible amount. | other | 0.15 | Wexcombe is 4% of the market and still served. | Not reported. |
| A-19 | Airlines cannot add flights at Pellham at unchanged cost, so Pellham fares rise. | other | 0.35 | Pellham 45% used; aircraft are mobile. | Not reported; C-27 kept as a group. |
| A-20 | In Pellham's prospective night contour, the discount buyers place on night noise exceeds the added demand from hub workers. | other | 0.6 | 900 hub jobs over 40,000 homes; 1,200 homes under the night path; hedonic studies. | C-41 becomes ambiguous. |
| A-21 | Concession sales follow passenger numbers. | other | 0.8 | Concession accounts. | C-37 fails. |
| A-22 | Buyers of homes in a night-noise contour value quieter nights, so night movements are capitalized in home prices. | other | 0.85 | Hedonic studies; the residents' campaign. | C-39 becomes decrease at Tier C. |
| A-23 | Under U1-b, airlines move some flights scheduled 22:00 to 23:00 earlier to keep a buffer against delays. | expectations | 0.65 | Delay distributions; diversion costs. | C-9 under U1-b becomes increase. |
| A-24 | Under U1-a, airlines schedule some flights just before 23:00 knowing they will often operate after it. | other | 0.6 | Practice at curfewed airports with a delay allowance. | C-9 and C-10 under U1-a lose this chain. |
| A-25 | Employment and hours at WXI follow movements and the night sort. | alternative_uses | 0.8 | Staffing per movement; sort shifts. | C-34, C-35, C-38 fail. |
| A-26 | The scarcity premium per seat exceeds the rise in WAA charges per seat (about $2 by 2030). | other | 0.75 | Fare premiums at capped airports against the charge arithmetic. | C-23, C-43 become ambiguous. |
| A-27 | Some night services are neither moved to the shoulders nor to Pellham. | other | 0.7 | Late passenger flights on thin routes; ad hoc charters. | C-30 fails. |
| A-28 | Night operators moved night flights into the daytime during the base seasons to earn daytime history. | expectations | 0.35 | A night sort cannot run in the day; passenger night flights have their own timing needs. | Not reported. |
| A-N1 | Some slots will be freed under K5 (a holder ceases or under-uses), so the night operators' priority claim has value. | other | 0.75 | NEW. Fourteen airlines; the 80% use rule; airline exits over a decade or more. | C-13, C-14 fail. |
| A-N2 | Penalty receipts are far smaller than the shortfall in charge revenue from fewer movements. | other | 0.8 | NEW. Record figures: about $300 more per movement by 2030; $50,000 per violation, which A-14 puts as occasional. | C-22 becomes ambiguous. |

**Not reported** (an assumption below 0.5):
- The national price of overnight parcel delivery rises (CR-9, CR-6): needs A-18 (p 0.15).
- Pellham fares rise because airlines cannot add flights there at unchanged cost: needs A-19 (p 0.35). Pellham's price and quantity are reported only as a group (C-27).
- Night operators' daytime movements in the base seasons rise (CR-10a, CR-7c): needs A-28 (p 0.35).
- Night operators added night movements in winter 2026/27 to earn a larger K5 share (CR-10a): the direction is a priori (CR-4a), but no case premise says the share was worth it; added as a Tier C note only.

## 11. Report

**The policy:** From 31 October 2027, no aircraft may take off or land at Wexcombe International between 23:00 and 06:00 (with an unclear allowance for late-running flights), and daytime movements are capped at 380 a day. The 380 daily slots are given free to airlines in proportion to the daytime flights they operated in summer 2026 and winter 2026/27, and may be sold, leased and retimed. Unused or abandoned slots go first to night operators, then to new entrants. Penalties are $50,000 per curfew movement and $10,000 per unslotted daytime movement.

**Visible consequences:** About 40 scheduled night movements a night stop at WXI (C-1), and daytime movements stay at 380 while they would have grown (C-2). Airlines with base-season history receive slots that are worth a great deal (C-3).

**Invisible consequences:**
- *Airlines and slot holders:* Slots trade and lease at a positive price (C-5, C-6). Holders receive more per seat even after higher charges (C-23, C-43). Airlines move to larger aircraft (C-7). New airlines enter less (C-16). In the base seasons airlines added off-peak flights to earn history, which lowered off-peak fares then (C-4, C-26) and used up part of the slots' value (C-44).
- *Night operators:* The integrator moves its sort to Pellham (C-11); its WXI hall loses value (C-12); it bears trucking and duplicate costs (C-45). Some night flights move into the 06:00 and 22:00 shoulders (C-8, C-9). Some operators break the curfew and pay penalties (C-15, C-46). Their priority claim to freed slots has value (C-13), so the net change in their WXI business values is ambiguous (C-14).
- *Travelers and shippers:* Fares at WXI rise and fewer seats are flown (C-24, C-25); travelers who keep flying have less for other things (C-42). Some use Pellham, with longer trips (C-27, C-28). Some night trips are lost (C-30). Under U1-b, late flights divert to Pellham (C-29). Wexcombe shippers' overnight service gets earlier cut-offs (C-32).
- *Workers and local trade:* Employment at WXI falls, at the sort and overall (C-34, C-35); it rises at Pellham (C-36); hauliers carry more between the two (C-33); WXI concessions sell less (C-37).
- *Homes:* Through fewer airport workers, home values near WXI fall (C-38) and those near Pellham rise (C-40), not counting noise. Counting noise (Tier C), the WXI contour is ambiguous (C-39) and the Pellham contour falls (C-41).
- *The WAA:* Spends about $2.8 million a year on slots and monitoring (C-19), raises charges per movement (C-22) and collects penalties (C-21). Airlines bear slot paperwork (C-20). Lobbying rises among slot holders, night operators and entrants (C-17).

**Ambiguous effects:** Movements 22:00 to 23:00 under U1-b (shoulder flights against buffers before the curfew; C-9). Night operators' total WXI business value (lost night use against a claim to freed slots; C-14). Home values in the WXI night contour once quieter nights are counted (C-39). Residents' lobbying (goal met against defending it at the review; C-18).

**Key conditions:** Counterfactual growth above 380 (A-1, 0.85) makes the cap bind and the slots valuable; partial responses (A-9, 0.8) keep fares above the old level; the integrator moving to Pellham (A-6, 0.7) drives the employment, haulage, shipper and housing chains; the premium exceeding the charge rise (A-26, 0.75) signs holders' net receipts. Two premises were added: freed slots will occur (A-N1, 0.75) and penalties are small against the charge shortfall (A-N2, 0.8).

**What this analysis cannot say:** How large any effect is, including the slot price, the fare rise or how many travelers move to Pellham; whether the gains to slot holders and residents outweigh the losses to travelers, night operators and workers; or whether the order is good. Noise, sleep, health and environmental effects are out of scope; home values are reported only as asset prices, and chains through noise are Tier C.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | operators.night | quantity_supplied (scheduled movements 23:00 to 06:00 at WXI) | decrease | medium; long | visible | B | CR-1 (op 1: K1 removes night movements where enforced, A-2); CR-4b (operators for whom the penalty does not make violation worthwhile stop; CR-4a: none add night movements) | A-2 |
| C-2 | airlines.daytime | quantity_traded (daytime movements at WXI) | decrease | medium; long | visible | B | CR-1 (op 1: K2 removes movements above 380); counterfactual movements would exceed 380 (A-1: about 409 in winter 2027/28, 440 by 2030); CR-6 (fixed quantity clause: the price of the right, not the quantity, adjusts) | A-1, A-2 |
| C-3 | airlines.slot_holders | asset_value (WXI slots) | increase | short (from the draft); medium; long | invisible | B | CR-1 (op 4: K3 transfers a created right free); CR-7c (an asset the policy creates is valued for its expected yield and captured by whoever receives it at creation; partly from the draft of 2 March 2026 as adoption became likely); CR-10c (value reflects the expected scarcity yield, which exists because the cap binds, A-1, and lasts past 2032, A-3) | A-1, A-3 |
| C-4 | airlines.daytime | quantity_supplied (off-peak daytime movements in summer 2026 and winter 2026/27) | increase | short (base seasons) | invisible | B | CR-10a (a change expected in the future alters choices now); CR-7c (0.7, claims before creation: each base-season movement carries a claim to a future slot); CR-4 (x: no extra flight, y: extra off-peak flight; y made better by the claim's value, which exceeds its cost for some airlines, A-5) | A-5 |
| C-5 | airlines.slot_holders | right_lease_price (WXI slots) | increase | medium; long | invisible | B | CR-6 (a rule fixes the quantity and leaves the price free: the price of the permission rations the fixed number of movements); CR-12 (0.9: an activity the policy creates is an increase against a counterfactual of none); a market forms (A-4) | A-1, A-4 |
| C-6 | airlines.slot_holders | quantity_traded (slot sales and leases) | increase | medium; long | invisible | B | CR-1 (op 2: K4 adds the option to trade); CR-5 (an exchange takes place where the buyer values the slot more than the seller); CR-7a (slots move to the uses that yield more, since airlines differ, A-10); CR-12 (0.9, created activity) | A-4, A-10 |
| C-7 | airlines.daytime | unit_size (seats per movement at WXI) | increase | medium; long | invisible | B | CR-4 (x: smaller aircraft, y: larger aircraft on a scarce slot; the slot's value makes each movement's capacity worth more, A-1); CR-10b (fleets change only through flows over two to four years, A-8) | A-8, A-1 |
| C-8 | operators.night | quantity_supplied (movements 06:00 to 07:00) | increase | medium; long | invisible | B | CR-4 (x: a night movement, now removed; y: a shoulder movement on a bought or leased slot); CR-1 (op 2 via K4: retiming into an hour with room under the limit of 34); A-7, A-4 | A-7, A-4 |
| C-9 | operators.night, airlines.daytime | quantity_supplied (movements 22:00 to 23:00) | U1-a: increase; U1-b: ambiguous | medium; long | invisible | B | U1-a: CR-4 (night operators retime into the shoulder, A-7, A-4; airlines schedule just before 23:00 knowing late running is allowed, A-24), all (+). U1-b: (+) as before from A-7; (-) CR-4 (x: schedule at 22:00 to 23:00, y: earlier; diversion risk attached to x, A-23); CR-12b: no dominance premise | A-7, A-4, A-24, A-23 |
| C-10 | airlines.daytime | quantity_supplied (late-running movements 23:00 to 00:00) | U1-a: increase; U1-b: decrease | medium; long | invisible | B | U1-a: CR-1 (op 2 for delayed flights scheduled before 23:00); CR-4 (flights retimed to just before 23:00 run late more often, A-24). U1-b: CR-1 (op 1: no dispensation; the about 6 late movements a night divert or cancel, A-2) | A-24, A-2 |
| C-11 | operators.night.integrator | quantity_supplied (night sort and cargo movements at Pellham) | increase | medium; long | invisible | B | CR-4 (x: sort at WXI, now removed; y: sort at Pellham, with no curfew and spare capacity); CR-7a (the mobile parts of the operation move to the use still open) | A-6 |
| C-12 | operators.night.integrator | asset_value (WXI sort facility) | decrease | short; medium | invisible | B | CR-7c and CR-10c (the hall's expected yield falls when the curfew becomes expected, and is borne by its owner then); CR-7b (the loss settles on the means that cannot move: an airside hall with no equally valuable use, A-16) | A-6, A-16 |
| C-13 | operators.night | asset_value (claim to freed slots under K5) | increase | short; medium | invisible | B | CR-1 (op 4: K5 transfers a contingent claim to free slots); CR-7c (a created right is captured by whoever holds it at creation); CR-10c (valued for expected yield, which exists if slots are freed, A-N1) | A-N1 |
| C-14 | operators.night | asset_value (WXI night businesses, total) | ambiguous | short; medium | invisible | B | CR-12b (0.8, two items in one variable): (+) the K5 claim (C-13); (-) lost night use and the sort hall (C-12). No dominance premise | A-6, A-16, A-N1 |
| C-15 | operators.night | legal_breach (curfew movements without dispensation) | increase | medium; long | invisible | B | CR-4 (x: comply, y: violate; for a stranded aircraft or missed sort the penalty is below the cost of complying, A-14); CR-1 (op 3 where violation is detected and fined, A-2); CR-12 (0.9: none exist without the curfew) | A-14, A-2 |
| C-16 | airlines.prospective | entry_rate (new airlines at WXI) | decrease | medium; long | invisible | B | CR-1 (op 1: no free capacity; K5 puts entrants after night operators); CR-4 (x: stay out, y: enter; y now needs a slot bought or leased at the scarcity price, C-5); CR-6 | A-1, A-4 |
| C-17 | operators.night, airlines.slot_holders, airlines.prospective | lobbying_effort (on the curfew, U1, slot rules and the 2032 review) | increase | medium; long | invisible | B | CR-4 (x: accept, y: lobby; each has a concentrated stake: night operators in loosening K1 and in U1, holders in keeping K3 at the review, A-3, entrants in reallocation); CR-10a (the 2032 review is expected); CR-8c (resources used up); organization feasible (A-15) | A-15, A-3 |
| C-18 | residents.wxi_associations | lobbying_effort | ambiguous | medium; long | invisible | B | CR-4 applied against a counterfactual in which the campaign continues: (-) the campaign's goal is met; (+) defending the curfew against U1-a claims and at the 2032 review (CR-10a). CR-12b: no dominance premise | A-15 |
| C-19 | officials.waa | enforcement_cost | increase | medium; long | invisible | A | CR-1 (op 3: the WAA must coordinate slots and monitor the curfew, about $2.8 million a year); CR-8c (used up) | none |
| C-20 | airlines.daytime, operators.night | compliance_cost (slot coordination, records) | increase | short; medium | invisible | A | CR-1 (op 3: slot filings, use records and retiming requests attached to operating); CR-8c | none |
| C-21 | officials.waa | non_tax_receipts (penalties) | increase | medium; long | invisible | B | CR-8b (penalties paid by violators, C-46, are received by the WAA); detection complete (A-2); some violations (A-14) | A-14, A-2 |
| C-22 | airlines.daytime, operators.night | price_paid (WAA charges per movement) | increase | medium; long | invisible | B | CR-9 (relation: shared_facility; the existing cost-recovery rule divides largely fixed costs, A-13, over fewer movements, A-1; arithmetic in the record: about $300 more per movement by 2030); (+) CR-8b (K6 costs recovered from charge payers, C-19); (-) penalty receipts credited to costs (C-21); CR-12b and CR-12e: dominance by A-N2 (receipts far smaller than the shortfall) | A-13, A-1, A-N2 |
| C-23 | airlines.slot_holders | net_price_received (per seat, net of charges) | increase | medium; long | invisible | B | CR-6 (the fare rises to ration fixed movements, C-24); CR-7b (the scarcity gain settles on the holders of the fixed right); (-) higher charges per seat (C-22); CR-12b and CR-12e: dominance by A-26 (premium exceeds about $2 per seat) | A-1, A-9, A-26, A-13 |
| C-24 | travelers.wxi | price_paid (fares at WXI) | increase | medium; long | visible | B | CR-6 (seats demanded at the old fares exceed seats on 380 movements, A-1; the fare moves toward clearing); CR-9 (slots input_to seats; charges up, C-22, A-13, same direction); (-) larger aircraft (C-7) and Pellham (C-27) are responses to the scarcity: CR-12e response argument, with A-9 that they are partial (CR-12, 0.9 note) | A-1, A-9 |
| C-25 | travelers.wxi | quantity_traded (seats flown at WXI) | decrease | medium; long | invisible | B | CR-4c (at higher fares the last trip, valued least, is given up; LW-3); CR-6 (seats limited by the cap; larger aircraft only partly offset it, A-9) | A-1, A-9 |
| C-26 | travelers.wxi | price_paid (off-peak fares in the base seasons) | decrease | short (base seasons) | invisible | B | CR-9 (relation: added off-peak flights are the same market); CR-6 (airlines flying extra off-peak movements for history, C-4, fill seats by lowering fares) | A-5 |
| C-27 | travelers.pellham | price_substitute (+), quantity_substitute (+) (flights from Pellham) | at_least_one_increase | medium; long | invisible | B | CR-9 (relation: Pellham flights substitute for WXI flights; demand moves there as WXI fares rise, A-11); CR-6 (0.9, splitting a shift: price and quantity recorded as a group; A-19, a price premise, has p 0.35) | A-11, A-1, A-9 |
| C-28 | travelers.wxi | travel_time (Wexcombe-area travelers who use Pellham) | increase | medium; long | invisible | B | CR-4 (x: WXI at the higher fare, y: Pellham, 55 minutes away; travelers for whom the two were close switch, A-11); CR-9 | A-11, A-1, A-9 |
| C-29 | travelers.wxi.late | travel_time (late flights diverted to Pellham) | U1-a: no_change; U1-b: increase | medium; long | invisible | B | U1-a: CR-1 (late flights may still land until 00:00). U1-b: CR-1 (op 1: late flights after 23:00 are removed); CR-4 (x: cancel, y: divert to Pellham) | A-2 |
| C-30 | travelers.wxi.night | quantity_traded (night passenger flights from WXI) | decrease | medium; long | invisible | B | CR-1 (op 1); CR-5a (night trips that would have taken place are prevented, and both parties lose the gain each expected; some are neither moved to the shoulders nor to Pellham, A-27) | A-27, A-2 |
| C-31 | airport.pellham | quantity_traded (movements at Pellham) | increase | medium; long | invisible | B | CR-9 (relation: Pellham substitute for WXI; the sort moves, A-6, and travelers switch, A-11); CR-6 (spare capacity: quantity rises; independent chains, CR-12d) | A-6, A-11 |
| C-32 | shippers.wexcombe | quality_per_unit (overnight parcel service: collection cut-off) | decrease | medium; long | invisible | B | CR-9 (relation: sort location input_to overnight delivery; the sort is 70 km away, A-6); CR-4 (the integrator moves collection cut-offs earlier to reach the sort, A-17) | A-6, A-17 |
| C-33 | haulage.wexcombe_pellham | quantity_traded (road haulage Wexcombe to Pellham) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: haulage input_to the relocated sort; parcels from Wexcombe must reach Pellham) | A-6 |
| C-34 | workers.wxi | employment (night sort at WXI) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to the sort; the sort leaves WXI, A-6; employment follows it, A-25) | A-6, A-25 |
| C-35 | workers.wxi | employment (WXI, all movements) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to movements; fewer movements than the counterfactual, A-1, and staff follow movements, A-25) | A-1, A-25 |
| C-36 | workers.pellham | employment (Pellham sort and movements) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to the sort at Pellham, A-6); CR-7a (labor moves to the use now open) | A-6 |
| C-37 | sellers.concessions_wxi | quantity_traded (concession sales) | decrease | medium; long | invisible | B | CR-9 (relation: concessions complement, trip, of flights; fewer passengers than the counterfactual, C-25, and sales follow passengers, A-21) | A-21, A-1, A-9 |
| C-38 | homeowners.near_wxi | asset_value (homes), not counting effects through proximity | decrease | medium; long | invisible | B | CR-9 (relation: homes complement, location, of WXI jobs; fewer jobs, C-34, C-35, A-25, and workers' demand is material, A-12); CR-7c and CR-10c (lower expected demand is capitalized when the move becomes expected) | A-12, A-6, A-25 |
| C-39 | homeowners.near_wxi | asset_value (homes in the night contour), combined | ambiguous | short; medium; long | invisible | C | CR-12 (0.9, Tier C against Tier B): (+) proximity: quieter nights capitalized (A-22; CR-9, CR-7c); (-) the Tier B chain C-38. No dominance premise | A-22, A-12, A-6 |
| C-40 | homeowners.pellham | asset_value (homes), not counting effects through proximity | increase | medium; long | invisible | B | CR-9 (relation: homes complement, location, of Pellham jobs; more jobs, C-36; workers' demand material, A-12); CR-7c and CR-10c | A-12, A-6 |
| C-41 | homeowners.pellham | asset_value (homes in the prospective night contour), combined | decrease | short; medium; long | invisible | C | CR-12 (0.9, Tier C against Tier B): (-) proximity: night noise from the moved sort (A-6; CR-9, CR-7c); (+) the Tier B chain C-40; CR-12e: dominance by A-20 (noise discount exceeds added demand in the contour) | A-20, A-6, A-12 |
| C-42 | travelers.wxi | resources_available_other_uses (travelers who keep flying from WXI) | decrease | medium; long | invisible | B | CR-3 (note: falls only for those who keep buying the burdened option; travelers who keep flying pay the higher fare, C-24); CR-8a | A-1, A-9 |
| C-43 | airlines.slot_holders | resources_available_other_uses | increase | medium; long | invisible | B | CR-8b (the scarcity premium paid by travelers, C-42, and by slot buyers, C-5, is received by holders); CR-7b; net of charges by A-26 | A-1, A-9, A-26 |
| C-44 | airlines.daytime | resources_available_other_uses (airlines that added base-season movements) | decrease | short (base seasons) | invisible | B | CR-7c (0.7: where actors compete to qualify for a claim, part of its value is used up in the competition); CR-8c (flights flown only for history) | A-5 |
| C-45 | operators.night.integrator | resources_available_other_uses | decrease | medium; long | invisible | B | CR-3c and CR-8a (trucking 70 km and a second facility are paid for to keep serving Wexcombe; the integrator keeps paying, A-6, A-17) | A-6, A-17 |
| C-46 | operators.night | resources_available_other_uses (operators that pay penalties) | decrease | medium; long | invisible | B | CR-8b (penalties are a payment to the WAA, C-21); CR-3c (paid by those who violate, A-14, and are detected, A-2) | A-14, A-2 |

## Gaps found

**(a) Calculus gaps.**
- GAP-054-C1. The use-it-or-lose-it rule (K5, 80% of days) attaches a loss to under-use of a right that does not exist in the counterfactual. CR-1 op 3 and CR-4 give the direction (holders fly or lease slots they would leave idle), but no core rule says how to sign a response that is defined only relative to the policy's own created right; it is recorded as a note in section 8.
- GAP-054-C2. CR-4's 0.9 note on lobbying against a contested baseline covers repeals only. For an imposition whose counterfactual includes a continuing campaign (C-18), the same reasoning was applied by analogy; the rule should say so.
- GAP-054-C3. CR-9 lists exchange, contract, currency, trip and location relations, but a cost-recovery charge rule (an existing rule) links all users of a facility through the authority's budget. It was recorded as `shared_facility` with arithmetic on the existing rule (C-22); whether that relation is Tier C (as CR-9's 0.7 note implies for shared facilities) or Tier B when the link is a pricing rule rather than congestion is not settled. It was treated as Tier B because the link runs through a stated rule and money payments, not through proximity.

**(b) Core-rule wording that was hard to apply.**
- CR-7c on a contingent, ranked claim (K5: night operators first, entrants second, only if slots are freed). Valuing a claim whose yield depends on an uncertain future event needed A-N1; the rule does not say how a priority order among claimants is capitalized.
- CR-12 0.9 (Tier C against Tier B) where the Tier B chain itself depends on a fairly weak premise (A-12, p 0.6): the rule gives two consequences, but the Tier C combined sign (C-41) relies on a dominance premise (A-20) that is about the proximity chain's size; it was not clear whether such a premise lifts the combined sign to anything above Tier C (it was left at C).
- CR-6 (0.9, splitting a shift) for the Pellham market: A-19 (p 0.35) says the price rises; its negation does not establish that the price does not rise, so price and quantity were left as a group (C-27).

**(c) Vocabulary missing from the ontology.**
- No variable for activity by time of day (movements per hour or window). `quantity_supplied` with a qualifier was used for night, shoulder and late-running movements (C-1, C-8 to C-10).
- No variable for the timeliness of a service (collection cut-off, delivery time); `quality_per_unit` was used (C-32).
- No actor class for an integrated operator's owned facility separately from the operator, and no variable for the utilization of a right (slot use rate) under a use-it-or-lose-it rule.
- Noise and sleep are out of scope; only their capitalization into home values appears, at Tier C.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the structure of the Wexcombe case and on every sign they share. Night movements stop and daytime movements are held below their path. Slots are created and capitalized from the draft. Airlines race for history in the base seasons. A slot price and a slot market appear, and airlines move to larger aircraft. Night flights move to the shoulders, and the sort moves to Pellham, with its facility at WXI losing value. Entry falls, some operators break the curfew, and fares rise while trips fall (both with A-9 as the partial-response premise). Holders' net price per seat rises with A-26, and WAA charges per movement rise. Travelers, workers and concessions move as Pellham gains. Home values at both airports get the same Tier B and Tier C pair. The residents' lobbying is `ambiguous` in both. There is no S row. The differences are omissions on both sides, plus two premise choices. The core version omits that fewer airlines operate at WXI, what slot buyers and lessees pay, the noise office's lighter night-complaint load and the Tier C total it requires, and airlines' operations as a whole. It also signs the integrator's money outlays without a premise and signs all of WXI employment alone where only the group is derivable. The pattern version omits lower off-peak fares during the race, haulage to Pellham, travelers' and penalty payers' means, and the value of the K5 claim. It declined that value for want of a premise that the flow is "material", which is not a reason the method recognizes for withholding a sign. Both versions sign night operators' lobbying `increase`, although the counterfactual has the residents' curfew campaign, which night operators would have opposed. By the reasoning both use for the residents, that sign needs a premise.

Counts: M 27, V 10, S 0, OP 7, OC 5.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | Under U1-b the pattern's C-1 also covers the late-running movements, which the core records separately (C-10). |
| C-2 | C-2 | V | | `quantity_supplied` by `airlines.history` in the pattern; `quantity_traded` by `airlines.daytime` in the core. |
| C-3 | C-3 | M | | |
| C-4 | C-5 | M | | Same rules (CR-6 fixed-quantity clause; CR-12 0.9, an activity that exists only under the policy). |
| C-5 | C-4 | M | | |
| C-6 | C-44 | V | | Race costs. The pattern uses `compliance_cost` (CR-8c, used up); the core uses `resources_available_other_uses` decrease. The core's form also needs the race flights' fares not to cover their cost, which "thinly loaded" (A-5) implies but does not state. `compliance_cost`, or a variable for resources used in competing to qualify, is the cleaner record. |
| C-7 | C-11 | V | | `quantity_substitute` against `quantity_supplied` at Pellham. |
| C-8 | C-8 | M | | |
| C-9 | C-9 | M | | Same chains and premises per reading. |
| C-10 | C-6 | V | | The pattern records slot purchases and leases by night operators; the core records all slot trades. |
| C-11 | C-7 | M | | The core cites CR-4 and CR-10b instead of CR-4c's unit clause; same premises (A-1, A-8). |
| C-12 | none | OC | E | `number_of_sellers` (airlines at WXI) decrease. Derivable against the no-order counterfactual. Entrants stay out (core C-16, CR-4), and under A-10 some small airlines that value their slots below the lease price lease out or sell all of them and leave (CR-4: x: operate, y: lease out, where y did not exist before). Core-version omission. The pattern derives it from EN-13, whose "number of sellers using the right decreases" compares with the allocation before trading, not with no policy (Findings). Neither version considered entry during the base seasons to earn free slots, an opposing chain in the short window. |
| C-13 | C-16 | M | | |
| C-14 | C-15 | M | | |
| C-15 | C-10 | V | | Under U1-a the pattern records the reshaping of schedules (`reclassification`); the core records its result, more late-running movements 23:00 to 00:00 (A-24). Under U1-b the pattern gives `no_change` for reshaping and the core gives `decrease` for late-running movements, but those are different variables, so the signs do not conflict. |
| C-16 | C-17 | M | | Both versions sign night operators' lobbying `increase`. That is an error in both: see Findings. |
| C-17 | C-18 | M | | Same reasoning (counterfactual campaign), by analogy to CR-4 0.9 in both. |
| C-18 | C-12 | M | | |
| C-19 | C-24 | M | | Same response argument with A-9. The core also lists higher charges as a (+) chain. |
| C-20 | C-25 | M | | Trips in the pattern, seats flown in the core; both rest on A-9. |
| C-21 | C-23 | M | | Same dominance premise (A-26). |
| C-22 | C-28, C-29 | V | | The pattern gives one `travel_time` increase for night travelers. The core splits it into travelers who switch to Pellham (C-28) and late flights diverted per reading (C-29: U1-a `no_change`, U1-b increase). The core's split is more exact: retiming into the shoulders is not a longer trip. |
| C-23 | C-27 | V | | The pattern signs `quantity_substitute` alone; the core gives price and quantity as a group (CR-6 0.9, splitting a shift). Signing quantity alone needs a supply premise. The record supports one (Pellham's runway is 45% used, and aircraft can be moved), but the pattern states it only in prose. The core used that same premise to sign Pellham's movements alone (C-31), so it is inconsistent. |
| C-24 | C-31 | M | | |
| C-25 | C-34, C-35 | V | | The pattern gives the group (`employment`, `hours_worked`, `at_least_one_decrease`). The core signs `employment` alone, twice. C-34 (the night sort, which leaves WXI entirely) is derivable alone. C-35 (all movements) is not: hours can fall instead of heads, so it should be the group. Core-version error. |
| C-26 | C-36 | M | | |
| C-27 | C-38 | M | | The core's horizon omits `short`, though its own derivation capitalizes from when the move becomes expected. |
| C-28 | C-39 | M | | The core's proximity chain has only quieter nights; it omits busier shoulders (the pattern's kind 3 part). The sign is unaffected, since it is `ambiguous` either way. |
| C-29 | C-40 | M | | |
| C-30 | C-41 | M | | Same dominance premise (A-20). |
| C-31 | C-32 | M | | |
| C-32 | C-22 | M | | The core adds the K6 cost chain (+) and penalty receipts credited to costs (−), and signs with A-N2. |
| C-33 | C-37 | M | | |
| C-34 | C-43 | V | | The pattern records lessors' and sellers' receipts (CR-8b); the core records holders' means as a whole, through the scarcity premium net of charges (A-26). |
| C-35 | none | OC | E | Lessees and buyers of slots (night operators, entrants) have less for other uses: they pay for something that was free in the counterfactual and keep paying (CR-3 note, CR-8b). The core's CR-8 symmetry note names them as payers but records no consequence. Core-version omission. |
| C-36 | none | OC | J | Holders' WXI operations as a whole `ambiguous` (CR-12b). Defensible, though the pattern lists slots (C-3) and the scarcity premium (C-21) as two (+) items when the first is the capitalized second. Nothing scorable lost. |
| C-37 | C-19 | M | | The core does not add the qualifier "not counting effects through proximity" that CR-12 0.9 asks for when a Tier C chain reaches the same key (see C-38, C-39). |
| C-38 | none | OC | E | Night-noise complaints handled by the WAA decrease (Tier C; CR-9 `proximity`, CR-8c against the right baseline). The record gives the noise office ($0.5 million) and its share of night cases (60%). Core-version omission. |
| C-39 | none | OC | E | Total enforcement cost at Tier C: increase, by arithmetic ($2.8 million against a $0.5 million office). CR-12 0.9 requires this second record once C-38's chain is found. Core-version omission, following from C-38. The sign equals the core's C-19. |
| C-40 | C-20 | M | | |
| C-41 | C-30 | V | | The pattern covers night passengers and cargo shippers; the core covers passengers only. |
| C-42 | C-21 | M | | |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-13 | OP | A | The K5 claim's value to night operators increases, given that some slots will be freed (A-N1, p 0.75). The pattern declined it because "the case gives no premise that the flow is material". The method signs direction, not size: a free claim on any flow with positive probability has positive value (CR-7c, CR-10c), and CR-3b rules out a loss. The difference is the premise A-N1. The pattern's argument that holders sell instead of returning slots bears on size only. |
| C-14 | OP | J | Night operators' WXI businesses as a whole `ambiguous` (the K5 claim against lost night use and the hall). It depends on C-13. Defensible, but adds no sign. |
| C-26 | OP | E | Off-peak fares fall in the base seasons, because the race flights add seats to the same market (CR-9, CR-6; A-5). Pattern-version omission: it records the race flights (C-5) but not their effect on fares. |
| C-33 | OP | E | Road haulage Wexcombe to Pellham increases (CR-9, LW-10; A-6). Pattern-version omission (its stopping points do not name it, and it is at depth 2). |
| C-42 | OP | E | Travelers who keep flying from WXI have less for other uses (CR-3 note, CR-8b). Pattern-version omission (as in WE-003); its own final check 4 names only slot lessees and lessors. |
| C-45 | OP | E | Integrator's `resources_available_other_uses` decrease. Core-version overclaim: trucking and a Pellham facility are added outlays, but the WXI charges and hall costs are no longer paid, and nothing in the record says the moved operation costs more in money. By CR-3a the integrator is worse off by its own ranking. A money sign needs an `other` premise (the Pellham operation costs more), which the pattern version rightly did not assume (its final check 4). |
| C-46 | OP | E | Operators who pay penalties have less for other uses (CR-8b, CR-3 note). The pattern records the receipt (C-42) but not the payer's side; its section 9 pairs C-42 with C-14, which is breach, not means. Pattern-version omission. |

### Findings

- **Pattern overclaims or hidden premises.** *EN-13 as written* signs `number_of_sellers` decrease and "the quantity per remaining user increases" against the allocation before trading, not against the no-policy counterfactual. Against no order, quantity per remaining user need not rise, since every holder is capped below its counterfactual growth. The number of airlines does fall, but through entry (CR-4) and whole-holding exits (A-10), which the analysis should cite. This is the same baseline fault that 6.2g found in RS-20 and EN-11's Unless clause. *EN-2* has no clause for an opposing chain from a cost-recovery charge spread over the capped quantity (the pattern's own Gaps c2). The core version needed the same premise, A-26, so this is confirmed. *RS-8's "two sides"* does not fit a race that adds activity without taking it from another window (Gaps c3). Confirmed: the core recorded the race as a rise in its window only (C-4). Pattern C-23 signs a substitute's quantity alone on a supply premise stated only in prose.
- **Errors in both versions.** Night operators' `lobbying_effort` is signed `increase` (pattern C-16, core C-17). The counterfactual contains the residents' campaign for a curfew, which the integrator and the night passenger airlines would have opposed. RS-7's Unless clause, which the pattern applied to the residents (C-17), and the CR-4 0.9 analogy, which the core applied to them (C-18), both say that a class that lobbies in both worlds needs a premise. Without one, night operators' lobbying is `ambiguous`. Slot holders' and entrants' lobbying is a valid `increase`: it concerns slots that do not exist in the counterfactual. For the pattern version this is an analyst misapplication of RS-7, not a fault in the pattern. Neither version considered entry during the base seasons to earn free slots (K3 issues slots to any airline with base-season movements). That is a chain the rules derive (CR-10a, CR-4: x: stay out, y: enter now; EN-12's newcomer sentence points to it) and needs a premise like A-5.
- **Errors in the core version.** `employment` alone for all WXI movements (C-35), where only the group is derivable. The integrator's money outlays (C-45), signed without a premise. Omissions: `number_of_sellers` (pattern C-12), slot buyers' and lessees' means (C-35), the Tier C complaint chain and the Tier C total CR-12 0.9 asks for (C-38, C-39), and the shoulder-noise part of the WXI proximity chain (sign unaffected). Pellham is handled inconsistently: movements are signed alone on the spare-capacity premise (C-31), while travelers' trips are kept as a group (C-27). C-38's horizon omits `short`.
- **Errors in the pattern version (omissions).** Off-peak fares in the base seasons (core C-26), haulage to Pellham (C-33), travelers' means (C-42), penalty payers' means (C-46), and the K5 claim. The K5 claim was declined on materiality, which is a judgment about size, not sign (core C-13, cause A). `travel_time` for night travelers (C-22) is signed for all readings, though under U1-a it rests on moves to Pellham alone.
- **Test of 0.9 verdicts.** The pattern version reports no "failed" verdict. On the "needed interpretation" verdicts: *CR-12 0.9 Tier C against Tier B, with a kind 3 Tier C chain:* not tested by the core version, which missed the shoulder half of the chain; it reached the same `ambiguous` and the same pair of records (C-38, C-39). It raised a separate unclear point: whether a dominance premise about the Tier C chain's size can lift the combined sign above Tier C (C-41). *CR-12 0.9 response argument with two responses:* confirmed. The core also read "the response" as both responses together and stated A-9 for both. *EN-6 0.9 Inputs, one capped input feeding outputs in a local and a national market:* confirmed. Working per output from CR-6 and CR-9, the core reached the same split (fares local, the national parcel price negligible on A-18). *CR-7c, the part of the value used up in the race:* confirmed. The core read the race costs as wholly used up (C-44, CR-8c) with nothing created. *RS-7 Unless by analogy for an imposition:* confirmed; the core made the same analogy (GAP-054-C2). Both versions failed to carry it to night operators, as above. *EN-12's newcomer clause and K5 (Gaps c1):* partly contradicted. The core shows that CR-7c and CR-10c give K5 a signed value with one premise, so "no consequence" was not forced. *High-grading candidate (Gaps c5):* confirmed. The core derived larger aircraft (C-7) from CR-4 without the candidate.
- **Limits of the core rules.** None produced a difference: no S, OP or OC row has cause K. Unclear core-rule wording: (1) CR-4 0.9 on lobbying against a contested baseline names repeals only. Both versions extended it to an imposition, and neither saw that it reaches every class active in the counterfactual contest. (2) CR-9 0.7 puts `shared_facility` chains at Tier C, but a cost-recovery charge that links users through an authority's budget runs through money payments (core GAP-054-C3). The pattern version treated it at Tier B through PC-15. (3) CR-12 0.9 Tier C against Tier B does not say what a dominance premise must cover when the Tier C chain is itself kind 3, or whether a dominance premise can raise the combined tier. (4) CR-7c does not say how a contingent claim ranked behind or ahead of other claimants (K5) is capitalized. (5) No rule addresses a use-it-or-lose-it condition on a right that does not exist in the counterfactual (core GAP-054-C1). (6) CR-6 0.9, splitting a shift, does not say whether figures in the record (spare runway capacity) are enough to sign quantity alone.
