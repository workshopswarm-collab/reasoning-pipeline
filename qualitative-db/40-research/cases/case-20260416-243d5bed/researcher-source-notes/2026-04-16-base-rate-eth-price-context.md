---
type: source_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: asset-price-context
entity: ethereum
topic: ETH recent trading range and outside-view threshold context
question: How demanding is an ETH > 2300 noon-ET print on April 17 relative to recent prices?
driver: reliability
date_created: 2026-04-16
source_name: CoinGecko ETH market chart API
source_type: secondary-contextual
source_url: https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=90&interval=daily
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/base-rate.md]
tags: [source-note, coingecko, context, base-rate, threshold]
---

# Summary

CoinGecko 90-day ETH/USD daily price context suggests 2300 is not an extreme upside threshold but also not a trivially safe level. In the pulled 91-point daily series, about 25% of observations were above 2300. However, the most recent several daily points cluster near or above the threshold, including the latest reading near 2337.

## Key facts extracted

- In the pulled 90-day daily ETH/USD series, roughly 25% of daily observations were above 2300.
- The 90-day range ran from about 1821 to 3307.
- The latest few daily readings were approximately 2323, 2359, and 2337.
- The most recent 10 daily observations include several values near the 2300 line rather than far below it.

## Evidence directly stated by source

- CoinGecko market-chart output provides timestamped ETH/USD price series.

## What is uncertain

- CoinGecko ETH/USD is not the settlement source; Binance ETH/USDT noon-ET 1-minute close is.
- Daily data blurs intraday path dependence and does not directly tell us the probability of one exact 1-minute close tomorrow.
- Stablecoin basis and exchange-specific pricing can create small deviations versus ETH/USD aggregators.

## Why this source may matter

It provides the outside-view backdrop for whether 2300 should be thought of as an easy hold, a demanding breakout, or a near-current-level coin flip zone.

## Possible impact on the question

The source pushes against two overreactions: it argues against treating 2300 as a remote moonshot, but also against treating a one-minute print above 2300 as nearly guaranteed just because ETH is modestly above it right now.

## Reliability notes

- Good contextual source for recent market range and base-rate framing.
- Not authoritative for settlement.
- Best used as secondary/contextual evidence paired with Binance-specific contract mechanics and current Binance spot context.