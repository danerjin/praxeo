"""Render an annex: one row per consequence, its praxeological sign, the annex range and the sign check."""
from __future__ import annotations

from .result import Result, check_sign


def annex_table(title: str, intro: str, rows: list[tuple[str, str, Result, str]]) -> str:
    out = [f"# {title}", "", intro, "",
           "| Consequence | Praxeological sign | Annex range | Rung | Sign check | Basis |", "|---|---|---|---|---|---|"]
    for name, sign, r, basis in rows:
        out.append(f"| {name} | {sign} | {r.value} | {r.rung} | {check_sign(sign, r)} | {basis} |")
    out += ["", "Assumptions, by consequence:", ""]
    for name, _, r, _ in rows:
        out.append(f"- {name}: " + "; ".join(r.assumptions) + (f". **{r.note}**" if r.note else ""))
    return "\n".join(out) + "\n"
