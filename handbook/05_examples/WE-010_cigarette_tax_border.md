# WE-010 Cigarette tax increase in a state with low-tax neighbors

Analyst: draft (Handbook 0.3)  |  Rule catalog version: 0.3  |  Status: awaiting expert review

A stylized policy in a fictional state. It resembles many real state cigarette tax increases but is not one of them. Its main lessons are the border (RS-4), the move from casual bootlegging to organized smuggling (RS-3, RS-10), incidence by subgroup (DM-1), and why revenue falls short of the static projection (TX-9) while the sign of revenue itself stays open, and how the base of other taxes moves with it (TX-10). The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Marren Tobacco Tax Act of the current session.** Marren is a state of about 6 million people. Its capital, Port Alder, lies on the river that forms the border with Dunmarch; three bridges cross it. About 45% of Marren's population lives within a 20-minute drive of Dunmarch or of Kessick, its southern neighbor. Per-pack cigarette taxes are $1.50 in Marren, $0.40 in Dunmarch and $0.80 in Kessick; Dunmarch has not changed its rate in 15 years. Before the act, a typical pack cost about $7.50 in Marren and $5.80 in Dunmarch. The bill was introduced in June, passage was expected from early August, it was signed on 1 October, and it took effect on 1 January.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Tax increase | `per_unit_tax` | Cigarettes sold in Marren | Licensed stamping agents (wholesalers), who buy tax stamps and affix them before sale to retailers | From $1.50 to $3.50 per pack of 20, fixed in money terms (not indexed). | Other tobacco products (roll-your-own tobacco, cigars, "little cigars") stay at 25% of the wholesale price. E-cigarettes are untaxed. |
| K2 Floor-stock tax | `per_unit_tax` | Stamped packs held by wholesalers and retailers at 00:01 on 1 January | Wholesalers and retailers | $2.00 per stamped pack in inventory, reported and paid within 30 days. | Packs held by consumers. |
| K3 Personal allowance and possession rules | Enforcement | Cigarettes brought in from other states | Residents | One carton (10 packs) per person every 30 days may be brought in without Marren tax; anything more owes Marren use tax, self-reported. Possession of more than 5 cartons of unstamped cigarettes is a misdemeanor; more than 50 cartons is a felony with seizure of the vehicle. | None |
| K4 Enforcement | Enforcement | K1 to K3 | Revenue Department Tobacco Unit | Unit grows from 12 to 20 agents; road checks near bridges; retailer audits; counterfeit-stamp detection. | None |
| K5 Revenue use | Earmark | Revenue from the $2.00 increase | State | $0.30 per pack to the Tobacco Unit and to the existing quit-smoking program (already funded from general revenue); the rest to the general fund. | None |

Unclear provisions: whether the use tax on cartons above the allowance will be collected at all in practice. Assumed it will rarely be (A-4).

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: a forced payment to the state, on a selective good | Yes, from 1 January | TX (incl. TX-9, TX-10), RS |
| K2 | Binary | Yes, once | TX-5, RS-8 |
| K3 | Triangular in effect: restricts exchanges between Marren residents and out-of-state sellers above the allowance | Partly: depends on enforcement (A-4) | RS-3, RS-4, RS-10 |
| K4 | Binary: funded from the earmark | Yes | OC-3 |
| K5 | Binary: transfer to the quit program | Yes | SB-7 |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `smokers.border` | Marren smokers within a 20-minute drive of a lower-tax state | Can buy across the line; the gap is about $3.70 a pack, $37 a carton. |
| `smokers.interior` | Marren smokers far from a border, or without a car | Pay the tax, switch to untaxed products, cut back, or buy informally. |
| `smokers.light` / `smokers.heavy` | Buyers of single packs / buyers of cartons | The fixed cost of a trip is spread over more packs for heavy smokers. |
| `retailers.marren.border` | Convenience stores and gas stations near the bridges and the southern line | Face customers who can cross. |
| `retailers.marren.interior` | Retailers far from a border | Face less cross-border competition, more informal competition. |
| `stamping_agents` | Licensed wholesalers | Collect the tax; pay the floor-stock tax; lose volume. |
| `retailers.neighbors` | Stores in Dunmarch and Kessick near the line | More Marren customers. |
| `neighboring_jurisdictions` | Dunmarch and Kessick state budgets | More cigarette and sales tax revenue. |
| `intermediaries.bootleggers` | Individuals buying across the line for resale to friends and coworkers | A margin of up to $3.70 a pack. |
| `intermediaries.smuggling_networks` | Organized groups moving truckloads, often with counterfeit stamps | The same margin at scale, against felony penalties. |
| `producers` | Tobacco manufacturers | Can design products that fall under the lower "other tobacco" rate. |
| `sellers.substitutes` | Sellers of roll-your-own tobacco, cigars and e-cigarettes | More demand. |
| `quit_program.clients` | People using the state quit-smoking program | Earmarked funding. |
| `officials.enforcement`, `taxpayers` | Tobacco Unit, Revenue Department, and general-fund taxpayers | More enforcement work; more revenue at stake. |

## 4. Direct effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `smokers` (all Marren) | `price_paid` (stamped cigarettes, in Marren) | increase | short | TX-2, DM-1 | A-1 |
| C-2 | `retailers.marren` | `quantity_traded` (stamped cigarettes, in Marren) | decrease | short | TX-2 | A-1, A-2 |

C-1 and C-2 are the effects the act's supporters point to: cigarettes cost more in Marren and fewer are sold there. The revenue the act was expected to raise is discussed in section 7, because its sign is not settled by the method.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `smokers.border` | `cross_border_purchases` | increase | short | RS-4, TX-4 | A-3 |
| C-4 | `intermediaries.bootleggers` | `informal_activity` (casual resale, carrying above the allowance) | increase | short | RS-3, TX-4 | A-3, A-4 |
| C-5 | `intermediaries.smuggling_networks` | `informal_activity` (organized smuggling, counterfeit stamps) | increase | medium | RS-3, TS-2 | A-4, A-5 |
| C-6 | `smokers` | `quantity_substitute` (roll-your-own tobacco, cigars, e-cigarettes) | increase | short | RS-1, TX-3 | A-6 |
| C-7 | `producers` | `reclassification` (cigarette-like little cigars taxed as "other tobacco") | increase | medium | RS-5, TX-4 | A-7 |
| C-8 | `smokers` | `quantity_traded` (stamped packs bought October to December) | increase | short | RS-8 | A-9 |
| C-9 | `stamping_agents`, `retailers.marren` | `compliance_cost` (floor-stock count and return; new stamps) | increase | short | TX-5 | none |
| C-10 | `retailers.marren.border`, health groups, `producers` | `lobbying_effort` (border-zone relief, tighter limits on other states' sales, parity for little cigars) | increase | medium | RS-7 | A-8 |

C-4 and C-5 are different trades. Casual bootlegging starts at once and needs nothing but a car. Organized smuggling needs suppliers in Dunmarch, storage, transport, outlets in Marren and often counterfeit stamps; groups invest in these only if they expect the price gap to last (TS-2), and it builds over months. C-8: retailers' stock is caught by the floor-stock tax, but smokers' own stock is not, so smokers who can afford it buy cartons before 1 January.

Not reported: corruption of enforcement officers by smuggling networks (`side_payments`); A-12 is below the cut-off (p = 0.25). Not reported: Dunmarch or Kessick limiting sales to Marren residents; A-13 is below the cut-off (p = 0.2). Not reported: Marren retailers moving across the line (RS-4 for sellers); store licenses and leases make it slow, and the medium-horizon evidence is thin (A-14, p = 0.35).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-11 | `retailers.neighbors` | `quantity_traded` (cigarettes and goods bought on the same trip) | increase | short | RS-4, RS-9 | Marren and Dunmarch/Kessick stores: `across_border`, close for `smokers.border` | A-3, A-10 |
| C-12 | `retailers.marren.border` | `quantity_traded` (untaxed goods bought on the same trip: fuel, snacks, drinks, lottery tickets) | decrease | short | RS-4, RS-9 | cigarettes and other convenience goods: `complement`, note `trip` | A-3, A-10 |
| C-13 | `retailers.marren.border` | `employment` | decrease | medium | TX-3, RS-9 | | A-3, A-10 |
| C-14 | `retailers.marren.border` | `net_price_received` (cigarettes) | decrease | short | TX-2, DM-1 | | A-3 |
| C-15 | `smokers.interior` | `tax_share_borne` (relative to `smokers.border`) | increase | short | DM-1 | | A-3 |
| C-16 | `smokers.light` | `tax_share_borne` (relative to `smokers.heavy`) | increase | short | DM-1, RS-4 | | A-3, A-11 |
| C-17 | Buyers of informal cigarettes | `search_cost` | increase | short | RS-10 | | A-4 |
| C-18 | Buyers of informal cigarettes | `quality_variability` (counterfeit and stale product) | increase | short | RS-10 | | A-4 |
| C-28 | Buyers of informal cigarettes | `quality_information` (no brands they can trust, no recourse) | decrease | short | RS-10 | | A-4 |
| C-19 | `neighboring_jurisdictions` | `tax_revenue` (Dunmarch and Kessick cigarette and sales taxes) | increase | short | RS-4 | across_border | A-3 |
| C-20 | `officials.enforcement` | `tax_revenue` (Marren sales tax on goods moved across the line by bundled trips) | decrease | short | RS-4, RS-9, TX-10 | | A-3, A-10 |
| C-21 | `officials.enforcement` | `tax_revenue_vs_static_projection` (cigarette tax) | decrease | short | TX-9 | | A-1 to A-4 |
| C-22 | `quit_program.clients` | `quantity_traded` (quit-program services funded from general revenue) | decrease | medium | SB-7 | | A-15 |
| C-29 | `officials.enforcement` | `tax_revenue` (tax on other tobacco products) | increase | short to medium | RS-1, RS-5, TX-10 | | A-6 |
| C-23 | `officials.enforcement` | `enforcement_cost` (further powers: more agents, track-and-trace stamps) | increase | medium to long | TS-4 | | A-5 |

C-14: retailers near the line cannot raise shelf prices by the full tax without losing customers to Dunmarch, so they absorb more of it in their margins than interior retailers do. C-15 and C-16 apply DM-1 within the buyers' side: those with the fewest alternatives bear more. Interior smokers have no cheap way across the line. Light smokers who buy one pack at a time cannot spread the cost of a trip over many packs (LW-1), so even near the border they cross less often than carton buyers do.

C-17, C-18 and C-28 follow RS-10: informal sellers cannot advertise; the quality of what buyers receive varies more (counterfeit and stale packs, C-18), and buyers cannot tell genuine from counterfeit or fresh from stale before buying, and have no recourse if cheated (C-28). Disputes between smugglers are settled outside the courts (RS-10); the safety consequences of that are out of scope for version 1.

C-23 is Tier C because TS-4 (the intervention spiral) is itself Tier C pending expert decision (Q4).

C-20 applies TX-10: RS-9 moves the bundled purchases across the line, where they bear Dunmarch's and Kessick's taxes rather than Marren's, so Marren's sales tax revenue on those goods falls; because the purchases move to untaxed (for Marren) cross-border sellers, the sign is a decrease. C-29 is TX-10's base shift: smokers who switch to roll-your-own tobacco and cigars, and products redesigned to fall under the "other tobacco" definition (C-6, C-7), pay Marren's 25% tax on those products, so its revenue rises. E-cigarettes are untaxed, so switching to them shifts no base. C-22 is relative to the counterfactual: without the act, the quit program would have kept its general-revenue funding; with it, part of that funding is withdrawn as the earmark arrives (SB-7), so total spending on the program rises by less than the earmark. C-11, C-19, C-20 and C-29 are at depth 3; C-13 is at depth 4 (tax, cross-border trips, bundled purchases, store employment). All chains stop there.

Checks. RS-9 applies (C-11, C-12). RS-10 applies (C-17, C-18). RS-11: no benefit is tied to where a smoker lives, so it does not apply.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| Marren smokers' total cigarette consumption from all sources, short | — | Higher price in Marren (C-1); switching to untaxed products (C-6). | None needed | **decrease**, but by less than stamped sales in Marren fall (C-2), because part of that fall moves across the line (C-3) or into informal trade (C-4, C-5) rather than being given up. |
| `officials.enforcement`, `tax_revenue` (cigarette tax), short and medium | The rate on each remaining stamped pack more than doubles. | The stamped base shrinks: fewer purchases (C-2), cross-border buying (C-3), bootlegging and smuggling (C-4, C-5), substitution and reclassification (C-6, C-7), pre-buying before 1 January (C-8). | None | **ambiguous**. Revenue falls only if stamped sales fall by more than 57% (1 − 1.50/3.50). The method cannot say whether they do. In the medium run the minus chain strengthens as smuggling networks grow (C-5). What is not ambiguous is that revenue falls short of the static projection (C-21). Across Marren's taxes as a whole, the sales tax on trip goods falls (C-20) and the other-tobacco tax rises (C-29); TX-10 gives no combined sign. |
| Split of the tax between smokers and sellers, short | — | — | DM-1 | **Smokers bear the larger part overall** (C-1): many have few substitutes they accept, while Marren retailers sell many other goods. Within each side, the split varies: interior and light smokers bear more (C-15, C-16); border retailers bear more than interior ones (C-14). Rothbard's argument that a general sales tax cannot be shifted to buyers (DM-1 note, Q3) concerns general taxes; this is a selective excise, so it is not directly in play here. Not resolved. |
| `retailers.neighbors` that open or expand stores at the line, `earnings` of owners and staff, medium | A stream of extra Marren customers (C-11). | A one-time cost of new stores and stock, at risk if Marren cuts its rate or Dunmarch raises its own. | DM-3 | **ambiguous** by design. Those who build expected the stream to repay the cost (LW-5). |

## 8. Time structure

- **Announcement window (August to December).** Smokers buy ahead (C-8), so stamped sales are above the counterfactual in the autumn and below it in January and February. Early monthly revenue reports will mix this dip with the floor-stock receipts (K2) and should not be read as the act's lasting effect.
- **First months.** Cross-border buying (C-3), casual bootlegging (C-4), switching to untaxed products (C-6) and the loss of bundled sales at border stores (C-12) start at once.
- **First one to three years.** Organized smuggling grows as networks form, learn where the Tobacco Unit checks, and set up counterfeit stamps (C-5). How far it grows depends on what the networks expect: Dunmarch has kept its rate for 15 years and Marren is unlikely to reverse an increase, so they expect the gap to last (A-5). Border-store employment adjusts as leases and staffing come up for renewal (C-13). Producers launch reclassified products (C-7).
- **Erosion.** The $3.50 is fixed in money terms (TS-3). With general prices rising, the real tax, and the real gap with Dunmarch, shrink slowly unless one of the states raises its rate. The incentives behind C-3 to C-5 are therefore strongest just after the increase. Networks already built may outlast that erosion, because their setup costs are sunk; this is noted but not reported. TS-6 makes this argument for a repeal, but not for an incentive that erodes while the policy stays in force (GAP-010-3).
- **Escalation.** As smuggling becomes visible, pressure grows for more agents, track-and-trace stamps and limits on other states' sellers (TS-4, contested; C-23, Tier C).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-24 | `smokers` who keep buying stamped packs | `resources_available_other_uses` | decrease | The goods they would have bought with the money now paid in tax. | TX-1, OC-1 |
| C-25 | `smokers`, `retailers.marren` | `quantity_traded` (purchases priced out of the legal market entirely, not moved) | decrease | Purchases that smokers would have made at the old price and now forgo; both sides lose the gain they expected. | OC-4 |
| C-26 | `smokers.border` | `search_cost` (travel time and fuel) | increase | Time and travel spent crossing the line. | OC-2 |
| C-27 | `taxpayers` | `resources_available_other_uses` | decrease | What the eight new agents and the stamp program would otherwise have funded. | OC-3, OC-1 |

The general-fund share of the revenue is out of scope: what it is spent on is a separate budget decision. C-24 records what the payers give up.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Most of the increase is passed on in Marren shelf prices. | other | 0.85 | Shelf-price surveys after past increases; stamp tax collected at wholesale; smokers' few accepted substitutes. | C-1 shrinks; the burden falls more on sellers; C-2 shrinks. |
| A-2 | Some smokers cut back or switch at the higher price. | substitutability | 0.85 | Range of untaxed products; past sales after increases. | C-2 shrinks. |
| A-3 | Many Marren smokers can easily buy in Dunmarch or Kessick. | mobility | 0.85 | 45% of the population within 20 minutes; bridges at Port Alder; existing cross-border shopping for fuel. | C-3, C-4, C-11 to C-16, C-19, C-20 fail. |
| A-4 | Enforcement against casual resale and carrying above the allowance is weak, and the use tax is rarely collected. | enforcement | 0.8 | 20 agents for a long border; self-reported use tax; past seizure records. | C-4, C-17, C-18, C-28 not reported; C-5 weakens. |
| A-5 | Smuggling networks expect the price gap to last for years. | expectations | 0.65 | Dunmarch's 15-year-old rate; politics of repealing tax increases in Marren. | C-5 and C-23 not reported; smuggling stays casual. |
| A-6 | Untaxed or lower-taxed products are acceptable substitutes for some smokers. | substitutability | 0.75 | Market shares of roll-your-own and e-cigarettes; experience after past increases. | C-6, C-29 not reported. |
| A-7 | Producers can make cigarette-like products that meet the "other tobacco" definition. | other | 0.7 | Statutory definitions of cigarette and little cigar; products already sold elsewhere. | C-7 not reported. |
| A-8 | Border retailers, health groups and producers organize to change the rules. | other | 0.7 | Existing associations; past lobbying on tobacco taxes. | C-10 not reported. |
| A-9 | Smokers know the date and can store cartons. | expectations | 0.8 | Publicity of the signing; cartons keep for months. | C-8 not reported. |
| A-10 | Cross-border cigarette buyers also buy fuel, snacks and other goods on the same trip. | other | 0.75 | Convenience-store basket data; fuel price differences across the line. | C-11, C-12, C-13, C-20 weaken. |
| A-11 | The cost of a trip is large relative to the saving on one pack but small relative to the saving on a carton. | other | 0.8 | $3.70 a pack against travel time and fuel for a 20-minute drive. | C-16 not reported. |
| A-12 | Smuggling networks corrupt enforcement officers on a meaningful scale. | enforcement | 0.25 | Integrity record of the Revenue Department. | Below cut-off; not reported. |
| A-13 | Dunmarch or Kessick limit sales to Marren residents. | other | 0.2 | Their revenue gain from the trade (C-19). | Below cut-off; not reported. |
| A-14 | Marren border retailers move across the line within five years. | mobility | 0.35 | Lease terms; licensing in the neighboring states. | Below cut-off; not reported. |
| A-15 | The quit program was already funded from general revenue, and the act has no maintenance-of-effort clause. | revenue_use | 0.6 | Budget lines for the program; text of K5. | C-22 not reported. |

## 11. Report

**The policy.** Marren raises its cigarette tax from $1.50 to $3.50 a pack, collected through tax stamps, with a one-time tax on retailers' stock. Its neighbors tax cigarettes at $0.40 and $0.80, and almost half of Marren's people live within 20 minutes of one of them. Residents may bring in one carton a month untaxed. A small share of the revenue funds enforcement and the quit-smoking program; the rest goes to the general fund.

**Visible consequences.** Cigarettes cost more in Marren (C-1) and fewer stamped packs are sold there (C-2).

**Invisible consequences.**
- *Smokers near the border* buy in Dunmarch and Kessick (C-3) and spend time doing it (C-26). *Interior smokers*, and those who buy a pack at a time, bear more of the tax (C-15, C-16). Many smokers switch to roll-your-own, cigars and e-cigarettes (C-6), and producers design cigarette-like products taxed at the lower rate (C-7). Before the increase, smokers stocked up (C-8).
- *An informal trade grows*: casual resale at once (C-4), organized smuggling with counterfeit stamps over the following years (C-5). Its buyers search harder (C-17), receive more variable quality (C-18) and cannot judge it before buying (C-28).
- *Marren retailers near the border* absorb part of the tax (C-14), lose the fuel, snacks and other goods their customers now buy on cross-border trips (C-12), and employ fewer people over time (C-13). *Stores across the line* gain (C-11), and the neighboring states collect more tax (C-19).
- *The state* collects less than a projection based on pre-increase sales (C-21) and loses some sales tax on goods bought across the line (C-20), while collecting more of the tax on other tobacco products (C-29). If general funding for the quit program is trimmed as the earmark arrives (C-22), the program gains less than the earmark. Enforcement costs grow (C-27), and pressure for more enforcement follows (C-23).
- *Smokers who keep buying stamped packs* give up what they would have bought with the tax (C-24); those priced out entirely forgo purchases they valued (C-25).

**Ambiguous effects.** Whether cigarette tax revenue rises or falls: it falls only if stamped sales fall by more than 57%. Whether new stores at the line pay for themselves.

**Key conditions.** Ease of crossing the border (A-3, p = 0.85) drives most of the less obvious effects. Whether smuggling becomes organized depends on networks expecting the gap to last (A-5, p = 0.65).

**What this analysis cannot say.** How large any effect is; whether revenue rises; health effects of smoking less or switching products, and safety effects of smuggling (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | smokers | price_paid (stamped, in Marren) | increase | short | visible | B | TX-2, DM-1 | A-1 |
| C-2 | retailers.marren | quantity_traded (stamped, in Marren) | decrease | short | visible | B | TX-2 | A-1, A-2 |
| C-3 | smokers.border | cross_border_purchases | increase | short | invisible | B | RS-4, TX-4 | A-3 |
| C-4 | intermediaries.bootleggers | informal_activity | increase | short | invisible | B | RS-3, TX-4 | A-3, A-4 |
| C-5 | intermediaries.smuggling_networks | informal_activity | increase | medium | invisible | B | RS-3, TS-2 | A-4, A-5 |
| C-6 | smokers | quantity_substitute (other tobacco, e-cigarettes) | increase | short | invisible | B | RS-1, TX-3 | A-6 |
| C-7 | producers | reclassification | increase | medium | invisible | B | RS-5, TX-4 | A-7 |
| C-8 | smokers | quantity_traded (stamped packs, Oct–Dec) | increase | short | invisible | B | RS-8 | A-9 |
| C-9 | stamping_agents, retailers.marren | compliance_cost | increase | short | invisible | A | TX-5 | none |
| C-10 | border retailers, health groups, producers | lobbying_effort | increase | medium | invisible | B | RS-7 | A-8 |
| C-11 | retailers.neighbors | quantity_traded (cigarettes and trip goods) | increase | short | invisible | B | RS-4, RS-9 | A-3, A-10 |
| C-12 | retailers.marren.border | quantity_traded (untaxed trip goods) | decrease | short | invisible | B | RS-4, RS-9 | A-3, A-10 |
| C-13 | retailers.marren.border | employment | decrease | medium | invisible | B | TX-3, RS-9 | A-3, A-10 |
| C-14 | retailers.marren.border | net_price_received (cigarettes) | decrease | short | invisible | B | TX-2, DM-1 | A-3 |
| C-15 | smokers.interior | tax_share_borne | increase | short | invisible | B | DM-1 | A-3 |
| C-16 | smokers.light | tax_share_borne | increase | short | invisible | B | DM-1, RS-4 | A-3, A-11 |
| C-17 | buyers of informal cigarettes | search_cost | increase | short | invisible | B | RS-10 | A-4 |
| C-18 | buyers of informal cigarettes | quality_variability | increase | short | invisible | B | RS-10 | A-4 |
| C-19 | neighboring_jurisdictions | tax_revenue | increase | short | invisible | B | RS-4 | A-3 |
| C-20 | officials.enforcement | tax_revenue (Marren sales tax on trip goods) | decrease | short | invisible | B | RS-4, RS-9, TX-10 | A-3, A-10 |
| C-21 | officials.enforcement | tax_revenue_vs_static_projection | decrease | short | invisible | B | TX-9 | A-1, A-2, A-3, A-4 |
| C-22 | quit_program.clients | quantity_traded (services funded from general revenue) | decrease | medium | invisible | B | SB-7 | A-15 |
| C-23 | officials.enforcement | enforcement_cost | increase | medium–long | invisible | C | TS-4 | A-5 |
| C-24 | smokers (stamped buyers) | resources_available_other_uses | decrease | short | invisible | A | TX-1, OC-1 | none |
| C-25 | smokers, retailers.marren | quantity_traded (purchases forgone entirely) | decrease | short | invisible | B | OC-4, TX-2 | A-1, A-2 |
| C-26 | smokers.border | search_cost | increase | short | invisible | B | OC-2 | A-3 |
| C-27 | taxpayers | resources_available_other_uses | decrease | short | invisible | A | OC-3, OC-1 | none |
| C-28 | buyers of informal cigarettes | quality_information | decrease | short | invisible | B | RS-10 | A-4 |
| C-29 | officials.enforcement | tax_revenue (other tobacco products) | increase | short–medium | invisible | B | RS-1, RS-5, TX-10 | A-6 |
| — | officials.enforcement | tax_revenue (cigarette tax) | ambiguous | short–medium | visible | B | rate vs base (C-2 to C-8) | A-1 to A-5 |
| — | retailers.neighbors (new stores) | earnings | ambiguous | medium | invisible | B | C-11 vs setup cost; DM-3 | A-3, A-5 |

## Gaps found

- GAP-010-1 (closed in catalog 0.3: `quality_variability`, `quality_information`; named in RS-10): C-18 is now `quality_variability` increase and the new C-28 is `quality_information` decrease, both Tier B.
- GAP-010-2 (closed in catalog 0.3: TX-10): C-20 now Tier B. TX-10 also gives C-29, the rise in the tax on other tobacco products as smokers switch to them.
- GAP-010-3 (open): TS-6 says that stock changes with sunk costs (exit, reclassification, lost capital) persist after a repeal. The same reasoning applies when the incentive behind an investment erodes while the policy stays in force (a money-fixed rate eroded by inflation, TS-3): smuggling networks whose setup costs are sunk keep operating at a smaller price gap than would have induced them to form. There is no rule to report this. Proposed fix: widen TS-6's precondition from "a repeal" to "a repeal, or the erosion of the policy's incentive (TS-3)", with `persistence` recorded the same way, or add a TS-3 note: "Responses that required sunk investment shrink by less than the incentive does." Tier B, assuming `reversal_cost`.
