---
type: source_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9a9c8ea3 | market-implied
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance public API (ticker price, 1m klines, server time)
source_type: exchange-api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15T19:22:03.965Z
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-9a9c8ea3/researcher-analyses/2026-04-15/dispatch-case-20260415-9a9c8ea3-20260415T192028Z/personas/market-implied.md]
tags: [binance, btcusdt, market-price, source-note]
---

# Summary

Direct Binance API checks show BTC/USDT trading around 74.6k on 2026-04-15 15:22 ET, comfortably above the 72k threshold for the 2026-04-16 noon ET settlement candle. Recent 1-minute klines confirm the instrument, price precision, and that Binance exposes the needed close-price surface.

## Key facts extracted

- `ticker/price` returned BTCUSDT = `74626.32000000`.
- `time` returned Binance server time `1776280923965`, which converts to 2026-04-15 19:22:03.965 UTC / 2026-04-15 15:22:03.965 ET.
- Recent `klines?interval=1m&limit=5` values showed closes between roughly `74613.33` and `74694.51`.
- The kline schema exposes a distinct close price for each 1-minute candle, matching the contract mechanic.

## Evidence directly stated by source

- Binance publicly serves BTC/USDT spot price data via API.
- Binance publicly serves 1-minute candle close data via API.
- At capture time, BTC/USDT was more than 2,600 points above 72,000.

## What is uncertain

- The API output is not itself the exact web UI candle used by Polymarket rules, though it is a direct Binance data surface and strongly consistent with the same underlying market.
- One full day remains before the noon ET settlement candle, so substantial price movement is still possible.

## Why this source may matter

This is the most direct authoritative source checked for the underlying market condition because the contract explicitly keys off Binance BTC/USDT 1-minute candle close values.

## Possible impact on the question

The direct Binance price evidence strongly supports why a 95.5% market-implied probability can be efficient: BTC is already well above 72k, so the contract requires a large adverse move before the specific noon ET settlement minute.

## Reliability notes

- High credibility as a first-party exchange API for the exact venue named in the contract.
- Small operational caveat: the contract references the Binance web candle surface, so UI/API parity is assumed but not absolutely proven from this note alone.
