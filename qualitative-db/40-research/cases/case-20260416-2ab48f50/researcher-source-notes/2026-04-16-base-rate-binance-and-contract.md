---
type: source_note
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-2ab48f50 | base-rate
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket market page
source_type: exchange API plus market contract page
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=30 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/base-rate.md]
tags: [source-note, binance, polymarket, contract, timing]
---

# Summary

This note captures the governing settlement source and a direct spot/context check relevant to the April 17 noon ET BTC/USDT threshold market.

## Key facts extracted

- Polymarket states this market resolves from the Binance BTC/USDT **1 minute candle for 12:00 ET (noon)** on April 17, using the candle's final **Close** price.
- The threshold is **strictly higher than $74,000**; equal to 74,000.00 would resolve No.
- Resolution is exchange-specific: **Binance BTC/USDT**, not a composite BTC index and not another venue.
- A live Binance ticker pull during this run returned **BTCUSDT = 74577.44**.
- Recent Binance daily candles in the API output show BTC trading mostly in the high-60k to low/mid-70k range, with at least one recent daily high above 74k and substantial day-to-day swings.

## Evidence directly stated by source

- The Polymarket market page directly states the rule text and governing source.
- The Binance API directly states current price and recent daily OHLC levels for BTCUSDT.

## What is uncertain

- The contract resolves from one very specific minute close tomorrow at noon ET, not from the current spot price.
- Daily kline data is contextual only; it does not reveal the exact intraday distribution around noon ET on the settlement date.
- Binance web UI remained hard to scrape directly, so I used Binance public API for context and Polymarket's own quoted rule text for contract interpretation.

## Why this source may matter

It is the highest-value source pair for this case: the market page defines what counts, and Binance is the source of truth for the observed price path.

## Possible impact on the question

These sources support a base-rate view that the question is close to a one-day directional threshold event rather than a broad thesis bet. Since current spot is already slightly above 74k but recent daily volatility is material, the outside-view baseline should be around a modestly-above-even chance rather than near-certainty.

## Reliability notes

- Polymarket is authoritative for contract wording but not for the actual settlement print.
- Binance is authoritative for the settlement print but the exact resolving observation is a future 12:00 ET 1-minute close, so any current-price inference is necessarily provisional.
- Evidence independence is medium: the contract page and Binance are distinct sources, but both relate to the same market mechanics rather than independent causal forecasting models.
