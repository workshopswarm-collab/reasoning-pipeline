---
type: source_note
case_key: case-20260416-dfb8f85e
dispatch_id: dispatch-case-20260416-dfb8f85e-20260416T140232Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the price of Bitcoin be above $72,000 on April 21?
driver:
date_created: 2026-04-16
source_name: Binance public API BTCUSDT spot and 1m klines
source_type: exchange_primary
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-dfb8f85e/researcher-analyses/2026-04-16/dispatch-case-20260416-dfb8f85e-20260416T140232Z/personas/market-implied.md]
tags: [binance, btcusdt, spot, klines, settlement-source]
---

# Summary

A direct Binance API spot-check showed BTCUSDT around 73.7k during research and confirmed 1-minute kline availability consistent with the contract's settlement source.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price 73720.78000000.
- Binance 1m kline endpoint returned recent minute candles with closes including 73651.03, 73728.95, and 73720.78.
- This places spot roughly 1.7k above the 72,000 threshold about five days before settlement.

## Evidence directly stated by source

- Binance is publishing live BTCUSDT spot and recent 1m candle closes.
- The relevant market threshold is currently in-the-money by about 2.4%.
- The contract's chosen source is operationally accessible and interpretable.

## What is uncertain

- This is a single-time spot-check, not a full realized-volatility study.
- Current spot being above 72k does not guarantee the Apr 21 noon ET 1m close remains above 72k.

## Why this source may matter

It is the closest available direct source to the eventual resolution source and shows the market is pricing a threshold that is already modestly below current Binance spot.

## Possible impact on the question

If spot remains near current levels, a Yes outcome is plausible and the market's high probability is understandable. The main residual risk is multi-day BTC volatility, not contract ambiguity.

## Reliability notes

High relevance because Binance is the stated resolution venue. Main limitation is temporal: current spot is only contextual evidence for a future noon close.