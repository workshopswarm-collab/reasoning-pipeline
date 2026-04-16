---
type: source_note
case_key: case-20260415-2cba3460
dispatch_id: dispatch-case-20260415-2cba3460-20260415T115730Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot BTCUSDT public market data API
source_type: exchange market data / resolution-adjacent primary source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2cba3460/researcher-analyses/2026-04-15/dispatch-case-20260415-2cba3460-20260415T115730Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, primary-source, resolution-adjacent, catalyst]
---

# Summary

Binance public BTC/USDT data on 2026-04-15 showed spot trading around 74.1k, comfortably above the 72k threshold for the April 16 noon-ET resolution candle. The same API surface also showed a 24-hour range of roughly 73.5k to 76.0k, which matters because the threshold is not far from the lower bound of recent realized trading, so the main catalyst question is whether a fresh downside move of a few percent occurs before the specific settlement minute.

## Key facts extracted

- `ticker/price` returned BTCUSDT around 74,145-74,155 on 2026-04-15 during this run.
- `ticker/24hr` returned:
  - lastPrice: 74,145.26
  - highPrice: 76,038.00
  - lowPrice: 73,514.00
  - priceChangePercent: -0.242%
- `klines?interval=1m&limit=5` returned recent 1-minute candles around 74.15k-74.20k.
- The 24-hour low remained above 72,000 by roughly 1,514 points.

## Evidence directly stated by source

- Binance currently prices BTC/USDT above 72,000.
- Binance exposes 1-minute candle close values directly through the kline endpoint, consistent with the market's stated settlement mechanics.
- Recent intraday realized range is wide enough that a several-percent move before tomorrow's noon ET print is possible, but not presently indicated by current spot.

## What is uncertain

- This API check is not itself the exact settlement candle and cannot settle the market early.
- Public API availability does not guarantee the website candle display will be identical in every edge case, though both are Binance-controlled surfaces.
- Crypto can move materially overnight on macro headlines, liquidation cascades, or exchange-specific operational events.

## Why this source may matter

This is the closest direct source to the governing source of truth because the market resolves from Binance BTC/USDT 1-minute candle close prices. It anchors the current level versus the threshold and makes the timing question concrete.

## Possible impact on the question

With spot around 74.1k and recent 24h low still above 72k, the market starts from a favorable buffer for a Yes outcome. The most relevant near-term catalysts are therefore downside catalysts large enough to erase roughly 2.9% before the specific noon-ET minute on April 16.

## Reliability notes

- High reliability for current exchange pricing and recent candle data.
- Still resolution-adjacent rather than the final settlement observation because the contract names the Binance trading interface candle at the exact target minute.