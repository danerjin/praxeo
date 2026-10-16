# WE-035 Calorie counts on chain restaurant menus

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

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
| L1 Disclosure | Disclosure mandate (no instrument type in 2.3; see Gaps found, d) | Calorie content of each "standard menu item" | Restaurant chains with 20 or more outlets in Sallow operating under the same name with substantially the same menu, counting franchised outlets | The count must appear next to each item on every menu and menu board, including drive-through boards, in type no smaller than the price, with the statement "2,000 calories a day is used for general nutrition advice". Combination meals are shown as a range. | L3 |
| L2 Accuracy | Part of L1 | Declared counts | Covered chains | The count needs a "reasonable basis" (laboratory analysis, nutrient databases, or recipes), and the basis must be kept on file. Actual content may not differ from the declared count by more than 20%. | — |
| L3 Exemptions | Exemption | — | — | Restaurants and chains with fewer than 20 outlets in Sallow. They may post counts voluntarily, and if they do, L2 applies. Also exempt: condiments for general use, daily specials, and "items appearing on the menu for a limited time" (undefined; U1). Grocery stores' prepared-food counters are not "restaurants" and are not covered. | — |
| L4 Enforcement | Enforcement | L1, L2 | County health departments | Checked during routine inspections, about two per outlet per year: presence and format, and the records behind the counts. Departments may send items for laboratory testing. The state funds $400,000 for laboratory tests in the first year, with nothing stated after. Fines: $250 per item with no count; $1,000 per item more than 20% off, per outlet; at most $10,000 per inspection. Fine revenue goes to county general funds. Counties receive no added funding for inspections. | — |

**Compliance costs in the record** (industry estimates submitted at the hearings).
- Analysis by a nutrient database costs about $60 per item, and laboratory analysis about $600 per item.
- A typical covered chain has 80 to 150 standard items.
- Menu boards cost $1,500 to $4,000 per outlet to replace. Boards are normally replaced every three to five years, and on major menu changes.

For a 20-outlet chain with 100 items, using laboratory analysis, the one-time cost is about $60,000 for analysis plus $50,000 for boards: about $5,500 per outlet. For a 500-outlet chain it is about $2,600 per outlet, and that is almost all boards. Each new item adds analysis cost and a board change at every outlet.

**Existing rules.** Packaged foods sold in shops already carry nutrition labels under national law, in both worlds.

**Unclear provision.**
- **U1: "items appearing on the menu for a limited time".** U1-a: a narrow reading, following the department's draft guidance: only items offered for two weeks or less are exempt, so seasonal items offered for six to twelve weeks must be analyzed and posted. U1-b: a broad reading, following industry comments: any item offered for less than 90 days in a year is exempt. The final rule repeats the statutory words without a number. No inspection practice exists yet.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| L1, L2 | Triangular in form: it attaches a condition (disclosure) to an exchange between private parties, without forbidding the exchange or fixing its price. It works mainly through what buyers learn (CR-11c), and through a fixed cost per item and per outlet borne by covered sellers. | Yes, for the roughly 75% of covered chains that do not now post on boards, and for buyers who do not look up website counts before ordering (A-1). | No pattern covers a disclosure mandate (Gaps found, c). Derived from CR-1, CR-2, CR-4, CR-11c and CR-12; RS-5 for the threshold and U1; OC-2, OC-3, OC-4 |
| L3 | Exemptions: a size threshold and an item boundary | Yes, as boundaries (A-9, A-10, A-7) | RS-5, RS-7 |
| L4 | Binary for the funded laboratory tests (taxpayers); fines are a transfer from fined chains to counties | Yes (A-15, A-17) | OC-3, CR-8b |

**CR-1 operations, per actor class.** The counterfactual is no rule: chains post if and where they choose.
- `chains.covered`: operation 3. A cost (analysis, boards, records) and a risk (fines) are attached to offering each item. Offering an item without a count is removed (operation 1), and for most items that is the same as attaching the cost.
- Buyers at covered chains: none of the four operations applies to their options. The policy changes their actions only through what it tells them (CR-1, last sentence; CR-11c).
- `restaurants.exempt`: none directly. They are reached through CR-9.
- `chains.near_threshold`: operation 3 is attached to the option of opening a 20th outlet.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `chains.covered` (`sellers.current`) | 160 chains with 20 or more outlets | Must analyze, post and keep records for every standard item; fined for missing or inaccurate counts. |
| `chains.near_threshold` (`sellers.current`, `sellers.prospective` of new outlets) | Chains with about 15 to 19 outlets | A 20th outlet brings compliance for all outlets. |
| `buyers.covered_chains` (`buyers.current`) | People who eat at covered chains | See counts at the point of sale. |
| `restaurants.exempt` (`sellers.substitutes`) | Independents and chains under 20 outlets | Unchanged rules; their competitors' costs and information change. |
| `grocery.prepared_food` (`sellers.substitutes`) | Grocery prepared-food counters | Uncovered substitute. |
| `intermediaries` | Food laboratories, nutrition consultants, menu-board printers | New demand. |
| `officials.enforcement` | County health departments | New inspection task; no added funding. |
| `taxpayers` | State budget | Fund $400,000 of laboratory tests. |
| `counties` | County general funds | Receive fines. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.covered_chains` | `quality_information` (calorie content at the point of sale) | increase | short | CR-11c, CR-2, CR-1 | A-1, A-2 |
| C-2 | `chains.covered` | `compliance_cost` (analysis, boards, records, staff training on portions) | increase | short | OC-2, CR-8c | none |

C-1 is the visible aim. Buyers at covered chains can see the calorie content of what they order before they order it. For chains that already post on boards, and for buyers who already looked counts up on websites, nothing changes (A-1 limits the claim to the others). `quality_information` is defined in 2.4 as how easily buyers can judge a seller's quality. Calorie content is an attribute rather than a quality that all buyers rank the same way, so the variable is used loosely here (Gaps found, d).

C-1 says only that buyers can know more. Whether anyone chooses differently is a further step (C-3). That step needs premises about what buyers believed before, and about what they want (section 5).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `buyers.covered_chains` | `quantity_demanded` (higher-calorie items at covered chains) | decrease | short to medium | CR-11c, CR-4b; CR-12b, CR-12e | A-1, A-2, A-3, A-4 |
| C-4 | `buyers.covered_chains` | `quantity_demanded` (lower-calorie items at covered chains) | increase | short to medium | CR-11c, CR-4b; CR-12b, CR-12e | A-1, A-2, A-3, A-4 |
| C-5 | `chains.covered` | `quantity_supplied` (reduced-calorie versions of existing items) | increase | medium | CR-9, CR-4 | A-3, A-4, A-5 |
| C-6 | `chains.covered` | `variety` (standard menu items) | ambiguous | medium | CR-4c (−); CR-9, CR-4 (+); CR-12b | A-4, A-6 |
| C-7 | `chains.covered` | `variety` (limited-time and seasonal items) | U1-a: decrease; U1-b: increase | medium | U1-a: CR-4c, CR-3; U1-b: RS-5 | U1-a: A-6; U1-b: A-7 |
| C-8 | `chains.covered` | `quality_variability` (portion and recipe variation between outlets and servings) | decrease | medium | CR-4 (x: variable portions with fine risk, y: standardized portions) | A-8 |
| C-9 | `chains.near_threshold` | `investment_target` (new outlets beyond the 19th) | decrease | medium | CR-4b, CR-4 (lumpy costs) | A-9 |
| C-10 | `chains.near_threshold`, small `chains.covered` (20 to 24 outlets) | `reclassification` (outlets opened, or franchised outlets renamed, under a second brand with a different menu) | increase | medium | RS-5 | A-10 |
| C-11 | `chains.covered`, `restaurants.exempt` | `lobbying_effort` (chains: to extend the rule to small restaurants and grocery counters, or to widen the tolerance; exempt restaurants: to keep the exemption) | increase | short to medium | RS-7 | A-11 |

**C-3 and C-4: what buyers learn, and why a sign needs two premises.** By CR-11c, a policy can change choices by conveying information, and only to the extent that the information differs from what buyers already believed. Two premises are needed.
- **Beliefs.** Some buyers' beliefs about calorie content differed from the posted counts (A-3). Buyers who already knew, or who correctly guessed, learn nothing and do not change.
- **Ends.** Of those who learn something, which way each moves depends on the error and on what they want. The rules never assume a ranking (CR-2), so the analysis cannot pick one.
  - A buyer who wants fewer calories, and learns that an item is heavier than they thought, chooses less of it (CR-4b): the − chain for higher-calorie items.
  - A buyer who learns that an item is lighter than they thought, or who seeks the most food for the money, may choose more of the heavier items: the + chain.

The two chains oppose each other (CR-12b). The sign rests on an empirical dominance premise (CR-12e, A-4): among buyers whose choices change, more move away from higher-calorie items than toward them. The evidence for it is surveys in which most buyers underestimate the calories of large items, and most say they would prefer fewer, together with sales data from chains that posted voluntarily. C-4 is the substitution side of the same choices, and it rests on the same premises.

Neither consequence is a claim about calories eaten. Buyers can eat more elsewhere in the day, and nutrient intake is out of scope.

**C-5: reformulation is not RS-5 here.** RS-5 needs a line between covered and uncovered forms. Lowering an item's calories does not take it out of L1's coverage: a lighter burger still needs a count. Demand-driven reformulation is instead derived directly. If buyers' demand moves toward lower-calorie items (C-4), chains offer lower-calorie versions of existing items where that costs less than the lost sales (CR-9 to the chains as sellers, then CR-4, with x the old recipe and y the lighter one). The premise is A-5.

No variable records an item's composition, so the move is recorded as an increase in the quantity supplied of a named good, reduced-calorie versions (Gaps found, d). RS-5 does apply in two places: the size threshold (C-10), and limited-time items under U1-b (C-7).

**C-6 and C-7: menu variety.** Each standard item now carries a fixed cost: analysis, a line on every board, and records (L1, L2).
- **Standard items (C-6).** By CR-4c, the unit is the item, and the items with the lowest expected sales are dropped first. For them the fixed cost is large relative to their contribution (A-6; for a 20-outlet chain, $600 of analysis plus a board change at 20 outlets). Against that, chains add new lower-calorie items to serve the demand in C-4. The combined sign is ambiguous.
- **Limited-time items (C-7).**
  - Under U1-a, seasonal items must be analyzed before each launch, so fewer are launched (CR-4c). Under CR-3, the cost is incurred for each new item, so it bears on launching, which is the margin for seasonal items.
  - Under U1-b, items offered for less than 90 days are exempt. New items are then introduced as limited-time offers rather than as standard items, to avoid the cost (RS-5, A-7), so limited-time items increase.

  This is the one consequence whose sign turns on the reading.

**C-8: portions.** L2 fines a count more than 20% off. A chain that lets outlets vary portions risks a fine, and a public finding that its counts are wrong. Standardizing portions and recipes lowers that risk (CR-4). The premise is that chains expect some checks, or some cost to reputation (A-8). Laboratory testing is rare (L4), and that keeps A-8 at 0.6. Items that cannot be standardized at reasonable cost are among those dropped (C-6, − chain).

**C-9 and C-10: the 20-outlet threshold.**
- **Staying below (C-9).** For a chain with 19 outlets, the 20th outlet brings the whole compliance cost for all 20 outlets, about $110,000 in the record's example, on top of that outlet's own costs. That is a lumpy cost attached to the option "open a 20th outlet" (CR-4, units and lumpy costs). Chains for which it reverses the ranking of "open" over "stay at 19" stay at 19. A-9 is supported by arithmetic on the record's figures against typical outlet profit.
- **Second brands (C-10).** Some chains grow under a second name with a different menu, or rename franchised outlets, so that neither brand reaches 20 (RS-5). L1 counts outlets "under the same name with substantially the same menu". A second brand that keeps most of the menu would be challenged, which keeps A-10 at 0.55.

**Checked and not reported.**
- **RS-4 (relocation).** Restaurants serve local buyers, and buyers have no reason to cross to Ambrine to avoid seeing a number.
- **RS-3 (evasion).** Missing counts are visible on every inspection and fined per item. Inaccurate counts are a different matter: the incentive is not to evade but to choose the cheapest "reasonable basis", which is the nutrient database (L2 allows it). That keeps compliance cost down and accuracy within the tolerance for most items (A-2).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `restaurants.exempt` | `quantity_traded` | ambiguous | medium | CR-9, CR-4 (+: buyers leaving chains; outlets not opened, C-9); CR-11c, CR-4 (−: buyers who value the counts move to chains); CR-12b | covered chains and exempt restaurants: `substitute`, close | A-3, A-9, A-12 |
| C-13 | `chains.near_threshold` | `asset_value` | decrease | short (from announcement) | CR-7c, CR-10c | | A-9 |
| C-14 | `chains.covered` (menus whose calories buyers underestimated) | `asset_value` | decrease | short (from announcement) | CR-7c, CR-10c, CR-11c | | A-3, A-4 |
| C-15 | `chains.covered` (other menus) | `asset_value` | ambiguous | short | CR-7c (−: compliance cost; +: demand from buyers who overestimated, or who value the counts); CR-12b | | A-3, A-12 |
| C-16 | `intermediaries` (food laboratories, nutrition consultants) | `quantity_traded` | increase | short | CR-9, CR-8b | analysis services `input_to` compliance | A-13 |
| C-17 | `intermediaries` (menu-board printers) | `quantity_traded` (board replacements, December 2025 to June 2026) | increase | short | RS-8, CR-10a | boards `input_to` compliance | A-14 |
| C-18 | `intermediaries` (menu-board printers) | `quantity_traded` (board replacements, July 2026 to June 2027) | ambiguous | short | RS-8 (−: replacements pulled into the window); CR-4c (+: changed items need new boards); CR-12b | boards `input_to` compliance | A-14, A-6 |
| C-19 | `buyers.covered_chains`, `chains.covered` | `quantity_traded` (low-volume items dropped because of the per-item cost) | decrease | medium | OC-4, CR-5a, CR-4c | | A-6 |

**C-12: exempt restaurants, and why RS-16 gives no sign.** RS-16 needs a policy that moves buyers to a substitute. Here demand can move either way between covered chains and exempt restaurants.
- Toward exempt restaurants (+): buyers who learn that chain items are heavier than they believed, and buyers who would rather not see the numbers. Outlets that near-threshold chains do not open (C-9) also leave their custom to others.
- Toward chains (−): buyers who value the counts now have a reason to prefer a chain (A-12).

With the direction of the shift ambiguous, RS-16 gives no sign for exempt restaurants' prices, and none is recorded. The compliance cost does not decide it either. Most of it is fixed per item and per outlet, so it bears on which items and outlets a chain offers (CR-4c). It does not bear on the price of a meal at an existing outlet: under CR-3, a cost already incurred is not given up by any pricing choice. RS-14's precondition, a higher input price per unit of output, is not met. So no sign is recorded for prices at covered chains either.

**C-13 to C-15: firm values (CR-7c).**
- **Near-threshold chains (C-13).** Their option to grow past 19 outlets now carries the compliance cost, and their value falls from the time the Act became expected. Buyers of such chains after August 2025 pay the lower price.
- **Covered chains whose items buyers underestimated (C-14).** Both chains push down: compliance cost, and demand that falls once buyers learn the counts (C-3, given A-3 and A-4).
- **Other covered chains (C-15).** Compliance cost pushes down, while buyers who overestimated their items, or who value the counts, push up. The sign is ambiguous.

**C-16 to C-18: suppliers of compliance.**
- **Laboratories and consultants (C-16).** They receive what chains spend on analysis (CR-8b). The resources are used up for the chains (CR-8c), and they are income to the laboratories.
- **Printers (C-17, C-18).** Boards are replaced every three to five years in any case. The Act pulls every covered outlet's replacement into the months before 1 July 2026, so replacements in that window increase (C-17). In the following year two chains oppose each other, so the result is ambiguous (C-18):
  - replacements that would have happened then were already made (−);
  - each item added or changed now needs a board change with a count (+).

**Not reported (below cut-off).**
- **Inference from silence.** Once chains post counts, buyers may read an exempt restaurant's silence as a sign that its food is heavy, and some exempt restaurants post voluntarily to avoid that. A-16 (p = 0.4) is below the cut-off. CR-11c does not say how inference from what is not posted should be treated (Gaps found, b).
- **Grocery counters.** Buyers who dislike seeing counts shift to grocery prepared-food counters (A-18, p = 0.35).

**Stopping points.**
- Suppliers of ingredients for reformulated items (from C-5) are at depth 3 and diffuse; stopped.
- The labor of laboratories and printers (from C-16, C-17) is at depth 3; stopped.
- RS-9 (bundled trips), RS-10 (informal trade) and RS-11 (lock-in) do not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `buyers.covered_chains`, `quantity_demanded` (higher-calorie items), short to medium | Buyers who learn that items are lighter than they thought, or who seek more food per dollar (CR-11c, CR-4b). | Buyers who learn that items are heavier than they thought and prefer fewer calories (CR-11c, CR-4b). | Empirical premise, CR-12e: A-4 (p = 0.6). | **decrease** (C-3). If A-4 failed, **ambiguous**; if A-3 failed, no change, and the consequence is not reported. |
| `chains.covered`, `variety` (standard items), medium | New lower-calorie items to serve the demand in C-4 (A-4). | Low-volume items dropped because of the per-item cost (CR-4c; A-6). | None | **ambiguous** (C-6). |
| `chains.covered`, `variety` (limited-time items), medium | U1-b: new items introduced as exempt limited-time offers (RS-5; A-7). | U1-a: each seasonal item must be analyzed first (CR-4c; A-6). | Readings, not chains: one sign per reading. | **U1-a: decrease; U1-b: increase** (C-7). |
| `restaurants.exempt`, `quantity_traded`, medium | Buyers leaving chains after learning counts (A-3); outlets not opened by near-threshold chains (C-9; A-9). | Buyers who value counts prefer chains (A-12). | None | **ambiguous** (C-12). |
| `chains.covered` (menus buyers underestimated), `asset_value`, short | None. | Compliance cost (C-2); lower demand (C-3; A-3, A-4). | None needed | **decrease** (C-14). |
| `chains.covered` (other menus), `asset_value`, short | Demand from buyers who overestimated, or who value counts (A-3, A-12). | Compliance cost (C-2). | None | **ambiguous** (C-15). |
| `intermediaries` (printers), `quantity_traded`, July 2026 to June 2027 | Board changes for each changed item (A-6). | Replacements already pulled into the window (A-14). | None | **ambiguous** (C-18). |
| `chains.covered`, `price_paid` (meals), medium | — | — | Not reported. Fixed costs do not bear on the price of a meal at an existing outlet (CR-3), and the demand chain is ambiguous. | No consequence. |

## 8. Time structure

- **Announcement, March to August 2025.** Near-threshold chains reconsider their 20th outlet, and their values fall as passage becomes likely (C-9, C-13; CR-7c). Covered chains' values fall where their menus are heavy (C-14). Lobbying over the threshold, the tolerance and U1 begins (C-11).
- **Window, December 2025 to June 2026.** Analysis and new boards are bought (C-16, C-17), and portions are standardized (C-8). Chains drop items that are not worth analyzing (C-6, C-19), and they may hold back new standard items until U1 is settled. This window is signed (C-17) because board replacement also happens without the Act, at other times.
- **Short run, from July 2026.** Counts appear (C-1), and buyers who learn something change some choices (C-3, C-4). Because ordering at a familiar restaurant is a routine, the change may grow over months as buyers notice the counts (TS-8). Inspections begin (C-20).
- **Medium run.** Reformulated items appear as recipes are tested (C-5). Menu variety settles (C-6, C-7). Near-threshold chains stay at 19 or grow under a second brand (C-9, C-10). Whether exempt restaurants gain or lose custom shows here (C-12).
- **Fixed threshold.** The threshold is fixed at 20 outlets and does not erode with prices (TS-3 does not apply). The compliance cost per outlet falls as a chain grows, so the threshold's effect is concentrated on chains near it.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-20 | `officials.enforcement` (county health departments) | `enforcement_cost` (calorie checks) | increase | Inspector time spent on counts and records. | OC-3 |
| C-21 | `officials.enforcement` (county health departments, other inspection work) | `enforcement_cost` (other rules) | decrease | Other inspection work displaced, since county budgets are not raised. The cost falls on those that work protected. | OC-3, CR-8a |
| C-22 | `taxpayers` | `resources_available_other_uses` | decrease | What the $400,000 for laboratory tests would otherwise have funded. | OC-1, OC-3 |
| C-23 | `chains.covered` (those fined) | `resources_available_other_uses` | decrease | Fines paid; an unavoidable sum once imposed. | CR-8b |
| C-24 | `counties` | `tax_revenue` (fine revenue to general funds) | increase | The receipt side of C-23. | CR-8b |

C-2's compliance spending is the main resource used up (CR-8c). Its receipt side is C-16 and C-17, not a gain to the economy, since the analysts' and printers' time could have served other ends (OC-1). The items no longer offered are C-19. Buyers' time spent reading counts is not recorded: reading is chosen, not imposed, and nothing in the record suggests it is costly.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most covered chains do not now post counts on boards, and most of their buyers do not look counts up before ordering. | binding | 0.8 | 25% post on boards; website traffic to nutrition pages against meals sold. | C-1 and everything that follows from it fail. |
| A-2 | Posted counts are within the tolerance for most items. | enforcement | 0.7 | Database methods; error rates in audits of voluntarily posted counts. | C-1 weakens; counts carry less information. |
| A-3 | Some buyers' beliefs about calorie content differ from the posted counts. | other | 0.75 | Surveys of estimated against actual calories for chain meals. | No change in choices; C-3, C-4, C-5, C-14 fail. |
| A-4 | Among buyers whose choices change, more move away from higher-calorie items than toward them (dominance premise, CR-12e). | other | 0.6 | Direction of estimation errors (larger items underestimated more); stated preferences; sales mix at chains that posted voluntarily. | C-3 and C-4 become ambiguous; C-5 and C-14 fail. |
| A-5 | For some items, a lighter version costs less than the sales it would keep. | other | 0.6 | Recipe-development costs; reformulation at chains that posted voluntarily. | C-5 fails. |
| A-6 | The per-item fixed cost is material relative to the contribution of a chain's lowest-volume items. | other | 0.65 | The record's costs ($60 to $600 per item, plus board changes) against sales of the bottom tenth of items. | C-19 fails; the − chain of C-6 and the U1-a sign of C-7 fail. |
| A-7 | Under U1-b, chains can present new items as limited-time offers at low cost. | other | 0.6 | Current share of limited-time items in launches; marketing practice. | The U1-b sign of C-7 fails. |
| A-8 | Chains expect some accuracy checks, or a cost to reputation from wrong counts. | enforcement | 0.6 | Laboratory budget ($400,000 in year one); press coverage of audits elsewhere. | C-8 fails. |
| A-9 | For some near-threshold chains, the compliance cost reverses the ranking of opening a 20th outlet. | other | 0.65 | Record's cost example (about $110,000) against typical outlet profit; growth plans of the 9 chains with 17 to 19 outlets. | C-9 and C-13 fail; one chain of C-12 fails. |
| A-10 | For some small chains, a second brand costs less than compliance. | other | 0.55 | Branding and menu-development costs; the "substantially the same menu" test. | C-10 fails. |
| A-11 | Chains' associations and independent restaurants' associations can organize at a cost below their stake. | other | 0.75 | Existing state restaurant association; hearing testimony. | C-11 fails. |
| A-12 | Some buyers value the counts enough to prefer a covered chain over an exempt restaurant. | other | 0.6 | Surveys of buyers' use of counts; chains' reasons for posting voluntarily. | The − chain of C-12 and the + chain of C-15 fail. |
| A-13 | Many chains buy analysis from outside laboratories or consultants. | other | 0.8 | Industry practice; hearing testimony. | C-16 fails. |
| A-14 | Boards are replaced every few years without the Act. | durability | 0.8 | Industry replacement cycles. | C-17 is a rise with no matching dip; C-18 becomes an increase. |
| A-15 | County inspection budgets are not raised for the new task. | revenue_use | 0.65 | No appropriation in the Act; county budget calendars. | C-21 becomes a cost to county taxpayers instead. |
| A-16 | Exempt restaurants post counts voluntarily because buyers read silence as a bad sign. | other | 0.4 | Voluntary posting by independents where chains post. | Below cut-off; not reported. |
| A-17 | Some inaccurate counts are detected and fined. | enforcement | 0.55 | Laboratory budget; inspection frequency. | C-23 and C-24 fail. |
| A-18 | Buyers who dislike seeing counts shift to grocery prepared-food counters. | substitutability | 0.35 | No evidence beyond anecdote. | Below cut-off; not reported. |

### Final check before the report

The eight checks in `03_workflow.md` were run on the list.

1. **Uncombined chains.** Every key reached by two chains is combined in section 7:
   - demand for heavier items;
   - variety;
   - exempt restaurants' trade;
   - chains' values;
   - printers' second year.

   Prices at chains and at exempt restaurants were checked and are not reported, for the reasons given in section 6.
2. **Single signs for a group.** No group is claimed. RS-14's "price and/or quantity" was considered for chains and rejected, because its precondition is not met.
3. **Baseline.** Every sign is against Sallow without the Act, in which 25% of covered chains post on boards voluntarily. It is not against Ambrine, and not against a world with no posting at all.
4. **Worse off is not poorer.** `resources_available_other_uses` is signed only for taxpayers (C-22) and for fined chains (C-23), who pay sums they cannot avoid. It is not signed for buyers or for chains in general.
5. **Timing.** Board replacement happens with and without the Act, so both windows are signed (C-17, C-18). Holding back new items until U1 is settled is a path note.
6. **Both sides of transfers.** The laboratory fund is recorded on both sides (C-22; the laboratories in C-16), and so are the fines (C-23, C-24). Compliance spending is recorded on both sides (C-2; C-16, C-17).
7. **Every actor class, every core rule.**
   - CR-7c was applied to near-threshold chains and to covered chains.
   - CR-9 was applied to exempt restaurants, grocery counters and suppliers.
   - CR-6 does not apply, since no price or quantity is fixed.
   - OC-3 was applied to the counties and the state.
   - CR-11c is the main channel.
8. **Unstated premises.**
   - What buyers did not know is A-3, and which way they move is A-4.
   - "Some actors are at the margin" is A-6, A-9 and A-10.
   - The ability to organize is A-11.

## 11. Report

**The policy.** From 1 July 2026, restaurant chains with 20 or more outlets in Sallow must show the calorie count of each standard item on menus and menu boards. Counts must have a documented basis and be within 20% of actual content. Fines apply for missing or inaccurate counts, checked by county inspectors during routine inspections. Smaller chains and independent restaurants are exempt. So are daily specials and items offered "for a limited time", a phrase the law does not define (U1).

**Visible consequences.** Buyers at covered chains can see calorie counts when they order (C-1). Chains spend on analyzing items, replacing boards and keeping records (C-2).

**Invisible consequences.**
- *Buyers at covered chains.* Fewer higher-calorie items and more lower-calorie items are ordered (C-3, C-4). This holds given that some buyers misjudged calories (A-3), and that more of those who change move toward lighter items than away from them (A-4). Some low-volume items are no longer offered at all (C-19).
- *Covered chains.*
  - They offer lighter versions of some items (C-5).
  - They standardize portions to stay within the tolerance (C-8).
  - Their offering of seasonal items depends on how "limited time" is read (C-7). Under the narrow reading there are fewer seasonal items, because each must be analyzed first. Under the broad reading new items come out as limited-time offers to avoid analysis.
  - Chains whose menus buyers underestimated lost value when the law became likely (C-14).
  - Chains and independents lobby over the threshold and the exemptions (C-11).
- *Chains near the threshold.* Some stop at 19 outlets (C-9) or grow under a second brand (C-10), and their values fell when the Act became expected (C-13).
- *Suppliers.* Laboratories and consultants sell more analysis (C-16). Printers replaced boards in the months before the effective date (C-17).
- *Public side.*
  - County health departments spend inspection time on counts (C-20). Since their budgets are not raised, other inspection work falls (C-21).
  - Taxpayers fund laboratory tests (C-22).
  - Fines move money from chains to counties (C-23, C-24).

**Ambiguous effects.**
- The number of standard menu items (C-6): items dropped because of the per-item cost, against new lighter items.
- Whether independent restaurants gain or lose custom (C-12): buyers who leave chains, against buyers who prefer chains because they post counts.
- The value of covered chains whose items buyers did not underestimate (C-15).
- Printers' work in the year after the effective date (C-18).
- Meal prices at chains and at independents are not signed. The compliance cost is mostly fixed per item and per outlet, so it bears on what is offered, not on the price of each meal.

**Key conditions.**
- Every change in buyers' choices rests on buyers having misjudged calories (A-3, p = 0.75). Its direction rests on more of them moving toward lighter items (A-4, p = 0.6).
- The variety and threshold effects rest on the per-item and per-chain costs being material at the margin (A-6, p = 0.65; A-9, p = 0.65).
- How "limited time" is read decides the sign for seasonal items.

**What this analysis cannot say.**
- Anything about health, nutrient intake, calories eaten over a day, or body weight. These are out of scope for version 1, and not analyzed.
- How many buyers change what they order, or by how much.
- Whether the information is worth its cost to chains, inspectors and taxpayers, or whether the Act is desirable.
- Which reading of "limited time" will prevail.
- Whether independent restaurants will begin posting counts voluntarily (A-16, below the cut-off).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.covered_chains | quality_information (calorie content at point of sale) | increase | short | visible | B | CR-11c, CR-2, CR-1 | A-1, A-2 |
| C-2 | chains.covered | compliance_cost | increase | short | visible | A | OC-2, CR-8c | none |
| C-3 | buyers.covered_chains | quantity_demanded (higher-calorie items) | decrease | short–medium | invisible | B | CR-11c, CR-4b; CR-12b, CR-12e | A-1, A-2, A-3, A-4 |
| C-4 | buyers.covered_chains | quantity_demanded (lower-calorie items) | increase | short–medium | invisible | B | CR-11c, CR-4b; CR-12b, CR-12e | A-1, A-2, A-3, A-4 |
| C-5 | chains.covered | quantity_supplied (reduced-calorie versions) | increase | medium | invisible | B | CR-9, CR-4 | A-3, A-4, A-5 |
| C-6 | chains.covered | variety (standard items) | ambiguous | medium | invisible | B | CR-4c (−); CR-9, CR-4 (+); CR-12b | A-4, A-6 |
| C-7 | chains.covered | variety (limited-time items) | U1-a: decrease; U1-b: increase | medium | invisible | B | U1-a: CR-4c, CR-3; U1-b: RS-5 | U1-a: A-6; U1-b: A-7 |
| C-8 | chains.covered | quality_variability (portions) | decrease | medium | invisible | B | CR-4 | A-8 |
| C-9 | chains.near_threshold | investment_target (20th and later outlets) | decrease | medium | invisible | B | CR-4b, CR-4 (lumpy costs) | A-9 |
| C-10 | chains.near_threshold, small chains.covered | reclassification (second brands) | increase | medium | invisible | B | RS-5 | A-10 |
| C-11 | chains.covered, restaurants.exempt | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-11 |
| C-12 | restaurants.exempt | quantity_traded | ambiguous | medium | invisible | B | CR-9, CR-4, CR-11c; CR-12b | A-3, A-9, A-12 |
| C-13 | chains.near_threshold | asset_value | decrease | short | invisible | B | CR-7c, CR-10c | A-9 |
| C-14 | chains.covered (menus underestimated) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, CR-11c | A-3, A-4 |
| C-15 | chains.covered (other menus) | asset_value | ambiguous | short | invisible | B | CR-7c; CR-12b | A-3, A-12 |
| C-16 | intermediaries (laboratories, consultants) | quantity_traded | increase | short | invisible | B | CR-9, CR-8b | A-13 |
| C-17 | intermediaries (printers) | quantity_traded (December 2025–June 2026) | increase | short | invisible | B | RS-8, CR-10a | A-14 |
| C-18 | intermediaries (printers) | quantity_traded (July 2026–June 2027) | ambiguous | short | invisible | B | RS-8 (−), CR-4c (+); CR-12b | A-14, A-6 |
| C-19 | buyers.covered_chains, chains.covered | quantity_traded (dropped low-volume items) | decrease | medium | invisible | B | OC-4, CR-5a, CR-4c | A-6 |
| C-20 | officials.enforcement | enforcement_cost (calorie checks) | increase | short | invisible | A | OC-3 | none |
| C-21 | officials.enforcement | enforcement_cost (other inspection work) | decrease | short–medium | invisible | B | OC-3, CR-8a | A-15 |
| C-22 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-1, OC-3 | none |
| C-23 | chains.covered (fined) | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b | A-17 |
| C-24 | counties | tax_revenue (fines) | increase | short–medium | invisible | B | CR-8b | A-17 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 and the patterns cited. The steps that needed the most care, buyers' response to information (CR-11c with CR-2 and CR-12e) and the threshold (CR-4's lumpy costs), are derivable but need explicit premises.

**(b) Unclear core rules (wording that was hard to apply here).**
- **CR-11c and the premises a sign needs.** CR-11c says a policy changes actions by conveying information "and only to that extent". It does not say what a derivation must state to get a sign. This case needed two separate premises:
  - what buyers believed before, and how it differed from what they now learn (A-3);
  - which way those who learn something move, which depends on their ends, which the rules never assume (A-4, a dominance premise over buyers with different ends).

  Proposed addition to CR-11: "a change in choice from information needs (i) a premise that some actors' beliefs differed from the information, and (ii) for a sign, a premise on the direction of their errors and ends; without (ii), the effect on choices is `ambiguous`."
- **CR-11c and inference from silence.** When some sellers must disclose and others are exempt, buyers may draw conclusions from the exempt sellers' silence, and those sellers may then disclose voluntarily (A-16). CR-11c covers information the policy conveys. It is unclear whether information conveyed by the absence of a disclosure the policy makes salient counts as conveyed "by the policy".
- **CR-1 and information that changes how an option is enjoyed.** Some buyers may enjoy a dessert less once they see its count. CR-1 says a policy does not change rankings "except through what it tells them about the world". It is unclear whether a change in the satisfaction an option brings, caused by knowing a fact about it, counts as information about the world (allowed) or a change in ranking (excluded). No consequence was reported on it.
- **CR-3 and CR-4 on fixed costs and price.** The case needed the step that a cost fixed per item or per outlet bears on whether to offer the item or open the outlet (CR-4, lumpy costs) but not on the price of each unit sold (CR-3: a cost already incurred is not given up by a pricing choice). Both rules support it, but neither says it. RS-14 is stated for input prices and does not mark the difference. A sentence under CR-4's "Units and lumpy costs" would prevent misapplying RS-14 to fixed compliance costs.

**(c) Missing patterns (derived moves likely to recur).**
- **Proposed pattern, a mandated disclosure.**
  - **If:** a policy requires sellers to show buyers a fact about the good before purchase.
  - **Then:**
    - `quality_information` increases for buyers of covered sellers who did not already have the fact (CR-11c).
    - Choices change only for buyers whose beliefs differed (premise). Their direction needs a premise on the errors and ends, or a dominance premise; without one, `quantity_demanded` of the affected items is `ambiguous`.
    - Sellers adjust the disclosed attribute where demand shifts (CR-9, CR-4).
    - Demand between covered and exempt sellers moves both ways: toward covered sellers for buyers who value the fact, and away for those who learn something unwelcome. It is `ambiguous` unless a premise says which dominates.
  - **Derivation:** CR-11c, CR-2, CR-4, CR-9, CR-12b, CR-12e. It recurs in nutrition labels, energy ratings, fee disclosures and safety ratings.
- **Proposed pattern, a size threshold.**
  - **If:** a burden applies only to actors at or above a size threshold (outlets, employees, revenue), and part of the burden is fixed per actor.
  - **Then:**
    - actors just below it grow less: `investment_target` decrease;
    - some reshape so as not to cross it, by splitting, a second brand or contracting out: `reclassification` increase (RS-5);
    - the value of a growth option for actors near the threshold falls: `asset_value` decrease (CR-7c).
    - The effect is concentrated near the threshold, because the per-unit burden falls with size above it.
  - **Derivation:** CR-4 (lumpy costs: x is crossing, y is staying below), RS-5, CR-7c, CR-10c. It recurs in employee-count thresholds in labor law, revenue thresholds for taxes, and unit-count thresholds in rent rules.
- **Proposed pattern, a fixed cost per variant.**
  - **If:** a policy attaches a fixed cost to each version of a good offered: analysis, certification, a label.
  - **Then:**
    - `variety` decreases among the lowest-volume versions (CR-4c, with the item as the unit);
    - versions are introduced in whichever form the definitions exempt (RS-5);
    - sellers with more volume per version bear less per unit sold, which shifts competition toward them (CR-7).
  - **Derivation:** CR-4c, CR-3, RS-5, CR-7. It is the per-variant counterpart of PC-14, where the cost is fixed per transaction.
- **Note on RS-5 and reformulation.** RS-5 does not cover demand-driven reformulation. A lower calorie count does not move an item out of coverage. Reformulation is derived from CR-9 and CR-4. The note is recorded so that later analysts do not cite RS-5 for it.

**(d) Vocabulary.**
- **No instrument type for a disclosure or labeling mandate.** The list in 2.3 has no type for a requirement to convey information to buyers. Proposed: `disclosure_requirement`, with rule family to be set, and with CR-11c as its main channel.
- **No variable for a product's composition or attribute** (calories per item, energy use, fee level). Reformulation was recorded as the `quantity_supplied` of a named variant (C-5). Proposed: `attribute_level`, with a named attribute.
- **`quality_information` is defined in terms of quality.** Calorie content is an attribute that buyers rank differently, not a quality all prefer more of. Either widen the definition ("how easily buyers can learn a seller's quality or a named attribute before buying") or add `attribute_information`.
- **No variable for fines.** Fine revenue was recorded as `tax_revenue` (C-24). Proposed: widen `tax_revenue` to "revenue collected, including fines and fees", or add `fine_revenue`.
- **Group signs whose members move in opposite directions** (RS-14's "price up and/or quantity down"). These cannot be recorded; see WE-034, Gaps found (b) and (d).
