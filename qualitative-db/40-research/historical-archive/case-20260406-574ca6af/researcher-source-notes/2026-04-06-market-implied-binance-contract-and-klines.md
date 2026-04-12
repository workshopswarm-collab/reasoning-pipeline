---
type: source_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
analysis_date: 2026-04-06
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260406-574ca6af | market-implied
question: Will Ethereum reach $2,200 March 30-April 5?
driver: crypto-price-threshold-resolution
date_created: 2026-04-06
source_name: Polymarket contract text and Binance ETHUSDT 1m klines API
source_type: primary + direct
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-march-30-april-5 ; https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&startTime=1774828800000&endTime=1775433599000&limit=1000
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum, binance, polymarket]
related_drivers: [crypto-price-threshold-resolution]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [primary-source, contract-rules, binance, klines, settlement]
---

# Summary

The Polymarket contract text explicitly makes Binance ETH/USDT 1-minute candle highs the governing source of truth. A direct Binance klines API pull over the queried window returned 1,000 rows with a maximum observed high of 2085.00, well below 2200, so the sampled direct evidence points away from a qualifying touch and also clarifies that DEX or other exchange prints do not matter.

## Key facts extracted

- Contract text: market resolves Yes if any Binance 1-minute candle for ETH/USDT during the titled date range has a final High >= 2200.
- Contract text: resolution source is Binance ETH/USDT with 1m candles.
- Contract text: prices from other exchanges, different trading pairs, or spot markets will not be considered.
- Direct Binance API query to `/api/v3/klines` with `symbol=ETHUSDT&interval=1m` returned 1,000 rows for the queried range.
- In that direct pull, the maximum observed `High` was 2085.00.
- The max-high row in the queried sample opened at Unix ms `1774876860000` and closed at `1774876919999`.

## Evidence directly stated by source

- The governing source of truth is Binance ETH/USDT 1-minute candle highs.
- The threshold is an intraperiod high, not a close.
- Non-Binance, non-ETH/USDT, and non-specified price surfaces are excluded.

## What is uncertain

- The Binance API call used here returned only 1,000 rows, so it is not by itself a full-window audit of every minute from March 30 through April 5.
- I did not obtain a second independent historical price dataset that reproduces Binance's exact 1-minute highs for the full period.
- I did not find case-specific market-maker attribution rules beyond the explicit contract language; the main practical rule is source exclusivity to Binance ETH/USDT 1m highs.

## Why this source may matter

This source pair is the core of the case. The contract text resolves the cex-vs-dex ambiguity directly, and the Binance klines pull gives direct evidence about whether the threshold was reached on the governing venue.

## Possible impact on the question

If further Binance 1-minute data for the full window continues to show no high at or above 2200, then the fair value should be materially below the market's implied 74%. If a later minute in the full window prints >=2200 on Binance ETH/USDT, then the contract resolves Yes regardless of what DEXes or other venues did.

## Reliability notes

- Contract text from the market page is the authoritative rules surface available to traders.
- Binance klines API is a direct exchange data surface and therefore highly relevant.
- The main limitation is completeness of the sampled window because of the 1,000-row API limit in this specific pull.