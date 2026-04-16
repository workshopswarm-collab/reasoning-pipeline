---
type: source_note
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-btcusdt-price-and-resolution-mechanics
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance spot API (ticker + 1m klines + daily uiKlines)
source_type: exchange_api
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
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-5baa54ee/researcher-analyses/2026-04-16/dispatch-case-20260416-5baa54ee-20260416T032738Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, candles, resolution-source, price-level]
---

# Summary

Binance direct market data shows BTC/USDT trading materially above 70000 during this research run, with the latest fetched spot price at 75042.98 and recent daily closes in the low-to-mid 74000s. Because the contract resolves from the Binance 1-minute candle close at 12:00 ET on April 20, this source is both the governing source-of-truth family and the best direct evidence that the market currently has a sizable cushion above the strike.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price of 75042.98000000.
- Recent 1-minute klines around fetch time showed closes clustered around 75000-75043.
- Recent daily uiKlines show BTC/USDT closed at 74417.99, 74131.55, 74809.99, and was trading 75042.98 intraday on the current day.
- The strike for the market is 70000, implying roughly a 5000-point cushion at fetch time.

## Evidence directly stated by source

- Direct ticker output: symbol BTCUSDT, price 75042.98000000.
- Direct 1-minute kline outputs include close values such as 75032.91, 75037.84, 75000.00, 75035.94, and 75042.98.
- Direct daily uiKline outputs show recent daily closes consistently above 70000 over the sampled period.

## What is uncertain

- The market resolves on a specific 12:00 ET one-minute close on April 20, not on the current price or daily close.
- Binance API timestamps are UTC epoch milliseconds; ET conversion for the resolution minute must still be handled explicitly at settlement.
- A sharp crypto selloff before or during the resolution window could still invalidate the current cushion.

## Why this source may matter

This is the closest thing to an authoritative pre-resolution source because the market itself says Binance BTC/USDT 1-minute candle close is the governing metric. It establishes both current distance from the threshold and the exact surface later reviewers should trust most.

## Possible impact on the question

Strongly supports a high-probability Yes view unless there is a large downside move before April 20 noon ET or a Binance-specific market anomaly near the resolution minute.

## Reliability notes

High reliability for the contract because it is the designated exchange/source family. Residual risk is not about source credibility but about operational details: exact candle selection at 12:00 ET, exchange-specific prints, and the possibility of a fast move into the settlement window.