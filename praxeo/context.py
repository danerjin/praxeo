"""Context grounding (plan 5.3): only sources dated before enactment reach the decider.

The parser and decider see the policy record plus `record.context`. `ground` adds
the text of each source published before the enactment date and reports the ones
it held back, so a run cannot draw on what happened after the policy was adopted.
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

from .schema import PolicyRecord, Source


def _date(s: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(s[:10])
    except ValueError:
        return None


def ground(record: PolicyRecord, sources: list[Source]) -> tuple[PolicyRecord, list[str]]:
    """Return a copy of the record with pre-enactment sources added to its context, and the held-back ids."""
    enacted = _date(record.enacted)
    if enacted is None:
        return record, [s.id for s in sources]  # no date to filter on: hold everything back
    kept, held = [], []
    for s in sources:
        d = _date(s.date)
        (kept if d is not None and d < enacted else held).append(s)
    context = list(record.context) + [f"{s.text} ({s.citation}, {s.date})" for s in kept]
    return record.model_copy(update={"context": context}), [s.id for s in held]


def load_sources(path: Path) -> list[Source]:
    return [Source(**s) for s in json.loads(path.read_text())] if path.exists() else []
