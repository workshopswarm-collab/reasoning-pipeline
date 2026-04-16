---
type: source_note
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bbc8ed19 | base-rate
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: reliability
date_created: 2026-04-16
source_name: Binance BTCUSDT 365-day daily kline sample
source_type: primary contextual market data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=365
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/base-rate.md
tags: [base-rate, historical-context, btcusdt, retention]
---

# Summary

This note records a simple outside-view check using 365 Binance daily BTCUSDT closes and short-horizon forward returns.

## Key facts extracted

- Latest daily close in the sample was 74909.72 on 2026-04-16.
- To fall below 72000 by resolution from that level would require roughly a 3.88% decline.
- In the 365-day sample, 83.29% of daily closes were already above 72000.
- In that same sample, the share of forward returns exceeding the needed threshold was:
  - 3-day: 86.19%
  - 4-day: 83.66%
  - 5-day: 80.83%
- Positive forward returns over those same windows were much closer to coin-flip territory (~50-53%), which means the relevant base-rate fact is not that BTC usually rises, but that it often does not fall enough from current levels to breach 72k.

## Evidence directly stated by source

- The kline dataset directly states daily OHLC values for BTCUSDT on Binance.

## What is uncertain

- This is a crude historical analog, not a regime-adjusted forecast.
- The sample mixes many market conditions and does not isolate only episodes where BTC was near 75k.
- Daily close analysis is not identical to the exact noon ET one-minute-candle condition.

## Why this source may matter

The market is a short-horizon threshold question. A base-rate analysis should ask how often BTC, starting from near-current levels, stays above a threshold over a 3-5 day window.

## Possible impact on the question

This contextual source supports a high Yes probability and suggests the market's ~84.5% implied probability is not obviously inflated. If anything, the simple historical retention rate is slightly higher, though not enough to justify a major disagreement given contract-specific noise.

## Reliability notes

- Same-source dependence is high because this contextual analysis also uses Binance data.
- Independence from the primary settlement source is therefore low, but the data is still directly relevant because the market explicitly resolves on Binance BTCUSDT.
- The main weakness is model simplicity rather than source credibility.
