---
type: source_note
case_key: case-20260416-63fb3082
dispatch_id: dispatch-case-20260416-63fb3082-20260416T145628Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-63fb3082 | market-implied
question: Will the price of Bitcoin be above $68,000 on April 21?
driver: reliability
date_created: 2026-04-16
source_name: CNBC Bitcoin/USD quote snapshot
source_type: market data page
source_url: https://www.cnbc.com/quotes/BTC.CM=
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-63fb3082/researcher-analyses/2026-04-16/dispatch-case-20260416-63fb3082-20260416T145628Z/personas/market-implied.md
tags: [cnbc, context, btcusd, cross-check]
---

# Summary

A secondary market-data check from CNBC showed Bitcoin/USD around 73,944 at 10:57 AM EDT on April 16, broadly consistent with the direct Binance BTCUSDT read around 73.9k.

## Key facts extracted

- CNBC snapshot showed BTC/USD last price 73,944.00 at 10:57 AM EDT.
- Day range shown was 73,354.75 to 75,441.03.
- Previous close shown was 74,976.85.

## Evidence directly stated by source

- The page directly displayed a live-ish quote and intraday range.

## What is uncertain

- This is a contextual cross-check, not the governing resolution source.
- BTC/USD on CNBC is not the same instrument as Binance BTC/USDT, though for this question the levels are directionally comparable.
- The extract is from a rendered quote page and could be slightly delayed.

## Why this source may matter

It provides an independent contextual check that the direct Binance read is not obviously anomalous and that Bitcoin broadly is trading in the mid-73k area, still well above 68k.

## Possible impact on the question

Marginally increases confidence that the market’s 95% prior is grounded in a real spot cushion rather than a stale or exchange-specific artifact.

## Reliability notes

Moderate reliability as an independent contextual source. Useful for cross-checking broad price level, but inferior to Binance for actual contract settlement mechanics.