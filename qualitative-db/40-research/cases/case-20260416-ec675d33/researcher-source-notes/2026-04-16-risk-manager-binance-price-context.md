---
type: source_note
case_key: case-20260416-ec675d33
dispatch_id: dispatch-case-20260416-ec675d33-20260416T073538Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on 2026-04-20?
driver: reliability
date_created: 2026-04-16
source_name: Binance API ticker and daily klines
source_type: exchange API / direct market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ec675d33/researcher-analyses/2026-04-16/dispatch-case-20260416-ec675d33-20260416T073538Z/personas/risk-manager.md]
tags: [binance, btcusdt, ticker, klines, settlement-source]
---

# Summary

Binance direct data shows BTC/USDT trading materially above 72,000 on April 16, with recent daily closes mostly above the threshold and current spot near 74.9k. This supports the market's bullish baseline, while also highlighting that resolution still depends on a single future one-minute close on the same exchange.

## Key facts extracted

- Binance ticker price observed: 74,888.68 BTC/USDT.
- Recent daily closes from Binance API over the last 10 sessions were mostly above 72,000 after an earlier sub-72k stretch.
- Specific recent daily closes included approximately 72,962.70, 73,043.16, 74,417.99, 74,131.55, 74,809.99, and an in-progress latest value around 74,873.96.
- Recent realized range still includes meaningful downside swings; one day in the sample closed near 70,740.98.

## Evidence directly stated by source

- Direct exchange price level on Binance is already around 2.9k above the threshold.
- Recent Binance daily data shows BTC has spent several consecutive sessions above 72,000.

## What is uncertain

- Daily klines are contextual only; this market resolves on a specific 1-minute candle at noon ET on April 20.
- Current spot being above the strike does not guarantee the specific settlement minute remains above it.
- The sampled recent history is short and does not directly measure intraday noon ET variance.

## Why this source may matter

This is the authoritative source class named by the contract. It grounds the analysis in the exact exchange and pair that will settle the market.

## Possible impact on the question

Current direct exchange pricing supports a Yes-lean, but the contract's narrow resolution window means the key risk is not broad exchange disagreement; it is timing fragility and possible short-horizon volatility around the settlement minute.

## Reliability notes

High-quality direct source for price context because it comes from Binance itself. Its limitation is scope: it informs current state, not the future settlement candle.