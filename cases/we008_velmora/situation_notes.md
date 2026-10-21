# WE-008 situation record: notes (written blind)

Assumption ids a1..a14 are the example's A-1..A-14 (statement, type, p copied). Every id is in the record; a3, a9, a11, a12 are not used as premises (see the end).

## Facts and what they rest on

| Fact | Rests on |
|---|---|
| e1: farmers.velmora sell raw milk to plants.commodity; e2: the same farmers to plants.specialty. Price vars net_price_received / price_paid | Sec. 1: K1 targets milk from Velmora farms, bound on Velmora plants that buy it. The commodity/specialty split comes from K2 (commodity plants, Board route) and a4 (specialty plants with a label) |
| held k1 above on e1 and e2 | K1 "at least $21.00 per cwt"; a1 (market below $21) |
| adjust e1 buyer plants.commodity quantity_demanded | K1 exempts milk produced outside Velmora; a5 (out-of-state milk arrives at transport cost). Plants control how much Velmora milk they take |
| outside e1 plants.commodity legal_breach | K2/K4 (origin certification); a6 (false certification undetected); a5 (cheap out-of-state milk to certify) |
| alt k1: plants.commodity quantity_substitute | K1 exemption of out-of-state milk; a5 |
| alt k1: farmers.velmora quantity_substitute (crops, beef) | a10 |
| stakes k1: farmers.velmora, plants.commodity | a14 |
| link plants.commodity quantity_substitute same_act farmers.neighboring quantity_traded | Sec. 1: Ostrand and Quillon dairy areas 30-90 miles away, no floor; a5. The out-of-state milk bought is the neighbors' sale |
| link farmers.velmora net_price_received yield farmers.entrants entry_rate | Sec. 1 unclear provision (farms moving in qualify after a three-month registration); a7; a2 |
| link farmers.velmora net_price_received yield plants.commodity investment_target | a13 (plants expand Board-route capacity as milk supply grows); a2 |
| yield e2 buyer plants.specialty | a4 (cannot pass the cost on; competitors not exposed) |
| yield e1 seller farmers.velmora | the floor itself (a1) |
| asset e1 seller factor_owners.specific (dairy land and barns) | a8 (fixed supply); a2 (the program is expected to last) |
| transfer e2 | a4: the floor is a transfer from specialty plants to farmers. I left out a transfer on e1 because K2 pays commodity plants back |
| compliance k4: plants.commodity, plants.specialty | K4 (segregate and document origin; audits, fines) |
| enforcer k4: officials.enforcement (the Dairy Board) | K4 |
| funded k2: taxpayers | Sec. 1: "sum sufficient" appropriation from the general fund |

## Not used as premises

- a3 (out-of-state supply does not replace all withdrawn product): it concerns the product market (price of cheese and powder). No fact I could write has a source effect there.
- a9 (donated stocks replace dairy bought by food programs) and a12 (stocks keep, Board disposes through K3 routes): they concern Board stocks and their disposal. No fact can create stocks as a source for a link (see below).
- a11 (repeal expected within two years, p 0.3): it is a rival expectation to a2. I did not make it a premise for anything.

## What the format could not hold

1. **K2, the purchase at a support price, with any quantity bought.** The format has held prices (removal of trades beyond a line) but no purchase commitment or subsidy. A held price on the product, with the Board as buyer, would wrongly create prevented trades for the Board, unsatisfied sellers and a lost exchange. I used no held fact for K2, only funded(k2, taxpayers). K2's central effect, that commodity plants break even at the $21 floor, is therefore not expressed: e1 still shows the plants as burdened by the line (price_paid up, a quantity cut, a substitution to out-of-state milk), which K2 may largely cancel. I think this over-states the commodity plants' burden. The substitution is also discouraged by the K2 eligibility test (Velmora milk paid the floor), which the format cannot express.
2. **Board stocks and K3 disposal** (accumulation, resale above 110%, donation, export). There is no stock variable that a rule creates, so a9 and a12 have nothing to attach to. The same holds for the surplus: with the Board buying everything offered, no seller is left unsatisfied, so I wrote no unsatisfied_seller and no criteria for e1/e2.
3. **Cheese and powder markets** (plants' output, a3). Linking the milk price to product prices needs a source effect on a price that plants pay or receive for product; the record has no product exchange to hang it on.
4. **Cost pass-through by specialty plants.** An output link from price_paid would predict a higher product price. a4 says the plants compete with unexposed cheesemakers, so the pass-through is limited; the format has output = pass-through only, so I left it out and recorded the unpassed cost as a yield fall and a transfer.
5. **The geographic boundary as such** (the floor applies to Velmora-origin milk, not to a place). It is held only through the out-of-state alternative; there is no "exemption" fact.
6. **Time structure** (floor not indexed, 4-year review, forward prices $17-19, short-run versus medium-run supply). Not representable.
7. **Compliance for k1 and the enforcer for k1/k2.** I attached compliance and enforcement to k4 only, to avoid duplicate effects from the same cost.

## Revision r2 (branch core-pilot-we008-r2, from 9c112b8)

Changed only situation.json. New facts:

| Fact | Rests on |
|---|---|
| e3: plants.commodity sell cheddar and powder to the Board (officials.enforcement); price vars net_price_received / price_paid | Sec. 1 K2: the Board buys product from licensed Velmora plants at $2.05 / $1.40 |
| held k2 above on e3 | K2 support prices set so a plant paying $21 breaks even, so above the market product price when milk is below $21 (a1) |
| backstop k2 / e3, buyer the Board, outlay subsidy_outlay | K2: "buys any quantity offered" |
| link plants.commodity quantity_supplied input farmers.velmora quantity_traded | K2: product must be made from Velmora milk paid at least the floor (no premise) |
| link plants.commodity net_price_received yield plants.commodity investment_target (replaces the old link from the farmers' price) | a13 (support prices cover full cost incl. return on new capacity), a2 |
| link Board inventory_held substitute buyers.food_programs quantity_traded | K3 donation to school meals and food banks; a9 (donations replace purchases), a12 (stocks are disposed of through K3 routes) |
| announced k2; timing k2 plants.commodity inventory_held carry_over | Sec. 1: proposed in February Year 0, enacted June, effective 1 January Year 1; a2; a12 (cheddar and powder keep, so stocks can be carried into the period) |

New engine output: the Board's purchases (quantity_demanded), inventory_held, subsidy_outlay and price_paid rise; plants.commodity net_price_received, quantity_supplied, investment_target and inventory_held (carry-over) rise; farmers.velmora milk quantity_traded rises; buyers.food_programs quantity_traded falls. No surplus or prevented trade appears on e3.

Still not held:
- K2 still does not cancel the burden I put on plants.commodity in e1 (price_paid up, quantity cut, out-of-state substitution, quantity_traded down). K2 says those plants break even at $21; the format has no way to net a backstop against the held price on another exchange. The K2 eligibility test also cannot be written.
- K3 resale above 110% and export: no fact for them. a3 (out-of-state supply and the withdrawn product): the Board's purchase has no link relation to a rise in the market product price.
- The timing fact is thin: the text gives the dates and a12 gives storability, but nothing says who holds stocks beyond what the engine draws. Specialty plants and farmers got no timing fact; milk is not storable.
