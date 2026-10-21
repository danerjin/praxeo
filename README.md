# Praxeological Policy Analysis System

An AI-assisted system for analyzing the consequences of a policy using Misesian praxeology, with predictions that are accurate (scored against historical outcomes) and interpretable (every consequence carries its causal chain and assumptions).

| Path | What it is |
|---|---|
| `Praxeology_AI_Project_Plan_v3.md` (.docx, .pdf) | Current project plan. Version 2 is kept alongside for reference. |
| `handbook/` | Phase 1: the Method Handbook, which covers how to analyze a policy praxeologically. It has the foundations, vocabulary, workflow, rule catalog, worked examples and open questions. Start at `handbook/README.md`. |
| `PHASE2_REPORT.md` (`Phase2_Progress_Report.pdf`) | Phase 2 progress report: what the analyser does, coverage of the worked examples, LLM-stage and control results, limits, and what needs people. |
| `praxeo/` | Phase 2 thin slice: parser, decider, clingo engine, explainer and scoring, run end to end on one case. Start at `praxeo/README.md`. |
| `cases/` | Cases for the pipeline: `sf_1994` (historical, with an outcome card) and `we001_riverton` (the handbook's WE-001, as a consistency check). |
| `tests/` | `python3 -m pytest tests` |
| `math-augmented-praxeo/` | A separate, minimal mathematical annex (not praxeology): interval-valued sizes for consequences the method has already signed, using identities and first-order statics only. It never sets a sign. Start at `math-augmented-praxeo/README.md`. |
| `figures/` | Diagrams used in the plan. |
| `tools/build_plan.py` | Builds the plan's .docx from its Markdown source. |
