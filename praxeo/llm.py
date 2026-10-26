"""One structured-output call to Claude, streamed (the SDK refuses non-streamed calls whose max_tokens could outlast its
timeout), with the token use of every call summed by role so a run can report its cost."""
from __future__ import annotations

from collections import defaultdict

# USD per million tokens, Opus 5.5: input, output, cache write (5 minutes), cache read.
PRICES = {"claude-opus-5-5": {"input": 4.00, "output": 20.00, "cache_write": 5.00, "cache_read": 0.20}}

USAGE: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))


def parse(client, role: str, **kw):
    """`messages.parse` as a stream; returns the final ParsedMessage and adds its usage to USAGE[role]."""
    with client.messages.stream(**kw) as stream:
        resp = stream.get_final_message()
    u, tally = resp.usage, USAGE[role]
    tally["calls"] += 1
    tally["input"] += u.input_tokens
    tally["output"] += u.output_tokens
    tally["cache_write"] += u.cache_creation_input_tokens or 0
    tally["cache_read"] += u.cache_read_input_tokens or 0
    return resp


def usage_report(model: str) -> dict:
    """USAGE by role, with each role's cost and the total, in USD."""
    price = PRICES.get(model)
    out, total = {}, 0.0
    for role, tally in USAGE.items():
        row = dict(tally)
        if price:
            row["usd"] = round(sum(tally[k] * price[k] for k in price) / 1e6, 4)
            total += row["usd"]
        out[role] = row
    out["total_usd"] = round(total, 4) if price else None
    return out
