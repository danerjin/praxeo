# WE-013 / Analysis: Halvern Steel Safeguard Order (25% tariff on imported steel)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Every derivation below cites only the core rules (CR-1 to CR-12, with clause), the foundations (AX-1, LW-1 to LW-10) and arithmetic. Assumptions A-1 to A-14 are the case assumptions as given; A-N1 and A-N2 are premises this re-run had to add.

## 1. Policy record

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Halvern, a mid-sized trading country with its own currency and a floating exchange rate; buys a small share of the world's steel. Outside: foreign steel mills, foreign makers of fabricated steel and finished goods. | Policy record preamble. |
| Announced / enacted / effective / expires | Investigation opened in September; recommendation published 1 January; order effective 1 April; three years, with a possible extension at a third-year review. | "The Trade Ministry opened an investigation in September, published its recommendation on 1 January, and the order took effect on 1 April." |
| Enforcement (who, penalties, resources) | Customs Service (classification checks at ports, penalties for misdeclaration); Ministry of Industry exclusion office. | K3. |
| Starting conditions | Three domestic firms (two integrated mills, one electric-arc mini-mill) employ about 18,000 and supply about 60% of steel used; the rest imported. About 4,000 steel-using manufacturers employ about 250,000; machinery makers export about 35% of output. Other large export industries: grain and tourism. | Policy record preamble. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Tariff | `tariff` (ad valorem) | Imports of flat-rolled and long steel products | Importers of record | 25% of the customs value, for three years. A review in the third year may extend it. | Imported fabricated steel products and finished goods containing steel (machinery, vehicles, appliances, fabricated structural sections, fasteners) are not covered. |
| K2 Product exclusions | Discretionary exemption | Specific steel products | Ministry of Industry | Steel users may apply to exclude a product "not produced domestically in sufficient quantity or quality". Domestic steelmakers may object. Decisions are due within 90 days; exclusions last one year and must be renewed. | None |
| K3 Enforcement | Enforcement | K1, K2 | Customs Service; Ministry of Industry exclusion office | Classification checks at ports; penalties for misdeclaration. | None |

Revenue use: general budget. Its spending is out of scope.

Existing rules: none recorded in the input.

Unclear provisions: the standard for "sufficient quantity or quality" in K2. Assumed to be applied case by case, with weight given to objections from domestic producers (A-5).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 | Binary (tax on importers) and triangular (domestic mills' sales protected from foreign rivals) | Binds: imports remain a meaningful share and foreign sellers do not absorb most of the tariff (A-1) | CR-1, CR-4, CR-5a, CR-7, CR-8, CR-9, CR-10 |
| K2 | Adds an option (exemption) at a procedural cost; gives mills an option to object | Binds where users apply; outcome case by case (A-5) | CR-1 op 2, op 3; CR-4 (x: accept, y: lobby); CR-8c |
| K3 | Enforcement | Smuggling and false origin judged rare (A-12, p 0.3); reshaping into exempt forms is legal (A-3) | CR-1, CR-4 (x: covered form, y: uncovered form) |

**CR-1 operations by component and actor class.** Operations: (1) remove an option, (2) add an option, (3) change what an option brings, (4) transfer means.

| Actor class | K1 | K2 | K3 |
|---|---|---|---|
| `importers.steel` | 3 (importing covered steel carries a 25% payment); 4 (the payment transfers their means to the budget) | 2 (excluded products enter free) | 3 (classification checks, risk of penalties) |
| `steel_users` (all manufacturers and builders using steel) | none directly; reached through the price of steel (CR-9) | 2 (they may apply), 3 (application costs and one-year renewal) | none |
| `mills.domestic` | none directly; their rivals' option worsens (CR-9) | 2 (they may object to exclusions) | none |
| `foreign_mills` | 3 (sales to Halvern now bring less or are fewer) | none | none |
| `foreign_fabricators` | none; their exempt products improve relative to covered steel (3, relative) | none | none |
| `officials.enforcement` (Customs, exclusion office) | none | 3 (applications to decide) | 3 (checks; means used up, CR-8c) |
| `government.budget` | 4 (receives the revenue) | none | none |
| Exporters in other industries, buyers of construction, workers | none directly; reached through CR-9 | none | none |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `importers.steel` | Importers of record of covered steel | Pay 25% on covered imports; can reshape, buy ahead, apply for exclusions |
| `steel_users` | All domestic buyers of steel, split where it matters: | Steel costs more |
| `steel_users.import_competing` | Makers of machinery, parts, appliances, cans that compete at home with untaxed imported finished goods (A-7) | Cannot pass the cost on fully |
| `steel_users.exporters` | Machinery makers selling abroad (35% of output) | Sell at prices set abroad (A-N1) |
| `buyers.construction` | Buyers of buildings and structures | Pay more where steel is a material cost (A-14) |
| `workers.steel_using` | About 250,000 in steel-using firms | Demand for their labor falls (CR-9) |
| `mills.domestic` | Three domestic steel firms | Can raise prices and output (A-2) |
| `owners.mills` | Shareholders of domestic mills | Asset value rises at expectation (CR-7c) |
| `workers.mills` | About 18,000 mill workers | Demand for their labor rises |
| `foreign_mills` | Foreign sellers of covered steel | Sell less to Halvern; other markets open (A-1) |
| `sellers.substitutes` | Foreign makers of fabricated products and finished goods | Untaxed products gain (A-3, A-7) |
| `exporters.other` | Grain and tourism exporters | Reached through the foreign-exchange market (A-8) |
| `producers.other_domestic` | Domestic firms competing with mills for labor, energy and capital | Means drawn away from them (CR-8a) |
| `lobby.steel` | Mills and users, organized (A-6) | Stake in exclusions and renewal |
| `officials.enforcement` | Customs; exclusion office | More checks and applications |
| `government.budget` | General budget | Tariff revenue |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | steel_users | price_paid (imported steel) | increase | short | CR-1 op 3; CR-7b (Halvern buys a small share of world steel and foreign mills have other markets, so foreign sellers are the side with alternatives and the burden settles on Halvern buyers) | A-1 |
| C-2 | government.budget | tax_revenue | increase | short | CR-1 op 4; CR-8b | A-1 |
| C-3 | importers.steel | quantity_traded (covered steel imports, from 1 April) | decrease | short | CR-4c (x: import the last unit, y: not); CR-5a (imports that would have taken place are prevented) | A-1 |
| C-4 | mills.domestic | net_price_received | increase | short | CR-9 (close substitute); CR-7a (the price of a close substitute is brought into line with the dearer import); CR-5c | A-1, A-2 |
| C-5 | steel_users | price_paid (domestic steel) | increase | short | CR-9 (close substitute); CR-7a | A-1, A-2 |
| C-6 | mills.domestic | quantity_supplied | increase | short | CR-4c (mirror case: selling more is now better); spare capacity | A-1, A-2 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | importers.steel | quantity_traded (covered steel imports, 1 January to 31 March) | increase | short | CR-10a (the tariff became expected on 1 January); CR-4b (x: import after 1 April, y: import before) | A-4 |
| C-8 | steel_users | inventory_held (steel stocks on 1 April) | increase | short | CR-10a; CR-4b (x: buy later, y: buy now and store) | A-4 |
| C-9 | importers.steel | reclassification (steel lightly fabricated abroad to fall outside K1) | increase | short | CR-4b (x: covered form, y: uncovered form); arithmetic (pays when fabrication costs less than 25%) | A-3 |
| C-10 | steel_users | compliance_cost (exclusion applications and yearly renewals) | increase | short | CR-1 op 2 and op 3 (an exclusion is an added option with a procedural cost attached); CR-8c | A-5 |
| C-11 | lobby.steel | lobbying_effort (on exclusions and renewal) | increase | short | CR-4b (x: accept, y: lobby), for mills and for users | A-6 |
| C-12 | steel_users.import_competing | return_on_capital | decrease | medium | CR-3a; CR-7b (they cannot pass the cost to buyers who can switch to untaxed imported finished goods, so the burden settles on them) | A-1, A-7 |
| C-13 | steel_users.exporters | quantity_supplied (exports of machinery) | decrease | medium | CR-4c (higher cost at an unchanged foreign price makes the marginal export unprofitable); CR-7b | A-1, A-N1 |
| C-14 | mills.domestic | investment_target | increase | medium | CR-7a (capital moves toward the higher yield); CR-10a, CR-10c (investment whose payback depends on the tariff lasting goes ahead to the extent it is expected to) | A-2, A-10, A-11 |
| C-15 | steel_users | capital_stock_target (domestic steel-using plants) | decrease | long | CR-4b (x: replace the plant here, y: there), CR-10b (only at replacement) | A-1, A-9, A-10 |
| C-16 | government.budget | tax_revenue_vs_static_projection | decrease | short | CR-4c (imports fall, C-3); CR-4b (reshaping, C-9); arithmetic | A-1 |

## 6. Second-order effects

Market relations: `imported_steel` and `domestic_steel`: `substitute`, close (A-2). `steel` and `steel_using_goods`, `construction`: `input_to`, close (A-14). `domestic_steel_using_goods` and `imported_finished_goods`: `substitute`, close (A-7). `covered_steel` and `lightly_fabricated_steel`: `substitute`, partial (A-3). `steel_imports` and `other_exports`: linked through the foreign-exchange market, recorded as `across_border` with the note "currency: importers' sales of crowns are exporters' purchases of crowns" (A-8). `mill_output` and `mill_labor`: `input_to` (labor is an input).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | owners.mills | asset_value (shares in domestic mills) | increase | short | CR-7c (a lasting rise in expected yield is captured by owners when it becomes expected, 1 January); CR-10c | substitute; depth 2 | A-1, A-2, A-11 |
| C-18 | workers.mills | employment | increase | medium | CR-9 (input_to; LW-10: demand for labor follows demand for its product) | input_to; depth 2 | A-1, A-2 |
| C-19 | steel_users.import_competing | quantity_supplied | decrease | medium | CR-9 (substitute); CR-4b for their buyers (x: domestic good, y: untaxed imported good) | substitute; depth 2 | A-1, A-7 |
| C-20 | sellers.substitutes | quantity_substitute (imported fabricated steel and finished goods) | increase | medium | CR-4b for Halvern buyers (x: domestic good, y: imported good); CR-9 | substitute; depth 2 | A-1, A-7 |
| C-21 | workers.steel_using | employment | decrease | medium | CR-9 (input_to; LW-10) from C-13 and C-19 | input_to; depth 3 | A-1, A-7 |
| C-22 | buyers.construction | price_paid (buildings and structures) | increase | medium | CR-9 (input_to); CR-7a | input_to; depth 2 | A-1, A-14 |
| C-23 | buyers.construction | quantity_demanded | decrease | medium | CR-4c | input_to; depth 3 | A-1, A-14 |
| C-24 | exporters.other | net_price_received (crowns per unit exported) | decrease | medium | CR-9 (importers buy less foreign currency and so offer fewer crowns; CR-6: the crown's price in foreign money moves toward the level at which crowns offered and sought are compatible, so it rises; exporters receive fewer crowns for the same foreign price) | across_border (currency); depth 3 | A-1, A-8 |
| C-25 | exporters.other | quantity_supplied (grain and tourism exports) | decrease | medium | CR-4c | across_border (currency); depth 4 | A-1, A-8 |
| C-26 | foreign_mills | quantity_traded (sales to Halvern) | decrease | short | CR-5a (exchanges prevented); CR-4b (x: sell to Halvern, y: other markets) | substitute; depth 1 | A-1 |

Interaction of components. K2 opens an exit from K1 product by product, and lets mills raise the cost of that exit by objecting (C-10, C-11). K1's exemption of fabricated and finished goods opens two exits: reshaping imports (C-9) and buying finished goods abroad (C-20); the second is what turns the cost increase to steel users into lost sales (C-19). Machinery exporters are reached twice: through dearer steel (C-13) and, if A-8 holds, through a dearer crown (same direction; not separately signed, see section 7).

Stopping points. The construction chain stops at C-23 (depth 3): effects on renters and occupants would be diffuse. The currency chain stops at C-25 (depth 4).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| importers.steel, quantity_traded | Window 1 January to 31 March: buying ahead (C-7) | From 1 April: tariff (C-3) | Different time windows, signed separately (normal form, timing shifts) | C-7 increase; C-3 decrease |
| steel_users.exporters, quantity_supplied, medium | none | Dearer steel (C-13); dearer crown (A-8) | Same direction; CR-12a | decrease (C-13) |
| mills.domestic, investment_target, medium | Higher expected yield (C-14) | none | Long-payback investment depends on renewal (A-10, p 0.55), so this sign is less certain than the price signs | increase (C-14) |
| workers.mills employment vs workers.steel_using employment | C-18 | C-21 | Different actor classes; not netted (CR-12c). The method cannot say whether total employment rises or falls | separate |

## 8. Time structure

Horizons: short = 1 January (recommendation) to the end of the first year of the tariff; medium = years 2 and 3 (the tariff's term); long = beyond the year-three review.

- **Announcement (CR-10a, CR-7c).** The recommendation of 1 January made the tariff expected. Mill shares rise then (C-17). Users and importers buy ahead and store steel before 1 April (C-7, C-8); imports in the months after 1 April are lower still as stocks are drawn down.
- **Fixed term (CR-10a, CR-10c).** Investment that pays back within three years goes ahead on A-11; investment with longer payback goes ahead only on the expectation of renewal (A-10, p 0.55), which is why C-14 carries A-10.
- **Slow stocks (CR-10b).** Steel users relocate only when plants are replaced (C-15, long). Mill capacity added during the term persists after the tariff ends, and gives the mills a stake in renewal (C-11).
- **Exclusions renew yearly.** Each exclusion must be renewed every year, so the compliance cost recurs (C-10), and users cannot rely on an exclusion for longer than a year.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-27 | steel_users | resources_available_other_uses | decrease | What they pay in higher prices for imported and domestic steel, which they would otherwise have spent or invested elsewhere | CR-8a, CR-8b; CR-3a |
| C-28 | producers.other_domestic | resources_available_other_uses | decrease | The labor, energy and capital that mills draw into added output are withdrawn from uses their owners would otherwise have chosen | CR-8a; CR-7a |
| C-29 | officials.enforcement | enforcement_cost | increase | Customs checks and exclusion decisions | CR-1 op 3; CR-8c |
| C-3, C-26 | importers.steel, foreign_mills | quantity_traded (in sections 4 and 6) | decrease | Imports that would have taken place, and the gains both parties expected from them | CR-5a |
| C-10, C-11 | steel_users, lobby.steel | compliance_cost, lobbying_effort (in section 5) | increase | Resources used up on applications, objections and lobbying | CR-8c |

The mills' gain (C-4, C-17) is visible; its counterpart is the higher price paid by every steel user (C-5, C-27). The tariff revenue (C-2) is a receipt to the budget equal to what importers pay on the steel still imported (CR-8b); its spending is out of scope.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff. | binding | 0.85 | Halvern's small share of world steel demand; foreign mills' other markets. | Nearly every consequence fails or weakens. |
| A-2 | Domestic mills can raise output from spare or idle capacity and produce close substitutes for most imports. | substitutability | 0.75 | Capacity utilization; product range of the three mills compared with imports. | C-4 to C-6, C-14, C-17, C-18 fail. |
| A-3 | Some imports can be reshaped to fall outside the tariff's definitions at a cost below 25%. | other | 0.7 | Customs definitions; cost of light fabrication abroad. | C-9 fails. |
| A-4 | Users and importers can store steel and order ahead. | expectations | 0.8 | Warehouse capacity; order lead times. | C-7, C-8 fail. |
| A-5 | Exclusions are decided case by case, with weight given to objections from the mills. | other | 0.7 | The order's text; the exclusion office's procedures and staffing. | C-10 weakens. |
| A-6 | Steelmakers and users organize to influence renewal and exclusions. | other | 0.85 | Existing industry associations; the investigation's hearings. | C-11 fails. |
| A-7 | Many steel users compete with imported finished goods that are not taxed. | substitutability | 0.8 | Import shares in machinery, appliances and parts; K1 exemptions. | C-12, C-19 to C-21 fail. |
| A-8 | The fall in steel imports is not offset by capital flows or other adjustments within the medium horizon. | other | 0.6 | Floating exchange rate; capital account. | C-24, C-25 fail. |
| A-9 | Some steel-using firms have the option of producing abroad when plants are replaced. | mobility | 0.6 | Firms with foreign plants; plant replacement cycles. | C-15 fails. |
| A-10 | Steelmakers expect the tariff to be renewed at the year-three review. | expectations | 0.55 | Political history of safeguard renewals; the mills' influence. | C-14 shrinks to short-payback investment; C-15 fails. |
| A-11 | Investors expect the tariff to stay in force for at least its three-year term. | expectations | 0.8 | The order's text; government statements. | C-14, C-17 fail. |
| A-12 | Smuggling or false declarations of origin occur on a meaningful scale. | enforcement | 0.3 | Bulk cargo, few ports, inspection rates. | Below cut-off; not used. |
| A-13 | Trading partners retaliate against Halvern's exports. | other | 0.4 | Partners' statements; their past responses. | Below cut-off; not used. |
| A-14 | Steel is a material part of construction costs and builders cannot replace it with other materials at the old cost in the medium run. | substitutability | 0.8 | Steel's share of building costs (reinforcing bar, structural sections); building codes; cost of switching to concrete or timber designs. | C-22, C-23 fail. |
| A-N1 | Halvern's machinery exporters sell at prices set in world markets, so they cannot pass the higher cost of steel to foreign buyers. | substitutability | 0.8 | Halvern's share of world machinery markets; foreign competitors' prices; export contracts in foreign currency. | C-13 fails. |
| A-N2 | Domestic mills price their steel at or near the import price including the tariff, rather than holding prices down to gain share or out of fear of the exclusion office. | other | 0.7 | Mills' pricing behavior in earlier protection episodes; how exclusion decisions weigh domestic prices. | C-4, C-5 weaken; C-17 weakens. |

Note on A-N2. CR-7a gives the direction of the domestic price (toward the import price) a priori once the products are close substitutes (A-2). A-N2 is recorded because K2 links the two: if mills raise prices fully, users can argue that domestic supply is not "sufficient", so mills may hold back. It is not needed for the sign of C-4 and C-5 and is not cited in the consequence list.

## 11. Report

**The policy:** From 1 April, Halvern taxes imports of flat-rolled and long steel at 25% for three years, with a possible extension. Fabricated steel and finished goods containing steel are not taxed. Users can apply, product by product, for one-year exclusions, and domestic mills can object. The tariff was expected from the recommendation of 1 January.

**Visible consequences:** Steel users pay more for imported steel (C-1) and for domestic steel (C-5). Imports fall (C-3). Domestic mills get higher prices (C-4), sell more (C-6), hire more (C-18), and their owners' shares rise in value (C-17). The budget collects revenue (C-2).

**Invisible consequences:**
- *Before the tariff.* Imports rise between 1 January and 1 April and users hold larger stocks on 1 April (C-7, C-8).
- *Avoidance.* Some steel is lightly fabricated abroad to enter untaxed (C-9). Users spend resources on exclusion applications every year (C-10); mills and users lobby (C-11). Revenue falls short of 25% of the old import value (C-16).
- *Steel users.* Makers that compete with untaxed imported finished goods earn less (C-12), produce less (C-19) and employ fewer people (C-21), while imports of finished goods rise (C-20). Machinery exporters sell less abroad (C-13, new premise A-N1). Over the long run, some steel-using plants are replaced abroad rather than at home (C-15).
- *Construction.* Buildings cost more (C-22) and fewer are bought (C-23).
- *Other exporters.* Fewer imports mean fewer crowns offered for foreign money, so the crown is dearer than otherwise and grain and tourism exporters receive fewer crowns (C-24) and export less (C-25).
- *Foreign sellers.* Foreign mills sell less to Halvern (C-26).
- *Unseen costs.* Steel users have less to spend on other things (C-27); the labor and capital drawn into the mills are taken from other uses (C-28); Customs and the exclusion office use resources (C-29).

**Ambiguous effects:** None at the level of a single actor class and variable. The method cannot say whether total employment in Halvern rises or falls: mill jobs (C-18) and steel-using jobs (C-21) are different classes, and are not netted.

**Key conditions:** Almost everything rests on A-1 (the tariff binds and is not absorbed abroad, 0.85). The domestic-price and mill chains rest on A-2 (0.75). The losses to steel users rest on A-7 (0.8) and, for exporters, on the new premise A-N1 (0.8). The currency chain rests on A-8 (0.6). Long-payback mill investment and plant relocation rest on A-10 (renewal expected, 0.55), the weakest premise reported.

**What this analysis cannot say:** How much prices, output or employment change; whether jobs gained in the mills exceed jobs lost elsewhere; whether the policy is good. The spending of the revenue, and health, safety and environmental effects, are not analyzed. Not reported (assumption below 0.5): smuggling and false declarations of origin (A-12, p 0.3); retaliation against Halvern's exports (A-13, p 0.4).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | steel_users | price_paid (imported steel) | increase | short | visible | B | CR-1 op 3; CR-7b (burden settles on the side with fewer alternatives: Halvern buyers, not foreign sellers) | A-1 |
| C-2 | government.budget | tax_revenue | increase | short | visible | B | CR-1 op 4; CR-8b | A-1 |
| C-3 | importers.steel | quantity_traded (covered steel imports, from 1 April) | decrease | short | visible | B | CR-4c; CR-5a | A-1 |
| C-4 | mills.domestic | net_price_received | increase | short | visible | B | CR-9 (substitute); CR-7a; CR-5c | A-1, A-2 |
| C-5 | steel_users | price_paid (domestic steel) | increase | short | visible | B | CR-9 (substitute); CR-7a | A-1, A-2 |
| C-6 | mills.domestic | quantity_supplied | increase | short | visible | B | CR-4c (mirror case) | A-1, A-2 |
| C-7 | importers.steel | quantity_traded (covered steel imports, 1 January to 31 March) | increase | short | invisible | B | CR-10a; CR-4b (x: import after 1 April, y: before) | A-4 |
| C-8 | steel_users | inventory_held (steel stocks on 1 April) | increase | short | invisible | B | CR-10a; CR-4b (x: buy later, y: buy now and store) | A-4 |
| C-9 | importers.steel | reclassification (light fabrication abroad) | increase | short | invisible | B | CR-4b (x: covered form, y: uncovered form); arithmetic | A-3 |
| C-10 | steel_users | compliance_cost (exclusion applications) | increase | short | invisible | B | CR-1 op 2, op 3; CR-8c | A-5 |
| C-11 | lobby.steel | lobbying_effort | increase | short | visible | B | CR-4b (x: accept, y: lobby) | A-6 |
| C-12 | steel_users.import_competing | return_on_capital | decrease | medium | invisible | B | CR-3a; CR-7b (cannot pass the cost to buyers with untaxed alternatives) | A-1, A-7 |
| C-13 | steel_users.exporters | quantity_supplied (machinery exports) | decrease | medium | invisible | B | CR-9 (input_to); CR-4c; CR-7b | A-1, A-N1 |
| C-14 | mills.domestic | investment_target | increase | medium | invisible | B | CR-7a; CR-10a, CR-10c | A-2, A-10, A-11 |
| C-15 | steel_users | capital_stock_target (domestic steel-using plants) | decrease | long | invisible | B | CR-4b (x: replace here, y: there); CR-10b | A-1, A-9, A-10 |
| C-16 | government.budget | tax_revenue_vs_static_projection | decrease | short | invisible | B | CR-4c; CR-4b (reshaping); arithmetic | A-1 |
| C-17 | owners.mills | asset_value (shares in domestic mills) | increase | short | invisible | B | CR-9 (substitute); CR-7c; CR-10c | A-1, A-2, A-11 |
| C-18 | workers.mills | employment | increase | medium | visible | B | CR-9 (input_to; LW-10) | A-1, A-2 |
| C-19 | steel_users.import_competing | quantity_supplied | decrease | medium | invisible | B | CR-9 (substitute); CR-4b (buyers: x: domestic good, y: imported good) | A-1, A-7 |
| C-20 | sellers.substitutes | quantity_substitute (imported fabricated steel and finished goods) | increase | medium | invisible | B | CR-9 (substitute); CR-4b | A-1, A-7 |
| C-21 | workers.steel_using | employment | decrease | medium | invisible | B | CR-9 (input_to; LW-10) | A-1, A-7 |
| C-22 | buyers.construction | price_paid (buildings and structures) | increase | medium | invisible | B | CR-9 (input_to); CR-7a | A-1, A-14 |
| C-23 | buyers.construction | quantity_demanded | decrease | medium | invisible | B | CR-9 (input_to); CR-4c | A-1, A-14 |
| C-24 | exporters.other | net_price_received (crowns per unit exported) | decrease | medium | invisible | B | CR-9 (across_border, currency); CR-6 | A-1, A-8 |
| C-25 | exporters.other | quantity_supplied (grain and tourism exports) | decrease | medium | invisible | B | CR-9 (across_border, currency); CR-4c | A-1, A-8 |
| C-26 | foreign_mills | quantity_traded (sales to Halvern) | decrease | short | invisible | B | CR-5a; CR-4b (x: sell to Halvern, y: other markets) | A-1 |
| C-27 | steel_users | resources_available_other_uses | decrease | short | invisible | B | CR-8a, CR-8b; CR-3a | A-1 |
| C-28 | producers.other_domestic | resources_available_other_uses | decrease | medium | invisible | B | CR-8a; CR-7a | A-1, A-2 |
| C-29 | officials.enforcement | enforcement_cost | increase | short | invisible | A | CR-1 op 3; CR-8c | none |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, the foundations and arithmetic, including the link from fewer imports to other exporters (C-24, C-25), which CR-9 and CR-6 carry through the foreign-exchange market as an exchange relation.

**(b) New premises.**
- A-N1 (p 0.8): C-13. CR-7b says machinery exporters bear the higher steel cost only if they are the side without alternatives, that is, if their foreign buyers can turn to other suppliers at the old price. A-7 covers competition with imports at home, not competition abroad, so a premise about export pricing was needed.
- A-N2 (p 0.7): recorded but not cited. It covers an interaction between K1 and K2 (mills may hold prices below the import price to avoid exclusions) that could weaken C-4, C-5 and C-17. The core rules give the direction of those consequences without it.

**(c) Unclear core rules.**
- CR-9 requires every link to name a relation from `02_ontology.md`, 2.8. The foreign-exchange link between importers and exporters (C-24, C-25) is an exchange relation, but none of the five relation types fits it; it was recorded as `across_border` with a note. The rule is clear; the relation list it points to is incomplete.
- CR-7b: "the burden settles on the side without alternatives" was applied to incidence between Halvern buyers and foreign sellers (C-1). The rule does not say how to treat a case where one side has many alternatives (foreign mills' other markets) and the other has some (domestic mills): it licenses "Halvern buyers bear most", and A-1 had to supply "foreign sellers do not absorb most".
- CR-7c says a lasting change in yield is captured by "whoever owns it when the change becomes expected". With a fixed three-year term and an uncertain renewal (A-10), it is unclear whether the change counts as "lasting"; C-17 was reported on A-11 (the three-year term), with the renewal premium left to A-10.
- CR-12b refers to "a dominance pattern" for a dominance claim. No dominance claim was needed in this case.
