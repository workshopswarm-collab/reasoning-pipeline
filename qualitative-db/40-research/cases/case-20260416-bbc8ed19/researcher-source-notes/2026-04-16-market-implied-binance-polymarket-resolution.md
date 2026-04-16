---
type: source_note
case_key: case-20260416-bbc8ed19
dispatch_id: dispatch-case-20260416-bbc8ed19-20260416T072336Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-bbc8ed19 | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on 2026-04-20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market rules plus Binance spot API market data docs and live BTCUSDT endpoints
source_type: primary-plus-resolution-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-bbc8ed19/researcher-analyses/2026-04-16/dispatch-case-20260416-bbc8ed19-20260416T072336Z/personas/market-implied.md]
tags: [polymarket, binance, resolution, btcusdt, source-note]
---

# Summary

This source set establishes both the governing contract mechanics and the live market context most relevant to whether an 84.5% implied probability for BTC/USDT > 72000 at noon ET on April 20 looks efficient.

## Key facts extracted

- Polymarket states the market resolves Yes if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 20 has a final close above 72000.
- Polymarket explicitly specifies Binance BTC/USDT, not other exchanges or other pairs.
- Binance spot API documentation states `/api/v3/klines` returns candlestick bars identified by open time and includes close price as the fifth price field.
- Binance documentation states `timeZone` can be supplied for interval interpretation, but `startTime` and `endTime` are always interpreted in UTC.
- Live Binance spot data checked during this run showed BTCUSDT around 74909.73, roughly 4.0% above 72000.
- Binance 24h ticker during this run showed BTCUSDT daily range 73514 to 75425, implying the market is pricing a buffer but not a trivial lock.

## Evidence directly stated by source

- Polymarket rules directly define the settlement condition and source of truth.
- Binance docs directly define how the kline endpoint represents the candle and close field.
- Live Binance endpoint responses directly state the observed current BTCUSDT spot price and recent daily range at run time.

## What is uncertain

- Polymarket references the Binance web chart UI as the settlement source, while this run used Binance's documented API as a strong verification/context surface rather than the literal settlement UI screenshot.
- The exact noon ET candle on April 20 has not happened yet, so all inference is probabilistic and depends on future BTC movement over roughly four days.
- Intraday volatility could still move BTC below 72000 at the specific settlement minute even if spot trades comfortably above it beforehand.

## Why this source may matter

This is the key source bundle because it covers both sides of the question: what exact condition must occur for Yes resolution, and whether current market pricing looks reasonable given live Binance BTCUSDT levels and recent realized range.

## Possible impact on the question

The source set supports a moderately bullish but not near-certain interpretation. With BTCUSDT already near 74.9k on Binance and recent lows still above 73.5k, an 84.5% market-implied probability for being above 72k at noon ET on April 20 looks broadly defensible. The main remaining risk is not contract ambiguity but normal crypto volatility over the next four days.

## Reliability notes

- Polymarket is authoritative for contract wording.
- Binance is the authoritative underlying data source named by the contract.
- Evidence independence is medium rather than high because both core sources are tied to the same market structure, though they answer different questions: contract mechanics versus live underlying price context.
- Source-of-truth ambiguity is low to medium: low on pair and threshold, medium only because Polymarket points to the Binance UI while this run also relied on Binance API documentation to make the kline mechanics auditable.