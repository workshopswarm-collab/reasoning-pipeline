---
type: source_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: tokens
entity: sol
topic: solana-above-80-on-april-19
question: Will the Binance SOL/USDT 12:00 ET one-minute candle on 2026-04-19 close above 80?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance API daily SOLUSDT klines
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&startTime=1775001600000&endTime=1776297600000&limit=1000
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/base-rate.md]
tags: [binance, solusdt, price-history, direct-source]
---

# Summary

Binance daily SOL/USDT candlestick data for April 1-15, 2026 shows SOL has closed above $80 on 13 of the 15 completed days in the sample, with the latest partial April 15 session around $85.26 at the retrieval time. This is direct exchange data from the same venue that defines contract resolution, though at a coarser interval than the final one-minute noon ET settlement candle.

## Key facts extracted

- Daily closes from Apr 1-15, 2026 were: 81.18, 78.94, 80.40, 80.83, 81.89, 80.03, 85.56, 82.57, 83.33, 84.83, 84.93, 81.53, 86.51, 83.72, 84.90, with Apr 15 partial session around 85.26 at retrieval.
- 13 of the 15 completed daily closes in the period were above $80; only Apr 2 (78.94) and Apr 6 (80.03 is above 80 by contract wording, since the threshold is strictly greater than 80, though very near the line) challenge the idea that $80 is far away.
- Intraperiod lows in the sample fell below $80 on several days even when daily closes finished above $80, which matters because the contract resolves on a specific one-minute candle at 12:00 ET rather than a daily close.
- Recent realized trading range was mostly low-to-mid 80s, with a high of 87.67 and lows as low as 78.38 in the sample.

## Evidence directly stated by source

- Binance returned raw SOLUSDT daily kline arrays including open, high, low, close, volume, and timestamps.
- The data directly establishes recent price level context on the exact resolution venue and trading pair.

## What is uncertain

- This source does not directly answer the specific resolution minute: 12:00 ET on Apr 19, 2026.
- Daily interval data can mask sub-day volatility that could pull the noon one-minute close below $80 even if the daily close later finishes above $80.
- The April 15 row was incomplete at retrieval because the UTC trading day had not ended.

## Why this source may matter

It supplies the best direct base-rate anchor from the exact exchange and pair that govern the contract. For a threshold market at $80, recent venue-specific distribution around that level is more relevant than narrative commentary.

## Possible impact on the question

This source supports an outside-view prior that SOL being above $80 at a random nearby observation time on Apr 19 is more likely than not, because recent Binance trading has spent most completed days closing above that level. It does not eliminate timing risk around the specific noon ET minute.

## Reliability notes

High reliability for venue-specific recent price context because Binance is also the stated resolution source. Medium fit for exact settlement because the interval is daily rather than the contract’s required one-minute candle.