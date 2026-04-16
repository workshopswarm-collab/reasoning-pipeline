---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: protocols
entity: ethereum
topic: recent ETH price trend into Apr 13-19 window
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: CoinGecko Ethereum market chart and spot snapshot
source_type: market_data_aggregator
source_url: https://api.coingecko.com/api/v3/coins/ethereum | https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=30&interval=daily
source_date: 2026-04-13
credibility: medium_high
recency: high
stance: neutral
certainty: medium_high
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.sidecar.json]
tags: [coingecko, eth, momentum, market-context]
---

# Summary

CoinGecko context shows ETH had risen from roughly 2024 at the end of March to roughly 2356 by Apr 13, including about 9.6% over 7 days and about 7.1% over 24 hours. The relevant catalyst implication is not one discrete scheduled event, but active momentum and reflexivity: a threshold only modestly above spot can be reached by continuation flows even without a new fundamental headline.

## Key facts extracted

- CoinGecko spot snapshot showed current_price around 2355.35 on review.
- 24h high in the snapshot was around 2349.27, while live market-chart data printed around 2355.90 near fetch time.
- 7-day change was about +9.59%.
- 24h change was about +7.10%.
- 30-day daily series showed ETH near 2023.82 on Mar 30 and near 2355.90 on Apr 13.
- The 7-day series included a rise from roughly 2189 on Apr 8 to roughly 2356 on Apr 13.

## Evidence directly stated by source

- Direct pricing/time-series data from CoinGecko API endpoints.

## What is uncertain

- CoinGecko is contextual, not the settlement venue.
- Aggregator timestamps and intraday highs may not align exactly with Binance 1-minute candle highs.
- Momentum continuation over the next six days is probabilistic, not guaranteed.

## Why this source may matter

It helps answer whether 2400 is an unusually distant target or a nearby threshold in the current regime. The answer is that it is nearby, with recent momentum already covering more than the required remaining move.

## Possible impact on the question

This source supports a moderately bullish view on a touch-to-threshold contract because the required move from current levels is small relative to realized recent volatility and weekly upside already observed.

## Reliability notes

Good contextual source for recent price path and magnitude. Not authoritative for settlement, but useful as an independent contextual check against the Binance-based thesis.