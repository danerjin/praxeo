# WE-010 Marren: notes on the situation record (written blind)

Sources: section 1 of the example (S1) and the assumptions a1 to a17 (A-1 to A-17: statement, type, p). All assumptions are copied; a13, a15 and a16 are not used by any fact (see the end).

## Facts and what they rest on

- Exchange e_ret (smokers.marren buy from retailers.marren): S1 "Cigarettes sold in Marren" and the shelf price ($7.50). Price vars price_paid and net_price_received.
- Charge k1 on e_ret, paid by the buyer side, received by officials.enforcement (Revenue Department): S1 K1, with moves(buyer) on a1 (increase passed on in shelf prices). Receipt tax_revenue, projection tax_revenue_vs_static_projection.
- Exchanges e_wh (wholesalers.stamping to retailers.marren), e_border (sellers.neighboring), e_smuggle (intermediaries.smuggling), e_other (sellers.substitutes: roll-your-own, cigars, e-cigarettes): S1 (stamping agents, Dunmarch and Kessick, K3 unstamped cigarettes, exemptions). They carry no held or charge fact, so they only name the parties.
- Alternatives under k1, chooser smokers.marren:
  - cross_border_purchases (a3, a11), S1 border geography and K3 allowance;
  - informal_activity by smokers (a4) and by intermediaries.smuggling (a4);
  - quantity_substitute (a6);
  - reclassification by producers (a7), S1 exemptions;
  - inventory_held (a9, stocking before 1 January).
- Stakes on k1: retailers.border, health_groups, producers (a8).
- Links:
  - own_price on quantity_demanded (a2);
  - substitute links to sellers.substitutes, price and quantity (a6);
  - same_act to sellers.neighboring (a3);
  - complement to sellers.complements (a10, fuel and snacks bought on the trip);
  - complement from smokers.marren quantity_traded to retailers.marren quantity_complement (a10);
  - smokers' informal_activity same_act with the smugglers' (a4);
  - smugglers' informal_activity yield to investment_target (a5);
  - smugglers' informal_activity same_act to side_payments of officials.enforcement (a12);
  - retailers.marren quantity_traded yield to number_of_sellers (a14), and substitute to sellers.neighboring number_of_sellers (a14);
  - sellers.neighboring quantity_traded yield to asset_value of factor_owners.border_sites (a17, a3).
- Compliance: wholesalers.stamping under k1 and k2 (buy and affix stamps; K2 report and pay), retailers.marren under k2 (S1 K2). Enforcer: k4 by officials.enforcement (S1 K4).
- Means out under k2 for wholesalers.stamping and retailers.marren (S1 K2: a tax on stock held, which no choice avoids after the date is known).

## What the format could not hold, or I left out

- The legal bound versus the economic incidence: the tax is bound on wholesalers (S1) but the record puts the charge on the retail exchange, paid by the buyer side, because the pass-on (a1) is stated at shelf prices. A charge on e_wh would put the payer on the seller side and give a different price effect.
- K3 (allowance and possession rules, penalties): no instrument fits (not a price line, not a payment). I did not set compliance for smokers, because a4 says the use tax is rarely collected. The misdemeanor and felony penalties (expected penalty against gain) have no fact: `outside` needs a held price line.
- K5 (earmark of $0.30 per pack to the Tobacco Unit and the quit program) and a15: no fact for an earmark, a funded share or a no-maintenance-of-effort clause. `funded` names who pays an enforcer, not a share of receipts; `fixed_budget` does not fit.
- a16 (sales fall by less than half): the engine signs tax_revenue as increasing from the charge alone and does not take this premise, so the revenue claim has no premise attached. a13 (neighbors limit sales to residents) has no fact either; it would cancel the alternative on a3, but the format has no way to defeat a fact.
- Timing: the dates (announcement, signing, effect) and the floor-stock moment; a9 is held only as an alternative on inventory_held, with no window.
- Subgroups (border versus interior smokers, cartons versus packs): one class smokers.marren; no group-level split.
- The 45% share, the dollar figures and the three bridges are not stated; the format takes no magnitudes.
- Effects on the base of other taxes (sales tax on the fuel and snacks bought elsewhere): no variable or fact for it beyond the quantity links.
- The relation "number_of_sellers" links use `yield` and `substitute` as the nearest relations; neither means "exit across a line" exactly.
- The receiver of K1 is entered as officials.enforcement, the nearest ontology class to the Revenue Department; the state's general fund is not a class.
