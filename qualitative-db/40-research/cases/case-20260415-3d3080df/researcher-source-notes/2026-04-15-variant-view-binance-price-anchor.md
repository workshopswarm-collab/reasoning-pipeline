---
type: source_note
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 be above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API BTCUSDT ticker and recent 1m klines
source_type: exchange market data / API
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/variant-view.md]
tags: [binance, btcusdt, api, price, kline]
---

# Summary

This source provides the most relevant direct price anchor because the contract resolves off Binance BTC/USDT. At review time, BTC/USDT was about 74.5k, comfortably above the 70k threshold.

## Key facts extracted

- Binance public ticker showed BTCUSDT at 74,534.15 at review time.
- Recent 1-minute klines were also in the mid-74k range.
- April 20, 2026 12:00 ET converts to 2026-04-20 16:00:00 UTC, which is the timestamp that should matter when checking the relevant Binance minute candle.

## Evidence directly stated by source

- The public exchange API directly reported the current Binance BTCUSDT price.
- Recent one-minute candles show BTC trading roughly 4.5k above the threshold, leaving a meaningful but not enormous cushion.

## What is uncertain

- This source does not settle the future April 20 noon candle; it is only a current anchor.
- Short-horizon crypto volatility can erase a multi-thousand-dollar cushion within days, especially around macro headlines or exchange-specific moves.

## Why this source may matter

Because the market resolves on Binance, Binance data deserves more weight than generic BTC/USD references from other venues.

## Possible impact on the question

The direct exchange anchor supports Yes as the base case, but the variant angle is that 85% may still be somewhat rich because the contract only needs one adverse noon print on one exchange four trading days from now.

## Reliability notes

High reliability for current price and time mapping. Independent of Polymarket for market-data purposes, though still not a final answer source until the target minute exists.