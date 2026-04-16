---
type: source_note
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance spot API + Polymarket market rules page
source_type: primary_plus_resolution_context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-881aa4d0/researcher-analyses/2026-04-16/dispatch-case-20260416-881aa4d0-20260416T044756Z/personas/market-implied.md]
tags: [binance, polymarket, resolution-rules, spot-price, direct-source]
---

# Summary

This source bundle establishes both the contract mechanics and the current direct market context. Polymarket states that resolution depends on the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17, specifically the final close price. Direct Binance spot data checked during this run shows BTC/USDT trading materially above the $70,000 threshold.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close above 70,000.
- The rules explicitly say Binance BTC/USDT is the source of truth, not other exchanges or pairs.
- Direct Binance ticker API check during this run returned BTCUSDT price `74735.47000000`.
- Direct Binance 1-minute kline API check during this run showed recent closes clustered around 74.7k-75.0k, confirming the ticker was not an isolated bad print.
- At the run timestamp, spot was roughly 6.8% above the 70,000 threshold.

## Evidence directly stated by source

- Polymarket directly states the governing resolution mechanics and source of truth.
- Binance directly states contemporaneous BTC/USDT spot and 1-minute candle data.

## What is uncertain

- The outcome depends on the specific noon ET April 17 minute close, not the current overnight April 16 level.
- A large intraday drawdown before noon ET April 17 could still invalidate a Yes resolution.
- Public checks here do not guarantee no Binance operational anomalies or data-display quirks at resolution time.

## Why this source may matter

This is the highest-value source bundle for the case because it combines the governing contract text with the directly relevant trading venue and pair.

## Possible impact on the question

The current direct evidence strongly supports the market's near-certain Yes pricing, because BTC/USDT is already well above 70k and the contract uses Binance BTC/USDT specifically.

## Reliability notes

- Polymarket rules page is authoritative for contract wording but not for future price.
- Binance API is authoritative for current Binance spot context and highly relevant because Binance is also the resolution venue.
- Independence is only moderate because both direct price context and settlement venue point to Binance, but that concentration is appropriate here because Binance is explicitly the source of truth.