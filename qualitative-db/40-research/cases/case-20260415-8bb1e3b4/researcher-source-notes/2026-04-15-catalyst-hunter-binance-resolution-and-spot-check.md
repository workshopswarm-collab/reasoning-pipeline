---
type: source_note
case_key: case-20260415-8bb1e3b4
dispatch_id: dispatch-case-20260415-8bb1e3b4-20260415T150551Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle closing at 12:00 ET on 2026-04-20 close above 70000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot market data endpoints + live BTCUSDT spot check
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8bb1e3b4/researcher-analyses/2026-04-15/dispatch-case-20260415-8bb1e3b4-20260415T150551Z/personas/catalyst-hunter.md]
tags: [source-note, primary-source, resolution-mechanics, binance]
---

# Summary

This source note captures the governing resolution mechanics and a live spot-price verification from Binance-referenced data. It confirms that klines are identified by open time, that Binance supports 1-minute BTCUSDT klines, and that timezone handling matters when mapping the contract's "12:00 ET" candle to UTC.

## Key facts extracted

- Binance spot API exposes `GET /api/v3/klines` for BTCUSDT 1-minute candles.
- The docs state klines are uniquely identified by their open time.
- Binance supports a `timeZone` parameter for interpreting kline intervals, but `startTime` and `endTime` are always interpreted in UTC.
- The market resolves off the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-20.
- 2026-04-20 12:00 ET corresponds to 2026-04-20 16:00 UTC.
- A live spot/API check on 2026-04-15 showed BTCUSDT around 74,000, materially above the 70,000 strike.

## Evidence directly stated by source

- Binance docs: 1-minute klines are available and are uniquely identified by open time.
- Binance docs: if `timeZone` is provided, intervals are interpreted in that timezone, but explicit query timestamps remain UTC.
- Live Binance ticker and recent kline output showed BTCUSDT trading roughly 5-6% above 70,000 on 2026-04-15.

## What is uncertain

- The Polymarket rule text says the "12:00 in the ET timezone (noon)" candle and final "Close" price. Binance documentation clarifies API mechanics but does not itself define Polymarket's intended contract interpretation for any edge-case UI/chart mapping.
- A 1-minute close four-plus days ahead remains path-dependent and can move materially with macro or crypto-specific shocks.

## Why this source may matter

This is the governing primary source family for settlement. It matters because the market is not about generic BTC spot price; it is specifically about Binance BTC/USDT's 1-minute candle close at a timezone-specific minute.

## Possible impact on the question

The source strongly supports a bullish base case because current Binance BTCUSDT is already well above 70,000, but it also narrows the real question: whether BTC stays above 70,000 precisely into the 2026-04-20 12:00 ET / 16:00 UTC minute close on Binance.

## Reliability notes

- Primary for resolution mechanics and spot reference.
- High credibility on candle structure and timing.
- Not sufficient alone for forecasting persistence through April 20; it needs contextual catalyst evidence.