---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-data
entity: sol
topic: solana-above-80-on-april-19
question: Will the price of Solana be above $80 on April 19?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API and CoinGecko API spot context for SOL
source_type: api_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: variant-view
related_entities: [sol, solana]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-c395460f/researcher-analyses/2026-04-16/dispatch-case-20260416-c395460f-20260416T022702Z/personas/variant-view.md]
tags: [binance, coingecko, spot-price, verification]
---

# Summary

Direct exchange/API checks show SOL is currently above the $80 threshold with a modest but not enormous cushion. Independent CoinGecko spot data broadly agrees with Binance on the current price region. This supports the base Yes case, but the cushion is small enough that a few percentage points of downside over three days would defeat the contract.

## Key facts extracted

- Binance public ticker returned SOLUSDT price of 84.96 at check time.
- Recent Binance 1-minute klines around the check showed closes clustered around 84.83 to 84.96.
- Binance exchange info confirms SOLUSDT is an active trading pair and exposes a price tick size of 0.01, relevant to how the final candle close would be represented.
- CoinGecko simple price returned Solana at about 84.9 USD, consistent with Binance spot context.
- CoinGecko 2-day hourly market chart shows SOL recently trading through roughly the low-to-mid 80s, with prints materially below the current level during the prior 48 hours.

## Evidence directly stated by source

- Binance ticker: {"symbol":"SOLUSDT","price":"84.96000000"}
- Binance recent 1m klines included closes near 84.83, 84.90, 84.93, 84.91, 84.96.
- Binance exchange info for SOLUSDT listed tickSize 0.01000000.
- CoinGecko simple price: {"solana":{"usd":84.9}}

## What is uncertain

- Spot data is only a snapshot; the contract settles three days later.
- CoinGecko is contextual and may aggregate from multiple venues, so Binance remains controlling.
- Recent hourly series does not alone quantify realized volatility or event risk into April 19 noon ET.

## Why this source may matter

This source pair establishes both the current starting point and that the market is not pricing a threshold far below spot. With SOL only about $5 above the strike, the market's ~89% Yes price implicitly assumes limited downside over a narrow time window into a single-minute close.

## Possible impact on the question

Supports a moderate Yes lean because current spot is above the threshold, but also supports skepticism toward extreme confidence because the cushion is not large relative to normal crypto moves.

## Reliability notes

Binance API is the strongest source for contract-relevant pricing mechanics. CoinGecko provides a useful independent contextual cross-check but is not the settlement source.