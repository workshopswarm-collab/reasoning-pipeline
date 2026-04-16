---
type: source_note
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-reach-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
driver: operational-risk
date_created: 2026-04-16
source_name: CoinGecko Solana market-chart range context
source_type: market-data-aggregator
source_url: https://api.coingecko.com/api/v3/coins/solana/market_chart/range?vs_currency=usd&from=1776052800&to=1776657600
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: medium
agent: variant-view
related_entities: [sol, solana]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [coingecko, context, independent-cross-check, volatility]
---

# Summary

This source provides an independent contextual cross-check on SOL price regime during the same April 13-19 window. It is not the governing settlement source, but it is useful for checking whether Binance-specific evidence is broadly consistent with wider market pricing.

## Key facts extracted

- CoinGecko range data for the same April 13-19 window returned **88 data points**.
- The maximum observed CoinGecko price in the returned series was approximately **88.87**.
- The minimum observed CoinGecko price in the returned series was approximately **81.74**.
- The range therefore confirms a strong move upward during the week, but still **below 90** in the independent contextual series used here.

## Evidence directly stated by source

- The broader aggregated market context appears to have approached but not clearly exceeded 90 during the checked window.
- The week’s price regime was roughly low-80s to high-88s, which is consistent with the Binance-specific evidence that the event was close but not already complete.

## What is uncertain

- CoinGecko timestamps are sampled/aggregated and may not capture every intraminute wick.
- CoinGecko is not the source of truth for resolution, so even a CoinGecko print above 90 would not settle the market.
- Small differences versus Binance are expected because aggregation methodology differs.

## Why this source may matter

It helps distinguish between two possibilities:
1. Binance is uniquely far from broader spot context, or
2. the entire market is trading near-but-below the strike.

The checked data favors the second interpretation.

## Possible impact on the question

This source supports the view that Yes is plausible because SOL has been trading near the strike, but it also supports the variant caution that the market may be treating “near 90” as too close to “already effectively touched 90.”

## Reliability notes

- Reliability is **medium-high** for broad context, lower than Binance for settlement-specific use.
- Independence versus the primary source is **medium**, because CoinGecko is an external aggregator rather than the named venue.
- Main limitation: not authoritative for final resolution and not ideal for exact threshold touch verification.