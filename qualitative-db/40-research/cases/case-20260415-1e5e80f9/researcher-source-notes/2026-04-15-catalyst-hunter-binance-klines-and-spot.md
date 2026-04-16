---
type: source_note
case_key: case-20260415-1e5e80f9
dispatch_id: dispatch-case-20260415-1e5e80f9-20260415T080017Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: binance-btcusdt-price-path-and-resolution-mechanics
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API market data endpoints and live BTCUSDT outputs
source_type: primary_exchange_data_and_api_docs
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, klines, resolution-source, price-path]
---

# Summary

Binance is both the governing source of truth for settlement and a usable direct data source for checking the relevant BTC/USDT one-minute candle mechanics. On 2026-04-15 around 04:04 ET, the live Binance ticker was about 73,728.64 and the most recent 1-minute kline closes from the Binance API remained consistently above 72,000 across the last 1,000 minutes returned.

## Key facts extracted

- Binance Spot API documentation states `GET /api/v3/klines` provides kline/candlestick bars for a symbol and supports `interval=1m` plus a `timeZone` parameter.
- Binance docs state that if `timeZone` is provided, kline intervals are interpreted in that timezone, while `startTime` and `endTime` remain interpreted in UTC.
- The Polymarket contract resolves from the Binance BTC/USDT 1-minute candle at 12:00 ET on the named date, using the final close price.
- Direct API call to `https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT` returned `73,728.64` at the time of checking.
- Direct API call to `GET /api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000&timeZone=-4:00` returned 1,000 recent one-minute candles.
- Across those 1,000 returned minute closes, the lowest close observed was `73,566.00`, the highest was `75,662.69`, and 100% of returned closes were above `72,000`.
- Over the last 16 hours in that sample, the series fell from about `75,458.63` to about `73,755.51`, so the market is comfortably above 72,000 but has been drifting lower.

## Evidence directly stated by source

- Binance API docs directly define the kline endpoint and timezone semantics.
- The live ticker endpoint directly states the current BTCUSDT spot price.
- The returned kline data directly states the recent minute-by-minute close prices.

## What is uncertain

- This check does not directly observe the future 2026-04-16 12:00 ET candle, only the current buffer above 72,000 and recent path behavior.
- Binance website chart UI could theoretically display the same underlying data differently from the API, though the contract text points to the Binance trading page and not explicitly to the API.
- Intraday crypto volatility could still erase a 2%+ cushion before noon ET tomorrow.

## Why this source may matter

This is the most authoritative available source because the market explicitly settles on Binance BTC/USDT one-minute candle data. It also lets us verify the timezone-sensitive contract mechanics rather than relying on generic BTC price aggregators.

## Possible impact on the question

The source supports a strong base case for Yes because BTCUSDT is already well above 72,000 and recent minute closes never approached the threshold in the checked sample. The main residual risk is not contract ambiguity but a material downside move before the specified noon ET candle.

## Reliability notes

High reliability for settlement mechanics and current price state. Moderate caveat: the Polymarket contract points to the Binance trading interface as the resolution surface, so API-based verification is highly relevant but not literally identical to the UI surface named in the rules.