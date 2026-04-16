---
type: source_note
case_key: case-20260414-9c18e804
dispatch_id: dispatch-case-20260414-9c18e804-20260414T135145Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Polymarket market page and embedded rules payload
source_type: market/rules page
source_url: https://polymarket.com/event/what-price-will-bitcoin-hit-april-13-19
source_date: 2026-04-14
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414T135145Z/personas/variant-view.md]
tags: [polymarket, rules, resolution, market-implied-probability]
---

# Summary

This source established both the market-implied probability baseline and the governing resolution mechanics for the case.

## Key facts extracted

- The assigned market `Will Bitcoin reach $76,000 April 13-19?` appeared on the Polymarket event page with outcomePrices approximately `0.825` / `0.175`, best bid/ask around `0.81` / `0.84`, and active status on 2026-04-14.
- The rule text states: the market resolves to **Yes** if any Binance BTC/USDT **1-minute candle High** during the date range in the title is equal to or greater than $76,000.
- The rule text also states that prices from other exchanges, different trading pairs, or spot markets are **not** considered.
- The event page simultaneously showed adjacent ladder markets such as `Will Bitcoin reach $74,000 April 13-19?` already resolved Yes and `Will Bitcoin reach $78,000 April 13-19?` trading around 0.4485, which helps contextualize the $76k rung.

## Evidence directly stated by source

- Governing source of truth is Binance BTC/USDT High prices on 1-minute candles.
- Resolution is threshold-based and path-dependent: a single qualifying 1-minute high is sufficient.
- Polymarket consensus for the $76k rung was roughly 82.5% at observation time.

## What is uncertain

- The page payload did not provide a clean timestamped history for how quickly the $76k rung repriced after the latest BTC rally.
- Polymarket can lag or move around microstructure events; it is a market signal, not the settlement source.

## Why this source may matter

It defines the exact contract mechanics, removing ambiguity about whether the relevant price is a close, an index price, a CoinGecko spot print, or some daily summary.

## Possible impact on the question

Because the contract only needs **one** Binance 1-minute high at or above $76,000, proximity matters more than end-of-week closing strength. That slightly favors Yes versus narratives focused on sustained breakout confirmation.

## Reliability notes

- Strong for contract interpretation because it is the native market page and embedded rule payload.
- Weaker as a pure price source than Binance itself because the page is a derivative interface and may show delayed or rounded market data.