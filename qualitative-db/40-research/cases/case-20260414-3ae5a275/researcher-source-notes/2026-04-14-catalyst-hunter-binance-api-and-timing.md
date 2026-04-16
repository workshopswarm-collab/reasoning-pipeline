---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-14
source_name: Binance spot API market data endpoints and live BTCUSDT data
source_type: exchange API documentation + live API
author: Binance
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/catalyst-hunter.md]
tags: [binance, api, klines, timing, verification]
---

# Summary

Binance’s API documentation confirms how 1-minute klines are defined and that a timezone parameter exists for interval interpretation, while the live BTCUSDT API showed spot trading around 74.2k on 2026-04-14 — comfortably above the 70k threshold with a 24h high above 76k and 24h low above 73k.

## Key facts extracted

- Binance documents `GET /api/v3/klines` as the endpoint for candlestick bars.
- Klines are uniquely identified by **open time**.
- The endpoint supports `interval=1m`.
- The documentation states `timeZone` defaults to `0 (UTC)` and, if provided, intervals are interpreted in that timezone instead of UTC.
- Binance also states `startTime` and `endTime` are always interpreted in UTC regardless of `timeZone`.
- Live API data on 2026-04-14 showed BTCUSDT trading around **74,198** with a 5-minute average near **74,240**.
- The 24-hour ticker showed **high 76,038**, **low 73,071**, and **last price 74,198**, meaning BTC was already several thousand dollars above the 70k line at research time.
- Recent 1-minute kline samples corresponded to UTC timestamps around **2026-04-14 20:30Z-20:33Z**, which aligns with **16:30-16:33 EDT** and supports the ET/UTC conversion needed for final settlement checking.

## Evidence directly stated by source

From Binance docs:
- “Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time.”
- `GET /api/v3/klines`
- Parameters include `symbol`, `interval`, optional `startTime`, `endTime`, and `timeZone`.
- “If timeZone provided, kline intervals are interpreted in that timezone instead of UTC.”
- “Note that startTime and endTime are always interpreted in UTC, regardless of timeZone.”

From live API pulls:
- `lastPrice`: 74198.00000000
- `highPrice`: 76038.00000000
- `lowPrice`: 73071.21000000
- `avgPrice`: 74240.31144006

## What is uncertain

- The Polymarket rule text points traders to the Binance web chart, while this note also relies on Binance API documentation and live API data. That is highly consistent but still not literally the same front-end rendering path.
- Near-term spot level alone does not settle the Apr 20 noon ET print; a large drawdown remains possible in crypto over six days.
- Binance documentation does not by itself identify upcoming catalysts; it only clarifies mechanics and current buffer vs the strike.

## Why this source may matter

This is the strongest source for verifying the operational resolution mechanics and establishing that the contract is asking about a specific one-minute exchange print, not a broader index or end-of-day level. It also quantifies the current cushion above 70k.

## Possible impact on the question

The live Binance data materially supports a high Yes baseline because BTC is already above the strike by roughly 4k+ and the last 24h range remained above 70k. It also reduces timestamp ambiguity by showing how UTC timestamps line up with ET/EDT handling.

## Reliability notes

High quality for market mechanics and current state because it comes from the same venue named in the contract. Independence versus the Polymarket rules is only moderate since both rely on Binance as the core source, but they answer different questions: one defines the contract, the other verifies how the venue structures the relevant candle data.