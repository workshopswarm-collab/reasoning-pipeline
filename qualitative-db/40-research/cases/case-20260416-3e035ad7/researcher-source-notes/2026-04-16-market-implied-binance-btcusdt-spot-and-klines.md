---
type: source_note
case_key: case-20260416-3e035ad7
dispatch_id: dispatch-case-20260416-3e035ad7-20260416T043505Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 70000?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance public market data endpoints (ticker price, klines, server time, exchange info)
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-3e035ad7/researcher-analyses/2026-04-16/dispatch-case-20260416-3e035ad7-20260416T043505Z/personas/market-implied.md]
tags: [binance, btcusdt, candle, resolution-source, source-note]
---

# Summary

Binance public data confirms BTC/USDT was trading around 74,975.57 at approximately 2026-04-16 04:36 UTC, well above the 70,000 strike relevant to the April 17 noon ET market. The same source family also confirms Binance timestamps in UTC and provides one-minute kline data needed to understand the eventual settlement mechanic.

## Key facts extracted

- `ticker/price` returned BTCUSDT price `74975.57000000`.
- Recent one-minute klines ended at 2026-04-16 04:32, 04:33, 04:34, 04:35, and 04:36 UTC.
- The most recent sampled one-minute candle closed at `74975.57000000`.
- `exchangeInfo` reports Binance exchange timezone as `UTC` and BTCUSDT status as `TRADING`.
- BTCUSDT price filter tick size is `0.01000000`, which indicates cent-level precision for the quoted market data available through Binance.
- `time` endpoint returned serverTime `1776314217376`, consistent with the sampled kline timestamps.

## Evidence directly stated by source

- Binance currently quotes BTCUSDT near 74.98k.
- Binance exposes one-minute klines for BTCUSDT and timestamps them in UTC.
- BTCUSDT spot trading is active.

## What is uncertain

- This source does not directly tell us where BTC/USDT will trade at 2026-04-17 12:00 ET.
- The Polymarket rule text points users to the Binance trading UI candle display rather than directly to the API; the API is therefore best treated as a strong contextual/verification surface for the same exchange rather than the formal settlement page itself.
- Intraday BTC volatility could still produce a drop below 70,000 by the settlement minute.

## Why this source may matter

This is the closest direct source to the governing exchange price series. It verifies that the underlying reference market is live, that current spot is materially above the strike, that one-minute close data exists on Binance, and that UTC/ET timing conversion needs to be handled explicitly for the noon ET settlement candle.

## Possible impact on the question

Because spot is roughly 7.1% above the strike about 31.4 hours before settlement, the market's very high implied probability for "above 70,000" looks directionally sensible unless a large downward move occurs before the specific noon ET minute on April 17.

## Reliability notes

High reliability for current spot and kline mechanics because the data comes directly from Binance public endpoints. Slight source-of-truth caveat remains because Polymarket names the Binance UI candle as the formal resolution surface, so the API should be treated as a close operational proxy and verification aid rather than the sole formal settlement artifact.
