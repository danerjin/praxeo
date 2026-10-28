# Handoff: the core path and the LLM pilot

Read this first in a new session. The history behind it is in `PILOT_CORE_RULES.md` (steps 1 to 15), the summary in
`PHASE2_REPORT.md`, and every blind score with its audited mapping in `tests/blind_scores.json`.

## Where things stand

- The core rules (`praxeo/core/core.lp`) are the engine's main path: the situation record (`praxeo/core/situation.py`), the
  expand-as-you-go loop (`praxeo/core/expand.py`), the pipeline (`praxeo/core/pipeline.py`). The pattern engine is the fallback
  for cases without core inputs, and its patterns are kept as checks the core rules re-derive
  (`tests/test_core_derives_patterns.py`).
- Every worked-example case has core inputs from blind stand-in runs (sonnet subagents as proposer and decider).
- Out of sample, the core path beats the pattern engine on 8 of 15 cases and trails on 6; the two tax cases (WE-042, WE-046)
  are far behind. Run-to-run spread is now as large as the effect of rule changes, so the gap is in what the proposer
  proposes. That is what the LLM pilot tests.
- Full suite: `python -m pytest -q` (about 15 minutes). Last full run: 248 passed, 1 skipped.

## Next step: the LLM pilot

The API key is read from `ANTHROPIC_API_KEY`, or, in a cloud session (which withholds that variable), from a network
secret for `api.anthropic.com` with header `x-api-key`: `praxeo/llm.py` `client()` then sends no key and routes through the
egress proxy, which adds it. Check either with
`python -c "from praxeo import llm; print(llm.client().models.retrieve('claude-opus-5-5').id)"` (a 401 means no key reached
the API). In a new session:

1. Check it is visible: `python -c "import os; print(bool(os.environ.get('ANTHROPIC_API_KEY')))"`.
   A fresh container also needs the dependencies: `python -m pip install "anthropic>=1,<2" "clingo>=5.6" pydantic pytest`.
2. Pilot: `python -m praxeo.core.llm_eval WE-036 we036_quenby --runs 1`. It writes `cases/we036_quenby/llm/run_1/` (seed,
   situation, log, `meta.json` with proposer calls, rejected proposals, questions, and token use and cost by role from
   `praxeo/llm.py`). All three roles stream their calls (the SDK refuses the seed's 32000-token call unstreamed). The harness is untested against the live
   API: watch the first `messages.parse` call (structured output with a closed schema; facts travel as JSON strings and are
   validated, `praxeo/core/expand.py` `ProposalOut`, `praxeo/core/seed.py` `SeedOut`).
3. Score it like the stand-in runs: map class names only where both denote the same class (never across trades, never a
   broader class merging distinct table classes; when unsure, leave it out), then
   `tests/test_core_expand.py::_loop_score(case, example, short, windows, loop)` with `loop="llm/run_1"`. WE-036 stand-in
   runs gave 13 to 26 of 60; the pattern engine 29.
   Pilot run 1 (`llm/run_1`, proposer at medium effort): 7 of 60 for $3.05 (seed $0.15, proposer $2.08 over 24 calls,
   decider $0.81 over 28 questions). The proposer proposed only links and alternatives (30 facts), and the seed held 2
   exchanges against r7's 4, so the engine reported 33 consequences against r7's 63. Since then the proposer prompt
   describes every part with its fields and a general example and asks for a pass over all of them per node, the
   proposer runs at high effort (`--proposer-effort`), and the proposer's system prompt and policy text and the
   decider's record are cached. Of run 1's 53 missed rows, 25 are classes never reached (offering and paying employers,
   insurers, taxpayers, recipients of other spending), 23 are classes reached without the variable (lobbying, asset values,
   returns: no stakes, assets or yields; labour as quantity_traded), 5 differ in sign. The seed writer had not been given the
   controlled vocabulary and priced labour in `labour_cost` and `wage`, which the engine does not read as prices; the seed
   now gets the vocabulary, and a seed or proposal naming a variable off the list (or an exchange price that is not a
   price variable) goes back once with the errors.
   Run 2 (new proposer prompt at high effort, seed without the vocabulary): 11 of 60, $11.05. Run 3 (all changes): 13 of
   60, $9.85 (seed $0.15, proposer $7.14 over 44 calls, decider $2.56 over 208 questions; caching read 1.5M tokens). Both
   now propose every part (run 3: 20 exchanges, 20 margins, 26 stakes, 9 assets, 12 yields, 111 links). Of run 3's 47
   misses, 16 are classes never reached (bound employers are still not split into offering and paying), 20 variables not
   derived, 11 signs that differ, mostly a group claim in the table (at least one of hours, employment, benefits; taxpayers
   or recipients) where the run gives one sign per variable or class.
4. Report the token use and cost of the pilot to the user before running the batch: three runs each on WE-036, WE-020,
   WE-046, WE-042, WE-064.

## Conventions

- Branch `claude/wizardly-bardeen-xb4yh0`; commit and push there only; no pull requests unless asked. Commit messages end with
  the session's Co-Authored-By and Claude-Session lines; no model names elsewhere in the repo.
- Blind runs see only section 1 of the example and its assumption table's ID, Statement, Type and p columns
  (`praxeo/core/llm_eval.py` `blind_inputs` gives exactly that). Never the consequence list, the later sections,
  `handbook/05_examples_core/`, existing case files or tests for that case.
- Fixes found from runs are general (core rules in CR-1 terms, no instrument names in `core.lp`; a test checks that), each
  with a check in `tests/test_core_derives_patterns.py`. Record before and after counts; update `PILOT_CORE_RULES.md`,
  `PHASE2_REPORT.md` and rebuild the PDF with `python tools/build_report_pdf.py`.

## Open items

- `quantity_traded` merges an actor's exchanges (makers' parts sales and equipment sales are one variable).
- Dated windows beyond announcement, first months, deadline and after expiry.
- Depth 3 leaves some classes unvisited.
- The tax cases need detailed facts (drawback claims by yield table, scrap's two outlets) no writer proposed.
