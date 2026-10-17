"""Praxeo: Phase 2 thin slice of the praxeological policy analyser.

One pipeline, every stage crude: policy text -> parser -> policy record ->
typed questions answered by a decider -> clingo engine -> consequences with
derivations and minimal assumption sets -> templated explanation -> score
against an outcome card. See README.md in this directory.
"""

RULEBASE_VERSION = "rb-thin-0.2 (handbook catalog 1.3: PC-1, PC-3, PC-5, PC-7, PC-21, RS-5)"
