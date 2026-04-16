---
type: source_note
case_key: case-20260414-4e668883
dispatch_id: dispatch-case-20260414-4e668883-20260414T133938Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2400-april-13-19
question: Will Ethereum reach $2,400 April 13-19?
driver: liquidity
date_created: 2026-04-14
source_name: Binance ticker plus CoinGecko market data spot check
source_type: market data cross-check
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: market-implied
related_entities: [ethereum]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4e668883/researcher-analyses/2026-04-14/dispatch-case-20260414-4e668883-20260414T133938Z/personas/market-implied.md]
tags: [binance, coingecko, spot-price, verification]
---

# Summary

This note records the extra verification pass on current ETH price level relative to the 2400 trigger.

## Key facts extracted

- Binance ETHUSDT ticker snapshot returned `2387.54`.
- CoinGecko ETH market data snapshot returned about `2388.36` USD.
- The two independent references are very close, suggesting no obvious stale-print issue in the working price anchor.
- ETH is therefore only around 12 dollars below the 2400 trigger at the time of review.

## Evidence directly stated by source

- Direct quoted Binance price: 2387.54.
- Direct quoted CoinGecko USD price: 2388.36.

## What is uncertain

- These are current price snapshots, not forward-looking evidence.
- Neither snapshot alone proves whether any future 1-minute high will print above 2400.

## Why this source may matter

For a date-bounded weekly high market, distance-to-trigger matters a lot. If ETH is already within roughly 0.5% of the threshold with several days remaining, a high Yes probability is easier to justify.

## Possible impact on the question

This supports the market-implied view that the contract can plausibly resolve Yes even without a major trend change, because a brief intraday wick could be sufficient.

## Reliability notes

Good for live spot anchoring and extra verification, but these are contextual market-data references rather than the governing settlement source.