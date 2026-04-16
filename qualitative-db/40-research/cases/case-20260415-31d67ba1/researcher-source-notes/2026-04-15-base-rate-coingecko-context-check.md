---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: CoinGecko bitcoin spot price check
source_type: contextual_market_data
source_url: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd
source_date: 2026-04-15
credibility: medium_high
recency: high
stance: neutral
certainty: medium_high
importance: medium
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [coingecko, contextual, price-check, btc]
---

# Summary

This is an external contextual price check used as an additional verification pass against Binance and Polymarket.

## Key facts extracted

- CoinGecko simple price endpoint showed bitcoin at 74,375 USD on 2026-04-15.
- This is effectively the same level as the contemporaneous Binance spot snapshot near 74,374.

## Evidence directly stated by source

- The endpoint returned bitcoin.usd = 74375.

## What is uncertain

- CoinGecko aggregates exchange data and is not the governing settlement source.
- It does not answer the exact April 17 noon ET candle-close question by itself.

## Why this source may matter

It provides an independent contextual confirmation that the broader market reference level is in the mid-74k area rather than near the 70k boundary.

## Possible impact on the question

The close agreement with Binance reduces the chance that the thesis is being driven by one stale or anomalous quote. It supports, but does not settle, a high-probability Yes view.

## Reliability notes

Useful as a secondary source and independence check, but inferior to Binance for settlement purposes because the contract is exchange-specific.
