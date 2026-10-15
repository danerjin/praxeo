# WE-023 Repeal of a lumber tariff

Analyst: draft (Handbook 0.2)  |  Rule catalog version: 0.2  |  Status: awaiting expert review

A stylized repeal in a fictional country. There is no separate worked example for the original tariff, so section 1 records the tariff's expected consequences briefly, from TX-7, TX-8 and the rules they build on, as the reference for the metamorphic check at the end of section 7. The counterfactual throughout is **the tariff stays in force at its current rate**; every sign is relative to that, not to the situation before the repeal and not to a country that never had the tariff. "In reverse" after a rule ID means the rule is applied to the removal of its precondition; where that direction is not obviously valid, the text says so. The probabilities are illustrative.

## 1. Policy record

**Velmora Lumber Duty Repeal Act.** Velmora is a mid-sized country. For twenty years it has charged a 25% ad valorem duty on imported sawn softwood lumber, most of which comes from its larger neighbor, Dravenland. Domestic lumber comes from about forty sawmills in Velmora's northern forest region, which buy logs from private timberland owners. The main domestic users of lumber are home builders and furniture makers. Imported furniture has never been subject to the duty. Velmora's main export industries (machinery and processed foods) sell largely to Dravenland. Duty revenue has gone to the general budget. The Act passed nine months before its effective date; it had been expected for some weeks before that.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Repeal | Removal of a `tariff` | Imported sawn softwood lumber | Importers | The duty falls from 25% to zero on the effective date, in one step. | None |
| R2 Customs procedure | End of administration | Classification and valuation of lumber imports for the duty | Customs service | Duty-specific checks end; ordinary customs procedures continue. | None |

Unclear provisions: how the lost duty revenue is to be replaced (higher other taxes, more borrowing, or lower spending). The Act does not say. Treated as unknown (A-14).

### The original tariff: expected consequences (reference for the metamorphic check)

Not a full worked example. Signs are relative to no tariff, under the standard assumptions of TX-7 and TX-8 (domestic substitutes exist; the duty is not absorbed entirely by foreign sellers; trade is not fully offset by capital flows).

| ID | Actor class | Variable | Sign | Horizon | Rules |
|---|---|---|---|---|---|
| T-1 | `buyers.lumber` (builders, furniture makers, households) | `price_paid` (lumber, imported and domestic) | increase | short to long | TX-7 |
| T-2 | `sawmills.domestic` | `net_price_received` | increase | short | TX-7 |
| T-3 | `sawmills.domestic` | `quantity_supplied` | increase | short to medium | TX-7 |
| T-4 | `sawmills.domestic` | `investment_target` | increase | medium | TX-7, LW-4 |
| T-5 | `workers.sawmill` | `employment` | increase | medium | TX-7, LW-4 |
| T-6 | `timberland_owners` | `asset_value` | increase | short to medium | SB-4, EN-2 |
| T-7 | `importers`, foreign sellers | `quantity_traded` (imported lumber) | decrease | short | TX-2, OC-4 |
| T-8 | `importers` | `reclassification` (lightly processed wood declared outside the lumber heading) | increase | short to medium | RS-5, TX-4 |
| T-9 | `builders` | `quantity_supplied` (new houses) | decrease | medium | TX-7, RS-6 |
| T-10 | `homebuyers` | `price_paid` (new houses) | increase | medium | TX-7 |
| T-11 | `furniture_makers.domestic` | `quantity_supplied` | decrease | medium | TX-7, RS-6 |
| T-12 | `buyers.furniture` | `quantity_substitute` (imported furniture) | increase | medium | RS-1 |
| T-13 | `exporters` | `quantity_supplied`, `employment` | decrease | medium to long | TX-8 |
| T-14 | `buyers.lumber` | `resources_available_other_uses` | decrease | short | TX-1, OC-1 |
| T-15 | `officials.enforcement` (treasury) | `tax_revenue` | increase | short | TX-1 |
| T-16 | `sawmills.domestic`, `timberland_owners` | `lobbying_effort` | increase | medium | RS-7 |
| T-17 | `taxpayers` | `resources_available_other_uses` (customs administration of the duty) | decrease | short | OC-3 |

T-11 and T-12 follow from the duty falling on lumber but not on furniture: domestic furniture makers paid more for their main input than foreign competitors did, while selling against untaxed imports.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| R1 | Removal of a binary intervention (the duty paid by importers) and of a triangular one (the privilege granted to domestic mills) | Yes: imports are a substantial share of lumber used, and domestic prices exceed Dravenland's by about the duty plus transport (A-1) | TX in reverse, RS-8, SB-4 in reverse |
| R2 | Removal of a binary intervention (taxpayer-funded administration) | Yes | OC-3 in reverse |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.lumber` | Builders, furniture makers and households who buy lumber | Can buy imported lumber without the duty. |
| `importers` | Firms that import lumber | No duty, no classification disputes. |
| `sawmills.domestic` (`sellers.substitutes`) | Velmoran sawmills | Lose the protection; mills built for the protected market are specific, durable capital. |
| `workers.sawmill` | Mill employees, concentrated in the forest region | Fewer mill jobs; skills partly specific to milling. |
| `timberland_owners` (`factor_owners.specific`) | Owners of forest land that supplies sawlogs to domestic mills | Lower demand for logs from domestic mills. |
| `builders`, `homebuyers` | Home builders and buyers of new houses | Lower input costs for builders. |
| `furniture_makers.domestic`, `buyers.furniture` | Domestic furniture makers and their customers | Domestic makers' input costs fall to their foreign competitors' level. |
| `exporters` | Velmoran machinery and processed-food exporters | Dravenland buyers earn more crowns from lumber sales. |
| `sellers.foreign` (`neighboring_jurisdictions`) | Dravenland lumber sellers | Duty-free access to Velmora. |
| `officials.enforcement`, `taxpayers` | Treasury and customs, and those who fund the budget | Revenue lost; duty administration ends. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.lumber` | `price_paid` (lumber, imported and domestic) | decrease | short | TX-7 in reverse | A-1, A-2 |
| C-2 | `sawmills.domestic` | `net_price_received` | decrease | short | TX-7 in reverse | A-1 |
| C-3 | `officials.enforcement` (treasury) | `tax_revenue` | decrease | short | TX-1 in reverse | none |

The visible effects: lumber is cheaper, domestic mills receive less for it, and the duty revenue is gone. Unlike in WE-022, the visible loss falls on a concentrated, identifiable group (mill owners and their workers), while the gains are spread across many buyers.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `importers` | `quantity_traded` (imported lumber) | increase | short (from the effective date) | TX-2, OC-4 in reverse | A-1 |
| C-5 | `sawmills.domestic` | `quantity_supplied` | decrease | short to medium | TX-7 in reverse, TS-1 | A-1, A-3 |
| C-6 | `sawmills.domestic` | `investment_target` | decrease | short to medium | RS-6, TX-7 in reverse | A-1 |
| C-7 | `sawmills.domestic` | `number_of_sellers` | decrease | medium to long | RS-6, TS-1 | A-1, A-3 |
| C-8 | `workers.sawmill` | `employment` | decrease | medium | RS-6, LW-4 | A-1, A-3 |
| C-9 | `workers.sawmill` who lose mill jobs | `earnings` | decrease | medium | RS-6, LW-4 | A-1, A-4 |
| C-10 | `importers` | `reclassification` | decrease | short | RS-5, TX-4 in reverse | A-5 |
| C-11 | `buyers.lumber` | `quantity_traded` (lumber) | decrease | short (announcement window only) | RS-8 | A-6 |
| C-12 | `sawmills.domestic`, `timberland_owners`, `builders`, `exporters` | `lobbying_effort` | ambiguous (see section 7) | medium | RS-7 | A-15 |

C-5 applies TS-1 in its own direction: the mills built or expanded behind the duty are specific and durable, so they keep running as long as the lower price covers their operating costs, and capacity falls as equipment wears out and is not replaced. Output falls first at high-cost mills.

C-9: the repeal lowers the return to work in milling. Workers who lose mill jobs move to their next-best work, which they ranked lower; with partly specific skills and few other employers in the forest region (A-4), it pays less.

C-11 is RS-8 in its own words: "delay until after a repeal is expected". In the nine months before the effective date, builders and furniture makers draw down stocks and defer purchases, and importers hold shipments in bonded warehouses. Domestic mills see a dip in orders before the repeal takes effect.

Not reported: an end to lumber smuggling. Under the duty, smuggling was minor given the controlled crossing points (A-16, p = 0.15).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-13 | `timberland_owners` | `asset_value` | decrease | short (from the announcement) | SB-4 in reverse | sawlogs `input_to` domestic lumber, close | A-1, A-7 |
| C-14 | `sawmills.domestic` | `asset_value` (mill capital) | decrease | short (from the announcement) | TX-7 in reverse, TS-1 | | A-1, A-3 |
| C-15 | `builders` | `quantity_supplied` (new houses) | increase | medium | TX-7 in reverse, LW-4 | lumber `input_to` housing, partial | A-1, A-8 |
| C-16 | `homebuyers` | `price_paid` (new houses) | decrease | medium | TX-7 in reverse | lumber `input_to` housing, partial | A-1, A-8 |
| C-17 | `furniture_makers.domestic` | `quantity_supplied` | increase | medium | TX-7 in reverse, LW-4 | lumber `input_to` furniture, close | A-1, A-9 |
| C-18 | `buyers.furniture` | `quantity_substitute` (imported furniture) | decrease | medium | RS-1 in reverse | domestic and imported furniture: `substitute`, close | A-1, A-9 |
| C-19 | `exporters` | `quantity_supplied`, `employment` | increase | medium to long | TX-8 in reverse | | A-1, A-10 |
| C-20 | `sellers.foreign` | `net_price_received` | increase | short | TX-7 in reverse | Velmora and Dravenland lumber: `across_border`, close | A-11 |
| C-21 | `builders`, `furniture_makers.domestic` | `investment_target` (lumber-using capacity) | increase | medium to long | TX-7 in reverse, LW-4, GAP-023-2 | lumber `input_to` housing and furniture | A-1, A-12 |
| C-22 | `furniture_makers.domestic` | `entry_rate` | increase | long | LW-4, GAP-023-1 | | A-1, A-9, A-13 |

C-13 applies SB-4 in reverse: the duty raised the return to a resource in fixed supply (forest land whose logs go to domestic mills), and its removal lowers it. The fall is capitalized as soon as the repeal is expected. It falls on whoever owns the land then, including owners who bought during the twenty years at prices that included the duty's value. The owners at the time the duty was introduced captured the original gain (T-6) and, if they have since sold, bear none of the loss.

C-14 is the same logic for mill capital, which is durable and specific. The resources sunk into mills built behind the duty (T-4) are not recovered by the repeal; the loss shows up as lower mill values.

C-16 is at depth 3 and reaches a broad group, so the chain stops there. Effects on shops and services in the forest region (depth 4, through lower mill employment) are diffuse bystander effects and are pruned.

C-21 and C-22 are Tier C. C-21: capacity that pays back over many years depends on users expecting the duty to stay gone, which no rule covers (GAP-023-2). C-22: the sign follows from LW-4, but the horizon does not. EN-3 and RS-6 say how firms leave a less profitable trade, not how fast they come back after twenty years in which skills, supplier links and retail placement were lost (GAP-023-1).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `taxpayers`, `resources_available_other_uses`, medium | The customs work of administering the duty ends (C-24; OC-3 in reverse). | The lost duty revenue (C-3) must be made up by other taxes now, borrowing that implies taxes later, or lower spending on someone (A-14; GAP-023-3). | None | **ambiguous**, Tier C. The method cannot net them, and cannot say which group bears the replacement until the budget response is known. |
| `sawmills.domestic`, `timberland_owners`, `builders`, `exporters`, `lobbying_effort`, medium | Mill owners, timberland owners and mill workers now bear a concentrated loss that restoring the duty would undo, and organize for it (RS-7, A-15). Builders and exporters defend the repeal. | The campaign over the duty that would have continued with it in force (T-16, and lumber users' efforts for repeal) ends in its old form. | None | **ambiguous**. The repeal changes who lobbies for what; the method cannot say whether total effort rises or falls. |
| `buyers.furniture`, `quantity_substitute` (imported furniture), medium | Foreign makers' established distribution and buyer familiarity, built over twenty years, persist (Tier C, GAP-023-1). | Domestic furniture becomes cheaper relative to imports (C-17, A-9). | None needed | **decrease**. The + chain does not reverse the sign; it slows the change. It is noted, not reported as a separate consequence. |

### Metamorphic check against the original tariff

"Reverses" means the expected sign under repeal is the opposite of the tariff's. "Partly reverses" means the sign reverses for the flow but not for a stock the tariff already changed, or reverses for the variable but not for the persons who gained or lost. Rows whose verdict depends on GAP-023-1 are marked Tier C.

| Tariff ID | Actor class, variable | Sign under the tariff | Expected sign under repeal (this example) | Reverses? | Reason |
|---|---|---|---|---|---|
| T-1 | `buyers.lumber`, `price_paid` | increase | decrease (C-1) | Reverses | Immediate on the effective date. |
| T-2 | `sawmills.domestic`, `net_price_received` | increase | decrease (C-2) | Reverses | |
| T-3 | `sawmills.domestic`, `quantity_supplied` | increase | decrease (C-5) | Partly reverses | The increase came through new investment; the decrease comes through wear-out, because mill capital is specific and keeps running while it covers operating costs (A-3, TS-1). The speeds differ. |
| T-4 | `sawmills.domestic`, `investment_target` | increase | decrease (C-6) | Partly reverses | New investment falls at once. Capital already sunk is not recovered; it appears as lower mill values (C-14), which has no counterpart in the tariff list. |
| T-5 | `workers.sawmill`, `employment` | increase | decrease (C-8) | Partly reverses | In sign. But workers who built careers on milling skills under the duty bear an earnings loss on leaving (C-9). The tariff's workers chose to move in, expecting to gain (LW-5); the repeal's workers do not choose to move out. The loss has no mirror in the tariff list. |
| T-6 | `timberland_owners`, `asset_value` | increase | decrease (C-13) | Partly reverses | Reverses for the asset, not for the persons. Owners at the duty's introduction captured the gain; current owners who bought at duty-inclusive prices bear the loss. |
| T-7 | `importers`, `quantity_traded` (imported lumber) | decrease | increase (C-4); decrease in the announcement window (C-11) | Reverses after a temporary dip | RS-8 delays purchases until the duty ends. |
| T-8 | `importers`, `reclassification` | increase | decrease (C-10) | Reverses | No reason remains to shape imports around the duty. |
| T-9 | `builders`, `quantity_supplied` (new houses) | decrease | increase (C-15) | Reverses | For the flow. Houses not built over twenty years are not built retroactively, but they are not part of a comparison with the tariff staying. |
| T-10 | `homebuyers`, `price_paid` (new houses) | increase | decrease (C-16) | Reverses | |
| T-11 | `furniture_makers.domestic`, `quantity_supplied` | decrease | increase (C-17); `entry_rate` increase, long (C-22, Tier C) | Partly reverses (Tier C) | Surviving makers expand as their input cost falls. Firms that closed, the skills of their workers, supplier links and retail placement lost over twenty years come back slowly, if at all (A-13, GAP-023-1). |
| T-12 | `buyers.furniture`, `quantity_substitute` (imported furniture) | increase | decrease (C-18) | Partly reverses (Tier C) | Foreign makers' distribution and buyers' familiarity with their brands persist (GAP-023-1). |
| T-13 | `exporters`, `quantity_supplied`, `employment` | decrease | increase (C-19) | Partly reverses (Tier C) | In sign. Entering or re-entering foreign markets has sunk costs (distribution, buyer relationships), so the response is slower than the original decline (GAP-023-1); the horizon is set to medium to long. |
| T-14 | `buyers.lumber`, `resources_available_other_uses` | decrease | increase (C-23) | Reverses | |
| T-15 | treasury, `tax_revenue` | increase | decrease (C-3) | Reverses | The spending the revenue funded must now be funded in some other way (section 7 row 1, Tier C). The tariff list did not trace the revenue's use, so this has no counterpart. |
| T-16 | `sawmills.domestic`, `timberland_owners`, `lobbying_effort` | increase | ambiguous (C-12) | Does not reverse | Those who lose from the repeal now lobby to restore the duty; those who gain defend it. |
| T-17 | `taxpayers`, `resources_available_other_uses` (customs) | decrease | ambiguous (C-25, Tier C); `enforcement_cost` decrease (C-24) | Partly reverses | The administrative saving reverses T-17, but the same taxpayers must make up the lost revenue. |

Consequences with no counterpart in the tariff list: C-9 (earnings of displaced mill workers), C-11 (purchases deferred in the announcement window), C-14 (mill values), C-20 (foreign sellers' net price), C-21 (lumber-using capacity, Tier C).

## 8. Time structure

- **Announcement window (nine months).** Timberland and mill values fall as soon as the repeal is expected (C-13, C-14). Buyers defer purchases and importers hold shipments until the effective date (C-11), so domestic mills lose orders before the duty ends.
- **Effective date.** Lumber prices fall and imports rise at once (C-1, C-4). The flows of trade reverse within months.
- **Mill capacity declines at the speed of wear-out.** Mills keep running while the lower price covers their operating costs (A-3). Exits and job losses spread over several years (C-5, C-7, C-8). This direction is TS-1 as written.
- **Re-entry is not the mirror of exit.** Domestic furniture making shrank over twenty years. Its recovery needs new firms, trained workers, supplier links and shelf space that foreign brands now hold (C-22, Tier C). Export firms that never entered, or left, Dravenland's market face sunk entry costs (C-19). These responses take longer than the original decline did, and no rule in the catalog says so (GAP-023-1).
- **Who bears the capital losses.** Lower land and mill values (C-13, C-14) fall on owners at the time of the announcement. Over twenty years many assets have changed hands at prices that included the duty's value; the original gainers are not the present losers.
- **Expectations of restoration.** The duty lasted twenty years, and its beneficiaries are concentrated and organized (C-12). Builders and furniture makers who would add capacity that pays back over ten years or more weigh the chance that the duty returns (A-12, p = 0.6; GAP-023-2). Mills, conversely, may keep idle capacity on standby rather than scrapping it, if they expect the duty back.
- **The budget.** The revenue loss is immediate (C-3). How and when it is made up (other taxes, borrowing, spending cuts) is a budget decision the Act leaves open (A-14).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-23 | `buyers.lumber` | `resources_available_other_uses` | increase | Nothing given up; the part of the duty that buyers bore (A-2) is freed for other purchases. | TX-1, OC-1 in reverse |
| C-24 | `officials.enforcement` (customs) | `enforcement_cost` | decrease | Nothing given up; customs staff time spent classifying and valuing lumber for the duty is freed. | OC-3 in reverse |
| C-25 | `taxpayers` | `resources_available_other_uses` | ambiguous (section 7) | Freed: the cost of administering the duty. Given up: what other taxpayers, or recipients of cut spending, would have done with the resources that now replace the lost revenue. | OC-3, OC-1 in reverse; GAP-023-3 |

The imports that the duty prevented (OC-4) are now made: that is C-4, not listed again.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Imports are a substantial share of lumber used, and the duty raised domestic lumber prices. | binding | 0.9 | Import share; domestic prices against Dravenland prices plus transport. | Almost every consequence weakens or disappears. |
| A-2 | Velmoran buyers bore at least part of the duty (foreign sellers did not absorb all of it). | other | 0.85 | Price gap across the border; Dravenland's other markets. | C-1 and C-23 shrink. |
| A-3 | Mill capital is specific and durable: mills keep operating while prices cover operating costs and close as equipment wears out. | durability | 0.85 | Age and type of mill equipment; resale market for used mill equipment. | Capacity falls faster; C-14 smaller. |
| A-4 | Mill workers' skills are partly specific, and the forest region has few other employers. | alternative_uses | 0.75 | Regional employment structure; wages in other local work. | C-9 not reported. |
| A-5 | Some imports had been shaped to fall outside the lumber heading. | other | 0.6 | Customs classification disputes; import volumes of lightly processed wood. | C-10 not reported. |
| A-6 | Lumber buyers can defer purchases or draw down stocks for some months. | expectations | 0.7 | Inventory practices of builders and furniture makers; bonded warehouse capacity. | C-11 not reported. |
| A-7 | Timberland is valued mainly for sawlogs sold to domestic mills; exporting logs costs too much to replace that demand. | alternative_uses | 0.7 | Land prices against log prices; transport costs; other uses of forest land. | C-13 weakens. |
| A-8 | Lumber is a significant share of building costs, and builders compete. | other | 0.8 | Cost breakdowns of new houses; number of builders. | C-15 and C-16 weaken. |
| A-9 | Lumber is a significant input for domestic furniture, and imported furniture is a close substitute. | substitutability | 0.8 | Cost breakdowns; import share of furniture sales. | C-17, C-18 and C-22 weaken. |
| A-10 | Changes in imports are not fully offset by capital flows: Dravenland sellers spend more of the crowns they earn on Velmoran goods. | other | 0.65 | Composition of the balance of payments; trade patterns with Dravenland. | C-19 not reported. |
| A-11 | Foreign sellers bore part of the duty. | other | 0.6 | Dravenland export prices to Velmora against prices to other markets. | C-20 not reported. |
| A-12 | Lumber users expect the repeal to last at least ten years, the payback of new capacity. | expectations | 0.6 | Size of the parliamentary majority; organization and history of the mill lobby. | C-21 not reported. |
| A-13 | Furniture-making skills, supplier links and retail placement lost over twenty years take years to rebuild. | durability | 0.7 | Number of furniture firms and workers now against twenty years ago; training available. | C-22 comes sooner. |
| A-14 | The lost revenue is made up by some combination of other taxes, borrowing and spending cuts; the Act does not say which. | revenue_use | 0.95 | Budget documents; fiscal rules. | Section 7 row 1 changes. |
| A-15 | Mill owners, timberland owners, builders and exporters can organize at a cost below their stake. | other | 0.85 | Twenty years of organized lobbying over the duty. | C-12 not reported. |
| A-16 | Lumber smuggling was significant under the duty. | enforcement | 0.15 | Controlled crossing points; seizure records. | Below cut-off; not reported. |

## 11. Report

**The policy.** Velmora abolishes, in one step, the 25% duty it has charged for twenty years on imported softwood lumber. The repeal was known nine months in advance. The Act does not say how the lost revenue will be replaced.

**Visible consequences.** Lumber is cheaper (C-1). Domestic sawmills receive less for their lumber (C-2). The treasury loses the duty revenue (C-3).

**Invisible consequences.**
- *Sawmills and their workers* sell less and invest less (C-5, C-6). Mills close over several years as equipment wears out (C-7), and mill employment falls (C-8). Workers who lose mill jobs earn less in their next-best work, because their skills are partly specific and the forest region has few other employers (C-9).
- *Owners of forest land and of mills* see their assets lose value as soon as the repeal is expected (C-13, C-14). The losses fall on present owners, many of whom bought at prices that included the duty's value.
- *Builders and furniture makers* pay less for lumber, so more houses are built and sold at lower prices (C-15, C-16), and domestic furniture makers expand against imported furniture (C-17, C-18). In the months before the repeal takes effect, they buy less lumber, waiting for the lower price (C-11).
- *Export industries* sell more abroad over time, because Dravenland buyers earn more crowns from lumber sales (C-19).
- *Lumber buyers* keep the part of the duty they used to pay (C-23). *Dravenland sellers* receive more (C-20).
- *Taxpayers* save the cost of administering the duty, but must make up the lost revenue through other taxes, borrowing or reduced spending; the net effect cannot be determined (C-25, Tier C).

**Ambiguous effects.** Whether taxpayers as a group are better or worse off, until the budget response is known. Whether total lobbying effort rises or falls: the mill lobby now seeks restoration, while lumber users defend the repeal (C-12).

**What does not reverse.** Mill capital built behind the duty is not recovered; its owners bear the loss. Land and mill values reverse, but not for the same persons who gained twenty years ago. Domestic furniture making and exporting recover more slowly than they shrank, because skills, supplier links, retail placement and foreign customers lost over twenty years must be rebuilt (C-22, Tier C; GAP-023-1).

**Key conditions.** That the duty raised domestic prices (A-1, p = 0.9) underlies almost everything. The export gain rests on the duty's effect not being offset by capital flows (A-10, p = 0.65). Long-lived investment by lumber users rests on their trusting the repeal to last (A-12, p = 0.6).

**What this analysis cannot say.** How large any of these effects will be; how far domestic furniture making and exports come to resemble what they would have been without the duty; whether gains to lumber users and exporters outweigh losses to mill owners, landowners and mill workers; whether the repeal is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.lumber | price_paid (lumber) | decrease | short | visible | B | TX-7 in reverse | A-1, A-2 |
| C-2 | sawmills.domestic | net_price_received | decrease | short | visible | B | TX-7 in reverse | A-1 |
| C-3 | officials.enforcement (treasury) | tax_revenue | decrease | short | visible | A | TX-1 in reverse | none |
| C-4 | importers | quantity_traded (imported lumber) | increase | short | invisible | B | TX-2, OC-4 in reverse | A-1 |
| C-5 | sawmills.domestic | quantity_supplied | decrease | short–medium | invisible | B | TX-7 in reverse, TS-1 | A-1, A-3 |
| C-6 | sawmills.domestic | investment_target | decrease | short–medium | invisible | B | RS-6, TX-7 in reverse | A-1 |
| C-7 | sawmills.domestic | number_of_sellers | decrease | medium–long | invisible | B | RS-6, TS-1 | A-1, A-3 |
| C-8 | workers.sawmill | employment | decrease | medium | invisible | B | RS-6, LW-4 | A-1, A-3 |
| C-9 | workers.sawmill (displaced) | earnings | decrease | medium | invisible | B | RS-6, LW-4 | A-1, A-4 |
| C-10 | importers | reclassification | decrease | short | invisible | B | RS-5, TX-4 in reverse | A-5 |
| C-11 | buyers.lumber | quantity_traded (lumber, announcement window) | decrease | short | invisible | B | RS-8 | A-6 |
| C-12 | sawmills, timberland_owners, builders, exporters | lobbying_effort | ambiguous | medium | invisible | B | RS-7 | A-15 |
| C-13 | timberland_owners | asset_value | decrease | short | invisible | B | SB-4 in reverse | A-1, A-7 |
| C-14 | sawmills.domestic | asset_value (mill capital) | decrease | short | invisible | B | TX-7 in reverse, TS-1 | A-1, A-3 |
| C-15 | builders | quantity_supplied (new houses) | increase | medium | invisible | B | TX-7 in reverse, LW-4 | A-1, A-8 |
| C-16 | homebuyers | price_paid (new houses) | decrease | medium | invisible | B | TX-7 in reverse | A-1, A-8 |
| C-17 | furniture_makers.domestic | quantity_supplied | increase | medium | invisible | B | TX-7 in reverse, LW-4 | A-1, A-9 |
| C-18 | buyers.furniture | quantity_substitute (imported furniture) | decrease | medium | invisible | B | RS-1 in reverse | A-1, A-9 |
| C-19 | exporters | quantity_supplied, employment | increase | medium–long | invisible | B | TX-8 in reverse | A-1, A-10 |
| C-20 | sellers.foreign | net_price_received | increase | short | invisible | B | TX-7 in reverse | A-11 |
| C-21 | builders, furniture_makers.domestic | investment_target (lumber-using capacity) | increase | medium–long | invisible | C | TX-7 in reverse, LW-4, GAP-023-2 | A-1, A-12 |
| C-22 | furniture_makers.domestic | entry_rate | increase | long | invisible | C | LW-4, GAP-023-1 | A-1, A-9, A-13 |
| C-23 | buyers.lumber | resources_available_other_uses | increase | short | invisible | B | TX-1, OC-1 in reverse | A-2 |
| C-24 | officials.enforcement (customs) | enforcement_cost | decrease | short | invisible | A | OC-3 in reverse | none |
| C-25 | taxpayers | resources_available_other_uses | ambiguous | medium | invisible | C | OC-3, OC-1 in reverse vs GAP-023-3 | A-14 |

## Gaps found

- **GAP-023-1 Slow re-entry after a long restriction (hysteresis).** EN-3 and RS-6 describe how producers leave a trade whose return falls, and TS-1 how capacity wears out. No rule describes how industries that shrank under a long-standing policy (here, furniture makers squeezed by a duty on their input, and exporters) come back once it is removed: closed firms, lost skills, broken supplier links, and buyers' attachment to foreign brands must be rebuilt, at a cost and over a time that are not the mirror of the decline. Used for C-22 and the Tier C rows of the metamorphic check (T-11, T-12, T-13). *Proposed fix:* the same rule proposed as TS-6 in GAP-022-2 ("Stock changes persist after repeal"), extended with an entry clause: when a repeal raises the return to an activity that shrank under the policy, `entry_rate` and `number_of_sellers` rise only as the sunk costs of entry are paid, with the horizon set by a `reversal_cost` assumption.
- **GAP-023-2 Expectations of restoration.** TS-2 covers expectations that a policy in force will be extended. It does not cover the chance that a repealed duty is restored, which governs whether lumber users add long-lived capacity and whether mills scrap or mothball theirs. Used for C-21. *Proposed fix:* the rule proposed as TS-5 in GAP-022-1 ("Credibility of a repeal"), with this case as an example: a long history and a concentrated, organized losing group raise the probability of restoration.
- **GAP-023-3 Replacing lost revenue.** SB-1 says a subsidy is funded by someone, and TX-1 says a tax takes resources from those who bear it. No rule covers the mirror case: when a repeal removes revenue that the budget was spending, other taxes rise now, borrowing rises (and with it later taxes), or spending falls, and some identifiable group's `resources_available_other_uses` decreases. Used for C-25. *Proposed fix:* a rule OC-5 "Lost revenue is made up elsewhere": if a repeal or cut reduces `tax_revenue`, apply TX-1 and OC-1 to whichever group bears the replacement, named from the budget response; if the policy does not say, record the replacement chain with a `revenue_use` assumption and combine it with any chain that frees resources for the same group as ambiguous.
