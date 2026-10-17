# praxeo: Phase 2 thin slice

Plan §5.5 step 1: one rule family, one worked example, one historical case, run end to end. Every stage is crude. The point is that the stages connect and that scoring code exists.

```
policy.txt ──parser──▶ PolicyRecord ──context (sources before enactment)──▶ typed questions ──▶ Decider ──p per assumption──▶
clingo engine, once per reading of each unclear provision ──▶ consequences + derivations + minimal assumption sets ──▶
CR-12 combiner (subclass totals) ──▶ verifier ──▶ templated explainer ──▶ prediction.json (frozen, hashed) ──▶
outcome card opened ──▶ score.json, report.md
```

## Run

```
pip install -e '.[test]'           # pydantic, clingo, anthropic, pytest
python3 -m praxeo cases/sf_1994     # fixture parser and fixture decider (offline)
python3 -m pytest tests
```

Options: `--parser fixture|llm`, `--decider fixture|llm|human`, `--out DIR` (default `runs/…`, git-ignored), and `--thresholds PATH --fallback fixture|human|llm [--fallback-answers PATH]` to escalate low-confidence answers (example thresholds in `cases/sf_1994/thresholds.example.json`; real ones must come from the labelled question bank). The LLM parser and decider call Claude through the Anthropic SDK with structured outputs (`messages.parse` into the pydantic schema) and need `ANTHROPIC_API_KEY`. A sample offline run is committed in `cases/sf_1994/sample_run/`.

## Stages

| Module | Stage (plan) | What it does now |
|---|---|---|
| `schema.py` | typed records | PolicyRecord, Component, Unclear, Question, Answer, Assumption, Consequence, Step, Source, OutcomeCard, Finding. |
| `vocabulary.py` | shared vocabulary (7.4) | Reads the controlled variable list from `handbook/02_ontology.md` §2.4, the single source of truth. The verifier, the scorer and a test check the rule base and every outcome card against it. |
| `context.py` | context grounding (5.3) | Adds dated sources from `sources.json` to the record's context only if they were published before enactment, and logs the ones held back. If the record has no enactment date, it holds every source back. |
| `parser.py` | LLM parser (5.2) | Fills PolicyRecord from text; each component quotes its source sentences; `check_citations` verifies the quotes in code. Fixture backend loads `record.json`. |
| `questions.py` | typed questions (4.4) | Dispatched by instrument. Nine noul questions per price ceiling, one per assumption the rules name (binding, enforced, alternative_uses, nontransferable, buyouts_limited, would_leave, lockin_dominates, keepers_dominate, substitutes). Three per per-unit tax (quantity_responds, buyers_bear, sellers_bear), three per tariff (binding, domestic_substitutes, no_offset), and, when the record names downstream users of the good as an input, input_not_replaceable and, if their competitors are exempt, competitors_exempt. |
| `decider.py` | Decider interface (5.2) | FixtureDecider, LLMDecider, HumanDecider behind one `answer(question, record)` call. A Jev decider would slot in here. |
| `escalation.py` | confidence thresholds and escalation (5.4) | Thresholds per question kind and per assumption class, loaded from JSON; `EscalatingDecider` asks a fallback decider for any answer below threshold and logs each escalation. Off unless `--fallback` is given; thresholds must come from the question bank. |
| `rules/price_controls.lp` | rule base (4.4) | Covers PC-1 (the plan's PR-017) with the 1.4 vacancy-decontrol note, PC-3 with RS-4, PC-5, RS-5, PC-7 and PC-21 as revised in 1.4 (buyout and dominance premises, keepers and displaced as separate subclasses). Each rule has an `exception/2` default. |
| `config_b.py` | Configuration B (5.2) | The same price-ceiling rules as a list of steps, with no engine: a step is asked only if the steps it needs held, and holds at P(yes) ≥ 0.5. Logs every question asked. `compare_a_b` runs A and B on one record and decider and reports which (actor, variable, sign) rows agree. |
| `rules/taxes.lp` | rule base (4.4) | Covers TX-1 (revenue; resources of those who bear the tax), TX-2 (wedge and smaller market for a per-unit tax, and fewer imports for a tariff), TX-7 (tariff: buyers' price up, protected producers' price and quantity up, with the `Unless` exception), TX-8 (exporters and their workers sell and employ less, given no offset) and RS-14 (input cost passed down: price where competitors face the same cost, quantity where they are exempt). Same style as the ceiling rules. The incidence split of a per-unit tax (DM-1) is two assumptions, not a rule. TX-3 to TX-6 and TX-9 to TX-12 are not encoded. |
| `engine.py` | symbolic engine, Configuration A (5.4) | Loads every `.lp` file in `rules/`. Writes facts (`ceiling`, `tax`, `tariff` and the actor roles the record names), opens a choice over assumptions, enumerates answer sets, and labels each conclusion with its minimal assumption sets (ATMS-style). A consequence is reported when its most probable minimal set has every p ≥ 0.5. It runs once per reading of each unclear provision that carries `reading_facts`; where the readings disagree, the consequence gets a sign per reading. |
| `combiner.py` | effect combiner (CR-12) | Forms the total for a class from subclasses whose chains run in opposite directions (PC-21 keepers against the displaced). The total is `ambiguous` unless a dominance premise with p ≥ 0.5 settles it. |
| `verifier.py` | verifier | Checks every consequence. Its variable must be in the vocabulary and its actor class must have a known role (the ontology's, or one the record names). Every premise must be a record fact, an estimated assumption or an earlier conclusion. `reported` must agree with the cut-off, and per-reading signs must name existing readings. |
| `explainer.py` | templated explainer | One sentence per consequence from the derivation steps; no free text. |
| `scoring.py` | scoring (7.3, 7.4) | Headline and logic precision, recall and F1, with deduplication on (actor class, variable, horizon). Ambiguous and unverifiable predictions are excluded from precision and their counts reported. Actor classes match only when identical, because a subclass's sign can differ from its class total. It also gives the Brier score on assumptions. |
| `pipeline.py` | run log | Writes and hashes the prediction before the outcome card is read. The card is optional: a fictional case has none, and its run is then not scored. |

## Cases

- `cases/sf_1994`: San Francisco Proposition I (1994), which brought small multi-unit buildings built before 1979 under rent control. It has a policy summary, a fixture record, fixture answers and an outcome card.
- `cases/we001_riverton`: the handbook's WE-001 as input. `test_consistent_with_worked_example_we001` checks that every engine consequence appears in WE-001's consequence list.
- `cases/we013_halvern`: the handbook's WE-013 (fictional steel tariff) as input, with probabilities from its assumption table. It has no outcome card, so it is not scored; `test_consistent_with_worked_example_we013` checks every engine consequence against WE-013's table, with one listed exception (employment of export-industry workers: TX-8 signs `employment` alone, the table records the group sign `at_least_one_decrease`). It produces 11 consequences, all in the table; the other table rows rest on rules not encoded (LW-4, RS-6, RS-8, RS-15, SB-4, TS-1, OC-*, TX-9 and others). Annex run: `math-augmented-praxeo/examples/we013_halvern/`.

## What the first run shows, and what it does not

Offline run on `sf_1994` (rule base 0.4), 9 consequences reported:
- 5 verifiable and 4 unverifiable. The unverifiable ones are the keeper and displaced subclasses, the insiders' price and the shut-out seekers' price for uncovered units.
- Headline precision 1.00, recall 1.00, F1 1.00.
- Logic F1 0.57: consequences resting on premises the card does not record drop out of the logic score.
- Assumption Brier score 0.06.
- Under 1.4 there is no excess-demand claim, because Proposition I lets the rent reset on a new tenancy. The card's citywide-rent finding is matched by the rise in initial rents.
- Rule base 0.1 had recall 0.80; the miss was F-2.

**These numbers test the plumbing. They are not evidence of accuracy.** The reasons:

1. **Contamination, and now fitting.** The patterns encoded and the fixture probabilities were chosen with knowledge of the published findings for this case. A real test needs a decider and parser that see only material dated before enactment (plan 7.2), and a held-out case. PC-21 was added to the catalog because of this case's recall miss, so this case is now development data for PC-21 and cannot test it.
2. **The outcome card is unverified.** It was written from memory of Diamond, McQuade and Qian (2019, *AER* 109(9)), because the paper could not be fetched from this environment. Every figure has to be checked against the paper, and the card has to be checked by a second person.
3. **The policy text is a summary**, not the ordinance or the ballot pamphlet.
4. **The LLM stages have not run.** There is no API credential in this environment. The code follows the SDK's documented structured-output call, but it has not been exercised against the API.

Gaps the slice exposed (inputs for the next steps):

- **Vocabulary**, closed. The ontology is now the single list, and the rule base and cards are checked against it. Shut-out buyers' price for uncovered units is `price_substitute`, as in the handbook. Seekers' initial price on covered units is `price_paid` for `tenants.prospective`.
- **Recall miss F-2** (lower displacement out of the city), in rule base 0.1: no rule concluded anything about relocation. Closed in catalog 1.3 by PC-21 (insiders leave the area less) and the variable `relocation_out_of_area`; PC-21 still needs a use in a worked example or a held-out case.
- **Unclear provisions**, closed for readings that change facts. The parser does not yet propose `reading_facts`; a person or the LLM must write them.
- **Horizons** are crude: each effect is taken to hold from its first horizon onward.
- **Built in a first form:** context grounding (date filter only; there is no retrieval and no source corpus yet), the CR-12 combiner (subclass totals only) and the verifier.
- **Built in a first form:** per-question confidence thresholds with escalation (`escalation.py`).
- **Configuration B** (`config_b.py`) is built for the price-ceiling rules. On `sf_1994` it agrees with Configuration A on all 9 reported (actor, variable, sign) rows. Its results are Tier J (plan 5.2): a decision trail of questions and answers, not a proof. It does not yet take exception facts or per-reading facts.
- **Not built yet:** retrieval, and thresholds set from a labelled question bank.
