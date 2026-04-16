---
type: source_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API + Polymarket rules page
source_type: exchange-api-and-market-rules
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-c0464347/researcher-analyses/2026-04-15/dispatch-case-20260415-c0464347-20260415T011958Z/personas/variant-view.md]
tags: [binance, polymarket, contract-check, timing]
---

# Summary

This note verifies the direct source-of-truth surface named by the contract and checks current BTC/USDT levels against the 70,000 threshold.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT **1 minute candle** for **12:00 ET (noon)** on April 20, using the candle's final **Close** price.
- The market is specifically about **Binance BTC/USDT**, not another exchange or pair.
- Binance ticker API showed BTCUSDT around **74.68k** on 2026-04-15 during this research pass.
- Binance 24h ticker showed a same-day high around **76,038** and low around **73,795**, implying recent realized volatility of roughly 3% intraday.
- Binance daily klines for the prior week showed closes mostly between **~70.7k and ~74.6k**, so 70k is below the current spot level but not so far below that a multi-day drawdown is impossible.

## Evidence directly stated by source

- Direct from Polymarket rules page: resolution uses Binance BTC/USDT 1m candle close at 12:00 ET on the named date.
- Direct from Binance API: spot and recent 1m / 1d price data place BTC well above 70k at research time.

## What is uncertain

- The API endpoints are direct Binance data surfaces, but the contract specifically references the Binance trading UI candle display rather than the public REST API; these should normally align, but the settlement surface is the UI candle.
- The April 20 noon ET candle has not occurred yet, so all current price evidence is contextual rather than outcome-settling.
- A sharp weekend or macro-driven selloff before the resolution window could still push BTC below 70k.

## Why this source may matter

It establishes the governing resolution mechanics and confirms the threshold is currently meaningfully in-the-money rather than near the strike.

## Possible impact on the question

This source supports a high Yes probability because BTC is currently several thousand dollars above the strike and the contract only asks whether the specified noon ET Binance close stays above 70k on April 20. It also highlights the main residual risk: path-dependent volatility over the next five days, not rule ambiguity about exchange choice.

## Reliability notes

- High reliability for exchange price context because Binance is the named resolution source.
- Medium residual operational ambiguity because the contract references the Binance UI candle, while this check used public API endpoints for faster verification.
- Independence is limited because both the pricing context and settlement source come from the same exchange family; this is good for directness but not independent corroboration.