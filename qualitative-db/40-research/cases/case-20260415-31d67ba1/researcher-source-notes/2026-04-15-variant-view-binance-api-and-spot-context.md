---
type: source_note
case_key: case-20260415-31d67ba1
dispatch_id: dispatch-case-20260415-31d67ba1-20260415T185542Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-17
question: Will the price of Bitcoin be above $70,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance Spot API docs and live BTCUSDT endpoints
source_type: exchange documentation + live market data
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-31d67ba1/researcher-analyses/2026-04-15/dispatch-case-20260415-31d67ba1-20260415T185542Z/personas/variant-view.md]
tags: [binance, api, klines, settlement-mechanics, timezone, price-context]
---

# Summary

Binance documentation confirms that klines are uniquely identified by open time and that the API supports a `timeZone` parameter for interpreting interval boundaries in a non-UTC timezone, while `startTime` and `endTime` remain UTC. Live Binance endpoints show BTCUSDT around $74.3k-$74.4k on Apr. 15, roughly 6% above the market threshold, which supports the market's Yes bias but also clarifies that the decisive object is a single exchange-specific 1-minute close rather than a generic spot reference.

## Key facts extracted

- Binance `GET /api/v3/klines` provides 1-minute BTCUSDT candles.
- Binance docs state klines are uniquely identified by their open time.
- Binance docs state `timeZone` can shift interval interpretation away from UTC, including values like `-4` for ET during daylight saving time.
- Binance docs state `startTime` and `endTime` are always interpreted in UTC regardless of `timeZone`.
- Live Binance `ticker/price` showed BTCUSDT at approximately 74,356.32.
- Live Binance `avgPrice` showed approximately 74,360.19.
- Live Binance `ticker/24hr` showed last price approximately 74,377.74, 24h high about 74,786.72, and 24h low about 73,514.00.
- Noon ET on Apr. 17, 2026 maps to 16:00 UTC.

## Evidence directly stated by source

- Binance docs explicitly document `GET /api/v3/klines`, its `timeZone` parameter, and that klines are identified by open time.
- Binance docs explicitly say `startTime` and `endTime` remain UTC even if `timeZone` is supplied.
- Live exchange endpoints directly reported current BTCUSDT prices in the mid-74k range on Apr. 15.

## What is uncertain

- Current spot price does not guarantee the Apr. 17 noon ET close remains above 70k.
- The Polymarket rules refer to the Binance trading UI candle, while our verification uses Binance API endpoints and docs rather than the web UI itself.
- Sudden BTC drawdowns over two days are uncommon at this magnitude but still plausible in crypto.

## Why this source may matter

This source is the strongest primary evidence for both settlement mechanics and current exchange-specific spot context. It materially reduces ambiguity about timezone handling and about whether the market is keyed to a broad price narrative or a single exchange-defined minute close.

## Possible impact on the question

It pushes strongly toward Yes because the market only needs BTCUSDT to remain above 70,000 on one specified Binance minute close and the live exchange price is more than $4,300 above that level. The main surviving variant concern is operational/contract interpretation fragility, not a base-case price-level argument.

## Reliability notes

High reliability for exchange mechanics and live spot context. Independence versus the Polymarket source is partial: Polymarket rules cite Binance, and Binance docs/data independently clarify how the referenced instrument is constructed.