---
type: source_note
case_key: case-20260415-7b143efd
dispatch_id: dispatch-case-20260415-7b143efd-20260415T132144Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-7b143efd | base-rate
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot API market data docs + live BTCUSDT endpoints
source_type: primary_and_contextual_exchange_source
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7b143efd/researcher-analyses/2026-04-15/dispatch-case-20260415-7b143efd-20260415T132144Z/personas/base-rate.md]
tags: [binance, btcusdt, market-rules, resolution-mechanics]
---

# Summary

Binance documentation confirms that BTCUSDT kline/candlestick data expose 1-minute bars with a defined close price and support timezone interpretation, while live Binance BTCUSDT price endpoints show spot BTC trading materially above $70,000 on 2026-04-15.

## Key facts extracted

- Binance spot API includes `GET /api/v3/klines` for kline/candlestick data.
- Klines are available at `1m` interval and return open, high, low, close, volume, and close time.
- Binance docs state `timeZone` can be specified for kline interpretation, while `startTime` and `endTime` remain UTC.
- Live Binance endpoints on 2026-04-15 showed BTCUSDT around $74.3k:
  - `ticker/price`: 74273.07
  - `avgPrice`: 74295.49
- Recent daily BTCUSDT closes from Binance for Apr 13-15 were approximately 74.4k, 74.1k, and 74.3k after trading above 70k for multiple recent sessions.

## Evidence directly stated by source

- Binance docs directly describe the kline endpoint and its returned close-price field.
- Live Binance API endpoints directly returned current BTCUSDT prices above 70,000 at the time checked.

## What is uncertain

- Polymarket specifies the Binance website candle at 12:00 ET on Apr 20, not the REST API endpoint directly; the API is best treated as a strong contextual/verification surface rather than the exact formal settlement surface.
- A spot price materially above 70k on Apr 15 does not itself settle the Apr 20 noon ET question.

## Why this source may matter

This source is the closest direct source-of-truth family because the market resolves from Binance BTCUSDT 1-minute candle close data. It also gives current price context showing the threshold is already in-the-money by roughly 6% on the analysis date.

## Possible impact on the question

This supports a high prior that BTC can remain above 70k by Apr 20 noon ET absent a sharp downside move. It also reduces contract-mechanics ambiguity by confirming the relevant exchange/pair/candle structure.

## Reliability notes

High relevance and high credibility for mechanics and current price context because Binance is the named resolution source family. Slight residual ambiguity remains because the formal rule names the Binance website candle display rather than the API endpoint explicitly.