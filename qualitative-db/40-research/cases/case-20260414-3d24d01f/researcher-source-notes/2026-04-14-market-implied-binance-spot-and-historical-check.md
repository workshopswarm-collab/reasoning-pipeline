---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 1-minute candle closing at 12:00 PM America/New_York on 2026-04-19 close above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Binance public API spot price and historical 1-minute klines
source_type: exchange data / primary contextual market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/market-implied.md]
tags: [binance, spot-price, klines, verification]
---

# Summary

Binance primary data shows BTC/USDT around 74.28k at research time, comfortably above 70k, and historical noon ET 1-minute closes for the last two completed days also closed above 70k.

## Key facts extracted

- Binance ticker price at fetch time: 74,281.10 USDT for BTCUSDT.
- Recent 1-minute klines near fetch time were also around 74.25k-74.29k, consistent with the ticker.
- Historical 2026-04-13 12:00 PM America/New_York candle close from Binance API: 71,902.91.
- Historical 2026-04-14 12:00 PM America/New_York candle close from Binance API: 75,356.48.
- BTCUSDT exchange info shows Binance server timezone metadata in UTC, which matters because contract time is specified in ET and requires explicit conversion.
- BTCUSDT price filter tick size is 0.01, relevant to price precision.

## Evidence directly stated by source

- The Binance API directly returns spot ticker price and kline close prices.
- The exchange metadata directly states timezone UTC for server/exchange info.
- The kline endpoint returns minute-level open/high/low/close values with timestamps.

## What is uncertain

- The public API data used here is a strong proxy for the UI-defined source, but the contract text points specifically to the Binance web trading interface with candles selected.
- We cannot fetch the rendered Binance UI content cleanly through this tooling, so final settlement still depends on the UI-visible candle at resolution time.
- Four-plus days remain before settlement, so current price and recent noon closes are contextual rather than dispositive.

## Why this source may matter

This is the best primary contextual source for whether the market's 89% probability is broadly sensible: current venue-specific price is already well above the strike, and recent noon ET prints on the same venue are also above the line.

## Possible impact on the question

This source strongly supports the market's bullish baseline, while also highlighting the key residual risks: a venue-specific dislocation, a sharp multi-day BTC selloff, or a timing/settlement mismatch on the exact noon ET candle.

## Reliability notes

High-quality primary exchange data for contextual pricing and timing checks. Independence versus the settlement source is limited because both come from Binance, so this should be paired with the contract/rules source rather than treated as a fully independent forecast source.