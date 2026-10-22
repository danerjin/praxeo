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
    # and the roles of the controlled class list (names the worked examples share)
    roles |= {n.split(".")[0] for n in actor_classes()}
    return frozenset(roles)


@lru_cache(maxsize=1)
def instruments() -> frozenset[str]:
    text = ONTOLOGY.read_text()
    section = text[text.index("## 2.3"):text.index("## 2.4")]
    # every backticked name in the first cell of a row: one row may list several instruments
    cells = re.findall(r"^\| ([^|]*)\|", section, re.M)
    return frozenset(n for cell in cells for n in re.findall(r"`([a-z_]+)`", cell))


def check_instrument(name: str) -> str | None:
    return None if name in instruments() else f"instrument `{name}` is not in 02_ontology.md section 2.3"


@lru_cache(maxsize=1)
def variable_meanings() -> dict[str, str]:
    """Each controlled variable with its meaning (02_ontology.md 2.4); a row naming two variables gives both the meaning."""
    text = ONTOLOGY.read_text()
    section = text[text.index("## 2.4"):text.index("## 2.5")]
    out = {}
    for names, meaning in re.findall(r"^\| (`[a-z_]+`(?:, `[a-z_]+`)*) \| (.*?) \|$", section, re.M):
        for n in re.findall(r"`([a-z_]+)`", names):
            out[n] = meaning
    return out


@lru_cache(maxsize=8)
def actor_classes(min_examples: int = 2, exclude: tuple[str, ...] = ()) -> tuple[str, ...]:
    """Controlled list of actor-class names for parsers: the classes in 02_ontology.md 2.2, plus every name
    used in the consequence lists of at least `min_examples` worked examples (handbook/05_examples). `exclude` drops
    examples by id prefix ("WE-036") from the count, so a blind run on an example is not shown names only it supports."""
    from collections import Counter
    text = ONTOLOGY.read_text()
    section = text[text.index("## 2.2"):text.index("## 2.3")]
    names = set(re.findall(r"^\| `([a-z_]+(?:\.[a-z_]+)*)`", section, re.M))
    for pair in re.findall(r"^\| `([a-z_.]+)`, `([a-z_.]+)`", section, re.M):
        names.update(pair)
    counts: Counter = Counter()
    for path in sorted((ONTOLOGY.parent / "05_examples").glob("WE-*.md")):
        if any(path.name.startswith(x) for x in exclude):
            continue
        body = path.read_text()
        if "## Consequence list" not in body:
            continue
        table = body.split("## Consequence list", 1)[1].split("## Gaps", 1)[0]
        used = set()
        for line in table.splitlines():
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) > 3 and re.match(r"C-\d+", cells[0]):
                for a in re.split(r",\s*", cells[1]):
                    a = a.strip("` ").split(" (")[0].strip("` ")
                    if re.fullmatch(r"[a-z_]+(\.[a-z_]+)*", a):
                        used.add(a)
        counts.update(used)
    names |= {n for n, k in counts.items() if k >= min_examples}
    return tuple(sorted(names))


def check_variable(name: str) -> str | None:
    return None if name in variables() else f"variable `{name}` is not in 02_ontology.md section 2.4"


def check_actor(name: str) -> str | None:
    role = name.split(".")[0]
    return None if role in actor_roles() else f"actor class `{name}`: role `{role}` not in 02_ontology.md section 2.2"
