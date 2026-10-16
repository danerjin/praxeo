# WE-033 One-time household cash payment funded by borrowing

Analyst: draft (Handbook 0.6; corrected under 0.8)  |  Rule catalog version: 0.8  |  Status: awaiting expert review

A stylized policy in a fictional country, chosen to test the core rules on a pure change in means. Every household receives the same sum, and no relative price is changed directly. That is the case covered by CR-4's paragraph "A change in means alone", and it bears directly on `06_gaps.md` Q19 (which purchases rise or fall when means change). The payment is funded by borrowing, so the case also tests CR-8 across time: borrowing now means taxes, or less spending, later; the bondholders are a party to the exchange; and other borrowers compete for the same funds. Catalog 0.7 added OC-8 (crowding out by public borrowing) and the `government_borrowing` instrument, drawn partly from this example's gap notes. The probabilities are illustrative; the evidence column says what a real analysis would cite.

**Out of scope, stated explicitly.** Monetary policy and effects on the general price level are out of scope in version 1. This analysis does not ask whether the payment raises prices in general, whether the central bank responds, or whether the bonds end up held by the central bank. It assumes the bonds are sold to private and foreign buyers, as the Act provides. Where a question can only be answered with monetary analysis, the analysis says so and stops (section 7).

## 1. Policy record

**Kestland Household Support Payment Act 2027.** Kestland is a country of 9.6 million people. Its address register lists 4.0 million households; the Tax Agency has 4.6 million tax-filing units with an adult member. The economy produces about 420 billion crowns a year. Government debt is about 45% of that, and the government sells about 35 billion crowns of bonds in a typical year; about 30% of its bonds are held abroad. About 35% of households report less than one month's income in liquid savings. A survey of intentions by Kestland Statistics in March 2027 found that 30% of households planned to save most of the payment, 40% to pay bills or debts, and 30% to spend it on goods and services. A 2014 energy rebate of 300 crowns per household was followed by higher card spending in the following two months.

The Finance Minister announced the payment in the budget speech on 4 March 2027. Parliament enacted it on 29 April 2027.

| Component | Instrument | Target | Bound | Parameters | Exemptions |
|---|---|---|---|---|---|
| K1 Payment | `lump_sum_subsidy` (cash) | Households resident in Kestland on 1 April 2027 | Tax Agency | 1,000 crowns per household, once, tax-free, not counted as income for benefits. Paid by direct deposit from 1 July 2027 to the 3.4 million households with bank details on file. Others apply by form, with identity documents, by 31 December 2027, and are paid within eight weeks. | None. Non-resident citizens are not eligible. |
| K2 Borrowing | `government_borrowing` | Ten-year "Support Bonds" | Treasury | Up to 4.1 billion crowns, sold at auction from May to August 2027 to banks, pension funds, other private buyers and foreign buyers. Covers the payments and up to 60 million crowns of administration. | None |
| K3 Repayment | Budget rule | Principal and interest on K2 | Treasury | "Repaid from general revenue in ten equal annual installments from 2028." No tax is named. The Finance Ministry says repayment will come "within existing tax rates, through spending restraint". The opposition says taxes will rise. | None |
| K4 Administration and enforcement | Enforcement | K1 | Tax Agency | Payment runs, application processing, a call center, identity checks. Bank details on file can be changed online with a password. False claims must be repaid, with a fine of 2,000 crowns, and may be prosecuted as fraud. Funded from K2. | None |

Unclear provisions:
- **U1.** What a "household" is. The Act defines it as "persons living together at one address and sharing living expenses". The Tax Agency's first guidance pays by tax-filing unit. Reading U1-a: one payment per registered address. Reading U1-b: one payment per tax-filing unit, so an address with an adult child or a lodger who files separately receives two. Under U1-b about 4.6 million payments are due, more than K2's 4.1 billion crowns covers. Readings get no probability; where a sign depends on the reading, one sign per reading is given.
- How the later installments are funded (K3): by higher taxes, lower spending, or both. The record holds statements on both sides but no decision. This is treated as an assumption (A-4), since the record bears on it (`02_ontology.md`, 2.5).

Counterfactual: the same country and years, with no payment, no Support Bonds and no repayment installments.

## 2. Classification

| Component | Rothbard type | Binding? | Rule families |
|---|---|---|---|
| K1 | Binary: the state gives each household a sum. It is the same for all and attached to no purchase, so no relative price changes directly. | Yes | SB-1; CR-4 "A change in means alone", "Means over time" and "Saving is a use" (0.7); CR-8. SB-2, SB-3, SB-5 and SB-6 do not apply, because there is no subsidized good or activity. |
| K2 | A voluntary exchange between the Treasury and bond buyers (CR-5): money now for repayment later. It is not an intervention in Rothbard's types by itself. Its effect on others runs through the loan market (CR-9, CR-6, CR-7). | Yes, as it is sold | OC-8; CR-5, CR-6, CR-7, CR-7c, CR-9 |
| K3 | Binary, later: taxes, or spending withheld from those who would have received it. | Yes for interest; for principal, if the schedule is kept (A-11) | SB-1, TX-1, OC-1 (Who pays: a group), OC-8, CR-8 (borrowing, 0.7) |
| K4 | Binary: administration funded from K2, and so from K3 later. Repayments and fines attach to false claims. | Yes | OC-3, CR-8c, CR-1, CR-4 (comply or violate) |

No `lump_sum_tax` is levied now. The tax side comes later and its form is not decided, so TX-2 to TX-9 are not applied to it (section 9).

## 3. Actor classes

| Actor class | Role | How its options change |
|---|---|---|
| `households.recipients` | Households paid in 2027 | 1,000 crowns more now. |
| `households.no_account` | Recipients without bank details on file | Must apply; paid later. |
| `households.splittable` | Addresses with more than one adult who could form a separate household (adult children, lodgers, separated couples) | Under U1-a, registering a separate address; under U1-b, filing separately, brings a second payment. |
| `households.borrowing_in_advance` | Recipients who borrow against the payment before it arrives | Can buy now and repay from the payment. |
| `households.would_have_borrowed` | Recipients who would have borrowed in July to December 2027 for purchases they now pay with the payment | No loan to repay in 2028. |
| `claimants.false`, `households.defrauded` | People who divert payments or claim twice; households whose payment is diverted | A false claim now brings 1,000 crowns, with repayment, a fine and prosecution attached; the defrauded must report and reclaim. |
| `consumer_lenders` | Banks, card issuers, payday lenders, and firms offering advances against the payment | Some customers borrow before the payment arrives; others borrow less after it. |
| `lenders.new` | Buyers of the Support Bonds and other lenders: banks, pension funds, foreign buyers | Lend 4.1 billion to the Treasury. |
| `bondholders.existing` | Holders of bonds already issued and of fixed-rate loans | The prices of their bonds depend on interest rates. |
| `homeowners` | Owners of homes, which are bought largely with mortgage loans | Home values depend on the rate at which buyers borrow. |
| `owners.consumer_businesses` | Owners of businesses that sell to recipients | Sales rise in the payment window; the rate at which yields are discounted may rise too. |
| `borrowers.private` | Firms and households seeking new loans in 2027 and after | Compete with the Treasury for funds. |
| `sellers.recipients` | Sellers of whatever recipients buy with the payment (not named) | Gain those sales. |
| `sellers.investment_goods_housing` | Sellers of business equipment, commercial building and new homes, financed largely by loans | Lose the purchases of crowded-out borrowers. |
| `sellers.all` | All sellers of goods and services in Kestland taken together | Both of the two rows above. |
| `taxpayers.later`, `public_spending_recipients.later` | Those who pay the installments from 2028 to 2037, through higher taxes, or through spending they no longer receive | Means taken later. |
| `shortfall_bearers` | Under U1-b only: claimants paid less or later, or taxpayers, recipients of other spending and further lenders, if the shortfall is made up | Bear payments due beyond K2. |
| `officials.enforcement` | Tax Agency | New payment and checking task; pays out the payments. |
| `officials.prosecution` | Prosecutors and courts | Fraud cases. |

## 4. Direct effect

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-1 | `households.recipients` | `resources_available_other_uses` | increase | short (July 2027 to February 2028) | SB-1, CR-8b | none |
| C-2 | `officials.enforcement` | `enforcement_cost` | increase | short | OC-3 | none |
| C-3 | `lenders.new` | `quantity_traded` (government bonds bought) | increase | short (May to August 2027) | CR-5, CR-8b | none |
| C-22 | `officials.enforcement` | `subsidy_outlay` | increase | short | CR-1 (op 4), CR-8b | none |
| C-23 | `shortfall_bearers` (claimants paid less or later; or taxpayers, recipients of other spending and further lenders) | `resources_available_other_uses` | U1-a: no_change; U1-b: at_least_one_decrease | short (2027–2028) | CR-8b, CR-8 (0.8: a law that promises more than its budget can pay) | none |

C-1 is the visible effect: each household has 1,000 crowns more. CR-8b records where it comes from: the Tax Agency's outlay (C-22), financed by the bond buyers now (C-3) and by the payers of K3 later (C-19). Under U1-a, the payments (about 4.0 billion crowns) and administration fit within K2. Under U1-b, about 4.6 billion crowns of payments are due, about 0.5 billion more than K2 covers. By CR-8 (0.8), who bears that shortfall is recorded per reading: claimants paid less or later, or, if it is made up, a group of other payers (other spending cut, the Treasury's cash, further borrowing). Under U1-a no one bears it (C-23). C-2 is the Tax Agency's cost of payment runs, applications, the call center and identity checks. It includes checking for diverted and duplicate payments (A-14). It is funded from K2 (OC-3: funded from the policy's own borrowing, so it adds to what K3 repays).

## 5. Responses

| ID | Actor class | Variable | Sign | Horizon | Rules | Assumptions |
|---|---|---|---|---|---|---|
| C-4 | `households.recipients` | `saving` (including repaying debt) | increase | short | CR-3c, CR-8; CR-4 "A change in means alone" and "Saving is a use" | A-2 |
| C-24 | `households.recipients` | `consumption` | increase | short (July to December 2027) | CR-4 "A change in means alone" (A-1 names present goods; A-16 that some are not purchases moved off credit); CR-12e against the rate chain (A-17) | A-1, A-16, A-17 |
| C-5 | `households.no_account` | `compliance_cost` (forms, identity documents, office visits) | increase | short | CR-1 (op 3), CR-8c | none |
| C-6 | `households.splittable` | `reclassification` (forming separate qualifying households) | increase | short (March to April 2027) | RS-5, CR-10a | A-7 |
| C-7 | `consumer_lenders` | `quantity_traded` (credit extended against the expected payment) | increase | short (March to June 2027) | RS-8, CR-10a | A-5 |
| C-25 | `households.borrowing_in_advance` | `consumption` | increase | short (March to June 2027) | RS-8, CR-10a, CR-4 (x: wait for the payment, y: borrow now and repay from it) | A-5 |
| C-8 | `consumer_lenders` | `quantity_traded` (new consumer credit) | decrease | short (July to December 2027) | CR-4 (x: borrow for a purchase, y: use the payment) | A-6 |
| C-26 | `households.would_have_borrowed` | `resources_available_other_uses` | increase | short (2028) | RS-8, CR-10b, CR-8b (loans not taken in 2027 are not repaid in 2028) | A-6 |
| C-27 | `claimants.false` | `legal_breach` (diverted payments, duplicate and false claims) | increase | short | CR-1 (op 3), CR-4 (x: comply, y: violate; y made better where there was no payment to take) | A-14 |
| C-28 | `claimants.false` | `resources_available_other_uses` | increase | short | CR-8b (a diverted payment adds to the fraudster what it takes from the outlay) | A-14 |
| C-29 | `households.defrauded` | `compliance_cost` (reporting and reclaiming) | increase | short | CR-1 (op 3), CR-8c, OC-2 | A-14 |
| C-30 | `officials.enforcement` | `non_tax_receipts` (repayments and fines from detected false claims) | increase | short to medium | CR-1 (op 3), CR-8b | A-14, A-18 |

**What recipients do with the payment (C-4, C-24).** The case was chosen to test this step. The core rules give the following and no more.
- CR-8b and CR-3c: the household's means rise by 1,000 crowns. Every crown goes to some use, and saving and repaying debt count as uses (CR-4, 0.7: "Saving is a use").
- CR-4, "A change in means alone": which uses, and how much each, depends on the household's own ranking, which the rules never assume.
- LW-2 and CR-4c add one thing. The uses added are those the household ranked just below what it could afford before, its next uses in rank. That is a statement about rank, not about goods. It does not say whether the next use is more of something already bought, a new kind of good, a debt paid off, or money kept for later. Because 1,000 crowns is lumpy relative to many purchases, the next use may be a single indivisible item the household could not reach before (a refrigerator, a deposit on a lease) (CR-4, "Units and lumpy costs").
- CR-10a and CR-4's 0.7 clause "Means over time": what households expect about K3 enters their choice now. A household that expects to pay about its share of the later installments has received something close to a loan at the government's rate rather than a gift. For a household that would otherwise borrow at a much higher rate (A-6), that is a fall in the cost of present goods relative to future goods, and CR-4 proper applies, toward present use. A household that expects to bear the installments also has a reason to keep part of the payment to meet them (A-12), an independent chain for C-4 under CR-12d.

So two uses are signed, each with a premise drawn from the record. Some of the payment is saved or used to repay debt (C-4, A-2). Some is spent on present goods and services (C-24, A-1). Present spending needs two further steps. First, A-1 does not separate purchases that would not otherwise have been made from purchases that would have been made on credit anyway (A-6); only the first kind adds to what recipients buy, and A-16 states that some of it is of that kind. Second, the Treasury's borrowing raises interest rates under U1-a (C-9), which makes saving more rewarding and buying on credit dearer: a chain against present spending (CR-4). It is combined under CR-12e with an empirical dominance premise (A-17): rates on household deposits and on card and payday credit move little in 2027, so the higher rate falls mainly on business and mortgage borrowers and does not reach these households' choices in that window. A-17 covers the rate chain in both directions, so it also settles C-24 under U1-b, where the rate is not signed (CR-12, 0.8, an ambiguous chain). No named good is signed, because no premise in the record names one with p ≥ 0.5: the survey reports intentions by broad category, and "goods and services" is not a market. Section 7 says why even "total purchases" cannot be signed.

C-7, C-25, C-8 and C-26 are timing shifts in households' use of credit, signed per window. Between the announcement and the payment, some households borrow against it, through card balances or advance offers (A-5): lenders extend more credit (C-7), and those borrowers consume more in that window (C-25, the borrowers' side that RS-8 asks for). Their consumption in July to December depends on the fees they pay, which no premise states, so it is not signed. After the payment arrives, some who would have borrowed for a purchase pay with it instead (A-6): new consumer credit falls (C-8), and those households have no loan to repay in 2028, so they have more for other uses then (C-26); lenders' repayments received in 2028 fall correspondingly, the other side of the loans in C-8. All these kinds of borrowing happen in the counterfactual too, so each window is signed against it (`02_ontology.md`, 2.5).

C-6 is reclassification (RS-5, CR-4 with x: one household, y: two). Eligibility is fixed on 1 April 2027, so splitting must happen between the announcement on 4 March and that date (CR-10a). Under U1-a, it takes the form of registering a separate address, such as a converted basement. Under U1-b, it takes the form of an adult filing separately. Splitting costs less than a second payment for some households (A-7). The sign is the same under both readings, so one sign is given; the forms differ, and so do the agency's checks.

Fraud (C-27 to C-31). Payments are made to bank details on file, which can be changed online with a password. That invites identity fraud: diverting a household's payment to another account (A-14). Duplicate claims are a related risk, where a direct deposit is followed by a paper application from another member of the same household. Without the payment there was nothing to take, so false claims rise (C-27, `legal_breach`), and what is diverted adds to the fraudsters' means what it takes from the outlay (C-28, CR-8b). A household whose payment is stolen has not lost the payment compared with the counterfactual, in which it receives nothing; its loss of the payment is against what it was promised, which is not this method's baseline (workflow final check 3). The time it spends reporting and reclaiming is a loss against the baseline (C-29). Where the Tax Agency detects false claims (A-18), it recovers repayments and fines (C-30), and prosecution uses resources (C-31). Fraud also raises the agency's checking costs (C-2), and payments made twice or to fraudsters add to what K2 borrows and K3 repays.

Not reported:
- Households delaying purchases in the expectation of a further payment (CR-10a; A-15, p = 0.25).
- Lobbying by retailers for a repeat payment (RS-7; A-13, p = 0.45).

## 6. Second-order effects

| ID | Actor class | Variable | Sign | Horizon | Rules | Market relation | Assumptions |
|---|---|---|---|---|---|---|---|
| C-9 | `borrowers.private` | `interest_rate` (on new loans) | U1-a: increase; U1-b: ambiguous | short to medium | OC-8; CR-9, CR-6, CR-7a; CR-12e (U1-a: accounting identity) | Treasury and private borrowers: `same_market_other_segment` (loanable funds), close | A-1, A-3, A-16 |
| C-10 | `borrowers.private` | `quantity_traded` (new business and mortgage loans) | U1-a: decrease; U1-b: ambiguous | short to medium | OC-8, CR-4c | as C-9 | A-1, A-3, A-8, A-16 |
| C-11 | `sellers.investment_goods_housing` | `quantity_traded` | U1-a: decrease; U1-b: ambiguous | short to medium | OC-1 (naming the forgone uses), CR-9 | loans and investment goods, homes: `complement`, close | A-1, A-3, A-8, A-16 |
| C-12 | `sellers.investment_goods_housing` | `employment`, `hours_worked` | U1-a: at_least_one_decrease; U1-b: ambiguous | short to medium | OC-5 | | A-1, A-3, A-8, A-9, A-16 |
| C-13 | `sellers.recipients` | `quantity_traded` (+), `net_price_received` (+) (markets not named) | at_least_one_increase | short | CR-8b, CR-9, CR-6 (more buyers at each price); CR-4 "A change in means alone" | | A-1, A-16, A-17 |
| C-14 | `sellers.recipients` | `employment`, `hours_worked` | at_least_one_increase | short | OC-5 | | A-1, A-9, A-16, A-17 |
| C-15 | `bondholders.existing` (bonds already issued and fixed-rate loans) | `asset_value` | U1-a: decrease; U1-b: ambiguous | short (from 4 March 2027) | OC-8, CR-7c, CR-10a, CR-10c | new and existing bonds: `substitute`, close | A-1, A-3, A-16 |
| C-16 | `lenders.new` | `return_on_capital` | U1-a: increase; U1-b: ambiguous | short to medium | OC-8, CR-7a | | A-1, A-3, A-16 |
| C-17 | `economy` | `capital_stock_economy` | U1-a: decrease; U1-b: ambiguous | long | CR-7, CR-10b | | A-1, A-3, A-10, A-16 |
| C-32 | `homeowners` | `asset_value` (homes) | U1-a: decrease; U1-b: ambiguous | short to medium (2027–2028) | OC-8, CR-9, CR-7c, CR-10c | homes and mortgage loans: `complement`, close | A-1, A-3, A-8, A-16 |
| C-33 | `owners.consumer_businesses` | `asset_value` | ambiguous | short (from 4 March 2027) | CR-7c, CR-10c (+: sales in the payment window) vs CR-10c (−: a higher rate under U1-a); CR-12b | | A-1, A-16, A-17 |
| C-18 | `sellers.all` | `quantity_traded` (all goods and services taken together) | ambiguous | short | C-13 (+) vs C-11 (−); CR-12b | | A-1, A-3, A-8, A-16 |

**The loan market (C-9 to C-17, C-32).** The Treasury sells 4.1 billion crowns of bonds between May and August. Bond buyers rank the bonds above their other uses for those funds (CR-5), and they are better off by their own ranking. But they would have lent much of that money elsewhere. The Treasury is now one more borrower competing for it (OC-8; CR-9).

Recipients return part of the payment to the loan market by saving it or repaying debt (C-4), and by borrowing less (C-8). What they spend on goods they would not otherwise have bought (A-1, A-16) is not returned; what they spend in place of a purchase they would have made on credit is returned, as borrowing avoided. Under U1-a, the payments (about 4.0 billion crowns) and administration are all borrowed, so what recipients return is at most the payments less the added purchases, which is less than the bonds sold. The net demand for loans therefore rises (CR-12e, an accounting identity on the first round). Where the supply of loans cannot expand at an unchanged rate (A-3), the interest rate rises (CR-6, CR-7a; C-9) and private borrowers take fewer loans (C-10). A-3 is a premise because foreign lenders may supply most of the extra funds at the going rate. Under U1-b, about 4.6 billion crowns is paid out, about 0.5 billion more than is borrowed, and the rest comes from an unnamed source (C-23). If it comes from cuts to other spending or from the Treasury's cash, recipients could return more to the loan market than the Treasury takes from it, and the identity no longer settles the sign. No premise in the record compares recipients' added purchases with that 0.5 billion, so under U1-b the rate and everything downstream of it are `ambiguous`.

Who is crowded out is the one place in this case where a named use is reached with a strong premise. In the loan market, the marginal borrowers are those whose projects or purchases are just worth the old rate. Credit statistics show that most private borrowing finances business investment and home purchases (A-8). So it is those sellers whose sales fall (C-11), and with them work in those sectors (C-12, OC-5). The use is named from the composition of the market through which the means are taken, not from anyone's ranking of ends (OC-1, "Naming the forgone uses", added in 0.7 from this example).

C-15 is CR-7c. When rates rise, existing bonds and fixed-rate loans bring their holders less than new ones, so their price falls until a buyer expects to earn on them what new bonds pay. The issuance was expected from the announcement on 4 March, so the fall is borne by holders from then (CR-10a). C-16 is the same movement seen from lenders. C-17 is depth 4 (payment, Treasury borrowing, loans, investment, capital). Less investment in 2027 and 2028 leaves a smaller stock of capital later, unless it is made up afterwards (A-10). TS-9's effect on wages would be depth 5, so the chain stops at C-17.

C-32. Homes are bought largely with mortgage loans (A-8), so a higher mortgage rate lowers what buyers will pay for the same expected yield from a home, for the period the rate is higher (CR-9, CR-7c, CR-10c). An opposing chain exists: recipients could spend part of the payment on housing (a deposit toward a purchase, a higher rent), which would raise home values. The rules derive it, but only with a premise the case lacks: nothing in the record names housing as a use of a 1,000-crown payment. Under CR-12 (0.8), the premise is stated with its probability (A-19, p = 0.3); being below 0.5, it does not make the sign ambiguous, and the chain is recorded in section 10. Under U1-b the rate itself is not signed, so neither are home values.

C-33. Businesses that sell to recipients expect higher sales in the payment window, which is capitalized from the announcement for the yields it affects (CR-7c, CR-10c). The same higher rate that lowers the value of bonds and homes lowers the present value of every expected yield, including theirs. No premise says which dominates, so the sign is `ambiguous` (CR-12b); under U1-b the rate chain is itself ambiguous, which does not change that.

C-13 and C-14 are Hazlitt's tailor in reverse. The part of the payment that recipients add to their purchases (A-16) is received by whoever sells to them. More buyers at each price means that either more is sold or the terms move toward sellers (CR-6); quantity alone would need a premise that sellers' supply is not fixed in the short run, so the two are a group with `at_least_one_increase`. Those sellers are not named, for the reasons given under C-24. Their sales rest on A-17 as well, since C-24 does.

## 7. Combined effects

| Actor class, variable, horizon | Chains (+) | Chains (−) | Dominance rule | Combined sign |
|---|---|---|---|---|
| `borrowers.private`, `interest_rate`, short to medium | The Treasury's added demand for loans of about 4.1 billion crowns, with loan supply not perfectly elastic (OC-8, CR-6, CR-7a, A-3). | Recipients' saving, debt repayment and borrowing avoided add to loan supply or reduce loan demand (C-4, C-8). | U1-a: CR-12e, an accounting identity on the first round: what recipients return is at most the payments less their added purchases (A-1, A-16: greater than zero), which is less than the bonds sold. U1-b: none, since payments exceed the bonds and the source of the rest is unclear. | **U1-a: increase; U1-b: ambiguous** (C-9), and C-10 to C-12, C-15 to C-17 and C-32 per reading with it. |
| `households.recipients`, `consumption`, July to December 2027 | Part of the payment spent on present goods not otherwise bought (A-1, A-16); for credit-constrained households, a loan at the state's rate (CR-4, means over time). | A higher rate makes saving more rewarding and buying on credit dearer (CR-4). | CR-12e with an empirical premise (A-17): household deposit and credit rates move little in 2027. It covers the rate chain in either direction, so it holds under both readings. | **increase** (C-24). |
| `owners.consumer_businesses`, `asset_value`, short | Expected sales in the payment window (CR-7c, CR-10c). | A higher discount rate under U1-a (CR-10c). | None | **ambiguous** (C-33). |
| `homeowners`, `asset_value`, short to medium | Recipients' spending on housing: derivable only with a premise the case lacks (A-19, p = 0.3). | A higher mortgage rate under U1-a (CR-9, CR-7c, CR-10c). | CR-12 (0.8): a chain whose premise has p below 0.5 does not make the sign ambiguous; it is recorded in section 10. | **U1-a: decrease; U1-b: ambiguous** (C-32). |
| `sellers.all`, `quantity_traded` (all goods and services taken together), short | Recipients spend part of the payment (C-13). | Crowded-out borrowers buy fewer investment goods and homes (C-11). | None | **ambiguous** (C-18). Under CR-8, the funds recipients spend were lent to the Treasury, and would otherwise have gone to the crowded-out borrowers. The two chains offset each other in full only where all the funds came from domestic lenders at a rate that moved enough to clear the market. How far they do not offset depends on foreign lending (A-3) and on whether lenders draw down money holdings they would otherwise have kept idle. The second is a monetary question and out of scope in version 1, so the method stops here. |
| Employment across sectors, short | Sellers to recipients (C-14). | Sellers of investment goods and homes (C-12). | None | **ambiguous**, for the same reason. The visible jobs are where recipients spend; the invisible ones are in building and equipment. |
| `households.recipients`, `resources_available_other_uses`, short vs later | The payment, July 2027 (C-1). | Their share of K3, 2028 to 2037 (C-19). | Not applied: chains at different horizons are not combined (CR-12g). A `whole period` consequence would need a dominance premise (CR-12g, 0.7); none clears the cut-off (below). | **increase** in the short run (C-1). For the later window, see C-19 (a group sign over payers). |

**Who gains and who loses over the whole period.** Some households will pay much more in K3 than they received, and others much less. The top fifth of taxpayers pays about 60% of income tax. If the installments are paid through income tax, such a household would pay about three times its payment over ten years, and a household that pays little income tax, or that leaves the country or the tax roll before 2028, receives 1,000 crowns and pays back little or nothing. For such a household the undiscounted later sum would be smaller than the payment, and LW-7 says discounting can only shrink it, so CR-12g's 0.7 clause would allow a `whole period` sign. But that arithmetic rests on the installments being paid through income tax (A-4, p = 0.45, below the cut-off). Under spending cuts, no premise identifies who pays. So no whole-period consequence is reported, and the method records separate signs per window: an increase now and a decrease later.

**What expectations change.** Households that expect to bear the later installments have more reason to save the payment (CR-10a). Households that do not expect to, or that are credit-constrained, have more reason to spend it. This changes how much of C-4 and C-24 happens, and A-12 (p = 0.6), that many households expect to bear part of the later cost, gives C-4 a second, independent chain (CR-12d); it is not needed for either sign. If households fully expected to repay exactly their share at the government's rate, and could borrow and lend at that rate themselves, K1 would change nothing in their choices. The cases where it does change something are the departures from that: credit constraints (A-6), unequal shares of K3, and people who will not pay K3 at all.

**The installments and later sellers.** From 2028, the payers of K3 have less (C-19). Which uses they give up is not signed: saving is a use (OC-1; CR-4, 0.7), and some payers, such as pension savers and firms, may meet part of the installments by saving or lending less. The installments are received by bondholders, which is a further chain on any aggregate of later purchases. So no sign is given for sellers after 2027; the 0.6 version's decreases in later sellers' sales and jobs are withdrawn (see the corrections note). For the same reasons, private interest rates during repayment are not signed: principal repaid to bondholders is lent again (A-11), while payers may lend less.

## 8. Time structure

| Window | What happens | Consequences |
|---|---|---|
| 4 March to 30 June 2027 (announcement to payment) | Some households borrow against the payment and consume more (A-5). Households split before the qualifying date of 1 April (A-7). The value of existing bonds, homes and consumer businesses moves from the announcement. The Treasury sells bonds from May. | C-6, C-7, C-25; C-15, C-32, C-33; C-3, C-9 begin |
| July to December 2027 | Direct deposits from 1 July; recipients spend part, save part, and borrow less. Fraud attempts peak around the deposit runs. | C-1, C-4, C-8, C-13, C-14, C-22, C-24, C-27 to C-29 |
| January and February 2028 | Late applicants are paid. Under U1-b, the payments beyond K2 must be found. | C-1 (for `households.no_account`), C-5, C-23 |
| 2028 | Households that did not borrow in 2027 have no loan to repay. Detected false claims are repaid and prosecuted. | C-26, C-30, C-31 |
| 2027 to about 2029 | Under U1-a, higher rates; fewer business and mortgage loans; fewer purchases of investment goods and new homes. | C-9 to C-12, C-15, C-16, C-32 |
| 2028 to 2037 | Ten installments of principal and interest, from taxes or spending cuts. | C-19 |
| After 2037 | Under U1-a, a smaller capital stock than otherwise, unless it was made up (A-10). | C-17 |

Spending by recipients is moved in time only in part. The payment adds to recipients' means in 2027 (C-1) and the installments take from payers' means in 2028 to 2037 (C-19). These are signed per window, with different actor classes, because the later payers are not the same people as the recipients: taxpayers include firms and people who received nothing, and public spending cuts fall on its recipients. Recipients' added consumption in 2027 is signed (C-24). The later payers' purchases are not, because which uses they give up needs a premise (section 7).

Two timing shifts in credit are signed per window. Advance borrowing: credit and consumption rise in March to June 2027 (C-7, C-25). Borrowing avoided: new credit falls in July to December 2027 (C-8), and those households have more for other uses in 2028 (C-26).

Under reading U1-b, the payments due exceed K2's 4.1 billion crowns by about 0.5 billion. Under CR-8b, that sum must come from somewhere in 2027 and 2028: claimants paid less or later, other spending, the Treasury's cash, or further borrowing. Under U1-a it does not arise. Catalog 0.7 added the sign `no_change`, so this chain is now recorded per reading (C-23).

## 9. Opportunity costs

| ID | Actor class | Variable | Sign | What is given up | Rules |
|---|---|---|---|---|---|
| C-19 | `taxpayers.later`, `public_spending_recipients.later` | `resources_available_other_uses` | at_least_one_decrease | About 4.1 billion crowns plus interest, in ten installments from 2028: through higher taxes, or through spending that its recipients no longer receive (pensions, services, public wages), or both. Two independent chains (CR-12d): interest is paid from general revenue under K3 in any case, and principal is repaid on the schedule if the debt is not rolled over (A-11). | SB-1, OC-1 (Who pays), OC-8, CR-8a, CR-8b |
| C-23 | `shortfall_bearers` | `resources_available_other_uses` | U1-a: no_change; U1-b: at_least_one_decrease | Under U1-b, about 0.5 billion crowns of payments beyond K2. | CR-8b, CR-8 (0.8) |
| C-5 | `households.no_account` | `compliance_cost` | increase | Time spent on forms and visits. | CR-8c |
| C-29 | `households.defrauded` | `compliance_cost` | increase | Time spent reporting a diverted payment and reclaiming it. | CR-8c, OC-2 |
| C-2 | `officials.enforcement` | `enforcement_cost` | increase | Up to 60 million crowns of staff time, systems and checks, used up (CR-8c). Borrowed under K2, so repaid under K3. | OC-3 |
| C-31 | `officials.prosecution` | `enforcement_cost` | increase | Prosecuting detected false claims (A-14, A-18), funded from the general budget. Its payers are recorded with the other general-budget payers, not separately. | OC-3, CR-8c |

Not signed: what the payers of K3 would have bought (section 7). The 0.6 version recorded later sellers' sales (`quantity_traded` decrease) and their staff or hours (`at_least_one_decrease`) as C-20 and C-21; both are withdrawn, because OC-1's "Saving is a use" clause requires a premise that the payers cut purchases rather than saving, and the bondholders who receive the installments are a further chain.

Both sides of every transfer:
- *Payment:* the Tax Agency pays (C-22), recipients receive (C-1); funded by bond buyers now (C-3) and K3 payers later (C-19). Under U1-b, the shortfall's bearers (C-23).
- *Bonds:* buyers give funds now and receive principal and interest later. They gain by their own ranking (CR-5), and their yield is higher if rates rise (C-16). The later installments are a transfer from K3's payers to bondholders (CR-8b; OC-8). In the counterfactual, the bondholders would have been repaid by private borrowers out of the returns on what those borrowers built or bought.
- *Crowding out:* the funds lent to the Treasury are funds not lent to private borrowers (C-10). What those borrowers would have bought is not bought (C-11).
- *Credit timing:* lenders extend less credit in July to December 2027 (C-8) and receive fewer repayments in 2028; the households that did not borrow have more in 2028 (C-26).
- *Fraud:* diverted payments add to fraudsters' means (C-28) and are part of the outlay (C-22); detected claimants repay and pay fines to the Tax Agency (C-30).
- *Interest:* about a third of the bonds are held abroad, so part of the later installments goes to foreign holders. This follows the `currency` relation (TX-8's logic in reverse) and is not followed further.

## 10. Assumptions

| ID | Statement | Type | p | Evidence | If false |
|---|---|---|---|---|---|
| A-1 | Some recipient households spend part of the payment on present goods and services within six months, rather than saving it all or repaying debt. | other | 0.9 | 35% of households have less than a month's income in liquid savings; the survey (30% plan to spend); card spending after the 2014 rebate. | C-13, C-14 not reported; C-9 to C-12, C-15 to C-17 not reported (no net new demand for loans). |
| A-2 | Some recipient households save part of the payment or use it to repay debt. | other | 0.9 | The survey (30% save, 40% bills or debt). | C-4 not reported. |
| A-3 | The supply of loans to Kestland is not perfectly elastic in 2027 and 2028: foreign lenders do not supply all the extra funds at the going rate. | other | 0.6 | Support Bonds add about 12% to a typical year's issuance; foreign share 30%; past auction results. | C-9 to C-12, C-15 to C-17 not reported. |
| A-4 | The installments are funded mainly by higher taxes rather than lower spending. | revenue_use | 0.45 | The Finance Ministry says spending restraint; the opposition says taxes; fiscal rules allow either. | Below the cut-off. C-19 is recorded as a group over taxpayers and spending recipients; no TX chain is reported on the later taxes. |
| A-5 | Some households borrow against the expected payment before it arrives. | expectations | 0.55 | Advance products advertised after 4 March; card balances before the 2014 rebate. | C-7 not reported. |
| A-6 | Some recipients would have borrowed in July to December 2027 for purchases they now pay with the payment. | other | 0.8 | Share of households using card credit or payday loans for routine purchases. | C-8 not reported. |
| A-7 | For some households, forming a separate qualifying household costs less than a second payment. | other | 0.7 | Number of addresses with more than one tax-filing unit (600,000); cost of a separate registration or filing. | C-6 not reported. |
| A-8 | Most private borrowing at the margin finances business investment and home purchases. | other | 0.75 | Central bank credit statistics by purpose. | C-10 to C-12 lose their named sellers; C-18 loses its minus chain as stated. |
| A-9 | Sellers adjust staff or hours to sales within months. | alternative_uses | 0.8 | Share of hourly and part-time staff; scheduling practice. | C-12, C-14, C-21 not reported. |
| A-10 | Investment crowded out in 2027 and 2028 is not fully made up in later years. | durability | 0.6 | Projects deferred or cancelled when rates rise; planning horizons. | C-17 not reported. |
| A-11 | The bonds are repaid on the ten-year schedule rather than rolled over. | expectations | 0.6 | Fiscal rules; past practice with special-purpose bonds. | C-19 to C-21 move later, beyond 2037; the same signs, at a later horizon. |
| A-12 | Many households expect to bear part of the later installments. | expectations | 0.6 | Survey question on expected taxes. | Changes magnitudes only; attached to no consequence (section 7). |
| A-13 | Retailers can organize to press for a repeat payment, and expect a chance of success. | other | 0.45 | Retail association statements; the government calls the payment one-time. | Below the cut-off; lobbying not reported. |
| A-14 | Some payments are diverted by identity fraud, or made twice. | enforcement | 0.7 | Online change of bank details by password; experience of other one-time payments. | The fraud part of C-2 is smaller; C-2's sign does not change. |
| A-15 | Many households expect a further payment and delay purchases to wait for it. | expectations | 0.25 | The Act and the government call the payment one-time. | Below the cut-off; not reported. |

**Final check before the report** (workflow).
1. *Uncombined chains.* All purchases taken together (C-18) and employment across sectors have opposing chains and are `ambiguous`. The interest rate (C-9) has recipients' saving and lower borrowing pushing it down, against the Treasury's borrowing pushing it up. These are combined by arithmetic: the net change in demand for loans equals the part of the payment spent, which is positive under A-1 (CR-12e, arithmetic on the case's identity). The sign is therefore an increase given A-3.
2. *Group signs.* C-12, C-14 and C-21 are groups over `employment` and `hours_worked`. C-19 is a group over two actor classes (Gaps (d)).
3. *Baseline.* Signs are against no payment, no bonds and no installments, not against what households were promised. Stolen payments are therefore not a loss against the baseline (section 5).
4. *Worse off is not poorer.* `resources_available_other_uses` is signed for recipients (a sum received) and for K3's payers (a sum they cannot avoid). It is not signed for bond buyers, who chose to lend.
5. *Timing.* Credit (C-7, C-8) and household spending (C-13, C-20) are signed per window.
6. *Both sides.* See section 9.
7. *Every class, every core rule.* CR-7c is applied to existing bonds (C-15). No other asset is tied to the payment. Houses are reached only through C-11, and their prices are not signed, because rates (−) and recipients' spending (unnamed) give no premise on house prices.
8. *Premises.* That some households spend, and some save, is each stated with a probability (A-1, A-2). Neither is taken as given.

## 11. Report

**The policy.** Kestland pays every household 1,000 crowns once, from July 2027. It borrows the money by selling ten-year bonds, and repays them from general revenue in ten installments from 2028.

**Visible consequences.** Every household has 1,000 crowns more in the second half of 2027 (C-1). The Tax Agency pays out and checks the payments (C-2). Banks, pension funds and foreign buyers buy the new bonds (C-3). Some of the payment is spent, and sellers to recipients sell more (C-13), with more work there (C-14).

**Invisible consequences.**
- *Recipients* save part of the payment or repay debts (C-4). Some borrow against it before it arrives, and some borrow less after (C-7, C-8). Households without bank details on file spend time applying (C-5). Some households split to receive a second payment (C-6).
- *Private borrowers* face higher interest rates and take fewer loans (C-9, C-10). Sellers of business equipment, commercial building and new homes sell less (C-11), with less work there (C-12). Holders of existing bonds see their value fall (C-15), while new lenders earn more (C-16). In the long run the economy has less capital than it would have had (C-17).
- *From 2028 to 2037*, taxpayers pay more or recipients of public spending receive less, or both (C-19). The sellers they would have bought from sell less (C-20), with less work there (C-21).

**Ambiguous effects.** Whether total purchases of goods and services in Kestland in 2027 rise (C-18), and whether total employment rises. Recipients spend more; crowded-out borrowers spend less. Settling the balance needs monetary analysis, which is out of scope.

**Key conditions.** That some recipients spend part of the payment (A-1, p = 0.9) is what makes net borrowing rise at all. That foreign lenders do not supply all of it at the going rate (A-3, p = 0.6) is what makes rates rise and private borrowing fall. Whether the later installments come from taxes or from spending cuts (A-4, p = 0.45) is not settled by the record, so the later burden is reported as falling on one group or the other.

**What this analysis cannot say.**
- Which goods recipients buy. No premise names one, and the core rules do not name one without it (CR-4; Q19).
- How much of the payment is spent rather than saved, or how large any effect is.
- Whether total spending or employment in 2027 rises.
- Whether a given household gains or loses over the whole period. The method does not combine the payment now with the installments later, even where the arithmetic is lopsided.
- Anything about the general price level, inflation, monetary policy or the exchange rate. These are out of scope in version 1.
- Whether the transfer is fair or the policy worthwhile.

## Consequence list (normal form)

| ID | Actor class | Variable | Sign | Horizon | Visibility | Tier | Derivation | Assumptions |
|---|---|---|---|---|---|---|---|---|
| C-1 | households.recipients | resources_available_other_uses | increase | short (Jul 2027–Feb 2028) | visible | A | SB-1, CR-8b | none |
| C-2 | officials.enforcement | enforcement_cost | increase | short | invisible | A | OC-3 | none |
| C-3 | lenders.new | quantity_traded (government bonds) | increase | short (May–Aug 2027) | visible | A | CR-5, CR-8b | none |
| C-4 | households.recipients | saving (incl. debt repaid) | increase | short | invisible | B | CR-3c, CR-8; CR-4 (means alone) | A-2 |
| C-5 | households.no_account | compliance_cost | increase | short | invisible | A | CR-1, CR-8c | none |
| C-6 | households.splittable | reclassification (separate households) | U1-a: increase; U1-b: increase | short | invisible | B | RS-5 | A-7 |
| C-7 | consumer_lenders | quantity_traded (credit against the payment) | increase | short (Mar–Jun 2027) | invisible | B | RS-8, CR-10a | A-5 |
| C-8 | consumer_lenders | quantity_traded (new consumer credit) | decrease | short (Jul–Dec 2027) | invisible | B | CR-4 | A-6 |
| C-9 | borrowers.private | price_paid (interest rate on new loans) | increase | short–medium | invisible | B | CR-9, CR-6, CR-7a; CR-12e | A-1, A-3 |
| C-10 | borrowers.private | quantity_traded (new business and mortgage loans) | decrease | short–medium | invisible | B | CR-4c | A-1, A-3, A-8 |
| C-11 | sellers.investment_goods_housing | quantity_traded | decrease | short–medium | invisible | B | CR-9 | A-1, A-3, A-8 |
| C-12 | sellers.investment_goods_housing | employment, hours_worked | at_least_one_decrease | short–medium | invisible | B | OC-5 | A-1, A-3, A-8, A-9 |
| C-13 | sellers.recipients | quantity_traded (markets not named) | increase | short (2027) | visible | B | CR-8b, CR-9; CR-4 (means alone) | A-1 |
| C-14 | sellers.recipients | employment, hours_worked | at_least_one_increase | short | visible | B | OC-5 | A-1, A-9 |
| C-15 | bondholders.existing | asset_value (existing bonds) | decrease | short | invisible | B | CR-7c, CR-10c | A-1, A-3 |
| C-16 | lenders.new | return_on_capital | increase | short–medium | invisible | B | CR-7a | A-1, A-3 |
| C-17 | economy | capital_stock_economy | decrease | long | invisible | B | CR-7, CR-10b | A-1, A-3, A-10 |
| C-18 | sellers.all | quantity_traded (all goods and services) | ambiguous | short | invisible | B | C-13 vs C-11; CR-12b | A-1, A-3, A-8 |
| C-19 | taxpayers.later, public_spending_recipients.later | resources_available_other_uses | at_least_one_decrease | medium–long (2028–2037) | invisible | B | SB-1, CR-8a, CR-8b | A-11 |
| C-20 | sellers.later | quantity_traded (markets not named) | decrease | medium–long (2028–2037) | invisible | B | OC-1 | A-11 |
| C-21 | sellers.later | employment, hours_worked | at_least_one_decrease | medium–long (2028–2037) | invisible | B | OC-5 | A-9, A-11 |
| — | all sectors | employment, hours_worked | ambiguous | short | invisible | B | C-14 vs C-12; CR-12b | A-1, A-3, A-8, A-9 |

## Gaps found

**(a) Calculus gaps.** None. Every step was derived from CR-1 to CR-12, or from a pattern. The one place the analysis stops, the effect on total spending (C-18), stops because of the version 1 scope (monetary effects), not because no core rule applies. CR-6 would apply to the demand for money as to any good, but the method excludes that market for now.

**(b) Unclear core rules.**
- **CR-4, "A change in means alone", across time.** The paragraph treats a lump-sum grant as a change in means with no change in relative cost. A grant funded by borrowing is not that, for any household that expects to bear part of the repayment (CR-10a). For such a household it is closer to a loan at the government's rate. Where the household's own borrowing or lending rate differs from that rate, it changes the relative cost of present and future goods. CR-4's ordinary direction then applies, toward the present for credit-constrained households. The paragraph should say: "A change in means now matched by an expected change in means later is a change in the relative cost of present and future goods for actors whose own rate of borrowing or lending differs from the rate implied; CR-4's ordinary rules apply to that part".
- **CR-4, which use is added (Q19).** The paragraph says which uses rise "depends on the actor's ranking". It does not say that saving and repaying debt are among the uses, that the use added is the next in rank (LW-2), or that with lumpy goods it may be a new kind of good rather than more of an old one. All three were needed here (C-4).
- **CR-12g against CR-12e and LW-7.** CR-12g forbids combining chains at different horizons. CR-12e allows a dominance premise from arithmetic on the case's figures. For a household that receives 1,000 crowns now and pays back less than that later in undiscounted money, LW-7 guarantees the net is positive at any positive rate of time preference. No magnitude or discount rate is needed, yet CR-12g blocks the conclusion. Proposed clause for CR-12g: "unless the later chain is smaller than the earlier one before discounting, and they are opposite in sign. Then, by LW-7, the earlier one dominates over the whole period, and a combined sign may be given for a variable that spans both". This would also need a variable for means over a whole period (see (d)).
- **CR-8, "borrowing now means taxes later".** CR-8 holds this only implicitly, through CR-8b (the bonds are repaid by someone). SB-1 states it, but only for subsidies. The step needs a premise that the debt is repaid rather than rolled over indefinitely (A-11). CR-8 could say so: "a payment funded by borrowing is a claim on later payers, whose timing depends on whether the debt is repaid or rolled over".

**(c) Missing patterns.**
- **Proposed OC-8: crowding out by public borrowing.** *If:* a policy is funded by government borrowing, and recipients spend part of what it pays for (or, for purchases, the state spends it). *Then:* `price_paid` (interest rate) for private borrowers increases and their `quantity_traded` of new loans decreases. The purchases those borrowers would have financed decrease: `quantity_traded` decrease for their sellers, named from the composition of private borrowing. Existing bonds' `asset_value` decreases. *Assumes:* loan supply not perfectly elastic (`other`), and the composition of marginal borrowing. *Derivation:* CR-8a and CR-8b (funds lent to the state are not lent elsewhere), CR-9 to the loan market, CR-6 and CR-7a there, CR-7c for existing bonds, CR-9 to borrowers' sellers. It is likely to recur in every case funded by borrowing (SB-1 already mentions borrowing).
- **Proposed clause for OC-1 and SB-1: naming the forgone use.** Where means are taken through a market (borrowing, a sale of assets), the forgone uses are those of the marginal participants in that market. They can be named from that market's composition, with a premise. Where means are taken or given as a lump sum, they cannot be named without a premise about the payers' or recipients' rankings. This is the main finding for Q19 below.
- **Proposed TS-10: debt-financed transfer, two windows.** *If:* a transfer now is funded by debt repaid later. *Then:* the recipients' means increase in the payment window, and the repayers' means decrease in the repayment windows. Spending by each is signed per window, with different actor classes, and they are not netted (CR-12g). *Derivation:* CR-8b, CR-10a, CR-12g.

**What the case shows about Q19 (which purchases fall or rise when means change).**
1. *The core rules give only the total.* The recipient's means rise by the payment (CR-8b), and each crown goes to some use, including saving and repaying debt (CR-3c). No named purchase follows. The case confirms the WE-004 finding from the other side.
2. *LW-2 gives a statement about rank, not about goods.* The use added is the one ranked next below the old margin, and when means fall, the use given up is the last one. That is a priori, and it answers Q19's suggestion: yes, the marginal use is the one added or given up. But knowing a household's marginal use requires knowing its ranking, and the rules never assume one. With lumpy goods, the next use may be a whole item not bought before, so not even "more of what is already bought" follows. The suggestion therefore does not let the analyst name a good.
3. *Even the split between present and future is not a priori.* Saving is a use like any other. In this case the split needed two premises with evidence (A-1, A-2), not a rule.
4. *Two sources of nameable uses were found, and neither comes from the actor's ranking.* (a) Where means pass through a market, the marginal participants in that market can be identified from its composition (A-8): crowded-out borrowers are firms investing and households buying homes. (b) Where a debt-financed transfer changes the relative cost of present and future goods for credit-constrained actors, CR-4's ordinary direction applies (toward present use), but it still names no good.
5. *Proposed resolution of Q19.* Keep the rule that a named use needs a premise for lump-sum changes in means. Add that the use is the next or last in the actor's own ranking (LW-2), which is a priori but does not name a good. Add that changes in means made through a market are named from the composition of that market's marginal participants, with a premise (proposed OC-8 and the OC-1 clause). Experts should confirm whether point 2 is the praxeological ground Q19 asks for, or only a restatement of it.

**(d) Vocabulary.**
- **Instrument types (2.3).** There is no type for government borrowing, or for a repayment rule. K2 and K3 were described in words. Proposed: `public_borrowing`.
- **Group signs over actor classes (2.5).** C-19 needs "at least one of these actor classes" (taxpayers or recipients of public spending), with one variable. 2.5 defines group signs only over variables.
- **No "no change" value for readings (2.5).** Under U1-b, about 0.5 billion crowns must be found in 2027; under U1-a, nothing. The reading field can give one sign per reading, but none of the signs means "this chain does not arise under this reading". The chain was left out of the consequence list (section 8). Proposed: allow `none` as a per-reading value.
- **Variables (2.4).** The following are missing:
  - an aggregate of a class's purchases of goods and services (consumption). `quantity_traded` for unnamed "sellers" was used instead (C-13, C-18, C-20);
  - interest rates. `price_paid` on loans was used (C-9);
  - fraudulent or duplicate claims. Fraud could be recorded only through `enforcement_cost` (C-2);
  - an actor class's means over a whole period, which (b)'s proposed CR-12g clause would need.
