---
type: source_note
case_key: case-20260416-c395460f
dispatch_id: dispatch-case-20260416-c395460f-20260416T022702Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-price
entity: sol
topic: case-20260416-c395460f | market-implied
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close be above 80 on April 19, 2026?
driver: reliability
date_created: 2026-04-16
source_name: Binance SOLUSDT API and contract reference
source_type: primary_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: supports_yes
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, primary-source, resolution-source, solana, market-implied]
---

# Summary

Binance is both the live spot reference and the stated settlement source for this contract, so the most decision-relevant evidence is current SOL/USDT trading on Binance plus the exact noon-ET 1-minute-candle rule.

## Key facts extracted

- Binance spot API returned `SOLUSDT` last price `84.96000000` during this run.
- Recent 1-minute klines were accessible from Binance API, confirming the exchange is publishing granular candle data for the exact instrument referenced by the market.
- Recent 14 daily candles from Binance show SOL/USDT has closed above 80 on most recent sessions, though there were still lows below 80 inside the window and at least one close near 78-79 earlier in the sample.
- The Polymarket contract text states resolution is based specifically on the Binance SOL/USDT 1-minute candle at 12:00 ET on April 19, 2026, using the final close for that minute.

## Evidence directly stated by source

- Binance ticker endpoint directly stated the live price near 84.96.
- Binance kline endpoints directly stated recent OHLC history and minute-candle availability.
- The contract directly states the governing source of truth: Binance SOL/USDT, 1m candle, 12:00 ET, close price above 80.

## What is uncertain

- A live spot reading on April 16 does not settle the April 19 noon ET price.
- Daily candles do not tell us the exact noon ET close on resolution day.
- Weekend crypto volatility can still move SOL materially over a three-day horizon.

## Why this source may matter

This is the highest-quality source set because it anchors both current price level and exact resolution mechanics. For a short-horizon price-threshold market, direct Binance pricing matters more than broader commentary.

## Possible impact on the question

With SOL trading around 84.96 and having spent much of the recent period above 80, the market's high Yes probability has a clear basis. The main remaining risk is not source ambiguity but short-horizon price volatility that could drag the April 19 noon ET 1-minute close below 80.

## Reliability notes

High reliability for instrument definition and current price. Moderate inferential power for the future outcome because this remains a forward-looking threshold market.