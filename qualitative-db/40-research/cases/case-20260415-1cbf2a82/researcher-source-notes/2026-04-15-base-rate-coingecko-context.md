---
type: source_note
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-17 be above 72000?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko 30-day Bitcoin market chart
source_type: market_data_aggregator
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30&interval=daily
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: medium
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/base-rate.md]
tags: [coingecko, contextual-evidence, bitcoin, 30d-range]
---

# Summary

CoinGecko 30-day daily price series provides an independent contextual cross-check: BTC has spent a substantial portion of the last month near or above the low-70k region, but has also repeatedly traded in the upper-60k to low-70k band. That supports a Yes-leaning base rate while preserving meaningful downside risk for a specific timestamp contract.

## Key facts extracted

- 30-day daily prices include a low area near `65970` on 2026-03-28 and highs around `74858` on 2026-03-15 and `74515` on 2026-04-13.
- The last week before retrieval shows daily values roughly: `71976`, `71117`, `71771`, `72973`, `73054`, `70757`, `74515`, `74181`, `74064`.
- BTC has therefore oscillated around the 72,000 threshold rather than sitting safely far above it.

## Evidence directly stated by source

- CoinGecko directly states daily BTC/USD market prices and volumes across the last 30 days.

## What is uncertain

- CoinGecko is not the governing settlement source.
- BTC/USD on CoinGecko is only contextual; the contract resolves on Binance BTC/USDT 1-minute close.
- Daily series obscures intraday variance around the noon ET decision point.

## Why this source may matter

It is a useful independent contextual source for recent regime and range behavior, reducing single-source dependence on Binance API alone.

## Possible impact on the question

This source reinforces that the threshold is live and plausible rather than trivial. The outside-view implication is that Yes should be favored because current regime is near/above 72k, but not near certainty because the threshold has been crossed back and forth repeatedly.

## Reliability notes

- Good for contextual independence and recency.
- Not sufficient for settlement by itself.
- Best used as a volatility/range check rather than an authoritative answer source.