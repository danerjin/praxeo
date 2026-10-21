# WE-047 / Analysis: Sugar tariff-rate quota replacing a flat tariff, with tradable licences allocated by history

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Kestrany Sugar Import Regime Act.** Kestrany consumes about 1,750,000 t of sugar a year (about 60% by food and drink manufacturers, 40% by households). Domestic beet sugar supplies about 1,100,000 t, from about 4,000 growers on about 120,000 ha and two processors (Ardmouth Sugar and the Pellmont Beet Co-operative) with six mills at about 90% of capacity. Imports averaged about 650,000 t a year in 2023 to 2025: about 450,000 t of raw cane sugar refined at two Vellport port refineries and about 200,000 t of white sugar. Kestrany takes about 1.2% of world sugar trade from many exporters. World prices (illustrative): raw $360 a tonne, white $440. Under the existing flat 25% tariff white sugar lands at about $550, which sets the domestic white price; revenue is about $62.5 million a year. Nine firms imported in 2023 to 2025: two Vellport refiners (66% of imports), four trading houses (25%) and three manufacturers importing directly (9%). Food manufacturers export about a fifth of their output; imported sugar-containing goods (not covered) hold about a quarter of the home market. Two wet mills make glucose syrup from domestic maize. Main exports: timber, machinery, tourism.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Kestrany's customs territory. Outside: the world sugar market, and foreign makers of sugar-containing goods, which the act does not cover. | §2. |
| Announced / enacted / effective / expires | Bill with the base period published 2 March 2026; enacted 10 June 2026; effective for the quota year from 1 January 2027; volume reviewed in 2031; no expiry. | §1, §15. |
| Enforcement (who, penalties, resources) | Customs applies the rates; the Ministry of Trade's licence office keeps the register of shares and licences. Imports above a firm's licence pay the out-of-quota rate; misdeclaration penalized under existing customs law. The licence office's funding is not stated. | §10, §11. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Two-rate tariff (replaces the flat 25%) | `tariff` | Imports of raw and white sugar | Importers of record | 2% ad valorem on imports covered by a licence, up to 400,000 t a year in total; 60% on all other sugar imports. A licence covers raw or white sugar tonne for tonne. | Sugar-containing goods (as now). |
| K2 Allocation by history | `rights_allocation` | Permanent quota shares and each year's licences | Licence office | Each firm that imported in 2023 to 2025 receives a permanent share of the 400,000 t equal to its share of imports in those years; licences issued each December pro rata. | - |
| K3 Trading | Rule on transfers | Shares and licences | Holders | Sale or lease to any registered importer; $200 per registered transfer; registration as an importer open to any firm for $500. | - |
| K4 Surrender | Rule on the use of licences | Licences | Holders | §9: "A licence not used by 30 September of the quota year is surrendered." | - |

Existing rules that stay in the counterfactual: the flat 25% tariff on raw and white sugar; customs classification of sugar mixtures; the general budget, which receives the tariff. Counterfactual: imports continue at about 650,000 t a year, evenly through the year (about 160,000 t a quarter), at a landed white price of about $550.

Unclear provisions:
- **U1, surrendered licences.** §9 surrenders licences unused by 30 September; §4(2): "The tariff quota shall be allocated in full in each quota year"; §12: "The Minister may make rules for the allocation of quantities among registered importers on application." U1-a: surrendered quantities return to the quota and are allocated again in the same year to registered importers on application. U1-b: surrender cancels the licence and the quantity lapses for that year. Readings get no probability.

**Figures used.** At $550 import demand is about 650,000 t, 250,000 t above the quota, so the domestic white price must rise above $550, at most to the out-of-quota landed price of about $704 (440 × 1.60). In-quota white lands at about $449. The quota rent is more than $100 and at most about $255 a tonne of white sugar (about $200 and $80 million a year at an illustrative $650; a share of the whole quota about $1 billion capitalized at 8%). Revenue: in-quota about $3.2 million a year; out-of-quota about $264 a tonne of white; below about $56 million in total if out-of-quota imports stay below 200,000 t, against $62.5 million now. Importers' trading margin about $15 a tonne.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Two-rate tariff | binary (state takes, at two rates) and triangular (a privilege for licence holders and domestic sellers) | Yes: import demand at $550 exceeds 400,000 t (A-1); enforced (A-2) | 3 for importers: the charge on importing falls from 25% to 2% for licensed tonnes (op 3, a burden removed) and rises to 60% for others (op 3, a burden attached); against the counterfactual the quantity at the low rate is fixed, so the price of the right rations it (CR-6 0.7 note) | CR-4, CR-5a, CR-5c, CR-6, CR-7, CR-8, CR-9, CR-10, CR-11a |
| K2 Allocation by history | binary (state gives a created right) | Yes once K1 binds | 2 and 4 for the nine historical importers: an option (import at 2%) added and means (a valuable, tradable share) transferred to them at creation; the qualifying history was fixed before the measure became expected | CR-7c (asset created by the policy), CR-7 0.7 (claims before creation, windfall), CR-8b, CR-10c |
| K3 Trading | rule on transfers | Yes, at low cost (A-6) | 2 (sale and lease added for holders and registered importers); 3 ($200 per transfer, $500 to register) | CR-4, CR-5, CR-7a, CR-8c |
| K4 Surrender | rule on use | Yes (A-18, A-19) | 1 (dated: the option to import at 2% under a licence is removed after 30 September); per U1, an option to apply for surrendered quantities is added (U1-a) or not (U1-b) | CR-1 0.7 (dated operation), CR-4 (timing), CR-6 (non-price allocation under U1-a), CR-10a |

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| buyers.domestic (manufacturers and households) | Buy white sugar at the domestic price | Through CR-6: the domestic price rises to ration the restricted import quantity. |
| manufacturers.home_market | Food and drink makers competing with imported sugar-containing goods (A-8) | Sugar input costs more; foreign rivals' costs unchanged. |
| manufacturers.exporting | Food exporters selling at world prices (A-9) | Sugar input costs more; output price fixed abroad. |
| manufacturers.direct_importers | The three manufacturers that imported directly | Receive shares (op 2, op 4); face the domestic price as their cost by opportunity cost (CR-3). |
| households | Buy about 40% of sugar | Pay more (A-24). |
| holders.refiners | The two Vellport refiners (66% of shares) | Op 2 and op 4: shares; their refining throughput may change (A-15). |
| holders.trading_houses | Four trading houses (25% of shares) | Op 2 and op 4: shares; lower trading volume. |
| importers.prospective | Firms that register to buy or lease licences or to apply under U1-a | Op 2 (registration, applications under U1-a); op 3 (fees). |
| domestic_processors | Ardmouth and Pellmont, six mills | Through CR-9 (same market): higher white price. |
| beet_growers | About 4,000 growers | Through CR-9 (input_to): processors' demand for beet rises. |
| land_owners.haul_radius | Owners of land within reach of the mills | CR-7c on the higher yield of beet land. |
| workers.beet_and_mills, workers.food_manufacturing | Labor in those activities | Through CR-9 (input_to). |
| wet_mills | Glucose syrup makers | Through CR-9 (substitute). |
| sellers.foreign.sugar | World sugar exporters | Sell less to Kestrany (A-5 for any world price effect). |
| sellers.foreign.sugar_goods | Foreign makers of sugar-containing goods | Through CR-9 (substitute): domestic rivals' costs rise. |
| port_warehouses | Storage at the ports | Through CR-9 (complement): stock built in 2026 and before each 30 September. |
| exporters.other | Timber, machinery, tourism | Through CR-9 (currency). |
| taxpayers / recipients of other spending | General budget | Revenue falls (C-5); licence office funded (A-27). |
| officials.licence_office, officials.customs | Administer and enforce | Op 4: new tasks. |
| organized_groups | Holders, growers, manufacturers, would-be importers | CR-4 (x: accept, y: lobby). |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.domestic | price_paid (white sugar, domestic) | increase | short; medium | CR-6 (fixed quantity at the low rate), CR-12e (response argument, 0.9 partial response) | A-1, A-2, A-3 |
| C-2 | buyers.domestic | price_paid (white sugar, domestic) | increase | long | CR-6, CR-12e (0.9) | A-1, A-2, A-26 |
| C-3 | holders (nine 2023 to 2025 importers) | asset_value (quota shares) | increase | short (from 2 March 2026) | CR-7c, CR-10c, CR-7 0.7 note | A-1, A-2, A-4, A-11 |
| C-4 | holders | right_lease_price (licences) | increase | short; medium; long | CR-6 0.7 note, CR-12 0.9 | A-1, A-2, A-4, A-6 |
| C-5 | taxpayers / general budget | tax_revenue (sugar tariff, quota years) | decrease | short; medium; long | CR-1 op 3, arithmetic | A-2, A-25 |
| C-6 | importers; sellers.foreign.sugar | quantity_traded (sugar imports, quota years) | decrease | short; medium; long | CR-5a, CR-6, arithmetic | A-2, A-25 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-7 | importers (2026, before the act takes effect) | quantity_traded (imports at 25%, March to December 2026) | increase | short (announcement window) | CR-10a, CR-4 (x: import in 2027 under the new rates, y: import in 2026 and store) | A-10 |
| C-8 | importers, manufacturers | inventory_held (31 December 2026) | increase | short (announcement window) | CR-10a, CR-7c (stocks are durable assets) | A-10 |
| C-9 | general budget | tax_revenue (sugar tariff, March to December 2026) | increase | short (announcement window) | CR-8b on C-7 | A-10 |
| C-10 | importers | quantity_traded (imports, October to December of each quota year) | decrease | short; medium; long | CR-1 0.7 (dated removal), CR-4 (x: import after 30 September at 60%, y: before at 2%) | A-18 |
| C-11 | importers, manufacturers | inventory_held (30 September of each quota year) | increase | short; medium; long | CR-4 (timing), CR-10a | A-18 |
| C-12 | importers | quantity_traded (imports, January to September of each quota year) | ambiguous | short; medium; long | CR-12b | A-18, A-25 |
| C-13 | holders, registered importers | quantity_traded (transfers and leases of shares and licences) | increase | short; medium; long | CR-7a, CR-5, CR-12 0.9 | A-6, A-7 |
| C-14 | importers.prospective | entry_rate (firms registered as importers) | increase | short; medium | CR-4 (x: stay out, y: register), CR-12 0.9 | A-1, A-6 |
| C-15 | importers.prospective | compliance_cost (applications for surrendered quantities) | U1-a: increase; U1-b: no_change | short; medium; long | CR-6, CR-8c per reading | A-19, A-20 |
| C-16 | importers.prospective | allocation_by_non_price_criteria (surrendered quantities) | U1-a: increase; U1-b: no_change | short; medium; long | CR-6 (criteria by which the scarce side chooses) per reading | A-19, A-20 |
| C-17 | importers | reclassification (sugar imported as mixtures outside the sugar heading) | increase | short; medium; long | CR-4 (x: covered form at 60% at the margin, y: mixture at a lower duty) | A-2, A-14 |
| C-18 | manufacturers | quantity_demanded (sugar) | decrease | short; medium; long | CR-4c, CR-4 (substitutes), CR-12d | A-1, A-2 |
| C-19 | manufacturers | quantity_substitute (glucose syrup and other sweeteners) | increase | short; medium; long | CR-4 (x: sugar, y: glucose syrup) | A-12 |
| C-20 | domestic_processors | quantity_supplied (white sugar) | increase | medium; long | CR-4, CR-7a | A-1, A-2, A-16 |
| C-21 | domestic_processors | investment_target (mill capacity) | increase | medium; long | CR-4 (x: hold capacity, y: expand), CR-10c | A-11, A-N1 |
| C-22 | organized_groups | lobbying_effort | increase | short (from 2 March 2026); medium; long | CR-4 (x: accept, y: lobby), CR-8c, CR-10a | A-17 |
| C-23 | officials.licence_office | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | - |
| C-24 | officials.customs | enforcement_cost (two rates, licence checks, mixtures) | increase | short; medium; long | CR-1, CR-8c | - |
| C-25 | importers | compliance_cost (registration, transfer fees, licence records) | increase | short; medium; long | CR-1 op 3, CR-8c | - |
| C-26 | officials.licence_office | non_tax_receipts (registration and transfer fees) | increase | short; medium; long | CR-8b | - |

## 6. Second-order effects

Depth limit 4. Chains through maize growers (maize input_to glucose syrup) and through the customers of food manufacturers are pruned at depth 3 as diffuse.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-27 | domestic_processors | net_price_received (white sugar) | increase | short; medium; long | CR-9, CR-6, CR-12e | domestic sugar same market as imported (close) | A-1, A-2, A-3 |
| C-28 | beet_growers | net_price_received (beet) | increase | medium; long | CR-9, LW-10, CR-7b | beet input_to white sugar (close) | A-1, A-2, A-16 |
| C-29 | beet_growers | quantity_supplied (beet) | increase | medium; long | CR-4, CR-7a | as above | A-16 |
| C-30 | land_owners.haul_radius | asset_value (land within reach of the mills) | increase | short (from announcement) | CR-7c, CR-10c | land input_to beet (close) | A-11, A-16 |
| C-31 | domestic_processors | asset_value (mills) | increase | short (from announcement) | CR-7c, CR-10c, CR-7b | mills input_to white sugar | A-1, A-2, A-3, A-11 |
| C-32 | workers.beet_and_mills | employment (beet farming and mills) | increase | medium; long | CR-9, LW-10 | labor input_to beet and sugar | A-16, A-23 |
| C-33 | manufacturers.home_market, manufacturers.exporting | return_on_capital (food manufacturing) | decrease | short; medium | CR-9, CR-7b, CR-12d | sugar input_to food (close) | A-8 |
| C-34 | manufacturers.home_market | quantity_traded (sugar-containing goods, home market) | decrease | medium; long | CR-9, CR-4 | imported sugar goods substitute (close) | A-8 |
| C-35 | sellers.foreign.sugar_goods | quantity_traded (imports of sugar-containing goods) | increase | medium; long | CR-9, CR-4 | as above | A-8 |
| C-36 | manufacturers.exporting | quantity_supplied (food exports) | decrease | medium; long | CR-4b, CR-7a | sugar input_to exported food; world price fixed | A-9 |
| C-37 | workers.food_manufacturing | employment (food manufacturing) | decrease | medium; long | CR-9, LW-10, CR-12d | labor input_to food | A-8, A-23 |
| C-38 | wet_mills | price_substitute (glucose syrup) | increase | short | CR-9, CR-6 | glucose substitute for sugar (partial) | A-12, A-13 |
| C-39 | households | resources_available_other_uses | decrease | short; medium; long | CR-3 (note), CR-8a, CR-8b | - | A-1, A-2, A-24 |
| C-40 | manufacturers.direct_importers | price_paid (sugar used, counting the lease value of their own licences) | increase | short; medium; long | CR-3 (cost is the alternative given up), CR-6 | - | A-1, A-2, A-6 |
| C-41 | holders.trading_houses (and direct importers as holders) | asset_value (the firm as a whole) | increase | short (from 2 March 2026) | CR-12b, CR-12e (A-22) | - | A-1, A-2, A-22 |
| C-42 | holders.refiners | quantity_supplied (white sugar refined at Vellport) | ambiguous | short; medium; long | CR-12b | raw sugar input_to refining | A-6, A-15, A-25 |
| C-43 | holders.refiners | asset_value (the firm as a whole) | ambiguous | short (from 2 March 2026) | CR-12 0.8 kind (3) | - | A-1, A-2, A-15 |
| C-44 | port_warehouses | price_complement, quantity_complement (storage) | at_least_one_increase | short (2026; each summer) | CR-9, CR-6 0.9 | storage complement of stock-building | A-10 |
| C-45 | taxpayers / recipients of other spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | CR-8b, CR-8 0.7 (payers from the general budget), CR-12d | - | A-25 |
| C-46 | exporters.other | quantity_traded (timber, machinery, tourism) | ambiguous | medium; long | CR-9 (currency), CR-12b | currency | A-8, A-9, A-21 |
| C-47 | all | exchange_rate | ambiguous | medium; long | CR-9 (currency), CR-12b | currency | A-8, A-9, A-21 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| buyers.domestic, price_paid, short; medium | in-quota quantity fixed below demand at $550 (CR-6, A-1, A-2) | domestic supply expands (A-16); buyers move to glucose (A-12) and imported goods (A-8); 2026 stocks drawn down | CR-12e response argument (the responses cannot push the price back below $550, since they stop when yields are equal) with the 0.9 note: the response is partial (A-3, five years) | increase (C-1) |
| buyers.domestic, price_paid, long | as above | as above, with new mill capacity (C-21) | Response argument with A-26 (ten years, p 0.6) as the partial-response premise | increase (C-2) |
| taxpayers / general budget, tax_revenue | 2026: imports brought forward at 25% (C-9) | quota years: in-quota at 2%, out-of-quota volume below 200,000 t (A-25) | Different horizons: not combined (CR-12g) | increase (2026, C-9); decrease (quota years, C-5) |
| importers, quantity_traded (imports by window) | Jan to Sep: licences used before 30 September (A-18) | Jan to Sep: total imports cut (A-25); Oct to Dec: only out-of-quota imports and any U1-a reallocations | Oct to Dec: A-18 (empirical) signs the window; Jan to Sep: none | decrease (Oct to Dec, C-10); ambiguous (Jan to Sep, C-12); decrease (whole year, C-6) |
| holders.trading_houses, asset_value (firm) | quota shares (C-3) | trading margin lost on about 250,000 t | A-22 (empirical: rent far exceeds the lost margin) | increase (C-41) |
| holders.refiners, quantity_supplied | out-of-quota imports at the margin may be raw (lands at about $576 against $704 for white, A-25) | licences move to white imports where the rent per tonne is larger (A-15, A-6); total imports fall | None: the cost of refining is not in the case | ambiguous (C-42) |
| holders.refiners, asset_value (firm) | quota shares (C-3) | refinery throughput if it falls (C-42, itself ambiguous) | A-22 covers the trading margin only, not the refining margin: kind (3) chain without a dominance premise | ambiguous (C-43) |
| exchange_rate; exporters.other | food exports fall (A-9) and imports of sugar goods rise (A-8): more foreign currency demanded relative to supply | sugar imports fall (C-6, A-21): less foreign currency demanded | None | ambiguous (C-46, C-47) |
| manufacturers, return_on_capital | - | higher sugar cost with output prices held by foreign rivals at home (A-8) and abroad (A-9) | Independent chains with the same sign (CR-12d) | decrease (C-33) |
| taxpayers / recipients of other spending, resources_available_other_uses | - | lost revenue (C-5, A-25); licence office budget (A-27) | Independent chains with the same sign (CR-12d) | at_least_one_decrease (C-45) |

CR-12f does not apply. Prices and quantities are not netted against each other (CR-12c).

**Final check before the report** (`03_workflow.md`).
1. Uncombined chains: the price chains from the time structure (stocks bought ahead) and from the substitutes are combined in C-1 and C-2; revenue is split by window; refiners' value is combined across shares and plant.
2. Group signs: storage (C-44) and the general-budget payers (C-45) are groups.
3. Baseline: every sign is against the flat 25% tariff staying, not against free trade; revenue falls against $62.5 million, not against zero; the price rises against $550.
4. Worse off is not poorer: `resources_available_other_uses` is signed for households, who keep buying (A-24), and for budget payers; manufacturers are signed on return and output, not on other spending.
5. Timing shifts: imports are signed per window (2026; January to September; October to December; whole year).
6. Both sides of every transfer: the quota rent (C-3, C-4) is paid by domestic buyers through the higher price (C-1) and by the budget through the 2% in place of 25% on 400,000 t (C-5, C-45); fees paid (C-25) and received (C-26); processors' and growers' gains (C-27, C-28) are paid by buyers (C-1).
7. Every actor class, every core rule: CR-7c applied to shares, land, mills and stocks; CR-6 to the domestic price, storage, glucose and surrendered quantities; enforcement and the licence office are recorded.
8. Unstated premises: one added (A-N1), flagged.

## 8. Time structure

- **Announcement (2 March 2026, with the base period).** The shares were known, by firm, from publication, and their value was a windfall: the qualifying history (2023 to 2025) was fixed before the act was expected (CR-7 0.7 and 0.8 notes; C-3). Beet land and mills gain value from the same date (C-30, C-31), and the trading houses' and direct importers' firms gain (C-41). Lobbying starts at once (C-22).
- **Imports brought forward (March to December 2026).** Sugar stores well and is expected to sell higher after January (A-10), so imports at 25% rise in 2026 (C-7), stocks are high on 31 December 2026 (C-8), the 2026 revenue rises (C-9) and port storage is in demand (C-44). In early 2027 these stocks are drawn down; by the CR-12e response argument they cannot hold the domestic price below the counterfactual, but whether the price is strictly higher in the first months depends on the size of the stocks, which the case does not give, so C-1's short horizon is read as starting once the stocks bought ahead are used.
- **Within each quota year.** Licences are lost on 30 September (K4), so they are used or sold before it (A-18): imports from October to December fall below the counterfactual's even flow (C-10) and stocks are high at 30 September (C-11), with storage demanded each summer (C-44). January to September is ambiguous (C-12). Under U1-a, surrendered quantities are reallocated on application late in the year (C-15, C-16); under U1-b they lapse. Licence lease prices may fall as 30 September approaches for holders who have not yet used them (a path note, not signed).
- **Supply response.** Domestic supply responds through beet rotations (one year in four) and spare mill capacity (A-16), then through new capacity (C-21). The price stays above the counterfactual over five years (A-3) and, less surely, over ten (A-26).
- **The 2031 review.** Investors expect the act to last at least to 2031 (A-11); a change in the volume would move share, land and mill values when it becomes expected (CR-7c, CR-10c).
- **Relation to the flat tariff the act replaces.** This is not a repeal: the counterfactual keeps the 25% tariff. Against it, the act (i) keeps and raises the domestic price premium over the world price (C-1, C-2); (ii) moves most of the premium on in-quota sugar from the budget (25% duty) to licence holders (C-3, C-4, C-5); (iii) cuts imports further (C-6) and raises domestic production further (C-20, C-29). No effect of the flat tariff is reversed.
- **Price signals (CR-11a).** The in-quota quantity no longer responds to world prices, so domestic buyers' price stops conveying changes in world scarcity on the quota margin; only the out-of-quota margin, if used, still links them. No variable is signed for this.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-6 | importers; sellers.foreign.sugar | quantity_traded (sugar imports, quota years) | decrease | Imports that buyers and foreign sellers each expected to gain from | CR-5a |
| C-15 | importers.prospective | compliance_cost (applications) | U1-a: increase; U1-b: no_change | Time and money spent seeking surrendered quantities | CR-8c |
| C-22 | organized_groups | lobbying_effort | increase | Staff time and money spent lobbying | CR-8c |
| C-23 | officials.licence_office | enforcement_cost | increase | Budget that would have served other uses | CR-8c |
| C-24 | officials.customs | enforcement_cost | increase | Customs time on two rates, licences and mixtures | CR-8c |
| C-25 | importers | compliance_cost | increase | Fees and records | CR-8c |
| C-34 | manufacturers.home_market | quantity_traded (sugar-containing goods, home market) | decrease | Sales lost to foreign goods | CR-5a, CR-8a |
| C-36 | manufacturers.exporting | quantity_supplied (food exports) | decrease | Export sales not made | CR-5a |
| C-39 | households | resources_available_other_uses | decrease | Other purchases forgone to pay more for sugar | CR-8a |
| C-45 | taxpayers / recipients of other spending | resources_available_other_uses | at_least_one_decrease | Revenue lost and the licence office's budget | CR-8b |

CR-8a: land, labor and capital drawn into beet and mills (C-29, C-32, C-21) are withdrawn from the uses their owners would otherwise have chosen; which uses is not signed.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | At the old landed price (about $550 a tonne, white), demand for imports would exceed 400,000 t. | binding | 0.9 | Imports about 650,000 t; consumption growing. | The quota does not bind: C-1 to C-4, C-14, C-18, C-20, C-27, C-28, C-31, C-33, C-39 to C-41, C-43 fail. |
| A-2 | Customs enforce the out-of-quota rate and licence limits. | enforcement | 0.85 | Customs controls at three ports; register. | As A-1, and C-5, C-6, C-17. |
| A-3 | Domestic supply cannot expand at the old cost enough to replace the cut imports within five years. | durability | 0.8 | Beet rotations; mills at 90%. | C-1, C-27, C-31: the price is not reversed but may not stay above $550 (CR-12 0.9). |
| A-4 | Foreign supply comes from many exporters, and no exporting country administers a share of the quota. | other | 0.85 | 1.2% of world trade; licences go to domestic importers. | C-3, C-4: part of the rent goes abroad. |
| A-5 | Kestrany's import cut moves the world sugar price by more than a negligible amount. | other | 0.15 | 250,000 t against about 55 million t. | Below cut-off: not used. |
| A-6 | Licences and shares trade and lease at low cost. | mobility | 0.8 | $200 fee; registry. | C-4, C-13, C-14, C-40, C-42 fail. |
| A-7 | Holders value licences differently. | other | 0.8 | Refining against trading margins. | C-13 fails. |
| A-8 | Domestic food manufacturers compete at home with imported sugar-containing goods not covered by the act. | substitutability | 0.8 | Imports hold about a quarter of the market. | C-33 loses a chain; C-34, C-35, C-37 fail; C-46, C-47 lose a chain. |
| A-9 | Food exporters sell at prices set in world markets. | substitutability | 0.75 | Export contracts. | C-33 loses a chain; C-36 fails; C-46, C-47 lose a chain. |
| A-10 | Sugar can be imported ahead in 2026 at 25% and stored into 2027, and is expected to sell higher after January. | expectations | 0.85 | Sugar stores well; port warehouses. | C-7 to C-9, C-44 fail. |
| A-11 | Investors expect the act to last at least until the 2031 review. | expectations | 0.75 | No expiry; statements. | C-3, C-21, C-30, C-31 shrink to the expected duration; signs hold. |
| A-12 | Glucose syrup and other sweeteners substitute for sugar in some industrial uses. | substitutability | 0.65 | Soft drinks and baking use both. | C-19, C-38 fail. |
| A-13 | Glucose syrup supply cannot expand at once. | durability | 0.6 | Two wet mills near capacity. | C-38 fails. |
| A-14 | Some sugar can be imported as mixtures classified outside the sugar heading at a lower duty. | other | 0.6 | Customs nomenclature. | C-17 fails. |
| A-15 | The quota rent per tonne is larger for white sugar than for raw. | other | 0.6 | Ad valorem rates on a higher white price. | C-42, C-43 lose a chain. |
| A-16 | Growers can move land to beet within the mills' haul radius, and the mills have about 10% spare capacity. | alternative_uses | 0.75 | Rotations; mill capacity. | C-20, C-28 to C-30, C-32 fail. |
| A-17 | Licence holders, growers, manufacturers and would-be importers can organize at a cost below their stakes. | other | 0.85 | Associations; 2026 hearings. | C-22 fails. |
| A-18 | Holders use or sell their licences before 30 September, so that October to December imports fall below the counterfactual's even flow. | other | 0.75 | Surrender rule; small out-of-quota imports. | C-10, C-11 fail. |
| A-19 | Some licence volume is left unused and unsold on 30 September each year. | other | 0.6 | Trading frictions; forecasting errors. | C-15, C-16 fail. |
| A-20 | Under U1-a, applications for surrendered quantities exceed them, and the Minister's rules allocate them otherwise than by price. | other | 0.65 | Rent over $100 a tonne; open registration. | C-15, C-16 fail. |
| A-21 | The change in imports is not offset by capital flows within the medium term. | other | 0.6 | Floating rate; capital account. | C-46, C-47 lose a chain. |
| A-22 | For the importing firms, the quota rent far exceeds the trading margin on the volume they lose. | other | 0.85 | Rent above $100 a tonne on 400,000 t against $15 a tonne on 250,000 t. | C-41 becomes ambiguous. |
| A-23 | Employment and hours in food manufacturing, mills and beet farming adjust with output. | alternative_uses | 0.75 | Labor per tonne. | C-32, C-37 fail. |
| A-24 | Households keep buying sugar at the higher price. | other | 0.75 | Household surveys. | C-39 fails for households who cut purchases. |
| A-25 | Out-of-quota imports stay below 200,000 t a year. | other | 0.85 | Import demand at $704 well below 650,000 t. | C-5, C-6 rest on the price chain alone; C-45 loses a chain. |
| A-26 | Even over ten years domestic supply cannot replace the cut imports at the old cost, while consumption grows. | durability | 0.6 | Land within reach; cost of a new mill. | C-2: price not reversed but may return to $550. |
| A-27 | The licence office's budget is raised with its task. | revenue_use | 0.6 | Budget practice. | C-45 loses a chain. |
| A-N1 | At the higher expected price, some expansion or debottlenecking of mill capacity becomes worthwhile for the processors before 2031. | alternative_uses | 0.6 | NEW. Mills at 90% with about 10% spare (A-16); a price premium of $100 or more a tonne expected to last to 2031 (A-11); A-26 says capacity cannot fully replace imports, not that none is added. Flagged: added by this analysis. | C-21 fails. |

**Not reported** (an assumption below 0.5):
- The world sugar price falls because of Kestrany's import cut, and foreign exporters receive less per tonne (CR-6 0.7 note on a wider-market price; CR-9): needs A-5 (p 0.15). The direction is a priori; the size is taken as negligible.

## 11. Report

**The policy:** From 1 January 2027 Kestrany replaces its flat 25% tariff on sugar with 2% on up to 400,000 t a year covered by licences and 60% on everything else. Permanent shares of the 400,000 t go to the nine firms that imported in 2023 to 2025, in proportion to their imports; licences are issued each December, can be sold or leased, and are surrendered if unused by 30 September. What happens to surrendered quantities is unclear (U1).

**Visible consequences:** Domestic buyers pay more for sugar, in the short, medium and long run (C-1, C-2); imports fall (C-6). The nine historical importers receive shares worth a large sum (C-3) and licences that lease for more than $100 a tonne (C-4). Tariff revenue falls in the quota years (C-5).

**Invisible consequences:**
- *Domestic producers:* processors receive more (C-27), produce more (C-20) and invest (C-21); growers receive more for beet and grow more (C-28, C-29); land near the mills and the mills gain value from the announcement (C-30, C-31); employment in beet and mills rises (C-32).
- *Manufacturers:* earn less on capital (C-33), lose home sales to imported sugar goods (C-34, C-35), export less (C-36) and employ fewer people (C-37); they use less sugar and more glucose syrup (C-18, C-19), whose price rises at first (C-38). The direct importers face the domestic price as their cost even on their own licences (C-40).
- *Households:* have less to spend on other things (C-39).
- *Importers:* bring imports forward into 2026 at 25% (C-7 to C-9); use licences before 30 September and hold larger stocks then (C-10, C-11); trade licences (C-13); new firms register (C-14); some import as mixtures (C-17). Trading houses' firms gain on balance (C-41).
- *State:* new administrative and customs costs (C-23, C-24), compliance costs (C-25) and fee receipts (C-26); budget payers bear the lost revenue (C-45). Organized groups lobby (C-22).
- *Under U1-a only:* would-be importers spend resources applying for surrendered quantities, allocated otherwise than by price (C-15, C-16).

**Ambiguous effects:** Imports from January to September (C-12): fewer imports overall against licences crowded before the deadline. Vellport refining throughput and the refiners' value as firms (C-42, C-43): licences may move to white imports, while marginal out-of-quota imports may be raw. The exchange rate and other exporters' sales (C-46, C-47): fewer sugar imports against fewer food exports and more imported sugar goods.

**Key conditions:** The quota binds (A-1, 0.9) and is enforced (A-2, 0.85); domestic supply cannot replace the cut imports in five years (A-3, 0.8) or ten (A-26, 0.6); the rent stays at home (A-4, 0.85); licences trade cheaply (A-6, 0.8). One premise was added: some mill capacity is added (A-N1, 0.6).

**What this analysis cannot say:** The domestic price between $550 and $704; how large any effect is; whether the gains to holders, growers and processors outweigh the losses to buyers, manufacturers and the budget; whether the policy is good. Health effects of sugar consumption are out of scope.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | buyers.domestic | price_paid (white sugar, domestic) | increase | short; medium | visible | B | CR-6 (a rule fixes the quantity at the low rate below what is demanded at $550, A-1, A-2; the price rises to ration it; out-of-quota imports at 60% cap it at about $704); CR-12b with CR-12e response argument (domestic supply, glucose and imported goods cannot push it back below $550) and the 0.9 note (the response is partial, A-3) | A-1, A-2, A-3 |
| C-2 | buyers.domestic | price_paid (white sugar, domestic) | increase | long | visible | B | As C-1, with new capacity among the responses; partial response over ten years (A-26) | A-1, A-2, A-26 |
| C-3 | holders (nine 2023 to 2025 importers) | asset_value (quota shares) | increase | short (from 2 March 2026) | visible | B | CR-7c (an asset the policy creates is valued at its expected yields and captured by whoever receives it at creation); CR-10c; CR-7 0.7 and 0.8 notes (the qualifying history was fixed before the act was expected: a windfall); rent not captured abroad (A-4); expected to last (A-11) | A-1, A-2, A-4, A-11 |
| C-4 | holders | right_lease_price (licences) | increase | short; medium; long | invisible | B | CR-6 0.7 note (where a cap fixes the quantity of a good priced in a wider market, the price of the right rations it); CR-12 0.9 (a right that exists only under the policy: increase against none); tradable (A-6) | A-1, A-2, A-4, A-6 |
| C-5 | taxpayers / general budget | tax_revenue (sugar tariff, quota years) | decrease | short; medium; long | visible | B | CR-1 (op 3: 2% in place of 25% on 400,000 t; 60% on the rest); arithmetic on the case's figures: about $3.2 million plus at most about $53 million (under 200,000 t at about $264, A-25) is below $62.5 million | A-2, A-25 |
| C-6 | importers; sellers.foreign.sugar | quantity_traded (sugar imports, quota years) | decrease | short; medium; long | visible | B | CR-6 (the domestic price rises, so fewer imports at 60% are worth making); arithmetic: 400,000 t plus under 200,000 t (A-25) is below 650,000 t; CR-5a (imports that would have taken place do not) | A-2, A-25 |
| C-7 | importers (2026) | quantity_traded (imports at 25%, March to December 2026) | increase | short (announcement window) | invisible | B | CR-10a (a change expected in the future alters choices now); CR-4 (x: import in 2027 at 60% at the margin, y: import now at 25% and store); sugar stores well (A-10) | A-10 |
| C-8 | importers, manufacturers | inventory_held (31 December 2026) | increase | short (announcement window) | invisible | B | CR-10a; CR-7c (stocks are durable assets valued at the expected 2027 price) | A-10 |
| C-9 | general budget | tax_revenue (sugar tariff, March to December 2026) | increase | short (announcement window) | invisible | B | CR-8b on C-7 (more imports at 25%) | A-10 |
| C-10 | importers | quantity_traded (imports, October to December of each quota year) | decrease | short; medium; long | invisible | B | CR-1 0.7 note (a dated removal: the 2% option ends on 30 September for unused licences); CR-4 (x: import after 30 September at 60%, y: before at 2%); timing signed per window (02_ontology.md, 2.5) | A-18 |
| C-11 | importers, manufacturers | inventory_held (30 September of each quota year) | increase | short; medium; long | invisible | B | CR-4 (timing: sugar for the last quarter is imported before the deadline and stored); CR-10a | A-18 |
| C-12 | importers | quantity_traded (imports, January to September of each quota year) | ambiguous | short; medium; long | invisible | B | CR-12b: (+) licences crowded into the months before 30 September (A-18); (-) total imports cut (C-6, A-25) | A-18, A-25 |
| C-13 | holders, registered importers | quantity_traded (transfers and leases of shares and licences) | increase | short; medium; long | invisible | B | CR-7a (licences move from holders who value them less to those who value them more, A-7, until yields are equal net of the $200 fee, A-6); CR-5; CR-12 0.9 (an activity existing only under the policy) | A-6, A-7 |
| C-14 | importers.prospective | entry_rate (firms registered as importers) | increase | short; medium | invisible | B | CR-4 (x: stay out, y: register for $500 to buy or lease licences worth more than $100 a tonne); CR-12 0.9 (registration exists only under the policy) | A-1, A-6 |
| C-15 | importers.prospective | compliance_cost (applications for surrendered quantities) | U1-a: increase; U1-b: no_change | short; medium; long | invisible | B | U1-a: CR-6 (quantities worth a rent are allocated otherwise than by price, A-20; applicants spend to obtain them); CR-8c. U1-b: the quantities lapse; no application exists | A-19, A-20 |
| C-16 | importers.prospective | allocation_by_non_price_criteria (surrendered quantities) | U1-a: increase; U1-b: no_change | short; medium; long | invisible | B | U1-a: CR-6 (the scarce side chooses among applicants by criteria: the Minister's rules, A-20). U1-b: nothing is allocated | A-19, A-20 |
| C-17 | importers | reclassification (sugar imported as mixtures outside the sugar heading) | increase | short; medium; long | invisible | B | CR-4 (x: import sugar at 60% at the margin, y: import a mixture at a lower duty; y made relatively better, since the marginal rate rises from 25% to 60%); A-14 | A-2, A-14 |
| C-18 | manufacturers | quantity_demanded (sugar) | decrease | short; medium; long | invisible | B | CR-4c (at a higher price the last unit is given up); independent chains through substitution to glucose (A-12) and lower output (A-8, A-9); CR-12d | A-1, A-2 |
| C-19 | manufacturers | quantity_substitute (glucose syrup and other sweeteners) | increase | short; medium; long | invisible | B | CR-4 (x: sugar, y: glucose syrup; y made relatively better) | A-12 |
| C-20 | domestic_processors | quantity_supplied (white sugar) | increase | medium; long | invisible | B | CR-4 (x: run as now, y: use spare capacity at the higher price, A-16); CR-7a | A-1, A-2, A-16 |
| C-21 | domestic_processors | investment_target (mill capacity) | increase | medium; long | invisible | B | CR-4 (x: hold capacity, y: expand); CR-10c (the return is expected to last to 2031, A-11); A-N1 | A-11, A-N1 |
| C-22 | organized_groups | lobbying_effort | increase | short (from 2 March 2026); medium; long | invisible | B | CR-4 (x: accept, y: lobby: holders to keep the volume and the 2031 review in their favour, manufacturers to enlarge it, would-be importers over U1 and the §12 rules, growers to keep it); CR-10a; CR-8c | A-17 |
| C-23 | officials.licence_office | enforcement_cost | increase | short; medium; long | invisible | A | CR-1 (op 4: a register of shares, licences and transfers); CR-8c | none |
| C-24 | officials.customs | enforcement_cost (two rates, licence checks, mixtures) | increase | short; medium; long | invisible | A | CR-1 (two rates and a licence check where there was one rate); CR-8c | none |
| C-25 | importers | compliance_cost (registration, transfer fees, licence records) | increase | short; medium; long | invisible | A | CR-1 (op 3: $500 registration, $200 per transfer, records); CR-8c | none |
| C-26 | officials.licence_office | non_tax_receipts (registration and transfer fees) | increase | short; medium; long | invisible | A | CR-8b (every payment is a receipt: the fees in C-25) | none |
| C-27 | domestic_processors | net_price_received (white sugar) | increase | short; medium; long | invisible | B | CR-9 (relation: same market as imported white sugar); CR-6 and CR-12e as in C-1 | A-1, A-2, A-3 |
| C-28 | beet_growers | net_price_received (beet) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: beet input_to white sugar; processors expand, A-16, and bid more for beet); CR-7b (growers within the haul radius have few other buyers, so the gain is shared) | A-1, A-2, A-16 |
| C-29 | beet_growers | quantity_supplied (beet) | increase | medium; long | invisible | B | CR-4 (x: other crops, y: beet; within rotations, A-16); CR-7a | A-16 |
| C-30 | land_owners.haul_radius | asset_value (land within reach of the mills) | increase | short (from announcement) | invisible | B | CR-7c and CR-10c (the expected rise in beet yields, C-28, is captured by owners when the act becomes expected; land is the immobile means, CR-7b) | A-11, A-16 |
| C-31 | domestic_processors | asset_value (mills) | increase | short (from announcement) | invisible | B | CR-7c and CR-10c (expected higher yield, C-27); CR-7b (mills are specific) | A-1, A-2, A-3, A-11 |
| C-32 | workers.beet_and_mills | employment (beet farming and mills) | increase | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to beet and sugar; output rises, C-20, C-29); A-23 | A-16, A-23 |
| C-33 | manufacturers.home_market, manufacturers.exporting | return_on_capital (food manufacturing) | decrease | short; medium | invisible | B | CR-9 (relation: sugar input_to food); CR-7b (manufacturers cannot pass the cost to buyers who can turn to imported goods, A-8, or to world buyers, A-9); independent chains, CR-12d | A-8 |
| C-34 | manufacturers.home_market | quantity_traded (sugar-containing goods, home market) | decrease | medium; long | invisible | B | CR-9 (relation: imported sugar goods substitute, close); CR-4 applied to their buyers (x: domestic goods whose price rises, y: imported goods) | A-8 |
| C-35 | sellers.foreign.sugar_goods | quantity_traded (imports of sugar-containing goods) | increase | medium; long | invisible | B | CR-9 (as C-34, the other side); CR-4a (none switch the other way) | A-8 |
| C-36 | manufacturers.exporting | quantity_supplied (food exports) | decrease | medium; long | invisible | B | CR-4b (x: export at a world price with a higher cost, y: other uses of capacity); CR-7a | A-9 |
| C-37 | workers.food_manufacturing | employment (food manufacturing) | decrease | medium; long | invisible | B | CR-9 and LW-10 (relation: labor input_to food; output falls, C-34, C-36); independent chains, CR-12d | A-8, A-23 |
| C-38 | wet_mills | price_substitute (glucose syrup) | increase | short | invisible | B | CR-9 (relation: glucose substitute for sugar, partial); CR-6 (demand rises against supply that cannot expand at once, A-13) | A-12, A-13 |
| C-39 | households | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-3 (note: households keep buying the burdened good, A-24); CR-8a and CR-8b (what they pay in a higher price goes to holders, processors and growers) | A-1, A-2, A-24 |
| C-40 | manufacturers.direct_importers | price_paid (sugar used, counting the lease value of their own licences) | increase | short; medium; long | invisible | B | CR-3 (the cost of using a licence is the lease it could have earned); CR-6 (the lease price reflects the domestic price) | A-1, A-2, A-6 |
| C-41 | holders.trading_houses (and direct importers as holders) | asset_value (the firm as a whole) | increase | short (from 2 March 2026) | invisible | B | CR-12b: (+) shares (C-3); (-) trading margin lost on lower volume (C-6). Dominance by A-22 (CR-12e, empirical) | A-1, A-2, A-22 |
| C-42 | holders.refiners | quantity_supplied (white sugar refined at Vellport) | ambiguous | short; medium; long | invisible | B | CR-12b: (-) licences move to white imports where the rent per tonne is larger (A-15, A-6) and total imports fall (C-6); (+) out-of-quota raw sugar lands at about $576 and may be the cheaper marginal import once refined; the cost of refining is not in the case | A-6, A-15, A-25 |
| C-43 | holders.refiners | asset_value (the firm as a whole) | ambiguous | short (from 2 March 2026) | invisible | B | CR-12 0.8 kind (3): (+) shares (C-3); refinery value follows C-42, itself ambiguous; A-22 covers the trading margin only, so no dominance premise covers a fall in refining | A-1, A-2, A-15 |
| C-44 | port_warehouses | price_complement, quantity_complement (storage) | at_least_one_increase | short (2026; each summer) | invisible | B | CR-9 (relation: storage complement of stock-building, C-8, C-11); CR-6 0.9 (a rise in demand; the split between price and quantity needs a premise, so a group) | A-10 |
| C-45 | taxpayers / recipients of other spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | B | CR-8b and the CR-8 0.7 note (a budget shortfall is met by someone: higher taxes, less other spending or borrowing); chains: lost revenue (C-5, A-25) and the licence office's budget (A-27); CR-12d | A-25 |
| C-46 | exporters.other | quantity_traded (timber, machinery, tourism) | ambiguous | medium; long | invisible | B | CR-9 (currency link) and CR-12b: (-) fewer sugar imports give foreigners less means to buy exports (C-6, A-21); (+) fewer food exports (C-36) and more imported sugar goods (C-35) work the other way | A-8, A-9, A-21 |
| C-47 | all | exchange_rate | ambiguous | medium; long | invisible | B | As C-46 | A-8, A-9, A-21 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-047-C1: Which out-of-quota good (raw or white) is the marginal import, and so how refining throughput moves (C-42). The rules give the direction for each good, but comparing the two landed costs needs the cost of refining, a figure, not a rule. Recorded as ambiguous.
- GAP-047-C2: The price in the first months of 2027, while stocks bought ahead in 2026 are drawn down. CR-12e gives "not below the counterfactual", and the 0.9 note says "increase" needs a partial response, but the stock is finite and its size unknown; no rule says how to sign a window bounded by a stock rather than by a date.

**(b) Core-rule wording that was hard to apply.**
- CR-6 0.7 note on a fixed quantity priced in a wider market fits a domestic quota on a traded good, but here the quantity fixed is the quantity at the low rate, with unlimited imports at a higher rate. The domestic price is then set either by the quota (below $704) or by the out-of-quota landed price; which applies depends on demand at $704, which the rules leave to arithmetic the case cannot complete.
- CR-7c and the 0.7 note on claims before creation: the act publishes the base period with the bill, so "becomes expected" and "creation" coincide for the windfall; the rule does not say whether the windfall dates from proposal (2 March) or enactment (10 June). Dated from proposal, with the share of value rising as passage became more likely.
- CR-12e: A-22 compares the rent with the trading margin; for refiners the lost margin is a refining margin. The rule allows a dominance premise but does not say how far a premise's wording extends to a related quantity; read narrowly (C-43 ambiguous).
- CR-1 0.7 on dated operations: K4 removes an option on a date every year, and under U1-a adds another (applications) on the same date. The per-window convention fits, but the rule does not say how to sign a window (January to September) where a dated removal and the overall cut push opposite ways (C-12).

**(c) Vocabulary missing from the ontology.**
- No variable for the composition of imports (raw against white); `quantity_supplied` of refined sugar was used.
- No actor class for holders of a created right distinct from current sellers; `holders` was coined.
- No variable for the value of a firm as a whole as distinct from a single asset; `asset_value (the firm as a whole)` was used.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the core of the case: the domestic sugar price rises in the short, medium and long run (by the response argument with a partial-response premise), imports fall, the nine historical importers receive a windfall captured from the proposal date, licences lease at a positive price and are traded, domestic growers and processors gain and expand, beet land and mills gain value, manufacturers lose sales to imported sugar goods and exports, glucose syrup substitutes at a higher price, the timing effects around 2026 and each 30 September, the per-reading effects of U1, tariff revenue falls and is made up by a group, and the currency link is `ambiguous`. Both reach the price rise without the single-rate tariff pattern: the core version from CR-6 applied to the quantity fixed at the low rate, which confirms the pattern version's verdict that TX-7 fails on a two-rate tariff. The differences are mostly omissions on both sides, plus five sign differences. Two are core errors: Vellport refining throughput is `ambiguous` in the core version although its own premises A-15 and A-25 sign it as a decrease, and its registrations of new importers rise for a reason that misapplies CR-7a. One is a pattern error: the firms' value rises for the refiners on a premise (A-22) that covers only trading margins. Two are judgment calls on group against single signs for labor. The pattern version's EN-13 sign on the number of active importers is against the initial allocation, not the counterfactual.

Counts: M 27, V 8, S 5, OP 7, OC 5.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | none | OC | E | Licence holders' in-quota landed cost falls (25% to 2%; CR-1 op 3). Core omission: stated as an operation in section 2, not recorded. |
| C-2 | none | OC | E | Out-of-quota landed cost rises (25% to 60%). Core omission, as C-1. |
| C-3 | C-3 | M | | |
| C-4 | C-6 | M | | Pattern by the response argument (A-3); core by arithmetic on A-25. Independent chains, same sign (CR-12d). |
| C-5 | C-1 | M | | Both from the marginal rate. The core version notes (GAP-047-C2) that stocks bought ahead in 2026 are a response A-3 does not cover; the pattern's short horizon "from 1 January 2027" needs a premise that those stocks do not cover the shortfall in the first months (CR-12 0.9: a partial response). |
| C-6 | C-27, C-28 | V | | Split into processors (white sugar) and growers (beet). |
| C-7 | C-20, C-29 | V | | Split; core horizon medium and long, pattern from the 2026 sowing. |
| C-8 | C-4 | M | | |
| C-9 | C-13 | M | | |
| C-10 | none | OC | P | Pattern: fewer firms actively import (EN-13). EN-13 signs the number of users against the initial allocation (every holder active), not against the counterfactual. Here licences may be leased to any registered importer, so high-value users outside the nine (manufacturers importing directly) can raise the count. The decrease needs a premise that the high-value users are among the nine and that lessors stop importing. Pattern as written (baseline); core omitted the key. |
| C-11 | C-14 | S | E | Pattern: total entry U1-a `ambiguous`, U1-b `decrease`. Core: registrations increase under both readings, because firms "register for $500 to buy or lease licences worth more than $100 a tonne". A firm that buys or leases a licence at its market price pays the rent (CR-6, CR-7a), so the licence's value is no reason to register; the core sign holds only in the trivial sense that a register exists only under the act (CR-12 0.9), which is not entry into importing. Core error. The pattern's U1-b decrease holds through the smaller import volume and the new fees, not through "must buy licences", which treats the lease price as a barrier. |
| C-12 | C-14 (part) | V | | Registrations to apply for surrendered tonnes under U1-a; the core records a wider item (all registrations). |
| C-13 | C-16 | M | | |
| C-14 | C-15 | M | | |
| C-15 | C-11 | M | | |
| C-16 | C-10 | M | | |
| C-17 | C-12 | M | | |
| C-18 | C-7 | M | | |
| C-19 | C-8 | M | | |
| C-20 | C-18 | V | | Core signs manufacturers only; households' quantity is not signed (A-24 is about their spending). CR-4c gives the household decrease too. |
| C-21 | C-19 | M | | |
| C-22 | C-38 | M | | |
| C-23 | C-17 | M | | |
| C-24 | none (a chain of core C-42) | OC | E | Share of white sugar in in-quota imports rises: a licence counts tonnes, and with A-15 the rent per tonne is larger for white (CR-4c with the tonne as the unit). The core version uses this only as a chain of C-42 and notes it lacks a variable for import composition. Core omission. |
| C-25 | C-42 | S | E | Pattern: refining of imported raw sugar decreases. Core: `ambiguous`, with out-of-quota raw at the margin as a (+) chain. With A-15 every holder faces the same white price, so every licence goes to white (a corner, not a share); raw then enters only out of quota, below 200,000 t (A-25), against 450,000 t now. The decrease follows by arithmetic on two premises the core version itself lists. Core error. The pattern version omits A-25 from C-25's premises, and its "If false" for A-15 ("rests on lower imports alone") is wrong: lower total imports do not sign raw imports. |
| C-26 | C-22 | M | | |
| C-27 | C-34, C-36 | V | | Output split into home sales and exports. |
| C-28 | C-37 | S | J | Pattern: employment or hours, as a group. Core: employment decrease. A-23 ("employment and hours adjust with output") can be read as covering each; both defensible. |
| C-29 | C-35 | M | | |
| C-30 | C-36 | M | | |
| C-31 | C-46 | M | | Same sign. The core version adds a chain the pattern version dismissed: fewer food exports leave foreign buyers' means for other exports (CR-9 0.7: exporters of different goods compete for the same foreign means). The pattern's "not in foreigners' means" is wrong, though the sign is unchanged. |
| C-32 | C-30 | M | | |
| C-33 | C-31 | M | | |
| C-34 | C-33 | V | | Pattern signs manufacturers' asset value; core their return on capital. CR-7c would carry the core's sign to the asset. |
| C-35 | C-41, C-43 | S | P | Pattern: every importing firm's value rises, by A-22 (rent far exceeds the trading margin on lost volume). Core: trading houses and direct importers increase (C-41, matching), refiners `ambiguous` (C-43). The refiners lose refining throughput (pattern C-25 itself), and the refining margin on it is not in the case; A-22's evidence is the $15 trading margin. Analyst misapplication of a premise beyond its evidence; for refiners there is no dominance premise (CR-12b). |
| C-36 | none | OC | E | Seed, fertilizer and haulage for beet rise (CR-9, LW-10). Core omission. |
| C-37 | C-32 | S | J | As C-28, for mills and beet farms. |
| C-38 | C-39 | M | | |
| C-39 | C-2 | M | | |
| C-40 | C-5 | M | | |
| C-41 | C-45 | M | | |
| C-42 | C-23 | M | | |
| C-43 | C-45 | V | | Core merges the licence office's funding into the general-budget group. |
| C-44 | C-25 | M | | |
| C-45 | C-6, C-18 | V | | Purchases not made, recorded by the core on imports and manufacturers' quantity. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-9 | OP | E | Tariff revenue in March to December 2026 rises with the imports brought forward at 25% (CR-8b on C-7). Pattern omission; its C-40 covers the quota years only. |
| C-21 | OP | E | Processors invest in mill capacity (CR-4, CR-10c, A-N1). Pattern omission: its C-39 text names new mill capacity but records nothing. |
| C-24 | OP | E | Customs' enforcement cost rises (two rates, licence checks, mixtures; CR-8c). Pattern omission: its OC-3 note says only that customs work "does not fall". |
| C-26 | OP | E | Licence office receives registration and transfer fees (CR-8b). Pattern omission. |
| C-40 | OP | J | Direct importers' cost of sugar, counting the lease value of their own licences, rises (CR-3). The pattern version states this in its text (C-8 paragraph) without recording it. |
| C-44 | OP | E | Port storage, price or quantity as a group, rises in 2026 and each summer (CR-9, CR-6 0.9). Pattern omission. |
| C-47 | OP | J | Exchange rate `ambiguous`. The pattern version records the currency link only through export industries (C-31); recording the link variable is a choice. |

### Findings

- **Pattern overclaims or hidden premises.** C-35: A-22 (rent against the trading margin) was stretched to the refiners, who lose a refining margin the case does not give; their firm value is `ambiguous`. C-10: EN-13's decrease in users is against the initial allocation; against the flat-tariff counterfactual, with licences leasable to any registered importer, it needs a premise that the high-value users are among the nine. C-5 (short horizon): stocks bought ahead in 2026 are a response the partial-response premise A-3 does not cover, so the first months of 2027 need their own premise. C-11: the reasoning treats the lease price as a barrier to entry; the sign survives on other grounds.
- **Errors in the core version.** C-42: A-15 implies every licence goes to white (all holders face the same price), and A-25 then caps raw imports below 200,000 t against 450,000 t, so refining throughput decreases; GAP-047-C1 is not a gap. C-14: the rise in registrations was justified by the licences' value, which a buyer or lessee pays for at the market price (CR-7a). Omissions: the two landed costs (C-1, C-2), the number of active importers, the white share of in-quota imports, and beet input suppliers.
- **Errors in the pattern version (omissions).** 2026 tariff revenue, mill investment, customs' enforcement cost, licence fee receipts, port storage, direct importers' opportunity cost (recorded only in text), and the fewer-food-exports chain in the currency link (C-31).
- **Test of 0.9 verdicts against the core-only version.** "Failed": TX-7 on a two-rate tariff: confirmed. The core version derived the price rise from CR-6 applied at the marginal quantity and treated the in-quota cut as a change in who receives the gap (C-4, C-5), exactly the reading the pattern version had to impose on TX-7. "Needed interpretation": EN-6 for a tariff-rate quota: confirmed; the core version hit the same difficulty with CR-6's 0.7 note on a fixed quantity priced in a wider market (its Gaps found, b). EN-6 0.9 Inputs clause fitting the output but not the input's price: confirmed; the core version needed no Inputs clause, signing the input's price by CR-6 and the output by CR-9 and CR-7b. CR-1 0.9 for a threshold on a total allocated by licences: not confirmed as a difficulty; the core version recorded operation 3 per class (holders' licensed tonnes, everyone's other tonnes) under CR-1's ordinary recording rule without the 0.9 clause. CR-12 0.9 on the response argument ("worked as written"): partly contradicted. The core version found the 2026 stocks to be a response with no partial-response premise (GAP-047-C2), which bears on the pattern's short-run C-5.
- **Limits of the core rules.** No K. GAP-047-C1 is closed by A-15 and A-25 (above). GAP-047-C2 is real wording: CR-12 0.9 says a partial response is needed to report `increase`, but not how to sign a window in which a finite stock built in response holds the price, which needs a premise on the stock's size or a horizon that starts when it runs out. Unclear wording: CR-6's 0.7 note on a fixed quantity priced in a wider market does not cover a quantity fixed only at a lower rate (a quota on the rate, not on imports); the CR-12e scope of a dominance premise (A-22) over a related margin. The core version's doubt over whether the windfall dates from proposal or enactment is answered by CR-7c's probability clause, which both versions applied.
