# WE-028 / Analysis: Kallmark Ridge Cod Fishery Act (catch cap with individual transferable quota shares)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Kallmark Ridge Cod Fishery Act.** Kallmark is a coastal country of about 3 million people. Its boats land about 48,000 tonnes of ridge cod a year (average of 2022 to 2024). About 70% is frozen or filleted by four processing plants (two at Brennhavn, one at Haldrun, one at Tornhavn) and exported to the North Basin whitefish market, of which Kallmark's ridge cod is about 7%, alongside close substitutes (saithe, haddock from other countries). About 30% is sold fresh in Kallmark to fish shops and restaurants. The fishery is open: any owner of a registered vessel may fish ridge cod; 290 vessels did so in 2024 (38 trawlers over 24 m landing about 60% of the catch, and 252 coastal boats). The nearby saithe and ling fisheries are open and not covered. About 1,700 crew are paid by "lay": under the Fishermen's Share Agreement, a standard private contract used on about 80% of vessels, the crew together receive 45% of each trip's revenue after trip expenses (fuel, ice, bait, landing fees).

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Kallmark vessels landing ridge cod. Outside: the open saithe and ling fisheries (not covered); foreign fleets supplying the North Basin market; recreational fishing (exempt up to 10 fish a person a day, not for sale). | "Nearby fisheries for saithe and ling are open as well and are not covered by the Act." |
| Announced / enacted / effective / expires | Announced 3 February 2026 (bill introduced with its allocation formula; passage widely expected); enacted 14 October 2026; effective 1 January 2028; TAC fixed at 40,000 t for 2028 to 2032, set yearly by the Ministry from 2033; no expiry. | "introduced by the government on 3 February 2026, with its allocation formula published ... passed on 14 October 2026 and takes effect on 1 January 2028." |
| Enforcement (who, penalties, resources) | Fisheries Directorate: landing only at 13 designated sites with dockside weighing (fee 15 marks/t paid by the owner); observers on 10% of trips by vessels over 24 m, none on coastal boats; discarding of legal-size ridge cod prohibited; forfeiture of the catch, a fine of three times its value, share suspension after a third offense; budget raised by 18 million marks a year from the general budget. | K4. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Catch cap | `quota` | Landings of ridge cod by Kallmark vessels | Vessel owners | TAC 40,000 t a year for 2028 to 2032; from 2033 set yearly by the Ministry "having regard to scientific advice". | Recreational fishing up to 10 fish a person a day, not for sale. |
| K2 Quota shares | `rights_allocation` (allocation of K1) | Shares of the annual catch | Vessel owners | One million shares, given free on 1 January 2028 to the registered owner of each vessel on 31 December 2027, in proportion to the vessel's recorded ridge cod landings in 2025 to 2027. Permanent and saleable; annual tonnage may be leased. Transfers registered with the Directorate, fee 1% of the price. Only owners of at least one registered vessel may hold shares. Holding limit 8% with affiliates. A vessel that lands more than its owner's tonnage must lease the difference within 30 days, or the excess is forfeited and fined. | None |
| K3 Crew settlements | Rule on a private contract term (`contract`: the Fishermen's Share Agreement) | Deductions from trip revenue before the crew share | Vessel owners | "The cost of acquiring quota shall not be deducted as a trip expense in crew settlements." | None |
| K4 Monitoring and enforcement | Enforcement | K1, K2 | Fisheries Directorate | As in the enforcement row above. | None |

Existing rules (in force in the counterfactual too): R1 vessel registration (open to any seaworthy vessel, 600 marks a year); R2 minimum landing size 35 cm (smaller fish returned to the sea).

Counterfactual: Kallmark with an open ridge cod fishery, no cap, no shares, the same R1 and R2, and the Share Agreement as it is. Landings stay near 48,000 t a year (A-1).

Unclear provisions:
- **U1** (from the record): whether "the cost of acquiring quota" in K3 covers leasing a year's tonnage. U1-a: only purchases are covered, so lease payments may be deducted before the crew share. U1-b: leases are covered too, so the owner pays them from the owner's side.
- Noted here, not analyzed (no reported consequence depends on them; marked `unclear`, not guessed): whether a vessel whose 2025 to 2027 history would give its owner more than 8% of shares is allocated the excess; whether a lease of annual tonnage is a "transfer" that pays the 1% fee; whether buying a vessel for its catch history before 2028 is "acquiring quota" under K3.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Catch cap | triangular (prohibits sales of ridge cod landed beyond the cap) | Yes from 2028 (A-1), where enforced (A-2) | 1 (landing beyond the owner's tonnage removed, dated 1 January 2028); 3 where enforcement is imperfect (a risk attached to unrecorded landing or discarding, A-10, A-11) | CR-4, CR-5a, CR-6, CR-9, CR-10a |
| K2 Quota shares | binary (the state gives a created right) and triangular (only vessel owners may hold; 8% limit) | Yes: shares have a price whenever K1 binds (A-1) | 2 and 4 for recipients (a saleable right is added and means transferred, dated 1 January 2028, expected from 3 February 2026); 1 for non-vessel-owners (holding removed) and for owners above 8%; 3 for everyone else who wants to fish ridge cod (the option to fish now carries the price of a share or lease); 3 on the option "land ridge cod in 2026 and 2027" (it now also brings a share of a future right) | CR-1, CR-4, CR-5, CR-6, CR-7a, CR-7c, CR-8b, CR-10a, CR-10c |
| K3 Crew settlements | triangular (regulates a term of a private contract) | Binding where owners buy shares (A-6, A-23); for leases, per reading U1 | 1 for owners (deducting purchase costs before the crew share removed); under U1-b also deducting leases. Counterfactual law: no quota exists, so no such deduction exists either; K3 limits a deduction the Act itself creates. | CR-1, CR-4, CR-5c, CR-7b, CR-9 (contract) |
| K4 Monitoring and enforcement | binary (budget spending; per-tonne fee) | Yes (A-22) | 3 (landing only at 13 sites, 15 marks/t fee, observers, penalties) for owners; 4 (18 million marks a year) from the general budget to the Directorate | CR-1, CR-4 (x: comply, y: violate), CR-8b, CR-8c, CR-8e |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| vessel_owners.recipients | Owners of vessels with 2025 to 2027 ridge cod history on 31 December 2027 | Op 2 and 4: shares; op 1: landing above holding; op 3: monitoring fee, landing sites, transfer fee; op 1 under K3 |
| vessel_owners.low_cost | Owners whose cost per tonne is low (A-6) | Op 2: can buy or lease tonnage from others; expand |
| vessel_owners.high_cost | Owners whose cost per tonne is high (A-6) | Op 2: can sell or lease their tonnage instead of fishing it |
| vessel_owners.leaving_holders | Recipients who stop fishing but keep shares (A-24) | Op 1: must keep a registered vessel to hold shares |
| vessel_owners.largest_firms | Firms near the 8% limit (A-13) | Op 1: holding above 8% removed |
| vessel_buyers.2026_2027 | Buyers of vessels before 31 December 2027 | Through CR-7c: pay for history (A-5) |
| sellers.prospective | Would-be entrants to ridge cod fishing (A-N1) | Op 3: entry now requires buying or leasing tonnage; op 1 without a registered vessel |
| crew.ridge_cod | Crew paid by lay | Through CR-9 (contract: Share Agreement; labor input_to fishing); op 3 via K3 (protects their share from purchase costs; per U1 for leases) |
| processors | Four plants | Through CR-9 (ridge cod input_to processing); op 1 (cannot hold shares without a vessel) |
| workers.processing_plants | Plant workers | Through CR-9 (labor input_to processing) |
| buyers.fresh | Fish shops, restaurants and their customers in Kallmark | Through CR-9 (fewer fish landed) |
| recreational_fishers | Households who fish under the exemption | Through CR-9 and CR-4: own catch is a substitute for bought fresh fish (A-N2) |
| sellers.substitutes | Kallmark saithe and ling fishers | Through CR-9 (substitute in demand; shared_facility in the fishing grounds) |
| buyers.foreign | North Basin whitefish buyers | Through CR-9 (fewer exports; A-17) |
| sellers.foreign | Foreign saithe and haddock suppliers | Through CR-9 (substitute) |
| input_suppliers | Fuel, ice, bait sellers; landing services at the ten small harbors and three processing ports | Through CR-9 (input_to fishing) |
| vessel_market | Buyers and sellers of second-hand fishing vessels, at home and abroad | Through CR-9 (surplus vessels; vessels as a condition of holding) |
| intermediaries | Quota brokers | Through CR-9: a new market in shares and leases |
| officials.fisheries_directorate | Administers K2, enforces K1 and K4 | Op 4: +18 million marks; receives fees, fines, forfeitures |
| monitors | Dockside monitors and observers | Through CR-8b and CR-9 (paid from the fee and the budget) |
| taxpayers | Fund the Directorate's extra budget, with recipients of other spending | Op 4 (through the general budget) |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1, K2 and K4 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | vessel_owners (ridge cod fleet) | quantity_traded (ridge cod landed in the legal market) | decrease | medium (2028-2032) | CR-1 op 1, CR-6, CR-4b | A-1, A-2 |
| C-2 | vessel_owners.recipients | asset_value (quota shares) | increase | medium (from 1 January 2028) | CR-1 op 2 and 4, CR-6, CR-7c, CR-10c | A-1, A-2, A-3 |
| C-3 | vessel_owners.recipients | asset_value (vessels with 2025-2027 ridge cod history) | increase | short (from 3 February 2026) | CR-7c (claims before creation), CR-10a, CR-10c | A-1, A-3, A-5 |
| C-4 | vessel_owners, lessees | right_lease_price (annual ridge cod tonnage) | increase | medium | CR-6 (fixed quantity of a good priced in a wider market), CR-5c | A-1, A-2 |
| C-5 | officials.fisheries_directorate | enforcement_cost | increase | medium | CR-1 op 4, CR-8c | A-22 |
| C-6 | taxpayers, recipients of other public spending | resources_available_other_uses | at_least_one_decrease | medium | CR-8b, CR-8a | A-22 |
| C-7 | vessel_owners (ridge cod fleet) | compliance_cost (monitoring fee, designated sites, registration of transfers) | increase | medium | CR-1 op 3, CR-8c | none |

## 5. Responses

CR-4 for every pair of options each class has; CR-6 for the fixed quantity; CR-10a for timing; CR-5 for the exchanges that now take place or no longer do.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-8 | vessel_owners | quantity_traded (ridge cod landed) | increase | short (2026-2027) | CR-10a, CR-4 (x: stay idle or fish other species, y: land ridge cod for history), CR-7c | A-4 |
| C-9 | vessel_owners | capital_stock_target (vessels and days at sea in ridge cod) | increase | short (2026-2027) | CR-10a, CR-4 | A-4 |
| C-10 | vessel_owners (racing for history) | resources_available_other_uses | decrease | short (2026-2027) | CR-7c (part of the value used up in the competition), CR-8c, CR-3c | A-4 |
| C-11 | vessel_owners | number_of_sellers (vessels fishing ridge cod) | decrease | medium | CR-7a, CR-4 (x: fish own tonnage, y: sell or lease it), CR-5 | A-1, A-6 |
| C-12 | vessel_owners.low_cost | quantity_supplied (ridge cod per vessel still fishing) | increase | medium | CR-7a, CR-5 | A-1, A-6 |
| C-13 | vessel_owners.recipients (sellers and lessors of tonnage) | resources_available_other_uses | increase | medium | CR-8b, CR-7c | A-1, A-23 |
| C-14 | vessel_owners.low_cost (buyers and lessees of tonnage) | resources_available_other_uses | decrease | medium | CR-8b, CR-3c | A-1, A-6 |
| C-15 | sellers.prospective | entry_rate | decrease | medium | CR-1 op 1 and op 3, CR-4 (x: enter, y: stay out) | A-N1, A-1, A-2 |
| C-16 | vessel_owners | discards (legal-size ridge cod) | increase | medium | CR-6 (illegal margin), CR-4 (x: land a small fish against tonnage, y: discard it and land a larger one) | A-1, A-9, A-10 |
| C-17 | vessel_owners | quality_per_unit (average size of ridge cod landed) | increase | medium | CR-4 (same chain as C-16) | A-1, A-9, A-10 |
| C-18 | vessel_owners (landing at small harbors) | informal_activity (unrecorded ridge cod landings) | increase | medium | CR-6, CR-4 (x: land within tonnage or lease, y: land unrecorded) | A-1, A-11 |
| C-19 | vessel_owners.leaving_holders | units_held_vacant (registered vessels kept idle to hold shares) | increase | medium | CR-1 op 1, CR-4 (x: sell vessel and shares, y: keep a minimal vessel and the shares) | A-24 |
| C-20 | processors | quantity_traded (registered vessels bought by processors to hold shares) | increase | medium | CR-1 op 1, CR-4 (x: buy fish at the dock, y: buy a vessel and hold shares) | A-14, A-1 |
| C-21 | vessel_owners.recipients | lobbying_effort (allocation formula; TAC from 2033) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-10a, CR-8c | A-15, A-3 |
| C-22 | crew.ridge_cod, vessel_owners | lobbying_effort (Directorate's ruling on U1) | increase | short; medium | CR-4 (x: accept either ruling, y: press for one), CR-8c | A-15 |
| C-23 | vessel_owners.largest_firms | lobbying_effort (to raise the 8% limit) | increase | medium | CR-1 op 1, CR-4 (x: accept, y: lobby), CR-8c | A-13, A-15 |
| C-24 | vessel_owners (acquiring tonnage) | reclassification (acquisitions structured as leases) | U1-a: increase; U1-b: no_change | medium | CR-4 (x: buy shares, not deductible; y: lease long-term, deductible under U1-a) | A-6 |
| C-25 | recreational_fishers | home_production (ridge cod caught under the exemption) | increase | medium | CR-9, CR-4 (x: buy fresh ridge cod, y: catch it), CR-6 (open margin) | A-N2, A-16, A-1 |
| C-26 | officials.fisheries_directorate | non_tax_receipts (transfer fees; fines and forfeitures) | increase | medium | CR-1 op 3, CR-8b, CR-8e | A-23; A-2 |
| C-27 | vessel_owners (detected violators) | resources_available_other_uses | decrease | medium | CR-8e, CR-8b | A-2, A-1 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Pruned at depth 3 as diffuse: the currency link (fewer ridge cod exports leave foreigners with fewer marks for Kallmark's other exports; relation `currency`), coastal towns' shops via proximity, and the customers of restaurants beyond the fresh fish price.

Shared facility (Tier C, not in the list): vessels displaced into the open saithe and ling grounds share those grounds with incumbents (relation `shared_facility`), so the catch available to each incumbent vessel falls; and the race of 2026-2027 draws more from the shared ridge cod stock. No variable records catch per unit of effort or stock size, and stock effects are environmental and out of scope.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-28 | buyers.fresh | price_paid (fresh ridge cod) | increase | medium | CR-9, CR-6, CR-7a | ridge cod landed same_market_other_segment of fresh and processed ridge cod (close); imported and frozen whitefish substitute (partial) | A-1, A-2, A-16 |
| C-29 | buyers.fresh | price_paid (fresh ridge cod) | decrease | short (2026-2027) | CR-9, CR-6 | as above | A-4, A-16 |
| C-30 | buyers.fresh | quantity_traded (fresh ridge cod) | decrease | medium | CR-4c | as above | A-1, A-2, A-16 |
| C-31 | buyers.fresh | quantity_substitute (saithe and ling bought fresh) | increase | medium | CR-4 (x: ridge cod, y: saithe or ling) | saithe and ling substitute for fresh ridge cod (partial) | A-1, A-25 |
| C-32 | sellers.substitutes, buyers.fresh | price_substitute (saithe and ling in Kallmark) | ambiguous | short; medium | CR-12b | substitute (demand); vessels and crew alternative_uses (supply) | A-4, A-7, A-25, A-1 |
| C-33 | sellers.substitutes | quantity_substitute (saithe and ling landed by Kallmark vessels) | decrease | short (2026-2027) | CR-9, CR-7a, CR-10a | vessels move between fisheries (alternative uses) | A-4, A-7 |
| C-34 | sellers.substitutes | quantity_substitute (saithe and ling landed by Kallmark vessels) | increase | medium | CR-7a, CR-9 | as above; substitute in demand | A-1, A-6, A-7 |
| C-35 | processors | price_paid (ridge cod bought at the dock) | increase | medium | CR-7a, CR-6, CR-9 | ridge cod input_to processing; fresh segment same_market_other_segment | A-1, A-16, A-18 |
| C-36 | processors | quantity_traded (ridge cod processed) | decrease | medium | CR-9, LW-10 | ridge cod input_to processing (close) | A-1, A-2, A-19 |
| C-37 | processors | quantity_traded (ridge cod processed) | increase | short (2026-2027) | CR-9, LW-10 | as above | A-4, A-18 |
| C-38 | processors | return_on_capital | decrease | medium | CR-7b, CR-9 | as above; output priced in the North Basin market | A-1, A-17, A-18, A-19 |
| C-39 | processors | asset_value (processing plants) | decrease | short (from 3 February 2026) | CR-7c, CR-10c | as above | A-1, A-18, A-19 |
| C-40 | workers.processing_plants | employment | decrease | medium | CR-9, LW-10 | plant labor input_to processing | A-1, A-19 |
| C-41 | buyers.foreign | quantity_traded (Kallmark ridge cod exports) | decrease | medium | CR-9 | processed ridge cod sold to the North Basin | A-1, A-2 |
| C-42 | buyers.foreign | price_paid (North Basin whitefish) | increase | medium | CR-9, CR-6 | ridge cod substitute for saithe and haddock (close) | A-1, A-17 |
| C-43 | sellers.foreign | quantity_traded (saithe and haddock sold in the North Basin) | increase | medium | CR-9, CR-4 | substitute (close) | A-1, A-17 |
| C-44 | crew.ridge_cod | employment (ridge cod fishing) | decrease | medium | CR-9, LW-10, CR-7a | crew labor input_to fishing; contract (Share Agreement) | A-1, A-6 |
| C-45 | crew.ridge_cod | employment, hours_worked (ridge cod fishing) | at_least_one_increase | short (2026-2027) | CR-9, LW-10 | as above | A-4 |
| C-46 | crew.ridge_cod (displaced) | earnings | decrease | medium | CR-7b, CR-3a | crew labor; alternative_uses | A-1, A-6, A-8 |
| C-47 | crew.ridge_cod (still fishing) | earnings (per crew member) | ambiguous | medium (first season after tonnage concentrates) | CR-12b | contract (Share Agreement) | A-6, A-26, A-N3 |
| C-48 | crew.ridge_cod | term_prevalence (agreements with a crew share below 45%) | increase | medium (after renegotiation) | CR-5c, CR-7a, CR-7b | contract (Share Agreement) | A-26, A-6, A-8 |
| C-49 | input_suppliers (fuel, ice, bait) | quantity_traded (to ridge cod vessels) | increase | short (2026-2027) | CR-9, LW-10 | fuel, ice, bait input_to fishing (close) | A-4 |
| C-50 | input_suppliers (fuel, ice, bait) | quantity_traded (to ridge cod vessels) | decrease | medium | CR-9, LW-10, CR-7a | as above | A-1, A-6 |
| C-51 | input_suppliers (landing services at the ten small harbors) | quantity_traded (ridge cod landed at small harbors) | decrease | medium | CR-9, CR-7a | landing services input_to fishing | A-1, A-20 |
| C-52 | input_suppliers (landing services at the three processing ports) | quantity_traded (ridge cod landed at processing ports) | ambiguous | medium | CR-12b | as above | A-1, A-20 |
| C-53 | vessel_market | asset_value (fishing vessels without ridge cod history) | ambiguous | medium | CR-12b | vessels alternative_uses; vessels as a condition of holding shares | A-14, A-21, A-24 |
| C-54 | vessel_market | quantity_traded (vessels sold abroad) | increase | medium | CR-7a, CR-4 (x: keep idle, y: sell abroad) | across_border vessel market | A-7, A-21, A-1, A-6 |
| C-55 | vessel_buyers.2026_2027 | resources_available_other_uses | decrease | short (2026-2027) | CR-8b, CR-7c | vessel market | A-5, A-3 |
| C-56 | intermediaries (quota brokers) | employment (brokering shares and leases) | increase | medium | CR-9, LW-10 | brokerage input_to share trading | A-6, A-23 |
| C-57 | monitors | employment (dockside monitoring and observers) | increase | medium | CR-8b, CR-9 | monitoring input_to enforcement | A-22 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| vessel_owners, quantity_traded (ridge cod landed) | short: race for history (C-8) | medium: binding cap (C-1) | Different horizons, not combined (CR-12g); unrecorded landings (C-18) cannot lift legal landings back, since they are outside the legal market (CR-12e: a response cannot reverse its cause) | increase (short); decrease (medium) |
| buyers.fresh, price_paid | medium: fewer fish, partial substitutes (C-28) | short: more fish landed in the race (C-29) | Different horizons | decrease (short); increase (medium) |
| price_substitute (saithe and ling), short | vessels leave saithe and ling to build history (supply down, A-4, A-7) | fresh buyers turn to cheaper ridge cod (demand down, A-16) | None | ambiguous (C-32) |
| price_substitute (saithe and ling), medium | fresh buyers turn from dearer ridge cod (A-25) | displaced vessels and crew enter saithe and ling (A-7) | None | ambiguous (C-32) |
| quantity_substitute (saithe and ling landed) | medium: both chains (more demand, more supply) | short: both chains (less supply, less demand) | Same direction within each horizon | decrease (short, C-33); increase (medium, C-34) |
| processors, quantity_traded | short (C-37) | medium (C-36) | Different horizons | increase (short); decrease (medium) |
| processors, price_paid at the dock, medium | fresh price up, landings allocated between segments until yields equal (C-35) | none derived | Not needed | increase (C-35) |
| crew, employment | short (C-45) | medium (C-44) | Different horizons | at_least_one_increase (short); decrease (medium) |
| crew still fishing, earnings per crew member, medium | more tonnes per vessel and lower trip expenses per tonne on low-cost vessels (A-6), lay unchanged for a season (A-26); higher fresh price and larger fish (C-28, C-17) | monitoring fee deducted as a landing fee (A-N3); under U1-a, lease payments deducted before the crew share | None | ambiguous under both readings (C-47); U1-b removes one negative chain but not the fee |
| input_suppliers (fuel, ice, bait), quantity_traded | short (C-49) | medium (C-50) | Different horizons | increase (short); decrease (medium) |
| landing services at processing ports, quantity_traded, medium | consolidation toward larger vessels that land at the ports (A-20) | fewer tonnes landed in total (C-1) | None | ambiguous (C-52) |
| vessel_market, asset_value (vessels without history), medium | demand for minimal registered vessels as a condition of holding (A-14, A-24) | surplus vessels not absorbed at unchanged prices (A-21) | None | ambiguous (C-53) |
| vessel_owners, resources_available_other_uses | sellers and lessors (C-13), medium | racers (C-10), short; buyers and lessees (C-14), medium; violators (C-27) | Different subclasses and horizons, not netted | as listed |
| vessel_owners.recipients, asset_value (shares) | creation of a priced right (C-2) | none against the counterfactual: the 8% limit, the 1% fee, K3 and evasion reduce the value only relative to other versions of the policy | Not needed | increase (C-2) |

CR-12f: no pair of provisions cancels by construction.

## 8. Time structure

- **Announcement window (3 February 2026 to 31 December 2027).** The formula was published with the bill and passage was widely expected (A-4), so the right to future shares attached to vessels at once (CR-7 clarification "claims before creation", CR-10a). History for 2025 was already fixed at announcement: that part of the value is a pure windfall to 2025 owners, captured on 3 February 2026 as passage became likely and fully on 14 October 2026 (C-3). History for 2026 and 2027 is competed for: owners reactivate idle vessels and use spare days (C-8, C-9), part of the value is used up in the race (C-10), and fresh fish is cheaper (C-29), plants busier (C-37), suppliers sell more (C-49), and saithe and ling landings fall (C-33). Vessels with history are sold at prices that include it (C-3, C-55; A-5). Plant values fall from announcement (C-39). These effects exist only in the window (`persistence: n/a` if the Act were later repealed).
- **2028 to 2032 (fixed TAC).** The cap binds (C-1); shares and leases have prices (C-2, C-4). Tonnage moves to low-cost vessels through sales and leases (C-11, C-12); the move is gradual, since vessels and crew are stocks that change through flows (CR-10b). The lay stays at 45% for at least a season (A-26), so remaining crew may gain at first; renegotiation then moves terms (C-48).
- **From 2033.** The TAC is set by the Ministry each year. No sign is given against the counterfactual for landings, prices or share values after 2032: they depend on future TAC decisions and on the stock (biological premises, out of scope). Recipients lobby around these decisions (C-21). Consolidation and the exit of vessels and crew persist after 2032 whatever the TAC (CR-10b), because selling a vessel abroad or leaving the trade is costly to undo.
- **Persistence.** This is not a repeal; persistence is recorded only for effects of the window (n/a, above) and for consolidation (persists, CR-10b).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-5 | officials.fisheries_directorate | enforcement_cost | increase | 18 million marks a year of staff and equipment that would have served other public or private ends | CR-1 op 4, CR-8c |
| C-6 | taxpayers, recipients of other public spending | resources_available_other_uses | at_least_one_decrease | Other spending or lower taxes forgone to fund the Directorate | CR-8b, CR-8a |
| C-7 | vessel_owners | compliance_cost | increase | Monitoring fees, travel to designated sites, registration | CR-1 op 3, CR-8c |
| C-10 | vessel_owners (racing) | resources_available_other_uses | decrease | Fuel, crew time and vessel wear spent landing fish for history | CR-7c, CR-8c, CR-3c |
| C-14 | vessel_owners.low_cost | resources_available_other_uses | decrease | Sums paid for shares and leases | CR-8b, CR-3c |
| C-15 | sellers.prospective | entry_rate | decrease | Entries that would have taken place in an open fishery | CR-4, CR-5a |
| C-16 | vessel_owners | discards | increase | Legal-size fish caught and thrown away instead of sold | CR-4, CR-8a |
| C-21 | vessel_owners.recipients | lobbying_effort | increase | Time and money spent seeking favorable TACs and rules | CR-8c |
| C-22 | crew.ridge_cod, vessel_owners | lobbying_effort | increase | Time and money spent on the U1 ruling | CR-8c |
| C-23 | vessel_owners.largest_firms | lobbying_effort | increase | Time and money spent on the 8% limit | CR-8c |
| C-30 | buyers.fresh | quantity_traded (fresh ridge cod) | decrease | Fresh ridge cod meals and sales no longer made (CR-5a: both sides lose an expected gain) | CR-4c, CR-5a |
| C-41 | buyers.foreign | quantity_traded (Kallmark exports) | decrease | Exports no longer made | CR-5a |
| C-55 | vessel_buyers.2026_2027 | resources_available_other_uses | decrease | Sums paid to sellers for catch history | CR-8b |

CR-8 symmetry: the share value (C-2, C-3) is matched by what buyers of vessels and shares pay (C-14, C-55), by the entry option removed from prospective entrants (C-15) and by the higher prices paid by fresh buyers and plants (C-28, C-35); the budget (C-5) by taxpayers (C-6) and the monitors who receive it (C-57); fees and fines (C-26) by owners (C-7, C-27); the race (C-10) and lobbying (C-21 to C-23) are used up (CR-8c). Where the share value comes from the end of yields being competed away in an open fishery, CR-8b names no single payer (Gaps found, GAP-028-C2).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Without the Act, landings would stay well above 40,000 tonnes a year, so the cap binds from 2028. | binding | 0.9 | Landings of 48,000 t on average in 2022 to 2024; fleet capacity. | Most medium-horizon consequences fail: C-1, C-2, C-4, C-11 to C-15, C-16 to C-18, C-20, C-25, C-27, C-28, C-30, C-31, C-34 to C-36, C-38 to C-44, C-46, C-50 to C-52, C-54. |
| A-2 | Landings are recorded and overages enforced at the designated sites. | enforcement | 0.8 | Weighing at every site; forfeiture and triple fines; share suspension. | C-1, C-2, C-4, C-15, C-26 (fines), C-27, C-28, C-30, C-36, C-41. |
| A-3 | Owners expect the bill to pass and the shares to keep their value past the 2033 review. | expectations | 0.7 | Government sponsorship; owners' association; the review's terms. | C-2, C-3, C-21, C-55. |
| A-4 | Owners know the formula, expect passage, and have idle vessels or spare capacity to land more in 2026 and 2027. | expectations | 0.8 | Formula published with the bill; laid-up vessels; spare days. | C-8, C-9, C-10, C-29, C-32, C-33, C-37, C-45, C-49. |
| A-5 | A vessel's history passes to its buyer, and buyers price it in. | expectations | 0.85 | K2 allocates by vessel to the owner on 31 December 2027; brokers' practice. | C-3, C-55. |
| A-6 | Costs per tonne differ materially among vessels, and transfers are not blocked for most owners by the 8% limit. | other | 0.8 | Fuel use and catch per day by class; holdings far below 8%. | C-11, C-12, C-14, C-24, C-34, C-44, C-46 to C-48, C-50, C-54, C-56. |
| A-7 | Vessels and crew have other uses: the open saithe and ling fisheries, or sale abroad. | alternative_uses | 0.7 | Vessels that fish several species; second-hand market. | C-32, C-33, C-34, C-54. |
| A-8 | Crew skills are specific to fishing, and coastal towns offer few other jobs. | mobility | 0.6 | Local labor data; crew age and training. | C-46, C-48. |
| A-9 | Large ridge cod sell for more per kilo than small ones above 35 cm, and the gear catches mixed sizes. | other | 0.85 | Size-grade prices; gear selectivity. | C-16, C-17. |
| A-10 | Discarding is rarely detected. | enforcement | 0.75 | Observers on 10% of trawler trips, none on coastal boats. | C-16, C-17. |
| A-11 | The ten small harbors are monitored only at scheduled hours, so some landings go unrecorded. | enforcement | 0.55 | Staffing plans; night landings. | C-18. |
| A-12 | Ridge cod is landed as saithe or ling on a meaningful scale. | enforcement | 0.35 | The species are easy to tell apart. | Not reported (below). |
| A-13 | The 8% limit binds for a few of the largest firms. | binding | 0.55 | Current shares of the largest trawler firms; their plans. | C-23. |
| A-14 | Processors value secure supply enough to buy a vessel in order to hold shares. | other | 0.6 | Vertical integration elsewhere; price of a small vessel against share values. | C-20, C-53 (one chain). |
| A-15 | Recipients, processors and crew can organize at a cost below their stake. | other | 0.85 | Owners' association; four processors; crew union. | C-21, C-22, C-23. |
| A-16 | Fresh local ridge cod is only partly substitutable with imported or frozen whitefish. | substitutability | 0.7 | Menus; freshness premium. | C-25, C-28, C-29, C-30, C-35. |
| A-17 | Kallmark's ridge cod is a small part of the North Basin market, with close substitutes. | substitutability | 0.8 | Market shares; price correlation. | C-38, C-42, C-43. |
| A-18 | The plants are specific to ridge cod and compete for the fish landed, while their output is priced in the wider market. | alternative_uses | 0.6 | Plant equipment; number of buyers at each port. | C-35, C-37, C-38, C-39. |
| A-19 | The plants cannot fully replace ridge cod with other species. | other | 0.7 | Filleting lines; volumes of other species. | C-36, C-38, C-39, C-40. |
| A-20 | Consolidation favors larger vessels, which land at the processing ports. | other | 0.6 | Costs by class; where trawlers land. | C-51, C-52. |
| A-21 | Surplus vessels are not absorbed by other fisheries and buyers abroad at unchanged prices. | other | 0.6 | Second-hand prices; size of the foreign market. | C-53, C-54. |
| A-22 | The Directorate's budget is raised by the stated 18 million marks. | revenue_use | 0.9 | K4. | C-5, C-6, C-57. |
| A-23 | Some recipients sell shares, realizing their value. | other | 0.8 | Retirements; trading in comparable schemes. | C-13, C-26 (fees), C-56. |
| A-24 | For some holders who stop fishing, keeping a minimal registered vessel costs less than what they gain by holding rather than selling. | other | 0.7 | 600-mark fee; mooring costs; expected rise in share values. | C-19, C-53 (one chain). |
| A-25 | Fresh-fish buyers turn to saithe and ling when ridge cod costs more. | substitutability | 0.7 | Menus; fishmongers' sales. | C-31, C-32. |
| A-26 | The lay stays at 45% for at least a season after tonnage concentrates. | other | 0.75 | The agreement is renegotiated by season. | C-47, C-48. |
| A-N1 | Without the Act, some owners not now fishing ridge cod would enter the fishery from 2028. | counterfactual_trend | 0.7 | NEW. Open fishery; registration open to any seaworthy vessel for 600 marks; laid-up vessels (A-4's evidence); vessels that switch among species (A-7's evidence). | C-15. |
| A-N2 | Some households who buy fresh ridge cod can catch it themselves within the recreational exemption, and do so when its price rises. | substitutability | 0.55 | NEW. Coastal country; the exemption allows 10 fish a person a day. Weak evidence: no data on recreational effort. | C-25. |
| A-N3 | The dockside monitoring fee (15 marks a tonne) is treated as a landing fee and deducted as a trip expense under the Share Agreement. | other | 0.6 | NEW. The Agreement lists landing fees among trip expenses; the fee is charged per tonne at landing; K3 restricts only the cost of acquiring quota. | C-47 (one chain). |

**Not reported** (an assumption below 0.5):
- Ridge cod landed as saithe or ling to avoid tonnage (`reclassification` increase; CR-4 with x: land as ridge cod, y: land as another species): needs A-12 (p 0.35).
- Recreational catch sold illegally (`informal_activity`): no case assumption; the direction is licensed by CR-6 (an open illegal margin) but needs its own premise.
- Largest firms holding through nominally unaffiliated owners to evade the 8% limit: needs a premise beyond A-13 that such holding is feasible.

### Final check before the report

1. *Uncombined chains.* Every (class, variable) reached by two chains is in section 7; opposite signs within a horizon are `ambiguous` (C-32, C-47, C-52, C-53). Chains in section 8 (race, plants, fresh prices) are recorded as consequences and combined by horizon.
2. *Group signs.* Taxpayers and recipients of other spending (C-6) and crew employment or hours in the race (C-45) use group signs.
3. *Baseline.* Every sign is against the open fishery with no cap. K3, the 8% limit and the 1% fee are not signed against versions of the policy without them (section 7, last row); K3 is signed only through its per-reading effects (C-24, C-47) and lobbying (C-22).
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for sums paid (C-10, C-14, C-27, C-55, C-6) or received (C-13), not for fresh buyers who may buy less.
5. *Timing shifts.* Landings, fresh prices, plant throughput, inputs, crew work and saithe landings are signed per window (short 2026-2027; medium 2028-2032).
6. *Both sides of every transfer.* Section 9, last paragraph.
7. *Every class, every core rule.* CR-4 (every pair), CR-6, CR-7 (incl. 7c) and CR-9 were checked for each class in section 3: capitalization for recipients (C-2, C-3), plants (C-39) and vessels (C-53); enforcement costs (C-5) and the payer (C-6); CR-6 for the right (C-4) and illegal margins (C-16, C-18); CR-9 for crew (contract), plants, inputs, harbors, substitutes, foreign markets, brokers and monitors. For officials, CR-4 (whether to enforce strictly) needs a premise on their ends; not signed.
8. *Unstated premises.* Three added (A-N1 to A-N3); lobbying rests on A-15; quality and discard claims on A-9 and A-10.

## 11. Report

**The policy:** From 2028, Kallmark's ridge cod landings are capped at 40,000 tonnes a year (about 48,000 are landed now), to be set by the Ministry from 2033. The cap is divided into permanent, saleable shares given free to vessel owners in proportion to their vessels' landings in 2025 to 2027; only vessel owners may hold them, up to 8% each. Owners may not deduct the cost of acquiring quota from the crew's share of trip revenue. Landings are weighed at 13 sites at the owners' expense, and the Directorate's budget rises by 18 million marks a year.

**Visible consequences:** Less ridge cod is landed from 2028 (C-1). Owners with catch history receive shares worth money (C-2), and their vessels gain value from the day the bill was introduced (C-3). Tonnage leases have a price (C-4). The Directorate spends more (C-5), at the expense of taxpayers or other public spending (C-6); owners pay monitoring fees (C-7).

**Invisible consequences:**
- *Owners:* in 2026 and 2027 they race to land more ridge cod to build history (C-8, C-9), using up part of the shares' value (C-10). From 2028 tonnage moves to low-cost vessels: fewer vessels fish, each lands more (C-11, C-12). Sellers and lessors realize value (C-13); buyers and lessees pay (C-14). Legal-size fish are discarded to land larger ones (C-16, C-17), some landings go unrecorded at small harbors (C-18), and detected violators lose catch and pay fines (C-27, C-26). Holders who stop fishing keep idle registered vessels (C-19). Owners lobby over the 2033 TAC (C-21) and the largest firms over the 8% limit (C-23).
- *Entrants:* fewer enter, since entry now costs the price of shares or leases (C-15).
- *Crew:* more work in the race (C-45), less from 2028 (C-44); displaced crew earn less (C-46); agreements below 45% become more common after renegotiation (C-48). Crew and owners lobby over the lease ruling (C-22).
- *Processors and plant workers:* plants process more in the race and less from 2028 (C-37, C-36), pay more for fish (C-35), earn less on their capital (C-38) and lose value from announcement (C-39); plant employment falls (C-40). Processors buy vessels to hold shares (C-20).
- *Fresh fish buyers:* fresh ridge cod is cheaper in 2026-2027 (C-29), dearer from 2028 (C-28), and less is bought (C-30); buyers turn to saithe and ling (C-31) and some households catch their own (C-25).
- *Other markets:* saithe and ling landings fall in the race and rise from 2028 (C-33, C-34); fuel, ice and bait sales rise then fall (C-49, C-50); fewer landings at small harbors (C-51); more vessels sold abroad (C-54); North Basin buyers get fewer Kallmark exports at a slightly higher price and buy more foreign saithe and haddock (C-41 to C-43). Brokers and monitors find work (C-56, C-57); fees and fines flow to the Directorate (C-26).

**Ambiguous effects:** saithe and ling prices in Kallmark (C-32: more demand from fresh buyers against more supply from displaced vessels); earnings per crew member on vessels still fishing in the first season (C-47: more tonnes each and cheaper trips against the monitoring fee and, under U1-a, lease payments deducted before the share); landings at the processing ports (C-52: consolidation toward them against fewer tonnes in total); values of vessels without history (C-53: demand for vessels as a condition of holding shares against surplus vessels). Under U1-a acquisitions are more often structured as leases (C-24); under U1-b they are not.

**Key conditions:** the cap binds (A-1, 0.9) and is enforced at the dock (A-2, 0.8); owners expect shares to keep their value (A-3, 0.7) and could race in 2026-2027 (A-4, 0.8); costs differ among vessels (A-6, 0.8), which drives consolidation; plants are specific and cannot switch species (A-18, 0.6; A-19, 0.7); discarding is rarely detected (A-10, 0.75). Three premises were added: entry would continue without the Act (A-N1, 0.7), households can catch their own (A-N2, 0.55), and the monitoring fee is deducted as a landing fee (A-N3, 0.6).

**What this analysis cannot say:** the size of any effect; whether total crew or owner income rises or falls; the effect of the cap on the ridge cod stock and on catches, prices and share values after 2032 (biological and environmental effects are out of scope, as are health and safety); whether the policy is good. It does not weigh the windfall to recipients against the losses to entrants, crew, plants and fish buyers.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | vessel_owners (ridge cod fleet) | quantity_traded (ridge cod landed in the legal market) | decrease | medium (2028-2032) | visible | B | CR-1 (op 1: landing beyond tonnage removed where enforced, A-2); CR-6 (the cap fixes the quantity below the counterfactual 48,000 t, A-1); CR-4b (owners who would have landed more stop at their tonnage) | A-1, A-2 |
| C-2 | vessel_owners.recipients | asset_value (quota shares) | increase | medium (from 1 January 2028) | visible | B | CR-1 (op 2 and 4: a saleable right is added and given free); CR-6 (with the quantity fixed and the fish priced in a wider market, the price of the right rations it); CR-7c and CR-10c (a created asset is valued at its expected yields and captured by whoever receives it, A-3) | A-1, A-2, A-3 |
| C-3 | vessel_owners.recipients | asset_value (vessels with 2025-2027 ridge cod history) | increase | short (from 3 February 2026) | invisible | B | CR-7c, 0.7 clarification "claims before creation" (the claim travels with the vessel, A-5, and is capitalized when the rule becomes expected, partly as passage becomes likely); CR-10a; CR-10c | A-1, A-3, A-5 |
| C-4 | vessel_owners, lessees | right_lease_price (annual ridge cod tonnage) | increase | medium | invisible | B | CR-6, 0.7 clarification "a fixed quantity of a good priced in a wider market" (the lease price rations the capped tonnage); CR-5c | A-1, A-2 |
| C-5 | officials.fisheries_directorate | enforcement_cost | increase | medium | visible | B | CR-1 (op 4: 18 million marks a year); CR-8c (used up in enforcing) | A-22 |
| C-6 | taxpayers, recipients of other public spending | resources_available_other_uses | at_least_one_decrease | medium | invisible | B | CR-8b, 0.7 clarification "payers from the general budget"; CR-8a | A-22 |
| C-7 | vessel_owners (ridge cod fleet) | compliance_cost (monitoring fee, designated sites, registration of transfers) | increase | medium | visible | A | CR-1 (op 3: 15 marks a tonne, landing only at 13 sites, registration); CR-8c | none |
| C-8 | vessel_owners | quantity_traded (ridge cod landed) | increase | short (2026-2027) | invisible | B | CR-10a (the expected allocation alters choices now); CR-4 (x: stay idle or fish other species, y: land ridge cod; y now also brings a claim to shares, A-4); CR-7c clarification (actors compete to qualify for the claim) | A-4 |
| C-9 | vessel_owners | capital_stock_target (vessels and days at sea in ridge cod) | increase | short (2026-2027) | invisible | B | CR-10a; CR-4 (idle vessels reactivated and spare days used, A-4) | A-4 |
| C-10 | vessel_owners (racing for history) | resources_available_other_uses | decrease | short (2026-2027) | invisible | B | CR-7c clarification (part of the value is used up in the race); CR-8c; CR-3c (trips that pay only through history cost more than the fish brings: in an open fishery any trip that paid in money would have been made anyway) | A-4 |
| C-11 | vessel_owners | number_of_sellers (vessels fishing ridge cod) | decrease | medium | invisible | B | CR-4 (x: fish own tonnage, y: sell or lease it to a lower-cost vessel); CR-5 (exchanges of tonnage both sides expect to gain from); CR-7a (tonnage moves to the use that yields more, A-6) | A-1, A-6 |
| C-12 | vessel_owners.low_cost | quantity_supplied (ridge cod per vessel still fishing) | increase | medium | invisible | B | CR-7a; CR-5 (low-cost vessels buy or lease tonnage, A-6) | A-1, A-6 |
| C-13 | vessel_owners.recipients (sellers and lessors of tonnage) | resources_available_other_uses | increase | medium | invisible | B | CR-8b (the price of shares or leases is a receipt to the seller); CR-7c (the value captured at creation is realized, A-23) | A-1, A-23 |
| C-14 | vessel_owners.low_cost (buyers and lessees of tonnage) | resources_available_other_uses | decrease | medium | invisible | B | CR-8b (both sides of C-13); CR-3c (sums paid, and leases paid every year) | A-1, A-6 |
| C-15 | sellers.prospective | entry_rate | decrease | medium | invisible | B | CR-1 (op 3: entry now carries the price of shares or leases; op 1 without a registered vessel); CR-4 (x: enter, y: stay out; x made worse; A-N1: some would have entered); CR-5a | A-N1, A-1, A-2 |
| C-16 | vessel_owners | discards (legal-size ridge cod) | increase | medium | invisible | B | CR-6 (pressure moves to the illegal margin, which needs its own premise: A-10); CR-4 (x: land a small fish against scarce tonnage, y: discard it and land a larger one, A-9); CR-8a | A-1, A-9, A-10 |
| C-17 | vessel_owners | quality_per_unit (average size of ridge cod landed) | increase | medium | invisible | B | CR-4 (same choice as C-16: larger fish are kept, A-9, A-10) | A-1, A-9, A-10 |
| C-18 | vessel_owners (landing at small harbors) | informal_activity (unrecorded ridge cod landings) | increase | medium | invisible | B | CR-6 (illegal margin, own premise A-11); CR-4 (x: land within tonnage or lease, y: land unrecorded where unmonitored) | A-1, A-11 |
| C-19 | vessel_owners.leaving_holders | units_held_vacant (registered vessels kept idle to hold shares) | increase | medium | invisible | B | CR-1 (op 1: only vessel owners may hold); CR-4 (x: sell vessel and shares, y: keep a minimal vessel and the shares, A-24) | A-24 |
| C-20 | processors | quantity_traded (registered vessels bought by processors to hold shares) | increase | medium | invisible | B | CR-1 (op 1: holding needs a vessel); CR-4 (x: buy fish at the dock, y: buy a vessel and hold shares, A-14) | A-14, A-1 |
| C-21 | vessel_owners.recipients | lobbying_effort (allocation formula; TAC from 2033) | increase | short; medium; long | invisible | B | CR-4 (x: accept, y: lobby; their stake in share values, A-3, makes y worth more); CR-10a; CR-8c | A-15, A-3 |
| C-22 | crew.ridge_cod, vessel_owners | lobbying_effort (Directorate's ruling on U1) | increase | short; medium | invisible | B | CR-4 (x: accept either ruling, y: press for one; each side gains from its reading); CR-8c | A-15 |
| C-23 | vessel_owners.largest_firms | lobbying_effort (to raise the 8% limit) | increase | medium | invisible | B | CR-1 (op 1: holding above 8% removed, A-13); CR-4 (x: accept, y: lobby); CR-8c | A-13, A-15 |
| C-24 | vessel_owners (acquiring tonnage) | reclassification (acquisitions structured as long-term leases) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-4 (x: buy shares, whose cost K3 bars from the crew settlement; y: lease, deductible under U1-a, so y gains; under U1-b both are barred, so K3 does not favor either) | A-6 |
| C-25 | recreational_fishers | home_production (ridge cod caught under the exemption) | increase | medium | invisible | B | CR-9 (relation: own catch substitute for fresh ridge cod); CR-4 (x: buy at the higher price, C-28; y: catch it, A-N2); CR-6 (the exemption is an open margin) | A-N2, A-16, A-1 |
| C-26 | officials.fisheries_directorate | non_tax_receipts (transfer fees; fines and forfeitures) | increase | medium | invisible | B | CR-1 (op 3: 1% fee on transfers; penalties); CR-8b; CR-8e (forfeited catch). Independent chains (CR-12d): fees need A-23, fines need A-2 | A-23; A-2 |
| C-27 | vessel_owners (detected violators) | resources_available_other_uses | decrease | medium | invisible | B | CR-8e (forfeiture and fines: the holder's means fall); CR-8b | A-2, A-1 |
| C-28 | buyers.fresh | price_paid (fresh ridge cod) | increase | medium | visible | B | CR-9 (relation: fresh and processed segments share the fish landed); CR-6 (fewer fish, partial substitutes, A-16: the domestic fresh price is not set in the wider market); CR-7a (owners allocate landings between segments until yields are equal) | A-1, A-2, A-16 |
| C-29 | buyers.fresh | price_paid (fresh ridge cod) | decrease | short (2026-2027) | invisible | B | CR-9; CR-6 (more fish landed in the race, C-8, partial substitutes, A-16) | A-4, A-16 |
| C-30 | buyers.fresh | quantity_traded (fresh ridge cod) | decrease | medium | invisible | B | CR-4c (at a higher price the last unit is given up); CR-5a | A-1, A-2, A-16 |
| C-31 | buyers.fresh | quantity_substitute (saithe and ling bought fresh) | increase | medium | invisible | B | CR-4 (x: ridge cod, y: saithe or ling; x made worse, A-25) | A-1, A-25 |
| C-32 | sellers.substitutes, buyers.fresh | price_substitute (saithe and ling in Kallmark) | ambiguous | short; medium | invisible | B | CR-12b. Short: (+) CR-7a, vessels leave saithe and ling to build history (A-4, A-7); (−) CR-4, fresh buyers turn to cheaper ridge cod. Medium: (+) CR-4, fresh buyers turn from dearer ridge cod (A-25); (−) CR-7a, displaced vessels and crew enter saithe and ling (A-7). No dominance premise | A-4, A-7, A-25, A-1 |
| C-33 | sellers.substitutes | quantity_substitute (saithe and ling landed by Kallmark vessels) | decrease | short (2026-2027) | invisible | B | CR-10a and CR-7a (vessels move to ridge cod to build history, A-4, A-7); CR-9 (fresh buyers also buy less saithe while ridge cod is cheap): both chains the same way | A-4, A-7 |
| C-34 | sellers.substitutes | quantity_substitute (saithe and ling landed by Kallmark vessels) | increase | medium | invisible | B | CR-7a (vessels without tonnage move to the open fisheries, A-6, A-7); CR-9 (demand from fresh buyers, C-31): both chains the same way | A-1, A-6, A-7 |
| C-35 | processors | price_paid (ridge cod bought at the dock) | increase | medium | invisible | B | CR-7a (owners sell to whichever segment pays more until yields are equal; the fresh price rises, C-28); CR-6; CR-9 (plants compete for the fish landed, A-18) | A-1, A-16, A-18 |
| C-36 | processors | quantity_traded (ridge cod processed) | decrease | medium | invisible | B | CR-9 and LW-10 (relation: ridge cod input_to processing; fewer fish landed, C-1; no full replacement, A-19) | A-1, A-2, A-19 |
| C-37 | processors | quantity_traded (ridge cod processed) | increase | short (2026-2027) | invisible | B | CR-9 and LW-10 (more fish landed in the race, C-8; plants compete for it, A-18) | A-4, A-18 |
| C-38 | processors | return_on_capital | decrease | medium | invisible | B | CR-7b (the loss settles on the means that cannot move: plants specific to ridge cod, A-18, A-19, whose output price is set in the wider market, A-17, so higher input prices and lower throughput cannot be passed on); CR-9 | A-1, A-17, A-18, A-19 |
| C-39 | processors | asset_value (processing plants) | decrease | short (from 3 February 2026) | invisible | B | CR-7c and CR-10c (the expected fall in yield, C-38, is borne by whoever owns the plants when it becomes expected) | A-1, A-18, A-19 |
| C-40 | workers.processing_plants | employment | decrease | medium | invisible | B | CR-9 and LW-10 (relation: plant labor input_to processing; demand for it follows throughput, C-36) | A-1, A-19 |
| C-41 | buyers.foreign | quantity_traded (Kallmark ridge cod exports) | decrease | medium | invisible | B | CR-9 (fewer fish processed, C-36); CR-5a | A-1, A-2 |
| C-42 | buyers.foreign | price_paid (North Basin whitefish) | increase | medium | invisible | B | CR-9 (relation: substitute, close); CR-6 (less supply at each price; A-17: Kallmark is about 7%, so the direction is signed, not the size) | A-1, A-17 |
| C-43 | sellers.foreign | quantity_traded (saithe and haddock sold in the North Basin) | increase | medium | invisible | B | CR-9 (relation: substitute, close); CR-4 (buyers turn to substitutes, A-17) | A-1, A-17 |
| C-44 | crew.ridge_cod | employment (ridge cod fishing) | decrease | medium | invisible | B | CR-9 and LW-10 (relation: crew labor input_to fishing; fewer tonnes, C-1, and fewer vessels, C-11); CR-7a | A-1, A-6 |
| C-45 | crew.ridge_cod | employment, hours_worked (ridge cod fishing) | at_least_one_increase | short (2026-2027) | invisible | B | CR-9 and LW-10 (reactivated vessels and spare days in the race, C-9, need crew; whether as more crew or more days each is not established) | A-4 |
| C-46 | crew.ridge_cod (displaced) | earnings | decrease | medium | invisible | B | CR-7b (the loss settles on those without alternatives: skills specific to fishing and few other jobs, A-8); CR-3a | A-1, A-6, A-8 |
| C-47 | crew.ridge_cod (still fishing) | earnings (per crew member) | ambiguous | medium (first season after tonnage concentrates) | invisible | B | CR-12b. (+) CR-7a and CR-9 (contract): more tonnes per vessel and lower trip expenses per tonne on low-cost vessels (A-6) with the lay unchanged (A-26); higher fresh price and larger fish (C-28, C-17). (−) CR-1 and CR-9 (contract): monitoring fee deducted as a landing fee (A-N3); under U1-a only, lease payments deducted before the crew share. Ambiguous under both readings | A-6, A-26, A-N3 |
| C-48 | crew.ridge_cod | term_prevalence (agreements with a crew share below 45%) | increase | medium (after renegotiation) | invisible | B | CR-5c (quota costs the owner must bear from the owner's side, all purchases and under U1-b also leases, move the range of acceptable terms against the crew); CR-7a (earnings per remaining crew member above what crew earn in other uses are pulled back); CR-7b (crew with few alternatives bear more, A-8); not before a season has passed (A-26) | A-26, A-6, A-8 |
| C-49 | input_suppliers (fuel, ice, bait) | quantity_traded (to ridge cod vessels) | increase | short (2026-2027) | invisible | B | CR-9 and LW-10 (relation: input_to; more trips in the race, C-9) | A-4 |
| C-50 | input_suppliers (fuel, ice, bait) | quantity_traded (to ridge cod vessels) | decrease | medium | invisible | B | CR-9 and LW-10 (fewer tonnes, C-1, landed by lower-cost vessels that use less per tonne, A-6); CR-7a | A-1, A-6 |
| C-51 | input_suppliers (landing services at the ten small harbors) | quantity_traded (ridge cod landed at small harbors) | decrease | medium | invisible | B | CR-9 (relation: landing services input_to fishing); CR-7a (fewer tonnes, and tonnage moves to larger vessels landing at the processing ports, A-20) | A-1, A-20 |
| C-52 | input_suppliers (landing services at the three processing ports) | quantity_traded (ridge cod landed at processing ports) | ambiguous | medium | invisible | B | CR-12b: (+) CR-7a, consolidation toward larger vessels that land there (A-20); (−) CR-9, fewer tonnes landed in total (C-1) | A-1, A-20 |
| C-53 | vessel_market | asset_value (fishing vessels without ridge cod history) | ambiguous | medium | invisible | B | CR-12b: (+) CR-1 op 1 and CR-4: a registered vessel is a condition of holding shares (A-14, A-24); (−) CR-7a and CR-6: surplus vessels not absorbed at unchanged prices (A-21) | A-14, A-21, A-24 |
| C-54 | vessel_market | quantity_traded (vessels sold abroad) | increase | medium | invisible | B | CR-7a and CR-4 (x: keep a vessel without tonnage, y: sell it abroad; A-7, A-21) | A-7, A-21, A-1, A-6 |
| C-55 | vessel_buyers.2026_2027 | resources_available_other_uses | decrease | short (2026-2027) | invisible | B | CR-8b (both sides of C-3: buyers pay sellers for history, A-5); CR-7c | A-5, A-3 |
| C-56 | intermediaries (quota brokers) | employment (brokering shares and leases) | increase | medium | invisible | B | CR-9 and LW-10 (relation: brokerage input_to share trading; trading exists, A-6, A-23) | A-6, A-23 |
| C-57 | monitors | employment (dockside monitoring and observers) | increase | medium | invisible | B | CR-8b (the budget and the fee are receipts to those paid from them); CR-9 and LW-10 | A-22 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-028-C1: The cap's effect on the shared ridge cod stock, and through it on cost per tonne, catches and share values after 2032. No core rule covers the growth of a natural resource; CR-9 follows `shared_facility` relations only at Tier C, and stock effects are environmental and out of scope. The analysis therefore gives no sign after 2032.
- GAP-028-C2: The payer's side of a created right. CR-8b requires every transfer to be matched by a payer, but the value of free shares comes partly from ending the competition that kept yields at the level of other uses in an open fishery (CR-7a). The losers can be named (entrants whose free entry is removed, buyers of fish and of tonnage, plants), but no core rule says whether this value is a transfer from them, or resources that were previously used up and now are not. Section 9 records the named losers and leaves the matching open.

**(b) Core-rule wording that was hard to apply.**
- CR-6, 0.7 clarification "a fixed quantity of a good priced in a wider market": here 70% of the good is priced in the wider market and 30% is not (A-16). The clarification does not say what happens when only part of the capped good is priced elsewhere; it was applied as "the right rations the quantity, and the domestic segment's price also rises", with CR-7a linking the two segments (C-28, C-35).
- CR-7c, clarification "claims before creation": it does not distinguish history already fixed when the rule becomes expected (2025: a windfall, nothing to compete for) from history still to be earned (2026-2027: competed for and partly used up). Both were recorded under C-3 and C-10.
- CR-1, recording the counterfactual law: K3 regulates a deduction that cannot exist without the Act (no quota, no quota cost). Against the no-policy counterfactual K3 has no direct sign; it acts only through the choice between buying and leasing (C-24) and through the crew's terms (C-47, C-48). The rule does not say how to sign a provision that limits a burden the same policy creates.
- CR-5c: it says the range of acceptable terms moves, not that the agreed term moves. C-48 needed CR-7a and CR-7b, and A-8, to sign the term itself.
- CR-12g with a race: the race for history is extra activity in 2026-2027, not activity moved from another window, so the per-window signs are against the counterfactual in each window; the rule and the ontology speak of shifts, and it took care to confirm that a short-horizon increase and a medium-horizon decrease are not to be combined.
- CR-3 note: whether owners racing for history have fewer resources for other uses (C-10) depends on reading their extra trips as paying less in money than they cost; this was argued from the open-fishery counterfactual (any trip that paid in money would have been made anyway), which the rule does not state.

**(c) Vocabulary missing from the ontology.**
- No variable for catch per unit of effort or for the size of a shared stock (needed for the Tier C chain through `shared_facility`).
- No variable for a share-of-revenue pay rate (the lay). `wage_rate` is per hour; C-48 used `term_prevalence` instead.
- No variable for the concentration of holdings of a right (share of quota held by the largest firms), which the 8% limit concerns.
- No variable for where an activity takes place within the jurisdiction (landings by port); C-51 and C-52 used `quantity_traded` with a named segment.
- No actor class for workers paid by a share of revenue under a standing contract; `crew.ridge_cod` was named ad hoc.
- No instrument type for a rule that limits the deductions in a private share contract; it is close to `mandated_contract_term` but restricts a term rather than mandating one.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the structure of the quota case: from 2028 fewer ridge cod are landed, the free shares and the vessels that carry a claim to them gain value (the vessels from the announcement), a lease price for tonnage appears and is what rations the cap, owners race for history in 2026 and 2027 with more landings, more vessels at sea and more work for crew, plants and suppliers, and less of each from 2028; tonnage consolidates on low-cost vessels, entry falls, legal-size fish are discarded to land larger ones, some landings go unrecorded, holders keep idle vessels and processors buy vessels to hold shares; the plants lose return and value from the announcement and plant work falls; fresh ridge cod costs more; and crew pay per remaining crew member, saithe and ling prices and landings at the processing ports are ambiguous in both. Much of this agreement is not independent: the pattern version (catalog 0.6) proposed the 0.7 clarifications the core version relied on (CR-6 "a fixed quantity of a good priced in a wider market" and "illegal margins", CR-7 "claims before creation", and the variables `right_lease_price`, `discards`, `no_change`), so where the two record the same claim differently because of them, the row is V, not an error. One key is signed in opposite directions: the value of vessels without history, which the pattern version signs `decrease` although its own C-11 and C-16 record the opposing demand for registered vessels as a condition of holding shares; the core version is right that it is `ambiguous`. The pattern version also signs nominee holdings under the 8% limit without the separate premise an illegal margin needs (the very point its own gap b2 made), declines to sign the North Basin whitefish price that CR-6 signs in direction, rests the fall in entry on an unstated premise that some would have entered (the core's A-N1), and names taxpayers alone as the payers of the Directorate's budget, which the 0.7 clarification to CR-8 replaces with a group. The core version omitted two derivable claims (entry during the race, the long-run decline of the fleet) and processors' lobbying, and signs crew and plant employment, and displaced crew's money earnings, more strongly than its premises carry. Most of the 19 core-only claims are pattern-version omissions: the race window seen from other markets (fresh prices, plant throughput, saithe and ling landings), both sides of the money flows (racers, vessel buyers, violators, fees and fines), crew contract terms, the U1 choice between buying and leasing, and the receiving side of enforcement spending.

Counts: M 19, V 15, S 1, OP 19, OC 4.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1, C-30, C-41 | V | | Split by side: owners' legal landings (C-1), fresh buyers (C-30), foreign buyers (C-41). Pattern labels the horizon "short (from 2028)", core "medium (2028-2032)"; same window. |
| C-2 | C-2 | M | | Core dates the shares' own value from creation and puts the pre-creation value on vessels (C-3), as the 0.7 clarification "claims before creation" asks. Core's derivation still says the value is "captured by whoever receives it", which its own C-3 and C-55 qualify; the sign is unaffected. |
| C-3 | C-4 | V | | Pattern: `price_paid` with a qualifier, signed from a price that did not exist; core: `right_lease_price`, added in 0.7 from the pattern version's own vocabulary gap (d2). Pattern cites CR-7b; core cites the 0.7 CR-6 clarification on a good priced in a wider market, which this example prompted. |
| C-4 | C-8 | M | | Both rest on A-4. |
| C-5 | C-9 | V | | Pattern: `investment_target` (vessels, engines, gear); core: `capital_stock_target` (idle vessels reactivated, days at sea). Same race response under CR-10a and CR-4. Pattern's engine and gear upgrades go slightly beyond A-4, which speaks only of idle vessels and spare capacity. |
| C-6 | none | OC | E | `entry_rate` increase in 2026-2027: CR-10a with CR-4 (x: stay out, y: enter and land ridge cod; y now also brings a claim to shares; A-4, A-5, and registration open to any seaworthy vessel for 600 marks). Core-version omission: its C-8 and C-9 cover existing owners only, and its C-15 signs entry from 2028 alone. |
| C-7 | C-15 | M | | Same sign. The core adds A-N1 (without the Act some owners would enter from 2028), the premise that CR-4 needs for anyone to be at the margin of entry. The pattern version cites only A-1 and A-2 and hides it. |
| C-8 | C-3 | M | | Same claim, same timing (from 3 February 2026, in steps as passage becomes likely). Core labels the class `vessel_owners.recipients` (owners on 31 December 2027), while its own section 8 and the 0.7 clarification put the gain on owners when the rule became expected, as the pattern's `vessel_owners.at_announcement` does; a class-label slip in the core. |
| C-9 | C-11 | M | | |
| C-10 | none | OC | E | `capital_stock_target` (vessels in the ridge cod fishery) decrease, long. Derivable: CR-7a and CR-4 (x: keep a vessel without tonnage, y: sell, move or scrap it), CR-10b (gradual; A-1, A-6, A-7). Core-version omission: its section 8 says exit persists and C-54 records vessels sold abroad, but no consequence signs the fleet, and its only `capital_stock_target` entry is the window increase (C-9). |
| C-11 | C-19 | M | | |
| C-12 | C-17 | M | | |
| C-13 | C-16 | V | | Pattern records the discard indirectly as fewer small fish landed (its gap d1); core uses `discards`, added in 0.7. Core derives it from CR-4 on the pair of options (land a small fish against tonnage, or discard it and land a larger one) without needing the CR-4c "unit of the constraint" reading the pattern version proposed. |
| C-14 | C-18 | M | | Both rest on A-11; core applies the 0.7 CR-6 clarification that illegal margins need their own premise, which the pattern version followed here. |
| C-15 | none (core: "Not reported") | OC | P | `reclassification` (holdings through nominees and nominally separate companies to stay under 8%). The limit counts holdings "with affiliates", so this is evasion (CR-4, x: comply, y: violate), and the 0.7 CR-6 clarification requires each illegal margin to carry its own premise on detection and cost. A-13 says only that the limit binds. The pattern version (RS-5) hides the premise that nominee holdings escape the affiliate rule at a cost below the stake, the same point its own gap b2 made for the other illegal margins. The core declined it for that reason. |
| C-16 | C-20 | V | | Pattern: `reclassification`; core: `quantity_traded` of registered vessels bought by processors. Same response under CR-1 op 1 and CR-4 (A-14). |
| C-17 | C-21, C-22 | V | | Split by group and object: recipients on the TAC and formula (C-21), crew and owners on the U1 ruling (C-22). Processors' lobbying for a right to hold shares is in the pattern but not the core: derivable from CR-1 op 1 on processors with CR-4 and A-15; core-version omission within a matched row. |
| C-18 | C-44 | V | | Pattern: `employment`, `hours_worked`, `at_least_one_decrease`; core: `employment` decrease alone. CR-9 with LW-10 gives a fall in demand for crew labor, not which of berths or days falls; low-cost vessels landing more each (core C-12) could keep crew and fish more days. The core's single sign needs an unstated premise that crew per vessel does not rise; the group sign is what the rules give. |
| C-19 | C-45 | M | | |
| C-20 | C-34 | M | | Pattern's "short to medium" runs from 2028; core's medium is the same window. |
| C-21 | C-28 | M | | Both rest on A-16. |
| C-22 | C-35 | V | | The same exchange from the other side: owners' ex-vessel price received (pattern) and plants' price paid at the dock (core). Pattern rests on A-17 and A-18 (plants compete for the fish landed); core adds the fresh segment through CR-7a (A-16). |
| C-23 | C-36 | V | | Pattern: `quantity_supplied` of processed ridge cod; core: `quantity_traded` processed. |
| C-24 | C-38 | M | | Core adds A-19. |
| C-25 | C-40 | V | | Pattern: `employment`, `hours_worked` group; core: `employment` alone. As C-18: the core's single sign goes beyond CR-9 without a premise that plants cut staff rather than hours. |
| C-26 | C-51 | M | | |
| C-27 | C-49 | V | | Pattern: `quantity_complement` (fuel, ice, gear, repair, boatbuilding); core: `quantity_traded` to vessels (fuel, ice, bait), as `input_to`. |
| C-28 | C-50 | V | | As C-27. |
| C-29 | C-53 | S | P | Pattern: `asset_value` of vessels without shares decrease (RS-13, A-21). Core: `ambiguous` (CR-12b): against surplus vessels, a registered vessel is now a condition of holding shares, so processors buy vessels (A-14) and leaving holders keep theirs off the market (A-24). The pattern version recorded both responses (its C-11 and C-16) but did not combine them with C-29. No premise in either version separates the minimal vessels held for registration from the surplus trawlers, so the opposing chain stands and the pattern's decrease is not valid. |
| C-30 | C-47 | V | | Both `ambiguous` under both readings of U1. Pattern: `wage_rate` per day at sea, with fewer berths and A-8 among its (−) chains, which mixes displaced crew into the class; core: `earnings` per remaining crew member, with displaced crew separate (C-46) and the monitoring fee as a further (−) chain (A-N3). |
| C-31 | C-7 | M | | Both Tier A. |
| C-32 | C-5 | M | | Pattern Tier A with no premise; core Tier B on A-22. |
| C-33 | C-6 | V | | Pattern: `taxpayers` decrease. Core: taxpayers or recipients of other public spending, `at_least_one_decrease`, as the 0.7 clarification to CR-8 ("payers from the general budget") requires. Written before that clarification, the pattern overclaims for taxpayers alone; its own A-22 "if false" column already names the alternative. |
| C-34 | C-13 | M | | Core adds lessors. |
| C-35 | C-14 | V | | Pattern: later buyers of shares; core: low-cost owners buying or leasing tonnage. Same CR-8b side of C-34. |
| C-36 | C-32 | M | | Core also signs the race window `ambiguous` with the chains reversed. |
| C-37 | C-52 | M | | |
| C-38 | C-39 | M | | |
| — (share recipients' position by their own ranking, not signed) | none | OC | J | Pattern leaves it unsigned by DM-3 (one-time race costs against a lasting asset). The core rules give the same result (CR-12b; CR-2 for those who raced), and the core records both sides (C-2, C-3, C-10) without a combined row. Nothing scorable lost. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-10 | OP | E | Racers' `resources_available_other_uses` decrease in 2026-2027 (CR-8c, CR-3c; A-4). The pattern version described the race's cost in section 9 but declined to record it for want of a variable for "effort beyond output"; the money side of it fits `resources_available_other_uses`. Pattern-version omission. |
| C-12 | OP | E | Low-cost vessels land more each (CR-7a, CR-5; A-6). Stated in the pattern version's consolidation prose and its proposed EN-13, not recorded. Pattern-version omission. |
| C-23 | OP | E | Largest firms lobby to raise the 8% limit (CR-1 op 1, CR-4; A-13, A-15). RS-7 gives it; the pattern version's C-17 names recipients but not this object. Pattern-version omission. |
| C-24 | OP | E | Acquisitions structured as leases: U1-a increase, U1-b `no_change` (CR-4, x: buy, y: lease; K3 bars only purchase costs from the crew settlement under U1-a). Signed against the counterfactual, where no such line exists, so `no_change` under U1-b is right. RS-5 applied to K3's line would give it; the pattern version analyzed U1 only for crew pay. Its vocabulary gap (d4) would have blocked the U1-b half before `no_change` was added in 0.7. Pattern-version omission. |
| C-25 | OP | A | Recreational fishers catch more under the exemption. Rests on the new premise A-N2 (p 0.55, weak evidence). Valid given it. |
| C-26 | OP | E | Directorate's `non_tax_receipts` increase: 1% transfer fees (A-23) and fines and forfeitures (A-2), independent chains (CR-12d). The pattern version recorded the Directorate's costs but not its receipts; `non_tax_receipts` was added in 0.7, but the claim was derivable before. Pattern-version omission. |
| C-27 | OP | E | Detected violators lose means (CR-8e, CR-8b). Pattern-version omission (K4's forfeiture and triple fines). The core cites A-2 and A-1, but the claim also needs violations to occur: A-10 or A-11 should be listed as alternative premises (CR-12d). |
| C-29 | OP | E | Fresh ridge cod cheaper in 2026-2027 (CR-9, CR-6; more fish landed in the race, A-4, A-16). The pattern version signed the race window for landings, crew and suppliers but not for fresh buyers. Pattern-version omission. |
| C-31 | OP | E | Fresh buyers buy more saithe and ling (CR-4; A-25). The pattern version used this chain in section 7 (RS-16 with A-25) but did not record the quantity, which RS-16 also gives. Pattern-version omission. |
| C-33 | OP | E | Saithe and ling landed by Kallmark vessels fall in 2026-2027 (CR-10a, CR-7a: vessels move to ridge cod to build history; A-4, A-7). Pattern-version omission: its C-20 records only the return flow from 2028. |
| C-37 | OP | E | Plants process more in 2026-2027 (CR-9, LW-10; A-4, A-18). Pattern-version omission of the race window for processors. |
| C-42 | OP | P | North Basin whitefish `price_paid` increase. CR-6: with Kallmark offering less, planned purchases at the old price exceed planned sales, since other sellers were already selling what they wished at that price; so the direction is signed and only the size is small (A-17). The pattern version declined to sign it ("a rise needs a premise that buyers treat ridge cod as distinct"), which confuses a small change with no direction; the core signs the whole whitefish market, not ridge cod's premium. The 0.7 CR-6 clarification says only that the good's price does not *ration* the capped quantity, not that it does not move; EN-6's 0.7 Unless clause ("`price_paid` is not signed") follows the pattern version here and overstates the point. |
| C-43 | OP | E | Foreign saithe and haddock sellers sell more in the North Basin (CR-9, CR-4; A-17). The pattern version's own argument (close substitutes take up the gap) implies it, but it stopped at buyers as diffuse bystanders. Pattern-version omission. |
| C-46 | OP | E | Displaced crew's `earnings` decrease (CR-7b, CR-3a; A-8). Core-version overclaim: CR-3a gives a loss by the crew's own ranking, not a fall in money earnings, and A-8 is a premise about mobility (few other jobs), not that the next-best work pays less money (the same point WE-003's comparison made against EN-3). Valid only if A-8 is extended to say so. |
| C-48 | OP | E | Agreements with a crew share below 45% become more common after renegotiation (CR-5c, CR-7a, CR-7b; A-26, A-6, A-8). All chains push the same way (quota costs borne on the owner's side, more crew than berths, few alternatives). The pattern version named renegotiation (CR-5c) in section 7 but did not sign the term. Pattern-version omission. |
| C-54 | OP | E | More vessels sold abroad (CR-7a, CR-4; A-7, A-21). Stated in the pattern version's C-29 note, not recorded. Pattern-version omission. |
| C-55 | OP | E | Buyers of vessels in 2026-2027 have fewer means for other uses (CR-8b, both sides of C-3; A-5). The pattern version says in section 7 that they "paid for the claim" but records no consequence; OC-7 requires the matching chain. Pattern-version omission. |
| C-56 | OP | J | Quota brokers' employment rises (CR-9, LW-10). A new market at depth 2; the pattern version pruned the analogous lenders. Depth choice. |
| C-57 | OP | E | Dockside monitors' and observers' employment rises (CR-8b, CR-9; A-22). The receiving side of the enforcement budget and the per-tonne fee; the pattern version recorded only the cost side (OC-3). Pattern-version omission. |

### Findings

- **Pattern version signs through an opposing chain (C-29, RS-13).** RS-13 gives the supply chain for surplus vessels, but the case's own K2 condition (only vessel owners may hold shares) adds demand for registered vessels, which the pattern version recorded as C-11 and C-16 and then did not combine. Under CR-12b the value of vessels without history is `ambiguous`; the decrease is not valid without a premise that the two segments of the vessel market are separate.
- **Pattern hides premises.** C-15 (nominee holdings) treats evasion of the affiliate rule as RS-5 reclassification with no premise on detection or cost; under the 0.7 CR-6 clarification on illegal margins it needs its own premise. C-7 (less entry from 2028) needs a premise that some would have entered the open fishery, which the core added as A-N1. C-33 names taxpayers alone as payers; the 0.7 clarification to CR-8 gives only the group. C-5 adds engine and gear upgrades beyond what A-4 supports.
- **Pattern under-claims (North Basin price).** The pattern version left the whitefish price unsigned because ridge cod is a small part of the market. CR-6 signs the direction of a supply reduction whatever its share; smallness bears on size, which the method does not sign. EN-6's 0.7 Unless clause was written from this pattern version's reading and should say that the capped good's price moves in the CR-6 direction but does not ration the cap, rather than that it "is not signed".
- **Errors in the core version.** Omissions: entry during the race (pattern C-6), the long-run decline of the fleet (pattern C-10), processors' lobbying (within pattern C-17). Overclaims: crew and plant `employment` signed alone where CR-9 gives only the `employment`, `hours_worked` group (C-44, C-40), and displaced crew's money `earnings` signed from a mobility premise (C-46). Recording: C-3's class should be owners when the rule became expected, as the core's own section 8 says; C-2's derivation repeats "captured by whoever receives it" without the qualification the 0.7 "claims before creation" clarification adds; C-27 omits the premises that violations occur (A-10, A-11).
- **Errors in the pattern version (omissions).** The race window outside the fleet (fresh prices C-29, plant throughput C-37, saithe and ling landings C-33), both sides of money flows (racers C-10, vessel buyers C-55, violators C-27, Directorate receipts C-26, monitors C-57), more catch per remaining vessel (C-12), fresh buyers' switch to saithe and ling (C-31), the lobbying over the 8% limit (C-23), the U1 choice between buying and leasing (C-24), crew contract terms after renegotiation (C-48), vessels sold abroad (C-54) and foreign substitute sellers (C-43).
- **Limits of the core rules.** None produced a difference: no row needed cause K. The core version's own GAP-028-C1 (no rule for a shared natural stock, so no sign after 2032) and GAP-028-C2 (the payer side of a value created by ending competition in an open fishery) bind both versions alike; the pattern version reached the same place by stating that the free allocation is not a transfer from taxpayers and leaving the stock out of scope. The 0.7 clarifications drawn from this example (CR-6 for a good priced in a wider market and for illegal margins; CR-7 "claims before creation") did the work they were written for, and the core version needed none of the pattern version's other proposals: high-grading followed from CR-4 on a pair of options without a "unit of the constraint" reading of CR-4c. Two core-rule wordings remain open, as the core version noted: the CR-6 clarification does not say what happens when only part of the capped good is priced in the wider market (here 30% is sold fresh at home), and CR-7c's "claims before creation" does not distinguish history fixed before the announcement (a windfall) from history still to be earned (competed for and partly used up).
