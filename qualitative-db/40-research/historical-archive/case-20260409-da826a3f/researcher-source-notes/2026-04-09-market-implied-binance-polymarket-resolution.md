---
type: source_note
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260409-da826a3f | market-implied
question: Will the Binance BTC/USDT 1 minute candle for 12:00 ET on 2026-04-10 close above 68000?
driver: operational-risk
date_created: 2026-04-09
source_name: Polymarket rules + Binance BTCUSDT API surface
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-10
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-da826a3f/researcher-analyses/2026-04-09/dispatch-case-20260409-da826a3f-20260409T211410Z/personas/market-implied.md]
tags: [polymarket, binance, resolution-criteria, timing]
---

# Summary

This note captures the governing market rule and the practical Binance minute-candle timing behavior relevant to the Apr 10 noon ET settlement check.

## Key facts extracted

- Polymarket rules say the market resolves from the Binance BTC/USDT 1 minute candle for **12:00 in the ET timezone (noon)** on the date in the title.
- The rule specifies the relevant field is the candle's final **"Close"** price and that price must be **higher than 68,000** for Yes.
- Binance public API `api/v3/klines` returns 1-minute BTCUSDT candles with an open timestamp, close timestamp, and final close price.
- On Apr 9, 2026 at run time, BTC/USDT on Binance was about **72.3k**, materially above the 68k threshold.
- Converting the settlement timestamp shows **2026-04-10 12:00 ET = 2026-04-10 16:00 UTC**.
- Recent Binance 1m klines show that a candle opened at `21:14:00 UTC` maps to `17:14:00 ET` and closes at `17:14:59.999 ET`, which supports interpreting the target settlement candle as the minute beginning at 12:00:00 ET and ending at 12:00:59.999 ET.

## Evidence directly stated by source

- Polymarket directly states the market resolves to Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on Apr 10 has a final close above 68,000.
- Binance directly exposes 1m klines and ticker prices for BTCUSDT.

## What is uncertain

- Binance web UI wording references "Candles" with 1m selected, but the public website fetch did not yield a clean readable extraction; API behavior was used as a verification/context surface instead.
- There is slight residual ambiguity only if Polymarket internally interprets "12:00" differently than the minute bucket labeled by its start time, but observed Binance kline structure strongly suggests start-time labeling.
- The market resolves tomorrow, so intraday volatility before 12:00 ET can still change the outcome.

## Why this source may matter

It defines the source of truth and narrows the key failure mode from broad BTC direction to one specific minute-close on one venue and pair.

## Possible impact on the question

Because BTC is already ~4.3k above the strike, the market's very high probability can be rationalized if traders mainly view the relevant risk as one-day downside tail risk plus any settlement/timing mismatch. The timing mechanics matter because a wrong ET/UTC mapping or wrong minute interpretation could create false confidence.

## Reliability notes

- Polymarket rules are the governing resolution language, so they are authoritative for contract interpretation.
- Binance API is a direct exchange surface and strong practical verification source for timestamp and close-price structure.
- CoinGecko was used separately only as a low-detail independent spot cross-check, not as the source of truth.
