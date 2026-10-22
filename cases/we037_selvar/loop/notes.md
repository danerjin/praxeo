# WE-037 Selvar Fair Ticket Act: expand loop, blind run

Inputs read: section 1 and the assumption table only. Branch `loop-we037_selvar` from 6292d7c. 3 rounds, 24 node visits, 22 questions (18 from the table, 4 judged), plus 7 seed assumptions (6 table, 1 judged).

## Seed (policy's own facts)
- Exchanges: `e_resale_fans` and `e_resale_brokers` (buyers.current / buyers.prospective unsatisfied; the two seller classes split because the Act's reach, bots and season-ticket holdings differ by seller type), `e_platform` (platform fee to the buyer), `e_bots` (brokers buy bot software).
- `held` k1 (cap, below) on both resale exchanges, premises A-1 (binds) and A-2 (enforced on compliant platforms); `k1_fee` on `e_platform`, which exists only under reading U1-a (fee inside the cap). U1-b has no component. `banned` k2 on `e_bots` (A-13). Charges: k4_penalty ($500 per ticket, to officials.enforcement, non_tax_receipts; premise j1) and k4_damages (treble recovery paid by the seller to the buyer; premise and quantity premise A-11). `transfers` (A-2), `compliance` k1 on platforms.compliant, `enforcers` and `fixed_budget` k4 (A-21), `announced` k1 (A-8).
- Judged in seed: j1 "The Attorney General's division brings penalty actions against some above-cap resales", p 0.75 (section 1: penalty up to $500, enforced by the division; no table row says the division acts).
- Not seeded: expiry (none), `fixed` (no price is fixed by a rule other than the Act), thresholds, qualifies, grants, capped, incidence, moves (the text says nothing on which side's price takes a wedge).

## Round 1 (depth 1: sellers.fans, intermediaries.brokers, buyers.prospective, buyers.current, platforms.compliant, officials.enforcement)
- sellers.fans: outside trade (A-4); charity auctions as an alternative (A-23, the K1 exemption); offshore platforms (A-5, A-7); packages as reclassification (A-12); bring forward sales before 1 Sept (A-8); season-seat-rights asset owned by owners.season_ticket (A-16).
- intermediaries.brokers: outside resale (A-6), outside bot use (A-6, on `e_bots`); packages (A-12); shift buying to Brackmere (A-20) with a same_act link to sellers.brackmere; link to sellers.demand_priced demand (A-3, A-22); crowding link to the waiting list (A-17, A-24); stake (A-9); broker-business asset (A-18); timing (A-8).
- buyers.prospective: move to the primary sale, into sellers.fixed_price and sellers.demand_priced (A-10); Brackmere substitution (A-19); side payments through add-ons (A-12); outside purchases (A-4).
- buyers.current: hold purchases back to Sept (A-8); stake (A-9).
- platforms.compliant: stake (A-9); cut service quality under U1-a (judged J2); raise the seller-side fee under U1-a, as `inverse` alternatives on sellers.fans and brokers (judged J3); under U1-b a side_payments criterion for buyers.current (reading U1-b, no premise: the reading is the premise).
- officials.enforcement: empty (see "could not hold").

## Round 2 (depth 2, 13 visits)
Proposals: buyers.border same_act to sellers.brackmere; brokers and fans packages as complement link to sellers.complements (A-12); owners.season_ticket yield link to buyers.waitlist wait_time (A-24, for holders who renew less); platforms.offshore substitute link to platforms.compliant volume; sellers.demand_priced: supply_price link to buyers.primary price_paid (A-14, short horizon), yield link to its own term_prevalence (A-15, more seats priced by demand), stake (A-9); sellers.fixed_price: same_act to buyers.primary excess_demand and crowding to wait_time (J4), stake (A-9). Empty lists: buyers.current#2, buyers.prospective#2, buyers.waitlist, platforms.compliant#2, sellers.brackmere, sellers.charities, sellers.fans#2 only repeats the packages link.

## Round 3 (depth 3, 5 visits)
buyers.primary and sellers.demand_priced#2 each got a `dominance` fact (price_paid and term_prevalence ambiguous because the A-10 chain raises demand for demand-priced seats and the A-3/A-22 chain lowers it): premise J5 "The demand added in primary sales by fans priced out of resale is larger than the demand lost when brokers withdraw", judged 0.7 (A-10 is 0.7, A-22 is 0.4). Empty: platforms.compliant#3, sellers.complements, sellers.fixed_price#2.

## Answers
From the table (p as given): A-1, A-2, A-8, A-11, A-13, A-21 (seed); A-3, A-4, A-5, A-6, A-7, A-9, A-10, A-12, A-14, A-15, A-16, A-17, A-18, A-19, A-20, A-22, A-23, A-24 (answers.json).
Judged: j1 (0.75, seed); J2 services cut under a capped fee (0.55); J3 seller fee raised (0.6); J4 fixed face values do not rise with demand (0.9, from "fixed face values only"); J5 dominance above (0.7).
Every table row A-1 to A-24 is used once as a premise.

## Final engine output
DONE in 3 rounds, 22 questions. Notable lines: price_paid falls and quantity_traded falls for buyers.current; excess_demand rises and the criteria group (at_least_one_increase) for buyers.prospective; net_price_received and quantity fall for sellers.fans and brokers; brokers' asset_value falls; owners.season_ticket asset_value falls; buyers.waitlist wait_time falls; buyers.primary excess_demand, price_paid (via dominance) and wait_time rise; platforms.compliant net_price_received, quality and (per reading) volume ambiguous or down; officials.enforcement enforcement_cost both up (items) and down (other_work). k2 effects on sellers.software are unreported (A-13 is 0.45).

## What the format could not hold
- The primary market is not an exchange I could add: proposals cannot create exchanges, so primary-sale rationing (CR-6 margins on primary sellers' fixed prices) is carried only by links into buyers.primary excess_demand and wait_time.
- A-15 (more seats priced by demand) was held as a `yield` link into `term_prevalence`; there is no variable for the share of seats priced by demand.
- Fixed budget: the division's R3 enforcement (fake tickets, speculative listings) giving way. enforcement_cost moves in both directions (increase from k4, decrease as other_work), so a link from it would carry both signs; none proposed.
- U1: the two fee items of price_paid (capped price and platform fee, CR-6 1.0) cannot be signed separately; U1-a is held as a second held line on a platform-fee exchange, U1-b as a side_payments margin.
- CR-11b (informal trade loses reputation and certification, more fake tickets) has no relation that lowers quality_information from a rise in informal_activity; not proposed.
- Timing of the broker-business asset loss (buyers expected the cap from introduction, A-18) cannot be dated: assets carry no date.
- k4_damages is paid by the seller to the buyer for the same trade, which the charge format treats as a wedge on the exchange; its sign on quantity depends on A-11 (0.45), so the chain is unreported.
- Brackmere substitution (A-19) lowers Selvar primary demand while A-10 raises it; the opposing link into sellers.fixed_price demand was not added because it would feed back onto buyers.prospective excess_demand.
- Unreached: the football club (season-ticket seller) and seat-rights trading through its exchange have no class of their own, since only effects on existing parties reach new nodes.
