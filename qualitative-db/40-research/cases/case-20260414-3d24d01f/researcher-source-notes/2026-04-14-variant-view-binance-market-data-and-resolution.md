---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET one-minute candle close above 70000 on 2026-04-19?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance Spot API docs and live BTCUSDT endpoints
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/variant-view.md]
tags: [binance, btcusdt, resolution-source, source-note]
---

# Summary

This source note captures the governing resolution mechanics and a live spot check of Binance BTC/USDT pricing relevant to the April 19 noon ET market.

## Key facts extracted

- Binance documents `GET /api/v3/klines` for 1-minute candlestick data and states klines are uniquely identified by open time.
- The kline response explicitly includes Open, High, Low, and `Close` price fields.
- Binance docs note `timeZone` can be supplied for interval interpretation, while `startTime` and `endTime` are interpreted in UTC.
- Live Binance spot endpoints on 2026-04-14 showed BTCUSDT around 74.3k, materially above the market strike of 70k.
- Recent 24h stats showed a low near 72.3k and high near 76.0k, so the market is not merely barely above the threshold at assignment time.

## Evidence directly stated by source

- Binance market-data docs define the kline endpoint and identify the `Close` field in the kline payload.
- Live Binance `ticker/price`, `avgPrice`, `ticker/24hr`, and recent `klines` endpoints all showed BTCUSDT above 70000 on 2026-04-14.

## What is uncertain

- The docs support how the candle is represented, but Polymarket resolves from the Binance front-end chart display at the specified timestamp, not necessarily from an API pull generated later.
- There remains path risk over the next five days: BTC can trade below 70k by the exact April 19 12:00 ET minute even if it is comfortably above today.
- The docs themselves do not prove the exact ET mapping Polymarket will operationally use on settlement day beyond the contract wording.

## Why this source may matter

This is the primary source family because the contract explicitly resolves to Binance BTC/USDT 1-minute candle close data. It also provides a direct live baseline showing the threshold is currently well in the money.

## Possible impact on the question

The source materially supports a high Yes probability because the contract source of truth is clear enough to audit and current BTCUSDT price is several thousand dollars above the strike. The main residual risk is not source confusion but a real price move below 70k at the specific resolution minute.

## Reliability notes

- Primary-source quality is high for contract mechanics and current quoted market data.
- Settlement still contains some operational ambiguity because the contract references the Binance UI chart selection rather than a frozen API query recipe.
- Independence is limited within the Binance source family, so a second contextual source is still useful for market-state cross-checking.