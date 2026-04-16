---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-8bb1e3b4 | market-implied
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-20 close above 70000?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Bitcoin market data
source_type: market-data aggregator
source_url: https://api.coingecko.com/api/v3/coins/bitcoin
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8bb1e3b4/researcher-analyses/2026-04-15/dispatch-case-20260415-8bb1e3b4-20260415T150551Z/personas/market-implied.md]
tags: [coingecko, bitcoin, market-data, context]
---

# Summary

CoinGecko provides an independent contextual check that Bitcoin was trading around 74.1k USD with mild recent weakness but still well above 70k.

## Key facts extracted

- CoinGecko current price was about 74,099 USD.
- 24-hour move was about -0.94%.
- 7-day move was about +3.50%.
- 14-day move was about +8.73%.
- 30-day move was about +0.11%.

## Evidence directly stated by source

- Current price USD: 74,099.
- Price change percentage 24h: -0.94284.
- Price change percentage 7d: 3.49677.
- Price change percentage 14d: 8.72703.
- Price change percentage 30d: 0.10724.

## What is uncertain

- CoinGecko aggregates across venues and does not govern settlement.
- Aggregator methodology can differ from Binance-specific spot prints.
- It is only a contextual cross-check and not a substitute for the contract source.

## Why this source may matter

It helps test whether the Binance snapshot is idiosyncratic. Seeing a very similar price from an independent aggregator makes the high-70k neighborhood look broadly representative rather than a Binance-only quirk.

## Possible impact on the question

This cross-check modestly supports the market's high Yes probability by showing BTC broadly trades near 74k, not just on Binance.

## Reliability notes

Medium-to-high usefulness as an independent contextual source. Good for triangulation, but weaker than Binance for settlement relevance.