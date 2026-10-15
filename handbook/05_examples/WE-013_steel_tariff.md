# WE-013 Tariff on imported steel

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional country. It resembles real steel "safeguard" tariffs but is not one of them. A tariff has two components: a tax on importers (binary) and a grant of privilege to domestic producers (triangular). Its main lessons are TX-7 and TX-8, the many domestic firms that use steel as an input (RS-14), and the rationing and lobbying that a discretionary exclusion process invites (RS-15). The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Halvern Steel Safeguard Order.** Halvern is a mid-sized trading country with its own currency and a floating exchange rate. Three domestic steel firms (two integrated mills and one electric-arc mini-mill) employ about 18,000 people and supply about 60% of the steel used in Halvern; the rest is imported. About 4,000 domestic manufacturers use steel as a main input (machinery, vehicle parts, household appliances, cans, construction products), employing about 250,000 people; machinery makers export about 35% of their output. Halvern's other large export industries are grain and tourism. Halvern buys a small share of the world's steel. The Trade Ministry opened an investigation in September, published its recommendation on 1 January, and the order took effect on 1 April.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Tariff | `tariff` (ad valorem) | Imports of flat-rolled and long steel products | Importers of record | 25% of the customs value, for three years. A review in the third year may extend it. | Imported fabricated steel products and finished goods containing steel (machinery, vehicles, appliances, fabricated structural sections, fasteners) are not covered. |
| K2 Product exclusions | Discretionary exemption | Specific steel products | Ministry of Industry | Steel users may apply to exclude a product "not produced domestically in sufficient quantity or quality". Domestic steelmakers may object. Decisions are due within 90 days; exclusions last one year and must be renewed. | None |
| K3 Enforcement | Enforcement | K1, K2 | Customs Service; Ministry of Industry exclusion office | Classification checks at ports; penalties for misdeclaration. | None |

Revenue use: general budget. Its spending is out of scope; OC-1 is applied to the payers.

Unclear provisions: the standard for "sufficient quantity or quality" in K2. Assumed to be applied case by case, with weight given to objections from domestic producers (A-5).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1, as a tax | Binary: a forced payment by importers to the state | Yes, from 1 April | TX-1, TX-2, TX-9 |
| K1, as a privilege | Triangular: makes exchanges between domestic steel users and foreign steelmakers more costly, to the benefit of domestic steelmakers | Yes, while imports remain a meaningful share of supply (A-1) | TX-7, TX-8, RS-14, SB-4 |
| K2 | Triangular: a discretionary grant of relief from K1 | Yes, for those granted | RS-15, RS-7, RS-5 |
| K3 | Binary: funded by taxpayers | Yes | OC-3 |

Rothbard treats tariffs as grants of monopolistic privilege, alongside licensing and quotas; whether the Handbook adopts that category is open (Q10). It is used here only to locate the triangular component.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `steelmakers.domestic` (`sellers.substitutes`) | The three domestic firms | Foreign competition is taxed. |
| `steelmakers.owners` (`factor_owners.specific`) | Owners of the mills and of the firms' shares | The mills are specific, durable capital. |
| `steelworkers` | Employees of the domestic firms | More work at the mills. |
| `steel_users` (`buyers.current`) | Domestic manufacturers and builders using steel | Pay more for imported steel and for domestic steel. |
| `steel_users.exporters` | Steel users who sell abroad, mainly machinery makers | Higher costs, against foreign rivals who pay world prices. |
| `workers.steel_users` | Employees of steel users | Their employers' costs rise. |
| `buyers.steel_goods` | Buyers of goods made with steel, at home | Domestic steel-using goods cost more; imported finished goods do not. |
| `buyers.construction` | Buyers of buildings and infrastructure | Construction is not traded across borders, so it cannot be imported finished. |
| `importers` | Steel traders and service centers | Pay the tariff; lose volume. |
| `export_industries` | Grain, tourism and other exporters not using much steel | Linked to imports through the exchange of currencies (TX-8). |
| `input_suppliers` | Sellers of scrap, ore, energy and services to the mills | More demand from the mills. |
| `sellers.foreign` | Foreign steelmakers and foreign makers of finished steel goods | Less steel sold to Halvern; more finished goods sold to Halvern. |
| `officials.enforcement`, `taxpayers` | Customs, the exclusion office, and their funders | New work. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `steelmakers.domestic` | `net_price_received` | increase | short to medium | TX-7 | A-1, A-2 |
| C-2 | `steelmakers.domestic` | `quantity_supplied` | increase | short to medium | TX-7, LW-4 | A-1, A-2 |
| C-3 | `steelworkers` | `employment`, `hours_worked` | at_least_one_increase | short to medium | TX-7, LW-4 | A-1, A-2 |
| C-4 | `officials.enforcement` | `tax_revenue` (tariff) | increase | short | TX-1 | none |

These are the visible effects that the order's supporters point to: domestic mills sell more steel at better prices and use more labor. C-3 is a group consequence: mills running spare capacity may add shifts and overtime before they add staff, so the method does not say whether headcount, hours or both rise.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `steel_users` | `price_paid` (imported steel) | increase | short | TX-7, DM-1 | A-1 |
| C-6 | `steel_users` | `price_paid` (domestic steel) | increase | short | TX-7 | A-1, A-2 |
| C-7 | `importers` | `quantity_traded` (steel imports) | decrease | short | TX-2, TX-7 | A-1 |
| C-8 | `steel_users` | `quantity_traded` (steel imports, January to March) | increase | short | RS-8 | A-4 |
| C-9 | `importers`, `steel_users` | `reclassification` (imports of lightly fabricated products just outside the tariff's definitions) | increase | short to medium | RS-5, TX-4 | A-3 |
| C-10 | `steel_users` | `compliance_cost` (preparing exclusion requests and answering objections) | increase | short | RS-15, OC-2 | A-5 |
| C-11 | `steel_users` | `allocation_by_non_price_criteria` (who gets an exclusion) | increase | short to medium | RS-15 | A-5 |
| C-12 | `steelmakers.domestic` | `lobbying_effort` (renewal; extension to fabricated products; objections to exclusions) | increase | medium to long | RS-7, RS-15, TS-2 | A-6 |
| C-13 | `steel_users` | `lobbying_effort` (exclusions, repeal, non-renewal) | increase | medium | RS-7, RS-15 | A-6 |
| C-14 | `steelmakers.domestic` | `investment_target` (new or reopened capacity) | increase | medium | TX-7, LW-4, TS-2 | A-2, A-10 |

C-5 applies DM-1 between domestic buyers and foreign sellers: foreign steelmakers can sell to many other markets, and Halvern buys a small share of world steel, so they absorb little of the tariff and Halvern's buyers bear most of it. C-6: domestic mills price up toward the cost of imports including the tariff; this is the transfer from steel users to steelmakers, which the state never collects.

C-11: an exclusion is valuable, it is granted by officials case by case, and the domestic mills can object. It goes to whoever argues best, is best connected, or is not objected to, rather than to whoever would pay most for it (RS-15). RS-15 also gives the cost of applying (C-10) and the lobbying on both sides of each request (C-12, C-13). C-12 and C-13 are the privilege dynamics: a concentrated, identifiable gain for three firms that depends on renewal in year three, against costs spread over 4,000 users.

Not reported: smuggling or false declarations of origin (RS-3). Steel is heavy, arrives in bulk at a few ports, and is easy to inspect; A-12 is below the cut-off (p = 0.3). Not reported: retaliation by trading partners against Halvern's exports. No rule covers foreign governments' responses (the question is open under Q5), and the partners have not signaled it; A-13 is below the cut-off (p = 0.4).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-15 | `steel_users` | `quantity_supplied` (steel-using goods made in Halvern) | decrease | medium | RS-14, RS-6 | steel: `input_to` machinery, parts, appliances, cans, construction products | A-1, A-7 |
| C-16 | `workers.steel_users` | `employment`, `hours_worked` | at_least_one_decrease | medium | RS-14, RS-6 | | A-1, A-7 |
| C-17 | `buyers.steel_goods` | `quantity_substitute` (imported finished goods: machinery, appliances, fabricated sections) | increase | medium | RS-1 | domestic and imported finished goods: `substitute`, close | A-7 |
| C-18 | `steel_users.exporters` | `quantity_supplied` (exports) | decrease | medium | RS-6, TX-8 | | A-1, A-7, A-8 |
| C-19 | `export_industries` | `quantity_supplied`, `employment` | decrease | medium | TX-8 | imports and exports: linked through the currency (TX-8) | A-8 |
| C-20 | `steel_users` | `capital_stock_target` (domestic steel-using plants) | decrease | long | RS-4, RS-6, TS-1 | | A-1, A-9 |
| C-21 | `steelmakers.owners` | `asset_value` (mills, shares) | increase | short (from January) | SB-4 | | A-2, A-11 |
| C-22 | Owners of steel-using firms | `asset_value` | decrease | short (from January) | SB-4 | | A-1, A-7, A-11 |
| C-23 | `input_suppliers` | `quantity_demanded` (scrap, ore, energy for the mills) | increase | short to medium | TX-7 | scrap and ore: `input_to` steel | A-2 |
| C-24 | `buyers.construction` | `price_paid` (buildings and infrastructure) | increase | medium | RS-14 | steel: `input_to` construction | A-1, A-14 |
| C-25 | `officials.enforcement` | `tax_revenue_vs_static_projection` (tariff) | decrease | short | TX-9 | | A-1 |

C-15 to C-18: domestic steel users pay more for steel, but their foreign rivals do not, and imported finished goods are untaxed (K1 exemptions). Users that compete with imports cannot raise their prices to cover the cost, so their expected return falls and they produce less (RS-14: where competitors are exempt, the quantity effect dominates; RS-6), and buyers turn to imported finished goods (C-17). C-16 is a group consequence: users may cut staff or hours. The tariff thus moves part of the steel-using work abroad: Halvern imports less steel and more goods made of steel. Exporters lose twice, through their costs (RS-6) and through TX-8.

C-19 applies TX-8: foreigners earn fewer crowns from selling steel to Halvern and so buy fewer of Halvern's exports, grain and tourism among them. C-24 applies RS-14: construction cannot be imported finished, so all builders face the same higher steel cost and the price rise dominates; builders' clients pay more (A-14). C-22 applies SB-4 in its generalized form: the plants of steel users are specific, durable capital, and the tariff lowers their expected return for its expected life (A-11), so the shares of steel-using firms fall when the tariff becomes expected, in January.

C-19, C-23 and C-24 are at depth 3; C-18 and C-20 at depth 3 to 4 (tariff, steel prices, users' returns, exports or plants abroad). Diffuse bystanders beyond these (for example, the suppliers of export industries) are not followed.

Checks. RS-9: no shopping trips are involved. RS-10: no trade is pushed into an informal market (smuggling not reported). RS-11: no benefit is tied to a place.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| Manufacturing employment in Halvern (steelworkers and steel users' workers together), medium | More work at the mills (C-3). | Less work at steel users (C-16) and exporters (C-18, C-19). | None | **Not combined.** These are different actor classes; each is reported with its own sign. The method cannot net them, because it cannot measure sizes. The jobs at the mills are visible and attributed to the order; the jobs not created or lost among 4,000 users and the export industries are spread thin and not attributed to it. |
| `steelmakers.domestic`, `investment_target`, medium | Higher prices make new or reopened capacity pay, if the tariff is renewed (A-10, p = 0.55). | If the mills expect the tariff to lapse after three years, capacity built for it would be stranded; they would add little or none. | None | **increase** (C-14), reported because A-10 is just above the cut-off. If evidence moved A-10 below 0.5, C-14 would not be reported: the sign would not reverse, but the investment would not happen. |
| Steelmakers that reopen idle capacity or build new capacity, `return_on_capital` on that capacity, medium | Higher prices for the life of the tariff (C-1). | One-time cost of reopening or building; risk of non-renewal. | DM-3 | **ambiguous** by design. Those who invest expected it to pay (LW-5). |
| Split of the tariff between Halvern's buyers and foreign sellers, short | — | — | DM-1 | **Halvern's buyers bear most** (C-5): foreign sellers have many other markets. |

Revenue. The more the tariff protects (the more imports fall, C-7), the less it collects (C-25). Much of what steel users pay goes not to the state but to the domestic mills, in higher prices for domestic steel (C-6).

## 8. Time structure

- **Announcement window (January to March).** Users and importers buy ahead and stock up before 1 April (C-8), so imports dip by more than the long-run fall in the months just after. Share prices move at once: up for the mills (C-21), down for steel users (C-22).
- **First year.** Steel prices rise (C-5, C-6) and the mills use spare capacity (C-2, C-3). Users file exclusion requests and wait up to 90 days or more (C-10, C-11). Importers redesign shipments to fall outside the definitions (C-9).
- **One to three years.** Users that compete with imported finished goods lose sales and cut output and jobs (C-15, C-16); exporters lose foreign sales (C-18); the currency channel works through (C-19). Whether the mills invest depends on what they expect of the year-three review (C-14, TS-2). Lobbying peaks before the review (C-12, C-13).
- **Long run.** The order is for three years, but expectations of renewal make it matter for longer. Plants of steel users are durable: when they come up for replacement, some owners rebuild abroad, nearer to steel at world prices (C-20, TS-1). That decision is hard to reverse even if the tariff lapses (TS-6: the flow reverses, the stock already moved does not). If the tariff lapses, the mills' share prices fall back on whoever holds them then (SB-4). If it is renewed, each renewal reinforces the mills' stake in the next one (C-12).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-26 | `steel_users`, `importers` | `resources_available_other_uses` | decrease | The tariff paid: what users would otherwise have spent, invested or saved. The higher price paid for domestic steel (C-6) is a further transfer to the mills, not counted again here. | TX-1, OC-1 |
| C-27 | `steel_users`, `sellers.foreign` | `quantity_traded` (steel purchases forgone, not replaced by domestic steel) | decrease | Purchases that would have been made at world prices and are not made at all; both sides lose the gain they expected. | OC-4, TX-2 |
| C-28 | `taxpayers` | `resources_available_other_uses` | decrease | What the customs checks and the exclusion office would otherwise have funded. | OC-3, OC-1 |

Time spent on exclusion requests is already C-10.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Imports remain a meaningful share of supply, and foreign sellers do not absorb most of the tariff. | binding | 0.85 | Halvern's small share of world steel demand; foreign mills' other markets. | C-1, C-5, C-6 and everything downstream weaken; the tariff then falls on foreign sellers. |
| A-2 | Domestic mills can raise output from spare or idle capacity and produce close substitutes for most imports. | substitutability | 0.75 | Capacity utilization; product range of the three mills compared with imports. | C-2, C-3, C-14, C-23 weaken; C-6 grows. |
| A-3 | Some imports can be reshaped to fall outside the tariff's definitions at a cost below 25%. | other | 0.7 | Customs definitions; cost of light fabrication abroad. | C-9 not reported. |
| A-4 | Users and importers can store steel and order ahead. | expectations | 0.8 | Warehouse capacity; order lead times. | C-8 not reported. |
| A-5 | Exclusions are decided case by case, with weight given to objections from the mills. | other | 0.7 | The order's text; the exclusion office's procedures and staffing. | C-11 not reported; C-10 shrinks. |
| A-6 | Steelmakers and users organize to influence renewal and exclusions. | other | 0.85 | Existing industry associations; the investigation's hearings. | C-12, C-13 not reported. |
| A-7 | Many steel users compete with imported finished goods that are not taxed. | substitutability | 0.8 | Import shares in machinery, appliances and parts; K1 exemptions. | C-15 to C-18 and C-22 weaken; users pass costs on instead. |
| A-8 | The fall in steel imports is not offset by capital flows or other adjustments within the medium horizon. | other | 0.6 | Floating exchange rate; capital account. | C-18 (through TX-8) and C-19 not reported. |
| A-9 | Some steel-using firms have the option of producing abroad when plants are replaced. | mobility | 0.6 | Firms with foreign plants; plant replacement cycles. | C-20 not reported. |
| A-10 | Steelmakers expect the tariff to be renewed at the year-three review. | expectations | 0.55 | Political history of safeguard renewals; the mills' influence. | C-14 not reported. |
| A-11 | Investors expect the tariff to stay in force for at least its three-year term. | expectations | 0.8 | The order's text; government statements. | C-21, C-22 shrink. |
| A-12 | Smuggling or false declarations of origin occur on a meaningful scale. | enforcement | 0.3 | Bulk cargo, few ports, inspection rates. | Below cut-off; not reported. |
| A-13 | Trading partners retaliate against Halvern's exports. | other | 0.4 | Partners' statements; their past responses. | Below cut-off; not reported. |
| A-14 | Steel is a material part of construction costs and builders cannot replace it with other materials at the old cost in the medium run. | substitutability | 0.8 | Steel's share of building costs (reinforcing bar, structural sections); building codes; cost of switching to concrete or timber designs. | C-24 not reported. |

## 11. Report

**The policy.** Halvern taxes imported steel at 25% for three years, with a possible extension. Finished goods made of steel are not taxed. Steel users may ask for one-year exclusions, which the domestic mills may oppose. The revenue goes to the general budget.

**Visible consequences.** Domestic mills sell more steel (C-2) at higher prices (C-1) and employ more people or work longer hours (C-3). The state collects the tariff (C-4).

**Invisible consequences.**
- *Steel users* pay more for imported steel (C-5) and for domestic steel (C-6). The second is a transfer to the mills that the state never sees. Users stock up before the tariff (C-8), redesign imports to avoid it (C-9), and spend time seeking exclusions (C-10), which go to some firms and not others by criteria other than price (C-11).
- *Users that compete with imported finished goods* produce less (C-15) and use less labor, in jobs or hours (C-16), as buyers switch to imported machinery, appliances and parts (C-17). *Exporters* using steel lose foreign sales (C-18). Over the long run some users rebuild plants abroad (C-20).
- *Other exporters*, such as grain and tourism, sell less abroad, because foreigners earn fewer crowns from selling steel to Halvern (C-19).
- *Builders' clients* pay more for buildings and infrastructure (C-24).
- *Owners* of the mills gain when the tariff is announced (C-21); owners of steel-using firms lose (C-22). Suppliers of scrap, ore and energy to the mills gain (C-23).
- *Mills and users* lobby over exclusions and renewal (C-12, C-13). The mills invest in capacity if they expect renewal (C-14).
- *Importers and users* give up what the tariff would have bought (C-26); some steel purchases are not made at all (C-27); taxpayers fund customs and the exclusion office (C-28). Revenue falls short of a projection at the old import volume (C-25).

**Ambiguous effects.** Whether total manufacturing employment rises or falls: jobs at the mills are set against jobs at users and exporters, and the method cannot weigh them. Whether new capacity at the mills pays for itself.

**Key conditions.** That foreign sellers do not absorb the tariff (A-1, p = 0.85) and that many users compete with untaxed imported finished goods (A-7, p = 0.8) drive most of the costs to users. The export-industry effect rests on A-8 (p = 0.6). The mills' investment depends on their expecting renewal (A-10, p = 0.55).

**What this analysis cannot say.** How many jobs are gained at the mills or lost elsewhere; whether national security or other aims justify the tariff; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | steelmakers.domestic | net_price_received | increase | short–medium | visible | B | TX-7 | A-1, A-2 |
| C-2 | steelmakers.domestic | quantity_supplied | increase | short–medium | visible | B | TX-7, LW-4 | A-1, A-2 |
| C-3 | steelworkers | employment, hours_worked | at_least_one_increase | short–medium | visible | B | TX-7, LW-4 | A-1, A-2 |
| C-4 | officials.enforcement | tax_revenue (tariff) | increase | short | visible | A | TX-1 | none |
| C-5 | steel_users | price_paid (imported steel) | increase | short | invisible | B | TX-7, DM-1 | A-1 |
| C-6 | steel_users | price_paid (domestic steel) | increase | short | invisible | B | TX-7 | A-1, A-2 |
| C-7 | importers | quantity_traded (steel imports) | decrease | short | invisible | B | TX-2, TX-7 | A-1 |
| C-8 | steel_users | quantity_traded (imports, Jan–Mar) | increase | short | invisible | B | RS-8 | A-4 |
| C-9 | importers, steel_users | reclassification | increase | short–medium | invisible | B | RS-5, TX-4 | A-3 |
| C-10 | steel_users | compliance_cost (exclusions) | increase | short | invisible | B | RS-15, OC-2 | A-5 |
| C-11 | steel_users | allocation_by_non_price_criteria (exclusions) | increase | short–medium | invisible | B | RS-15 | A-5 |
| C-12 | steelmakers.domestic | lobbying_effort | increase | medium–long | invisible | B | RS-7, RS-15, TS-2 | A-6 |
| C-13 | steel_users | lobbying_effort | increase | medium | invisible | B | RS-7, RS-15 | A-6 |
| C-14 | steelmakers.domestic | investment_target | increase | medium | invisible | B | TX-7, LW-4, TS-2 | A-2, A-10 |
| C-15 | steel_users | quantity_supplied (steel-using goods) | decrease | medium | invisible | B | RS-14, RS-6 | A-1, A-7 |
| C-16 | workers.steel_users | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-14, RS-6 | A-1, A-7 |
| C-17 | buyers.steel_goods | quantity_substitute (imported finished goods) | increase | medium | invisible | B | RS-1 | A-7 |
| C-18 | steel_users.exporters | quantity_supplied (exports) | decrease | medium | invisible | B | RS-6, TX-8 | A-1, A-7, A-8 |
| C-19 | export_industries | quantity_supplied, employment | decrease | medium | invisible | B | TX-8 | A-8 |
| C-20 | steel_users | capital_stock_target (domestic plants) | decrease | long | invisible | B | RS-4, RS-6, TS-1 | A-1, A-9 |
| C-21 | steelmakers.owners | asset_value | increase | short | invisible | B | SB-4 | A-2, A-11 |
| C-22 | owners of steel-using firms | asset_value | decrease | short | invisible | B | SB-4 | A-1, A-7, A-11 |
| C-23 | input_suppliers | quantity_demanded | increase | short–medium | invisible | B | TX-7 | A-2 |
| C-24 | buyers.construction | price_paid | increase | medium | invisible | B | RS-14 | A-1, A-14 |
| C-25 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short | invisible | B | TX-9 | A-1 |
| C-26 | steel_users, importers | resources_available_other_uses | decrease | short | invisible | A | TX-1, OC-1 | none |
| C-27 | steel_users, sellers.foreign | quantity_traded (purchases forgone) | decrease | short | invisible | B | OC-4, TX-2 | A-1 |
| C-28 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| — | steelmakers.domestic (new capacity) | return_on_capital | ambiguous | medium | invisible | B | C-1 vs one-time cost; DM-3 | A-10 |

## Gaps found

- GAP-013-1 (closed in catalog 0.3: RS-15): C-11 now Tier B; RS-15 is also cited for C-10, C-12 and C-13.
- GAP-013-2 (closed in catalog 0.3: SB-4 generalized): C-22 now Tier B, adding A-11 for SB-4's `expectations` premise.
- GAP-013-3 (closed in catalog 0.3: RS-14): C-24 now Tier B, with the new assumption A-14; RS-14 is also cited for C-15 and C-16, where exempt imported finished goods make the quantity effect dominate.
- GAP-013-4 (open: Q5): responses by foreign governments, such as retaliation, are not encoded; the question is added to Q5. Retaliation stays unreported here because A-13 is below the cut-off.
- GAP-013-5 (closed in catalog 0.3: `return_on_capital`): the DM-3 row for new capacity now has a variable and is Tier B (ambiguous by design).
