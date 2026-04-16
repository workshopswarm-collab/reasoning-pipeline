---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: case-20260416-cc34f737 | market-implied
question: Will the price of Ethereum be above $2,300 on April 17?
driver: reliability
date_created: 2026-04-16
source_name: Binance ETHUSDT API spot price and recent 1-minute candles
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [binance, ethusdt, spot-price, kline, source-note]
---

# Summary

Binance primary market data showed ETH/USDT around `2334.92` at fetch time, with the recent one-minute candles clustering in the low `2330s` to low `2340s`. That places spot modestly above the 2300 threshold about one day before resolution.

## Key facts extracted

- Binance ticker endpoint returned `ETHUSDT` price `2334.92000000`.
- Recent one-minute klines showed closes such as `2341.45`, `2338.73`, `2337.20`, `2334.68`, `2334.71`, `2336.04`, `2334.20`, `2334.91`, `2335.02`, `2334.92`.
- A separate earlier kline pull also showed prices around `2339` to `2342`, indicating the market was near but not barely above 2300.
- The current level implies roughly `1.5%` downside from `2334.92` to fall below `2300` by the relevant noon ET minute tomorrow.

## Evidence directly stated by source

- Binance currently prices ETH/USDT above 2300.
- Binance recent one-minute candles show short-run trading concentrated above 2330 during the check window.

## What is uncertain

- This does not show the exact April 17 12:00 ET candle yet.
- Short-horizon crypto volatility can easily exceed 1.5%, so being above 2300 now is supportive but not decisive.

## Why this source may matter

This is the same exchange family and instrument named in the contract, so it is the strongest direct contextual evidence for what the market is likely keying off.

## Possible impact on the question

Because the current price already sits modestly above the line, the market's 71% yes price looks broadly consistent with the current spot state, though not obviously conservative given the small buffer.

## Reliability notes

High relevance because Binance ETH/USDT is the governing source of truth. Still, this is contextual rather than dispositive because the contract resolves on a future minute close, not the current print.