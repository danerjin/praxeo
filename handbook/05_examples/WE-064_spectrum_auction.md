# WE-064 Auction of licenses in an unused radio band, with a build-out obligation and a per-bidder cap

Analyst: draft (Handbook 1.0, held-out test)  |  Rule catalog version: 1.0  |  Status: awaiting expert review

A stylized policy in a fictional country. Several countries auction spectrum licenses with coverage obligations and caps; this one is not modeled on any of them. It is a held-out test of catalog 1.0 on a kind of policy none of the 1.0 changes were drawn from: a right created by the policy and allocated by auction rather than by history. It probes EN-12 (which should not apply, since nothing is allocated by history), CR-7c on who captures the value of a created right when the recipient pays for it, EN-13's 1.0 baseline note where the resource has no users at all without the policy, PC-17 for a mandated term attached to a right the state creates (the build-out obligation), RS-17 for a cap on holdings per bidder, OC-1 and CR-8's 1.0 notes on receipts into the budget that also pays the administration, CR-6's 1.0 note that small effects are signed (the world price of radio equipment; the interest rate), and CR-12's 1.0 notes on what the response argument needs and on the baseline of patterns. The unclear provision is whether a license may be resold before the build-out deadline. The counterfactual throughout is **Tarnesse without the Award Regulations**: the band stays unused, as the Radio Act requires for spectrum that is not licensed, and the question of whether and how to release it stays open. Health effects of radio emissions and the visual effect of towers are outside the scope of version 1. The probabilities are illustrative; the evidence column says what a real analysis would cite.

## 1. Policy record

**Tarnesse 2.9 GHz Award Regulations.** Tarnesse is a country of about 12 million people with its own currency, the mark (M). Three mobile network operators serve it: Ardel Mobile (about 42% of subscriptions), Nevra Telecom (36%) and Kostel (22%). Each holds national licenses in three existing bands (about 110, 100 and 70 MHz in total respectively), all expiring in 2035. Mobile data traffic grows about 30% a year, and busy-hour capacity in the cities is tight; without new spectrum, operators add capacity by adding cell sites in their existing bands ("densification"). Fixed broadband: Linmark Fibre passes about 25% of homes with fibre; Pellow Networks' copper (DSL) lines serve about 1.6 million households, including about 700,000 outside fibre and cable areas. There are about 11,000 tower and rooftop sites, most owned by two tower companies (Selwyn Towers and Haldmoor Sites); new towers need municipal permits that take 4 to 9 months. About 1,400 certified tower riggers do about 3,000 site installations a year. All radio equipment is imported; Tarnesse buys about 0.4% of the world's mobile radio equipment.

The 2,880 to 3,000 MHz band ("the 2.9 GHz band", 120 MHz) has been unused since a defence radar left it in 2024. Under the Radio Act, no one may transmit on spectrum without a license. The Tarnesse Communications Authority (TCA) consulted on releasing the band in March 2026; the Award Regulations were made on 1 March 2027. The auction ran in September and October 2027; licenses run from 1 January 2028 to 31 December 2042. Five bidders qualified: the three operators, Linmark Fibre (which plans fixed wireless access outside its fibre footprint) and Ombra Group (a foreign operator seeking entry). A financial investor registered interest but did not qualify by the deposit date under the TCA's provisional reading of regulation 9(3).

**Figures.** Six blocks of 20 MHz at a reserve price of M40 million each (M240 million in all). The TCA's consultant valued the blocks at M100 million to M200 million each; projected receipts are M600 million to M1.2 billion, against a general budget of about M58 billion a year and annual borrowing of about M2 billion. Covering 90% of the population with this band takes about 6,500 sites per network; covering the cities and large towns (about 65% of the population), which operators said in consultation they would cover commercially within five years, takes about 3,000. Three to four networks building to 6,500 sites each is 20,000 to 26,000 installations in five years, 4,000 to 5,000 a year, beside the existing 3,000. About 2,000 new towers are projected. The TCA's added costs: M9 million for the auction and M2 million a year for monitoring coverage, funded by an increase in its annual appropriation from the general budget.

| Field | Value | Source sentence |
|---|---|---|
| Jurisdiction (and what lies just outside) | Tarnesse, nationally. Neighboring countries license the same band in their own ways; cross-border coordination limits power near borders. | reg. 2. |
| Announced / enacted / effective / expires | Consultation March 2026; Regulations made (announced) 1 March 2027; auction September to October 2027; licenses effective 1 January 2028; coverage deadline 31 December 2032; licenses expire 31 December 2042. | regs. 1, 8, 9, 12. |
| Enforcement (who, penalties, resources) | The TCA: coverage verified by drive tests and operators' coverage maps; a licensee that has not met the coverage obligation by the deadline has its license revoked, without refund. | reg. 9(2), reg. 10. |

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Auction | `rights_allocation` (auction) | Six national licenses of 20 MHz in the 2.9 GHz band | Bidders who qualify by deposit | Ascending clock auction; reserve M40 million a block; 15-year term; no right of renewal ("the Authority may re-auction or renew at market value"). | — |
| K2 Build-out obligation | `mandated_contract_term` | Each license | Each licensee | Service in the band to areas containing 90% of the population by 31 December 2032, or revocation without refund. | — |
| K3 Cap | `quota` on holdings | Blocks in the band | Each bidder and later holder, with its affiliates (control of more than 50%, or the right to appoint a majority of the board) | No more than two blocks awarded to, or held by, one person and its affiliates. | — |
| K4 Receipts | `revenue_use` | Auction payments | The Treasury | "Payments under these Regulations shall be paid into the Consolidated Fund." | — |
| K5 Administration | Enforcement | K1 to K3 | TCA, funded by its appropriation from the general budget | M9 million for the auction; M2 million a year for monitoring. | — |

Existing rules that stay in the counterfactual: the Radio Act (no transmission without a license); the operators' existing licenses, expiring 2035; tower permits; no regulation of mobile or broadband prices.

Unclear provision:
- **U1, resale before the coverage deadline.** Reg. 14: "A licence may be transferred, in whole or in part, with the consent of the Authority, and the obligations in regulation 9 pass with it." Reg. 9(3): "Until the coverage obligation is met, the licence is held by the licensee for the purpose of meeting it." Reading U1-a: transfers are allowed at any time with consent (reg. 14), and reg. 9(3) only states the purpose of the obligation. Reading U1-b: reg. 9(3) bars any transfer until the obligation is met or the deadline passes. The TCA has issued no guidance; its provisional reading for the deposit date is not a decision on the Regulations.

Readings get no probability; where a sign depends on U1, one sign per reading is given.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Rule families |
|---|---|---|---|
| K1 | Binary: the state creates a right and sells it. Against the counterfactual, it adds an option for winners (CR-1, operation 2: transmitting in the band), at a payment attached to the option of winning (operation 3). Allocated by auction, not in proportion to any history, so EN-12's preconditions are not met. | Yes, if any block is bid at or above reserve (A-1). | CR-5, CR-7c, CR-8b, SB-4, EN-13 (1.0), CR-4 (0.8: fixed cost per firm) |
| K2 | Triangular in form (a term in each license), with the state as the counterparty. It attaches revocation to the option of holding the license without building to 90% (CR-1, operation 3, dated 31 December 2032). | Binding on coverage beyond what licensees would choose (A-8). | PC-17, CR-1, CR-10a, RS-3, RS-5 |
| K3 | Triangular: removes the option of holding a third block. | Yes for bidders who would value a third block above its price (the three operators). | RS-17 (1.0), RS-5, EN-13 (1.0) |
| K4 | Binary: receipts to the general budget. | Yes | OC-1 (1.0), CR-8 (1.0), CR-8b, CR-8d |
| K5 | Binary: administration funded from the general budget that also receives K4. | Yes | OC-3, CR-8 (1.0) |

**The counterfactual law.** Without the Regulations, nobody may use the band (Radio Act). So the auction removes no one's option: every operation in K1 is an addition (CR-1, recording). Against that baseline, the losing bidders are not worse off by the band itself; they are reached only through what winners do with it (CR-9).

**K2 against PC-17's baseline.** PC-17's conclusion ("the bargaining range moves, so the other terms adjust") compares contracts with the term and the same contracts without it. Here the contract is a license that does not exist without the policy, so that comparison is with another policy (an auction without the obligation), not with the counterfactual. By CR-12's 1.0 note on the baseline of patterns, PC-17's "other terms adjust" is re-signed: against no band, the obligation's cost lowers what bidders will pay, but receipts still rise from zero (C-1); its consequences against the counterfactual are what licensees build (C-3, C-5), its breach (C-11), and its pull on inputs (C-25 to C-30). See section 7.

**K3 against RS-17's baseline.** RS-17 gives, for a threshold, staying below it, splitting into separately counted units, and a lower value of growing past it. The first is the law's own content. The second is valid against the counterfactual (C-8). The third compares with an auction without the cap: against no band, there is nothing to grow into, so it gives no consequence (CR-12, 1.0). RS-17's notch and kink distinction (1.0) does not fit: the cap is a prohibition above the line, not a burden that jumps or rises.

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `bidders` (incumbents and entrants) | The five qualified bidders | May bid for up to two blocks each. |
| `licensees` | Winners of blocks | May transmit in the band from 2028; must cover 90% by end-2032 or lose the license; may (U1-a) or may not (U1-b) transfer it before then. |
| `owners.incumbents` (`factor_owners.specific`) | Shareholders of Ardel, Nevra and Kostel | Their existing licenses and networks face added capacity and possible entry. |
| `entrants` | Linmark Fibre, Ombra | May enter wireless broadband if they win. |
| `bidders.financial` | Investors without networks | May bid to resell under U1-a; under U1-b would have to build or lose the license. |
| `mobile_customers.urban`, `customers.towns` | Buyers of mobile and wireless broadband in cities and in smaller towns | More capacity; service in the band reaches towns because of K2. |
| `fixed_broadband_sellers` (`sellers.substitutes`), `owners.copper` | Pellow Networks and its owners | Fixed wireless competes with DSL outside fibre areas. |
| `tower_owners` (`input_suppliers`, `factor_owners.specific`) | Selwyn, Haldmoor, landowners leasing sites | More demand for sites. |
| `riggers` | Certified tower riggers | More demand for installation work. |
| `other_projects` | Fibre builders and other operators' upgrade projects | Compete with the build-out for riggers and sites. |
| `equipment_vendors`, `buyers.foreign` | Foreign makers of radio equipment; operators abroad buying the same equipment | More orders from Tarnesse. |
| `other_borrowers` | Borrowers in Tarnesse's loan market | Licensees borrow; the Treasury may borrow less. |
| `treasury`; `taxpayers`, recipients of other spending, future taxpayers | The general budget and those it serves | Receives the auction payments; funds the TCA's added costs. |
| `officials.enforcement` | The TCA | Runs the auction and monitors coverage. |
| `lobbying groups` | Operators, entrants, town councils | Stakes in the deadline, waivers, U1 and the cap. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `treasury` | `non_tax_receipts` (auction payments) | increase | short (October 2027) | CR-5c, CR-8b | A-1 |
| C-2 | `licensees` | `asset_value` (licenses in the band) | increase | short | CR-7c, CR-10c, SB-4, CR-7 (0.9: assets without a market price, U1-b) | A-1 |
| C-3 | `licensees` | `investment_target` (network equipment in the band) | increase | short to medium | CR-1, CR-4, PC-17 | A-1, A-3 |
| C-4 | `mobile_customers.urban` | `quality_per_unit` (data speed and capacity in busy hours) | increase | medium | CR-9, LW-10 | A-1, A-4 |
| C-5 | `customers.towns` | `quality_per_unit` (service in the band in towns between the cities and the last 10%) | increase | medium | PC-17, CR-1 | A-3 |

C-1 to C-5 are what the Regulations' supporters expect: the state is paid, operators build, customers get more capacity, and coverage reaches the towns. Against the counterfactual every one is an increase from nothing in the band.

**Who captures the band's value (CR-7c with CR-5 and CR-8b).** CR-7c says that the value of an asset the policy creates "is captured by whoever receives it at creation". With an auction, the recipient pays for it. CR-5c places the price within the range both sides accept: no winner pays more than the value it expects (else it would have stopped bidding), and the clock rises until no more blocks are demanded than offered, so the price is set by the bids of those who drop out (CR-6). CR-8b: what the winner pays, the state receives. So the band's value is split: the price goes to the general budget (C-1), and each winner keeps the excess of its own expected value over the price (C-2 net of C-36). With five bidders each allowed two blocks, demand at the reserve is ten blocks for six, so the price rises above the reserve; the cap holds each operator's demand to two, so the price is set by the third-highest bidder's value for its blocks rather than by an operator's value for a third or fourth block. How large each share is the method cannot say. Two points follow without magnitudes: no part of the value goes to anyone by history (EN-12 does not apply), and the excess kept by winners is non-negative by their own ranking at the time of bidding (CR-5), not necessarily in money afterwards. There is no variable for the split ((d) 1).

**Prices to customers.** The auction price and the build-out cost are paid once per license, whatever the traffic carried: a cost fixed per firm, which bears on whether a firm takes and keeps a license, not on the price of each unit sold (CR-4, 0.8). The common claim that auction payments are passed on in phone bills is therefore not derived; a price effect would need a premise about entry and exit, which C-19 handles through added capacity instead.

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-6 | `bidders` | `applications` (qualified bidders) | increase | short | CR-4 (x: stay out, y: bid) | A-1 |
| C-7 | `bidders` | `compliance_cost` (auction preparation, advisers, deposits held) | increase | short | OC-2, CR-8c | A-1 |
| C-8 | `bidders`, `licensees` | `reclassification` (minority stakes and joint ventures below the affiliate line) | increase | short to medium | RS-17 (1.0), RS-5, CR-4 | A-5 |
| C-9 | `licensees` | `term_prevalence` (network-sharing agreements pooling band blocks) | increase | medium | RS-17, CR-4, CR-5 | A-6 |
| C-10 | `licensees` | `investment_target` (densification in existing bands) | decrease | medium | CR-4 (x: add sites in old bands, y: use the new band), CR-9, LW-10 | A-1, A-7 |
| C-11 | `licensees` | `legal_breach` (coverage overstated, letter-only sites, deadline missed) | increase | medium | RS-3, RS-5, CR-4 | A-8, A-9 |
| C-12 | `licensees` | `quantity_traded` (transfers of band licenses before 31 December 2032) | U1-a: increase; U1-b: no_change | medium | CR-1, CR-5a, EN-13 (1.0) | A-10 |
| C-13 | `licensees` | `reclassification` (sales of licensee companies or long capacity leases used in place of license transfers, before 31 December 2032) | U1-a: no_change; U1-b: increase | medium | RS-5, CR-4 | A-10, A-11 |
| C-14 | `bidders.financial` | `applications` (bidders without networks who plan to resell) | U1-a: increase; U1-b: no_change | short | CR-4, CR-10a | A-12 |
| C-15 | `lobbying groups` | `lobbying_effort` (questions that exist only under the Regulations: the deadline, waivers of revocation, U1, the cap at re-award) | increase | medium | RS-7 (1.0), CR-4 (1.0), CR-12 (0.9: activities only under the policy) | A-13 |
| C-16 | `entrants` | `number_of_sellers` (networks selling mobile or fixed wireless broadband) | increase | medium | CR-1, CR-4, RS-17 | A-14 |
| C-17 | `licensees` | `number_of_sellers` (users of the band) | increase | medium | EN-13 (1.0), CR-1 | A-1 |
| C-18 | `entrants` | `quantity_supplied` (fixed wireless broadband lines outside fibre areas) | increase | medium | CR-4, CR-9 | A-14, A-18 |

**Entry into the auction (C-6, C-7, C-14).** Bidding is an option the counterfactual lacks; those who expect a license to be worth more than the reserve after the build-out cost bid (CR-4; A-1). Preparing to bid uses resources that winners and losers alike spend (C-7; CR-8c). Under U1-a an investor without a network can win, resell to a builder before the deadline, and keep the margin; under U1-b it must build or lose the license, which it cannot do, so it does not bid (C-14; CR-4, CR-10a; A-12). There is no race to qualify: eligibility depends on a deposit, not on any history (EN-12 does not apply; TS-5 1.0 is not needed).

**The cap (C-8, C-9, C-16).** The cap removes the option of holding a third block for any person "together with its affiliates", defined by control. Investors who want more can take minority stakes in a second bidder, or form joint ventures below the control line (C-8; RS-17, RS-5; A-5). Licensees can also pool their blocks by network-sharing agreements, which the cap does not count (C-9; A-6). Against the counterfactual, where there is no band, both are increases from none. The cap's purpose is to leave room for a bidder other than the three operators; with A-14 an entrant wins and builds, raising the number of networks selling wireless broadband (C-16). That an entrant wins depends on the cap, but the sign is against no band, not against an uncapped auction.

**Substitution between capacity sources (C-10).** Without the band, traffic growth is met by adding sites in the existing bands. With it, part of that capacity comes from the band instead, which is cheaper per unit of capacity in the cities (A-7). So densification in the existing bands is lower than it would have been (CR-4; CR-9, LW-10: spectrum and sites are substitutes as inputs to capacity).

**The obligation and its breach (C-3, C-5, C-11).** K2 binds where licensees would not otherwise cover the towns with this band within five years (A-8: operators told the consultation they would cover about 65%). Against the counterfactual, all building in the band is an increase (C-3), and the towns get service in the band (C-5) because K2 requires it (A-3). Coverage is checked by drive tests and maps, so some licensees will meet it by the cheapest sites that pass the test, or overstate it, or miss it (C-11; RS-3, RS-5; A-9). That the building is bunched toward the deadline is a path note, not a consequence (section 8): without the policy no building in the band would happen at all (02_ontology.md, 2.5).

**Transfers (U1; C-12, C-13).** Under U1-a, a licensee who finds it cannot finance the build-out, or that another values the license more, sells it with the obligation (C-12; CR-5a; A-10). Under U1-b, no license changes hands before the deadline, as in the counterfactual, where there are no licenses (C-12, `no_change`); the same pressure goes to forms the regulation may not catch: selling the company that holds the license, or leasing its capacity long-term to another network (C-13; RS-5; A-11). Under U1-a no such reshaping is needed. After 31 December 2032 both readings allow transfers.

**EN-13's baseline (C-17).** EN-13 gives: rights move to those who value them most, so the number of users of the capped resource falls. Its 1.0 baseline note says that against no policy the number falls "through blocked entry and holders who sell their whole holding". Here the resource has no users without the policy, so no entry is blocked and no user is lost: the number of users of the band rises from none, under both readings (C-17). Transfers under U1-a can bring it below the number of first winners; that is a comparison with the allocation, not with the counterfactual ((e)). The cap also bounds consolidation: an operator already holding two blocks cannot buy more, so EN-13's premise that the highest-value users are among the buyers may fail (EN-13, 1.0).

**Lobbying (C-15).** Whether and how to release the band was debated before the Regulations and would have stayed contested on the counterfactual path (the 2026 consultation drew submissions from all five bidders). By CR-4's 1.0 note and RS-7 (1.0), lobbying on release as such is signed against that contest, and the case gives no premise, so it is not signed. The questions in C-15 exist only under the Regulations: an extension of the deadline, waivers of revocation, the reading of U1, the cap when the band is re-awarded in 2042. Lobbying on them is an increase against none (CR-12, 0.9; A-13). Town councils have a concentrated stake in the deadline being enforced; licensees in its extension.

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-19 | `mobile_customers.urban` | `quality_adjusted_price` (price per GB at a given speed) | decrease | medium | RS-13, CR-6, CR-9, CR-12 (0.8: kind 2 below the cut-off) | spectrum `input_to` mobile capacity | A-4, A-15 |
| C-20 | `owners.incumbents` | `asset_value` (licenses held in the existing bands) | decrease | short (from March 2027) | RS-13, CR-7c, CR-10c | existing bands and the new band: `substitute` (inputs to capacity) | A-4, A-15, A-28 |
| C-21 | `owners.incumbents` | `asset_value` (shares of the three operators) | ambiguous | short | CR-7c, CR-10c, CR-5, CR-12b | as C-20 | A-14, A-15, A-17, A-28 |
| C-22 | `fixed_broadband_sellers` | `quantity_traded` (DSL lines outside fibre areas) | decrease | medium | RS-16 (mirror), CR-9 | fixed wireless and DSL: `substitute` | A-14, A-18 |
| C-23 | `fixed_broadband_sellers` | `price_substitute` (DSL price per line of a given speed) | decrease | medium | RS-16 (1.0: per unit of quality; mirror), CR-6 (0.9: splitting a shift) | as C-22 | A-14, A-18, A-19 |
| C-24 | `owners.copper` | `asset_value` (Pellow's copper network) | decrease | short to medium | CR-7c, CR-10c | as C-22 | A-14, A-18, A-28 |
| C-25 | `tower_owners` | `net_price_received` (site lease rates) | increase | short to medium | CR-9, CR-6 (0.9), CR-12e (1.0: what the response argument needs) | sites `input_to` networks | A-3, A-20 |
| C-26 | `tower_owners` | `asset_value` (towers and site portfolios) | increase | short (from March 2027) | CR-7c, CR-10c, SB-4 | as C-25 | A-3, A-20, A-28 |
| C-27 | `tower_owners` | `quantity_supplied` (new towers) | increase | medium | CR-4, CR-7a, CR-6 (0.9) | as C-25 | A-3, A-20 |
| C-28 | `riggers` | `wage_rate` | increase | short to medium | CR-9, LW-10, CR-6 (0.9) | rigging `input_to` networks | A-3, A-22 |
| C-29 | `riggers` | `employment` | increase | medium | CR-9, LW-10, CR-7a | as C-28 | A-3, A-23 |
| C-30 | `other_projects` | `quantity_supplied` (installations by fibre builders and other upgrades, 2028 to 2032) | decrease | short to medium | CR-8a, RS-13 (1.0: crowding out), CR-6 | riggers and sites shared as inputs | A-3, A-22 |
| C-31 | `other_projects` | `quantity_supplied` (installations, 2033 onward) | ambiguous | medium to long | RS-8, CR-9, CR-12b | as C-30; fixed wireless and fibre: `substitute` | A-14, A-18, A-24 |
| C-32 | `equipment_vendors` | `quantity_traded` (radio equipment sold to Tarnesse) | increase | short to medium | CR-9, LW-10 | equipment `input_to` networks | A-1 |
| C-33 | `buyers.foreign` | `price_paid` (radio equipment, world market) | increase | short | CR-6 (1.0: small effects are signed), CR-9 | as C-32 | A-1, A-25 |
| C-34 | `other_borrowers` | `interest_rate` (Tarnesse loan market) | ambiguous | short | CR-8a, CR-6 (1.0), OC-8, CR-12b | loans: licensees and the Treasury borrow in the same market | A-26, A-27 |
| C-35 | `taxpayers`, recipients of other spending, future taxpayers | `resources_available_other_uses` | at_least_one_increase | short to medium | CR-8b, CR-8d, OC-1 (1.0), CR-8 (1.0) | general budget | A-1 |

**Price of mobile capacity (C-19).** The band adds spectrum, an input to capacity, and with A-4 it is used where busy-hour capacity is tight. Added supply at the old price leaves sellers wishing to sell more capacity than buyers take, so the price per GB at a given speed falls (RS-13, CR-6), provided the licensees compete rather than hold prices (A-15). RS-16's 1.0 note applies to how it is signed: per unit of a given quality (a GB at a given speed), so that a shift toward faster plans is not counted as a price change. Two possible opposing chains were checked. (1) The auction price and the build-out cost are costs fixed per firm and give no unit-price chain (CR-4, 0.8; section 4). (2) A smaller operator that wins little of the band may exit or merge, and fewer networks could raise the price. That chain is derivable but needs a premise the case does not support (A-16, p = 0.3), so by CR-12's 0.8 note (kind 2) the derived sign is reported and the chain is recorded in section 10. CR-12e's response argument was not used to bound the price: the incumbents' responses (less densification, C-10; a possible merger) are responses to the new capacity, but mobile networks have large costs fixed per network, so by CR-12's 1.0 note a contraction can restore equal yields at a higher price; the argument would need a constant-cost premise that does not hold here.

**Incumbents' assets (C-20, C-21).** The existing licenses are worth what the capacity they provide is expected to earn until 2035 and at renewal. Added capacity in a substitute band lowers that yield (RS-13, CR-7c), from when the award became expected (CR-10c; A-28: partly at the March 2026 consultation, the rest when the Regulations were made). The operators' shares combine that fall and the fall from possible entry (C-16) with the gain on blocks they win at a price below their own value (A-17: the cap holds the clearing price below some operators' values for their two blocks). No premise ranks them: `ambiguous` (C-21; CR-12b). An operator that wins no block bears only the losses.

**Fixed broadband (C-22 to C-24).** Linmark's fixed wireless offers outside its fibre footprint, and the operators' "home internet" plans in the band, are substitutes for DSL (A-18). DSL lines fall (C-22; RS-16 mirror case), and since the copper network is sunk and cannot contract at once (A-19), its price per line of a given speed falls (C-23; CR-6, 0.9). Pellow's network loses value from when the award became expected (C-24).

**Sites, towers and riggers (C-25 to C-30).** The build-out raises demand for sites and installation work, more so because K2 requires building beyond the cities (A-8). Sites cannot be added at an unchanged cost per site within the period: permits take 4 to 9 months and the riggers are already busy (A-20); so lease rates rise (C-25) and tower portfolios gain value when the award becomes expected (C-26). New towers are built in response (C-27). The response argument (CR-12e) says that new towers drawn by higher lease rates cannot push rates back below their old level; CR-12's 1.0 note says what it needs. The total it bounds is all sites available to networks (existing and new together). The cost premise is that cost per site does not fall as building expands in the period (A-20: permits and riggers are scarcer, not cheaper, as more is built). The response is partial because towers take months to permit and build. With those premises the sign is `increase` (CR-12, 0.9 and 1.0). Riggers' pay rises (C-28) because certification takes 6 to 12 months (A-22; CR-6, 0.9: the split goes to price while supply cannot expand), and their number rises in the medium run as more are trained (C-29; A-23). The riggers and sites the build-out takes are not available to other projects, which install less in 2028 to 2032 (C-30; CR-8a, RS-13 1.0).

**Other projects after the deadline (C-31).** Projects delayed by the shortage of riggers are done after 2032 (A-24): a timing shift of work that happens with and without the policy, so the later window is signed against the counterfactual (02_ontology.md, 2.5), with an increase from catch-up. But fixed wireless competes with fibre outside the cities, which lowers the return on some fibre builds that would otherwise have gone ahead (A-18; CR-9). The two chains oppose: `ambiguous` (CR-12b). In the earlier window both push down (C-30).

**Equipment (C-32, C-33).** Equipment is imported; Tarnesse's orders rise from none in this band (C-32). Tarnesse buys about 0.4% of the world's radio equipment, so its added orders raise the world price by a small amount, where vendors' supply cannot expand at an unchanged cost at once (A-25). By CR-6's 1.0 note the sign is recorded even though the effect may be small (C-33); its size goes in the evidence column.

**Loans (C-34).** Licensees borrow part of what they pay and build (A-27): more demand for loans in Tarnesse's market at the old rate pushes the rate up for other borrowers (CR-8a, CR-6). The receipts let the Treasury borrow less than its M2 billion a year (A-26), which pushes the rate down (OC-8 in reverse). Each effect may be small; each is signed (CR-6, 1.0). They oppose, and no premise ranks them: `ambiguous` (C-34; CR-12b).

**The general budget (C-35).** The receipts go to the Consolidated Fund (K4). CR-8b gives that someone receives them; CR-8d and CR-8's 0.7 note on payers from a general budget, read in reverse, give the recipients as a group: taxpayers (taxes lower than otherwise), recipients of other spending (more spending), or future taxpayers (less borrowing). The TCA's added costs come out of the same budget, so OC-1 and CR-8's 1.0 note apply: the receipts (C-1) and the outlay (C-37) are two items of the budget, and the net (C-38) is a separate consequence, signed by arithmetic (M600 million or more against M9 million plus M2 million a year). The group's sign follows the net: `at_least_one_increase` (C-35).

Stopping points. The currency link (CR-9): more equipment imports give foreigners more marks to buy Tarnesse's exports, while licensees' payments reduce their other spending, some of it on imports; no premise ranks these, and the chain is diffuse at depth 3, so it is stopped. The spending of riggers and tower owners, and of the group in C-35: diffuse, depth 3 to 4; stopped. What licensees give up to pay (C-36) is not followed to named uses: which uses fall needs a premise (CR-4, a change in means alone). Proximity effects of new towers on neighbors (CR-9, 0.7, Tier C) and health effects: out of scope.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `mobile_customers.urban`, `quality_adjusted_price`, medium | An operator exits or merges (A-16, p = 0.3). | Added capacity in the band (A-4, A-15). | CR-12 0.8, kind 2: the opposing chain's premise is below the cut-off. Response argument not used (fixed costs per network, CR-12 1.0). Auction price and build-out are fixed costs per firm (CR-4, 0.8): no chain. | **decrease** (C-19) |
| `owners.incumbents`, `asset_value` (shares), short | Blocks won below the operator's own value (A-17). | Existing licenses lose value (C-20); entry (C-16). | None | **ambiguous** (C-21) |
| `tower_owners`, `net_price_received`, short to medium | More sites demanded (A-3, A-8). | New towers built in response. | CR-12e response argument, with its 1.0 premises: the total of sites; cost per site not falling as building expands (A-20); partial response (permits, riggers). | **increase** (C-25) |
| `other_projects`, `quantity_supplied`, 2033 onward | Delayed projects done later (A-24). | Fixed wireless lowers the return on some fibre builds (A-18). | None | **ambiguous** (C-31) |
| `other_borrowers`, `interest_rate`, short | Licensees borrow (A-27). | Treasury borrows less (A-26). | None | **ambiguous** (C-34) |
| General budget: receipts and TCA costs, short to long | Receipts (C-1). | TCA costs (C-37). | Arithmetic on the case's figures (CR-12e): M600 million or more against M9 million and M2 million a year. | Net **increase** (C-38); the group, **at_least_one_increase** (C-35). |
| Split of the band's value between the state and the licensees | — | — | No variable; CR-5 gives each winner's excess as non-negative by its own ranking at bidding. | Not signed as a share ((d) 1). |

**Not consequences: comparisons with another policy.** Three conclusions that patterns give as written compare the policy with a variant of itself, not with no policy (CR-12, 1.0). They are recorded here so that a reader does not take them as consequences. (1) PC-17: the obligation lowers bids compared with an auction without it, moving part of the band's value from the state's receipts to the towns' service. Against no band, receipts and service both rise. (2) RS-17: the cap lowers the value of operators' growth beyond two blocks compared with no cap; against no band, nothing is lost. (3) U1: readings differ in how much is resold and how much the licenses are worth, but against no band most signs are the same under both readings (C-2, C-3, C-11, C-17); only transfers and their substitutes differ in sign (C-12 to C-14).

**Final check** (`03_workflow.md`).
1. Uncombined chains: every key with opposing chains is in the table above; C-30 and C-31 are separate windows, not combined (CR-12g).
2. Group signs: the budget's beneficiaries are a group (C-35). Riggers' wage and employment are signed separately, each with its supply premise (CR-6, 0.9).
3. Baseline: every sign is against no band. PC-17's "other terms", RS-17's value clause and EN-13's fall in users were each re-signed (above; C-17).
4. Worse off is not poorer: `resources_available_other_uses` is signed for licensees, who pay (C-36), and for the budget's group (C-35). Losing bidders are not signed: the auction takes nothing from them that they had without it.
5. Timing shifts: other projects are signed per window (C-30, C-31); the bunching of the build-out before the deadline is a path note (section 8), since there is no building in the band without the policy.
6. Both sides of every transfer: licensees pay (C-36) and the Treasury receives (C-1); the TCA's costs (C-37) and the net (C-38); the group (C-35).
7. Every actor class, every core rule: CR-7c for licenses in both bands, shares, towers and copper; CR-6 for sites, riggers, DSL and equipment; enforcement costs and compliance costs recorded (C-7, C-37, C-39).
8. Unstated premises: the organizing premise for lobbying (A-13), the margins for each response (A-5 to A-12), the cost premise for the response argument (A-20).
9. Baseline of every pattern: as in item 3. EN-12 is not cited for a consequence (its conditions are not met). OC-8 is used in reverse for the Treasury's borrowing. RS-16 is used in its mirror case with its 1.0 per-quality clause.

## 8. Time structure

- **March 2026 to March 2027: the release becomes likely.** Values move part of the way at the consultation and the rest when the Regulations are made (CR-7c, "becomes expected is a matter of probability"; A-28): incumbents' existing licenses and Pellow's copper fall (C-20, C-24), tower portfolios rise (C-26).
- **March to October 2027: the auction.** Bidders spend on preparation (C-7); receipts are paid (C-1). The financial investor's participation depends on U1 (C-14).
- **2028 to 2032: build-out.** Licensees build in the cities first, where the band earns most, and in the towns as the deadline nears: building is bunched toward the end of 2032. This is a path note: without the policy no building in the band would take place at all, so no window is signed as a decrease (02_ontology.md, 2.5; CR-12h). Riggers' pay and tower lease rates are highest in this window (C-25, C-28); other projects are delayed (C-30). Under U1-a, licenses change hands; under U1-b, companies or capacity do (C-12, C-13). Lobbying on an extension peaks before the deadline (C-15).
- **End of 2032: the deadline.** A licensee that has not met the obligation loses its license without refund (C-11). The band then reverts to the TCA, which may re-auction it: further receipts are contingent on a revocation (A-30, p = 0.3, below the cut-off; CR-8 0.8, contingent payers, read for receipts). Transfers become possible under both readings.
- **2033 onward.** Delayed projects resume (C-31). Mobile prices per GB stay lower while the band is in use (C-19). In 2035 the operators' existing licenses expire; their renewal value is lower than it would have been (C-20).
- **Toward 2042.** With no right of renewal, licensees' investment in the band falls in the last years of the term. Against the counterfactual there is no investment in the band at all, so this is a path note, not a decrease (CR-10a).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-36 | `licensees` | `resources_available_other_uses` (money) | decrease | The M600 million or more paid for licenses, which licensees would otherwise have invested elsewhere, paid out or kept. Which uses fall is not signed (CR-4, a change in means alone). | OC-1, CR-8a, CR-3 |
| C-37 | `officials.enforcement` (TCA) | `enforcement_cost` | increase | M9 million for the auction and M2 million a year for monitoring, from the general budget. | OC-3, CR-8c |
| C-38 | `treasury` | `non_tax_receipts` (net of the TCA's added costs) | increase | — (the net of two budget items). | CR-8 (1.0), OC-1 (1.0), CR-12e |
| C-39 | `licensees` | `compliance_cost` (coverage maps, drive tests, reporting) | increase | Staff time and testing used only to prove coverage. | OC-2, CR-8c |

The resources used in the build-out itself (equipment, riggers, sites) are withdrawn from other uses (CR-8a): for riggers and sites that is C-30; for the money, C-36. Bidders' preparation is C-7. Losing bidders lose what they spent preparing (C-7) and nothing else against the counterfactual. Prevented exchanges (OC-4): none; the Regulations prevent no exchange that would otherwise take place, since the band cannot be used without them.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Some blocks are bid at or above the reserve: bidders expect a license to be worth more than M40 million after the build-out cost. | binding | 0.95 | Five qualified bidders; the consultant's valuation of M100 million to M200 million a block. | Nothing follows; the band stays unused. |
| A-3 | The obligation is enforced: revocation is credible, so licensees build to 90% by the end of 2032. | enforcement | 0.75 | Regulations' text; the TCA's record on earlier coverage conditions. | C-5 is not reported; C-3, C-25 to C-30 shrink to the commercial build. |
| A-4 | The band is used to add capacity where busy-hour demand presses on existing capacity. | other | 0.85 | Traffic growth about 30% a year; city congestion. | C-4, C-19, C-20 are not reported. |
| A-5 | Some bidders or holders use stakes or joint ventures below the affiliate line. | other | 0.55 | Control-based affiliate test; practice in other awards. | C-8 is not reported. |
| A-6 | Some licensees pool blocks by network-sharing agreements. | other | 0.6 | Existing sharing in the old bands; contiguous spectrum is worth more. | C-9 is not reported. |
| A-7 | Without the band, operators would densify sites in the existing bands; with it, they densify less. | substitutability | 0.75 | Operators' capacity plans; cost per unit of capacity from spectrum and from sites. | C-10 is not reported. |
| A-8 | Licensees would not, on their own, cover 90% of the population with the band by 2032 (about 65% commercially). | binding | 0.8 | Consultation responses; site counts. | C-11 is not reported; K2 adds nothing to the commercial build. |
| A-9 | Some licensees overstate coverage, meet it by minimal sites, or miss the deadline. | enforcement | 0.55 | Drive-test sampling; cost of the last sites. | C-11 is not reported. |
| A-10 | After the auction, some licensees value their licenses less than others would (an entrant cannot finance the build-out, or values change). | other | 0.6 | Entrants' financing; five years is long. | C-12 and C-13 are not reported. |
| A-11 | Under U1-b, sales of licensee companies or long capacity leases are not treated as transfers. | enforcement | 0.55 | Reg. 14 speaks of transfer of the license; no rule on change of control. | C-13 under U1-b is not reported. |
| A-12 | Some investors without networks bid only if they can resell before the deadline. | other | 0.55 | One investor registered interest. | C-14 is not reported. |
| A-13 | Licensees, entrants and town councils can organize to lobby at a cost below their stakes. | other | 0.85 | Existing industry associations; councils' coverage campaigns. | C-15 is not reported. |
| A-14 | At least one of Linmark and Ombra wins blocks and builds a network. | other | 0.6 | Demand at the reserve of ten blocks for six; the cap; entrants' stated plans. | C-16, C-18, C-22 to C-24 are not reported; C-21 and C-31 lose a chain. |
| A-15 | Licensees compete on price; no network leaves the market because of the award in the medium run. | other | 0.7 | Three operators with active price competition; entry. | C-19 and C-20 are not reported. |
| A-16 | Kostel exits or merges because it wins too little of the band. | other | 0.3 | Kostel's share and finances. | Below the cut-off: C-19 stays `decrease`; if true, C-19 is `ambiguous` (CR-12, 0.8, kind 2). |
| A-17 | Some operators win blocks at prices below their own value for them (the cap holds the clearing price at the third-highest bidder's value). | other | 0.6 | Auction structure; operators' higher values for busy-hour capacity. | C-21 becomes `decrease` (only the losses remain). |
| A-18 | Fixed wireless in the band substitutes for DSL for some households outside fibre areas. | substitutability | 0.7 | 700,000 households on DSL outside fibre and cable; Linmark's plans. | C-18, C-22 to C-24 are not reported; C-31 loses its (−) chain and becomes `increase` with A-24. |
| A-19 | Pellow's copper network cannot be withdrawn or its costs cut at once. | durability | 0.8 | Sunk copper plant. | C-23 shrinks; the shift goes to quantity. |
| A-20 | Sites cannot be added at an unchanged cost per site in the period, and cost per site does not fall as building expands (permits 4 to 9 months; riggers scarce). | durability | 0.8 | Permit times; rigger numbers against the projected 4,000 to 5,000 installations a year. | C-25 and C-26 shrink; C-25's response argument gives only "not below the old level". |
| A-22 | Riggers cannot be added at once (certification takes 6 to 12 months). | durability | 0.75 | Training and certification rules. | C-28 and C-30 shrink. |
| A-23 | Some new riggers are trained or move from other work in the medium run. | mobility | 0.8 | Training places; related trades. | C-29 is not reported. |
| A-24 | Some projects delayed by the shortage are done after 2032 rather than cancelled. | other | 0.6 | Fibre builders' plans run beyond 2032. | C-31 becomes `decrease`. |
| A-25 | Equipment vendors' supply cannot expand at an unchanged cost at once. | durability | 0.6 | Order books; lead times. | C-33 is not reported. |
| A-26 | The Treasury borrows less than it would have, by part of the receipts. | revenue_use | 0.6 | Annual borrowing about M2 billion; finance ministry statements. | C-34 becomes `increase`. |
| A-27 | Licensees borrow part of what they pay and build in Tarnesse's loan market. | other | 0.7 | Operators' debt; entrants' financing. | C-34 becomes `decrease` with A-26. |
| A-28 | Investors expected the award partly from the March 2026 consultation and fully from 1 March 2027. | expectations | 0.8 | Market commentary; share prices. | C-20, C-21, C-24, C-26 move later. |
| A-30 | A license is revoked and the band re-auctioned. | other | 0.3 | Licensees' finances; lobbying for extension. | Below the cut-off: contingent re-auction receipts are not reported. |

## 11. Report

**The policy.** Tarnesse auctions six national licenses of 20 MHz each in a radio band nobody may use today. Licenses run for 15 years from 2028. Each licensee must cover 90% of the population with the band by the end of 2032, or lose the license without refund. No one may hold more than two blocks. The payments go to the general budget. It is unclear whether a license may be sold before the coverage deadline.

**Visible consequences.** The state is paid (C-1), net of the regulator's costs (C-38), and the general budget's beneficiaries gain as a group (C-35). Licensees hold valuable licenses (C-2) and build networks in the band (C-3). City customers get more capacity (C-4), and towns get service in the band because the obligation requires it (C-5).

**Invisible consequences.**
- *Who keeps the band's value.* The price goes to the state; each winner keeps any excess of its own value over the price. No one receives any of it by history. The auction payment is a cost fixed per firm and is not passed on in the price per GB by any chain the method derives.
- *Licensees.* They pay (C-36), spend on proving coverage (C-39), use the band in place of some densification (C-10), use stakes below the affiliate line (C-8) and network sharing (C-9), and some fall short of or game the obligation (C-11).
- *Customers and rivals.* The price per GB falls (C-19). Fixed wireless takes DSL customers (C-18, C-22), and DSL prices per line fall (C-23). An entrant adds a network (C-16), and the number of users of the band rises from none (C-17).
- *Asset owners.* Incumbents' existing licenses lose value (C-20); their shares may rise or fall (C-21). Pellow's copper loses value (C-24). Tower owners gain (C-26) and charge more for sites (C-25), and build more towers (C-27).
- *Inputs.* Riggers are paid more (C-28) and more are employed (C-29); other projects install less until 2032 (C-30), and after it may install more or less (C-31). Equipment vendors sell more (C-32), and the world price of radio equipment rises by a small amount (C-33). The interest rate for other borrowers may rise or fall (C-34).
- *Process.* Bidders spend on preparing (C-7); the regulator's costs rise (C-37); lobbying grows on the deadline, waivers, U1 and the cap (C-15).

**Per reading of U1.** If licenses can be sold before the deadline (U1-a), some are (C-12), and investors without networks bid to resell (C-14). If they cannot (U1-b), no license changes hands before 2033, and the same pressure goes to sales of the companies that hold them and to long leases of capacity (C-13). Against the counterfactual of no band, every other sign is the same under both readings.

**Ambiguous effects.** Incumbents' share values (C-21); other projects after 2032 (C-31); other borrowers' interest rate (C-34).

**Key conditions.** That the obligation is enforced (A-3, p = 0.75); that the band adds capacity where it is needed and licensees compete (A-4, A-15); that an entrant wins and builds (A-14, p = 0.6); that sites and riggers cannot be added at once (A-20, A-22).

**What this analysis cannot say.** How much the state receives and how much licensees keep; whether a different design (no cap, no obligation, an auction with a resale rule) would have raised more or covered more, since those are comparisons between policies; how large any price change is; whether the policy is desirable; health and visual effects (out of scope).

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | treasury | non_tax_receipts (auction payments) | increase | short | visible | B | CR-5c, CR-8b | A-1 |
| C-2 | licensees | asset_value (licenses in the band) | increase | short | visible | B | CR-7c, CR-10c, SB-4, CR-7 | A-1 |
| C-3 | licensees | investment_target (network in the band) | increase | short–medium | visible | B | CR-1, CR-4, PC-17 | A-1, A-3 |
| C-4 | mobile_customers.urban | quality_per_unit (busy-hour capacity) | increase | medium | visible | B | CR-9, LW-10 | A-1, A-4 |
| C-5 | customers.towns | quality_per_unit (service in the band) | increase | medium | visible | B | PC-17, CR-1 | A-3 |
| C-6 | bidders | applications (qualified bidders) | increase | short | invisible | B | CR-4 | A-1 |
| C-7 | bidders | compliance_cost (auction preparation) | increase | short | invisible | B | OC-2, CR-8c | A-1 |
| C-8 | bidders, licensees | reclassification (stakes and joint ventures below the affiliate line) | increase | short–medium | invisible | B | RS-17, RS-5, CR-4 | A-5 |
| C-9 | licensees | term_prevalence (network sharing of band blocks) | increase | medium | invisible | B | RS-17, CR-4, CR-5 | A-6 |
| C-10 | licensees | investment_target (densification in existing bands) | decrease | medium | invisible | B | CR-4, CR-9, LW-10 | A-1, A-7 |
| C-11 | licensees | legal_breach (coverage overstated, letter-only sites, deadline missed) | increase | medium | invisible | B | RS-3, RS-5, CR-4 | A-8, A-9 |
| C-12 | licensees | quantity_traded (license transfers before end-2032) | U1-a: increase; U1-b: no_change | medium | invisible | B | CR-1, CR-5a, EN-13 | A-10 |
| C-13 | licensees | reclassification (company sales and capacity leases in place of transfers, before end-2032) | U1-a: no_change; U1-b: increase | medium | invisible | B | RS-5, CR-4 | A-10, A-11 |
| C-14 | bidders.financial | applications (bidders who plan to resell) | U1-a: increase; U1-b: no_change | short | invisible | B | CR-4, CR-10a | A-12 |
| C-15 | lobbying groups | lobbying_effort (questions that exist only under the Regulations) | increase | medium | invisible | B | RS-7, CR-4, CR-12 | A-13 |
| C-16 | entrants | number_of_sellers (wireless broadband networks) | increase | medium | invisible | B | CR-1, CR-4, RS-17 | A-14 |
| C-17 | licensees | number_of_sellers (users of the band) | increase | medium | invisible | B | EN-13, CR-1 | A-1 |
| C-18 | entrants | quantity_supplied (fixed wireless lines) | increase | medium | invisible | B | CR-4, CR-9 | A-14, A-18 |
| C-19 | mobile_customers.urban | quality_adjusted_price (per GB at a given speed) | decrease | medium | invisible | B | RS-13, CR-6, CR-9, CR-12 | A-4, A-15 |
| C-20 | owners.incumbents | asset_value (licenses in existing bands) | decrease | short | invisible | B | RS-13, CR-7c, CR-10c | A-4, A-15, A-28 |
| C-21 | owners.incumbents | asset_value (operators' shares) | ambiguous | short | invisible | B | CR-7c, CR-10c, CR-5, CR-12b | A-14, A-15, A-17, A-28 |
| C-22 | fixed_broadband_sellers | quantity_traded (DSL lines outside fibre areas) | decrease | medium | invisible | B | RS-16, CR-9 | A-14, A-18 |
| C-23 | fixed_broadband_sellers | price_substitute (DSL per line of a given speed) | decrease | medium | invisible | B | RS-16, CR-6 | A-14, A-18, A-19 |
| C-24 | owners.copper | asset_value (copper network) | decrease | short–medium | invisible | B | CR-7c, CR-10c | A-14, A-18, A-28 |
| C-25 | tower_owners | net_price_received (site lease rates) | increase | short–medium | invisible | B | CR-9, CR-6, CR-12e | A-3, A-20 |
| C-26 | tower_owners | asset_value (towers and sites) | increase | short | invisible | B | CR-7c, CR-10c, SB-4 | A-3, A-20, A-28 |
| C-27 | tower_owners | quantity_supplied (new towers) | increase | medium | invisible | B | CR-4, CR-7a, CR-6 | A-3, A-20 |
| C-28 | riggers | wage_rate | increase | short–medium | invisible | B | CR-9, LW-10, CR-6 | A-3, A-22 |
| C-29 | riggers | employment | increase | medium | invisible | B | CR-9, LW-10, CR-7a | A-3, A-23 |
| C-30 | other_projects | quantity_supplied (installations, 2028–2032) | decrease | short–medium | invisible | B | CR-8a, RS-13, CR-6 | A-3, A-22 |
| C-31 | other_projects | quantity_supplied (installations, 2033 onward) | ambiguous | medium–long | invisible | B | RS-8, CR-9, CR-12b | A-14, A-18, A-24 |
| C-32 | equipment_vendors | quantity_traded (radio equipment to Tarnesse) | increase | short–medium | invisible | B | CR-9, LW-10 | A-1 |
| C-33 | buyers.foreign | price_paid (radio equipment, world; small) | increase | short | invisible | B | CR-6, CR-9 | A-1, A-25 |
| C-34 | other_borrowers | interest_rate | ambiguous | short | invisible | B | CR-8a, CR-6, OC-8, CR-12b | A-26, A-27 |
| C-35 | taxpayers, recipients of other spending, future taxpayers | resources_available_other_uses | at_least_one_increase | short–medium | invisible | B | CR-8b, CR-8d, OC-1, CR-8 | A-1 |
| C-36 | licensees | resources_available_other_uses (money) | decrease | short | invisible | B | OC-1, CR-8a, CR-3 | A-1 |
| C-37 | officials.enforcement (TCA) | enforcement_cost | increase | short–long | invisible | A | OC-3, CR-8c | none |
| C-38 | treasury | non_tax_receipts (net of TCA costs) | increase | short–long | visible | B | CR-8, OC-1, CR-12e | A-1 |
| C-39 | licensees | compliance_cost (coverage proof) | increase | medium | invisible | A | OC-2, CR-8c | none |

## Gaps found

**(a) Calculus gaps (a step no core rule covers).** None. Every step was derived from CR-1 to CR-12. Proximity effects of new towers would be the open GAP-026-1 (Tier C, Q20); they were not followed.

**(b) Unclear core rules.**
1. *CR-7c, an asset created and sold by the state.* CR-7c says the value of a created asset "is captured by whoever receives it at creation". With an auction the recipient pays, and by CR-5c and CR-8b the state captures the price and the recipient only the excess of its own value over the price. The rule is right for free allocation (EN-12) and literally wrong for a sale. It needed CR-5 and CR-8b to give the split. A sentence is needed: "where the right is sold at creation, the seller captures the price and the buyer the excess of its value over the price; an auction sets the price at the value of the bidders who drop out."
2. *CR-1, recording against a counterfactual law that forbids the act.* Because the Radio Act forbids use of the band without a license, the Regulations remove no option from anyone. CR-1's recording note ("state the counterfactual law") settled this, but a consequence of it was not obvious: losing bidders are not worse off by the band itself (CR-3b), only through what winners do with it (CR-9).
3. *CR-8 0.8, contingent payers, read for receipts.* Re-auction receipts after a revocation are contingent on a breach. The clause speaks of payers; it was read for a contingent receipt, which seems right but is not stated.
4. *CR-12 1.0, what the response argument needs, in an input market.* For site lease rates (C-25) the 1.0 note was written for a contraction ("cost per unit does not fall as the activity contracts"). Here the response is an expansion (new towers), and the needed premise is the mirror: cost per site does not fall as building expands. Worked with that reading; the note could state both directions.

**(c) Missing or wrong patterns.**
1. *PC-17, a term in a right the state creates.* Its preconditions are met (the term is required in every license; it is absent from what licensees would choose for coverage beyond 65%). Its conclusion that "the other terms adjust" compares the license with the term against the same license without it: another policy. Against no policy there is no license, so the conclusion had to be re-signed: the term's consequences are what is built, its breach and its pull on inputs, and the lower bids show only as a comparison between designs (section 7). PC-17 needs a clause: "where the contract exists only under the policy, the adjustment of other terms is a comparison between policies; against the counterfactual, sign what the term causes to be done."
2. *RS-17, a cap on holdings.* Applied as written, its third conclusion (the value of growing past the threshold falls, CR-7c) would have given a decrease in operators' value from the cap. That compares with an auction without the cap. Against no band, the cap takes nothing away. I overrode it (no consequence). Its splitting conclusion worked (C-8). RS-17 is written for a burden above a line; a cap is a prohibition above the line, which its notch and kink note does not name.
3. *EN-13 on a resource with no users without the policy.* Its main conclusion ("number of sellers using the right decreases") and its 1.0 baseline note both presume users in the counterfactual. Here the number rises from none (C-17); transfers reduce it only against the first allocation. Overrode the main conclusion as written.
4. *EN-12 has no counterpart for allocation by auction.* EN-12 covers allocation by history and, in one sentence, by lottery. A pattern for allocation by sale would say: no windfall and no race; the state captures the price; a cap or set-aside on bidders changes who wins and the clearing price; costs paid for the right are fixed per firm (CR-4, 0.8) and not passed into unit prices without a premise on entry and exit.
5. No other pattern gave a sign I had to override.

**(d) Vocabulary.**
1. No variable for the share of a created right's value captured by the state against its recipients. `subsidy_share_received` and `tax_share_borne` are for subsidies and taxes. A `rent_share_captured` (signed for one party relative to the other) would let the brief's question be scored.
2. No variable for the coverage of a network (population reached); `quality_per_unit` with a qualifier was used (C-5).
3. No actor class for the state as a receiver of non-tax payments; `treasury` was coined.
4. The instrument list has `rights_allocation` "by history, auction or lottery" but the rule families listed for it (SB-4, CR-7c, EN-12) cover only history; no pattern covers the auction case ((c) 4).

**(e) Test of 1.0.**
- *EN-12 (auction rather than history).* Worked as written in the sense that its preconditions were not met and it was not applied; TS-5 1.0 (lines fixed before announcement) likewise not needed, since there is no history to race for. But nothing in the catalog took its place ((c) 4), and CR-7c's capture clause needed CR-5 and CR-8b ((b) 1).
- *EN-13 1.0, baseline.* Needed interpretation: the note assumes the resource had users without the policy. With none, the number of users rises from zero (C-17); its "blocked entry" clause has nothing to apply to ((c) 3).
- *PC-17 (the build-out obligation).* Failed as written on its "other terms adjust" conclusion, which compares with the license without the term ((c) 1); re-signed under CR-12 1.0. Its binding premise (A-8) and its enforcement premise (A-3) worked.
- *CR-7c, capitalization and who captures the rent.* Worked as written for existing assets (incumbents' licenses C-20, copper C-24, towers C-26) and for the timing of capitalization by probability (A-28). Needed interpretation for the created right ((b) 1).
- *RS-17 1.0 (the per-bidder cap).* Needed interpretation: splitting below the affiliate line worked (C-8); the value clause compared with no cap and was overridden ((c) 2); the 1.0 notch/kink note does not cover a prohibition above the line.
- *OC-1 1.0 and CR-8 1.0, receipts into the same budget.* Worked as written: receipts (C-1) and the TCA's costs (C-37) recorded as two items, the net (C-38) by arithmetic, and the group (C-35) from the net.
- *CR-6 1.0, small effects are signed.* Worked as written for the world price of radio equipment (C-33) and the interest rate (C-34), where the small effect had an opposing chain and the sign is `ambiguous`.
- *CR-12 1.0, what the response argument needs.* Worked: it gave `increase` for site lease rates with the total, the cost premise and the partial response stated (C-25), with the direction of the cost premise read as its mirror ((b) 4). It also correctly stopped me from using the argument for the price per GB, where networks have large fixed costs (C-19).
- *CR-12 1.0, the baseline of patterns.* Worked, and was the most used 1.0 change: it caught PC-17, RS-17 and EN-13 comparing with something other than no policy.
- *CR-12 0.8, kind 2 below the cut-off.* Worked as written for the exit of a smaller operator (A-16, C-19).
- *CR-4 0.8, a cost fixed per firm.* Worked as written: the auction price and the build-out cost give no chain to unit prices (section 4).
- *RS-16 1.0, per unit of quality.* Worked as written in its mirror case for DSL (C-23), signed per line of a given speed.
- *CR-4 1.0 and RS-7 1.0, lobbying against a contested counterfactual.* Worked as written: lobbying on release is not signed; questions that exist only under the Regulations are (C-15).
- *Readings against the counterfactual (02_ontology.md, 2.5).* Most U1 differences vanished against no band: under both readings licenses are worth something, are built on and are breached. Only transfers and their substitutes differ in sign (C-12 to C-14). Not a failure, but worth recording: readings that differ in degree give the same sign.
- *Candidates from 06_gaps.md, 6.2e.* None needed. "Public entry at a set price against sunk incumbents" resembles C-23 (fixed wireless against sunk copper) but the entrant is private and prices freely; RS-16's mirror case covered it.
