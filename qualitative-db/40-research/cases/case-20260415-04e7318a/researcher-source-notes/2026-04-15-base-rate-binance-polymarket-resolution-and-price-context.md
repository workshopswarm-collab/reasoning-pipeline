---
type: source_note
case_key: case-20260415-04e7318a
dispatch_id: dispatch-case-20260415-04e7318a-20260415T145259Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT daily klines API plus Polymarket market rules page
source_type: primary-plus-contextual
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=10
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [crypto, bitcoin, polymarket, binance, resolution-source]
---

# Summary

This note combines the direct settlement mechanics visible on the Polymarket event page with recent Binance BTCUSDT daily price context. Together they establish both the governing source of truth and the current outside-view baseline that BTC is already trading materially above the $70,000 threshold several days before the April 20 noon ET resolution check.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on April 20, using the final Close price.
- The contract requires the Binance BTC/USDT close to be strictly higher than $70,000.
- Recent Binance daily closes from April 6 through April 15 were: 68,853.66; 71,924.22; 71,069.93; 71,787.97; 72,962.70; 73,043.16; 70,740.98; 74,417.99; 74,131.55; and approximately 74,133.90 at fetch time for April 15.
- In that 10-day sample, 8 of 10 daily closes were above $70,000 and the last 3 completed daily closes before the fetch were all above $70,000.
- The threshold is not close to spot in this sample; BTC is roughly 5-6% above the line rather than sitting on it.

## Evidence directly stated by source

- Polymarket rules page directly states the resolution source, timing convention, exchange/pair specificity, and the strict-higher-than requirement.
- Binance API directly states the recent BTCUSDT OHLC values used here for context.

## What is uncertain

- Daily candles are not the same as the exact April 20 12:00 ET 1-minute candle, so this is contextual evidence rather than direct settlement evidence.
- A several-day crypto move can easily exceed 5%, so being above $70,000 today does not guarantee being above $70,000 at resolution.
- Binance UI-specific display/rounding for the exact 1-minute candle still matters at settlement, though the rules make the source surface clear.

## Why this source may matter

- It is the cleanest direct verification of contract mechanics available in the run.
- It provides the most relevant outside-view context: BTC is already trading above the threshold and has done so on most recent days, which raises the prior probability that the April 20 noon close also clears the line.

## Possible impact on the question

This source set pushes toward Yes relative to a neutral prior because the asset is already above the required level by a visible margin and the governing source-of-truth is explicit. It does not settle the market today, but it supports a high-probability view rather than certainty.

## Reliability notes

- Binance is the named resolution source, so source-of-truth ambiguity is low.
- The daily kline API is authoritative for price context, but it is not the exact settlement-time 1-minute candle.
- Polymarket’s event page is the relevant contextual source for contract wording and timing, but it is derivative of the underlying exchange data for settlement.