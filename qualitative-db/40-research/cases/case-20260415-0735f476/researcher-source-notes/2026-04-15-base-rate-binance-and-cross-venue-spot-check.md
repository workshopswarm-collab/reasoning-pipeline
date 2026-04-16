---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-market
entity: btc
topic: binance and cross-venue spot checks for Bitcoin relative to 70,000 threshold
driver: reliability
date_created: 2026-04-15
source_name: Binance API ticker and 1-minute klines with CoinGecko and Coinbase spot cross-checks
source_type: exchange/API and market-data cross-check
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/base-rate.md
tags: [source-note, binance, coingecko, coinbase, btc, spot-check]
---

# Summary

This note records a direct Binance spot/API check plus independent cross-venue price checks to verify that BTC is materially above the 70,000 threshold as of the research run.

## Key facts extracted

- Binance ticker API returned **BTCUSDT = 74,605.50**.
- Binance recent 1-minute klines around **2026-04-15 16:09-16:13 ET** showed closes between roughly **74,605 and 74,770**.
- CoinGecko simple price endpoint returned **BTC = 74,748 USD**.
- Coinbase spot endpoint returned **BTC-USD = 74,671.255**.
- The Binance kline timestamps were converted to **America/New_York** and aligned to current intraday ET minutes, confirming the data were current and usable for timing sanity checks.

## Evidence directly stated by source

- Binance directly states current BTCUSDT price and recent 1-minute OHLCV closes.
- CoinGecko and Coinbase independently show BTC spot pricing in the mid-74k area.

## What is uncertain

- These checks do **not** prove the April 20 12:00 ET closing minute yet; they only show current distance from threshold.
- Spot checks cannot rule out a large drawdown before the governing minute.
- Binance API data are machine-readable and current, but this note does not independently verify every UI detail of the exact chart surface mentioned in the Polymarket wording.

## Why this source may matter

This is the main direct evidence for current state. For a short-dated threshold-close market, current distance from threshold is the dominant outside-view input.

## Possible impact on the question

Being about **6.5% above** the threshold with about five days remaining makes a Yes outcome structurally likely under ordinary BTC volatility, but not certain, because the contract depends on one exact minute close on Binance rather than a broader weekly average or any-touch test.

## Reliability notes

High recency and decent independence across sources. Binance is closest to the governing source; CoinGecko and Coinbase mainly reduce the risk of a bad single-endpoint read. Cross-source agreement was tight enough that the current-state conclusion is robust.