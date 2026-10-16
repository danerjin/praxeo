# WE-030 Per-tonne subsidy on wheat exports

Analyst: draft (Handbook 0.6)  |  Rule catalog version: 0.6  |  Status: awaiting expert review

A stylized policy in a fictional country. It is the mirror image of a tariff (WE-013): instead of taxing goods that come in, the state pays for goods that go out. It is a gap-probing example. It tests CR-8b and the `currency` relation run in reverse (the mirror of TX-8), CR-7a for a domestic price tied to an export price, CR-7c for farmland, and a payment conditioned on a good crossing a border, which invites trade that crosses it twice. The catalog has no pattern for an export subsidy, so most steps are derived from the core rules. Responses by foreign governments (countervailing duties, retaliation, matching subsidies) are out of scope: no rule covers them (`06_gaps.md`, Q5). The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Tarvona Grain Export Support Act.** Tarvona is a trading country of about 22 million people with its own currency, the tal (T), and a floating exchange rate. It harvests about 12 million tonnes (Mt) of wheat a year, mostly in the Eastern Plains. About 7.5 Mt is used at home (4.5 Mt milled into flour, 2.0 Mt fed to livestock, 1.0 Mt seed and other uses) and about 4.5 Mt is exported, about 6% of world wheat exports. The export price at Tarvona's ports is about T 240 per tonne; the farm-gate price is about T 220 (inland freight about T 20). About 40% of wheat land is farmed by tenants on one-year cash leases renewed each 1 October. Tarvona also exports some feed barley (about 0.8 Mt) and grows canola and pulses on land that can also grow wheat. Its other large export industries are wine and tourism; its main import-competing industries are clothing, household goods and processed foods.

Neighboring Morvia grows about 2 Mt of wheat, roughly what it uses. Tarvona and Morvia have a free trade agreement (FTA): goods of Morvian origin enter Tarvona duty-free, and milling wheat into flour confers Morvian origin on the flour. The main wheat region of the Eastern Plains lies 40 to 80 km from the Morvian border; trucking wheat across it costs about T 10 per tonne each way.

The finance minister announced the subsidy in the budget speech on 10 March of Year 1. Parliament enacted it on 20 May. It applies to wheat exported on or after 1 July of Year 1, the start of the marketing year, and expires on 30 June of Year 4. The Minister of Agriculture "may extend it by regulation".

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Export payment | `per_unit_subsidy` | Wheat (grain) exported from Tarvona, by sea or by land | Paid to registered exporters | T 35 per tonne, about 15% of the export price, paid by the Ministry of Agriculture on presentation of a customs export declaration showing that the wheat left Tarvona. No cap on tonnage. Funded from the general budget; the budget estimate is T 160 million a year (4.5 Mt × T 35). | None by grade or destination. Whether wheat exported as flour qualifies is unclear (U1). |
| K2 Registration and clawback | Condition of K1 | Exporters | Exporters | Registration with the Ministry, with a bond of T 50,000. "Where wheat for which a payment was made is re-imported into Tarvona, the payment shall be repaid with a penalty of 50%," and the exporter loses registration. | — |
| K3 Enforcement | Enforcement | K1, K2 | Customs Service; Ministry of Agriculture payments office | Customs checks export declarations and samples 2% of wheat imports declared as of Morvian origin. Both bodies administer the Act "within existing appropriations". | — |

Existing rules, which stay in place in the counterfactual:
- a 25% tariff on imports of wheat and flour, except goods of Morvian origin under the FTA (about T 64 per tonne on wheat at world prices, more than the subsidy);
- Morvian certificates of origin for wheat are issued by Morvian chambers of commerce on the shipper's declaration.

Funding: "the general budget". The Act names no new tax and no offsetting cut. Whether the outlay is met by higher taxes, by borrowing (implying later taxes) or by lower spending elsewhere is not stated (A-27).

Unclear provisions: **U1**, whether "wheat" in K1 includes flour exported by Tarvonian mills, paid per tonne of wheat equivalent. The Act defines wheat by its customs heading for grain; the minister told Parliament that "products of wheat" were "intended to be covered in due course", and no regulation has been made. Reading U1-a: flour exports do not qualify. Reading U1-b: they qualify per tonne of wheat equivalent. Readings get no probability; C-24 reports one sign for each.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a transfer from the budget to whoever exports wheat | Yes, while Tarvona remains a net exporter (A-1) and imports cannot hold the domestic price down (A-2) | SB-1, SB-2, SB-3, SB-4; core rules for the domestic price (CR-7a) and the currency link (CR-8b, CR-9) |
| K1, effect on domestic buyers | Not a separate intervention: no exchange between private parties is forced or forbidden. Domestic buyers are reached only through the market (CR-9), because sellers can now earn more abroad. | — | CR-7a, CR-9 |
| K2 | Binary (registration cost) and a condition on K1 | Yes | OC-2, RS-3 |
| K3 | Binary: administered within fixed budgets (A-26) | Yes | OC-3 (fixed-budget case) |

The catalog's subsidy patterns assume a subsidy that lowers the price buyers pay. K1 lowers the price that *foreign* buyers pay and raises the price that *domestic* buyers pay. SB-2 is cited only for the wedge between what exporters receive and what foreign buyers pay; every effect on domestic buyers is derived from CR-7a.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `wheat_growers` (`sellers.current`) | Farmers who grow wheat, owners and tenants | Selling abroad, through an exporter, now earns T 35 a tonne more than before. |
| `landowners.wheat_land` (`factor_owners.specific`) | Owners of land suited to wheat | The land's expected yield rises. |
| `tenant_farmers` | Farmers renting wheat land on one-year cash leases | Gain until their lease is renewed; then bid against other tenants for the land. |
| `exporters` | Grain traders, and large farms that register to export directly | Paid per tonne exported; must register and post a bond. |
| `stockholders.wheat` | Farmers and traders holding wheat from the Year 0 harvest in March of Year 1 | Selling after 1 July pays more than selling before. |
| `domestic_buyers.wheat` (`buyers.current`) | Flour millers, feed compounders and livestock farmers | Sellers now compare their offers with the export price plus the payment. |
| `millers.domestic` | Tarvonian flour mills, some of which export flour | Pay more for wheat; flour exports qualify only under U1-b. |
| `bakers` | Bakeries and food makers using flour | Pay more for Tarvonian flour; Morvian flour enters duty-free. |
| `buyers.bread` | Households buying bread and other wheat foods | Pay more if bakers pass on the cost. |
| `livestock_producers` | Pig and poultry farmers | Pay more for feed wheat; compete with imported meat. |
| `exporters.barley`, `growers.other_crops` | Sellers of barley; growers of canola and pulses | Feed buyers turn to barley; land is bid toward wheat. |
| `buyers.foreign` | Mills and feed makers abroad that buy wheat | More Tarvonian wheat is offered to them. |
| `sellers.foreign` | Wheat growers in other exporting countries | Compete with subsidized Tarvonian wheat. |
| `neighboring_jurisdictions` (Morvian growers and millers) | Morvian wheat sellers and buyers | Morvian wheat can be sold into Tarvona duty-free at the higher Tarvonian price; subsidized Tarvonian wheat can be bought. |
| `round_trippers` | Exporters and Morvian traders who would ship wheat out and bring it back | The payment exceeds the cost of a round trip across the land border. |
| `importers.morvia` | Importers of genuine Morvian wheat and flour | Face origin checks aimed at re-imports. |
| `users.grain_terminals` | Other shippers using grain rail and port capacity | Compete with added wheat exports for the same capacity at harvest. |
| `input_suppliers`, `workers.farm` | Sellers of fertilizer, seed and machinery; farm labor | More wheat is grown. |
| `importers`, `producers.import_competing`, `workers.import_competing` | Buyers of imported goods; domestic firms competing with imports; their workers | Linked to wheat exports through the currency (CR-9, `currency`). |
| `export_industries.other` | Wine, tourism and other exporters | Sell foreign currency for tals, in competition with wheat exporters' added receipts. |
| `taxpayers` | Those who fund the general budget, now or later | Fund the payments. |
| `officials.enforcement` | Customs and the Ministry's payments office | New work within fixed budgets. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `wheat_growers` | `net_price_received` (wheat, from 10 March of Year 1) | increase | short to medium | SB-2, CR-7a, CR-10a | A-1, A-2 |
| C-2 | `exporters` | `quantity_traded` (wheat exports, from 1 July of Year 1) | increase | short to medium | SB-2, CR-4 | A-1, A-3 |
| C-3 | `taxpayers` | `resources_available_other_uses` | decrease | short to long | SB-1, TX-1, OC-1, CR-8a | A-27 |

These are the effects the Act's supporters point to: growers get a better price (C-1) and more wheat is sold abroad (C-2). The budget outlay is also visible, as a line in the budget; C-3 records what its payers give up.

C-1 is derived from CR-7a, not from SB-2 alone. A tonne of Tarvonian wheat can go to a domestic mill or to a port. Before the Act, a grower's best offer was the same either way, net of freight. After it, the export route pays about T 35 more. Sellers move wheat to export until what domestic buyers offer has risen to match the export route (CR-7a). So the price growers receive rises on every tonne they sell, at home or abroad, not only on exported tonnes. That holds as long as Tarvona still exports some wheat at the margin (A-1) and imports cannot supply domestic buyers at a lower price (A-2: the 25% tariff exceeds the subsidy, and Morvia's wheat is too little). The price moves from the announcement, because stocks held in March can be sold after 1 July (CR-10a; C-10).

C-3: SB-1 requires the payers to be named. The Act names only "the general budget". If the outlay is met by taxes now or borrowing (taxes later), the payers are taxpayers (A-27, p = 0.6). If it is met by cutting other spending, the cost falls on those who would have received that spending instead. The method can record only one actor class per consequence, so C-3 names `taxpayers` and rests on A-27 (see Gaps found, b4). The recipients' side of the transfer (CR-8b) is C-1 and C-6 for Tarvonian sellers, C-7 for foreign buyers and C-13 for those who claim the payment on wheat that comes back.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `domestic_buyers.wheat` | `price_paid` (wheat, from 10 March of Year 1) | increase | short to medium | CR-7a, CR-9, CR-10a | A-1, A-2 |
| C-5 | `domestic_buyers.wheat` | `quantity_demanded` (wheat) | decrease | short to medium | CR-4c, RS-1 | A-1, A-2, A-4 |
| C-6 | `wheat_growers` (relative to `buyers.foreign`) | `subsidy_share_received` | increase | short to medium | DM-1, CR-7b | A-5 |
| C-7 | `buyers.foreign` | `price_paid` (wheat on the world market) | decrease | short to medium | SB-2, RS-13, CR-6 | A-3, A-6 |
| C-8 | `sellers.foreign` | `net_price_received` (wheat) | decrease | short to medium | RS-13, CR-9 | A-3, A-6 |
| C-9 | `wheat_growers` | `quantity_supplied` (wheat) | increase | medium | CR-7a, SB-3 | A-1, A-7 |
| C-10 | `stockholders.wheat` | `inventory_held` (wheat, at 30 June of Year 1) | increase | short | CR-10a, CR-7a | A-8 |
| C-11 | `exporters` | `quantity_traded` (wheat exports, 10 March to 30 June of Year 1) | decrease | short | RS-8 | A-8 |
| C-12 | `exporters` | `entry_rate` (registered exporters) | increase | short | CR-4, CR-7a | A-9 |
| C-13 | `round_trippers` | `informal_activity` (wheat re-imported from Morvia under false Morvian origin) | increase | short to medium | RS-3, RS-4, CR-4 | A-10 |
| C-14 | `importers.morvia` | `compliance_cost` (proving the origin of Morvian wheat and flour) | increase | short | CR-1, OC-2 | A-11 |
| C-15 | `wheat_growers`, `exporters` | `lobbying_effort` (extension past Year 4; extension to flour and barley) | increase | medium | RS-7, SB-5 | A-12 |
| C-16 | `domestic_buyers.wheat` | `lobbying_effort` (repeal; a duty-free import quota for millers and feeders) | increase | medium | RS-7 | A-13 |

C-4 is the other face of C-1: what growers receive more on domestic sales, domestic buyers pay more (CR-8b). Domestic buyers are not party to the subsidy at all; they are reached because their sellers' alternative has improved (CR-9: those who would have bought from the sellers). At the higher price they buy less (C-5): feed compounders switch toward barley (C-26) and some uses at the margin are given up (CR-4c). The exchanges that no longer happen are not prevented by the policy, as in OC-4: the sellers now rank a foreign sale higher and make it. Domestic buyers lose by their own ranking (CR-3a); the sellers gain (see Gaps found, b2).

C-6 applies DM-1 between Tarvonian sellers and foreign buyers. Foreign buyers can buy from many origins, and Tarvona supplies about 6% of world exports; Tarvonian growers' land and stocks have few other outlets in the short run. A-5 states the comparison: Tarvonian sellers receive more of the subsidy than foreign buyers do. DM-1 says nothing about how large either share is. C-7 and C-8: the added Tarvonian exports are added supply on the world market (RS-13, CR-6), so the world price is lower than it would have been, to the benefit of foreign buyers and the cost of competing exporters, provided the addition is large enough to move the price at all (A-6, p = 0.6).

C-9: the higher price draws land, labor and fertilizer into wheat from barley, canola and pulses (CR-7a, SB-3; C-27, C-36). C-10 and C-11 are a timing shift (RS-8; `02_ontology.md`, 2.5): wheat from the Year 0 harvest that would have been exported between March and June is held for export after 1 July, when it earns the payment. Exports in that window fall (C-11) and stocks at the end of June are higher than they would have been (C-10); the July exports are part of C-2. Holding back stock also raises the domestic price from March (C-4), since domestic buyers must now outbid the July export price (CR-7 across time, CR-10a).

C-12: registration and a bond cost less than the payment on a few hundred tonnes, so large farms near the border register and truck wheat to Morvia themselves (CR-4, x: sell to a trader, y: export directly).

C-13 is the probe for re-importing. Wheat trucked to Morvia earns T 35; bringing it back costs about T 10, and declared as Morvian wheat it enters duty-free. The clawback in K2 applies only if Customs can show the wheat is the same wheat, and wheat is fungible once it leaves the truck. With 2% of declarations sampled and origin certified on the shipper's word, the expected penalty is below the gain for some traders (RS-3, CR-4: x comply, y round-trip; RS-4 for the border). A-10 (p = 0.65) states it. C-14: checks aimed at round-trips fall also on genuine Morvian imports (CR-1, op 3: paperwork attached to an option). C-13 is the illegal form of a trade the FTA also allows legally (C-19, section 7).

C-15, C-16: RS-7, with each group's ability to organize stated (A-12, A-13). The Act's power to extend by regulation makes the gain depend on a political decision every year after Year 3.

Not reported: a rush of exports in the weeks before the Act expires on 30 June of Year 4, followed by a dip. That needs exporters to expect it to lapse on schedule; given the power to extend, A-25 is below the cut-off (p = 0.4). Not reported: responses of foreign governments (out of scope, Q5).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-17 | `landowners.wheat_land` | `asset_value` (wheat land) | increase | short (from 10 March of Year 1) | SB-4, CR-7c, CR-10c | wheat land: `input_to` wheat | A-1, A-14 |
| C-18 | `tenant_farmers` | `price_paid` (cash rent at lease renewal) | increase | medium (from 1 October of Year 1) | CR-7b, CR-5c | land lease: `contract` | A-1, A-15 |
| C-19 | `neighboring_jurisdictions` (Morvian growers) | `quantity_traded` (Morvian wheat sold into Tarvona) | increase | short to medium | RS-4, CR-7a | Tarvonian and Morvian wheat: `across_border`, close | A-1, A-16 |
| C-20 | `neighboring_jurisdictions` (Morvian millers and feeders) | `price_paid` (wheat in Morvia) | ambiguous | short to medium | CR-9, CR-6, CR-12b | as C-19 | A-1, A-16 |
| C-21 | `buyers.bread` | `price_paid` (bread and other wheat foods) | increase | medium | RS-14, CR-9 | wheat: `input_to` flour; flour: `input_to` bread | A-1, A-2, A-17 |
| C-22 | `buyers.bread` | `quantity_demanded` (bread and other wheat foods) | decrease | medium | RS-14, CR-4c | as C-21 | A-1, A-2, A-17, A-18 |
| C-23 | `buyers.bread` | `resources_available_other_uses` | decrease | medium | CR-3, CR-8a | as C-21 | A-1, A-2, A-17, A-19 |
| C-24 | `millers.domestic` | `quantity_supplied` (flour exports) | U1-a: decrease; U1-b: ambiguous | medium | CR-9, CR-4, CR-12b | wheat: `input_to` flour | A-1, A-2 |
| C-25 | `bakers` | `quantity_substitute` (Morvian flour, duty-free) | increase | medium | RS-1, CR-7a | Tarvonian and Morvian flour: `substitute`, close; `across_border` | A-1, A-20 |
| C-26 | `livestock_producers` | `quantity_substitute` (feed barley) | increase | short to medium | RS-1 | wheat and barley in feed: `substitute`, close | A-1, A-21 |
| C-27 | `exporters.barley` | `quantity_traded` (barley exports) | decrease | medium | CR-9, CR-7a; SB-3 | as C-26; wheat and barley compete for land | A-21 or A-7 |
| C-28 | `livestock_producers` | `quantity_supplied` (pork and poultry) | decrease | medium | RS-14, RS-6 | feed wheat: `input_to` pork and poultry | A-1, A-22 |
| C-29 | `input_suppliers` | `quantity_demanded` (fertilizer, seed, machinery for wheat) | increase | medium | CR-9 | fertilizer, seed, machinery: `input_to` wheat | A-7 |
| C-30 | `workers.farm` | `employment`, `hours_worked` | at_least_one_increase | medium | CR-9, CR-7a | farm labor: `input_to` wheat | A-7 |
| C-31 | `users.grain_terminals` | `price_paid` (grain rail freight and port handling, harvest season) | increase | short | CR-9, CR-6 | rail and port handling: `input_to` exports | A-23 |
| C-32 | `importers` | `quantity_traded` (imports) | increase | medium | CR-8b, CR-9 | wheat exports and imports: `currency` | A-24 |
| C-33 | `producers.import_competing` | `quantity_supplied` | decrease | medium | CR-8b, CR-9, CR-4 | as C-32; imports and domestic clothing, household goods, processed foods: `substitute` | A-24 |
| C-34 | `workers.import_competing` | `employment`, `hours_worked` | at_least_one_decrease | medium | CR-9, OC-5 | as C-33 | A-24 |
| C-35 | `export_industries.other` | `net_price_received` (in tals, per unit sold abroad) | decrease | medium | CR-9, CR-6 | wheat exporters and other exporters both sell foreign currency for tals: `currency` | A-24 |
| C-36 | `growers.other_crops` | `quantity_supplied` (canola, pulses) | decrease | medium | SB-3, CR-7a | wheat and other crops compete for land | A-7 |

C-17: wheat land is in fixed supply, and its expected yield rises for as long as the payment is expected to last. Its price rises when the payment becomes expected, on 10 March of Year 1, and the gain goes to whoever owns it then (CR-7c, CR-10c; SB-4). The Act runs for three years with a power to extend, so the land capitalizes the payments expected over that term and the chance of extension: less than for a permanent subsidy, with the same sign. C-18: tenants on one-year leases keep the higher wheat price until 1 October; at renewal, landowners can let to whoever bids most, and the rent rises toward the land's higher yield (CR-5c within the lease `contract`; CR-7b: the lasting gain settles on the fixed factor, A-15). Growers who rent are thus better off only until their lease is renewed. Growers who own their land gain both as growers (C-1) and as landowners (C-17).

C-19 and C-20 are the legal form of round-tripping. Morvian wheat now fetches the Tarvonian price, so Morvian growers truck it into Tarvona duty-free (C-19; RS-4, CR-7a). At the same time, Tarvonian wheat exported to Morvia earns the payment. With a payment of T 35 and transport of T 10 each way, both flows can pay at once: the subsidy is then paid on Tarvonian wheat that replaces, in Morvian mills, the Morvian wheat sent to Tarvona. The Morvian price is pushed up by Tarvonian buyers and down by subsidized Tarvonian sellers (C-20, ambiguous; section 7). Swaps are limited by Morvia's own harvest (about 2 Mt, against 7.5 Mt of Tarvonian use), so they do not hold the Tarvonian price at its old level (A-2).

C-21 to C-23: flour is most of the cost of bread, and bread is baked fresh and is not imported in any quantity, so all Tarvonian bakers face the same higher flour cost and pass it on (RS-14, A-17). At the higher price, households buy somewhat less (C-22). CR-4's exception applies to heavy buyers of a staple whose price rises: for poor households that spend much of their means on bread, the loss in means could raise their purchases of bread against other foods. C-22 needs A-18, that bread is not so large a share of spending for most households that this dominates for the class. Most households keep buying most of their bread at the higher price, so they have less for other uses (C-23; CR-3 note, A-19).

C-24 depends on U1. Under U1-a, Tarvonian mills pay the higher domestic price for wheat, while their competitors abroad pay the world price, which is lower than it would have been (C-7), so they export less flour (CR-9, CR-4). Under U1-b, the payment on flour exports offsets the higher wheat price, which is a (+) chain against the loss from the higher tal (C-35, −); the sign is `ambiguous` (CR-12b; section 7). C-25: Morvian mills can buy wheat at the world price, and the flour they mill from it is of Morvian origin and enters Tarvona duty-free, so Tarvonian bakers buy more of it (RS-1, CR-7a; A-20). This holds under both readings.

C-26, C-27: feed compounders switch toward barley (RS-1). Tarvona exports barley, so the domestic barley price is tied to its export price (CR-7a, export parity). Added domestic demand for barley is met by exporting less of it, not by a higher price, as long as some barley is still exported. The supply of barley to domestic buyers can expand at an unchanged cost, so RS-16's precondition for a price rise fails. What falls is barley exports (C-27). Two independent chains reach C-27 with the same sign: feed buyers take barley that would have been exported (A-21), and land moves from barley to wheat (A-7). By CR-12d it holds if either chain's premise holds. C-28: livestock producers pay more for feed and compete with imported meat, so the quantity effect dominates (RS-14, RS-6; A-22).

C-31: added exports and the held-back stock (C-10) arrive at the ports in the harvest months, when rail and terminal capacity is already tight. The price of that capacity rises for every shipper using it (CR-9, CR-6; A-23).

C-32 to C-35 apply the `currency` relation in reverse, the mirror of TX-8. TX-8 states it one way: payments for imports are the means with which foreigners buy exports. By CR-8b the converse also holds: what foreigners pay for Tarvona's exports is the foreign money with which Tarvonians buy imports. More wheat exports put more foreign currency in Tarvonian hands, and more imports are bought with it (C-32). Domestic producers of goods that compete with imports face more competition and produce less (C-33), and their workers lose jobs or hours (C-34; OC-5, as a group). Under a floating rate, the added foreign currency that wheat exporters offer for tals lowers the tal price of foreign currency (CR-6 in the market for foreign currency). Every other exporter therefore gets fewer tals for each unit sold abroad (C-35). The relation is a shared market, the one in which both sell foreign currency; CR-9 names it as "those who compete with them for the same means or customers". All four need A-24, that the added export receipts are not offset by capital flows within the medium horizon, as TX-8 does. There is no `exchange_rate` variable, so C-35 is recorded as other exporters' `net_price_received` in tals (Gaps found, d1).

Depth. C-21 to C-23 are at depth 3 (payment, wheat price, flour price, bread). C-28 is at depth 3; C-34 and C-35 at depth 3 to 4 (payment, exports, foreign-currency receipts, imports or the tal, producers). The spending of the payers of C-3, and the purchases of buyers who pay more for bread, are not followed into named markets: which purchases fall needs a premise the case does not supply (CR-4, "A change in means alone"; Q19).

Second-order checks:
- **RS-9 (bundled trips):** no buyer changes where they shop. Not applicable.
- **RS-10 (informal trade):** round-trip wheat (C-13) moves through ordinary grain channels under false papers, not through a separate informal market; buyers can still judge it, so RS-10's effects on search and quality are not claimed.
- **RS-11 (lock-in):** the payment is tied to exporting, not to a place or status. Not applicable.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `domestic_buyers.wheat`, `price_paid`, short to medium (and `wheat_growers`, `net_price_received`) | Export route pays T 35 more; sellers move wheat abroad until domestic offers match it (CR-7a). | The world price falls (C-7); the tal rises (C-35 chain), so a dollar of world price is worth fewer tals; Morvian wheat flows in (C-19). Each lowers the export route's yield in tals. | CR-12e, by logic: each (−) chain is caused by Tarvona exporting more. Tarvona exports more only if the export route's yield in tals is above what it would have been. If the (−) chains brought it below that, exports would fall below the counterfactual, and the (−) chains would vanish. So they can shrink the rise but not reverse it, while A-1 holds. | **increase** (C-1, C-4). |
| `neighboring_jurisdictions` (Morvian buyers), `price_paid`, short to medium | Morvian wheat is drawn into Tarvona at the higher price (C-19). | Subsidized Tarvonian wheat is sold into Morvia (part of C-2). | None | **ambiguous** (C-20). Decided by the cost of crossing the border both ways against the payment, and by how much Morvian wheat Tarvonian buyers absorb. |
| `millers.domestic`, `quantity_supplied` (flour exports), medium, reading U1-b | The payment on flour exports offsets the higher wheat price. | The tal is higher (C-35 chain); foreign mills buy wheat at a lower world price (C-7). | None | **U1-a: decrease; U1-b: ambiguous** (C-24). Under U1-a, only the (−) chains act. |
| `exporters.barley`, barley price at home, medium | Feed buyers switch to barley (C-26); land leaves barley (C-36, C-9). | — | — | **Not signed.** While Tarvona still exports barley, the domestic price stays tied to its export price, and the added demand is met by exporting less (C-27). If barley exports stopped, RS-16 would apply and the price would rise. |
| `producers.import_competing`, `quantity_supplied`, medium | Taxpayers and growers spend part of their changed means on these goods: the sign is not known without a premise (Q19). | Imports bought with added export receipts (C-33). | None needed | **decrease** (C-33). The funding chain has no sign for this market without a premise (CR-4, "A change in means alone"), so only the currency chain is signed. |
| Wheat supply chain jobs against jobs in import-competing industries and other exporters | More farm work (C-30). | Fewer jobs or hours in import-competing industries (C-34) and at other exporters (C-35). | — | **Not combined.** Different actor classes (CR-12c). The farm jobs are seen and credited to the Act; the others are spread thin and not attributed to it. |

Both sides of the transfer (CR-8b). The payment is taken from the payers of C-3. It is received partly by Tarvonian sellers (C-1, C-6), and through them by landowners (C-17, C-18); partly by foreign buyers, as a lower world price (C-7); and partly by round-trippers on wheat that never stays abroad (C-13). Domestic buyers of wheat (C-4), bread buyers (C-21, C-23) and other exporters (C-35) pay a further cost that never passes through the budget. What domestic buyers pay more goes to growers; it is a transfer between them that the budget does not record.

## 8. Time structure

- **Announcement window (10 March to 30 June of Year 1).** Holders of Year 0 wheat keep it for export after 1 July (C-10), so exports in the window fall (C-11) and the domestic price rises from March, before any payment is made (C-1, C-4). Land prices rise from the announcement (C-17).
- **First marketing year (from 1 July of Year 1).** Exports rise (C-2), new exporters register (C-12), and round-tripping begins, as soon as traders learn how thinly origin is checked (C-13). Ports and rail are busier at harvest (C-31). Tenants keep the gain until their leases are renewed on 1 October (C-18).
- **Second and third years.** Land moves into wheat from barley, canola and pulses (C-9, C-27, C-36); input suppliers and farm labor follow (C-29, C-30). The currency effects build up as export receipts are spent (C-32 to C-35). Bread prices follow flour prices with a lag (C-21). Lobbying peaks before the expiry date, when an extension by regulation is in question (C-15, C-16).
- **Expiry or extension (30 June of Year 4).** If the Act lapses, land values fall back on whoever holds the land then, including buyers who paid the higher price (SB-4). Land moved into wheat moves back only as far as the return on wheat falls below other crops, net of the cost of switching (TS-6). Whether exports rush before the expiry depends on whether exporters expect it to lapse (A-25, below the cut-off).
- **Erosion.** The payment is fixed in tals per tonne (TS-3). If prices in general rise, its value relative to the price of wheat falls each year, and every effect above shrinks unless the rate is raised.
- **Counterfactual.** Every sign is relative to Tarvona without the Act over the same years, including whatever trend in world wheat prices would have occurred anyway.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-3 | `taxpayers` | `resources_available_other_uses` | decrease | What the T 160 million or more a year would otherwise have bought, now or (if borrowed) later. The outlay is above the static estimate by the tonnes added (C-2) and the tonnes that come back (C-13). | SB-1, TX-1, OC-1 |
| C-37 | `officials.enforcement` | `enforcement_cost` (export verification, origin checks, payment processing) | increase | Staff time at Customs and the Ministry. | OC-3 |
| C-38 | `officials.enforcement` | `enforcement_cost` (other customs work) | decrease | Within fixed appropriations (A-26), staff moved to the new checks are taken from other customs work; those whom that work protected bear the cost. | OC-3, CR-8a |
| C-39 | `exporters` | `compliance_cost` (registration, bonds, payment claims) | increase | Clerical work and the cost of tying up the bond. | OC-2, CR-8c |
| C-14 | `importers.morvia` | `compliance_cost` | increase | Proving origin for genuine Morvian imports. | CR-1, OC-2 |
| C-36 | `growers.other_crops` | `quantity_supplied` (canola, pulses) | decrease | The canola and pulses not grown on land moved into wheat: the seen added wheat against the unseen other crops. | SB-3, CR-7a |
| C-23 | `buyers.bread` | `resources_available_other_uses` | decrease | What households paying more for bread would have bought with the difference. | CR-3, CR-8a |

OC-4 (prevented exchanges) is not applied to the wheat that domestic buyers no longer buy (C-5). The policy prevents no exchange: sellers prefer to sell abroad and do so. Domestic buyers lose by their own ranking (CR-3a); sellers gain. Recording the forgone domestic purchases as a loss to both parties would misstate the sellers' side.

The real resources used to truck round-trip wheat across the border and back (C-13) are used up and serve no end except collecting the payment (CR-8c). They have no separate entry because no controlled variable records resources spent on evasion apart from `informal_activity` itself.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Tarvona remains a net exporter of wheat throughout, so the domestic price is set by the export route. | binding | 0.9 | 4.5 Mt exported against 7.5 Mt used at home; harvest variability; the Act raises exports further. | In a drought year with no exports, the payment does not bind; C-1, C-4 and everything downstream lapse for that year. |
| A-2 | Imports cannot hold the domestic price below the export price plus the payment: the 25% tariff exceeds the payment, and Morvian wheat is too little to fill the gap. | binding | 0.8 | Tariff schedule; Morvian harvest (about 2 Mt) against Tarvonian use (7.5 Mt). | The domestic price rises less, or not at all; the subsidy goes mainly to round trips and swaps. C-4, C-21 to C-24 weaken. |
| A-3 | Some Tarvonian sellers sell more abroad at the higher yield, and foreign buyers take more Tarvonian wheat at a slightly lower price. | substitutability | 0.9 | Stocks and spare land; foreign buyers' choice among origins. | C-2, C-7, C-8 not reported. |
| A-4 | Some domestic users can reduce their use of wheat (feed rations, marginal uses). | substitutability | 0.85 | Feed formulation practice; share of feed wheat in rations. | C-5 not reported. |
| A-5 | Foreign buyers have clearly more alternatives than Tarvonian sellers: many origins against land and stocks with few other outlets in the short run. | substitutability | 0.75 | Tarvona's 6% share of world exports; number of competing origins; crop rotation constraints. | DM-1 does not apply; C-6 not reported; the split is open. |
| A-6 | Tarvona's added exports are large enough to lower the world price at all, and are not offset by other exporters withdrawing. | other | 0.6 | Tarvona's share of world exports; studies of world price responses to supply shifts of that size. | C-7, C-8 not reported. |
| A-7 | Land and other farm resources can move from barley, canola and pulses to wheat within the medium horizon. | alternative_uses | 0.85 | Rotations in the Eastern Plains; planting decisions each autumn. | C-9, C-29, C-30, C-36 not reported; the barley-land chain of C-27 fails. |
| A-8 | Holders of Year 0 wheat believed the announcement and can store it until July. | expectations | 0.8 | Government majority in Parliament; on-farm and elevator storage. | C-10, C-11 not reported. |
| A-9 | Registration and the bond cost less than the payment on the tonnes some large farms would export directly. | other | 0.7 | Bond size against T 35 per tonne; farm sizes near the border. | C-12 not reported. |
| A-10 | Round-tripping through Morvia pays for some traders: the round trip costs about T 20, the clawback needs proof that the same wheat came back, and origin is checked on 2% of declarations. | enforcement | 0.65 | K2 and K3; experience with origin fraud under the FTA; border crossing costs. | C-13 not reported; C-14 shrinks. |
| A-11 | Customs extends origin checks to genuine Morvian wheat and flour imports. | enforcement | 0.75 | K3's sampling rule; Customs practice after earlier fraud cases. | C-14 not reported. |
| A-12 | The growers' federation and exporters' association can organize to lobby at a cost below their stake (RS-7's premise). | other | 0.85 | Existing farm federation; the Act's annual extension power. | C-15 not reported. |
| A-13 | Millers, feed compounders and livestock producers can organize to lobby. | other | 0.7 | Millers' association; pig and poultry associations. | C-16 not reported. |
| A-14 | Buyers of land expect the payment to last at least its three-year term; wheat land is in fixed supply. | expectations | 0.8 | The Act's text; government statements; land market reports. | C-17 shrinks; it does not reverse. |
| A-15 | Cash leases are renewed each year at negotiated rents, and landowners can let to other tenants. | other | 0.75 | Lease terms; number of tenants seeking land. | C-18 not reported; tenants keep more of the gain. |
| A-16 | Morvian wheat can be trucked into Tarvona at a cost below the price gap the Act opens. | mobility | 0.8 | Distance to the border; FTA rules of origin for grain. | C-19, C-20 not reported. |
| A-17 | Flour is a material part of the cost of bread, bakers cannot replace it at the old cost, and bread is not imported in quantity. | substitutability | 0.75 | Bakery cost shares; trade data for bread. | C-21 to C-23 not reported. |
| A-18 | For most households, bread is not so large a share of spending that the loss in means outweighs the higher price in their choice (CR-4's exception). | other | 0.85 | Household budget surveys. | C-22 becomes ambiguous for the class. |
| A-19 | Most households keep buying most of their bread at the higher price. | substitutability | 0.85 | Studies of bread demand. | C-23 not reported. |
| A-20 | Morvian mills can buy wheat at world prices and supply flour to Tarvona, and milling confers Morvian origin under the FTA. | other | 0.65 | FTA rules of origin; Morvian milling capacity near the border. | C-25 not reported. |
| A-21 | Feed rations can switch from wheat to barley. | substitutability | 0.85 | Feed formulation practice. | C-26 not reported; the feed chain of C-27 fails. |
| A-22 | Feed wheat is a material part of pork and poultry costs, and imported meat competes with Tarvonian meat. | substitutability | 0.6 | Cost shares; meat import shares. | C-28 not reported. |
| A-23 | Grain rail and port capacity is close to full in the harvest months. | other | 0.6 | Terminal throughput; rail car availability. | C-31 not reported. |
| A-24 | The exchange rate floats, and the added export receipts are not offset by capital flows within the medium horizon. | other | 0.6 | Exchange rate regime; capital account. | C-32 to C-35 not reported. |
| A-25 | Exporters expect the Act to lapse on 30 June of Year 4. | expectations | 0.4 | The minister's power to extend; the farm federation's influence. | Below cut-off; the rush before expiry and the dip after it are not reported. |
| A-26 | Customs and the Ministry administer the Act within fixed appropriations, as K3 says. | revenue_use | 0.7 | K3's text; budget documents. | C-38 not reported; if budgets rise, OC-3's first case applies and the cost falls on taxpayers. |
| A-27 | The outlay is met by taxes or borrowing, not by cuts in other spending. | revenue_use | 0.6 | Budget statement; the government's borrowing plans. | C-3 is borne instead by those whose spending is cut. |

**Final check before the report** (`03_workflow.md`).
1. *Uncombined chains.* Domestic wheat price: the (−) chains (world price, tal, Morvian wheat) are combined with the (+) chain in section 7, with a dominance premise by logic. Morvian price and flour exports under U1-b: ambiguous. Import-competing output: the funding chain has no sign, stated. Barley price: not signed, stated.
2. *Group signs.* Farm labor (C-30) and import-competing labor (C-34) are groups. Other exporters' quantity is not signed separately from C-35.
3. *Baseline.* Every sign is against Tarvona without the Act. C-11 is against the exports that would have happened in March to June, not against Year 0.
4. *Worse off is not poorer.* `resources_available_other_uses` is signed only for taxpayers (an unavoidable payment, given A-27) and for bread buyers who keep buying (A-19). Domestic wheat buyers as a class are not given it, since some buy less (C-5).
5. *Timing shifts.* The announcement window is signed per window (C-10, C-11, with July in C-2). The expiry window is below the cut-off.
6. *Both sides of transfers.* Budget to sellers, foreign buyers and round-trippers; domestic buyers to growers; tenants to landowners; port users to terminals. All recorded (section 7).
7. *Every class, every core rule.* CR-7c applied to wheat land (C-17); CR-6 to ports and the foreign-currency market; enforcement cost and its funding (C-37, C-38); the payer's side (C-3).
8. *Unstated premises.* Lobbying (A-12, A-13), the margin for each response (A-3, A-4, A-21), and the CR-4 exception for bread (A-18) are in the table.

## 11. Report

**The policy.** Tarvona pays exporters T 35 for every tonne of wheat they ship abroad, from July of Year 1 to June of Year 4, from the general budget. Exporters must register; payments are repayable if the wheat comes back. Tarvona already taxes imported wheat at 25%, except wheat and flour from Morvia, which enter duty-free.

**Visible consequences.** Wheat growers get a higher price for all their wheat, not only what is exported (C-1), and more wheat is exported (C-2). The budget pays for it; taxpayers have that much less for other uses (C-3).

**Invisible consequences.**
- *Domestic buyers of wheat* (millers, feed makers and livestock farmers) pay more for it from the announcement (C-4) and buy less (C-5). *Bread buyers* pay more (C-21), buy a little less (C-22), and have less to spend on other things (C-23). *Pig and poultry farmers*, who compete with imported meat, produce less (C-28). Feed makers turn to barley (C-26), and Tarvona exports less barley (C-27).
- *Owners of wheat land* gain when the subsidy is announced (C-17). *Tenant farmers* gain until their leases are renewed, when rents rise (C-18).
- *Foreign buyers* pay less for wheat than they would have (C-7), and *growers in other exporting countries* receive less (C-8). Tarvonian sellers receive more of the subsidy than foreign buyers do (C-6).
- *Wheat comes back.* Some exporters ship wheat to Morvia, collect the payment and bring it back as Morvian wheat (C-13). Morvian growers legally sell their wheat into Tarvona (C-19), while Tarvonian wheat earns the payment in Morvia. Morvian flour, milled from wheat bought at world prices, replaces some Tarvonian flour (C-25). Importers of genuine Morvian goods bear origin checks (C-14).
- *Land and other farm resources* move into wheat from canola, pulses and barley (C-9, C-36); farm suppliers and farm labor gain (C-29, C-30). Other shippers pay more for rail and port capacity at harvest (C-31).
- *Through the currency*, more wheat exports mean more imports (C-32): domestic producers that compete with imports produce less (C-33) and use less labor, in jobs or hours (C-34). Other exporters, such as wine and tourism, get fewer tals for what they sell abroad (C-35).
- Stocks are held back between the announcement and July (C-10), and exports in that window fall (C-11). New exporters register (C-12). Growers and exporters lobby to extend the Act; millers and feeders lobby against it (C-15, C-16). Customs and the Ministry spend staff time on the Act (C-37), taken from other customs work (C-38); exporters bear registration and claim costs (C-39).

**Ambiguous effects.** The wheat price in Morvia, which is pulled up by Tarvonian buyers and down by subsidized Tarvonian sellers (C-20). Tarvonian flour exports if flour qualifies for the payment (C-24, reading U1-b); if it does not, they fall.

**Key conditions.** That Tarvona remains an exporter (A-1, p = 0.9) and that imports cannot hold the domestic price down (A-2, p = 0.8) drive every effect on domestic buyers. Foreign buyers' gain rests on Tarvona being large enough to move the world price (A-6, p = 0.6). The currency effects rest on A-24 (p = 0.6). Round-tripping rests on how thinly origin is checked (A-10, p = 0.65). The Act's text, not this analysis, decides whether flour qualifies (U1).

**What this analysis cannot say.** How large any effect is, including how much of the subsidy foreign buyers receive and how much leaks through round trips; how the domestic gains to growers and landowners compare with the losses to domestic buyers, taxpayers, import-competing industries and other exporters; how foreign governments respond (out of scope, Q5); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | wheat_growers | net_price_received (wheat) | increase | short–medium | visible | B | SB-2, CR-7a, CR-10a | A-1, A-2 |
| C-2 | exporters | quantity_traded (wheat exports, from 1 July Year 1) | increase | short–medium | visible | B | SB-2, CR-4 | A-1, A-3 |
| C-3 | taxpayers | resources_available_other_uses | decrease | short–long | visible | B | SB-1, TX-1, OC-1, CR-8a | A-27 |
| C-4 | domestic_buyers.wheat | price_paid (wheat) | increase | short–medium | invisible | B | CR-7a, CR-9, CR-10a | A-1, A-2 |
| C-5 | domestic_buyers.wheat | quantity_demanded (wheat) | decrease | short–medium | invisible | B | CR-4c, RS-1 | A-1, A-2, A-4 |
| C-6 | wheat_growers (vs buyers.foreign) | subsidy_share_received | increase | short–medium | invisible | B | DM-1, CR-7b | A-5 |
| C-7 | buyers.foreign | price_paid (world wheat) | decrease | short–medium | invisible | B | SB-2, RS-13, CR-6 | A-3, A-6 |
| C-8 | sellers.foreign | net_price_received (wheat) | decrease | short–medium | invisible | B | RS-13, CR-9 | A-3, A-6 |
| C-9 | wheat_growers | quantity_supplied (wheat) | increase | medium | invisible | B | CR-7a, SB-3 | A-1, A-7 |
| C-10 | stockholders.wheat | inventory_held (30 June Year 1) | increase | short | invisible | B | CR-10a, CR-7a | A-8 |
| C-11 | exporters | quantity_traded (wheat exports, 10 March–30 June Year 1) | decrease | short | invisible | B | RS-8 | A-8 |
| C-12 | exporters | entry_rate | increase | short | invisible | B | CR-4, CR-7a | A-9 |
| C-13 | round_trippers | informal_activity (false-origin re-imports) | increase | short–medium | invisible | B | RS-3, RS-4, CR-4 | A-10 |
| C-14 | importers.morvia | compliance_cost (origin proof) | increase | short | invisible | B | CR-1, OC-2 | A-11 |
| C-15 | wheat_growers, exporters | lobbying_effort | increase | medium | invisible | B | RS-7, SB-5 | A-12 |
| C-16 | domestic_buyers.wheat | lobbying_effort | increase | medium | invisible | B | RS-7 | A-13 |
| C-17 | landowners.wheat_land | asset_value | increase | short | invisible | B | SB-4, CR-7c, CR-10c | A-1, A-14 |
| C-18 | tenant_farmers | price_paid (cash rent at renewal) | increase | medium | invisible | B | CR-7b, CR-5c | A-1, A-15 |
| C-19 | neighboring_jurisdictions (Morvian growers) | quantity_traded (Morvian wheat into Tarvona) | increase | short–medium | invisible | B | RS-4, CR-7a | A-1, A-16 |
| C-20 | neighboring_jurisdictions (Morvian buyers) | price_paid (wheat in Morvia) | ambiguous | short–medium | invisible | B | CR-9, CR-6, CR-12b | A-1, A-16 |
| C-21 | buyers.bread | price_paid (bread) | increase | medium | invisible | B | RS-14, CR-9 | A-1, A-2, A-17 |
| C-22 | buyers.bread | quantity_demanded (bread) | decrease | medium | invisible | B | RS-14, CR-4c | A-1, A-2, A-17, A-18 |
| C-23 | buyers.bread | resources_available_other_uses | decrease | medium | invisible | B | CR-3, CR-8a | A-1, A-2, A-17, A-19 |
| C-24 | millers.domestic | quantity_supplied (flour exports) | U1-a: decrease; U1-b: ambiguous | medium | invisible | B | CR-9, CR-4, CR-12b | A-1, A-2 |
| C-25 | bakers | quantity_substitute (Morvian flour) | increase | medium | invisible | B | RS-1, CR-7a | A-1, A-20 |
| C-26 | livestock_producers | quantity_substitute (feed barley) | increase | short–medium | invisible | B | RS-1 | A-1, A-21 |
| C-27 | exporters.barley | quantity_traded (barley exports) | decrease | medium | invisible | B | CR-9, CR-7a; SB-3; CR-12d | A-21 or A-7 |
| C-28 | livestock_producers | quantity_supplied (pork, poultry) | decrease | medium | invisible | B | RS-14, RS-6 | A-1, A-22 |
| C-29 | input_suppliers | quantity_demanded (fertilizer, seed, machinery) | increase | medium | invisible | B | CR-9 | A-7 |
| C-30 | workers.farm | employment, hours_worked | at_least_one_increase | medium | invisible | B | CR-9, CR-7a | A-7 |
| C-31 | users.grain_terminals | price_paid (rail and port handling) | increase | short | invisible | B | CR-9, CR-6 | A-23 |
| C-32 | importers | quantity_traded (imports) | increase | medium | invisible | B | CR-8b, CR-9 | A-24 |
| C-33 | producers.import_competing | quantity_supplied | decrease | medium | invisible | B | CR-8b, CR-9, CR-4 | A-24 |
| C-34 | workers.import_competing | employment, hours_worked | at_least_one_decrease | medium | invisible | B | CR-9, OC-5 | A-24 |
| C-35 | export_industries.other | net_price_received (in tals) | decrease | medium | invisible | B | CR-9, CR-6 | A-24 |
| C-36 | growers.other_crops | quantity_supplied (canola, pulses) | decrease | medium | invisible | B | SB-3, CR-7a | A-7 |
| C-37 | officials.enforcement | enforcement_cost (the Act's checks and payments) | increase | short | invisible | A | OC-3 | none |
| C-38 | officials.enforcement | enforcement_cost (other customs work) | decrease | short | invisible | B | OC-3, CR-8a | A-26 |
| C-39 | exporters | compliance_cost (registration, bonds, claims) | increase | short | invisible | A | OC-2, CR-8c | none |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from a pattern or from CR-1 to CR-12. Responses of foreign governments were excluded as out of scope (Q5), not because no core rule reaches them.

**(b) Unclear core rules.**
1. *CR-9 and the `currency` relation are stated in one direction.* CR-9 and `02_ontology.md` 2.8 say that "payments for imports are the means with which foreigners buy exports". The converse (export receipts are the means with which residents buy imports, C-32 to C-34) follows from CR-8b, but neither text states it, and TX-8 covers only import restrictions. CR-9 also lists no relation for the effect on *other* exporters (C-35): wheat exporters and wine exporters are linked not by trade with each other but because both sell foreign currency in the same market. The analysis used "those who compete with them for the same means" and CR-6 in the market for foreign currency. Proposed wording for 2.8: "currency: in either direction, receipts from selling abroad are the means for buying from abroad; all who sell or buy foreign currency share one market for it."
2. *CR-5a and OC-4 do not separate prevented exchanges from exchanges that lose out to a better offer.* Workflow step 9 asks "what exchanges no longer happen" and points to OC-4, which says that both parties lose. Here domestic purchases that no longer happen (C-5) were not prevented: sellers chose a foreign buyer instead. Only the domestic buyer loses (CR-3a). CR-5a should say "prevents (forbids or makes impossible)", and the step-9 question should note that an exchange displaced by a better offer is a loss to one side only.
3. *CR-12e and dominance by logic.* The domestic price (section 7) combines a (+) chain with (−) chains that are themselves caused by it. The claim that such chains can shrink but not reverse their cause is neither an empirical premise nor arithmetic on the case's figures: it is an argument from CR-6 and CR-7. CR-12e lists only three kinds of dominance premise. It should say whether "a response cannot overturn the change in yield that causes it" counts as a fourth.
4. *SB-1 and CR-8a when funding is "the general budget".* SB-1 says "name the payers", and CR-8a says the means are withdrawn from some other use. When the record names no tax, borrowing or cut, the payers are one of three different actor classes: current taxpayers, future taxpayers, or recipients of cut spending. Group signs (`02_ontology.md`, 2.5) group variables, not actor classes, so C-3 had to name `taxpayers` and rest on a `revenue_use` premise (A-27). A group form over actor classes ("at least one of these classes: decrease") would let the Tier A conclusion of CR-8a be stated without the premise.
5. *RS-16 and traded substitutes.* RS-16's precondition ("supply cannot expand at an unchanged cost") is met for barley only while barley is not exported. When a substitute is itself exported, the domestic supply comes from diverted exports at the export price. The rule is correct, but the case is easy to miss; RS-16's Unless clause could name it.

**(c) Missing patterns.**
1. *SB-10 Export subsidy (mirror of TX-7)* (proposed). If a `per_unit_subsidy` is paid on exports of a good the country already exports, and imports cannot supply the home market below the new export price, then: `price_paid` by domestic buyers and `net_price_received` by domestic sellers increase on all sales, at home and abroad; domestic `quantity_demanded` decreases; foreign buyers' `price_paid` decreases where the country's added exports move the world price; fixed factors (land) capture the lasting gain. Unless: the country stops exporting (the payment no longer binds), or imports are open at a price below the new export price (then trade circles: see 3). Derivation: CR-7a (sellers equalize the yield of home and foreign sales), CR-5c (the wedge abroad), CR-6 (world market), CR-7b and CR-7c (land), CR-8b (both sides). Used here for C-1, C-4 to C-8 and C-17.
2. *TX-8 in both directions* (proposed revision). "A policy that changes a country's receipts from exports, or its payments for imports, changes the means for the other side of its trade in the same direction; under a floating rate, it also changes what every other exporter or import-competing seller receives in the domestic currency." Derivation: CR-8b, CR-9 (currency), CR-6 in the market for foreign currency. TX-8 as written passes the symmetry test only for one direction. Used here for C-32 to C-35.
3. *RS-17 Circular trade under a payment or charge conditioned on crossing a boundary* (proposed). If a payment is made (or a charge is levied) when a good crosses a boundary in one direction, and the cost of crossing back is less than the payment, then goods cross twice: illegally, where the return is forbidden but hard to detect (`informal_activity` increase), and legally, where an equivalent good can cross the other way (swaps, origin rules, processing that changes a good's legal identity). Derivation: CR-4 (x: one crossing, y: two crossings) with CR-1 (what the rules allow on each crossing) and CR-7a. The same move appears in excise refunds on exports, in tariffs with drawback, and in WE-010's border trade. Used here for C-13, C-19, C-20 and C-25.

**(d) Vocabulary.**
1. *No `exchange_rate` variable.* The currency link in reverse (C-35) changes the price of foreign currency. It had to be recorded as other exporters' `net_price_received` in tals, which hides the common cause. Proposed: `exchange_rate` (domestic currency per unit of foreign currency).
2. *No variable for public spending on a subsidy.* `tax_revenue` records what a tax brings in; nothing records what a subsidy pays out, or `subsidy_outlay_vs_static_projection` (here above projection because of added tonnes and round trips). Proposed: `subsidy_outlay` and `subsidy_outlay_vs_static_projection`, the mirror of TX-9's variables.
3. *No variable for resources used up in evasion.* The trucking of round-trip wheat is used up (CR-8c) but has no home except `informal_activity`, which records the volume of evasion, not the resources it uses. `compliance_cost` covers only those complying. Proposed: `evasion_cost`.
4. *No generic actor classes for foreign buyers and sellers.* 2.2 lists `neighboring_jurisdictions` but not `buyers.foreign` and `sellers.foreign`, which both this example and WE-013 needed. Proposed: add them.
5. *Instrument types.* `per_unit_subsidy` does not say whether the subsidy is on production, consumption or export, and the subsidy patterns (SB-2) assume one that lowers buyers' price. Proposed: a parameter `subsidy.base` (output, purchase, export, import) in 2.3.
