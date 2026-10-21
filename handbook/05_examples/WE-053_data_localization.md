# WE-053 Data localization requirement

Analyst: draft (Handbook 0.9 held-out test, corrected under 1.0)  |  Rule catalog version: 1.0  |  Status: awaiting expert review

A stylized policy in a fictional country. Several countries require some personal data to be stored at home; this one is not modeled on any of them. It is a held-out test of catalog 0.9 on a case the 0.9 changes were not drawn from. It probes CR-4's 0.8 clause on costs fixed per firm and per outlet (a migration per firm; a local data center per country for a cloud provider; a certificate per facility), RS-17's 0.9 clause on the value of firms near a size threshold (50,000 residents' records, measured over the year before the requirement applies), TX-8's 0.9 clause on a change in the form of imports (cloud services imported from abroad against imported servers and foreign investment in local data centers), CR-6's 0.9 clause on splitting a shift in demand between price and quantity, RS-16's 0.9 clause on costs the policy attaches to the substitute, a barrier to foreign suppliers that collects no tax (the candidate "tariff-like burden without a tax" from `06_gaps.md`), and CR-12's three kinds of opposing chain. The unclear provision is whether encrypted backup copies may be kept abroad. The counterfactual throughout is **Corvany without the requirement**; every sign is relative to that path. Effects on privacy, security and the environment are out of scope for version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite. The example was corrected under catalog 1.0 after its core-only comparison; the changes are listed before "Gaps found".

## 1. Policy record

**Corvany Personal Data Residency Act.** Corvany is a country of 22 million people with its own currency, the crown, and a floating exchange rate. Its largest trading partner is Esterland, 300 km away, where the three large cloud providers that serve Corvany run their nearest data center regions. Corvany's main exports are machinery, timber and tourism.

The Data Protection Office's register (2026) counts firms by the number of Corvany residents whose personal data each data controller holds:

| Residents' records held | Controllers |
|---|---|
| 20,000 to 40,000 | 1,900 |
| 40,000 to 50,000 | 650 |
| 50,001 to 60,000 | 380 |
| 60,001 to 100,000 | 720 |
| Over 100,000 | 2,000 |

So about 3,100 controllers are above the threshold. About 2,150 of them (70%) store and process this data mainly abroad, almost all in the three providers' Esterland regions. About 950 already host it in Corvany, in their own data centers or with local colocation firms; about 600 of these keep backup copies abroad. About 400 of the 3,100 are foreign online services with no establishment in Corvany (shops, apps, games).

| Item | Figure |
|---|---|
| Corvany firms' spending on cloud services | about 1.1 billion crowns a year, nearly all bought from the Esterland regions |
| Local colocation | four firms, nine facilities, 60 MW, 85% occupied; facility revenue 30 to 120 million crowns a year |
| Cost of local hosting per unit of computing | estimated 25% to 40% above the Esterland regions (smaller scale, dearer electricity) |
| A provider's local region (two separate sites) | about 400 million crowns, 18 to 30 months to build. Providers N and S announced regions in August 2027; provider T has not decided; dozens of smaller foreign providers have none. |
| Grid connections | below 10 MW about 12 months; above 10 MW three to four years. Sites with grid capacity and fiber are in two industrial zones. |
| Hosting as a share of costs | 1% to 3% for banks and retailers; 10% to 20% for online services |
| Migration of a firm's systems | 150,000 to 2 million crowns per firm, by consultants (about 40 firms in Corvany) |

The bill was introduced on 14 October 2026 and enacted on 1 July 2027. The requirement applies from 1 January 2029, 18 months after enactment. It has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Residency | `prohibition` of storing or processing covered data outside Corvany | Personal data of Corvany residents | Each data controller that held such data on more than 50,000 residents on any day of the preceding calendar year | From 1 January 2029, the data "shall be stored and processed only on servers located in Corvany". A foreign provider may comply by operating servers in Corvany. The count is per controller; a group's companies count separately. | Controllers at or below 50,000 |
| K2 Officer and statement | Compliance requirement | Covered controllers | Covered controllers | Appoint a data residency officer; file an annual residency statement. | — |
| K3 Facility certificate | `licensing_requirement` for facilities | Data centers in Corvany that host covered data | Facility operators | Annual audit of physical security and access logs; fee 40,000 crowns per facility a year. | — |
| K4 Enforcement | — | — | Data Protection Office | Fines up to 4% of turnover. For a foreign controller with no establishment in Corvany, the Office may order internet providers to block its service, after a hearing; it has never issued a blocking order under the existing privacy law. The Office receives a supplementary appropriation of 6 million crowns a year from the general budget. Fees go to the general budget. | — |

Unclear provisions:
- **U1, encrypted backups abroad.** Section 4(2): "A copy made solely for security may be kept outside Corvany where the Office so allows by regulation." The Office has issued no regulation and has said nothing about whether it will. Reading U1-a: encrypted backup copies may be kept abroad (the provision is read as permitting security copies, with the regulation setting only conditions). Reading U1-b: until the Office allows it by regulation, every copy, including backups, must be in Corvany. Readings get no probability; where a sign depends on one, each reading's sign is reported.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: forbids exchanges between covered controllers and providers serving them from abroad. CR-1: removes, for covered controllers, the option of hosting abroad (operation 1), dated 1 January 2029; before then it acts through expectations (CR-10a), and asset values move at once (CR-7c). For foreign providers, the option of serving covered controllers from abroad is removed and the option of serving them from Corvany is open at a fixed cost per country (CR-4, 0.8, per outlet). The operation differs on either side of 50,000 (CR-1, 0.9), and the line is a notch: once a controller passes it, the whole of its covered data is bound, so the jump is a cost of crossing (CR-1, 1.0; RS-17, 1.0). The count repeats each calendar year and binds for the next. | Yes: 70% of covered controllers host abroad (A-1). | CR-1, CR-4 (0.8), CR-6 (0.9), CR-7c, CR-12e (1.0), RS-1, RS-3, RS-4 (0.9), RS-13 (1.0), RS-14, RS-16 (1.0), RS-17 (0.9, 1.0), RS-21, RS-6, TX-8 (0.9), OC-5 |
| K2 | Operation 3 on the option of holding data above the threshold: a cost fixed per controller (CR-4, 0.8) | Yes | CR-4, CR-8c, RS-17 |
| K3 | Operation 3 on the option of hosting covered data in a facility: a cost fixed per facility (CR-4, 0.8, per outlet) | Yes | CR-4, RS-16 (1.0) |
| K4 | Enforcement; funding from the general budget, into which fees and fines also go | — | OC-3, OC-1 (1.0), CR-8 (1.0), RS-3, RS-4 (0.9) |
| U1 | U1-a: no operation on encrypted backups abroad. U1-b: removes the option of keeping them abroad (operation 1). | Per reading | CR-1, CR-4 |

**A barrier to foreign suppliers without a tax.** K1 works like an import ban on a service for one class of buyers, with a route around it for foreign suppliers that invest locally. Nothing is collected: the difference between the cost of hosting abroad and at home is used up (CR-8c), not received by the state. TX-7's preconditions are not met (there is no tariff), so the consequences are derived from the core rules in sections 5 and 6: covered controllers lose options and pay more (CR-1, CR-6), domestic sellers of the substitute gain in the short run (CR-9, CR-6), foreign sellers abroad lose sales (CR-4), and part of the burden settles on whoever has the worse alternatives (CR-7b). Unlike a tariff, the barrier has a route around it: a foreign supplier that builds locally becomes a domestic rival of the protected sellers, so their gain is not signed in the medium run (C-18, C-40, C-21). This is not the move of the candidate "tariff-like burden without a tax" (WE-040), which is a cost per unit on an imported input; catalog 1.0 did not promote that candidate.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `firms.covered` | The 3,100 controllers above 50,000 | Must host in Corvany from 2029; appoint an officer, file a statement. |
| `firms.covered.abroad` | The 2,150 that host abroad now | Must migrate. |
| `firms.covered.local` | The 950 that host in Corvany now (600 with backups abroad) | Under U1-b, must bring backups home. |
| `firms.near_threshold` | Controllers with roughly 40,000 to 60,000 records | Can stay or get below the line by purging records or splitting. |
| `firms.below_threshold` | Controllers just below 50,000 | Not bound; their rivals above are. |
| `sellers.foreign` (cloud providers) | The three large providers and smaller foreign providers | Cannot serve covered controllers from abroad; may build in Corvany, with means drawn from investment elsewhere. |
| `sellers.foreign.online` | The 400 foreign online services above the threshold with no establishment | Localize, cap Corvany users, withdraw, or ignore the law. |
| `sellers.substitutes` (local data center operators) | Four colocation firms, nine facilities | More demand; certificate per facility. |
| `sellers.prospective` | New local data centers | Entry pays where demand rises. |
| `sellers.domestic_digital` | Domestic online services already hosting locally | Some foreign rivals withdraw or cap. |
| `buyers` | Corvany users of online services | Some foreign services leave; prices of some rise. |
| `workers.data_centers` | Staff who run data centers in Corvany | More local capacity to run. |
| `factor_owners.specific` | Owners of sites with grid capacity and fiber | Data centers seek sites. |
| `input_suppliers` | Foreign makers of servers and network equipment; construction workers | Data centers are built in Corvany. |
| `intermediaries` | Migration consultants | Migrations before 2029. |
| `neighboring_jurisdictions` | Data centers in Esterland | Lose Corvany workloads; their other customers face less demand for the same capacity. |
| `exporters` | Corvany's export industries | The currency link changes (TX-8). |
| `officials.enforcement` | Data Protection Office | Audits, statements, certificates. |
| `taxpayers`, recipients of other spending, future taxpayers | Fund the Office's appropriation; the same budget receives fees and fines | Pay for it, and receive the fees and fines. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `firms.covered` | `compliance_cost` (migration, residency officer, annual statement) | increase | short–medium | CR-1, CR-4 (0.8), CR-8c, OC-2 | A-1, A-2 |
| C-2 | `sellers.substitutes` | `quantity_supplied` (capacity hosting covered data in Corvany) | increase | medium | CR-1, CR-9, CR-6, CR-7a | A-1, A-2, A-3 |
| C-3 | `sellers.foreign` (cloud providers) | `investment_target` (local regions in Corvany) | increase | medium | CR-4 (0.8, per outlet), CR-7a | A-4 |

The visible effects are that data moves home (C-2), cloud providers build local regions (C-3), and firms pay to move (C-1). C-1 is mainly a cost fixed per controller (migration, officer, statement) and, for a provider, C-3 is a cost fixed per country: by CR-4's 0.8 clarification each bears on whether the firm serves covered data in Corvany at all, and on the size at which it pays to do so (RS-17, C-9 to C-12), not on the price of each unit of service. Only the higher cost per unit of local computing (C-4) bears on unit prices (C-26).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `firms.covered.abroad` | `price_paid` (hosting per unit of computing) | increase | medium | CR-1, CR-4, CR-6 | A-1, A-5 |
| C-5 | `firms.covered` | `number_of_sellers` (providers whose hosting they may use) | decrease | short–medium | CR-1 | A-1, A-6 |
| C-6 | `sellers.foreign` | `quantity_traded` (cloud services supplied from abroad to covered controllers) | decrease | medium (from 2029) | CR-1, CR-4 | A-1, A-2 |
| C-7 | `firms.covered` | `quantity_traded` (backup storage abroad) | U1-a: no_change; U1-b: decrease | medium | CR-1 | A-2, A-7 |
| C-8 | `firms.covered.local` (with backups abroad) | `compliance_cost` (a second site in Corvany) | U1-a: no_change; U1-b: increase | short–medium | CR-1, CR-8c | A-2, A-7 |
| C-9 | `firms.near_threshold` | `reclassification` (records of inactive users deleted; data split between controllers) | increase | short (during 2028, the first counting year) | RS-17, RS-21, CR-4, CR-10a | A-8, A-9 |
| C-10 | `firms.near_threshold` | `number_of_sellers` (controllers just below 50,000, relative to just above) | increase | short–medium | RS-17 | A-8, A-10 |
| C-11 | `firms.below_threshold` | `asset_value` | ambiguous | short | RS-17 (0.9), CR-7c, CR-12b | A-10 |
| C-12 | `sellers.foreign.online` | `quantity_supplied` (accounts offered to Corvany residents) | decrease | medium | RS-17, CR-4 (0.8), RS-6 | A-11 |
| C-13 | `sellers.foreign.online` | `legal_breach` (serving above the threshold from abroad without complying) | increase | medium | RS-3, RS-4 (0.9: reach of enforcement), CR-4 | A-11, A-12 |
| C-14 | `sellers.substitutes`, `sellers.foreign`, `firms.near_threshold` | `lobbying_effort` (threshold, U1 regulation, exemptions) | increase | short–medium | RS-7, CR-4 | A-13 |
| C-15 | `intermediaries` | `quantity_traded` (migration services, July 2027 to December 2028) | increase | short (window) | RS-8, CR-12 (0.9: activities that exist only under the policy) | A-1, A-2 |
| C-16 | `firms.covered.abroad` | `quality_per_unit` (hosting: latency and range of services) | ambiguous | medium | CR-4, CR-12b | A-14, A-15 |

**Covered controllers (C-4 to C-8).** For the 2,150 that host abroad, the cheaper option is removed (CR-1, operation 1), so they buy from a local source: colocation, a provider's local region, or their own servers. Local computing costs more per unit (A-5), so they pay more (C-4). They can no longer buy from providers without a Corvany presence: provider T unless it builds, and the smaller foreign providers (C-5; A-6). The foreign providers' sales from Esterland to covered controllers fall (C-6). Under U1-b, backups must come home too: backup storage bought abroad falls (C-7), and the 600 controllers that host locally but back up abroad need a second local site (C-8). Under U1-a, nothing changes for encrypted backups, provided they were encrypted on the counterfactual path (A-7).

**The threshold (C-9 to C-12): RS-17 with its 0.9 clause.** The line is drawn on records held on any day of the preceding calendar year, so the first count is 2028, and the response comes then, before the requirement applies (RS-17). For a controller just above 50,000, deleting the records of inactive users, or splitting customers between two controllers of the same group (which the Act counts separately), costs less than migrating (A-8, A-9). So some do (C-9), and controllers bunch just below the line (C-10). Deleting the records of inactive users is RS-21's move (promoted in 1.0): the line counts records whose value differs, so a controller near it keeps the more valuable ones. Since the line is a notch (section 2), the cost of crossing it is the whole of C-1, not a cost on the records above 50,000. C-11, the value of controllers just below the line: RS-17's 0.9 clause applies as written. (−) Growing past 50,000 now brings the fixed costs of C-1, so the option to grow is worth less (CR-7c). (+) Their rivals above the line bear those costs and pay more per unit (C-4), so the controllers below gain customers or margin (CR-9). No premise ranks the two: `ambiguous`. Foreign online services with modest Corvany user numbers face a fixed cost per country they serve (CR-4, 0.8, per outlet). Where Corvany is too small a market to cover it (A-11), they cap Corvany sign-ups below the line or withdraw (C-12; RS-6).

**Evasion and the reach of enforcement (C-13).** RS-4's 0.9 clause: the Act claims to reach every controller holding Corvany residents' data, but it can be enforced by fines only against those with an establishment or assets in Corvany. Against the rest the only tool is a blocking order, which the Office has never used (A-12). So some foreign services above the line keep serving from abroad without complying (CR-4, x: comply, y: breach). This is breach within a legal market, not informal trade (`legal_breach`).

**Lobbying (C-14).** The Act creates concentrated stakes: local operators gain from a lower threshold and from U1-b; providers and covered controllers gain from U1-a and from exemptions; controllers near the line gain from a higher one (RS-7; A-13). There was no question on these points on the counterfactual path, so the lobbying is an increase against none.

**Timing (C-15).** Migration services exist only because of the Act (CR-12, 0.9), so the window's work is an increase against none, signed on the flow of migration work. Migrations bunch in the last months of 2028, when colocation space is scarcest (section 8).

**Quality of hosting (C-16): CR-12's kinds of opposing chain.** Two derived chains push the quality of hosting for migrated controllers in opposite directions. (+) Servers in Corvany are nearer Corvany users, so latency falls (A-14). (−) New local regions launch with fewer services than the Esterland regions, and colocation offers fewer still (A-15). Both are kind (2) chains: the rules derive them and each needs a premise with p of at least 0.5. Before the Act, these controllers chose Esterland over the colocation already available in Corvany, which shows they ranked it higher in the situation then (CR-2); that says nothing about each attribute. The combined sign is `ambiguous`.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | `firms.covered` | `price_substitute` (local colocation per rack) | increase | short (2028 to 2029) | RS-16 (1.0, per unit of quality), CR-6 (0.9: splitting a shift) | local hosting and foreign hosting: `substitute`, close | A-1, A-16 |
| C-18 | `firms.covered` | `price_substitute` (local colocation per rack) | ambiguous | medium | RS-16, CR-6, CR-12e (0.9, 1.0), RS-13 (1.0), CR-12b | as C-17; providers' local regions and colocation: `substitute`, close | A-1, A-4, A-17, A-26 |
| C-19 | `sellers.substitutes` | `net_price_received` (colocation per rack) | increase | short (2028 to 2029) | RS-16 (1.0), CR-6, CR-4 (0.8) | as C-17 | A-1, A-16 |
| C-40 | `sellers.substitutes` | `net_price_received` (colocation per rack) | ambiguous | medium | RS-16 (1.0), CR-12e (1.0), RS-13 (1.0), CR-12b | as C-18 | A-1, A-4, A-17, A-26 |
| C-20 | `sellers.substitutes` | `number_of_sellers` (facilities hosting covered data) | ambiguous | medium | CR-4 (0.8, per outlet), RS-16, CR-12b | as C-17 | A-3, A-18 |
| C-21 | `sellers.substitutes` | `asset_value` (local data center firms) | ambiguous | short (from enactment) | CR-7c, CR-10c, CR-12b | as C-18 | A-1, A-2, A-4, A-16, A-26 |
| C-22 | `sellers.prospective` | `entry_rate` (new data centers in Corvany) | increase | medium | CR-4, CR-7a | as C-17 | A-3 |
| C-23 | `factor_owners.specific` | `asset_value` (sites with grid capacity and fiber) | increase | short | CR-7c, CR-9 | sites `input_to` data centers | A-3, A-17 |
| C-24 | `input_suppliers` (foreign makers of servers and equipment) | `quantity_traded` (imports of servers and network equipment into Corvany) | increase | medium | CR-9 | equipment `input_to` local hosting | A-3, A-4 |
| C-25 | `input_suppliers` (construction workers) | `employment` (data center construction in Corvany) | increase | short–medium | OC-5 (new to the place), CR-9 | construction `input_to` data centers | A-3 |
| C-38 | `workers.data_centers` | `employment` (data center operation in Corvany) | increase | medium | OC-5 (new to the place), CR-9, LW-10 | labor `input_to` local hosting | A-3, A-4 |
| C-26 | `buyers` (of online services from covered controllers) | `price_paid` (+), `quantity_supplied` (−) | at_least_one_as_stated | medium | RS-14, CR-9 | hosting `input_to` online services | A-5, A-19 |
| C-27 | `buyers` (Corvany users) | `variety` (online services available) | decrease | medium | CR-9, CR-4 (0.8) | — | A-11 |
| C-36 | `buyers` (users of foreign services that cap or withdraw) | `quantity_traded` (use of those services) | decrease | medium | CR-9, CR-5a, OC-4 | exchange with the services in C-12 | A-11 |
| C-28 | `sellers.domestic_digital` | `quantity_supplied`, `net_price_received` | at_least_one_increase | medium | CR-9, CR-6 (0.9) | domestic and foreign online services: `substitute`, partial | A-11, A-20 |
| C-37 | `sellers.domestic_digital` | `asset_value` | ambiguous | short (from enactment) | CR-7c, CR-10c, CR-9, RS-17 (0.9), CR-12b | as C-28; colocation `input_to` their services | A-11, A-16, A-20 |
| C-29 | `exporters` | `quantity_supplied`, `employment` | ambiguous | medium | TX-8 (0.9), CR-9 (currency), CR-12b | `currency` | A-21 |
| C-30 | `neighboring_jurisdictions` (data centers in Esterland) | `quantity_supplied` (hosting for Corvany covered controllers) | decrease | medium | CR-1, CR-9 | `across_border` | A-1, A-2 |
| C-41 | `neighboring_jurisdictions` (data centers in Esterland) | `net_price_received` (hosting, all customers of the Esterland regions) | decrease | medium | CR-9, CR-6 (0.9; 1.0, small effects are signed) | `across_border` | A-1, A-2, A-25 |

**Local colocation (C-17 to C-22): CR-6's 0.9 clause on splitting a shift.** K1 shifts covered controllers' demand to hosting in Corvany (RS-16). CR-6's 0.9 clarification: the shift gives the direction; how it divides between price and quantity needs a premise about local supply in the period. In 2028 and 2029, before the providers' regions open and new facilities are connected, the nine facilities have 15% of their space free and cannot add more within a year (A-16). So the price rises (C-17), and the quantity used rises only into the free space. In the medium run, the providers' regions open and new facilities are connected (C-2, C-22). Two chains meet there, and CR-12's 1.0 clarification keeps them apart. (+) CR-12e's response argument bounds colocation's own expansion: new colocation space drawn by the higher price cannot push it below its old level, since entry stops once a new facility earns no more than elsewhere. The total it bounds is the price of local hosting as a whole, colocation and regions together, and with A-17 (large capacity cannot be added at the old cost within five years: connections above 10 MW take three to four years, sites with grid capacity are few; a rising-cost premise) it gives an increase in that total. (−) The providers' regions are a new competitor attracted by the policy, a second chain that the argument does not cover (CR-12, 1.0). A region is a close substitute for colocation (RS-13, 1.0, supply added to a linked market), and it is also a new option for customers the Act did not move: controllers that already host in Corvany for latency and would rather have a provider's full range of services nearby (A-26). If enough of them leave colocation, its price per rack can fall below the counterfactual. No premise ranks the two chains, so the medium-run colocation price (C-18) and operators' net price (C-40) are `ambiguous`.

**Costs on the substitute (C-19, C-20): RS-16's 0.9 and 1.0 clauses.** RS-16 0.9 says a cost the policy attaches to the substitute is an opposing chain on its sellers' net price. Here the cost is K3's certificate, 40,000 crowns per facility a year, a cost fixed per outlet. By CR-4's 0.8 clarification a fixed cost per outlet bears on whether the outlet operates, not on the price of each unit, and RS-16's 1.0 clause now says so: only a cost per unit sold opposes sellers' net price. So it is not an opposing chain on the net price per rack (C-19, increase in the short run, from the demand shift alone); the 0.9 clause, applied as written, would have made C-19 `ambiguous` wrongly. Prices are signed per rack of a given specification (RS-16, 1.0, per unit of quality). Where the fixed cost does bite is on the number of facilities hosting covered data (C-20): the demand shift draws more facilities in (+), while for some small facilities the certificate and audit cost more than the margin on covered data, so they decline it (−; A-18). Kind (2) chains: `ambiguous`. Recorded in (c) 1.

**Operators' value (C-21).** The value of local colocation firms, capitalized at enactment and partly from the bill's introduction (CR-7c, CR-10c), reflects their whole expected yield path: higher in 2028 and 2029 (C-19), `ambiguous` once the providers' regions open (C-40). The certificate is an opposing cost, but arithmetic on the case's figures makes it small (40,000 crowns a facility against facility revenue of 30 to 120 million). What decides the sign is the regions' competition, which no premise ranks against the short-run gain: `ambiguous` (CR-12b).

**Inputs and sites (C-23 to C-25).** Data centers need sites with grid capacity and fiber, which are few (C-23; CR-7c), servers and network equipment, which Corvany imports (C-24), and construction (C-25; OC-5, new to the place). Once built, the new capacity is run by staff in Corvany (C-38; CR-9 with LW-10; OC-5, new to the place). Stopped: electricity users who compete for grid connections, depth 3, diffuse.

**Prices of online services (C-26).** For online services, hosting is 10% to 20% of costs (A-19), and the cost per unit of computing rises (C-4). RS-14: the price rises or the quantity supplied falls, at least one. Their competitors are mixed: rivals above the line bear the same cost, rivals below it and foreign services that ignore the law (C-13) do not, so neither RS-14 clause dominates. Recorded as a mixed group. For banks and retailers, hosting is 1% to 3% of costs, and no claim is made. The fixed costs (C-1) are not passed into unit prices (CR-4, 0.8).

**Users and domestic rivals (C-27, C-28, C-36, C-37).** Foreign services that withdraw or cap sign-ups (C-12) leave Corvany users fewer services to choose from (C-27), and the exchanges those users would have made with them do not take place (C-36; CR-5a, OC-4: both sides lose the gain each expected). Domestic services that already host locally gain some of those users (CR-9; A-20); how the gain divides between more sales and higher prices needs a supply premise (CR-6, 0.9), so it is a group (C-28). Their value (C-37) is reached by opposing chains. (+) The gain in C-28 is capitalized at enactment (CR-7c, CR-10c). (−) Those that rent colocation pay more per rack in 2028 and 2029 (C-17; A-16); those above 50,000 records bear K2's officer and statement; those below it lose part of the value of growing past it (RS-17, 0.9). No premise ranks these: `ambiguous`.

**Exports and the currency link (C-29): TX-8's 0.9 clause.** Corvany pays foreigners about 1.1 billion crowns a year for cloud services. Under K1 the form of these imports changes. (−) Imports of cloud services from Esterland fall (C-6): foreigners earn fewer crowns to spend on Corvany's exports (TX-8). (+) Imports of servers and network equipment rise (C-24), and the foreign providers' local subsidiaries pay their parents for software, licenses and profits: foreigners earn crowns that way instead. (−, during construction) The providers bring about 800 million crowns of investment from abroad (A-21): foreigners buy Corvany assets with crowns that would otherwise have gone to exports, and in the currency market the crown is dearer than it would have been while they buy it (CR-6), which makes exports dearer abroad. TX-8's 0.9 clause covers "imports of one good fall but imports of goods made from it rise" and makes the chain `ambiguous` (kind 3). Here what rises is imports of the inputs to a local substitute, plus a capital inflow, which TX-8's own premise ("trade is not offset by capital flows") rules out. Read with that extension, the chain's parts push both ways and nothing cancels by construction: CR-12's 0.9 kind (3), `ambiguous`.

**Esterland (C-30, C-41).** Data centers in Esterland lose Corvany workloads (C-6): the quantity they supply to covered controllers falls directly, since the option is removed (CR-1, operation 1), so no premise on splitting a shift is needed for it (C-30). The capacity freed is offered to their other customers. Where it cannot be cut at once (A-25), the price they receive falls in that wider market (CR-6). Corvany is a small share of that market, so the fall may be small; under CR-6's 1.0 clarification it is signed, not left as negligible (C-41).

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `firms.below_threshold`, `asset_value`, short | Rivals above the line bear fixed and unit costs (CR-9). | The option to grow past 50,000 is worth less (CR-7c). | None (RS-17, 0.9). | **ambiguous** (C-11). |
| `firms.covered.abroad`, `quality_per_unit`, medium | Lower latency (A-14). | Fewer services in new regions and colocation (A-15). | None: kind (2) chains. | **ambiguous** (C-16). |
| `firms.covered`, `price_substitute` (colocation), medium | Demand shifted home; colocation's own expansion cannot reverse it (CR-12e, with A-17 as the rising-cost and partial premise, bounding local hosting as a whole). | Providers' regions, a new competitor attracted by the policy, which also draw customers the Act did not move (A-4, A-26); a second chain (CR-12, 1.0). | None. | **ambiguous** (C-18). |
| `sellers.substitutes`, `net_price_received`, short | Demand shifted home (A-16). | None per unit: the certificate is a cost fixed per facility (CR-4, 0.8; RS-16, 1.0). | — | **increase** (C-19). |
| `sellers.substitutes`, `net_price_received`, medium | As C-18 (+). | As C-18 (−). | None. | **ambiguous** (C-40). |
| `sellers.substitutes`, `number_of_sellers` (facilities hosting covered data), medium | Demand draws facilities in. | Certificate exceeds the margin for some small facilities (A-18). | None: kind (2) chains. | **ambiguous** (C-20). |
| `sellers.substitutes`, `asset_value`, short | Higher yield in 2028 and 2029 (C-19). | The regions' competition in the medium run (C-40, itself `ambiguous`); annual certificate (small by arithmetic). | None covers the regions' chain in both its directions (CR-12, 0.8, kind 3). | **ambiguous** (C-21). |
| `sellers.domestic_digital`, `asset_value`, short | Users of withdrawn foreign rivals (C-28). | Dearer colocation in 2028 and 2029 (C-17); K2 above the line; the option to grow past 50,000 below it (RS-17, 0.9). | None. | **ambiguous** (C-37). |
| `taxpayers`, recipients of other spending, future taxpayers, `resources_available_other_uses`, short–medium | Certificate fees and fines paid into the same budget (C-33). | The 6 million crown appropriation (C-31). | None: fees alone are far smaller (40,000 crowns a facility), but fines cannot be bounded from the case's figures (CR-8, 1.0). | **ambiguous** (C-32). |
| `exporters`, `quantity_supplied`, `employment`, medium | Imports of equipment; subsidiaries' payments abroad. | Imports of cloud services fall; capital inflow during construction. | None: kind (3) chain (TX-8, 0.9). | **ambiguous** (C-29). |
| `buyers`, `price_paid` and `quantity_supplied` of online services, medium | — | — | RS-14 gives at least one; competitors' exposure is mixed. | **at_least_one_as_stated** (C-26). |
| `sellers.foreign`, sales to covered controllers | Sales from local regions (C-3). | Sales from abroad (C-6). | Different segments, not netted (CR-12c). | Recorded separately. |

**CR-12's three kinds of opposing chain, as met here.**
- *Kind (1), a chain no rule derives.* Supporters claim residents will trust domestic hosting more and shop online more; that needs premises on what residents believe and how they would move (CR-11, 0.7), and the Act conveys no information about any firm. Opponents claim Esterland will retaliate against Corvany's exports; responses of foreign governments are not derived (Q5). Both are Tier C notes, not chains, and they do not make C-27, C-28 or C-29 ambiguous.
- *Kind (2), a derived chain with a premise.* C-11, C-16, C-18, C-20, C-37 and C-40: each opposing chain has its premise in section 10 with p of at least 0.5, so the result is `ambiguous`. A chain with a premise below 0.5 would have been reported in section 10 only; A-24 is such a premise (section 10).
- *Kind (3), a chain whose own sign is ambiguous.* The currency chain (C-29); the medium-run colocation yield as it enters operators' value (C-21).

**Readings.** C-7 and C-8 are `no_change` under U1-a, an increase in cost or a decrease in backups abroad under U1-b. U1-b also adds to the demand shift for local capacity (C-17, C-18, C-2), in the same direction, so those signs do not depend on the reading.

## 8. Time structure

- **Introduction to enactment (October 2026 to July 2027).** Values of local data center firms and of sites with grid capacity rise part of the way as passage becomes likely, the rest at enactment (C-21, C-23).
- **Window (July 2027 to December 2028).** Providers N and S build their regions (C-3), which take 18 to 30 months, so some may not be ready by January 2029; their customers then need colocation in the meantime, which adds to the pressure on the nine facilities (C-17). 2028 is the first counting year: controllers near the line purge records and split before it ends (C-9, C-10), and foreign services cap Corvany sign-ups (C-12). Migration work runs through the window and bunches in its last months (C-15). This bunching is a path note: migrations exist only because of the Act, so it is not a timing shift against the counterfactual (CR-12, 0.9).
- **From January 2029.** Data must be in Corvany; foreign services that do not comply and have no establishment continue in breach (C-13). The Office's first statements and audits (C-31). Under U1-b, backups come home (C-7, C-8).
- **Medium run.** New facilities connect: those below 10 MW within about a year, larger ones in three to four years (C-22), and the providers' regions open. Covered controllers still pay more per unit of computing than in Esterland (C-4), but colocation's own price is `ambiguous`, since the regions also draw its existing customers (C-18, C-40, A-26). Data center operating jobs rise as capacity opens (C-38).
- **Threshold over time (TS-3).** The 50,000 line is fixed in records while online use grows, so more controllers cross it each year; the share of firms bound rises over time.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-31 | `officials.enforcement` | `enforcement_cost` (statements, audits, certificates) | increase | Staff time and resources, funded by the supplementary appropriation. | OC-3, CR-8c |
| C-32 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` | ambiguous | The 6 million crowns a year from the general budget, net of the certificate fees and fines paid into it. | OC-1 (1.0), OC-3, CR-8 (0.7, 1.0), CR-12b |
| C-33 | State budget | `non_tax_receipts` (certificate fees, fines) | increase | Nothing given up by the state: operators' and fined controllers' outlay. | CR-8b |
| C-34 | `firms.covered` (those that stay above the threshold) | `resources_available_other_uses` | decrease | Other uses of the money paid for migration, compliance and dearer hosting, which they cannot avoid while they stay above the line. | CR-3, CR-8a |
| C-35 | `sellers.substitutes` | `compliance_cost` (facility certificate and audit) | increase | The other uses of the fee and audit time. | CR-8c, CR-4 (0.8) |
| C-39 | `sellers.foreign` (providers that build) | `resources_available_other_uses` (investment elsewhere) | decrease | About 400 million crowns per region that the providers would have invested elsewhere. | CR-8a, CR-3 |

**Where the burden goes.** The difference between the cost of hosting in Esterland and in Corvany is not collected by anyone: it is means used up (CR-8c), the core of a barrier to foreign suppliers without a tax. Part of the higher price of local hosting is not a cost but a rent to the owners of local facilities and sites while capacity is short (C-19 in 2028 and 2029, C-23): that part is a transfer from covered controllers (and, through C-26, their customers) to them (CR-8b). In the medium run the providers' regions compete for it (C-40, C-21 `ambiguous`). The regions themselves are built with means the providers would have invested elsewhere (C-39; CR-8a), and users of foreign services that withdraw lose the exchanges they would have made (C-36). How the burden divides among covered controllers, their customers and the foreign providers depends on their alternatives (CR-7b); no premise compares them, so only the direction of each price is signed. The certificate fee is paid by operators (C-35) and received by the state (C-33). The state budget has two items, the appropriation (C-31) and the fees and fines (C-33), both in the general budget; the net for its payers is C-32, `ambiguous` (CR-8, 1.0; OC-1, 1.0). Migration spending by covered controllers (C-1) is received by consultants (C-15).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The requirement binds: many covered controllers would host abroad without it. | binding | 0.95 | 70% host abroad now. | Almost every consequence vanishes. |
| A-2 | The Office enforces the requirement against controllers with an establishment in Corvany. | enforcement | 0.85 | Fines up to 4% of turnover; existing privacy enforcement. | C-1, C-2, C-6 to C-8, C-15, C-21 and C-30 shrink. |
| A-3 | Local capacity can be added at some cost: colocation expansions and connections below 10 MW within about a year. | alternative_uses | 0.8 | Grid operator's lead times; operators' expansion plans. | C-2, C-22 to C-25 not reported; C-20 loses its (+) chain. |
| A-4 | At least one foreign provider builds a local region. | expectations | 0.85 | Providers N and S announced regions in August 2027. | C-3, C-39 not reported; C-24 and C-38 rest on colocation alone; C-18, C-21 and C-40 lose their (−) chain. |
| A-5 | Local computing costs more per unit than the Esterland regions. | other | 0.85 | Estimates of 25% to 40%; scale; electricity prices. | C-4 not reported; C-26 loses its premise. |
| A-6 | Some providers that covered controllers used do not build in Corvany. | other | 0.8 | Provider T undecided; dozens of smaller foreign providers. | C-5 not reported. |
| A-7 | On the counterfactual path, covered controllers' backups abroad are encrypted. | other | 0.8 | Industry practice; the providers' default settings. | Under U1-a, controllers would have to encrypt backups, so C-7 and C-8 become increases in cost under U1-a too. |
| A-8 | For some controllers near 50,000, deleting inactive records or splitting between controllers costs less than compliance. | other | 0.75 | Records of inactive users; groups with several brands. | C-9, C-10 not reported. |
| A-9 | The Office does not treat a group's controllers as one. | enforcement | 0.6 | The Act counts "each controller". | C-9 rests on deletions alone. |
| A-10 | The cost of compliance is material against the gain from growing past 50,000. | binding | 0.8 | Migration costs of 150,000 to 2 million crowns per controller. | C-10, C-11 not reported. |
| A-11 | Some foreign online services find Corvany too small to justify local hosting, and cap sign-ups or withdraw. | alternative_uses | 0.7 | 400 foreign services above the line; Corvany's market size. | C-12, C-27, C-28, C-36 not reported; C-37 loses its (+) chain; C-13 loses its population. |
| A-12 | Enforcement against foreign services without an establishment is weak. | enforcement | 0.7 | No blocking order ever issued. | C-13 not reported. |
| A-13 | Local operators, providers and controllers near the line can organize at a cost below their stake. | other | 0.85 | Their submissions on the bill. | C-14 not reported. |
| A-14 | Local hosting cuts latency for Corvany users, which some controllers value. | other | 0.7 | Round trips of about 10 ms to Esterland. | C-16 becomes a decrease. |
| A-15 | New local regions launch with fewer services than the Esterland regions; colocation offers fewer still. | other | 0.6 | Providers' launch practice for new regions. | C-16 becomes an increase. |
| A-16 | Local colocation cannot add space beyond its 15% free capacity within a year. | durability | 0.8 | 85% occupancy; 12-month connections. | C-17 becomes a group of price and quantity; C-19, C-21 and C-37 lose a premise. |
| A-17 | Large capacity cannot be added at the old cost within five years, and the cost of adding it does not fall as more is added. | durability | 0.65 | Connections above 10 MW take three to four years; few sites. | C-18 and C-40 lose their (+) chain's sign; C-23 loses a premise. |
| A-18 | For some small facilities, the certificate and audit cost more than the margin on hosting covered data. | other | 0.55 | Small facilities among the nine; audit requirements. | C-20 becomes an increase. |
| A-19 | Hosting is a material part of the cost of online services. | other | 0.75 | 10% to 20% of costs. | C-26 not reported. |
| A-20 | Domestic services that host locally are substitutes for some foreign services that withdraw. | substitutability | 0.7 | Domestic shops and apps in the same categories. | C-28 not reported. |
| A-21 | The providers' investment is financed from abroad, and servers and equipment are imported. | other | 0.8 | Providers' practice; no server manufacturing in Corvany. | C-29 would rest on the fall in service imports alone and become a decrease; C-39's means come from the providers' investment in Corvany or elsewhere, still a decrease. |
| A-22 | The supplementary appropriation is paid from the general budget, with no named tax. | revenue_use | 0.9 | K4. | C-32's payers change. |
| A-23 | Some controllers above the threshold continue to pay higher costs rather than drop below it. | other | 0.9 | 2,000 controllers above 100,000 records. | C-34 not reported. |
| A-24 | Covered controllers move other operations (staff, offices) to Corvany along with their data. | other | 0.2 | Data can be hosted locally without moving staff. | Below the cut-off; not reported. |
| A-25 | The Esterland regions' capacity is not cut as fast as Corvany workloads leave. | durability | 0.7 | Data center capacity is durable; Corvany's demand is about 1.1 billion crowns a year. | C-41 not reported. |
| A-26 | Some controllers that already host in Corvany colocation, covered or not, move to a provider's local region when it opens. | substitutability | 0.65 | They host locally for latency; a region adds the providers' full range of services. | C-18 and C-40 become increases (with A-17), and C-21 an increase. |

## 11. Report

**The policy.** From January 2029, any controller that held personal data on more than 50,000 Corvany residents in the previous year must store and process it on servers in Corvany. Foreign cloud providers may comply by building local data centers. Covered controllers appoint an officer and file a statement; facilities hosting covered data must be certified each year. Whether encrypted backups may be kept abroad is unclear (U1).

**Visible consequences.** Firms pay to move their data home (C-1); local data centers fill and expand (C-2); two foreign providers build local regions (C-3).

**Invisible consequences.**
- *Covered firms* pay more per unit of computing (C-4), from fewer providers (C-5); whether their hosting is better or worse is open (C-16). If backups must also stay home, those that host locally need a second site (C-8, U1-b). They have less for other uses (C-34).
- *The threshold.* Firms near 50,000 delete records or split before the 2028 count (C-9) and bunch below the line (C-10); whether firms just below are worth more or less is open (C-11). Some foreign online services cap Corvany users or leave (C-12), so users have fewer services (C-27) and lose the use they made of them (C-36), and domestic rivals gain sales or margin (C-28), though whether they are worth more is open (C-37); others ignore the law where it cannot reach them (C-13).
- *Local suppliers.* Colocation prices rise in the short run (C-17), and operators receive more per rack then (C-19); in the medium run, when the providers' regions open and compete for colocation's customers, both are open (C-18, C-40), and so is the value of colocation firms (C-21). New data centers enter (C-22); sites with power and fiber rise in value (C-23); construction work, operating jobs and equipment imports rise (C-24, C-25, C-38). Whether more or fewer facilities host covered data is open (C-20).
- *Customers of online services* pay more or are offered less (C-26).
- *Abroad.* Foreign providers sell less from Esterland (C-6), and Esterland's data centers lose Corvany work (C-30) and receive a little less from their other customers (C-41). Providers that build in Corvany invest less elsewhere (C-39). The effect on Corvany's exports is open (C-29).
- *The state.* The Office's costs rise, paid from the general budget (C-31); the same budget collects certificate fees and fines (C-33), so whether its payers end up with less is open (C-32).
- Lobbying over the threshold and backups rises (C-14); migration consultants are busy until 2029 (C-15).

**Ambiguous effects.** Value of firms just below the line (C-11); quality of hosting (C-16); colocation prices and operators' net price in the medium run, and operators' value (C-18, C-40, C-21); number of facilities hosting covered data (C-20); value of domestic rivals (C-37); exports (C-29); the general budget's payers (C-32).

**Key conditions.** The requirement binds (A-1, p = 0.95) and is enforced at home (A-2, p = 0.85); local computing costs more (A-5, p = 0.85); large capacity is slow to add (A-17, p = 0.65); some local colocation customers move to the providers' regions (A-26, p = 0.65).

**What this analysis cannot say.** How much hosting costs rise or how many firms change their size; whether firms' costs outweigh any gains; whether the Act is desirable; effects on privacy, security and the environment, which are out of scope for version 1; and whether foreign governments respond (Q5).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | firms.covered | compliance_cost (migration, officer, statement) | increase | short–medium | visible | B | CR-1, CR-4 (0.8), CR-8c, OC-2 | A-1, A-2 |
| C-2 | sellers.substitutes | quantity_supplied (capacity hosting covered data in Corvany) | increase | medium | visible | B | CR-1, CR-9, CR-6, CR-7a | A-1, A-2, A-3 |
| C-3 | sellers.foreign (cloud providers) | investment_target (local regions) | increase | medium | visible | B | CR-4 (0.8), CR-7a | A-4 |
| C-4 | firms.covered.abroad | price_paid (hosting per unit of computing) | increase | medium | invisible | B | CR-1, CR-4, CR-6 | A-1, A-5 |
| C-5 | firms.covered | number_of_sellers (providers they may use) | decrease | short–medium | invisible | B | CR-1 | A-1, A-6 |
| C-6 | sellers.foreign | quantity_traded (cloud services from abroad to covered controllers) | decrease | medium | invisible | B | CR-1, CR-4 | A-1, A-2 |
| C-7 | firms.covered | quantity_traded (backup storage abroad) | U1-a: no_change; U1-b: decrease | medium | invisible | B | CR-1 | A-2, A-7 |
| C-8 | firms.covered.local | compliance_cost (second site in Corvany) | U1-a: no_change; U1-b: increase | short–medium | invisible | B | CR-1, CR-8c | A-2, A-7 |
| C-9 | firms.near_threshold | reclassification (records deleted; data split) | increase | short | invisible | B | RS-17, RS-21, CR-4, CR-10a | A-8, A-9 |
| C-10 | firms.near_threshold | number_of_sellers (just below 50,000, relative to just above) | increase | short–medium | invisible | B | RS-17 | A-8, A-10 |
| C-11 | firms.below_threshold | asset_value | ambiguous | short | invisible | B | RS-17 (0.9), CR-7c, CR-12b | A-10 |
| C-12 | sellers.foreign.online | quantity_supplied (accounts offered to Corvany residents) | decrease | medium | invisible | B | RS-17, CR-4 (0.8), RS-6 | A-11 |
| C-13 | sellers.foreign.online | legal_breach | increase | medium | invisible | B | RS-3, RS-4 (0.9), CR-4 | A-11, A-12 |
| C-14 | sellers.substitutes, sellers.foreign, firms.near_threshold | lobbying_effort | increase | short–medium | invisible | B | RS-7, CR-4 | A-13 |
| C-15 | intermediaries | quantity_traded (migration services, window) | increase | short | invisible | B | RS-8, CR-12 (0.9) | A-1, A-2 |
| C-16 | firms.covered.abroad | quality_per_unit (hosting) | ambiguous | medium | invisible | B | CR-4, CR-12b | A-14, A-15 |
| C-17 | firms.covered | price_substitute (local colocation) | increase | short | invisible | B | RS-16 (1.0), CR-6 (0.9) | A-1, A-16 |
| C-18 | firms.covered | price_substitute (local colocation) | ambiguous | medium | invisible | B | RS-16, CR-6, CR-12e (0.9, 1.0), RS-13 (1.0), CR-12b | A-1, A-4, A-17, A-26 |
| C-19 | sellers.substitutes | net_price_received (colocation per rack) | increase | short | invisible | B | RS-16 (1.0), CR-6, CR-4 (0.8) | A-1, A-16 |
| C-20 | sellers.substitutes | number_of_sellers (facilities hosting covered data) | ambiguous | medium | invisible | B | CR-4 (0.8), RS-16, CR-12b | A-3, A-18 |
| C-21 | sellers.substitutes | asset_value (local data center firms) | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-12b | A-1, A-2, A-4, A-16, A-26 |
| C-22 | sellers.prospective | entry_rate (new data centers) | increase | medium | invisible | B | CR-4, CR-7a | A-3 |
| C-23 | factor_owners.specific | asset_value (sites with grid capacity and fiber) | increase | short | invisible | B | CR-7c, CR-9 | A-3, A-17 |
| C-24 | input_suppliers (foreign equipment makers) | quantity_traded (imports of servers and equipment) | increase | medium | invisible | B | CR-9 | A-3, A-4 |
| C-25 | input_suppliers (construction workers) | employment (data center construction) | increase | short–medium | invisible | B | OC-5, CR-9 | A-3 |
| C-26 | buyers (of online services) | price_paid (+), quantity_supplied (−) | at_least_one_as_stated | medium | invisible | B | RS-14, CR-9 | A-5, A-19 |
| C-27 | buyers (Corvany users) | variety (online services) | decrease | medium | invisible | B | CR-9, CR-4 (0.8) | A-11 |
| C-28 | sellers.domestic_digital | quantity_supplied, net_price_received | at_least_one_increase | medium | invisible | B | CR-9, CR-6 (0.9) | A-11, A-20 |
| C-29 | exporters | quantity_supplied, employment | ambiguous | medium | invisible | B | TX-8 (0.9), CR-9, CR-12b | A-21 |
| C-30 | neighboring_jurisdictions (Esterland data centers) | quantity_supplied (hosting for Corvany covered controllers) | decrease | medium | invisible | B | CR-1, CR-9 | A-1, A-2 |
| C-31 | officials.enforcement | enforcement_cost | increase | short–medium | invisible | B | OC-3, CR-8c | A-22 |
| C-32 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses | ambiguous | short–medium | invisible | B | OC-1 (1.0), OC-3, CR-8 (0.7, 1.0), CR-12b | A-22 |
| C-33 | state budget | non_tax_receipts (certificate fees, fines) | increase | medium | invisible | B | CR-8b | A-1, A-3 |
| C-34 | firms.covered (staying above the line) | resources_available_other_uses | decrease | medium | invisible | B | CR-3, CR-8a | A-1, A-5, A-23 |
| C-35 | sellers.substitutes | compliance_cost (facility certificate) | increase | short | invisible | B | CR-8c, CR-4 (0.8) | A-1 |
| C-36 | buyers (users of foreign services that cap or withdraw) | quantity_traded (use of those services) | decrease | medium | invisible | B | CR-9, CR-5a, OC-4 | A-11 |
| C-37 | sellers.domestic_digital | asset_value | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-9, RS-17 (0.9), CR-12b | A-11, A-16, A-20 |
| C-38 | workers.data_centers | employment (data center operation in Corvany) | increase | medium | invisible | B | OC-5, CR-9, LW-10 | A-3, A-4 |
| C-39 | sellers.foreign (providers that build) | resources_available_other_uses (investment elsewhere) | decrease | short–medium | invisible | B | CR-8a, CR-3 | A-4 |
| C-40 | sellers.substitutes | net_price_received (colocation per rack) | ambiguous | medium | invisible | B | RS-16 (1.0), CR-12e (1.0), RS-13 (1.0), CR-12b | A-1, A-4, A-17, A-26 |
| C-41 | neighboring_jurisdictions (Esterland data centers) | net_price_received (hosting, all customers) | decrease | medium | invisible | B | CR-9, CR-6 (0.9, 1.0) | A-1, A-2, A-25 |

Final check (workflow). (1) Every (actor class, variable) reached by more than one chain is in section 7, including the threshold (C-11), the quality of hosting (C-16), the certificate against the demand shift for operators (C-19, C-20, C-21), the providers' regions against the shifted demand in the medium run (C-18, C-40, C-21; CR-12, 1.0: a new competitor is a second chain), domestic rivals' value (C-37), the budget's outlay against fees and fines (C-32) and the currency chain (C-29); the providers' sales abroad and at home are different segments (CR-12c). (2) Group signs: online services' price or quantity (C-26), domestic rivals (C-28); Esterland's quantity to covered controllers falls directly (C-30) and its wider-market price is signed with a premise (C-41; CR-6, 1.0, small effects are signed). (3) Every sign is against Corvany without the Act; the U1-a `no_change` on backups is against counterfactual backups that are already encrypted (A-7). (4) `resources_available_other_uses` is signed only for controllers that keep paying (C-34, A-23) and for providers that build (C-39); for the budget's payers it is `ambiguous` (C-32). (5) Timing: migration work exists only under the Act (C-15, an increase against none); the bunching before January 2029 is a path note; the 2028 threshold response is signed in its window (C-9). (6) Transfers: fees (C-35, C-33); migration spending (C-1, C-15); the appropriation and the receipts into the same budget (C-31, C-33, net C-32; CR-8, 1.0); the rent to local operators (section 9). (7) CR-7c for local operators, sites, firms below the line and domestic rivals (C-21, C-23, C-11, C-37); enforcement and its funding (C-31, C-32); CR-9 to inputs and labor (C-24, C-25, C-38), users (C-27, C-36), domestic rivals, Esterland and exporters; CR-8a for the providers' investment (C-39). (8) Every premise is in section 10, including the regions' draw on existing colocation customers (A-26) and Esterland's capacity (A-25); the response argument names its total (local hosting as a whole) and its rising-cost premise (A-17; CR-12, 1.0). (9) Baselines of the patterns cited: RS-16 is used with its 1.0 clauses (per unit of quality; a fixed cost per facility bears on the number of facilities); RS-17 with its 0.9 and 1.0 clauses (notch); RS-21 (promoted in 1.0) for deletions; RS-13 (1.0) for the regions' added supply. RS-1, RS-3, RS-4, RS-6, RS-7, RS-8, RS-14, TX-8, TS-3, OC-1 to OC-5 compare with Corvany without the Act. RS-20, EN-11, EN-13 and PC-17 are not used; TX-7 is named only to say its preconditions fail. No pattern compares with anything else.

## Corrections after the core-only comparison

The core-only re-run (`05_examples_core/WE-053_data_localization_core.md`) was compared with this example. Each conclusion was checked against the core rules and catalog 1.0 before it was applied.

**Changed.**
- C-18: increase → `ambiguous`. The providers' regions are a new competitor attracted by the policy, which CR-12's 1.0 clarification makes a second chain outside the response argument; they also draw colocation customers the Act did not move (A-26, new). The argument now names its total (local hosting as a whole) and its rising-cost premise (A-17, reworded). The comparison classed this row J; 1.0 settles it.
- C-19: horizon short–medium → short (A-16); the medium run is the new C-40, `ambiguous`. Cites RS-16 (1.0), which now states the pattern version's override.
- C-21: increase → `ambiguous`; the value follows the yield path, which is `ambiguous` in the medium run.
- C-30: group of quantity and price → quantity supplied to covered controllers, decrease, directly by CR-1; the price is the new C-41, signed under CR-6's 1.0 note on small effects instead of being left as possibly negligible.
- C-32: `at_least_one_decrease` → `ambiguous`. Fees and fines go into the same general budget that pays the appropriation (CR-8, 1.0; OC-1, 1.0). Fees alone are far smaller, but fines cannot be bounded from the case's figures.
- C-9: cites RS-21 (promoted in 1.0) for deleting inactive users' records. Section 2: the line is recorded as a notch with an annual count (CR-1, 1.0; RS-17, 1.0).
- Section 2 and Gaps found (c) 4: the barrier is no longer called a second use of the candidate "tariff-like burden without a tax"; domestic sellers' gain is signed only in the short run.
- Section 7, 8, 9 and the report follow these changes; final check item (9) added; Gaps found (b) 1, (b) 2, (c) 1 and (c) 3 marked as settled or covered in 1.0.

**Added.** C-36 users' lost exchanges with foreign services that cap or withdraw (core C-32). C-37 domestic rivals' value, `ambiguous` (core C-35, re-signed; see below). C-38 data center operating jobs (core C-41). C-39 providers' investment withdrawn from elsewhere (core C-42). C-40 operators' net price per rack in the medium run, `ambiguous` (split from C-19). C-41 Esterland's price to its other customers, decrease (CR-6, 1.0). New assumptions A-25 and A-26.

**Removed.** None.

**Comparison conclusions rejected or applied only in part.**
- Core C-35 (domestic substitutes' value increase): not applied as an increase. The class also faces dearer colocation in 2028 and 2029 (C-17), K2 above the line, and a less valuable option to grow below it (RS-17, 0.9), each derived, so the sign is `ambiguous` (C-37).
- Core C-15, C-37 and C-38 (early breach, consultants' price, crowded-out IT projects; cause A) and C-39 (grid queues; cause J): not added; each rests on a new premise or a depth choice that 1.0 does not settle.
- The comparison's verdict that the candidate "tariff-like burden without a tax" was not validly used a second time: accepted; the candidate was not promoted in 1.0, and this example no longer claims that use.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12. The claimed effects on residents' trust and on foreign retaliation are kind (1) notes (Q5, CR-11), not calculus gaps.

**(b) Unclear core rules.**
1. *CR-4 0.8, fixed costs per firm and per outlet, against RS-16 0.9.* CR-4's clause says a cost fixed per outlet bears on whether the outlet operates, not on the unit price. RS-16's 0.9 clause says a cost on the substitute is an opposing chain on its sellers' net price, without saying per unit. The two had to be reconciled (C-19, C-20): only a per-unit cost opposes the net price per unit; a fixed cost per outlet opposes the number of outlets. (Settled in 1.0: RS-16, "Per unit of quality".)
2. *CR-6 0.9, splitting a shift, over two horizons.* Worked, but in the medium run it had to be combined with CR-12e's response argument and its 0.9 partial-response clause to give a sign (C-18); without A-17 the price would be "increase or no change", a result the ontology has no sign for (recorded in (d) 2). (Superseded in 1.0: CR-12's clarification makes the providers' regions a second chain, so the medium run is `ambiguous`, C-18.)
3. *CR-12 0.8, kind (2), with a revealed preference.* For C-16, that controllers chose Esterland before shows only their ranking of the bundle (CR-2); the attribute chains still need their own premises. Worked, but the note could say that a past choice does not decide a kind (2) chain.

**(c) Missing or wrong patterns.**
1. *RS-16 0.9, costs on the substitute.* Applied as written to K3's certificate, its clause gives an opposing chain on operators' net price and makes C-19 `ambiguous`. The derivation (CR-4, 0.8) gives no per-unit chain from a fixed cost per facility, so C-19 is an increase. I overrode the pattern's sign. Suggested fix: "Where the policy attaches a cost per unit to the substitute ...; a cost fixed per outlet bears on the number of outlets (CR-4, 0.8)." (Settled in 1.0: RS-16, "Per unit of quality".)
2. *TX-8 0.9, a change in the form of imports.* Its clause names "goods made from it". Here imports of a service fall and imports of the inputs to its local substitute rise, together with a capital inflow, which TX-8's own premise excludes. The conclusion (`ambiguous`, kind 3) was right, but only by extension. Suggested wording: "imports of the good, of goods made from it, or of the inputs to a domestic substitute, or capital flows the policy draws".
3. *RS-17 0.9.* Worked as written, including the clause on measurement over a past period (C-9 in 2028). It does not mention deleting records, a way of staying below a line on a stock rather than a flow; `reclassification` fitted. (Covered in 1.0 by RS-21, high-grading under a cap counted in physical units.)
4. *A barrier to foreign suppliers without a tax.* No pattern covers it; derived from CR-1, CR-4, CR-6, CR-7b, CR-8c and CR-9 (section 2). This is the second use of the candidate "tariff-like burden without a tax" (WE-040). The use is valid against the counterfactual: each sign (C-4, C-6, C-17 to C-21, C-30) is against Corvany without the Act, and nothing is collected. It differs from WE-040 in that the burden is a prohibition with a route around it for foreign suppliers who invest locally, not a cost per unit, so the pattern should cover both a per-unit burden and an option removed with a fixed-cost route around it. (Not promoted in 1.0: the core-only comparison found this a different move, since the route around the barrier turns foreign suppliers into domestic rivals and the protected sellers' gain holds only in the short run. At most it is a separate candidate: a location requirement with a route around it for suppliers who invest locally.)
5. RS-14 worked as written; mixed exposure of competitors gave a group (C-26).

**(d) Vocabulary.**
1. *Data held.* No variable for the stock of records a firm holds; deletions to stay below the line were recorded as `reclassification` (C-9).
2. *"Increase or no change".* There is no sign for the result CR-12e's response argument gives without a partial-response premise; it can only be written in prose.
3. *Instrument.* No instrument type for a location requirement (where an activity must take place); K1 was recorded as a `prohibition`.
4. *Latency and range of services* were folded into `quality_per_unit` (C-16).

**(e) Test of 0.9.**
- *CR-4 0.8, a cost fixed per firm and per outlet.* Worked as written for firms (C-1, C-9, C-12) and providers (C-3): no unit-price claim was drawn from fixed costs. For facilities it conflicted with RS-16's 0.9 clause ((b) 1, (c) 1).
- *RS-17 0.9, value of firms near the line.* Worked as written: `ambiguous` (C-11). The past-period clause also worked (C-9 in 2028).
- *TX-8 0.9, a change in the form of imports.* Needed interpretation ((c) 2): extended from "goods made from it" to inputs of a local substitute and capital flows; the kind (3) result then followed.
- *CR-6 0.9, splitting a shift.* Worked as written in the short run (C-17, with A-16) and for groups (C-28, C-30); in the medium run it needed CR-12e ((b) 2).
- *CR-12 0.9, what the response argument gives.* Worked as written: the partial-response premise (A-17) turned "not below the old level" into `increase` (C-18).
- *RS-16 0.9, costs on the substitute.* Failed as written for a fixed cost per facility: it gave a sign the derivation does not support ((c) 1).
- *A barrier to foreign suppliers without a tax.* Derived from the core rules; second valid use of the 6.2e candidate ((c) 4), which by the rule in 6.2e promotes it, with the widening noted.
- *CR-12 0.8 and 0.9, kinds of opposing chain.* Worked as written: kind (1) as Tier C notes (trust, retaliation), kind (2) as `ambiguous` (C-11, C-16, C-20), kind (3) for the currency chain (C-29), with the 0.9 note that a chain whose parts push both ways is kind (3) unless they cancel by construction.
- *CR-1 0.9, an operation that differs on either side of a threshold.* Worked as written (section 2).
- *RS-4 0.9, reach of enforcement.* Worked as written: the effective boundary is where fines can be collected (C-13).
- *CR-12 0.9, activities that exist only under the policy.* Worked as written (C-15, C-14).
- *OC-3 and OC-1, payers from a general budget.* Worked as written (C-32, a group).
- *Candidates from 06_gaps.md, 6.2e.* "Tariff-like burden without a tax" was needed; see above.

Re-run note: the comparison contradicted three verdicts above: the candidate's use here is not a valid second use (a different move; not promoted in 1.0); CR-6 0.9 with CR-12e and CR-12 0.9 on the response argument did not "work as written" for C-18, since the providers' regions are a second chain and the medium run is `ambiguous` (C-18, C-40, C-21); and OC-1 and OC-3 on general-budget payers gave C-32 without the fees and fines paid into the same budget.
