---
type: source_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity:
topic: ethereum-above-2100-on-april-10
question: Will the price of Ethereum be above $2,100 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance ETHUSDT API resolution mechanics check
source_type: primary_exchange_api
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: risk-manager
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/risk-manager.md]
tags: [binance, resolution-source, kline, timezone-check]
---

# Summary

This source note captures the direct verification pass on Binance surfaces relevant to resolution mechanics for the April 10 ETH > 2100 market.

## Key facts extracted

- `GET /api/v3/exchangeInfo?symbol=ETHUSDT` returned `"timezone":"UTC"` and current `serverTime`, indicating Binance API timestamps are expressed on a UTC basis rather than ET.
- `GET /api/v3/time` returned server time `1775768577232`, which converts to 2026-04-09T20:22:57.232Z / 2026-04-09T16:22:57.232-04:00, matching the expected ET-to-UTC offset of 4 hours on April 9-10, 2026 because U.S. daylight saving time is active.
- `GET /api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5` returned 1-minute candles as arrays with open time, OHLC, volume, and close time.
- Sample rows show the candle labeled by open time, with close time equal to open time + 59.999 seconds. Example: open time `1775768520000` = 2026-04-09T20:22:00Z and close time `1775768579999` = 2026-04-09T20:22:59.999Z.
- Under the market wording, ET noon on April 10 corresponds to 16:00 UTC on April 10. On Binance API conventions, that points to the 1-minute candle whose open time is 2026-04-10T16:00:00Z and whose final close is set at the end of that minute.

## Evidence directly stated by source

- Binance exchange info explicitly states `timezone: UTC`.
- Binance kline payload directly exposes open time, close time, and final close price fields for each 1-minute candle.

## What is uncertain

- The Polymarket rule references the Binance trading UI with `1m` and `Candles` selected, rather than the public API docs directly. The API and UI usually align, but the exact visual labeling convention in the UI was not independently screenshotted here.
- The rule says the Binance 1 minute candle for `12:00 in the ET timezone (noon)`. This almost certainly maps to the candle beginning at 12:00:00 ET / 16:00:00 UTC, but a reviewer should note the operational dependence on Binance’s chart labeling convention.

## Why this source may matter

This is the governing source-of-truth family for settlement. It directly answers the case-specific checks about UTC offset vs Binance server time and the candle close definition.

## Possible impact on the question

The market is mostly a pure price-level question, but timing mechanics matter because a one-minute labeling misunderstanding could flip resolution if price is near the threshold. The verification reduces that timing-risk ambiguity but does not eliminate UI-labeling risk entirely.

## Reliability notes

High reliability for raw exchange timestamps and kline structure because the data comes directly from Binance’s own public API. Independence is low because the same exchange governs both the raw data and effective settlement source.