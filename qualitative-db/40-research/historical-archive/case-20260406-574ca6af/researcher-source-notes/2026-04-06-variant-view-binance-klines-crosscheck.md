---
type: source_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
analysis_date: 2026-04-06
persona: variant-view
topic: case-20260406-574ca6af | variant-view
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
source_name: Binance ETHUSDT 1m klines API and CoinGecko contextual cross-check
source_type: exchange market data + contextual secondary
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m
source_date: 2026-04-06
credibility: high
recency: current/historical-window
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum, binance, coingecko]
related_drivers: []
upstream_inputs: []
downstream_uses: [variant-view finding]
tags: [price-verification, binance, coingecko, crosscheck]
---

# Summary

Direct Binance 1-minute kline data for the relevant window shows ETH/USDT traded well below $2,200 on Binance during the settlement period. A CoinGecko contextual cross-check shows broader market pricing also remained below $2,200, so there is no meaningful evidence of a Binance-vs-rest-of-market divergence that would rescue a Yes case.

## Key facts extracted

- Pulled Binance ETH/USDT 1m klines from 2026-03-30 00:00 ET through the end of the named window using paginated API requests.
- Observed 9,934 one-minute rows in the pull.
- Maximum observed Binance 1m High in the pull: **2167.85**.
- Timestamp of max observed High: **2026-04-01T17:03:00Z** open time.
- Independent contextual cross-check via CoinGecko market-chart-range showed a max around **2158.96** over the same broad interval.

## Evidence directly stated by source

- Binance API data directly reports 1-minute OHLCV candles for ETHUSDT and includes the candle High used to infer whether the $2,200 threshold was ever touched on the designated venue.
- CoinGecko provides contextual aggregated price history, useful only as a secondary check rather than the settlement authority.

## What is uncertain

- The Binance API pull slightly exceeded the nominal title window on the trailing edge because the request was run after the period; however the observed max High was still materially below $2,200, so the extra trailing rows do not create threshold ambiguity.
- The Binance API endpoint is not literally the same rendered chart surface named in the market rules, but it is a direct Binance market-data source for the same pair and interval.

## Why this source may matter

This is the core empirical check against the contract rule. If Binance ETH/USDT 1m highs never reached $2,200, the market should resolve No regardless of any off-venue prints.

## Possible impact on the question

The direct kline evidence strongly supports No and substantially weakens any variant thesis based on broader ETH strength, alternative venue wicks, or stale market optimism.

## Reliability notes

High reliability for Binance as direct exchange data, though the exact UI chart named in the rule would be an even tighter surface match. CoinGecko is a useful but non-authoritative contextual check. Evidence independence is medium because both are market-data vendors reflecting the same underlying asset, but one is the governing venue and the other is a cross-source sanity check.
