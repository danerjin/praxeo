"""The shared variable vocabulary (plan 7.4), read from the handbook's ontology.

One source of truth: handbook/02_ontology.md, section 2.4. The rule base, the
engine's output and the outcome cards are all checked against it, so a
prediction and a finding can only match if they use the same variable name.
Actor classes are open (role plus market, section 2.2), so they are checked
only for a known role.
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

ONTOLOGY = Path(__file__).resolve().parents[1] / "handbook" / "02_ontology.md"


@lru_cache(maxsize=1)
def variables() -> frozenset[str]:
    text = ONTOLOGY.read_text()
    section = text[text.index("## 2.4"):text.index("## 2.5")]
    names = set(re.findall(r"^\| `([a-z_]+)`", section, re.M))
    for pair in re.findall(r"^\| `([a-z_]+)`, `([a-z_]+)`", section, re.M):
        names.update(pair)
    return frozenset(names)


@lru_cache(maxsize=1)
def actor_roles() -> frozenset[str]:
    """Roles named in section 2.2 and in the worked examples' usual vocabulary."""
    text = ONTOLOGY.read_text()
    section = text[text.index("## 2.2"):text.index("## 2.3")]
    roles = {name.split(".")[0] for name in re.findall(r"`([a-z_]+(?:\.[a-z_]+)*)`", section)}
    # roles the worked examples use for housing, labor and public finance
    roles |= {"tenants", "landlords", "renters", "homebuyers", "developers", "workers", "employers",
              "consumers", "producers", "officials", "residents"}
    return frozenset(roles)


@lru_cache(maxsize=1)
def instruments() -> frozenset[str]:
    text = ONTOLOGY.read_text()
    section = text[text.index("## 2.3"):text.index("## 2.4")]
    return frozenset(re.findall(r"^\| `([a-z_]+)`", section, re.M))


def check_instrument(name: str) -> str | None:
    return None if name in instruments() else f"instrument `{name}` is not in 02_ontology.md section 2.3"


def check_variable(name: str) -> str | None:
    return None if name in variables() else f"variable `{name}` is not in 02_ontology.md section 2.4"


def check_actor(name: str) -> str | None:
    role = name.split(".")[0]
    return None if role in actor_roles() else f"actor class `{name}`: role `{role}` not in 02_ontology.md section 2.2"
