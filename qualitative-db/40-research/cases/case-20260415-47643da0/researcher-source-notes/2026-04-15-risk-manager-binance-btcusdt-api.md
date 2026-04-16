---
type: source_note
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API BTCUSDT ticker and 1m klines
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-47643da0/researcher-analyses/2026-04-15/dispatch-case-20260415-47643da0-20260415T010752Z/personas/risk-manager.md]
tags: [binance, btcusdt, spot-price, resolution-source, direct-evidence]
---

# Summary

Direct pull from Binance public API provides a recent BTC/USDT spot price and recent 1-minute kline data. This is not itself the stated Polymarket settlement UI surface, but it is a direct Binance data surface that materially supports understanding the current level versus the 72,000 threshold and the mechanics of a 1-minute close.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price `74680.51000000` at research time.
- Binance 1-minute klines endpoint returned recent candles with closes in the mid-74.6k to 74.7k range.
- Recent 1-minute closes were roughly 2.6k above the 72,000 threshold.
- The contract resolves off the Binance BTC/USDT 12:00 ET 1-minute candle close on April 17, so the relevant operational object is a single exact 1-minute close rather than a daily average or another exchange print.

## Evidence directly stated by source

- Public Binance API response for ticker price: `{"symbol":"BTCUSDT","price":"74680.51000000"}`.
- Public Binance API response for recent 1m klines showed recent closes around `74690.86`, `74655.53`, and `74680.51`.

## What is uncertain

- The API endpoint is a direct Binance data surface, but the contract text specifically names the Binance trading interface with `1m` and `Candles` selected; final settlement could in practice key off what appears there.
- Current price is not enough by itself because the market resolves at a precise future minute close.
- BTC can move materially over ~38 hours; being above the threshold now does not eliminate downside path risk.

## Why this source may matter

This is the best direct evidence available in-run for the underlying reference market level and for how far BTC currently sits above the contract threshold.

## Possible impact on the question

The source supports a high yes probability because BTC is currently well above 72,000 on Binance itself, but it does not settle the market. Risk remains from crypto volatility, event-driven selloffs, or a sharp drawdown into the specific noon ET minute on April 17.

## Reliability notes

- High credibility as an official Binance public API surface.
- Strong recency.
- Independence is limited because both current-price and minute-candle mechanics come from the same exchange ecosystem named by the contract.
- Good direct evidence for current state, not direct evidence for final resolution.