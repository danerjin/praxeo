"""Parser: policy text -> PolicyRecord (workflow steps 1 and 2).

The LLM parser fills the schema and must quote the sentences each component
rests on. `check_citations` then verifies in code that every quoted sentence
occurs in the source text; a component whose quotes are not found is flagged.
"""
from __future__ import annotations

import re
from pathlib import Path

from .decider import MODEL
from .schema import PolicyRecord

PARSER_SYSTEM = """You turn the text of a policy into a structured policy record for a praxeological analysis.
For each operative provision, give one component: the instrument, the good and market, the actor class it binds
and the actor class it is meant to benefit (use ontology names such as landlords.controlled, tenants.controlled,
tenants.prospective, buyers.prospective), and the sentences of the text it rests on, quoted exactly.
If a provision can be read more than one way, record it under `unclear` with each reading; do not pick one.
Leave `reading_facts` empty: it takes engine facts written by a person, not text.
Copy into `context` only facts stated in the text about the market at enactment. Use nothing from after the enactment date."""


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


def check_citations(record: PolicyRecord, text: str) -> list[str]:
    """Return a problem line for every quoted source sentence not found in the text."""
    body = _norm(text)
    problems = []
    for comp in record.components:
        if not comp.source_sentences:
            problems.append(f"{comp.id}: no source sentence quoted")
        for sent in comp.source_sentences:
            if _norm(sent) not in body:
                problems.append(f"{comp.id}: quoted sentence not in source: {sent[:80]!r}")
    return problems


def parse_fixture(path: Path) -> PolicyRecord:
    return PolicyRecord.model_validate_json(path.read_text())


def parse_llm(text: str, model: str = MODEL, effort: str = "medium") -> PolicyRecord:
    import anthropic

    client = anthropic.Anthropic()
    resp = client.messages.parse(
        model=model,
        max_tokens=16000,
        system=PARSER_SYSTEM,
        output_config={"effort": effort},
        messages=[{"role": "user", "content": f"Policy text:\n\n{text}"}],
        output_format=PolicyRecord,
    )
    if resp.stop_reason == "refusal" or resp.parsed_output is None:
        raise RuntimeError(f"parser returned no record (stop_reason={resp.stop_reason})")
    return resp.parsed_output
