# WE-037 / Analysis: Ticket resale price cap and bot ban

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Selvar Fair Ticket Act.** The State of Selvar has about 6.8 million people. Its largest city, Dunholt, has an 18,000-seat arena, a 64,000-seat stadium (home of a football club with nine home games a year), an amphitheater and three large theaters. About 9.5 million tickets a year are sold for events in Selvar; about 11% (1.05 million) are resold. Of those, about 52% (545,000) are resold above face value plus 10%, at a median markup of 70%; the rest at less, many below face, mostly for events that do not sell out.

About 60% of resale listings come from about 600 professional brokers (40 based in Selvar), the rest from fans who cannot attend. By value, 68% of resales go through two national platforms with offices in Selvar, 9% through the club's own exchange, 11% through offshore platforms with no Selvar presence, and 12% through social media and in person. Platform fees are typically 18% of the resale price charged to the buyer and 10% to the seller.

Primary sellers set their own prices. A national promoter running about 60% of arena concerts prices about 10% of seats at high-demand events by demand and the rest at fixed face values; many artists and the theaters use fixed face values only. The club sells 38,000 season tickets with a waiting list of about 9,000; brokers hold about 15% (about 5,700). Season seat rights are transferable through the club for a fee and trade at a price. Brackmere City, 55 minutes from Dunholt in a state with no resale law, has a 14,000-seat arena; about 40% of arena tours that play Dunholt also play there.

| Field | Value | Source sentence |
| --- | --- | --- |
| Jurisdiction (and what lies just outside) | Resale of tickets to events in Selvar, wherever the parties or platform are (asserted); Brackmere City, 55 minutes away, has no resale law; offshore platforms have no Selvar presence | K1; policy record |
| Announced / enacted / effective / expires | Introduced 3 Feb 2027; signed 12 May 2027; applies to resales made on or after 1 Sep 2027; resale contracts made before 1 Sep exempt; no expiry | Policy record |
| Enforcement (who, penalties, resources) | Attorney General's consumer division: civil penalty up to $500 per ticket resold above the cap, $2,500 per ticket obtained with a bot; buyers may recover three times the excess; no new appropriation (existing $14 million budget) | K2, K4 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
| --- | --- | --- | --- | --- | --- |
| K1 Resale cap | `price_ceiling` | Resale of tickets to events held in Selvar | Any reseller; any platform that lists or processes payment | No resale above face value plus 10%; face value is the primary seller's price including taxes and its own fees, as printed or recorded | Resale by registered charities at auction; resale contracts made before 1 Sep 2027 |
| K2 Bot ban | `prohibition` | Software that evades primary sellers' purchase limits or access controls | Users and sellers of it | $2,500 civil penalty per ticket obtained with it | - |
| K3 Primary sellers | Explicit non-application | Primary sales | - | Nothing limits the primary price | - |
| K4 Enforcement | Enforcement | K1, K2 | AG consumer division | $500 per ticket; treble damages to buyers; no new money | - |

Existing rules, in force in the counterfactual too: R1 primary sellers' terms forbid bots and allow cancellation, enforced by the seller; R2 primary sellers may make tickets non-transferable or limit resale to their own exchange; R3 consumer fraud law (fake tickets, speculative listings) enforced by the same division.

Unclear provisions:
- U1, platform fees. U1-a: buyer fees are part of the capped price, so the buyer pays at most face plus 10% in total. U1-b: fees are charged on top of the capped price, and "reasonable" is not defined.

Not a reading: whether hospitality packages are tickets; the AG's existing practice is an assumption (A-12).

Counterfactual: Selvar without the Act, with R1 to R3. Counterfactual law for CR-1: any holder of a transferable ticket may resell it at any price the buyer accepts.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Resale cap | triangular (prohibits resales above a price) | Yes for high-demand events (A-1); not for events resold at or below face plus 10% | 1 (removes the option of reselling above face plus 10% where enforced: compliant platforms, A-2); 3 (attaches a risk of a $500 penalty and treble damages to above-cap resales elsewhere, A-4, A-5); per reading U1 for platform fees | CR-4, CR-5a, CR-5c, CR-6, CR-7, CR-9, CR-10, CR-11 |
| K2 Bot ban | triangular (prohibition of a good and its use) | Beyond R1 only if enforced (A-13, p 0.45) | 3 (a $2,500 penalty risk attached to bot use and sale) | CR-4 (x: use bots, y: not) |
| K3 Primary sellers | explicit non-application | - | none (states the counterfactual law for primary prices) | CR-1 (recording) |
| K4 Enforcement | binary within a fixed budget | Yes | 4 (work assigned to the division with no new money: resources moved from its other work, A-21); 3 (penalty risk) | CR-8a, CR-8c |

The policy fixes a price only in the resale market. Primary prices stay free (K3), but most are set by the primary sellers' own choice below the level that clears the market for high-demand events (CR-2: a chosen price, not a rule). K1 caps the resale price that, without the Act, moved toward the clearing level.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| buyers.resale | Fans who buy resale tickets to high-demand events | Op 1 (on compliant platforms they cannot pay above the cap, so units are rationed otherwise) |
| sellers.resale.brokers | About 600 brokers (40 in Selvar) | Op 1 on compliant platforms; op 3 elsewhere |
| sellers.resale.fans | Fans who cannot attend and resell | Op 1 and op 3 as for brokers |
| platforms.compliant | Two national platforms and the club exchange (77% by value) | Op 1 (cannot list or process above-cap resales); op 3 (compliance); per reading on fees |
| platforms.offshore | Platforms with no Selvar presence (11%) | Op 3 with low expected penalty (A-5) |
| sellers.informal | Social media and in-person resellers (12%) | Op 3 (A-4) |
| sellers.packages | Sellers of hospitality packages | Op 3 only if the package is treated as a ticket (A-12) |
| primary_sellers | Promoter, artists, theaters, club | No operation (K3); through CR-9 their buyers change |
| fans.primary | Fans who try to buy in primary sales | Through CR-9: fewer brokers compete; more fans try (A-10) |
| season_ticket_holders | Holders of season seat rights, including brokers | Through CR-7c: expected resale of games capped |
| fans.waiting_list | About 9,000 on the season ticket list | Through CR-9: seats released by brokers |
| bot_users, sellers.bots | Users and sellers of purchase bots | Op 3 (K2); through CR-9 the resale margin falls |
| charities | Registered charities auctioning tickets | Op 2 relative to other resellers: their auctions are exempt |
| neighboring_jurisdictions | Brackmere City fans, venues and resellers | Through CR-9 (across_border) |
| officials.ag_consumer | AG consumer division | Op 4 within a fixed budget (A-21) |
| interest_groups | Brokers, platforms, fan groups, primary sellers | Lobbying (A-9) |

## 4. Direct effect

CR-1 and CR-2: the immediate change in the resale market for high-demand events.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.resale (high-demand events, compliant platforms) | price_paid (resale tickets, including buyer fees) | U1-a: decrease; U1-b: decrease | short; medium; long | CR-1 op 1, CR-5c, CR-6 | A-1, A-2 (U1-b also A-7, A-N2) |
| C-2 | sellers.resale (brokers and fans, compliant platforms) | net_price_received | decrease | short; medium; long | CR-1 op 1, CR-5c | A-1, A-2 |
| C-3 | platforms.compliant | net_price_received (fee revenue per high-demand resale) | U1-a: decrease; U1-b: ambiguous | short; medium | CR-5c, CR-6 (0.8: a free price's rise), CR-12b | A-1, A-2 |
| C-4 | buyers.resale (high-demand events) | excess_demand (compliant resale market) | increase | short; medium; long | CR-6 | A-1, A-2 |
| C-5 | buyers.resale (high-demand events) | wait_time (+), search_cost (+), allocation_by_non_price_criteria (+) | at_least_one_increase | short; medium; long | CR-6 | A-1, A-2 |

## 5. Responses

CR-4 applied to every pair of options each actor class has; CR-6 for where the capped pressure goes; CR-10a for the window between introduction and 1 September.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-6 | sellers.resale.brokers | quantity_traded (primary purchases for Selvar high-demand events) | decrease | short; medium; long | CR-4 (x: buy to resell in Selvar, y: other uses), CR-7a | A-1, A-2, A-3 |
| C-7 | sellers.resale | informal_activity (above-cap resales of Selvar tickets on offshore platforms, social media and in person) | increase | short; medium; long | CR-4 (x: comply, y: violate), CR-6 | A-1, A-4; or A-1, A-5, A-6 |
| C-8 | platforms.offshore | quantity_traded (resales of Selvar tickets) | increase | short; medium; long | CR-9, CR-4 (x: list on a compliant platform, y: offshore) | A-1, A-2, A-5, A-6 |
| C-9 | platforms.compliant | quantity_traded (resales of high-demand tickets) | decrease | short; medium; long | CR-4, CR-5a, CR-9 | A-1, A-2, A-3; or A-1, A-2, A-5, A-6 |
| C-10 | buyers.resale (informal channels) | quality_information | decrease | short; medium; long | CR-11b | A-1, A-4; or A-1, A-5, A-6 |
| C-11 | sellers.packages | reclassification (tickets sold inside hospitality packages) | increase | short; medium; long | CR-4 (x: the covered form, y: the uncovered form) | A-1, A-12 |
| C-12 | buyers.resale (high-demand events) | side_payments (tie-in package items) | increase | short; medium; long | CR-6, CR-4 | A-1, A-12 |
| C-13 | sellers.resale.brokers | number_of_sellers (brokers active in Selvar events) | decrease | medium; long | CR-4 (x: stay, y: exit), CR-7a | A-1, A-2, A-3 |
| C-14 | sellers.resale.brokers | asset_value (broker businesses) | decrease | short (from introduction, Feb 2027) | CR-7c, CR-10c | A-1, A-3, A-18 |
| C-15 | sellers.resale.brokers | quantity_traded (purchases for Brackmere City events) | increase | medium; long | CR-7a, CR-4 (x: here, y: there) | A-20 |
| C-16 | fans.selvar | cross_border_purchases (Brackmere City stops of touring acts) | increase | short; medium; long | CR-4 (x: Dunholt stop, y: Brackmere City stop), CR-6 | A-1, A-2, A-19 |
| C-17 | fans.selvar | travel_time | increase | short; medium; long | CR-4 | A-1, A-2, A-19 |
| C-18 | resale market (sellers and buyers of tickets for events after 1 Sep 2027) | price_paid (resales made Feb to Aug 2027) | decrease | short (announcement window) | CR-10a, CR-4 (x: now, y: later) | A-1, A-8 |
| C-19 | resale market (sellers and buyers of tickets for events after 1 Sep 2027) | quantity_traded (resales made Feb to Aug 2027) | ambiguous | short (announcement window) | CR-10a, CR-12b | A-1, A-8 |
| C-20 | bot_users | legal_breach (bot purchases for Selvar events) | decrease | short; medium; long | CR-4 (x: use bots, y: not), LW-10 | A-1, A-2, A-3 |
| C-21 | platforms.compliant | compliance_cost (screening listings against face value) | increase | short; medium; long | CR-1 op 1, CR-8c | A-2 |
| C-22 | officials.ag_consumer | enforcement_cost (resale cap and bot ban) | increase | short; medium; long | CR-1 op 4, CR-8c | none |
| C-23 | interest_groups (brokers, platforms, fan groups, primary sellers) | lobbying_effort | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-9 |
| C-24 | charities | quantity_traded (exempt charity auctions of donated tickets) | increase | short; medium; long | CR-4 (x: resell at the cap, y: give to a charity auction), CR-5 (0.7: gifts) | A-1, A-2, A-N1 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-8 in each market reached. Depth limit 4.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-25 | fans.primary | quantity_traded (primary tickets for high-demand events bought by fans) | increase | short; medium; long | CR-9, CR-6 | broker and fan purchases same_market_other_segment of primary seats (close) | A-1, A-2, A-3 |
| C-26 | fans.primary | excess_demand (fixed-face primary sales of high-demand events) | ambiguous | short; medium; long | CR-12b, CR-9 | resale substitute for primary (close) | A-1, A-2, A-3, A-10 |
| C-27 | primary_sellers (demand-priced seats) | price_paid (demand-priced seats) | increase | short; medium; long | CR-9, CR-6 | resale substitute for demand-priced primary seats (close) | A-1, A-2, A-10, A-14 |
| C-28 | primary_sellers | term_prevalence (demand-based pricing of seats) | increase | medium; long | CR-4 (x: fixed face, y: demand pricing) | - | A-1, A-15 |
| C-29 | primary_sellers | net_price_received (primary tickets for high-demand events) | increase | medium; long | CR-9, CR-6, CR-4 | - | A-1, A-2, A-10, A-14; or A-1, A-15 |
| C-30 | season_ticket_holders | asset_value (season seat rights) | decrease | short (from introduction, Feb 2027) | CR-7c, CR-10c | season seat right complement of single-game resale (close) | A-1, A-2, A-16 |
| C-31 | sellers.resale.brokers (season tickets) | quantity_traded (season ticket renewals by brokers) | decrease | medium | CR-4 (x: renew, y: not), CR-9 | season ticket input_to single-game resale (close) | A-17 |
| C-32 | fans.waiting_list | wait_time (season ticket waiting list) | decrease | medium; long | CR-9 | same season tickets (close) | A-17 |
| C-33 | primary_sellers (football club) | quantity_traded (season tickets sold) | no_change | medium | CR-9, CR-12e (arithmetic) | same season tickets (close) | A-17 |
| C-34 | sellers.bots | quantity_traded (bot software used for Selvar events) | decrease | medium; long | CR-9, LW-10 | bot software input_to broker purchases (close) | A-1, A-2, A-3 |
| C-35 | buyers.neighboring_jurisdictions (Brackmere City) | price_paid (resale tickets to Brackmere City stops) | increase | short; medium; long | CR-9, CR-6 | Dunholt and Brackmere City stops across_border (partial) | A-1, A-2, A-19 |
| C-36 | officials.ag_consumer | enforcement_cost (other consumer-protection work) | decrease | short; medium; long | CR-8a | - | A-21 |
| C-37 | taxpayers | resources_available_other_uses | no_change | short; medium; long | CR-8b | - | A-21 |
| C-38 | buyers.resale (who obtain tickets at the cap) | resources_available_other_uses | increase | short; medium; long | CR-8b, CR-5c | - | A-1, A-2 |
| C-39 | sellers.resale | resources_available_other_uses | decrease | short; medium; long | CR-8b, CR-3c | - | A-1, A-2 |
| C-40 | buyers.resale (high-demand events) | full_cost_per_unit | ambiguous | short; medium; long | CR-12b, CR-6 | - | A-1, A-2 |
| C-41 | platforms.compliant | asset_value | U1-a: decrease; U1-b: ambiguous | short (from introduction, Feb 2027) | CR-7c, CR-10c, CR-12b | - | A-1, A-2, A-3 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| buyers.resale, price_paid, all (U1-b) | buyer fee rises as the open margin (CR-6 0.8) | the cap on the price | A-N2: the fee does not absorb the whole gap (p 0.75) | U1-a: decrease; U1-b: decrease (C-1) |
| platforms.compliant, fee revenue per resale (U1-b) | fee rises as the open margin | percentage of a lower price | None | U1-a: decrease; U1-b: ambiguous (C-3) |
| fans.primary, excess_demand, all | fans move from resale to primary (A-10) | brokers withdraw (A-3) | None | ambiguous (C-26) |
| primary_sellers, price_paid (demand-priced seats) | fans move from resale (A-10, A-14) | brokers withdraw (A-22, p 0.4) | Kind (2) opposing chain below 0.5: derived sign reported (CR-12 0.8) | increase (C-27) |
| resale market, quantity_traded, Feb to Aug 2027 | sellers bring resales forward (A-8) | buyers defer (A-8) | None | ambiguous (C-19) |
| resale market, price_paid, Feb to Aug 2027 | - | sellers forward and buyers defer | Same direction | decrease (C-18) |
| buyers.resale, full_cost_per_unit | waiting, search, tie-ins, informal risk | money price | None | ambiguous (C-40) |
| bot_users, legal_breach | - | cap removes the margin (A-3); K2 (A-13, p 0.45, not reported) | Same direction | decrease (C-20) |
| platforms.compliant, asset_value (U1-b) | buyer fee | fewer resales, compliance | None | U1-a: decrease; U1-b: ambiguous (C-41) |
| Brackmere City, price_paid | Selvar fans (A-19) | broker buying adds resale supply and primary demand alike | Broker chain has no sign of its own | increase (C-35) |
| season tickets sold by the club | waiting list buys | brokers do not renew (C-31) | CR-12e arithmetic: 5,700 released, fewer than 9,000 waiting | no_change (C-33) |

C-5 (waiting, search or allocation criteria) is a group sign because CR-6 licenses only "at least one margin". C-38 and C-39 are the two sides of one transfer (CR-8b) and are different classes, not netted.

## 8. Time structure

- **Introduction to start (3 Feb to 31 Aug 2027).** The cap became expected at introduction and certain at signing in May. Broker businesses and season seat rights lose value as passage becomes likely (C-14, C-30; CR-7c, CR-10c). Resales of tickets for autumn events are brought forward into the window and buyers defer: the window's price falls (C-18) and its quantity moves either way (C-19). After 1 September the counterpart is the lower compliant resale volume (C-9). Resale contracts made before 1 September are exempt, which is what makes bringing sales forward possible.
- **From 1 September 2027.** The cap binds on compliant platforms at once (C-1 to C-5); listings move offshore and informal (C-7, C-8) as quickly as sellers can relist.
- **Medium run.** Brokers exit or move to Brackmere City as their capital turns over (C-13, C-15; CR-10b). Season ticket renewals by brokers fall at the next renewal (C-31), shortening the waiting list (C-32). Primary sellers extend demand pricing as new tours and seasons are priced (C-28, C-29).
- **Persistence.** The Act has no expiry; the stock effects (fewer brokers, more demand pricing) persist as long as it stays.

## 9. Opportunity costs

Each is written as a signed change in a variable.

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-5 | buyers.resale (high-demand events) | wait_time (+), search_cost (+), allocation_by_non_price_criteria (+) | at_least_one_increase | Fans' time spent waiting and searching, and allocation to buyers who are not those willing to give most | CR-6 |
| C-9 | platforms.compliant | quantity_traded (resales of high-demand tickets) | decrease | Resale exchanges at the market price that no longer take place (CR-5a): gains to both buyer and seller | CR-4, CR-5a, CR-9 |
| C-12 | buyers.resale (high-demand events) | side_payments (tie-in package items) | increase | Package items bought only to obtain the ticket | CR-6, CR-4 |
| C-17 | fans.selvar | travel_time | increase | Fans' time spent traveling to Brackmere City | CR-4 |
| C-21 | platforms.compliant | compliance_cost (screening listings against face value) | increase | Platform staff and systems screening listings | CR-1 op 1, CR-8c |
| C-22 | officials.ag_consumer | enforcement_cost (resale cap and bot ban) | increase | Division staff time on the cap and the bot ban | CR-1 op 4, CR-8c |
| C-23 | interest_groups (brokers, platforms, fan groups, primary sellers) | lobbying_effort | increase | Resources spent lobbying | CR-4 (x: accept, y: lobby), CR-8c |
| C-36 | officials.ag_consumer | enforcement_cost (other consumer-protection work) | decrease | Other consumer-protection work not done | CR-8a |
| C-39 | sellers.resale | resources_available_other_uses | decrease | Resale receipts sellers would have used elsewhere | CR-8b, CR-3c |

CR-8b symmetry: the money price buyers save at the cap (C-38) is what sellers lose (C-39); above-cap receipts that move offshore are captured by offshore platforms and informal sellers (C-7, C-8). The enforcement work (C-22) is withdrawn from the division's other work (C-36), not from taxpayers (C-37). Seats brokers no longer take are gained by fans (C-25), and the club's released season seats by the waiting list (C-32).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | For high-demand events, the market resale price is above face value plus 10%, so K1 binds. | binding | 0.95 | 545,000 resales a year above the cap; median markup 70%. | These consequences fail or lose this chain: C-1, C-2, C-3, C-4, C-5, C-6, C-7, C-8, C-9, C-10, C-11, C-12, C-13, C-14, C-16, C-17, C-18, C-19, C-20, C-24, C-25, C-26, C-27, C-28, C-29, C-30, C-34, C-35, C-38, C-39, C-40, C-41. |
| A-2 | Compliant platforms, which carry 77% of resale by value, enforce the cap on their listings. | enforcement | 0.85 | Offices and assets in Selvar; existing compliance with state consumer law. | These consequences fail or lose this chain: C-1, C-2, C-3, C-4, C-5, C-6, C-8, C-9, C-13, C-16, C-17, C-20, C-21, C-24, C-25, C-26, C-27, C-29, C-30, C-34, C-35, C-38, C-39, C-40, C-41. |
| A-3 | Brokers' purchases in primary sales are made mainly to resell above face value, so the cap removes most of their gain on Selvar high-demand events. | other | 0.75 | Broker margins concentrated in high-demand events. | These consequences fail or lose this chain: C-6, C-9, C-13, C-14, C-20, C-25, C-26, C-34, C-41. |
| A-4 | The expected penalty for individual above-cap resales outside compliant platforms is small enough that some take place. | enforcement | 0.8 | $500 civil penalty, a fixed budget, no criminal penalty. | These consequences fail or lose this chain: C-7, C-10. |
| A-5 | Offshore platforms with no Selvar presence are hard for the Attorney General to reach. | enforcement | 0.65 | No assets in Selvar; experience with offshore gambling and pharmacy sites. | These consequences fail or lose this chain: C-7, C-8, C-9, C-10. |
| A-6 | Some brokers keep reselling Selvar tickets outside the cap and keep using bots for it. | other | 0.6 | Existing bot use despite R1; offshore channels. | These consequences fail or lose this chain: C-7, C-8, C-9, C-10. |
| A-7 | Platforms compete for listings and for buyers. | other | 0.7 | Two national platforms plus the club's exchange and offshore rivals. | These consequences fail or lose this chain: C-1. |
| A-8 | Holders and buyers know from February 2027 that resales from 1 September will be capped, and can time their sales and purchases. | expectations | 0.7 | Press coverage; platforms' notices; tickets for autumn events on sale in spring. | These consequences fail or lose this chain: C-18, C-19. |
| A-9 | Brokers, platforms, fan groups and primary sellers can organize at a cost below their stakes. | other | 0.85 | Existing trade associations and fan groups active on the bill. | These consequences fail or lose this chain: C-23. |
| A-10 | Some fans who would have bought on resale at the market price now try to buy in the primary sale, including demand-priced seats. | substitutability | 0.7 | Resale buyers who also tried the primary sale; seat-category substitution. | These consequences fail or lose this chain: C-26, C-27, C-29. |
| A-11 | Buyers sue in meaningful numbers to recover three times the excess. | enforcement | 0.45 | Small sums per ticket against the cost of suing. | Not reported (p below 0.5). |
| A-12 | Under the Attorney General's existing practice, packages whose other items carry most of the price are not treated as tickets, so some sellers use them. | enforcement | 0.6 | The division's guidance under R3. | These consequences fail or lose this chain: C-11, C-12. |
| A-13 | K2 is enforced enough to cut bot purchases beyond what R1 already did. | enforcement | 0.45 | Most bot users are out of state; R1 already blocks many bots. | Not reported (p below 0.5); C-20 rests on the cap chain instead. |
| A-14 | Demand-based prices respond to demand within the sale period. | other | 0.8 | The promoter's pricing practice. | These consequences fail or lose this chain: C-27, C-29. |
| A-15 | Primary sellers who already price some seats by demand find it worth doing for more seats once resale is capped. | other | 0.55 | Their existing use of demand pricing; reputational cost of extending it. | These consequences fail or lose this chain: C-28, C-29. |
| A-16 | Season seat rights trade at a price that reflects expected resale of games. | expectations | 0.7 | Club transfers of seat rights; prices higher for seats with resale value. | These consequences fail or lose this chain: C-30. |
| A-17 | Brokers hold about 15% of season tickets mainly to resell single games, and renew fewer once resale is capped. | other | 0.7 | Club data on holders who resell most games. | These consequences fail or lose this chain: C-31, C-32, C-33. |
| A-18 | Broker businesses are valued on expected earnings, and buyers of them expected the cap from introduction. | expectations | 0.6 | Sales of resale businesses. | These consequences fail or lose this chain: C-14. |
| A-19 | Some fans of a touring act substitute the Brackmere City stop for Dunholt. | substitutability | 0.55 | 40% of arena tours play both; 55 minutes' drive. | These consequences fail or lose this chain: C-16, C-17, C-35. |
| A-20 | Brokers shift some of their buying from Selvar to Brackmere City events. | mobility | 0.6 | Brokers already buy for both. | These consequences fail or lose this chain: C-15. |
| A-21 | The division's budget does not rise with the new work. | revenue_use | 0.8 | K4: no new appropriation. | These consequences fail or lose this chain: C-36, C-37. |
| A-22 | Brokers bought a material share of demand-priced seats, so their withdrawal lowers demand for them. | other | 0.4 | Demand-priced seats leave little resale margin. | Not reported (p below 0.5): the opposing chain to C-27 (kind 2, CR-12 0.8). |
| A-N1 | Some holders of high-demand tickets who cannot attend give them to exempt charity auctions rather than resell at the cap. | substitutability | 0.5 | NEW, flagged. K1 exempts charity auctions; existing charity ticket auctions; at the cap a holder recovers little more than face, so a gift costs little more than a capped sale. Needed for C-24; at the cut-off. | These consequences fail or lose this chain: C-24. |
| A-N2 | Under U1-b, platforms do not raise buyer fees by the whole gap between the cap and the market price. | enforcement | 0.75 | NEW, flagged. 'Reasonable fee' would be tested by the division; platforms compete for buyers (A-7); a fee several times the usual 18% would be conspicuous. Needed for the U1-b sign of C-1. | These consequences fail or lose this chain: C-1. |

**Not reported** (an assumption below 0.5):
- Buyers recover three times the excess in meaningful numbers, which would raise the expected cost of above-cap resales by individuals (CR-4, x: comply, y: violate): needs A-11 (p 0.45).
- K2 cuts bot purchases beyond R1 (CR-4, x: use bots, y: not): needs A-13 (p 0.45). Its direction is the same as C-20, so it would not change a sign.
- Brokers' withdrawal lowers demand for demand-priced seats, pushing their price down (CR-9, CR-6): needs A-22 (p 0.4). Recorded as a kind (2) opposing chain to C-27; with p below 0.5 the derived sign stands.
- Tier C notes (no premise in the case): whether primary sellers drop non-transferable terms (R2) now that resale profits are capped; whether less enforcement elsewhere (C-36) raises violations of other consumer law; whether informal prices include a risk premium above the counterfactual market price.

## 11. Report

**The policy:** From 1 September 2027, no one may resell a ticket to an event in Selvar for more than face value plus 10%, on any platform, with a $500 civil penalty per ticket and treble damages to buyers. Using or selling software that evades primary sellers' purchase limits carries $2,500 per ticket. Primary prices are not limited. Charity auctions and contracts made before 1 September are exempt. No new enforcement money is provided.

**Visible consequences:** Fans who buy resale tickets for high-demand events on the national platforms and the club's exchange pay less (C-1), and resellers receive less (C-2). More primary tickets for high-demand events go to fans rather than brokers (C-25). Football fans on the season ticket waiting list wait less (C-32).

**Invisible consequences:**
- *Resale buyers:* At the capped price more want tickets than are offered (C-4); tickets go by waiting, searching or other criteria (C-5) and some come with tie-in packages (C-12). Buyers who do get tickets at the cap keep more for other uses (C-38). Those who buy offshore or informally get less information and recourse (C-10).
- *Resellers and brokers:* Sellers have less (C-39). Above-cap resale moves to offshore platforms, social media and in-person sales (C-7, C-8) and into packages (C-11). Brokers buy fewer primary tickets (C-6), exit (C-13), move buying to Brackmere City (C-15), renew fewer season tickets (C-31), and their businesses lose value from the bill's introduction (C-14). Bot use for Selvar events falls (C-20, C-34).
- *Platforms:* Compliant platforms carry fewer high-demand resales (C-9) and spend on screening listings (C-21).
- *Primary sellers:* Prices of demand-priced seats rise as fans turn to them (C-27), more seats are priced by demand (C-28), and primary revenue for high-demand events rises (C-29). The club still sells all its season tickets (C-33). Season seat rights lose value (C-30).
- *Elsewhere:* Some Selvar fans travel to Brackmere City (C-16, C-17), where resale prices rise (C-35). The AG's division spends on the Act (C-22) and does less of its other work (C-36); taxpayers pay nothing more (C-37). Charity auctions receive more tickets (C-24). Interest groups lobby (C-23).
- *Before the start:* Resales for autumn events are brought forward into February to August 2027 at lower prices (C-18).

**Ambiguous effects:** Platforms' fee revenue per resale and their business value under U1-b (C-3, C-41: higher fees on top, fewer and cheaper resales). Excess demand in fixed-face primary sales (C-26: brokers leave, fans arrive). The full cost to fans of a high-demand ticket (C-40: lower money price, more waiting, searching and risk). The number of resales in the announcement window (C-19).

**Key conditions:** The cap binds for high-demand events (A-1, 0.95) and compliant platforms enforce it (A-2, 0.85); brokers' gain is mostly removed (A-3, 0.75); penalties outside compliant platforms are small (A-4, 0.8) and offshore platforms hard to reach (A-5, 0.65); fans turn to the primary sale (A-10, 0.7) where demand prices respond (A-14, 0.8). Added premises: some holders give tickets to charity auctions (A-N1, 0.5, at the cut-off); under U1-b fees do not absorb the whole gap (A-N2, 0.75). Under U1-a the buyer pays at most face plus 10% in all and platforms' fee per resale falls; under U1-b fees rise on top and their direction for platforms is unclear.

**What this analysis cannot say:** How much resale moves offshore or informal, how far primary prices rise, or whether fans as a group pay more or less in full cost. It does not weigh buyers' gains against sellers' losses or say whether the Act is good. Safety effects of informal sales (fraud, crowding) are out of scope except as information (C-10).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.resale (high-demand events, compliant platforms) | price_paid (resale tickets, including buyer fees) | U1-a: decrease; U1-b: decrease | short; medium; long | visible | B | CR-1 (op 1: compliant platforms enforce the cap on listings, A-2, and the cap binds, A-1); CR-5c (the terms of exchanges that do take place lie within the range now allowed). U1-a: the total paid is at most face plus 10%. U1-b: the buyer fee is an open margin (CR-6 0.8) and rises, but platforms do not raise it by the whole gap, since 'reasonable' would be tested and platforms compete for buyers (A-N2, A-7) | A-1, A-2 (U1-b also A-7, A-N2) |
| C-2 | sellers.resale (brokers and fans, compliant platforms) | net_price_received | decrease | short; medium; long | visible | B | CR-1 and CR-5c: the price a seller may receive on a compliant platform is at most face plus 10% (U1-b) or face plus 10% less the buyer fee (U1-a), below the market price where the cap binds (A-1, A-2) | A-1, A-2 |
| C-3 | platforms.compliant | net_price_received (fee revenue per high-demand resale) | U1-a: decrease; U1-b: ambiguous | short; medium | invisible | B | U1-a: fees are percentages of a capped price and fall inside it (CR-5c). U1-b: CR-12b over (-) a percentage of a lower price and (+) the buyer fee as the open margin to which the capped pressure moves (CR-6 0.8). No premise decides | A-1, A-2 |
| C-4 | buyers.resale (high-demand events) | excess_demand (compliant resale market) | increase | short; medium; long | invisible | B | CR-6 (at the capped price more buyers wish to buy than sellers wish to sell; A-1, A-2) | A-1, A-2 |
| C-5 | buyers.resale (high-demand events) | wait_time (+), search_cost (+), allocation_by_non_price_criteria (+) | at_least_one_increase | short; medium; long | invisible | B | CR-6 (the gap closed by price no longer closes; the pressure moves to queues, search and first-come or favoritism criteria on compliant platforms). CR-6 licenses only that at least one margin is used | A-1, A-2 |
| C-6 | sellers.resale.brokers | quantity_traded (primary purchases for Selvar high-demand events) | decrease | short; medium; long | invisible | B | CR-4 (x: buy primary tickets to resell, y: use the capital elsewhere; the cap removes most of the gain on Selvar high-demand events, A-3, so brokers at the margin switch); CR-7a | A-1, A-2, A-3 |
| C-7 | sellers.resale | informal_activity (above-cap resales of Selvar tickets on offshore platforms, social media and in person) | increase | short; medium; long | invisible | B | CR-6 (exchanges outside the rule are a margin where the expected gain exceeds the expected penalty); CR-4 (x: sell at the cap on a compliant platform, y: sell above it elsewhere; the $500 penalty with a fixed budget is small, A-4; offshore platforms are hard to reach, A-5). Independent chains (CR-12d) | A-1, A-4; or A-1, A-5, A-6 |
| C-8 | platforms.offshore | quantity_traded (resales of Selvar tickets) | increase | short; medium; long | invisible | B | CR-4 (sellers move listings from compliant platforms to offshore ones where they can sell above the cap, A-5; brokers keep reselling outside the cap, A-6); CR-9 (offshore platforms are a substitute channel) | A-1, A-2, A-5, A-6 |
| C-9 | platforms.compliant | quantity_traded (resales of high-demand tickets) | decrease | short; medium; long | invisible | B | CR-4 (brokers buy fewer tickets to resell, C-6, A-3, and move listings offshore, C-8, A-5); CR-5a (exchanges that would have taken place at the market price do not). Independent chains (CR-12d) | A-1, A-2, A-3; or A-1, A-2, A-5, A-6 |
| C-10 | buyers.resale (informal channels) | quality_information | decrease | short; medium; long | invisible | B | CR-11b (exchanges moved outside the legal market lose the platforms' guarantees, reputations and legal recourse; R3 still forbids fake tickets but enforcement is through the same budget) | A-1, A-4; or A-1, A-5, A-6 |
| C-11 | sellers.packages | reclassification (tickets sold inside hospitality packages) | increase | short; medium; long | invisible | B | CR-4 (x: sell a ticket at the cap, y: sell a package whose other items carry most of the price, which the AG's practice does not treat as a ticket, A-12) | A-1, A-12 |
| C-12 | buyers.resale (high-demand events) | side_payments (tie-in package items) | increase | short; medium; long | invisible | B | CR-6 (tie-ins are a margin open to the capped pressure); C-11 (sellers use packages, A-12) | A-1, A-12 |
| C-13 | sellers.resale.brokers | number_of_sellers (brokers active in Selvar events) | decrease | medium; long | invisible | B | CR-4 and CR-7a (with most of the gain on Selvar high-demand events removed, A-3, some brokers move their capital and effort to other uses) | A-1, A-2, A-3 |
| C-14 | sellers.resale.brokers | asset_value (broker businesses) | decrease | short (from introduction, Feb 2027) | invisible | B | CR-10c (the value of a broker business reflects expected earnings); CR-7c (the expected fall in earnings, A-3, is borne by whoever owns it when the cap becomes expected, from introduction, A-18, partly as passage became more likely) | A-1, A-3, A-18 |
| C-15 | sellers.resale.brokers | quantity_traded (purchases for Brackmere City events) | increase | medium; long | invisible | B | CR-4 (x: buy for Selvar events, y: buy for Brackmere City events; y unchanged, x made worse); CR-7a (brokers move buying toward the higher yield, A-20) | A-20 |
| C-16 | fans.selvar | cross_border_purchases (Brackmere City stops of touring acts) | increase | short; medium; long | invisible | B | CR-6 (buyers who cannot get a ticket at the capped price in Dunholt seek other margins); CR-4 (x: the Dunholt stop, now rationed, y: the Brackmere City stop, 55 minutes away, A-19) | A-1, A-2, A-19 |
| C-17 | fans.selvar | travel_time | increase | short; medium; long | invisible | B | C-16: fans who switch to the Brackmere City stop travel further (A-19) | A-1, A-2, A-19 |
| C-18 | resale market (sellers and buyers of tickets for events after 1 Sep 2027) | price_paid (resales made Feb to Aug 2027) | decrease | short (announcement window) | invisible | B | CR-10a (holders know from February that resales from 1 September are capped, A-8); CR-4 (sellers: x: resell after 1 Sep at the cap, y: resell before at the market price; y made better, so they bring sales forward; buyers: x: buy before at the market price, y: buy after at the cap; y made better, so some wait). Both raise sellers relative to buyers in the window, so the price falls (CR-6) | A-1, A-8 |
| C-19 | resale market (sellers and buyers of tickets for events after 1 Sep 2027) | quantity_traded (resales made Feb to Aug 2027) | ambiguous | short (announcement window) | invisible | B | CR-12b: (+) sellers bring resales forward; (-) buyers defer purchases to the capped period (both A-8). No premise decides | A-1, A-8 |
| C-20 | bot_users | legal_breach (bot purchases for Selvar events) | decrease | short; medium; long | invisible | B | LW-10 (a bot is valued for the resale margin it brings); CR-4 (the cap removes most of that margin on Selvar high-demand events, A-3, so bot use falls). A-6: some continue for offshore resale, which limits but does not reverse the fall. K2's own chain needs A-13 (p 0.45), same direction, not reported | A-1, A-2, A-3 |
| C-21 | platforms.compliant | compliance_cost (screening listings against face value) | increase | short; medium; long | invisible | B | CR-1 (platforms are bound and enforce the cap, A-2, which requires checking each listing against the primary seller's recorded face value); CR-8c | A-2 |
| C-22 | officials.ag_consumer | enforcement_cost (resale cap and bot ban) | increase | short; medium; long | invisible | A | CR-1 (K4 assigns the work to the division); CR-8c (resources spent enforcing are used up) | none |
| C-23 | interest_groups (brokers, platforms, fan groups, primary sellers) | lobbying_effort | increase | short; medium; long | invisible | B | CR-4 (brokers and platforms gain from repeal or a wider fee reading, fan groups and primary sellers from keeping the cap; each can organize, A-9); CR-8c | A-9 |
| C-24 | charities | quantity_traded (exempt charity auctions of donated tickets) | increase | short; medium; long | invisible | B | CR-1 (charity auctions are exempt, op 2 relative to capped resale); CR-4 (holders who cannot attend: x: resell at the cap, now worth less, y: give the ticket to a charity auction; some at the margin switch, A-N1); CR-5 0.7 (a gift the giver ranks above keeping it) | A-1, A-2, A-N1 |
| C-25 | fans.primary | quantity_traded (primary tickets for high-demand events bought by fans) | increase | short; medium; long | visible | B | CR-9 (brokers compete with fans for the same primary seats; brokers buy fewer, C-6, A-3); with fixed-face seats rationed, the seats brokers no longer take go to other buyers | A-1, A-2, A-3 |
| C-26 | fans.primary | excess_demand (fixed-face primary sales of high-demand events) | ambiguous | short; medium; long | invisible | B | CR-12b: (-) brokers withdraw from primary sales (C-6, A-3); (+) fans who would have bought on resale at the market price try the primary sale (A-10). No premise decides | A-1, A-2, A-3, A-10 |
| C-27 | primary_sellers (demand-priced seats) | price_paid (demand-priced seats) | increase | short; medium; long | invisible | B | CR-9 (resale tickets and demand-priced primary seats are substitutes; with resale capped and rationed, fans move to demand-priced seats, A-10); CR-6 (demand-based prices move toward the new clearing level within the sale, A-14). The opposing chain, brokers' withdrawal lowering demand for these seats, needs A-22 (p 0.4): kind (2) below 0.5, so the derived sign is reported (CR-12 0.8) | A-1, A-2, A-10, A-14 |
| C-28 | primary_sellers | term_prevalence (demand-based pricing of seats) | increase | medium; long | invisible | B | CR-4 (x: sell at a fixed face below the clearing price, leaving the gap to resellers and queues, y: price by demand and capture it; with resale capped, the gap is no longer taken by resellers and buyers turn to the primary sale, so y yields more for sellers who already found it worth doing on some seats, A-15) | A-1, A-15 |
| C-29 | primary_sellers | net_price_received (primary tickets for high-demand events) | increase | medium; long | invisible | B | From C-27 (higher prices on demand-priced seats, A-10, A-14) and C-28 (more seats priced by demand, A-15). Independent chains (CR-12d) | A-1, A-2, A-10, A-14; or A-1, A-15 |
| C-30 | season_ticket_holders | asset_value (season seat rights) | decrease | short (from introduction, Feb 2027) | invisible | B | CR-10c (seat rights are valued for the expected resale of games, A-16); CR-7c (the capped resale value is borne by whoever holds the rights when the cap becomes expected) | A-1, A-2, A-16 |
| C-31 | sellers.resale.brokers (season tickets) | quantity_traded (season ticket renewals by brokers) | decrease | medium | invisible | B | CR-4 (brokers hold season tickets to resell single games; with that capped they renew fewer, A-17) | A-17 |
| C-32 | fans.waiting_list | wait_time (season ticket waiting list) | decrease | medium; long | visible | B | CR-9 (seats not renewed by brokers, C-31, go to those on the list, A-17) | A-17 |
| C-33 | primary_sellers (football club) | quantity_traded (season tickets sold) | no_change | medium | invisible | B | CR-9 (broker non-renewals, C-31); CR-12e arithmetic: at most about 5,700 seats are released, fewer than the 9,000 on the waiting list, who already wish to buy at the club's price, so the seats are resold and the number sold is unchanged | A-17 |
| C-34 | sellers.bots | quantity_traded (bot software used for Selvar events) | decrease | medium; long | invisible | B | CR-9 and LW-10 (demand for bots follows the resale margin they serve, C-20) | A-1, A-2, A-3 |
| C-35 | buyers.neighboring_jurisdictions (Brackmere City) | price_paid (resale tickets to Brackmere City stops) | increase | short; medium; long | invisible | B | CR-9 (Selvar fans add to demand for Brackmere City stops, C-16, A-19); CR-6 (with fixed-face primary prices, resale prices rise toward the new clearing level). Broker purchases moving there (C-15) add both supply on resale and demand on primary, so they give no sign of their own | A-1, A-2, A-19 |
| C-36 | officials.ag_consumer | enforcement_cost (other consumer-protection work) | decrease | short; medium; long | invisible | B | CR-8a (with no new appropriation, A-21, resources directed to K1 and K2 are withdrawn from the division's other work, including R3) | A-21 |
| C-37 | taxpayers | resources_available_other_uses | no_change | short; medium; long | invisible | B | CR-8b (no payment is made; the division's budget does not rise, A-21). Penalty receipts are not signed, since their scale rests on enforcement premises the case does not supply | A-21 |
| C-38 | buyers.resale (who obtain tickets at the cap) | resources_available_other_uses | increase | short; medium; long | invisible | B | CR-5c and CR-8b (they pay less than the market price for the tickets they would have bought anyway; the difference is taken from sellers, C-2, and kept for other uses; they keep buying, so the CR-3 note's condition holds) | A-1, A-2 |
| C-39 | sellers.resale | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-8b (the other side of C-38: sellers who keep reselling at the cap receive less, C-2) | A-1, A-2 |
| C-40 | buyers.resale (high-demand events) | full_cost_per_unit | ambiguous | short; medium; long | invisible | B | CR-12b: (-) the money price falls on compliant platforms (C-1); (+) waiting, search and tie-ins rise (C-5, C-12), and informal purchases carry less information and some risk (C-10). CR-6 says the full price moves toward the clearing level as far as open margins allow, not that it reaches or passes it | A-1, A-2 |
| C-41 | platforms.compliant | asset_value | U1-a: decrease; U1-b: ambiguous | short (from introduction, Feb 2027) | invisible | B | CR-7c and CR-10c (expected earnings are capitalized when expected). U1-a: lower fees per resale (C-3) and fewer resales (C-9), plus compliance cost (C-21). U1-b: (+) a higher buyer fee as the open margin against (-) fewer resales and compliance cost; no premise decides | A-1, A-2, A-3 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-037-C1: None needed. The one step that came close is the primary sellers' fixed face value: it is a price below the clearing level set by the sellers' own choice (CR-2), not by a rule, and K1 then caps the market that cleared the gap. CR-6's main clause ("whatever the reason the price is where it is") covered it, but the rules do not say how a chosen below-clearing price and a legal cap on resale combine (who now captures the gap: buyers at the cap, primary sellers through demand pricing, or queues).

**(b) Core-rule wording that was hard to apply.**
- CR-6 (0.8, a free price's rise is enough) with U1-b: the platform fee is a free price on top of a capped one, so under U1-b its rise satisfies CR-6 alone. That made the buyer's total price under U1-b need an added premise (A-N2) to be signed; the rule does not say whether a capped price plus a free fee is one price or two.
- CR-10a with an exemption for contracts made before the start: the per-window signs for the announcement window conflicted between quantity (ambiguous) and price (decrease). The rule and the normal form handled it, but the quantity of tickets resold across both windows is the same stock of tickets resold earlier or later, and neither the rule nor 2.5 says whether the same ticket counted in two windows is one action or two.
- CR-1 for a jurisdictional claim the state cannot enforce (resales offshore): op 1 where enforced, op 3 where not; the operation depends on the channel, so the class was split by channel. The rule's recording note covers this but only via the enforcement premise.
- CR-12 0.8 kind (2): applied to A-22 (p 0.4). Clear, but it means the reported sign of C-27 depends on a premise being below 0.5, not on its being false.

**(c) Vocabulary missing from the ontology.**
- No actor class for platforms or marketplaces (intermediaries that charge both sides); `platforms.compliant` and `platforms.offshore` were added.
- No variable for an intermediary's fee or take rate; `net_price_received (fee revenue per resale)` was used.
- No variable for the share of a good bought by intermediaries for resale; `quantity_traded (primary tickets bought by fans)` was used.
- No variable for the share of output priced by a given method (demand pricing); `term_prevalence` was used.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on almost all of the ticket case. Both find that buyers who obtain tickets at the cap on compliant platforms pay less and resellers receive less. Both find excess demand at the cap, rationed by waiting, search or other criteria, and fewer resales on compliant platforms. Brokers buy fewer primary tickets, leave Selvar events and lose business value. Above-cap resale moves to offshore platforms, social media and packages, with tie-ins and less information for buyers. Bot use falls. More primary seats go to fans, and queue pressure at fixed-face primary sales is `ambiguous`. Demand-priced seats rise in price, opposed only by a kind 2 chain below 0.5 (A-22), and demand pricing spreads. Season seat rights lose value and the waiting list moves faster. More Selvar fans go to Brackmere City. The announcement window brings a lower resale price with an `ambiguous` quantity. Lobbying, compliance and enforcement cost rise, and other consumer-protection work is displaced. There are three sign differences. The pattern version records bot use in breach of K2 as rising `informal_activity` (C-16), counting only breaches of the new public rule against a zero baseline. Bot purchases already breached the primary sellers' terms (R1), take place in the legal primary market, and fall (its own C-15). The total paid on compliant platforms under U1-b is `ambiguous` in the pattern version (C-19). The core signs it as a decrease on an added dominance premise (A-N2), a difference of premises. Brackmere resale prices are `ambiguous` in the pattern version (C-39). The core signs an increase by treating the broker chain as having "no sign of its own", which misapplies CR-12's 0.8 kind 3. The core version omitted several RS-10 consequences of informal trade, including disputes outside the courts, fake tickets and the risk premium, along with the per-reading seller fee and the money price across all channels. The pattern version omitted travel time, charity auctions under the exemption, platforms' business value, brokers' Brackmere buying and season renewals, and the club's season sales.

Counts: M 24, V 9, S 3, OP 11, OC 7.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | V | | The pattern version records the price before fees. The core records it including the buyer fee, per reading (the pattern's C-19 key). Both find a decrease before fees. |
| C-2 | C-2 | M | | |
| C-3 | C-9 | V | | Resellers' listings on compliant channels, recorded as the platforms' `quantity_traded`. |
| C-4 | C-4 | M | | |
| C-5 | C-5 | M | | The core leaves `side_payments` out of the group and records tie-ins in C-12. |
| C-6 | C-9 | V | | The outsiders' lost exchanges are recorded as the market's lower compliant quantity (CR-5a). |
| C-7 | C-6 | V | | `quantity_demanded` against `quantity_traded` of primary tickets bought for resale. |
| C-8 | C-13 | M | | |
| C-9 | C-7 | M | | |
| C-10 | C-12 | M | | Same sign. The pattern version rests tie-ins on compliant platforms on A-4, a premise about penalties outside compliant platforms. A tie-in sold through a compliant platform needs a premise that add-ons get past the platforms' screening, or A-12 for packages, as the core uses. Pattern-version premise mismatch. |
| C-11 | C-11 | M | | |
| C-12 | C-8 | V | | The core records only the offshore platforms' side. `cross_border_purchases` (purchases made just outside the jurisdiction) is a stretch for a Selvar resident buying from an offshore website for a Selvar event. |
| C-13 | C-9 | M | | |
| C-14 | C-8 | M | | |
| C-15 | C-20, C-34 | M | | The core records bot users (C-20) and bot sellers (C-34, medium and long). Both rest the sign on the K1 chain (A-3), with K2's chain below the cut-off. |
| C-16 | C-20 | S | E | Pattern: `informal_activity` (bot use in breach of K2) increase. Core: `legal_breach` (bot purchases) decrease. Bot purchases take place in the legal primary market, so `legal_breach` is the ontology's variable, not `informal_activity`. Every bot purchase already breached R1 in the counterfactual. The number of breaching purchases falls (the pattern version's own C-15). Counting only breaches of the new rule against zero takes the wrong baseline (final check 3). That some remaining use is now unlawful is a CR-1 operation, not a consequence. Pattern-version error. The core's label also mixes a private term (R1) with a public rule (K2), so its row should say it counts purchases in breach of either. |
| C-17 | C-1, C-3 | V | | The core folds the buyer fee into C-1's U1-b derivation (it rises as the open margin) and records the platform side as fee revenue per resale (C-3: U1-a decrease, U1-b ambiguous). |
| C-18 | none | OC | E | The seller fee per ticket, U1-a `ambiguous`, U1-b decrease (platforms compete for scarce listings; a percentage of a lower price). Derivable from CR-6 and CR-9 with A-7. The core records only the platforms' total fee revenue (C-3). Core-version omission. |
| C-19 | C-1 | S | A | U1-b. Pattern: total per ticket `ambiguous` (capped price down, fee up). Core: decrease, on the premise A-N2 (p 0.75) that the fee does not absorb the whole gap. A-N2 is a dominance premise under CR-12e. The pattern version had none, so the difference is one of premises. A-N2 is weaker than it looks, though: listings on compliant platforms fall (C-3), so the total that clears the smaller quantity on those platforms could exceed the counterfactual total. A-N2 should be stated against the counterfactual total, not against "the gap". |
| C-20 | none | OC | E | Pattern: low-demand events' resale price `no_change`, Tier A, on CR-1 alone (the cap removes no option anyone was choosing). CR-9 is not checked. Fans who fail at the cap for high-demand events may turn to other events, and brokers leaving Selvar events reduce resale supply for all events. Both chains need premises, so the honest record is `no_change` from the direct operation only, or not reported. Pattern-version overclaim. The core version did not record it. |
| C-21 | C-18, C-19 | V | | Sellers bring resales forward. The core uses it as the (+) chain of C-19 and in C-18, and does not record it as its own consequence. |
| C-22 | C-18, C-19 | V | | Buyers defer purchases, recorded the same way. |
| C-23 | C-18 | M | | |
| C-24 | C-19 | M | | The pattern version cites RS-8's 0.8 Unless clause. That clause covers a policy that also improves the earlier window. Here the opposition is between sellers moving sales forward and buyers moving purchases back, which is plain CR-12b, as the core cites. |
| C-25 | C-23 | M | | |
| C-26 | C-26 | V | | Queue margins (`wait_time`, `search_cost`) against `excess_demand` in fixed-face primary sales. Both are `ambiguous` on the same two chains. |
| C-27 | C-25 | M | | |
| C-28 | C-27 | M | | Same kind 2 treatment of A-22. |
| C-29 | C-28 | M | | |
| C-30 | none (core Tier C note) | OC | E | Prices on offshore and informal channels `ambiguous`: risk premium (+), redirected buyers (+), redirected sellers (−), kind 3. The core puts the risk premium in a Tier C note "with no premise in the case". CR-7a derives it: sellers' yields are equalized net of the expected penalty, as RS-10's derivation says. A-4 is the premise. The chain is derivable, so the consequence belongs in the list. Core-version omission. |
| C-31 | none | OC | E | The resale money price across all channels is `ambiguous` (capped price on compliant platforms against the price outside the cap). The core records `full_cost_per_unit` (C-40), a different variable. Core-version omission. |
| C-32 | C-10 | M | | |
| C-33 | none | OC | E | `disputes_settled_outside_courts` increase for informal trade (CR-11b with CR-1: recourse to courts removed). Core-version omission. |
| C-34 | none | OC | E | More fake or duplicated tickets in informal trade. With reputation and courts removed, CR-4 for a seller (x: deliver a genuine ticket, y: sell a fake) has y made better, with A-4. The core version treated fraud as out of scope, but the case's scope excludes only safety at events. Core-version omission. |
| C-35 | C-30 | M | | |
| C-36 | C-32 | M | | |
| C-37 | C-14 | M | | |
| C-38 | C-16 | M | | |
| C-39 | C-35 | S | E | Pattern: Brackmere resale price `ambiguous`. Fans add demand (+). The broker chain adds resale supply but also displaces Brackmere fans from the primary sale into resale, so its own sign is ambiguous (kind 3). The core states the same broker chain but says it "gives no sign of its own" and drops it, signing an increase. CR-12's 0.8 kind 3 says a chain whose own sign is ambiguous makes the combined sign `ambiguous` unless a dominance premise covers both its directions. The parts do not cancel by construction (CR-12f). Core-version error. |
| C-40 | C-22 | M | | The core records Tier A with no premise. The pattern version carries A-21, which is not needed for the sign of the division's work on the Act. |
| C-41 | C-36 | M | | |
| C-42 | C-21 | M | | |
| C-43 | C-5 (group only) | OC | E | Pattern: `search_cost` signed alone. PC-2 and the workflow's final check 2 allow a member alone only with a premise that the margin is open and used. The premise the pattern version cites is A-2 (platforms enforce the cap), which says nothing about search. Under U1-b the free fee can carry the pressure (CR-6 0.8). Pattern-version overclaim (an analyst misapplication of PC-2). |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-15 | OP | E | Brokers move buying to Brackmere City events (CR-7a, A-20). The pattern version uses this as a chain in C-39 but does not record it. Pattern-version omission. |
| C-17 | OP | E | Selvar fans' `travel_time` increase, following from the pattern version's own C-38. Pattern-version omission. |
| C-24 | OP | E | Charity auctions receive more donated tickets: the K1 exemption is relatively better (CR-4, A-N1 at p 0.5). The pattern version did not analyze the exemption. Pattern-version omission. |
| C-29 | OP | J | Primary sellers' `net_price_received` increase, from C-27 and C-28 by independent chains. Largely a restatement of the pattern version's C-28 and C-29 for the same class. |
| C-31 | OP | E | Brokers renew fewer season tickets (A-17). The pattern version states it in its text but records only the waiting list. Pattern-version omission. |
| C-33 | OP | E | The club's season sales `no_change` by arithmetic (5,700 released, 9,000 waiting). Valid for broker seats. Non-broker holders whose seat value falls (C-30) could also renew less, which the arithmetic does not cover, though the waiting list covers them too. Pattern-version omission. |
| C-37 | OP | E | Core: taxpayers' means `no_change`. The fixed budget is right, but K4's penalties are receipts to the state whenever any are levied (CR-8b). The core says only that their scale is unknown. The row should be at least one increase with an enforcement premise, or not reported. Core-version overclaim of `no_change`. |
| C-38 | OP | J | Buyers at the cap have more for other uses (CR-8b, CR-3 note). The pattern version recorded the transfer as prices (C-1, C-2), which the final check accepts. Tie-ins (C-12) could take back part of the saving. |
| C-39 | OP | J | Sellers' means decrease, the other side of C-38. Same remark. |
| C-40 | OP | J | `full_cost_per_unit` `ambiguous`. The pattern version says under "cannot say" that it cannot tell whether fans pay more or less in total, and records the money price (C-31) instead. |
| C-41 | OP | E | Compliant platforms' value, U1-a decrease and U1-b `ambiguous` (CR-7c, CR-10c). The pattern version missed this capitalization (final check 7). Pattern-version omission. |

### Findings

- **Pattern overclaims or hidden premises.** No pattern, applied as written, produced a wrong sign here, so no row needed cause P. Two patterns lack a clause. PC-8's Unless clause misses demand withdrawn from the uncontrolled segment, which the pattern version found itself and the core version confirms (C-26 `ambiguous`; C-27 by kind 2). RS-4's If clause assumes the law stops at a boundary, where here only enforcement does; the core version handled this by recording CR-1's operations per channel. RS-8 says nothing about a market where sellers and buyers move in opposite directions, and that silence led the pattern version to cite its Unless clause for C-24. Hidden or mismatched premises in the pattern version: tie-ins on compliant platforms rest on A-4, a premise about other channels (C-10). Search is signed alone on A-2 (C-43). The Tier A `no_change` for low-demand events has no CR-9 check (C-20).
- **Errors in the core version.** CR-12 kind 3 misapplied to Brackmere resale prices (C-35). The informal-market risk premium is relegated to a Tier C note though CR-7a derives it (pattern C-30). Fraud is treated as out of scope, so disputes outside the courts and fake tickets are omitted (C-33, C-34). The seller fee per reading and the all-channel money price are omitted (C-18, C-31). Taxpayers' `no_change` (C-37) ignores penalty receipts. `legal_breach` for bot purchases mixes R1 and K2 without saying so. A-N2 is stated against "the gap" rather than against the counterfactual total.
- **Errors in the pattern version.** The bot-breach row takes the wrong variable and the wrong baseline (C-16). The Tier A `no_change` for low-demand events skips CR-9 (C-20). Search is signed alone on an unrelated premise (C-43). `cross_border_purchases` is used for offshore websites (C-12). RS-8's Unless clause is miscited (C-24). Omissions: Fans' travel time, the charity-auction exemption, compliant platforms' value, brokers' Brackmere buying and season renewals, and the club's season sales.
- **Limits of the core rules.** None produced a difference: no row needed cause K. Unclear core-rule wording: CR-12's 0.8 kind 3 does not say that a chain with offsetting parts (added supply and added demand in the same market) is a kind 3 chain unless the parts cancel by construction (CR-12f). The core version read "no sign of its own" as no chain (C-35). CR-7a does not name the expected penalty among the costs that net yields are equalized over, which made the risk premium look underivable (pattern C-30). CR-11b says the means of learning are lost. It does not say whether more fraud then follows by CR-4 or needs a separate premise (C-34). CR-6's 0.8 free-price clause does not say whether a capped price plus a free fee is one price or two (core gap (b)). CR-10a does not say whether the same ticket counted in two windows is one action or two (core gap (b)).
- **Test of 0.8 verdicts.** *RS-4, 0.7 widening (needed interpretation):* confirmed. The core version reached C-7 and C-8 from CR-1's recording rule (operation 1 where enforced, operation 3 where not, A-5), and its gap (b) raises the same point about a jurisdictional claim the state cannot enforce. *CR-6 0.8, private supplier (worked for existence; needed CR-12 for the change against the counterfactual):* confirmed. The core version signed the fixed-face primary pressure (`excess_demand`, C-26) as `ambiguous` by CR-12b over the same two chains. Neither version got a sign from the clause itself. The pattern version reports no "failed" verdict. Among the verdicts of "worked as written", the core version confirms PC-1 to PC-3, PC-16, PC-18 (correctly not used), RS-10 (except that the core omitted two of its members), CR-6's free-price clause, CR-12's three kinds (though the core misapplied kind 3 at C-35) and OC-3's baseline (same total). It adds one qualification to *RS-8 0.8 Unless:* the core reached the same signs with CR-10a and CR-12b alone, so the clause the pattern version cites is not the one doing the work.
