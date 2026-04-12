---
type: source_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
analysis_date: 2026-04-11
persona: catalyst-hunter
domain: crypto
subdomain: exchange-market-data
entity: btc
topic: bitcoin-above-72k-on-april-11
question: Will the price of Bitcoin be above $72,000 on April 11?
driver: reliability
date_created: 2026-04-11
source_name: Binance API spot price and kline verification
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-11
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/catalyst-hunter.md
tags: [binance, btcusdt, api, kline, verification]
---

# Summary

This note captures a direct verification pass against Binance API endpoints for BTCUSDT spot data and 1-minute klines.

## Key facts extracted

- Binance spot ticker endpoint returned BTCUSDT at 72,877.49 at capture time, above the 72,000 threshold.
- Recent 1-minute klines around capture time were also above 72,000.
- A test query for 2026-04-10 16:00 UTC returned a valid 1-minute kline with close 72,476.00, showing the endpoint structure works as expected.
- A direct query for 2026-04-11 16:00 UTC returned an empty list at capture time, consistent with that target minute not having occurred yet.
- This confirms that noon ET on April 11 should be checked as 16:00 UTC because DST is active in New York in April.

## Evidence directly stated by source

- `ticker/price?symbol=BTCUSDT` returned `{"symbol":"BTCUSDT","price":"72877.49000000"}`.
- `klines?symbol=BTCUSDT&interval=1m&limit=5` returned recent closes including `72861.31`, `72864.59`, `72884.30`, `72877.18`, and `72877.49`.
- `klines` query for `startTime=1775836800000` (2026-04-10 16:00 UTC) returned a candle whose close was `72476.00000000`.
- `klines` query for `startTime=1775923200000` (2026-04-11 16:00 UTC) returned `[]` at capture time.

## What is uncertain

- This note does not directly observe the eventual target 2026-04-11 16:00 UTC candle close because the query was made before that minute occurred.
- Binance web UI and API are closely related but the contract language names the web chart; operationally they should align, but that is still a small source-of-truth ambiguity.

## Why this source may matter

It is the strongest direct evidence about the relevant exchange, pair, and short-term price level. It materially supports that the market is pricing an already-in-the-money condition, subject to intraday downside before the exact close minute.

## Possible impact on the question

Because the spot level was already about $877 above the threshold with only hours remaining, the main remaining catalyst is adverse BTC price movement before noon ET rather than a need for bullish repricing to get above the line.

## Reliability notes

High-value primary source for the relevant pair and interval mechanics. Remaining uncertainty comes from future path dependence and small UI-versus-API settlement wording ambiguity, not from pair identification.