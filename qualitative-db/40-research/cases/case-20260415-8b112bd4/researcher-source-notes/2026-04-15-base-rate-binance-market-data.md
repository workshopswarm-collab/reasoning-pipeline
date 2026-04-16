---
type: source_note
case_key: case-20260415-8b112bd4
dispatch_id: dispatch-case-20260415-8b112bd4-20260415T153012Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: spot-price
entity: btc
topic: bitcoin-above-70k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance API BTCUSDT ticker and recent klines
source_type: exchange market data / primary contextual
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [base-rate finding, evidence map]
tags: [binance, btcusdt, spot-price, primary-context]
---

# Summary

Binance spot market data is the most important contextual source for this case because the contract resolves off a Binance BTC/USDT one-minute close at 12:00 ET on 2026-04-16.

## Key facts extracted

- Binance API ticker returned BTCUSDT around 73.6k to 74.1k during this research pass on 2026-04-15.
- Recent daily candles from Binance showed closes around 71.8k, 73.0k, 73.0k, 70.7k, 74.4k, 74.1k, and roughly 73.6k intraday on 2026-04-15.
- Recent hourly candles for the last 24 hours showed BTC mostly trading in a roughly 73.5k to 74.8k band, with no print near 70k during that window.
- The 2026-04-15 12:00 UTC-anchored hourly close from Binance was 74273.77; later hours remained above 73.5k during this pass.

## Evidence directly stated by source

- Current ticker price: BTCUSDT near 73610 to 74087 depending on exact query time during the run.
- Daily candle data showed recent lows/highs such as 70505.88 low on one day and highs up to 76038.00 on another, indicating realized volatility still exists.
- Despite that volatility, the market has recently spent most of its time materially above 70000.

## What is uncertain

- This source does not directly settle the contract because settlement depends specifically on the one-minute candle labeled 12:00 ET on 2026-04-16.
- Intraday crypto volatility means a sub-70k move by tomorrow noon remains possible even if current price is well above the threshold.
- API point-in-time reads can differ slightly from the exchange UI or the exact eventual candle close.

## Why this source may matter

This is the closest available direct source to the eventual settlement source. It provides the current level, recent realized volatility, and distance from the threshold.

## Possible impact on the question

Current Binance pricing materially above 70000 pushes the base rate toward Yes, but recent realized daily swings large enough to cross several thousand dollars argue against treating Yes as virtually certain.

## Reliability notes

Primary contextual source. High credibility for current exchange pricing, though the exact settlement still depends on the designated one-minute candle and exchange display at the relevant time.