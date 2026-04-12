---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260409-99902b0b | base-rate
question: Will the price of Bitcoin be above $70,000 on April 10?
driver: reliability
date_created: 2026-04-09
source_name: Binance API spot price and 1m klines, cross-checked with CoinGecko
source_type: exchange API plus secondary price aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-99902b0b/researcher-analyses/2026-04-09/dispatch-case-20260409-99902b0b-20260409T203957Z/personas/base-rate.md]
tags: [binance, coingecko, price-check, verification]
---

# Summary

This note records a direct Binance price check plus an independent secondary cross-check near analysis time.

## Key facts extracted

- Binance BTCUSDT last price fetched at analysis time was 72,363.48.
- Binance recent 1-minute klines showed closes around 72,375 to 72,363 immediately before and during the fetch window.
- Binance server time corresponded to 2026-04-09 16:40 ET, confirming the timing of the observed prices.
- CoinGecko cross-check showed bitcoin around 72,390 USD at nearly the same time.

## Evidence directly stated by source

- Direct exchange data places BTC/USDT more than 3% above the 70,000 threshold roughly 19 hours before the relevant noon ET observation window.
- Recent 1-minute Binance candles were not near the threshold; they were clustered in the low 72.3k range.

## What is uncertain

- This is not the resolving candle itself; it is only a current-state check.
- Bitcoin volatility over 19 hours is nontrivial, so spot being above the threshold now does not guarantee a noon-ET close above 70,000 tomorrow.

## Why this source may matter

The contract resolves off Binance, so direct Binance data is the strongest non-final evidence available before settlement. CoinGecko provides a useful independent contextual cross-check that the Binance reading is not obviously anomalous.

## Possible impact on the question

Being roughly 2.3k above the threshold shortly before resolution materially supports a Yes view on base rates, because BTC would need a fairly sharp downside move before noon ET tomorrow to finish below 70,000.

## Reliability notes

Binance API is highly relevant and primary for this contract. CoinGecko is secondary and contextual, but useful for evidence independence. Independence is medium rather than high because CoinGecko likely ingests exchange data rather than generating wholly separate underlying prices.