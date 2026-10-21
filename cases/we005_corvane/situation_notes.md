# WE-005 situation record: notes (written blind)

Source: section 1 of WE-005 (policy text, K1 to K3, unclear provisions) and assumptions a1 to a16 (= A-1 to A-16; statement, type, p copied).

## Facts and what they rest on
- Exchange e1 (drivers.current buy from stations.retail; drivers.unserved are the unsatisfied buyers; price vars price_paid / net_price_received): K1 "gasoline sold at retail", "retail stations".
- Exchange e2 (stations.retail buy from refiners.corvane): "Wholesale (rack) prices are not capped." No held fact on e2; it only names the parties.
- held k1 e1 below (a1, a2): K1 cap $4.20 with "Days 5 to 95"; binds if a1, is enforced if a2.
- criteria wait_time, search_cost for drivers.unserved; criterion facts wait_time and search_cost (a3: drivers queue and search).
- adjust, seller side, on drivers.current: quality_per_unit (hours, service, payment terms) and transaction_size (per-car limits) (a4; "Unclear provisions" reads these as allowed).
- outside: drivers.current informal_activity (a5, resale in cans).
- alt k1 stations.retail reclassification (a15, exemption reshaping; p 0.15).
- alt k1 drivers.unserved quantity_substitute (a10, transit, car-sharing, dropped trips).
- alt k1 drivers.unserved and drivers.current cross_border_purchases (a11; eastern cities 20 to 45 minutes from the Brennick line; the favored buyers use it less, the unserved more).
- stake k1 stations.retail (a16, retailers' association).
- link stations.retail quantity_traded -> input -> refiners.corvane quantity_traded (a7).
- link refiners.corvane quantity_traded -> substitute -> buyers.brennick quantity_traded (a6, pipeline to Brennick, other buyers).
- link drivers.unserved quantity_traded -> substitute -> stations.brennick quantity_traded (a11).
- link drivers.unserved quantity_traded -> substitute -> transit_operators quantity_traded (a10).
- link stations.retail quantity_traded -> complement -> stations.retail quantity_complement (a12, in-store goods on fuel trips).
- yield e1 seller stations.retail (a1); asset e1 seller stations.retail (a13, order expected to end on Day 95, so the loss is capitalized for the limited period).
- transfer e1 (a1): the held price moves means from stations to drivers who still buy.
- compliance k1 stations.retail ("Retail stations" are bound); enforcer k1 officials.enforcement (K3, Attorney General); funded k1 taxpayers (K3 "emergency appropriation from the general fund"; stated in the text, so no premise).

## Left out, and why
- a8 (shifting purchases by two days around the effective date), a9 (speeding repair), a14 (expected extension beyond Day 95): no fact in the format can carry them without a dated window (a8, a14) or an actor whose option the cap changes (a9). a14 would only qualify a13.
- The allocation_by_non_price_criteria criterion: no assumption supports it.
- fixed_budget: none; the appropriation is new.
- Quantity-supplied cut by stations, rack price, diesel and pre-Day-0 fleet contracts exemptions: no assumption.

## What the format could not hold
- K2 (no surcharges or tied purchases) closes the side_payments margin and K1 and K2 both burden stations; the format has no way to record a closed margin, or a restriction on terms as a second held component. Compliance and enforcement are recorded once, on k1.
- Dated operations (CR-1 0.7): announcement on Day 3, effect on Day 5, expiry on Day 95; windows, rush before Day 5, stocks held for the last days (a8, a13, a14).
- Two-sided cross-border price gap: Brennick at $4.00 against the cap at $4.20 (the cap can be above the neighboring price); cross_border_purchases uses the premise only.
- Commodity-specific caps by grade (regular, midgrade, premium) are one held component here.
- A repairer's (refinery owner's) option to speed repair is not an option the cap changes through any party of e1.
- Tier of the information in section 1 that is not an assumption (the 10% pipeline capacity, 40% refinery share) has no place.

## Revision r2 (format at 9c112b8)
Added from section 1 (announcement on Day 3, effective Day 5) and a8 (drivers and stations know the effective date and can shift purchases by two days):
- announced k1 (a8).
- timing k1 drivers.current quantity_demanded bring_forward (a8): the favored buyers hold purchases back until the cap binds; the engine signs it decrease in the announcement window.
- timing k1 stations.retail inventory_held carry_over (a8): the burdened stations carry less stock into the cap period; decrease in the announcement window.
- early_price e1 (a8): stations can set the price before the line binds; price_paid for drivers.current and net_price_received for stations.retail increase in the announcement window.

Not added:
- Expiry on Day 95: the format has no expiry or end window (the cap lifting, stock held into the post-expiry days, the rush to buy before the end). a13 (suppliers expect the end on Day 95 and can hold product for a few days) and a14 (extension expected, p 0.35) therefore still rest unused except a13 on the asset fact. A supplier holding product past Day 95 is also not a party of e1 (timing needs a chooser who is a party).
- Suppliers' (refiners') timing under a13 and a8: refiners are not a party of a held exchange.
- Backstops: section 1 has no buyer or seller of last resort.
- Stations bringing sales forward before Day 5: not supported by a8's wording ("shift purchases").

## Revision r3 (format at 73b9bc2)
No change to situation.json. Reasons:
- parts: the only candidate whole is "drivers" (drivers.current and drivers.unserved). Neither section 1 nor any assumption names a total for drivers, stations or any other class; a3, a10 and a11 speak of drivers, unserved drivers and eastern drivers, but name no variable whose total is at issue. Adding a whole would only match an imagined answer, so none is added.
- dominance: no assumption states that one direction dominates a chain that clashes with another. a8 (shifting purchases by two days) and a13/a14 (end of the order expected or not) give expectations, not dominance; section 1 gives no figures that settle a sign by arithmetic. None added.
- Effect of the new engine: the first_months window is now combined automatically (early_price from r2 against the cap): drivers.current price_paid and stations.retail net_price_received come out ambiguous (reported) in first_months, with no dominance premise to settle them.
