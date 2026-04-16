---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-d9ca8ddf | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API cross-check with CoinGecko spot reference
source_type: exchange-api-and-market-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager.md, risk-manager.sidecar.json, assumptions/risk-manager.md, evidence/risk-manager.md]
tags: [binance, coingecko, spot-price, verification-pass, timing-risk]
---

# Summary

This source note captures the additional verification pass on live price context and exchange mechanics.

## Key facts extracted

- Binance spot API returned BTCUSDT around **74,917.99** during the run.
- Binance 1-minute klines showed recent closes near **74.8k-75.1k**, well above the 72,000 strike.
- Binance exchange info confirmed BTCUSDT is an active trading symbol and the pair uses a **0.01** tick size in the API metadata.
- CoinGecko simple price returned Bitcoin around **74,915 USD**, closely matching Binance spot context.
- Binance server time and recent klines were consistent with the current run timestamp, supporting that the live check was current.

## Evidence directly stated by source

- Direct from Binance: current BTCUSDT price and recent 1-minute candle closes.
- Direct from CoinGecko: independent spot reference in roughly the same price region.

## What is uncertain

- These checks do not settle the market because the contract depends specifically on the **April 17, 2026 12:00 ET** Binance 1-minute candle close.
- A one-day move of several percent is normal for BTC; current margin above 72k reduces but does not eliminate downside risk.
- CoinGecko is contextual rather than governing for settlement.

## Why this source may matter

This is the most important extra verification pass for a high-confidence market. It tests whether the market's extreme probability is grounded in a large current price cushion and whether an independent contextual source broadly agrees on price level.

## Possible impact on the question

The live price cushion materially supports a Yes view, but the note also clarifies the main residual risk: BTC only needs a modest drawdown before the exact noon ET candle on April 17 to flip the contract to No.

## Reliability notes

Binance is primary for settlement venue and direct market state. CoinGecko is a useful independent contextual source, though not independent in a perfect microstructure sense because it aggregates exchange data. Independence is therefore medium rather than high.