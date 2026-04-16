---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: price-threshold-markets
entity: sol
topic: case-20260416-143465dc | market-implied
question: Will Solana reach $90 April 13-19?
date_created: 2026-04-16
source_name: Binance SOLUSDT 1m kline API verification pass
source_type: exchange-price-data
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1m&limit=1000
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/market-implied.md]
tags: [binance, kline, 1m, verification-pass, touch-market]
---

# Summary

A direct Binance API check on April 16 shows recent SOL/USDT 1-minute highs below 90, with the sampled window peaking at 89.15 and the latest sampled minute showing a high of 89.04 and close of 88.96. This does not settle the entire April 13-19 interval, but it materially confirms that the market is pricing a near-threshold setup rather than an already-cleared one.

## Key facts extracted

- Sample size returned: 1000 one-minute candles.
- Sampled window maximum high: 89.15.
- Latest sampled candle high: 89.04.
- Latest sampled candle close: 88.96.
- Sampled window low: 83.8.

## Evidence directly stated by source

- Binance returned machine-readable 1-minute kline rows for SOLUSDT.
- The observed sampled highs in this pass remained below the 90 threshold.

## What is uncertain

- This API call did not cover the full April 13-19 interval; it is a recent-window verification pass rather than complete-settlement proof.
- A later wick between now and April 19 could still trigger Yes immediately.
- Because the market uses Binance chart highs during the entire date window, final resolution still depends on all qualifying minutes through the deadline.

## Why this source may matter

This is the most relevant live verification source because it matches the governing exchange and candle granularity used for settlement. It is better than generic spot-price references for assessing whether the market is already effectively at the threshold.

## Possible impact on the question

The sampled highs below 90 support a view that Yes remains plausible but not yet effectively locked. They also help explain why a 0.74 market price may encode expectation of a likely intraday wick rather than certainty of an already-observed touch.

## Reliability notes

High reliability for the returned sampled data because it comes from Binance directly. Moderate completeness for this case because the pass covered a recent window, not the full resolution interval.