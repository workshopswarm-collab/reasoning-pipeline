---
type: source_note
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-data-infrastructure
entity:
topic: case-20260416-969f7c01 | risk-manager
question: Will the Binance ETH/USDT 1-minute candle closing at 12:00 ET on 2026-04-17 close above 2200?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance market data endpoint documentation
source_type: API documentation
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints#klinecandlestick-data
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: medium
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-969f7c01/researcher-analyses/2026-04-16/dispatch-case-20260416-969f7c01-20260416T013210Z/personas/risk-manager.md]
tags: [source-note, binance-docs, timezone, klines, contract-interpretation]
---

# Summary

Binance documentation confirms how kline bars are identified and how timezone interpretation works. This matters because the contract references a specific 12:00 ET 1-minute candle.

## Key facts extracted

- `GET /api/v3/klines` returns kline/candlestick bars for a symbol.
- Klines are uniquely identified by open time.
- A `timeZone` parameter can be supplied so intervals are interpreted in that timezone instead of UTC.
- `startTime` and `endTime` are always interpreted in UTC regardless of `timeZone`.

## Evidence directly stated by source

- The exchange provides explicit timezone handling notes.
- The exchange states that kline bars are tied to open time.

## What is uncertain

- The Polymarket UI language says "12:00 in the ET timezone (noon)" and "final close"; it does not spell out whether it conceptually refers to the minute beginning at 12:00:00 ET or the candle whose close is stamped at 12:00:59.999 ET, though these usually refer to the 12:00-12:00:59 bar in charting language.
- Binance website UI rendering and API retrieval conventions could still create user confusion if someone queries the wrong timezone.

## Why this source may matter

This is the best available source for checking timezone and candle mechanics before settlement exists.

## Possible impact on the question

It reduces but does not fully eliminate timestamp interpretation risk. The contract still appears operationally clear enough that the main uncertainty is price path, not wording ambiguity.

## Reliability notes

High for infrastructure interpretation because it is first-party exchange documentation, though it is documentation rather than the live settlement candle itself.