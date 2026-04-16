---
type: source_note
case_key: case-20260415-d9ca8ddf
dispatch_id: dispatch-case-20260415-d9ca8ddf-20260415T195847Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET Apr 17 2026 1-minute candle close exceed 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API plus CoinGecko spot cross-check
source_type: exchange API plus market-data aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: very-high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, coingecko, price-context, verification]
---

# Summary

Direct Binance market data and an independent CoinGecko spot cross-check both showed BTC comfortably above 72,000 on Apr 15, two days before resolution. Binance spot was near 74.9k-75.0k during the verification window, leaving a cushion of roughly 2.9k above the contract threshold.

## Key facts extracted

- Binance BTCUSDT last price during verification was about 74,927 to 74,929.
- Binance 24h stats showed high about 75,281 and low about 73,514.
- Binance recent 1-minute candles remained above 74,900 during the capture window.
- Over the last 72 hourly candles, observed high was about 76,038 and low about 70,505.88.
- CoinGecko independently showed BTC around 75,056 USD, broadly consistent with Binance.
- The relevant settlement time of Apr 17 2026 12:00 ET maps to 2026-04-17 16:00:00 UTC.

## Evidence directly stated by source

- Binance ticker endpoint returned BTCUSDT price 74927.42 and later 74928.79 during local checks.
- Binance 24h ticker returned highPrice 75281.00 and lowPrice 73514.00.
- Binance kline endpoint showed recent candle closes all well above 72,000.
- CoinGecko simple price endpoint returned bitcoin usd 75056.

## What is uncertain

- These are snapshots before the resolution window, not the final determining candle.
- BTC is volatile enough that a 2-4% move by Apr 17 noon ET is plausible.
- CoinGecko is contextual confirmation, not the settlement source.

## Why this source may matter

This is the strongest direct evidence on current distance from threshold and whether the market's high Yes probability is grounded in real current price margin rather than stale narrative.

## Possible impact on the question

Current spot context supports Yes, but the variant-view angle is that a two-day horizon plus one-minute-candle settlement means intraday downside volatility, exchange-specific deviations, or a broad crypto risk-off move still matter more than the raw 93% price may imply.

## Reliability notes

Binance is the actual settlement venue and therefore the most relevant primary source. CoinGecko adds an independent contextual cross-check that the Binance reading is not obviously anomalous.