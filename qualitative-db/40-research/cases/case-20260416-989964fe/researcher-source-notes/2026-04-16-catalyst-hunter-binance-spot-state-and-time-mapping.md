---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: Binance ETHUSDT spot state and resolution-time mapping
question: Will the Binance ETH/USDT 12:00 ET one-minute candle on April 17 close above 2200?
driver: reliability
date_created: 2026-04-16
source_name: Binance public API
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/catalyst-hunter.md]
tags: [binance, api, ethusdt, spot, timestamp]
---

# Summary

Binance public API currently shows ETH/USDT trading around 2353-2354, meaning spot is already comfortably above the 2200 threshold roughly a day before the relevant resolution minute. Additional checks verify how Binance timestamps 1-minute candles and how Apr 17 12:00 ET maps to UTC.

## Key facts extracted

- Binance ticker showed ETHUSDT around 2353.42-2353.66 during checks.
- Binance 24h stats showed open 2334.44, high 2385.61, low 2308.50, last 2353.66.
- Recent 1-minute klines confirm Binance returns standard OHLC candle data with close timestamps.
- Apr 17 2026 12:00 ET converts to 2026-04-17 16:00:00 UTC, epoch 1776441600000.
- ETHUSDT spot trading status is active according to exchangeInfo.
- Binance price filter tick size for ETHUSDT is 0.01, so a final close of 2200.00 would not be enough; it must close at 2200.01 or higher.

## Evidence directly stated by source

- Ticker endpoint returned: {"symbol":"ETHUSDT","price":"2353.42000000"} during the first check.
- 24h ticker returned lastPrice 2353.66, openPrice 2334.44, highPrice 2385.61, lowPrice 2308.50.
- exchangeInfo returned symbol status TRADING for ETHUSDT.
- Python timezone conversion verified Apr 17 2026 12:00 ET = Apr 17 2026 16:00 UTC.

## What is uncertain

- A current spot price above 2200 does not guarantee the exact Apr 17 noon ET close stays above 2200.
- Public API checks do not identify tomorrow's catalysts; they only show present distance from threshold and timestamp mechanics.

## Why this source may matter

This is the most direct external source for the actual instrument and exchange that will decide settlement. It materially reduces ambiguity about whether the threshold is already deeply in-the-money and how far ETH would need to fall before resolution.

## Possible impact on the question

Because ETHUSDT is currently about 153 points above the threshold, the market would need a sizable downside move before noon ET tomorrow for No to win. That pushes the key catalyst question toward whether any near-term shock could plausibly produce a >6% drop into the exact resolution minute.

## Reliability notes

High reliability for current Binance spot state and instrument metadata because this is direct exchange API output. Lower for predicting the future resolution minute, which still depends on market movement between now and then.