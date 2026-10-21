# WE-035 Calorie counts on chain restaurant menus

Analyst: draft (Handbook 0.6, corrected under 0.8)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional state, modeled on a common type of disclosure law. It is a gap-probing example. The policy acts mainly by conveying information (CR-11c), which no earlier example has as its main channel. It neither prices, bans nor licenses anything. It tests:
- what a sign needs when buyers learn something: a premise about what they did not know, and about what they want;
- a compliance cost that falls on chains but not on small restaurants, and how the two compete;
- the incentive to stay below a size threshold;
- whether reformulating dishes is reclassification (RS-5);
- a fixed cost per menu item, and its effect on variety.

Health effects, nutrient intake and body weight are out of scope for version 1 (`02_ontology.md`, 2.4). They are not analyzed here, and nothing below should be read as a claim about them. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Sallow Menu Calorie Disclosure Act.** The State of Sallow has about 14,000 restaurants.
- **Covered chains.** 160 chains have 20 or more outlets in the state: about 5,200 outlets, serving about 45% of restaurant meals.
- **Near the threshold.** 38 chains have 10 to 19 outlets, and 9 of them have 17 to 19.
- **Posting today.** About 25% of covered chains already post calories on their menu boards, and about 70% post them on a website.

The neighboring State of Ambrine has no such rule. The bill was introduced on 10 March 2025 and passed on 28 August 2025. The Department of Health issued rules on 1 December 2025, and the Act takes effect on 1 July 2026, with no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| L1 Disclosure | `disclosure_mandate` | Calorie content of each "standard menu item" | Restaurant chains with 20 or more outlets in Sallow operating under the same name with substantially the same menu, counting franchised outlets | The count must appear next to each item on every menu and menu board, including drive-through boards, in type no smaller than the price, with the statement "2,000 calories a day is used for general nutrition advice". Combination meals are shown as a range. | L3 |
| L2 Accuracy | Part of L1 | Declared counts | Covered chains | The count needs a "reasonable basis" (laboratory analysis, nutrient databases, or recipes), and the basis must be kept on file. Actual content may not differ from the declared count by more than 20%. | — |
| L3 Exemptions | Exemption | — | — | Restaurants and chains with fewer than 20 outlets in Sallow. They may post counts voluntarily, and if they do, L2 applies. Also exempt: condiments for general use, daily specials, and "items appearing on the menu for a limited time" (undefined; U1). Grocery stores' prepared-food counters are not "restaurants" and are not covered. | — |
| L4 Enforcement | Enforcement | L1, L2 | County health departments | Checked during routine inspections, about two per outlet per year: presence and format, and the records behind the counts. Departments may send items for laboratory testing. The state funds $400,000 for laboratory tests in the first year, with nothing stated after. Fines: $250 per item with no count; $1,000 per item more than 20% off, per outlet; at most $10,000 per inspection. Fine revenue goes to county general funds. Counties receive no added funding for inspections. | — |

**Compliance costs in the record** (industry estimates submitted at the hearings).
- Analysis by a nutrient database costs about $60 per item, and laboratory analysis about $600 per item.
- A typical covered chain has 80 to 150 standard items.
- Menu boards cost $1,500 to $4,000 per outlet to replace. Boards are normally replaced every three to five years, and on major menu changes.

For a 20-outlet chain with 100 items, using laboratory analysis, the one-time cost is about $60,000 for analysis plus $50,000 for boards: about $5,500 per outlet. For a 500-outlet chain it is about $2,600 per outlet, and that is almost all boards. Each new item adds analysis cost and a board change at every outlet.

**Existing rules.** Packaged foods sold in shops already carry nutrition labels under national law, in both worlds. Without the Act, a restaurant that posts counts voluntarily is subject only to the general law on false advertising; there is no state tolerance, record-keeping duty or per-item fine (counterfactual law, CR-1).

**Unclear provision.**
- **U1: "items appearing on the menu for a limited time".** U1-a: a narrow reading, following the department's draft guidance: only items offered for two weeks or less are exempt, so seasonal items offered for six to twelve weeks must be analyzed and posted. U1-b: a broad reading, following industry comments: any item offered for less than 90 days in a year is exempt. The final rule repeats the statutory words without a number. No inspection practice exists yet.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| L1, L2 | Triangular in form: a `disclosure_mandate` attaches a condition (disclosure) to an exchange between private parties, without forbidding the exchange or fixing its price. It works mainly through what buyers learn (CR-11c), and through a fixed cost per item and per outlet borne by covered sellers (CR-4, fixed costs per item and per outlet). | Yes, for the roughly 75% of covered chains that do not now post on boards, and for buyers who do not look up website counts before ordering (A-1). | No pattern covers a disclosure mandate (candidate pattern, `02_ontology.md` 2.3). Derived from CR-1, CR-2, CR-4, CR-11c and CR-12; RS-17 for the threshold; RS-5 for U1; OC-1, OC-2, OC-3, OC-4 |
| L3 | Exemptions: a size threshold and an item boundary; a condition on voluntary posting | Yes, as boundaries (A-9, A-10, A-7) | RS-17, RS-5, RS-7 |
| L4 | Binary for the funded laboratory tests (payers from the general budget, as a group); fines are a transfer from fined chains to counties | Yes (A-15, A-17) | OC-1, OC-3, CR-8b |

**CR-1 operations, per actor class.** The counterfactual is no rule: chains post if and where they choose, under the general law on false advertising.
- `chains.covered`: operation 3. A cost (analysis, boards, records) and a risk (fines) are attached to offering each item, and a cost per outlet (boards) to operating each outlet. Offering an item without a count is removed (operation 1), and for most items that is the same as attaching the cost. The operations are dated 1 July 2026; before that they act through expectations (CR-1, 0.7 clarification on dated operations).
- Buyers at covered chains: none of the four operations applies to their options. Information that changes how much they value an option works through CR-11c (CR-1, 0.7 clarification).
- `restaurants.exempt`: operation 3 on the option of posting counts voluntarily: L3 attaches L2's tolerance, records and fines to it. Otherwise they are reached through CR-9.
- `chains.near_threshold`: operation 3 is attached to the option of opening a 20th outlet.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `chains.covered` (`sellers.current`) | 160 chains with 20 or more outlets | Must analyze, post and keep records for every standard item; fined for missing or inaccurate counts. |
| `chains.near_threshold` (`sellers.current`, `sellers.prospective` of new outlets) | Chains with about 15 to 19 outlets | A 20th outlet brings compliance for all outlets. |
| `buyers.covered_chains` (`buyers.current`) | People who eat at covered chains | See counts at the point of sale. |
| `restaurants.exempt` (`sellers.substitutes`) | Independents and chains under 20 outlets | Voluntary posting now carries L2's conditions; their competitors' costs and information change. |
| `grocery.prepared_food` (`sellers.substitutes`) | Grocery prepared-food counters | Uncovered substitute. |
| `intermediaries` | Food laboratories, nutrition consultants, menu-board printers | New demand. |
| `officials.enforcement` | County health departments | New inspection task; no added funding. |
| `taxpayers` and recipients of other state spending | Payers from the state's general budget | Fund $400,000 of laboratory tests. |
| `counties` | County general funds | Receive fines. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.covered_chains` | `quality_information` (calorie content at the point of sale) | increase | short | CR-11c, CR-2, CR-1 | A-1, A-2 |
| C-2 | `chains.covered` | `compliance_cost` (analysis, boards, records, staff training on portions) | increase | short | OC-2, CR-8c | none |
| C-25 | `buyers.covered_chains` (those who looked counts up before ordering) | `search_cost` (finding calorie counts before ordering) | decrease | short to medium | CR-11c, CR-8a | A-22 |

C-1 is the visible aim. Buyers at covered chains can see the calorie content of what they order before they order it. For chains that already post on boards nothing changes (A-1 limits the claim to the others). `quality_information` is defined in 2.4 as how easily buyers can judge a seller's quality. Calorie content is an attribute (`product_attribute`) rather than a quality that all buyers rank the same way, so the variable is used loosely here (Gaps found, d).

Buyers who already looked counts up on websites learn nothing new, but they no longer need to look: the time they spent doing so is freed (C-25; CR-8a, given A-22). The 0.6 version said that nothing changes for them; that missed this chain.

C-1 says only that buyers can know more. Whether anyone chooses differently is a further step (C-3). That step needs premises about what buyers believed before, and about which way those who learn something move (CR-11, 0.7 clarification "what a sign needs"; section 5).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `buyers.covered_chains` | `quantity_demanded` (higher-calorie items at covered chains) | decrease | short to medium | CR-11c, CR-4b; CR-12b, CR-12e | A-1, A-2, A-3, A-4 |
| C-4 | `buyers.covered_chains` | `product_attribute` (calories per item bought at covered chains, sales-weighted) | decrease | short to medium | CR-11c, CR-4b; CR-12b, CR-12e; CR-12a with C-5 | A-1, A-2, A-3, A-4 |
| C-5 | `chains.covered` | `product_attribute` (calories of existing items: lighter versions) | decrease | medium | CR-9, CR-4 (x: keep the recipe, y: a lighter version) | A-3, A-4, A-5 |
| C-6 | `chains.covered` | `variety` (standard menu items) | ambiguous | medium | CR-4c and CR-4 (fixed costs per item) (−); CR-9, CR-4 (+); CR-12b | A-4, A-6, A-19 |
| C-7 | `chains.covered` | `variety` (limited-time and seasonal items) | U1-a: decrease; U1-b: increase | medium | U1-a: CR-4c, CR-4 (fixed costs per item); U1-b: RS-5 | U1-a: A-6; U1-b: A-7 |
| C-8 | `chains.covered` | `quality_variability` (portion and recipe variation between outlets and servings) | decrease | medium | CR-4 (x: variable portions with fine risk, y: standardized portions) | A-8, A-20 |
| C-9 | `chains.near_threshold` | `investment_target` (new outlets beyond the 19th) | decrease | medium | RS-17, CR-4b, CR-4 (lumpy costs; fixed costs per outlet and per firm) | A-9 |
| C-10 | `chains.near_threshold`, small `chains.covered` (20 to 24 outlets) | `reclassification` (outlets opened, or franchised outlets renamed, under a second brand with a different menu) | increase | medium | RS-17, RS-5 | A-10 |
| C-11 | `chains.covered`, `restaurants.exempt` | `lobbying_effort` (chains: to extend the rule to small restaurants and grocery counters, or to widen the tolerance; exempt restaurants: to keep the exemption) | increase | short to medium | RS-7 | A-11 |

**C-3 and C-4: what buyers learn, and why a sign needs two premises.** By CR-11c, a policy can change choices by conveying information, and only to the extent that the information differs from what buyers already believed. The 0.7 CR-11 clarification states the two premises this needs.
- **Beliefs.** Some buyers' beliefs about calorie content differed from the posted counts (A-3). Buyers who already knew, or who correctly guessed, learn nothing and do not change.
- **Direction.** Of those who learn something, which way each moves depends on the error and on what they want. The rules never assume a ranking (CR-2), so the analysis cannot pick one.
  - A buyer who wants fewer calories, and learns that an item is heavier than they thought, chooses less of it (CR-4b): the − chain for higher-calorie items.
  - A buyer who learns that an item is lighter than they thought, or who seeks the most food for the money, may choose more of the heavier items: the + chain.

The two chains oppose each other (CR-12b). The sign rests on an empirical dominance premise (CR-12e, A-4): among buyers whose choices change, more move away from higher-calorie items than toward them. The evidence for it is surveys in which most buyers underestimate the calories of large items, and most say they would prefer fewer, together with sales data from chains that posted voluntarily.

C-4 is the mix of what is bought, recorded as `product_attribute` (0.7). The 0.6 version recorded it as more lower-calorie items demanded, which assumed that buyers who turn from heavy items buy lighter ones at the same chain rather than eat elsewhere; A-4 does not say that. The sales-weighted calories per item fall whichever they do, given A-4, and reformulation (C-5) pushes the same way (CR-12a).

Neither consequence is a claim about calories eaten. Buyers can eat more elsewhere in the day, and nutrient intake is out of scope.

**C-5: reformulation is not RS-5 here.** RS-5 needs a line between covered and uncovered forms. Lowering an item's calories does not take it out of L1's coverage: a lighter burger still needs a count. Demand-driven reformulation is instead derived directly. If buyers turn from higher-calorie items (C-3), chains offer lower-calorie versions of existing items where that costs less than the lost sales (CR-9 to the chains as sellers, then CR-4, with x the old recipe and y the lighter one). The premise is A-5. It is recorded as a fall in `product_attribute` of the items offered (0.7). RS-5 does apply in two places: the size threshold (C-10, with RS-17), and limited-time items under U1-b (C-7).

**C-6 and C-7: menu variety.** Each standard item now carries a fixed cost: analysis, a line on every board, and records (L1, L2). Under the 0.7 CR-4 clarification, a cost fixed per item offered bears on which items are offered (x: offer it, y: drop it), not on the price of each unit sold.
- **Standard items (C-6).** By CR-4c, the unit is the item, and the items with the lowest expected sales are dropped first. For them the fixed cost is large relative to their contribution (A-6; for a 20-outlet chain, $600 of analysis plus a board change at 20 outlets). Against that, some chains add new lower-calorie items to win back buyers who turn from heavier ones (CR-9, CR-4), rather than only reformulating existing items (A-19). The combined sign is ambiguous.
- **Limited-time items (C-7).**
  - Under U1-a, seasonal items must be analyzed before each launch, so fewer are launched (CR-4c). The cost is incurred for each new item, so it bears on launching, which is the margin for seasonal items.
  - Under U1-b, items offered for less than 90 days are exempt. New items are then introduced as limited-time offers rather than as standard items, to avoid the cost (RS-5, A-7), so limited-time items increase.

  This is the one consequence whose sign turns on the reading.

**C-8: portions.** L2 fines a count more than 20% off. A chain that lets outlets vary portions risks a fine, and a public finding that its counts are wrong. Standardizing portions and recipes lowers that risk (CR-4). Two premises are needed: that, for some items, serving-to-serving variation is large enough to matter for the tolerance (A-20), and that chains expect some checks, or some cost to reputation (A-8). Laboratory testing is rare (L4), and that keeps A-8 at 0.6. Items that cannot be standardized at reasonable cost are among those dropped (C-6, − chain).

**C-9 and C-10: the 20-outlet threshold (RS-17).**
- **Staying below (C-9).** For a chain with 19 outlets, the 20th outlet brings the whole compliance cost for all 20 outlets, about $110,000 in the record's example, on top of that outlet's own costs. That is a lumpy cost attached to the option "open a 20th outlet" (CR-4, units and lumpy costs; the 0.8 clarification on costs fixed per outlet or per firm, which bear on whether the outlet or firm operates and on the size at which it pays). Chains for which it reverses the ranking of "open" over "stay at 19" stay at 19. A-9 is supported by arithmetic on the record's figures against typical outlet profit.
- **Second brands (C-10).** Some chains grow under a second name with a different menu, or rename franchised outlets, so that neither brand reaches 20 (RS-17, RS-5). L1 counts outlets "under the same name with substantially the same menu". A second brand that keeps most of the menu would be challenged, which keeps A-10 at 0.55.

**Checked and not reported.**
- **RS-4 (relocation).** Restaurants serve local buyers, and buyers have no reason to cross to Ambrine to avoid seeing a number.
- **RS-3 (evasion).** Missing counts are visible on every inspection and fined per item. Inaccurate counts are a different matter: the incentive is not to evade but to choose the cheapest "reasonable basis", which is the nutrient database (L2 allows it). That keeps compliance cost down and accuracy within the tolerance for most items (A-2). Detected inaccurate counts (`legal_breach`) are implicit in C-23 and C-24 and not recorded separately.
- **Marginal outlets of covered chains.** By the 0.8 CR-4 clarification, the per-outlet board cost bears on whether an outlet operates. That it tips some existing outlet into closing needs A-24 (p = 0.4), below the cut-off.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `restaurants.exempt` | `quantity_traded` | ambiguous | medium | CR-9, CR-4 (+: buyers leaving chains; outlets not opened, C-9); CR-11c, CR-4 (−: buyers who value the counts move to chains); CR-12b | covered chains and exempt restaurants: `substitute`, close | A-3, A-9, A-12, A-21 |
| C-13 | `chains.near_threshold` | `asset_value` | decrease | short (from announcement) | RS-17, CR-7c, CR-10c | | A-9 |
| C-14 | `chains.covered` (menus whose calories buyers underestimated) | `asset_value` | ambiguous | short (from announcement) | CR-7c, CR-10c, CR-11c (−: compliance cost; lower demand where buyers leave the chain); CR-7c, CR-9 (+: buyers who value the counts); CR-12b | | A-3, A-4, A-12, A-21 |
| C-15 | `chains.covered` (other menus) | `asset_value` | ambiguous | short | CR-7c (−: compliance cost; +: demand from buyers who overestimated, or who value the counts); CR-12b | | A-3, A-12 |
| C-16 | `intermediaries` (food laboratories, nutrition consultants) | `quantity_traded` | increase | short | CR-9, CR-8b | analysis services `input_to` compliance | A-13 |
| C-17 | `intermediaries` (menu-board printers) | `quantity_traded` (board replacements, December 2025 to June 2026) | increase | short | RS-8, CR-10a | boards `input_to` compliance | A-14 |
| C-18 | `intermediaries` (menu-board printers) | `quantity_traded` (board replacements, July 2026 to June 2027) | ambiguous | short | RS-8 (−: replacements pulled into the window); CR-4c (+: changed items need new boards); CR-12b | boards `input_to` compliance | A-14, A-6 |
| C-19 | `buyers.covered_chains`, `chains.covered` | `quantity_traded` (low-volume items dropped because of the per-item cost) | decrease | medium | OC-4, CR-5a, CR-4c | | A-6 |
| C-26 | `restaurants.exempt` | `quality_information` (counts posted voluntarily) | ambiguous | medium | CR-1 (operation 3 on voluntary posting), CR-4b (−); CR-9, CR-4 (+); CR-12b | covered chains and exempt restaurants: `substitute`, close | A-12, A-23 |

**C-12: exempt restaurants, and why RS-16 gives no sign.** RS-16 needs a policy that moves buyers to a substitute. Here demand can move either way between covered chains and exempt restaurants.
- Toward exempt restaurants (+): buyers who learn that chain items are heavier than they believed, and who then eat elsewhere rather than choose a lighter item at the chain (A-21), and buyers who would rather not see the numbers. Outlets that near-threshold chains do not open (C-9) also leave their custom to others.
- Toward chains (−): buyers who value the counts now have a reason to prefer a chain (A-12).

With the direction of the shift ambiguous, RS-16 gives no sign for exempt restaurants' prices, and none is recorded. The compliance cost does not decide it either. It is fixed per item and per outlet, so under the CR-4 clarifications (0.7 per item, 0.8 per outlet and per firm) it bears on which items and outlets a chain offers, and on the size at which a chain pays, not on the price of each meal. The unit price could be signed only with a premise about entry and exit, which the record does not give. RS-14's precondition, a higher input price per unit of output, is not met. So no sign is recorded for prices at covered chains either.

**C-13 to C-15: firm values (CR-7c).**
- **Near-threshold chains (C-13).** Their option to grow past 19 outlets now carries the compliance cost, and their value falls from the time the Act became expected (RS-17). Buyers of such chains after August 2025 pay the lower price.
- **Covered chains whose items buyers underestimated (C-14).** Compliance cost pushes down. Demand pushes down only where buyers who turn from heavy items leave the chain rather than choose its lighter items (A-21); A-4 is a premise about the mix, not about spending at the chain. And buyers who value the counts prefer covered chains (A-12), which reaches these chains as much as any. With a (+) chain and no dominance premise, the sign is ambiguous (CR-12b).
- **Other covered chains (C-15).** Compliance cost pushes down, while buyers who overestimated their items, or who value the counts, push up. The sign is ambiguous.

**C-16 to C-18: suppliers of compliance.**
- **Laboratories and consultants (C-16).** They receive what chains spend on analysis (CR-8b). The resources are used up for the chains (CR-8c), and they are income to the laboratories.
- **Printers (C-17, C-18).** Boards are replaced every three to five years in any case. The Act pulls every covered outlet's replacement into the months before 1 July 2026, so replacements in that window increase (C-17). No provision makes the later window better for acting early, so RS-8's 0.8 clause on opposing timing chains does not apply to the window. In the following year two chains oppose each other, so the result is ambiguous (C-18):
  - replacements that would have happened then were already made (−);
  - each item added or changed now needs a board change with a count (+).

**C-26: voluntary posting by exempt restaurants.** L3 lets exempt restaurants post counts, but if they do, L2's tolerance, records and fines apply. Against the counterfactual law, where voluntary posting answers only to the general law on false advertising, that attaches a burden to the option of posting (CR-1, operation 3), so some that would have posted do not (CR-4b, A-23). Against that, buyers who value counts give exempt restaurants a reason to post to win them back (CR-9, CR-4; A-12). No premise says which dominates: ambiguous. The 0.6 version recorded "none directly" for exempt restaurants under CR-1, against its own L3.

**Not reported (below cut-off).**
- **Inference from silence.** Once chains post counts, buyers may read an exempt restaurant's silence as a sign that its food is heavy, and some exempt restaurants post voluntarily to avoid that. Under the 0.7 CR-11 clarification on silence, that inference is information conveyed by the policy and falls under CR-11c, with its own premise: A-16 (p = 0.4), below the cut-off. It would push C-26 the same way as A-12.
- **Grocery counters.** Buyers who dislike seeing counts shift to grocery prepared-food counters (A-18, p = 0.35).

**Stopping points.**
- Suppliers of ingredients for reformulated items (from C-5) are at depth 3 and diffuse; stopped.
- The labor of laboratories and printers (from C-16, C-17) is at depth 3; stopped.
- RS-9 (bundled trips), RS-10 (informal trade) and RS-11 (lock-in) do not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.covered_chains`, `quantity_demanded` (higher-calorie items), short to medium | Buyers who learn that items are lighter than they thought, or who seek more food per dollar (CR-11c, CR-4b). | Buyers who learn that items are heavier than they thought and prefer fewer calories (CR-11c, CR-4b). | Empirical premise, CR-12e: A-4 (p = 0.6). | **decrease** (C-3). If A-4 failed, **ambiguous**; if A-3 failed, `no_change`, and the consequence is not reported. |
| `buyers.covered_chains`, `product_attribute` (calories per item bought), short to medium | Buyers who move toward heavier items (CR-11c). | Buyers who move away from heavier items (CR-11c; A-4); lighter versions of existing items (C-5; CR-12a). | Empirical premise, CR-12e: A-4. | **decrease** (C-4). |
| `chains.covered`, `variety` (standard items), medium | New lower-calorie items to win back buyers who turn from heavier ones (A-4, A-19). | Low-volume items dropped because of the per-item cost (CR-4c; A-6). | None | **ambiguous** (C-6). |
| `chains.covered`, `variety` (limited-time items), medium | U1-b: new items introduced as exempt limited-time offers (RS-5; A-7). | U1-a: each seasonal item must be analyzed first (CR-4c; A-6). | Readings, not chains: one sign per reading. | **U1-a: decrease; U1-b: increase** (C-7). |
| `restaurants.exempt`, `quantity_traded`, medium | Buyers leaving chains after learning counts (A-3, A-21); outlets not opened by near-threshold chains (C-9; A-9). | Buyers who value counts prefer chains (A-12). | None | **ambiguous** (C-12). |
| `restaurants.exempt`, `quality_information` (voluntary posting), medium | Posting to win back buyers who value counts (A-12). | L2's conditions attached to voluntary posting (CR-1, operation 3; A-23). | None | **ambiguous** (C-26). |
| `chains.covered` (menus buyers underestimated), `asset_value`, short | Buyers who value counts prefer covered chains (A-12). | Compliance cost (C-2); lower demand where buyers leave the chain (C-3; A-3, A-4, A-21). | None | **ambiguous** (C-14). |
| `chains.covered` (other menus), `asset_value`, short | Demand from buyers who overestimated, or who value counts (A-3, A-12). | Compliance cost (C-2). | None | **ambiguous** (C-15). |
| `intermediaries` (printers), `quantity_traded`, July 2026 to June 2027 | Board changes for each changed item (A-6). | Replacements already pulled into the window (A-14). | None | **ambiguous** (C-18). |
| `chains.covered`, `resources_available_other_uses`, short to medium | None. | Compliance costs they keep paying (C-2); fines (A-17). | None needed; CR-12d | **decrease** (C-23). |
| `chains.covered`, `price_paid` (meals), medium | — | — | Not reported. Fixed costs per item and per outlet do not bear on the price of a meal without a premise on entry and exit (CR-4, 0.7 and 0.8), and the demand chain is ambiguous. | No consequence. |

No chains cancel exactly by construction (CR-12f).

## 8. Time structure

- **Announcement, March to August 2025.** Near-threshold chains reconsider their 20th outlet, and their values fall as passage becomes likely (C-9, C-13; CR-7c). Covered chains' values move as the expected compliance cost and the expected shift of demand are priced in (C-14, C-15). Lobbying over the threshold, the tolerance and U1 begins (C-11).
- **Window, December 2025 to June 2026.** Analysis and new boards are bought (C-16, C-17), and portions are standardized (C-8). Chains drop items that are not worth analyzing (C-6, C-19), and they may hold back new standard items until U1 is settled. This window is signed (C-17) because board replacement also happens without the Act, at other times.
- **Short run, from July 2026.** Counts appear (C-1), buyers who looked counts up no longer need to (C-25), and buyers who learn something change some choices (C-3, C-4). Because ordering at a familiar restaurant is a routine, the change may grow over months as buyers notice the counts (TS-8). Inspections begin (C-20), and fines are paid (C-23, C-24).
- **Medium run.** Reformulated items appear as recipes are tested (C-5). Menu variety settles (C-6, C-7). Near-threshold chains stay at 19 or grow under a second brand (C-9, C-10). Whether exempt restaurants gain or lose custom, and whether more or fewer of them post counts, shows here (C-12, C-26).
- **Fixed threshold.** The threshold is fixed at 20 outlets and does not erode with prices (TS-3 does not apply: it is not a product standard and has no price to move past). The compliance cost per outlet falls as a chain grows, so the threshold's effect is concentrated on chains near it (RS-17).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-20 | `officials.enforcement` (county health departments) | `enforcement_cost` (calorie checks) | increase | Inspector time spent on counts and records. | OC-3 |
| C-21 | `officials.enforcement` (county health departments, other inspection work) | `enforcement_cost` (other rules) | decrease | Other inspection work displaced, since county budgets are not raised. The cost falls on those that work protected. | OC-3, CR-8a |
| C-22 | `taxpayers`, recipients of other state spending, future taxpayers (group) | `resources_available_other_uses` | at_least_one_decrease | What the $400,000 for laboratory tests would otherwise have funded. | OC-1, OC-3, CR-8b |
| C-23 | `chains.covered` | `resources_available_other_uses` | decrease | Compliance costs, which chains keep paying because they keep offering their menus, and fines paid, an unavoidable sum once imposed. | CR-3 note, CR-8a, CR-8b; CR-12d |
| C-24 | `counties` | `non_tax_receipts` (fines to general funds) | increase | The receipt side of the fines in C-23. | CR-8b |

C-2's compliance spending is the main resource used up (CR-8c). Its receipt side is C-16 and C-17, not a gain to the economy, since the analysts' and printers' time could have served other ends (OC-1). The items no longer offered are C-19. The $400,000 comes from the state's general budget and the record names no tax, so its payers are recorded as a group (OC-1, OC-3, 0.8). Buyers' time spent reading counts is not recorded as a cost: reading is chosen, not imposed, and nothing in the record suggests it is costly; the time freed for buyers who used to look counts up is C-25.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most covered chains do not now post counts on boards, and most of their buyers do not look counts up before ordering. | binding | 0.8 | 25% post on boards; website traffic to nutrition pages against meals sold. | C-1 and everything that follows from it fail. |
| A-2 | Posted counts are within the tolerance for most items. | enforcement | 0.7 | Database methods; error rates in audits of voluntarily posted counts. | C-1 weakens; counts carry less information. |
| A-3 | Some buyers' beliefs about calorie content differ from the posted counts. | other | 0.75 | Surveys of estimated against actual calories for chain meals. | No change in choices; C-3, C-4, C-5 fail; C-12, C-14 and C-15 lose a chain. |
| A-4 | Among buyers whose choices change, more move away from higher-calorie items than toward them (dominance premise, CR-12e). | other | 0.6 | Direction of estimation errors (larger items underestimated more); stated preferences; sales mix at chains that posted voluntarily. | C-3 and C-4 become ambiguous; C-5 fails; C-6 and C-14 lose a chain. |
| A-5 | For some items, a lighter version costs less than the sales it would keep. | other | 0.6 | Recipe-development costs; reformulation at chains that posted voluntarily. | C-5 fails. |
| A-6 | The per-item fixed cost is material relative to the contribution of a chain's lowest-volume items. | other | 0.65 | The record's costs ($60 to $600 per item, plus board changes) against sales of the bottom tenth of items. | C-19 fails; the − chain of C-6 and the U1-a sign of C-7 fail. |
| A-7 | Under U1-b, chains can present new items as limited-time offers at low cost. | other | 0.6 | Current share of limited-time items in launches; marketing practice. | The U1-b sign of C-7 fails. |
| A-8 | Chains expect some accuracy checks, or a cost to reputation from wrong counts. | enforcement | 0.6 | Laboratory budget ($400,000 in year one); press coverage of audits elsewhere. | C-8 fails. |
| A-9 | For some near-threshold chains, the compliance cost reverses the ranking of opening a 20th outlet. | other | 0.65 | Record's cost example (about $110,000) against typical outlet profit; growth plans of the 9 chains with 17 to 19 outlets. | C-9 and C-13 fail; one chain of C-12 fails. |
| A-10 | For some small chains, a second brand costs less than compliance. | other | 0.55 | Branding and menu-development costs; the "substantially the same menu" test. | C-10 fails. |
| A-11 | Chains' associations and independent restaurants' associations can organize at a cost below their stake. | other | 0.75 | Existing state restaurant association; hearing testimony. | C-11 fails. |
| A-12 | Some buyers value the counts enough to prefer a covered chain over an exempt restaurant. | other | 0.6 | Surveys of buyers' use of counts; chains' reasons for posting voluntarily. | The − chain of C-12 and the + chains of C-14, C-15 and C-26 fail; C-14 becomes a decrease if A-21 holds. |
| A-13 | Many chains buy analysis from outside laboratories or consultants. | other | 0.8 | Industry practice; hearing testimony. | C-16 fails. |
| A-14 | Boards are replaced every few years without the Act. | durability | 0.8 | Industry replacement cycles. | C-17 is a rise with no matching dip; C-18 becomes an increase. |
| A-15 | County inspection budgets are not raised for the new task. | revenue_use | 0.65 | No appropriation in the Act; county budget calendars. | C-21 becomes a cost to a group of county payers instead (county taxpayers, recipients of other county spending; OC-3). |
| A-16 | Exempt restaurants post counts voluntarily because buyers read silence as a bad sign (CR-11, silence). | other | 0.4 | Voluntary posting by independents where chains post. | Below cut-off; not reported. |
| A-17 | Some inaccurate counts are detected and fined. | enforcement | 0.55 | Laboratory budget; inspection frequency. | C-24 fails; C-23 loses its second chain. |
| A-18 | Buyers who dislike seeing counts shift to grocery prepared-food counters. | substitutability | 0.35 | No evidence beyond anecdote. | Below cut-off; not reported. |
| A-19 | Some chains add new lower-calorie items, rather than only reformulating existing ones, to keep buyers who turn from heavier items. | other | 0.6 | Launches of "lighter" menu sections at chains that posted voluntarily. | The + chain of C-6 fails; C-6 becomes a decrease if A-6 holds. |
| A-20 | For some items, calorie content varies between servings by enough that portion control matters for staying within 20%. | other | 0.6 | A-2 says most items, not all, are within tolerance; variation in hand-portioned items. | C-8 fails. |
| A-21 | Some buyers who turn from a heavy item after seeing its count go to another restaurant, including exempt ones, rather than choose another item at the same chain. | substitutability | 0.6 | Restaurant density (14,000 restaurants, 55% of meals at exempt ones); A-3 implies some buyers learn their usual order is heavier than they thought. | The + chain of C-12 through buyers leaving chains, and the demand chain of C-14, fail. |
| A-22 | Some buyers at covered chains look counts up on websites before ordering. | other | 0.7 | 70% of covered chains post counts on a website; traffic to nutrition pages (A-1 says most buyers do not, not that none do). | C-25 fails. |
| A-23 | Some exempt restaurants are near the margin of posting counts voluntarily: some would post without the Act, and some would post to win back buyers. | other | 0.6 | 25% of covered chains post voluntarily today; small chains with websites; A-12. | C-26 is not reported. |
| A-24 | For some outlets of covered chains near closing, the one-time per-outlet board cost tips the decision to close. | other | 0.4 | Board costs ($1,500 to $4,000) against outlet profit; boards are replaced on a normal cycle anyway. | Below cut-off; not reported. |

### Final check before the report

The eight checks in `03_workflow.md` were run on the list.

1. **Uncombined chains.** Every key reached by two chains is combined in section 7:
   - demand for heavier items, and the calorie mix of what is bought;
   - variety;
   - exempt restaurants' trade and their voluntary posting;
   - chains' values, both subclasses, with the A-12 chain reaching each;
   - printers' second year;
   - chains' means.

   Prices at chains and at exempt restaurants were checked and are not reported, for the reasons given in section 6.
2. **Single signs for a group.** One group is claimed: the payers of the laboratory budget (C-22), as OC-1 and OC-3 require for a general budget. RS-14's "price and/or quantity" was considered for chains and rejected, because its precondition is not met and fixed costs per item and per outlet leave the unit price unsigned (CR-4, 0.7 and 0.8).
3. **Baseline.** Every sign is against Sallow without the Act, in which 25% of covered chains post on boards voluntarily and voluntary posting answers only to the general law on false advertising. It is not against Ambrine, and not against a world with no posting at all.
4. **Worse off is not poorer.** `resources_available_other_uses` is signed for the payers of the laboratory budget (C-22) and for covered chains (C-23), which keep paying compliance costs for menus they keep offering, and pay fines they cannot avoid. It is not signed for buyers.
5. **Timing.** Board replacement happens with and without the Act, so both windows are signed (C-17, C-18). No provision improves the earlier window (RS-8, 0.8). Holding back new items until U1 is settled is a path note.
6. **Both sides of transfers.** The laboratory fund is recorded on both sides (C-22; the laboratories in C-16), and so are the fines (C-23, C-24). Compliance spending is recorded on both sides (C-2; C-16, C-17).
7. **Every actor class, every core rule.**
   - CR-7c was applied to near-threshold chains and to covered chains.
   - CR-1 was applied to exempt restaurants' voluntary posting (C-26).
   - CR-9 was applied to exempt restaurants, grocery counters and suppliers.
   - CR-6 does not apply, since no price or quantity is fixed.
   - OC-3 was applied to the counties and the state.
   - CR-11c is the main channel, including the silence inference (not reported).
8. **Unstated premises.**
   - What buyers did not know is A-3, and which way they move is A-4.
   - Where buyers who turn from heavy items go is A-21.
   - "Some actors are at the margin" is A-6, A-9, A-10, A-19 and A-23.
   - Serving variation that matters for the tolerance is A-20.
   - The ability to organize is A-11.

## 11. Report

**The policy.** From 1 July 2026, restaurant chains with 20 or more outlets in Sallow must show the calorie count of each standard item on menus and menu boards. Counts must have a documented basis and be within 20% of actual content. Fines apply for missing or inaccurate counts, checked by county inspectors during routine inspections. Smaller chains and independent restaurants are exempt, but if they post counts voluntarily the same accuracy rules apply. So are daily specials and items offered "for a limited time", a phrase the law does not define (U1).

**Visible consequences.** Buyers at covered chains can see calorie counts when they order (C-1). Chains spend on analyzing items, replacing boards and keeping records (C-2).

**Invisible consequences.**
- *Buyers at covered chains.* Fewer higher-calorie items are ordered, and the average item bought is lighter (C-3, C-4). This holds given that some buyers misjudged calories (A-3), and that more of those who change move toward lighter items than away from them (A-4). Buyers who used to look counts up online no longer need to (C-25). Some low-volume items are no longer offered at all (C-19).
- *Covered chains.*
  - They offer lighter versions of some items (C-5).
  - They standardize portions to stay within the tolerance (C-8).
  - Their offering of seasonal items depends on how "limited time" is read (C-7). Under the narrow reading there are fewer seasonal items, because each must be analyzed first. Under the broad reading new items come out as limited-time offers to avoid analysis.
  - They have less to spend on other things, through compliance costs and fines (C-23).
  - Chains and independents lobby over the threshold and the exemptions (C-11).
- *Chains near the threshold.* Some stop at 19 outlets (C-9) or grow under a second brand (C-10), and their values fell when the Act became expected (C-13).
- *Suppliers.* Laboratories and consultants sell more analysis (C-16). Printers replaced boards in the months before the effective date (C-17).
- *Public side.*
  - County health departments spend inspection time on counts (C-20). Since their budgets are not raised, other inspection work falls (C-21).
  - The laboratory tests are paid from the state budget, by taxpayers or by recipients of other state spending (C-22).
  - Fines move money from chains to counties (C-23, C-24).

**Ambiguous effects.**
- The number of standard menu items (C-6): items dropped because of the per-item cost, against new lighter items.
- Whether independent restaurants gain or lose custom (C-12): buyers who leave chains, against buyers who prefer chains because they post counts.
- Whether more or fewer independents post counts voluntarily (C-26): the accuracy rules now attached to posting, against buyers who value counts.
- The value of covered chains (C-14, C-15): compliance costs and, for heavy menus, buyers who leave, against buyers who now prefer a chain that posts counts.
- Printers' work in the year after the effective date (C-18).
- Meal prices at chains and at independents are not signed. The compliance cost is fixed per item and per outlet, so it bears on what is offered and which outlets open, not on the price of each meal.

**Key conditions.**
- Every change in buyers' choices rests on buyers having misjudged calories (A-3, p = 0.75). Its direction rests on more of them moving toward lighter items (A-4, p = 0.6).
- The variety and threshold effects rest on the per-item and per-chain costs being material at the margin (A-6, p = 0.65; A-9, p = 0.65).
- How "limited time" is read decides the sign for seasonal items.

**What this analysis cannot say.**
- Anything about health, nutrient intake, calories eaten over a day, or body weight. These are out of scope for version 1, and not analyzed.
- How many buyers change what they order, or by how much.
- Whether buyers who change their order are better or worse off by their own ranking: a disclosure adds no option and removes none, so CR-3 does not say.
- Whether the information is worth its cost to chains, inspectors and taxpayers, or whether the Act is desirable.
- Which reading of "limited time" will prevail.
- Whether independent restaurants read silence as a reason to post (A-16, below the cut-off).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.covered_chains | quality_information (calorie content at point of sale) | increase | short | visible | B | CR-11c, CR-2, CR-1 | A-1, A-2 |
| C-2 | chains.covered | compliance_cost | increase | short | visible | A | OC-2, CR-8c | none |
| C-3 | buyers.covered_chains | quantity_demanded (higher-calorie items) | decrease | short–medium | invisible | B | CR-11c, CR-4b; CR-12b, CR-12e | A-1, A-2, A-3, A-4 |
| C-4 | buyers.covered_chains | product_attribute (calories per item bought, sales-weighted) | decrease | short–medium | invisible | B | CR-11c, CR-4b; CR-12b, CR-12e; CR-12a | A-1, A-2, A-3, A-4 |
| C-5 | chains.covered | product_attribute (calories of existing items: lighter versions) | decrease | medium | invisible | B | CR-9, CR-4 | A-3, A-4, A-5 |
| C-6 | chains.covered | variety (standard items) | ambiguous | medium | invisible | B | CR-4c, CR-4 fixed costs per item (−); CR-9, CR-4 (+); CR-12b | A-4, A-6, A-19 |
| C-7 | chains.covered | variety (limited-time items) | U1-a: decrease; U1-b: increase | medium | invisible | B | U1-a: CR-4c, CR-4 fixed costs per item; U1-b: RS-5 | U1-a: A-6; U1-b: A-7 |
| C-8 | chains.covered | quality_variability (portions) | decrease | medium | invisible | B | CR-4 | A-8, A-20 |
| C-9 | chains.near_threshold | investment_target (20th and later outlets) | decrease | medium | invisible | B | RS-17, CR-4b, CR-4 (lumpy costs; fixed costs per outlet and per firm) | A-9 |
| C-10 | chains.near_threshold, small chains.covered | reclassification (second brands) | increase | medium | invisible | B | RS-17, RS-5 | A-10 |
| C-11 | chains.covered, restaurants.exempt | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-11 |
| C-12 | restaurants.exempt | quantity_traded | ambiguous | medium | invisible | B | CR-9, CR-4, CR-11c; CR-12b | A-3, A-9, A-12, A-21 |
| C-13 | chains.near_threshold | asset_value | decrease | short | invisible | B | RS-17, CR-7c, CR-10c | A-9 |
| C-14 | chains.covered (menus underestimated) | asset_value | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-11c, CR-9; CR-12b | A-3, A-4, A-12, A-21 |
| C-15 | chains.covered (other menus) | asset_value | ambiguous | short | invisible | B | CR-7c; CR-12b | A-3, A-12 |
| C-16 | intermediaries (laboratories, consultants) | quantity_traded | increase | short | invisible | B | CR-9, CR-8b | A-13 |
| C-17 | intermediaries (printers) | quantity_traded (December 2025–June 2026) | increase | short | invisible | B | RS-8, CR-10a | A-14 |
| C-18 | intermediaries (printers) | quantity_traded (July 2026–June 2027) | ambiguous | short | invisible | B | RS-8 (−), CR-4c (+); CR-12b | A-14, A-6 |
| C-19 | buyers.covered_chains, chains.covered | quantity_traded (dropped low-volume items) | decrease | medium | invisible | B | OC-4, CR-5a, CR-4c | A-6 |
| C-20 | officials.enforcement | enforcement_cost (calorie checks) | increase | short | invisible | A | OC-3 | none |
| C-21 | officials.enforcement | enforcement_cost (other inspection work) | decrease | short–medium | invisible | B | OC-3, CR-8a | A-15 |
| C-22 | taxpayers, recipients of other state spending, future taxpayers (group) | resources_available_other_uses | at_least_one_decrease | short | invisible | A | OC-1, OC-3, CR-8b | none |
| C-23 | chains.covered | resources_available_other_uses | decrease | short–medium | invisible | A | CR-3 note, CR-8a (compliance); CR-8b (fines); CR-12d | chain 1: none; chain 2: A-17 |
| C-24 | counties | non_tax_receipts (fines) | increase | short–medium | invisible | B | CR-8b | A-17 |
| C-25 | buyers.covered_chains (who looked counts up) | search_cost (finding counts before ordering) | decrease | short–medium | invisible | B | CR-11c, CR-8a | A-22 |
| C-26 | restaurants.exempt | quality_information (counts posted voluntarily) | ambiguous | medium | invisible | B | CR-1, CR-4b (−); CR-9, CR-4 (+); CR-12b | A-12, A-23 |

## Corrections after the core-only comparison

- **Header** changed to catalog 0.8. L1 is now a `disclosure_mandate`, and RS-17 (0.7, size thresholds) is cited for C-9, C-10 and C-13.
- **C-14**: sign changed from decrease to ambiguous. The A-12 chain (buyers who value counts prefer covered chains) reaches these chains too. The demand chain also needs a premise that buyers leave the chain rather than switch to its lighter items (new A-21).
- **C-4**: variable changed from `quantity_demanded` of lower-calorie items to `product_attribute` (sales-weighted calories per item bought). This removes the hidden premise that buyers stay at the chain. **C-5** is now recorded as `product_attribute` too (0.7).
- **C-6**: the (+) chain now names its premise (new A-19). **C-8**: the premise on serving variation is now explicit (new A-20). **C-12**: the (+) chain now names A-21.
- **C-22**: changed to a group of payers from the general budget with `at_least_one_decrease` (OC-1 and OC-3, 0.8). **C-24**: `tax_revenue` changed to `non_tax_receipts` (0.7). **A-15** "if false" now names a group of payers.
- **C-23**: widened from fined chains to all covered chains. They keep paying compliance costs for the menus they keep (CR-3 note), and fines are a second chain (CR-12d). Final check 4 was revised to match.
- **Added**: C-25, buyers' lower search cost for counts (new A-22). C-26, exempt restaurants' voluntary posting, ambiguous: L3 attaches L2 to voluntary posting (CR-1, operation 3) against A-12 (new A-23). The CR-1 list for exempt restaurants is corrected, and the counterfactual law is stated.
- **Prices** are still not signed, now on the 0.7 and 0.8 CR-4 clarifications on costs fixed per item and per outlet. The per-outlet chain on existing outlets was checked and is not reported (A-24, p = 0.4).
- **Rejected**: the core's standard-item variety as a decrease (core C-10). The (+) chain of new lighter items is derivable (CR-9, CR-4), so C-6 stays ambiguous.
- **Rejected**: the core's `no_change` for seasonal items under U1-b (core C-11). Items launched as exempt offers enlarge that band, so C-7 stays an increase under U1-b.
- **Not adopted (J)**: separate keys for detected breaches (`legal_breach`, core C-14) and for meals at covered chains (core C-24). The per-outlet burden on small covered chains (core C-26) is also left out. It is a comparison between chains rather than a change against the counterfactual, and 0.8 does not settle how to record it.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 and the patterns cited. The steps that needed the most care, buyers' response to information (CR-11c with CR-2 and CR-12e) and the threshold (CR-4's lumpy costs, RS-17), are derivable but need explicit premises. Whether buyers who change their order are better off cannot be said: a disclosure adds and removes no option, so CR-3 gives nothing (see b).

**(b) Unclear core rules (wording that was hard to apply here).**
- **CR-11c and the premises a sign needs** (closed in 0.7: CR-11 clarification "what a sign needs"). CR-11c says a policy changes actions by conveying information "and only to that extent". It did not say what a derivation must state to get a sign. This case needed two separate premises: what buyers believed before (A-3), and which way those who learn something move (A-4).
- **CR-11c and inference from silence** (closed in 0.7: CR-11 clarification on silence; the inference falls under CR-11c with its own premise, here A-16). When some sellers must disclose and others are exempt, buyers may draw conclusions from the exempt sellers' silence.
- **CR-1 and information that changes how an option is enjoyed** (closed in 0.7 for recording: CR-1 clarification, information is not one of the four operations and works through CR-11c). Whether a buyer who enjoys a dessert less once they see its count is worse off by their own ranking remains open; CR-3 does not cover it, and no consequence is reported on it.
- **CR-3 and CR-4 on fixed costs and price** (closed in 0.7 for costs per item and in 0.8 for costs per outlet or per firm: CR-4 clarification). A cost fixed per item or per outlet bears on whether to offer the item or operate the outlet, not on the price of each unit sold; the unit price is signed only with a premise about entry and exit.

**(c) Missing patterns (derived moves likely to recur).**
- **Proposed pattern, a mandated disclosure** (still a candidate: `disclosure_mandate` is in 2.3 with "CR-11c; candidate pattern"; the premises it needs are now in the CR-11 clarifications).
  - **If:** a policy requires sellers to show buyers a fact about the good before purchase.
  - **Then:**
    - `quality_information` increases for buyers of covered sellers who did not already have the fact (CR-11c), and `search_cost` falls for those who used to look it up.
    - Choices change only for buyers whose beliefs differed (premise). Their direction needs a premise on the errors and ends, or a dominance premise; without one, `quantity_demanded` of the affected items is `ambiguous`.
    - Sellers adjust the disclosed attribute where demand shifts (`product_attribute`; CR-9, CR-4).
    - Demand between covered and exempt sellers moves both ways: toward covered sellers for buyers who value the fact, and away for those who learn something unwelcome. It is `ambiguous` unless a premise says which dominates.
    - Where voluntary disclosure by exempt sellers is made subject to the mandate's rules, a burden is attached to it (CR-1, operation 3).
  - **Derivation:** CR-11c, CR-2, CR-4, CR-9, CR-12b, CR-12e. It recurs in nutrition labels, energy ratings, fee disclosures and safety ratings.
- **Proposed pattern, a size threshold** (closed in 0.7: RS-17).
- **Proposed pattern, a fixed cost per variant** (covered in 0.7 by the CR-4 clarification on fixed costs per item; no separate pattern).
  - **If:** a policy attaches a fixed cost to each version of a good offered: analysis, certification, a label.
  - **Then:** `variety` decreases among the lowest-volume versions (CR-4c, with the item as the unit); versions are introduced in whichever form the definitions exempt (RS-5); sellers with more volume per version bear less per unit sold, which shifts competition toward them (CR-7).
  - **Derivation:** CR-4c, CR-4 (fixed costs per item), RS-5, CR-7.
- **Note on RS-5 and reformulation.** RS-5 does not cover demand-driven reformulation. A lower calorie count does not move an item out of coverage. Reformulation is derived from CR-9 and CR-4. The note is recorded so that later analysts do not cite RS-5 for it.

**(d) Vocabulary.**
- **No instrument type for a disclosure or labeling mandate** (closed in 0.7: `disclosure_mandate`).
- **No variable for a product's composition or attribute** (closed in 0.7: `product_attribute`, now used in C-4 and C-5).
- **`quality_information` is defined in terms of quality.** Calorie content is an attribute that buyers rank differently, not a quality all prefer more of. C-1 and C-26 still use the variable loosely. Either widen the definition ("how easily buyers can learn a seller's quality or a named attribute before buying") or add `attribute_information`. Open.
- **No variable for fines** (closed in 0.7: `non_tax_receipts`, now used in C-24).
- **Group signs whose members move in opposite directions** (closed in 0.7: `at_least_one_as_stated`).
