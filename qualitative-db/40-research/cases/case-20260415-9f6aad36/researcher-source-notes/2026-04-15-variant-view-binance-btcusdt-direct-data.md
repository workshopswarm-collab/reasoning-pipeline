---
type: source_note
case_key: case-20260415-9f6aad36
dispatch_id: dispatch-case-20260415-9f6aad36-20260415T082436Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT direct market data endpoints
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [variant-view finding, variant-view assumption note]
tags: [binance, source-of-truth-adjacent, direct-market-data, btcusdt]
---

# Summary

Direct Binance API data shows BTC/USDT trading materially above the market threshold at assignment time, but only by a modest cushion relative to crypto day-scale volatility. This supports a Yes lean while preserving a credible variant risk that a sub-$72k move by the exact noon ET minute remains plausible.

## Key facts extracted

- Binance ticker price at research time: 73,970.88 USDT.
- Binance 24h stats showed:
  - open: 74,517.01
  - high: 76,038.00
  - low: 73,514.00
  - last: 73,970.88
  - 24h change: -0.733%
- Recent 1h klines over the last 24 hours showed BTC trading in a range roughly 73.5k to 76.0k, with several hourly closes in the low-to-mid 74k area and some downward drift into the current reading.
- The current spot level is about 1,970.88 above the 72,000 threshold, or about 2.74% above the cutoff.
- The market resolves on the Binance BTC/USDT 1-minute candle close at 12:00 ET on April 16, not on a daily close and not on another venue.

## Evidence directly stated by source

- Binance direct endpoints report the latest BTCUSDT last price and 24h range.
- Binance klines provide recent hourly path information showing realized short-horizon volatility sufficient to move price by several hundred dollars within hours.

## What is uncertain

- The authoritative settlement surface is the Binance front-end candle display for the exact 12:00 ET 1-minute candle on April 16; the API checks here are direct Binance data but not the exact final settlement observation yet.
- Crypto can move materially within the remaining window; current price does not settle the contract.
- API and front-end values should normally align, but the contract points to the chart surface and exact minute close.

## Why this source may matter

This is the closest direct source to the governing resolution source before settlement. It establishes both the current buffer above 72k and the plausible volatility that could erase that buffer before the decisive minute.

## Possible impact on the question

This source supports a base Yes view because BTC is currently well above 72k on Binance, but it also undermines overconfidence because the cushion is not large relative to typical crypto intraday movement.

## Reliability notes

- High credibility for current Binance BTC/USDT pricing because Binance is the named resolution source.
- Slight source-of-truth caveat: the contract settles from the Binance candle chart close for the exact ET noon minute, not from a generic ticker endpoint.
- Useful for pre-resolution inference, not direct settlement by itself.
