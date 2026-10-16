# WE-037 Ticket resale price cap and bot ban

Analyst: draft (Handbook 0.8 held-out test, corrected under 0.9)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles real ticket resale laws but is not modeled on any one of them. It is a held-out test of catalog 0.8: the 0.7 and 0.8 changes were tuned on WE-026 to WE-035, and this case was not among them. It probes a price ceiling on a secondary market only, while the primary market it resells from stays free and is supplied by sellers who often choose not to charge the clearing price (PC-1 to PC-3, PC-8, PC-16, and CR-6's 0.8 clause on a private supplier not bound by a rule); whether PC-18 (prohibited contract term) applies to a cap on a resale price; a boundary drawn by where the event is held, not where the sale is made (RS-4); informal trade (RS-10); a free price as an open margin (CR-6, 0.8); an unclear provision on platform fees; and all three kinds of opposing chain in CR-12's 0.8 clarification. Effects on safety at events are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

This version is corrected under catalog 0.9, after the blind core-only re-run (`05_examples_core/WE-037_ticket_resale_cap_core.md`). The changes are listed in "Corrections after the core-only comparison"; part (e) of "Gaps found" is the record of the 0.8 test and is kept as written.

## 1. Policy record

**Selvar Fair Ticket Act.** The State of Selvar has about 6.8 million people. Its largest city, Dunholt, has an 18,000-seat arena, a 64,000-seat stadium (home of a football club with nine home games a year), an amphitheater and three large theaters. About 9.5 million tickets a year are sold for events in Selvar. About 11% (1.05 million) are resold. Of those, about 52% (545,000) are resold above face value plus 10%, at a median markup of 70% and several times face value for the most sought-after events; the rest are resold at less, many below face value, mostly for events that do not sell out.

About 60% of resale listings come from professional brokers (about 600 of them, 40 based in Selvar); the rest from fans who cannot attend. By value, 68% of Selvar resales go through two national platforms with offices and staff in Selvar, 9% through the football club's own exchange, 11% through platforms based abroad with no presence in Selvar, and 12% through social media and in person. Typical platform fees are 18% of the resale price charged to the buyer and 10% to the seller.

Primary sellers set their own prices. A national promoter that runs about 60% of arena concerts uses demand-based pricing on about 10% of seats at high-demand events and fixed face values on the rest; many artists and the theaters use fixed face values only. The football club sells 38,000 season tickets, with a waiting list of about 9,000; brokers hold about 15% of season tickets. Season ticket holders may transfer their seat rights through the club for a fee, and those rights trade at a price. The State of Brackmere, whose capital Brackmere City is 55 minutes from Dunholt, has a 14,000-seat arena and no resale law; about 40% of the arena tours that play Dunholt also play Brackmere City.

The bill was introduced on 3 February 2027, signed on 12 May 2027, and applies to resales made on or after 1 September 2027. It has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Resale cap | `price_ceiling` | Resale of tickets to events held in Selvar | Any person who resells or offers to resell; any platform that lists or processes payment for a resale | No resale above face value plus 10%. Face value is the price charged by the primary seller, including taxes and the primary seller's own fees, as printed or recorded by the primary seller. The Act asserts jurisdiction over any resale of a ticket to an event in Selvar, wherever the parties or platform are. | Resale by registered charities at auction. Resale contracts made before 1 September 2027. |
| K2 Bot ban | `prohibition` | Software that evades a primary seller's purchase limits or access controls | Any person who uses or sells it | Civil penalty of $2,500 per ticket obtained with it. | — |
| K3 Primary sellers | Explicit non-application | Primary sales | — | "Nothing in this Act limits the price at which a primary seller or venue may sell a ticket." | — |
| K4 Enforcement | Enforcement | K1, K2 | Attorney General's consumer division | Civil penalty up to $500 per ticket resold above the cap. A buyer may recover three times the excess paid. No new appropriation: the division absorbs the work within its existing $14 million budget. | — |

Existing rules (in force in the counterfactual too):

| Rule | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Primary sellers' terms | Private contract term | Use of bots, purchase limits | Buyers in primary sales | Bots forbidden; tickets bought in breach may be cancelled. Enforced by the seller alone. | — |
| R2 Non-transferable tickets | Permitted contract term | Transfer of tickets | Primary sellers who choose it | A primary seller may make tickets non-transferable or limit resale to its own exchange. | — |
| R3 Consumer protection law | Prohibition of fraud | Fake tickets, speculative listings of tickets not held | Sellers | Enforced by the same division. | — |

Unclear provisions:
- U1, platform fees. Section 3 caps "the price" of a resale at face value plus 10%; section 5 says "nothing in this Act prevents a platform from charging a reasonable fee for its services". Reading U1-a: platform fees charged to the buyer are part of the price, so the buyer pays at most face value plus 10% in total. Reading U1-b: platform fees are charged on top of the capped price, and "reasonable" is not defined.

Readings get no probability; where a sign depends on U1, each reading's sign is reported.

Not a reading: whether a "hospitality package" (a ticket sold with parking, food or a lounge pass) is covered. The Attorney General's guidance under the existing consumer law treats a package as a ticket where the ticket is its main item, so this is an assumption about enforcement practice with a probability (A-12), not a reading (`02_ontology.md`, 2.5).

The counterfactual is Selvar without the Act, with the primary sellers' terms, R2 and R3 in place.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: a ceiling on the price of a private resale. By CR-1: for holders, removes the option of reselling above the cap where enforced (operation 1) and attaches a risk to it where not (operation 3); for buyers, removes the option of buying by offering more; for platforms, removes the option of listing above the cap, and under U1-a constrains their fee. For primary sellers, no option is removed (K3); their face value now also sets the cap on resale of their tickets (operation 3 on the option of setting a face value). The counterfactual law leaves resale prices free. | For the 545,000 resales a year above face plus 10%, at events in high demand (A-1). Not binding for events whose resale price would be lower. | PC-1 to PC-6, PC-8, PC-16, RS-3, RS-4 (0.9: reach of enforcement), RS-5, RS-10, RS-8, CR-6 (0.9: a capped price with a free fee) |
| K2 | Triangular: prohibits the use and sale of a means of buying in primary sales. It backs with a public penalty a term primary sellers already impose privately (R1): for bot users, a risk attached to an option already in breach of contract (CR-1, operation 3). That remaining bot use is now also unlawful is this operation, not a consequence; the count of purchases in breach of R1 or K2 is signed in C-16. | Where bots were used and R1 was not enough to stop them (A-13). | EN-7, CR-1, CR-4 |
| K3 | Not an intervention: the primary market is left free, so it is an uncontrolled segment next to the controlled one. | — | PC-8, CR-6 (0.8, private supplier) |
| K4 | Binary: funded from a fixed budget (A-21). The buyer's remedy works only if buyers sue: for that part, enforcement on complaint (RS-20). | Yes | OC-3 (0.9: fixed budget), RS-3, RS-20 |
| K1 exemption for charity auctions | Exemption: resale by registered charities at auction is not capped, so giving a ticket to a charity auction is made better relative to reselling it at the cap (CR-1, CR-4). | For holders who would otherwise resell at the cap (A-23). | CR-1, CR-4, CR-5 |

**PC-18 does not apply.** PC-18's If clause is a `term_prohibition` making a contract term unenforceable. K1 makes a price above the cap unlawful, with a remedy of three times the excess; that is a ceiling on the price term, which PC-1 to PC-6 and PC-16 cover. Applied anyway, PC-18's Then clause (the party who valued the term offers less on other terms or moves to substitute terms) adds nothing beyond PC-6 and RS-5 (packages, tie-ins). It has no existing contracts to void, because resale contracts made before 1 September 2027 are exempt. K2 is not a term prohibition either: it adds a public penalty to a private term (R1), the opposite operation. See Gaps found, (c) 3.

Every resale at the cap is a payment from a buyer to a reseller and a platform (CR-8b): C-1 and C-2 are its two sides, with the platform's side in C-17 and C-18.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.insiders` (`buyers.current`) | Fans who buy resale tickets to high-demand events at or under the cap | Pay less than the market resale price. |
| `buyers.outsiders` (`buyers.prospective`) | Fans who would have bought on resale at the market price and do not obtain a ticket at the cap | Wait, search, pay more outside the law, or go without. |
| `buyers.primary` | Fans buying in primary sales of high-demand events | Fewer brokers and bots compete with them; more fans who would have bought on resale join them. |
| `buyers.low_demand` | Buyers of tickets to events whose resale price would be below the cap | Nothing changes. |
| `resellers.brokers` | Professional resellers | Cannot resell above the cap on compliant platforms; bots banned. |
| `resellers.fans` | Fans reselling tickets they cannot use | Receive at most face plus 10%. |
| `platforms.compliant` | The two national platforms with Selvar presence, and the club's exchange | Cannot list above the cap; fees per U1. |
| `platforms.offshore` | Platforms based abroad with no Selvar presence | Bound in law, hard to reach in practice. |
| `informal_sellers` (`intermediaries`) | Sellers on social media and in person | Above-cap sales are now unlawful. |
| `primary_sellers.dynamic` | Primary sellers who use demand-based pricing on some seats | Not capped (K3); more fans turn to their seats. |
| `primary_sellers.fixed` | Primary sellers who set fixed face values below the clearing price by choice | Not capped; their face value now caps resale. |
| `season_holders` | Holders of football season tickets and seat rights | Cannot resell single games above the cap. |
| `season_waitlist` | Fans on the club's waiting list | More seats may come free. |
| `charities` | Registered charities that auction donated tickets | Their auctions are exempt from the cap. |
| `bot_vendors` | Sellers of bot software and services | Their product is banned. |
| `neighboring_jurisdictions` | Buyers and sellers of tickets to Brackmere City events | Not bound. |
| `officials.enforcement` | The Attorney General's consumer division | New work within a fixed budget. |
| Those protected by the division's other work | Consumers in other markets | Slower or less of the division's other work. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.insiders` | `price_paid` (resale price paid to the reseller, before platform fees) | decrease | short | PC-16, CR-6, CR-8b | A-1, A-2 |
| C-2 | `resellers.brokers`, `resellers.fans` (units sold at the cap) | `net_price_received` | decrease | short | PC-16, CR-8b | A-1, A-2 |

C-1 is what the Act's supporters point to: fans who get resale tickets pay at most face plus 10%. C-2 is the other side of the same payment (PC-16): what the buyer does not pay, the reseller does not receive. PC-16's clause that side payments and lower quality take back part of the transfer is followed in C-9 and C-10.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `resellers.brokers`, `resellers.fans` | `quantity_supplied` (resale listings of high-demand tickets on compliant channels) | decrease | short | PC-5, CR-4, CR-7 | A-1, A-2, A-3 |
| C-4 | resale market, high-demand events | `excess_demand` | increase | short | PC-1, CR-6 | A-1, A-2 |
| C-5 | `buyers.outsiders` | `wait_time`, `search_cost`, `side_payments`, `allocation_by_non_price_criteria`, and under U1-b `price_paid` (platform buyer fee) | at_least_one_increase | short | PC-2, CR-6 | A-1, A-2 |
| C-6 | `buyers.outsiders` | `quantity_traded` (high-demand tickets obtained) | decrease | short | PC-3, CR-5a | A-1, A-2 |
| C-7 | `resellers.brokers` | `quantity_demanded` (tickets bought in primary sales for resale) | decrease | short | CR-4, CR-7a, PC-12 | A-1, A-2, A-3 |
| C-8 | `resellers.brokers` | `number_of_sellers` (brokers active in Selvar events) | decrease | medium | RS-6, CR-7a | A-1, A-2, A-3 |
| C-9 | `informal_sellers`, `resellers.brokers` | `informal_activity` (resales above the cap) | increase | short | PC-6, RS-3, CR-4 | A-1, A-4 |
| C-10 | `buyers.outsiders` | `side_payments` (tie-ins: overpriced parking, merchandise or "fees" outside the ticket price) | increase | short | PC-6, CR-6, CR-12d | Outside compliant platforms: A-1, A-4. On compliant platforms: A-1, A-12. |
| C-11 | `resellers.brokers`, `primary_sellers.dynamic` | `reclassification` (tickets sold inside packages whose other items carry the price) | increase | short to medium | RS-5, CR-4 | A-1, A-12 |
| C-12 | `buyers.outsiders` | `cross_border_purchases` (purchases of Selvar tickets on offshore platforms) | increase | short | RS-4 (0.9: reach of enforcement), CR-4 | A-1, A-5 |
| C-13 | `platforms.compliant` | `quantity_traded` (resales of Selvar tickets) | decrease | short | RS-4 (0.9), CR-4, CR-9 | A-1, A-2, A-5 |
| C-14 | `platforms.offshore` | `quantity_traded` (resales of Selvar tickets) | increase | short | RS-4 (0.9), CR-4, CR-9 | A-1, A-5 |
| C-15 | `bot_vendors` | `quantity_traded` (bot software and services used on Selvar events) | decrease | short | EN-7, CR-4, CR-12d | Chain K1: A-1, A-2, A-3. Chain K2: A-13. |
| C-16 | `resellers.brokers` (bot users) | `legal_breach` (bot purchases for Selvar events, in breach of R1 or K2) | decrease | short | CR-4, LW-10, CR-12d | Chain K1: A-1, A-2, A-3. Chain K2: A-13. |
| C-17 | `buyers.insiders` (on compliant platforms) | `price_paid` (platform buyer fee per ticket) | U1-a: decrease; U1-b: increase | short | CR-6 (0.8, free price; 0.9, a capped price with a free fee), CR-5c | A-1, A-7 |
| C-18 | `resellers.brokers`, `resellers.fans` (on compliant platforms) | `price_paid` (platform seller fee per ticket) | U1-a: ambiguous; U1-b: decrease | short | CR-6, CR-9 | A-1, A-7 |
| C-19 | `buyers.insiders` (on compliant platforms) | `price_paid` (total per ticket, including fees) | U1-a: decrease; U1-b: ambiguous | short | PC-16, CR-6 (0.9), CR-12b | A-1, A-2, A-7 |
| C-21 | `resellers.brokers`, `resellers.fans` | `quantity_supplied` (resale listings of tickets to events after 1 September 2027, a flow), February to August 2027 | increase | short | RS-8, CR-10a, CR-12 (0.9) | A-1, A-8 |
| C-22 | `buyers.outsiders` | `quantity_demanded` (resale purchases of tickets to events after 1 September 2027, a flow), February to August 2027 | decrease | short | RS-8, CR-10a, CR-12 (0.9) | A-1, A-8 |
| C-23 | resale market, events after 1 September 2027 | `price_paid` (resales made February to August 2027) | decrease | short | RS-8, CR-6, CR-12a | A-1, A-8 |
| C-24 | resale market, events after 1 September 2027 | `quantity_traded` (resales made February to August 2027, a flow) | ambiguous | short | RS-8 (0.9: more timing chains), CR-12b | A-1, A-8 |
| C-25 | brokers, platforms, fan groups, primary sellers | `lobbying_effort` | increase | medium | RS-7 | A-9 |
| C-46 | `charities` | `quantity_traded` (exempt charity auctions of donated tickets to high-demand events) | increase | short | CR-1, CR-4, CR-5 | A-1, A-2, A-23 |

**The cap on a secondary market only (C-1 to C-6).** The tickets to an event are a fixed stock once the primary sale is over. The resale market moves them from those who hold them to those who value them more. For high-demand events the market resale price is above face plus 10% (A-1). At the cap, holders offer fewer tickets: a fan who cannot attend keeps the ticket for a friend, or uses it, and a broker buys fewer in the primary sale (C-3, C-7; PC-5, with the brokers' stock of tickets as the capital, so the response is in weeks, not years). Buyers want more at the lower price (CR-4c). So `excess_demand` rises (C-4, PC-1). PC-2 gives the rationing margins as a group (C-5): speed on the platform, searching, payments outside the ticket price, and favor or connections. PC-3 splits buyers: those who obtain tickets at the cap gain (C-1), those who would have paid the market price and now fail lose the exchange (C-6, CR-5a).

**PC-16 (C-1, C-2).** The ceiling is a transfer from resellers to the buyers who obtain tickets at the cap. Both sides are recorded. Resellers include fans, not only brokers: a fan who would have resold a ticket for $250 now receives at most $110 for a $100 face value.

**Informal trade and tie-ins (C-9 to C-11).** Where the expected penalty is small (a $500 civil penalty, rarely pursued against individuals; A-4), some resales above the cap take place outside compliant platforms (C-9, PC-6), and some within them through payments the cap does not reach: parking passes, merchandise, "delivery" (C-10). Tie-ins sold through compliant platforms must get past the platforms' screening, which is the same question as for packages: they rest on A-12, while tie-ins in informal sales rest on A-4 (C-10, two chains, CR-12d). Packages that bundle a ticket with other items are covered under the Attorney General's practice only where the ticket is the main item, so some sellers build packages whose other items carry the price (C-11, RS-5; A-12, p = 0.6).

**Where the boundary is (C-12 to C-14).** K1 applies to every resale of a ticket to a Selvar event, wherever it is made, so in law there is no other side. RS-4's 0.9 clause on the reach of enforcement covers this: the boundary that matters is the limit of enforcement. Platforms with Selvar offices comply; platforms based abroad, with no assets in Selvar, are hard to reach (A-5). So listings and purchases move to offshore platforms (C-12 to C-14). The event cannot move; only the sale can, so the rest of RS-4 (sellers and production relocating) does not apply.

**Bots (C-15, C-16).** Two chains reduce bot use on Selvar events. K1 lowers what a ticket bought by bot is worth to a broker (CR-4, CR-7a, LW-10; A-3); K2 attaches a penalty to bot use (A-13, p = 0.45: primary sellers already block bots under R1, and the users are mostly out of state). Same sign, independent premises: C-15 holds if either chain's premises hold (CR-12d), and here the K1 chain clears the cut-off. Bot purchases take place in the legal primary market, and every one of them already breached the primary sellers' terms (R1) in the counterfactual. Counted against that baseline, purchases in breach of R1 or K2 fall (C-16, `legal_breach`). That the bot use which remains (A-6) is now also unlawful under K2 is the operation K2 performs (CR-1), not a rise in breach.

**Platform fees (C-17 to C-19).** By CR-6's 0.9 clause on a capped price with a free fee, the buyer's price is the total paid, recorded as two items of `price_paid` (the capped part, C-1; the fee, C-17) and their total (C-19). Under U1-a, the fee is inside the cap. Sellers are now the scarce side at the cap (C-4), so platforms compete for listings and cannot raise the buyer's fee above what fits within face plus 10%: buyer fees fall (C-17, A-7). Whether seller fees rise or fall depends on how the fixed total is split, which is not derived (C-18, `ambiguous`). Under U1-b, the fee is a free price on top of the capped price. Unsatisfied buyers can offer more only through it, so the buyer fee rises (C-17), and platforms competing for scarce listings cut what they charge sellers (C-18). By CR-6's 0.8 clarification, the fee's rise satisfies the "at least one margin" conclusion by itself; the other margins then each need their own premise. C-5 therefore includes the buyer fee as a member under U1-b, and no non-price margin is signed alone. The total paid per ticket on compliant platforms falls under U1-a; under U1-b it combines the capped price (−) with the fee (+), so it is `ambiguous` (C-19).

**Not a quality claim.** PC-4 would say that platforms cut services (buyer guarantees, customer support) under the cap. Under U1-a, with the fee squeezed, that is plausible, but under U1-b nothing requires it, since the free fee carries the pressure. No per-reading sign can be stated for U1-b (the derivation establishes neither a change nor `no_change`), so the consequence is not recorded. See Gaps found, (d) 2.

**Events in low demand (no consequence).** Where the market resale price is below face plus 10%, the cap removes no option anyone was choosing (CR-1). That does not make their price unchanged: by CR-9, fans who fail at the cap for high-demand events may turn to other events, and brokers who leave Selvar events (C-8) stop reselling low-demand tickets too. Both chains would raise these prices, and each needs a premise the record does not support, so no consequence is reported.

**Announcement to effect (C-21 to C-24).** Between introduction in February and 1 September 2027, resales of tickets to later events are still free. Holders who expect to resell move their sales into the window (C-21). Buyers who expect to buy move their purchases after it, when the price is capped (C-22). Both chains push the price in the window down (C-23, CR-12a). For the quantity traded in the window, the two timing chains oppose each other (more listings, fewer buyers), so it is `ambiguous` (C-24). The opposition is between sellers and buyers moving in opposite directions in time, which RS-8's 0.9 clause on more timing chains places under its Unless clause; the 0.8 Unless clause alone (a policy that also improves the earlier window) did not cover it. All four are signed on flows, resales made in the window (CR-12, 0.9). After 1 September, C-3 and C-13 apply.

**Charity auctions (C-46).** K1 exempts resale by registered charities at auction. For a holder who cannot attend, reselling at the cap is now worth little more than face, while giving the ticket to a charity auction is unchanged, so those at the margin give (CR-4, a gift being a transfer the giver ranks above keeping the thing, CR-5's 0.7 clause; A-23, p = 0.5).

**Lobbying (C-25).** Brokers and platforms have a stake in the U1-b reading or repeal; fan groups and some artists in U1-a and stricter enforcement against offshore platforms (RS-7).

Not reported: buyers recovering three times the excess under K4 (A-11, p = 0.45: the sums per ticket are small next to the cost of suing). The private remedy is enforcement on complaint (RS-20): breach concentrates where buyers are least likely to sue, which is where C-9 and C-12 already place it.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-26 | `buyers.primary` (fixed-price high-demand events) | `wait_time`, `search_cost` (primary sale queues) | ambiguous | short | CR-6 (0.8, private supplier), CR-9, CR-12b | primary and resale: `same_market_other_segment`, close | A-1, A-3, A-10 |
| C-27 | `buyers.primary` (fixed-price high-demand events) | `quantity_traded` (primary tickets obtained by fans rather than brokers) | increase | short | CR-9, CR-5, CR-12d | as C-26 | A-1, A-3 |
| C-28 | `primary_sellers.dynamic` | `price_paid` (demand-based prices at high-demand events) | increase | short to medium | PC-8 (0.9: withdrawn demand), CR-6, CR-9 | as C-26 | A-1, A-10, A-14 |
| C-29 | `primary_sellers.dynamic` | `term_prevalence` (share of seats sold at demand-based prices) | increase | medium | PC-8, CR-4, CR-7a | as C-26 | A-1, A-10, A-14, A-15 |
| C-30 | resale market (offshore and informal channels), high-demand Selvar events | `price_paid` | ambiguous | short | RS-10, RS-16, RS-13, CR-12 (0.8 and 0.9, kind 3) | offshore and compliant channels: `same_market_other_segment`, close | A-1, A-4, A-5 |
| C-31 | buyers of resale tickets to high-demand Selvar events, all channels | `price_paid` | ambiguous | short | PC-16, RS-10, CR-12 (0.8, kind 3) | — | A-1, A-2, A-4, A-5 |
| C-32 | `buyers.outsiders` (informal channels) | `quality_information` | decrease | short | RS-10, CR-11b | — | A-4 |
| C-33 | `buyers.outsiders` (informal channels) | `disputes_settled_outside_courts` | increase | short | RS-10 | — | A-4 |
| C-34 | `buyers.outsiders` (informal channels) | `quality_variability` (fake or duplicated tickets) | increase | short | RS-10 | — | A-4 |
| C-35 | `season_holders` | `asset_value` (season seat rights) | decrease | short (part from introduction, the rest at signing) | CR-7c, CR-10c | season seat and single-game resale: `contract` | A-1, A-16 |
| C-47 | `resellers.brokers` (season tickets) | `quantity_traded` (season ticket renewals by brokers) | decrease | medium | CR-4, CR-9 | season ticket `input_to` single-game resale | A-1, A-17 |
| C-36 | `season_waitlist` | `wait_time` (club's season waiting list) | decrease | medium | CR-4, CR-9 | as C-35 | A-1, A-17 |
| C-48 | `primary_sellers.fixed` (the football club) | `quantity_traded` (season tickets sold) | no_change | medium | CR-9, CR-12e | as C-35 | A-17, A-24 |
| C-37 | `resellers.brokers` (owners) | `asset_value` (broker businesses) | decrease | short | CR-7c, CR-10c | — | A-1, A-3, A-18 |
| C-49 | `platforms.compliant` (owners) | `asset_value` | U1-a: decrease; U1-b: ambiguous | short (from introduction) | CR-7c, CR-10c, CR-12b, CR-12e | — | A-1, A-2, A-5, A-7 |
| C-38 | `neighboring_jurisdictions` (Brackmere City events) | `cross_border_purchases` (tickets bought by Selvar residents) | increase | short to medium | RS-1, RS-4, CR-9 | tour stops in Dunholt and Brackmere City: `substitute`, partial | A-1, A-19 |
| C-45 | `buyers.outsiders` (Selvar fans who go to Brackmere City stops) | `travel_time` | increase | short to medium | CR-4, CR-9 | as C-38 | A-1, A-19 |
| C-44 | `resellers.brokers` | `quantity_traded` (primary tickets bought for Brackmere City events) | increase | medium | RS-4, CR-4, CR-7a | broker capital: `across_border` | A-1, A-3, A-20 |
| C-39 | `neighboring_jurisdictions` (Brackmere City events) | `price_paid` (resale prices) | ambiguous | short to medium | RS-16, RS-13, CR-12 (0.8 and 0.9, kind 3) | as C-38; broker capital: `across_border` | A-1, A-19, A-20 |

**The primary market next to a capped resale market (C-26 to C-29).** K3 leaves the primary market free, so it is the uncontrolled segment PC-8 points to. Two kinds of primary seller must be kept apart.

- *Fixed-price sellers (C-26, C-27).* They set face values below the clearing price by their own choice. CR-6's 0.8 clause applies: a private supplier not bound by a rule rations by its own choice (queues, presales, lotteries), and the margins are signed as a group. Against the counterfactual, two derived chains reach the pressure on those margins: brokers withdraw from the queue, because the cap removes their resale gain (−, A-3, p = 0.75); fans who would have bought on resale join it, because resale at the cap is hard to obtain (+, A-10, p = 0.7). Both premises clear the cut-off, so the queue margins are `ambiguous` (C-26; CR-12, 0.8, kind 2). What is signed is who obtains the tickets: with fewer brokers in the queue, more go to fans (C-27). Whether these sellers raise their face values is not derived: the cap removes none of their options, and their reason for pricing low is their own ranking (CR-2), which the rules never assume. A suggestion that the law, by naming above-face resale as unfair, makes artists keep face values low is not derivable and is a Tier C note (CR-12, 0.8, kind 1).
- *Demand-based pricers (C-28, C-29).* For seats priced by demand, PC-8 applies: buyers who cannot obtain capped resale tickets turn to the uncontrolled seats, and their price rises (C-28, A-10, A-14). An opposing chain is derivable: brokers no longer buy demand-priced seats to resell, so demand for those seats falls (CR-9, CR-6). PC-8's 0.9 clause on withdrawn demand names this chain and asks that it be combined under CR-12b. It needs the premise that brokers bought a material share of demand-priced seats, which is unlikely, since a seat priced near its clearing level leaves a broker little margin (A-22, p = 0.4). By CR-12's 0.8 kind 2, with p below 0.5, the derived sign is reported (C-28, increase) and the chain is recorded in section 10. Sellers who already use demand pricing on some seats extend it to more (C-29, CR-4; A-15).

**Prices outside the cap (C-30, C-31).** On offshore and informal channels, three chains reach the price of a Selvar high-demand ticket: sellers there must be paid for the risk of penalty (RS-10, CR-7: +); buyers who fail at the cap turn to these channels (RS-16: +); and sellers escaping the cap list there too (RS-13: −), which is RS-16's Unless clause. Against the counterfactual market price, the second and third come from the same fall in the whole market's legal trade, so their net is itself `ambiguous`: a chain whose parts push in opposite directions and do not cancel by construction is a kind 3 chain (CR-12, 0.9). One chain (+) against a chain whose own sign is ambiguous: by CR-12's 0.8 kind 3, the combined sign is `ambiguous` (C-30), since no dominance premise covers the risk premium against both directions of the other chain. For buyers of resale tickets on all channels, the capped price on compliant platforms (−, PC-16) meets the ambiguous price outside the cap, so the total is `ambiguous` too (C-31, kind 3).

**Informal trade (C-32 to C-34).** RS-10 applies to the resales that move outside compliant platforms: no guarantees, no recourse to the platform or the courts, more fake and duplicated tickets. The extra fraud complaints fall on the same division's fixed budget (C-41).

**Season tickets (C-35, C-36).** Part of a season seat's value is the right to resell games the holder does not attend. The cap lowers that yield for high-demand games, so the value of seat rights falls, borne by holders when the Act became expected: part of the way from introduction, as passage became likely, and the rest at signing (C-35, CR-7c, CR-10c; A-16). Brokers who held season tickets for resale renew fewer of them (C-47), and the seats go to the waiting list (C-36, A-17). At most about 5,700 seats are released by brokers, against 9,000 on the waiting list; with A-24 (those released, including by other holders who renew less, are fewer than the waiting-list members who still buy at the club's price) the club sells as many season tickets as before (C-48, CR-12e, arithmetic with a premise).

**Brokers (C-37).** Brokers' businesses (client lists, accounts, software) are specific to resale; their value falls with the expected yield of Selvar events (C-37).

**Compliant platforms (C-49).** Their value reflects expected fee earnings on Selvar resales and is capitalized from introduction (CR-7c, CR-10c). Under U1-a, resales on them fall (C-13), they bear compliance costs (C-42), and fee revenue per high-demand resale falls: the buyer's whole payment is capped at face plus 10%, while platforms took about 28% of a resale price at a median markup of 70% (about 0.48 of face value), so matching that would need sellers to accept under 0.62 of face, which platforms competing for scarce listings (A-7) cannot impose (CR-12e, arithmetic with a premise). So the value falls. Under U1-b the free buyer fee rises (C-17) against fewer resales and compliance costs: `ambiguous` (CR-12b).

**Brackmere (C-38, C-39, C-44, C-45).** Fans who cannot get Dunholt tickets travel to the same tour's Brackmere City stop (C-38, A-19), and spend more time travelling (C-45). Brokers move some of their primary buying to Brackmere City events, where resale is not capped (C-44, A-20). Brackmere resale prices: those fans add demand (RS-16, +), while brokers shift their buying from Selvar events to Brackmere events, which adds resale supply but also displaces Brackmere fans from the primary sale into the resale market, a chain whose own sign is ambiguous (A-20). By CR-12's 0.8 kind 3, confirmed by its 0.9 clause (the broker chain's parts do not cancel by construction), the combined sign is `ambiguous` (C-39).

Stopping points: hotels and restaurants in Dunholt (depth 3): who gets tickets changes, but whether more or fewer visitors come is not derived; stopped. Ticket scanning and identity-verification vendors (depth 3, diffuse; stopped).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.primary`, `wait_time` and `search_cost` (fixed-price high-demand events), short | Fans redirected from resale (A-10). | Brokers withdraw (A-3); bots banned (A-13, below the cut-off, recorded under A-13). | None | **ambiguous** (C-26). CR-12 0.8, kind 2: both main premises at or above 0.5. |
| `primary_sellers.dynamic`, `price_paid`, short to medium | Buyers redirected from capped resale (PC-8, A-10, A-14). | Brokers no longer buy demand-priced seats (PC-8, 0.9: withdrawn demand; A-22, p = 0.4). | — | **increase** (C-28). CR-12 0.8, kind 2: the opposing chain's premise is below 0.5, so the derived sign is reported and the chain recorded with A-22. |
| Resale price outside the cap, short | Risk premium (RS-10); buyers redirected (RS-16). | Sellers redirected (RS-13). | None | **ambiguous** (C-30). Kind 3: the redirected buyers and sellers form a chain whose own sign is ambiguous. |
| Resale buyers, all channels, `price_paid`, short | Price outside the cap (C-30, itself ambiguous). | Capped price on compliant platforms (C-1). | None | **ambiguous** (C-31). Kind 3. |
| Brackmere resale `price_paid`, short to medium | Selvar fans redirected (A-19). | Broker redirection (A-20), itself ambiguous. | None | **ambiguous** (C-39). Kind 3. |
| `buyers.insiders`, total `price_paid` on compliant platforms, short | U1-b: platform fee (C-17). | Capped price (C-1). | None | **U1-a: decrease; U1-b: ambiguous** (C-19). |
| Bot use on Selvar events, short | — | K1 removes the resale gain (A-3); K2 penalty (A-13). | None needed | **decrease** (C-15 for bot vendors, C-16 for bot purchases in breach of R1 or K2). CR-12d: holds through the K1 chain alone. |
| Resales made February to August 2027, events after 1 September, `quantity_traded` (flow) | Holders sell early (C-21). | Buyers wait (C-22). | None | **ambiguous** (C-24); RS-8, 0.9: more timing chains. |
| Same, `price_paid` | — | Both chains. | — | **decrease** (C-23). |
| `platforms.compliant`, `asset_value`, short | U1-b: buyer fee (C-17). | Fewer resales (C-13); compliance cost (C-42); under U1-a, fee revenue per resale (A-7). | U1-a: arithmetic with A-7 (CR-12e). | **U1-a: decrease; U1-b: ambiguous** (C-49). |
| The club's season tickets sold, medium | Waiting-list buyers take released seats (A-24). | Brokers renew fewer (C-47). | CR-12e: released seats fewer than waiting buyers (A-24). | **no_change** (C-48). |

## 8. Time structure

- **Introduction to effect (February to August 2027).** Holders move resales of later events into the window; buyers delay (C-21 to C-24). Brokers buy fewer primary tickets for events after September (C-7, CR-10a). Season seat rights, broker businesses and compliant platforms lose value as passage becomes likely (C-35, C-37, C-49; for platforms under U1-a).
- **From September 2027.** Listings on compliant platforms fall (C-3, C-13), offshore and informal resales rise (C-12, C-14, C-9) and the rationing margins open (C-5). Fees adjust at once under either reading (C-17, C-18).
- **First season renewal after the Act (spring 2028).** Brokers renew fewer season tickets (C-47); the waiting list moves (C-36) and the club's sales are unchanged (C-48).
- **Medium run.** Brokers leave Selvar events (C-8) and buy more for Brackmere City events (C-44); demand pricing spreads among primary sellers who already use it (C-29).
- **Erosion.** The cap is stated as a ratio to face value, not in money, so it does not erode with prices (TS-3). It binds more or less as the gap between demand and face values changes event by event.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-40 | `officials.enforcement` | `enforcement_cost` (K1 and K2 cases) | increase | Staff time on resale and bot cases. | OC-3, CR-8c |
| C-41 | `officials.enforcement` | `enforcement_cost` (other consumer-protection cases) (−), `wait_time` (complaints handled by the division) (+) | at_least_one_as_stated | With a fixed budget, the new work comes from some other use of the division's time: fewer other cases, or slower handling. The cost falls on consumers whom that work served (OC-3, 0.9: fixed budget). | OC-3, CR-8a |
| C-42 | `platforms.compliant` | `compliance_cost` (checking face values, blocking above-cap listings) | increase | What that staff time and engineering would otherwise have done. | OC-2, CR-8c |
| C-45 | `buyers.outsiders` (Selvar fans who go to Brackmere City stops) | `travel_time` | increase | Other uses of the time spent travelling. | CR-4, CR-9 |

The resales that no longer take place (C-6) are prevented exchanges (OC-4): the reseller who would have sold above the cap and the buyer who would have paid it both lose the gain each expected. Searching at the cap is a member of C-5 and is not signed alone: PC-2 allows that only with a premise that the margin is open and used, and under U1-b the free fee can carry the pressure. (C-43, which signed it alone, has been removed.)

**OC-3 against the right baseline.** The division already enforced R3 (fraud, speculative listings) before the Act. The Act shrinks compliant resale, where speculative listings occurred, and grows informal resale, where fake tickets occur (C-34). Its effect on R3 cases is therefore `ambiguous` and not reported separately; because the budget is fixed, all of it falls within the division's total, which does not change: what rises (C-40) is matched by what falls (C-41).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | For high-demand events, the market resale price is above face value plus 10%, so K1 binds. | binding | 0.95 | 545,000 resales a year above the cap; median markup 70%. | Nearly every consequence fails. |
| A-2 | Compliant platforms, which carry 77% of resale by value, enforce the cap on their listings. | enforcement | 0.85 | Offices and assets in Selvar; existing compliance with state consumer law. | C-1 to C-6, C-13, C-19, C-46 and C-49 shrink to whatever share complies; C-9 grows. |
| A-3 | Brokers' purchases in primary sales are made mainly to resell above face value, so the cap removes most of their gain on Selvar high-demand events. | other | 0.75 | Broker margins concentrated in high-demand events. | C-3, C-7, C-8, C-37, C-44, the K1 chains of C-15 and C-16 and the (−) chain of C-26 are not reported. |
| A-4 | The expected penalty for individual above-cap resales outside compliant platforms is small enough that some take place. | enforcement | 0.8 | $500 civil penalty, a fixed budget, no criminal penalty. | C-9, C-32 to C-34 and the informal chain of C-10 are not reported; C-30 loses its risk-premium chain. |
| A-5 | Offshore platforms with no Selvar presence are hard for the Attorney General to reach. | enforcement | 0.65 | No assets in Selvar; experience with offshore gambling and pharmacy sites. | C-12 to C-14 are not reported; C-30 and C-31 lose a chain. |
| A-6 | Some brokers keep reselling Selvar tickets outside the cap and keep using bots for it. | other | 0.6 | Existing bot use despite R1; offshore channels. | No sign rests on it: it limits the fall in C-15 and C-16, and is the bot use that K2 makes unlawful. |
| A-7 | Platforms compete for listings and for buyers. | other | 0.7 | Two national platforms plus the club's exchange and offshore rivals. | C-17 and C-18 are not reported. |
| A-8 | Holders and buyers know from February 2027 that resales from 1 September will be capped, and can time their sales and purchases. | expectations | 0.7 | Press coverage; platforms' notices; tickets for autumn events on sale in spring. | C-21 to C-24 are not reported. |
| A-9 | Brokers, platforms, fan groups and primary sellers can organize at a cost below their stakes. | other | 0.85 | Existing trade associations and fan groups active on the bill. | C-25 is not reported. |
| A-10 | Some fans who would have bought on resale at the market price now try to buy in the primary sale, including demand-priced seats. | substitutability | 0.7 | Resale buyers who also tried the primary sale; seat-category substitution. | The (+) chain of C-26, C-28 and C-29 are not reported. |
| A-11 | Buyers sue in meaningful numbers to recover three times the excess. | enforcement | 0.45 | Small sums per ticket against the cost of suing. | Below the cut-off; transfers under K4's private remedy not reported. |
| A-12 | Under the Attorney General's existing practice, packages whose other items carry most of the price are not treated as tickets, so some sellers use them, and add-ons sold with tickets get past platforms' screening. | enforcement | 0.6 | The division's guidance under R3. | C-11 and the compliant-platform chain of C-10 are not reported. |
| A-13 | K2 is enforced enough to cut bot purchases beyond what R1 already did. | enforcement | 0.45 | Most bot users are out of state; R1 already blocks many bots. | Below the cut-off: the K2 chains of C-15 and C-16 and its (−) chain in C-26 are recorded here only. |
| A-14 | Demand-based prices respond to demand within the sale period. | other | 0.8 | The promoter's pricing practice. | C-28 is not reported. |
| A-15 | Primary sellers who already price some seats by demand find it worth doing for more seats once resale is capped. | other | 0.55 | Their existing use of demand pricing; reputational cost of extending it. | C-29 is not reported. |
| A-16 | Season seat rights trade at a price that reflects expected resale of games. | expectations | 0.7 | Club transfers of seat rights; prices higher for seats with resale value. | C-35 is not reported. |
| A-17 | Brokers hold about 15% of season tickets mainly to resell single games, and renew fewer once resale is capped. | other | 0.7 | Club data on holders who resell most games. | C-36, C-47 and C-48 are not reported. |
| A-18 | Broker businesses are valued on expected earnings, and buyers of them expected the cap from introduction. | expectations | 0.6 | Sales of resale businesses. | C-37 is not reported. |
| A-19 | Some fans of a touring act substitute the Brackmere City stop for Dunholt. | substitutability | 0.55 | 40% of arena tours play both; 55 minutes' drive. | C-38 and C-45 are not reported; C-39 loses its (+) chain. |
| A-20 | Brokers shift some of their buying from Selvar to Brackmere City events. | mobility | 0.6 | Brokers already buy for both. | C-44 is not reported; C-39 loses its ambiguous chain and becomes an increase. |
| A-21 | The division's budget does not rise with the new work. | revenue_use | 0.8 | K4: no new appropriation. | C-41 is not reported; OC-1 applies to the payers of a larger budget instead. |
| A-23 | Some holders of high-demand tickets who cannot attend give them to exempt charity auctions rather than resell at the cap. | substitutability | 0.5 | Existing charity ticket auctions; at the cap a holder recovers little more than face, so a gift costs little more than a capped sale. At the cut-off. | C-46 is not reported. |
| A-24 | The season seats released (by brokers, about 5,700 at most, and by other holders who renew less now that resale is capped) are fewer than the waiting-list members who still buy at the club's price. | other | 0.75 | 9,000 on the waiting list; brokers hold about 15% of 38,000 season tickets; the club's price is below what seat rights trade at. | C-48 is not reported; the club's sales may fall. |
| A-22 | Brokers bought a material share of demand-priced seats, so their withdrawal lowers demand for them. | other | 0.4 | Demand-priced seats leave little resale margin. | Below the cut-off: recorded here as the opposing chain to C-28 (CR-12, 0.8, kind 2). If it held, C-28 would be `ambiguous`. |

## 11. Report

**The policy.** From 1 September 2027, no one may resell a ticket to an event in Selvar for more than its face value plus 10%, and no platform may list or process such a resale; using or selling software to get around primary sellers' purchase limits is banned. Venues and primary sellers may still charge what they like. The law does not say whether platforms' fees count toward the cap.

**Visible consequences.** Fans who buy resale tickets to sought-after events at the cap pay less (C-1); the brokers and fans who resell them receive less (C-2).

**Invisible consequences.**
- *Fewer resale tickets.* Fewer tickets are offered for resale on compliant platforms (C-3), and brokers buy fewer in primary sales (C-7) and leave Selvar events (C-8). Buyers want more than is offered at the cap (C-4), so at least one of waiting, searching, payments outside the price, favoritism or (if fees are not capped) the platform fee rises (C-5), and fans who would have paid the market price and now fail go without (C-6).
- *Trade outside the cap.* Some resales move to informal channels (C-9), to tie-ins (C-10), to packages (C-11) and to offshore platforms (C-12 to C-14). There, buyers know less about what they buy, settle disputes without courts, and meet more fake tickets (C-32 to C-34). Bot use falls, and with it the number of primary purchases made in breach of the sellers' terms or the new ban (C-15, C-16).
- *Fees.* If fees count toward the cap, platform fees to buyers fall and the total paid falls (C-17, C-19). If they do not, buyer fees rise and seller fees fall, and the total paid may rise or fall (C-17 to C-19).
- *The primary market.* More tickets in primary sales go to fans rather than brokers (C-27). Where seats are priced by demand, their prices rise (C-28), and more seats are priced that way (C-29).
- *Assets.* Season seat rights (C-35) and broker businesses (C-37) lose value from the bill's introduction, and so do compliant platforms if fees count toward the cap (C-49). Brokers renew fewer season tickets (C-47), the club's waiting list moves faster (C-36), and the club sells as many season tickets as before (C-48).
- *Charity auctions.* Some holders give tickets to exempt charity auctions rather than resell at the cap (C-46).
- *Timing.* Before September, resales of later events are moved earlier and purchases later, so prices in that window fall (C-21 to C-23).
- *Brackmere.* More Selvar fans buy tickets for the Brackmere City stop of the same tour (C-38) and travel further (C-45); brokers buy more for Brackmere City events (C-44).
- *Costs.* Enforcement within a fixed budget displaces or slows other consumer-protection work (C-40, C-41); platforms bear compliance costs (C-42); lobbying (C-25).

**Ambiguous effects.** Queues and searching in primary sales of fixed-price events (C-26); prices on offshore and informal channels (C-30) and for resale buyers across all channels (C-31); Brackmere resale prices (C-39); the number of resales made in the months before the cap (C-24); under one reading of the fee clause, the total paid on compliant platforms (C-19) and compliant platforms' value (C-49), and, under the other, how platforms split their fees (C-18). Prices for events in low demand are not signed: the cap does not bind there, but chains through other markets could raise them, and each needs a premise the record lacks.

**Key conditions.** That the cap binds for high-demand events (A-1, p = 0.95) and is enforced by the platforms that carry most resale (A-2, p = 0.85); that offshore platforms are hard to reach (A-5, p = 0.65); that brokers buy mainly to resell above face (A-3, p = 0.75). The bot ban adds little to what primary sellers already do (A-13, p = 0.45).

**What this analysis cannot say.** How large any effect is; whether fans as a whole pay more or less for tickets to sought-after events; whether artists and teams change their face values; whether the gain to fans who get capped tickets outweighs the loss to those who do not and to resellers; safety at events (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.insiders | price_paid (resale price before fees) | decrease | short | visible | B | PC-16, CR-6, CR-8b | A-1, A-2 |
| C-2 | resellers.brokers, resellers.fans | net_price_received (units sold at the cap) | decrease | short | invisible | B | PC-16, CR-8b | A-1, A-2 |
| C-3 | resellers.brokers, resellers.fans | quantity_supplied (resale listings, compliant channels) | decrease | short | invisible | B | PC-5, CR-4, CR-7 | A-1, A-2, A-3 |
| C-4 | resale market, high-demand events | excess_demand | increase | short | invisible | B | PC-1, CR-6 | A-1, A-2 |
| C-5 | buyers.outsiders | wait_time, search_cost, side_payments, allocation_by_non_price_criteria; under U1-b also price_paid (buyer fee) | at_least_one_increase | short | invisible | B | PC-2, CR-6 | A-1, A-2 |
| C-6 | buyers.outsiders | quantity_traded (high-demand tickets obtained) | decrease | short | invisible | B | PC-3, CR-5a | A-1, A-2 |
| C-7 | resellers.brokers | quantity_demanded (primary tickets bought for resale) | decrease | short | invisible | B | CR-4, CR-7a, PC-12 | A-1, A-2, A-3 |
| C-8 | resellers.brokers | number_of_sellers (brokers active in Selvar events) | decrease | medium | invisible | B | RS-6, CR-7a | A-1, A-2, A-3 |
| C-9 | informal_sellers, resellers.brokers | informal_activity (resales above the cap) | increase | short | invisible | B | PC-6, RS-3, CR-4 | A-1, A-4 |
| C-10 | buyers.outsiders | side_payments (tie-ins) | increase | short | invisible | B | PC-6, CR-6, CR-12d | outside compliant platforms: A-1, A-4; on them: A-1, A-12 |
| C-11 | resellers.brokers, primary_sellers.dynamic | reclassification (packages) | increase | short–medium | invisible | B | RS-5, CR-4 | A-1, A-12 |
| C-12 | buyers.outsiders | cross_border_purchases (offshore platforms) | increase | short | invisible | B | RS-4, CR-4 | A-1, A-5 |
| C-13 | platforms.compliant | quantity_traded (Selvar resales) | decrease | short | invisible | B | RS-4, CR-4, CR-9 | A-1, A-2, A-5 |
| C-14 | platforms.offshore | quantity_traded (Selvar resales) | increase | short | invisible | B | RS-4, CR-4, CR-9 | A-1, A-5 |
| C-15 | bot_vendors | quantity_traded (bots used on Selvar events) | decrease | short | invisible | B | EN-7, CR-4, CR-12d | K1 chain: A-1, A-2, A-3 |
| C-16 | resellers.brokers (bot users) | legal_breach (bot purchases in breach of R1 or K2) | decrease | short | invisible | B | CR-4, LW-10, CR-12d | K1 chain: A-1, A-2, A-3 |
| C-17 | buyers.insiders (compliant platforms) | price_paid (platform buyer fee) | U1-a: decrease; U1-b: increase | short | invisible | B | CR-6, CR-5c | A-1, A-7 |
| C-18 | resellers.brokers, resellers.fans (compliant platforms) | price_paid (platform seller fee) | U1-a: ambiguous; U1-b: decrease | short | invisible | B | CR-6, CR-9 | A-1, A-7 |
| C-19 | buyers.insiders (compliant platforms) | price_paid (total per ticket) | U1-a: decrease; U1-b: ambiguous | short | visible | B | PC-16, CR-12b | A-1, A-2, A-7 |
| C-21 | resellers.brokers, resellers.fans | quantity_supplied (resales of later events, Feb–Aug 2027) | increase | short | invisible | B | RS-8, CR-10a | A-1, A-8 |
| C-22 | buyers.outsiders | quantity_demanded (resales of later events, Feb–Aug 2027) | decrease | short | invisible | B | RS-8, CR-10a | A-1, A-8 |
| C-23 | resale market, later events | price_paid (Feb–Aug 2027) | decrease | short | invisible | B | RS-8, CR-6, CR-12a | A-1, A-8 |
| C-24 | resale market, later events | quantity_traded (Feb–Aug 2027, flow) | ambiguous | short | invisible | B | RS-8, CR-12b | A-1, A-8 |
| C-25 | brokers, platforms, fan groups, primary sellers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-9 |
| C-26 | buyers.primary (fixed-price events) | wait_time, search_cost (primary queues) | ambiguous | short | invisible | B | CR-6, CR-9, CR-12b | A-1, A-3, A-10 |
| C-27 | buyers.primary (fixed-price events) | quantity_traded (primary tickets obtained by fans) | increase | short | invisible | B | CR-9, CR-5, CR-12d | A-1, A-3 |
| C-28 | primary_sellers.dynamic | price_paid (demand-based prices) | increase | short–medium | invisible | B | PC-8, CR-6, CR-9 | A-1, A-10, A-14 |
| C-29 | primary_sellers.dynamic | term_prevalence (seats at demand-based prices) | increase | medium | invisible | B | PC-8, CR-4, CR-7a | A-1, A-10, A-14, A-15 |
| C-30 | resale market, offshore and informal channels | price_paid | ambiguous | short | invisible | B | RS-10, RS-16, RS-13, CR-12b | A-1, A-4, A-5 |
| C-31 | resale buyers, all channels | price_paid | ambiguous | short | invisible | B | PC-16, RS-10, CR-12b | A-1, A-2, A-4, A-5 |
| C-32 | buyers.outsiders (informal channels) | quality_information | decrease | short | invisible | B | RS-10, CR-11b | A-4 |
| C-33 | buyers.outsiders (informal channels) | disputes_settled_outside_courts | increase | short | invisible | B | RS-10 | A-4 |
| C-34 | buyers.outsiders (informal channels) | quality_variability (fake or duplicated tickets) | increase | short | invisible | B | RS-10 | A-4 |
| C-35 | season_holders | asset_value (season seat rights) | decrease | short | invisible | B | CR-7c, CR-10c | A-1, A-16 |
| C-36 | season_waitlist | wait_time (season waiting list) | decrease | medium | invisible | B | CR-4, CR-9 | A-1, A-17 |
| C-37 | resellers.brokers (owners) | asset_value (broker businesses) | decrease | short | invisible | B | CR-7c, CR-10c | A-1, A-3, A-18 |
| C-38 | neighboring_jurisdictions (Brackmere City events) | cross_border_purchases (by Selvar residents) | increase | short–medium | invisible | B | RS-1, RS-4, CR-9 | A-1, A-19 |
| C-39 | neighboring_jurisdictions (Brackmere City events) | price_paid (resale) | ambiguous | short–medium | invisible | B | RS-16, RS-13, CR-12b | A-1, A-19, A-20 |
| C-40 | officials.enforcement | enforcement_cost (K1 and K2 cases) | increase | short | invisible | B | OC-3, CR-8c | A-21 |
| C-41 | officials.enforcement | enforcement_cost (other cases) (−), wait_time (complaints handled) (+) | at_least_one_as_stated | short | invisible | B | OC-3, CR-8a | A-21 |
| C-42 | platforms.compliant | compliance_cost (face-value checks) | increase | short | invisible | A | OC-2, CR-8c | none |
| C-44 | resellers.brokers | quantity_traded (primary tickets bought for Brackmere City events) | increase | medium | invisible | B | RS-4, CR-4, CR-7a | A-1, A-3, A-20 |
| C-45 | buyers.outsiders (fans going to Brackmere City) | travel_time | increase | short–medium | invisible | B | CR-4, CR-9 | A-1, A-19 |
| C-46 | charities | quantity_traded (exempt charity auctions of donated tickets) | increase | short | invisible | B | CR-1, CR-4, CR-5 | A-1, A-2, A-23 |
| C-47 | resellers.brokers (season tickets) | quantity_traded (season ticket renewals) | decrease | medium | invisible | B | CR-4, CR-9 | A-1, A-17 |
| C-48 | primary_sellers.fixed (football club) | quantity_traded (season tickets sold) | no_change | medium | invisible | B | CR-9, CR-12e | A-17, A-24 |
| C-49 | platforms.compliant (owners) | asset_value | U1-a: decrease; U1-b: ambiguous | short | invisible | B | CR-7c, CR-10c, CR-12b, CR-12e | A-1, A-2, A-5, A-7 |

There is no C-20 or C-43: both were removed after the core-only comparison (see the next section).
## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from patterns whose preconditions held, or held after the interpretation stated in (c) and (e). The step closest to a gap was whether fixed-price primary sellers change their face values: the rules derive no direction, because the cap removes none of their options and their reason for pricing low is their own ranking (CR-2). That is the method declining to assume a ranking, not a gap.

**(b) Unclear core rules.**
1. *CR-6, 0.8, private supplier, when the policy changes the demand that reaches it.* The clause says a private supplier that chooses not to charge rations by its own choice and its margins are signed as a group. It is written for the supplier's own market. Here the policy acts on the next market (resale), and the demand reaching the supplier's queue moves both ways (brokers out, fans in). The clause gives the group's existence, not its change against the counterfactual; C-26 needed CR-12 to get `ambiguous`. The clause could say that the group's change is signed by the chains that reach the supplier's demand.
2. *CR-6, 0.8, a free price's rise is enough, under one reading only.* Under U1-b, the platform fee is a free price and its rise satisfies the "at least one margin" conclusion (C-17). Under U1-a there is no free price on compliant platforms, and the group of non-price margins carries the pressure. The clause worked; what was unclear is how to record a margin (platform service quality) that is derived under one reading and neither established nor ruled out under the other ((d) 2).
3. *CR-12d with one chain below the cut-off.* C-15 (bot use) has two same-sign chains, one with premises at 0.75 and one at 0.45. CR-12d reports the consequence if at least one chain clears; the weaker chain's premise is listed in section 10 but not in the row. CR-12d could say whether a below-cut-off chain is listed in the consequence's assumptions or only in section 10.

**(c) Missing or wrong patterns.**
1. *RS-4 when the law reaches across the boundary.* RS-4's If clause assumes the policy applies within a boundary. K1 applies to every resale of a ticket to a Selvar event, wherever made. Applied as written, RS-4 would find nowhere to relocate to. What gives the response is the reach of enforcement, not the law (A-5). Proposed: RS-4's If should read "the policy applies, or is enforced, within a boundary", with the note that where the target is tied to a place (an event, land) only the sale can move.
2. *PC-8's Unless clause misses demand withdrawn from the uncontrolled segment.* PC-8 says demand moves to the uncontrolled segment, and its Unless clause covers sellers pushed into that segment. Here the same policy also withdraws demand from the uncontrolled segment (brokers who bought in the primary market to resell in the capped one). Applied as written, PC-8 gives an increase in the primary price with no opposing chain to check. Here the opposing chain's premise was below the cut-off (A-22), so the sign stood (C-28); for fixed-price sellers, where brokers' demand was large, the opposing chain held and the margins were `ambiguous` (C-26). Proposed: add to PC-8's Unless clause "or withdraws buyers from it (buyers who bought there to resell in the controlled segment)".
3. *PC-18, prohibited contract term: not applicable, and nothing missing.* PC-18 is for non-price terms made unenforceable; a resale price cap is a price ceiling, covered by PC-1 to PC-6 and PC-16. The test was whether PC-18 would wrongly be reached for; its If clause (`term_prohibition`) kept it out. K2 suggests a different missing pattern: *public enforcement of a private term* (a statute that adds a penalty to a term sellers already impose, R1). Its derivation is CR-1 (a risk added to an option already removed in contract), CR-4 for those who breached the private term, and a binding premise on how much the private enforcement already achieved. Candidate, seen once.
4. *PC-5 on a stock of tickets.* PC-5's default horizon (medium to long, through TS-1) assumes durable capital. Here the "capital" is a broker's stock of tickets, turned over in weeks, so the supply response was short (C-3). PC-5 could say its horizon follows the durability of the stock.
5. *PC-1 to PC-3 on a secondary market of a fixed stock.* They worked as written, with one point to note: the shortage at the cap is in the resale market only, while the stock of seats is fixed. PC-3's outsiders "go without" a ticket to this event, but the seats are still used by someone; the total attended does not fall, and no consequence says it does.

**(d) Vocabulary.**
1. *No variable for platform fees.* Fees were recorded as `price_paid` with a qualifier (buyer fee, seller fee). A variable for an intermediary's charge (`intermediary_fee`) would keep it apart from the price of the good.
2. *A per-reading sign where one reading establishes nothing.* The sign list has `no_change` for a reading where the derivation establishes no change, but nothing for a reading where it establishes neither a change nor no change. A consequence derived under U1-a only (platform service quality under PC-4) could not be recorded. Proposed: allow `not_signed` per reading, as distinct from `no_change` and `ambiguous`.
3. *Those protected by displaced enforcement.* OC-3's fixed-budget branch says the cost falls on those whom the displaced enforcement protected, but no variable records their loss; C-41 records only the division's side.

**(e) Test of 0.8.**
- *PC-1, PC-2, PC-3 on a secondary market only.* Worked as written (C-3 to C-6), with the note in (c) 5.
- *PC-16 (0.6), a ceiling as a transfer.* Worked as written: both sides recorded (C-1, C-2), including fans who resell.
- *PC-18 (0.7).* Not applicable, correctly kept out by its If clause; nothing was lost by not applying it ((c) 3).
- *RS-4 (0.7 widening).* Needed interpretation: the boundary that matters is enforcement's reach, not the law's ((c) 1).
- *RS-10 (0.5).* Worked as written (C-32 to C-34).
- *CR-6 0.8, private supplier not bound by a rule.* Worked for the existence of rationing by fixed-price primary sellers; needed interpretation (CR-12) for its change against the counterfactual ((b) 1).
- *CR-6 0.8, a free price's rise is enough.* Worked as written under U1-b (C-17); exposed the per-reading recording problem in (d) 2.
- *CR-12 0.8, three kinds of opposing chain.* Worked as written, all three kinds used: kind 1, artists keeping face values low because the law names above-face resale unfair (Tier C note); kind 2 with p at or above 0.5 (C-26, `ambiguous`) and below 0.5 (C-28 reported as an increase, the chain recorded with A-22); kind 3 (C-30, C-31, C-39).
- *RS-8 0.8 Unless, opposing timing chains.* Worked as written: quantity in the window `ambiguous` (C-24), price in the window signed because both chains push it the same way (C-23).
- *RS-16 Unless (supply added to the substitute's market).* Worked as written for offshore channels (C-30).
- *OC-3 0.8, right baseline.* Worked as written, but gave no separate consequence: the old fraud enforcement moves both ways, and the fixed budget makes the total no change.
- *Candidate patterns from 06_gaps.md, 6.2e, needed here (second use).* "A claim payable inside a boundary draws items from outside" (WE-027) and "Circular trade under a payment for crossing a boundary" (WE-030) were not needed. "Complaint-only enforcement" (WE-029) was close: K4's buyer remedy works only if buyers sue, and the derivation (CR-4, expected cost of breach differing by counterparty) was used for A-11, which fell below the cut-off. That is a partial second use, recorded here for the catalog to decide.
