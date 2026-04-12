---
type: source_note
case_key: case-20260407-42a10bc6
dispatch_id: dispatch-case-20260407-42a10bc6-20260407T014927Z
analysis_date: 2026-04-07
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: binance
topic: case-20260407-42a10bc6 | variant-view
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07 close above 68000?
driver: operational-risk
date_created: 2026-04-06
source_name: Binance API + Polymarket rules page
source_type: primary-source-and-contract
source_url: https://api.binance.com/api/v3/klines ; https://polymarket.com/event/bitcoin-above-on-april-7
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [bitcoin, binance]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-42a10bc6/researcher-analyses/2026-04-07/dispatch-case-20260407-42a10bc6-20260407T014927Z/personas/variant-view.md]
tags: [binance, polymarket, resolution-source, timezone-check, candle-close]
---

# Summary

This note checks the governing source of truth and the exact time interpretation for the market. The key result is that the market settles off Binance BTC/USDT 1-minute candle data at 12:00 ET, which on 2026-04-07 is 16:00 UTC because New York is on EDT (UTC-4). At research time, Binance API endpoints were reachable and current 1-minute candles were available, but the settlement candle had not occurred yet.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1-minute candle for `12:00` in ET on the specified date, using the candle `Close` price.
- On 2026-04-07, ET is EDT, so `12:00 ET = 16:00 UTC`.
- Binance public API endpoints `api/v3/time` and `api/v3/klines` responded successfully during the check.
- Querying recent BTCUSDT 1-minute klines without a future timestamp returned normal live data.
- Querying Binance for candles around `2026-04-07T16:00:00Z` returned an empty set because that timestamp was still in the future at research time, confirming the market was not yet directly settled.
- Binance server time during verification was about `2026-04-07T01:50:55Z`, i.e. `2026-04-06 21:50:55 EDT`.

## Evidence directly stated by source

- Polymarket rules explicitly identify Binance BTC/USDT with `1m` candles as the resolution source and specify the `Close` price as the deciding field.
- Binance API directly exposes 1-minute BTCUSDT kline data and server time.

## What is uncertain

- The exact settlement candle close for `2026-04-07 12:00 ET` cannot yet be observed because the candle had not opened/closed at research time.
- The Polymarket rules page text is clear, but the visible trading interface on the public webpage can show odds snapshots that may differ from the assignment's `current_price`; the assignment value is the proper market-implied reference for this run.

## Why this source may matter

This is the governing source-of-truth surface. The case is mostly a timestamp and source-resolution problem rather than a broad interpretive macro call.

## Possible impact on the question

If BTC/USDT remains above 68000 into noon ET, the contract should resolve Yes; if it trades below by the candle close, it resolves No. The main research burden is verifying the correct settlement source, timezone conversion, and that the deciding value is the final 1-minute candle close rather than an intraminute high.

## Reliability notes

- Binance is the authoritative source because the contract names it explicitly.
- Evidence independence is limited for the settlement itself because there is one governing source of truth.
- A contextual secondary source is still useful for checking the public contract wording and avoiding misread timestamp mechanics.
- Operational caveat: public web chart rendering may differ from API accessibility, but both point to the same exchange source.