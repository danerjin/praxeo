"""Builds proposals.json and answers.json from the proposer's facts (written below, round by round) and the decider's table.
Run from the loop directory: python tools/mk_props.py"""
import json, re
from pathlib import Path

TABLE_FILE = "/tmp/claude-0/-home-user-praxeo/6d563eb7-45da-5432-b932-3230b691929b/scratchpad/blind/WE-044_assumptions.txt"
TAB = {}
for line in Path(TABLE_FILE).read_text().splitlines():
    parts = [x.strip() for x in line.split("|")]
    if len(parts) >= 4 and parts[0].startswith("A-"):
        TAB[parts[0].lower().replace("-", "")] = (parts[1], parts[2], float(parts[3]))

# statements judged by the decider from section 1 (not in the table): text -> (p, class, note)
JUDGED = {}
exec(Path("tools/judged.py").read_text())

PROPS = {}
CLASS = {}


def st(x):
    return TAB[x][0] if x in TAB else x


def add(node, part, fact, prem=(), src=None):
    texts = [st(x) for x in prem]
    cls = TAB[prem[0]][1] if prem and prem[0] in TAB else "other"
    d = {"part": part, "fact": fact, "premises": texts, "premise_class": cls}
    if src:
        d["source"] = src
    PROPS.setdefault(node, []).append(d)


for _f in ("rounds.py", "round2.py", "round3.py", "round4.py"):
    if Path("tools", _f).exists():
        exec(Path("tools", _f).read_text())

Path("proposals.json").write_text(json.dumps(PROPS, indent=1))
ans = {}
need = [t for ps in PROPS.values() for p in ps for t in p["premises"]]
by_text = {v[0]: v[2] for v in TAB.values()}
used_table, used_judged = {}, {}
for t in dict.fromkeys(need):
    if t in by_text:
        ans[t] = by_text[t]; used_table[t] = by_text[t]
    elif t in JUDGED:
        ans[t] = JUDGED[t][0]; used_judged[t] = JUDGED[t]
    else:
        print("NO ANSWER:", t)
Path("answers.json").write_text(json.dumps(ans, indent=1))
print(len(used_table), "from table;", len(used_judged), "judged")
