# WE-053 loop notes (blind run)

Inputs read: section 1 (copied to policy.txt) and the assumption table only. The run took 3 rounds, 26 node visits (10, 11, 5), 22 loop questions, no off-list names. Seed assumptions a1, a2, a10, a18, a22 are table items A-1, A-2, A-10, A-18, A-22; a27 is judged (see below). Of the 22 loop questions, 20 matched a table statement exactly (taken at the table's p); 2 were judged (below). Branch: loop-we053_corvany.

## Seed (policy's own facts, CR-1)
- Exchanges: `e_abroad` (buyers.abroad, the covered controllers with an establishment that host abroad / sellers.foreign, the Esterland regions), `e_foreign` (buyers.foreign, the ~400 foreign online services / sellers.foreign), `e_backup` (buyers.backup, the ~600 local hosts that keep backups abroad / sellers.foreign), `e_local` (buyers.current, controllers already hosting in Corvany / sellers.current, local colocation and own data centers). Split because the policy treats them differently: enforcement differs for foreign services (K4 blocking never used), and backups are covered only under U1-b.
- `banned` K1 on e_abroad (A-1 binds, A-2 enforced against controllers with an establishment) and on e_foreign (A-1 only, see limits). `banned` k1_b on e_backup, listed under U1-b in `unclear` (A-2).
- `charges` K3: 40,000 crowns per facility per year, `basis: operating`, payer seller, receiver general_fund (non_tax_receipts), premise A-18 (small facilities for which it exceeds the margin).
- `thresholds` K1 at 50,000: buyers.near_threshold, measured by `membership` (customers/residents' records), premise A-10.
- `compliance` K2 (officer, annual statement) for the four controller classes; `enforcers` K4 officials.enforcement; `funded` K4 taxpayers (A-22, general budget, no named tax); `announced` K1 (a27, judged 0.95: enacted 1 July 2027, applies from 1 January 2029).
- Not seeded: no held price, grant, cap, expiry ("It has no expiry"), qualifies, fixed, incidence, terms.

## Round 1 (10 nodes)
- buyers.abroad: alternatives of hosting locally in colocation / own centers (A-23), in a provider's local region (A-4, the "may comply by operating servers in Corvany" sentence), paying more (price_paid, A-5 and A-23), latency (quality_per_unit, A-14), fewer services (variety, inverse, A-15), deleting records below the line (membership, inverse, A-8), splitting between controllers (reclassification, A-8 and A-9). Links: compliance_cost to consultants' demand (input, judged premise from the migration row); price_paid to online services' supply (cost, A-19).
- buyers.backup: backups moved into Corvany, only under U1-b (judged premise).
- buyers.foreign: withdraw or cap sign-ups (membership, inverse, A-11); local region (A-4); `outside` margin informal_activity on e_foreign (A-12); link to domestic substitutes (A-20).
- buyers.near_threshold: splitting between controllers (A-8, A-9); stake in K1 (A-13).
- general_fund: receipts paid into fund_balance (the "fees go to the general budget" sentence). officials.enforcement: spending paid from the fund (A-22, the 6 million appropriation). Both flows are in the text, so fund_balance comes out ambiguous.
- sellers.current: supply_price link demand to price, short (A-16); price yields investment, capital stock, supply (A-3); fewer sellers lowers supply (A-18); price yields asset value (A-16); same_act price to buyers.current's price_paid; stake (A-13).
- sellers.foreign: local region as alternative (A-4); yield link from lost trades to return_on_capital (A-25); stake (A-6, A-13).
- buyers.current, taxpayers: empty (nothing reaches them yet / reach no one else).

## Round 2 (11 nodes)
Empty: buyers.abroad#2, buyers.foreign#2, buyers.near_threshold#2, general_fund#2, input_suppliers, sellers.foreign#2, sellers.online. Added: buyers.current#2 moves to a provider's local region once its price rose (A-26); sellers.current#2 complement link to employment (A-24, p 0.2, so not reported); sellers.prospective: investment to capital_stock_economy and to importers (A-21), long-run supply_price (A-17), substitute link to sellers.current demand (A-26); sellers.substitutes: input link to local demand (A-20).

## Round 3 (5 nodes)
buyers.current#3, economy, importers, sellers.current#3, sellers.prospective#2: empty. Several totals are ambiguous (sellers.current price, demand, supply, asset value; sellers.prospective price and demand; buyers.current price_paid; general_fund fund_balance). No premise in section 1 or the table says which direction outweighs, so I proposed no dominance.

## Answers
From the table (exact statement, table p): A-3, A-4, A-5, A-6, A-8, A-9, A-11, A-12, A-13, A-14, A-15, A-16, A-17, A-18, A-19, A-20, A-21, A-23, A-24, A-25, A-26 (and A-1, A-2, A-10, A-22 in the seed). Judged: "Covered controllers pay consultants to migrate their systems." 0.9 (the migration row names consultants); "Some controllers that keep backups abroad would store them in Corvany if required." 0.85 (the U1-b reading forces it, 600 controllers keep backups abroad); a27 "Actors expect the requirement to apply from 1 January 2029, as enacted." 0.95 (enacted 18 months ahead). Not used: A-7 (backups encrypted), A-10 only in the seed, A-22 only in the seed; A-7 has no home (see below).

## What the format could not hold
- Enforcement strength on one ban: A-12 (weak against foreign services) cannot gate the ban without removing it, so e_foreign is banned on A-1 alone and the weakness appears as an `outside` margin. The foreign ban therefore reads as fully binding (quantity_traded falls) with informal activity rising beside it.
- A-7 (backups abroad are encrypted) and the U1-a exempt alternative: under U1-a nothing happens to backups, and an alternative needs a chooser made worse, which exists only under U1-b. The exemption shows as "none" for U1-a, not as an option.
- `reading` on a banned entry already listed under `unclear.components` drops it from every run (the engine filters facts with a reading out of the base run and the component out of the reading run); the component listing alone is enough. I removed `reading` from k1_b after finding that.
- Threshold direction: `thresholds` covers those below the line growing; controllers just above (380 in 50,001 to 60,000) deleting records appear only as an alternative of buyers.abroad.
- Fines up to 4% of turnover and the block order: no field attaches a risk to a banned trade; they are not recorded.
- A fee per facility cannot be tied to the number of facilities (own centers, new regions, nine colocation sites), so the fund balance (fees against the 6 million) is ambiguous rather than comparable by arithmetic.
- The A-19 cost link needs an "online services" class that the exchanges do not name (sellers.online), and latency (A-14) and fewer services (A-15) are mapped onto quality_per_unit and variety as alternatives of the buyer, which is a stretch.
- Loops (price, investment, capital stock, supply) are cut by CR-12e: I left out the supply link that would close the loop, so the price effect of added capacity does not feed back.
