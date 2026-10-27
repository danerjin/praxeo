"""One structured-output call to Claude, streamed (the SDK refuses non-streamed calls whose max_tokens could outlast its
timeout), with the token use of every call summed by role so a run can report its cost."""
from __future__ import annotations

import os
import sys
import time
from collections import defaultdict

# USD per million tokens, Opus 5.5: input, output, cache write (5 minutes), cache read.
PRICES = {"claude-opus-5-5": {"input": 4.00, "output": 20.00, "cache_write": 5.00, "cache_read": 0.20}}

USAGE: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))


def client():
    """An Anthropic client. With ANTHROPIC_API_KEY set, the SDK's default. Without it (a cloud session, where the key is a
    network secret the egress proxy adds to requests for api.anthropic.com), the client sends no key and goes through
    HTTPS_PROXY even though api.anthropic.com is in NO_PROXY, so the proxy can add it."""
    import anthropic

    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if os.environ.get("ANTHROPIC_API_KEY") or not proxy:
        return anthropic.Anthropic()
    import httpx2

    # A plain httpx2 client: the SDK's DefaultHttpxClient still applies NO_PROXY to an explicit proxy.
    http = httpx2.Client(proxy=proxy, verify=os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt",
                         timeout=anthropic.DEFAULT_TIMEOUT, limits=anthropic.DEFAULT_CONNECTION_LIMITS, follow_redirects=True)
    return anthropic.Anthropic(http_client=http, default_headers={"X-Api-Key": anthropic.Omit()})


def parse(client, role: str, attempts: int = 3, **kw):
    """`messages.parse` as a stream; returns the final ParsedMessage and adds its usage to USAGE[role]. A stream the
    connection drops part way is not retried by the SDK, so the whole call is, up to `attempts` times. A dropped call's
    tokens are billed but not reported, so its count is kept as `dropped`."""
    import anthropic
    import httpx2

    tally = USAGE[role]
    for attempt in range(attempts):
        try:
            with client.messages.stream(**kw) as stream:
                resp = stream.get_final_message()
            break
        except (httpx2.TransportError, anthropic.APIConnectionError) as e:
            tally["dropped"] += 1
            if attempt == attempts - 1:
                raise
            print(f"{role}: connection dropped ({type(e).__name__}); retrying", file=sys.stderr)
            time.sleep(10 * (attempt + 1))
    u = resp.usage
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
