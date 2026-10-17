# praxeo: Phase 2 thin slice

Plan §5.5 step 1: one rule family, one worked example, one historical case, run end to end. Every stage is crude. The point is that the stages connect and that scoring code exists.

```
policy.txt ──parser──▶ PolicyRecord ──typed questions──▶ Decider ──p per assumption──▶
clingo engine (rules/price_controls.lp) ──▶ consequences + derivations + minimal assumption sets ──▶
templated explainer ──▶ prediction.json (frozen, hashed) ──▶ outcome card opened ──▶ score.json, report.md
```

## Run

```
pip install -e '.[test]'           # pydantic, clingo, anthropic, pytest
python3 -m praxeo cases/sf_1994     # fixture parser and fixture decider (offline)
python3 -m pytest tests
```

Options: `--parser fixture|llm`, `--decider fixture|llm|human`, `--out DIR` (default `runs/…`, git-ignored). The LLM parser and decider call Claude through the Anthropic SDK with structured outputs (`messages.parse` into the pydantic schema) and need `ANTHROPIC_API_KEY`. A sample offline run is committed in `cases/sf_1994/sample_run/`.

## Stages

| Module | Stage (plan) | What it does now |
|---|---|---|
| `schema.py` | typed records | PolicyRecord, Component, Unclear, Question, Answer, Assumption, Consequence, Step, OutcomeCard, Finding. |
| `parser.py` | LLM parser (5.2) | Fills PolicyRecord from text; each component quotes its source sentences; `check_citations` verifies the quotes in code. Fixture backend loads `record.json`. |
| `questions.py` | typed questions (4.4) | Eight noul questions per price ceiling, one per assumption the rules name (binding, enforced, alternative_uses, nontransferable, buyouts_limited, would_leave, lockin_dominates, substitutes). |
| `decider.py` | Decider interface (5.2) | FixtureDecider, LLMDecider, HumanDecider behind one `answer(question, record)` call. A Jev decider would slot in here. |
| `rules/price_controls.lp` | rule base (4.4) | PC-1 (the plan's PR-017), PC-3 (insiders and outsiders, with RS-4), PC-5, RS-5, PC-7 and PC-21 (as revised in catalog 1.4: buyout and dominance premises), each with an `exception/2` default. |
| `engine.py` | symbolic engine, Configuration A (5.4) | Writes facts, opens a choice over assumptions, enumerates answer sets, and labels each conclusion with its minimal assumption sets (ATMS-style). A consequence is reported when its most probable minimal set has every p ≥ 0.5. |
| `explainer.py` | templated explainer | One sentence per consequence from the derivation steps; no free text. |
| `scoring.py` | scoring (7.3, 7.4) | Headline and logic precision, recall and F1; deduplication on (actor class, variable, horizon); ambiguous and unverifiable predictions excluded from precision with their counts reported; Brier score on assumptions. |
| `pipeline.py` | run log | Writes and hashes the prediction before the outcome card is read. |

## Cases

- `cases/sf_1994`: San Francisco Proposition I (1994), which brought small multi-unit buildings built before 1979 under rent control. It has a policy summary, a fixture record, fixture answers and an outcome card.
- `cases/we001_riverton`: the handbook's WE-001 as input. `test_consistent_with_worked_example_we001` checks that every engine consequence appears in WE-001's consequence list.

## What the first run shows, and what it does not

Offline run on `sf_1994` (rule base 0.3): 7 consequences reported, 5 verifiable and 2 unverifiable. Headline precision 1.00, recall 1.00, F1 1.00. Logic F1 0.57: three consequences rest on premises the card does not record (substitutes; the 1.4 premises on buyouts and on the lock-in outweighing diverted movers), so they leave the logic score. Assumption Brier score 0.04. Rule base 0.1 had recall 0.80; the miss was F-2.

**These numbers test the plumbing. They are not evidence of accuracy.** The reasons:

1. **Contamination, and now fitting.** The patterns encoded and the fixture probabilities were chosen with knowledge of the published findings for this case. A real test needs a decider and parser that see only material dated before enactment (plan 7.2), and a held-out case. PC-21 was added to the catalog because of this case's recall miss, so this case is now development data for PC-21 and cannot test it.
2. **The outcome card is unverified.** It was written from memory of Diamond, McQuade and Qian (2019, *AER* 109(9)), because the paper could not be fetched from this environment. Every figure has to be checked against the paper, and the card has to be checked by a second person.
3. **The policy text is a summary**, not the ordinance or the ballot pamphlet.
4. **The LLM stages have not run.** There is no API credential in this environment. The code follows the SDK's documented structured-output call, but it has not been exercised against the API.

Gaps the slice exposed (inputs for the next steps):

- **Vocabulary.** WE-001 calls the outsiders' price `price_substitute`, while the engine and the SF card call it `price_paid`. Plan 7.4 normalization needs one shared vocabulary file used by the handbook, the rules and the cards.
- **Recall miss F-2** (lower displacement out of the city), in rule base 0.1: no rule concluded anything about relocation. Closed in catalog 1.3 by PC-21 (insiders leave the area less) and the variable `relocation_out_of_area`; PC-21 still needs a use in a worked example or a held-out case.
- **Unclear provisions** are recorded, but the engine does not yet branch on readings (per-reading signs).
- **Horizons** are crude: each effect is taken to hold from its first horizon onward.
- **Not built yet:** context grounding (retrieval limited to sources before enactment), the effect combiner and CR-12 conflicts, the verifier, Configuration B, per-question confidence thresholds and escalation.
