# WE-030 / Analysis: Per-tonne subsidy on wheat exports (Tarvona Grain Export Support Act)

Analyst: core-only re-run (Handbook 0.7)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Tarvona Grain Export Support Act.** Tarvona (about 22 million people; own currency, the tal (T); floating exchange rate) harvests about 12 Mt of wheat a year, mostly in the Eastern Plains. About 7.5 Mt is used at home (4.5 Mt milled, 2.0 Mt fed to livestock, 1.0 Mt seed and other uses) and about 4.5 Mt exported, about 6% of world wheat exports. Port export price about T 240 per tonne; farm-gate about T 220 (inland freight about T 20). About 40% of wheat land is farmed by tenants on one-year cash leases renewed each 1 October. Tarvona also exports about 0.8 Mt of feed barley and grows canola and pulses on land that can grow wheat. Other large export industries: wine and tourism. Main import-competing industries: clothing, household goods, processed foods. Neighboring Morvia grows about 2 Mt of wheat, roughly what it uses; under a free trade agreement (FTA) goods of Morvian origin enter Tarvona duty-free, and milling wheat into flour confers Morvian origin. The main wheat region lies 40 to 80 km from the Morvian border; trucking across costs about T 10 per tonne each way.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Tarvona. Just outside: Morvia, linked by the FTA and a border 40 to 80 km from the main wheat region. | "Neighboring Morvia grows about 2 Mt of wheat ... Tarvona and Morvia have a free trade agreement" |
| Announced / enacted / effective / expires | Announced 10 March Year 1 (budget speech); enacted 20 May Year 1; applies to wheat exported on or after 1 July Year 1; expires 30 June Year 4. The Minister of Agriculture "may extend it by regulation". | Policy record, dates paragraph |
| Enforcement (who, penalties, resources) | Customs checks export declarations and samples 2% of wheat imports declared as Morvian origin; Ministry of Agriculture payments office pays claims. Clawback of the payment plus 50% and loss of registration where paid wheat is re-imported. Both bodies act "within existing appropriations". | K2, K3 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Export payment | `per_unit_subsidy` | Wheat (grain) exported from Tarvona, by sea or by land | Registered exporters | T 35 per tonne (about 15% of the export price), paid on a customs declaration that the wheat left Tarvona; no tonnage cap; general budget; estimate T 160 million a year (4.5 Mt × T 35) | None by grade or destination; flour unclear (U1) |
| K2 Registration and clawback | Condition of K1 | Exporters | Exporters | Registration with a T 50,000 bond; repayment plus 50% penalty and loss of registration if paid wheat is re-imported | — |
| K3 Enforcement | Enforcement | K1, K2 | Customs; Ministry payments office | Declaration checks; 2% sampling of imports declared Morvian; within existing appropriations | — |

Existing rules kept in the counterfactual: a 25% tariff on wheat and flour imports (about T 64 per tonne on wheat), except goods of Morvian origin; Morvian certificates of origin issued by Morvian chambers of commerce on the shipper's declaration.

Funding: "the general budget"; no new tax and no offsetting cut named (A-27).

Unclear provisions: **U1**, whether "wheat" in K1 includes flour exported by Tarvonian mills, paid per tonne of wheat equivalent. U1-a: flour does not qualify. U1-b: flour qualifies per tonne of wheat equivalent. No probabilities are given; consequences that depend on U1 carry one sign per reading.

Counterfactual law (CR-1, recording): without the Act, wheat exports earn the world price only; the tariff, the FTA and the origin rules are as stated.

Horizons used: **short** = the announcement window (10 March to 30 June Year 1) and marketing year 1 (from 1 July Year 1); **medium** = marketing years 2 to 4 (to 30 June Year 4), after one autumn planting and one lease renewal; **long** = after 30 June Year 4.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Export payment | binary (state gives) | Yes: every exported tonne qualifies; the domestic price follows the export route (A-1, A-2) | 3 (a payment of T 35 is attached to the option 'export a tonne of wheat'); 4 (means move from the general budget to exporters on every tonne, including tonnes that would have been exported anyway) | CR-4, CR-5c, CR-6, CR-7a, CR-7b, CR-7c, CR-8b, CR-9, CR-10a, CR-10c, CR-12e |
| K2 Registration and clawback | condition of K1 | Yes for exporters who claim; binding on round-trippers only where enforced (A-10) | 3 (registration and bond attached to claiming); 3 (repayment plus 50% and loss of registration attached to re-importing paid wheat, as a risk where detection is uncertain); 1 (claiming removed for unregistered sellers) | CR-1, CR-3a, CR-4 (x: comply, y: violate), CR-8c |
| K3 Enforcement | binary (state uses means) | Yes, within fixed appropriations (A-26) | 3 (checks attached to exporting and to importing goods declared Morvian, A-11); 4 (staff time redirected from other duties) | CR-8a, CR-8c |

The Act names no price; it attaches a payment to one route of sale (export) and not to the other (home use). Because Tarvona is a net exporter (A-1) and imports cannot undercut (A-2), sellers move wheat between the two routes until their yields are equal net of moving costs (CR-7a). The domestic price therefore rises with the export receipt, although no domestic transaction is paid.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| exporters.registered | Grain exporters (traders and large farms) who claim K1 | Op 3: exporting brings T 35 a tonne; op 3: registration, bond and declarations; op 3: clawback risk on re-import. |
| exporters.forward_buyers | Exporters holding Year 1 crop bought forward before 10 March at fixed prices (A-N4) | Contract relation: the payment accrues to them on wheat whose price was fixed before the Act was expected. |
| growers.wheat | Owner-operators and tenants who grow wheat (sellers.current) | Through CR-7a: the home price rises toward the export receipt; switching land into wheat yields more (CR-4). |
| growers.forward_sold | Growers who sold Year 1 crop forward before 10 March (A-N4) | Contract relation: price fixed; no change on that tonnage. |
| holders.year0_wheat | Holders of Year 0 wheat on 10 March Year 1 | CR-10a: wheat exported after 1 July earns the payment; storing until July becomes worth more (A-8). |
| landowners.wheat_land | Owners of land that can grow wheat (factor_owners.specific) | CR-7c: the expected yield of the land rises from 10 March Year 1 (A-14). |
| tenants.wheat_land | Tenants on one-year cash leases | Contract relation: rent fixed until 1 October Year 1, then renegotiated (A-15). |
| buyers.domestic_wheat | Millers, feed users, seed and other users (buyers.current) | Through CR-7a: pay the higher home price; no CR-1 operation is performed on them directly. |
| millers.tarvona | Tarvonian flour mills (domestic sales and exports) | Pay more for wheat; U1-a: flour exports earn nothing; U1-b: flour exports earn T 35 per tonne of wheat equivalent. |
| bakers | Buyers of flour | Through CR-9 (flour input_to bread). |
| households | Buyers of bread | Through CR-9 (bread). |
| livestock_producers | Pig and poultry producers who feed wheat | Through CR-7a: dearer feed wheat; option to switch to barley (A-21); compete with imported meat (A-22). |
| growers.barley, growers.canola_pulses | Sellers of goods grown on the same land (sellers.substitutes) | CR-9: land competes for wheat; barley is a feed substitute. |
| input_suppliers.wheat | Sellers of seed and other inputs to wheat growing | CR-9 (input_to). |
| rail_port_operators | Sellers of grain rail and port services | CR-9 (input_to exports); capacity near full in harvest months (A-23). |
| shippers.other_bulk | Barley, canola and other bulk shippers using the same rail and ports | CR-9: compete with wheat exporters for the same capacity. |
| buyers.foreign | Foreign buyers of wheat | CR-9: Tarvonian supply to them rises (A-3). |
| sellers.foreign | Exporters of wheat from other origins | CR-9: compete with Tarvonian wheat for the same buyers. |
| sellers.foreign_meat | Exporters of pork and poultry to Tarvona | CR-9: compete with Tarvonian meat (A-22). |
| neighboring_jurisdictions.morvia_growers | Morvian wheat growers | CR-9 (across_border): Tarvonian price higher; FTA lets Morvian wheat in duty-free (A-16). |
| neighboring_jurisdictions.morvia_mills | Morvian flour mills | CR-9 (across_border): can buy wheat at world prices and sell flour duty-free into Tarvona (A-20). |
| buyers.tarvona_near_border | Tarvonian buyers who can buy Morvian wheat or flour | CR-4 (x: buy Tarvonian, y: buy Morvian). |
| traders.round_trip | Traders who export paid wheat to Morvia and bring it back declared as Morvian (A-10) | CR-4 (x: comply, y: violate). |
| importers.morvian_goods | Importers of genuine Morvian wheat and flour | Op 3: extended origin checks (A-11). |
| officials.ministry_agriculture | Payments office | Op 4: pays K1 out of the budget; administers registration within fixed appropriations (A-26). |
| officials.customs | Customs Service | Op 3: checks declarations and origin within fixed appropriations (A-26). |
| taxpayers.current, taxpayers.future, recipients_of_other_spending | Those who fund K1 through the general budget | Op 4 (through the budget, CR-8b); which group bears it depends on A-27. |
| growers_federation, exporters_association | Organized beneficiaries | CR-4 (x: accept expiry, y: lobby for extension). |
| millers, feed_compounders, livestock_producers (organized) | Organized payers of the higher home price | CR-4 (x: accept, y: lobby against, or for flour coverage). |
| foreign_exchange_market | Buyers and sellers of foreign currency | CR-9 (currency): more export receipts offered (A-24). |
| sellers.wine_tourism | Other exporters | CR-9 (currency): compete for the same foreign buyers' means; tal value of receipts. |
| sellers.import_competing | Clothing, household goods, processed foods | CR-9 (currency): imports dearer or cheaper in tal; processed foods also buy flour. |
| buyers.imports | Buyers of imported goods | CR-9 (currency). |
| road_users.border_region | Users of roads between the Eastern Plains and Morvia | CR-9 (shared_facility): more trucks. |

Relations followed: exchange (wheat, flour, bread, feed, meat, freight, inputs); contract (cash leases; forward sales); currency (export receipts and imports); shared_facility (border roads; rail and port capacity is bought, so it is followed as exchange); across_border (Morvia); proximity: none found that falls inside the controlled variables (dust or traffic near elevators would be environmental and is out of scope); gift: none found.

## 4. Direct effect

CR-1 and CR-2: what K1 changes first, against the no-policy counterfactual.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | exporters.registered | net_price_received (per tonne exported, including the payment) | increase | short; medium | CR-1 op 3, CR-5c, CR-12e | - |
| C-2 | officials.ministry_agriculture | subsidy_outlay | increase | short; medium | CR-1 op 4, CR-8b | - |
| C-3 | growers.wheat | net_price_received (farm-gate wheat) | increase | short; medium | CR-7a, CR-6, CR-12e | A-1, A-2 |
| C-4 | buyers.domestic_wheat | price_paid (wheat) | increase | short; medium | CR-7a, CR-6, CR-5c | A-1, A-2 |
| C-5 | buyers.foreign | price_paid (world wheat) | decrease | short; medium | CR-9, CR-6 | A-3, A-6 |
| C-6 | growers.wheat | subsidy_share_received (against foreign buyers) | increase | short; medium | CR-7b | A-5 |

## 5. Responses

CR-4 for every pair of options each class has; CR-5 for exchanges; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | growers.wheat, exporters.registered | quantity_traded (wheat exports from 1 July Year 1) | increase | short; medium | CR-4 (x: sell at home, y: export), CR-7a, CR-5 | A-3 |
| C-8 | buyers.domestic_wheat (feed users) | quantity_demanded (wheat) | decrease | short; medium | CR-4c; CR-4 (x: wheat, y: barley) | A-4 or A-21 |
| C-9 | buyers.domestic_wheat | quantity_traded (wheat used in Tarvona) | decrease | short; medium | CR-4c, CR-5 | A-1, A-2, A-4 |
| C-10 | growers.wheat | quantity_supplied (wheat harvest) | increase | medium | CR-4 (x: barley, canola or pulses, y: wheat), CR-7a, CR-10b | A-1, A-2, A-7 |
| C-11 | holders.year0_wheat | quantity_traded (wheat exports, 10 March to 30 June Year 1) | decrease | short (announcement window) | CR-10a, CR-4 (x: export now, y: store until July) | A-8 |
| C-12 | holders.year0_wheat | inventory_held (wheat on 30 June Year 1) | increase | short | CR-10a, CR-4 | A-8 |
| C-13 | holders.year0_wheat | quantity_traded (wheat exports, July to September Year 1) | increase | short | CR-10a, CR-4 | A-8 |
| C-14 | buyers.domestic_wheat | price_paid (wheat, 10 March to 30 June Year 1) | increase | short (announcement window) | CR-10a, CR-7a (across time), CR-6 | A-1, A-2, A-8 |
| C-15 | exporters.registered | number_of_sellers (registered exporters, including large farms) | increase | short | CR-4 (x: sell to a trader, y: register and export directly) | A-9 |
| C-16 | exporters.registered | compliance_cost (registration, bond, declarations) | increase | short; medium | CR-1 op 3, CR-8c | - |
| C-17 | traders.round_trip | informal_activity (paid wheat re-imported as Morvian) | increase | short; medium | CR-4 (x: comply, y: violate), CR-8c | A-10 |
| C-18 | officials.customs, officials.ministry_agriculture | enforcement_cost | increase | short; medium | CR-1 op 3, CR-8c | - |
| C-19 | importers.morvian_goods | compliance_cost (origin checks on genuine Morvian wheat and flour) | increase | short; medium | CR-1 op 3, CR-8c | A-11 |
| C-20 | growers_federation, exporters_association | lobbying_effort (to extend the Act) | increase | medium | CR-4 (x: accept expiry, y: lobby), CR-10a, CR-8c | A-12 |
| C-21 | millers, feed_compounders, livestock_producers | lobbying_effort (against the Act, or for flour coverage) | increase | short; medium | CR-4 (x: accept, y: lobby), CR-8c | A-13 |
| C-22 | exporters.registered | quantity_traded (wheat exported by land to Morvia) | increase | short; medium | CR-4 (x: export by port, y: truck to Morvia), CR-9 | A-23 or A-20 |
| C-23 | millers.tarvona | quantity_traded (flour exports) | U1-a: decrease; U1-b: ambiguous | short; medium | CR-4c, CR-9, CR-12b | A-1, A-2 |
| C-24 | landowners.wheat_land | asset_value (wheat land) | increase | short (from 10 March Year 1) | CR-7c, CR-10c, CR-12e | A-1, A-2, A-14 |
| C-25 | tenants.wheat_land | price_paid (cash rent, leases renewed from 1 October Year 1) | increase | medium | CR-7b, CR-6 (existing contracts), CR-5c | A-1, A-2, A-15 |
| C-26 | tenants.wheat_land | resources_available_other_uses | increase | short (Year 1 crop, rent fixed) | CR-6 (existing contracts), CR-8b | A-1, A-2 |
| C-27 | landowners.wheat_land | subsidy_share_received | increase | medium | CR-7b | A-14, A-15 |
| C-28 | exporters.forward_buyers | subsidy_share_received | increase | short | CR-6 (existing contracts), CR-8b | A-N4 |
| C-57 | growers.forward_sold | net_price_received (wheat sold forward before 10 March Year 1) | no_change | short | CR-6 (existing contracts) | A-N4 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth counted from K1. Branches stopped: buyers of imports at depth 3 (diffuse bystanders, C-53); importing countries' wheat growers at depth 3 (world price, diffuse); customers of meat processors and of processed-food makers at depth 4.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-29 | bakers | price_paid (flour) | increase | short; medium | CR-9, CR-4, CR-6, CR-12e | wheat input_to flour (close) | A-1, A-2, A-N2 |
| C-30 | households | price_paid (bread) | increase | short; medium | CR-9, CR-6, CR-7b | flour input_to bread (close) | A-1, A-2, A-17, A-N2 |
| C-31 | households | quantity_demanded (bread) | decrease | short; medium | CR-4c | as above | A-1, A-2, A-17, A-18, A-N2 |
| C-32 | households | resources_available_other_uses | decrease | short; medium | CR-3c, CR-8a | as above | A-1, A-2, A-17, A-19, A-N2 |
| C-33 | millers.tarvona | quantity_traded (flour sold in Tarvona) | decrease | short; medium | CR-9, LW-10 | flour input_to bread (close) | A-1, A-2, A-17, A-18, A-N2 |
| C-34 | millers.tarvona | asset_value (mills) | U1-a: decrease; U1-b: ambiguous | short; medium | CR-7c, CR-10c, CR-12b | - | A-1, A-2, A-17, A-18, A-N2, A-N3 |
| C-35 | livestock_producers | quantity_substitute (barley in feed rations) | increase | short; medium | CR-4 (x: wheat, y: barley), CR-9 | barley substitute for feed wheat (close) | A-1, A-2, A-21 |
| C-36 | growers.barley | quantity_traded (barley exports) | decrease | short; medium | CR-9, CR-7a | barley substitute for feed wheat; land shared by barley and wheat | A-21 or A-7 |
| C-37 | growers.canola_pulses | quantity_supplied (canola, pulses) | decrease | medium | CR-7a, CR-9 | land input_to wheat, canola and pulses | A-7 |
| C-38 | growers.barley | net_price_received (barley, in tal) | decrease | medium | CR-9, CR-7a | currency | A-N1, A-3, A-5, A-24 |
| C-39 | livestock_producers | quantity_supplied (pork, poultry) | decrease | medium | CR-9, CR-4, CR-7b | feed wheat input_to meat; imported meat substitute | A-1, A-2, A-22 |
| C-40 | sellers.foreign_meat | quantity_traded (meat imports into Tarvona) | increase | medium | CR-9, CR-4 | imported meat substitute for Tarvonian meat | A-1, A-2, A-22 |
| C-41 | sellers.foreign | quantity_traded (wheat from other origins) | decrease | short; medium | CR-9, CR-4 | Tarvonian wheat substitute for other origins (close) | A-3 |
| C-42 | sellers.foreign | net_price_received (wheat) | decrease | short; medium | CR-9, CR-6 | as above | A-3, A-6 |
| C-43 | buyers.tarvona_near_border | cross_border_purchases (Morvian wheat) | ambiguous | short; medium | CR-12b | across_border (close) | A-16, A-11 |
| C-44 | bakers | cross_border_purchases (Morvian flour) | ambiguous | short; medium | CR-12b | across_border (close) | A-20, A-11 |
| C-45 | neighboring_jurisdictions.morvia_growers | net_price_received (wheat) | ambiguous | short; medium | CR-12b | across_border; world wheat market | A-16, A-6, A-20, A-11 |
| C-46 | rail_port_operators | net_price_received (grain freight, harvest months) | increase | short; medium | CR-9, CR-6 | rail and port services input_to exports (close) | A-3, A-23 |
| C-47 | shippers.other_bulk | price_paid (rail and port services), wait_time (rail and port) | at_least_one_increase | short; medium | CR-9, CR-6 | same capacity input_to other bulk exports | A-3, A-23 |
| C-48 | input_suppliers.wheat | quantity_traded (seed and inputs for wheat) | increase | medium | CR-9, LW-10 | inputs input_to wheat | A-7 |
| C-49 | foreign_exchange_market | exchange_rate | decrease | medium | CR-9, CR-6 | currency | A-3, A-5, A-24 |
| C-50 | sellers.wine_tourism | net_price_received (in tal) | decrease | medium | CR-9, CR-5c | currency | A-3, A-5, A-24 |
| C-51 | sellers.wine_tourism | quantity_traded (wine exports, tourist services) | decrease | medium | CR-4c, CR-9 | currency | A-3, A-5, A-24 |
| C-52 | sellers.import_competing | quantity_supplied (clothing, household goods, processed foods) | decrease | medium | CR-9, CR-4 | currency; flour input_to processed foods | A-3, A-5, A-24 |
| C-53 | buyers.imports | price_paid (imported goods, in tal) | decrease | medium | CR-9 | currency | A-3, A-5, A-24 |
| C-54 | road_users.border_region | travel_time | increase | short; medium | CR-9 (shared_facility) | shared_facility (border roads) | A-23 or A-20 |
| C-55 | taxpayers.current, taxpayers.future | resources_available_other_uses | at_least_one_decrease | short; medium | CR-8b, CR-8a, CR-3c | - | A-27 |
| C-56 | officials.customs, officials.ministry_agriculture | resources_available_other_uses (for other duties) | decrease | short; medium | CR-8a, CR-3c | - | A-26 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise (CR-12e) | Combined sign |
| --- | --- | --- | --- | --- |
| exporters.registered, net_price_received per tonne, short; medium | T 35 payment (CR-1 op 3) | world price falls as exports rise (A-6) | Response cannot reverse its cause: added exports lower the world price only while the receipt with the payment exceeds the counterfactual receipt, so the fall stops short of T 35 | increase (C-1) |
| growers.wheat, net_price_received, short; medium | export receipt with payment, passed to the home price (CR-7a, A-1, A-2) | world price fall (A-6); dearer freight in harvest months (A-23); appreciation of the tal lowers the tal value of the world price (A-24, medium) | Same argument: each of the three falls is a response to added exports, and added exports stop once the farm-gate yield is back at the counterfactual level, so none can push it below | increase (C-3) |
| buyers.domestic_wheat, price_paid, short; medium | as for growers | as for growers; imports cannot hold it down (A-2) | as above | increase (C-4) |
| landowners.wheat_land, asset_value, short | higher expected wheat yield (CR-7c) | appreciation lowers the tal value of world wheat (A-24) | as above: the land yield falls only as far as the wheat price, which stays above the counterfactual | increase (C-24) |
| bakers, price_paid (flour), short; medium | dearer wheat (CR-9, CR-6) | Morvian flour priced off a lower world wheat price (A-20, A-6) | Empirical premise A-N2: the import flow responds to the gap; it pushes the Tarvonian price no lower than the delivered Morvian price, which before the Act was above the Tarvonian flour price by more than the world price fall | increase (C-29) |
| buyers.tarvona_near_border, cross_border_purchases (Morvian wheat) | price gap opened by the Act exceeds trucking cost (A-16) | extended origin checks on genuine imports (A-11) | None stated | ambiguous (C-43) |
| bakers, cross_border_purchases (Morvian flour) | price gap (A-20) | extended origin checks (A-11) | None stated | ambiguous (C-44) |
| morvia_growers, net_price_received | sales into Tarvona at the higher price (A-16) | lower world price, which also prices Morvian mills' wheat (A-6, A-20); check costs (A-11) | None stated | ambiguous (C-45) |
| millers.tarvona, quantity_traded (flour exports) | U1-b: payment per tonne of wheat equivalent | dearer domestic wheat (C-4); under U1-b the world flour price also falls with the world wheat price | U1-a: no (+) chain. U1-b: none stated | U1-a: decrease; U1-b: ambiguous (C-23) |
| millers.tarvona, asset_value | U1-b: paid flour exports | lower domestic flour sales (C-33); U1-a: lower flour exports | U1-a: all chains (−). U1-b: none stated | U1-a: decrease; U1-b: ambiguous (C-34) |
| buyers.domestic_wheat (feed), quantity_demanded | - | less use at a higher price (A-4); switch to barley (A-21) | Independent chains with the same sign (CR-12d) | decrease (C-8) |
| growers.barley, quantity_traded (barley exports) | - | feed switching raises home use of barley (A-21); land moves out of barley (A-7) | Independent chains with the same sign (CR-12d) | decrease (C-36) |
| growers.barley, net_price_received, medium | possible rise in the world barley price as Tarvona exports less barley: not derivable without a premise on Tarvona's weight in world barley (Tier C note, CR-12 clarification) | appreciation (A-24) with the price set by the export route (A-N1) | Only the derived chain is reported | decrease (C-38) |
| sellers.import_competing, quantity_supplied, medium | - | cheaper competing imports (A-24); for processed foods, dearer flour (C-29) | Same sign | decrease (C-52) |
| tenants.wheat_land | short: Year 1 crop sold higher while rent is fixed (C-26) | medium: rent rises at renewal (C-25) | Different variables and horizons: not netted (CR-12c, CR-12g) | resources_available_other_uses increase (short); price_paid (rent) increase (medium) |
| holders.year0_wheat, quantity_traded (exports) | July to September Year 1 (C-13) | 10 March to 30 June Year 1 (C-11) | Separate windows, each against the counterfactual | decrease (window 1); increase (window 2) |
| growers.wheat, net_price_received on forward-sold tonnage | - | - | Contract fixes the price | no_change (C-57) |

No chains cancel by construction (CR-12f). The K2 clawback offsets a K1 payment only where detected; it does not undo C-2 by construction.

## 8. Time structure

- **Announcement window (10 March to 30 June Year 1).** The payment became expected at the budget speech; the government majority makes passage likely (A-8). Holders of Year 0 wheat store it until July rather than export it before (CR-10a; C-11, C-12, C-13), and the home price rises at once because home buyers must bid against storage for July export (C-14). Landowners capture the expected rise in land yields from 10 March (CR-7c, CR-10c; C-24). Holders of land who sold between 10 March and enactment (20 May) shared the gain with buyers according to the probability of passage then (CR-7c, "becomes expected" is a matter of probability).
- **Contracts.** Year 1 crop sold forward before 10 March at fixed prices: the exporter who holds the contract receives the payment and the grower does not (C-28, C-57; A-N4). Cash leases for Year 1 were fixed on 1 October Year 0, so tenants keep the gain on the Year 1 crop (C-26) and rents rise at the 1 October Year 1 renewal (C-25). From then on the gain moves to landowners (C-27).
- **Planting.** The first planting decision after the announcement is in autumn Year 1, so land moves from barley, canola and pulses into wheat for the Year 2 harvest (A-7; C-10, C-36, C-37, C-48). Year 1 added exports come from stocks and from lower home use (A-3, A-4).
- **Exchange rate.** The currency link (C-49 to C-53) works within the medium horizon (A-24).
- **U1.** The minister's statement that "products of wheat" are "intended to be covered in due course" conveys information (CR-11c): millers who believe it may hold flour export capacity rather than close it. No sign is given, because what millers believed before and how they read the statement are not among the premises.
- **Expiry (30 June Year 4).** Whether exporters expect the Act to lapse is below the cut-off (A-25, p 0.4), so no end-of-term rush and no fall in land values ahead of expiry are reported. The extension power gives beneficiaries a standing stake in lobbying (C-20). If the Act does lapse, the effects run only on flows that end with the payment: land values return toward the counterfactual (persistence: none, long); wheat plantings return over one planting season because rotations are annual (persistence: none, long); the payment, registration and bonds end (persistence: n/a). Investments made for the Act that cost something to undo (registration, storage, any rail or port expansion) persist (CR-10b), but no premise in this case says such investments were made.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-55 | taxpayers.current, taxpayers.future | resources_available_other_uses | at_least_one_decrease | Purchases and saving forgone through taxes now or later to fund T 160 million a year or more (C-2) | CR-8b, CR-8a, CR-3c |
| C-32 | households | resources_available_other_uses | decrease | Other purchases forgone because households keep buying most bread at the higher price | CR-3c, CR-8a |
| C-9 | buyers.domestic_wheat | quantity_traded (wheat used in Tarvona) | decrease | Flour, feed and other home uses of wheat that are no longer served because the wheat is exported | CR-4c, CR-5 |
| C-37 | growers.canola_pulses | quantity_supplied (canola, pulses) | decrease | Canola and pulses not grown on land moved into wheat | CR-7a |
| C-39 | livestock_producers | quantity_supplied (pork, poultry) | decrease | Meat not produced in Tarvona | CR-9, CR-4 |
| C-16 | exporters.registered | compliance_cost | increase | Time, fees and the use of T 50,000 per bond | CR-1 op 3, CR-8c |
| C-17 | traders.round_trip | informal_activity | increase | About T 20 per tonne of trucking, and false paperwork, used up on wheat that ends where it started | CR-4, CR-8c |
| C-18 | officials.customs, officials.ministry_agriculture | enforcement_cost | increase | Staff time checking declarations, origin and claims | CR-1 op 3, CR-8c |
| C-56 | officials.customs, officials.ministry_agriculture | resources_available_other_uses (for other duties) | decrease | Other checks and services not done, since appropriations are fixed | CR-8a, CR-3c |
| C-19 | importers.morvian_goods | compliance_cost | increase | Paperwork and delay on genuine Morvian imports | CR-1 op 3, CR-8c |
| C-20 | growers_federation, exporters_association | lobbying_effort | increase | Time and money spent seeking an extension | CR-4, CR-8c |
| C-21 | millers, feed_compounders, livestock_producers | lobbying_effort | increase | Time and money spent opposing the Act or seeking flour coverage | CR-4, CR-8c |
| C-47 | shippers.other_bulk | price_paid (rail and port services), wait_time (rail and port) | at_least_one_increase | Capacity in harvest months drawn to wheat exports | CR-6, CR-9 |

Both sides of each transfer (CR-8b): the outlay (C-2) is matched by taxpayers' payment (C-55) and by exporters' receipts (C-1), which pass to growers (C-3, C-6), to forward buyers on fixed contracts (C-28), and with time to landowners (C-24, C-27). The higher home price is a second transfer, not from the budget: home buyers pay more on what they keep buying (C-4, C-32), and growers receive it on their home sales (C-3). Foreign buyers gain through the lower world price (C-5), matched by lower receipts for other origins (C-42). Land value gains (C-24) are matched by what later buyers pay for them (CR-8 symmetry). Round-trip payments (C-17) are a transfer to traders from the budget, plus the trucking used up.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | Tarvona remains a net exporter of wheat throughout, so the domestic price is set by the export route. | binding | 0.9 | 4.5 Mt exported against 7.5 Mt used at home; harvest variability; the Act raises exports further. | These consequences fail or lose this chain: C-3, C-4, C-9, C-10, C-14, C-23, C-24, C-25, C-26, C-29 to C-35, C-39, C-40. |
| A-2 | Imports cannot hold the domestic price below the export price plus the payment: the 25% tariff exceeds the payment, and Morvian wheat is too little to fill the gap. | binding | 0.8 | Tariff schedule; Morvian harvest (about 2 Mt) against Tarvonian use (7.5 Mt). | As A-1. |
| A-3 | Some Tarvonian sellers sell more abroad at the higher yield, and foreign buyers take more Tarvonian wheat at a slightly lower price. | substitutability | 0.9 | Stocks and spare land; foreign buyers' choice among origins. | These consequences fail or lose this chain: C-5, C-7, C-38, C-41, C-42, C-46, C-47, C-49 to C-53. |
| A-4 | Some domestic users can reduce their use of wheat (feed rations, marginal uses). | substitutability | 0.85 | Feed formulation practice; share of feed wheat in rations. | C-9 fails; C-8 loses one chain. |
| A-5 | Foreign buyers have clearly more alternatives than Tarvonian sellers. | substitutability | 0.75 | Tarvona's 6% share of world exports; number of competing origins; crop rotation constraints. | These consequences fail: C-6, C-38, C-49 to C-53. |
| A-6 | Tarvona's added exports are large enough to lower the world price, and are not offset by other exporters withdrawing. | other | 0.6 | Tarvona's share of world exports; studies of world price responses. | C-5, C-42 fail; C-45 loses an opposing chain (it becomes increase or stays ambiguous through A-11). C-1, C-3 hold more strongly. |
| A-7 | Land and other farm resources can move from barley, canola and pulses to wheat within the medium horizon. | alternative_uses | 0.85 | Rotations in the Eastern Plains; planting decisions each autumn. | C-10, C-37, C-48 fail; C-36 loses one chain. |
| A-8 | Holders of Year 0 wheat believed the announcement and can store it until July. | expectations | 0.8 | Government majority; on-farm and elevator storage. | C-11 to C-14 fail. |
| A-9 | Registration and the bond cost less than the payment on the tonnes some large farms would export directly. | other | 0.7 | Bond size against T 35 per tonne; farm sizes near the border. | C-15 fails. |
| A-10 | Round-tripping through Morvia pays for some traders. | enforcement | 0.65 | K2 and K3; experience with origin fraud under the FTA; border crossing costs. | C-17 fails; C-2 loses one of its sources of growth but keeps its sign. |
| A-11 | Customs extends origin checks to genuine Morvian wheat and flour imports. | enforcement | 0.75 | K3's sampling rule; Customs practice after earlier fraud cases. | C-19 fails; C-43 and C-44 become increase (one chain left); C-45 keeps an opposing chain through A-6. |
| A-12 | The growers' federation and exporters' association can organize to lobby at a cost below their stake. | other | 0.85 | Existing farm federation; the Act's extension power. | C-20 fails. |
| A-13 | Millers, feed compounders and livestock producers can organize to lobby. | other | 0.7 | Millers' association; pig and poultry associations. | C-21 fails. |
| A-14 | Buyers of land expect the payment to last at least its three-year term; wheat land is in fixed supply. | expectations | 0.8 | The Act's text; government statements; land market reports. | C-24, C-27 fail. |
| A-15 | Cash leases are renewed each year at negotiated rents, and landowners can let to other tenants. | other | 0.75 | Lease terms; number of tenants seeking land. | C-25, C-27 fail. |
| A-16 | Morvian wheat can be trucked into Tarvona at a cost below the price gap the Act opens. | mobility | 0.8 | Distance to the border; FTA rules of origin for grain. | C-43 loses its (+) chain; C-45 loses its (+) chain. |
| A-17 | Flour is a material part of the cost of bread, bakers cannot replace it at the old cost, and bread is not imported in quantity. | substitutability | 0.75 | Bakery cost shares; trade data for bread. | C-30 to C-34 fail. |
| A-18 | For most households, bread is not so large a share of spending that the loss in means outweighs the higher price in their choice. | other | 0.85 | Household budget surveys. | C-31, C-33, C-34 become ambiguous (CR-4 exception). |
| A-19 | Most households keep buying most of their bread at the higher price. | substitutability | 0.85 | Studies of bread demand. | C-32 fails. |
| A-20 | Morvian mills can buy wheat at world prices and supply flour to Tarvona, and milling confers Morvian origin under the FTA. | other | 0.65 | FTA rules of origin; Morvian milling capacity near the border. | C-44 loses its (+) chain; C-22 and C-54 lose one chain; C-45 loses part of its (−) chain. |
| A-21 | Feed rations can switch from wheat to barley. | substitutability | 0.85 | Feed formulation practice. | C-35 fails; C-8, C-36 lose one chain. |
| A-22 | Feed wheat is a material part of pork and poultry costs, and imported meat competes with Tarvonian meat. | substitutability | 0.6 | Cost shares; meat import shares. | C-39, C-40 fail. |
| A-23 | Grain rail and port capacity is close to full in the harvest months. | other | 0.6 | Terminal throughput; rail car availability. | C-46, C-47 fail; C-22 and C-54 lose one chain; C-3 loses an opposing chain. |
| A-24 | The exchange rate floats, and the added export receipts are not offset by capital flows within the medium horizon. | other | 0.6 | Exchange rate regime; capital account. | C-38, C-49 to C-53 fail; C-3, C-24 lose an opposing chain. |
| A-25 | Exporters expect the Act to lapse on 30 June of Year 4. | expectations | 0.4 | The minister's power to extend; the farm federation's influence. | No reported consequence rests on it (see Not reported). |
| A-26 | Customs and the Ministry administer the Act within fixed appropriations, as K3 says. | revenue_use | 0.7 | K3's text; budget documents. | C-56 fails; the cost then falls on the budget and joins C-55. |
| A-27 | The outlay is met by taxes or borrowing, not by cuts in other spending. | revenue_use | 0.6 | Budget statement; the government's borrowing plans. | C-55's group widens to include recipients_of_other_spending; the group sign at_least_one_decrease still holds (CR-8b, no premise). |
| A-N1 | Tarvona remains a net exporter of feed barley, so the domestic barley price is set by the export route. | binding | 0.6 | NEW. 0.8 Mt of barley exports; only marginal feed users switch (A-21) and only part of barley land moves (A-7). | C-38 fails; the home barley price could instead rise with feed demand, and C-38 becomes ambiguous. |
| A-N2 | Before the Act, little or no Morvian flour sold in Tarvona because delivered Morvian flour cost more than Tarvonian flour, by a margin larger than the fall in the world wheat price the Act causes. | other | 0.55 | NEW. No flour imports appear in the record of Tarvonian use; the world price fall is small (A-5: foreign buyers have many alternatives). | C-29 to C-34 become ambiguous (the Morvian flour chain is no longer dominated). |
| A-N3 | Mill capacity is specific to milling and cannot be moved to other uses at low cost. | durability | 0.85 | NEW. Milling plant and sites; no alternative use of the equipment. | C-34 fails (yields would be equalized by moving capacity, CR-7a). |
| A-N4 | Some Year 1 crop was sold forward at fixed prices before 10 March Year 1 for delivery after 1 July, and the contracts do not reopen the price. | other | 0.6 | NEW. Forward selling is common practice for export wheat; standard contracts fix the price. | C-28, C-57 fail. |

**Not reported** (an assumption below 0.5):
- If exporters expect the Act to lapse (A-25, p 0.4): exports bunch in the months before 30 June Year 4 and fall after it, against the counterfactual (CR-10a, CR-4 with x: export after, y: export before); land values fall as expiry approaches (CR-7c, CR-10c). Not reported.
- If Customs does not extend checks (negation of A-11, p 0.25): imports of Morvian wheat and flour increase. Not reported.

### Final check before the report (workflow)

1. **Uncombined chains.** Every key reached by two chains is in section 7. The world price fall, freight and appreciation chains against growers, home buyers and land were combined by CR-12e's response argument. Origin checks against the price gap give ambiguous signs (C-43 to C-45). The Morvian flour chain against the flour price needed A-N2.
2. **Group signs.** C-47 (price or waiting) and C-55 (current or future taxpayers) are groups.
3. **Baseline.** All signs are against Tarvona without the Act, with the tariff and FTA in place. The announcement-window signs (C-11, C-14) are against the same window without the Act.
4. **Worse off is not poorer.** `resources_available_other_uses` is signed only for households that keep buying bread (A-19), taxpayers (unavoidable), tenants receiving the Year 1 gain, and officials within fixed budgets. Feed users and millers are worse off (CR-3a) but no sign is claimed for their other spending.
5. **Timing shifts.** Year 0 exports are signed per window (C-11, C-13). The expiry rush is below the cut-off (A-25).
6. **Both sides of every transfer.** Outlay (C-2) and payers (C-55); payment and receivers (C-1, C-3, C-28, C-27); home price paid (C-4) and received (C-3); world price (C-5, C-42); rent (C-25, C-27); land value (C-24, buyers of land).
7. **Every class, every core rule.** CR-7c applied to land, mills and (below the cut-off) land before expiry; CR-8c to registration, enforcement, lobbying and round-trip trucking; CR-9 followed along exchange, contract (leases, forward sales), currency, shared_facility and across_border. No proximity or gift relation was found that bears on a controlled variable.
8. **Unstated premises.** Four were added (A-N1 to A-N4) and flagged.

## 11. Report

**The policy:** From 1 July Year 1 to 30 June Year 4, registered exporters receive T 35 for every tonne of wheat grain they export, by sea or land, paid from the general budget (estimated at T 160 million a year). Exporters register with a T 50,000 bond and repay the payment plus 50% if paid wheat comes back into Tarvona. Customs checks declarations and samples 2% of imports declared Morvian. Whether flour exports qualify is unclear (U1). The minister may extend the Act by regulation.

**Visible consequences:** Exporters receive more per tonne exported (C-1), and the Ministry pays out at least the budget estimate (C-2). Growers receive a higher farm-gate price (C-3). Wheat exports rise from July Year 1 (C-7).

**Invisible consequences:**
- *Home buyers of wheat and their customers.* The home price rises with the export receipt although no home sale is paid (C-4), from the announcement (C-14). Less wheat is used at home (C-9); feed users cut wheat and switch to barley (C-8, C-35). Flour and bread cost more (C-29, C-30); households buy somewhat less bread and have less for other things (C-31, C-32). Mills sell less flour at home (C-33); under U1-a they also export less flour and their plants lose value (C-23, C-34). Pork and poultry output falls and meat imports rise (C-39, C-40).
- *Land.* Landowners capture the gain from 10 March Year 1 (C-24) and, through rent at the October renewal, most of what tenants received at first (C-25, C-26, C-27). Exporters with forward contracts, not growers, receive the payment on that tonnage (C-28, C-57).
- *Other crops and trades.* Land moves from barley, canola and pulses to wheat (C-10, C-37); barley exports fall (C-36). Rail and port operators charge more at harvest, and other shippers pay more or wait longer (C-46, C-47). Wheat input sales rise (C-48).
- *Abroad.* Foreign buyers pay a little less (C-5); other exporting countries sell less at a lower price (C-41, C-42); more wheat crosses to Morvia by road (C-22).
- *Currency.* The tal rises (C-49): wine and tourism earn less in tal and sell less (C-50, C-51); import-competing industries produce less (C-52); buyers of imports pay less (C-53); barley growers receive less in tal (C-38).
- *Evasion and administration.* Some traders round-trip paid wheat through Morvia (C-17). Customs and the Ministry spend more on checks (C-18) and, within fixed budgets, do less of their other work (C-56). Importers of genuine Morvian goods bear origin checks (C-19). Exporters bear registration costs (C-16) and more farms register (C-15).
- *Payers.* Current or future taxpayers have less to spend (C-55). Growers and exporters lobby to extend the Act (C-20); millers and livestock producers lobby against it or for flour coverage (C-21).
- *Tier C.* Traffic on border roads increases (C-54).

**Ambiguous effects:** Imports of Morvian wheat and flour (C-43, C-44): the price gap draws them in; origin checks on genuine imports push them back. Morvian growers' price (C-45): sales into Tarvona against a lower world price and check costs. Under U1-b, flour exports and mill values (C-23, C-34): the payment against dearer domestic wheat and a lower world flour price. What would decide each: the size of the price gap against the cost of the checks; the payment against the rise in domestic wheat cost.

**Key conditions:** Tarvona stays a net exporter and imports cannot undercut (A-1, 0.9; A-2, 0.8), which is what carries the payment into the home price. Foreign buyers have more alternatives (A-5, 0.75), so growers keep most of the payment. Leases are renegotiated (A-15, 0.75) and land buyers expect the term to run (A-14, 0.8), which moves the gain to landowners. The currency effects need A-24 (0.6). Four premises were added: barley stays export-priced (A-N1, 0.6), Morvian flour did not undercut before (A-N2, 0.55), mills are specific (A-N3, 0.85), and some crop was sold forward (A-N4, 0.6).

**What this analysis cannot say:** Sizes: how far the world price falls, how much of the payment reaches growers rather than foreign buyers, by how much outlay exceeds the T 160 million estimate, or whether Morvian imports end up higher or lower. It does not net the gains to growers, landowners and foreign buyers against the losses to home users, taxpayers and other exporters, or say whether the policy is good. Whether paid wheat that returns as Morvian flour falls under the K2 clawback is not decided by the text and is not analyzed. What happens after 30 June Year 4 depends on expectations below the cut-off (A-25). Health, safety and environmental effects (including nutrition and traffic emissions) are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | exporters.registered | net_price_received (per tonne exported, including the payment) | increase | short; medium | visible | A | CR-1 (op 3: T 35 attached to exporting); CR-5c (the range of terms moves for the exporter); CR-12e (the world price fall is a response to added exports and stops before it cancels the payment) | none |
| C-2 | officials.ministry_agriculture | subsidy_outlay | increase | short; medium | visible | A | CR-1 (op 4: payments from the general budget on every exported tonne, including tonnes exported anyway); CR-8b; grows with C-7 and C-17 | none |
| C-3 | growers.wheat | net_price_received (farm-gate wheat) | increase | short; medium | visible | B | CR-7a (sellers move wheat from home use to export until yields are equal, so the home price rises toward the export receipt plus payment); CR-6 (A-2: imports cannot hold it down); CR-12e (world price fall, freight and appreciation are responses to added exports and cannot reverse it) | A-1, A-2 |
| C-4 | buyers.domestic_wheat | price_paid (wheat) | increase | short; medium | invisible | B | CR-7a and CR-6 as in C-3; CR-5c (home buyers must match the export alternative) | A-1, A-2 |
| C-5 | buyers.foreign | price_paid (world wheat) | decrease | short; medium | invisible | B | CR-9 (more Tarvonian wheat offered to the same buyers, A-3); CR-6 (the world price moves to a lower clearing level, A-6) | A-3, A-6 |
| C-6 | growers.wheat | subsidy_share_received (against foreign buyers) | increase | short; medium | invisible | B | CR-7b (the side with clearly worse alternatives keeps more: foreign buyers have many origins, growers have few other outlets, A-5) | A-5 |
| C-7 | growers.wheat, exporters.registered | quantity_traded (wheat exports from 1 July Year 1) | increase | short; medium | visible | B | CR-4 (x: sell at home, y: export; y made better); CR-7a; CR-5 (foreign buyers take more at a slightly lower price, A-3) | A-3 |
| C-8 | buyers.domestic_wheat (feed users) | quantity_demanded (wheat) | decrease | short; medium | invisible | B | CR-4c (the last tonne, valued least, is given up at the higher price, A-4); CR-4 (x: wheat, y: barley, A-21); independent chains, CR-12d | A-4 or A-21 |
| C-9 | buyers.domestic_wheat | quantity_traded (wheat used in Tarvona) | decrease | short; medium | invisible | B | CR-4c (home users reduce use at the higher price C-4, A-4); CR-5 (home sales that would have taken place do not) | A-1, A-2, A-4 |
| C-10 | growers.wheat | quantity_supplied (wheat harvest) | increase | medium | invisible | B | CR-4 (x: barley, canola or pulses, y: wheat; y made better by C-3); CR-7a (land moves until yields equal, A-7); CR-10b (through autumn planting) | A-1, A-2, A-7 |
| C-11 | holders.year0_wheat | quantity_traded (wheat exports, 10 March to 30 June Year 1) | decrease | short (announcement window) | invisible | B | CR-10a (an expected payment from 1 July alters choices now); CR-4 (x: export before July, y: store and export after; y made better) | A-8 |
| C-12 | holders.year0_wheat | inventory_held (wheat on 30 June Year 1) | increase | short | invisible | B | CR-10a, CR-4 (as C-11) | A-8 |
| C-13 | holders.year0_wheat | quantity_traded (wheat exports, July to September Year 1) | increase | short | invisible | B | CR-10a, CR-4 (stored wheat is exported once paid) | A-8 |
| C-14 | buyers.domestic_wheat | price_paid (wheat, 10 March to 30 June Year 1) | increase | short (announcement window) | invisible | B | CR-10a; CR-7a across time (holders sell at home now only for what storing to July would bring); CR-6 | A-1, A-2, A-8 |
| C-15 | exporters.registered | number_of_sellers (registered exporters, including large farms) | increase | short | invisible | B | CR-4 (x: sell to a trader, y: register and export directly; y gains the payment net of bond and registration, A-9) | A-9 |
| C-16 | exporters.registered | compliance_cost (registration, bond, declarations) | increase | short; medium | invisible | A | CR-1 (op 3: K2 attaches registration and a bond to claiming); CR-8c | none |
| C-17 | traders.round_trip | informal_activity (paid wheat re-imported as Morvian) | increase | short; medium | invisible | B | CR-4 (x: comply, y: export, truck back with a Morvian certificate, collect T 35 against about T 20 in trucking and a low chance of detection, A-10); CR-8c (trucking used up) | A-10 |
| C-18 | officials.customs, officials.ministry_agriculture | enforcement_cost | increase | short; medium | invisible | A | CR-1 (op 3: K3 duties of checking declarations, origin and claims); CR-8c | none |
| C-19 | importers.morvian_goods | compliance_cost (origin checks on genuine Morvian wheat and flour) | increase | short; medium | invisible | B | CR-1 (op 3: checks attached to importing goods declared Morvian, A-11); CR-8c | A-11 |
| C-20 | growers_federation, exporters_association | lobbying_effort (to extend the Act) | increase | medium | invisible | B | CR-4 (x: accept expiry, y: lobby the minister to extend; the extension power makes y open); CR-10a; CR-8c | A-12 |
| C-21 | millers, feed_compounders, livestock_producers | lobbying_effort (against the Act, or for flour coverage) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; x made worse by C-4); CR-8c | A-13 |
| C-22 | exporters.registered | quantity_traded (wheat exported by land to Morvia) | increase | short; medium | invisible | B | CR-4 (x: export by port, y: truck to Morvia; land exports qualify); chain 1: ports full in harvest months (A-23); chain 2: Morvian mills buy wheat at world prices to sell flour into Tarvona (A-20); CR-12d | A-23 or A-20 |
| C-23 | millers.tarvona | quantity_traded (flour exports) | U1-a: decrease; U1-b: ambiguous | short; medium | invisible | B | U1-a: CR-9 (wheat input_to flour; input dearer, C-4) and CR-4c (flour export price not raised). U1-b: CR-12b (payment per tonne of wheat equivalent against dearer wheat and a lower world flour price; no dominance premise) | A-1, A-2 |
| C-24 | landowners.wheat_land | asset_value (wheat land) | increase | short (from 10 March Year 1) | invisible | B | CR-10c and CR-7c (land in fixed supply; the expected rise in its yield from C-3 is captured by whoever owns it when the payment becomes expected, A-14); CR-12e (appreciation cannot reverse it) | A-1, A-2, A-14 |
| C-25 | tenants.wheat_land | price_paid (cash rent, leases renewed from 1 October Year 1) | increase | medium | invisible | B | CR-6 (rents fixed by existing leases until renewal); CR-5c and CR-7b (at renewal landowners can let to other tenants, A-15, so the land's higher yield is bid into the rent) | A-1, A-2, A-15 |
| C-26 | tenants.wheat_land | resources_available_other_uses | increase | short (Year 1 crop, rent fixed) | invisible | B | CR-6 (existing contract: the Year 1 rent was fixed on 1 October Year 0); CR-8b (tenants receive the higher price on the Year 1 crop and pay no more rent) | A-1, A-2 |
| C-27 | landowners.wheat_land | subsidy_share_received | increase | medium | invisible | B | CR-7b (the lasting gain settles on the means that cannot move: wheat land, A-14), through rents (A-15) | A-14, A-15 |
| C-28 | exporters.forward_buyers | subsidy_share_received | increase | short | invisible | B | CR-6 (existing forward contracts fix the price before the Act was expected); CR-8b (the payment goes to the exporter who ships the wheat) | A-N4 |
| C-29 | bakers | price_paid (flour) | increase | short; medium | invisible | B | CR-9 (wheat input_to flour); CR-4 (millers at the margin cut output at the higher input cost); CR-6; CR-12e (Morvian flour limits but does not reverse the rise, A-N2) | A-1, A-2, A-N2 |
| C-30 | households | price_paid (bread) | increase | short; medium | invisible | B | CR-9 (flour input_to bread); CR-6; CR-7b (bakers cannot replace flour and bread is not imported, A-17) | A-1, A-2, A-17, A-N2 |
| C-31 | households | quantity_demanded (bread) | decrease | short; medium | invisible | B | CR-4c (the last loaf, valued least, is given up); CR-4's exception ruled out by A-18 | A-1, A-2, A-17, A-18, A-N2 |
| C-32 | households | resources_available_other_uses | decrease | short; medium | invisible | B | CR-3c and CR-8a (households keep buying most bread at the higher price, A-19, so other uses lose) | A-1, A-2, A-17, A-19, A-N2 |
| C-33 | millers.tarvona | quantity_traded (flour sold in Tarvona) | decrease | short; medium | invisible | B | CR-9 and LW-10 (demand for flour follows demand for bread, C-31) | A-1, A-2, A-17, A-18, A-N2 |
| C-34 | millers.tarvona | asset_value (mills) | U1-a: decrease; U1-b: ambiguous | short; medium | invisible | B | CR-10c and CR-7c (specific mills, A-N3, carry expected yields). U1-a: lower home sales (C-33) and lower exports (C-23). U1-b: CR-12b (lower home sales against paid exports) | A-1, A-2, A-17, A-18, A-N2, A-N3 |
| C-35 | livestock_producers | quantity_substitute (barley in feed rations) | increase | short; medium | invisible | B | CR-4 (x: wheat, y: barley; x made worse by C-4, A-21); CR-9 (barley substitute for feed wheat) | A-1, A-2, A-21 |
| C-36 | growers.barley | quantity_traded (barley exports) | decrease | short; medium | invisible | B | CR-9 (relation: substitute; more barley used at home, A-21); CR-7a (land moves to wheat, A-7, medium); independent chains, CR-12d | A-21 or A-7 |
| C-37 | growers.canola_pulses | quantity_supplied (canola, pulses) | decrease | medium | invisible | B | CR-7a (land moves to the higher yield, wheat, A-7); CR-9 (land shared) | A-7 |
| C-38 | growers.barley | net_price_received (barley, in tal) | decrease | medium | invisible | B | CR-9 (currency: the tal appreciates, C-49); CR-7a (export-route pricing, A-N1, passes the lower tal export price to the home price). A suspected rise in the world barley price is not derivable without a premise and is a Tier C note | A-N1, A-3, A-5, A-24 |
| C-39 | livestock_producers | quantity_supplied (pork, poultry) | decrease | medium | invisible | B | CR-9 (feed wheat input_to meat; feed dearer, C-4); CR-7b (imported meat competes, A-22, so producers cannot pass on the cost); CR-4 (marginal producers cut output) | A-1, A-2, A-22 |
| C-40 | sellers.foreign_meat | quantity_traded (meat imports into Tarvona) | increase | medium | invisible | B | CR-9 (substitute: buyers move to imported meat as Tarvonian supply falls, C-39); CR-4 | A-1, A-2, A-22 |
| C-41 | sellers.foreign | quantity_traded (wheat from other origins) | decrease | short; medium | invisible | B | CR-9 (competitors for the same customers); CR-4 applied to foreign buyers (x: other origin, y: Tarvonian wheat, A-3) | A-3 |
| C-42 | sellers.foreign | net_price_received (wheat) | decrease | short; medium | invisible | B | CR-9; CR-6 (more supply at each price lowers the world clearing price, A-6) | A-3, A-6 |
| C-43 | buyers.tarvona_near_border | cross_border_purchases (Morvian wheat) | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-4 (x: Tarvonian wheat, y: Morvian wheat trucked in duty-free; y made better by C-4, A-16); (−) CR-4 (y made worse by origin checks on genuine imports, A-11). No dominance premise | A-16, A-11 |
| C-44 | bakers | cross_border_purchases (Morvian flour) | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-4 (y: Morvian flour milled from world-priced wheat, duty-free, A-20); (−) origin checks (A-11). No dominance premise | A-20, A-11 |
| C-45 | neighboring_jurisdictions.morvia_growers | net_price_received (wheat) | ambiguous | short; medium | invisible | B | CR-12b: (+) CR-9 across_border (sales into Tarvona at the higher price, A-16); (−) CR-9 (world price lower, A-6, and Morvian mills buy at world prices, A-20); (−) check costs (A-11) | A-16, A-6, A-20, A-11 |
| C-46 | rail_port_operators | net_price_received (grain freight, harvest months) | increase | short; medium | invisible | B | CR-9 (rail and port services input_to exports; more exports, A-3); CR-6 (capacity close to full, A-23, so the price rises to ration it) | A-3, A-23 |
| C-47 | shippers.other_bulk | price_paid (rail and port services), wait_time (rail and port) | at_least_one_increase | short; medium | invisible | B | CR-9 (competitors for the same capacity); CR-6 (pressure goes to price or waiting; which is not said) | A-3, A-23 |
| C-48 | input_suppliers.wheat | quantity_traded (seed and inputs for wheat) | increase | medium | invisible | B | CR-9 and LW-10 (demand for inputs follows the wheat area, C-10) | A-7 |
| C-49 | foreign_exchange_market | exchange_rate | decrease | medium | invisible | B | CR-9 (currency: added export receipts are offered for tal, A-3 with a small price fall, A-5); CR-6 (the price of foreign currency falls, A-24) | A-3, A-5, A-24 |
| C-50 | sellers.wine_tourism | net_price_received (in tal) | decrease | medium | invisible | B | CR-9 (currency: the same foreign price buys fewer tal, C-49); CR-5c | A-3, A-5, A-24 |
| C-51 | sellers.wine_tourism | quantity_traded (wine exports, tourist services) | decrease | medium | invisible | B | CR-4c (foreign buyers pay more in their currency, or sellers at the margin withdraw); CR-9 | A-3, A-5, A-24 |
| C-52 | sellers.import_competing | quantity_supplied (clothing, household goods, processed foods) | decrease | medium | invisible | B | CR-9 (currency: competing imports cheaper in tal, C-49); CR-4 (marginal producers withdraw); for processed foods, a same-sign chain through dearer flour (C-29; A-1, A-2, A-N2), CR-12d. Depth 4: stop | A-3, A-5, A-24 |
| C-53 | buyers.imports | price_paid (imported goods, in tal) | decrease | medium | invisible | B | CR-9 (currency, C-49). Depth 3, diffuse bystanders: stop | A-3, A-5, A-24 |
| C-54 | road_users.border_region | travel_time | increase | short; medium | invisible | C | CR-9 (shared_facility: more trucks to Morvia, C-22); Tier C pending the open question on shared facilities | A-23 or A-20 |
| C-55 | taxpayers.current, taxpayers.future | resources_available_other_uses | at_least_one_decrease | short; medium | invisible | B | CR-8b (the outlay, C-2, is taken from someone); CR-8a and CR-3c; group because the Act does not say taxes or borrowing (A-27 excludes cuts) | A-27 |
| C-56 | officials.customs, officials.ministry_agriculture | resources_available_other_uses (for other duties) | decrease | short; medium | invisible | B | CR-8a (staff time used for the Act within fixed appropriations, A-26, is withdrawn from other duties); CR-3c | A-26 |
| C-57 | growers.forward_sold | net_price_received (wheat sold forward before 10 March Year 1) | no_change | short | invisible | B | CR-6 (existing contract fixes the price; the payment goes to the buyer, C-28) | A-N4 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-030-C1: The currency link needs the sign of total export receipts in foreign currency, which is price times quantity: quantity rises (C-7) and the world price falls (C-5). No core rule signs a product of two variables moving in opposite directions, and CR-12c forbids netting different variables. A-24's wording ("the added export receipts") was used, with A-5 as the reason the price fall is small; the step is a premise, not a derivation.
- GAP-030-C2: CR-12e's "a response cannot reverse the change that causes it" covers the world price, freight and appreciation chains against the wheat price. It does not cover a response driven partly by a second change the policy also causes (Morvian flour priced off a lower world wheat price). The flour price needed the empirical dominance premise A-N2.
- GAP-030-C3: Export-route pricing (a net exporter's home price follows the export receipt) was derived from CR-7a, applied to wheat moving between two uses, with A-1 and A-2. The same structure for barley (C-38) needed the added premise A-N1. The derivation works, but no core rule prompts the analyst to check whether a substitute's price is set by an export route, which decides whether added home demand raises its price or only lowers its exports.

**(b) Core-rule wording that was hard to apply.**
- CR-1: home buyers of wheat face none of the four operations, yet they bear a large share of the cost through CR-7a. The workflow's "for each actor class, write down which operations it performs" gives "none" for them, and the rule's recording note does not say how to record classes reached only through equalization across uses.
- CR-7b: there are four parties to one payment (foreign buyers, exporters, growers, landowners), plus home buyers who are not parties to the export exchange but pay through the home price. "Rank each pair" needs pairwise premises the case does not supply beyond A-5 and A-15. No share was signed between exporters and growers.
- CR-7c and CR-10a with a probable extension: the land value reflects both the three-year term and the chance of extension by regulation. A-14 covers the term; A-25 (below the cut-off) concerns exporters' expectations, not land buyers'. The rule's "becomes expected is a matter of probability" gives no way to sign a fall ahead of expiry while the extension is uncertain.
- CR-12e "response" argument applied to appreciation: appreciation is a response to all added export receipts, not only wheat's, and it also acts on other exporters. Whether CR-12e's wording covers an economy-wide response that feeds back on the causing market was a judgment.
- CR-6 "existing contracts" was used for leases and forward sales; it is stated under price pressure rather than as a transfer rule, so it gives the no_change for forward-sold growers (C-57) only indirectly, together with CR-8b.
- The `persistence` field is defined for repeals only; a scheduled expiry is a repeal written into the policy, and it was handled as a note in section 8.

**(c) Vocabulary missing from the ontology.**
- No variable for outlay against the budget estimate (the counterpart of `tax_revenue_vs_static_projection`): the derivation shows outlay exceeds T 160 million (added exports, round-tripping, U1-b), but only `subsidy_outlay` increase could be recorded.
- No variable for export receipts in foreign currency (needed for the currency link, GAP-030-C1).
- No variable for land rent; `price_paid (cash rent)` was used for tenants. `right_lease_price` is defined for tradable rights only.
- No generic actor classes for landowners and tenants under a lease (used `landowners.wheat_land`, `tenants.wheat_land`), for parties to forward contracts, or for the foreign-exchange market (used `foreign_exchange_market`).
- The instrument list's entry for export subsidies points to a pattern family, with no core-rule entry; `per_unit_subsidy` was used as the record does.
- No variable for the share of payments made on fraudulent claims, which would let round-tripping be scored separately from `informal_activity`.
