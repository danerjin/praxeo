"""Praxeo: Phase 2 thin slice of the praxeological policy analyser.

One pipeline, every stage crude: policy text -> parser -> policy record ->
typed questions answered by a decider -> clingo engine -> consequences with
derivations and minimal assumption sets -> templated explanation -> score
against an outcome card. See README.md in this directory.
"""

RULEBASE_VERSION = "rb-thin-0.6 (handbook catalog 1.4: price ceilings PC-1..PC-7, PC-16, PC-21, RS-2..RS-11, SB-4, OC-2..OC-4; taxes and tariffs TX-1, TX-2, TX-4, TX-7..TX-9, RS-1, RS-5..RS-7, RS-14, RS-15, TS-2, SB-4, OC-2..OC-4; CR-12 totals)"
