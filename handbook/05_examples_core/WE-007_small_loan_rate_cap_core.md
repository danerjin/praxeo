# WE-007 / Analysis: Interest-rate cap on small consumer loans (core-only re-run)

Analyst: core-only re-run (Handbook 0.4)  |  Rules: core rules CR-1 to CR-12 only  |  Status: awaiting comparison

## 1. Policy record

**Wexmoor Small Loan Act.** Wexmoor is a state of about four million people. Before the Act, about 40 companies licensed under Wexmoor's consumer lending law ran about 380 storefronts, and 12 online lenders held Wexmoor licenses. Typical loans were two-week payday loans of $300 to $600 at about $15 per $100 borrowed (roughly 390% APR) and six-month installment loans of $500 to $1,500 at 150% to 250% APR. Banks charge an overdraft fee of about $34. Pawn loans are governed by a separate Pawn Act, which allows fees of up to 15% a month. Some credit unions offer small loans below 28% APR, mostly to members with a history at the credit union.

The neighboring state of Kestria has no rate cap. Its border is 20 minutes from Brannock (Wexmoor's second city, about 300,000 people) and two hours from Wexmoor City. Informal lending (family, employers, street lenders) exists in both states.

The bill was introduced in January, with polls showing wide support; it passed in April and takes effect on October 1. Loans made before October 1 are honored on their original terms; a loan renewed or refinanced after that date is a new loan.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Rate cap | `price_ceiling` | Consumer loans of $2,500 or less | Lenders licensed under Wexmoor's consumer lending law | All-in APR of at most 36%, counting interest, all fees and any product sold with the loan (credit insurance, memberships). | Loans over $2,500. Banks and credit unions (chartered under other laws). Pawn loans (Pawn Act). |
| K2 License reach | `licensing_requirement` (existing, restated) | Any consumer loan to a Wexmoor resident | All lenders, including online lenders based elsewhere | A Wexmoor license is required; loans by unlicensed lenders, and loans above the cap, are void (the borrower owes neither interest nor principal). | As K1 |
| K3 Enforcement | Administration and enforcement | K1, K2 | Department of Financial Institutions; Attorney General | Examinations of licensees; license revocation; civil suits against unlicensed lenders. Lenders based in other states or abroad are hard to reach. Funded from license fees and the general budget. | None |

Unclear provisions:
- **U1.** Whether "earned wage access" products (advances on wages already earned, repaid from the next paycheck, with optional "tips" and fees for fast delivery) are loans. The Act defines a loan as an agreement with an obligation to repay; many such products are written without one. Reading U1-a: products written without a repayment obligation are not loans and fall outside the Act. Reading U1-b: they are loans, and their fees count toward the 36% APR. Readings get no probability; [a consequence of the original analysis] reports one sign for each.


Horizons used below: short = from the announcement in January to the first months after October 1; medium = one to three years; long = beyond.

## 2. Classification

| Component | Rothbard type | Binding? (assumption ID) | Core rules applied |
|---|---|---|---|
| K1 Rate cap | triangular (forbids loans between private parties above 36% APR) | Yes for most current borrowers (A-1, p 0.9); complied with by licensees (A-2, p 0.85) | CR-1, CR-4, CR-5a, CR-6, CR-7, CR-9, CR-10, CR-11 |
| K2 License reach | triangular (existing, restated); voids unlicensed and above-cap loans | Binds on lenders that can be reached; incomplete for unlicensed online lenders (A-10, p 0.7) | CR-1 (op 1 and op 3), CR-4, CR-11b |
| K3 Enforcement | binary on the budget side (license fees and general budget) | Effective against licensees (A-2) | CR-1 (op 3), CR-8 |

**CR-1: what each component does to each actor class.** Operations: 1 remove an option, 2 add an option, 3 change what an option brings, 4 transfer means. A dash means no direct effect; indirect effects are traced with CR-9.

| Actor class | K1 Rate cap | K2 License reach | K3 Enforcement |
|---|---|---|---|
| borrowers.current (small-loan borrowers) | 1: borrowing $2,500 or less above 36% APR from a licensee removed; 3: loans still made cost less | 2 and 3: a void loan need not be repaid, so borrowing from an unlicensed lender brings a right not to repay | — |
| borrowers.prospective | as borrowers.current | as borrowers.current | — |
| lenders.licensed (storefront and online licensees) | 1: lending above 36% APR on $2,500 or less removed | 3: above-cap loans are void (loss of principal and interest) | 3: examinations, revocation risk; compliance paperwork |
| lenders.prospective (would-be entrants) | 1: entry into above-36% lending removed | 3 | 3 |
| intermediaries (unlicensed online lenders) | — (not licensed) | 3: their loans are void; collection through courts unavailable | 3: risk of civil suits, hard to reach |
| sellers.substitutes (pawnbrokers, banks, credit unions, wage-advance providers) | — (exempt; wage advances depend on reading U1) | — | — |
| neighboring_jurisdictions (Kestria lenders) | — | 3 for any loan to a Wexmoor resident made in Wexmoor's reach | — |
| officials.enforcement (Department of Financial Institutions, Attorney General) | — | — | 2 and 4: new duties, means directed to them |
| taxpayers | — | — | 4: funding from license fees and the general budget |

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| borrowers.current | Payday and installment borrowers | Capped loans cost less where made; most cannot get one (A-1); fall back to pawn, overdraft, late payment, family (A-7), Kestria (A-8), wage advances (A-11), unlicensed online lenders (A-10) |
| lenders.licensed | About 40 companies, 380 storefronts, 12 online licensees | Cannot lend at their prior prices; can lend larger amounts or above $2,500 (A-4), convert to pawn (A-4), move capital elsewhere (A-3) |
| lenders.prospective | Would-be entrants | Entry returns cut from January (A-6) |
| workers (storefront staff) | Employees of licensed lenders | Their employers' demand for their work falls (CR-9, input_to) |
| factor_owners.specific | Owners of lending firms and licenses | Expected yield cut |
| intermediaries | Unlicensed online lenders | Served demand left unmet by licensees; their loans are void |
| sellers.substitutes | Pawnbrokers, banks (overdraft), credit unions, wage-advance providers | More demand from former borrowers |
| buyers.complements | Users of check cashing and money orders at loan storefronts | Lose a nearby storefront (A-9) |
| neighboring_jurisdictions | Kestria storefronts, 20 minutes from Brannock | Receive Wexmoor borrowers (A-8) |
| officials.enforcement | Department of Financial Institutions; Attorney General | More cases against unlicensed lenders; fewer licensees |
| taxpayers | General budget | Make up any fall in license fees |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | borrowers.current | price_paid (APR on capped loans that are made) | decrease | short | CR-1 (op 1) → CR-6 | A-1, A-2 |
| C-2 | lenders.licensed | net_price_received (per small loan) | decrease | short | CR-1 (op 1) → CR-3a | A-1, A-2 |

Supporters expect borrowers to pay less. They do on loans that are still made; but A-1 says most current borrowers' loans cannot be made at 36%, so for most borrowers the direct effect is the removal of the loan (C-4), not a cheaper one.

## 5. Responses

**CR-2 to CR-5 by actor class.**

| Actor class | CR-2/CR-3: which chosen option is removed or burdened | CR-4 pairs (x made worse relative to y) | CR-5 |
|---|---|---|---|
| borrowers.current | Borrowing at the prior price removed (CR-3a: worse off by their own ranking, unless they obtain a capped loan) | x: licensed small loan (unavailable), y: pawn, overdraft, late payment, family, Kestria, wage advance, unlicensed lender | 5a: loans that would have been made are prevented |
| lenders.licensed | Lending at prior prices removed | x: small loans in Wexmoor, y: other products, other states, other work; x: small loan, y: larger or over-$2,500 loan; x: loan storefront, y: pawn storefront; x: lend after October 1, y: lend before; x: accept, y: lobby | 5a; 5c: the range of permitted terms is moved |
| lenders.prospective | Entry at prior prices removed | x: enter, y: stay out (CR-10a from January) | — |
| intermediaries | — | Mirror: lending to Wexmoor residents illegally made relatively better by unmet demand; x: comply, y: violate | — |
| sellers.substitutes | — | Mirror: their products made relatively better for borrowers | — |
| Kestria lenders | — | Mirror | — |
| owners of lending firms | Expected yield cut | CR-7c rather than CR-4: price of the asset adjusts | — |

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-3 | lenders.licensed | quantity_supplied (loans of $2,500 or less) | decrease | short | CR-4b (x: small loans in Wexmoor, y: other uses) → CR-7a | A-1, A-2, A-3 |
| C-4 | borrowers.current | quantity_traded (licensed loans of $2,500 or less) | decrease | short | CR-6 → C-3 → CR-5a | A-1, A-2, A-3 |
| C-5 | borrowers.current | excess_demand (small loans at 36% APR or less) | increase | short | CR-6 | A-1, A-2 |
| C-6 | borrowers.current | wait_time, search_cost, allocation_by_non_price_criteria | at_least_one_increase | short | CR-6 (criteria margin) → CR-11a | A-1, A-2 |
| C-7 | lenders.licensed | transaction_size | increase | medium | CR-6 (loan size open) → CR-4b (x: small loan, y: larger loan) | A-1, A-2, A-14 |
| C-8 | lenders.licensed | reclassification (loans over $2,500; pawn conversion) | increase | medium | CR-4b (x: covered form, y: exempt form) | A-1, A-2, A-4 |
| C-9 | lenders.licensed | number_of_sellers (licensed small-loan storefronts) | decrease | medium | C-3 → CR-10b → CR-7a | A-1, A-2, A-3 |
| C-11 | lenders.prospective | entry_rate | decrease | short | CR-10a → CR-4b (x: enter, y: stay out) | A-1, A-6 |
| C-12 | factor_owners.specific (owners of Wexmoor lending firms and licenses) | asset_value | decrease | short | CR-10c → CR-7c | A-1, A-2, A-6 |
| C-13 | lenders.licensed | quantity_traded (window: loans made April to September) | increase | short | CR-10a → CR-4 (x: lend after October 1, y: lend before) | A-1, A-5 |
| C-14 | borrowers.current | quantity_substitute (pawn loans, overdrafts, late bill payment, family loans) | increase | short | C-4 → CR-4b (x: small loan, y: substitute) | A-1, A-2, A-7 |
| C-16 | borrowers.current | cross_border_purchases (loans from Kestria storefronts) | increase | short | C-4 → CR-4b (x: go without, y: borrow in Kestria) | A-1, A-2, A-8 |
| C-20 | intermediaries (unlicensed online lenders) | informal_activity (unlicensed loans to Wexmoor residents) | increase | short | C-5 → CR-6 (exchanges outside the rule) → CR-4b (x: comply, y: violate) | A-1, A-2, A-10 |
| C-23 | borrowers.current | quantity_substitute (earned wage access) | U1-a: increase; U1-b: ambiguous | short | U1-a: C-4 → CR-4b (x: small loan, y: wage advance outside the Act); U1-b: (+) C-4 → CR-4b; (−) CR-1 (op 1 on providers whose fees exceed 36% APR) → CR-4b → CR-12b | A-1, A-2, A-11 |
| C-25 | lenders.licensed | lobbying_effort | increase | medium | CR-4 (x: accept, y: lobby) | A-1, A-N1 |
| C-26 | lenders.licensed | compliance_cost (all-in APR calculation and product review) | increase | short | CR-1 (op 3) → CR-8c | none |

Notes on the responses.
- C-7: A-14 says a material part of a loan's cost is fixed per loan. Under an APR cap the permitted charge rises with the amount and the term, while the fixed cost does not, so the smallest loans are the first to become unprofitable (CR-4c applied to loan sizes). Lenders that stay shift toward larger loans within the cap and, where borrowers accept (A-4), above $2,500 (C-8).
- C-13: loans made before October 1 are honored on their original terms, so a loan made in the window keeps its prior price, while a loan made after does not. Lenders who can raise volume and lengthen terms (A-5) do so. After October 1 the comparison is C-4 (decrease). Borrowers who renew after October 1 make new loans under the cap.
- C-23: under U1-a, wage advances written without a repayment obligation fall outside the Act and gain borrowers. Under U1-b their fees count toward 36% APR; providers with fees above that are removed (decrease), while unmet small-loan demand pushes the other way (CR-12b).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-10 | workers (storefront staff) | employment (licensed small-loan lending) | decrease | medium | C-9 → CR-9 → LW-10 | labor `input_to` lending | A-1, A-2, A-3 |
| C-15 | sellers.substitutes (pawnbrokers) | number_of_sellers (pawn shops) | increase | medium | C-8 (conversion), C-14 → CR-9 → CR-7a | pawn loans `substitute` for small loans, close | A-1, A-2, A-4, A-7 |
| C-17 | neighboring_jurisdictions (Kestria lenders near the border) | quantity_substitute (loans to Wexmoor residents) | increase | short | C-16 → CR-9 | Wexmoor loans to Kestria loans, `across_border` | A-1, A-2, A-8 |
| C-18 | neighboring_jurisdictions (Kestria storefronts) | quantity_complement (check cashing and money orders for Wexmoor residents) | increase | medium | C-16 → CR-9 | loans and check cashing, `complement` (trip) | A-1, A-2, A-8, A-9 |
| C-19 | buyers.complements (check cashing and money orders in Wexmoor) | search_cost | increase | medium | C-9 → CR-9 → CR-4 (x: nearby storefront, now closed, y: farther outlet) | loans and check cashing, `complement` (trip) | A-1, A-2, A-3, A-9 |
| C-21 | borrowers.current (from unlicensed lenders) | disputes_settled_outside_courts | increase | medium | C-20 → CR-1 (K2 op 3: loan void, courts unavailable to lender) → CR-11b | legal to illegal segment, `same_market_other_segment` | A-1, A-2, A-10 |
| C-22 | borrowers.current (from unlicensed lenders) | quality_information | decrease | medium | C-20 → CR-11b | `same_market_other_segment` | A-1, A-2, A-10 |
| C-24 | borrowers.current | full_cost_per_unit (cost of covering a short-term cash need) | ambiguous | short | (−) C-1; (+) C-6, C-14 → CR-3a (fallbacks ranked lower) → CR-12b | same need, substitutes | A-1, A-2, A-7 |
| C-27 | officials.enforcement | enforcement_cost | increase | short | C-20 → CR-1 (K3) → CR-8c | — | A-1, A-10 |
| C-28 | taxpayers | resources_available_other_uses | decrease | medium | C-9 → fewer license fees → CR-8b; C-27 → CR-8a → CR-12a | — | A-1, A-2, A-3, A-N2 |

Chains stopped: billers who are paid late (C-14) and the families who lend are diffuse bystanders at depth 3; not followed further. Street lending is below the cut-off (A-13). Effects on Kestria's tax base and on Wexmoor landlords of vacated storefronts would be depth 4 bystander effects with no recorded evidence; pruned.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| borrowers.current, full_cost_per_unit, short | fallbacks ranked lower (C-14), stricter criteria (C-6) | lower APR on loans still made (C-1) | none: no premise says which dominates | ambiguous (C-24) |
| borrowers.current, quantity_substitute (earned wage access), short | unmet demand (both readings) | U1-b: high-fee providers removed | not combined across readings | U1-a: increase; U1-b: ambiguous (C-23) |
| lenders.licensed, transaction_size, medium | fixed per-loan cost (A-14); exempt loans over $2,500 (A-4) | none | none needed (CR-12a) | increase (C-7) |
| taxpayers, resources_available_other_uses, medium | none | lost license fees (C-9), more enforcement (C-27) | none needed (CR-12a) | decrease (C-28) |
| lenders, quantity_traded, window vs after October 1 | window (C-13) | after the effective date (C-4) | different windows, not netted (CR-12c applies by analogy; signs are per window) | increase in window; decrease after |

No dominance claim is made.

## 8. Time structure

- January (introduction, passage expected, A-6): would-be entrants hold back (C-11); the value of lending firms and licenses falls when the cap becomes expected, borne by those who own them then (C-12, CR-7c).
- April to September (enacted, not yet effective): lenders who know the date make more loans and longer loans, which are honored on their original terms (C-13, A-5).
- From October 1: loans cannot be renewed above the cap, so borrowers on rolling payday loans lose access as their loans come due, not all at once.
- Storefronts close as leases end and staff move (C-9, C-10, CR-10b); pawn conversions take time (C-15). These persist if the cap is later lifted, because reopening costs something (CR-10b).
- Unlicensed online lending and wage advances grow as providers learn of the unmet demand (C-20, C-23).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-4 | borrowers.current | quantity_traded | decrease | Loans that borrowers and lenders both would have chosen; each expected a gain | CR-5a, CR-3a |
| C-6 | borrowers.current | wait_time, search_cost, allocation_by_non_price_criteria | at_least_one_increase | Time spent finding a lender willing to lend at the cap | CR-6, CR-8c |
| C-19 | buyers.complements | search_cost | increase | Time spent reaching a farther check-cashing outlet | CR-8c |
| C-26 | lenders.licensed | compliance_cost | increase | Staff time on APR calculation and product review | CR-8c |
| C-27 | officials.enforcement | enforcement_cost | increase | Staff time on suits against unlicensed lenders | CR-8c |
| C-28 | taxpayers | resources_available_other_uses | decrease | Whatever the general budget would otherwise have funded | CR-8a, CR-8b |

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Small loans to most current borrowers cannot be made profitably at 36% APR. | binding | 0.9 | Lenders' cost per loan and default rates; experience in places with similar caps. | The cap binds on few loans; most consequences shrink to those few. |
| A-2 | Licensed lenders comply: they do not lend above the cap. | enforcement | 0.85 | Examinations; void-loan penalty; license revocation. | Licensed lending above the cap continues; C-3, C-4, C-9 weaken. |
| A-3 | Lenders' capital and staff have other uses (other products, other states, other work). | alternative_uses | 0.85 | Multi-state lenders; storefront lease terms. | Lenders stay and bear the loss; C-3, C-9, C-10 weaken. |
| A-4 | Some borrowers accept loans over $2,500, and the Pawn Act allows storefronts to convert. | other | 0.7 | Underwriting standards; pawn licensing rules. | C-8, C-15 fail. |
| A-5 | Lenders can raise volume and lengthen terms between April and October, and know the effective date. | expectations | 0.6 | Loan volumes in the window; lender statements. | C-13 fails. |
| A-6 | From January, would-be entrants expected the bill to pass. | expectations | 0.8 | Polls; sponsors; legislative calendar. | C-11, C-12 move to April. |
| A-7 | Unserved borrowers have legal substitutes (pawn, overdraft, late payment, family). | substitutability | 0.85 | Bank account holding among borrowers; pawn store locations. | C-14, C-15 fail; C-24 loses a chain. |
| A-8 | Borrowers in Brannock can easily reach Kestria storefronts and may legally borrow there. | mobility | 0.6 | Drive time of 20 minutes; Kestria law on lending to non-residents. | C-16 to C-18 fail. |
| A-9 | Borrowers use the same storefront for loans, check cashing and money orders. | other | 0.7 | Storefront transaction data. | C-18, C-19 fail. |
| A-10 | Some unlicensed online lenders reach Wexmoor borrowers, and enforcement against them is incomplete. | enforcement | 0.7 | Online advertising aimed at Wexmoor; record of suits against out-of-state lenders. | C-20 to C-22, C-27 fail. |
| A-11 | Wage advances are a usable substitute for small loans for some borrowers (they have a regular paycheck and access to a provider). | substitutability | 0.65 | Share of small-loan borrowers in regular employment; providers' reach among Wexmoor employers. | C-23 fails under both readings. |
| A-12 | Lenders can add fees or products to capped loans without breaching the all-in APR rule. | other | 0.3 | Text of K1. | (Below cut-off; used by no reported consequence.) |
| A-13 | Borrowing from street lenders rises on a meaningful scale. | enforcement | 0.35 | Police reports; surveys of borrowers in places with similar caps. | (Below cut-off; used by no reported consequence.) |
| A-14 | A material part of the cost of a small loan is fixed per loan (underwriting, servicing, collection), not proportional to the amount lent. | other | 0.85 | Lenders' cost accounts; the cost per loan relative to the charge on a $300 loan. | C-7 rests on A-4 alone (loans above $2,500). |
| A-N1 | Licensed lenders (about 40 companies with a concentrated stake) spend resources to change the cap or its reach after enactment. | other | 0.6 | A small number of firms each losing most of a business line; the bill was contested in the legislature. | C-25 fails. |
| A-N2 | License fees under the consumer lending law are charged per licensee or per location, so fee revenue falls when licensees and storefronts close. | other | 0.75 | The record says K3 is funded from license fees; fee schedules of this kind are usually per license or location. | C-28 rests on C-27 alone. |

**Not reported (an assumption below 0.5).**
- Lenders add fees or tied products to capped loans (CR-6, unregulated terms): needs A-12 (p 0.3). The all-in APR rule closes most such margins.
- Borrowing from street lenders rises, with disputes settled outside courts (CR-6, CR-11b): needs A-13 (p 0.35).

## 11. Report

**The policy:** From October 1, licensed lenders in Wexmoor may not charge more than 36% APR, all fees included, on consumer loans of $2,500 or less. Loans by unlicensed lenders, and loans above the cap, are void. Loans over $2,500, banks, credit unions and pawn loans are exempt. Loans made before October 1 keep their terms.

**Visible consequences:** Borrowers who still get a licensed small loan pay a lower rate (C-1); lenders receive less per loan (C-2). Licensed lenders make fewer small loans (C-3), and many storefronts close (C-9).

**Invisible consequences:**
- Borrowers: fewer licensed small loans are made (C-4), more is wanted at the cap than is offered (C-5), and borrowers face stricter criteria, longer searches or waits (at least one, C-6). They turn to pawn loans, overdrafts, late payment and family (C-14), to Kestria storefronts in the Brannock area (C-16), and to wage advances where these fall outside the Act (C-23, U1-a). Some turn to unlicensed online lenders (C-20); with them, disputes are settled outside courts (C-21) and borrowers have less to judge lenders by (C-22).
- Lenders: loans grow larger and shift above $2,500 or into pawn (C-7, C-8), because a fixed cost per loan makes the smallest loans the first to become unprofitable at a capped rate. Lending rises in the April to September window (C-13). Lenders spend more on compliance (C-26) and on seeking changes to the law (C-25).
- Would-be entrants hold back from January (C-11); owners of lending firms and licenses bear a fall in their value when the cap becomes expected (C-12).
- Storefront staff: fewer jobs in licensed small-loan lending (C-10). Users of check cashing at closed storefronts search farther (C-19); Kestria storefronts gain loans and check-cashing business (C-17, C-18). Pawn shops become more numerous (C-15).
- The state: more spent pursuing unlicensed lenders (C-27); license fees fall, so taxpayers fund more of enforcement (C-28).

**Ambiguous effects:**
- Borrowers' full cost of covering a short-term cash need (C-24): lower on loans still made; higher for those pushed to lower-ranked fallbacks.
- Wage advances under reading U1-b (C-23): unmet demand pulls up; the cap removes high-fee providers.

**Key conditions:** That the cap binds for most borrowers (A-1, p 0.9) and licensees comply (A-2, p 0.85); that lenders' capital has other uses (A-3, p 0.85). Cross-border borrowing needs A-8 (p 0.6); the window rush needs A-5 (p 0.6); lobbying rests on a new premise (A-N1, p 0.6).

**What this analysis cannot say:** How many loans disappear, how many borrowers are better or worse off on balance, or whether the cap is good policy. It cannot say which substitute each borrower uses, or how large the move to Kestria or to unlicensed lenders will be. Effects on borrowers' health, safety and well-being beyond the variables listed (for example, the consequences of default or of street lending) are outside version 1 and are not analyzed.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | borrowers.current | price_paid (APR on capped loans that are made) | decrease | short | visible | B | CR-1 (op 1: loans above 36% removed) → CR-6 (price held below clearing) | A-1, A-2 |
| C-2 | lenders.licensed | net_price_received (per small loan) | decrease | short | visible | B | CR-1 (op 1) → CR-3a (chosen option removed) | A-1, A-2 |
| C-3 | lenders.licensed | quantity_supplied (loans of $2,500 or less) | decrease | short | visible | B | CR-1 (op 1) → CR-4b (x: small loans in Wexmoor, y: other products, states, work) → CR-7a | A-1, A-2, A-3 |
| C-4 | borrowers.current | quantity_traded (licensed loans of $2,500 or less) | decrease | short | invisible | B | CR-6 (trade limited by lenders' offers) → C-3 → CR-5a (prevented exchanges) | A-1, A-2, A-3 |
| C-5 | borrowers.current | excess_demand (small loans at 36% APR or less) | increase | short | invisible | B | CR-6 (price held below clearing) | A-1, A-2 |
| C-6 | borrowers.current | wait_time, search_cost, allocation_by_non_price_criteria | at_least_one_increase | short | invisible | B | CR-6 (pressure displaced to criteria by which lenders choose borrowers) → CR-11a (rate no longer prices risk) | A-1, A-2 |
| C-7 | lenders.licensed | transaction_size | increase | medium | invisible | B | CR-6 (loan size an open margin) → CR-4b (x: small loan, y: larger loan; fixed per-loan cost) → CR-4c | A-1, A-2, A-14 |
| C-8 | lenders.licensed | reclassification (loans over $2,500; pawn conversion) | increase | medium | invisible | B | CR-4b (x: covered form, y: exempt form) | A-1, A-2, A-4 |
| C-9 | lenders.licensed | number_of_sellers (licensed small-loan storefronts) | decrease | medium | visible | B | C-3 → CR-10b (closures as leases end) → CR-7a | A-1, A-2, A-3 |
| C-10 | workers (storefront staff) | employment (licensed small-loan lending) | decrease | medium | invisible | B | C-9 → CR-9 (labor input_to lending) → LW-10 | A-1, A-2, A-3 |
| C-11 | lenders.prospective | entry_rate | decrease | short | invisible | B | CR-10a (cap expected from January) → CR-4b (x: enter, y: stay out) | A-1, A-6 |
| C-12 | factor_owners.specific (owners of Wexmoor lending firms and licenses) | asset_value | decrease | short | invisible | B | CR-10c → CR-7c (lasting fall in expected yield borne by owners when expected) | A-1, A-2, A-6 |
| C-13 | lenders.licensed | quantity_traded (window: loans made April to September) | increase | short | invisible | B | CR-10a (deadline; earlier loans honored) → CR-4 (x: lend after October 1, y: lend before) | A-1, A-5 |
| C-14 | borrowers.current | quantity_substitute (pawn loans, overdrafts, late bill payment, family loans) | increase | short | invisible | B | C-4 → CR-4b (x: small loan, y: substitute) | A-1, A-2, A-7 |
| C-15 | sellers.substitutes (pawnbrokers) | number_of_sellers (pawn shops) | increase | medium | invisible | B | C-8 (conversion), C-14 → CR-9 (substitute) → CR-7a | A-1, A-2, A-4, A-7 |
| C-16 | borrowers.current | cross_border_purchases (loans from Kestria storefronts) | increase | short | invisible | B | C-4 → CR-4b (x: go without, y: borrow in Kestria) | A-1, A-2, A-8 |
| C-17 | neighboring_jurisdictions (Kestria lenders near the border) | quantity_substitute (loans to Wexmoor residents) | increase | short | invisible | B | C-16 → CR-9 (across_border) | A-1, A-2, A-8 |
| C-18 | neighboring_jurisdictions (Kestria storefronts) | quantity_complement (check cashing and money orders for Wexmoor residents) | increase | medium | invisible | B | C-16 → CR-9 (complement, trip) | A-1, A-2, A-8, A-9 |
| C-19 | buyers.complements (check cashing and money orders in Wexmoor) | search_cost | increase | medium | invisible | B | C-9 → CR-9 (complement, trip) → CR-4 (x: nearby storefront, closed; y: farther outlet) | A-1, A-2, A-3, A-9 |
| C-20 | intermediaries (unlicensed online lenders) | informal_activity (unlicensed loans to Wexmoor residents) | increase | short | invisible | B | C-5 → CR-6 (exchanges outside the rule) → CR-4b (x: comply, y: violate) | A-1, A-2, A-10 |
| C-21 | borrowers.current (from unlicensed lenders) | disputes_settled_outside_courts | increase | medium | invisible | B | C-20 → CR-1 (K2 op 3: loan void) → CR-11b (courts unavailable) | A-1, A-2, A-10 |
| C-22 | borrowers.current (from unlicensed lenders) | quality_information | decrease | medium | invisible | B | C-20 → CR-11b (licensing, reputation and courts unavailable) | A-1, A-2, A-10 |
| C-23 | borrowers.current | quantity_substitute (earned wage access) | U1-a: increase; U1-b: ambiguous | short | invisible | B | U1-a: C-4 → CR-4b (x: small loan, y: wage advance outside the Act); U1-b: (+) C-4 → CR-4b; (−) CR-1 (op 1 on high-fee providers) → CR-4b → CR-12b | A-1, A-2, A-11 |
| C-24 | borrowers.current | full_cost_per_unit (cost of covering a short-term cash need) | ambiguous | short | invisible | B | (−) C-1; (+) C-6, C-14 → CR-3a (fallbacks ranked lower) → CR-12b | A-1, A-2, A-7 |
| C-25 | lenders.licensed | lobbying_effort | increase | medium | invisible | B | CR-1 (op 1) → CR-4 (x: accept, y: lobby) | A-1, A-N1 |
| C-26 | lenders.licensed | compliance_cost (all-in APR calculation and product review) | increase | short | invisible | A | CR-1 (op 3) → CR-8c | none |
| C-27 | officials.enforcement | enforcement_cost | increase | short | invisible | B | C-20 → CR-1 (K3) → CR-8c | A-1, A-10 |
| C-28 | taxpayers | resources_available_other_uses | decrease | medium | invisible | B | C-9 → fewer license fees → CR-8b; C-27 → CR-8a → CR-12a | A-1, A-2, A-3, A-N2 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12 and the foundations.

**(b) New premises.**
- A-N1 (p 0.6, other): CR-4 (x: accept, y: lobby) gives only the direction; that some lenders are at that margin is empirical and not among the case assumptions.
- A-N2 (p 0.75, other): the fiscal chain (C-28) needs to know that K3's license-fee funding shrinks when licensees exit; CR-8b says every payment is a receipt to someone but not how fee revenue scales with the number of payers.

**(c) Unclear core rules.**
- CR-7c and CR-10c both cover the fall in the value of lending firms (C-12); CR-7c says who bears it, CR-10c says what the value reflects. It is not clear which is primary; both are cited.
- CR-4c and loan size (C-7): CR-4c is stated for "how many units of x" an actor takes. Applying it to the size of a loan under a rate cap with a fixed per-loan cost takes an extra step of arithmetic (charge proportional to amount, cost partly fixed) that the rule does not spell out.
- CR-12c and timing windows (C-13 against C-4): 02_ontology 2.5 says timing shifts are signed per window; CR-12 does not mention windows. The analysis treated the window as a separate named market so the two signs are not combined; a sentence in CR-12 would settle this.
- CR-1 operation for the void rule (K2): voiding a loan both removes an option for the lender (enforceable lending) and adds one for the borrower (not repaying). CR-1 handles this as two operations on two classes, which works, but the K2 text is restated existing law and it is unclear whether it changes anything relative to the counterfactual; the analysis treated only its interaction with the new cap as new.
