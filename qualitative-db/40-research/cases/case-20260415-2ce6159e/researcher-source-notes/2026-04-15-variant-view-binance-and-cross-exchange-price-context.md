---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET Apr 16 1-minute candle close be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT live price and 1-minute klines, cross-checked with CoinGecko, Coinbase, and Kraken
source_type: exchange-api-and-market-data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2ce6159e/researcher-analyses/2026-04-15/dispatch-case-20260415-2ce6159e-20260415T142913Z/personas/variant-view.md]
tags: [source-note, binance, btc, market-data, verification]
---

# Summary

This note captures the direct resolution-source context for the case: Binance BTC/USDT was trading around 74.4k on 2026-04-15 10:30 ET, materially above the 72k threshold, and the same general level was corroborated by major secondary market data sources.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price `74405.16000000` at fetch time.
- Binance 24h ticker returned last price `74396.13000000`, 24h high `76038.00000000`, 24h low `73514.00000000`, and weighted average `74449.99126137`.
- Binance recent 1-minute klines show BTCUSDT closing prices in the `74392`-`74473` range in the minutes around the fetch.
- The kline timestamp `1776263400000` converts to `2026-04-15T14:30:00+00:00`, which is 10:30 ET on Apr 15, confirming correct timezone alignment for the observation window.
- CoinGecko simple price endpoint returned BTC at `74428` USD with recent update timestamp.
- Coinbase spot endpoint returned BTC-USD `74419.995`.
- Kraken ticker returned last trade `74406.70000` for XBT/USD.

## Evidence directly stated by source

- Binance is currently pricing BTC/USDT roughly 2.4k above the relevant 72k threshold.
- Recent minute-level Binance candles remain above 72k and are clustered around 74.4k rather than hovering near the cutoff.
- Cross-exchange spot references are tightly aligned with Binance, reducing concern that Binance is showing a one-off idiosyncratic print at the time checked.

## What is uncertain

- This does not settle the market because resolution depends on the final Binance 1-minute candle close at 12:00 ET on Apr 16, not the current spot price on Apr 15.
- BTC can move materially intraday; a 24h move larger than 2.4k is common enough that path risk remains live.
- Cross-exchange agreement supports current price context, but only Binance BTC/USDT at the specified time governs settlement.

## Why this source may matter

This is the closest available direct evidence because the contract explicitly names Binance BTC/USDT 1-minute candle close as the source of truth. The current level versus the strike is the most direct state variable for the case.

## Possible impact on the question

The current evidence supports a high but not near-certain Yes probability. The neglected variant against an overconfident 92.5% market is that the contract is still a one-minute, next-day, exchange-specific timing event; being comfortably above 72k now is favorable but not equivalent to being safely above 72k at settlement.

## Reliability notes

- Binance is the authoritative source for contract resolution, so it is primary for settlement logic.
- Exchange APIs are machine-readable and recent, but operational quirks, temporary mismatches, or data revisions are possible.
- CoinGecko, Coinbase, and Kraken are independent enough for contextual price confirmation, though they do not govern settlement.