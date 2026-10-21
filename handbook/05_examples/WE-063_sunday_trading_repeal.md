# WE-063 Repeal of a ban on Sunday opening for large shops, with a right to refuse Sunday work

Analyst: draft (Handbook 1.0 held-out test, corrected under 1.1)  |  Rule catalog version: 1.1  |  Status: awaiting expert review

A stylized, fictional repeal in a fictional state. Several real jurisdictions have restricted Sunday opening by shop size and later relaxed the rule; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a case none of the 1.0 changes were drawn from (they came from WE-046 to WE-055). No worked example of the original ban exists, so, as the workflow's 0.9 note on repeals asks, the ban's own effects are derived first from the core rules (section 2) and the repeal is checked against them (section 7, metamorphic check). The case probes RS-9 on location complements and bundled trips (shops and cafés around large stores, small shops' neighbors, trips across the state line), RS-8 on sales moved between days of the week and on hiring in the six-month window, CR-7's 1.0 clause on which stock an asset's value follows (small shops lose a Sunday advantage they held only because larger rivals were shut), RS-17 in reverse (the 280 m² line, with shops bunched just below it), PC-17 on the mandated right to refuse Sunday work and its baseline, RS-7's and CR-4's 1.0 clauses on lobbying where the question was contested on the counterfactual path, and CR-12's 1.0 clauses on the baseline of patterns. The unclear provision is whether the right to refuse covers workers hired after the repeal takes effect. The counterfactual throughout is **the ban stays in force**; every sign is relative to that path. `persistence` compares each consequence with the path on which the ban was never imposed (TS-6). Effects on family life, religious observance and health are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite. After its core-only re-run (`05_examples_core/WE-063_sunday_trading_repeal_core.md`) it was corrected under catalog 1.1; the changes are listed just before "Gaps found".

## 1. Policy record

**Hastrow Shop Opening (Sunday Trading) Act 2027.** Hastrow is a state of about 4.3 million people. Since the Shop Hours Act 1961, section 9 has provided: "A shop with a sales area of more than 280 square metres shall not be open for the serving of customers on Sunday." Sales area is the floor area to which customers have access. Shops of 280 m² or less may open on Sunday at any hours. The figures:

| Item | Figure |
|---|---|
| Shops | about 24,000 |
| Shops over 280 m² | about 1,600: 640 supermarkets, 190 DIY and garden, 260 furniture and electrical, 510 department, clothing and other; about 112,000 employees |
| Shops of 280 m² or less | about 22,400; about 10,500 open on Sunday, where Sunday is about 16% of their weekly sales (about 20% for convenience stores) |
| Chain-owned convenience formats | about 1,250 stores run by the three supermarket chains, fitted at 250 to 280 m² |
| Shops near the line | about 1,050 between 250 and 280 m²; about 260 between 280 and 310 m² |
| Shop workers | about 205,000; about 58,000 in small shops, of whom about 31,000 work some Sundays. Most small-shop contracts require Sunday work "as rostered". |
| Pay | The retail pay agreement, renegotiated each April, pays Sunday hours at time-and-a-half in shops that open on Sunday; it applies on both paths. |
| Rents | Town-centre units of 280 m² or less rent for about 12% more per m² than comparable units of 300 to 400 m²; letting agents attribute the gap to Sunday trading. |
| Corsland | The neighboring state allows Sunday opening for all shops. About 700,000 Hastrow residents live within 30 minutes of the line. The revenue department estimates that Hastrow residents spend about 380 million a year in Corsland shops on Sundays. |
| Online | About 11% of retail sales; about 18% of online orders by Hastrow residents are placed on Sundays. |
| Sales tax | 6% |
| Enforcement of the ban | Municipal trading standards officers; fines up to 50,000 per Sunday; about 30 prosecutions a year; about 1.2 million a year of officer time across the municipalities. Fines go to municipal budgets. |

The large retailers' association has campaigned for repeal since 2012. The small shops' federation, the shop workers' union and church groups opposed it. A repeal bill failed in 2024 by 61 votes to 64. The 2027 bill was introduced on 11 January 2027, passed the House on 9 April (68 to 57) and the Senate on 22 April (21 to 14), and was signed on 3 May 2027. The right to refuse Sunday work was added in committee as the price of the union's neutrality. The Act takes effect on 3 November 2027, six months after signing, and has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Repeal of the ban | Removal of a `prohibition` (of Sunday opening by shops over 280 m²) | Sunday opening of shops over 280 m² | — | Section 9 of the 1961 Act repealed from 3 November 2027. No other limit on Sunday hours. | — |
| K2 Right to refuse Sunday work | `mandated_contract_term` | Contracts of employment of shop workers, in shops of any size | Employers of shop workers | s. 6(1): a shop worker may give written notice objecting to Sunday work; from one month after the notice the employer may not require the worker to work on Sunday, nor dismiss or otherwise disadvantage the worker for refusing. s. 6(4): complaint to the Employment Tribunal; compensation up to 26 weeks' pay. s. 6(5): "This section applies to every contract of employment of a shop worker in force when this Act comes into force." | — |
| K3 Commencement | — | — | — | Six months after signing: 3 November 2027. | — |

Existing rules, unchanged on both paths: the retail pay agreement and its Sunday rate; working-time rules; zoning; the sales tax; Corsland's rules.

Unclear provisions:
- **U1, who has the right to refuse.** Section 6(5) applies section 6 to "every contract of employment of a shop worker in force when this Act comes into force". Reading U1-a: the phrase fixes when the section starts to apply, and it applies to every shop worker's contract in force at any time from then, including contracts made after 3 November 2027; the explanatory memorandum says the right is meant "to protect all shop workers". Reading U1-b: it applies only to contracts in force on 3 November 2027; workers hired after that date, including existing workers who change employer, have no statutory right to refuse. The Labour Department has issued no guidance, and no tribunal has ruled. Readings get no probability; where a sign depends on one, each reading's sign is reported.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Removal of a triangular intervention: the ban forbade exchanges between large shops and buyers on Sunday. CR-1: adds the option of opening on Sunday for large shops and of buying there for buyers (operation 2), dated 3 November 2027. Before that date it acts through expectations (CR-10a), while asset values move from the bill's introduction (CR-7c; CR-1, 0.7, dated operations). The counterfactual law keeps the ban. For small shops, K1 performs no operation: their options are unchanged. Their situation changes through what their rivals and customers now do (CR-9). | The ban binds: Corsland's large shops open on Sunday, and Hastrow residents travel there to shop (A-1, A-6). | CR-4, CR-5, CR-6, CR-7 (1.0), CR-8 (1.0), CR-9, CR-10, RS-1, RS-4, RS-6, RS-7, RS-8, RS-9, RS-16 (mirror), RS-17 (in reverse), TS-5, TS-6, TS-8, OC-3, OC-5, TX-10 |
| K2 | Triangular: a term each contract must allow (CR-1, operation 3 on the option of employing without it). It binds where Sunday work would be required on the counterfactual path: in small shops, which open on Sunday and require it. In large shops there is no Sunday work on the counterfactual path; there the right is a condition attached to the option K1 adds, and no burden against the counterfactual. Per reading: under U1-a, on all shop contracts; under U1-b, on contracts in force on 3 November 2027 only. | In small shops, for workers who object (A-8) | PC-17 (1.1), RS-20, RS-11, RS-8, CR-1, CR-3 (1.1), CR-5c, CR-7, CR-8 (0.7: voiding) |
| K3 | Dates K1 and K2 | — | RS-8, CR-10a |

### Effects of the ban itself (derived first)

No worked example of the 1961 ban exists. Its consequences against a Hastrow that never had it are derived here from the core rules, with the same figures (workflow, "Analyzing a repeal", 0.9 note). The ban is a prohibition, with a size line, on one day's trade by large shops. Section 7 compares each with the repeal. Each row carries the premises it needs, the mirror of the repeal's (an assumption ID marked "mirrored" means the same premise read for the ban against the path without it).

| ID | Actor class | Variable | Sign (ban against never imposed) | Derivation | Premises |
|---|---|---|---|---|---|
| B-1 | `large_shops` | `quantity_traded` (Sunday) | decrease (to none) | CR-1 (operation 1), CR-5a, OC-4 | A-1, A-2 mirrored |
| B-2 | `large_shops` | `quantity_traded` (Monday to Saturday) | increase | RS-8, CR-4 (purchases moved to other days) | A-5 mirrored |
| B-3 | `large_shops` | `quantity_traded` (weekly) | decrease | CR-9, CR-4 (Sunday buyers lost to small shops and Corsland; moved purchases cancel, CR-12 1.1) | A-3, A-6 mirrored |
| B-4 | `small_shops.standalone`; `small_shops.in_centres` | `quantity_traded` (Sunday) | increase; ambiguous | CR-9, RS-1 (large shops' Sunday buyers move to them); in centres, against the anchor's Sunday footfall lost (RS-9, location), CR-12b | A-3 mirrored; A-12 mirrored for the centres |
| B-5 | `small_shops` | `number_of_sellers` | increase | CR-4, CR-7a (entry while the Sunday advantage pays) | A-3, A-7 mirrored |
| B-6 | owners of `small_shops.standalone`; owners of `small_shops.in_centres`; owners of small units | `asset_value`; `asset_value`; values and rents of small units | increase; ambiguous; increase | CR-7c, CR-10c (captured by those holding in 1961, and since by holders as Sunday demand grew); in centres as B-4, CR-12b | A-3, A-23 mirrored; A-12 mirrored for the centres |
| B-7 | `buyers.border` | `cross_border_purchases` (Sunday) | increase | RS-4 | A-6 mirrored |
| B-8 | Corsland sellers and their trip goods | `quantity_supplied`, `net_price_received`, `quantity_traded` | at least one increase | RS-4, RS-9, CR-6 | A-6, A-12 mirrored |
| B-9 | Shops near 280 m² | `unit_size`; `number_of_sellers` just below the line | decrease; increase | RS-17 (a notch: the whole shop closes on Sunday above the line; 1.1 baseline), CR-4 | A-11 mirrored |
| B-10 | Chains | `reclassification` (formats fitted at 280 m² or less) | increase | RS-5, RS-17 | A-11 mirrored |
| B-11 | Shops just below the line | `asset_value` | ambiguous | RS-17 (0.9): rivals above the line shut on Sunday (+); growing past the line costs Sunday trade (−) | A-3, A-11 mirrored |
| B-12 | `large_shops.owners`, landlords of large units | `asset_value` | decrease | CR-7c; the class loses the Sunday trade it would draw from small shops and Corsland, which outweighs the cost of a seventh day that rivals' opening would force (dominance premise) | A-1, A-4, A-13 mirrored |
| B-13 | `shop_workers.large` | `hours_worked` (Sunday; Monday to Saturday); `employment`, `hours_worked` (weekly) | decrease (to none); increase; at least one decrease | CR-9 with LW-10 (labor follows sales by day); the weekly sign needs the minimum-crew premise mirrored (CR-12e) | A-1, A-10; A-9 mirrored for the week |
| B-14 | `shop_workers.small` | `employment`, `hours_worked` | at least one increase | CR-9, OC-5 | A-3, A-7 mirrored |
| B-15 | `sellers.complements` | `quantity_traded` (Sunday): around large stores; next to small shops | decrease; increase | RS-9 (trips and location) | A-12; A-21 mirrored |
| B-16 | `sellers.substitutes` (online) | `quantity_substitute` (Sunday orders) | increase | RS-1 | A-22 mirrored |
| B-17 | Municipalities | `enforcement_cost`; `non_tax_receipts` (fines); net of the two | increase; increase; ambiguous | OC-3, CR-8b, CR-8 (1.0: receipts into the same budget) | A-24 |
| B-18 | State budget | `tax_revenue` (sales tax) | decrease | TX-10 (purchases moved to Corsland) | A-6 mirrored |
| B-19 | Large retailers; small shops, the union | `lobbying_effort` | increase (contested) | RS-7, EN-5 | A-14 |
| B-20 | `large_shops` | `investment_target` (large stores; extensions past 280 m²) | decrease | CR-4, CR-10a, CR-10c | A-1, A-11 mirrored |
| B-21 | Corsland shops near the line | `asset_value` | increase | CR-7c, CR-10c | A-6 mirrored |
| B-22 | Buyers near small shops that exist only under the ban | `travel_time` | decrease | CR-9, CR-3b | A-3, A-7 mirrored |
| B-23 | `large_shops` that open in breach | `resources_available_other_uses` (fines paid) | decrease | CR-8b | A-24 |
| B-24 | `shop_workers.large` | `earnings` | decrease | CR-9, arithmetic: no Sunday hours at time-and-a-half, and fewer hours over the week | A-9, A-28 mirrored |
| B-25 | Small-shop owners who stay open | `resources_available_other_uses` | increase | CR-3 (lost receipts net of saved outlays), CR-12e | A-3, A-27 mirrored |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `large_shops` (`sellers.current`) | About 1,600 shops over 280 m² | May open on Sunday from 3 November 2027 |
| `large_shops.owners` | Owners of large retailers | Expected yields change |
| `small_shops.standalone` | Small shops in residential streets and villages, well below the line | Lose the Sunday trade of buyers who prefer large shops |
| `small_shops.in_centres` | Small shops in centres and retail parks anchored by large shops | Lose Sunday exclusivity; gain Sunday footfall from the anchor |
| `small_shops.near_line` | Shops fitted at 250 to 280 m², including the chains' convenience formats | Lose the Sunday advantage; may now grow past 280 m² |
| `shop_workers.large`, `shop_workers.small` | Employees of large and small shops | Sunday work in large shops; a right to refuse Sunday work (per U1) |
| `shop_workers` (job changers), job seekers | Workers moving between shops or entering retail | Whether a new contract is covered depends on U1 |
| `buyers` (`buyers.current`) | Hastrow households | May shop at large shops on Sunday |
| `buyers.border` | Residents within 30 minutes of Corsland | May shop at home on Sunday |
| `buyers.small_shop_dependent` | Buyers who relied on small shops that close | Travel farther (C-51) |
| `neighboring_jurisdictions` | Corsland's shops, cafés and fuel stations | Fewer Hastrow Sunday shoppers |
| `sellers.complements` | Cafés, restaurants and fuel stations around large stores; bakeries and newsagents next to small shops | Sunday trips move |
| `sellers.substitutes` | Online sellers | Fewer Sunday orders placed because shops were shut |
| `landlords.small_units`, `landlords.large_units` (`factor_owners.specific`) | Owners of retail premises | The small-unit premium ends; large units are worth more |
| `officials.enforcement` | Municipal trading standards; the Employment Tribunal | Ban enforcement ends; complaints under s. 6 begin |
| Lobbies: large retailers' association; small shops' federation and union | Organized interests on the ban | Lobbied on both paths; new questions under the Act |
| State budget, municipal budgets | Sales tax; fines; officer time | Receipts and outlays change; the municipal net (C-42) |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `large_shops`, `buyers` | `quantity_traded` (Sunday sales at shops over 280 m²) | increase | short (from 3 November 2027) | CR-1, CR-4, CR-5, CR-12 (0.9: activity against none) | A-1, A-2 |
| C-2 | `buyers` (who prefer to shop at large shops on Sunday) | `full_cost_per_unit` (time given up to buy at large shops) | decrease | short–medium | CR-1, CR-3b, CR-4 | A-2 |
| C-3 | `small_shops.standalone` | `quantity_traded` (Sunday sales) | decrease | short–medium | CR-9, RS-16 (mirror case), CR-4 | A-3 |
| C-4 | owners of `small_shops.standalone` | `asset_value` (shop as a going concern) | decrease | short (part from January 2027, most at signing) | CR-7c, CR-10c, CR-7 (1.0: which stock), CR-8 (1.0: statutory rights) | A-3, A-4 |

**C-1, C-2.** From 3 November 2027 large shops that expect Sunday opening to pay open (CR-4, x: stay shut, y: open; A-1). On the counterfactual path they sell nothing on Sunday, so their Sunday sales rise from none (CR-12, 0.9). Buyers who rank a Sunday trip to a large shop above what they would otherwise have done gain an option (CR-3b) and take it (A-2). Their full cost of obtaining goods, counting the weekday or Saturday time it took on the counterfactual path, falls (C-2).

**C-3, C-4: what small shops lose, and when.** Small shops' options do not change; their Sunday buyers' options do. Buyers who used a small shop on Sunday only because the supermarket was shut move to it (CR-9; RS-16's mirror case: a good made more available pulls buyers from its substitutes; A-3).

The value of a small shop included the expected yield of Sunday trade protected by its rivals' closure. When the repeal becomes expected, that part of the value falls (CR-7c, CR-10c), part of the way from the bill's introduction in January and most at signing, given the failed 2024 vote (CR-7c's probability clause; A-4).

CR-7's 1.0 clause on which stock: the advantage depended on a legal rule, not on a stock that grows slowly. The rivals' capacity, 1,600 large shops, already exists and needs only staff to open on Sunday, so the advantage ends on the effective date with no transition rent of the kind existing stores kept in WE-052. The small shops' capital (premises, fittings, the 1,250 chain formats fitted under 280 m²) persists. Its value now reflects only its use without the advantage (section 7).

CR-8's 1.0 clause on statutory rights says that the holder loses the right's value and that who gains depends on who now obtains what the right excluded. Here that is large shops (C-1) and buyers who switch (C-2). Much of their gain is new exchanges, not a transfer: purchases made at a large shop on Sunday that the ban prevented (CR-5). Small shops never held a right as such. Their advantage was a by-product of a prohibition on others, and Gaps found (b) 2 records the reading this needed. CR-3's 1.1 clarification now says that the note on lost receipts and saved outlays applies to every seller who loses sales, including to a better offer: what small shops lose in money is analyzed in section 9 (C-40), not as a voided right.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | `large_shops`, `buyers` | `quantity_traded` (Monday to Saturday sales at large shops) | decrease | short–medium | RS-8, CR-4 | A-5 |
| C-6 | `large_shops` | `quantity_traded` (weekly sales) | increase | short–medium | CR-12e (accounting identity), CR-12 (1.1: items that cancel), CR-9, RS-4, RS-16 (mirror) | A-3, A-6 |
| C-7 | `buyers.border` | `cross_border_purchases` (Sunday purchases in Corsland) | decrease | short–medium | RS-4 | A-6 |
| C-8 | `small_shops` | `number_of_sellers` | decrease | medium | RS-6, CR-4, CR-7a | A-3, A-7 |
| C-13 | shops that would be fitted at or near 280 m² | `unit_size` (sales area of new and refitted shops near the line) | increase | medium–long | RS-17 (in reverse; 1.0; 1.1 baseline), CR-1, CR-4, TS-6 | A-11 |
| C-14 | supermarket chains | `reclassification` (formats fitted to stay at or below 280 m²) | decrease | medium | RS-5 (in reverse), RS-17 (in reverse), CR-4 | A-11 |
| C-19 | large retailers' association | `lobbying_effort` (over Sunday opening) | ambiguous | medium | RS-7 (repeal clause; 1.0; 1.1), CR-4 (0.9, 1.0, 1.1), CR-12b | A-14, A-15 |
| C-20 | small shops' federation, shop workers' union | `lobbying_effort` (over Sunday opening) | ambiguous | medium | RS-7 (repeal clause; 1.0; 1.1), CR-4 (0.9, 1.0, 1.1), CR-12b | A-14, A-15 |
| C-21 | shop workers' union, large retailers' association | `lobbying_effort` (on U1 and the rules for s. 6) | increase | short–medium | RS-7, CR-4 (1.0, 1.1), CR-12 (0.9) | A-14 |
| C-22 | `large_shops` | `investment_target` (Sunday opening: rosters, systems, recruitment, May to November 2027) | increase | short (window) | RS-8, CR-10a, CR-12 (0.9) | A-1 |
| C-23 | `large_shops` | `employment` (hires, May to 2 November 2027) | U1-a: increase; U1-b: ambiguous | short (window) | RS-8 (0.9), CR-10a, CR-12b | A-1, A-16 |
| C-24 | `shop_workers` | `job_changes` (May to 2 November 2027) | U1-a: increase; U1-b: ambiguous | short (window) | RS-8 (0.9), CR-10a, CR-12b | A-16, A-17, A-19 |
| C-25 | `shop_workers` with contracts in force on 3 November 2027 | `job_changes` (after the effective date) | U1-a: increase; U1-b: ambiguous | medium | RS-11, CR-3, CR-4, CR-9, CR-12b | A-1, A-18, A-19 |
| C-26 | `shop_workers.small` | `wage_rate` (−), `non_wage_compensation` (other non-wage terms) (−), `employment`/`hours_worked` (−) | at_least_one_as_stated | medium | PC-17 (1.1), CR-1, CR-5c, CR-6, CR-7 (0.7: gross and net) | A-8 |
| C-27 | employers of shop workers | `legal_breach` (workers who object pressed or disadvantaged) | increase | short–medium | RS-20 (1.0: baseline), CR-4 | A-8, A-20 |
| C-43 | `shop_workers.small` (who object) | `term_prevalence` (contracts under which Sunday work can be required of a worker who objects) | decrease | short–medium | CR-1, CR-8 (0.7: voiding a contract right) | A-8 |
| C-44 | `shop_workers.small` (who object) | `non_wage_compensation` (freedom to refuse Sunday work: the item transferred) | increase | short–medium | CR-8 (0.7: voiding), CR-8b, CR-3b | A-8 |
| C-45 | `small_shops` (employers) | `compliance_cost` (re-rostering Sunday cover around objectors) | increase | short–medium | CR-1 (operation 1), CR-3a, CR-8c | A-8 |
| C-46 | `large_shops` | `investment_target` (new large stores; shops enlarged past 280 m²) | increase | medium–long | CR-4, CR-10a, CR-10c, TS-5, TS-1 | A-1, A-4, A-11 |
| C-47 | `large_shops` | `employment` (replacement hires, from 3 November 2027) | U1-a: no_change; U1-b: increase | short (from 3 November 2027) | RS-8, CR-1 (per reading), CR-10a | A-16 |
| C-48 | `shop_workers` who moved employer before 3 November 2027 | `job_changes` (from 3 November 2027) | U1-a: no_change; U1-b: decrease | short (from 3 November 2027) | RS-8, CR-1 (per reading), CR-10a | A-17 |

**Sales moved between days (C-5, C-6).** RS-8 applies: the repeal treats the same purchase differently by day. Some buyers who did their main shop at a large shop on Saturday or a weekday now do it on Sunday (A-5). The purchase happens on both paths, at different times, so it is signed per window (02_ontology, 2.5): Sunday at large shops up (C-1), Monday to Saturday down (C-5). Large shops' weekly sales are a separate key (C-6). Purchases moved within the week appear in both windows and add nothing to the week. Purchases drawn from small shops (A-3), from Corsland (A-6) and from online sellers (A-22) are additions. So the weekly total rises by an accounting identity (CR-12e), given at least one of those premises. CR-12's 1.1 clause on items that cancel confirms the form: the moved purchases cancel by construction, a third item (purchases drawn from elsewhere) remains, so the items and the total are recorded, and per-window signs may be summed into the weekly total.

**Corsland (C-7).** Border residents who crossed the line on Sundays because Hastrow's large shops were shut shop at home (RS-4 in reverse; A-6). Habits and ties to Corsland stores change gradually (TS-8).

**Small shops close (C-8).** Some small shops covered their costs only with their Sunday trade (A-7). With it reduced, they close or are not replaced when leases end (RS-6; CR-4, x: keep trading, y: close; CR-7a). The stock falls gradually (CR-10b).

**The 280 m² line in reverse (C-13 to C-15).** Under the ban the line was a notch: a shop one square metre over it lost all its Sunday trade (CR-1, 1.0; RS-17, 1.0: a burden above the line). RS-17's 1.1 baseline clause asks that each band be signed against no policy; here every sign is against the ban in force, the repeal's counterfactual. The case's figures show the bunching RS-17 predicts: about 1,050 shops at 250 to 280 m² against 260 at 280 to 310 m², and 1,250 chain formats fitted under the line (B-9, B-10). The repeal removes the notch. New and refitted shops that were held at or just under 280 m² can be fitted at the size that suits them (C-13; A-11), and chains stop designing formats to the line (C-14). Existing shops are not rebuilt for the repeal alone. The stock fitted under the line changes only as shops are refitted or replaced, so the ban's effect on unit size persists in part for years (TS-6). RS-17's 0.9 clause, in reverse, decides the value of near-line shops (C-15, section 7).

**Lobbying (C-19 to C-21).** RS-7's repeal clause and CR-4's 0.9 and 1.0 clauses apply. On the counterfactual path the ban was contested: twenty years of campaigning and a 61 to 64 vote in 2024 (A-15). After the repeal, large retailers defend it against efforts to restore the ban (+), in place of the campaign to end it (−). The small shops' federation and the union seek to restore the ban or win new limits (+), in place of defending the ban (−). Each class lobbied on both paths, and no premise ranks the two efforts: each is `ambiguous` (C-19, C-20). Questions that exist only under the Act are signed from none (CR-12, 0.9): the reading of s. 6(5), the Labour Department's guidance, and what counts as "disadvantage" (C-21; A-14). CR-4's 1.1 clause on "the same question" fits this split: the contested question on the counterfactual path is the policy field (Sunday opening), not the exact provision, and lobbying over provisions that exist only under the Act is an increase.

**Hiring and job changes in the window (C-22 to C-24).** Large shops prepare to open on 3 November: rosters, systems, and recruitment of Sunday staff (C-22; an activity that exists only under the repeal). U1 changes the timing of hiring.
- Under U1-a every contract is covered whenever made, so the date does not matter for coverage. Large shops hire ahead of opening (C-23, increase), some of them from small shops (A-19), so job changes rise in the window (C-24).
- Under U1-b a contract made on or after 3 November is not covered, and a contract in force on that date is. Employers gain from deferring hires they would have made in the window anyway on the counterfactual path (ordinary replacement hiring) until after the date, so that those contracts are not covered (A-16, −), against the hiring to prepare for opening (+). Hires in the window: `ambiguous` (C-23). Workers who plan to change employer gain from moving before the date, so that their new contract is covered (A-17, +). That chain meets the employers' deferral (−) and the preparation hiring (+), and job changes in the window are `ambiguous` (C-24). This is RS-8's 0.9 case of sellers and buyers, here employers and workers, moving in opposite directions in time. RS-8 asks for both sides of each move. Under U1-b, the replacement hires deferred out of the window are made after the date (C-47, increase), and workers who moved before the date to hold a covered contract do not make that move later (C-48, decrease). Under U1-a neither move is made, so both are `no_change`.

**Lock-in after the date (C-25).** Under U1-b, a worker whose contract was in force on 3 November loses the right on taking a new job. RS-11 applies: a non-transferable benefit lost by a change of status. Workers who value the right (A-18) turn down moves they would otherwise make (−). Large shops' added Sunday staffing draws some existing shop workers into new jobs (A-19, +). No premise ranks them: `ambiguous`. Under U1-a the right travels with every new contract, so there is no lock-in, and the hiring chain alone gives an increase.

**The right to refuse in small shops (C-26).** PC-17's If clause is "the term is absent from some contracts that would otherwise be made". On the counterfactual path, small shops require Sunday work. So in small shops the right binds for workers who object (A-8). It binds on existing contracts under both readings, and also on new contracts under U1-a. The employer's cost of covering Sunday rises: rosters, replacement staff, or shorter Sunday hours. The bargaining range moves (CR-5c), and the other terms adjust as PC-17's mixed group: `wage_rate` (−), `non_wage_compensation` (−), `employment`/`hours_worked` (−), sign `at_least_one_as_stated`. The right is worth something to workers who use it, so part of the cost is recovered through the other terms (CR-7, 0.7: gross and net). Whether those workers are better off by their own ranking depends on why the term was absent, which is a premise this case does not settle (CR-2, 0.7). PC-17's 1.1 clause says to compare with no term: for small shops that is the contract as it stands on the counterfactual path, with Sunday work "as rostered".

The right also does three things directly, recorded on their own. For each worker who gives notice, the employer can no longer require Sunday work under the "as rostered" clause (C-43; CR-1). Under existing contracts that is a voided contract right, a transfer under CR-8's 0.7 voiding note: the worker gains the value of being free to refuse (C-44, an item of `non_wage_compensation`), and the employer loses it, bearing the cost of re-rostering cover around objectors (C-45; CR-1 operation 1, CR-3a, CR-8c). C-44 and the `non_wage_compensation` member of C-26's group are items of one variable that may move in opposite directions. But C-26 is a group, and a member of a group cannot be used as a signed chain in another combination (CR-12, 1.1), so no total of `non_wage_compensation` is recorded.

**The right to refuse in large shops: PC-17's baseline.** PC-17 compares a contract with the term against the same contract without it. In large shops there is no Sunday work on the counterfactual path. The contracts that would carry the term (Sunday work in a large shop) would not otherwise be made at all, so PC-17's precondition is not met there. Applied as written, comparing Sunday opening with the right against Sunday opening without it, PC-17 would give large-shop workers lower pay or fewer hours. That compares with another policy, not with the ban in force (CR-12, 1.0, the baseline of patterns). Against the ban, the right only narrows the option K1 adds. It lowers what Sunday opening is worth to large shops (A-1 is stated with it) and makes Sunday work voluntary for those it covers. Large-shop workers covered by it gain an option they may refuse (CR-3b). Catalog 1.1 now says this: PC-17's 1.1 clause compares with no term, not with the same contract minus the term, and CR-3's 1.1 clarification says that a burden attached to an option that exists only under the policy is no loss against the counterfactual, which is not having the option at all. Gaps found (c) 1.

**Breach (C-27).** The right is enforced only on complaint to the tribunal. RS-20, in its 1.0 form, applies: against the counterfactual, where no right exists, breach rises from none wherever enforcement is less than certain. Under its main clause, the breach falls where complaint is least likely: short-tenure, part-time and young workers (A-20).

**Credibility (TS-5).** Retailers would hold back long-payback investment (new large stores, extensions past 280 m²) if they expected the ban to return within the payback period. With the 2027 margins and the failed 2024 attempt by the other side, A-25 (p = 0.25) is below the cut-off. Quick-payback responses (opening hours, rosters) go ahead whatever is expected. So long-payback investment in new large stores and in extensions past 280 m² rises (C-46; CR-4, x: a format at 280 m² or less, y: a larger one; CR-10a, CR-10c; A-1, A-4, A-11), at the speed of planning and building (TS-1).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-10 | `shop_workers.large` | `employment`, `hours_worked` (weekly) | at_least_one_increase | medium | OC-5, CR-9, LW-10, CR-12e | large-shop sales `input_to` labor demand | A-1, A-9 |
| C-11 | `shop_workers.large` | `hours_worked` (Sunday) | increase | short–medium | CR-9, LW-10, CR-12 (0.9) | as C-10 | A-1 |
| C-12 | `shop_workers.large` | `hours_worked` (Monday to Saturday) | decrease | short–medium | CR-9, LW-10, RS-8 | as C-10 | A-5, A-10 |
| C-9 | `shop_workers.small` | `employment`, `hours_worked` | at_least_one_decrease | medium | RS-6, OC-5, CR-9 | small-shop sales `input_to` labor demand | A-3, A-7 |
| C-15 | owners of `small_shops.near_line` | `asset_value` | ambiguous | short | RS-17 (0.9, in reverse), CR-7c, CR-12b | — | A-3, A-11 |
| C-16 | `small_shops.in_centres` | `quantity_traded` (Sunday sales) | ambiguous | short–medium | RS-9 (0.9: location complements), CR-9, CR-12b | anchor store and nearby shops: `complement` (location) | A-3, A-12 |
| C-17 | owners of `small_shops.in_centres` | `asset_value` | ambiguous | short | CR-7c, RS-9, CR-12b | as C-16 | A-3, A-12 |
| C-18 | `large_shops.owners` | `asset_value` | increase | short (part from January 2027, most at signing) | CR-7c, CR-10c, CR-2, CR-12e | — | A-1, A-4, A-13 |
| C-28 | `sellers.complements` (cafés, restaurants, fuel stations around large stores) | `quantity_traded` (Sunday sales) | increase | short–medium | RS-9 (trip; 0.9 location), CR-9 | shopping and cafés, meals, fuel: `complement` (trip) | A-1, A-12 |
| C-29 | `sellers.complements` (bakeries, newsagents next to standalone small shops) | `quantity_traded` (Sunday sales) | decrease | short–medium | RS-9, CR-9 | `complement` (trip) | A-3, A-21 |
| C-30 | `neighboring_jurisdictions` (Corsland shops) | `quantity_supplied`, `net_price_received` (Sunday sales to Hastrow residents) | at_least_one_decrease | short–medium | RS-4, CR-9, CR-6 (0.9: splitting a shift) | Hastrow and Corsland: `across_border`, partial | A-6 |
| C-31 | `neighboring_jurisdictions` (Corsland cafés and fuel stations) | `quantity_traded` (on Hastrow residents' Sunday shopping trips) | decrease | short–medium | RS-9, RS-4 | `complement` (trip) | A-6, A-12 |
| C-32 | `sellers.substitutes` (online sellers) | `quantity_substitute` (Sunday orders by Hastrow residents) | decrease | short–medium | RS-16 (mirror case), CR-9 | in-store and online purchases: `substitute`, partial | A-22 |
| C-33 | tenants and `landlords.small_units` | `price_paid` (rent per m² of units of 280 m² or less) | decrease | short–medium | CR-9, CR-6, CR-7c | units `input_to` small shops | A-3, A-23 |
| C-34 | `landlords.small_units` | `asset_value` (units of 280 m² or less) | decrease | short | CR-7c, CR-10c | as C-33 | A-3, A-4, A-23 |
| C-35 | `landlords.large_units` | `asset_value` (units over 280 m²) | increase | short | CR-7c, CR-10c, CR-9 | units `input_to` large shops | A-1, A-4, A-13 |
| C-41 | `buyers` | `quantity_traded` (total retail purchases in Hastrow, weekly) | increase | medium | RS-4, CR-4c | — | A-6 |
| C-49 | `shop_workers.large` | `earnings` (3 November 2027 to the April 2028 pay round) | increase | short | CR-9, LW-10, CR-12e (arithmetic with A-9) | as C-10 | A-1, A-9, A-28 |
| C-50 | `neighboring_jurisdictions` (Corsland shops near the line) | `asset_value` | decrease | short (part from January 2027, most at signing) | CR-7c, CR-10c, CR-9 | Hastrow and Corsland: `across_border`, partial | A-4, A-6 |
| C-51 | `buyers.small_shop_dependent` | `travel_time` | increase | medium | CR-9, CR-3a | buyers and the small shops that close (exchange) | A-3, A-7 |

**Labor in large shops (C-10 to C-12).** Two items of one variable move in opposite directions (CR-12, 0.8). Sunday hours rise from none (C-11). Monday to Saturday hours fall where staffing follows the sales moved to Sunday (C-12; A-5, A-10). The weekly total combines them. A-9 is the dominance premise (CR-12e, empirical): a store needs a minimum crew for each hour it is open, so the hours added on a seventh day exceed the hours saved on the six others, and the weekly sales gain (C-6) adds to it. So C-10 is an increase, as a group of staff and hours (OC-5: an existing activity). The tier stays B (CR-12, 1.0: a dominance premise settles a sign, it does not raise a tier). Under U1-a, Sunday shifts are staffed by volunteers. Under U1-b they can also be staffed by new hires whose contracts require Sunday work. The sign is the same under both readings.

**Large-shop workers' earnings (C-49).** Earnings are derived directly, not from C-10's group (CR-12, 1.1). The added Sunday hours are paid at time-and-a-half under the pay agreement, which applies on both paths; the weekday hours lost are paid at the base rate; total hours rise by the minimum-crew premise (A-9); and the agreement fixes rates until its April renegotiation (A-28). So earnings rise until the April 2028 pay round (arithmetic, CR-12e). After it, the rates can move, and no sign is given without a premise on the renegotiation.

**Small-shop labor (C-9).** Lower Sunday sales and closures (C-3, C-8) reduce staff or hours (RS-6, OC-5). The right to refuse is not used as a chain here: its effect on hours is a member of C-26's group, and a group member cannot be used as a signed chain in another combination (CR-12, 1.1).

**Location complements and trips (C-16, C-17, C-28, C-29, C-31).** RS-9 has no 1.0 clause; its 0.9 clause on location complements applies. Around a large store, Sunday shoppers also buy coffee, meals and fuel, and visit the small shops beside it (C-28; A-12). For small shops in centres anchored by a large store, two chains meet. The anchor's Sunday footfall brings buyers past them (+, RS-9 location complements). The anchor now competes with them for the Sunday trade they had to themselves (−, C-3's chain). No premise ranks them, so their Sunday sales (C-16) and their value (C-17) are `ambiguous`. Next to standalone small shops, the trips that leave carry their other purchases with them: the bakery or newsagent next to a corner shop loses Sunday trade (C-29; A-21). Across the line, the Sunday trips that stop take Corsland's café and fuel sales with them (C-31), and Corsland shops near the line, whose expected Sunday trade from Hastrow falls, lose value when the repeal becomes expected (C-50; CR-7c, CR-10c; A-4, A-6). RS-9's 0.9 clause also asks about new occupants of a location. None arises here: no premises change hands because of the repeal within the short run.

**Corsland (C-30).** Corsland's shops face fewer Hastrow buyers. How that divides between fewer sales and lower prices needs a premise on their supply (CR-6, 0.9), so the two are a group.

**Buyers of shops that close (C-51).** Buyers who bought at a small shop that closes (C-8) lose that option and fall back to a farther shop (CR-9, CR-3a; A-3, A-7). Their travel time rises.

**Online (C-32).** Some Sunday online orders were placed because the shops were shut (A-22). With large shops open, some of those buyers shop in person (RS-16's mirror case). Online prices are set across a national market; their sign is not recorded, because the chain moves quantity at prices set elsewhere and the case gives no premise on online sellers' supply.

**Premises (C-33 to C-35).** The 12% rent premium on small units capitalized the Sunday advantage (A-23). With the advantage gone and the stock of small units fixed in the short run (CR-6, 0.9: supply cannot contract at once), rents on new and renewed leases fall toward those of comparable larger units (C-33), and so do the units' values, from the bill's introduction (C-34; CR-7c). Large units gain a seventh trading day, and their values rise (C-35; A-13). Tenants on fixed leases pay the old rent until renewal (CR-6, 0.7: existing contracts).

**Large retailers' value (C-18).** Each large shop gains an option (CR-3b). But a class can be worse off when every member gains the same option: if every rival opens on Sunday, each may have to open to keep its customers, and sales spread over seven days at higher cost (CR-9). That is a chain the rules derive, and it needs a premise to be signed, so it is a kind (2) chain (CR-12, 0.8). A-13 is the dominance premise: the class campaigned for repeal for fifteen years (CR-2: demonstrated preference about what they expected), and the sales they draw from small shops, Corsland and online buyers are gains that rivals' opening does not take from the class as a whole (C-6). So C-18 is an increase, from January 2027 in part and at signing in most.

**Total purchases in Hastrow (C-41).** Two independent chains give an increase, so it holds if either holds (CR-12d). Purchases come back from Corsland (C-7; A-6). Purchases moved between days within Hastrow add nothing. Orders that move from online sellers to shops (C-32) are not used: whether they leave or enter Hastrow depends on where the online sellers are, which the record does not say, and the sign rests on the Corsland chain alone. Whether buyers buy more in total because shopping costs them less time (C-2) is not used: it would need a premise on their spending as a whole.

**Stopping points.** The staff of Corsland's shops (depth 3, across the line); suppliers and wholesalers to large shops, whose weekly deliveries follow C-6 (depth 3, diffuse); traffic and noise near large stores on Sundays (`proximity`, Tier C under GAP-026-1). Neighbors' rankings are not in the record, so no chain is drawn and none is reported.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `large_shops`, `quantity_traded` (weekly), short–medium | Sunday sales: moved purchases, plus purchases drawn from small shops, Corsland and online. | Monday to Saturday: moved purchases. | Accounting identity (CR-12e): moved purchases cancel; drawn purchases are additions (A-3, A-6). | **increase** (C-6). |
| `shop_workers.large`, `employment`/`hours_worked` (weekly), medium | Sunday staffing from none (C-11). | Fewer hours Monday to Saturday (C-12). | A-9, an empirical premise (minimum crew per open hour). | **at_least_one_increase** (C-10). |
| `large_shops.owners`, `asset_value`, short | New Sunday trade drawn from small shops, Corsland and online. | Rivals' opening forces costly opening (CR-9). | A-13, an empirical premise. | **increase** (C-18). |
| owners of `small_shops.near_line`, `asset_value`, short | Freedom to grow past 280 m² without losing Sunday trade (RS-17, in reverse). | Loss of Sunday trade to large shops (A-3). | None (RS-17, 0.9). | **ambiguous** (C-15). |
| `small_shops.in_centres`, Sunday `quantity_traded` and `asset_value` | Anchor's Sunday footfall (RS-9, location; A-12). | Anchor competes for Sunday buyers (A-3). | None. | **ambiguous** (C-16, C-17). |
| `large_shops`, hires in the window | Preparation for opening. | U1-b: replacement hiring deferred past the date (A-16). | U1-a: only the (+) chain. U1-b: none. | **U1-a: increase; U1-b: ambiguous** (C-23). |
| `shop_workers`, `job_changes` in the window | Preparation hiring (A-19); U1-b: workers move before the date (A-17). | U1-b: employers defer hires (A-16). | U1-a: only (+). U1-b: none (RS-8, 0.9). | **U1-a: increase; U1-b: ambiguous** (C-24). |
| `shop_workers` (contracts in force on 3 November 2027), `job_changes`, medium | Large shops' added staffing draws existing workers (A-19). | U1-b: lock-in of covered workers (RS-11; A-18). | U1-a: only (+). U1-b: none. | **U1-a: increase; U1-b: ambiguous** (C-25). |
| Large retailers' association, `lobbying_effort` (over Sunday opening), medium | Defending the repeal. | The campaign for repeal ends. | None (RS-7, repeal clause; A-15). | **ambiguous** (C-19). |
| Small shops' federation and union, same | Seeking to restore the ban or win new limits. | Defending the ban ends. | None. | **ambiguous** (C-20). |
| Municipal enforcement, `enforcement_cost`, short | — | Inspections and prosecutions under the ban end. | OC-3, right baseline: the comparison is the ban in force (A-24); no new municipal task. | **decrease** (C-36). |
| Municipal budgets, net of fines and officer time, short–medium | Officer time freed (C-36). | Fines lost (C-37). | None: with about 30 prosecutions a year and fines up to 50,000 per Sunday, the fines can be smaller or larger than 1.2 million (CR-8, 1.0). | **ambiguous** (C-42). |
| Owners of small shops that stay open, `resources_available_other_uses`, short–medium | Outlays saved on the lost Sunday sales: stock not bought, staff hours not paid. | Receipts lost on those sales. | A-27, an empirical premise (CR-12e; CR-4 1.1, several changes in means netted first): the receipts lost exceed the outlays saved. | **decrease** (C-40). |
| `large_shops`, `employment` (replacement hires), the window and after | U1-b: hires made after the date (C-47). | U1-b: hires deferred out of the window (A-16). | Signed per window (RS-8), not combined. | C-23 (window), C-47 (after). |

**Different variables and classes are not netted (CR-12c).** Small shops' losses (C-3, C-4, C-8, C-40) and large shops' gains (C-1, C-6, C-18) are separate consequences, as are the hours of large-shop and small-shop workers (C-10, C-9). The method does not say whether retail employment in Hastrow as a whole rises.

### Metamorphic check against the ban (derived in section 2)

Each repeal consequence is compared with the ban's derived effect. **Persistence** (TS-6) is how much of the ban's effect remains after the repeal, against the path on which it was never imposed.

| Ban (derived) | Repeal (this example) | Reverses? | Persistence (TS-6) | Reason |
|---|---|---|---|---|
| B-1 Large shops' Sunday sales: decrease to none | increase (C-1) | Reverses | partial (short); none (medium) | Shops open at once; buyers' habits shift over months (TS-8). |
| B-2 Large shops' Monday to Saturday sales: increase | decrease (C-5) | Reverses | partial (short); none (medium) | As B-1. |
| B-3 Large shops' weekly sales: decrease | increase (C-6) | Reverses | partial (short); none (medium) | Corsland and online habits change gradually (TS-8; A-6). |
| B-4 Small shops' Sunday sales: standalone increase; in centres ambiguous | decrease (C-3; standalone); ambiguous (C-16; in centres) | Reverses for standalone shops; no sign to reverse in centres | none (medium); n/a (centres) | Follows buyers' choices, which change within months. In centres the anchor's footfall and its competition oppose on both paths (corrected: the ban row was signed up for all small shops). |
| B-5 Small shops' number: increase | decrease (C-8) | Reverses, slowly | partial (medium); none (long) | Shops close as leases end and owners retire, not at once (CR-10b). |
| B-6 Standalone small shops' and small units' values and rents: increase; in-centre shops' value: ambiguous | decrease (C-4, C-33, C-34); ambiguous (C-17) | Reverses; no sign to reverse in centres | none; n/a (centres) | The advantage followed a legal rule that ends on one date, and the rivals' capacity already exists (CR-7, 1.0: which stock). What persists is the stock of shops and units, valued without the advantage (see section 8 on the stock of small units). |
| B-7 Sunday cross-border purchases: increase | decrease (C-7) | Reverses | partial (short); none (medium) | Habits and store loyalties (TS-8). |
| B-8 Corsland sellers and trip goods: at least one increase | at least one decrease (C-30); decrease (C-31) | Reverses | partial (short); none (medium) | As B-7. |
| B-21 Corsland shops near the line: value increase | decrease (C-50) | Reverses | none | Follows the legal rule, as B-6. |
| B-9 Unit size near the line: decrease; bunching below 280 m² | increase for new and refitted shops (C-13) | Reverses for the flow | partial (medium); none (long) | The stock fitted under the line changes only as shops are refitted or replaced (TS-6). |
| B-10 Formats fitted to the line: increase | decrease (C-14) | Reverses for new formats | partial (medium) | The 1,250 existing formats stay where they are. |
| B-11 Near-line shops' value: ambiguous | ambiguous (C-15) | No sign to reverse | n/a | RS-17 (0.9) both ways. |
| B-12 Large shops' and large units' values: decrease (with A-13 mirrored) | increase (C-18, C-35; A-13) | Reverses | none | Follows the legal rule. The same dominance premise is needed on both paths. |
| B-20 Investment in large stores and extensions: decrease | increase (C-46) | Reverses, slowly | partial (medium); none (long) | New building comes at the speed of planning and construction (TS-1). |
| B-13 Large-shop hours: Sunday none, Monday to Saturday up, weekly at least one decrease (with A-9 mirrored) | Sunday up (C-11); Monday to Saturday down (C-12); weekly at least one increase (C-10) | Reverses | none (medium) | Rosters change within months. |
| B-24 Large-shop workers' earnings: decrease | increase until the April 2028 pay round (C-49) | Reverses | none | Follows Sunday hours; later horizons need a premise on the pay round. |
| B-14 Small-shop workers: at least one increase | at least one decrease (C-9) | Reverses | partial (medium); none (long) | Follows the number of small shops. |
| B-22 Travel time of buyers near small shops that exist only under the ban: decrease | increase (C-51) | Reverses | partial (medium); none (long) | Follows the number of small shops. |
| B-15 Complements: around large stores down, next to small shops up | up (C-28); down (C-29) | Reverses | partial (short); none (medium) | Follows trips. |
| B-16 Online Sunday orders: increase | decrease (C-32) | Reverses | partial (short); none (medium) | Online habits (TS-8). |
| B-17 Municipal enforcement and fines: increase; net ambiguous | decrease (C-36, C-37); net ambiguous (C-42) | Reverses; no sign to reverse for the net | none; n/a (net) | Ends with the ban. |
| B-23 Large shops' fines paid: decrease in means | increase (C-52) | Reverses | none | Ends with the ban. |
| B-18 Sales tax: decrease | increase (C-39) | Reverses | partial (short); none (medium) | Follows cross-border purchases (the online chain is not used: corrected). |
| — Total in-state purchases (derived with B-7): decrease | increase (C-41) | Reverses | partial (short); none (medium) | As B-7. |
| B-25 Small shops' owners' means: increase (with A-27 mirrored) | decrease (C-40; A-27) | Reverses | none (medium) | Follows B-4; lost receipts netted against saved outlays on both paths (CR-3, 1.1). |
| B-19 Lobbying on both sides: increase | ambiguous (C-19, C-20) | Does not reverse in sign | n/a | Contested on both paths (RS-7, repeal clause). |
| — | Right to refuse in small shops (C-26), the voided rostering right and its two sides (C-43, C-44, C-45), breach (C-27), the tribunal's work (C-38), lobbying on U1 (C-21), lock-in and job changes (C-25) | No counterpart | n/a | Effects of K2, which has no counterpart in the ban. |
| — | Window effects (C-22, C-23, C-24) and their other sides after the date (C-47, C-48) | No counterpart | n/a | Transition effects (CR-10b). |

The check finds no sign that fails to reverse without a stated reason. The corrected check also flags what the first version passed over: the ban's effect on small shops in anchored centres was `ambiguous` (B-4, B-6), the mirror of C-16 and C-17, so there is nothing signed to reverse there; and every ban row now carries its premises, the mirror of the repeal's, including the dominance premises A-13 (B-12) and A-9 (B-13). Lobbying does not reverse because both sides lobbied in both worlds. Everything that does not reverse at once is a stock: small shops that close only as leases end, and premises fitted under 280 m² that change only when refitted. The values do reverse at once, because they followed the legal rule and the rivals' capacity was already in place. The right to refuse has no counterpart in the ban. It falls mainly on small shops, which the ban favored, so the Act's two components push in the same direction on them.

## 8. Time structure

- **Introduction to signing (January to May 2027).** As passage becomes likely, values move part of the way, and most of the rest at signing: small shops, small units and their rents down (C-4, C-34, C-33 on renewals), large retailers and large units up (C-18, C-35). Shops near the line are `ambiguous` (C-15).
- **Window (May to 2 November 2027).** The ban still binds; no Sunday trade moves. Large shops prepare (C-22). Under U1-a they hire ahead of opening; under U1-b ordinary hires are pushed past the date while workers who plan to move do so before it (C-23, C-24). The union and large retailers lobby on U1 (C-21). Small-shop workers who object begin giving notice; the month runs from notice, so refusals take effect from early December at the earliest for notices given on 3 November (C-26).
- **From 3 November 2027.** Large shops open on Sunday (C-1, C-11), and their staff earn more until the April 2028 pay round (C-49). Under U1-b, replacement hires deferred out of the window are made (C-47), and workers who moved early do not move again (C-48). Sales move from Saturday and weekdays (C-5, C-12), and from small shops, Corsland and online (C-3, C-7, C-32). Shoppers' habits change over months (TS-8), so the weekly shifts grow through the first year. Cafés and fuel stations around large stores gain (C-28); those next to corner shops lose (C-29).
- **Medium run.** Small shops close as leases end (C-8, C-9), and their buyers travel farther (C-51). Large retailers build new stores and extend past 280 m² (C-46). New and refitted shops are no longer fitted to 280 m² (C-13, C-14). Under U1-b, workers on contracts in force on 3 November weigh the right against moves (C-25). Lobbying continues on both sides (C-19, C-20).
- **Long run.** The number of small shops approaches what it would have been without the ban. The stock fitted under 280 m² turns over. Under U1-b the covered group shrinks as workers retire or move, until the right covers few workers.
- **Costs already incurred.** Shops fitted at 279 m², and small shops bought at prices that included the Sunday advantage, are the same with and without the repeal. They enter only through what they make cheaper or dearer next (CR-10b): those who bought recently bear the fall in value (C-4).
- **The stock of small units (CR-7, 0.9: persistence).** The premium on small units ends with the rule (C-33, C-34, persistence none). But the ban drew more small units into use than the path without it (B-5, B-6), and those units do not disappear at once. While they persist, small units can be worth less than on the never-imposed path: an overshoot, not a persistence of the ban's (+) effect. How large and how long needs a premise on the stock, so it is a path note, not a consequence.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-36 | `officials.enforcement` (municipal trading standards) | `enforcement_cost` (Sunday closure inspections and prosecutions) | decrease | Nothing given up: about 1.2 million a year of officer time freed for other tasks. | OC-3 (right baseline), CR-8a |
| C-37 | municipal budgets | `non_tax_receipts` (fines under the ban) | decrease | Fines no longer paid by large shops that opened in breach; the other side is the shops' saved fines. | CR-8b |
| C-38 | `officials.enforcement` (Employment Tribunal) | `enforcement_cost` (complaints under s. 6) | increase | Tribunal time taken from other cases or funded by the state budget. | OC-3, CR-8c |
| C-39 | state budget | `tax_revenue` (sales tax) | increase | Nothing given up: purchases back from Corsland (C-7). Orders moved from online sellers (C-32) are not used: whether they bore Hastrow sales tax is not in the record. | TX-10 (in reverse), CR-9 |
| C-40 | owners of `small_shops` (who stay open) | `resources_available_other_uses` | decrease | Receipts from Sunday sales lost to large shops, net of the outlays saved on them (stock, staff hours); the buyers took a better offer, so only the seller loses (CR-5, 0.7; OC-4 Unless). The net is signed with A-27. | CR-3 (note on lost receipts; 1.1), CR-4 (1.1), CR-5, OC-4, CR-12b, CR-12e |
| C-42 | municipalities | `resources_available_other_uses` (municipal budgets, net of fines and officer time) | ambiguous | Officer time freed against fines lost; no figure decides which is larger. | CR-8 (1.0: receipts into the same budget), CR-12b |
| C-52 | `large_shops` (that would have opened in breach) | `resources_available_other_uses` (fines no longer paid) | increase | Nothing given up: the other side of C-37. | CR-8b |

**Small shops' means (C-40).** CR-3's note, which its 1.1 clarification extends to every seller who loses sales, including to a better offer, says to combine the lost receipts with the outlays saved (CR-12b). A-27 is the dominance premise: on the Sunday sales they lose, small shops' receipts exceed the stock and staff hours they save, since they sold at positive margins and part of their staffing is fixed by opening hours. Without it, C-40 is `ambiguous`.

**Fines (C-37, C-52, C-42).** Large shops that would have opened in breach keep the fines that municipalities no longer receive (C-52, C-37; CR-8b). The fines and the officer time are two items of the municipal budget (CR-8, 1.0): the net is `ambiguous` (C-42).

**Who gains what small shops lose (CR-8b, CR-5).** On purchases that move from a small shop to a large one on Sunday, the small shop loses the sale. The large shop gains it, and the buyer gains a better offer (C-2, C-6). This is not a transfer of a right but a lost sale (CR-5, 0.7). On purchases that move from Corsland and online sellers, Hastrow's shops gain sales that Corsland and the online sellers lose (C-30, C-32). On purchases moved between days, nobody loses a sale. The capitalized value small shops lose (C-4) is the expected stream of those lost sales' margins, and it falls on whoever held the shop when the repeal became expected.

**The right to refuse (C-26, C-27, C-38).** Its cost to small-shop employers is cover for Sunday shifts. Its value to workers who use it is the Sunday they no longer work. The tribunal's time and the breach that goes unremedied are used up (CR-8c).

**Unseen uses.** Large shops' Sunday opening draws labor and energy from other uses (CR-8a). The labor is mostly hours that workers, by taking Sunday shifts, choose over their other uses of Sunday, so no named market loses it without a premise. Lobbying (C-19 to C-21) is used up (CR-8c). The repeal reduces no tax revenue, so OC-6 does not apply. Re-rostering around objectors (C-45) is used up (CR-8c).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Some large shops expect Sunday opening to cover its costs, including staff at the Sunday rate and, under U1-a, volunteers only. | alternative_uses | 0.9 | Corsland's large shops open on Sunday; the association's campaign. | Almost every consequence vanishes. |
| A-2 | Some buyers rank a Sunday trip to a large shop above their counterfactual shopping times. | other | 0.85 | Hastrow residents' Sunday trips to Corsland; surveys. | C-1 rests on A-3 and A-6; C-2 not reported. |
| A-3 | Some buyers who shop at small shops on Sunday move to large shops when they open. | substitutability | 0.85 | Small shops' Sunday share (16% to 20%); Corsland's experience. | C-3, C-4, C-8, C-9, C-29, C-33, C-34, C-40 and C-51 not reported. |
| A-4 | Owners and buyers of shops and premises expect the repeal to last. | expectations | 0.75 | Votes of 68 to 57 and 21 to 14; the failed 2024 bill on the other side. | C-4, C-18, C-34, C-35 and C-50 shrink; C-46 not reported. |
| A-5 | Some buyers move purchases from Saturday or weekdays to Sunday. | other | 0.8 | Corsland's sales by day of the week. | C-5 and C-12 not reported; C-10 rests on Sunday staffing alone. |
| A-6 | Some border residents bought in Corsland on Sundays because Hastrow's large shops were shut, and now buy at home. | mobility | 0.8 | The revenue department's 380 million estimate; 700,000 residents within 30 minutes. | C-7, C-30, C-31, C-39, C-41 and C-50 not reported. |
| A-7 | Some small shops cover their costs only with Sunday trade at its counterfactual level. | alternative_uses | 0.7 | Margins of convenience stores; Corsland's closures after its own change. | C-8 and C-51 not reported; C-9 rests on lower Sunday sales alone. |
| A-8 | Some small-shop workers object to Sunday work and give notice. | other | 0.7 | Union surveys; 31,000 small-shop workers work Sundays under "as rostered" clauses. | C-26, C-43, C-44 and C-45 not reported; C-27 and C-38 shrink. |
| A-9 | Large shops need a minimum crew for each hour open, so Sunday staffing exceeds the hours saved on other days. | other | 0.65 | Staffing rules; store opening practice in Corsland. | C-10 becomes `ambiguous`; C-49 rests on the Sunday premium alone. |
| A-10 | Large shops' Monday to Saturday staffing follows sales. | other | 0.7 | Rostering systems. | C-12 not reported. |
| A-11 | Some shops near the line would have been larger without it. | binding | 0.8 | About 1,050 shops at 250 to 280 m² against 260 at 280 to 310 m²; 1,250 chain formats fitted under the line. | C-13, C-14 and C-46's extensions not reported; C-15 loses its (+) chain and becomes a decrease. |
| A-12 | Sunday shoppers at large shops combine the trip with cafés, meals, fuel and nearby small shops. | other | 0.75 | Retail park footfall data; Corsland's Sunday trade. | C-28, C-31 not reported; C-16, C-17 lose their (+) chain. |
| A-13 | For large retailers as a class, the trade drawn from small shops, Corsland and online sellers outweighs the cost of opening a seventh day that rivals' opening may force. | other | 0.7 | Fifteen years of campaigning (demonstrated preference); Corsland's large shops' Sunday trade. | C-18 and C-35 become `ambiguous`. |
| A-14 | Organized interests on both sides can lobby at a cost below their stake. | other | 0.85 | Existing associations; the 2024 and 2027 campaigns. | C-19 to C-21 not reported. |
| A-15 | On the counterfactual path the ban would have stayed contested, with both sides lobbying. | other | 0.8 | The 2024 vote (61 to 64); the association's continuing campaign. | C-19 becomes an increase for large retailers, and C-20 an increase for the federation and union. |
| A-16 | Under U1-b, some large shops defer replacement hires past 3 November 2027 so that the new contracts are not covered. | expectations | 0.6 | Employers' advisers' guidance; turnover of about 2% a month. | C-23 and C-24 under U1-b become increases; C-47 under U1-b not reported. |
| A-17 | Under U1-b, some workers who plan to change employer move before 3 November 2027 to hold a covered contract. | expectations | 0.55 | Union advice to members. | C-24 under U1-b loses a (+) chain (still `ambiguous`); C-48 under U1-b not reported. |
| A-18 | Under U1-b, some covered workers value the right enough to turn down moves that would end it. | other | 0.6 | Survey of workers who object to Sunday work. | C-25 under U1-b becomes an increase. |
| A-19 | Large shops hire some Sunday staff from among existing shop workers. | mobility | 0.75 | Hiring patterns in retail. | C-24 and C-25 under U1-a not reported; under U1-b, C-25 becomes a decrease. |
| A-20 | The right is enforced only on complaint, and some workers who are pressed do not complain. | enforcement | 0.75 | Tribunal claim rates under other employment rights. | C-27 not reported. |
| A-21 | Some Sunday buyers at standalone small shops combine the trip with purchases at a neighboring small seller. | other | 0.65 | Parades of shops in residential streets. | C-29 not reported. |
| A-22 | Some Sunday online orders by Hastrow residents were placed because large shops were shut. | substitutability | 0.6 | Sunday share of online orders (18%) against Corsland's lower share. | C-32 not reported. |
| A-23 | The 12% rent premium on small units reflects Sunday trading, and the stock of small units cannot shrink at once. | durability | 0.7 | Letting agents' evidence; rents of comparable units in Corsland. | C-33 and C-34 not reported. |
| A-24 | On the counterfactual path the ban is enforced at about its present level. | enforcement | 0.85 | About 30 prosecutions a year; municipal budgets. | C-36, C-37 and C-52 shrink; C-42 unchanged (`ambiguous`). |
| A-25 | Retailers expect the ban to be restored within the payback period of new large stores. | expectations | 0.25 | The federation's lobbying; against it, the 2027 margins. | Below the cut-off; not reported. |
| A-26 | Retail labor cannot expand at the old wage in the first year, so large shops' Sunday hiring raises shop wages. | other | 0.45 | Retail vacancy rates; the pay agreement fixes base rates until April. | Below the cut-off; not reported. |
| A-27 | For small shops that stay open, the receipts lost on the Sunday sales that move to large shops exceed the outlays saved on those sales (stock, staff hours). | other | 0.75 | Convenience-store gross margins; staffing fixed in part by opening hours. | C-40 becomes `ambiguous`. |
| A-28 | The retail pay agreement fixes base and Sunday rates until its April 2028 renegotiation. | binding | 0.85 | The record: the agreement is renegotiated each April and applies on both paths. (The core re-run's A-N1, restricted to the period before the pay round.) | C-49 not reported. |

## 11. Report

**The policy.** From 3 November 2027, Hastrow lets shops of any size open on Sunday, ending a 1961 ban on Sunday opening by shops with more than 280 m² of sales area. Shop workers gain a statutory right to refuse Sunday work. Whether that right covers contracts made after the Act takes effect is unclear (U1).

**Visible consequences.** Large shops open and sell on Sunday (C-1), and buyers who want to shop there on Sunday can (C-2). Small shops lose Sunday trade (C-3) and value (C-4).

**Invisible consequences.**
- *Shoppers and days.* Large shops sell less from Monday to Saturday (C-5), more over the week (C-6). Fewer Sunday trips go to Corsland (C-7), so more is bought in Hastrow (C-41) and the state collects more sales tax (C-39). Fewer Sunday orders go online (C-32).
- *Small shops.* Some close over the years (C-8), with fewer jobs or hours for their staff (C-9), and their buyers travel farther (C-51). Their owners have less to spend, since the receipts lost exceed the outlays saved (C-40; A-27). Small units rent and sell for less (C-33, C-34). Bakeries and newsagents beside corner shops lose Sunday trade (C-29).
- *Large shops.* Their owners and the owners of large units gain value (C-18, C-35), and they invest in new and larger stores (C-46). Their staff work on Sunday, fewer hours on other days and more over the week (C-11, C-12, C-10), and earn more until the April 2028 pay round (C-49). Cafés and fuel stations around them gain (C-28).
- *The 280 m² line.* New and refitted shops are no longer held to it (C-13), and chains stop designing formats to it (C-14). The existing stock changes only as it is refitted.
- *The right to refuse.* In small shops, where Sunday work was required, workers who object can no longer be required to work Sundays (C-43): they gain that freedom (C-44), and their employers bear the cost of re-rostering (C-45) and adjust other terms (C-26). Some employers press workers who object, mostly where complaint is least likely (C-27); the tribunal has new work (C-38). In large shops the right is no burden against the ban; it makes their new Sunday work voluntary for those it covers.
- *U1.* If the right covers every contract (U1-a), large shops hire ahead of opening, and job changes rise in the window and after it (C-23 to C-25). If it covers only contracts in force on 3 November 2027 (U1-b), employers gain by hiring after that date and workers by moving before it, and covered workers lose the right by changing jobs, so hiring and job changes are open (C-23 to C-25); hires deferred past the date are made after it (C-47), and early movers do not move again (C-48).
- *Corsland.* Its shops, cafés and fuel stations lose Hastrow's Sunday trade (C-30, C-31), and its shops near the line lose value (C-50).
- *Enforcement.* Municipalities stop enforcing the ban (C-36) and lose its fines (C-37), which large shops keep (C-52); the municipal net is open (C-42).
- *Politics.* Both sides lobby on the reading of s. 6 (C-21).

**Ambiguous effects.** The value of shops near 280 m² (C-15); the Sunday trade and value of small shops in centres with a large store (C-16, C-17); lobbying over Sunday opening on each side (C-19, C-20); under U1-b, hiring and job changes (C-23 to C-25); municipal budgets net of fines and officer time (C-42).

**What does not reverse.** The ban's effects on values and on Sunday trade end within months: the small shops' advantage depended on a rule, not on a stock that takes years to rebuild, since the large shops were already there. What lasts is physical and contractual: small shops that close only as leases end, and premises fitted to 280 m² that change only when refitted.

**Key conditions.** Large shops expect Sunday opening to pay (A-1, p = 0.9); small shops' Sunday buyers prefer large shops when both are open (A-3, p = 0.85). The rise in large-shop staffing rests on minimum crews (A-9, p = 0.65); large retailers' gain in value on A-13 (p = 0.7); small-shop owners' loss of means on A-27 (p = 0.75).

**What this analysis cannot say.** How much trade moves, or how many small shops close; whether buyers' gains outweigh small shops' losses; effects on family life, religious observance and health, which are outside the scope of version 1; whether the repeal is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions | Persistence |
|---|---|---|---|---|---|---|---|---|---|
| C-1 | large_shops, buyers | quantity_traded (Sunday sales at shops over 280 m²) | increase | short | visible | B | CR-1, CR-4, CR-5, CR-12 | A-1, A-2 | partial (short); none (medium) |
| C-2 | buyers (who prefer large shops on Sunday) | full_cost_per_unit (time given up to buy at large shops) | decrease | short–medium | visible | B | CR-1, CR-3b, CR-4 | A-2 | none |
| C-3 | small_shops.standalone | quantity_traded (Sunday sales) | decrease | short–medium | visible | B | CR-9, RS-16, CR-4 | A-3 | none (medium) |
| C-4 | owners of small_shops.standalone | asset_value | decrease | short | visible | B | CR-7c, CR-10c, CR-7, CR-8 | A-3, A-4 | none |
| C-5 | large_shops, buyers | quantity_traded (Monday to Saturday sales at large shops) | decrease | short–medium | invisible | B | RS-8, CR-4 | A-5 | partial (short); none (medium) |
| C-6 | large_shops | quantity_traded (weekly sales) | increase | short–medium | invisible | B | CR-12e, CR-12, CR-9, RS-4, RS-16 | A-3, A-6 | partial (short); none (medium) |
| C-7 | buyers.border | cross_border_purchases (Sunday, Corsland) | decrease | short–medium | invisible | B | RS-4 | A-6 | partial (short); none (medium) |
| C-8 | small_shops | number_of_sellers | decrease | medium | invisible | B | RS-6, CR-4, CR-7a | A-3, A-7 | partial (medium); none (long) |
| C-9 | shop_workers.small | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-6, OC-5, CR-9 | A-3, A-7 | partial (medium); none (long) |
| C-10 | shop_workers.large | employment, hours_worked (weekly) | at_least_one_increase | medium | invisible | B | OC-5, CR-9, LW-10, CR-12e | A-1, A-9 | none |
| C-11 | shop_workers.large | hours_worked (Sunday) | increase | short–medium | invisible | B | CR-9, LW-10, CR-12 | A-1 | none |
| C-12 | shop_workers.large | hours_worked (Monday to Saturday) | decrease | short–medium | invisible | B | CR-9, LW-10, RS-8 | A-5, A-10 | none |
| C-13 | shops that would be fitted at or near 280 m² | unit_size (sales area of new and refitted shops) | increase | medium–long | invisible | B | RS-17 (1.1), CR-1, CR-4, TS-6 | A-11 | partial (medium); none (long) |
| C-14 | supermarket chains | reclassification (formats fitted to the line) | decrease | medium | invisible | B | RS-5, RS-17, CR-4 | A-11 | partial (medium) |
| C-15 | owners of small_shops.near_line | asset_value | ambiguous | short | invisible | B | RS-17, CR-7c, CR-12b | A-3, A-11 | n/a |
| C-16 | small_shops.in_centres | quantity_traded (Sunday sales) | ambiguous | short–medium | invisible | B | RS-9, CR-9, CR-12b | A-3, A-12 | n/a |
| C-17 | owners of small_shops.in_centres | asset_value | ambiguous | short | invisible | B | CR-7c, RS-9, CR-12b | A-3, A-12 | n/a |
| C-18 | large_shops.owners | asset_value | increase | short | invisible | B | CR-7c, CR-10c, CR-2, CR-12e | A-1, A-4, A-13 | none |
| C-19 | large retailers' association | lobbying_effort (over Sunday opening) | ambiguous | medium | invisible | B | RS-7, CR-4, CR-12b | A-14, A-15 | n/a |
| C-20 | small shops' federation, shop workers' union | lobbying_effort (over Sunday opening) | ambiguous | medium | invisible | B | RS-7, CR-4, CR-12b | A-14, A-15 | n/a |
| C-21 | shop workers' union, large retailers' association | lobbying_effort (U1 and the rules for s. 6) | increase | short–medium | invisible | B | RS-7, CR-4, CR-12 | A-14 | n/a (no counterpart) |
| C-22 | large_shops | investment_target (Sunday opening preparations, May to November 2027) | increase | short | invisible | B | RS-8, CR-10a, CR-12 | A-1 | n/a (transition) |
| C-23 | large_shops | employment (hires, May to 2 November 2027) | U1-a: increase; U1-b: ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b | A-1, A-16 | n/a (transition) |
| C-24 | shop_workers | job_changes (May to 2 November 2027) | U1-a: increase; U1-b: ambiguous | short | invisible | B | RS-8, CR-10a, CR-12b | A-16, A-17, A-19 | n/a (transition) |
| C-25 | shop_workers with contracts in force on 3 November 2027 | job_changes (after the effective date) | U1-a: increase; U1-b: ambiguous | medium | invisible | B | RS-11, CR-3, CR-4, CR-9, CR-12b | A-1, A-18, A-19 | n/a (no counterpart) |
| C-26 | shop_workers.small | wage_rate (−), non_wage_compensation (other non-wage terms) (−), employment/hours_worked (−) | at_least_one_as_stated | medium | invisible | B | PC-17 (1.1), CR-1, CR-5c, CR-6, CR-7 | A-8 | n/a (no counterpart) |
| C-27 | employers of shop workers | legal_breach (workers who object pressed or disadvantaged) | increase | short–medium | invisible | B | RS-20, CR-4 | A-8, A-20 | n/a (no counterpart) |
| C-28 | sellers.complements (around large stores) | quantity_traded (Sunday sales) | increase | short–medium | invisible | B | RS-9, CR-9 | A-1, A-12 | partial (short); none (medium) |
| C-29 | sellers.complements (next to standalone small shops) | quantity_traded (Sunday sales) | decrease | short–medium | invisible | B | RS-9, CR-9 | A-3, A-21 | partial (short); none (medium) |
| C-30 | neighboring_jurisdictions (Corsland shops) | quantity_supplied, net_price_received (Sunday sales to Hastrow residents) | at_least_one_decrease | short–medium | invisible | B | RS-4, CR-9, CR-6 | A-6 | partial (short); none (medium) |
| C-31 | neighboring_jurisdictions (Corsland cafés, fuel) | quantity_traded (on Hastrow residents' Sunday trips) | decrease | short–medium | invisible | B | RS-9, RS-4 | A-6, A-12 | partial (short); none (medium) |
| C-32 | sellers.substitutes (online sellers) | quantity_substitute (Sunday orders by Hastrow residents) | decrease | short–medium | invisible | B | RS-16, CR-9 | A-22 | partial (short); none (medium) |
| C-33 | tenants and landlords.small_units | price_paid (rent per m² of units of 280 m² or less) | decrease | short–medium | invisible | B | CR-9, CR-6, CR-7c | A-3, A-23 | none |
| C-34 | landlords.small_units | asset_value (units of 280 m² or less) | decrease | short | invisible | B | CR-7c, CR-10c | A-3, A-4, A-23 | none |
| C-35 | landlords.large_units | asset_value (units over 280 m²) | increase | short | invisible | B | CR-7c, CR-10c, CR-9 | A-1, A-4, A-13 | none |
| C-36 | officials.enforcement (municipal trading standards) | enforcement_cost (ban enforcement) | decrease | short | invisible | B | OC-3, CR-8a | A-24 | none |
| C-37 | municipal budgets | non_tax_receipts (fines under the ban) | decrease | short | invisible | B | CR-8b | A-24 | none |
| C-38 | officials.enforcement (Employment Tribunal) | enforcement_cost (complaints under s. 6) | increase | short–medium | invisible | B | OC-3, CR-8c | A-8, A-20 | n/a (no counterpart) |
| C-39 | state budget | tax_revenue (sales tax) | increase | short–medium | invisible | B | TX-10, CR-9 | A-6 | partial (short); none (medium) |
| C-40 | owners of small_shops (who stay open) | resources_available_other_uses | decrease | short–medium | invisible | B | CR-3, CR-4, CR-5, OC-4, CR-12b, CR-12e | A-3, A-27 | none (medium) |
| C-41 | buyers | quantity_traded (total retail purchases in Hastrow, weekly) | increase | medium | invisible | B | RS-4, CR-4c | A-6 | partial (short); none (medium) |
| C-42 | municipalities | resources_available_other_uses (municipal budgets, net of fines and officer time) | ambiguous | short–medium | invisible | B | CR-8, CR-12b | A-24 | n/a |
| C-43 | shop_workers.small (who object) | term_prevalence (contracts under which Sunday work can be required of an objector) | decrease | short–medium | visible | B | CR-1, CR-8 | A-8 | n/a (no counterpart) |
| C-44 | shop_workers.small (who object) | non_wage_compensation (freedom to refuse Sunday work) | increase | short–medium | invisible | B | CR-8, CR-8b, CR-3b | A-8 | n/a (no counterpart) |
| C-45 | small_shops (employers) | compliance_cost (re-rostering Sunday cover around objectors) | increase | short–medium | invisible | B | CR-1, CR-3a, CR-8c | A-8 | n/a (no counterpart) |
| C-46 | large_shops | investment_target (new large stores; shops enlarged past 280 m²) | increase | medium–long | invisible | B | CR-4, CR-10a, CR-10c, TS-5, TS-1 | A-1, A-4, A-11 | partial (medium); none (long) |
| C-47 | large_shops | employment (replacement hires, from 3 November 2027) | U1-a: no_change; U1-b: increase | short | invisible | B | RS-8, CR-1, CR-10a | A-16 | n/a (transition) |
| C-48 | shop_workers who moved employer before 3 November 2027 | job_changes (from 3 November 2027) | U1-a: no_change; U1-b: decrease | short | invisible | B | RS-8, CR-1, CR-10a | A-17 | n/a (transition) |
| C-49 | shop_workers.large | earnings (3 November 2027 to the April 2028 pay round) | increase | short | invisible | B | CR-9, LW-10, CR-12e | A-1, A-9, A-28 | none |
| C-50 | neighboring_jurisdictions (Corsland shops near the line) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, CR-9 | A-4, A-6 | none |
| C-51 | buyers.small_shop_dependent | travel_time | increase | medium | invisible | B | CR-9, CR-3a | A-3, A-7 | partial (medium); none (long) |
| C-52 | large_shops (that would have opened in breach) | resources_available_other_uses (fines no longer paid) | increase | short–medium | invisible | B | CR-8b | A-24 | none |

Final check (workflow). (1) Uncombined chains: every key with opposing chains is in section 7. That includes large shops' weekly sales, where moved purchases cancel by construction and drawn purchases add (C-6); large-shop staffing over the week (C-10); large retailers' value against rivals' opening (C-18); near-line and in-centre small shops (C-15 to C-17); the U1-b timing and lock-in chains (C-23 to C-25); lobbying on each side (C-19, C-20); small-shop owners' lost receipts against saved outlays (C-40, with A-27); and the municipal net (C-42). Sunday and other-day items are recorded per window (C-1, C-5; C-11, C-12). (2) Groups: small-shop and large-shop labor (C-9, C-10), PC-17's mixed group (C-26), Corsland's sales or prices (C-30). No group member is used as a chain elsewhere (CR-12, 1.1): the right's effect on small-shop hours is not added to C-9, large-shop earnings (C-49) are derived from A-9 directly, and no total of `non_wage_compensation` is formed from C-44 and C-26. Large-shop Sunday hours (C-11) rise from none, a new activity; weekday hours (C-12) rest on A-10 that rosters follow sales. (3) Baseline: every sign is against Hastrow with the ban in force, never against the situation before the Act or against Sunday opening without the right. U1 readings are each signed against the ban in force, not against each other. Persistence is against the path without the ban. (4) Worse off is not poorer: small-shop owners' means are signed because they lose receipts (CR-3, note), not because they are worse off. Buyers who switch are better off by their own ranking, with no money sign. (5) Timing: sales moved between days are signed per day (C-1, C-5) and hiring per window (C-23, C-24), with the other side of each U1-b move after the date (C-47, C-48), on flows; the medium run is a separate horizon (C-25). (6) Transfers: sales lost by small shops and gained by large shops (C-3, C-40; C-1, C-6); fines no longer paid and no longer received (C-52, C-37), with the municipal net (C-42); the voided rostering right, gained by objecting workers and lost by employers (C-44, C-45); sales tax gained in Hastrow against sales lost in Corsland (C-39, C-30). (7) Every class against CR-4, CR-6, CR-7 and CR-9: capitalization for small shops, near-line and in-centre shops, large retailers, both kinds of premises and Corsland's near-line shops (C-4, C-15, C-17, C-18, C-34, C-35, C-50); long-payback investment (C-46); buyers of shops that close (C-51); enforcement of the ban and of the right (C-36, C-38); CR-9 to workers, complements, Corsland, online sellers and landlords. (8) Premises: every derivation's premises are in section 10, including those below the cut-off (A-25, A-26); A-9, A-13 and A-27 are stated as dominance premises, and the accounting identity for C-6 is named. The ban table carries its premises too, mirrored. The online chain was dropped from C-39 and C-41, since it needed a premise the record does not supply. (9) Baseline of every pattern cited (catalog 1.1). PC-17 is applied only where Sunday work exists on the counterfactual path (small shops), compared with no term as its 1.1 clause says; for large shops the contracts that would carry the term exist only under the repeal, so it is not applied there (section 5; CR-3, 1.1). RS-20 is used in its 1.0 form, from none. RS-17 is applied in reverse with its 1.1 baseline clause, each band and each value signed against the ban in force, not one band against another. RS-7 is used with its repeal clause (A-15) and CR-4's 1.1 note on the same question. TS-5 and TS-1 bound long-payback investment (C-46). RS-4, RS-5, RS-6, RS-8, RS-9, RS-11, RS-16, OC-3, OC-4, OC-5, TS-6 and TX-10 compare with the path without the change, here the ban in force. PC-20, RS-24, RS-23, PC-1, PC-16, SB-4, SB-8, EN-13, EN-14, TX-1, TX-7 and TX-9 do not apply; the response argument is not used.

## Corrections after the core-only comparison

The core-only re-run (`05_examples_core/WE-063_sunday_trading_repeal_core.md`) was compared with this example. Each conclusion was checked against the core rules and catalog 1.1 before it was applied.

**Changed.**
- C-40: lost receipts are now combined with the outlays saved (CR-3's note, extended by its 1.1 clarification to sellers who lose sales to a better offer; CR-4 1.1 on netting means). The sign stays a decrease on a new dominance premise, A-27 (p 0.75), which the comparison allowed as the alternative to `ambiguous`.
- C-39, C-41: the online chain is dropped; it needed an unstated premise (that online orders bore no Hastrow sales tax, or came from sellers outside Hastrow). Both rest on the Corsland chain (A-6); A-22 removed from them.
- C-9: the right to refuse is no longer used as a (−) chain; it is a member of C-26's group (CR-12, 1.1). Sign unchanged.
- C-26: cites PC-17's 1.1 clause; its `non_wage_compensation` member is qualified as other non-wage terms, distinct from C-44.
- C-6: cites CR-12's 1.1 clause on items that cancel. C-13: cites RS-17's 1.1 baseline clause. C-19 to C-21: cite CR-4 and RS-7 1.1 on the same question. Signs unchanged.
- Ban table: premises added to every row (mirrored), including A-13 for B-12 and A-9 for B-13 (the weekly sign now a group, `at least one decrease`); B-4 and B-6 split, with shops in anchored centres `ambiguous`; B-17 adds the municipal net; B-18 drops the online chain; rows B-20 to B-25 added for the new repeal consequences.
- Metamorphic check: B-4, B-6, B-12, B-13, B-17, B-18 and the means row corrected; rows for B-20 to B-25 and for the K2 and window consequences added; the summary notes what the first check passed over.
- Section 8: path note on the stock of small units (CR-7, 0.9: persistence). Final check rewritten for 1.1, including item (9). Gaps found (b) 2 and (c) 1 marked as settled or partly settled in 1.1; a Re-run note added under (e).

**Added.** C-42 municipal budgets net of fines and officer time, `ambiguous` (core C-5). C-43 contracts under which Sunday work can be required of an objector, decrease (core C-6). C-44 objecting workers' freedom to refuse, `non_wage_compensation` increase (core C-7). C-45 small shops' re-rostering cost (core C-9). C-46 long-payback investment in large stores (core C-15). C-47 replacement hires after the date, U1-a `no_change`, U1-b increase (core C-18). C-48 early movers' later job changes, U1-a `no_change`, U1-b decrease (core C-20). C-49 large-shop workers' earnings until the April 2028 pay round (core C-29, short run only). C-50 Corsland near-line shops' value (core C-38). C-51 travel time of buyers whose small shop closes (core C-42). C-52 fines kept by large shops (core C-43). New assumptions A-27 and A-28 (the core re-run's A-N1, restricted to before the pay round).

**Removed.** None.

**Comparison conclusions rejected or applied only in part.**
- Core C-7 with a total: the item is added (C-44), but no `ambiguous` total of `non_wage_compensation` is recorded, because the opposing item is a member of C-26's group and cannot be used as a signed chain (CR-12, 1.1).
- Core C-29 in the medium and long run: not added; A-28 covers the rates only until the April 2028 pay round, as the comparison itself notes.
- Pattern C-40, which the comparison says should be `ambiguous`: applied as the comparison's alternative, a premise that the lost margins exceed the saved outlays (A-27), not as `ambiguous`.
- The comparison's view that the right still moves terms of large shops' new Sunday contracts under U1-a against none (core C-22, as a group): rejected. Under CR-3's 1.1 clarification and PC-17's 1.1 clause, a term attached to contracts that exist only under the repeal is no burden against the ban in force, where those contracts do not exist; what the right does to large shops is already in A-1.
- Core C-22 (screening of new hires) and C-30 (total retail hours, cause J): not added; the first signs one CR-6 margin with no premise for it, and nothing in 1.1 settles the second (CR-12c).
- The unit-size persistence in the long run (J): unchanged; 1.1 does not settle it.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None new. Proximity effects of Sunday traffic near large stores would run through the open GAP-026-1 (Tier C, Q20); they were not drawn, for want of neighbors' rankings in the record.

**(b) Unclear core rules.**
1. *(Open in 1.1; the core re-run reached the same answer through CR-7's 0.9 persistence clause.)* *CR-7 1.0, which stock, when the rivals' stock already exists.* The clause was written for a permission and the capital it allowed coming apart (a license and its store). Here the asset that loses value is the protected party's capital (small shops). The stock whose scarcity mattered was not a stock of small shops but large shops' Sunday capacity, which existed in full and was held shut by the rule. The clause gave the right answer, that the value falls at once and persistence is none, but only once read as: "the stock that matters is the capacity the rule held out of use; where it already exists, the value follows the legal rule alone". A sentence saying so would help.
2. *(Partly settled in 1.1: CR-3's 1.1 clarification extends the note on lost receipts to every seller who loses sales, including to a better offer.)* *CR-8 1.0, statutory rights, for an advantage that is not a right.* Small shops held no right: they gained from a prohibition on their rivals. CR-8's 1.0 note on statutory rights ("the holder loses the right's value; who gains depends on who now obtains what the right excluded") was applied by analogy (C-4). CR-5's 0.7 clause, lost sales to a better offer, gave the payer side more precisely (C-40, section 9). Worth a note under CR-8 that a protection held by virtue of a restriction on others is analyzed as lost sales (CR-5), not as a voided right.
3. *CR-3b and a class of competitors.* Each large shop gains an option, but the class can be worse off if every rival's opening forces each to open (CR-9). CR-3b is about one actor at the time of choice, and it is silent on whether an option added to all competitors can lower their joint yield. The chain was treated as kind (2), needing a dominance premise (A-13). A note under CR-3 would stop analysts from reading CR-3b as signing a class's value.

**(c) Missing or wrong patterns.**
1. *(Settled in 1.1: PC-17's 1.1 clause, compare with no term, and CR-3's 1.1 clarification on burdens attached to an option that exists only under the policy.)* *PC-17 where the mandated term attaches to an activity the counterfactual forbids.* PC-17's preconditions read as met for every shop worker, since the right covers all shop contracts. Its conclusion (other terms adjust against the worker) is right only where Sunday work exists on the counterfactual path. In large shops, where the ban rules Sunday work out, PC-17 as written would compare with Sunday opening without the right, another policy, and give a wage cut that the counterfactual does not support. I had to override it there (CR-12, 1.0). PC-17 could say: "where the term attaches to an option the policy itself adds, it narrows that option and is not a burden against the counterfactual".
2. *RS-17 in reverse.* RS-17 has no clause for removing a threshold. In reverse, its conclusions split by stock and flow: new and refitted units move away from the line at once (C-13), the stock fitted to it persists (TS-6), and the 0.9 value clause gives `ambiguous` for near-line firms (C-15), with the freedom to grow as the (+) chain. A sentence pointing to TS-6 would help.
3. *RS-22 has no variable for "harder to fill".* Under U1-b, new hires whose contracts require Sunday work would get a compensating differential (RS-22). Its group includes "those jobs are harder to fill", which has no variable, so a group of `wage_rate` and `non_wage_compensation` would overclaim. Combined with the labor-demand premise (A-26, p = 0.45), the chain was not recorded. See (d) 2.
4. *RS-11 for a status fixed at a date.* RS-11 worked as written for U1-b (C-25). It does not say that a status fixed at a date also produces a rush to acquire it before the date (C-24). That came from RS-8 and is worth a cross-reference.
5. No other pattern gave a sign I had to override. *(Corrected after the core-only comparison: C-40 cited CR-3 without netting the saved outlays, and C-39 and C-41 used an online chain resting on an unstated tax premise; both were the analyst's errors, not the patterns'.)*

**(d) Vocabulary.**
1. *Days and hours of sale.* There is still no variable for the days or hours on which a good may be sold or a shop may open (as in WE-052). Sunday trade was recorded as `quantity_traded` per day.
2. *Vacancies.* No variable for how hard jobs are to fill, which RS-22 needs (c) 3.
3. *A repealed prohibition.* The instrument list has `prohibition` but no instrument for ending one; K1 was recorded as the removal of a `prohibition`.
4. `full_cost_per_unit` is defined by waiting, search and side payments; it was used for the time buyers give up to shop on a day they rank lower (C-2), which fits its spirit but not its examples.

**(e) Test of 1.0.**
- *Repeal with a metamorphic check (workflow, 0.9 note: derive the original first).* Worked as written: the ban's effects were derived in section 2 (B-1 to B-19) before the repeal, and every repeal sign was compared with them in section 7. No sign failed to reverse without a stated reason.
- *RS-9, location complements and trips.* RS-9 has no 1.0 clause; the 0.9 clause on location complements worked as written. It gave the gain to cafés and fuel stations around large stores (C-28), the loss beside corner shops (C-29) and in Corsland (C-31), and the opposing chain for small shops in anchored centres (C-16, C-17). Its "new occupants" clause did not arise.
- *RS-8, sales moved between days.* Worked as written: Sunday and other days signed per window (C-1, C-5), and the week as a separate key settled by an accounting identity (C-6). RS-8's 0.9 clause on parties moving in opposite directions in time worked for U1-b hiring (C-23, C-24). The 1.0 clause on races and rivals did not apply.
- *CR-7 1.0, which stock (values of small shops whose Sunday advantage ends).* Needed interpretation ((b) 1): the stock that mattered was the rivals' existing capacity, not the small shops. Read so, it gave a fall in value at once and persistence none (C-4, C-34), with the physical stock persisting (C-8, C-13).
- *CR-8 1.0, statutory rights.* Needed interpretation ((b) 2): small shops held no right, so CR-5's lost-sale clause gave the payer side.
- *RS-17 in reverse (the 280 m² line), with RS-17 1.0 (notches, mirrors).* Worked, with a reading for the reverse ((c) 2). The ban was a notch on the whole shop above the line (RS-17 1.0's mirror clause), and the case's figures show the bunching (B-9). The repeal gives larger new units (C-13), fewer formats fitted to the line (C-14), and an `ambiguous` value near the line (C-15, RS-17 0.9).
- *PC-17, the mandated right to refuse.* Worked as written for small shops (C-26). Failed for large shops, where its preconditions read as met but its comparison is with another policy ((c) 1); re-signed there under CR-12 1.0 and not applied.
- *RS-7 1.0 and CR-4 1.0, lobbying where the question was contested.* Worked as written: both sides lobbied on both paths, each `ambiguous` (C-19, C-20; A-15). Questions that exist only under the Act gave an increase (C-21).
- *CR-12 1.0, the baseline of patterns.* Worked as written, and it mattered: it caught PC-17's comparison for large shops ((c) 1). It also confirmed RS-20's 1.0 baseline (C-27, from none) and RS-17's bands signed against the ban, not against each other.
- *CR-12 1.0, what the response argument needs.* Not used: no price in this case was signed by the response argument. Small-unit rents (C-33) were signed with a fixed stock in the short run (CR-6, 0.9), and large shops' weekly sales by an accounting identity (C-6).
- *CR-12 1.0, tiers and dominance.* Worked as written: the dominance premises A-9 and A-13 settled C-10 and C-18 without changing their tier (B).
- *RS-20 1.0, baseline.* Worked as written (C-27).
- *TS-5, credibility.* Worked as written; the premise (A-25) was below the cut-off.
- *Candidate patterns from 06_gaps.md, 6.2e.* None needed. Two new moves were derived from the core rules: a status fixed at a date producing a rush before it and lock-in after it (C-24, C-25; RS-8 with RS-11), and an option added to all competitors that can lower their joint yield (C-18; CR-3b with CR-9). Both are candidates if a second case needs them.
Re-run note: the core-only comparison found that the metamorphic check did not "work as written" in one respect, since it passed over ban rows B-4 and B-6 that should have been `ambiguous` for shops in anchored centres (now corrected), and that PC-17's failure for large shops lay in how its If clause is read rather than in its logic.
