# WE-038 Municipal fiber network funded by revenue bonds

Analyst: draft (Handbook 0.8, held-out test)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional city. It resembles real municipal broadband projects but is not modeled on any one of them. It was chosen as a held-out test of catalog 0.8: a public supplier that sells at a set price **without** a fixed quantity (so PC-19's precondition fails), into a market with private incumbents whose networks are sunk; the network is paid for by revenue bonds (OC-8), and any shortfall in debt service falls on the ratepayers or the other spending of a city-owned electric utility, depending on how an unclear provision is read (CR-8, 0.8 clarification on contingent payers). It also exercises RS-16's mirror case, CR-7c on the incumbents' asset values, and OC-3's funding and baseline clauses. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Calderby Community Fiber Ordinance.** Calderby, in the State of Merrin, has about 180,000 people in 72,000 households and about 6,000 business premises. About 64,000 households (89%) buy home broadband. Two private incumbents serve the city: a cable company with about 60% of subscribers and a telephone company with about 40%, half of them on older copper lines. Their price for a 1 Gbps service, or the nearest they offer, is about $80 a month, and has risen about 3% a year for five years. A private fiber builder applied in 2025 for permits to build in two newer neighborhoods (about 9,000 homes) and has not started.

The city owns its electric utility, Calderby Light and Power (CLP): about 84,000 accounts, of which 72,000 are inside the city (66,000 residential, 6,000 commercial) and 12,000 in the townships of Orvel and Dunmere, outside the city, which the broadband network will not serve. CLP's annual revenue is about $150 million. Its rates are set by the city council on a cost-of-service basis, including interest on CLP's own debt. Each year CLP transfers 6% of its revenue (about $9 million) to the city's general fund in lieu of taxes, spends about $18 million on distribution maintenance (tree trimming, pole and transformer replacement) and about $25 million on capital work paid from rates. Merrin law lets cities charge private telecom providers a right-of-way fee of 4% of gross revenue earned in the city (about $2.5 million a year from the two incumbents); the city's own network does not pay it.

The ordinance was proposed by the mayor with a feasibility study on 3 March 2026, introduced on 14 April 2026, adopted on 9 June 2026; the bonds were sold on 15 September 2026. Construction starts in October 2026; service opens zone by zone from 1 July 2027 and reaches the whole city by December 2029. No expiry.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 City service | `public_supply` | Home and small-business broadband (1 Gbps symmetric) | City, through a broadband division of CLP | $55 a month, no installation charge, fixed by ordinance until 30 June 2032, after which the council may change it. "Service shall be offered to every premises passed, without limit on the number of subscribers." The network passes all 78,000 premises; the backbone and electronics are sized for 100% take-up at the projected peak load of 2030. | Not offered outside the city limits. |
| K2 Revenue bonds | `government_borrowing` | Construction | City | $150 million of tax-exempt revenue bonds, 25 years, 4.5%, sold in the national municipal bond market. Includes $12 million of capitalized interest (interest until 30 September 2029) and a $10 million debt-service reserve. Level debt service from fiscal 2030: about $10.1 million a year. "Payable solely from the revenues of the network," subject to K3. | — |
| K3 Backstop | Contingent transfer | Debt service on K2 | CLP | "Any shortfall in the revenues of the network available for debt service shall be made good by the Calderby Light and Power from its rates." A drawn reserve is to be replenished by CLP within twelve months. | — |
| K4 Administration | Administration | K1 to K3 | CLP broadband division; bond trustee; city auditor | Operating costs (about $4 million a year fixed plus about $150 per subscriber a year), trustee fees and audits paid from network revenue before debt service. | — |

Unclear provision:
- U1, what "from its rates" requires of CLP. Reading U1-a: CLP may raise electricity rates to cover a shortfall. Reading U1-b: CLP must cover it out of the revenue its existing rates bring in, by cutting other spending (the transfer to the general fund, maintenance or capital work); the phrase identifies the source of the money, not a power to raise rates. The city attorney's memo to council cites both readings and does not choose.

Readings get no probability; where a sign depends on one, each reading's sign is reported.

**Figures for the shortfall.** Network revenue at $55 is $660 per subscriber a year. Revenue covers operating costs and debt service when 660 S = 4.0 million + 150 S + 10.1 million, that is S ≈ 27,700 subscribers (about 36% of premises). The feasibility study projects 45% take-up by 2031, assuming the incumbents keep charging about $80. At 30% take-up (23,400 subscribers) the shortfall would be about $3.2 million a year: about 2.1% of CLP's revenue, about $38 per electricity account, or about a third of the general-fund transfer.

The counterfactual is Calderby without the ordinance: no city network, no bonds, no backstop; the incumbents' prices follow their trend; the private builder decides on its own.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: the state sells a service at a price it sets. By CR-1: for households and businesses, adds an option (operation 2); for incumbents, changes what their own offer brings, since buyers now have a better alternative (CR-9; no option of theirs is removed). Not a price ceiling: incumbents may charge what they like. | The quantity is **not** fixed: anyone may subscribe, and capacity is ample at first (A-3). So PC-19's precondition ("quantity fixed by a budget") does not hold, and CR-6's 0.7 public-supply clause (a fixed quantity) does not either. See section 5. | CR-4, CR-6 (main clause and 0.8 mirror case, by analogy), RS-13, RS-16 (mirror case), SB-8 (in part), CR-7c, SB-4, RS-6, RS-7, RS-8 |
| K2 | Binary: the city borrows from lenders who choose to lend (CR-5), to be repaid from network revenue. | Yes | OC-8, OC-1, CR-8a, CR-8b |
| K3 | Binary: a transfer from CLP's ratepayers or other spending to bondholders, **only if** network revenue falls short (CR-8, 0.8: contingent payers). Which of CLP's payers bears it depends on U1. | Contingent on a shortfall (A-6) | CR-8 (0.7 and 0.8), CR-8d, OC-1, CR-12 |
| K4 | Binary: administration funded from the policy's own revenue | Yes | OC-3 (own revenue, and through K3 the contingent payers) |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `subscribers.city` (`buyers.current` who switch) | Households and small firms that move to the city service | Gain an option at $55 (CR-1, operation 2). |
| `subscribers.incumbent` (`buyers.current` who stay) | Those who stay with an incumbent | Their alternative improves; incumbents' offers to them change. |
| `buyers.prospective` | About 8,000 households without home broadband | A cheaper option appears. |
| `incumbents` (`sellers.current`), and their owners | Cable and telephone companies | A public rival sells at $55 with no limit on quantity; their networks in Calderby are sunk. |
| `incumbent_workers` | Local technicians, installers, retail and call staff | Fewer subscribers to serve. |
| `private_builder` (`sellers.prospective`) | The private fiber builder with pending permits | Its expected customers now have a $55 public option. |
| `bondholders` (lenders) | Buyers of the K2 bonds | A new tax-exempt bond, backstopped by CLP. |
| `borrowers.other` | Other borrowers in the municipal and wider bond market | Compete with K2 for lenders' means. |
| `CLP` | The utility, as a borrower and budget | Carries a contingent liability (K3). |
| `ratepayers.city`, `ratepayers.outside_city` | CLP's electricity customers in the city, and in Orvel and Dunmere | Under U1-a, pay higher rates in a shortfall year; outside the city, without access to K1. |
| `recipients.clp_other_spending` | The general fund (through CLP's transfer) and those it funds; ratepayers served by CLP's maintenance and capital work | Under U1-b, bear a shortfall through cuts. |
| `recipients.general_fund`, `taxpayers` | Those funded by and paying for the city's general fund | Right-of-way fee revenue changes. |
| `sellers.complements` | Sellers of streaming services and home-network equipment | More households online. |
| `contractors.construction` | Fiber construction firms and crews | Build the network, 2026 to 2029. |
| `officials.enforcement` | CLP broadband division, bond trustee, city auditor | Run and oversee the network. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `subscribers.city` | `price_paid` (monthly broadband price, against what they would have paid an incumbent) | decrease | short to medium (from the zone opening, July 2027 to December 2029) | CR-1 (operation 2), CR-2, CR-4 | A-1, A-2 |
| C-2 | `CLP` broadband division | `quantity_supplied` (city subscriptions) | increase | short to medium | CR-4, CR-6 (0.8 mirror case, by analogy) | A-2, A-3 |

C-1 is what the ordinance's supporters point to. A household that switches reveals that it ranks the $55 service above the incumbents' offers (CR-2); against the counterfactual price of about $80 (A-1), it pays less. C-2: because the quantity is not fixed, the number served is set by buyers' responses to $55 (CR-4), as the 0.8 mirror case of CR-6 says of a public buyer with an open quantity. While capacity is ample (A-3), no one who asks is refused, so there is no excess demand and no rationing (section 5).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | `incumbents` | `quantity_traded` (subscriptions in Calderby) | decrease | short to medium | RS-16 (mirror case), CR-4, CR-5 (0.7: a sale lost to a better offer) | A-2 |
| C-4 | `subscribers.incumbent` | `price_paid` | decrease | short to medium | RS-16 (mirror case), RS-13, CR-6 | A-1, A-4 |
| C-5 | `incumbents` | `net_price_received` (Calderby) | decrease | short to medium | CR-8b, RS-16 (mirror case) | A-1, A-4 |
| C-6 | `buyers.prospective` | `quantity_traded` (households buying broadband from any provider) | increase | short to medium | CR-4c (LW-3) | A-5 |
| C-7 | `incumbents` | `investment_target` (upgrades of their Calderby networks) | ambiguous | medium | CR-4, CR-7, CR-12b | A-4, A-23 |
| C-8 | `incumbents` | `lobbying_effort` (at the state for limits on municipal networks; against the bond ordinance) | increase | short to medium | RS-7 | A-10 |
| C-9 | `private_builder` | `entry_rate` (private fiber building in Calderby) | decrease | short to medium | CR-4 (x: build, y: invest elsewhere), CR-7c, CR-10a | A-11 |
| C-10 | `subscribers.incumbent` | `term_prevalence` (contracts of one to two years with early-termination fees, signed before the city service reaches a zone) | increase | short (2026 to 2029) | RS-8, CR-10a, CR-4 | A-15 |
| C-11 | `incumbent_workers` | `employment`, `hours_worked` (incumbents' local staff) | at_least_one_decrease | medium | RS-6, CR-9 | A-2, A-12 |

**Why PC-19 does not apply, and what does.** PC-19 needs "the quantity fixed by a budget". Here the ordinance fixes the price and leaves the quantity open, and the network is sized for every premises (A-3). Applied as written, PC-19 would conclude excess demand at $55 and pressure on waiting, crowding and travel. That conclusion is wrong for this case and is not recorded: the precondition fails, so the pattern correctly does not fire. What remains is derived from the core rules. At $55 the city sells to every household that prefers it (CR-4), so the city's quantity is set by buyers (C-2), the 0.8 mirror case of CR-6 read for a seller. In the market as a whole, the city's entry is added supply at a lower price (RS-13): at their old price the incumbents now wish to sell more than buyers will take from them (CR-6, main clause, on the incumbents' side), so their price falls (C-4) and their quantity falls (C-3). RS-16's mirror case says the same: a good made cheaper pulls buyers from its substitutes, and the substitute's price falls where its supply cannot contract at once. The incumbents' networks are sunk and their cost of serving one more subscriber is far below $55 (A-4), so they cut prices and offer retention deals rather than withdraw. Two pieces of PC-19 survive: buyers who would have paid anyway gain what they no longer pay (SB-8's logic, here a lower price rather than a free good; C-20), and buyers move from substitutes (RS-16).

**Prices to those who stay (C-4, C-5).** Each dollar by which an incumbent cuts its price to a retained subscriber is a dollar less received (CR-8b). This is the transfer side of the incumbents' response, recorded on both sides.

**New buyers (C-6).** Some of the 8,000 households without broadband buy at $55 or at the incumbents' lower prices (CR-4c, A-5).

**Investment by incumbents (C-7).** Two chains. A lower expected return in Calderby lowers the yield of new investment there (CR-7, CR-4 with x: invest in Calderby, y: invest elsewhere): (−). Against that, an incumbent's older copper or cable plant now loses subscribers to fiber, so upgrading in Calderby keeps subscribers it would otherwise lose (CR-4, x: keep the old plant, y: upgrade): (+), with the premise that upgrading keeps enough subscribers to pay (A-23, p = 0.55). The (+) chain is a chain the rules derive with a premise above 0.5, so under CR-12's 0.8 clarification (kind 2) the combined sign is `ambiguous`.

**Lobbying (C-8).** The incumbents' loss is concentrated and depends on political decisions (the ordinance, a state law on municipal networks), so they lobby (RS-7, A-10). From 2027 on, the city has a concentrated stake in keeping K1 too; the city is not an actor class with means of its own, so this is not signed.

**The private builder (C-9).** Its expected customers now have a $55 public option, and it has not yet sunk its capital, so it can still invest elsewhere (CR-4, CR-10a; A-11). This is the unseen supply: fiber that a private firm would have built in two neighborhoods.

**Timing (C-10).** Service reaches zones over 30 months. Before the city service reaches a zone, incumbents offer contracts with early-termination fees to hold subscribers through the opening (CR-10a, RS-8; A-15). Against the counterfactual, such contracts are more common in 2026 to 2029; after the build-out the reason fades, and no sign is given for later years.

**Exit, relocation, reclassification, evasion.** Nothing is prohibited or taxed, so RS-3 and RS-5 have nothing to act on. The network serves only premises in the city limits; no household moves for broadband alone (no premise supports it).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-12 | `incumbents` (owners) | `asset_value` (incumbents' Calderby networks and the firms that own them) | decrease | short (part from 3 March 2026, more at adoption and the bond sale) | CR-7c, CR-10c, SB-4 | — | A-1, A-4, A-9 |
| C-13 | `incumbents` | `return_on_capital` (Calderby operations) | decrease | short to medium | CR-7b | — | A-1, A-4 |
| C-14 | `borrowers.other` | `interest_rate` | increase | short (from the sale) to long | OC-8, CR-6 (loan market), CR-7a | lenders' means: K2 bonds and other bonds, `substitute` | A-7 |
| C-15 | `borrowers.other` | `quantity_traded` (loans and bonds to other borrowers) | decrease | short to medium | OC-8, OC-1, CR-8a | as C-14 | A-7 |
| C-16 | `contractors.construction` | `employment`, `hours_worked` (fiber construction in Calderby) | at_least_one_increase | short (2026 to 2029) | OC-5, CR-8b, CR-9 | construction labor `input_to` the network | A-17 |
| C-17 | `recipients.general_fund`, `taxpayers` | `tax_revenue` (right-of-way fees from incumbents) | decrease | short to medium | TX-10, CR-9 | city service and incumbents: `substitute`; the fee is a share of incumbents' revenue | A-1, A-4 |
| C-18 | `recipients.general_fund`, `taxpayers` | `resources_available_other_uses` | at_least_one_decrease | short to medium | OC-6, CR-8b (0.7: payers from a general budget) | follows C-17 | A-1, A-4 |
| C-19 | `CLP` | `interest_rate` (on CLP's own borrowing) | increase | short to medium | CR-6 (loan market), CR-7c, CR-11c | K3: `contract` between CLP and bondholders | A-13 |
| C-20 | `subscribers.city`, `subscribers.incumbent` (households that would have bought broadband anyway) | `resources_available_other_uses` | increase | short to medium | CR-3 (note), CR-8b, SB-8 | — | A-1, A-2, A-4 |
| C-21 | `sellers.complements` | `quantity_complement` (streaming subscriptions, home-network equipment) | increase | medium | RS-12, CR-9 | broadband and streaming/equipment: `complement`, partial | A-5, A-18 |
| C-22 | `ratepayers.city`, `ratepayers.outside_city` | `price_paid` (electricity) | U1-a: increase; U1-b: no_change | medium (shortfall years, from fiscal 2030) | CR-8 (0.8: contingent payers), CR-1, CR-2 | K3: `contract` | A-6 |
| C-23 | `recipients.clp_other_spending` | `resources_available_other_uses` (general fund, through a smaller CLP transfer), `maintenance_spending` (CLP distribution maintenance), `capital_stock_target` (CLP capital work) | U1-a: no_change; U1-b: at_least_one_decrease | medium (shortfall years) | CR-8 (0.8: contingent payers; 0.7: payers from a budget are a group), CR-8a | K3: `contract` | A-6 |
| C-24 | `ratepayers.city`, `ratepayers.outside_city` (who keep buying electricity) | `resources_available_other_uses` | U1-a: decrease; U1-b: no_change | medium (shortfall years) | CR-3 (note), CR-8b | as C-22 | A-6, A-24 |
| C-25 | `ratepayers.city`, `ratepayers.outside_city` | `price_paid` (electricity) | increase | long | CR-1 (cost-of-service rate rule), CR-2, CR-9 | CLP's borrowing `input_to` electricity | A-13, A-14 |

**Incumbents' asset values (C-12, C-13).** The incumbents' Calderby plant cannot be moved, so the lower yield settles on it (CR-7b): until the market reprices, their return falls (C-13). Their networks are durable assets whose price reflects expected yields (CR-10c), so the fall is capitalized when the network becomes expected, borne by whoever owns the incumbents then (CR-7c): part of the way from the mayor's proposal and feasibility study on 3 March 2026, as adoption grew more likely, and the rest at adoption (9 June) and the bond sale (15 September), after which construction was nearly certain. Later buyers of the firms pay the lower price and neither gain nor lose. This is the entry-side counterpart of EN-2: there, restricting entry raises incumbents' value; here, public entry lowers it (SB-4: "competing entry that lowers them"). In the long run returns on the incumbents' other capital are equalized (CR-7a), so no lasting change in return is signed.

**Borrowing (C-14, C-15).** The $150 million is lent by people who would otherwise have lent it to other borrowers (A-7). By CR-8a those means are not available to them; by CR-6 in the loan market their rate is higher than it would have been, and they borrow less (OC-8). The size is tiny against the national bond market, but the method signs directions, and OC-8 has no clause for a negligible effect (Gaps found, b). OC-8's further step, "repayment implies taxes later", does not fit revenue bonds: repayment comes from subscribers' payments and, only under a shortfall, from CLP (C-22 to C-24). Bondholders receive the interest (CR-8b); against the counterfactual of lending at a similar rate elsewhere, their return is not signed (CR-7a), and by CR-5 they expected to gain from buying.

**Fees to the general fund (C-17, C-18).** The fee is 4% of the incumbents' gross revenue in the city; their revenue falls (C-3, C-4), and the city network does not pay it. Fee revenue falls, and the general fund's loss is borne by a group: recipients of its spending, or taxpayers if it is made up (CR-8, 0.7; OC-6).

**CLP's own credit (C-19, C-25).** K3 is a contingent claim on CLP. Lenders to CLP know it (CR-11c) and price it (CR-6 in the loan market): CLP's own borrowing costs more than it would have (A-13). This holds under both readings of U1, since under either CLP must find the money. Because CLP's rates are set on cost of service, including interest (A-14), its next rate reviews pass the higher interest to ratepayers (C-25). This is a separate chain from the shortfall payments, at a later horizon (CR-12g).

**Who pays a shortfall (C-22 to C-24).** CR-8, 0.8: where a budget pays only if something happens, record its payers per reading or with a premise on the contingency. Here both are needed: whether a shortfall happens is a premise (A-6, p = 0.6), and who pays it is a reading. Under U1-a, CLP raises rates in shortfall years, and every electricity customer pays, including the 12,000 accounts in Orvel and Dunmere, who cannot buy the service (C-22). Customers who keep buying electricity, which almost all do (A-24), pay a sum they cannot avoid, so their means for other uses fall (C-24, CR-3 note). Under U1-b, rates do not move for this reason (C-22, `no_change`), and the shortfall is taken from CLP's other spending: a smaller transfer to the general fund, less maintenance, or less capital work, at least one (C-23, a group over actor classes and variables, CR-8 0.7). Each reading's sign is reported; the text, not the analyst, decides.

**Whether U1-b holds in the long run.** Money is fungible (CR-8d): a CLP that has cut maintenance to cover a shortfall can later ask for a general rate rise to restore it, on cost-of-service grounds. That chain would turn U1-b's `no_change` into an increase at a later horizon. It needs the premise that the council restores cut spending through a later rate rise (A-20, p = 0.45). Under CR-12's 0.8 clarification (kind 2) a derived chain whose premise is below 0.5 does not make the sign ambiguous: the derived sign stands, and the chain is recorded in section 10.

**Complements (C-21).** More households online buy more streaming and home-network equipment (RS-12, A-18).

**Construction (C-16).** The $150 million pays for crews and materials (CR-8b): fiber construction work rises while it lasts (OC-5). The matching loss is in C-15: the borrowing and spending of those crowded out.

Stopping points. C-24 leads to ratepayers' other spending (depth 3), diffuse: stopped. C-22 under U1-a raises the cost of electricity to local businesses, including the incumbents; electricity is not a material part of broadband cost, so RS-14's precondition fails and no chain to broadband prices is recorded. Home values in Calderby (cheaper broadband against a possible rate rise) would need a premise that buyers price either; not recorded. The private builder's suppliers: depth 3, diffuse.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `incumbents`, `investment_target`, medium | Upgrading keeps subscribers who would leave old plant for city fiber (A-23). | Lower expected return in Calderby (CR-7). | None | **ambiguous** (C-7). Decided by how much of each incumbent's plant is older copper or cable. |
| Households that buy broadband anyway and pay CLP for electricity (most city households), `resources_available_other_uses`, medium | Lower broadband price (C-20). | Under U1-a, higher electricity bills in shortfall years (C-24). Under U1-b, no rate chain; the cut in CLP's transfer reaches them only as recipients of general-fund spending, a group (C-23). | None | **U1-a: ambiguous; U1-b: increase** (C-26). Under U1-a the figures (about $300 a year saved by a switcher at $25 a month, against about $38 an account in a 30% take-up year) suggest the + chain is larger for switchers, but the households who stay with an incumbent save an unknown price cut, and many accounts are commercial; no dominance premise is stated. |
| City households and premises that buy no broadband, and `ratepayers.outside_city`, `resources_available_other_uses`, medium | None. | Under U1-a, higher electricity bills in shortfall years (C-24). | None needed | **U1-a: decrease; U1-b: no_change** (C-24). These are the ratepayers who pay for a service they do not use or cannot buy. |
| `ratepayers`, `price_paid` (electricity), medium and long | Shortfall payments under U1-a (C-22, medium); CLP's higher interest (C-25, long); restoration of cut spending under U1-b (A-20, below the cut-off). | None. | — | Medium: per reading (C-22). Long: **increase** (C-25). Not combined across horizons (CR-12g). |
| `recipients.general_fund`, `resources_available_other_uses`, medium | None. | Lower right-of-way fees (C-18); under U1-b, a possibly smaller CLP transfer (member of C-23). | None needed | **at_least_one_decrease** (C-18), more so under U1-b. |
| `subscribers.incumbent`, `price_paid`, short to medium | Under U1-a, CLP's rate rise raises incumbents' electricity cost. | City entry adds supply (C-4). | — | The (+) link is not a chain: RS-14 requires an input that is a material part of cost, and electricity is not, for broadband (CR-12, 0.7: an underivable opposing chain is a Tier C note). **decrease** (C-4). |
| `incumbents`, `return_on_capital`, long | — | — | CR-7a | **Not signed**: returns are equalized across uses in the long run. |

## 8. Time structure

- **Announcement to adoption (March to June 2026).** The incumbents' values fall part of the way from the proposal and the rest by the bond sale (C-12). The private builder's decision is affected from the proposal (C-9). Incumbents begin lobbying (C-8).
- **Build-out (October 2026 to December 2029).** Zones open in sequence. Before its zone opens, a household can sign an incumbent's retention contract (C-10); some delay switching until their term ends, so city take-up in each zone lags its opening. This shifts switching within a period in which it would not happen at all without the network, so it is a path note, not a timed consequence. Construction work runs through these years (C-16). Capitalized interest pays the bondholders until 30 September 2029, so no shortfall can arise before fiscal 2030.
- **Fiscal 2030 to 2032: the shortfall window.** Debt service of $10.1 million begins while take-up is still rising and incumbents' prices have fallen (C-4), which slows take-up below the study's projection. This is when A-6 is most likely to bite, and when C-22 to C-24 apply, per reading.
- **The fixed price erodes (TS-3).** $55 is fixed in money until mid-2032, while operating costs rise with prices. In real terms the price falls each year, which raises the chance of a shortfall (A-6) and lowers the incumbents' prices further against the counterfactual. After June 2032 the council may raise the price; actors' expectations of that are not modeled.
- **Capacity.** The network is sized for 2030 peak load at full take-up (A-3). If data use grows faster than planned and peak demand reaches capacity before CLP adds electronics, PC-19's situation arises: a set price with a capacity that does not expand, with pressure going to speed at the peak (`quality_per_unit`) or waiting for installations. A-21 (p = 0.3) is below the cut-off, so this is a conditional possibility, not a consequence.
- **Long run.** CLP's higher borrowing costs pass to rates at its reviews (C-25). Incumbents' returns are equalized (CR-7a).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-27 | `officials.enforcement` (CLP broadband division, trustee, auditor) | `enforcement_cost` (administration, billing, oversight of the bonds) | increase | The staff time and systems used for these. | OC-3, CR-8c |
| C-15 | `borrowers.other` | `quantity_traded` (loans) | decrease | Investment and purchases by borrowers crowded out (recorded in section 6). | OC-8, OC-1 |
| C-28 | `incumbents` | `resources_available_other_uses` | decrease | The price cuts on retained subscribers (C-5) and the margin on lost ones, while their Calderby costs are sunk. | CR-8b, CR-3 (note) |

**OC-3, who pays the administration.** K4 pays administration from the network's own revenue (OC-3: "from the policy's own revenue: it reduces what the revenue does elsewhere"). Here what the revenue does elsewhere is cover debt service, and any shortfall in that cover is made good under K3. So the payers of administration are, in good years, subscribers (through the $55), and, in shortfall years, the contingent payers of C-22 to C-24, per reading. They are not recorded again. **Right baseline (OC-3, 0.8):** the ordinance shrinks no activity that the city itself enforced; the city does not regulate the incumbents' service. No enforcement is made unnecessary, so C-27 is Tier A.

**Prevented exchanges.** None: the incumbents' lost sales are lost to a better offer, not prevented, so only the incumbents lose them (OC-4 Unless; CR-5, 0.7). Households that switch gain by their own ranking (CR-3b).

**Construction resources.** The $150 million of labor and materials used to build the network is withdrawn from other uses (CR-8a), named through the loan market as the borrowing of those crowded out (C-15; OC-1, naming the forgone uses).

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Without the network, incumbents' prices for comparable service would have stayed near $80, following their trend. | counterfactual_trend | 0.75 | Five years of about 3% a year rises; no other entrant built. | C-1, C-4, C-5, C-12, C-13, C-17, C-18 and C-20 shrink or vanish; if the private builder would have pushed prices down anyway, the counterfactual price is lower. |
| A-2 | Some households rank the $55 service above the incumbents' offers, and switch. | substitutability | 0.9 | Take-up of public fiber elsewhere; the $25 gap. | C-1 to C-3 and C-11 are not reported. |
| A-3 | Network capacity exceeds peak demand through the medium horizon, so no one who asks is refused. | binding | 0.8 | Network sized for 100% take-up at the 2030 projected peak. | PC-19 applies: rationing by speed or installation waits. |
| A-4 | The incumbents' Calderby networks are sunk and their cost of serving a subscriber is far below $55, so they keep serving and cut prices to retain subscribers rather than withdraw. | durability | 0.75 | Cable and copper plant already in place; retention offers in markets with public entrants. | C-4, C-5, C-17, C-18 vanish; C-3 is larger. |
| A-5 | Some households without broadband buy at $55 or at the incumbents' lower prices. | substitutability | 0.8 | Surveys give price as the main reason for not subscribing. | C-6 and C-21 are not reported. |
| A-6 | Network revenue falls short of debt service in at least one fiscal year from 2030 to 2034. | other | 0.6 | Break-even at about 27,700 subscribers (36%); the study's 45% assumes incumbents stay at $80, against A-4; capitalized interest ends in 2029; the price is fixed in money (TS-3). | C-22 to C-24 are not reported; K3 is never called; subscribers pay the network's full cost. |
| A-7 | The bonds are bought from saving that would otherwise have been lent to other borrowers at home. | other | 0.8 | Tax-exempt bonds are bought mainly by domestic households and funds. | C-14 and C-15 are not reported. |
| A-8 | The debt is expected to be repaid on schedule, not rolled over. | expectations | 0.85 | Level 25-year amortization; K3. | OC-8's repayment chain changes; not used further. |
| A-9 | Investors value the incumbents on expected earnings and treat the network as likely from the proposal on. | expectations | 0.8 | Analyst coverage; local press. | C-12 is not reported. |
| A-10 | The incumbents can organize lobbying at a cost below their stake. | other | 0.9 | Their trade association's activity on municipal networks. | C-8 is not reported. |
| A-11 | The private builder would have built in at least one of its two neighborhoods without the network. | other | 0.55 | Permit applications filed in 2025; its build-outs in similar cities. | C-9 is not reported. |
| A-12 | Incumbents adjust their local staff to the subscribers they serve. | alternative_uses | 0.6 | Staffing ratios per subscriber. | C-11 is not reported. |
| A-13 | Lenders and rating agencies treat K3 as a contingent liability of CLP. | other | 0.65 | Rating agency criteria for utility guarantees of affiliated enterprises. | C-19 and C-25 are not reported. |
| A-14 | CLP's rates are set on cost of service, including interest on its debt. | other | 0.85 | Council rate ordinance. | C-25 is not reported. |
| A-15 | Incumbents can offer term contracts with early-termination fees, and some households sign them. | other | 0.6 | Incumbents' practice in markets with announced entrants. | C-10 is not reported. |
| A-17 | Construction contractors hire or add hours for the build. | alternative_uses | 0.8 | Contract volume relative to local crews. | C-16 is not reported. |
| A-18 | Broadband and streaming services or home-network equipment are used together by marginal subscribers. | substitutability | 0.6 | Household surveys of new subscribers. | C-21 is not reported. |
| A-20 | Under U1-b, the council later restores spending cut to cover a shortfall through a general rate rise. | revenue_use | 0.45 | Council's record of deferring rate rises before elections; CR-8d makes it possible. | Below the cut-off: not reported. If true, C-22 under U1-b becomes an increase at a later horizon. |
| A-21 | Peak demand reaches network capacity before 2033. | binding | 0.3 | Traffic growth forecasts against the network's design. | Below the cut-off: not reported. If true, PC-19 applies from then: speed at the peak or installation waits worsen, as a group. |
| A-22 | CLP uses its control of poles to slow incumbents' work on them. | other | 0.35 | Pole attachment rules are set by the state and enforced on complaint. | Below the cut-off: not reported. If true, incumbents' `compliance_cost` and delays rise. |
| A-23 | For an incumbent with older plant in Calderby, upgrading to fiber keeps enough subscribers to pay. | other | 0.55 | Half the telephone incumbent's subscribers are on copper. | The (+) chain of C-7 fails; investment is a decrease. |
| A-24 | Almost all electricity customers keep buying electricity from CLP when rates rise slightly. | substitutability | 0.9 | No competing supplier; few customers can self-generate. | C-24 under U1-a weakens to those who keep buying. |

## 11. Report

**The policy.** Calderby borrows $150 million through revenue bonds to build a fiber network to every premises in the city, and from mid-2027 sells 1 Gbps service at $55 a month, fixed until mid-2032, to anyone who asks, with no limit on numbers. The bonds are to be paid from the network's revenue; any shortfall is to be made good by the city's electric utility "from its rates". Whether that lets the utility raise electricity rates, or requires it to cut other spending, is unclear.

**Visible consequences.** Households that switch pay $55 rather than about $80 (C-1); the city network serves whoever signs up (C-2); construction work rises during the build (C-16).

**Invisible consequences.**
- *The incumbents and their customers.* The incumbents lose subscribers (C-3), cut prices to those who stay (C-4, C-5), lose value from the day the network became likely (C-12) and earn less on their Calderby plant (C-13). Their local staff or hours fall (C-11). Before the city service reaches each area, they sign more customers to term contracts (C-10). They lobby against the network (C-8). Whether they invest more or less in Calderby is ambiguous (C-7).
- *Households.* Households that would have bought broadband anyway have more to spend on other things (C-20); some households without broadband start buying it (C-6), and buy more streaming and home equipment (C-21).
- *What is not built.* A private builder that would have built fiber in two neighborhoods is less likely to (C-9).
- *Borrowing.* Other borrowers face slightly higher rates and borrow less (C-14, C-15). The utility's own borrowing costs more because of the backstop (C-19), and over time that reaches electricity rates (C-25).
- *The general fund.* Fee revenue from the incumbents falls (C-17), and its recipients or taxpayers bear it (C-18).
- *If revenue falls short (A-6, p = 0.6).* Under U1-a, every electricity customer pays more in the shortfall years, including the 12,000 outside the city who cannot buy the service (C-22, C-24). Under U1-b, electricity rates do not move for this reason, and the shortfall is taken from the utility's transfer to the general fund, its maintenance or its capital work (C-23).
- *Costs.* Administration and oversight (C-27), paid from network revenue and, in a shortfall, by the same contingent payers.

**Ambiguous effects.** Incumbents' investment in Calderby (C-7). Under U1-a, whether a typical city household gains or loses in money (C-26): cheaper broadband against higher electricity bills in shortfall years.

**Key conditions.** Whether a shortfall occurs (A-6, p = 0.6); this is the premise on which the payers' side rests. That the incumbents cut prices rather than withdraw (A-4, p = 0.75). That capacity stays ample (A-3, p = 0.8); if it does not, the service would be rationed at the peak (A-21, below the cut-off). The counterfactual price trend (A-1).

**What this analysis cannot say.** How large any effect is; whether the network will pay for itself; whether the gain to subscribers outweighs the losses to incumbents, crowded-out borrowers and contingent payers; which reading of U1 a court would adopt; any effect on health, education or the environment (out of scope for version 1); whether the policy is desirable.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | subscribers.city | price_paid (broadband, against the incumbents' price) | decrease | short–medium | visible | B | CR-1, CR-2, CR-4 | A-1, A-2 |
| C-2 | CLP broadband division | quantity_supplied (city subscriptions) | increase | short–medium | visible | B | CR-4, CR-6 (0.8 mirror, by analogy) | A-2, A-3 |
| C-3 | incumbents | quantity_traded (Calderby subscriptions) | decrease | short–medium | invisible | B | RS-16 (mirror), CR-4, CR-5 | A-2 |
| C-4 | subscribers.incumbent | price_paid | decrease | short–medium | invisible | B | RS-16 (mirror), RS-13, CR-6 | A-1, A-4 |
| C-5 | incumbents | net_price_received (Calderby) | decrease | short–medium | invisible | B | CR-8b, RS-16 (mirror) | A-1, A-4 |
| C-6 | buyers.prospective | quantity_traded (households buying broadband) | increase | short–medium | invisible | B | CR-4c | A-5 |
| C-7 | incumbents | investment_target (Calderby upgrades) | ambiguous | medium | invisible | B | CR-4, CR-7, CR-12b | A-4, A-23 |
| C-8 | incumbents | lobbying_effort | increase | short–medium | invisible | B | RS-7 | A-10 |
| C-9 | private_builder | entry_rate (private fiber in Calderby) | decrease | short–medium | invisible | B | CR-4, CR-7c, CR-10a | A-11 |
| C-10 | subscribers.incumbent | term_prevalence (contracts with early-termination fees) | increase | short | invisible | B | RS-8, CR-10a, CR-4 | A-15 |
| C-11 | incumbent_workers | employment, hours_worked | at_least_one_decrease | medium | invisible | B | RS-6, CR-9 | A-2, A-12 |
| C-12 | incumbents (owners) | asset_value (Calderby networks and their firms) | decrease | short | invisible | B | CR-7c, CR-10c, SB-4 | A-1, A-4, A-9 |
| C-13 | incumbents | return_on_capital (Calderby) | decrease | short–medium | invisible | B | CR-7b | A-1, A-4 |
| C-14 | borrowers.other | interest_rate | increase | short–long | invisible | B | OC-8, CR-6, CR-7a | A-7 |
| C-15 | borrowers.other | quantity_traded (loans to other borrowers) | decrease | short–medium | invisible | B | OC-8, OC-1, CR-8a | A-7 |
| C-16 | contractors.construction | employment, hours_worked (fiber construction) | at_least_one_increase | short | visible | B | OC-5, CR-8b, CR-9 | A-17 |
| C-17 | recipients.general_fund, taxpayers | tax_revenue (right-of-way fees) | decrease | short–medium | invisible | B | TX-10, CR-9 | A-1, A-4 |
| C-18 | recipients.general_fund, taxpayers | resources_available_other_uses | at_least_one_decrease | short–medium | invisible | B | OC-6, CR-8b | A-1, A-4 |
| C-19 | CLP | interest_rate (CLP's own borrowing) | increase | short–medium | invisible | B | CR-6, CR-7c, CR-11c | A-13 |
| C-20 | subscribers.city, subscribers.incumbent (would have bought anyway) | resources_available_other_uses | increase | short–medium | invisible | B | CR-3, CR-8b, SB-8 | A-1, A-2, A-4 |
| C-21 | sellers.complements | quantity_complement (streaming, home-network equipment) | increase | medium | invisible | B | RS-12, CR-9 | A-5, A-18 |
| C-22 | ratepayers.city, ratepayers.outside_city | price_paid (electricity) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-8, CR-1, CR-2 | A-6 |
| C-23 | recipients.clp_other_spending | resources_available_other_uses (general fund), maintenance_spending (CLP), capital_stock_target (CLP capital work) | U1-a: no_change; U1-b: at_least_one_decrease | medium | invisible | B | CR-8, CR-8a | A-6 |
| C-24 | ratepayers.city, ratepayers.outside_city (keep buying) | resources_available_other_uses | U1-a: decrease; U1-b: no_change | medium | invisible | B | CR-3, CR-8b | A-6, A-24 |
| C-25 | ratepayers.city, ratepayers.outside_city | price_paid (electricity) | increase | long | invisible | B | CR-1, CR-2, CR-9 | A-13, A-14 |
| C-26 | households buying broadband anyway and paying CLP | resources_available_other_uses | U1-a: ambiguous; U1-b: increase | medium | invisible | B | CR-12b, CR-3, CR-8b | A-1, A-2, A-4, A-6, A-24 |
| C-27 | officials.enforcement (broadband division, trustee, auditor) | enforcement_cost (administration) | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-28 | incumbents | resources_available_other_uses | decrease | short–medium | invisible | B | CR-8b, CR-3 | A-1, A-4 |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. The step closest to one was the public supplier with an open quantity (section 5): no pattern covers it and CR-6's public-supply clause covers only the fixed-quantity case and a public *buyer* with an open quantity. It was derived from CR-4 (buyers set the quantity), CR-6's main clause on the incumbents' side, CR-9 and RS-13. That is a missing pattern, not a gap in the calculus.

**(b) Unclear core rules.**
1. *CR-8, 0.8, contingent payers: "per reading or with a premise".* This case needs both at once: a premise on whether the contingency happens (A-6) and a reading for who pays (U1). Read "or" as "and/or": the consequences carry per-reading signs and the contingency premise (C-22 to C-24).
2. *CR-6, 0.7 and 0.8, public supply.* The 0.7 clause covers a public supplier with a fixed quantity; the 0.8 mirror covers a public buyer with an open quantity. A public *seller* with an open quantity is the other mirror case and is not stated. Applied by analogy (C-2): the quantity is set by buyers' response and, while capacity is ample, no pressure arises; the price effect appears in the private segment instead (C-4).
3. *Who pays administration funded from own revenue that is itself backstopped.* OC-3's "from the policy's own revenue" bullet and CR-8's contingent-payer clause meet here; the analysis read them together (section 9), so that administration is paid by subscribers in good years and the contingent payers in bad ones.

**(c) Missing or wrong patterns.**
1. *PC-19 and a public seller with an open quantity.* PC-19's precondition (quantity fixed by a budget) correctly fails here. Applied as written without checking it, PC-19 would have given excess demand, waiting and crowding: the wrong signs, since no one is refused. Nothing in the catalog states the open-quantity case. Proposed: a branch of PC-19, or a new pattern, "public entry at a set price, quantity open": quantity set by buyers (CR-4); private sellers of the same good lose quantity and, where their capital is sunk, cut price (RS-13, RS-16 mirror, CR-6); their asset values fall from announcement (CR-7c); PC-19 applies only once capacity binds.
2. *OC-8 and revenue bonds.* OC-8's "repayment implies taxes later, recorded as a group of later payers" is wrong for revenue bonds: repayment is from the project's buyers, and from a backstop only if revenue falls short. Applied as written it would have added a taxpayer group that the record does not support; that piece was overridden. Proposed: OC-8 names the repayment source from the record (taxes, user charges, or a contingent backstop under CR-8 0.8).
3. *OC-8 and negligible size.* OC-8 has no clause like EN-6's 0.8 Unless ("record it ... with a premise that the effect is not negligible, or note it as negligible"). A $150 million issue in the national bond market gives C-14 a sign that is right in direction and almost certainly unobservable. Signed as OC-8 says; the asymmetry with EN-6 should be decided one way.
4. *Candidate: public entry into a market with sunk incumbents.* Not in 6.2e. Derivation as in (c)1. Seen once here.

**(d) Vocabulary.**
1. `public_supply` is defined as "quantity set by a budget". This case has a set price and an open quantity; the instrument fits only by stretching. Proposed: `public_supply` with a field for whether quantity is fixed or open.
2. No instrument for a contingent guarantee or backstop (K3); recorded as "contingent transfer". `government_borrowing` does not cover it.
3. No actor class for lenders (bondholders); 2.2 has none, though OC-8 and CR-8 (0.7, borrowing) both name the lenders' side.
4. No variable for the quantity of loans to a class of borrowers; `quantity_traded (loans)` used for C-15.

**(e) Test of 0.8.**
- *PC-19 (0.7).* Worked as written in the sense that its precondition excluded it; but the case it excludes (set price, open quantity) is not covered anywhere, so the analyst had to derive it from the core rules. Partial: correct refusal, no coverage.
- *CR-6 0.7/0.8, public supply clarification.* Needed interpretation: the 0.8 mirror case (public buyer, open quantity) was applied by symmetry to a public seller with an open quantity. It gave the right answer (no rationing while capacity is ample), but only by analogy.
- *OC-8 (0.7), public borrowing.* Needed interpretation and one override: the crowding-out chain (C-14, C-15) worked as written; "repayment implies taxes later" failed for revenue bonds and was replaced by the record's repayment source.
- *CR-8 0.8, contingent payers.* Worked, with one interpretation: "per reading or with a premise on the contingency" had to be read as both (A-6 and U1). The per-reading recording of payers, including `no_change` for the reading under which a group does not pay, was straightforward.
- *CR-8 0.7, payers from a budget are a group.* Worked as written for U1-b (C-23) and for the general fund (C-18).
- *RS-16 (0.6, mirror case 0.7).* Worked as written: the mirror case gave the incumbents' price fall (C-4) once A-4 (supply cannot contract at once, because the plant is sunk) was stated. RS-13 gives the same sign; no conflict.
- *CR-7c, capitalization with the probability clause.* Worked as written for the incumbents (C-12), dated from proposal to bond sale; SB-4's "competing entry that lowers them" named the case.
- *OC-3 0.8, right baseline.* Worked as written: no enforcement is made unnecessary, so C-27 stays Tier A. The funding bullet needed reading with CR-8 0.8 (b3).
- *CR-12 0.8, three kinds of opposing chain.* Worked as written: kind 2 with p ≥ 0.5 made C-7 ambiguous (A-23); kind 2 with p < 0.5 left U1-b's `no_change` standing with the chain recorded in section 10 (A-20); kind 1 handled the incumbents' electricity cost (no chain, since RS-14's precondition fails).
- *Candidates from 6.2e.* None needed. A new candidate, "public entry at a set price into a market with sunk incumbents", is proposed in (c)4.
