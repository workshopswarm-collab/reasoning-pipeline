---
type: source_note
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchange-market-data
entity: btc
topic: case-20260416-b08a3934 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15T22:42:00-04:00
source_name: Binance public market data endpoints for BTCUSDT
source_type: authoritative market data / direct exchange source
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
downstream_uses: []
tags: [binance, btcusdt, direct-source, current-price, candle-data]
---

# Summary

Direct Binance public market-data endpoints showed BTCUSDT around 75,101.71 at the time checked, roughly 4.3% above the 72,000 threshold. Recent 1-minute klines also showed closes around 75,025 to 75,131, confirming the pair was comfortably above the target at the time of verification.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price 75,101.71.
- Recent 1-minute kline closes included values around 75,029.83, 75,025.25, 75,048.63, 75,131.00, and 75,101.71.
- Spot level at check time was about 3,101.71 above the threshold.
- That margin is meaningful but still small enough for a volatile asset that a one-day reversal remains plausible.

## Evidence directly stated by source

- Binance direct API response reported the current BTCUSDT last price.
- Binance direct API response reported recent 1-minute OHLCV candles for BTCUSDT.

## What is uncertain

- The contract settles on the Apr 17 12:00 ET one-minute close, not the current price on Apr 15/16.
- A large overnight or intraday move could erase the current cushion.
- Direct API responses do not by themselves prove the exact noon ET candle that will exist tomorrow.

## Why this source may matter

This is the clearest direct source for both settlement mechanics and current state. It anchors the analysis in the exact exchange and pair named by the contract rather than using another venue or generic BTC references.

## Possible impact on the question

Current direct pricing supports a Yes-lean because BTCUSDT is already materially above 72,000. But because settlement is tied to one exact minute tomorrow, the source also highlights the residual path risk: the thesis only holds if the pair stays above 72,000 through the specific resolution window.

## Reliability notes

High reliability for direct exchange market data and highly relevant because it matches the contract's named source. It is still a snapshot rather than the final settlement print, so it reduces but does not eliminate uncertainty.