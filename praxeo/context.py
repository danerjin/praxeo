"""Context grounding (plan 5.3): only sources dated before enactment reach the decider, and each question gets the ones
relevant to it.

`split` keeps the sources published before the enactment date and reports the ones it held back, so a run cannot draw
on what happened after the policy was adopted. `retrieve` ranks the kept sources for one question by the words they share
with it, weighted by how rare each word is across the sources (a plain inverse-document-frequency score: deterministic,
no model), and `for_question` gives the decider the record with those sources added to its context. `ground` (every kept
source in the context) remains for callers that want all of them.
"""
from __future__ import annotations

import datetime as dt
import json
import math
import re
from pathlib import Path

from .schema import PolicyRecord, Source


def _date(s: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(s[:10])
    except ValueError:
        return None


STOP = frozenset("""the and for that with this from are was were will would can could have has had not but its their they them
which what when where whether into than then there these those under over about after before also each more most other
some such only same been being does did any all per out who whom how why our your his her she him one two""".split())


def _tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", text.lower().replace("_", " ")) if len(w) > 2 and w not in STOP}


def split(record: PolicyRecord, sources: list[Source]) -> tuple[list[Source], list[str]]:
    """The sources dated before enactment, and the ids of the ones held back (on or after it, or undated)."""
    enacted = _date(record.enacted)
    if enacted is None:
        return [], [s.id for s in sources]  # no date to filter on: hold everything back
    kept, held = [], []
    for s in sources:
        d = _date(s.date)
        (kept if d is not None and d < enacted else held).append(s)
    return kept, [s.id for s in held]


def retrieve(sources: list[Source], query: str, k: int = 3) -> list[Source]:
    """The k sources sharing the most informative words with the query; sources sharing none are not returned."""
    toks = [_tokens(s.text) for s in sources]
    n = len(sources)
    df: dict[str, int] = {}
    for t in toks:
        for w in t:
            df[w] = df.get(w, 0) + 1
    q = _tokens(query)
    scored = [(sum(math.log(1 + n / df[w]) for w in q & t), s.id, s) for s, t in zip(sources, toks)]
    return [s for score, _, s in sorted(scored, key=lambda x: (-x[0], x[1])) if score > 0][:k]


def for_question(record: PolicyRecord, kept: list[Source], query: str, k: int = 3) -> tuple[PolicyRecord, list[str]]:
    """The record with the k kept sources most relevant to the query added to its context, and their ids."""
    hits = retrieve(kept, query, k)
    if not hits:
        return record, []
    context = list(record.context) + [f"{s.text} ({s.citation}, {s.date})" for s in hits]
    return record.model_copy(update={"context": context}), [s.id for s in hits]


def ground(record: PolicyRecord, sources: list[Source]) -> tuple[PolicyRecord, list[str]]:
    """Return a copy of the record with every pre-enactment source added to its context, and the held-back ids."""
    kept, held = split(record, sources)
    context = list(record.context) + [f"{s.text} ({s.citation}, {s.date})" for s in kept]
    return record.model_copy(update={"context": context}), held


def load_sources(path: Path) -> list[Source]:
    return [Source(**s) for s in json.loads(path.read_text())] if path.exists() else []
