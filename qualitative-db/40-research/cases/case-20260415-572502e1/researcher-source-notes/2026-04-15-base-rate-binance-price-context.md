---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-16 close above 72000?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API BTCUSDT spot data
source_type: exchange_primary_data
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, spot, klines, primary-data]
---

# Summary

This source provides direct primary data from Binance. At capture time on 2026-04-15 around 12:47 UTC, BTC/USDT spot was trading around 74.3k, comfortably above the 72,000 line. Recent 1-minute closes in the public API were also around 74.33k-74.35k.

## Key facts extracted

- Binance server time returned normally, indicating live API availability during the check.
- Binance ticker price for BTCUSDT was about 74,353.07 at capture.
- Recent 1-minute kline closes from Binance were around 74,337.67, 74,333.96, 74,331.98, 74,353.07, and 74,348.52.
- A targeted request for the future resolving minute on 2026-04-16 16:00 UTC returned no data yet, which is expected and helps verify the time conversion logic rather than accidentally reading the wrong day.

## Evidence directly stated by source

- Binance `/api/v3/time` returned a live server timestamp.
- Binance `/api/v3/ticker/price?symbol=BTCUSDT` returned spot price about 74.35k.
- Binance `/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5` returned current-minute candles above 74.3k.

## What is uncertain

- This is a spot snapshot roughly one day before resolution, not the resolving candle itself.
- Short-horizon crypto volatility can easily move BTC by several percent inside 24 hours.
- API accessibility today does not guarantee zero exchange or data-display issues at settlement time.

## Why this source may matter

It is the closest direct contextual evidence to the governing source of truth. A base-rate view should start from the actual distance between current spot and the line.

## Possible impact on the question

With BTC about 2.3k above the line one day out, the default outside view favors Yes unless there is a substantial downside move before noon ET tomorrow.

## Reliability notes

High-quality primary exchange data and meaningfully independent from the Polymarket contract page. It is still only a current snapshot, so it should be interpreted as contextual evidence for distance-to-threshold rather than direct settlement evidence.