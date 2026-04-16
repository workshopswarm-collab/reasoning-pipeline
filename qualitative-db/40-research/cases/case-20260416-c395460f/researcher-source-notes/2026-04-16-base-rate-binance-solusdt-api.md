---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 19, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance public market data API (SOLUSDT ticker and 1d klines)
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: base-rate
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/base-rate.md]
tags: [source-note, binance, solusdt, price-data]
---

# Summary

This source note captures direct exchange data from Binance, which is also the governing source of truth for resolution. It matters because the contract resolves specifically on the Binance SOL/USDT 1-minute candle at 12:00 ET on April 19, so current Binance spot and recent Binance daily path are the most decision-relevant primary evidence.

## Key facts extracted

- Binance spot ticker at research time returned `SOLUSDT = 84.94000000`.
- Binance 1-day klines for the last 10 daily bars show recent closes of approximately:
  - Apr 7: 85.56
  - Apr 8: 82.57
  - Apr 9: 83.33
  - Apr 10: 84.83
  - Apr 11: 84.93
  - Apr 12: 81.53
  - Apr 13: 86.51
  - Apr 14: 83.72
  - Apr 15 partial/current day around 84.94 at extraction time
- Recent daily lows in the sample reached as low as 78.38 on Apr 7, with several other lows still above 80.
- The market resolves on a specific 1-minute candle close, not on daily close, intraday high, or a different exchange.

## Evidence directly stated by source

- Direct current Binance SOL/USDT price was above 80 at extraction time.
- Direct recent Binance historical trading range over the previous several days was mostly low-to-mid 80s.
- Direct recent realized volatility was large enough that a move from mid-80s to below 80 by the target minute remains plausible.

## What is uncertain

- This note does not provide the exact April 19 12:00 ET 1-minute close.
- 1-day klines do not directly measure the noon ET minute-candle distribution.
- Crypto trades continuously, so weekend and overnight volatility can still alter the final resolution minute materially.

## Why this source may matter

This is the cleanest primary evidence because the same venue/source family both informs the current price baseline and governs market settlement.

## Possible impact on the question

The source supports a base-rate leaning toward Yes because current spot is already about 6% above the threshold and recent Binance daily closes were generally above 80. At the same time, the range data warns against treating a currently-above-threshold state as near-certain over a multi-day horizon.

## Reliability notes

- High credibility for price levels and contract relevance because Binance is the explicit settlement source.
- Some operational caveat remains because the contract references the Binance trading interface candle, while this note uses Binance public API endpoints rather than the UI itself. That should not usually matter, but it is worth noting as a minor implementation-layer ambiguity.