# WE-004 / Analysis: Storm-window replacement funded by a household levy (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

Rule set: the core rules CR-1 to CR-12 (`../04a_core_rules.md`), AX-1 and LW-1 to LW-10 (`../01_foundations.md`), and arithmetic. No pattern is cited. New premises that the derivations needed are numbered A-N1, A-N2, ... and are listed in section 10 and under "Gaps found".

## 1. Policy record

**Brackwater Storefront Recovery Program.** Brackwater is a coastal town of about 40,000 people in 16,000 households. On 3 March a windstorm broke about 600 ground-floor shop windows in the town center, and many home windows. The storm happens in both worlds: the counterfactual is "the same storm, and no program". About 70% of the damaged shops carry property insurance that covers glass, with a $500 deductible; most of the insurers are based outside the town. Four local glazing firms employ about 40 glaziers; the nearest other glaziers are 90 minutes away. The council debated the program in public from 6 March and adopted it on 14 March. Its supporters said it would "put 40 glaziers to work for two months, and their wages will be spent in our shops".

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Levy | `lump_sum_tax` | Households | Every household water account holder | $80 per household, once, on the April water bill, due within 60 days. Unpaid levies are added to water arrears and, for owners, become a lien on the property. Total about $1.28 million. | None |
| K2 Replacement program | In-kind transfer (`lump_sum_subsidy`) | Ground-floor commercial windows broken by the storm and not permanently replaced by 14 March | Town | The town hires the four local firms under emergency contracts at a fixed schedule (about $2,000 per window on average) and replaces every eligible window at no charge to the owner. Owners apply within 30 days with photos; a town inspector verifies. | Home windows; windows already permanently replaced by 14 March (no reimbursement). |
| K3 Administration | Enforcement | K1, K2 | Town finance office and building inspector | Billing, collection, inspection of claims, contract management; funded from the general budget. | None |

Revenue use: all levy revenue pays for K2. The town advances the money from its cash reserve in March and repays the reserve from the levy; any surplus goes to the general fund. The council resolution calls the program "a one-time response to an exceptional storm".

Unclear provisions: whether the town, or the shop owners' insurers, can recover the cost of replaced windows from each other (subrogation). The resolution is silent; assumed that insurers simply pay no claim for windows the town replaced (A-5).

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
| --- | --- | --- | --- |
| K1 Levy | binary (forced payment from households to the town) | Yes: a fixed sum that no behavior avoids (only late payment, with arrears or a lien) | CR-1, CR-8, CR-9 |
| K2 Replacement program | binary (in-kind transfer from the town to shop owners); the town buys from glaziers at a fixed schedule | Yes for eligible windows (A-1) | CR-1, CR-3b, CR-4, CR-5c, CR-6, CR-9, CR-10a |
| K3 Administration | binary (general budget) | Yes | CR-1, CR-8c |

**CR-1 operations, by component and actor class.** Operation 1: removes an option; 2: adds an option; 3: changes what an option brings; 4: transfers means.

| Component | Actor class | CR-1 operations |
| --- | --- | --- |
| K1 | taxpayers.households | 4 ($80 per household transferred to the town); 3 (arrears or a lien attached to not paying) |
| K2 | shop_owners.damaged (eligible windows) | 2 (free replacement added); 4 (in-kind transfer of a window worth about $2,000) |
| K2 | shop_owners.replaced_early (replaced by 14 March) | none (no reimbursement) |
| K2 | glaziers (four local firms) | 2 (emergency contracts at a fixed schedule) |
| K2 | insurers (mostly outside the town) | none directly; their contracts with shop owners change in effect (CR-9; A-5, reading U1) |
| K2 | homeowners.damaged | none directly (home windows exempt); compete for the same glaziers (CR-9) |
| K3 | taxpayers.general_budget | 4 (administration funded from the general budget) |
| K3 | officials.enforcement (finance office, inspector) | 2 (billing, collection, inspection) |
| K1, K2 | town (cash reserve) | 4 (reserve advanced in March, repaid from the levy) |

## 3. Actor classes

| Actor class | Role | How its options change |
| --- | --- | --- |
| taxpayers.households | 16,000 water account holders | Pay $80 once (K1) |
| shop_owners.damaged | Owners of about 600 broken ground-floor shop windows | Free replacement if not permanently replaced by 14 March (K2) |
| insurers | Insure about 70% of damaged shops for glass, $500 deductible; mostly based outside the town | Pay no claim for windows the town replaces (A-5, U1-a) |
| glaziers | Four local firms, about 40 glaziers; the next firms 90 minutes away | Town contracts at a fixed schedule |
| homeowners.damaged | Households with broken home windows (exempt) | Compete with the program for glaziers' time |
| sellers.local | Brackwater shops selling to residents | Residents' and recipients' spending changes (CR-9) |
| workers (Brackwater retail and services) | Staff of local sellers | Demand for their labor changes (CR-9, input_to) |
| taxpayers.general_budget | Fund administration | Means transferred (K3) |
| town (cash reserve) | Advances the money | Reserve tied up until the levy is collected |
| officials.enforcement | Finance office and building inspector | New duties (K3) |

## 4. Direct effect

CR-1 with CR-2. The counterfactual is the same storm with no program, so the comparison is with the windows owners and insurers would have replaced themselves (A-4).

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-1 | taxpayers.households | resources_available_other_uses | decrease | short | CR-1 (op 4, K1: $80 per household; no behavior avoids it) → CR-8a, CR-8b | none |
| C-2 | shop_owners.damaged | resources_available_other_uses | increase | short | CR-1 (op 2 and op 4, K2) → CR-3b → CR-8b (uninsured owners keep the full cost they would have paid; insured owners keep the $500 deductible; owners who would not have replaced receive a window) | A-1, A-4, A-5 |
| C-3 | glaziers | quantity_supplied (shop windows replaced within the year) | increase | short | CR-1 (op 2, K2) → CR-4 mirror (x: leave the window unreplaced, y: free replacement) for owners who would not have replaced (A-2); plus claims for windows not broken by the storm (A-7) | A-1, A-2 |

## 5. Responses

CR-4 pairs of options examined for each actor class (substitute, adjust terms, evade, relocate, reclassify, exit, lobby, change timing, enter), with CR-6 where a price is fixed and CR-5 where an exchange is prevented or compelled.

| Actor class | Pair of options (CR-4) or rule | Result |
| --- | --- | --- |
| taxpayers.households | CR-4 (x: pay, y: let the levy go to arrears) | Not followed: no premise on non-payment; the levy is a fixed sum, so no other margin exists |
| shop_owners.damaged | CR-10a (x: hire a glazier now at own or insurer's cost, y: wait for the free program) | Some waited after 6 March (A-6) |
| shop_owners.damaged | CR-4 mirror (x: leave a window unreplaced, y: free replacement) | Windows replaced that would not have been (A-2) |
| shop_owners.damaged | CR-4 (x: pay to replace an old window, y: claim it as storm damage) | Some false claims pass (A-7) |
| shop_owners.damaged and homeowners | CR-4 (x: accept a one-time program, y: lobby to extend it) | Some lobby (A-8) |
| shop_owners (all) | CR-10a with CR-4 (x: insure, y: rely on the town after future storms) | A-9, p 0.4: not reported |
| glaziers | CR-4 (x: town contract, y: private jobs) | Capacity is fixed in the short run (A-3); town work displaces other work |
| insurers | CR-4 (x: pay the claim, y: decline it for a window made good by the town) | Decline (A-5; reading U1-a) |
| homeowners.damaged | CR-6 (glaziers' time scarce at the going price) | Higher price or longer wait |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
| --- | --- | --- | --- | --- | --- | --- |
| C-4 | shop_owners.damaged | wait_time (until permanent replacement) | increase | short | CR-10a (program expected from 6 March) → CR-4 (x: hire a glazier now, y: wait for the free program) → the program queue is slower than direct hiring | A-3, A-6 |
| C-5 | shop_owners.damaged | quantity_traded (own sales while boarded up) | decrease | short | C-4 → CR-9 (customers deal less with a boarded shop) | A-3, A-6, A-N1 |
| C-6 | shop_owners.damaged | reclassification (claims for windows not broken by the storm) | increase | short | CR-1 (op 2) → CR-4 (x: pay to replace an old window, y: claim it as storm damage) | A-7 |
| C-7 | shop_owners.damaged and homeowners | lobbying_effort | increase | medium | CR-4 (x: accept a one-time program, y: lobby to extend it to homes or future storms) → CR-8c | A-8 |
| C-8 | officials.enforcement | enforcement_cost | increase | short | CR-1 (op 2, K3: billing, inspection, contract management) → CR-8c | none |
| C-9 | taxpayers.general_budget | resources_available_other_uses | decrease | short | CR-1 (op 4, K3 funded from the general budget) → CR-8a | none |
| C-10 | town (cash reserve) | resources_available_other_uses | decrease | short | CR-1 (op 4: reserve advanced in March, repaid within about 60 days of the April bill) → CR-10 (the means are unavailable for that time) → CR-8a | none |

## 6. Second-order effects

Depth limit 4; diffuse bystander effects pruned after depth 3. Each link names the exchange relation it follows (CR-9).

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C-11 | insurers | resources_available_other_uses | U1-a: increase; U1-b: ambiguous | short | C-2 → CR-9 (the insurance contract: a window the town replaces is a claim not paid) → CR-8b; under U1-b (the town recovers its cost from insurers) the payment is made to the town at the schedule price instead, and the sign depends on that price against the claim cost | the insurance contract (insurer ↔ shop owner) | A-4, A-5 |
| C-12 | homeowners.damaged | price_paid, wait_time (home window replacement) | at_least_one_increase | short | C-3 (more windows to replace with fixed capacity) → CR-9 (the same glaziers serve both) → CR-6 (glaziers' time scarcer; price or queue adjusts) | same_market_other_segment (shop windows ↔ home windows), close | A-2, A-3 |
| C-13 | glaziers | earnings | ambiguous | short | (+) C-3 (extra windows); (+ or −) the fixed schedule of about $2,000 against the price glaziers would have charged after the storm (CR-6, CR-5c); with capacity fixed (A-3), extra town work displaces other work; CR-12b | input_to (glaziers' labor → windows) | A-1, A-2, A-3 |
| C-14 | sellers.local | quantity_traded (sales to Brackwater residents) | U1-a: decrease; U1-b: ambiguous | short | (−) C-1 → CR-9 (households buy from local sellers) with A-N2; (+) C-2 and C-13 → CR-9 (local recipients spend part of their gain locally); CR-12b resolved by CR-8b plus arithmetic: under U1-a the part of the levy retained by insurers (C-11) is spent outside Brackwater (A-10), so local recipients receive less than local payers give, and with A-N3 the net is a decrease; under U1-b that leak is absent and the sign is ambiguous | households and recipients ↔ local shops | A-4, A-5, A-10, A-N2, A-N3 |
| C-15 | workers (Brackwater retail and services) | employment, hours_worked | U1-a: at_least_one_decrease; U1-b: ambiguous | short | C-14 → CR-9 (labor used to make the sales) → LW-10 | input_to (labor → local sales) | A-4, A-5, A-10, A-11, A-N2, A-N3 |

**Where chains were stopped.**

- C-15 is at depth 4 (levy → household spending → local sales → staffing); stopped. The supporters' claim ("their wages will be spent in our shops") is evaluated only to this depth.
- Insurers' spending outside Brackwater (A-10) leaves the analysis at depth 2: no recorded relation ties it back to the town.
- Effects of C-12 on homeowners' own spending are diffuse at depth 3; stopped.

## 7. Combined effects

Keys reached by one chain, or by chains with the same sign, take that sign (CR-12a). Keys where chains conflict:

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance premise | Combined sign |
| --- | --- | --- | --- | --- |
| sellers.local, quantity_traded, short | Recipients (shop owners, glaziers for extra windows) spend part of their gain locally | Households pay $1.28 million and cut some local purchases (A-N2) | U1-a: CR-8b plus arithmetic: the insurers' share leaves town (A-10), so local receipts are smaller than local payments; with similar local spending shares (A-N3) the payers' cut dominates. U1-b: no leak, no dominance | U1-a: decrease; U1-b: ambiguous (C-14) |
| glaziers, earnings, short | Extra windows (A-2, A-7); schedule above the post-storm price, if it is | Schedule below the post-storm price, if it is; displaced private jobs | None | ambiguous (C-13) |
| insurers, resources, short (reading U1-b) | Claims not paid | Cost recovered by the town at the schedule price | None under U1-b | U1-a: increase; U1-b: ambiguous (C-11) |

## 8. Time structure

- **Announcement (CR-10a).** The program was debated in public from 6 March and adopted on 14 March; only windows not permanently replaced by 14 March qualify. Owners who heard the debate had reason to wait, and the program's queue is slower than direct hiring (A-6), so boarded-up time lengthens (C-4, C-5). Owners who replaced early, before the debate, receive nothing; owners who replaced between 6 and 14 March gave up a free window.
- **Glaziers' capacity (CR-10b).** Crews cannot be expanded quickly and outside firms are 90 minutes away (A-3). In the months after the storm, every window the program adds displaces or delays another job, mainly home windows (C-12).
- **Timing of payments.** The town pays glaziers from its reserve in March and households pay from April, within 60 days (C-10, C-1). Local spending is cut when households pay, not when glaziers are paid.
- **Expectations.** The council calls the program one-time; if owners came to expect the town to pay after future storms (A-9, p 0.4), they would insure less. Not reported. Lobbying to extend the program is reported (A-8; C-7).

## 9. Opportunity costs

Each written as a signed change in a variable (CR-3, CR-8).

| ID | Actor class | Variable | Sign | What is given up | Rules |
| --- | --- | --- | --- | --- | --- |
| C-1 | taxpayers.households | resources_available_other_uses | decrease | What 16,000 households would have bought or saved with $80 each, about $1.28 million (the unseen) | CR-8a, CR-8b |
| C-5 | shop_owners.damaged | quantity_traded (own sales while boarded up) | decrease | Sales lost while shops stayed boarded waiting for the program | CR-10a, CR-9 |
| C-7 | shop_owners.damaged and homeowners | lobbying_effort | increase | Time and money spent lobbying (CR-8c) | CR-8c |
| C-8 | officials.enforcement | enforcement_cost | increase | Staff time of the finance office and inspector (CR-8c) | CR-8c |
| C-9 | taxpayers.general_budget | resources_available_other_uses | decrease | Other general-budget spending | CR-8a |
| C-10 | town (cash reserve) | resources_available_other_uses | decrease | Use of the reserve, including for other emergencies, while it is advanced | CR-8a, CR-10 |
| C-12 | homeowners.damaged | price_paid, wait_time (home window replacement) | at_least_one_increase | Home windows repaired later or at a higher price because glaziers' time went to windows that would not otherwise have been replaced | CR-9 → CR-6 → CR-8a |

## 10. Assumptions

Case assumptions are used as given. New premises added by this re-run are marked A-N.

| ID | Statement | Type | p | Evidence | If false |
| --- | --- | --- | --- | --- | --- |
| A-1 | The town completes the eligible replacements within the year, as contracted. | other | 0.9 | Contracts, firm capacity, the town's record on emergency works. | Fail or lose support: C-2, C-3, C-13 |
| A-2 | Some damaged-shop owners would not have replaced their windows within the year without the program (uninsured, marginal or about to close). | other | 0.8 | Insurance coverage of town-center shops; vacancy and closure rates; what owners did after earlier storms. | Fail or lose support: C-3, C-12, C-13 |
| A-3 | Glaziers' capacity is limited in the months after the storm: crews cannot be expanded quickly, and outside firms are far away. | mobility | 0.8 | Number of local crews; backlog after the storm; distance to the nearest other firms. | Fail or lose support: C-4, C-5, C-12, C-13 |
| A-4 | Most damaged-shop owners would have replaced their windows within the year at their own or their insurer's expense. | other | 0.9 | Insurance coverage (about 70%); shops cannot trade for long behind boards; past storms. | Fail or lose support: C-2, C-11, C-14, C-15 |
| A-5 | Insured owners' claims for windows the town replaced are not paid, and the town does not recover the cost from insurers. | other | 0.65 | Policy wording on losses made good by a third party; whether the town pursues subrogation. | Fail or lose support: C-2, C-11, C-14, C-15 |
| A-6 | Owners who heard the debate delayed permanent replacement, and the program's queue is slower than hiring a glazier directly. | expectations | 0.7 | Dates of replacements before and after 6 March; the program's schedule. | Fail or lose support: C-4, C-5 |
| A-7 | Inspection lets through some claims for windows not broken by the storm. | enforcement | 0.6 | Photo-only applications; one inspector for about 600 claims. | Fail or lose support: C-6 |
| A-8 | Homeowners and shop owners organize to extend the program to homes or to future storms. | other | 0.6 | Council meeting attendance; existing business association. | Fail or lose support: C-7 |
| A-9 | Shop owners come to expect the town to pay after future storms. | expectations | 0.4 | Council's "one-time" resolution; history of repeated relief in the region. | Fail or lose support: No reported consequence depends on it alone; see Not reported. |
| A-10 | Insurers spend or hold most of the claims they no longer pay outside Brackwater. | other | 0.8 | Where the insurers are based. | Fail or lose support: C-14, C-15 |
| A-11 | Sellers whose sales fall or rise adjust the labor they use, in staff or in hours, within the year. | alternative_uses | 0.8 | Share of hourly and part-time staff in local retail, hospitality and services; scheduling practice. | Fail or lose support: C-15 |
| A-N1 | Shops sell less while their windows are boarded up. (new premise) | other | 0.8 | Shops cannot trade for long behind boards (evidence for A-4); ground-floor displays and access. | Fail or lose support: C-5 |
| A-N2 | Households pay part of the levy by buying less from Brackwater sellers, not only from savings. (new premise) | other | 0.85 | An $80 charge on a water bill; share of household spending done locally. | Fail or lose support: C-14, C-15 |
| A-N3 | Local recipients of the transfer (shop owners, glaziers for extra work) spend no larger a share of their gain in Brackwater than households would have spent from the levy. (new premise) | other | 0.55 | Both groups live and shop locally; shop owners may use the gain to pay debts or reinvest; no direct evidence. | Fail or lose support: C-14, C-15 |

**Not reported** (a premise has p below 0.5, or the record lacks a needed fact):

- Shop owners insure less or protect windows less, expecting the town to pay after future storms (CR-10a, CR-4): A-9, p 0.4.
- Glaziers' employment: with crews fixed in the short run (A-3) and most windows replaced anyway (A-4), no sign follows for the number employed; the program changes who pays for most of their work, not whether it is done. Earnings are ambiguous (C-13).
- Households that do not pay and incur arrears or liens: no premise on non-payment.

## 11. Report

**The policy:** After a windstorm broke about 600 shop windows and many home windows, Brackwater charges each of its 16,000 households $80 once (about $1.28 million) and uses the money to have the four local glazing firms replace, at no charge to the owner, every broken ground-floor shop window not already replaced by 14 March, at about $2,000 a window. Home windows are excluded. The town advances the money from its reserve.

**Visible consequences:** Every household pays $80 (C-1). Damaged-shop owners receive free windows: uninsured owners keep what they would have paid, insured owners keep their deductible (C-2). Some windows are replaced that would not otherwise have been within the year (C-3).

**Invisible consequences:** Households have $1.28 million less for other purchases (C-1), and Brackwater sellers sell less to residents (reading U1-a; C-14), so some local staff lose hours or jobs (C-15). Insurers, mostly outside the town, keep claims they would have paid (reading U1-a; C-11). Homeowners with broken windows pay more or wait longer for glaziers (C-12). Shop owners who waited for the program stay boarded longer and sell less (C-4, C-5); some false claims are paid (C-6); some owners lobby to extend the program (C-7). Administration, the general budget and the town's reserve carry costs (C-8, C-9, C-10).

**Ambiguous effects:** Glaziers' earnings (C-13): extra windows push up, but crews are fully booked and the fixed schedule may be above or below what they would have charged. Local sales under reading U1-b, where insurers repay the town (C-14).

**Key conditions:** Most damaged windows would have been replaced anyway (A-4, p 0.9); glaziers' capacity is fixed in the short run (A-3, p 0.8); insurers pay no claim for town-replaced windows (A-5, p 0.65); insurers spend outside the town (A-10, p 0.8); local recipients do not spend a larger share locally than payers (A-N3, p 0.55, new).

**What this analysis cannot say:** How much local sales or staffing fall; whether shop owners' gains outweigh households' and homeowners' losses; whether the program is good. Safety effects of boarded or unrepaired windows are out of scope in version 1. The comparison of spending shares rests on a new premise with p only just above the cut-off.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-1 | taxpayers.households | resources_available_other_uses | decrease | short | visible | A | CR-1 (op 4, K1: $80 per household; no behavior avoids it) → CR-8a, CR-8b | none |
| C-2 | shop_owners.damaged | resources_available_other_uses | increase | short | visible | B | CR-1 (op 2 and op 4, K2) → CR-3b → CR-8b (uninsured owners keep the full cost they would have paid; insured owners keep the $500 deductible; owners who would not have replaced receive a window) | A-1, A-4, A-5 |
| C-3 | glaziers | quantity_supplied (shop windows replaced within the year) | increase | short | visible | B | CR-1 (op 2, K2) → CR-4 mirror (x: leave the window unreplaced, y: free replacement) for owners who would not have replaced (A-2); plus claims for windows not broken by the storm (A-7) | A-1, A-2 |
| C-4 | shop_owners.damaged | wait_time (until permanent replacement) | increase | short | invisible | B | CR-10a (program expected from 6 March) → CR-4 (x: hire a glazier now, y: wait for the free program) → the program queue is slower than direct hiring | A-3, A-6 |
| C-5 | shop_owners.damaged | quantity_traded (own sales while boarded up) | decrease | short | invisible | B | C-4 → CR-9 (customers deal less with a boarded shop) | A-3, A-6, A-N1 |
| C-6 | shop_owners.damaged | reclassification (claims for windows not broken by the storm) | increase | short | invisible | B | CR-1 (op 2) → CR-4 (x: pay to replace an old window, y: claim it as storm damage) | A-7 |
| C-7 | shop_owners.damaged and homeowners | lobbying_effort | increase | medium | invisible | B | CR-4 (x: accept a one-time program, y: lobby to extend it to homes or future storms) → CR-8c | A-8 |
| C-8 | officials.enforcement | enforcement_cost | increase | short | invisible | A | CR-1 (op 2, K3: billing, inspection, contract management) → CR-8c | none |
| C-9 | taxpayers.general_budget | resources_available_other_uses | decrease | short | invisible | A | CR-1 (op 4, K3 funded from the general budget) → CR-8a | none |
| C-10 | town (cash reserve) | resources_available_other_uses | decrease | short | invisible | A | CR-1 (op 4: reserve advanced in March, repaid within about 60 days of the April bill) → CR-10 (the means are unavailable for that time) → CR-8a | none |
| C-11 | insurers | resources_available_other_uses | U1-a: increase; U1-b: ambiguous | short | invisible | B | C-2 → CR-9 (the insurance contract: a window the town replaces is a claim not paid) → CR-8b; under U1-b (the town recovers its cost from insurers) the payment is made to the town at the schedule price instead, and the sign depends on that price against the claim cost | A-4, A-5 |
| C-12 | homeowners.damaged | price_paid, wait_time (home window replacement) | at_least_one_increase | short | invisible | B | C-3 (more windows to replace with fixed capacity) → CR-9 (the same glaziers serve both) → CR-6 (glaziers' time scarcer; price or queue adjusts) | A-2, A-3 |
| C-13 | glaziers | earnings | ambiguous | short | invisible | B | (+) C-3 (extra windows); (+ or −) the fixed schedule of about $2,000 against the price glaziers would have charged after the storm (CR-6, CR-5c); with capacity fixed (A-3), extra town work displaces other work; CR-12b | A-1, A-2, A-3 |
| C-14 | sellers.local | quantity_traded (sales to Brackwater residents) | U1-a: decrease; U1-b: ambiguous | short | invisible | B | (−) C-1 → CR-9 (households buy from local sellers) with A-N2; (+) C-2 and C-13 → CR-9 (local recipients spend part of their gain locally); CR-12b resolved by CR-8b plus arithmetic: under U1-a the part of the levy retained by insurers (C-11) is spent outside Brackwater (A-10), so local recipients receive less than local payers give, and with A-N3 the net is a decrease; under U1-b that leak is absent and the sign is ambiguous | A-4, A-5, A-10, A-N2, A-N3 |
| C-15 | workers (Brackwater retail and services) | employment, hours_worked | U1-a: at_least_one_decrease; U1-b: ambiguous | short | invisible | B | C-14 → CR-9 (labor used to make the sales) → LW-10 | A-4, A-5, A-10, A-11, A-N2, A-N3 |

## Gaps found

**(a) Calculus gaps.** One. The direction in which a fall in an actor's means changes their purchases of a named good (here, households' purchases from Brackwater sellers) is not given by any core rule. CR-3c and CR-8a say only that some other use is given up; CR-4's exception says a change in means can make directions ambiguous. A rule such as "a fall in means reduces at least one of the actor's purchases" exists in effect (CR-8a), but naming which one needs a premise (A-N2). Comparing payers' and recipients' local spending needed a further premise (A-N3).

**(b) New premises.**

- A-N1 (p 0.8): the link from a longer wait to lower sales of a boarded shop is empirical.
- A-N2 (p 0.85): see (a); needed to say that the levy reduces local purchases rather than only savings.
- A-N3 (p 0.55): needed as the dominance premise under CR-12b for local sales; CR-8b and A-10 give the leak, but the leak decides the sign only if payers and local recipients spend similar shares locally.

**(c) Unclear core rules.**

- CR-12b refers to a dominance pattern (DM); in a core-only run the dominance for local sales was built from CR-8b, A-10, arithmetic and A-N3. The rule does not say this is an admissible form.
- CR-9 relations: the insurance contract (insurer to shop owner) is an exchange relation, but none of the 2.8 types (substitute, complement, input_to, same_market_other_segment, across_border) fits it.
- The unclear subrogation provision is both a reading (U1) and a case assumption (A-5, p 0.65). The normal form says readings get no probability; here the record gave one. Signs were reported per reading and A-5 cited for the empirical part (whether insurers in fact decline).
- CR-4 does not fit a lump-sum levy: no choice changes what is paid. CR-1 operation 4 and CR-8 carry the whole chain; CR-4's exception (change in total means) is the only link to behavior, and it gives no direction for a named good.

## Comparison with the pattern-based analysis

**Summary.** Both versions reach Bastiat's point by the same route: households lose $80 each; for windows that would have been replaced anyway the program is a transfer to shop owners and insurers, not new glazing work; homeowners pay more or wait longer for glaziers; owners who heard the debate waited; some false claims pass; and administration costs something. The structural difference is in how spending effects are recorded. The pattern version follows OC-1 and OC-5 and defines its actor classes by the effect (`sellers.forgone` lose, `sellers.recipients` gain), so each sign holds by construction, and it reports local employment overall as ambiguous. The core version nets the two into Brackwater sellers as a whole and, using the insurers' leak out of town (A-10) and a new premise on spending shares (A-N3, p 0.55), signs local sales and staffing a decrease under reading U1-a. That sign is defensible under the method's per-premise cut-off but fragile: it holds only if A-N2, A-N3 and A-10 all hold, whose joint probability is well below 0.5. The pattern version overclaims once (home repairs completed within the year fall, when its own timeline has the program finished by early summer, so home work is delayed, not forgone) and claims glaziers' hours rise without a premise on their ability to add hours. The core version omitted tax revenue and over-aggregated the waiting effect to all damaged shop owners.

Counts: M 6, V 7, S 2, OP 2, OC 2.

### Pattern version → core version

| Pattern ID | Matched core ID(s) | Class | Cause | Note |
| --- | --- | --- | --- | --- |
| C-1 | C-2 | V | | Free window recorded as resources increase rather than price_paid decrease. |
| C-2 | C-3, C-13 | S | J | Pattern: glaziers' hours_worked increase. Core: shop windows replaced increase (C-3), earnings ambiguous (C-13), no sign for total glazier labor because, with capacity limited (A-3), extra shop work displaces home work (C-12). With capacity limited but not fixed, CR-4 gives hours up or unchanged; "increase" needs a premise that some glaziers can and will add hours. Both defensible; the pattern version should name that premise. |
| C-3 | none | OC | E | tax_revenue increase (CR-8b, Tier A). Core-version omission; it records only the payers' side (C-1). |
| C-4 | C-2 | M | | Core's class covers all damaged owners; the claim for those who would have replaced is the same. |
| C-5 | C-11 | V | | Core gives per-reading signs (U1-a increase; U1-b ambiguous); the record assumes U1-a. |
| C-6 | C-4 | M | | Same sign for the pattern's subgroup (owners who would have replaced). The core records it for all damaged owners, which is too broad; see Findings. |
| C-7 | C-6 | M | | |
| C-8 | C-7 | M | | Core omits glaziers as lobbyists; minor. |
| C-9 | C-12 | M | | |
| C-10 | C-14 | V | | Pattern's `sellers.recipients` gain by construction; core nets them with payers' sellers into `sellers.local`. The substantive difference is in the "—" row below. |
| C-11 | C-15 | V | | As C-10, for employment and hours of sellers that lose spending. |
| C-12 | C-15 | V | | As C-10, for sellers that gain spending. |
| C-13 | C-1 | M | | |
| C-14 | C-14 | V | | As C-10. Note that the pattern's Tier A holds only because the class is defined by where the money would have gone; for a named market (Brackwater sellers) the core needs A-N2. |
| C-15 | C-12 | OC | P | Pattern: home repairs completed within the year decrease (SB-3). By the pattern version's own time structure the program is finished by early summer, so glaziers' time is displaced in time, not over the year; C-9 (price or wait, at least one) is the valid claim, and a fall in repairs within the year needs a premise that some homeowners forgo the repair altogether. SB-3 misapplied to a timing shift (2.5, timing shifts). |
| C-16 | C-8, C-9, C-10 | V | | Split into enforcement cost, general budget and the use of the reserve. |
| — (workers outside glazing, employment and hours, ambiguous) | C-15 | S | A | Pattern ambiguous; core U1-a at_least_one_decrease, U1-b ambiguous. The core's dominance comes from CR-8b with A-10 (insurers' share leaves town) plus the new premise A-N3 (p 0.55) that local recipients do not spend a larger share locally. Valid under the per-premise cut-off; the joint probability of A-N2, A-N3 and A-10 is about 0.37, so the pattern version's ambiguous is the more cautious report. |

### Core-only consequences

| Core ID | Class | Cause | Note |
| --- | --- | --- | --- |
| C-5 | OP | A | Shops' own sales fall while boarded up, resting on the new premise A-N1. Recorded for all damaged owners, though owners who would not have replaced get their windows sooner and sell more (the pattern version notes this in section 8); valid only for the waiting subgroup. |
| C-13 | OP | J | Glaziers' earnings ambiguous (fixed schedule against the post-storm price; displaced work). Unsigned. |

### Findings

- **Pattern misapplied (SB-3).** Pattern C-15 reads a displacement in time as a fall in quantity within the year. SB-3 should be applied with the timing convention of 2.5 when the subsidized use is temporary.
- **Pattern framing (OC-1, OC-5).** Classes such as `sellers.forgone` and `sellers.recipients` are defined by the sign of the effect, so their consequences cannot fail. They are correct but uninformative for scoring; for any named market the sign needs a premise (here A-N2), as the core version shows.
- **Error in the core version (aggregation).** C-4 (wait_time increase) and C-5 (own sales decrease) are recorded for all damaged shop owners. For owners who would not have replaced their windows soon, the program brings the window sooner; for the class as a whole CR-12b gives ambiguous. The signs hold only for owners who would have replaced promptly, as the pattern version records.
- **Error in the core version (omission).** tax_revenue increase.
- **Core version fragility.** C-14 and C-15 under U1-a rest on a premise at p 0.55 joined with two others; the method's per-premise cut-off admits it, but the joint probability is below 0.5.
- **Limit of the core rules.** The core version's gap (a) is real but narrow: CR-8a says a fall in means reduces some use, and no core rule says which named purchase falls. This did not produce a sign difference with any valid pattern claim; OC-1's Tier A sign for named sellers holds only by defining the class by the effect.
