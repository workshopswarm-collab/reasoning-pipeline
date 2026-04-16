---
type: source_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: case-20260416-305ed3c4 | market-implied
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2200?
driver: reliability
date_created: 2026-04-16
source_name: Binance Spot API market data + Polymarket contract page
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/market-implied.md]
tags: [binance, polymarket, ethusdt, source-note, market-implied]
---

# Summary

This source note pairs the governing contract wording on Polymarket with direct Binance spot-market data relevant to the resolution source.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance ETH/USDT 1-minute candle for **12:00 ET on Apr 17, 2026** has a final **Close** above 2200.
- The Polymarket rules explicitly say the source of truth is Binance ETH/USDT with **1m** candles, not another exchange or pair.
- Binance Spot API documentation confirms `/api/v3/klines` returns candlestick bars with a defined close price field and supports `1m` intervals.
- Direct spot pull from Binance on 2026-04-16 around 19:02Z returned `{"symbol":"ETHUSDT","price":"2343.56000000"}`.
- Direct recent 1-minute klines from Binance around the same time showed closes clustered around **2343.1 to 2343.56**, well above 2200.

## Evidence directly stated by source

- Polymarket contract text: Yes if the Binance 1-minute candle for ETH/USDT at 12:00 ET on the specified date has a final close above the strike.
- Binance API docs: `/api/v3/klines` provides kline/candlestick bars, including open time, close time, open/high/low/close, and supports `1m` interval.
- Binance live data: ETHUSDT spot price and recent 1-minute closes were above 2200 at time of check.

## What is uncertain

- This source does not guarantee the Apr 17 noon ET close will remain above 2200; it only confirms the market is currently far above the strike and that the contract mechanics are checkable against Binance.
- Polymarket references the Binance website chart rather than the public REST API as the formal resolution surface, so there is minor implementation ambiguity even though both should normally align.

## Why this source may matter

This is the most important source pair for a date-specific crypto threshold market because it addresses both the governing resolution mechanics and the current underlying state of the asset on the named venue/pair.

## Possible impact on the question

Because ETH/USDT on Binance was about **6.5% above** the 2200 threshold less than a day before resolution, the market-implied high probability is understandable. The main residual risk is not current level but whether ETH can fall materially before the specific noon ET minute close on Apr 17.

## Reliability notes

- Binance is the named resolution source, which makes it the authoritative direct source for this contract.
- Binance API documentation is a high-credibility technical source for interpreting what the 1-minute close represents.
- The Polymarket page is authoritative for the contract wording but not for the eventual price print itself.
- Independence is limited because contract mechanics and spot data are tightly linked to the same exchange ecosystem, so a contextual secondary source is still useful.