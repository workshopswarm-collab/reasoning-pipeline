---
type: source_note
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 68000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API and Polymarket market rules
source_type: primary
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [source-note, primary-source, binance, polymarket, btc]
---

# Summary

This source note captures the governing resolution mechanics plus current spot context from Binance, the contract's stated source of truth.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, using the candle's final Close price.
- The market is specifically about Binance BTC/USDT, not other exchanges or pairs.
- Binance spot API fetched during this run showed BTCUSDT at 74,613.01.
- Recent 1-minute Binance klines fetched during this run were tightly clustered around 74.6k, far above the 68k threshold.

## Evidence directly stated by source

- Binance ticker endpoint returned `{ "symbol": "BTCUSDT", "price": "74613.01000000" }`.
- Binance 1-minute kline endpoint returned several consecutive minute closes in the 74,627-74,677 range.
- Polymarket rules explicitly say the relevant datapoint is the Binance 1-minute candle for 12:00 ET on the target date.

## What is uncertain

- Current price does not settle the contract; the relevant close is five days later at a specific minute.
- The Binance API endpoints used here are not the exact visual interface named in the rules, though they reference the same BTC/USDT market data family.
- Exchange-specific anomalies, outages, or temporary dislocations near the resolution minute could still matter even if broader BTC pricing stays strong.

## Why this source may matter

It anchors both the contract interpretation and the live distance from the strike. For a date-specific crypto threshold market, using the named source-of-truth venue matters more than generic BTC pricing.

## Possible impact on the question

Because Binance spot was about 9.7% above the 68k threshold during this run, the market's high Yes probability has a clear mechanical basis. The main variant angle is not that BTC is currently below threshold, but that the market may still be underpricing path-dependent downside or resolution-minute venue risk over the next five days.

## Reliability notes

- High reliability for venue-specific current spot context and contract-source interpretation.
- Limited as a forecasting source on its own; it tells us current level and mechanics, not whether the level will hold through the exact resolution minute.