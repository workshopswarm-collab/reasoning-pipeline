---
type: source_note
case_key: case-20260415-bebdf03e
dispatch_id: dispatch-case-20260415-bebdf03e-20260415T221944Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-21
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-21 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API docs + live BTCUSDT endpoints
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-bebdf03e/researcher-analyses/2026-04-15/dispatch-case-20260415-bebdf03e-20260415T221944Z/personas/risk-manager.md]
tags: [source-note, primary-source, binance, resolution]
---

# Summary

This source note captures the governing settlement mechanics and current spot context from Binance itself. The API docs confirm that 1-minute klines expose an explicit close price field, and live BTCUSDT endpoints on 2026-04-15 show BTC trading around 75,012, meaning the market is currently about 3,000 above the 72,000 threshold with roughly 5.5 days remaining.

## Key facts extracted

- Binance `/api/v3/klines` provides 1-minute candlestick data for a symbol and includes a distinct close price field in the response array.
- Binance docs note `timeZone` can be specified for kline interval interpretation, but `startTime` and `endTime` are always interpreted in UTC.
- Live Binance endpoint `/api/v3/ticker/price?symbol=BTCUSDT` returned `75011.98000000` on 2026-04-15.
- Live Binance `/api/v3/ticker/24hr?symbol=BTCUSDT` returned last price `75011.98000000`, 24h high `75281.00000000`, low `73514.00000000`, and +1.30% 24h change.
- Recent 1-minute klines sampled during the run were all near 74,915-75,012, reinforcing that BTC is comfortably above 72,000 at research time.

## Evidence directly stated by source

- Binance docs explicitly describe kline/candlestick bars and show response structure including close price.
- Binance live endpoints directly state current BTCUSDT price and 24h trading range.

## What is uncertain

- The contract resolves on the Binance web chart with 1m candles at 12:00 ET on April 21, not on today's API snapshot.
- The docs establish mechanics, but they do not guarantee there will be no exchange display/API discrepancy or operational issue at settlement time.
- Current spot level alone does not settle a five-day-forward noon snapshot market.

## Why this source may matter

This is the highest-quality source because the market explicitly settles from Binance BTC/USDT 1-minute candle close data. It also anchors the current distance-to-threshold and highlights the operational dependence on a single exchange/source.

## Possible impact on the question

The source supports a bullish baseline because BTC is currently above the threshold by roughly 4%. But it also sharpens the main risk framing: a single noon-minute Binance close decides the contract, so late volatility or exchange-specific microstructure matters more than broad cross-exchange averages.

## Reliability notes

High reliability for settlement mechanics and current Binance price context. Independence is limited because the same source both defines and partly informs the contract; it should be paired with an external contextual source for broader market conditions.