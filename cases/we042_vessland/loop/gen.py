"""Writes proposals.json and answers.json for the WE-042 blind loop. Proposals are written round by round (R1, R2, ...);
statements that match the assumption table take its p; the others take the judged p in JUDGED (see notes.md)."""
import json
from pathlib import Path

HERE = Path(__file__).parent
TABLE = {}
for line in Path("/tmp/claude-0/-home-user-praxeo/6d563eb7-45da-5432-b932-3230b691929b/scratchpad/blind/WE-042_assumptions.txt").read_text().splitlines():
    if "|" in line:
        i, st, ty, p = [x.strip() for x in line.split("|")]
        TABLE[i] = (st, ty, float(p))


def A(n):
    return TABLE[f"A-{n}"][0]


JUDGED = {}   # statement -> (p, class)
props: dict[str, list[dict]] = {}


def add(node, part, fact, premises=(), cls="other", source=None):
    props.setdefault(node, []).append({"part": part, "fact": fact, "premises": list(premises), "premise_class": cls, "source": source})


def link(node, src_var, rel, actor, var, premises=(), horizon=None, source=None, src_actor=None):
    f = {"source_actor": src_actor or node.split("#")[0], "source_variable": src_var, "relation": rel, "actor": actor, "variable": var}
    if horizon:
        f["horizon"] = horizon
    add(node, "links", f, premises, source=source)


for f in sorted(HERE.glob("rounds*.py")):
    exec(f.read_text())

json.dump(props, open(HERE / "proposals.json", "w"), indent=1)
used = {s for ps in props.values() for p in ps for s in p["premises"]}
ans, todo = {}, []
by_text = {v[0]: v[2] for v in TABLE.values()}
for s in sorted(used):
    if s in by_text:
        ans[s] = by_text[s]
    elif s in JUDGED:
        ans[s] = JUDGED[s][0]
    else:
        todo.append(s)
json.dump(ans, open(HERE / "answers.json", "w"), indent=1)
for s in todo:
    print("UNANSWERED:", s)
