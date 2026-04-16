---
type: source_note
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on April 20, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and Binance spot API check
source_type: primary-market-rules plus direct-exchange-data
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, resolution-rules, btc]
---

# Summary

This note captures the governing resolution mechanics and a direct price verification for the case. The market resolves using the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026, specifically the final close of that minute. A direct Binance API spot query on April 15 showed BTC/USDT around 74.2k, comfortably above the 70k threshold with five days left.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 ET on the specified date has a final close higher than 70,000.
- The source of truth is Binance BTC/USDT, not other exchanges or other BTC pairs.
- Price precision is determined by the Binance source.
- Direct Binance API spot check during this run returned BTCUSDT around 74,203 to 74,221.
- Recent Binance 1-minute kline data was retrievable directly from the exchange API, confirming the source surface is accessible in machine-readable form even if the website UI is awkward to scrape.

## Evidence directly stated by source

- From Polymarket rules: the relevant condition is the Binance BTC/USDT 12:00 ET one-minute candle close on April 20.
- From Binance API during run: current BTCUSDT spot was approximately 74.2k.

## What is uncertain

- The exact candle labeling convention on the Binance web UI around ET conversion still matters operationally; the market text says 12:00 in ET timezone, so the settlement convention is tied to that phrasing rather than raw UTC timestamps.
- Spot price now does not settle the market; a sharp move lower before April 20 noon ET remains possible.

## Why this source may matter

This is the governing contract-mechanics source and the most direct current-state verification. It defines exactly what must happen for Yes and anchors the magnitude of downside needed for No.

## Possible impact on the question

Because BTC is already roughly 6 percent above the strike with only five days left, the main question becomes whether a meaningful downside catalyst can push Binance BTC/USDT below 70k exactly into the April 20 noon ET minute close.

## Reliability notes

- Polymarket rules are the primary resolution surface for interpreting the contract.
- Binance API is a direct exchange source for current BTCUSDT spot and minute candles.
- Together they are high-quality and directly relevant, though they do not by themselves eliminate path risk between now and settlement.
