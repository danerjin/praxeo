# WE-053 / Analysis: Data localization requirement

Analyst: core-only re-run (Handbook 0.9)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Corvany Personal Data Residency Act.** Corvany has 22 million people, its own floating currency (the crown), and its largest trading partner, Esterland, 300 km away, where the three large cloud providers serving Corvany run their nearest regions. Main exports: machinery, timber, tourism.

The Data Protection Office's 2026 register counts controllers by Corvany residents' records held: 1,900 at 20,000 to 40,000; 650 at 40,000 to 50,000; 380 at 50,001 to 60,000; 720 at 60,001 to 100,000; 2,000 above 100,000. About 3,100 are above the threshold; about 2,150 (70%) store and process this data mainly abroad, almost all in Esterland; about 950 host it in Corvany (own data centers or local colocation), of which about 600 keep backups abroad; about 400 of the 3,100 are foreign online services with no establishment in Corvany.

Corvany firms buy about 1.1 billion crowns a year of cloud services, nearly all from Esterland. Local colocation: four firms, nine facilities, 60 MW, 85% occupied. Local hosting costs an estimated 25% to 40% more per unit of computing. A provider's local region costs about 400 million crowns and takes 18 to 30 months; providers N and S announced regions in August 2027; T has not decided; dozens of smaller foreign providers have none. Grid connections: below 10 MW about 12 months, above 10 MW three to four years; suitable sites are in two industrial zones. Hosting is 1% to 3% of costs for banks and retailers, 10% to 20% for online services. Migration costs 150,000 to 2 million crowns per firm, done by about 40 consulting firms.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Corvany; Esterland regions 300 km away (about 10 ms round trip) | Policy record |
| Announced / enacted / effective / expires | Introduced 14 October 2026; enacted 1 July 2027; applies from 1 January 2029 (coverage set by records held on any day of the preceding calendar year, so 2028 counts for 2029); no expiry | Policy record; K1 |
| Enforcement (who, penalties, resources) | Data Protection Office; fines up to 4% of turnover; blocking orders against foreign controllers without an establishment after a hearing (never yet used); supplementary appropriation of 6 million crowns a year from the general budget | K4 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Residency | `prohibition` of storing or processing covered data outside Corvany | Personal data of Corvany residents | Each controller holding data on more than 50,000 residents on any day of the preceding year | From 1 January 2029, "stored and processed only on servers located in Corvany"; foreign providers may comply by operating servers there; count per controller, group companies separately | Controllers at or below 50,000 |
| K2 Officer and statement | Compliance requirement | Covered controllers | Covered controllers | Appoint a residency officer; file an annual statement | — |
| K3 Facility certificate | `licensing_requirement` for facilities | Data centers hosting covered data | Facility operators | Annual audit of physical security and access logs; 40,000 crowns per facility a year | — |
| K4 Enforcement | — | — | Data Protection Office | Fines to 4% of turnover; blocking orders for foreign controllers without establishment; 6 million crowns a year from the general budget; fees to the general budget | — |

Unclear provisions:
- **U1, encrypted backups abroad.** Section 4(2) lets a security copy be kept abroad "where the Office so allows by regulation"; no regulation has been issued. U1-a: encrypted backups may be kept abroad. U1-b: until a regulation is issued, every copy must be in Corvany. No probability is given.

**Counterfactual.** No residency requirement: controllers host where they choose (70% of those above the line abroad), no certificate, no officer, no appropriation.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
| --- | --- | --- | --- | --- |
| K1 Residency | triangular (prohibits exchanges between covered controllers and providers hosting abroad) | Yes for controllers that host abroad (A-1), where enforced (A-2); weakly for foreign services without an establishment (A-12) | 1 for covered controllers with an establishment (hosting abroad removed); 3 for foreign controllers without an establishment (risk of a blocking order, CR-1 premises); 3 on the option "hold records on more than 50,000 residents" (the count threshold) | CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10a, CR-12 |
| K2 Officer and statement | triangular (condition on holding covered data) | Yes | 3 (paperwork and staff attached to being covered) | CR-3a, CR-8c |
| K3 Facility certificate | triangular (license for hosting covered data) | Yes for every facility that hosts covered data | 3 on the option "host covered data" (audit and fee, a cost fixed per facility, CR-4 0.8 note) | CR-4, CR-8b, CR-8c |
| K4 Enforcement | binary (appropriation from the general budget) | Yes | 4 (6 million crowns a year to the Office from the general budget's payers); 3 (fines and blocking attach risk to breach) | CR-8b, CR-8c, CR-8 0.7 (payers from the general budget) |

Per reading, K1 performs for the ~600 local hosts with backups abroad: U1-a no operation; U1-b op 1 (backups abroad removed).

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
| --- | --- | --- |
| controllers.covered.abroad | About 2,150 covered controllers hosting mainly abroad (incl. most of the 400 foreign services) | Op 1: hosting abroad removed (where enforced) |
| controllers.covered.local | About 950 already hosting in Corvany | Op 3 (K2); compete for local capacity (CR-9) |
| controllers.covered.local_backups_abroad | About 600 of the 950 | U1-a: none; U1-b: op 1 on backups abroad |
| controllers.covered | All 3,100 | Op 3 (K2) |
| controllers.near_threshold | Controllers around 40,000 to 60,000 records | Op 3 on crossing 50,000 (CR-4, x: covered form, y: uncovered form) |
| controllers.foreign_no_establishment | About 400 foreign online services | Op 3: risk of blocking, weakly enforced (A-12) |
| customers.covered_controllers | Buyers of covered controllers' goods and services | CR-9 (cost changes passed on, CR-5c) |
| users.foreign_services | Corvany users of foreign online services | CR-9 (some services cap or withdraw, A-11) |
| sellers.domestic_substitutes | Domestic shops and apps in the same categories | CR-9 (substitute, A-20) |
| colocation_firms | Four local colocation firms, nine facilities | CR-9 (input_to): more demand; op 3 (K3) |
| small_facilities | Small facilities among the nine and controllers' own data centers | Op 3 (K3), may drop covered data (A-18) |
| providers.building | Providers N and S | CR-4 (x: serve from Esterland, y: build locally) |
| providers.not_building | Provider T (if it does not build) and dozens of smaller providers | CR-9: lose covered customers (A-6) |
| migration_consultants | About 40 consulting firms | CR-9 (input_to): migration demand |
| buyers.other_it_consulting | Firms buying consulting for other projects | CR-9: compete for the same consultants |
| grid_connection_seekers.other | Other firms seeking large connections in the two zones | CR-9: compete for the same connections |
| landowners.industrial_zones | Owners of sites with grid capacity and fiber | CR-9 (input_to) |
| workers.data_centers | Data-center staff in Corvany | CR-9, LW-10 |
| officials.enforcement | Data Protection Office | Op 4 (appropriation), administers K1 to K4 |
| taxpayers, recipients_of_other_spending | General-budget payers | Op 4 (appropriation), receive facility fees (CR-8b) |
| currency_users | Buyers and sellers of crowns against foreign currency | CR-9 (currency) |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | controllers.covered.abroad | quantity_traded (hosting of covered data bought from Esterland regions) | decrease | short (from Jan 2029); medium; long | CR-1 op 1, CR-5a | A-1, A-2 |
| C-2 | controllers.covered | compliance_cost (officer, residency statement) | increase | short; medium; long | CR-1 op 3, CR-8c | none |
| C-3 | controllers.covered.abroad | compliance_cost (migration) | increase | short (2027 to 2029) | CR-1 op 1, CR-4, CR-8c | A-1, A-2 |
| C-4 | facility_operators (hosting covered data) | compliance_cost (audit, certificate fee) | increase | short; medium; long | CR-1 op 3, CR-8c | none |
| C-5 | officials.enforcement | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | none |
| C-6 | state.general_budget | non_tax_receipts (facility fees) | increase | short; medium; long | CR-1 op 3, CR-8b | none |
| C-7 | taxpayers, recipients_of_other_spending | resources_available_other_uses | ambiguous | short; medium; long | CR-8 0.7, CR-8b, CR-12b | A-22 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-8 | controllers.covered.abroad | price_paid (hosting per unit of computing) | increase | short; medium; long | CR-1 op 1, CR-3a, CR-4 | A-1, A-2, A-5 |
| C-9 | controllers.covered.abroad | quality_per_unit (hosting: latency against range of services) | ambiguous | medium; long | CR-12b | A-14, A-15 |
| C-10 | controllers.near_threshold | reclassification (deleting inactive records, splitting records between group controllers) | increase | short (count year 2028); medium | CR-4, CR-10a | A-8, A-9 |
| C-11 | controllers.near_threshold | quantity_supplied (service to Corvany residents beyond 50,000 records) | decrease | medium; long | CR-4c, CR-4 (lumpy costs) | A-10 |
| C-12 | controllers.foreign_no_establishment | quantity_supplied (service to Corvany residents) | decrease | medium | CR-4, CR-7a | A-11 |
| C-13 | controllers.foreign_no_establishment | legal_breach (covered data kept abroad) | increase | medium | CR-4 | A-1, A-12 |
| C-14 | controllers.covered.local_backups_abroad | compliance_cost (moving backups to Corvany) | U1-a: no_change; U1-b: increase | short | CR-1 per reading, CR-8c | A-2 |
| C-15 | controllers.covered (establishment, early 2029) | legal_breach (not yet compliant) | increase | short (first months of 2029) | CR-6, CR-4 | A-2, A-16, A-N2 |
| C-16 | providers.building | investment_target (Corvany regions) | increase | short; medium | CR-4, CR-10a | A-4 |
| C-17 | colocation_firms | investment_target (expansions below 10 MW) | increase | short | CR-4, CR-7a, CR-10a | A-1, A-3 |
| C-18 | small_facilities | quantity_supplied (hosting of covered data) | decrease | medium | CR-4 0.8 note | A-18 |
| C-19 | controllers.covered | asset_value (firms) | decrease | short (from enactment, partly from introduction) | CR-7c, CR-10c | A-1, A-2, A-23 |
| C-20 | controllers.covered | resources_available_other_uses | decrease | medium; long | CR-3 note, CR-8a | A-5, A-23 |
| C-21 | lobbying groups (local operators, building providers, near-threshold controllers, foreign services) | lobbying_effort (on the Act, its threshold and the backup regulation) | increase | short; medium | CR-4, CR-8c | A-13 |

## 6. Second-order effects

CR-9 along named relations. Depth limit 4. Effects on exporters through the currency link stop at the ambiguous exchange rate (a kind 3 chain, CR-12 0.8); effects on customers of firms displaced from grid connections are pruned at depth 3.

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-22 | providers.esterland_regions | quantity_traded (sales to Corvany controllers) | decrease | short; medium; long | CR-9, CR-5a | across_border (close) | A-1, A-2 |
| C-23 | providers.not_building | quantity_traded (sales to covered controllers) | decrease | medium; long | CR-9 | across_border | A-1, A-6 |
| C-24 | controllers.covered.abroad | variety (hosting providers and services available for covered data) | decrease | medium | CR-1 op 1, CR-9 | same_market_other_segment | A-6, A-15 |
| C-25 | colocation_firms | net_price_received (colocation space) | increase | short | CR-9, CR-6, CR-12e, CR-12 0.9 | colocation input_to covered hosting (close) | A-1, A-2, A-16 |
| C-26 | colocation_firms | net_price_received (colocation space) | ambiguous | medium; long | CR-12b | as above; provider regions substitute (close) | A-4, A-17 |
| C-27 | colocation_firms | quantity_traded (space hosted) | increase | short; medium | CR-9, LW-10 | input_to | A-1, A-2, A-3 |
| C-28 | colocation_firms | asset_value | ambiguous | short (from enactment) | CR-7c, CR-10c, CR-12b | input_to; provider regions substitute | A-1, A-4, A-16 |
| C-29 | controllers.covered.local | price_paid (local hosting) | increase | short | CR-9, CR-6 | compete for the same capacity | A-1, A-2, A-16 |
| C-30 | controllers.covered.local | price_paid (local hosting) | ambiguous | medium; long | CR-12b | as above | A-4, A-17 |
| C-31 | customers.covered_controllers | price_paid (+), quantity_traded (−) | at_least_one_as_stated | medium; long | CR-5c, CR-6 0.9 | covered hosting input_to their goods | A-5, A-23 |
| C-32 | users.foreign_services | quantity_traded (use of foreign services that cap or withdraw) | decrease | medium | CR-5a, CR-9 | exchange | A-11 |
| C-33 | users.foreign_services | variety (online services available) | decrease | medium | CR-9 | exchange | A-11 |
| C-34 | sellers.domestic_substitutes | quantity_substitute (domestic online services) | increase | medium | CR-9 | substitute (partial) | A-11, A-20 |
| C-35 | sellers.domestic_substitutes | asset_value (firms) | increase | short (from enactment) | CR-7c, CR-10c | substitute | A-11, A-20 |
| C-36 | migration_consultants | quantity_traded (migration projects) | increase | short (2027 to 2029) | CR-9, LW-10 | consulting input_to migration | A-1, A-2 |
| C-37 | migration_consultants | net_price_received (migration work) | increase | short (2027 to 2029) | CR-9, CR-6 0.9 | input_to | A-1, A-2, A-N1 |
| C-38 | buyers.other_it_consulting | quantity_traded (other consulting projects) | decrease | short (2027 to 2029) | CR-9, CR-4c, CR-8a | compete for the same consultants | A-1, A-2, A-N1 |
| C-39 | grid_connection_seekers.other | wait_time (connections above 10 MW in the two zones) | increase | medium | CR-9, CR-6 | compete for the same connections | A-4, A-17 |
| C-40 | landowners.industrial_zones | asset_value (sites with grid capacity and fiber) | increase | short (from Aug 2027) | CR-9, CR-7c, CR-10c | sites input_to data centers | A-4, A-17 |
| C-41 | workers.data_centers | employment (data-center operation in Corvany) | increase | medium; long | CR-9, LW-10 | labor input_to local hosting | A-3, A-4 |
| C-42 | providers.building | resources_available_other_uses (investment elsewhere) | decrease | short; medium | CR-8a | — | A-4, A-21 |
| C-43 | currency_users | exchange_rate (crowns per unit of foreign currency) | ambiguous | short; medium | CR-9 0.7, CR-12b | currency | A-1, A-4, A-21 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| taxpayers, recipients_of_other_spending, resources | Facility fees paid into the general budget (C-6) | 6 million crowns a year appropriation (A-22) | None: the number of certified facilities (own data centers among the 950) is not in the case's figures, so the arithmetic is not available (CR-12e) | ambiguous (C-7) |
| controllers.covered.abroad, quality_per_unit | Lower latency (A-14) | Fewer services in new regions and colocation (A-15) | None | ambiguous (C-9) |
| controllers.covered.abroad, price_paid | — | — | A-5: local computing costs more per unit; provider entry is a response to the Act and cannot bring the price below the Esterland price it replaces (CR-12e) | increase (C-8) |
| colocation_firms, net_price_received, short | Demand from covered controllers at fixed space (A-16) | — | Response argument (CR-12e) with partial expansion (A-16, CR-12 0.9) | increase (C-25) |
| colocation_firms, net_price_received, medium; long | Demand persists; large capacity cannot be added at the old cost within five years (A-17) | Provider regions compete for colocation's existing customers too (A-4); the response argument does not cover a competitor offering a different product to customers the Act did not move (CR-12 0.8 note) | None | ambiguous (C-26); same for C-28, C-30 |
| currency, exchange_rate | Imports of servers and equipment (A-21) | Fewer cloud imports (C-22); investment financed from abroad (A-21) | None | ambiguous (C-43) |
| controllers.near_threshold | — | — | — | C-10 and C-11 are different variables (CR-12c), not combined |

Not combined (CR-12g): C-25 and C-29 (short, increase) against C-26 and C-30 (medium and long, ambiguous).

## 8. Time structure

- **Introduction to enactment (October 2026 to July 2027).** Expectation of the Act moves the values of covered controllers, colocation firms and sites (CR-7c, CR-10c; C-19, C-28, C-35, C-40) in part as passage becomes likely, the rest at enactment.
- **The count year (2028).** Coverage in 2029 depends on records held on any day of 2028, so controllers near the line delete inactive records or split them between group companies during 2028 (CR-10a; C-10). Each later year repeats the count, so the incentive to stay below the line lasts (C-11).
- **Migration window (July 2027 to January 2029).** Migration work bunches before 1 January 2029: consultants' work and prices rise (C-36, C-37) and other consulting is crowded out (C-38). This is an activity the Act creates (CR-12 0.9): after migrations are done, consulting returns to its counterfactual level; no later decrease is claimed.
- **Capacity.** Provider regions announced in August 2027 take 18 to 30 months, so the earliest opens about February 2029 and the latest about February 2030. Until then local capacity is colocation's 15% free space plus expansions below 10 MW within about a year (A-3, A-16). In early 2029 the pressure goes to colocation prices (C-25, C-29) and to non-compliance by controllers whose provider is not ready (C-15). Connections above 10 MW take three to four years (A-17), so large capacity stays dear well into the medium run, and other firms wait longer for large connections (C-39).
- **Durability.** Regions and facilities are durable stocks (CR-10b); once built they persist whatever happens to the Act, and the providers that built them gain a stake in keeping it (C-21).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-2 | controllers.covered | compliance_cost (officer, statement) | increase | Staff time that would have served other ends | CR-8c |
| C-3 | controllers.covered.abroad | compliance_cost (migration) | increase | 150,000 to 2 million crowns per firm of consulting and staff time | CR-8c |
| C-4 | facility_operators | compliance_cost (audit, fee) | increase | Audit work and 40,000 crowns per facility a year | CR-8c, CR-8b |
| C-5 | officials.enforcement | enforcement_cost | increase | 6 million crowns a year the general budget would have spent elsewhere | CR-8c |
| C-20 | controllers.covered | resources_available_other_uses | decrease | 25% to 40% more per unit of computing, paid by controllers who stay above the line | CR-3 note, CR-8a |
| C-21 | lobbying groups | lobbying_effort | increase | Resources spent lobbying | CR-8c |
| C-32 | users.foreign_services | quantity_traded | decrease | Exchanges with withdrawn services that both sides expected to gain from | CR-5a |
| C-38 | buyers.other_it_consulting | quantity_traded | decrease | Other IT projects delayed or not done | CR-8a |
| C-42 | providers.building | resources_available_other_uses | decrease | About 400 million crowns per region invested elsewhere on the counterfactual path | CR-8a |

Both sides of each transfer: the appropriation (C-5) has payers in the general budget (C-7); facility fees (C-4) are received by the general budget (C-6); higher hosting prices paid (C-8, C-29) are received by local hosts (C-25, C-27). Covered controllers' customers pay part of the higher cost (C-31); how the burden splits between controllers and their customers needs a premise comparing their alternatives (CR-7b), which the case lacks, so no share is signed.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The requirement binds: many covered controllers would host abroad without it. | binding | 0.95 | 70% host abroad now. | Most consequences fail: C-1, C-3, C-8, C-13, C-19, C-22, C-25, C-27, C-29, C-36 to C-38. |
| A-2 | The Office enforces the requirement against controllers with an establishment in Corvany. | enforcement | 0.85 | Fines to 4% of turnover; existing privacy enforcement. | C-1, C-3, C-8, C-14, C-15, C-19, C-22, C-25, C-27, C-29, C-36 to C-38 fail. |
| A-3 | Local capacity can be added at some cost: colocation expansions and connections below 10 MW within about a year. | alternative_uses | 0.8 | Grid lead times; operators' plans. | C-17, C-27, C-41 fail. |
| A-4 | At least one foreign provider builds a local region. | expectations | 0.85 | N and S announced regions in August 2027. | C-16, C-39, C-40, C-41, C-42 fail; C-26, C-28, C-30 become increases. |
| A-5 | Local computing costs more per unit than the Esterland regions. | other | 0.85 | Estimates of 25% to 40%. | C-8, C-20, C-31 fail. |
| A-6 | Some providers that covered controllers used do not build in Corvany. | other | 0.8 | T undecided; dozens of smaller providers. | C-23, C-24 fail. |
| A-7 | On the counterfactual path, covered controllers' backups abroad are encrypted. | other | 0.8 | Industry practice; default settings. | No reported consequence rests on it; it bears only on security effects, which are out of scope. |
| A-8 | For some controllers near 50,000, deleting inactive records or splitting is cheaper than compliance. | other | 0.75 | Inactive users; multi-brand groups. | C-10 fails. |
| A-9 | The Office does not treat a group's controllers as one. | enforcement | 0.6 | The Act counts "each controller". | C-10 loses its splitting branch. |
| A-10 | Compliance cost is material against the gain from growing past 50,000. | binding | 0.8 | Migration of 150,000 to 2 million crowns. | C-11 fails. |
| A-11 | Some foreign online services find Corvany too small for local hosting and cap sign-ups or withdraw. | alternative_uses | 0.7 | 400 foreign services above the line. | C-12, C-32 to C-35 fail. |
| A-12 | Enforcement against foreign services without an establishment is weak. | enforcement | 0.7 | No blocking order ever issued. | C-13 fails. |
| A-13 | Local operators, providers and controllers near the line can organize at a cost below their stake. | other | 0.85 | Their submissions on the bill. | C-21 fails. |
| A-14 | Local hosting cuts latency for Corvany users, which some controllers value. | other | 0.7 | About 10 ms round trips to Esterland. | C-9 becomes decrease. |
| A-15 | New local regions launch with fewer services than Esterland's; colocation offers fewer still. | other | 0.6 | Launch practice for new regions. | C-9 becomes increase; C-24 rests on A-6 only. |
| A-16 | Local colocation cannot add space beyond its 15% free capacity within a year. | durability | 0.8 | 85% occupancy; 12-month connections. | C-15, C-25, C-29 fail. |
| A-17 | Large capacity cannot be added at the old cost within five years. | durability | 0.65 | Three to four years for connections above 10 MW; few sites. | C-39, C-40 fail; C-26, C-30 become decreases or no change. |
| A-18 | For some small facilities, the certificate and audit cost more than the margin on covered data. | other | 0.55 | Small facilities among the nine. | C-18 fails. |
| A-19 | Hosting is a material part of the cost of online services. | other | 0.75 | 10% to 20% of costs. | Used as support for C-12 and C-31; neither rests on it alone. |
| A-20 | Domestic services that host locally are substitutes for some withdrawn foreign services. | substitutability | 0.7 | Domestic shops and apps in the same categories. | C-34, C-35 fail. |
| A-21 | Providers' investment is financed from abroad, and servers and equipment are imported. | other | 0.8 | Providers' practice; no server manufacturing in Corvany. | C-42 fails; C-43 loses two chains. |
| A-22 | The appropriation is paid from the general budget, with no named tax. | revenue_use | 0.9 | K4. | C-7's payer group changes. |
| A-23 | Some controllers above the threshold keep paying higher costs rather than drop below it. | other | 0.9 | 2,000 controllers above 100,000 records. | C-19, C-20, C-31 fail. |
| A-24 | Covered controllers move other operations (staff, offices) to Corvany with their data. | other | 0.2 | Data can be hosted locally without moving staff. | Below the cut-off: see Not reported. |
| A-N1 | Migration consulting capacity (about 40 firms) cannot expand fully at the old cost before January 2029. | durability | 0.7 | NEW. About 2,150 migrations within 18 months; consultants' skills take time to acquire. | C-37, C-38 fail. |
| A-N2 | Some covered controllers with an establishment are not compliant on 1 January 2029 because their provider's local region is not open and colocation space is short. | other | 0.6 | NEW. Regions announced August 2027 take 18 to 30 months (earliest about February 2029); colocation has 15% free (A-16); T undecided. | C-15 fails. |
| A-N3 | For some foreign controllers with an establishment in Corvany, closing the establishment and serving Corvany from abroad (where enforcement is weak, A-12) costs less than compliance. | other | 0.35 | NEW. Establishments of foreign firms are often sales offices; against it, fines to 4% of turnover while the establishment exists, and the cost of closing it. | Below the cut-off: see Not reported. |

**Not reported** (an assumption below 0.5):
- Covered controllers moving staff and offices to Corvany, raising local employment and office demand (CR-9): needs A-24 (p 0.2).
- Foreign controllers with an establishment closing it to serve Corvany from abroad, where enforcement is weak (CR-4, x: keep the establishment, y: close it): needs A-N3 (p 0.35).
- Blocking orders against foreign services and their effect on internet providers: A-12 (weak enforcement, p 0.7) makes the negation unlikely.

## 11. Report

**The policy:** From 1 January 2029 every controller holding personal data on more than 50,000 Corvany residents (in any day of the previous year) must store and process that data only on servers in Corvany. Covered controllers must appoint an officer and file a statement; data centers hosting covered data need a certificate (audit and a 40,000-crown fee). The Data Protection Office enforces with fines and, for foreign services without an establishment, blocking orders, and receives 6 million crowns a year from the general budget. Whether encrypted backups may stay abroad is unclear (U1).

**Visible consequences:** About 2,150 covered controllers stop buying Esterland hosting for covered data (C-1) and pay to migrate (C-3) and more per unit of computing (C-8). All covered controllers bear officer and statement costs (C-2); facilities pay for certificates (C-4); the Office spends its appropriation (C-5) and the general budget collects facility fees (C-6). Providers N and S build local regions (C-16).

**Invisible consequences:**
- *Covered controllers:* firm values fall from enactment (C-19); controllers that stay above the line have less for other uses (C-20); fewer providers and services are available for covered data (C-24). Under U1-b, those with backups abroad must also move them (C-14). Some are not compliant in early 2029 for lack of capacity (C-15).
- *Controllers near the line:* they delete records or split them (C-10) and hold back growth past 50,000 (C-11).
- *Foreign services and their users:* some cap sign-ups or withdraw (C-12), so users lose services and choice (C-32, C-33), and domestic substitutes gain users and value (C-34, C-35); others ignore the rule (C-13).
- *Local hosts and inputs:* colocation firms earn more and host more in the short run (C-25, C-27) and expand (C-17), as do landowners with suitable sites (C-40); already-local controllers pay more for space in the short run (C-29). Some small facilities drop covered data (C-18). Data-center employment rises (C-41). Other firms wait longer for large grid connections (C-39).
- *Consultants:* migration work and prices rise before 2029 (C-36, C-37), and other IT projects are crowded out (C-38).
- *Abroad:* Esterland regions and providers that do not build lose Corvany sales (C-22, C-23); building providers give up investment elsewhere (C-42).
- *Customers of covered controllers:* pay more or buy less (C-31).
- *Politics:* local operators, building providers, near-threshold controllers and foreign services lobby over the Act, its threshold and the backup regulation (C-21).

**Ambiguous effects:** Hosting quality for covered controllers (C-9): lower latency against fewer services. Colocation prices, values and already-local controllers' prices after provider regions open (C-26, C-28, C-30): demand that large capacity cannot meet quickly against competition from the new regions. General-budget payers (C-7): the appropriation against facility fees. The exchange rate (C-43): fewer cloud imports and inflows for investment against imported equipment.

**Key conditions:** The requirement binds and is enforced on firms with an establishment (A-1, 0.95; A-2, 0.85); local computing costs more (A-5, 0.85); providers build (A-4, 0.85) but not all (A-6, 0.8); colocation cannot expand quickly (A-16, 0.8) and large capacity cannot be added cheaply within five years (A-17, 0.65); foreign services without an establishment face weak enforcement (A-12, 0.7). Added premises: consulting capacity is limited before 2029 (A-N1, 0.7) and some controllers miss the date for lack of capacity (A-N2, 0.6). The reading of U1 decides whether ~600 local hosts must move their backups.

**What this analysis cannot say:** Sizes; whether the requirement's gains to local hosts and domestic substitutes outweigh the costs to controllers, their customers and users; net welfare. Privacy and security effects (whether data are safer in Corvany, the effect of moving encrypted backups home under U1-b) are out of scope for version 1.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | controllers.covered.abroad | quantity_traded (hosting of covered data bought from Esterland regions) | decrease | short (from Jan 2029); medium; long | visible | B | CR-1 (op 1: hosting abroad removed for covered data, where enforced, A-2); CR-5a (exchanges that would have taken place, A-1, are prevented; both sides lose an expected gain) | A-1, A-2 |
| C-2 | controllers.covered | compliance_cost (officer, residency statement) | increase | short; medium; long | visible | A | CR-1 (op 3: K2 attaches an officer and an annual statement to being covered); CR-8c (resources spent complying are used up) | none |
| C-3 | controllers.covered.abroad | compliance_cost (migration) | increase | short (2027 to 2029) | visible | B | CR-1 (op 1); CR-4 (x: migrate, y: breach; enforcement, A-2, makes y worse); CR-8c (consulting and staff time used up) | A-1, A-2 |
| C-4 | facility_operators (hosting covered data) | compliance_cost (audit, certificate fee) | increase | short; medium; long | visible | A | CR-1 (op 3: K3 attaches an audit and a 40,000-crown fee to hosting covered data); CR-8c | none |
| C-5 | officials.enforcement | enforcement_cost | increase | short; medium; long | visible | A | CR-1 (op 4: 6 million crowns a year to the Office); CR-8c | none |
| C-6 | state.general_budget | non_tax_receipts (facility fees) | increase | short; medium; long | visible | A | CR-1 (op 3: K3 fee); CR-8b (the budget receives what facilities pay) | none |
| C-7 | taxpayers, recipients_of_other_spending | resources_available_other_uses | ambiguous | short; medium; long | invisible | B | CR-8 0.7 (payers from the general budget: the appropriation is paid by a group, at least one of which loses, A-22); CR-8b (facility fees, C-6, accrue to the same budget); CR-12b with no arithmetic available on the number of certified facilities | A-22 |
| C-8 | controllers.covered.abroad | price_paid (hosting per unit of computing) | increase | short; medium; long | visible | B | CR-1 (op 1 removes the cheaper option); CR-3a and CR-4 (they fall back to the next-best, local hosting, which costs more per unit, A-5); CR-12e (provider regions are a response to the Act and cannot bring the price below the Esterland price it replaced) | A-1, A-2, A-5 |
| C-9 | controllers.covered.abroad | quality_per_unit (hosting: latency against range of services) | ambiguous | medium; long | invisible | B | CR-12b: (+) shorter round trips that some controllers value (A-14); (−) new regions and colocation offer fewer services (A-15) | A-14, A-15 |
| C-10 | controllers.near_threshold | reclassification (deleting inactive records, splitting records between group controllers) | increase | short (count year 2028); medium | invisible | B | CR-4 (x: the covered form, above 50,000 records in one controller; y: the uncovered form; y made better by the cost of coverage, A-8; splitting works because the count is per controller, A-9); CR-10a (the 2028 count decides 2029 coverage) | A-8, A-9 |
| C-11 | controllers.near_threshold | quantity_supplied (service to Corvany residents beyond 50,000 records) | decrease | medium; long | invisible | B | CR-4c with CR-4's note on lumpy costs (the record that crosses 50,000 carries the whole cost of compliance, which is material, A-10, so growth past the line is given up by those for whom it was narrowly worth it) | A-10 |
| C-12 | controllers.foreign_no_establishment | quantity_supplied (service to Corvany residents) | decrease | medium | invisible | B | CR-4 (x: serve Corvany and host locally, y: cap sign-ups or withdraw; Corvany too small to justify local hosting for some, A-11); CR-7a (their means move to other markets) | A-11 |
| C-13 | controllers.foreign_no_establishment | legal_breach (covered data kept abroad) | increase | medium | invisible | B | CR-1 premises (an unenforced prohibition attaches a risk); CR-4 (x: comply, y: violate; weak enforcement, A-12, keeps y ranked first for some); against the counterfactual, no rule exists to breach, so any breach is an increase (CR-12 0.9) | A-1, A-12 |
| C-14 | controllers.covered.local_backups_abroad | compliance_cost (moving backups to Corvany) | U1-a: no_change; U1-b: increase | short | invisible | B | CR-1 per reading: U1-a no operation on backups; U1-b op 1 (backups abroad removed until a regulation); CR-8c | A-2 |
| C-15 | controllers.covered (establishment, early 2029) | legal_breach (not yet compliant) | increase | short (first months of 2029) | invisible | B | CR-6 (local capacity fixed in the short run, A-16, while regions open from about February 2029: pressure goes to colocation prices and to breach); CR-4 (x: pay the colocation price or wait, y: stay abroad past the date; some choose y, A-N2) | A-2, A-16, A-N2 |
| C-16 | providers.building | investment_target (Corvany regions) | increase | short; medium | visible | B | CR-4 (x: serve from Esterland, now closed for covered data; y: build locally); CR-10a (announced in August 2027 for the 2029 date) | A-4 |
| C-17 | colocation_firms | investment_target (expansions below 10 MW) | increase | short | invisible | B | CR-4 (x: keep capacity, y: expand); CR-7a (means move toward the higher yield, C-25); CR-10a | A-1, A-3 |
| C-18 | small_facilities | quantity_supplied (hosting of covered data) | decrease | medium | invisible | B | CR-1 (op 3: K3); CR-4 0.8 note (a cost fixed per facility bears on whether the facility offers covered hosting: x: host covered data, y: drop it; reversed for some, A-18) | A-18 |
| C-19 | controllers.covered | asset_value (firms) | decrease | short (from enactment, partly from introduction) | invisible | B | CR-7c and CR-10c (the expected fall in net yield from higher costs, C-2, C-3, C-8, is borne by owners when the Act becomes expected, in part as passage became likely); A-23 (the costs are kept, not escaped) | A-1, A-2, A-23 |
| C-20 | controllers.covered | resources_available_other_uses | decrease | medium; long | invisible | B | CR-3 note (they keep paying the burdened option, A-23); CR-8a (the extra 25% to 40% per unit, A-5, is withdrawn from other uses) | A-5, A-23 |
| C-21 | lobbying groups (local operators, building providers, near-threshold controllers, foreign services) | lobbying_effort (on the Act, its threshold and the backup regulation) | increase | short; medium | invisible | B | CR-4 (x: accept, y: lobby; local hosts and building providers to keep or tighten, near-threshold controllers to raise the line, foreign services and controllers with backups abroad to relax it or obtain a U1 regulation, A-13); against a counterfactual of no Act, any lobbying on it is an increase (CR-12 0.9); CR-8c | A-13 |
| C-22 | providers.esterland_regions | quantity_traded (sales to Corvany controllers) | decrease | short; medium; long | invisible | B | CR-9 (relation: across_border; the seller's side of C-1); CR-5a | A-1, A-2 |
| C-23 | providers.not_building | quantity_traded (sales to covered controllers) | decrease | medium; long | invisible | B | CR-9 (across_border; customers must move to a provider with local servers, and these do not build, A-6) | A-1, A-6 |
| C-24 | controllers.covered.abroad | variety (hosting providers and services available for covered data) | decrease | medium | invisible | B | CR-1 (op 1 removes every provider without local servers); CR-9 (providers that do not build, A-6, and fewer services in new regions, A-15) | A-6, A-15 |
| C-25 | colocation_firms | net_price_received (colocation space) | increase | short | invisible | B | CR-9 and LW-10 (relation: colocation input_to covered hosting; more buyers); CR-6 (space fixed beyond 15% free, A-16); CR-12e and CR-12 0.9 (expansion is a response and cannot reverse the rise, and it is partial within the year, A-16) | A-1, A-2, A-16 |
| C-26 | colocation_firms | net_price_received (colocation space) | ambiguous | medium; long | invisible | B | CR-12b: (+) covered demand persists and large capacity cannot be added at the old cost within five years (A-17); (−) CR-9 (relation: provider regions substitute for colocation, A-4) for colocation's existing customers too, a change the response argument does not cover (CR-12 0.8 note) | A-4, A-17 |
| C-27 | colocation_firms | quantity_traded (space hosted) | increase | short; medium | invisible | B | CR-9 and LW-10 (input_to; filled free space and expansions, A-3) | A-1, A-2, A-3 |
| C-28 | colocation_firms | asset_value | ambiguous | short (from enactment) | invisible | B | CR-7c and CR-10c (value reflects the expected yield path: C-25's rise, then C-26's ambiguous medium run; provider regions, A-4, compete; K3 costs); CR-12b | A-1, A-4, A-16 |
| C-29 | controllers.covered.local | price_paid (local hosting) | increase | short | invisible | B | CR-9 (they compete for the same local capacity as migrating controllers); CR-6 (fixed space, A-16) | A-1, A-2, A-16 |
| C-30 | controllers.covered.local | price_paid (local hosting) | ambiguous | medium; long | invisible | B | CR-12b: (+) A-17 as in C-26; (−) provider regions add a local option they did not have (A-4) | A-4, A-17 |
| C-31 | customers.covered_controllers | price_paid (+), quantity_traded (−) | at_least_one_as_stated | medium; long | invisible | B | CR-9 (relation: covered hosting input_to their goods; costs rise, A-5, for controllers that stay covered, A-23); CR-5c (the range of acceptable terms moves); CR-6 0.9 (without a premise on supply response, price and quantity are recorded as a group) | A-5, A-23 |
| C-32 | users.foreign_services | quantity_traded (use of foreign services that cap or withdraw) | decrease | medium | invisible | B | CR-9 (exchange with the services in C-12); CR-5a (exchanges both sides expected to gain from no longer take place) | A-11 |
| C-33 | users.foreign_services | variety (online services available) | decrease | medium | invisible | B | CR-9 (follows C-12, A-11) | A-11 |
| C-34 | sellers.domestic_substitutes | quantity_substitute (domestic online services) | increase | medium | invisible | B | CR-9 (relation: substitute, A-20; users of withdrawn services move to domestic ones, CR-4) | A-11, A-20 |
| C-35 | sellers.domestic_substitutes | asset_value (firms) | increase | short (from enactment) | invisible | B | CR-7c and CR-10c (the expected gain in C-34 is captured by owners when it becomes expected) | A-11, A-20 |
| C-36 | migration_consultants | quantity_traded (migration projects) | increase | short (2027 to 2029) | invisible | B | CR-9 and LW-10 (relation: consulting input_to migration, C-3); CR-12 0.9 (an activity the Act creates, signed on the flow in the window) | A-1, A-2 |
| C-37 | migration_consultants | net_price_received (migration work) | increase | short (2027 to 2029) | invisible | B | CR-9; CR-6 0.9 (the split goes partly to price because capacity cannot expand fully before the date, A-N1) | A-1, A-2, A-N1 |
| C-38 | buyers.other_it_consulting | quantity_traded (other consulting projects) | decrease | short (2027 to 2029) | invisible | B | CR-9 (they compete for the same consultants); CR-4c (at a higher price the marginal project is given up); CR-8a | A-1, A-2, A-N1 |
| C-39 | grid_connection_seekers.other | wait_time (connections above 10 MW in the two zones) | increase | medium | invisible | B | CR-9 (provider regions, A-4, compete for the same large connections); CR-6 (connections cannot be added at the old rate within years, A-17; the queue lengthens) | A-4, A-17 |
| C-40 | landowners.industrial_zones | asset_value (sites with grid capacity and fiber) | increase | short (from Aug 2027) | invisible | B | CR-9 and LW-10 (sites input_to data centers); CR-7c and CR-10c (few sites, A-17, so the rise is captured by owners when region plans become expected) | A-4, A-17 |
| C-41 | workers.data_centers | employment (data-center operation in Corvany) | increase | medium; long | invisible | B | CR-9 and LW-10 (labor input_to local hosting; capacity added, A-3, A-4) | A-3, A-4 |
| C-42 | providers.building | resources_available_other_uses (investment elsewhere) | decrease | short; medium | invisible | B | CR-8a (about 400 million crowns per region, financed from abroad, A-21, is withdrawn from the investments the providers would otherwise have made) | A-4, A-21 |
| C-43 | currency_users | exchange_rate (crowns per unit of foreign currency) | ambiguous | short; medium | invisible | B | CR-9 0.7 (currency link both ways): (−) fewer crowns offered for cloud imports (C-22) and foreign currency brought in to finance regions (A-21); (+) crowns offered for imported servers and equipment (A-21); CR-12b. Effects on exporters stop here (kind 3 chain) | A-1, A-4, A-21 |

## Gaps found

**(a) Calculus gaps.**
- GAP-053-C1: Thresholds that depend on a count over a past period. CR-4 with lumpy costs gives the direction of bunching below 50,000 (C-10, C-11), and CR-10a gives the timing, but no rule says how to treat a threshold computed on "any day of the preceding year", which makes one peak day decisive. The derivation used CR-4 and CR-10a together without a rule for the look-back.
- GAP-053-C2: Security and privacy effects (A-7, U1-b) are the stated purpose of the Act but have no variable; the method can only say they are out of scope.

**(b) Core-rule wording that was hard to apply.**
- CR-12e response argument and new entrants that compete with incumbents for customers the policy did not move (provider regions against colocation's existing customers). The 0.8 note excludes "a second change the policy also causes"; whether the arrival of a new competitor counts as a second change or as part of the response was a judgment, and it decided C-26, C-28 and C-30.
- CR-8 0.7 (payers from the general budget) for a budget that both pays (the appropriation) and receives (fees): the note covers only payers; combining it with receipts gave an ambiguous group sign that says little.
- CR-1 for foreign controllers without an establishment: whether the prohibition removes an option (op 1) or only attaches a risk (op 3) depends on enforcement; the recording note covers this, but the blocking order acts on third parties (internet providers), whose operation is not stated.
- CR-9 0.7 currency link: with foreign-owned local regions, payments for hosting become domestic payments to foreign-owned firms whose profits are later remitted; the rule names imports and exports but not remitted earnings.

**(c) Vocabulary missing from the ontology.**
- No variable for latency or other service attributes of hosting; `quality_per_unit` was used for a bundle that moves in two directions (C-9).
- No variable for the location of processing or storage (share of data hosted at home); C-1 uses `quantity_traded` from the foreign seller.
- No actor class for groups of related controllers counted separately; `controllers.near_threshold` covers both deleting and splitting.
- No variable for capacity queues at an infrastructure provider other than `wait_time` (grid connections).

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of data localization. Covered controllers stop buying Esterland hosting for covered data, pay to migrate, bear the officer's and statement's costs, and pay more per unit of computing. Their hosting quality is `ambiguous` (latency against range of services). Fewer providers serve them. Controllers near the line delete or split records in 2028 and bunch below it. Some foreign services cap or withdraw, and others breach where enforcement cannot reach them. Colocation prices rise in the short run, sites with grid capacity gain value, and migration work rises in the window. Customers of covered controllers pay more or buy less, lobbying rises, and the currency chain is `ambiguous`. Both versions use the same 24 premises with the same probabilities. The differences are of three kinds. (1) The medium run for local colocation (pattern C-18, C-19 and C-21 against core C-26, C-28 and C-30). The pattern version uses CR-12e's response argument, treating the providers' local regions as new supply drawn by the price. The core version counts the regions as a second change that also competes for colocation's existing customers, and finds the medium run `ambiguous`. Each reading needs a premise the other does not state, so this is a judgment call. (2) The general budget. The pattern version signs its payers down (C-32) and leaves out the certificate fees and fines it records itself going into the same budget. The core version is right that the group's sign is `ambiguous`. (3) Coverage. Only the core version has the users' lost exchanges, the domestic rivals' value, operating jobs, the providers' investment withdrawn from elsewhere, the consultants' price and the projects it crowds out, grid queues, and breaches in early 2029. Only the pattern version has firms just below the line, backup storage abroad, equipment imports and construction jobs. The one pattern that failed as written, RS-16's 0.9 clause, was overridden by the pattern version itself, and the core version confirms the override.

Counts: M 16, V 10, S 5, OP 9, OC 4.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-2, C-3 | V | | Split into the officer and statement (C-2, Tier A, all covered controllers) and migration (C-3, those hosting abroad). |
| C-2 | C-27 | V | | Local capacity hosting covered data, recorded as `quantity_traded` of colocation space. |
| C-3 | C-16 | M | | |
| C-4 | C-8 | M | | The core version adds the response argument (provider regions cannot bring the price below the Esterland price it replaced). |
| C-5 | C-24 | V | | `number_of_sellers` against `variety` (providers and services). |
| C-6 | C-1, C-22, C-23 | V | | The same prevented exchanges, recorded on the buyers' side (C-1) and on the sellers' side, split into Esterland regions (C-22) and providers that do not build (C-23). |
| C-7 | none | OC | E | Backup storage abroad: U1-a `no_change`, U1-b decrease. CR-1 per reading gives it directly. The core version left it out. The core version's A-7 note ("no reported consequence rests on it") is also wrong: its own C-14 under U1-a is `no_change` only if the counterfactual backups are already encrypted. Otherwise U1-a requires encryption, which is a cost. |
| C-8 | C-14 | M | | The core version should cite A-7 (see C-7). |
| C-9 | C-10 | M | | |
| C-10 | C-11 | V | | Bunching recorded as more controllers just below the line, against service beyond 50,000 records given up. Both rest on A-10. |
| C-11 | none | OC | E | Controllers just below the line: `asset_value` is `ambiguous`. CR-7c lowers the value of the option to grow, and CR-9 adds the gain from the burden on rivals above the line. The pattern version applied RS-17's 0.9 clause, and the core rules give the same result. The core version left it out. |
| C-12 | C-12 | M | | |
| C-13 | C-13 | M | | |
| C-14 | C-21 | M | | |
| C-15 | C-36 | M | | |
| C-16 | C-9 | M | | |
| C-17 | C-25, C-29 | V | | The short-run rise in colocation prices, recorded on both sides: sellers' net price (C-25) and the price already-local controllers pay (C-29). |
| C-18 | C-26, C-30 | S | J | Medium-run colocation price: pattern increase, core `ambiguous`. The pattern version treats provider regions as supply drawn by the price, so CR-12e with A-17 gives an increase. The core version notes that a local region is also a new option for latency-sensitive customers who were already hosting locally, customers the Act did not move. CR-12e's 0.8 note excludes such a second change from the response argument. Each sign needs a premise its version does not state: the pattern version, that the shifted demand dominates; the core version, that some existing colocation customers prefer a local region (it cites only A-4). Both are defensible. The 6.2g failure noted for CR-12e's 0.9 clause points the same way: the argument is fragile when the supply response is a different product. |
| C-19 | C-25, C-26 | S | J | Short run: both increase. Medium run: as C-18. |
| C-20 | C-18 | S | E | Pattern: the number of facilities hosting covered data is `ambiguous`, because the demand shift draws facilities in while the certificate drives some out (A-18). Core: small facilities' hosting of covered data decreases. The core version's class also gains from the demand shift and from the higher price (C-25), a kind 2 chain it left out. Without a premise splitting the class by response, the sign is `ambiguous`. The error is in the core version. |
| C-21 | C-28 | S | J | Operators' value: pattern increase (the certificate is small against facility revenue, by arithmetic), core `ambiguous`. The value follows the expected yield path, so it inherits the medium-run disagreement in C-18. |
| C-22 | C-17 | V | | New data centers entering, against incumbent colocation firms expanding below 10 MW. Same chain, CR-4 with A-3. |
| C-23 | C-40 | M | | |
| C-24 | none | OC | E | Imports of servers and network equipment increase (CR-9, A-21). The core version uses this as a chain in C-43 but does not record it. Core omission. |
| C-25 | none | OC | E | Employment in building data centers increases. The core version records operating jobs (C-41) but not construction. Core omission. |
| C-26 | C-31 | M | | The pattern version limits the claim to online services (A-19). The core version covers all customers of covered controllers, with A-5 and A-23. The group sign holds for both. Only the per-unit cost passes into prices (CR-4 0.8), and both versions say so. |
| C-27 | C-33 | M | | |
| C-28 | C-34, C-35 | V | | Pattern: a group (sales or prices of domestic rivals, at least one increase). Core: `quantity_substitute` increase signed alone, which under CR-6's 0.9 clause needs a premise on their supply, so the group is the safer form. The core version adds their value (C-35, below). |
| C-29 | C-43 | V | | The pattern version signs exporters `ambiguous` (TX-8 0.9, extended). The core version stops at an `ambiguous` exchange rate (CR-9 0.7). Same kind 3 chain. |
| C-30 | C-22 | V | | Pattern: a group of quantity and price for Esterland data centers. Core: quantity sold to covered controllers, which falls directly by CR-1 operation 1, so no split premise is needed. |
| C-31 | C-5 | M | | |
| C-32 | C-7 | S | E | Pattern: general-budget payers `at_least_one_decrease`. Core: `ambiguous`. K4 sends certificate fees (and fines, pattern C-33) to the same general budget that funds the 6 million crowns. By CR-8b and CR-8d the group both pays and receives, and the number of certified facilities is not in the case's figures, so CR-12b gives `ambiguous`. The pattern version applied OC-1's and OC-3's "who pays" clauses without the receipts it recorded itself. The analyst erred, though the wording of those clauses invites it (Findings). |
| C-33 | C-6 | M | | The core version leaves out fines. Fines need breach by controllers that have an establishment, and its own C-15 supplies that. |
| C-34 | C-20 | M | | Both rest on A-23. The fixed costs, which are not passed into unit prices (CR-4 0.8), are enough for the sign even if the per-unit cost is passed on. |
| C-35 | C-4 | M | | Tier A in the core version, B in the pattern version (premise A-1). |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-15 | OP | A | Controllers with an establishment that are not yet compliant in early 2029 (`legal_breach` increase). It rests on a new premise (A-N2: regions open from about February 2029, and colocation has 15% free). The pattern version's section 8 notes the timing but signs nothing. |
| C-19 | OP | E | Covered controllers' `asset_value` decreases. Valid for most of the class, but the class includes domestic online services that host locally. These gain users from withdrawn foreign rivals (the core version's own C-34 and C-35), an opposing chain. The class should be split (CR-1 recording) or the sign qualified. Core error. |
| C-32 | OP | E | Users of foreign services that cap or withdraw lose those exchanges (CR-5a). Valid. The pattern version records only `variety`. Pattern omission. |
| C-35 | OP | E | Domestic substitutes' value increases from enactment (CR-7c, CR-10c, A-20). Valid. Pattern omission. |
| C-37 | OP | A | Migration consultants' price increases. It needs a capacity premise (A-N1, new). |
| C-38 | OP | A | Other IT projects are crowded out by migrations (A-N1). |
| C-39 | OP | J | Other firms wait longer for large grid connections. The pattern version stopped it at depth 3 as diffuse. The connections are few and in two zones, so the core version's choice is the better one, but this is a matter of depth. |
| C-41 | OP | E | Data-center operating jobs in Corvany increase (CR-9 with LW-10, A-3, A-4). Valid. Pattern omission. |
| C-42 | OP | E | Building providers use about 400 million crowns per region that they would have invested elsewhere (CR-8a). Valid. Pattern omission. |

### Findings

- **Pattern overclaims or hidden premises.** RS-16's 0.9 clause, applied as written to a cost fixed per facility, would have made operators' net price `ambiguous`. The pattern version overrode it, and the core version confirms the override: CR-4's 0.8 note gives no per-unit chain, so C-25 is an increase. OC-1's and OC-3's "who pays" clauses give `at_least_one_decrease` for general-budget payers and say nothing of fees paid into the same budget. Read alone, they invite the error in pattern C-32. TX-8's 0.9 clause covers this case only when extended, as the pattern version said. No other pattern applied as written gave a sign the core rules do not.
- **Errors in the pattern version.** (1) C-32 should be `ambiguous` (the fees and fines go to the paying budget). (2) C-18, C-19 (medium run) and C-21 need a stated premise that the shifted demand dominates the regions' competition for colocation's existing customers, or else `ambiguous`. As written they rest on reading the regions as a response to the price, which CR-12e's 0.8 note puts in doubt. (3) Omissions: users' lost exchanges (core C-32), domestic rivals' value (C-35), operating jobs (C-41) and providers' investment withdrawn from elsewhere (C-42).
- **Errors in the core version.** (1) C-18 signs a decrease for a class that also gains from the demand shift (pattern C-20 is right). (2) C-19's class includes domestic services that gain from rivals' withdrawal. (3) A-7 is said to bear on nothing reported, but C-14's U1-a `no_change` rests on it. (4) C-34 signs one CR-6 margin with no premise. (5) Omissions: firms just below the line (pattern C-11), backup storage abroad (C-7), equipment imports (C-24) and construction jobs (C-25).
- **Test of 0.9 (the pattern version's verdicts).** *RS-16 0.9 (failed):* confirmed. *TX-8 0.9 (needed interpretation):* confirmed. The core version reached the same kind 3 result from CR-9's 0.7 currency clause without the pattern, and found that clause silent on earnings that local subsidiaries remit abroad. So the extension is needed in both layers. *CR-6 0.9 with CR-12e over two horizons (needed CR-12e in the medium run):* contradicted on the result, not on the need. The core version's reading of CR-12e's 0.8 note makes the medium run `ambiguous`, so the pattern version's verdict that the response argument "worked as written" for C-18 depends on a premise it did not state. *CR-4 0.8 against RS-16 0.9 (conflict):* confirmed. The conflict is in RS-16, not in CR-4.
- **Candidate "tariff-like burden without a tax" (6.2e list; first use WE-040).** The pattern version calls this a second valid use. The signs are taken against the right counterfactual (Corvany without the Act), and the parts that hold match the core version: buyers pay more (C-8), foreign sellers lose sales (C-22), domestic substitutes gain in the short run (C-25), and nothing is collected. But the move is not the same as WE-040's. WE-040 attached a cost per unit to an imported input. Here an option is removed, with a fixed-cost route around it for foreign suppliers that invest locally. That route turns the foreign suppliers into domestic rivals of the protected sellers, so the candidate's "protected sellers gain" holds only in the short run (core C-26 and C-28 `ambiguous`). The pattern version itself says the candidate would need widening to cover this. This use does not support promoting the candidate as stated. At most it supports a separate candidate: a location requirement with a route around it for suppliers who invest locally.
- **Limits of the core rules.** None produced a difference (K = 0). GAP-053-C1, the look-back threshold, is derived by CR-4 with CR-10a, as the core version itself did. GAP-053-C2, security and privacy, is a matter of scope. Neither is a missing step. The following wording caused trouble:
  - CR-12e's 0.8 note does not say whether a new competitor's entry is part of the response or a second change. The answer decided C-18 to C-21 and core C-26 to C-30.
  - CR-8's 0.7 clause on payers from the general budget does not mention receipts into the same budget.
  - CR-9's 0.7 currency clause does not mention earnings remitted abroad.
  - CR-1 does not say what operation a blocking order performs on internet providers.
