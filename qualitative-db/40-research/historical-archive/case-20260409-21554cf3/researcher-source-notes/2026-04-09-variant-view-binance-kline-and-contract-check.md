---
type: source_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
analysis_date: 2026-04-09
persona: variant-view
domain: crypto
subdomain: market-structure
entity: ethereum
topic: case-20260409-21554cf3 | variant-view
question: Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-09 close above 2100?
driver: reliability
date_created: 2026-04-09
source_name: Binance spot API klines and Binance market contract text
source_type: primary_and_resolution_context
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/variant-view.md]
tags: [binance, klines, resolution-mechanics, timezone-check]
---

# Summary

This source note checks the governing resolution mechanics and a direct Binance market-data surface. The Polymarket contract says resolution is based on the Binance ETH/USDT 1-minute candle at 12:00 ET on 2026-04-09, specifically the candle close. Binance developer docs confirm `/api/v3/klines` and `/api/v3/uiKlines` are the candlestick endpoints and that `timeZone` can be specified, while start and end timestamps remain interpreted in UTC.

## Key facts extracted

- Polymarket contract text states the market resolves to Yes if the Binance ETH/USDT 12:00 ET 1-minute candle has a final close above 2100.
- Binance API docs state klines are uniquely identified by open time and support `interval=1m`.
- Noon ET on 2026-04-09 is 16:00 UTC because New York is on EDT (UTC-4).
- A direct live Binance API pull around 03:34 ET returned recent ETHUSDT 1-minute candles with closes around 2181 to 2184, already well above 2100.
- Querying Binance for the exact future 16:00 UTC candle before it exists returned an empty array, which is expected and confirms the timestamp mapping rather than contradicting it.

## Evidence directly stated by source

- Binance docs: `GET /api/v3/klines` returns kline/candlestick bars for a symbol and `timeZone` changes interval interpretation while `startTime` and `endTime` are still in UTC.
- Polymarket rules: the resolution source is Binance ETH/USDT with 1m candles selected, and price precision is determined by Binance source decimals.

## What is uncertain

- The final noon ET close is still several hours away, so price path risk remains.
- The contract references the Binance site UI specifically, while this note also uses Binance API documentation and API endpoints as a verification surface. That is useful for mechanics verification but not a perfect substitute for the final site-rendered candle if any discrepancy appears.

## Why this source may matter

It defines both the governing source of truth and the exact temporal/candle mechanics. For this case, misunderstanding the noon-ET mapping or using the wrong exchange/pair would be a major error.

## Possible impact on the question

This supports a high-Yes baseline because ETH is already materially above 2100 on the same governing exchange and pair, and because the exact resolution mechanics appear straightforward rather than ambiguous.

## Reliability notes

- Primary reliability is high for the Binance docs and live Binance market-data endpoint.
- Independence is limited because both the docs and live endpoint come from Binance, but that is acceptable here because Binance is also the governing source of truth.
- Remaining risk is not source reliability but market movement between the current time and the noon-ET resolution candle.
