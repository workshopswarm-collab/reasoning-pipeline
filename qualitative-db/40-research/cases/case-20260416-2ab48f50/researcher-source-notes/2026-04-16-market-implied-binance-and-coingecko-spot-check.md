---
type: source_note
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416T002737Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-2ab48f50 | market-implied
question: Will the price of Bitcoin be above $74,000 on April 17?
driver:
date_created: 2026-04-15
source_name: Binance BTCUSDT ticker and CoinGecko BTC/USD spot check
source_type: exchange API + market data aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/market-implied.md]
tags: [binance, coingecko, spot-price, btc]
---

# Summary

This source note records an external spot-price check from both Binance and CoinGecko near research time.

## Key facts extracted

- Binance API returned BTCUSDT price 74589.27 at capture time.
- CoinGecko returned bitcoin USD 74530 at capture time.
- Both are above the 74,000 threshold, and the two quotes are directionally aligned within about 0.1%.

## Evidence directly stated by source

- Binance reported spot BTCUSDT above the contract threshold.
- CoinGecko also reported BTC above the threshold.

## What is uncertain

- The contract resolves on a specific Binance 1-minute candle close at 12:00 ET on April 17, not on the current spot price at research time.
- CoinGecko is contextual rather than the source of truth for settlement.
- A single spot check does not establish persistence above the threshold into resolution time.

## Why this source may matter

The market price near 61-62% makes intuitive sense if the source-of-truth venue is already trading modestly above the line with roughly half a day remaining before resolution.

## Possible impact on the question

Current spot being about 0.7-0.8% above the threshold supports the idea that the market is not pricing a deep out-of-the-money event. It also explains why the market is above 50% but still well below certainty: modest crypto moves over less than a day can easily cross this line in either direction.

## Reliability notes

Binance is the named settlement source, so its spot print is highly relevant though not directly dispositive. CoinGecko is a useful independent contextual check confirming that the Binance reading is not obviously anomalous.