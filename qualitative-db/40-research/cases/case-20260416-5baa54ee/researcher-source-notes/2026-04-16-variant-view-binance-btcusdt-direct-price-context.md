---
type: source_note
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: reliability
date_created: 2026-04-16
source_name: Binance BTCUSDT API direct price and kline surfaces
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, direct-source, resolution-context]
---

# Summary

Binance's direct BTCUSDT API surfaces show BTC trading around 75k on 2026-04-16, comfortably above the 70k threshold four days before resolution. This does not settle the market, because the contract resolves on the Binance 1-minute candle close at exactly 12:00 ET on 2026-04-20, but it materially informs the base state and the size of buffer the market is pricing.

## Key facts extracted

- Direct Binance ticker query returned `{"symbol":"BTCUSDT","price":"75045.79000000"}`.
- Direct Binance 1-minute klines query returned recent closes clustered around 75.0k-75.1k.
- Direct Binance 1-day klines for the prior week show closes at approximately 72.96k, 73.04k, 70.74k, 74.42k, 74.13k, 74.81k, and partial current day near 75.04k.
- Recent daily lows in the returned 7-day window stayed above 70k, with the lowest printed low in that sample about 70,505.88.

## Evidence directly stated by source

- Binance currently prices BTCUSDT at about 75k.
- Recent direct exchange candles indicate BTC has recently traded several thousand dollars above 70k.

## What is uncertain

- The contract depends on one specific future minute close: the Binance BTCUSDT 12:00 ET candle on 2026-04-20.
- A current cushion above 70k can still disappear if BTC sells off materially before or into the resolution minute.
- API access verifies Binance as a live direct source, but not the exact future settlement value.

## Why this source may matter

This is the governing exchange family named by contract. Even though Polymarket references the Binance chart UI, Binance API outputs are direct exchange data and useful for verifying the exchange, pair, price scale, and current state of the market.

## Possible impact on the question

The direct Binance data supports the market's very high implied probability by showing BTC already trading roughly 7% above the threshold with only four calendar days left. The main remaining path to a No outcome is a sharp selloff or exchange-specific dislocation before the exact noon ET minute close.

## Reliability notes

- High credibility for current BTCUSDT price context because Binance is the named resolution venue.
- Not a perfect settlement surface substitute, since the contract explicitly cites the Binance chart UI with 1m candles selected.
- Good for direct context and additional verification; still should be paired with the contract text and explicit timezone mapping.