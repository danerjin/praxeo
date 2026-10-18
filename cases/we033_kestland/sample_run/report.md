# Thin-slice run: Kestland Household Support Payment Act 2027

Rule base: rb-thin-0.7 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-8, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals and the declared comparisons; group signs; announcement windows)  |  Decider: fixture:answers.json  |  Run: 2026-10-18T06:36:47+00:00
Prediction log sha256 (frozen before the outcome card was opened): `d86e26d3c0fe2700…`

## Policy record

- Rule-maker: the Parliament of Kestland; enacted 29 April 2027, effective 1 July 2027.
- Stated aim: none stated
- k1: lump_sum_subsidy on household_cash_payment in kestland; binds households.recipients, protects None. Source: "Households resident in Kestland on 1 April 2027 receive 1,000 crowns per household, once, tax-free, not counted as income for benefits."
- Unclear U1: What a household is: one payment per registered address, or one per tax-filing unit. Readings: U1-a: one payment per registered address / U1-b: one payment per tax-filing unit, so the payments due (about 4.6 million) exceed the borrowing of 4.1 billion crowns
- Unclear U2: How the later installments are funded: higher taxes, lower spending, or both. Readings: U2-a: higher taxes / U2-b: spending restraint
- Citation check: every quoted source sentence was found in the text.
- Verifier: no problems.

## Assumptions (estimated before scoring)

| Atom | Class | p | Text |
|---|---|---|---|

## Consequences

| ID | Actor class | Variable | Sign | Horizon | Tier | Rules | Minimal assumption sets | Reported |
|---|---|---|---|---|---|---|---|---|
| C-1 | households.no_account | compliance_cost | increase | short+ | A | CR-8 | {} | yes |
| C-2 | officials.enforcement | enforcement_cost | increase | short+ | A | OC-3 | {} | yes |
| C-3 | taxpayers.later or public_spending_recipients.later | resources_available_other_uses | at_least_one_decrease | medium+ | A | SB-1, OC-1 | {} | yes |

## Explanations

- C-1. Compared with no Kestland Household Support Payment Act 2027, compliance cost for households.no_account rises from the short run onward (tier A, invisible). Why: CR-8: every payment is a receipt: what one side no longer pays or receives is what the other keeps or loses. This holds if: no assumption. Reported.
- C-2. Compared with no Kestland Household Support Payment Act 2027, enforcement cost for officials.enforcement rises from the short run onward (tier A, invisible). Why: OC-3: the measure must be administered, and a raised budget is paid for by taxpayers. This holds if: no assumption. Reported.
- C-3. Compared with no Kestland Household Support Payment Act 2027, resources available other uses for taxpayers.later or public_spending_recipients.later falls for at least one of them from the medium run onward (tier A, invisible). Why: SB-1: a subsidy is paid by someone: taxes now, or borrowing repaid from taxes later; OC-1: what the payers give up is what they would otherwise have bought. This holds if: no assumption. Reported.

## Score against the outcome card

No outcome card exists for this case (it is fictional), so the run is not scored.
