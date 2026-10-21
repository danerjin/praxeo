# WE-065 / Analysis: Deficiency payments to wheat growers with a Th 220 target price

Analyst: core-only re-run (Handbook 1.0)  |  Rules: core rules CR-1 to CR-12 only  |  Status: compared

## 1. Policy record

**Brisklund Wheat Price Assurance Act.** Brisklund (about 9 million people, currency the thaler, Th) has about 18,000 farms growing wheat on about 570,000 hectares, producing about 4.0 million tonnes a year (about 7.0 t/ha). About 2.5 million tonnes are used at home (1.4 by millers, 1.1 as feed) and about 1.5 million tonnes are exported, under 1% of world trade (world production about 800 Mt, trade about 200 Mt). The farm-gate price follows the export price less freight. Over the past ten marketing years it ranged from Th 175 to Th 285 a tonne, averaged about Th 232, and was below Th 220 in four years, by about Th 20 on average. Milling varieties fetch about Th 18 a tonne more than feed varieties and yield about 0.6 t/ha less. Barley (about 1.2 Mt, partly exported) competes with wheat for land and with feed wheat in feed. About 40% of wheat land is rented on three- to five-year leases; land sells for about Th 12,000/ha and rents for about Th 300/ha a year. The Farm Register records each registered farm's annual harvest declarations and, since 2026, its "established production" (average wheat output 2022 to 2026, about 3.8 Mt in all). Registration requires agricultural activity on the farm.

The bill was introduced with the government's majority on 10 February 2027 and enacted on 30 June 2027. It covers crop years 2028 to 2032 (winter wheat for 2028 is sown in autumn 2027). Parliament must review the target price before 2032.

**Figures.** Payment rate = Th 220 less the national average farm-gate price for the marketing year, if positive. Expected payment on past prices about Th 7 to Th 8 a tonne a year; at a price of Th 180, Th 40 a tonne: about Th 160 million on 4.0 Mt (U1-a) or Th 152 million on 3.8 Mt (U1-b), against a general budget of about Th 40 billion. 2028 futures about Th 228. Payments office about Th 4 million a year. Switching a hectare from milling to feed variety gains about Th 5/ha more than without the payment at a payment of Th 8, about Th 24/ha at Th 40.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Brisklund. Neighbors grow wheat without such payments; grain crosses the borders by rail and road. | §1. |
| Announced / enacted / effective / expires | Announced 10 February 2027 (bill introduced with a majority); enacted 30 June 2027; crop years 2028 to 2032; review before 2032. | §1, §12. |
| Enforcement (who, penalties, resources) | Ministry of Agriculture payments office: claims on the Farm Register; harvest declarations checked by sampling (about 3% of farms a year); false declarations: repayment and a fine of up to twice the payment. | §8 to §10. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Deficiency payment | `per_unit_subsidy` (contingent) under U1-a; `lump_sum_subsidy` (contingent) under U1-b | Wheat | Paid to the holder (person registered as farming the land) of each registered farm | Rate: Th 220 less the national average farm-gate price for the marketing year, if positive. Paid in December after the marketing year. | — |
| K2 Funding | `revenue_use` (outlay) | K1 | The general budget | "Such sums as are needed ... shall be paid out of the Consolidated Fund." | — |
| K3 Administration | Enforcement | K1 | Ministry payments office, from its general appropriation | About Th 4 million a year. | — |

Existing rules that stay in the counterfactual: the Farm Register and its registration rule; no tariff or quota on wheat; leases freely negotiated. **Counterfactual law:** no payment; growers receive the export-parity price.

Unclear provision:
- **U1, actual output or a historical base.** §4(1) pays "on the farm's wheat production for the crop year"; §2 defines wheat production as "the production of wheat recorded for the farm in the Farm Register", which records both annual declarations and established production. U1-a: payment on the harvest declared for the crop year. U1-b: payment on established production, "for the crop year" fixing only the year whose price sets the rate. No probability is given to either reading.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | CR-1 operations | Core rules applied |
|---|---|---|---|---|
| K1 Payment | binary (the state gives) | Yes in expectation for every crop year: the price may fall below Th 220 (A-2), and the Act is applied (A-1) | U1-a: 3 (attaches a contingent payment to each tonne of wheat produced and declared; the expected payment raises what each tonne is expected to bring); U1-b: 4 (a contingent transfer to each holder fixed by 2022 to 2026 history, which no current choice changes, except registration, CR-1 0.7) | CR-4 (per reading), CR-5c, CR-7b, CR-7c, CR-8b, CR-10a, CR-3 0.9 (U1-b: payment on a standard) |
| K2 Funding | binary (the state takes from the general budget) | Yes in low-price years (A-2) | 4 (from taxpayers, other spending or future taxpayers) | CR-8b, CR-8 0.7, CR-8 0.8 (contingent payers) |
| K3 Administration | binary; enforcement | Yes | 4 (appropriation); 3 (declaration checks and penalties attached to false claims, U1-a) | CR-8c, CR-4 (x: declare truly, y: overstate) |

The Act fixes no market price: the payment is added to the market price, which stays free and follows export parity (A-10). CR-6 enters only in the world market and in the markets for land and substitutes.

## 3. Actor classes

| Actor class | Role | How its options change (CR-1) |
|---|---|---|
| growers.registered | Holders of registered farms growing wheat | U1-a: op 3 on each tonne; U1-b: op 4 (contingent). |
| growers.marginal | Growers for whom wheat ranks narrowly against barley, other crops or less intensive growing | U1-a: CR-4 (x: other crop, y: wheat). |
| growers.new | Growers without established production (entrants, farms new to wheat after 2026) | U1-a: op 3 as others; U1-b: nothing. |
| growers.below_standard, growers.above_standard | Under U1-b, holders whose current output is below or above their established production | U1-b: CR-3 0.9 split: those below receive more per tonne grown than those above. |
| growers.overstating | Growers who overstate declarations or declare bought grain (A-6) | U1-a: CR-4 (x: declare truly, y: overstate), with 3% sampling and penalties. |
| growers.hedging | Growers who buy put options or forward sales | CR-4 (x: buy cover, y: rely on the payment). |
| landowners.wheat_land | Owners of wheat land, including the 40% let to tenants | Through CR-7b and CR-7c: the payment's yield settles on land. |
| tenants.wheat_land | Tenants on three- to five-year leases | Contract: rent fixed until renewal (CR-6 0.7), then renegotiated. |
| landowners.other_land | Owners of pasture or other land convertible to wheat | U1-a: CR-4 (x: keep as pasture, y: convert). |
| buyers.pasture | Livestock farmers who rent pasture | Through CR-9 (same land, other use). |
| buyers.domestic | Millers and feed buyers | Through CR-9: the domestic price follows export parity. |
| buyers.feed | Feed compounders and livestock farmers | Through CR-9 (substitute): feed wheat and feed barley. |
| sellers.foreign | Wheat growers abroad | Through CR-9 (same world market). |
| sellers.neighboring | Grain sellers across the border | Through CR-9 (across_border): grain bought to be declared (U1-a). |
| seed_sellers | Sellers of wheat seed by variety | Through CR-9 (input_to). |
| intermediaries | Sellers of put options and forward contracts | Through CR-9 (substitute for the payment as price cover). |
| lenders | Banks lending to wheat growers | Through CR-9 (contract: loans secured on farm income and land). |
| exporters.other, buyers.imports | Other exporters; buyers of imports | Through CR-9 (currency). |
| holders_of_currency | Buyers of foreign exchange | Through CR-9 (currency). |
| taxpayers or recipients of other spending or future taxpayers | Payers through the general budget | Op 4 (K2, K3). |
| officials.payments_office | Pays claims and checks declarations | Op 4; tasks of K3. |
| farm_unions, holders of established production, millers | Organized interests | CR-4 (x: accept, y: lobby) over U1 and renewal. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | growers.registered | resources_available_other_uses (payments received) | increase | medium | CR-1 op 3 or op 4, CR-8b | A-1, A-2 |
| C-2 | officials.payments_office | subsidy_outlay | increase | medium | CR-1 op 4, CR-8b | A-1, A-2 |
| C-3 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses | at_least_one_decrease | medium | CR-8b, CR-8 0.7, CR-8 0.8 | A-1, A-2 |
| C-4 | growers.registered | net_price_received (expected, per tonne, including the payment) | U1-a: increase; U1-b: no_change | short; medium | CR-1 op 3 per reading, CR-5c, CR-12e | A-1, A-2, A-18 |

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-5 | growers.marginal | quantity_supplied (wheat) | U1-a: increase; U1-b: no_change | medium | CR-4, CR-4c, CR-7a, CR-10a | A-3, A-4, A-1, A-2 |
| C-6 | growers.marginal | quantity_substitute (barley and other crops on wheat land) | U1-a: decrease; U1-b: no_change | medium | CR-4, CR-7a | A-3, A-4 |
| C-7 | growers.registered | product_attribute (share of feed varieties in wheat sown) | U1-a: increase; U1-b: no_change | medium | CR-4 (x: milling, y: feed variety) | A-5 |
| C-8 | growers.registered | quantity_supplied (feed wheat) | U1-a: increase; U1-b: no_change | medium | CR-12a, CR-12d | A-3, A-5 |
| C-9 | growers.registered | quantity_supplied (milling wheat) | U1-a: ambiguous; U1-b: no_change | medium | CR-12b | A-3, A-5 |
| C-10 | growers.overstating | legal_breach (overstated declarations, bought grain declared as own) | U1-a: increase; U1-b: no_change | medium | CR-4 (x: comply, y: violate) | A-6 |
| C-11 | growers.overstating | cross_border_purchases (grain bought abroad and declared) | U1-a: increase; U1-b: no_change | medium | CR-4 (x: buy here, y: across the border) | A-6 |
| C-12 | officials.payments_office | non_tax_receipts (repayments and fines) | U1-a: increase; U1-b: no_change | medium | CR-1 op 3, CR-8b | A-6 |
| C-13 | growers.hedging | quantity_substitute (put options and forward sales for price cover) | decrease | short; medium | CR-4 (x: buy cover, y: rely on the payment) | A-7 |
| C-14 | farm_unions, holders of established production, millers | lobbying_effort (on the reading of U1) | increase | short | CR-4, CR-12 0.9, CR-8c | A-8 |
| C-15 | farm_unions, holders of established production | lobbying_effort (on renewal and the target price at the review) | ambiguous | medium | CR-4 1.0, CR-12b | A-8 |
| C-16 | officials.payments_office | enforcement_cost | increase | medium | CR-1 op 4, CR-8c | - |
| C-17 | landowners.other_land | investment_target (conversion of pasture and other land to wheat) | U1-a: increase; U1-b: no_change | medium | CR-4, CR-7a | A-13, A-12, A-3 |

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-18 | landowners.wheat_land | asset_value (wheat land; under U1-b, land of farms with established production) | increase | short (from February 2027) | CR-7b, CR-7c, CR-10c | land input_to wheat (close) | A-11, A-12, A-14, A-2 |
| C-19 | tenants.wheat_land | price_paid (rent on renewed leases) | increase | medium | CR-7b, CR-5c, CR-6 0.7 | contract (lease) | A-14, A-15, A-12, A-2 |
| C-20 | landowners.wheat_land | subsidy_share_received | increase | medium (as leases renew) | CR-7b, CR-6 0.7 | contract (lease) | A-14, A-15 |
| C-21 | buyers.pasture | price_paid (pasture rent) | U1-a: increase; U1-b: no_change | medium | CR-9, CR-7a | same land, other use (partial) | A-13, A-3 |
| C-22 | growers.registered (as exporters) | quantity_traded (wheat exports) | U1-a: increase; U1-b: no_change | medium | CR-9, CR-6 | domestic wheat across_border to world market (close) | A-3, A-10, A-18 |
| C-23 | sellers.foreign | net_price_received (world wheat price) | U1-a: decrease; U1-b: no_change | medium | CR-9, CR-6, CR-6 1.0, CR-12e | same world market | A-3, A-9, A-18 |
| C-24 | sellers.foreign | quantity_supplied (wheat) | U1-a: decrease; U1-b: no_change | medium | CR-4c, CR-9 | same world market | A-3, A-9 |
| C-25 | buyers.domestic | price_paid (wheat) | U1-a: decrease; U1-b: no_change | medium | CR-9, CR-6 | export parity (close) | A-3, A-10, A-18, A-9 |
| C-26 | growers.registered | net_price_received (market price, excluding the payment) | U1-a: decrease; U1-b: no_change | medium | CR-9, CR-6 | export parity | A-3, A-10, A-18, A-9 |
| C-27 | buyers.feed | price_substitute (feed barley) | U1-a: ambiguous; U1-b: no_change | medium | CR-12b, CR-9 | feed barley substitute for feed wheat (close) | A-3, A-4, A-20 |
| C-28 | seed_sellers | quantity_traded (feed-variety wheat seed) | U1-a: increase; U1-b: no_change | medium | CR-9, LW-10 | seed input_to wheat | A-5 |
| C-29 | intermediaries | quantity_traded (wheat put options and forward contracts) | decrease | medium | CR-9 | price cover substitute for the payment | A-7 |
| C-30 | sellers.neighboring | quantity_traded (grain sold into Brisklund to be declared) | U1-a: increase; U1-b: no_change | medium | CR-9, CR-5 | across_border | A-6 |
| C-31 | growers.registered | interest_rate | decrease | medium | CR-9, CR-6 | contract (loans) | A-16, A-1, A-2 |
| C-32 | holders_of_currency | exchange_rate | U1-a: decrease; U1-b: no_change | medium | CR-9 (currency) | currency | A-3, A-10, A-17 |
| C-33 | exporters.other | net_price_received (in thaler) | U1-a: decrease; U1-b: no_change | medium | CR-9 (currency), CR-6 | currency; competitors for foreign buyers' means | A-3, A-10, A-17 |
| C-34 | buyers.imports | price_paid (imports, in thaler) | U1-a: decrease; U1-b: no_change | medium | CR-9 (currency) | currency | A-3, A-10, A-17 |
| C-35 | growers.new | resources_available_other_uses (payments received) | U1-a: increase; U1-b: no_change | medium | CR-1 per reading, CR-8b | - | A-1, A-2 |

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
|---|---|---|---|---|
| growers.registered, net_price_received including the payment, U1-a | Expected payment Th 7 to Th 8 a tonne (A-2) | World and farm-gate price fall from added output (C-26) | A-18 (empirical, p 0.9): the price fall is far smaller than the expected payment; also, the rate rises one for one as the farm-gate price falls below Th 220, so in paying years the total is held at Th 220 (arithmetic on the rate) | U1-a: increase (C-4) |
| growers.registered, quantity_supplied (milling wheat), U1-a | More wheat area and intensity (A-3) | Switch to feed varieties (A-5) | None | U1-a: ambiguous (C-9) |
| growers.registered, quantity_supplied (feed wheat), U1-a | Area (A-3) and switch (A-5), independent chains | - | CR-12d: holds if either chain's premises hold | U1-a: increase (C-8) |
| buyers.feed, price_substitute (feed barley), U1-a | Less barley grown (C-6) | Cheaper and more abundant feed wheat draws feed buyers from barley (A-20, C-25) | None | U1-a: ambiguous (C-27) |
| sellers.foreign, net_price_received, U1-a | - | Added Brisklund supply | Response argument (CR-12e, 1.0): foreign growers' contraction cannot restore the old price, because their cost per tonne does not rise as they contract and they cannot contract at once (A-9) | U1-a: decrease (C-23) |
| buyers.domestic, price_paid, U1-a | - | Export parity falls (C-23) | Domestic use takes a tiny share of the added supply; the price stays at export parity (A-10) | U1-a: decrease (C-25) |
| farm_unions, lobbying_effort on renewal | Concentrated stake in keeping the payment at the review | Counterfactual campaign for support (the 2025 to 2026 campaign) is no longer needed (CR-4 1.0) | None | ambiguous (C-15) |
| taxpayers group, resources_available_other_uses | - | Payments (C-2) and office costs (C-16); fines (C-12, U1-a) return a little | Arithmetic: fines are at most twice the payments on the 3% sampled and only on false claims, a small share of Th 7 to Th 8 a tonne on 3.8 to 4.0 Mt | at_least_one_decrease (C-3) |
| landowners.wheat_land, asset_value | Expected payments capitalized (CR-7c) | - | Both readings push the same way: U1-a through the per-tonne yield of wheat land, U1-b through the payment attached to registered farms with history fixed before the Act was expected (CR-7 0.7, a windfall) | increase (C-18) |
| growers.registered, resources_available_other_uses | Payments (C-1) | Higher rents on renewed leases (C-19), for tenants only | Different subgroups: tenants are split from owners (C-19, C-20); CR-7b says the payment's lasting gain settles on land, so tenants' gain is limited to the period before renewal | increase (C-1) for holders as a class; tenants' share falls as leases renew (C-20) |

No chains cancel by construction (CR-12f).

## 8. Time structure

- **Announcement (10 February 2027).** The bill had a majority, so land buyers expected the Act from then (A-11). Land values rise from then (C-18), part of the way as the probability of passage rose and with a further part for the chance of renewal (CR-7c). Buyers of land after February 2027 pay for the expected payments and gain nothing from them (CR-7c).
- **Sowing (autumn 2027).** Winter wheat for 2028 is sown before the 2028 price is known, on the expected payment (CR-10a): the supply response under U1-a (C-5, C-6, C-7) starts with the 2028 harvest.
- **Payments.** Paid in December after each marketing year, only in years when the price is below Th 220 (A-2). The payment is contingent, so growers' receipts (C-1) and the outlay (C-2) come in some years and not others; the planting response rests on the expected payment in every year.
- **Leases.** Rents on existing leases are fixed until renewal (CR-6 0.7); most leases come up within the term (A-15), so tenants keep the payment at first and landowners capture it as leases renew (C-19, C-20). This is a per-window shift in who receives the payment, recorded as the subsidy share.
- **Review and expiry (2032).** As the end approaches, land values carry only the remaining payments and the chance of renewal (CR-7c, CR-10c); lobbying for renewal is signed ambiguous (C-15). After 2032 without renewal, land converted to wheat (C-17) stays converted (CR-10b); whether it stays in wheat is not signed.

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-3 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses | at_least_one_decrease | About Th 7 to Th 8 a tonne in expectation, Th 152 to 160 million in a Th 180 year, and Th 4 million a year for the office | CR-8b, CR-8 0.7 |
| C-6 | growers.marginal | quantity_substitute (barley and other crops) | U1-a: decrease; U1-b: no_change | Barley and other crops not grown on land moved to wheat | CR-8a, CR-4 |
| C-14 | farm_unions and others | lobbying_effort (on U1) | increase | Staff time and money | CR-8c |
| C-16 | officials.payments_office | enforcement_cost | increase | Th 4 million a year | CR-8c |
| C-17 | landowners.other_land | investment_target (conversion) | U1-a: increase; U1-b: no_change | Draining and liming spent on converting land that would have stayed pasture | CR-8a |
| C-21 | buyers.pasture | price_paid (pasture rent) | U1-a: increase; U1-b: no_change | Grazing given up or paid for at a higher rent | CR-8a, CR-9 |

CR-8's symmetry: payments to growers (C-1, C-35) are the outlay (C-2) borne by the budget group (C-3); the part captured by landowners (C-18, C-20) is part of the same transfer, not an addition; tenants' higher rents (C-19) are landowners' receipts.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | The Act is in force for 2028 to 2032 and payments are made as it provides. | enforcement | 0.9 | Enacted; open-ended appropriation; payments office set up. | C-1 to C-5, C-31, C-35 fail. |
| A-2 | The national average price falls below Th 220 in at least one of the five crop years. | other | 0.85 | Four of the past ten years; futures at Th 228 with wide spread. | C-1, C-2, C-3, C-35 fail; expected-payment chains (C-4, C-18) weaken but keep their sign while a fall is possible. |
| A-3 | Some growers at the margin sow more wheat, or grow it more intensively, when the expected price including the payment rises. | substitutability | 0.85 | Rotations; past area responses. | C-5, C-6, C-9, C-17, C-21 to C-27, C-32 to C-34 fail; C-8 keeps the A-5 chain. |
| A-4 | Land can be moved between wheat and other crops from year to year. | alternative_uses | 0.9 | Rotations; soil suitability. | C-5, C-6, C-27 fail. |
| A-5 | Some growers switch to high-yield feed varieties when every tonne is paid alike. | other | 0.6 | Yield gap 0.6 t/ha against Th 18 premium; seed sales. | C-7, C-28 fail; C-8 keeps the A-3 chain; C-9 becomes U1-a: increase. |
| A-6 | Declarations are checked only by sampling, so some growers overstate or declare bought grain as their own. | enforcement | 0.55 | 3% sampled; free cross-border movement. | C-10, C-11, C-12, C-30 fail. |
| A-7 | Some growers who now buy put options or forward sales for price cover buy less. | substitutability | 0.7 | Hedging by larger growers. | C-13, C-29 fail. |
| A-8 | Farm unions, millers and holders of established production can organize at a cost below their stakes. | other | 0.9 | Existing unions; 2025 to 2026 campaign. | C-14, C-15 fail. |
| A-9 | Foreign growers' cost per tonne does not rise as their output contracts, and they cannot contract at once. | other | 0.85 | World cost structure; seasonal land commitment. | C-23, C-25, C-26 lose the dominance premise (sign becomes a decrease or no change); C-24 fails. |
| A-10 | The domestic farm-gate price follows export parity in every year (Brisklund exports in every year). | other | 0.9 | Exports of 1.5 Mt in each of the past ten years. | C-22, C-25, C-26, C-32 to C-34 fail. |
| A-11 | Land buyers expected the Act from February 2027 and expect it to run its term, with some chance of renewal. | expectations | 0.8 | Government majority; land reports. | C-18 timing fails; sign from enactment stands. |
| A-12 | Wheat land with history is in fixed supply in the short run, and converting other land does not get cheaper per hectare as more is converted. | durability | 0.8 | Soil limits; conversion costs. | C-18, C-19 lose the CR-7b premise; C-17 unaffected in sign. |
| A-13 | Some pasture or other land can be converted to wheat. | alternative_uses | 0.7 | Land-use surveys. | C-17, C-21 fail. |
| A-14 | Land has fewer alternatives than tenants' labor and machinery, and leases are let competitively. | substitutability | 0.7 | Tenancy market; contractors. | C-18, C-19, C-20 lose the ranking of shares (CR-7b). |
| A-15 | Most leases come up for renewal within the five-year term. | durability | 0.85 | Three- to five-year leases. | C-19, C-20 fail within the term. |
| A-16 | Lenders lower rates to wheat growers whose income in low-price years is now higher. | other | 0.6 | Banks' farm-risk models. | C-31 fails. |
| A-17 | The rise in wheat exports is not offset by capital flows in the medium run. | other | 0.55 | Floating exchange rate; capital account. | C-32, C-33, C-34 fail. |
| A-18 | The effect of Brisklund's added output on the world price is far smaller than the expected payment per tonne. | other | 0.9 | Added output of a few percent of 4 Mt against 800 Mt; Th 7 to Th 8. | C-4 (U1-a) becomes ambiguous; C-22, C-23, C-25, C-26 keep their direction but lose the small-share premise. |
| A-19 | Under U1-b, some land that would have left farming is kept registered, and some of it grows wheat. | other | 0.35 | Land leaving farming goes mostly to building. | Not reported. |
| A-20 | Feed buyers substitute between feed wheat and feed barley of a given quality. | substitutability | 0.7 | Feed rations; compounders' practice. | C-27 loses its (−) chain (becomes U1-a: increase). |

**Not reported** (an assumption below 0.5):
- Under U1-b, land kept registered rather than sold for building, some of it growing wheat (A-19, p 0.35): would give U1-b a small increase in wheat output and in registered land, and a lower supply of land for building.
- Under U1-a, whether domestic milling wheat output falls below millers' 1.4 Mt so that millers import at a higher price: no case assumption gives the milling share of output, and C-9 is ambiguous; not signed.

No new premises were needed (no A-N).

### Final check before the report

1. **Uncombined chains.** All keys with opposing chains are in section 7 (expected price including payment, milling wheat, feed barley price, foreign price, lobbying on renewal, budget). The announcement and lease-window chains have the same sign as the later chains on their keys.
2. **Group signs.** The budget payers are a group (C-3); no rule here licensed only "at least one of" several variables otherwise.
3. **Baseline.** All signs against no payments. U1-b's "no_change" is against the counterfactual, not against U1-a; the outlay is an increase under both readings, larger under U1-a in years of added output, which is a comparison of readings, not a consequence.
4. **Worse off is not poorer.** The budget group pays a sum it cannot avoid (C-3). Tenants are signed on the rent paid (C-19), not on their spending elsewhere. Buyers of pasture are signed on the rent, not on their other spending.
5. **Timing shifts.** Lease renewals move the payment from tenants to landowners over the term (C-20); no action is moved between windows against the counterfactual, so no per-window pair is needed.
6. **Both sides of every transfer.** Payments: C-1, C-35 against C-2, C-3. Rents: C-19 against C-20. Fines: C-12 (receipts) against C-10 (the breaching growers repay). Land value: captured by owners at announcement; later buyers pay it (CR-7c, noted in section 8).
7. **Every actor class, every core rule.** CR-4 per reading for growers, hedgers, overstaters, convertors, lobbyists; CR-6 in the world market (C-23), feed market (C-27), land and pasture (C-19, C-21); CR-7 for land (C-18 to C-20) and conversion (C-17); CR-9 along export parity, substitutes (barley, price cover), input_to (seed, land), contracts (leases, loans), across_border (C-30) and currency (C-32 to C-34). Proximity and gifts: none found.
8. **Unstated premises.** Lobbying rests on A-8; every response on a margin premise (A-3 to A-7, A-13, A-16, A-20). No premise outside the case assumptions was needed.
9. **Pattern baselines.** No patterns used.

## 11. Report

**The policy:** For the harvests of 2028 to 2032, Brisklund pays the holder of each registered wheat farm Th 220 a tonne less the national average farm-gate price, when that price is below Th 220, out of the general budget. The payment is on either the harvest declared for the year (U1-a) or the farm's 2022 to 2026 average output (U1-b); the text does not decide which.

**Visible consequences:** Growers receive payments in low-price years (C-1, C-35 under U1-a for new growers); the budget pays them (C-2), at the cost of taxpayers, other spending or future taxpayers (C-3). Under U1-a the expected price per tonne including the payment rises (C-4).

**Invisible consequences:**
- *Under U1-a only:* more wheat is grown (C-5), less barley and other crops (C-6), and more feed varieties (C-7, C-8, C-28); pasture is converted (C-17) and pasture rents rise (C-21); exports rise (C-22), the world and domestic wheat price falls slightly (C-23, C-25, C-26) and foreign growers grow less (C-24); the thaler rises (C-32), other exporters receive less (C-33), imports are cheaper (C-34); some growers overstate declarations or declare grain bought abroad (C-10, C-11, C-30), and some are fined (C-12).
- *Under both readings:* wheat land rises in value from February 2027 (C-18); rents rise as leases renew (C-19), so landowners capture more of the payment (C-20); growers buy less price cover (C-13, C-29) and borrow more cheaply (C-31); interests lobby over the reading (C-14); the office costs Th 4 million a year (C-16).

**Ambiguous effects:** under U1-a, milling wheat output (more area against the switch to feed varieties, C-9) and the price of feed barley (less barley against cheaper feed wheat, C-27); lobbying at the 2032 review (C-15).

**Key conditions:** whether growers respond at the margin (A-3, 0.85; A-4, 0.9) and switch varieties (A-5, 0.6), which matters only under U1-a; the price falls below Th 220 at least once (A-2, 0.85); land has fewer alternatives than tenants (A-14, 0.7); the world price effect is small (A-18, 0.9).

**What this analysis cannot say:** how large any effect is, how often payments are made, how the payment divides between tenants and landowners, whether U1-a or U1-b is right, or whether the policy is good. Environmental effects of converting pasture and of more intensive growing are out of scope, as are health and safety effects.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | growers.registered | resources_available_other_uses (payments received) | increase | medium | visible | B | CR-1 (U1-a: op 3, a payment on each tonne declared; U1-b: op 4, a contingent transfer on established production; under U1-b, CR-3 0.9 splits holders by current output against the standard); CR-8b (the payment adds to the recipient what it takes from the budget); made in years with a price below Th 220 (A-2) | A-1, A-2 |
| C-2 | officials.payments_office | subsidy_outlay | increase | medium | visible | B | CR-1 op 4 (K1, K2: paid from the Consolidated Fund); CR-8b | A-1, A-2 |
| C-3 | taxpayers or recipients of other spending or future taxpayers | resources_available_other_uses | at_least_one_decrease | medium | invisible | B | CR-8b and CR-8 0.7 (payers from the general budget are a group); CR-8 0.8 (contingent: only in years with a payment, A-2); K3's Th 4 million a year adds to it; fines (C-12) return a share that arithmetic shows is small | A-1, A-2 |
| C-4 | growers.registered | net_price_received (expected, per tonne, including the payment) | U1-a: increase; U1-b: no_change | short; medium | visible | B | U1-a: CR-1 op 3 (each tonne brings the expected payment, Th 7 to Th 8); CR-5c; CR-12e (A-18: the fall in the market price from added output, C-26, is far smaller than the payment; in paying years the rate rises one for one as the price falls). U1-b: the payment does not depend on the tonnes grown, so what a tonne brings is unchanged | A-1, A-2, A-18 |
| C-5 | growers.marginal | quantity_supplied (wheat) | U1-a: increase; U1-b: no_change | medium | visible | B | U1-a: CR-4 (x: barley or another crop, y: wheat; y made better, so growers for whom wheat ranked narrowly below switch, A-3, A-4); CR-4c (more intensive growing: the last tonne brings the payment too); CR-7a (land moves to the use that yields more); CR-10a (sown from autumn 2027 on the expected payment). U1-b: no change through the price at the margin; the change in means names no use (CR-4) | A-3, A-4, A-1, A-2 |
| C-6 | growers.marginal | quantity_substitute (barley and other crops on wheat land) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-4 (the mirror of C-5: x now barley, made worse relative to wheat); CR-7a; CR-8a (land moved to wheat is withdrawn from barley) | A-3, A-4 |
| C-7 | growers.registered | product_attribute (share of feed varieties in wheat sown) | U1-a: increase; U1-b: no_change | medium | invisible | B | U1-a: CR-4 (x: milling variety, y: feed variety; every tonne is paid alike, so the 0.6 t/ha extra yield gains about Th 5/ha more at a payment of Th 8 and Th 24/ha at Th 40, figures; growers for whom the two were close switch, A-5). U1-b: the payment does not depend on tonnes | A-5 |
| C-8 | growers.registered | quantity_supplied (feed wheat) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-12a: chain 1, more area and intensity (C-5, A-3); chain 2, the variety switch (C-7, A-5); CR-12d: independent chains, holds if either chain's premises hold (A-3 or A-5) | A-3, A-5 |
| C-9 | growers.registered | quantity_supplied (milling wheat) | U1-a: ambiguous; U1-b: no_change | medium | invisible | B | CR-12b: (+) more wheat area and intensity (C-5, A-3); (−) switch to feed varieties (C-7, A-5). No dominance premise | A-3, A-5 |
| C-10 | growers.overstating | legal_breach (overstated declarations, bought grain declared as own) | U1-a: increase; U1-b: no_change | medium | invisible | B | U1-a: CR-4 (x: declare truly, y: overstate or declare bought grain; 3% sampling makes the expected penalty smaller than the gain for some, A-6); CR-12 0.9 (breach exists only under the policy). U1-b: established production is fixed in the Register from 2026, so declarations carry no payment | A-6 |
| C-11 | growers.overstating | cross_border_purchases (grain bought abroad and declared) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-4 (x: buy grain here, y: across the border; grain crosses freely, and grain bought abroad was not counted in national output, A-6) | A-6 |
| C-12 | officials.payments_office | non_tax_receipts (repayments and fines) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-1 op 3 (repayment and a fine of up to twice the payment attached to false declarations); CR-8b (what the caught growers pay the state receives; some of C-10 is detected by sampling) | A-6 |
| C-13 | growers.hedging | quantity_substitute (put options and forward sales for price cover) | decrease | short; medium | invisible | B | CR-4 (x: buy price cover, y: rely on the payment, which pays when the price is low under both readings; growers for whom cover was worth only narrowly more than its cost drop it, A-7) | A-7 |
| C-14 | farm_unions, holders of established production, millers | lobbying_effort (on the reading of U1) | increase | short | invisible | B | CR-4 (x: accept whatever guidance comes, y: lobby for the reading that pays them more: holders with high history for U1-b, expanding growers for U1-a); CR-12 0.9 (the question exists only under the Act); CR-8c | A-8 |
| C-15 | farm_unions, holders of established production | lobbying_effort (on renewal and the target price at the review) | ambiguous | medium | invisible | B | CR-12b: (+) CR-4 (x: accept expiry, y: lobby for renewal and a higher target; a concentrated stake, A-8); (−) CR-4 1.0 (the question of support was contested on the counterfactual path, the 2025 to 2026 campaign; with payments in place part of that campaign is not needed until the review). No dominance premise | A-8 |
| C-16 | officials.payments_office | enforcement_cost | increase | medium | invisible | A | CR-1 op 4 (Th 4 million a year); CR-8c | none |
| C-17 | landowners.other_land | investment_target (conversion of pasture and other land to wheat) | U1-a: increase; U1-b: no_change | medium | invisible | B | U1-a: CR-4 (x: keep as pasture, y: convert; y made better by the payment on its output, A-13); CR-7a (conversion continues until the yield on converted land net of conversion cost is in line, A-12). U1-b: converted land has no established production and receives nothing | A-13, A-12, A-3 |
| C-18 | landowners.wheat_land | asset_value (wheat land; under U1-b, land of farms with established production) | increase | short (from February 2027) | invisible | B | CR-7b (the lasting gain settles on land, which has fewer alternatives than tenants' labor and machinery, A-14, and is in fixed supply in the short run, A-12); CR-10c and CR-7c (the expected yield is capitalized when the Act becomes expected, A-11, partly as passage became likely, with a share for the chance of renewal). U1-a: through the per-tonne payment on land's output; U1-b: through the payment attached to registered farms by history fixed before the Act was expected (CR-7 0.7: a windfall to holders) | A-11, A-12, A-14, A-2 |
| C-19 | tenants.wheat_land | price_paid (rent on renewed leases) | increase | medium | invisible | B | CR-6 0.7 (rents on existing leases are fixed until renewal); CR-5c (at renewal the range of acceptable rents moves up by what the land now brings the tenant, since the payment goes to the person farming it); CR-7b (leases let competitively, land with fewer alternatives, A-14); most leases renew within the term (A-15) | A-14, A-15, A-12, A-2 |
| C-20 | landowners.wheat_land | subsidy_share_received | increase | medium (as leases renew) | invisible | B | CR-7b (the payment's lasting gain settles on the means that cannot move, A-14); CR-6 0.7 (until renewal tenants keep it, after renewal owners take more of it, A-15) | A-14, A-15 |
| C-21 | buyers.pasture | price_paid (pasture rent) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-9 (relation: the same land in its other use; conversion, C-17, withdraws pasture); CR-7a (rents on remaining pasture are pulled up toward the yield of conversion, A-13) | A-13, A-3 |
| C-22 | growers.registered (as exporters) | quantity_traded (wheat exports) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-9 (relation: domestic wheat across_border to the world market); domestic use moves little because the price follows export parity (A-10) and that price falls only slightly (A-18), so added output (C-5) goes to export | A-3, A-10, A-18 |
| C-23 | sellers.foreign | net_price_received (world wheat price) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-9 (same world market); CR-6 (more supply at each price moves the price to a lower clearing level); CR-6 1.0 (a small effect is signed; size under A-18); CR-12e 1.0 (response argument: foreign contraction does not restore the old price, since their cost per tonne does not rise as they contract and they cannot contract at once, A-9) | A-3, A-9, A-18 |
| C-24 | sellers.foreign | quantity_supplied (wheat) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-4c (at a lower price, the least valued tonnes on the least productive land are given up, A-9); CR-9 | A-3, A-9 |
| C-25 | buyers.domestic | price_paid (wheat) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-9 (the domestic price follows export parity, A-10; export parity falls, C-23); CR-6 | A-3, A-10, A-18, A-9 |
| C-26 | growers.registered | net_price_received (market price, excluding the payment) | U1-a: decrease; U1-b: no_change | medium | invisible | B | As C-25: the farm-gate price is export parity less freight (A-10) | A-3, A-10, A-18, A-9 |
| C-27 | buyers.feed | price_substitute (feed barley) | U1-a: ambiguous; U1-b: no_change | medium | invisible | B | CR-12b: (+) CR-9 and CR-6 (less barley is grown, C-6); (−) CR-9 (relation: feed barley substitute for feed wheat, A-20: more and cheaper feed wheat, C-8, C-25, lowers demand for barley). No dominance premise | A-3, A-4, A-20 |
| C-28 | seed_sellers | quantity_traded (feed-variety wheat seed) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-9 and LW-10 (relation: seed input_to wheat; demand for the seed follows the variety switch, C-7, and the added area, C-5) | A-5 |
| C-29 | intermediaries | quantity_traded (wheat put options and forward contracts) | decrease | medium | invisible | B | CR-9 (relation: price cover substitute for the payment; growers buy less, C-13) | A-7 |
| C-30 | sellers.neighboring | quantity_traded (grain sold into Brisklund to be declared) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-9 (relation: across_border; C-11); CR-5 (the sale takes place because the buyer can now claim on it) | A-6 |
| C-31 | growers.registered | interest_rate | decrease | medium | invisible | B | CR-9 (relation: contract, loans secured on income and land); CR-6 (lenders compete for borrowers whose income in low-price years is higher, A-16), under both readings | A-16, A-1, A-2 |
| C-32 | holders_of_currency | exchange_rate | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-9 0.7 (currency link: more exports, C-22, give residents more foreign currency to sell; not offset by capital flows, A-17) | A-3, A-10, A-17 |
| C-33 | exporters.other | net_price_received (in thaler) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-9 0.7 (exporters of different goods compete for foreign buyers' means; a lower price of foreign currency, C-32, lowers their thaler receipts); CR-6. Depth 4: chain stops here | A-3, A-10, A-17 |
| C-34 | buyers.imports | price_paid (imports, in thaler) | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-9 (currency: C-32). Depth 4: chain stops here | A-3, A-10, A-17 |
| C-35 | growers.new | resources_available_other_uses (payments received) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-1 per reading (U1-a: op 3 on their declared harvest; U1-b: no established production, so no operation); CR-8b | A-1, A-2 |

## Gaps found

**(a) Steps no core rule covers.**
- GAP-065-C1: A contingent payment that depends on a market price the payment itself lowers (the rate rises one for one as the price falls below Th 220). The rules derive each link, but none states that a payment of this form holds the total received at the target in paying years whatever the supply response; this was done by arithmetic on the rate (C-4).
- GAP-065-C2: Under U1-b the payment is a contingent transfer of means (CR-1 op 4). CR-4 says a change in means alone names no use, so U1-b's effect on wheat output through the growers' means (or through lower risk) could not be signed either way; "no_change" was recorded for the effect through the price at the margin only. The core rules have no way to state "no change through this channel; other channels unsigned" in one sign.

**(b) Core-rule wording that was hard to apply.**
- CR-1 0.7 says operation 4 is "a transfer that no choice avoids". Under U1-b the payment still depends on keeping the farm registered (agricultural activity), so it is operation 4 only for holders who would have stayed registered anyway; the rest (A-19, below the cut-off) face operation 3 on staying registered. The clarification does not cover transfers conditional on a status rather than on a quantity.
- CR-7c and "becomes expected" with a contingent payment: the capitalized value is of an expected payment that may be zero in every year. The rule handles probability of passage, but not the probability that the policy pays at all; treated as part of the expected yield.
- CR-4 1.0 on lobbying against a counterfactual contest gave `ambiguous` for renewal lobbying (C-15); it is unclear whether the earlier campaign's success makes the counterfactual contest smaller or larger.
- CR-6 0.7 (existing contracts) was needed to time the rent increase; the timing appears only in the horizon field and in the subsidy share, since the normal form has no per-window pair for a transfer moving between recipients.

**(c) Vocabulary missing from the ontology.**
- No variable for land use by crop (area in wheat); `quantity_supplied` and `quantity_substitute` were used.
- No variable for price risk borne or hedging; `quantity_substitute (price cover)` was used.
- No actor class for holders of a historical entitlement (established production) as distinct from current producers; `growers.below_standard` and `growers.above_standard` were named for CR-3 0.9.

## Comparison with the pattern-based analysis

**Summary.** The two versions agree on the main structure of the deficiency-payment case. Growers receive payments in low-price years and the budget group pays. Under U1-a the expected price per tonne rises, more wheat and less barley are grown, feed varieties gain share, some declarations are overstated, exports rise, and the world and domestic prices fall slightly, a fall the response argument (on A-9) keeps from being reversed. Foreign growers receive and grow less. Hedging falls, and the feed-barley price is ambiguous. Wheat land rises in value from February 2027 under both readings, rents rise at renewal so landowners capture more of the payment, and growers' borrowing rates fall. Under U1-b nearly everything else is `no_change`. Most differences are in recording. The pattern version gives per-state signs (years below and at or above the line); the core version gives one contingent sign. The core version also records more of the second-order classes: milling wheat, fines, pasture rents, neighboring sellers, import buyers and the exchange rate. There are two substantive errors in the pattern version. It signs lobbying on renewal and on the target at review as an increase "against none", although that is the farm-support question that was contested on the counterfactual path. And it records the formula's mix effect on the rate (C-22) against a static projection, not against no Act, which gives a U1-b `no_change` that contradicts its own C-1. The core version omitted several keys that are easy to derive: farms growing wheat, growers' compliance costs, the value of convertible land, and import-competing industries.

Counts: M 18, V 11, S 1, OP 11, OC 6.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-2 | V | | The pattern signs the outlay per state of the world (years below Th 220) on `treasury`. The core gives one contingent sign over the period on the payments office, resting on A-2. |
| C-2 | none | OC | J | Outlay in years at or above Th 220: `no_change`. True by the formula. The core rules do not require per-state signs, and the core version folded the contingency into A-2. |
| C-3 | C-1 | V | | Per state against one contingent sign. The core splits new growers (C-35) and, under U1-b, holders by position against the standard (CR-3 0.9). |
| C-4 | C-4 | V | | Per-tonne receipt in paying years (U1-a increase, U1-b no_change). The core states it only inside the derivation of C-4 ("in paying years the rate rises one for one", so the total is held at Th 220). That holds exactly only for a grower whose price equals the national average and in years the counterfactual price was also below the line. The sign is safe in substance. |
| C-5 | C-26 | V | | The pattern signs the market price only in years at or above the line. The core signs the farm-gate market price, excluding the payment, in all years, which is the more general key. Both are derived from CR-6 1.0 and A-10. |
| C-6 | C-4 | M | | Both rest on A-18 as dominance. The core adds the arithmetic on the rate. |
| C-7 | C-3 | V | | Per state against one contingent group sign. |
| C-8 | C-3 | M | | Whole-period group sign on A-2. |
| C-9 | C-5 | M | | |
| C-10 | none | OC | E (core) | Farms growing wheat: U1-a increase. This is CR-4 (x: no wheat, y: wheat) for whole farms at the margin. The core records area and conversion but not the number of farms. Omission. |
| C-11 | C-6 | M | | |
| C-12 | C-7 | M | | |
| C-13 | C-10 | M | | |
| C-14 | C-13 | M | | |
| C-15 (U1, the formula) | C-14 | M | | These questions exist only under the Act (CR-12 0.9). |
| C-15 (target at review, extension) | C-15 | S | P (analyst misapplied RS-7 1.0) | Pattern: increase, as "questions that exist only under the Act". Core: `ambiguous`. Whether to keep supporting wheat after 2032, and at what target, is the farm-support question that the pattern version itself says was debated in 2025 and 2026 and would have stayed contested. RS-7's 1.0 Unless clause and CR-4 1.0 require signing against that contest, which needs a premise. Relabelling the question as "renewal" does not make it new. The core is right. RS-7 as written is unclear on what counts as "the same question" (see Findings). |
| C-16 | none | OC | E (core) | Growers' compliance costs (claims, declarations): increase (CR-8c). The core records the office's costs only. Omission. |
| C-17 | C-23 | V | | The core records the world price once, on foreign sellers. The pattern records it for foreign buyers too. |
| C-18 | C-23 | M | | |
| C-19 | C-24 | M | | |
| C-20 | C-25 | M | | |
| C-21 | C-22 | M | | |
| C-22 | none | OC | E (pattern) | Pattern: `subsidy_outlay` (rate per tonne in paying years), U1-a increase, U1-b `no_change`, because the shift to feed varieties lowers the national average over grades. Against no Act the outlay rises from zero under both readings (its own C-1). The comparison actually made is with the rate the counterfactual prices per grade would give, which is a static projection, as its gap (d) 2 concedes. The content is valid and derivable from the core rules (CR-4 on varieties, arithmetic on the formula), but it needs a projection variable or qualifier. As recorded, the U1-b sign is wrong. The core version did not note the mix effect at all. |
| C-23 | C-27 | M | | |
| C-24 | C-28 | V | | The pattern claims all inputs (seed, fertilizer, contract harvesting) increase; the core claims feed-variety wheat seed. The pattern's aggregate leaves out the inputs no longer bought for barley (C-11): wheat replacing barley moves input demand in a direction that needs a premise on input use per hectare. Conversion and intensification push up. The core's narrower key needs no such premise. |
| C-25 | C-18 | M | | The pattern cites EN-12 for U1-b; the core cites CR-7 0.7 (a windfall when history was fixed before the measure was expected). |
| C-26 | none | OC | E (core) | Convertible land without wheat history gains value under U1-a (CR-7c, CR-10c, A-13). The core records conversion investment (C-17) but not the asset value. Omission. |
| C-27 | C-20 | M | | |
| C-28 | C-19 | M | | |
| C-29 | C-31 | M | | |
| C-30 | none | OC | E (core) | Import-competing industries: output, employment or hours as a group, `at_least_one_decrease` under U1-a (CR-9 0.7 currency, A-17). The core records import buyers' prices (C-34) but not the producers who compete with imports. Omission. |
| C-31 | C-33 | V | | Same chain, different variable: the pattern uses an output and employment group, the core uses net price received in thaler. |
| C-32 | C-3 | V | | The pattern's own note says this is C-7 and C-8 again. |
| C-33 | C-16 | M | | |
| C-34 | C-3 | V | | The core folds the Th 4 million a year into C-3, which rests on A-2. Administration costs fall every year and need no A-2, so the pattern's separate Tier A record is the right form. |
| C-35 | C-6 | V | | The pattern's own note marks this as C-11 again. The core adds pasture through C-17 and C-21. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-8 | OP | J | Feed wheat increases (CR-12a, d). This is implied by the pattern's C-9 and C-12, and its barley chain uses it. |
| C-9 | OP | E (pattern) | Milling wheat `ambiguous` under U1-a (more area against the switch to feed varieties). Valid and scorable. The pattern version derives both chains but does not record the key. |
| C-11 | OP | J | Grain bought abroad to be declared. The pattern folds it into `legal_breach` (C-13). The purchase is legal and the declaration is not, so the core's separate key is the cleaner one. |
| C-12 | OP | E (pattern) | Repayments and fines received increase under U1-a (CR-8b). Valid, though it needs a premise that some false declarations are detected by the 3% sampling, which the core folds into A-6. |
| C-17 | OP | J | Conversion of pasture to wheat (investment). The pattern records its effects (C-26, C-35) but not the conversion itself. |
| C-21 | OP | E (pattern) | Pasture rents increase under U1-a (CR-9, CR-7a, A-13). Valid. The pattern version does not follow the other use of the land. |
| C-29 | OP | J | Sellers of price cover sell less: the other side of the hedging exchange (pattern C-14). |
| C-30 | OP | E (pattern) | Neighboring sellers sell grain into Brisklund to be declared (CR-9, CR-5, A-6). The pattern version mentions it only inside C-13. |
| C-32 | OP | J | Exchange rate (thaler rises). The pattern version uses it only as a link in C-30 and C-31. |
| C-34 | OP | E (pattern) | Import prices in thaler fall under U1-a (CR-9 0.7). Valid. The pattern version's text says "imports rise" but records no class on that side. |
| C-35 | OP | J | Growers without established production: U1-a increase, U1-b `no_change`. A split of the pattern's C-3 that shows the reading matters for this group. |

### Findings

- **Pattern overclaims or hidden premises.** (1) Lobbying on renewal and on the target at review (C-15) is treated as a new question. It is the farm-support question that was contested on the counterfactual path, so RS-7 1.0 requires `ambiguous` without a premise. (2) C-22 is signed against a static projection, not against no Act, and its U1-b `no_change` contradicts C-1. (3) The aggregate input-supplier increase (C-24) needs a premise on inputs per hectare of wheat against barley.
- **Errors in the core version.** Omissions: farms growing wheat (pattern C-10), growers' compliance costs (C-16), the value of convertible land (C-26), import-competing industries (C-30), the formula's mix effect on the outlay (C-22, as a projection claim), and per-state signs where the contingency is a yearly price. Recording: C-3 folds every-year administration costs into a consequence conditioned on A-2. C-12 needs a detection premise. GAP-065-C1 is not a calculus gap: arithmetic on the rate is a dominance premise that CR-12e allows. GAP-065-C2 is a recording limit (one sign cannot say "no change through this channel, other channels unsigned"), not a missing rule.
- **Errors in the pattern version (omissions).** Milling wheat (core C-9), fines (C-12), pasture rents (C-21), neighboring sellers (C-30), import buyers (C-34).
- **Test of 1.0 verdicts against the core-only version.** No verdict was "failed". *SB-2, needed interpretation* (no wider-market clause): confirmed. The core version reached the same result directly from CR-6 0.7 and CR-6 1.0 (C-4, C-23, C-25) with no pattern. *SB-10* (correctly not applied): confirmed. The core version derives a lower domestic price (C-25), not SB-10's rise. *CR-8 0.8, contingent payers, worked with interpretation*: confirmed. The core version also struggled to record a yearly contingency and settled on one sign resting on A-2, losing the per-state signs. *CR-7c, capitalizing a contingent payment, needed interpretation*: confirmed. The core version raised the same point independently (its (b), second bullet). *CR-12 1.0, response argument read in its mirror for a price fall*: confirmed. The core version applied the same mirror reading (A-9, C-23) without remarking on it. *EN-12, needed one addition* (history belongs to the farm): partly confirmed. The core version got the U1-b windfall from CR-7 0.7 but did not note the former tenant's loss. *TX-8 mirror, worked with interpretation*: confirmed. The core version derived the currency chain directly from CR-9 0.7 (C-32 to C-34) and needed no export-subsidy wording. *Verdicts of "worked" that the core comparison contradicts*: RS-7 1.0 and CR-4 1.0 on lobbying (the renewal question was misclassified), and RS-16 1.0 as used for C-22 (the projection was recorded as the counterfactual).
- **Limits of the core rules.** None that produced a difference (no K). Unclear wording: CR-4 1.0 and RS-7 1.0 do not say when a question settled by the policy is "the same question" as one contested on the counterfactual path. CR-1 0.7's "a transfer that no choice avoids" does not cover a transfer conditional on a status (registration). CR-7c and CR-10c are silent on a yield that is itself contingent on a market price. CR-8 0.8 has no per-state form for a yearly contingency. CR-12 1.0's cost premise needs its mirror for a price fall.
