# WE-040 / Analysis: Country-of-origin labeling for meat

Analyst: core-only re-run (Handbook 0.8)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Brennmark Meat Origin Labeling Act.** Brennmark (about 9.4 million people, own currency) slaughters about 1.5 million cattle and 6 million pigs a year. About 21% of the cattle (about 315,000 head) are born in neighboring Quorra, imported as feeder calves (about $900 each), finished in Brennmark for six to nine months and slaughtered there; another 3% come from Quorra for immediate slaughter. About 18% of the pigs (about 1.08 million) are Quorra-born weaners. Six of fourteen large processors, all within 60 km of the Quorra border, take about 80% of the Quorra-born cattle; the other eight take almost only Brennmark-born animals. About 12% of beef eaten is imported boxed beef, mostly from Ardova. Retail meat: three supermarket chains (about 2,100 outlets, about 70% of retail meat, most with a service counter) and about 1,800 independent butchers; about 1,300 butchers have turnover under $1.0 million (about 9% of retail meat) and about 160 have turnover between $0.8 and $1.2 million. About 35% of meat is eaten through food service. Survey (2025): 64% of shoppers believe "Product of Brennmark" means Brennmark-born; 41% would pay more for fully domestic meat; 3% prefer Quorra-born. Impact assessment: tracing and segregation about $9 per head of cattle and $1.50 per pig at plants handling both origins, about $1.20 per head at plants handling only Brennmark-born animals, $0.4 to $0.9 million one-time per plant, about $6,000 set-up and $3,500 a year per outlet with a service counter, and a template, shelf tag and inventory line per origin version of each cut.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Brennmark. Quorra lies across the border, within 60 km of six large processors; Ardova supplies boxed beef. | "Six of Brennmark's fourteen large processors, all within 60 km of the Quorra border" |
| Announced / enacted / effective / expires | Introduced 2 March 2026 (with the cow-calf producers' support); passed 18 June 2026; signed 1 July 2026. K2 and K3 from 1 January 2027; K1 from 1 July 2027; no expiry. | "The bill was introduced on 2 March 2026 ... signed on 1 July 2026. It has no expiry." |
| Enforcement (who, penalties, resources) | Food Standards Agency: record audits at plants, importers and retailers; fines up to $2,000 per mislabeled lot and up to $50,000 for falsified records; $5.2 million a year new appropriation from the general fund for 40 inspectors. | K6 |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Retail label | `disclosure_mandate` | Fresh, chilled and frozen muscle cuts and ground beef, pork and lamb sold at retail | Retailers | From 1 July 2027, each package or counter item states countries of birth, raising and slaughter: "Brennmark", "Product of X", or "Mixed origin" with each stage listed; mixed packages list every category | K4; poultry; processed meat; food service |
| K2 Processor records | Record-keeping requirement, part of K1 | Every animal slaughtered | Slaughterhouses and cutting plants | From 1 January 2027, records of each animal's origin carried to every lot, with written declarations to buyers; kept two years | None |
| K3 Importer records | Record-keeping requirement, part of K1 | Live cattle, pigs and sheep imported | Importers of live animals | From 1 January 2027, certificates per animal (cattle) or per lot (pigs), passed to the buyer | None |
| K4 Small retailers | Exemption from K1 | Retailers | - | Turnover under $1.0 million in the previous July-June year, per registered entity; first measuring year July 2026 to June 2027; not indexed; voluntary labeling allowed in the K1 form | - |
| K5 Transition | Exemption from K1 | Frozen meat | Retailers | Frozen meat from animals slaughtered before 1 January 2027 may be sold unlabeled until 30 June 2028 | - |
| K6 Enforcement | Enforcement | K1 to K3 | FSA | Audits, fines, $5.2 million a year from the general fund | - |

Existing rules, in force in the counterfactual too: R1 (imported meat labeled with its country of export; meat from animals slaughtered in Brennmark may be labeled "Product of Brennmark"); R2 (cattle passports record farm and country of birth; pig import tags are not now recorded by processors).

Counterfactual: Brennmark without the Act, with R1 and R2 in force. Every sign below is against that path.

Unclear provisions:
- U1, ground meat blended from several origins. Reading U1-a: cost is enough to show segregation impracticable, so a grinder may label every batch with every origin it handled in the previous 60 days ("may contain"). Reading U1-b: only physical impossibility counts, so each batch states the origins actually in it. Readings, not assumptions; no probability is given.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Retail label | triangular (attaches a term to every retail sale of covered meat) | Yes for bound retailers who comply (A-1); accuracy rests on A-2 | 3 (a label, template, tag and records attached to the option "sell covered meat at retail"; per-outlet records attached to "run a service counter"); information conveyed to shoppers (CR-11c, not one of the four operations) | CR-3a, CR-4, CR-4 0.8 note (fixed costs per item and per outlet), CR-6, CR-7, CR-9, CR-11c |
| K2 Processor records | triangular (condition on selling meat to retailers and others) | Yes, all plants (no exemption) | 3 (tracing cost per animal, higher for Quorra-born animals at mixed plants, A-5; one-time system per plant) | CR-4, CR-7b, CR-8c, CR-9 |
| K3 Importer records | triangular | Yes | 3 (certificate cost attached to the option "import a live animal") | CR-4, CR-8c, CR-9 |
| K4 Small retailers | exemption (removes K1's burden below a turnover line) | Binds on growth for butchers near the line (A-11) | 3 (K1's burden attached to the option "exceed $1.0 million turnover in a measuring year"); 2 (option to label voluntarily) | CR-4 (x: grow past the line, y: stay under it), CR-10a, CR-11c (silence) |
| K5 Transition | exemption, dated | Yes for frozen stock slaughtered before 1 January 2027 | 2 (option to sell such frozen meat unlabeled until 30 June 2028) | CR-4 (x: sell fresh and labeled, y: freeze and sell unlabeled), CR-10a |
| K6 Enforcement | binary (state takes from the general fund; fines) | Yes (A-29); fines rest on A-30 | 4 (means transferred from the general fund to the FSA); 3 (risk of fines attached to mislabeling and false records) | CR-4 (x: comply, y: violate), CR-8b, CR-8c |

The Act fixes no price. It changes what shoppers know (CR-11c) and attaches costs to options (CR-1 op 3); prices move only through CR-6 and CR-9.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| shoppers.bound_retail | Shoppers at supermarkets and butchers at or above the line | Learn the origin of covered meat (CR-11c); face prices that move with costs and demand |
| retailers.bound | Supermarket chains and butchers with turnover of $1.0 million or more | Op 3: labels, templates, tags, records per outlet and per origin version |
| butchers.near_threshold | About 160 butchers with turnover between $0.8 and $1.2 million | Op 3 attached to exceeding $1.0 million in the measuring year |
| butchers.exempt.brennmark_only | Exempt butchers who sell only Brennmark-born meat | Op 2: may label voluntarily; may be read by silence otherwise (CR-11c) |
| butchers.exempt.mixed | Exempt butchers who sell meat of mixed origin | No label duty; may buy mixed-origin meat at the discount (A-28); may be read by silence (A-14) |
| processors.mixed | The six border plants and others handling both origins | Op 3: about $9 per head and $1.50 per pig for Quorra-born animals, system cost; option to drop the Quorra stream (A-7) |
| processors.brennmark_only | Plants handling only Brennmark-born animals | Op 3: about $1.20 per head, system cost |
| processors.grinders | Plants that grind trim of several origins | Op 3, per reading of U1 |
| feedlots_processors.border | Feedlots and plants near the border specialized in Quorra-born animals (A-26) | Through CR-9: lower value of their main input's output; Brennmark-born calves cost them more |
| importers.live_animals | Importers of Quorra cattle, weaners and sheep | Op 3 (K3 certificates) |
| breeders.quorra | Quorra breeders selling feeder calves and weaners to Brennmark (sellers.foreign) | Through CR-9 (input_to): lower bids for their animals |
| sellers.foreign.quorra_plants | Quorra feedlots and plants that could finish and slaughter at home and ship boxed meat | Through CR-9: a new relative advantage for exporting boxed meat (A-22) |
| breeders.brennmark | Brennmark cow-calf and sow herds | Through CR-9 (input_to): higher bids for Brennmark-born animals |
| food_service | Restaurants, canteens, caterers (exempt) | Through CR-9 (same_market_other_segment): meat redirected to them |
| sellers.substitutes | Sellers of poultry and processed meat (exempt) | Through CR-9 (substitute) |
| sellers.violating | Sellers who mislabel | CR-4 (x: comply, y: mislabel) |
| officials.fsa | Food Standards Agency | Op 4: $5.2 million a year; audit tasks |
| taxpayers | General fund payers and recipients of other general-fund spending | Op 4: they fund K6 (A-29) |
| exporters.brennmark | Sellers of Brennmark's exports | Through CR-9 (currency) |
| lobbies.opponents | Quorra breeders, border processors, importers, Quorra's government | CR-4 (x: accept, y: lobby) |

## 4. Direct effect

CR-1 and CR-2: the immediate change for those whose options K1, K2, K3 and K6 alter.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | shoppers.bound_retail | quality_information (origin of covered meat) | increase | short; medium; long | CR-1 op 3, CR-11c | A-1, A-2, A-3 |
| C-2 | processors.mixed, processors.brennmark_only | compliance_cost (tracing and segregation) | increase | short; medium; long | CR-1 op 3, CR-8c | none |
| C-3 | importers.live_animals | compliance_cost (certificates) | increase | short; medium; long | CR-1 op 3, CR-8c | none |
| C-4 | retailers.bound | compliance_cost (labels, templates, records per outlet) | increase | short; medium; long | CR-1 op 3, CR-8c | A-1 |
| C-5 | officials.fsa | enforcement_cost | increase | short; medium; long | CR-1 op 4, CR-8c | none |
| C-6 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | CR-8b, CR-8a, CR-8 0.7 note (payers from the general budget) | A-29 |

## 5. Responses

CR-4 applied to every pair of options each actor class has (substitute, adjust terms, evade, relocate, reclassify, exit, lobby, change timing); CR-6 where a gap between versions' prices opens; CR-10a for timing.

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-7 | shoppers.bound_retail | quantity_demanded (meat labeled "Mixed origin" or from Quorra-born animals) | decrease | short; medium; long | CR-11c, CR-4 (x: mixed-origin meat, y: Brennmark meat) | A-1, A-2, A-3, A-4 |
| C-8 | shoppers.bound_retail | quantity_demanded (meat labeled "Brennmark") | increase | short; medium; long | CR-11c, CR-4 | A-1, A-2, A-3, A-4 |
| C-9 | processors.mixed | quantity_demanded (Quorra-born animals) | decrease | short; medium; long | CR-4 (x: keep the Quorra stream, y: drop it); CR-9, LW-10 | A-5, A-7; or A-1, A-2, A-3, A-4 |
| C-10 | importers.live_animals | quantity_traded (live cattle and pigs from Quorra) | decrease | short; medium; long | CR-4, CR-9, CR-5a | A-22; A-5 or A-1, A-2, A-3, A-4 |
| C-11 | sellers.foreign.quorra_plants | quantity_traded (boxed meat from Quorra exported to Brennmark) | increase | medium; long | CR-4 (x: sell the live animal to Brennmark, y: finish and slaughter in Quorra), CR-7a | A-22 |
| C-12 | breeders.quorra | net_price_received (feeder calves and weaners sold to Brennmark) | decrease | short; medium; long | CR-9, LW-10, CR-6, CR-10a | A-5 or A-1, A-2, A-3, A-4; A-20 |
| C-13 | breeders.quorra | tax_share_borne (of the discount on Quorra-born animals, relative to Brennmark feedlots and processors) | increase | short; medium; long | CR-7b | A-21, A-6 |
| C-14 | butchers.near_threshold | quantity_supplied (turnover in each measuring year) | decrease | short; medium; long | CR-4 (x: exceed $1.0 million, y: stay under), CR-10a | A-11, A-12 |
| C-15 | butchers.near_threshold | reclassification (splitting a shop into separately registered entities) | increase | short; medium | CR-4 (x: one entity over the line, y: two under it), CR-8c | A-11, A-13 |
| C-16 | butchers.exempt.brennmark_only | compliance_cost (voluntary labels) | increase | medium; long | CR-11c (silence), CR-4 (x: stay silent, y: label) | A-14, A-15 |
| C-17 | retailers.bound | number_of_sellers (outlets with a service counter) | decrease | medium | CR-4 0.8 note (cost fixed per outlet: x keep the counter, y close it) | A-1, A-10 |
| C-18 | retailers.bound | return_on_capital | decrease | short | CR-7b, CR-3a | A-1, A-31 |
| C-19 | processors.mixed | reclassification (cuts from Quorra-born animals sold seasoned, marinated or cured, which K1 exempts) | increase | medium; long | CR-4 (x: covered form, y: exempt form), CR-7a | A-4, A-N3 |
| C-20 | processors.mixed | quantity_traded (meat from Quorra-born animals sold to food service) | increase | short; medium; long | CR-7a (meat moves to the use where the discount is smallest), CR-9 | A-16; A-1, A-2, A-3, A-4 |
| C-21 | sellers.violating | legal_breach (meat from Quorra-born animals sold as "Brennmark") | increase | short; medium; long | CR-4 (x: comply, y: mislabel), CR-6 (the gap between versions' prices seeks open margins) | A-4, A-17, A-30 |
| C-22 | processors.mixed | inventory_held (frozen meat from Quorra-born animals slaughtered before 1 January 2027) | increase | short (late 2026 to June 2028) | CR-10a, CR-4 (x: sell fresh and labeled, y: freeze and sell unlabeled under K5) | A-19, A-4 |
| C-23 | processors.mixed | quantity_traded (Quorra-born cattle and pigs slaughtered, October to December 2026) | increase | short (window before 1 January 2027) | CR-10a, CR-4 (x: slaughter in 2027, y: slaughter in 2026) | A-19, A-N4, A-4 |
| C-24 | processors.mixed | quantity_traded (Quorra-born cattle and pigs slaughtered, January to June 2027) | decrease | short (window after 1 January 2027) | CR-10a (animals slaughtered early are not slaughtered later) | A-19, A-N4, A-4 |
| C-25 | lobbies.opponents | lobbying_effort (to repeal or amend the Act) | increase | short; medium; long | CR-4 (x: accept, y: lobby), CR-8c | A-18, A-5 |
| C-26 | processors.grinders | compliance_cost (segregating trim by origin for ground meat) | U1-a: no_change; U1-b: increase | short; medium; long | CR-1 op 3 per reading, CR-8c | none |
| C-27 | processors.grinders | reclassification (trim from Quorra-born animals moved into ground meat sold with a list of possible origins) | U1-a: increase; U1-b: no_change | medium; long | CR-4 (x: sell as a labeled cut, y: grind under a list), CR-7a | A-4 |

## 6. Second-order effects

CR-9 along named relations, then CR-5 to CR-7 in each market reached. Depth limit 4. Chains into the customers of food-service businesses and into foreign buyers of Brennmark's exports stop at depth 3 (diffuse).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-28 | breeders.brennmark | net_price_received (calves and weaners) | increase | short; medium | CR-9, LW-10, CR-6, CR-12b with CR-12e (dominance premise A-N1) | Brennmark-born animals input_to "Brennmark" meat (close); substitute for Quorra-born animals (close, A-6) | A-1, A-2, A-3, A-4, A-6, A-23, A-N1 |
| C-29 | breeders.brennmark | net_price_received (calves and weaners) | increase | long | CR-9, CR-7a, CR-12e (response argument: herd growth cannot push the price below its old level) | as C-28 | A-1, A-2, A-3, A-4, A-6, A-24, A-25, A-N1 |
| C-30 | breeders.brennmark | quantity_supplied (calves and weaners) | increase | long | CR-4 (x: keep herd size, y: expand), CR-7a, CR-10b | as C-28 | A-4, A-24, A-25 |
| C-31 | breeders.brennmark | asset_value (breeding herds, pasture, sow places) | increase | short (from 2 March 2026, rising with the bill's chance of passing) | CR-7c, CR-10c | as C-28 | A-4, A-6, A-24 |
| C-32 | feedlots_processors.border | asset_value (feedlots and plants specialized in Quorra-born animals) | decrease | short (from 2 March 2026) | CR-7c, CR-10c, CR-7b | Quorra-born animals input_to their output (close) | A-5, A-24, A-26 |
| C-33 | feedlots_processors.border | asset_value (Quorra-born cattle and pigs on feed when the Act became expected) | decrease | short | CR-7c, CR-10a | as C-32 | A-5 or A-1, A-2, A-3, A-4 |
| C-34 | feedlots_processors.border | return_on_capital | decrease | medium; long | CR-7b, CR-9 | as C-32 | A-5, A-26 |
| C-35 | shoppers.bound_retail | price_paid (meat labeled "Brennmark") | increase | short; medium; long | CR-6 (more demand, C-8, with herds fixed, A-23); CR-9 and CR-5c (costs passed, A-27); CR-12e for long | Brennmark-born animals input_to "Brennmark" meat | A-1, A-2, A-3, A-4, A-23; or A-27 |
| C-36 | shoppers.bound_retail | price_paid (meat labeled "Mixed origin" or "Product of Quorra") | ambiguous | short; medium; long | CR-12b over three chains | Quorra-born animals input_to mixed-origin meat | A-1, A-2, A-3, A-4, A-5, A-27 |
| C-37 | shoppers.bound_retail | quantity_demanded (labeled fresh meat, all origins) | decrease | short; medium; long | CR-4c, CR-9 | labeled meat substitute for poultry, processed meat and food service (partial) | A-27, A-N2 |
| C-38 | sellers.substitutes | quantity_substitute (poultry and processed meat) | increase | short; medium; long | CR-9, LW-10 | substitute (partial) | A-27, A-N2 |
| C-39 | butchers.exempt.brennmark_only | quantity_demanded | increase | medium; long | CR-9, CR-11c, CR-4 | same_market_other_segment of bound retail (close) | A-15; A-27 or A-1, A-2, A-3, A-4 |
| C-40 | butchers.exempt.mixed | quantity_demanded | ambiguous | medium; long | CR-12b over three chains | same_market_other_segment of bound retail (close) | A-14, A-27, A-28 |
| C-41 | food_service | price_paid (meat bought wholesale) | ambiguous | short; medium; long | CR-12b over two chains | same_market_other_segment of retail meat (close) | A-16, A-27, A-4 |
| C-42 | processors.mixed, processors.brennmark_only | quantity_traded (animals slaughtered in Brennmark) | decrease | short; medium | CR-9, CR-12a | Quorra-born and Brennmark-born animals input_to slaughter | A-22, A-23, A-5 |
| C-43 | processors.mixed, processors.brennmark_only | quantity_traded (animals slaughtered in Brennmark) | ambiguous | long | CR-12b | as C-42 | A-22, A-25, A-24 |
| C-44 | exporters.brennmark | quantity_traded (exports) | ambiguous | medium; long | CR-9 (currency), CR-12b | currency | A-22, A-5 |
| C-45 | officials.fsa | non_tax_receipts (fines) | increase | short; medium; long | CR-8b, CR-8e | - | A-30 |
| C-46 | sellers.violating | resources_available_other_uses | decrease | short; medium; long | CR-8b, CR-3c | - | A-30 |
| C-47 | shoppers.bound_retail (those who keep buying labeled meat) | resources_available_other_uses | decrease | short; medium; long | CR-3 note, CR-8a | - | A-27 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (-) | Dominance premise | Combined sign |
|---|---|---|---|---|
| breeders.brennmark, net_price_received, short; medium | Shoppers move toward "Brennmark" meat (C-8) and mixed plants drop the Quorra stream (C-9), raising bids for Brennmark-born animals, herds fixed (A-23) | K2 tracing cost of about $1.20 per head reduces the value of each animal to plants (CR-9, LW-10) | A-N1 (empirical, p 0.75): the premium per animal exceeds the $1.20 per head (CR-12e) | increase (C-28) |
| breeders.brennmark, net_price_received, long | As above | Herd growth (C-30) | Response argument (CR-12e): growth stops once yields are equal and cannot push the price below its old level; K2 cost as above, A-N1 | increase (C-29) |
| breeders.quorra, net_price_received | Lower retail demand for mixed-origin meat (C-7); higher handling cost at mixed plants (A-5); plants dropping the stream (C-9); expected discount from 2026 (A-20) | - | All chains same direction | decrease (C-12) |
| shoppers.bound_retail, price_paid ("Brennmark" meat) | More demand with herds fixed; costs passed (A-27) | - (herd growth in the long run cannot reverse it, CR-12e) | Same direction | increase (C-35) |
| shoppers.bound_retail, price_paid (mixed-origin meat) | Costs passed (A-27), higher at mixed plants (A-5) | Less demand for it (C-7) | None stated | ambiguous (C-36) |
| shoppers.bound_retail, quantity_demanded (all labeled meat) | No derivable chain: that labels raise shoppers' trust in meat as a whole is a Tier C note (CR-12 0.7 note) | Costs passed (A-27) | - | decrease (C-37) |
| butchers.exempt.mixed, quantity_demanded | Bound sellers' prices rise with costs (A-27); cheaper mixed-origin inputs (A-28) | Shoppers infer mixed origin from silence (A-14) | None stated | ambiguous (C-40) |
| butchers.exempt.brennmark_only, quantity_demanded | Labels show "Brennmark" (C-8); cost advantage over bound sellers (A-27) | Silence chain does not apply: they label (A-15) | Same direction | increase (C-39) |
| food_service, price_paid (meat) | K2 costs per animal passed into wholesale prices (A-27); Brennmark-born meat drawn to retail (C-8) | Meat from Quorra-born animals redirected to food service (C-20) | None stated | ambiguous (C-41) |
| processors, quantity_traded (slaughter in Brennmark), short; medium | - | Fewer Quorra-born animals imported (C-10); Brennmark herds fixed (A-23) | Same direction (CR-12a) | decrease (C-42) |
| processors, quantity_traded (slaughter in Brennmark), long | Brennmark herd growth (C-30) | Fewer Quorra-born animals (C-10) | None stated | ambiguous (C-43) |
| exporters.brennmark, quantity_traded (exports) | Payments for boxed meat from Quorra rise (C-11) | Payments for live animals from Quorra fall (C-10) | None stated | ambiguous (C-44) |
| processors.mixed, quantity_traded (Quorra-born slaughter) by window | Late 2026 (C-23) | Early 2027 (C-24); later windows lower through C-9 | Different windows signed separately (CR-12h, 2.5 timing shifts) | increase (Oct-Dec 2026); decrease (Jan-Jun 2027) |

CR-12f: no two provisions cancel by construction. K4's exemption does not undo K1 for the exempt; it creates a separate set of chains (C-14 to C-16, C-39, C-40).

## 8. Time structure

- **Announcement (2 March to 1 July 2026).** The bill was introduced with the breeders' support and became more likely to pass through June. Asset values move with that probability (CR-7c): breeding herds and pasture in Brennmark up (C-31); border feedlots and plants specialized in Quorra-born animals down (C-32); owners of Quorra-born animals already on feed bear the expected discount (C-33).
- **Measuring year (1 July 2026 to 30 June 2027).** K4's first measuring year began on the day of signing, before labeling starts. Butchers near the line hold turnover below $1.0 million in that year and every later one (C-14), or split entities (C-15). Because the threshold is not indexed, it binds on more butchers each year as prices and volumes grow (more butchers cross $1.0 million in money terms).
- **Feeder purchases in 2026.** Calves and weaners bought in the second half of 2026 are slaughtered in 2027 under K2 and sold in 2027-28 under K1; buyers bid less for them at once (A-20, C-12).
- **K2 from 1 January 2027 and K5.** Meat from animals slaughtered before 1 January 2027 may be sold frozen and unlabeled until 30 June 2028. Some Quorra-born animals are slaughtered in late 2026 rather than early 2027 (C-23, C-24) and their meat is frozen and held (C-22). These are timing shifts, signed per window against the counterfactual. After June 2028 the stock is gone and the effect ends.
- **K1 from 1 July 2027.** Retailers' costs (C-4), counter closures (C-17) and the shoppers' response (C-7, C-8) start then.
- **Breeding cycle.** Brennmark herds cannot grow within a breeding cycle (A-23), so the premium for Brennmark-born animals is largest in the short run; herds grow in the long run where the premium is expected to last (A-24, A-25; C-30), which narrows it without removing it (CR-12e).
- **Durable specific assets.** Border feedlots and plants (A-26) are located for the Quorra trade; their loss of value is borne by owners at announcement (C-32), and their lower returns persist (C-34) while the stock wears out (CR-10b).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-2 | processors.mixed, processors.brennmark_only | compliance_cost (tracing and segregation) | increase | Labor, plant time and systems ($0.4 to $0.9 million per plant) that would have served other ends | CR-1 op 3, CR-8c |
| C-3 | importers.live_animals | compliance_cost (certificates) | increase | Clerical time and fees | CR-1 op 3, CR-8c |
| C-4 | retailers.bound | compliance_cost (labels, templates, records per outlet) | increase | About $6,000 set-up and $3,500 a year per counter, and per-version templates and tags | CR-1 op 3, CR-8c |
| C-5 | officials.fsa | enforcement_cost | increase | $5.2 million a year of inspection | CR-1 op 4, CR-8c |
| C-6 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | Purchases or public services funded by the $5.2 million | CR-8a, CR-8b |
| C-15 | butchers.near_threshold | reclassification (splitting entities) | increase | Legal and accounting work spent only to stay under the line | CR-4, CR-8c |
| C-16 | butchers.exempt.brennmark_only | compliance_cost (voluntary labels) | increase | Label costs incurred to answer the inference from silence | CR-11c, CR-8c |
| C-14 | butchers.near_threshold | quantity_supplied (turnover in each measuring year) | decrease | Sales forgone by butchers and their customers (CR-5a) | CR-4, CR-5a |
| C-22 | processors.mixed | inventory_held (frozen meat) | increase | Cold storage and the value lost by freezing | CR-10a, CR-8c |
| C-25 | lobbies.opponents | lobbying_effort (to repeal or amend) | increase | Time and money spent on lobbying | CR-4, CR-8c |
| C-26 | processors.grinders | compliance_cost (segregating trim) | U1-a: no_change; U1-b: increase | Separate grinding runs and cleaning | CR-1 op 3, CR-8c |
| C-46 | sellers.violating | resources_available_other_uses | decrease | Fines paid | CR-8b |
| C-47 | shoppers.bound_retail (those who keep buying labeled meat) | resources_available_other_uses | decrease | Other purchases forgone because the same meat costs more | CR-3 note, CR-8a |

CR-8b both sides: the general fund's payment (C-6) is the FSA's receipt (spent, C-5); fines paid (C-46) are the FSA's receipts (C-45); higher prices paid for "Brennmark" meat (C-35) are in part receipts to Brennmark breeders (C-28) and in part cover costs used up (C-2, C-4); the lower prices received by Quorra breeders (C-12) are not a transfer to anyone in full, since they reflect a fall in what shoppers will pay for meat from their animals (C-7) and higher handling costs (A-5). Prevented exchanges: live animals not imported (C-10) deprive both Quorra breeders and Brennmark buyers of the gain each expected (CR-5a).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Retailers at or above the threshold label as required. | enforcement | 0.8 | Supermarket chains' central labeling systems; FSA audit plan. | These consequences fail or lose this chain: C-1, C-4, C-7, C-8, C-17, C-18, and the information chains of C-9, C-10, C-12, C-20, C-28, C-29, C-33, C-35, C-39. |
| A-2 | Records and audits keep labels mostly accurate. | enforcement | 0.75 | R2 passports for cattle; audit frequency. | As A-1. |
| A-3 | Many shoppers believed "Product of Brennmark" meant Brennmark-born (prior belief). | other | 0.85 | Consumer Council survey: 64%. | As A-1 except C-4, C-17, C-18. |
| A-4 | Shoppers who learn that meat is from Quorra-born animals move away from it, toward Brennmark meat (direction). | other | 0.7 | Survey: 41% would pay more for fully domestic meat; 3% prefer Quorra-born. | As A-3, plus C-19, C-21, C-22 to C-24, C-27, C-30, C-31, C-41. |
| A-5 | At mixed plants, handling a Quorra-born animal costs more than a Brennmark-born one. | other | 0.9 | Impact assessment: $9 against $1.20 a head for cattle. | C-9, C-12 (cost chain), C-25, C-32, C-34, C-42. |
| A-6 | Brennmark-born animals are close substitutes for Quorra-born ones for feedlots and processors. | substitutability | 0.9 | Same breeds and weights; existing trade in both. | C-13, C-28, C-29, C-31. |
| A-7 | Some mixed plants take few Quorra-born animals, so running two origin streams costs more than they gain from them. | other | 0.75 | Share of Quorra animals by plant. | C-9 (cost chain). |
| A-8 | For low-volume cuts, a second origin version costs a retailer more (template, tag, inventory line) than it gains. | other | 0.7 | Retailers' range reviews; sales per cut. | No reported consequence rests on it; see section 11. |
| A-9 | Retailers add a premium "Brennmark" line beside the mixed line for many cuts. | other | 0.4 | Experience with premium labels; shelf space. Below the cut-off. | Not reported. |
| A-10 | Some service counters are marginal, so records per outlet decide whether they stay open. | other | 0.6 | Counter sales by store size. | C-17. |
| A-11 | For some butchers near $1.0 million, labeling costs more than the gain from growing past the line. | binding | 0.6 | Butchers' margins; per-outlet costs. | C-14, C-15. |
| A-12 | Butchers know during the measuring year that it decides their status. | expectations | 0.75 | Act signed 1 July 2026; association guidance. | C-14 in the first measuring year. |
| A-13 | Splitting a shop into a separately registered entity is legal and cheap enough for some. | other | 0.6 | K4 counts per registered entity. | C-15. |
| A-14 | Some shoppers know the exemption and infer from an exempt butcher's silence that its meat may be mixed. | other | 0.55 | Publicity of the Act; survey on label reading. | C-16; the (-) chain of C-40. |
| A-15 | Exempt butchers may label voluntarily, and for those selling only Brennmark-born meat the label costs less than the sales lost to silence. | other | 0.6 | K4; label costs per shop. | C-16, C-39. |
| A-16 | Food-service buyers place little value on origin, and menus carry none. | other | 0.75 | Food-service purchasing practice. | C-20, C-41. |
| A-17 | Origin cannot be detected by testing the meat, only by audits of records, which sample. | enforcement | 0.8 | No laboratory test for country of birth; audit plan. | C-21. |
| A-18 | Breeders, processors, importers and Quorra's government can organize at a cost below their stake. | other | 0.85 | Existing associations; the breeders' campaign for the bill. | C-25. |
| A-19 | For some processors, freezing and storing meat from Quorra-born animals slaughtered in 2026 costs less than the expected discount. | other | 0.55 | Cold storage costs; frozen share of retail beef. | C-22, C-23, C-24. |
| A-20 | Buyers of feeders in 2026 expect the discount to apply when the animals are slaughtered. | expectations | 0.8 | Finishing takes six to nine months; Act signed July 2026. | C-12 in 2026. |
| A-21 | Quorra breeders' alternatives to selling to Brennmark are clearly worse than processors' alternatives (Brennmark-born animals). | mobility | 0.65 | Size of Quorra's own market; distance to other markets. | C-13. |
| A-22 | Some Quorra animals are finished and slaughtered in Quorra and exported as boxed meat instead. | mobility | 0.55 | Spare capacity at Quorra plants. | C-10, C-11, C-42, C-43, C-44. |
| A-23 | Brennmark herds cannot grow within a breeding cycle. | durability | 0.9 | Gestation and rearing times. | C-28, C-35 (demand chain), C-42. |
| A-24 | Owners expect the Act to stay in force for years. | expectations | 0.75 | Cross-party support; no expiry. | C-29, C-30, C-31, C-32, C-43. |
| A-25 | Breeders expand herds where the premium lasts (pasture and sow places are available). | alternative_uses | 0.65 | Land use; herd trends. | C-29, C-30, C-43. |
| A-26 | Border feedlots and plants are specialized in Quorra-born animals by location, and Brennmark-born calves cost them more to obtain. | other | 0.7 | Location and sourcing data. | C-32, C-34. |
| A-27 | Per-animal and per-unit tracing and labeling costs are passed partly into retail and wholesale prices; nearly all competitors of labeled sellers are bound. | other | 0.65 | 91% of retail meat sold by bound sellers. | C-35 (cost chain), C-36, C-37, C-38, C-39 (cost chain), C-40, C-41, C-47. |
| A-28 | Exempt butchers can buy mixed-origin meat at the discount without labeling it. | other | 0.7 | Wholesale price lists by origin. | The (+) chain of C-40. |
| A-29 | The $5.2 million is new money from the general fund. | revenue_use | 0.9 | K6. | C-6. |
| A-30 | Some violations are detected and fined. | enforcement | 0.6 | Audit plan; penalty schedule. | C-21, C-45, C-46. |
| A-31 | Part of the compliance cost stays with labeled retailers in the short run. | other | 0.75 | Competition among the three chains. | C-18. |
| A-N1 | The premium shoppers pay for meat from Brennmark-born animals, per animal, exceeds the record cost of about $1.20 per head (and its pig equivalent) passed back to breeders. | other | 0.75 | NEW. 41% of shoppers say they would pay more for fully domestic meat; $1.20 spread over the retail yield of a steer is well under one cent per kg. | C-28 and C-29 become ambiguous. |
| A-N2 | Some shoppers at the margin move from labeled fresh meat to poultry, processed meat or eating out when its price rises. | substitutability | 0.7 | NEW. These are exempt from K1 and serve the same meals. | C-37, C-38. |
| A-N3 | For some cuts from Quorra-born animals, selling them seasoned, marinated or cured (exempt as processed meat) costs less than the retail discount. | other | 0.55 | NEW. K1 exempts seasoned meat; existing marinated lines. | C-19. |
| A-N4 | Some Quorra-born animals on feed in late 2026 are near enough to slaughter weight that slaughtering before 1 January 2027 costs less than the expected discount. | other | 0.6 | NEW. Continuous placements over six to nine months of finishing mean some animals are within weeks of target weight at any date. | C-23, C-24. |

**Not reported** (an assumption below 0.5):
- Retailers add a premium "Brennmark" line beside the mixed line for many cuts (A-9, p 0.4), with its effect on variety and shelf space.
- A-8 (p 0.7) holds, but it yields no signed consequence against the counterfactual: without the Act each cut is sold in one version, and with A-8 low-volume cuts stay in one version. Its effect is to limit C-7 and C-8 for those cuts (shoppers cannot choose by origin there), which is a qualifier on magnitude, not a sign.

### Final check before the report

1. *Uncombined chains.* Every (class, variable, horizon) reached by more than one chain is in section 7, including the K2 per-head cost against the premium for Brennmark breeders (combined with A-N1) and the per-window slaughter timing.
2. *Group signs.* The general-fund payers are a group (C-6). No other rule here licenses only "at least one of".
3. *Baseline.* All signs are against Brennmark without the Act, with R1 and R2 in force. "Product of Brennmark" labels on imported-calf meat exist in the counterfactual (R1), which is why A-3 is needed for C-1.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for general-fund payers (unavoidable), violators who pay fines, and shoppers who keep buying labeled meat at a higher price (C-47). Quorra breeders are worse off (CR-3a) but their spending elsewhere is not signed.
5. *Timing shifts.* The 2026-27 slaughter shift is signed per window (C-23, C-24); the frozen stock (C-22) is dated.
6. *Both sides of every transfer.* General fund to FSA (C-6, C-5); fines (C-46, C-45); premium (C-35, C-28).
7. *Every class, every core rule.* CR-4 checked for every class's pairs (substitute: C-37, C-38; terms: C-17; evade: C-21; relocate: C-11; reclassify: C-15, C-19, C-27; exit: C-9, C-17; lobby: C-25; timing: C-14, C-22 to C-24). CR-6: C-28, C-35, C-36. CR-7 and CR-7c: C-13, C-20, C-31 to C-34. CR-9: section 6, including currency (C-44). Enforcement costs (C-5) and payers (C-6) recorded.
8. *Unstated premises.* Four premises added (A-N1 to A-N4).

## 11. Report

**The policy:** From 1 July 2027, retailers in Brennmark with turnover of $1.0 million or more must label fresh beef, pork and lamb with the countries where the animals were born, raised and slaughtered. From 1 January 2027 slaughterhouses and importers must trace each animal's origin. Small retailers, poultry, processed meat and food service are exempt; frozen meat from animals slaughtered before 2027 may be sold unlabeled until mid-2028. The Food Standards Agency enforces it with $5.2 million a year from the general fund.

**Visible consequences:** Shoppers at labeled retailers learn where their meat comes from (C-1) and move toward meat labeled "Brennmark" and away from mixed-origin meat (C-7, C-8). "Brennmark" meat costs more (C-35), and Brennmark breeders get more for their calves and weaners (C-28). Quorra breeders get less for animals sold to Brennmark (C-12), and fewer live animals are imported (C-10). Processors, importers and retailers bear tracing and labeling costs (C-2 to C-4), and the agency spends its appropriation (C-5).

**Invisible consequences:**
- *Breeders and asset owners:* Brennmark breeding herds and land gain value from the bill's introduction (C-31); herds grow in the long run (C-30) and the premium narrows but stays (C-29). Border feedlots and plants built around Quorra-born animals lose value (C-32) and earn less (C-34); owners of Quorra-born animals on feed when the bill became likely bear the expected discount (C-33). Quorra breeders bear more of the discount than Brennmark buyers (C-13).
- *Processors:* Some mixed plants drop the Quorra stream (C-9). Meat from Quorra-born animals moves to food service (C-20), into seasoned and processed forms (C-19) and, under reading U1-a, into ground meat with a "may contain" list (C-27). Under U1-b grinders must segregate trim (C-26). Some animals are slaughtered early in late 2026 and their meat frozen to be sold unlabeled under the transition (C-22 to C-24). Total slaughter in Brennmark falls in the short and medium run (C-42); some of the trade moves to Quorra plants, which export boxed meat instead (C-11).
- *Retailers:* Some service counters close (C-17); retailers' returns fall in the short run (C-18). Butchers near the $1.0 million line hold turnover below it in every measuring year, starting the day the Act was signed (C-14), or split into separate entities (C-15). Exempt butchers who sell only Brennmark-born meat label voluntarily (C-16) and gain customers (C-39).
- *Shoppers and other markets:* Shoppers buy less labeled fresh meat overall (C-37) and more poultry and processed meat (C-38); those who keep buying labeled meat have less for other things (C-47). Some sellers mislabel Quorra-born meat as Brennmark, since origin cannot be tested (C-21); some are fined (C-45, C-46). General-fund payers or recipients of other spending fund the agency (C-6). Opponents, including Quorra's government, lobby to repeal or amend the Act (C-25).

**Ambiguous effects:**
- The price of mixed-origin meat (C-36): costs push it up; lower demand pushes it down.
- Sales at exempt butchers who sell mixed meat (C-40): their cost advantage pushes up; shoppers reading their silence as "mixed" push down.
- The price food service pays for meat (C-41): tracing costs push up; meat from Quorra-born animals redirected to food service pushes down.
- Total slaughter in Brennmark in the long run (C-43): Brennmark herd growth against fewer Quorra-born animals.
- Brennmark's exports (C-44): fewer payments for live animals against more for boxed meat from Quorra.
What would decide each: the size of the cost pass-through against the demand shift; how many shoppers read silence; how far herds grow.

**Key conditions:** Shoppers' prior belief (A-3, 0.85) and their move toward Brennmark meat on learning (A-4, 0.7) drive the demand chains; labels are applied and accurate (A-1, 0.8; A-2, 0.75). Handling Quorra-born animals costs more at mixed plants (A-5, 0.9), which drives the price chain independently of shoppers. Quorra breeders have worse alternatives than processors (A-21, 0.65). Brennmark herds are fixed in a breeding cycle (A-23, 0.9) and grow later (A-25, 0.65). The near-threshold, frozen-stock and boxed-meat responses rest on weaker premises (A-11, A-13, A-19, A-22, all 0.55 to 0.6). Four premises were added: the premium per animal exceeds the record cost per head (A-N1, 0.75); shoppers substitute toward exempt meats (A-N2, 0.7); processing is a cheaper route for some Quorra-born cuts (A-N3, 0.55); some animals can be slaughtered early (A-N4, 0.6).

**What this analysis cannot say:** How large any effect is, so not whether the price of mixed-origin meat rises or falls, or how the discount on Quorra-born animals compares with the premium on Brennmark-born ones. It does not weigh shoppers' gain from information against the costs of tracing and the losses of Quorra breeders and border plants, or say whether the policy is good. Health and food-safety effects are out of scope. Whether shoppers' preference for domestic origin reflects anything about the meat is not a question the method addresses; it takes their rankings as given (CR-2).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | shoppers.bound_retail | quality_information (origin of covered meat) | increase | short; medium; long | visible | B | CR-1 (op 3: K1 attaches an origin label to every retail sale); CR-11c (the label conveys information; it changes beliefs only where shoppers believed otherwise, A-3) | A-1, A-2, A-3 |
| C-2 | processors.mixed, processors.brennmark_only | compliance_cost (tracing and segregation) | increase | short; medium; long | visible | A | CR-1 (op 3: K2 attaches tracing to every animal slaughtered, about $9 or $1.20 per head and a one-time system); CR-8c (resources spent on complying are used up) | none |
| C-3 | importers.live_animals | compliance_cost (certificates) | increase | short; medium; long | invisible | A | CR-1 (op 3: K3 certificates per animal or lot); CR-8c | none |
| C-4 | retailers.bound | compliance_cost (labels, templates, records per outlet) | increase | short; medium; long | visible | B | CR-1 (op 3: K1 labels, per-version templates and tags, per-outlet records at service counters); CR-8c; A-1: they comply | A-1 |
| C-5 | officials.fsa | enforcement_cost | increase | short; medium; long | visible | A | CR-1 (op 4: $5.2 million a year to the FSA); CR-8c (resources spent on enforcing are used up) | none |
| C-6 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short; medium; long | invisible | B | CR-8b (every payment is a receipt: the FSA's appropriation is paid by someone); CR-8 0.7 note (payers from the general budget: a group); CR-8a | A-29 |
| C-7 | shoppers.bound_retail | quantity_demanded (meat labeled "Mixed origin" or from Quorra-born animals) | decrease | short; medium; long | visible | B | CR-11c (labels reveal origin to shoppers who believed otherwise, A-3); CR-4 (x: mixed-origin meat, y: Brennmark meat; x now known to be worse for those who rank origin, A-4, so those at the margin switch; CR-4a: none switch the other way on account of the change, save the 3% who prefer Quorra-born, whom A-4 covers as direction) | A-1, A-2, A-3, A-4 |
| C-8 | shoppers.bound_retail | quantity_demanded (meat labeled "Brennmark") | increase | short; medium; long | visible | B | CR-11c; CR-4 (the mirror of C-7) | A-1, A-2, A-3, A-4 |
| C-9 | processors.mixed | quantity_demanded (Quorra-born animals) | decrease | short; medium; long | invisible | B | Two independent chains (CR-12d). Chain 1: CR-4 (x: keep two origin streams, y: take only Brennmark-born animals; K2 makes x dearer, A-5; plants with few Quorra animals switch, A-7). Chain 2: CR-9 and LW-10 (the derived value of Quorra-born animals falls with retail demand for their meat, C-7) | A-5, A-7; or A-1, A-2, A-3, A-4 |
| C-10 | importers.live_animals | quantity_traded (live cattle and pigs from Quorra) | decrease | short; medium; long | visible | B | CR-9 (lower bids from Brennmark buyers, C-9, C-12); CR-4 (Quorra breeders at the margin, x: sell live to Brennmark, y: finish at home, A-22, switch); CR-5a (the exchanges no longer made deprive both sides of a gain) | A-22; A-5 or A-1, A-2, A-3, A-4 |
| C-11 | sellers.foreign.quorra_plants | quantity_traded (boxed meat from Quorra exported to Brennmark) | increase | medium; long | invisible | B | CR-4 (x: sell the animal live, y: finish and slaughter in Quorra; y gains relative to x as live animals bear the mixed-plant cost and the "Mixed origin" label); CR-7a (means move to the use that yields more, net of moving cost) | A-22 |
| C-12 | breeders.quorra | net_price_received (feeder calves and weaners sold to Brennmark) | decrease | short; medium; long | visible | B | CR-9 and LW-10 (relation: Quorra-born animals input_to meat sold in Brennmark; lower demand for that meat, C-7, and higher handling cost, A-5, lower what buyers will pay); CR-6 (the price moves to the new clearing level); CR-10a (buyers in 2026 bid less for animals slaughtered after 2026, A-20). All chains same sign (CR-12a) | A-5 or A-1, A-2, A-3, A-4; A-20 |
| C-13 | breeders.quorra | tax_share_borne (of the discount on Quorra-born animals, relative to Brennmark feedlots and processors) | increase | short; medium; long | invisible | B | CR-7b (the lasting loss settles on the side with clearly worse alternatives: Quorra breeders' other markets are worse, A-21, while processors can use Brennmark-born animals, A-6) | A-21, A-6 |
| C-14 | butchers.near_threshold | quantity_supplied (turnover in each measuring year) | decrease | short; medium; long | invisible | B | CR-4 (x: exceed $1.0 million and bear K1, y: stay under; for some, x is reversed by the cost, A-11); CR-10a (the first measuring year began on 1 July 2026, so the choice is made before labeling starts, A-12); repeated each year since each year's turnover sets the next year's status | A-11, A-12 |
| C-15 | butchers.near_threshold | reclassification (splitting a shop into separately registered entities) | increase | short; medium | invisible | B | CR-4 (x: one entity over the line, y: two entities under it; K4 counts per registered entity, A-13); CR-8c (the cost of splitting is used up) | A-11, A-13 |
| C-16 | butchers.exempt.brennmark_only | compliance_cost (voluntary labels) | increase | medium; long | invisible | B | CR-11c 0.7 note (silence: shoppers infer mixed origin from an exempt seller's silence, A-14); CR-4 (x: stay silent, y: label; for those selling only Brennmark-born meat y costs less than the sales lost, A-15); CR-8c | A-14, A-15 |
| C-17 | retailers.bound | number_of_sellers (outlets with a service counter) | decrease | medium | invisible | B | CR-4 0.8 note (a cost fixed per outlet bears on whether the outlet operates: x keep the counter, y close it or sell pre-packed only; some counters are marginal, A-10); A-1 | A-1, A-10 |
| C-18 | retailers.bound | return_on_capital | decrease | short | invisible | B | CR-3a (a burden is attached to their chosen option); CR-7b (the part not passed on in the short run stays with them, A-31) | A-1, A-31 |
| C-19 | processors.mixed | reclassification (cuts from Quorra-born animals sold seasoned, marinated or cured, which K1 exempts) | increase | medium; long | invisible | B | CR-4 (x: the covered fresh form, which bears the "Mixed origin" discount, A-4; y: the exempt processed form; y cheaper for some cuts, A-N3); CR-7a (meat moves to the use that yields more, net of the cost of processing) | A-4, A-N3 |
| C-20 | processors.mixed | quantity_traded (meat from Quorra-born animals sold to food service) | increase | short; medium; long | invisible | B | CR-7a (meat from Quorra-born animals moves from retail, where it bears a discount, to food service, which is exempt and places little value on origin, A-16, until the yield gap is no greater than the cost of moving); CR-9 (relation: food service same_market_other_segment of retail meat) | A-16; A-1, A-2, A-3, A-4 |
| C-21 | sellers.violating | legal_breach (meat from Quorra-born animals sold as "Brennmark") | increase | short; medium; long | invisible | B | CR-6 (the gap between the prices of the two versions, C-35, C-36, is pressure that seeks every open margin, including exchanges outside the rule); CR-4 (x: comply, y: mislabel; origin cannot be tested, only audited by sample, A-17; some violations occur and are detected, A-30). Against a counterfactual with no such rule, any breach is an increase | A-4, A-17, A-30 |
| C-22 | processors.mixed | inventory_held (frozen meat from Quorra-born animals slaughtered before 1 January 2027) | increase | short (late 2026 to June 2028) | invisible | B | CR-10a (a change expected in the future alters choices now); CR-4 (x: sell fresh and labeled "Mixed origin", y: freeze and sell unlabeled under K5; y cheaper for some, A-19); persistence ends when K5 lapses on 30 June 2028 | A-19, A-4 |
| C-23 | processors.mixed | quantity_traded (Quorra-born cattle and pigs slaughtered, October to December 2026) | increase | short (window before 1 January 2027) | invisible | B | CR-10a and CR-4 (x: slaughter in early 2027 under K2 and K1, y: slaughter in late 2026 and freeze under K5; A-19, A-N4) | A-19, A-N4, A-4 |
| C-24 | processors.mixed | quantity_traded (Quorra-born cattle and pigs slaughtered, January to June 2027) | decrease | short (window after 1 January 2027) | invisible | B | CR-10a (animals slaughtered in late 2026 are not slaughtered in early 2027); 2.5 timing shift signed per window against the counterfactual | A-19, A-N4, A-4 |
| C-25 | lobbies.opponents | lobbying_effort (to repeal or amend the Act) | increase | short; medium; long | invisible | B | CR-4 (x: accept the Act, y: lobby; the Act lowers their yields, A-5, C-12, C-32, so y gains; they can organize, A-18); CR-8c (resources spent lobbying are used up) | A-18, A-5 |
| C-26 | processors.grinders | compliance_cost (segregating trim by origin for ground meat) | U1-a: no_change; U1-b: increase | short; medium; long | invisible | A | CR-1 per reading: U1-a lets a grinder list every origin handled in 60 days, so no segregation is needed beyond K2 records; U1-b attaches segregation by batch (op 3); CR-8c | none |
| C-27 | processors.grinders | reclassification (trim from Quorra-born animals moved into ground meat sold with a list of possible origins) | U1-a: increase; U1-b: no_change | medium; long | invisible | B | CR-4 (x: sell as a cut labeled "Mixed origin", y: grind under a list that names every origin; under U1-a every batch from a mixing grinder carries the same list, so Quorra-born trim bears no extra discount there, A-4); CR-7a. Under U1-b each batch states its actual origins, so the route gives no advantage | A-4 |
| C-28 | breeders.brennmark | net_price_received (calves and weaners) | increase | short; medium | visible | B | CR-9 and LW-10 (relation: Brennmark-born animals input_to "Brennmark" meat; more demand for it, C-8, and plants switching to Brennmark-born animals, C-9, A-6); CR-6 (herds fixed in a breeding cycle, A-23, so the price rises to ration them); CR-12b against the K2 cost per head passed back (CR-9, LW-10), dominance by A-N1 (CR-12e, empirical) | A-1, A-2, A-3, A-4, A-6, A-23, A-N1 |
| C-29 | breeders.brennmark | net_price_received (calves and weaners) | increase | long | invisible | B | As C-28; CR-7a (herd growth, C-30, brings yields back toward others); CR-12e (response argument: growth stops once yields are equal and cannot push the price below its old level); K2 cost per head dominated, A-N1 | A-1, A-2, A-3, A-4, A-6, A-24, A-25, A-N1 |
| C-30 | breeders.brennmark | quantity_supplied (calves and weaners) | increase | long | invisible | B | CR-4 (x: keep herd size, y: expand; y made better by the premium, C-28, expected to last, A-24); CR-7a (land and sow places move to breeding, A-25); CR-10b (herds grow only through births, so the response is gradual) | A-4, A-24, A-25 |
| C-31 | breeders.brennmark | asset_value (breeding herds, pasture, sow places) | increase | short (from 2 March 2026, rising with the bill's chance of passing) | invisible | B | CR-10c (value reflects expected yields); CR-7c (captured by owners when the change becomes expected, in part as the bill became more likely to pass, and in full on signing, A-24) | A-4, A-6, A-24 |
| C-32 | feedlots_processors.border | asset_value (feedlots and plants specialized in Quorra-born animals) | decrease | short (from 2 March 2026) | invisible | B | CR-10c and CR-7c (expected yields fall: Quorra-born animals bear the handling cost, A-5, and Brennmark-born calves cost them more, A-26; borne by owners at announcement); CR-7b (specific by location, so they cannot move) | A-5, A-24, A-26 |
| C-33 | feedlots_processors.border | asset_value (Quorra-born cattle and pigs on feed when the Act became expected) | decrease | short | invisible | B | CR-7c applied to a stock held when the change becomes expected (animals bought before March 2026 at undiscounted prices and slaughtered after 1 January 2027); CR-10a | A-5 or A-1, A-2, A-3, A-4 |
| C-34 | feedlots_processors.border | return_on_capital | decrease | medium; long | invisible | B | CR-7b (the lasting loss settles on means that cannot move, A-26); CR-9 (relation: Quorra-born animals input_to their output) | A-5, A-26 |
| C-35 | shoppers.bound_retail | price_paid (meat labeled "Brennmark") | increase | short; medium; long | visible | B | Two independent chains with the same sign (CR-12d). Chain 1: CR-6 (more demand, C-8, while herds are fixed, A-23); in the long run herd growth narrows it without reversing it (CR-12e). Chain 2: CR-9 and CR-5c (tracing and labeling costs passed partly into retail prices, A-27) | A-1, A-2, A-3, A-4, A-23; or A-27 |
| C-36 | shoppers.bound_retail | price_paid (meat labeled "Mixed origin" or "Product of Quorra") | ambiguous | short; medium; long | invisible | B | CR-12b: (+) CR-9 and CR-5c (costs passed, A-27, higher at mixed plants, A-5); (-) CR-6 (less demand for it, C-7, A-4). No premise says which dominates | A-1, A-2, A-3, A-4, A-5, A-27 |
| C-37 | shoppers.bound_retail | quantity_demanded (labeled fresh meat, all origins) | decrease | short; medium; long | invisible | B | CR-4c (the last unit, valued least, is given up as labeled meat costs more, A-27; LW-3); CR-9 (relation: substitute for exempt poultry, processed meat and food service, A-N2). A suspected rise in trust in labeled meat as a whole is not derivable and is a Tier C note (CR-12 0.7 note) | A-27, A-N2 |
| C-38 | sellers.substitutes | quantity_substitute (poultry and processed meat) | increase | short; medium; long | invisible | B | CR-9 and LW-10 (relation: substitute; when labeled meat costs more, demand for its substitutes rises); CR-4 (x: labeled meat, y: an exempt substitute, A-N2) | A-27, A-N2 |
| C-39 | butchers.exempt.brennmark_only | quantity_demanded | increase | medium; long | invisible | B | CR-9 (relation: same_market_other_segment of bound retail); CR-11c (their voluntary label shows "Brennmark", A-15, and shoppers move toward it, A-4); CR-4 (x: a bound seller whose prices carry K1 costs, A-27, y: an exempt seller). Two independent chains, same sign | A-15; A-27 or A-1, A-2, A-3, A-4 |
| C-40 | butchers.exempt.mixed | quantity_demanded | ambiguous | medium; long | invisible | B | CR-12b: (+) CR-9 and CR-4 (bound sellers' prices carry K1 costs, A-27); (+) CR-5c (they buy mixed-origin meat at the discount without labeling, A-28); (-) CR-11c (shoppers infer mixed origin from silence, A-14). No premise says which dominates | A-14, A-27, A-28 |
| C-41 | food_service | price_paid (meat bought wholesale) | ambiguous | short; medium; long | invisible | B | CR-12b: (-) CR-7a and CR-6 (meat from Quorra-born animals redirected to food service, C-20, A-16); (+) CR-9 and CR-5c (K2 costs per animal passed into wholesale prices, A-27, and Brennmark-born meat drawn to retail, C-8). No premise says which dominates. Chains into food-service customers stop here (depth 3, diffuse) | A-16, A-27, A-4 |
| C-42 | processors.mixed, processors.brennmark_only | quantity_traded (animals slaughtered in Brennmark) | decrease | short; medium | invisible | B | CR-9 (fewer Quorra-born animals imported, C-10, A-22, A-5); Brennmark herds fixed within a breeding cycle (A-23), so no offsetting chain in these horizons (CR-12a) | A-22, A-23, A-5 |
| C-43 | processors.mixed, processors.brennmark_only | quantity_traded (animals slaughtered in Brennmark) | ambiguous | long | invisible | B | CR-12b: (+) Brennmark herd growth (C-30, A-24, A-25); (-) fewer Quorra-born animals (C-10, A-22). No premise says which dominates | A-22, A-25, A-24 |
| C-44 | exporters.brennmark | quantity_traded (exports) | ambiguous | medium; long | invisible | B | CR-9 0.7 note (currency link both ways): (-) fewer payments for live animals from Quorra, C-10; (+) more payments for boxed meat from Quorra, C-11. No premise says which dominates. Stops at depth 3 | A-22, A-5 |
| C-45 | officials.fsa | non_tax_receipts (fines) | increase | short; medium; long | invisible | B | CR-8b (fines paid are receipts to the state); A-30 | A-30 |
| C-46 | sellers.violating | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-8b and CR-3c (fines are an unavoidable payment for those fined) | A-30 |
| C-47 | shoppers.bound_retail (those who keep buying labeled meat) | resources_available_other_uses | decrease | short; medium; long | invisible | B | CR-3 note (only those who keep buying the burdened good at a higher price have less for other uses); CR-8a; A-27 | A-27 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-040-C1: Shoppers' preference for origin is taken as given (CR-2), but whether the label changes the ranking of meat as a whole (more trust, more meat bought) cannot be derived: CR-11c needs a prior belief and a direction for each belief changed, and the case gives them only for the Quorra-born versus Brennmark comparison (A-3, A-4). Recorded as a Tier C note under C-37.
- GAP-040-C2: The direction of C-9 at the plant level needs CR-4 for a plant choosing which inputs to accept; no core rule says how a plant facing per-input handling costs chooses between running one stream and two, beyond CR-4's 0.8 note on fixed costs per item. Applied by analogy (the second stream as an "item"), with A-7 doing the work.

**(b) Core-rule wording that was hard to apply.**
- CR-11c with the silence clause: the clause says the inference from silence is information "conveyed by the policy", but it does not say whose decision it changes first. Here it changes both shoppers' choices and the exempt sellers' choice to label (C-16), and the second needs CR-4 on the seller's side; the rule could say so.
- CR-7c and stocks in transit: the rule speaks of durable assets; cattle on feed are a stock held for months that bears an expected change in yield (C-33). It was applied, but the rule does not say whether inventories count.
- CR-12e: the response argument settled the long-run sign for Brennmark breeders (C-29), but the K2 per-head cost is a second change the policy also causes, so it needed its own dominance premise (A-N1), as the 0.8 note warns. The note could say explicitly that a per-unit cost passed back is such a second change.
- CR-4 0.8 note (fixed costs per item): A-8 (a second origin version costs more than it gains) yields no sign against the counterfactual, because the counterfactual has only one version. The rule does not say how to record a fixed cost that limits the reach of an information effect rather than an output.
- The K4 threshold creates a bunching problem like CR-12h (activity held under a line in every year), but CR-12h speaks of moving activity between windows, not of holding it below a level; C-14 was signed per year against the counterfactual.

**(c) Vocabulary missing from the ontology.**
- No variable for the share of a good sold through an exempt channel (food service, processed forms); C-19, C-20 and C-27 were recorded as `quantity_traded` with a qualifier and as `reclassification`.
- No variable for the composition of supply by origin (share of Quorra-born animals in slaughter); recorded through `quantity_demanded` and `quantity_traded` with qualifiers.
- No actor class for a foreign government as a lobbying party; recorded inside `lobbies.opponents`.
- No variable for turnover held under a threshold distinct from `quantity_supplied`.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the labeling case. Both find the following: shoppers learn origin, and given A-3 and A-4 they move from mixed-origin meat toward "Brennmark" meat. Processors, importers and retailers bear tracing and labeling costs. Mixed plants take fewer Quorra-born animals, and Quorra breeders get less for them and sell fewer. Quorra plants ship boxed meat instead. Brennmark breeders get more, their herds gain value and grow, and border feedlots and plants lose returns and value. "Brennmark" meat costs more, while the mixed-origin price and the food-service price are ambiguous. Some service counters close, and butchers near the threshold stay under it or split. Exempt butchers who sell only Brennmark-born meat label voluntarily. Some meat is routed into processed forms and food service, there is a late-2026 rush with frozen stocks, some meat is mislabeled, and both versions record lobbying, enforcement, the general-fund payers and fines. There is no case where the two versions sign the same key in opposite directions. The main difference is one pattern-version error. The pattern version signs `variety` (origin versions per cut) as a decrease (C-10) and counts it as the second use of the candidate pattern "fixed cost per item reduces variety". Against the counterfactual, each cut is sold in one version with no origin shown, so a fixed cost per origin version cannot reduce the count. The core's refusal to sign is right. The pattern version also signs Brennmark breeders' price rise (C-29) without the opposing chain that K2's $1.20 per head on Brennmark-born animals creates; the core states that chain and a dominance premise (A-N1). The core version has its own errors. Its long-run sign for breeders' prices (C-29) takes more from CR-12e than the response argument gives. Its fall in demand for labeled meat as a whole (C-37), with the rise in substitutes that follows (C-38), ignores that the mixed-origin price is itself ambiguous. And it omits several derivable keys: buyers' information at exempt butchers, per-batch information on ground meat, Quorra breeders' asset value, and mixed plants' loss of means.

Counts: M 25, V 13, S 0, OP 10, OC 7.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-1 | M | | `quality_information` increase. The core adds A-3 as a premise; it is not needed for this variable (the label makes origin easier to judge whatever buyers believed before), only for any change in choices. |
| C-2 | C-2 | V | | The core merges mixed and single-origin plants into one row. |
| C-3 | C-2 | V | | As C-2. |
| C-4 | C-3 | M | | |
| C-5 | C-4 | M | | |
| C-6 | C-7 | V | | Same premises (A-1 to A-4). Pattern class `buyers.origin_minded`, core class all shoppers at bound retailers; the core cites CR-4a for the 3% who prefer Quorra-born meat. |
| C-7 | C-8 | V | | As C-6. |
| C-8 | C-9 | M | | Both have two independent chains (CR-12d). The pattern's cost chain is per head (CR-4c with A-5, A-6). The core's cost chain is through plants dropping the second stream (A-7). Both are valid. |
| C-9 | C-9 | V | | The pattern records `number_of_sellers` (plants handling both origins); the core folds the same CR-4 move (A-7) into chain 1 of C-9. |
| C-10 | none (core: "Not reported") | OC | P | Pattern: `variety` (origin versions per cut) decrease, from a fixed cost per version (A-8). The analyst misapplied the CR-4 0.7 note and the candidate pattern "fixed cost per item reduces variety". In the counterfactual, under R1, each cut is sold in one version with no origin shown. With the Act, a cut is sold in one version or, where it pays, two. So the count cannot fall below the counterfactual. A-8 only keeps it from rising for low-volume cuts. A-9, which the pattern treats as the opposing (+) chain, is in fact the only chain that moves the count against the baseline, and it is below the cut-off. The valid record is no sign (or `no_change`), which is the core's reading (its "Not reported" and Gaps (b)). This case is not a second use that promotes the candidate pattern. |
| C-11 | C-17 | M | | |
| C-12 | C-14 | V | | `number_of_sellers` just below the line relative to just above (pattern), against `quantity_supplied` (turnover held under the line in each measuring year, core). Same CR-4 move, A-11, A-12. |
| C-13 | C-15 | M | | |
| C-14 | C-16 | M | | The core starts the horizon at medium, the pattern at short. |
| C-15 | none | OC | E | `quality_information` at exempt butchers increase (voluntary labels and silence, A-14, A-15). This follows from the core's own C-16 by CR-11c, since buyers there had no origin information in the counterfactual. Core omission. |
| C-16 | C-19 | M | | `reclassification` into processed forms. The core adds A-N3 (processing costs less than the discount for some cuts). The pattern's RS-5 "Assumes" needs this premise, and the pattern did not state it, so the premise is hidden there. The pattern's cost chain (A-5) holds only for the part of the cost carried through retail cutting: K2's per-head records apply to every animal slaughtered whatever its later form. |
| C-17 | C-20 | V | | Food service's purchases (pattern) against processors' sales to food service (core). Same move, CR-7a and CR-4, A-16. |
| C-18 | C-21 | M | | The core lists A-30 (some breaches detected) as a premise. `legal_breach` increase does not need detection, so A-30 is needed only for fines. |
| C-19 | C-25 | V | | The core records only the opponents. The breeders' lobbying to extend K1 is derivable from CR-4 (x: accept, y: lobby) with A-18, so the core omitted it. Neither version asks what breeders would do in the counterfactual, though. Without the Act, they would presumably still be lobbying for an origin law. Against that baseline, their lobbying needs a comparison premise, as in RS-7's "Unless" clause. |
| C-20 | C-26 | M | | |
| C-21 | none | OC | E | Ground-meat `quality_information` per batch (U1-a no_change; U1-b increase). It follows from CR-11c per reading, and the core records the matching cost (C-26) but not the information. Core omission. |
| C-22 | C-23, C-24 | V | | The pattern signs the late-2026 window (July to December) and leaves the 2027 fall to C-8. The core signs both windows (October to December 2026 up, January to June 2027 down). The core adds A-N4 (some animals are near slaughter weight), which the pattern's rush needs and does not state. Neither version notes that fresh meat from animals slaughtered in January to June 2027 is sold before K1 applies. So the rush rests on K2's cost and K5's frozen window, not on the label as such. The core's "x: slaughter in early 2027 under K2 and K1" is imprecise on this. |
| C-23 | C-22 | M | | |
| C-24 | C-10, C-12 | V | | Importers bring in fewer feeders from mid-2026 (pattern, a window) against live imports decrease over all horizons, with CR-10a for 2026 inside C-12 (core). The core makes C-10 rest on A-22 (boxed meat), which it does not need: lower bids alone move marginal Quorra sellers to any alternative. |
| C-25 | C-12 | M | | |
| C-26 | C-10 | V | | Breeders' `quantity_supplied` (pattern) against importers' `quantity_traded` (core). Same prevented exchanges (CR-5a). |
| C-27 | C-11 | M | | |
| C-28 | none | OC | J | Total Quorra sales to Brennmark, `ambiguous`. The core records the two items (C-10, C-11) and the currency link (C-44), not the total. Nothing scorable is lost. |
| C-29 | C-28 | M | | Both increase, short to medium. The pattern's premises omit an opposing chain the core derives: K2 attaches about $1.20 per head to Brennmark-born animals too, which lowers what plants bid for every animal (CR-9, LW-10). Without a dominance premise (core A-N1, CR-12e), CR-12b gives `ambiguous`. So the pattern's sign has a hidden premise. RS-16's "Unless" clause, as written, names added supply but not a cost the policy also attaches to the substitute. |
| C-30 | C-31 | M | | |
| C-31 | C-30 | M | | |
| C-32 | C-34 | M | | |
| C-33 | C-32 | M | | |
| C-34 | C-35 | M | | |
| C-35 | C-36 | M | | Both `ambiguous`. |
| C-36 | C-41 | M | | Both `ambiguous`. |
| C-37 | C-39, C-40 | V | | The pattern gives all exempt butchers `ambiguous`. The core splits them: those selling only Brennmark-born meat increase (they label, so the silence chain does not reach them; A-15), and mixed sellers `ambiguous`. The split is the better record, but the core's C-39 class should be limited to those who do label. |
| C-38 | C-18 | V | | Pattern: labeled retailers' `asset_value` decrease (CR-7c on A-31). Core: `return_on_capital` decrease, short run. Same chain; the core omits the capitalization step (final check 7). A change of limited duration is capitalized for the yields it affects (CR-7c), so the pattern's row is derivable. |
| C-39 | none | OC | E | Quorra breeders' `asset_value` decrease (CR-7c, CR-10c with A-21, A-24). The core uses A-21 only for the incidence row (C-13) and omits the capitalization. Core omission. |
| C-40 | none | OC | J | Near-threshold butchers' `asset_value`, `ambiguous`. The pattern overrides RS-17's "decrease" with a (+) chain from rivals' burden; that is the valid sign (CR-7c, CR-9, CR-12b). The core does not record the key. Nothing scorable is lost. |
| C-41 | C-5 | M | | |
| C-42 | C-6 | M | | |
| C-43 | none | OC | E | Mixed plants that keep both origins have less for other uses (CR-3 note: they keep paying for the burdened option). The core's final check 4 signs this for shoppers but not for plants. Core omission; by the same reasoning single-origin plants and bound retailers qualify too, which neither version records. |
| C-44 | C-45 | M | | |
| C-45 | C-46 | M | | |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-13 | OP | J | Quorra breeders' `tax_share_borne` increase relative to Brennmark feedlots and processors (CR-7b, A-21, A-6). The pattern states the same comparison in prose (section 6) and puts A-21 into C-25's premises. A recording choice. |
| C-27 | OP | J | Under U1-a, Quorra-born trim is moved into ground meat sold under a "may contain" list (CR-4, CR-7a). The pattern says that such a list also deters origin-minded buyers. The core's claim needs a premise the core does not state: buyers discount a mixing grinder's list less than a "Mixed origin" cut. Both readings are defensible. |
| C-29 | OP | E | Brennmark breeders' price increase in the long run. CR-12e's response argument shows that herd growth cannot push the price below its old level. It does not show that the price stays above that level, which needs a premise that breeding supply is not perfectly elastic in the long run (scarce pasture or sow places). A-25 points the other way. Core error: the long-run sign should be `ambiguous` between increase and `no_change`, or carry that premise. The pattern rightly limits its sign to short and medium (section 8). |
| C-33 | OP | E | Quorra-born animals on feed when the Act became expected lose value (CR-7c, CR-10a). This is derivable, and the pattern omitted it (final check 7). The core's derivation contains a slip, though. Animals "bought before March 2026 ... slaughtered after 1 January 2027" hardly exist with six to nine months of finishing. The loss falls on animals on feed between March and July 2026 that are slaughtered from January 2027, through K2's cost (A-5). |
| C-37 | OP | E | Shoppers buy less labeled fresh meat overall. The core derives this from "labeled meat costs more" (A-27), but its own C-36 makes the mixed-origin price `ambiguous`. A chain whose sign is ambiguous (origin-indifferent shoppers facing a possibly lower mixed-origin price) opposes it, so by CR-12 0.8 (kind 3) the sign is `ambiguous` without a dominance premise. Core error. |
| C-38 | OP | E | Poultry and processed meat sell more. This rests on C-37 and fails with it. Core error. |
| C-42 | OP | E | Total slaughter in Brennmark decreases in the short and medium run (fewer Quorra-born animals, herds fixed, A-23). This is derivable, and the pattern omitted it. The core adds A-22, which the sign does not need. The late-2026 rush (C-23) also lies inside "short", so the short horizon should be signed per window (CR-12h). |
| C-43 | OP | J | Total slaughter in the long run is `ambiguous`. Nothing scorable is added. |
| C-44 | OP | J | Brennmark's exports `ambiguous` through the currency link. The pattern declines to sign the same link (kind 3 on an ambiguous first link). Same content, recorded differently. |
| C-47 | OP | E | Shoppers who keep buying labeled meat have less for other uses (CR-3 note). This is valid for buyers of "Brennmark" meat, whose price rises (C-35), and the pattern's final check 4 omitted them. The core's class is too broad, since the mixed-origin price is `ambiguous`. Error in both versions: an omission in the pattern and too wide a class in the core. |

### Findings

- **Pattern overclaims and hidden premises.**
  - C-10 (`variety` decrease) is signed against an imagined two-version baseline, not against the counterfactual, in which each cut has one version with no origin shown. The candidate pattern "fixed cost per item reduces variety" needs a precondition: the versions must exist in the counterfactual. This case is not a second use that promotes it.
  - C-29 (Brennmark breeders' price) leaves out the opposing chain from K2's per-head cost on Brennmark-born animals and needs a dominance premise (core A-N1). RS-16's "Unless" clause should also cover a cost the policy attaches to the substitute itself.
  - C-16 needs the premise that processing costs less than the discount (core A-N3), as RS-5's "Assumes" requires. C-22 needs the premise that some animals are near slaughter weight (core A-N4).
  - C-19 records breeders' lobbying without asking what they would have lobbied for without the Act.
- **Errors in the core version.**
  - C-29 (long run) reads the CR-12e response argument as giving "above the old level", where it gives only "not below".
  - C-37 and C-38 ignore the kind 3 chain from the ambiguous mixed-origin price.
  - C-47's class is too broad.
  - It omits buyers' information at exempt butchers (pattern C-15), per-batch information on ground meat (C-21), Quorra breeders' asset value (C-39), mixed plants' loss of means (C-43), retailers' capitalization (C-38) and breeders' lobbying (C-19).
  - Minor: unneeded premises (A-3 on C-1, A-22 on C-10 and C-42, A-30 on C-21), a dating slip in C-33, and the imprecise "under K2 and K1" in C-23.
- **Errors in the pattern version (omissions).** It omits animals on feed losing value (core C-33), total slaughter falling in the short and medium run (C-42), and the loss of means for buyers who keep buying "Brennmark" meat (part of C-47).
- **Limits of the core rules.**
  - No row has cause K. Every difference traces to an error or a recording choice.
  - GAP-040-C1 (trust in meat as a whole) is the CR-11 0.7 rule doing its job: no premise, no chain. It is not a gap.
  - GAP-040-C2 (a plant choosing between one origin stream and two) is covered by CR-4's paragraph on units and lumpy costs (a large cost attached to the option "handle both origins"). The 0.8 note's list of items, outlets and firms is incomplete, but the rule is not.
  - The real limit both versions meet is the welfare of buyers who choose differently once informed (Q22). Both leave it unsigned, correctly.
- **Unclear core-rule wording.**
  - CR-7c says "durable asset". Its scope over inventories held when a change becomes expected (cattle on feed) should be stated; CR-10b already lists inventories as a stock.
  - CR-12e's response argument should say explicitly that it bounds the response at the old level and does not establish a sign above it.
  - CR-4's 0.8 note on fixed costs should point back to the lumpy-cost paragraph rather than list items, outlets and firms.
  - CR-11's silence clause should name the second step, the sellers' response (both versions made this point independently).
  - CR-12h covers moving activity between windows, not holding it under a level in every window (core Gaps (b)).
- **Test of 0.8 verdicts.**
  - *CR-11 0.7, silence (needed interpretation):* confirmed. The core version had to derive the exempt sellers' response with CR-4 too (core C-16; core Gaps (b)).
  - *CR-4 0.8, a cost fixed per origin stream (needed interpretation):* confirmed (core GAP-040-C2), with the qualification above that CR-4's lumpy-cost paragraph already covers it.
  - *RS-17 (partly worked; the asset-value conclusion overridden):* the core-only version supports the override in principle. A derivation from CR-4, CR-7c and CR-9 has the rivals' burden as a (+) chain, and RS-17's "value of growing past the threshold falls" compares with a firm free of the policy, not with the counterfactual. The core does not record the key itself.
  - *CR-4 0.7 fixed costs per item and the candidate pattern ("worked as written", "needed here"):* contradicted (C-10 above).

