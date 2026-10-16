# WE-028 Catch cap with individual transferable quota shares

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

A stylized policy in a fictional country. It resembles real individual transferable quota schemes but is not modeled on any one of them. It was chosen to probe parts of the method the first 25 examples did not test: a fixed quantity whose price is set mostly in a wider market (CR-6), an asset the policy creates and gives away, with a claim to it that can be traded before it exists (CR-7c), consolidation through trade in the rights (CR-7a), and an allocation rule that rewards activity after the announcement (CR-10a). The fish stock is outside the scope of version 1: its size is not a variable, and nothing below says whether the cap helps or harms it. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Kallmark Ridge Cod Fishery Act.** Kallmark is a coastal country of about 3 million people. Its boats land about 48,000 tonnes of ridge cod a year (average of 2022 to 2024). About 70% is frozen or filleted by four processing plants (two at Brennhavn, one at Skelby, one at Tornhavn) and exported to the North Basin whitefish market, of which Kallmark's ridge cod is about 7%, alongside close substitutes such as saithe and haddock from other countries. About 30% is sold fresh in Kallmark to fish shops and restaurants. The fishery is open: any owner of a registered vessel may fish ridge cod, and 290 vessels did so in 2024 (38 trawlers over 24 m, which land about 60% of the catch, and 252 coastal boats). Nearby fisheries for saithe and ling are open as well and are not covered by the Act. About 1,700 crew are paid by "lay": under the Fishermen's Share Agreement, a standard private contract used on about 80% of vessels, the crew together receive 45% of each trip's revenue after trip expenses (fuel, ice, bait, landing fees).

The bill was introduced by the government on 3 February 2026, with its allocation formula published, and passage was widely expected. It was passed on 14 October 2026 and takes effect on 1 January 2028.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Catch cap | `quota` | Landings of ridge cod by Kallmark vessels | Vessel owners | Total allowable catch of 40,000 tonnes a year for 2028 to 2032. From 2033, set each year by the Ministry of Fisheries "having regard to scientific advice". | Recreational fishing up to 10 fish a person a day, which may not be sold. |
| K2 Quota shares | Allocation of K1 (part of K1) | Shares of the annual catch | Vessel owners | The catch is divided into one million shares. On 1 January 2028, shares are given free to the registered owner of each vessel on 31 December 2027, in proportion to that vessel's recorded ridge cod landings in 2025, 2026 and 2027 together. Shares are permanent and may be sold; each year's tonnage may be leased. Transfers are registered with the Fisheries Directorate, with a fee of 1% of the price. Only owners of at least one registered vessel may hold shares. No owner, with affiliates, may hold more than 8% of all shares. A vessel that lands more than its owner's tonnage must lease the difference within 30 days, or the excess is forfeited and fined. | None |
| K3 Crew settlements | Rule on a private contract term (`contract`: the crew share agreement) | Deductions from trip revenue before the crew share | Vessel owners | "The cost of acquiring quota shall not be deducted as a trip expense in crew settlements." | None |
| K4 Monitoring and enforcement | Enforcement | K1, K2 | Fisheries Directorate | Ridge cod may be landed only at 13 designated sites (the three processing ports and ten small harbors), where it is weighed by dockside monitors whose fee (15 marks a tonne) the vessel owner pays. Observers on 10% of trips by vessels over 24 m; none on coastal boats. Discarding ridge cod above the minimum landing size is prohibited. Penalties: forfeiture of the catch, a fine of three times its value, and suspension of shares after a third offense. The Directorate's budget is raised by 18 million marks a year from the general budget. | None |

Existing rules (in force in the counterfactual too):

| Rule | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Vessel registration | Registration (not a `licensing_requirement` in effect: any seaworthy vessel is registered for 600 marks a year) | Commercial fishing vessels | Owners | Open to all. | None |
| R2 Minimum landing size | Rule on the good | Ridge cod under 35 cm | Vessel owners | Must be returned to the sea. | None |

Unclear provisions: U1, whether "the cost of acquiring quota" in K3 covers leasing a year's tonnage, or only buying shares. Reading U1-a: only purchases are covered, so lease payments may be deducted before the crew share. Reading U1-b: leases are covered too, so the owner pays them from the owner's side. The Directorate has not ruled, and the Act gives no example.

The counterfactual is Kallmark with an open fishery, no catch cap and the same existing rules. Without the Act, landings stay near 48,000 tonnes a year (A-1).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: prohibits exchanges of ridge cod beyond the cap between Kallmark fishers and their buyers | Yes: 40,000 tonnes is below the 48,000 tonnes landed without it (A-1). | EN-6 (in part; see section 7), CR-6, RS-3, RS-6, OC-4 |
| K2 | Triangular (part of K1): decides who holds the scarce right to land, and so who captures the gap that CR-6 opens. By CR-1, it adds options (to sell or lease a right) and transfers means (a free asset) to recipients, and attaches a cost (buying or leasing) to fishing for everyone else. | Yes | SB-4, CR-7a, CR-7c, CR-10a, RS-5, RS-8 |
| K3 | Triangular: sets a term of the existing crew share contract | Under U1-a, only when shares are bought; under U1-b, also when tonnage is leased | CR-5c, CR-9 (`contract`) |
| K4 | Binary: funded from the general budget (raised by 18 million marks, A-22) and from monitor fees paid by owners | Yes | OC-2, OC-3 |

The cap collects no revenue for the state. Against the counterfactual (an open fishery), the free allocation is not a transfer from taxpayers: there is no auction in the counterfactual whose revenue is forgone. Comparing it with an auctioned scheme would be comparing two versions of the policy (final check, item 3).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `vessel_owners.at_announcement` | Owners of vessels with ridge cod landings on 3 February 2026 | The landings history of their vessels becomes the claim to a future asset. |
| `vessel_owners.history` (`sellers.current`) | Owners fishing ridge cod in 2026 and 2027 | Each tonne landed in those years enlarges a permanent share. |
| `share_recipients` | Registered owners on 31 December 2027 of vessels with 2025 to 2027 history | Receive shares free. |
| `operators.high_cost`, `operators.low_cost` | Vessel owners with high or low costs per tonne landed | Can fish their tonnage, lease more, or lease theirs out. |
| `holders.non_fishing` | Recipients who stop fishing but keep their shares | Must keep a registered vessel to hold shares. |
| `vessel_owners.large` | The few firms near the 8% holding limit | Limited in how many more shares they may buy. |
| `share_buyers.later` | Anyone who buys shares after 1 January 2028 | Pay a price that carries the expected yield. |
| `entrants.prospective` (`sellers.prospective`) | People who would start fishing ridge cod, many of them former crew | Before 2028, can enter and earn history; after, must buy or lease shares. |
| `crew` | Share-paid crew on ridge cod vessels | Fewer berths; their pay depends on the lay and on U1. |
| `processors` (`input_suppliers` to the export market) | The four plants | Less ridge cod to process; may not hold shares without a vessel. |
| `workers.processing` | Plant employees | Less throughput. |
| `ports.minor` | The ten small harbors and their landing services | Landings may move to the processing ports. |
| `ports.major` | Brennhavn, Skelby, Tornhavn | Fewer tonnes in total, a larger share of them. |
| `sellers.complements` | Fuel, ice, chandlery, boat repair and boatbuilding | Demand follows days at sea and the number of vessels. |
| `buyers.fresh_domestic` | Fish shops, restaurants and households in Kallmark | Less fresh ridge cod. |
| `buyers.regional` | Buyers in the North Basin market | Less Kallmark ridge cod among many substitutes. |
| `fishers.other_species` (`sellers.substitutes`) | Fishers of saithe and ling | Vessels and crew leaving ridge cod may join them. |
| `officials.enforcement`, `taxpayers` | Fisheries Directorate and its funders | Monitoring, observers and the share register. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `vessel_owners.history`, `buyers.fresh_domestic`, `buyers.regional` | `quantity_traded` (ridge cod landed and sold, 2028 on) | decrease | short (from 2028) | CR-6, EN-6, OC-4 | A-1, A-2 |
| C-2 | `share_recipients` | `asset_value` (quota shares, and before 2028 the expected claim to them) | increase | short (from the announcement) | CR-7c, CR-10c, SB-4 | A-1, A-2, A-3 |
| C-3 | all vessels fishing ridge cod | `price_paid` (annual lease of a tonne of quota) | increase | short (from 2028) | CR-6, CR-7b | A-1, A-2 |

C-1 is what the Act states: 8,000 tonnes fewer landed than without it. Both sides of each prevented sale lose the gain they expected (CR-5a, OC-4).

C-3 is where CR-6 puts the pressure. At the prevailing price of ridge cod, fishers would land 48,000 tonnes; the cap allows 40,000. The price of ridge cod in the export market hardly moves, because Kallmark's ridge cod is a small part of a market with close substitutes (A-17, section 7). What rations the fixed quantity is therefore not the price of the fish but the price of the right to land it: the gap between the price of fish and what it costs the vessel that would land the 40,000th tonne. Without the Act no such right exists and landing is free; the lease price rises from nothing. C-2 is the same gap capitalized (CR-7c, CR-10c). Every lease payment is a receipt to the holder who leases out (CR-8b); that income stream is what C-2 capitalizes, so the receiving side of C-3 is recorded there. Because the right is tradable, a legal price absorbs the pressure, and the illegal margins in section 5 are used only where their own premises hold.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `vessel_owners.history` | `quantity_traded` (ridge cod landings, 2026 and 2027) | increase | short (the announcement window) | RS-8, CR-10a, CR-4 | A-4 |
| C-5 | `vessel_owners.history` | `investment_target` (vessels, engines and gear, 2026 and 2027) | increase | short (the announcement window) | CR-10a, CR-7a | A-4 |
| C-6 | `entrants.prospective` | `entry_rate` (into ridge cod fishing, 2026 and 2027) | increase | short (the announcement window) | CR-10a, CR-4 | A-4, A-5 |
| C-7 | `entrants.prospective` | `entry_rate` (into ridge cod fishing, 2028 on) | decrease | medium | EN-6, SB-4, CR-7c | A-1, A-2 |
| C-8 | `vessel_owners.at_announcement` | `asset_value` (vessels carrying 2025 to 2027 landings history, during 2026 and 2027) | increase | short (from the announcement) | CR-7c, CR-10c, SB-4 | A-3, A-5 |
| C-9 | `operators.high_cost` | `number_of_sellers` (vessels landing ridge cod) | decrease | medium | CR-7a, CR-4, RS-6 | A-1, A-6 |
| C-10 | `vessel_owners.history` | `capital_stock_target` (vessels in the ridge cod fishery) | decrease | long | CR-7a, CR-10b, TS-1 | A-1, A-6, A-7 |
| C-11 | `holders.non_fishing` | `units_held_vacant` (registered vessels kept idle only to hold shares) | increase | medium | CR-1, CR-4 | A-6, A-24 |
| C-12 | `vessel_owners.history` | `quality_per_unit` (average size grade of landed ridge cod) | increase | short | CR-4c, CR-6, CR-4 | A-1, A-9, A-10 |
| C-13 | `vessel_owners.history`, `processors`, `buyers.fresh_domestic` | `quantity_traded` (small-grade ridge cod landed) | decrease | short | CR-4c, CR-6, CR-4 | A-1, A-9, A-10 |
| C-14 | `vessel_owners.history` | `informal_activity` (ridge cod landed unrecorded and sold for cash) | increase | short | CR-6, RS-3 | A-1, A-11 |
| C-15 | `vessel_owners.large` | `reclassification` (shares held through nominees and nominally separate companies to stay under 8%) | increase | medium | RS-5 | A-6, A-13 |
| C-16 | `processors` | `reclassification` (processors buying registered vessels in order to hold shares) | increase | medium | RS-5, CR-4 | A-14 |
| C-17 | `share_recipients`, `processors`, `crew` | `lobbying_effort` (recipients to keep the cap tight at the 2033 review and to resist reallocation; processors for a right to hold shares; crew for crew shares or a ruling on U1) | increase | medium | RS-7 | A-1, A-15 |

**The race for history (C-4 to C-6, C-8).** Two of the three base years lie after the announcement. From February 2026, a tonne landed in 2026 or 2027 brings both its sale price and a permanent claim on part of every future year's catch (CR-10a). Owners fish more in those years than they would have (CR-4, x: land a tonne now, y: do not), bring idle vessels back and upgrade engines and gear (C-5). New owners enter to earn some history (C-6). These are timing effects on actions that also take place without the Act, so each window is signed against the counterfactual (`02_ontology.md`, 2.5): landings, investment and entry rise in 2026 and 2027 (C-4 to C-6) and fall from 2028 (C-1, C-7, C-10). Unlike most RS-8 cases, the window's rise is not mainly moved from later years; it is added, because the later years are capped anyway. Section 9 records what the race uses up.

**Who captures the asset (C-2, C-8).** CR-7c says that an asset the policy creates is captured by whoever receives it at creation, and that a change in expected yield is captured by whoever owns the asset when the change becomes expected. Here the two point to different people. The shares are created on 1 January 2028, but the claim to them rides on each vessel's landings history, and vessels can be sold in between. From the announcement, a vessel with history sells for more (C-8), rising as passage becomes more likely and again on 14 October 2026. An owner who sells such a vessel in 2027 is paid for the shares the buyer will receive; the buyer, who receives the shares at creation, has paid for them. So the gain from the allocation settles on the owners of vessels with history as the scheme became expected, not on the recipients as such (section 7). Part of it is also used up in the race (C-4, C-5, section 9).

**Consolidation (C-9 to C-11).** Once rights are tradable, a tonne of quota yields its holder the gap between the fish price and the cost of landing it. An owner whose costs are high earns more by leasing or selling the right to an owner whose costs are low than by fishing it (CR-4, x: fish one's own tonnage, y: lease it out). Rights move to the lowest-cost vessels until the lease price equals the margin of the marginal user (CR-7a). Fewer vessels fish (C-9), and as the surplus is sold or scrapped, the fleet shrinks (C-10, TS-1). Holders who stop fishing must still own a registered vessel to keep their shares (K2), so some keep one tied up only for that purpose (C-11, CR-1: the condition attaches a cost to the option of leaving the trade entirely).

**High-grading (C-12, C-13).** The quota counts tonnes, but a tonne of large ridge cod sells for more than a tonne of small ones (A-9). Each tonne of tonnage is now a scarce means with a price (C-3); landing a small fish uses up tonnage that a large one could have filled (CR-3). Applying CR-4c to the unit of the constraint, the tonne of quota, the lowest-valued use of it (small fish above the minimum size) is the first given up: some are discarded at sea and replaced with larger ones. That breaks the discard ban (K4), so it is also CR-4 with x: comply, y: violate. Observers ride only 10% of trawler trips and no coastal boat trips (A-10), so the expected penalty is small. The result is a larger average size landed (C-12) and fewer small fish landed (C-13). Fish discarded are not traded at all and have no variable (Gaps found, d).

**Unreported landings (C-14).** CR-6 also opens the margin of exchanges outside the rule: a tonne landed unrecorded saves the lease price. Monitors weigh at all 13 sites, but the ten small harbors are staffed at scheduled hours only (A-11). RS-10 would apply to that trade, but its search-cost and quality conclusions add little for fish sold to known local buyers, and are not separately reported.

**Reclassification (C-15, C-16).** The 8% cap binds for a few of the largest firms (A-13), which then hold shares through relatives' or nominally separate companies (RS-5). Processors may not hold shares unless they own a vessel; some buy one to qualify, to secure supply for their plants (A-14).

Not reported: landing ridge cod as uncapped saithe or ling (RS-5, RS-3); A-12 is below the cut-off (p = 0.35), because the species are easy to tell apart at the dockside.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-18 | `crew` | `employment`, `hours_worked` (berths and days at sea in ridge cod, 2028 on) | at_least_one_decrease | medium | CR-9, RS-6 | crew labor `input_to` ridge cod landings; `contract` (Fishermen's Share Agreement) | A-1, A-6 |
| C-19 | `crew` | `employment`, `hours_worked` (berths and days at sea in ridge cod, 2026 and 2027) | at_least_one_increase | short (the announcement window) | CR-9, RS-8 | as C-18 | A-4 |
| C-20 | `fishers.other_species` | `quantity_supplied` (landings of saithe and ling) | increase | short to medium | CR-7a, CR-9, RS-6 | vessels and crew are means usable in either fishery: ridge cod and saithe or ling fishing `same_market_other_segment`, partial | A-1, A-7 |
| C-21 | `buyers.fresh_domestic` | `price_paid` (fresh ridge cod in Kallmark) | increase | short | CR-6, EN-6 | fresh local landings and imported or frozen whitefish: `substitute`, partial | A-1, A-2, A-16 |
| C-22 | `vessel_owners.history` | `net_price_received` (ex-vessel price of ridge cod sold to the plants) | increase | short to medium | CR-9, CR-6, CR-7b | ridge cod `input_to` processed fillets | A-1, A-17, A-18 |
| C-23 | `processors` | `quantity_supplied` (processed ridge cod) | decrease | short | CR-9 | as C-22 | A-1, A-2 |
| C-24 | `processors` | `return_on_capital` | decrease | medium | CR-7b, CR-9 | as C-22 | A-1, A-18 |
| C-25 | `workers.processing` | `employment`, `hours_worked` | at_least_one_decrease | medium | CR-9, RS-6 | labor `input_to` processing | A-1, A-19 |
| C-26 | `ports.minor` | `quantity_traded` (landing and harbor services at the ten small harbors) | decrease | medium | CR-9, CR-7a | harbor services `complement` to landings | A-6, A-20 |
| C-27 | `sellers.complements` | `quantity_complement` (fuel, ice, gear, repair and boatbuilding, 2026 and 2027) | increase | short (the announcement window) | RS-12, CR-9 | fuel, ice, gear and repair `complement` to days at sea and vessels | A-4 |
| C-28 | `sellers.complements` | `quantity_complement` (fuel, ice, gear, repair and boatbuilding, 2028 on) | decrease | medium | RS-12, CR-9 | as C-27 | A-1, A-6 |
| C-29 | `vessel_owners.history` (owners selling surplus vessels) | `asset_value` (fishing vessels without shares, 2028 on) | decrease | medium | RS-13, CR-7c | ridge cod vessels and vessels for other fisheries or for sale abroad: `same_market_other_segment`, partial | A-6, A-21 |
| C-38 | `processors` (owners) | `asset_value` (processing plants) | decrease | short (from the announcement) | CR-7c, CR-10c | as C-22 | A-1, A-3, A-18 |

C-18 and C-19: the crew's labor is an input to landings, and berths follow vessels (CR-9 through the share contract). Fewer vessels fishing fewer tonnes (C-1, C-9) means fewer berths or fewer days, at least one; during the race, more of either. These are per-window signs of the same group.

C-20: the vessels and crew that leave ridge cod (C-9, C-18) move to the next-best use open to them, which for many is the open saithe and ling fisheries (CR-7a, A-7). What this does to the price of saithe and ling is ambiguous (section 7). How it affects those stocks is outside scope.

C-22 to C-24: the plants' output is priced in the North Basin market (A-17), but their raw fish is landed in Kallmark. With 8,000 fewer tonnes and plants that cannot easily process anything else (A-18, A-19), the plants compete harder for what is landed, and the ex-vessel price rises toward the export price less processing costs (CR-6, CR-9). The plants' capital is specific, so the lasting loss from lower throughput settles on its owners (CR-7b). This also raises the gap that C-3 measures. The plants' lower expected yield is capitalized when the cap becomes expected, so their owners at the announcement bear it, not later buyers of the plants (C-38, CR-7c).

C-26: consolidation favors the vessels with the lowest cost per tonne, which are mostly larger vessels landing at the processing ports (A-20), so the small harbors lose landings. The processing ports' own landings combine two opposite chains (section 7).

C-29: after 2028, vessels leaving the fishery are sold into other fisheries or abroad. Unless that demand absorbs them at unchanged prices (A-21), the price of a vessel without shares falls. This is a different asset from C-8 (a vessel with a claim to shares before 2028), so the two are not combined.

Stopping points: C-20 leads to buyers of saithe and ling (depth 3, section 7) and stops there. Buyers in the North Basin market are diffuse bystanders at depth 2 whose price is not signed (section 7). Lenders financing share purchases are a new market but add no sign beyond C-2 and C-35; stopped. RS-11 (lock-in) was checked: a share is transferable, so leaving the fishery does not forfeit it; the only tie is K2's vessel condition, recorded as C-11. RS-9 does not apply: no buyer changes where they shop.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.regional`, `price_paid` (ridge cod and whitefish in the North Basin market), short | 8,000 fewer tonnes offered (C-1, CR-6). | None. | None needed | **Not signed.** Kallmark's ridge cod is about 7% of a market with close substitutes (A-17), so the price is held near the price of those substitutes; a rise needs a premise that buyers treat ridge cod as distinct, which the analysis does not have. EN-6's "`price_paid` increase" does not carry over to a capped good priced in a wider market (Gaps found, b and c). C-21 covers the partly insulated fresh segment only. |
| `crew`, `wage_rate` (pay per day at sea), medium | The share agreement pays a fixed 45% of trip revenue, and tonnage moves to vessels that land more per day (C-9); until the lay is renegotiated, pay per day on those vessels rises (A-6, A-26). | Fewer berths (C-18), and crew skills are specific with few local alternatives, so the lasting loss settles partly on crew (CR-7b, A-8). Under U1-a, lease payments are deducted before the crew share, so crew on vessels that lease tonnage bear part of the lease price (C-3), and crew mobility between vessels spreads this (CR-7a). | None | **ambiguous** under both readings (C-30). U1-a adds weight to the (−) chains; it does not decide the sign. Decided by how far tonnage concentrates on high-catch vessels compared with the fall in berths, and by how quickly lays are renegotiated (CR-5c). |
| `fishers.other_species` and their buyers, `price_substitute` (saithe and ling, ex-vessel), short to medium | Fresh buyers who find ridge cod dearer (C-21) turn to saithe and ling (RS-16, A-25). | Vessels and crew displaced from ridge cod add landings of saithe and ling (C-20, RS-13, A-7). | None | **ambiguous** (C-36). The export share of saithe and ling is also priced in the wider market (A-17), which damps both chains. |
| `ports.major`, `quantity_traded` (landing services), medium | Landings move from small harbors to the processing ports (C-26, A-20). | Total landings fall (C-1). | None | **ambiguous** (C-37). |
| Who captures the value of the shares, short to medium | Owners of vessels with history when the scheme became expected: through vessel prices (C-8) if they sold, through shares (C-2) if they kept the vessel. | Part of the value is used up in the race for history (C-4, C-5, section 9; CR-7a, CR-8c), and buyers of vessels in 2026 and 2027 paid for the claim they later received (C-8). Later buyers of shares pay the capitalized price (C-35). | CR-7c, CR-10c | **Owners at the announcement capture the value of the claim, less what the race uses up; recipients who bought their vessels in the window, and later buyers of shares, gain or lose only from changes after they bought** (for example the cap set at the 2033 review). Crew, who receive no shares (CR-1: no operation adds to their means), capture none of it directly. |
| `share_recipients`, their position by their own ranking, short to long | A free asset (C-2). | The race costs (C-5, section 9), the cap on their own landings (C-1), monitoring fees (C-31). | DM-3 | **Not signed.** One-time race costs against a lasting asset are ambiguous by design (DM-3). Those who raced expected the gain to be worth it (CR-2). |

Per-window signs that are not combined, because they are different windows (CR-12g): landings (C-4, C-1), investment (C-5, C-10), entry (C-6, C-7), crew berths (C-19, C-18) and complements (C-27, C-28).

## 8. Time structure

- **Announcement to the end of 2027 (23 months).** The value of the claim appears in vessel prices first (C-8), in steps as passage becomes likely and then certain. The race for history (C-4 to C-6, C-19, C-27) runs through 2026 and 2027, and is strongest in 2027, the last base year, when there is no later year to which effort could be shifted. In this window the cap does not yet bind, so landings rise above the counterfactual.
- **2028.** The cap binds at once (C-1). The race leaves more vessels and gear than the capped fishery needs, so consolidation (C-9) starts from a larger fleet than without the Act. The lease market (C-3) appears in the first season.
- **Consolidation is gradual.** Tonnage moves by lease within a year, but vessels leave the fleet as they are sold abroad, moved to other fisheries or not replaced (C-10, TS-1); the fall in vessels and berths grows over the medium to long horizon. Small harbors lose landings as this proceeds (C-26).
- **The 2033 review.** From 2033 the Ministry sets the catch each year. Share values (C-2) depend on what holders expect it to decide (A-3, CR-10a); lobbying (C-17) rises before it. A higher catch from 2033 would lower share values and fall on whoever holds shares then, including buyers after 2028 (CR-7c).
- **U1 and the timing of crew effects.** Under U1-a, lease deductions reach crew pay from the first leased tonne in 2028; under U1-b, any shift of the lease cost toward crew must wait for the lay to be renegotiated (CR-5c), which under the standard agreement happens at the start of each season.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-31 | `vessel_owners.history`, `holders.non_fishing` | `compliance_cost` (monitor fees, logbooks, share register and transfer fees, leasing to cover overages) | increase | What that time and money would otherwise have bought. | OC-2, CR-8c |
| C-32 | `officials.enforcement` | `enforcement_cost` | increase | Dockside monitoring at 13 sites, observers, the share register. | OC-3 |
| C-33 | `taxpayers` | `resources_available_other_uses` | decrease | What the 18 million marks a year would otherwise have funded. | OC-3, OC-1 |
| C-34 | `share_recipients` (those who sell shares) | `resources_available_other_uses` | increase | Nothing given up: the sale price is a receipt (CR-8b). | OC-7, CR-8b |
| C-35 | `share_buyers.later` | `resources_available_other_uses` | decrease | The other purchases or investments the price of the shares would have bought; the matching side of C-34. | OC-7, CR-8b |

The race for history (C-4, C-5) also uses resources whose only purpose is to enlarge a share: fuel, labor and vessels deployed in 2026 and 2027 beyond what the fish caught were worth to their owners on their own (CR-8c). The fish landed are real output; the vessels and gear bought for the race and idle from 2028 (C-5 against C-10) are the clearest part of the cost. It is not recorded as its own consequence because no variable measures effort spent beyond the output it yields (Gaps found, d).

The 8,000 tonnes not landed (C-1) are the prevented exchanges (OC-4): fishers who would have sold them and buyers who would have bought them both lose the gain each expected.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the Act, landings would stay well above 40,000 tonnes a year, so the cap binds from 2028. | binding | 0.9 | Landings of 48,000 tonnes on average in 2022 to 2024; fleet capacity. | Almost every consequence from 2028 fails. |
| A-2 | Landings are recorded and overages enforced at the designated sites. | enforcement | 0.8 | Weighing at every site; forfeiture and triple fines; share suspension. | C-1 and C-3 shrink; C-14 grows. |
| A-3 | Owners expect the bill to pass and the shares to keep their value past the 2033 review. | expectations | 0.7 | Government sponsorship; political strength of the owners' association; the review's terms. | C-2 and C-8 are smaller. |
| A-4 | Owners know the formula from the introduction of the bill, expect passage, and have idle vessels or spare capacity to land more in 2026 and 2027. | expectations | 0.8 | Formula published with the bill; laid-up vessels; spare days at sea. | C-4 to C-6, C-19 and C-27 are not reported. |
| A-5 | A vessel's history passes to its buyer, and buyers price it in. | expectations | 0.85 | K2 allocates by vessel to the owner on 31 December 2027; vessel brokers' practice. | C-8 is not reported; history is captured by recipients instead. |
| A-6 | Costs per tonne differ materially among vessels, and transfers are not blocked for most owners by the 8% limit. | other | 0.8 | Fuel use and catch per day by vessel class; current holdings would be far below 8% for all but a few. | C-9 to C-11, C-18 and C-26 to C-29 weaken. |
| A-7 | Vessels and crew have other uses: the open saithe and ling fisheries, or sale abroad. | alternative_uses | 0.7 | Vessels that already fish several species; the second-hand vessel market. | C-10 and C-20 weaken; the loss falls more on vessel owners and crew. |
| A-8 | Crew skills are specific to fishing, and coastal towns offer few other jobs. | mobility | 0.6 | Local labor market data; crew age and training. | The (−) chain on crew pay in section 7 weakens. |
| A-9 | Large ridge cod sell for more per kilo than small ones above 35 cm, and the gear catches mixed sizes. | other | 0.85 | Size-grade price lists at auction; selectivity of the gear. | C-12 and C-13 are not reported. |
| A-10 | With observers on 10% of trawler trips and none on coastal boats, discarding is rarely detected. | enforcement | 0.75 | K4; the size of the area patrolled. | C-12 and C-13 are smaller. |
| A-11 | The ten small harbors are monitored only at scheduled hours, so some landings go unrecorded. | enforcement | 0.55 | Staffing plans; night landings in the open fishery. | C-14 is not reported. |
| A-12 | Ridge cod is landed as saithe or ling on a meaningful scale. | enforcement | 0.35 | The species are easy to tell apart at the dockside. | Below the cut-off; not reported. |
| A-13 | The 8% limit binds for a few of the largest firms. | binding | 0.55 | Current shares of the largest trawler firms; their stated plans. | C-15 is not reported. |
| A-14 | Processors value secure supply enough to buy a vessel in order to hold shares. | other | 0.6 | Vertical integration in comparable fisheries; price of a small registered vessel compared with the value of shares. | C-16 is not reported. |
| A-15 | Recipients, processors and crew can organize at a cost below their stake. | other | 0.85 | The owners' association; four processors; the crew union. | C-17 is not reported. |
| A-16 | Fresh local ridge cod is only partly substitutable with imported or frozen whitefish. | substitutability | 0.7 | Restaurant menus; the freshness premium at the fish auction. | C-21 weakens; the fresh price follows the export price. |
| A-17 | Kallmark's ridge cod is a small part of the North Basin market, with close substitutes. | substitutability | 0.8 | Market shares; price correlation between ridge cod, saithe and haddock. | The export price rises with the cap, and part of the gap goes to fishers through the fish price rather than through the lease price. |
| A-18 | The plants are specific to ridge cod and compete for the fish landed, while their output is priced in the wider market. | alternative_uses | 0.6 | Plant equipment; the number of buyers at each port. | C-22 and C-24 weaken. |
| A-19 | The plants cannot fully replace ridge cod with other species. | other | 0.7 | Filleting lines are set for ridge cod; volumes of other species landed nearby. | C-25 weakens. |
| A-20 | Consolidation favors larger vessels, which land at the processing ports. | other | 0.6 | Costs per tonne by vessel class; where trawlers land. | C-26 is not reported; the major-port row in section 7 becomes a decrease. |
| A-21 | The surplus vessels are not absorbed by other fisheries and buyers abroad at unchanged prices. | other | 0.6 | Second-hand vessel prices; size of the foreign market for such vessels. | C-29 is not reported. |
| A-22 | The Directorate's budget is raised by the stated 18 million marks. | revenue_use | 0.9 | K4. | C-33 is not reported; other fisheries work falls instead (OC-3, fixed budget). |
| A-23 | Some recipients sell shares, realizing their value. | other | 0.8 | Retirements among owners; share trading in comparable schemes. | C-34 and C-35 are not reported. |
| A-24 | For some holders who stop fishing, keeping a minimal registered vessel costs less than what they gain by holding the shares rather than selling. | other | 0.7 | Registration fee of 600 marks; mooring costs; the expected rise in share values. | C-11 is not reported. |
| A-25 | Fresh-fish buyers turn to saithe and ling when ridge cod costs more. | substitutability | 0.7 | Menus; fishmongers' sales. | The (+) chain on `price_substitute` in section 7 weakens. |
| A-26 | The lay stays at 45% for at least a season after tonnage concentrates. | other | 0.75 | The standard agreement is renegotiated by season. | The (+) chain on crew pay in section 7 is shorter. |

## 11. Report

**The policy.** Kallmark caps the annual catch of ridge cod at 40,000 tonnes, about a sixth below what its boats now land, and divides the cap into permanent, tradable shares. The shares are given free, on 1 January 2028, to the owners of vessels in proportion to their landings in 2025 to 2027. Only vessel owners may hold shares, and no one may hold more than 8%. The Act was introduced in February 2026, so two of the three base years came after it was announced.

**Visible consequences.** Fewer ridge cod landed (C-1), and a valuable asset given to boat owners (C-2).

**Invisible consequences.**
- *The right to fish gets a price.* Because Kallmark's ridge cod is a small part of a wider market, the price of the fish hardly moves (section 7). What rations the catch is the price of leasing a tonne of quota, which did not exist before (C-3).
- *The race for history.* Once the formula was published, each tonne landed in 2026 and 2027 earned a permanent claim, so owners landed more, invested in vessels and gear, and newcomers entered in those two years (C-4 to C-6), with more work for crew and suppliers then (C-19, C-27) and less after (C-18, C-28). Some of the asset's value is used up in this race (section 9).
- *Who captures the asset.* The claim to shares travelled with the vessels, so vessels with history sold for more from the announcement (C-8). The owners at that time captured the value; buyers of those vessels paid for it, and later buyers of shares pay the full price (section 7, C-35). Crew receive no shares.
- *Consolidation.* Quota moves to the boats that can land it most cheaply, so fewer boats fish (C-9) and the fleet shrinks over time (C-10). Some owners who stop fishing keep a boat tied up only to keep their shares (C-11). There are fewer berths or days at sea for crew (C-18), and new fishers must buy or lease shares (C-7). Whether crew pay per day rises or falls is ambiguous, and depends in part on how the crew-settlement rule is read (section 7).
- *Fishing behavior.* Fishers throw back smaller fish to fill their tonnage with larger, dearer ones (C-12, C-13), and some landings at small harbors go unrecorded (C-14). The largest firms hold shares through others to stay under the limit (C-15), and processors buy boats in order to hold shares (C-16).
- *Processors and ports.* The plants process less (C-23) and pay more for the fish they get (C-22), so their owners earn less on their plants (C-24) and the plants are worth less from the announcement (C-38), with fewer jobs or hours for plant workers (C-25). Small harbors lose landings to the processing ports (C-26); suppliers of fuel, ice and repairs sell less from 2028 (C-28). Fresh ridge cod costs more in Kallmark (C-21). Displaced boats move into the saithe and ling fisheries (C-20). Surplus vessels sell for less (C-29).
- *Costs.* Owners pay for monitoring and the share register (C-31); the state pays for enforcement (C-32, C-33). Lobbying grows before the 2033 review (C-17).

**Ambiguous effects.** Crew pay per day at sea; the price of saithe and ling; landings at the processing ports; whether recipients are better off once the race's costs are counted. Not signed: the export price of ridge cod.

**Key conditions.** The cap binds (A-1, p = 0.9). The capture story depends on vessel sales carrying the history (A-5, p = 0.85) and on expectations about the 2033 review (A-3, p = 0.7). Consolidation rests on real cost differences among vessels (A-6, p = 0.8). Unrecorded landings rest on weak monitoring at small harbors (A-11, p = 0.55).

**What this analysis cannot say.** How large any effect is; whether recipients' gains outweigh crew, processor, small-harbor and buyer losses; how much of the asset's value the race used up; what the cap does to the ridge cod stock or to the saithe and ling stocks, and so whether later catches would be higher or lower than without it (environmental effects are out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | vessel_owners.history, buyers.fresh_domestic, buyers.regional | quantity_traded (ridge cod, 2028 on) | decrease | short | visible | B | CR-6, EN-6, OC-4 | A-1, A-2 |
| C-2 | share_recipients | asset_value (quota shares) | increase | short | visible | B | CR-7c, CR-10c, SB-4 | A-1, A-2, A-3 |
| C-3 | all vessels fishing ridge cod | price_paid (annual quota lease) | increase | short | invisible | B | CR-6, CR-7b | A-1, A-2 |
| C-4 | vessel_owners.history | quantity_traded (landings, 2026–2027) | increase | short | invisible | B | RS-8, CR-10a, CR-4 | A-4 |
| C-5 | vessel_owners.history | investment_target (2026–2027) | increase | short | invisible | B | CR-10a, CR-7a | A-4 |
| C-6 | entrants.prospective | entry_rate (2026–2027) | increase | short | invisible | B | CR-10a, CR-4 | A-4, A-5 |
| C-7 | entrants.prospective | entry_rate (2028 on) | decrease | medium | invisible | B | EN-6, SB-4, CR-7c | A-1, A-2 |
| C-8 | vessel_owners.at_announcement | asset_value (vessels with history, 2026–2027) | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-3, A-5 |
| C-9 | operators.high_cost | number_of_sellers (vessels landing ridge cod) | decrease | medium | invisible | B | CR-7a, CR-4, RS-6 | A-1, A-6 |
| C-10 | vessel_owners.history | capital_stock_target (vessels) | decrease | long | invisible | B | CR-7a, CR-10b, TS-1 | A-1, A-6, A-7 |
| C-11 | holders.non_fishing | units_held_vacant (idle registered vessels) | increase | medium | invisible | B | CR-1, CR-4 | A-6, A-24 |
| C-12 | vessel_owners.history | quality_per_unit (size grade landed) | increase | short | invisible | B | CR-4c, CR-6, CR-4 | A-1, A-9, A-10 |
| C-13 | vessel_owners.history, processors, buyers.fresh_domestic | quantity_traded (small-grade fish landed) | decrease | short | invisible | B | CR-4c, CR-6, CR-4 | A-1, A-9, A-10 |
| C-14 | vessel_owners.history | informal_activity (unrecorded landings) | increase | short | invisible | B | CR-6, RS-3 | A-1, A-11 |
| C-15 | vessel_owners.large | reclassification (nominee holdings) | increase | medium | invisible | B | RS-5 | A-6, A-13 |
| C-16 | processors | reclassification (vessels bought to hold shares) | increase | medium | invisible | B | RS-5, CR-4 | A-14 |
| C-17 | share_recipients, processors, crew | lobbying_effort | increase | medium | invisible | B | RS-7 | A-1, A-15 |
| C-18 | crew | employment, hours_worked (2028 on) | at_least_one_decrease | medium | invisible | B | CR-9, RS-6 | A-1, A-6 |
| C-19 | crew | employment, hours_worked (2026–2027) | at_least_one_increase | short | invisible | B | CR-9, RS-8 | A-4 |
| C-20 | fishers.other_species | quantity_supplied (saithe, ling) | increase | short–medium | invisible | B | CR-7a, CR-9, RS-6 | A-1, A-7 |
| C-21 | buyers.fresh_domestic | price_paid (fresh ridge cod) | increase | short | invisible | B | CR-6, EN-6 | A-1, A-2, A-16 |
| C-22 | vessel_owners.history | net_price_received (ex-vessel) | increase | short–medium | invisible | B | CR-9, CR-6, CR-7b | A-1, A-17, A-18 |
| C-23 | processors | quantity_supplied (processed ridge cod) | decrease | short | invisible | B | CR-9 | A-1, A-2 |
| C-24 | processors | return_on_capital | decrease | medium | invisible | B | CR-7b, CR-9 | A-1, A-18 |
| C-25 | workers.processing | employment, hours_worked | at_least_one_decrease | medium | invisible | B | CR-9, RS-6 | A-1, A-19 |
| C-26 | ports.minor | quantity_traded (landing services) | decrease | medium | invisible | B | CR-9, CR-7a | A-6, A-20 |
| C-27 | sellers.complements | quantity_complement (2026–2027) | increase | short | invisible | B | RS-12, CR-9 | A-4 |
| C-28 | sellers.complements | quantity_complement (2028 on) | decrease | medium | invisible | B | RS-12, CR-9 | A-1, A-6 |
| C-29 | vessel_owners.history | asset_value (vessels without shares, 2028 on) | decrease | medium | invisible | B | RS-13, CR-7c | A-6, A-21 |
| C-30 | crew | wage_rate (pay per day at sea) | ambiguous | medium | invisible | B | CR-5c, CR-7a, CR-7b, CR-12b | A-6, A-8, A-26 |
| C-31 | vessel_owners.history, holders.non_fishing | compliance_cost | increase | short | invisible | A | OC-2, CR-8c | none |
| C-32 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-33 | taxpayers | resources_available_other_uses | decrease | short | invisible | B | OC-3, OC-1 | A-22 |
| C-34 | share_recipients (sellers) | resources_available_other_uses | increase | medium | invisible | B | OC-7, CR-8b | A-23 |
| C-35 | share_buyers.later | resources_available_other_uses | decrease | medium | invisible | B | OC-7, CR-8b | A-23 |
| C-36 | fishers.other_species, buyers of saithe and ling | price_substitute (saithe, ling) | ambiguous | short–medium | invisible | B | RS-16, RS-13, CR-12b | A-7, A-25 |
| C-37 | ports.major | quantity_traded (landing services) | ambiguous | medium | invisible | B | CR-9, CR-12b | A-6, A-20 |
| C-38 | processors (owners) | asset_value (processing plants) | decrease | short | invisible | B | CR-7c, CR-10c | A-1, A-3, A-18 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12. The near-misses: the race for history is CR-10a with CR-4 and CR-7a; high-grading is CR-4c applied to the unit of the quota; the idle vessels kept to hold shares are CR-1 and CR-4. No step was marked `GAP`.

**(b) Unclear core rules.**
1. *CR-6, fixed quantity with a free price.* The clause says that "the price then rises to ration the fixed quantity". Here the capped good is sold in a wider market where its price hardly moves (A-17), so what rations the cap is the price of the right to land (C-3), not the price of the fish. The pressure is the gap between the price of the good and the cost of the marginal capped unit. The clause's parenthesis ("the value of the permission") points the right way, but read literally it predicts the export price rise that section 7 declines to sign. Proposed wording: "the full price of obtaining the good, or of the right to supply it, rises".
2. *CR-6, the group of margins.* CR-6 says to record the open margins as a group with `at_least_one_increase` when there are no premises per margin. When the policy makes the permission itself tradable, its price is a legal margin that can absorb all the pressure, so "at least one margin is used" is satisfied by the lease price alone, and says nothing about unrecorded landings, discarding or misreporting. The rule should say that a tradable right is one of the margins, and that the illegal margins then each need their own premise (as C-12 to C-14 do here).
3. *CR-7c, who captures a created asset.* CR-7c says both that a created asset "is captured by whoever receives it at creation" and that a change in expected yield is captured "by whoever owns [the asset] when the change becomes expected". When the claim to the future asset rides on another, tradable asset (here, a vessel's landings history), the two disagree, and the second governs (C-8): recipients who bought vessels in the window paid for their shares. Proposed addition: "where the claim to a created asset can be bought before creation, its value is captured by whoever holds the claim when the asset becomes expected".
4. *CR-7c and allocation by action.* Where receipt depends on actions taken after the announcement (landings in the base years), part of the asset's value is spent obtaining it (CR-7a, CR-8c), so "captured at creation" overstates the recipients' net gain. CR-7c should cross-refer CR-7a for this case.
5. *CR-4c, units.* CR-4c says the unit is "the unit of the end served". High-grading needs the unit of the constraint instead (a tonne of quota, which can be filled with fish of different value). A sentence saying that when a policy rations a means in its own units, the actor gives up the lowest-valued use of each unit of that means, would make the move explicit.

**(c) Missing patterns.**
1. *Allocation by history (proposed EN-12).* If a policy will allocate a valuable right in proportion to an activity measured over a base period that runs after the announcement, then in the window: the activity, investment in it and entry into it increase, compared with the counterfactual; afterwards they fall as the right binds; part of the right's value is used up in the race, and recipients' net gain is the value less those costs. Assumes: actors know the formula and can expand (`expectations`, `alternative_uses`). Derivation: CR-10a (a future payoff alters present choices), CR-4 (x: act in the window, y: do not), CR-7a (means move into the race until its marginal yield equals its cost), CR-8c (the race's resources are used up). It differs from RS-8 because the window's activity is added, not moved.
2. *A cap on output priced in a wider market (proposed EN-6 Unless clause, or a new pattern).* If a quota caps output whose price is set in a wider market with close substitutes, then `price_paid` for the good is not signed; the gap appears instead as the price of the right (`asset_value`, lease price) and, for inputs specific to the capped output, as a lower return to their owners. Derivation: CR-6 (fixed quantity), CR-7b (the gap settles on the scarce right), CR-9 for inputs. EN-6's "`price_paid` increase" overclaims in this case.
3. *Physical-unit quota on heterogeneous output (proposed RS-17).* If a quota, tax or limit counts physical units of a good whose value per unit varies, and the actor controls the mix, then `quality_per_unit` of the units counted increases and the low-value units are discarded or not produced. Derivation: CR-3 (each unit of the limit now has a cost), CR-4c applied to the unit of the limit (its lowest-valued use is given up first), CR-6 (pressure displaced to an unregulated term, the mix); where discarding is prohibited, CR-4 with x: comply, y: violate. The same move covers per-unit taxes that favor dearer grades.
4. *Consolidation under tradable rights (proposed EN-13).* If a policy creates tradable rights to a capped quantity and holders' costs differ, then rights move to the lowest-cost users: `number_of_sellers` decrease, `capital_stock_target` decrease over time, and the lease price equals the marginal user's margin. Assumes: cost differences and free transfer (`other`). Derivation: CR-4 (x: use one's own right, y: lease it out), CR-7a, CR-10b. WE-015's medallions are a near case, with the cap per vehicle instead of per tonne.

**(d) Vocabulary.**
1. *Discards.* No variable measures output produced and then destroyed or thrown away before any exchange (fish discarded at sea). C-13 records it indirectly as fewer small fish landed. A variable such as `output_discarded` is needed.
2. *Lease prices of a right.* `asset_value` measures the value of the right; there is no variable for the price of its use for a period. C-3 uses `price_paid` with a qualifier, signed from a counterfactual in which the price does not exist. Either a variable `use_price_of_right`, or a note in 2.5 that a price created by the policy is signed `increase` from nothing (as `asset_value` already is for created assets), would settle it.
3. *Instrument type.* 2.3 has `quota` but no type for allocating the rights it creates (free by history, auction, lottery). WE-014 and this example both write "Allocation of K1 (part of K1)". A type `allocation_of_rights`, with the allocation rule as a parameter, would make the rule that drives C-4 to C-8 a recorded field.
4. *Per-reading signs with no effect.* U1 changes the weight of a chain but not a sign. Had it decided a sign only under one reading (lease deductions lower crew pay under U1-a and leave it unchanged under U1-b, in the short run), there is no sign value for "no change" under a reading, so the consequence could not be written in the per-reading form. A sign value `none` usable only per reading is proposed.
5. *Effort beyond output.* Resources spent racing for an allocation, beyond what the output they produce is worth, have no variable (section 9). `compliance_cost` does not fit, since the race is not compliance.
6. *Actor class.* Share-paid crew (paid a fixed share of revenue under a standard contract) are neither `sellers` nor ordinary employees with a `wage_rate`; a note in 2.2 on share contracts would help.
