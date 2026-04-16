---
type: source_note
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: protocols
entity: solana
topic: case-20260415-5ecb60de | market-implied
question: Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above 80?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko Solana market data
source_type: contextual-market-data
source_url: https://api.coingecko.com/api/v3/coins/solana
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: modestly-supports-yes
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/market-implied.md]
tags: [coingecko, spot-context, corroboration]
---

# Summary

This note provides an independent contextual market-data check. CoinGecko also showed Solana near 84.93, broadly corroborating the Binance spot context used by the contract.

## Key facts extracted

- CoinGecko returned Solana `market_data.current_price.bmd = 84.93`.
- That level is nearly identical to Binance spot around 84.87-84.93 at the time of review.
- The corroboration suggests the contract is not relying on an obviously stale or anomalous Binance print.

## Evidence directly stated by source

- CoinGecko current USD-equivalent price for Solana was listed around 84.93.
- CoinGecko classifies Solana as a major Layer 1 crypto asset with broad market coverage.

## What is uncertain

- CoinGecko is not the settlement source and may aggregate across venues or use derived pricing.
- This does not address the exact noon ET minute close on April 19.
- A corroborating price snapshot now does not materially reduce future volatility risk.

## Why this source may matter

It functions as an additional verification pass, useful because the market-implied probability is extreme at 90%. It helps check whether Binance spot context is broadly representative of the wider market rather than a one-venue outlier.

## Possible impact on the question

This corroboration modestly supports the market's Yes lean by showing SOL is not just barely above 80 on an isolated venue. However, its impact is limited because the contract resolves only on Binance's exact minute-close.

## Reliability notes

- CoinGecko is a credible contextual source for spot levels, but secondary rather than authoritative here.
- Independence is medium: it is distinct from Binance's direct API but still reflects the same underlying market ecosystem.