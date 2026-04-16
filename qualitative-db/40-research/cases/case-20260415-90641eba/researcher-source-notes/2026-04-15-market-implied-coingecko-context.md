---
type: source_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: bitcoin-contextual-price-range
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 70000?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Bitcoin spot snapshot and 24h hourly market chart
source_type: market_data_aggregator
source_url: https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1&interval=hourly
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/market-implied.md
tags: [coingecko, bitcoin, context, source-note]
---

# Summary
CoinGecko provides an independent contextual check that Bitcoin is trading in the low-to-mid 74000 area and has spent the last day entirely above 70000.

## Key facts extracted
- CoinGecko simple price returned Bitcoin at `73982` USD during this run.
- CoinGecko hourly prices over the past day ranged from about `73761` to `74773` USD.
- In the returned 1-day hourly series, all observed points were above 70000.

## Evidence directly stated by source
- Independent aggregated spot data broadly matches Binance around 74000.
- The last-day observed range sits several thousand dollars above the contract threshold.

## What is uncertain
- CoinGecko is not the governing settlement source.
- A 1-day contextual range does not rule out a multi-day drop below 70000 before Apr 20 noon ET.

## Why this source may matter
It is a useful independent verification pass for current market state and helps test whether Binance-specific data might be anomalous.

## Possible impact on the question
This source supports the market's assumption that 70000 is currently not a near-line threshold. It does not remove the possibility of a sharp BTC selloff before the resolution minute.

## Reliability notes
- Medium-high reliability as an independent market-data aggregator.
- Useful as contextual verification, not as the settlement surface.
