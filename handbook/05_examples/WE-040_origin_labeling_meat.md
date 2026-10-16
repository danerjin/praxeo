# WE-040 Country-of-origin labeling for meat

Analyst: draft (Handbook 0.8 held-out test, corrected under 0.9)  |  Rule catalog version: 0.9  |  Status: awaiting expert review

A stylized policy in a fictional country. It resembles real mandatory country-of-origin labeling rules for meat but is not modeled on any one of them. It was written as a held-out test of catalog 0.8: none of the 0.7 and 0.8 changes were drawn from it. It probes a `disclosure_mandate` that conveys information to buyers (CR-11c, with the 0.7 clarifications on what a sign needs and on the silence of exempt sellers), compliance costs that are fixed per item, per outlet and per firm as well as per animal (CR-4, 0.7 and 0.8), a turnover threshold measured over a past year (RS-17), a burden on foreign suppliers of live animals that works like a tariff without being a tax, the three kinds of opposing chain (CR-12, 0.8), and the question of whether buyers who choose with more knowledge are better off (`06_gaps.md`, Q22). Health and food-safety effects are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Brennmark Meat Origin Labeling Act.** The Republic of Brennmark has about 9.4 million people and its own currency. It slaughters about 1.5 million cattle and 6 million pigs a year. About 21% of the cattle (about 315,000 head) are born in neighboring Quorra, imported as feeder calves at about 250 kg, finished in Brennmark feedlots for six to nine months and slaughtered in Brennmark; another 3% are imported from Quorra for immediate slaughter. About 18% of the pigs (about 1.08 million) are born in Quorra and imported as weaners. Six of Brennmark's fourteen large processors, all within 60 km of the Quorra border, take about 80% of the Quorra-born cattle; the other eight take almost only Brennmark-born animals. About 12% of the beef eaten in Brennmark is imported boxed beef, mostly from Ardova. A Quorra feeder calf sells for about $900.

Retail meat is sold by three supermarket chains (about 2,100 outlets, about 70% of retail meat, most of them with an in-store service counter where meat is cut) and about 1,800 independent butchers. About 1,300 butchers have annual turnover under $1.0 million and sell about 9% of retail meat; about 160 have turnover between $0.8 million and $1.2 million. About 35% of meat is eaten through food service (restaurants, canteens, caterers).

A 2025 survey by the Brennmark Consumer Council found that 64% of shoppers believe meat labeled "Product of Brennmark" comes from animals born in Brennmark, 41% say they would pay more for meat from animals born, raised and slaughtered in Brennmark, and 3% say they would prefer meat from Quorra-born animals. The agriculture ministry's impact assessment estimates the cost of tracing and segregation at about $9 per head of cattle and $1.50 per pig at plants that handle both origins (separate lots, separate slaughter runs, origin carried through cutting), about $1.20 per head at plants that handle only Brennmark-born animals (checking passports and keeping records), a one-time traceability system of $0.4 to $0.9 million per plant, about $6,000 to set up and $3,500 a year to run records at each outlet with a service counter, and a separate label template, shelf tag and inventory line for each origin version of each cut.

The bill was introduced on 2 March 2026 with the support of the cow-calf producers' association, passed on 18 June 2026 and was signed on 1 July 2026. It has no expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Retail label | `disclosure_mandate` | Fresh, chilled and frozen muscle cuts and ground meat of beef, pork and lamb sold at retail | Retailers | From 1 July 2027, each package or counter item states the country where the animals were born, raised and slaughtered. Three categories: "Brennmark" (all three stages in Brennmark); "Product of X" (all three stages in one other country X); "Mixed origin", with each stage's country listed ("Born in Quorra, raised and slaughtered in Brennmark"). A package with meat from animals of more than one category lists every category present. | K4. Poultry; processed meat (cured, cooked, seasoned, sausages); food service. |
| K2 Processor records | Record-keeping requirement, part of K1 | Every animal slaughtered | Slaughterhouses and cutting plants | From 1 January 2027, records tracing each animal's country of birth, raising and slaughter, carried through to every lot sold, with written origin declarations to buyers. Records kept for two years. | None |
| K3 Importer records | Record-keeping requirement, part of K1 | Live cattle, pigs and sheep imported | Importers of live animals | From 1 January 2027, import certificates per animal (cattle) or per lot (pigs), passed to the buyer with an origin declaration. | None |
| K4 Small retailers | Exemption from K1 | Retailers | — | Retailers whose turnover in the previous financial year (July to June) was under $1.0 million, counted per registered business entity. For the first labeling year (July 2027 to June 2028), the measuring year is July 2026 to June 2027. Not indexed. Exempt retailers may label voluntarily, in the K1 form. | — |
| K5 Transition | Exemption from K1 | Frozen meat | Retailers | Frozen meat from animals slaughtered before 1 January 2027 may be sold without an origin label until 30 June 2028. | — |
| K6 Enforcement | Enforcement | K1 to K3 | Food Standards Agency (FSA) | Record audits at plants, importers and retailers; fines up to $2,000 per mislabeled lot and up to $50,000 for falsified records. A new appropriation of $5.2 million a year from the general fund pays for 40 inspectors. | — |

Existing rules (in force in the counterfactual too):

| Rule | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| R1 Origin of imports | Labeling rule | Imported meat | Importers and retailers | Imported meat is labeled with its country of export; meat from animals slaughtered in Brennmark may be labeled "Product of Brennmark". | — |
| R2 Cattle passports | Identification rule | Cattle | Farmers, dealers | Every bovine carries a passport recording its farm and country of birth. Pigs carry a herd tattoo; imported weaners carry an import tag that processors do not now record. | — |

Unclear provisions:
- U1, ground meat blended from several origins. Section 9(3) says "Ground meat shall bear the origins of the meat it contains"; section 9(4) allows "a list of the origins that may be present, where the processor shows that segregation is impracticable". Reading U1-a: cost is enough to make segregation impracticable, so any grinder that mixes trim may label every batch "May contain meat from Brennmark, Quorra and Ardova", naming every origin it handled in the previous 60 days. Reading U1-b: only physical impossibility counts, so in practice each batch must state the origins actually in it. The FSA has issued no guidance and no court has ruled, so these are readings, not assumptions.

The counterfactual is Brennmark without the Act, with R1 and R2 in force.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: attaches a condition to every retail sale of covered meat. By CR-1, it attaches a cost to the option of selling covered meat at retail (operation 3), and removes the option of selling meat from Quorra-born animals as "Product of Brennmark" (operation 1). The information on the label is not one of the four operations (CR-1, 0.7); it works on buyers through CR-11c. | Yes for retailers at or above $1.0 million (A-1). Not binding on imported boxed meat, which R1 already labels by country. | EN-15, CR-11c, CR-4 (0.7, 0.8 fixed costs), CR-6, CR-7b, RS-1, RS-3, RS-5, RS-14, RS-16 |
| K2, K3 | Triangular: a cost attached to the option of slaughtering, cutting or importing animals (CR-1, operation 3). Part of the cost is per animal, part per plant, and part per origin stream a plant handles. | Yes | CR-4, CR-7b, CR-8c, OC-2 |
| K4 | Exemption: a boundary at $1.0 million of turnover, measured over a past year | Yes | RS-17 (0.9), RS-5, CR-11 (0.7 and 0.9, silence) |
| K5 | Exemption: a boundary in time | Yes | RS-8 |
| K6 | Binary: funded by a new appropriation from the general fund (A-29) | Yes | OC-3, OC-1 |

The Act collects no tax and pays no subsidy. It is the instrument type `disclosure_mandate`, for which `02_ontology.md` lists CR-11c and EN-15. EN-15 was promoted in 0.9 after its second use, which was this case (Gaps found, c4).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `buyers.retail_meat` (`buyers.current`) | Shoppers at labeled retailers | See the origin of each item. |
| `buyers.origin_minded` | Shoppers who believed "Product of Brennmark" meant Brennmark-born and prefer Brennmark-born meat | Learn which items are mixed origin. |
| `buyers.origin_indifferent` | Shoppers who do not care about origin | See labels they do not use; face any price change. |
| `buyers.exempt_butchers` | Shoppers at butchers under the threshold | See no label, or a voluntary one. |
| `processors.mixed` | The six border plants handling both Brennmark-born and Quorra-born animals | Must trace and segregate two origin streams. |
| `processors.single` | Plants handling only Brennmark-born animals | Must check passports and keep records. |
| `importers.live_animals` (`intermediaries`) | Livestock dealers importing Quorra calves and weaners | Must keep and pass on certificates. |
| `feedlots.border` | Brennmark finishers that buy mostly Quorra-born feeders | The animals they finish now sell as mixed origin. |
| `breeders.domestic` (`factor_owners.specific`, `sellers.substitutes`) | Brennmark cow-calf and sow herds | Their animals are the substitute for Quorra-born feeders. |
| `breeders.quorra` (`sellers.foreign`) | Quorra breeders selling feeders and weaners to Brennmark | Their animals now cost more to handle and carry a label. |
| `processors.quorra` (`sellers.foreign`) | Quorra slaughter plants | Could finish and slaughter at home and export boxed meat. |
| `retailers.labeled` | Supermarket chains and butchers at or above $1.0 million | Must label every covered item and keep records per outlet. |
| `butchers.exempt` | Butchers under $1.0 million | Exempt; may label voluntarily. |
| `butchers.near_threshold` | Butchers with turnover between $0.8 million and $1.2 million | Growth past $1.0 million brings labeling. |
| `food_service` | Restaurants, canteens, caterers (buyers of meat) | Not covered; buy from the same plants. |
| `processed_meat_makers` | Makers of sausages, ham, cooked meats | Their products are not covered. |
| `officials.enforcement` | FSA | Audits and fines. |
| `taxpayers`, recipients of other general-fund spending | Fund the $5.2 million a year | One or more of them gives up what it would otherwise have funded. |
| `exporters.brennmark` | Brennmark exporters to Quorra | Linked to imports from Quorra by the currency relation. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `buyers.retail_meat` | `quality_information` (country of birth, raising and slaughter of the animals) | increase | short (from July 2027) | CR-1 (0.7), CR-11c, EN-15 | A-1, A-2 |
| C-2 | `processors.mixed` | `compliance_cost` (tracing, separate lots and slaughter runs, origin carried through cutting) | increase | short (from January 2027) | CR-1, CR-8c, OC-2 | none |
| C-3 | `processors.single` | `compliance_cost` (checking passports and tags, records) | increase | short | CR-1, CR-8c, OC-2 | none |
| C-4 | `importers.live_animals` | `compliance_cost` (certificates and declarations) | increase | short | CR-1, CR-8c, OC-2 | none |
| C-5 | `retailers.labeled` | `compliance_cost` (label versions per item, records per outlet, supplier checks per firm) | increase | short | CR-1, CR-8c, OC-2, EN-15 | none |

C-1 is what the Act's supporters point to. It is information, and information alone changes no option (CR-1, 0.7). Whether it changes any choice depends on what buyers believed before and which way those who learn something move (CR-11, 0.7); those premises are A-3 and A-4, used from section 5 on. C-2 to C-5 are the costs of producing the information. They are Tier A given that the work is done (OC-2); the record-keeping is the stated requirement, but the cost is not what the supporters point to, so it is marked invisible in the consequence list.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | `buyers.origin_minded` | `quantity_demanded` (mixed-origin meat at labeled retailers) | decrease | short (from July 2027) | CR-11c (0.7), CR-4, EN-15 | A-1, A-2, A-3, A-4 |
| C-7 | `buyers.origin_minded` | `quantity_demanded` (meat labeled "Brennmark") | increase | short | CR-11c (0.7), CR-4, EN-15 | A-1, A-2, A-3, A-4 |
| C-8 | `processors.mixed` | `quantity_demanded` (Quorra-born feeders, weaners and slaughter cattle) | decrease | short–medium (from 2027) | CR-4, CR-4c, CR-9, CR-12d | A-6; A-5 or (A-3, A-4) |
| C-9 | `processors.mixed` | `number_of_sellers` (plants handling both origins) | decrease | short–medium | CR-4 (0.8 fixed cost per plant), CR-7a | A-5, A-7 |
| C-11 | `retailers.labeled` | `number_of_sellers` (outlets with an in-store service counter) | decrease | medium | CR-4 (0.8 fixed cost per outlet), CR-7a | A-1, A-10 |
| C-12 | `butchers.near_threshold` | `number_of_sellers` (butchers just below $1.0 million, relative to just above) | increase | short (FY 2026–27) to medium | RS-17, CR-4, CR-10a | A-11, A-12 |
| C-13 | `butchers.near_threshold` | `reclassification` (shops split into separately registered entities) | increase | short–medium | RS-17, RS-5 | A-11, A-13 |
| C-14 | `butchers.exempt` (selling only Brennmark-born meat) | `compliance_cost` (voluntary origin labels) | increase | short–medium | CR-11 (0.7 and 0.9 silence), CR-4, EN-15 | A-14, A-15 |
| C-15 | `buyers.exempt_butchers` | `quality_information` (origin, from voluntary labels and from silence) | increase | short–medium | CR-11c (0.7 and 0.9 silence), CR-4, EN-15 | A-14, A-15 |
| C-16 | `processors.mixed`, `processed_meat_makers` | `reclassification` (meat of Quorra-born animals routed into processed products, outside K1) | increase | short–medium | RS-5, CR-4 | A-3, A-4, A-33 |
| C-17 | `food_service` | `quantity_traded` (purchases of mixed-origin meat) | increase | short–medium | CR-4, CR-9, RS-1 | A-3, A-4, A-16 |
| C-18 | `processors.mixed`, `retailers.labeled` | `legal_breach` (meat of Quorra-born animals sold as "Brennmark") | increase | short–medium | CR-4, CR-1, RS-3 | A-3, A-4, A-17 |
| C-19 | `processors.mixed`, `importers.live_animals`, Quorra's government | `lobbying_effort` (for U1-a, a higher threshold or repeal) | increase | medium | RS-7, CR-12 (0.9, activities that exist only under the policy) | A-18 |
| C-20 | `processors.mixed` (grinders) | `compliance_cost` (segregating trim and recording origins per batch of ground meat) | U1-a: no_change; U1-b: increase | short | CR-1, CR-8c | A-2 |
| C-21 | `buyers.retail_meat` | `quality_information` (origin of a given ground-meat batch, among one plant's batches) | U1-a: no_change; U1-b: increase | short | CR-11c | A-1, A-2 |
| C-22 | `processors.mixed` | `quantity_traded` (Quorra-born animals slaughtered, July to December 2026) | increase | short (2026) | RS-8, CR-10a | A-19, A-34; A-5 or (A-3, A-4) |
| C-23 | `processors.mixed` | `inventory_held` (frozen, unlabeled meat of Quorra-born animals, end of 2026) | increase | short (2026 to mid-2028) | RS-8, CR-10a | A-19 |
| C-24 | `importers.live_animals` | `quantity_traded` (Quorra feeder calves imported, from mid-2026) | decrease | short (2026) | CR-10a, CR-4 | A-20; A-5 or (A-3, A-4) |
| C-46 | `breeders.domestic` | `lobbying_effort` (to extend K1 to processed meat and food service, against lobbying for an origin law without the Act) | ambiguous | medium | RS-7 (Unless), CR-4, CR-12b | A-18, A-35 |

**What the label tells buyers (C-6, C-7).** CR-11's 0.7 clarification asks for two premises before any sign. First, what buyers believed: under R1, meat from Quorra-born animals slaughtered here was sold as "Product of Brennmark", and 64% of shoppers took that to mean Brennmark-born (A-3). For them the "Mixed origin" label is news; for the "Brennmark" label it confirms what they believed, and changes nothing for them. Second, which way those who learn something move: the survey says 41% would pay more for fully domestic meat and 3% would prefer Quorra-born (A-4). With both, CR-4 applies to the origin-minded (x: mixed-origin meat, y: Brennmark meat; x is now known to be worse by their ranking): some move from x to y. Imported boxed meat was already labeled by country (R1), so the Act tells buyers nothing new about it.

**Processors (C-8, C-9).** Two chains reach C-8 with the same sign. The cost chain: each Quorra-born animal now costs a mixed plant about $9 a head (cattle) more to handle than a Brennmark-born one (A-5), so processors buy fewer of them at the old price (CR-4c, x: a Quorra-born animal, y: a Brennmark-born one, A-6). The demand chain: retail demand for mixed-origin meat falls (C-6), and demand for the animals follows the demand for their meat (CR-9 with LW-10). By CR-12d the consequence holds if either chain's premises hold, so they are listed separately. Part of the cost is fixed per plant for running two origin streams (separate runs, separate cutting, the system). CR-4's 0.8 clarification says such a cost bears on whether the plant handles both origins at all, not on the price per head: plants that take few Quorra animals stop taking them (C-9, A-7), and the price per head is not signed from that cost. The per-head part is signed (C-25).

**Retailers: costs per item and per outlet (C-11; C-10 withdrawn).** Each origin version of a cut needs its own label template, shelf tag and inventory line, a cost fixed per item offered (CR-4, 0.7): for low-volume cuts, retailers carry one version, not two (A-8). That yields no signed consequence for `variety`. Without the Act, under R1, each cut is sold in one version with no origin shown; with it, a cut is sold in one version or, where a second pays, two. A-8 only keeps low-volume cuts at one version, which is no change against the counterfactual, and limits C-6 and C-7 for those cuts in size, not in sign. The only chain that moves the count is a premium "Brennmark" line added beside the mixed line (CR-4 with C-7), which would raise it; it needs a premise the case does not support, that this pays for many cuts (A-9, p = 0.4), so it is a conditional possibility (section 10), not reported. The decrease signed here under 0.8 (C-10) compared with a two-version baseline that does not exist, and is withdrawn. Records kept at each outlet with a service counter are a cost fixed per outlet (CR-4, 0.8): where a counter is marginal, the store closes it and sells only prepackaged meat labeled by the processor (C-11, A-10). Neither cost is used to sign the price of a unit (section 6).

**The threshold (C-12, C-13).** K4 exempts retailers under $1.0 million of turnover in the previous financial year. RS-17's preconditions hold: a butcher near the line that grows past it takes on labeling for all its covered meat (A-11). Some stay below (C-12), and some split a second shop into a separately registered entity (C-13, A-13). Because turnover is measured over July 2026 to June 2027, the response comes in that year, before labels are required (RS-17, timing sentence; A-12). RS-17's clause on the value of firms near the line (0.9) is taken up in section 7.

**Silence (C-14, C-15).** An exempt butcher's meat carries no label. CR-11's 0.7 clarification on silence says buyers may infer something from it, and that the inference needs its own premise. Here: shoppers who know the exemption reason that a butcher selling only Brennmark-born meat would say so, so an unlabeled counter is more likely mixed (A-14, p = 0.55). Given that inference, the butchers who sell only Brennmark-born meat lose sales by staying silent, and K4 lets them label voluntarily; those for whom the label costs less than the lost sales do it (CR-4, x: stay silent, y: label; A-15). That makes silence more informative still. The sellers' response is now stated in CR-11's 0.9 clarification and in EN-15; it is CR-4 applied to the exempt sellers.

**Routing around the label (C-16, C-17).** Processed meat and food service are outside K1. Meat from Quorra-born animals that would sell at a discount at retail is routed into sausages and cooked products where processing costs less than the discount (C-16, RS-5; A-33, the premise RS-5's "Assumes" requires) and sold to food service (C-17). The routing rests on the demand chain (A-3, A-4), not on K2's per-head cost: K2's records apply to every animal slaughtered, whatever form its meat later takes. For food service the relative price of mixed-origin meat falls (section 6), and buyers who do not value origin (A-16) take more of it (CR-4). RS-1's 0.8 clarification asks for a supply premise before signing a traded quantity: here the supply is the meat diverted from retail, so it can expand.

**Mislabeling (C-18).** Where Brennmark meat sells at a premium (C-34), labeling mixed meat as Brennmark gains the premium. Origin cannot be detected by testing the meat, only by audits of records (A-17), so some sellers do it (CR-4, x: comply, y: violate). The trade stays in the legal market: `legal_breach`.

**Lobbying (C-19, C-46).** The Act's opponents lobby on questions that exist only under it: the reading of U1, the level of the threshold, and repeal (C-19; RS-7, A-18). The breeders who campaigned for the bill now lobby to extend K1 to processed meat and food service. But without the Act they would presumably still be lobbying for an origin law (A-35), so RS-7's Unless clause applies: against that baseline, the breeders' effort may rise or fall, and C-46 is `ambiguous` without a premise comparing the two.

**Ground meat under U1 (C-20, C-21).** Under U1-a, a grinder may label every batch with the plant's 60-day list, so it need not segregate trim by batch (no change in that cost), and the label does not distinguish one batch from another (no change in that information; the plant-level list is part of C-1). Under U1-b, each batch states its origins, so trim is segregated per batch (C-20) and buyers can tell batches apart (C-21). The demand chain into C-16 operates under both readings: a "may contain Quorra" list also deters origin-minded buyers.

**Timing (C-22 to C-24).** K5 lets frozen meat from animals slaughtered before 1 January 2027 be sold unlabeled until mid-2028. Mixed plants slaughter Quorra-born animals that are near slaughter weight before the end of 2026 (A-34) and freeze part of the meat, where freezing and storage cost less than the discount (C-22, C-23; A-19). Fresh meat from animals slaughtered in January to June 2027 is sold before K1 applies, so the rush rests on avoiding K2's per-head cost (A-5) and on K5's window for frozen meat sold after July 2027 (A-3, A-4), not on the label as such. C-22 is signed on a flow (animals slaughtered in the window). Feeder calves imported from mid-2026 will be slaughtered after January 2027, so importers bring in fewer from announcement on (C-24, CR-10a). RS-8's 0.8 Unless clause asks whether any provision improves the earlier window in a way that opposes the timing chain. K5 improves the earlier window, but in the same direction as the rush, so the chains do not oppose. The late-2026 rise in slaughter of Quorra-born animals moves slaughter from 2027 into 2026; 2027 slaughter of Quorra-born animals falls for that reason and for C-8, both the same sign.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-25 | `breeders.quorra` | `net_price_received` (feeders and weaners sold to Brennmark) | decrease | short–medium | CR-9, CR-6, CR-7b | Quorra-born and Brennmark-born feeders: `substitute`, close; feeders `input_to` meat | A-6, A-21; A-5 or (A-3, A-4) |
| C-26 | `breeders.quorra` | `quantity_supplied` (live animals exported to Brennmark) | decrease | short–medium | CR-4, CR-9, OC-4 | as C-25 | A-6; A-5 or (A-3, A-4) |
| C-27 | `processors.quorra` | `quantity_supplied` (boxed meat from Quorra-born and Quorra-raised animals, exported to Brennmark) | increase | medium | RS-4, CR-4, CR-7a | live animals and boxed meat: `substitute`, partial; `across_border` | A-22 |
| C-28 | `sellers.foreign` (Quorra: breeders and processors together) | `quantity_traded` (live animals and meat sold to Brennmark) | ambiguous | medium | CR-12b (0.8, kind 2) | as C-26, C-27 | A-22; A-5 or (A-3, A-4) |
| C-29 | `breeders.domestic` | `net_price_received` (Brennmark-born calves and weaners) | increase | short–medium | CR-9, RS-16 (0.9, costs on the substitute), CR-6, CR-12b, CR-12e | as C-25 | A-6, A-23, A-32; A-5 or (A-3, A-4) |
| C-30 | `breeders.domestic` | `asset_value` (breeding herds, pasture) | increase | short (from March 2026) | SB-4, CR-7c, CR-10c | — | A-23, A-24, A-32; A-5 or (A-3, A-4) |
| C-31 | `breeders.domestic` | `quantity_supplied` (calves and weaners) | increase | medium–long | CR-4, CR-10b, TS-1 | — | A-25, A-32; A-5 or (A-3, A-4) |
| C-32 | `feedlots.border` | `return_on_capital` | decrease | short–medium | CR-7b, CR-9 | Quorra feeders `input_to` finished cattle | A-26; A-5 or (A-3, A-4) |
| C-33 | `feedlots.border`, `processors.mixed` (owners) | `asset_value` | decrease | short (from March 2026) | CR-7c, CR-10c | — | A-24, A-26 |
| C-34 | `buyers.origin_minded` | `price_paid` (meat labeled "Brennmark") | increase | short–medium | CR-6, RS-16, RS-14, CR-12d | — | (A-3, A-4, A-23) or A-27 |
| C-35 | `buyers.retail_meat` | `price_paid` (mixed-origin meat at labeled retailers) | ambiguous | short–medium | CR-6, RS-14, CR-12b (0.8, kind 2) | — | A-3, A-4, A-27 |
| C-36 | `food_service` | `price_paid` (mixed-origin meat) | ambiguous | short–medium | CR-6, RS-13, RS-14, CR-12b | retail and food service: `same_market_other_segment` | A-3, A-4, A-16, A-27 |
| C-37 | `butchers.exempt` | `quantity_traded` (covered meat sold) | ambiguous | short–medium | CR-9, CR-11c (0.7 silence), CR-4, CR-12b (0.8, kind 2) | exempt and labeled butchers: `substitute`, close | A-14, A-27, A-28 |
| C-38 | `retailers.labeled` (owners) | `asset_value` | decrease | short (from March 2026) | CR-7c, CR-10c, CR-7b | — | A-24, A-31 |
| C-39 | `breeders.quorra` (owners) | `asset_value` (herds and land oriented to export to Brennmark) | decrease | short (from March 2026) | CR-7c, CR-10c | — | A-21, A-24 |
| C-40 | `butchers.near_threshold` (owners) | `asset_value` | ambiguous | short (from March 2026) | RS-17 (0.9), CR-7c, CR-9, CR-12b | as C-37 | A-11, A-27 |
| C-47 | `feedlots.border` (owners of Quorra-born animals on feed from March 2026 and slaughtered from January 2027) | `asset_value` (animals on feed) | decrease | short (March to December 2026) | CR-7c (0.9, inventories), CR-10a, CR-10c | Quorra-born animals `input_to` meat | A-5 or (A-3, A-4) |
| C-48 | `processors.mixed`, `processors.single` | `quantity_traded` (animals slaughtered in Brennmark, all origins, from January 2027) | decrease | short–medium | CR-9, CR-12a | Quorra-born and Brennmark-born animals `input_to` slaughter | A-6, A-23; A-5 or (A-3, A-4) |

**A tariff-like burden without a tax (C-25, C-26, C-39).** TX-7's preconditions are not met: there is no tariff and no revenue. But K2 and K3 attach a cost per head to handling Quorra-born animals that Brennmark-born animals mostly do not bear (A-5), and K1 lowers retail demand for their meat (C-6). From the processors' side, a Quorra-born animal now brings less net of handling, so they offer less for it (CR-6 in the feeder market). Who bears the gap is CR-7b: Quorra breeders' alternatives (finishing at home, selling into Quorra's smaller market, other export markets) are clearly worse than the processors' alternative (Brennmark-born animals, A-6), so they bear more of it (A-21). The fall is capitalized into the value of herds and land oriented to export, from the bill's introduction (C-39, CR-7c). Unlike a tariff, nothing is collected: the cost to Quorra breeders is a fall in their price, matched not by revenue but by resources used up in tracing (CR-8c) and by buyers who move away. The prevented sales (C-26) are lost exchanges for both sides (OC-4).

**The domestic side (C-29 to C-31).** Processors turn to Brennmark-born animals (CR-9, substitute). Herds cannot grow within a breeding cycle (two to three years for cattle, about a year for sows; A-23), so the price rises (RS-16). An opposing chain reaches the same key: K2 attaches about $1.20 per head of records to Brennmark-born animals too, which lowers what plants bid for every animal (CR-9, LW-10; RS-16's 0.9 clause on costs attached to the substitute). The premium per animal far exceeds $1.20 a head (A-32, an empirical dominance premise under CR-12e), so the combined sign is `increase` (section 7). The expected gain is capitalized into herds and pasture from the bill's introduction (C-30, SB-4). Herds expand over the cycle where the gain lasts (C-31, A-25, TS-1); C-29 is signed for the short and medium run only, since the response argument would show only that herd growth cannot push the price below its old level (CR-12, 0.9).

**Border feedlots and plants (C-32, C-33).** They are specialized in Quorra-born animals by location (A-26). The feeders they buy are cheaper (C-25), but the animals they sell are worth less to processors, and switching to Brennmark-born calves costs them more (C-29). By CR-7b, specific capital with few alternatives bears part of the gap; their returns fall until capital moves (C-32), and the loss is capitalized when the Act becomes expected (C-33). Quorra-born animals already on feed when the bill became expected (from March 2026) and slaughtered from January 2027 are inventories that take time to finish, durable assets under CR-7's 0.9 clarification: their owners bear the expected discount and K2's cost at once (C-47; CR-7c, CR-10a). With six to nine months of finishing, animals placed before about April 2026 are mostly slaughtered before January 2027; the loss falls on those who held animals placed later while passage became likely, between March and July 2026 (CR-7c, probability clause).

**Total slaughter (C-48).** From January 2027 mixed plants take fewer Quorra-born animals (C-8), and Brennmark herds cannot grow within the breeding cycle (A-23), so fewer Brennmark-born animals cannot replace them: total slaughter in Brennmark falls in the short and medium run (CR-9, CR-12a). The late-2026 window is signed separately (C-22, CR-12g and h); in the long run herd growth (C-31) opposes the fall and no sign is given.

**Retail prices (C-34 to C-36).** For Brennmark meat, both chains push up: demand rises against a supply that cannot grow at once (C-7, A-23), and the per-animal and per-unit costs of tracing and labeling are passed partly into prices, since nearly all competitors are bound (RS-14, A-27). For mixed-origin meat at labeled retailers, demand falls (C-6) while the cost per unit rises (A-27): opposite chains, both derived, with premises at or above 0.5 (CR-12 0.8, kind 2), so `ambiguous`. For food service the same holds, with diverted supply in place of the retail demand fall (RS-13). The costs fixed per item, per outlet and per firm (C-5, C-11) are not used in these signs: CR-4's 0.8 clarification allows that only with a premise about entry and exit, and the case does not need one, since the per-unit chain already signs the cost side.

**Exempt butchers (C-37).** Two chains push their sales up: labeled rivals' prices rise with costs exempt butchers do not bear (A-27), and they can buy mixed-origin meat at the discount without labeling it (A-28). One pushes down: shoppers who read silence as "mixed" move to labeled sellers (A-14). Each is derived and each premise is at least 0.5, so by CR-12's 0.8 clarification (kind 2) the sign is `ambiguous`.

**Total trade with Quorra and the currency link (C-27, C-28).** Live animal exports fall (C-26). Some Quorra breeders instead finish and slaughter at home and export boxed meat, which is single-origin "Product of Quorra" and needs no segregation in Brennmark (C-27, RS-4; A-22, p = 0.55). Total sales by Quorra to Brennmark therefore have opposite chains, both above the cut-off: `ambiguous` (C-28). The currency link (CR-9, 0.7) would carry a fall in imports to Brennmark's exporters; since the first link's own sign is ambiguous, it is a kind 3 chain under CR-12's 0.8 clarification, and the link to `exporters.brennmark` is not signed. Stopped at depth 2.

**Retailers' value (C-38).** Part of the compliance cost stays with labeled retailers at least in the short run (A-31, CR-7b), and its expected value is capitalized when the Act becomes expected.

Stopping points: the spending of food-service buyers' savings (depth 3, diffuse); Quorra's own beef prices (depth 3, a foreign market not recorded); feed suppliers to border feedlots (depth 3, diffuse; stopped). Imported boxed meat from Ardova: no new information on it (R1), and no chain derived beyond C-34's substitution, which runs toward Brennmark meat; not followed.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `processors.mixed`, `quantity_demanded` (Quorra-born animals), short–medium | — | Cost per head (A-5); demand for their meat (A-3, A-4) | CR-12a, CR-12d | **decrease** (C-8); holds if either chain's premises hold. |
| `buyers.origin_minded`, `price_paid` (Brennmark meat), short–medium | Demand shift (A-3, A-4, A-23); cost pass-through (A-27) | — | CR-12a, CR-12d | **increase** (C-34). |
| `buyers.retail_meat`, `price_paid` (mixed-origin meat), short–medium | Cost pass-through (A-27) | Demand falls (C-6) | None | **ambiguous** (C-35). CR-12 0.8 kind 2: both chains derived, both premises at least 0.5. Decided by the size of the demand fall against the cost per unit. |
| `food_service`, `price_paid` (mixed-origin meat), short–medium | Processor costs per animal passed on (A-27) | Supply diverted from retail (RS-13) | None | **ambiguous** (C-36). |
| `butchers.exempt`, `quantity_traded`, short–medium | Rivals' costs (A-27); discounted supply (A-28) | Silence read as mixed (A-14) | None | **ambiguous** (C-37). Kind 2. |
| `retailers.labeled`, `variety` (origin versions per cut), short–medium | A premium line added beside the mixed line (A-9, p = 0.4) | None against the counterfactual: without the Act each cut has one version, and A-8 keeps low-volume cuts at one | — | **Not reported** (C-10 withdrawn). The only chain that moves the count is below the cut-off; it is a conditional possibility (section 10). |
| `sellers.foreign` (Quorra), `quantity_traded`, medium | Boxed meat in place of live animals (A-22) | Fewer live animals (C-26) | None | **ambiguous** (C-28). The currency link built on it is kind 3 and is not signed. |
| `butchers.near_threshold`, `asset_value`, short | Labeled rivals bear costs these butchers do not (CR-9, CR-7c; A-27) | The value of growing past the threshold falls (RS-17) | None | **ambiguous** (C-40). RS-17's 0.9 clause on the value of firms near the line now gives the same sign; under 0.8 it gave a decrease (Gaps found, c1). |
| `breeders.domestic`, `net_price_received`, short–medium | Processors turn to Brennmark-born animals with herds fixed (A-6, A-23; A-5 or (A-3, A-4)) | K2's record cost of about $1.20 per head on Brennmark-born animals (CR-9, LW-10; RS-16, 0.9) | A-32 (empirical, p = 0.75): the premium per animal exceeds the $1.20 per head (CR-12e) | **increase** (C-29). |
| `breeders.domestic`, `lobbying_effort`, medium | Lobbying to extend K1 (A-18) | No campaign for an origin law, which they would have run without the Act (A-35) | None | **ambiguous** (C-46). RS-7, Unless. |
| `processors.mixed`, `processors.single`, `quantity_traded` (all animals slaughtered), from January 2027, short–medium | — | Fewer Quorra-born animals (C-8); herds fixed (A-23) | CR-12a | **decrease** (C-48). The late-2026 window is C-22 (CR-12g); the long run is not signed (herd growth, C-31, opposes). |
| `buyers.origin_minded`, welfare of choices made with the label | — | — | — | **Not signed.** The label adds and removes no option (CR-1, 0.7), so CR-3 cannot say whether a buyer who switches to Brennmark meat at a higher price is better off by their own ranking than when they bought mixed meat believing it Brennmark-born. This is `06_gaps.md`, Q22. |
| `buyers.origin_indifferent`, welfare | — | — | — | **Not signed.** They are worse off by CR-3a only if a price they pay rises; the mixed-origin price is ambiguous (C-35), and they can buy mixed meat. |
| `processors.mixed`, `quantity_traded` (Quorra-born animals slaughtered), by window | July to December 2026: rush before K2 (C-22) | 2027 on: C-8, and slaughter moved into 2026 | — | Signed per window: increase in late 2026 (C-22), decrease from 2027 (C-8). Not netted (CR-12g). |

Final check (workflow): (1) every key with opposite chains is ambiguous or has a stated dominance premise; (2) the margins of processors' response are signed per variable, each with its own premises; (3) every sign is against Brennmark without the Act, with R1 and R2 in force; R1 already labels imported meat, so no consequence is claimed for it; (4) `resources_available_other_uses` is signed only for the general-fund payers (a sum they cannot avoid), for plants and retailers that keep bearing the tracing and labeling costs (C-43), for buyers who keep buying "Brennmark" meat at its higher price (C-49), and for fined violators; it is not signed for buyers of mixed-origin meat, whose price is ambiguous (C-35); (5) timing is signed per window; (6) both sides: the Brennmark premium is paid by origin-minded buyers (C-34) and received by domestic breeders (C-29); the fall in Quorra breeders' price is not a transfer but resources used up (C-2) and sales lost (C-26); fines are paid (C-45) and received (C-44); (7) capitalization checked for every class with specific assets, including inventories on feed (C-30, C-33, C-38, C-39, C-40, C-47); (8) every premise is in section 10.

## 8. Time structure

- **Announcement (March to June 2026).** Breeding herds and pasture gain value, and border feedlots, mixed plants, labeled retailers and Quorra export herds lose value, part of the way from the bill's introduction as passage becomes likely, and the rest at signing (CR-7c's probability clause; C-30, C-33, C-38, C-39). Quorra-born animals on feed that will be slaughtered from January 2027 lose value in the same way (C-47). Feeder imports fall at once for animals that will be slaughtered after January 2027 (C-24).
- **Measuring year (July 2026 to June 2027).** Butchers near $1.0 million manage turnover and split shops in this year, before any label is required (C-12, C-13; RS-17).
- **Late 2026.** Quorra-born animals ready before January are slaughtered and part of the meat frozen for sale unlabeled until mid-2028 (C-22, C-23). Frozen stocks are run down through the first labeling year.
- **2027.** Records apply from January; plants that handle few Quorra animals stop taking them (C-9), and total slaughter falls against the counterfactual until herds grow (C-48). Labels apply from July; demand shifts (C-6, C-7) and prices follow.
- **Over the breeding cycle (2027 to 2030).** Brennmark herds expand (C-31), and the domestic premium narrows as supply catches up (TS-1); the sign of C-29 is for the short to medium horizon only. Quorra plants that take on finishing and slaughter for export do so as capacity allows (C-27).
- **Erosion of the threshold.** The $1.0 million threshold is fixed in money and not indexed (TS-3). As prices and sales rise, more butchers cross it, so the share of retail meat sold under the exemption shrinks over time.
- **U1.** Until the FSA or a court decides between U1-a and U1-b, grinders who segregate per batch bear a cost that may prove unnecessary, and those who do not risk fines; the two readings' signs (C-20, C-21) hold once the question is settled.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-41 | `officials.enforcement` | `enforcement_cost` | increase | Audits of records at plants, importers and retailers. No existing enforcement is made unnecessary: R1 is enforced as before (OC-3, right baseline). | OC-3 |
| C-42 | `taxpayers`, recipients of other general-fund spending | `resources_available_other_uses` | at_least_one_decrease | What the $5.2 million a year would otherwise have funded. The record names no tax, so the payers are a group. | OC-1, OC-3, CR-8b |
| C-43 | `processors.mixed` (plants that keep both origins), `processors.single`, `retailers.labeled` | `resources_available_other_uses` | decrease | What the per-head, per-plant, per-item and per-outlet tracing and labeling costs would otherwise have bought. Plants and retailers that keep slaughtering and selling covered meat keep paying them (CR-3, note). | OC-1, CR-8a, CR-3c |
| C-44 | `officials.enforcement` (the state) | `non_tax_receipts` (fines) | increase | Nothing: a receipt. | CR-8b |
| C-45 | `processors.mixed`, `retailers.labeled` (those fined) | `resources_available_other_uses` | decrease | What the fines would otherwise have bought. | CR-8b, CR-3c |
| C-49 | `buyers.retail_meat` (those who keep buying meat labeled "Brennmark") | `resources_available_other_uses` | decrease | Other purchases forgone because the same meat costs more (C-34). Not signed for buyers of mixed-origin meat, whose price is ambiguous (C-35). | CR-3 (note), CR-8a |

The compliance costs C-2 to C-5, C-14 and C-20 are means used up (CR-8c), whatever they would otherwise have done (OC-2). Live-animal sales that no longer take place (C-26) are prevented exchanges: breeders and processors each lose the gain they expected from them (OC-4). Labor in border feedlots and plants follows their output down and labor at domestic herds follows it up (OC-5); not recorded separately, since the case gives no premise on how sellers adjust labor, and the sign of each output change is already recorded.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Retailers at or above the threshold label as required. | enforcement | 0.8 | Supermarket chains' central labeling systems; FSA audit plan. | C-1, C-6, C-7, C-11, C-21 weaken to compliant sellers. |
| A-2 | Records and audits keep labels mostly accurate. | enforcement | 0.75 | R2 passports for cattle; audit frequency. | C-1 and C-21 weaken; C-18 is larger. |
| A-3 | Many shoppers believed "Product of Brennmark" meant Brennmark-born (prior belief, CR-11 0.7). | other | 0.85 | Consumer Council survey: 64%. | The label is no news; C-6, C-7 and every chain that rests on them fail; only the cost chains remain. |
| A-4 | Shoppers who learn that meat is from Quorra-born animals move away from it, toward Brennmark meat (direction, CR-11 0.7). | other | 0.7 | Survey: 41% would pay more for fully domestic meat; 3% prefer Quorra-born. | As A-3. |
| A-5 | At mixed plants, handling a Quorra-born animal costs more than a Brennmark-born one. | other | 0.9 | Impact assessment: $9 against $1.20 a head for cattle. | The cost chains fail; C-8, C-22, C-24 to C-33, C-47 and C-48 rest on the demand chain alone. |
| A-6 | Brennmark-born animals are close substitutes for Quorra-born ones for feedlots and processors. | substitutability | 0.9 | Same breeds and weights; existing trade in both. | C-8, C-25, C-26, C-29 are not reported. |
| A-7 | Some mixed plants take few Quorra-born animals, so running two origin streams costs more than they gain from them. | other | 0.75 | Share of Quorra animals by plant. | C-9 is not reported. |
| A-8 | For low-volume cuts, a second origin version costs a retailer more (template, tag, inventory line) than it gains. | other | 0.7 | Retailers' range reviews; sales per cut. | No reported consequence rests on it (C-10 withdrawn). If false, more cuts may carry two versions; see A-9. |
| A-9 | Retailers add a premium "Brennmark" line beside the mixed line for many cuts. | other | 0.4 | Experience with premium labels; shelf space. Below the cut-off. | Not reported. If true, `variety` (origin versions per cut) increases for those cuts: a conditional possibility. |
| A-10 | Some service counters are marginal, so records per outlet decide whether they stay open. | other | 0.6 | Counter sales by store size. | C-11 is not reported. |
| A-11 | For some butchers near $1.0 million, labeling costs more than the gain from growing past the line. | binding | 0.6 | Butchers' margins; per-outlet costs. | C-12, C-13 and the (−) chain of C-40 are not reported. |
| A-12 | Butchers know during the measuring year that it decides their status. | expectations | 0.75 | Act signed 1 July 2026; association guidance. | C-12 starts in 2027–28 instead. |
| A-13 | Splitting a shop into a separately registered entity is legal and cheap enough for some. | other | 0.6 | K4 counts per registered entity. | C-13 is not reported. |
| A-14 | Some shoppers know the exemption and infer from an exempt butcher's silence that its meat may be mixed (CR-11 0.7, silence). | other | 0.55 | Publicity of the Act; survey on label reading. | C-14 and C-15 are not reported; C-37 becomes an increase. |
| A-15 | Exempt butchers may label voluntarily, and for those selling only Brennmark-born meat the label costs less than the sales lost to silence. | other | 0.6 | K4; label costs per shop. | C-14 is not reported; C-15 rests on silence alone. |
| A-16 | Food-service buyers place little value on origin, and menus carry none. | other | 0.75 | Food-service purchasing practice. | C-17 and C-36 are not reported. |
| A-17 | Origin cannot be detected by testing the meat, only by audits of records, which sample. | enforcement | 0.8 | No laboratory test for country of birth; audit plan. | C-18, C-44, C-45 are not reported. |
| A-18 | Breeders, processors, importers and Quorra's government can organize at a cost below their stake. | other | 0.85 | Existing associations; the breeders' campaign for the bill. | C-19 and C-46 are not reported. |
| A-19 | For some processors, freezing and storing meat from Quorra-born animals slaughtered in 2026 costs less than the expected discount. | other | 0.55 | Cold storage costs; frozen share of retail beef. | C-22 and C-23 are not reported. |
| A-20 | Buyers of feeders in 2026 expect the discount to apply when the animals are slaughtered. | expectations | 0.8 | Finishing takes six to nine months; Act signed July 2026. | C-24 is not reported. |
| A-21 | Quorra breeders' alternatives to selling to Brennmark are clearly worse than processors' alternatives (Brennmark-born animals). | mobility | 0.65 | Size of Quorra's own market; distance to other markets. | C-25 holds as a direction only; C-39 is not reported. |
| A-22 | Some Quorra animals are finished and slaughtered in Quorra and exported as boxed meat instead. | mobility | 0.55 | Spare capacity at Quorra plants. | C-27 is not reported; C-28 becomes a decrease. |
| A-23 | Brennmark herds cannot grow within a breeding cycle. | durability | 0.9 | Gestation and rearing times. | C-29 and C-30 weaken; the demand chain of C-34 fails; C-48 is not reported. |
| A-24 | Owners expect the Act to stay in force for years. | expectations | 0.75 | Cross-party support; no expiry. | C-30, C-33, C-38, C-39 are not reported. |
| A-25 | Breeders expand herds where the premium lasts (pasture and sow places are available). | alternative_uses | 0.65 | Land use; herd trends. | C-31 is not reported. |
| A-26 | Border feedlots and plants are specialized in Quorra-born animals by location, and Brennmark-born calves cost them more to obtain. | other | 0.7 | Location and sourcing data. | C-32 and C-33 are not reported. |
| A-27 | Per-animal and per-unit tracing and labeling costs are passed partly into retail and wholesale prices; nearly all competitors of labeled sellers are bound. | other | 0.65 | 91% of retail meat sold by bound sellers. | One chain of C-34 fails; C-35 and C-36 become decreases; C-37 and C-40 lose a (+) chain. |
| A-28 | Exempt butchers can buy mixed-origin meat at the discount without labeling it. | other | 0.7 | Wholesale price lists by origin. | One (+) chain of C-37 fails. |
| A-29 | The $5.2 million is new money from the general fund. | revenue_use | 0.9 | K6. | C-42 is not reported; some other use of the FSA's time falls instead, as a group (OC-3, fixed budget, 0.9). |
| A-30 | Some violations are detected and fined. | enforcement | 0.6 | Audit plan; penalty schedule. | C-44 and C-45 are not reported. |
| A-31 | Part of the compliance cost stays with labeled retailers in the short run. | other | 0.75 | Competition among the three chains. | C-38 is not reported. |
| A-32 | The premium processors pay for a Brennmark-born animal exceeds the record cost of about $1.20 per head (and its pig equivalent) that K2 attaches to it. | other | 0.75 | 41% of shoppers say they would pay more for fully domestic meat; $1.20 spread over a steer's retail yield is well under one cent per kg. Added after the core-only comparison. | C-29 becomes `ambiguous`; C-30 and C-31 lose their premise. |
| A-33 | For some cuts from Quorra-born animals, selling them in processed form (exempt from K1) costs less than the retail discount. | other | 0.55 | Existing seasoned and cured lines; K1's exemption for processed meat. Added after the core-only comparison. | C-16 is not reported. |
| A-34 | Some Quorra-born animals on feed in late 2026 are near enough to slaughter weight that slaughtering them before 1 January 2027 costs less than the expected discount and K2 cost. | other | 0.6 | Continuous placements over six to nine months of finishing. Added after the core-only comparison. | C-22 is not reported. |
| A-35 | Without the Act, the breeders' association would still be lobbying for an origin law. | other | 0.7 | Its campaign for the bill; the survey's support for domestic labels. Added after the core-only comparison. | C-46 becomes an increase. |

## 11. Report

**The policy.** From July 2027, Brennmark requires retailers to label beef, pork and lamb cuts and ground meat with the country where the animals were born, raised and slaughtered, with a "Mixed origin" category that lists each stage. Processors and importers of live animals must keep records tracing each animal from January 2027. Retailers with turnover under $1.0 million, processed meat and food service are exempt. It is not yet settled whether ground meat may carry a "may contain" list of origins (U1).

**Visible consequences.** Shoppers at labeled retailers learn the origin of the animals (C-1). Processors, importers and retailers bear the cost of producing that information (C-2 to C-5).

**Invisible consequences.**
- *Buyers.* Shoppers who believed "Product of Brennmark" meant Brennmark-born, and prefer it, buy less mixed-origin meat and more Brennmark meat (C-6, C-7), which costs more (C-34), so those who keep buying it have less for other things (C-49). Whether mixed-origin meat costs more or less is ambiguous (C-35). Some service counters close (C-11). The analysis makes no claim about the number of origin versions per cut (C-10 withdrawn). Some meat from Quorra-born animals is sold as Brennmark meat (C-18).
- *Quorra.* Quorra breeders get less for the feeders and weaners they sell to Brennmark (C-25), sell fewer (C-26) and see their export herds lose value (C-39): a burden like a tariff's, with no revenue collected. Some Quorra animals are slaughtered at home and exported as boxed meat instead (C-27), so whether Brennmark's total imports from Quorra fall is ambiguous (C-28).
- *Brennmark breeders and border businesses.* Breeders get more for their calves and weaners (C-29), since the premium outweighs the record cost K2 attaches to their animals too (A-32); their herds and pasture gain value from the bill's introduction (C-30), and herds grow over the breeding cycle (C-31). Border feedlots and mixed plants lose returns and value (C-32, C-33), and owners of Quorra-born animals on feed when the bill became likely bear the expected discount (C-47); some plants stop taking Quorra animals at all (C-9). Total slaughter in Brennmark falls from 2027 until herds grow (C-48).
- *Routing around the label.* Meat from Quorra-born animals moves into processed products and food service (C-16, C-17), where its price may rise or fall (C-36).
- *Small butchers.* Butchers near $1.0 million stay below it or split their shops, during the year that is measured (C-12, C-13). Exempt butchers who sell only Brennmark meat label it voluntarily (C-14), so buyers learn something from their silence too (C-15). Whether exempt butchers sell more or less is ambiguous (C-37), and so is the value of butchers near the line (C-40).
- *Timing.* Quorra-born animals are rushed to slaughter in late 2026, and their meat frozen for sale unlabeled under the transition rule (C-22, C-23); feeder imports fall from mid-2026 (C-24).
- *Costs and transfers.* Enforcement (C-41), paid by taxpayers or recipients of other general-fund spending (C-42); tracing and labeling costs that plants and retailers keep paying (C-43); fines (C-44, C-45); labeled retailers' value (C-38).
- *Lobbying.* The Act's opponents lobby on the ground-meat reading, the threshold and repeal (C-19). Whether the breeders lobby more or less than they would have done without the Act, when they would have been campaigning for it, is ambiguous (C-46).
- *Ground meat.* If cost is enough to justify a "may contain" list (U1-a), grinders need not segregate per batch and buyers cannot tell batches apart; if not (U1-b), they segregate and buyers can (C-20, C-21).

**Ambiguous effects.** The price of mixed-origin meat at retail and in food service (C-35, C-36); exempt butchers' sales (C-37) and the value of butchers near the threshold (C-40); total trade with Quorra (C-28), and so its effect on Brennmark's exporters; breeders' lobbying against the counterfactual (C-46).

**Key conditions.** Every demand-side consequence rests on two premises CR-11 requires: that shoppers believed "Product of Brennmark" meant Brennmark-born (A-3, p = 0.85) and that those who learn otherwise move toward Brennmark meat (A-4, p = 0.7). The processor-side consequences hold on the cost of handling Quorra-born animals alone (A-5, p = 0.9). The burden on Quorra rests on its breeders' alternatives being worse than Brennmark processors' (A-21, p = 0.65). The inference from silence is the weakest link (A-14, p = 0.55).

**What this analysis cannot say.** How large any effect is; whether shoppers who switch after reading a label are better off by their own ranking (Q22); whether the information is worth what it costs to produce; any effect on food safety, animal health or disease tracing (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | buyers.retail_meat | quality_information (origin of animals) | increase | short | visible | B | CR-1, CR-11c, EN-15 | A-1, A-2 |
| C-2 | processors.mixed | compliance_cost (tracing and segregation) | increase | short | invisible | A | CR-1, CR-8c, OC-2 | none |
| C-3 | processors.single | compliance_cost (passports and records) | increase | short | invisible | A | CR-1, CR-8c, OC-2 | none |
| C-4 | importers.live_animals | compliance_cost (certificates and declarations) | increase | short | invisible | A | CR-1, CR-8c, OC-2 | none |
| C-5 | retailers.labeled | compliance_cost (per item, per outlet, per firm) | increase | short | invisible | A | CR-1, CR-8c, OC-2, EN-15 | none |
| C-6 | buyers.origin_minded | quantity_demanded (mixed-origin meat) | decrease | short | invisible | B | CR-11c, CR-4, EN-15 | A-1, A-2, A-3, A-4 |
| C-7 | buyers.origin_minded | quantity_demanded (Brennmark meat) | increase | short | invisible | B | CR-11c, CR-4, EN-15 | A-1, A-2, A-3, A-4 |
| C-8 | processors.mixed | quantity_demanded (Quorra-born animals) | decrease | short–medium | invisible | B | CR-4, CR-4c, CR-9, CR-12d | A-6; A-5 or (A-3, A-4) |
| C-9 | processors.mixed | number_of_sellers (plants handling both origins) | decrease | short–medium | invisible | B | CR-4, CR-7a | A-5, A-7 |
| C-11 | retailers.labeled | number_of_sellers (outlets with service counters) | decrease | medium | invisible | B | CR-4, CR-7a | A-1, A-10 |
| C-12 | butchers.near_threshold | number_of_sellers (just below $1.0m, relative to just above) | increase | short–medium | invisible | B | RS-17, CR-4, CR-10a | A-11, A-12 |
| C-13 | butchers.near_threshold | reclassification (split entities) | increase | short–medium | invisible | B | RS-17, RS-5 | A-11, A-13 |
| C-14 | butchers.exempt (only Brennmark-born meat) | compliance_cost (voluntary labels) | increase | short–medium | invisible | B | CR-11c, CR-4, EN-15 | A-14, A-15 |
| C-15 | buyers.exempt_butchers | quality_information (labels and silence) | increase | short–medium | invisible | B | CR-11c, CR-4, EN-15 | A-14, A-15 |
| C-16 | processors.mixed, processed_meat_makers | reclassification (into processed products) | increase | short–medium | invisible | B | RS-5, CR-4 | A-3, A-4, A-33 |
| C-17 | food_service | quantity_traded (mixed-origin meat) | increase | short–medium | invisible | B | CR-4, CR-9, RS-1 | A-3, A-4, A-16 |
| C-18 | processors.mixed, retailers.labeled | legal_breach (mislabeled origin) | increase | short–medium | invisible | B | CR-4, CR-1, RS-3 | A-3, A-4, A-17 |
| C-19 | processors.mixed, importers, Quorra's government | lobbying_effort (U1, threshold, repeal) | increase | medium | invisible | B | RS-7, CR-12 | A-18 |
| C-20 | processors.mixed (grinders) | compliance_cost (per-batch segregation of trim) | U1-a: no_change; U1-b: increase | short | invisible | B | CR-1, CR-8c | A-2 |
| C-21 | buyers.retail_meat | quality_information (origin of a given ground-meat batch) | U1-a: no_change; U1-b: increase | short | invisible | B | CR-11c | A-1, A-2 |
| C-22 | processors.mixed | quantity_traded (Quorra-born animals slaughtered, July–December 2026) | increase | short | invisible | B | RS-8, CR-10a | A-19, A-34; A-5 or (A-3, A-4) |
| C-23 | processors.mixed | inventory_held (frozen unlabeled meat, end 2026) | increase | short | invisible | B | RS-8, CR-10a | A-19 |
| C-24 | importers.live_animals | quantity_traded (Quorra feeders imported from mid-2026) | decrease | short | invisible | B | CR-10a, CR-4 | A-20; A-5 or (A-3, A-4) |
| C-25 | breeders.quorra | net_price_received (feeders and weaners sold to Brennmark) | decrease | short–medium | invisible | B | CR-9, CR-6, CR-7b | A-6, A-21; A-5 or (A-3, A-4) |
| C-26 | breeders.quorra | quantity_supplied (live exports to Brennmark) | decrease | short–medium | invisible | B | CR-4, CR-9, OC-4 | A-6; A-5 or (A-3, A-4) |
| C-27 | processors.quorra | quantity_supplied (boxed meat to Brennmark) | increase | medium | invisible | B | RS-4, CR-4, CR-7a | A-22 |
| C-28 | sellers.foreign (Quorra) | quantity_traded (live animals and meat sold to Brennmark) | ambiguous | medium | invisible | B | CR-12b | A-22; A-5 or (A-3, A-4) |
| C-29 | breeders.domestic | net_price_received (calves and weaners) | increase | short–medium | invisible | B | CR-9, RS-16, CR-6, CR-12b, CR-12e | A-6, A-23, A-32; A-5 or (A-3, A-4) |
| C-30 | breeders.domestic | asset_value (herds, pasture) | increase | short | invisible | B | SB-4, CR-7c, CR-10c | A-23, A-24, A-32; A-5 or (A-3, A-4) |
| C-31 | breeders.domestic | quantity_supplied (calves and weaners) | increase | medium–long | invisible | B | CR-4, CR-10b, TS-1 | A-25, A-32; A-5 or (A-3, A-4) |
| C-32 | feedlots.border | return_on_capital | decrease | short–medium | invisible | B | CR-7b, CR-9 | A-26; A-5 or (A-3, A-4) |
| C-33 | feedlots.border, processors.mixed (owners) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c | A-24, A-26 |
| C-34 | buyers.origin_minded | price_paid (Brennmark meat) | increase | short–medium | invisible | B | CR-6, RS-16, RS-14, CR-12d | (A-3, A-4, A-23) or A-27 |
| C-35 | buyers.retail_meat | price_paid (mixed-origin meat) | ambiguous | short–medium | invisible | B | CR-6, RS-14, CR-12b | A-3, A-4, A-27 |
| C-36 | food_service | price_paid (mixed-origin meat) | ambiguous | short–medium | invisible | B | CR-6, RS-13, RS-14, CR-12b | A-3, A-4, A-16, A-27 |
| C-37 | butchers.exempt | quantity_traded (covered meat) | ambiguous | short–medium | invisible | B | CR-9, CR-11c, CR-4, CR-12b | A-14, A-27, A-28 |
| C-38 | retailers.labeled (owners) | asset_value | decrease | short | invisible | B | CR-7c, CR-10c, CR-7b | A-24, A-31 |
| C-39 | breeders.quorra (owners) | asset_value (export herds and land) | decrease | short | invisible | B | CR-7c, CR-10c | A-21, A-24 |
| C-40 | butchers.near_threshold (owners) | asset_value | ambiguous | short | invisible | B | RS-17, CR-7c, CR-9, CR-12b | A-11, A-27 |
| C-41 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-42 | taxpayers, recipients of other general-fund spending | resources_available_other_uses | at_least_one_decrease | short | invisible | B | OC-1, OC-3, CR-8b | A-29 |
| C-43 | processors.mixed (keeping both origins), processors.single, retailers.labeled | resources_available_other_uses | decrease | short | invisible | B | OC-1, CR-8a, CR-3c | A-5 (mixed plants) |
| C-44 | officials.enforcement (the state) | non_tax_receipts (fines) | increase | short–medium | invisible | B | CR-8b | A-17, A-30 |
| C-45 | processors.mixed, retailers.labeled (those fined) | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b, CR-3c | A-17, A-30 |
| C-46 | breeders.domestic | lobbying_effort (to extend K1, against the counterfactual campaign) | ambiguous | medium | invisible | B | RS-7, CR-4, CR-12b | A-18, A-35 |
| C-47 | feedlots.border (owners of Quorra-born animals on feed, slaughtered from January 2027) | asset_value (animals on feed) | decrease | short | invisible | B | CR-7c, CR-10a, CR-10c | A-5 or (A-3, A-4) |
| C-48 | processors.mixed, processors.single | quantity_traded (all animals slaughtered in Brennmark, from January 2027) | decrease | short–medium | invisible | B | CR-9, CR-12a | A-6, A-23; A-5 or (A-3, A-4) |
| C-49 | buyers.retail_meat (keep buying Brennmark meat) | resources_available_other_uses | decrease | short–medium | invisible | B | CR-3, CR-8a | (A-3, A-4, A-23) or A-27 |

## Corrections after the core-only comparison

Changed under catalog 0.9, after checking each comparison row against the core rules:
- **C-10 withdrawn.** It signed `variety` (origin versions per cut) as a decrease against a two-version baseline. Without the Act, under R1, each cut is sold in one version with no origin shown, so a fixed cost per version (A-8) can only keep the count from rising, and the one chain that moves it (A-9) is below the cut-off. No sign is reported. This case is not a second use of the candidate "fixed cost per item reduces variety", which 0.9 did not promote.
- **C-29.** It now combines the opposing chain from K2's record cost of about $1.20 per head on Brennmark-born animals (RS-16, 0.9, costs on the substitute) with the demand chain, under the empirical dominance premise A-32 (CR-12e). The sign stays `increase`, short to medium only; C-30 and C-31 now rest on A-32 too.
- **C-16.** It now rests on A-33 (processing costs less than the discount for some cuts), the premise RS-5's "Assumes" requires, and on the demand chain alone: K2's per-head records apply whatever form the meat later takes, so the A-5 cost chain is dropped.
- **C-22.** It now rests on A-34 (some animals near slaughter weight before January 2027). The section 5 text now says the rush rests on K2's cost and K5's frozen window, since fresh meat slaughtered in January to June 2027 is sold before K1 applies.
- **C-19 split; C-46 added.** C-19 is now the opponents' lobbying, on questions that exist only under the Act. The breeders' lobbying is C-46, `ambiguous` under RS-7's Unless clause: without the Act they would have been campaigning for an origin law (A-35).
- **C-43 widened.** Single-origin plants and labeled retailers also keep paying the tracing and labeling costs (CR-3 note), so they join mixed plants in the class.
- **Omissions added:** C-47 (Quorra-born animals on feed while passage became likely lose value, CR-7c with CR-7's 0.9 clarification on inventories; dated to animals slaughtered from January 2027, which corrects the core version's dating), C-48 (total slaughter in Brennmark falls from January 2027 in the short and medium run, without the core version's unneeded A-22; the late-2026 window stays with C-22), and C-49 (buyers who keep buying "Brennmark" meat have less for other uses, limited to them because the mixed-origin price is ambiguous).
- **0.9 citations.** EN-15 is cited for the label, the compliance cost and the responses to it (C-1, C-5 to C-7, C-14, C-15); CR-11's 0.9 clarification for the exempt sellers' response to silence; RS-17 (0.9) for C-40, whose `ambiguous` sign the corrected pattern now gives; OC-3 (fixed budget, 0.9) in A-29's "if false". Gaps found (b)2, (b)3, (c)1 and (c)4 carry their status under 0.9.

Comparison conclusions rejected or not applied:
- **C-15, C-21, C-38, C-39, C-43 (core omissions): kept.** The comparison finds the pattern version's rows valid.
- **Core C-29 (long-run breeder price `increase`): not applied.** The comparison itself finds it a core error; under CR-12's 0.9 clarification the response argument gives only "not below the old level", so C-29 stays short to medium.
- **Core C-37, C-38 (less labeled meat overall; more poultry and processed meat): not applied.** They ignore the kind 3 chain from the ambiguous mixed-origin price (C-35).
- **Core C-13, C-27, C-43, C-44 and pattern C-28, C-40 (J rows): not applied.** Recording choices that 0.9 does not settle; C-40's sign now matches RS-17 (0.9).
- **Core C-39 and C-40 (exempt butchers split by what they sell): not applied.** A V row the comparison calls the better record but lists no correction for; C-37 keeps the class as a whole, and its sign is the same as the core's for the mixed sellers.

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12 or from patterns whose preconditions held. The closest was the welfare of buyers who choose differently once they know the origin (section 7). No variable in the controlled list needed a sign there, so the method's silence is recorded as Q22, not as a gap.

**(b) Unclear core rules.**
1. *CR-11 0.7, prior beliefs differ by label category.* The "prior belief" premise had to be stated per category: the "Mixed origin" label is news to those who believed "Product of Brennmark" meant Brennmark-born, while the "Brennmark" label only confirms that belief and changes nothing for them. The clarification speaks of "what the actors believed before" as if one premise covered the whole label. Suggest: "state the prior belief for each message the policy conveys".
2. *CR-11 0.7, silence: the sellers' response.* The clarification names the buyers' inference from silence but not what exempt sellers do about it. The analysis derived voluntary labeling by those with good news from CR-4 (C-14), which makes silence more informative (C-15). That is a two-step move (inference, then response) worth stating in the clarification. (Resolved in 0.9: CR-11's clarification on sellers' response to silence, and EN-15.)
3. *CR-4 0.8, a cost fixed per origin stream.* The tracing system and separate slaughter runs are fixed per plant, but only for plants that handle a second origin. The analysis treated this as a cost of the option "handle both origins" (C-9), in line with the clarification, but the clarification lists items, outlets and firms and does not say that the same reasoning applies to any lumpy cost attached to an option within a firm. (The core-only comparison found that CR-4's paragraph on units and lumpy costs already covers it.)
4. *CR-7b with a chain of four parties.* Quorra breeder, border feedlot, processor and retailer each sit between the cost and the buyer. CR-7b asks for each pair to be ranked; the case supplied a premise for only one pair (breeders against processors, A-21), and the feedlots' share (C-32) is signed only in direction.

**(c) Missing or wrong patterns.**
1. *RS-17 overclaims on asset values.* Its preconditions hold (a turnover threshold measured over a past year), and its first two conclusions and its timing clause worked as written (C-12, C-13). Its third conclusion, "`asset_value` of firms near it decreases", I had to override: against the no-policy baseline, the policy also burdens these firms' labeled rivals, which raises their value (CR-9, CR-7c), so the sign is `ambiguous` (C-40). RS-17's "value of growing past the threshold falls" is a comparison with a firm that could grow free of the policy, not with the counterfactual. Suggest: "the value of the option to grow falls; the firm's value combines this with the gain from rivals' burden, and is `ambiguous` without a premise". (Resolved in 0.9: RS-17's clause on the value of firms near the line.)
2. *A cost attached to imported inputs by a product rule (tariff-like burden without a tax).* No pattern covers it; TX-7's preconditions are not met. Derived here from CR-4 (per-head cost), CR-6 in the feeder market, CR-7b (the side with worse alternatives bears more) and CR-7c (C-25, C-26, C-39). It differs from a tariff in that nothing is collected and the substitute route (boxed meat slaughtered abroad, C-27) may escape the cost. Candidate pattern.
3. *TX-8's preconditions are too narrow.* A non-tariff cost also reduces some imports, but TX-8 names only tariffs and quotas, and has no clause for imports that shift form (live animals to boxed meat) so that total imports are ambiguous. The currency link was not signed here (C-28).
4. *Disclosure mandate.* `02_ontology.md` lists `disclosure_mandate` as "CR-11c; candidate pattern". This is its second use after WE-035, with the same structure: two CR-11 premises, costs fixed per item, a threshold, and the welfare question left open. Proposed for promotion. (Resolved in 0.9: promoted as EN-15.)
5. *Compliance cost outside taxes.* TX-5 covers only taxes; the analysis used OC-2 and CR-8c for record-keeping under a mandate. A general compliance-cost pattern (or widening TX-5) would fit better.

**(d) Vocabulary.**
1. *Voluntary disclosure cost.* `compliance_cost` is defined for "those bound to comply"; exempt butchers who label voluntarily are not bound (C-14). Used with a qualifier.
2. *Record-keeping requirements.* No instrument type covers a traceability duty on intermediaries (K2, K3) that serves a disclosure mandate further down the chain; recorded as part of K1.
3. *Welfare of informed choice.* No variable, by design; see Q22.

**(e) Test of 0.8.**
- *CR-11 0.7, what a sign needs:* worked as written. It forced the two premises (A-3, A-4) and kept the label from being signed as a demand change on its own; it needed the per-category reading in (b)1.
- *CR-11 0.7, silence:* needed interpretation. The inference from silence is covered (A-14), but the exempt sellers' response had to be derived separately with CR-4 (b)2.
- *CR-1 0.7, information is not an operation:* worked as written (section 2).
- *CR-4 0.7, fixed costs per item:* worked as written (C-10).
- *CR-4 0.8, fixed costs per outlet and per firm, unit price only with an entry premise:* worked as written for outlets (C-11) and needed interpretation for a cost fixed per origin stream within a plant (C-9; (b)3). It also kept the fixed costs out of the retail price signs, which rest on per-unit costs alone (C-34 to C-36).
- *RS-17:* partly worked. The preconditions held; the bunching, splitting and past-period timing clauses worked as written; the asset-value conclusion gave a sign I had to override (c)1.
- *CR-12 0.8, three kinds of opposing chain:* worked as written. Kind 2 at or above 0.5 gave `ambiguous` (C-35, C-36, C-37, C-28); kind 2 below 0.5 kept the derived sign and recorded the chain (C-10, A-9); kind 3 stopped the currency link on an ambiguous first link (C-28). No kind 1 chain arose.
- *CR-12d, independent chains:* worked; the "A-5 or (A-3, A-4)" form recorded which chain each consequence can stand on.
- *RS-1 0.8, supply premise for a substitute's traded quantity:* worked as written (C-17: the supply is diverted from retail; C-29: supply cannot expand, so the price rises under RS-16).
- *RS-8 0.8, opposing timing chains:* worked as written. The check found that K5 improves the earlier window in the same direction as the rush, so nothing opposes (C-22).
- *OC-1 and OC-3 0.8, payers from a general budget are a group; the right baseline:* worked as written (C-42; C-41 notes that no existing enforcement is made unnecessary).
- *Q22:* the case needed it and the method stayed silent, as Q22 says it must until the experts decide (section 7).
- *Candidate patterns from `06_gaps.md`, 6.2e:* "Fixed cost per item reduces variety" (WE-035) was needed here (C-10); this is its second use, which promotes it. No other candidate was needed.

Re-run note: the core-only comparison contradicted the verdicts on CR-4 0.7 fixed costs per item, on kind 2 below the cut-off as applied to C-10, and on the candidate "fixed cost per item reduces variety": against the counterfactual each cut has one version with no origin shown, so a fixed cost per version cannot reduce the count; C-10 is withdrawn and the candidate was not promoted in 0.9.
