# WE-018 Ban on single-use plastic shopping bags, with a fee for paper bags

Analyst: draft (Handbook 0.5)  |  Rule catalog version: 0.5  |  Status: awaiting expert review

A stylized policy in a fictional city. It resembles real local bag ordinances but is not modeled on any one of them, and it is kept apart from the historical cases reserved for evaluation. Environmental effects (litter, waste, emissions, use of materials) are the stated purpose of such policies but are out of scope for version 1, which has no variables for them; this analysis covers only the variables in the controlled list. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Brennick Carryout Bag Ordinance.** Brennick is a city of about 400,000 people. Retailers there have given away thin plastic carryout bags at the checkout, at a cost to them of about 2 cents a bag, built into their prices. About 120 million such bags are handed out a year. Surveys suggest that about 60% of households reuse some of them as bin liners or for pet waste. The neighboring town of Fallow Creek has no bag rules; two large supermarkets there are within 1 km of the city line on Route 9, close to several Brennick neighborhoods. Brennick's other edges are mostly residential or rural. The ordinance was passed nine months before it took effect.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Bag ban | `prohibition` | Single-use plastic carryout bags (plastic bags with handles, thinner than 4 mil (0.1 mm)) provided at the point of sale | All retailers in Brennick | From the effective date. | Bags without handles for produce, meat and bulk goods inside the store; pharmacy prescription bags; restaurant takeout bags |
| K2 Paper bag charge | `price_floor` | Recycled-paper carryout bags | All retailers | May be provided only for a charge of at least 10 cents a bag, kept by the retailer and shown on the receipt. Reusable bags (designed for at least 125 uses; at least 4 mil if plastic) may be sold at any price. | Customers paying with food-assistance benefits receive paper bags free |
| K3 Enforcement | Enforcement | K1, K2 | City Office of Sustainability | Complaint-driven. Written warning, then fines of $100, $250 and $500 per day of violation. Funded from the general budget. | None |

Unclear provisions: how a bag's design for 125 uses is verified. The ordinance sets no test, so a maker's claim is assumed to be accepted.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Triangular: forbids an exchange (a bag given with a purchase) between retailers and shoppers | Yes: almost every retailer gave thin bags (A-1) | EN-7 (legal trade falls to near zero; little reason for an informal market), RS |
| K2 | Triangular: fixes the minimum charge for a good retailers would otherwise give away | Yes: without it, stores would give paper bags free to compete | RS-1, RS-5, TS-3 |
| K3 | Binary: funded by taxpayers | Yes | OC-3 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `shoppers` (`buyers.current`) | People buying goods at Brennick retailers | No free thin bags; pay for paper, bring or buy reusable bags. |
| `shoppers.edge` | Shoppers living near Route 9, close to stores on both sides of the line | Can shop in Fallow Creek, where thin bags are still free. |
| `shoppers.assistance` | Shoppers paying with food-assistance benefits | Receive paper bags free. |
| `households.bag_reusers` | Households that reused carryout bags as bin liners or for pet waste | Lose a free supply of liners. |
| `retailers.brennick` (`sellers.current`) | All Brennick retailers | Change bag stock, train staff, collect fees, enforce the rule at the till. |
| `retailers.small` | Small convenience stores and corner shops | Same, with fewer staff and less scrutiny. |
| `retailers.edge` | Brennick stores near Route 9 | Lose some customers across the line. |
| `retailers.fallow_creek` (`neighboring_jurisdictions`) | Supermarkets in Fallow Creek near the line | Gain some Brennick customers. |
| `bag_makers.thin` (`input_suppliers`) | Makers and distributors of thin carryout bags | Lose Brennick sales. |
| `sellers.substitutes` | Makers and sellers of paper bags, reusable bags and bin liners | More demand. |
| `officials.enforcement`, `taxpayers` | Office of Sustainability and its funders | New enforcement task. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `shoppers`, `retailers.brennick`, `bag_makers.thin` | `quantity_traded` (thin plastic carryout bags in Brennick) | decrease (to near zero) | short | K1, EN-7 | A-1 |
| C-2 | `shoppers` | `price_paid` (carryout bags at the checkout) | increase | short | K2 | A-1 |

The visible effects: thin bags disappear from Brennick checkouts, and a bag now costs the shopper at least 10 cents instead of nothing at the till. EN-7's other conclusions (an informal market, a risk premium) do not follow here: a thin bag is cheap to replace legally, so no buyer values it highly enough to seek it out illegally.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `shoppers` | `quantity_substitute` (reusable bags and paid paper bags) | increase | short to medium | RS-1, TS-8 | A-2, A-14 |
| C-4 | `households.bag_reusers` | `quantity_substitute` (bought bin liners and pet-waste bags) | increase | short to medium | RS-1 | A-3 |
| C-5 | `retailers.brennick` | `compliance_cost` (new stock, till changes, signs, staff training, fee handling) | increase | short | CR-8c, OC-1 | none |
| C-6 | `retailers.brennick` | `net_price_received` (carryout bags) | increase | short | K2 | A-1 |
| C-7 | `retailers.brennick` | `reclassification` (thick plastic "reusable" bags sold cheaply at the till, in effect as single-use bags) | increase | short to medium | RS-5 | A-4 |
| C-8 | `retailers.small` | `informal_activity` (still handing out thin bags, or waiving the paper fee) | increase | short | RS-3 | A-5 |
| C-9 | `shoppers.edge` | `cross_border_purchases` | increase | short | RS-4 | A-6 |
| C-10 | `shoppers` | `quantity_demanded` (free thin bags taken in the announcement window) | increase | short | RS-8 | A-7 |
| C-11 | `bag_makers.thin`, `sellers.substitutes`, `retailers.brennick` | `lobbying_effort` (thin-bag makers for repeal or a looser definition; makers of thick bags to keep the 4 mil line; retailers over the fee) | increase | medium | RS-7 | A-8 |

C-4: households that lined bins with carryout bags were using a by-product that came free with their shopping. The relation is recorded as `substitute`, partial, with the note `secondary_use` (`02_ontology.md`, 2.8): carryout bags and bought liners serve the same end. The ban removes the free supply, so they buy liners (RS-1).

C-6: the store keeps the 10-cent fee. A paper bag costs a store a few cents more than a thin bag did, but the store now receives at least 10 cents for each one it hands out, where it received nothing for a thin bag.

C-3: the mix changes as routines form (TS-8). In the first weeks shoppers forget their bags and pay for paper; over the following months they learn to carry reusable bags, so paper use falls and reusable bags take a larger share (section 8).

C-9: the fee is small (perhaps 30 to 60 cents on a weekly shop). Only shoppers who were already close to indifferent between stores on either side of the line, at the margin in the sense of LW-2, change where they shop. Most shoppers do not.

Not reported:
- Longer waits at the checkout (OC-2) while shoppers pack their own bags and fees are rung up: A-11 is below the cut-off (p = 0.45).
- RS-10 (informal trade) was checked. The evasion in C-8 is open bag-giving at ordinary stores, not hidden trade between strangers, so RS-10's mechanisms (search costs, hidden quality, disputes outside the courts) do not arise in any meaningful way.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `retailers.fallow_creek` | `quantity_traded` (all goods) | increase | short | RS-4, RS-9 | Brennick and Fallow Creek stores near Route 9: `across_border`, close; carryout bags and the rest of the basket: `complement`, note `trip` | A-6, A-9 |
| C-13 | `retailers.edge` | `quantity_traded` (all goods) | decrease | short | RS-4, RS-9 | as C-12 | A-6, A-9 |
| C-14 | `retailers.edge` (staff) | `employment`, `hours_worked` | at_least_one_decrease | medium | RS-4, RS-9, OC-5 | as C-12 | A-6, A-9, A-15 |
| C-20 | `retailers.fallow_creek` (staff) | `employment`, `hours_worked` | at_least_one_increase | medium | RS-4, RS-9, OC-5 | as C-12 | A-6, A-9, A-15 |
| C-21 | `sellers.substitutes` (paper bag makers) | `quantity_traded` (paper bags sold to Brennick retailers) | increase | short | CR-9 | paper bags `input_to` the checkout; paper and thin plastic bags: `substitute`, close | A-1, A-2 |
| C-15 | `retailers.brennick` | `resources_available_other_uses` | ambiguous | short | CR-8b, CR-8c, CR-12b (section 7) | | A-2, A-12 |
| C-16 | `shoppers` | `price_paid` (groceries and other goods) | ambiguous | medium | RS-14, see section 7 | carryout bags `input_to` retail service | A-12, A-13 |

C-12 to C-14, C-20: the bag goes with the whole basket. A shopper who crosses the line to avoid the fee moves the entire week's shopping, not just the bags (RS-9). Stores that lose the sales need less labor, and stores that gain them need more (OC-5). OC-5 says only that employment or hours move, since stores can adjust either, so each side is recorded as a group (`02_ontology.md`, 2.5). C-14 and C-20 are at depth 4 (ban, cross-border shopping, moved basket, store staffing), where the chains stop.

C-21: in the counterfactual, stores hand out thin plastic bags (section 1), so any paper bags taken at 10 cents are added sales for paper-bag makers (CR-9, `input_to`).

C-15: stores no longer buy thin bags for every shopper. Many shoppers now bring their own bags, and those who take paper pay a fee that covers its cost (A-12), so store spending on bags per transaction falls (+). But the compliance work in C-5 is paid from the same resources (CR-8c), and edge stores lose sales (C-13) (−). The chains oppose on one variable, so the sign is ambiguous (section 7).

The relation between carryout bags and bin liners is recorded as `substitute`, partial, note `secondary_use` (see C-4).

Not reported: higher prices for bin liners or reusable bags. Brennick is too small a part of these markets to move their prices; the opposite assumption, A-10, has p = 0.1.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `shoppers`, `price_paid` (groceries and other goods), medium | Compliance costs (C-5) are a cost of every Brennick store, so they pass through to prices (RS-14); near the line, lost sales spread fixed costs over fewer customers (C-13). | Stores spend less on bags per transaction (C-15); in a competitive retail market, a lower input cost passes through to lower prices in the same way (RS-14 in reverse; A-13). | None | **ambiguous** (C-16). Decided by whether stores' saving on bags exceeds their compliance costs, which depends on how many shoppers bring their own bags. |
| `shoppers`, `households.bag_reusers`, `resources_available_other_uses`, short | None in the short run. | Paper-bag fees (C-2), reusable bags (C-3), bought liners (C-4): money spent on items that came free with shopping before. | None needed | **decrease** (C-17, C-18). Shelf prices do not move in the short run, so nothing offsets this. Over the medium run, lower grocery prices could offset part of it if stores' saving on bags is passed on (C-16, ambiguous), so the sign is not carried beyond the short run. |
| `retailers.brennick`, `resources_available_other_uses`, short | Fee income on paper bags (C-6) and less spent on bags per transaction (A-12). | Compliance spending (C-5), which comes from the same resources (CR-8c); lost sales at edge stores (C-13). | None | **ambiguous** (C-15). The per-bag price (C-6) and compliance cost (C-5) are also reported on their own, as separate variables. |

## 8. Time structure

- **Announcement window (nine months).** Shoppers take extra free thin bags while they still can (C-10), and stores run down their stocks of thin bags. Households that reuse bags as liners live off this stock at first, so bought liners (C-4) rise only after a few months, as the stock runs out.
- **The first months.** Shoppers forget their bags most often at first, so total paper-bag fee payments are highest early. Reusable bag purchases surge, then fall to a lower rate at which bags are replaced, since a reusable bag lasts many trips.
- **Habits form over months (TS-8).** Carrying bags is a routine repeated on every trip (A-14). As shoppers learn to carry bags, paper-bag use and fee payments fall from their early peak, without any change in prices; reusable bags take a growing share of C-3. The full response therefore has a short-to-medium horizon. The path changes sizes, not signs: compared with the counterfactual, paper and reusable bag use (C-3) stays an increase and shoppers' resources for other uses (C-17) stay a decrease, only by less than at first. The per-bag charge (C-2, C-6) is not affected.
- **Edge shoppers.** Shoppers who switch stores across the line (C-9) are likely to stay switched once they have learned the other store, so C-13 and C-14 do not fade with habit as fee payments do.
- **The fee erodes in real terms.** The minimum charge is fixed at 10 cents. As other prices rise, its real value falls, and, unless stores charge more, paper-bag use creeps up over the long run (TS-3).
- **Reclassification grows.** Bag makers design cheap bags that just meet the 4 mil and 125-use definition (C-7); this takes months. If they come to be used once and thrown away, pressure to tighten the definition is what TS-4 predicts; TS-4 is Tier C in the catalog, so this is a suggestion only. Makers who expect such tightening invest less in thick bags (TS-2).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-17 | `shoppers` | `resources_available_other_uses` | decrease | The goods shoppers would have bought with what they now spend on paper-bag fees and reusable bags. | OC-1, RS-1 |
| C-18 | `households.bag_reusers` | `resources_available_other_uses` | decrease | The goods these households would have bought with what they now spend on liners. | RS-1, LW-1 |
| C-22 | `officials.enforcement` | `enforcement_cost` | increase | Inspections, warnings and fines. | OC-3 |
| C-19 | `taxpayers` | `resources_available_other_uses` | decrease | What the Office's enforcement budget would otherwise have funded. | OC-3, OC-1 |

C-22, C-19: OC-3's funding case. Enforcement is funded from the general budget (K3), taken here as a budget that rises with the new task, so the cost falls on taxpayers.

The free thin bags no longer handed out are the prevented exchanges, recorded as C-1. Shoppers who drive across the line are those for whom the other store was about as convenient, so no separate travel cost is recorded.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most retailers comply, chains in particular. | enforcement | 0.85 | Store audits in the first months; complaint volumes; size of fines. | C-1, C-2, C-6 weaken; C-8 grows. |
| A-2 | Shoppers accept reusable and paper bags as substitutes. | substitutability | 0.95 | Experience of comparable towns; availability of bags. | C-3, C-15, C-21 weaken. |
| A-3 | Many households reused carryout bags as liners and will buy liners instead. | substitutability | 0.8 | Household surveys (about 60% reuse); liner sales in comparable towns after similar rules. | C-4, C-18 not reported. |
| A-4 | Thick plastic "reusable" bags can be sold cheaply at the till, and shoppers buy them. | other | 0.6 | Price of 4 mil bags; the 125-use claim is not tested. | C-7 not reported. |
| A-5 | Some small stores keep handing out thin bags, or waive the fee, without being caught. | enforcement | 0.6 | Complaint-driven enforcement; warnings before fines. | C-8 not reported. |
| A-6 | Some shoppers near Route 9 are close to indifferent between stores on either side of the line. | mobility | 0.55 | Store locations; loyalty-card data; surveys of shopping trips. | C-9, C-12 to C-14, C-20 not reported. |
| A-7 | Shoppers take extra free bags in the announcement window. | expectations | 0.7 | Bag orders by stores in the window in comparable towns. | C-10 not reported. |
| A-8 | Bag makers and retailers can organize at a cost below their stake. | other | 0.7 | Existing industry and retail associations. | C-11 weakens. |
| A-9 | A shopper who changes store moves the whole basket, since the fee applies per trip. | other | 0.9 | Basket data; the fee's structure. | C-12 to C-14 weaken. |
| A-10 | Brennick's demand is large enough to move the price of liners or reusable bags. | other | 0.1 | City population against the regional market. | Below cut-off; not reported. |
| A-11 | Checkout times rise meaningfully. | other | 0.45 | Till timing studies in comparable towns. | Below cut-off; not reported. |
| A-12 | Stores' spending on bags per transaction falls, because many shoppers bring bags and the fee covers paper. | other | 0.7 | Store bag purchasing records; paper-bag cost against the 10-cent fee. | C-15's (+) chain weakens; C-16 leans toward increase. |
| A-13 | Retail competition is strong enough that cost changes reach shelf prices over time. | other | 0.7 | Number of grocery chains; margins. | C-16's − chain weakens. |
| A-14 | Shopping trips are frequent and routine, so carrying bags can become a habit (the assumption of TS-8). | other | 0.9 | Trip frequency from household surveys (most households shop at least weekly). | C-3's path is flatter; paper-bag use does not fall over time. |
| A-15 | Stores near the line adjust staff hours and hiring to their sales (the assumption of OC-5). | alternative_uses | 0.8 | Share of part-time and hourly staff in grocery retail; scheduling practice. | C-14, C-20 not reported. |

## 11. Report

**The policy.** Brennick retailers may no longer give out thin plastic carryout bags. They may hand out paper bags only for at least 10 cents each, which they keep, and may sell reusable bags at any price. Shoppers on food assistance get paper bags free. The neighboring town has no such rule.

**Visible consequences.** Thin plastic bags disappear from Brennick checkouts (C-1), bags now cost shoppers money at the till (C-2), and shoppers switch to reusable and paper bags (C-3).

**Invisible consequences.**
- *Shoppers* give up the other goods that the money spent on fees and reusable bags would have bought (C-17). They pay for paper most often in the first weeks; as carrying bags becomes a habit, paper use and fee payments fall (C-3, section 8). Before the ban they took extra free bags (C-10).
- *Households that reused bags as bin liners* now buy liners (C-4, C-18).
- *Retailers* bear compliance costs (C-5), keep the paper-bag fee (C-6), and spend less on bags; whether they are left with more or less for other uses is ambiguous (C-15). Paper-bag makers sell more to Brennick stores (C-21). Some sell cheap thick "reusable" bags that are used like the old ones (C-7); some small stores carry on giving thin bags (C-8).
- *Near the city line*, some shoppers move their whole weekly shop to Fallow Creek (C-9, C-12), so Brennick stores there sell less and over time cut staff or hours, and the Fallow Creek stores the reverse (C-13, C-14, C-20).
- Interest groups lobby over the rules (C-11). The Office spends on enforcement (C-22), funded by *taxpayers* (C-19).

**Ambiguous effects.** Whether grocery prices end up higher or lower (C-16), and whether retailers end up with more or less to use elsewhere (C-15): stores save on bags but bear compliance costs.

**Key conditions.** That shoppers accept other bags (A-2, p = 0.95) and retailers comply (A-1, p = 0.85). The edge effects (C-9, C-12 to C-14, C-20) rest on A-6 (p = 0.55), the weakest reported assumption; with it false, they disappear.

**What this analysis cannot say.** Environmental effects, the policy's purpose, are out of scope for version 1, as are any health effects; how large any effect is; whether the costs to shoppers and households are worth any environmental effects; whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | shoppers, retailers.brennick, bag_makers.thin | quantity_traded (thin carryout bags) | decrease | short | visible | B | K1, EN-7 | A-1 |
| C-2 | shoppers | price_paid (carryout bags) | increase | short | visible | B | K2 | A-1 |
| C-3 | shoppers | quantity_substitute (reusable and paper bags) | increase | short–medium | visible | B | RS-1, TS-8 | A-2, A-14 |
| C-4 | households.bag_reusers | quantity_substitute (bought liners) | increase | short–medium | invisible | B | RS-1 | A-3 |
| C-5 | retailers.brennick | compliance_cost | increase | short | invisible | A | CR-8c, OC-1 | none |
| C-6 | retailers.brennick | net_price_received (carryout bags) | increase | short | invisible | B | K2 | A-1 |
| C-7 | retailers.brennick | reclassification | increase | short–medium | invisible | B | RS-5 | A-4 |
| C-8 | retailers.small | informal_activity | increase | short | invisible | B | RS-3 | A-5 |
| C-9 | shoppers.edge | cross_border_purchases | increase | short | invisible | B | RS-4 | A-6 |
| C-10 | shoppers | quantity_demanded (free bags, announcement window) | increase | short | invisible | B | RS-8 | A-7 |
| C-11 | bag_makers.thin, sellers.substitutes, retailers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-8 |
| C-12 | retailers.fallow_creek | quantity_traded (all goods) | increase | short | invisible | B | RS-4, RS-9 | A-6, A-9 |
| C-13 | retailers.edge | quantity_traded (all goods) | decrease | short | invisible | B | RS-4, RS-9 | A-6, A-9 |
| C-14 | retailers.edge (staff) | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-4, RS-9, OC-5 | A-6, A-9, A-15 |
| C-15 | retailers.brennick | resources_available_other_uses | ambiguous | short | invisible | B | (+) bag savings and fees, CR-8b; (−) compliance spending and lost edge sales, CR-8c; CR-12b | A-2, A-12 |
| C-16 | shoppers | price_paid (groceries and other goods) | ambiguous | medium | invisible | B | RS-14 (C-5) vs RS-14 in reverse (C-15) | A-12, A-13 |
| C-17 | shoppers | resources_available_other_uses | decrease | short | invisible | B | OC-1, RS-1 | A-2 |
| C-18 | households.bag_reusers | resources_available_other_uses | decrease | short–medium | invisible | B | RS-1, LW-1 | A-3 |
| C-19 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| C-20 | retailers.fallow_creek (staff) | employment, hours_worked | at_least_one_increase | medium | invisible | B | RS-4, RS-9, OC-5 | A-6, A-9, A-15 |
| C-21 | sellers.substitutes (paper bag makers) | quantity_traded (paper bags to Brennick) | increase | short | invisible | B | CR-9 (input_to), after C-3 | A-1, A-2 |
| C-22 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |

## Gaps found

- GAP-018-1 (closed in catalog 0.3: relation note `secondary_use` in 2.8). The bin-liner relation behind C-4 and C-18 is now recorded as `substitute`, partial, note `secondary_use`.
- GAP-018-2 (closed in catalog 0.3: TS-8). The habit path is now derived: C-3 carries TS-8 with a short-to-medium horizon, resting on A-14. It changes sizes along the path, not signs, so no new consequence is added.

Also applied on the update to catalog 0.3: RS-14 for the pass-through of compliance costs and bag savings to shelf prices (C-16), and OC-5 for staffing at stores that lose sales (C-14, A-15). Review corrections: the shoppers' outlay row in section 7 used a prose variable with an increase sign; it is now `resources_available_other_uses`, decrease, limited to the short run because lower shelf prices (C-16) may offset it later. C-3 is listed as visible, so the report now gives it among the visible consequences.
- Catalog 0.5: corrected after the core-only comparison (see ../05_examples_core/WE-018_plastic_bag_ban_core.md): edge-store staffing (C-14) made the group employment or hours, `at_least_one_decrease`, with its Fallow Creek mirror added (C-20); retailers' resources (C-15) made ambiguous, since compliance spending draws on the same resources; added paper-bag makers' sales (C-21) and the Office's enforcement cost with OC-3's funding case (C-22); C-5 cites CR-8c.
