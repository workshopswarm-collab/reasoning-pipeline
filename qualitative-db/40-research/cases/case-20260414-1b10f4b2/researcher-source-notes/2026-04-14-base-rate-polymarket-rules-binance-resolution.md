---
type: source_note
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-68k-on-april-20
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-20 close above 68000?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and Binance spot API docs
source_type: primary_market_rules_plus_exchange_api_docs
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-14
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-1b10f4b2/researcher-analyses/2026-04-14/dispatch-case-20260414-1b10f4b2-20260414T201759Z/personas/base-rate.md]
tags: [polymarket, binance, resolution, contract, timezone]
---

# Summary

The governing contract is narrow and operationally specific: the market resolves from the Binance BTC/USDT 1-minute candle corresponding to 12:00 ET on April 20, using the candle's final Close price, not spot price on another venue or a daily close.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on the specified date has a final Close price higher than 68,000.
- The rules explicitly say the source is Binance BTC/USDT with 1m candles selected.
- Binance spot API documentation for `GET /api/v3/klines` says klines are uniquely identified by open time and returns a Close price field.
- Binance docs also say `timeZone` can be specified for kline interval interpretation, but `startTime` and `endTime` remain interpreted in UTC.

## Evidence directly stated by source

- Direct contract wording from Polymarket establishes the resolution mechanics and source of truth.
- Direct exchange documentation establishes that 1-minute klines and a close-price field exist in the Binance API, matching the contract wording.

## What is uncertain

- The Polymarket page references the Binance UI chart rather than an explicit API endpoint for settlement, so there is a small operational ambiguity around UI-vs-API presentation, though both should reflect the same underlying Binance candle data.
- The exact 12:00 ET candle on April 20 is not yet observable.

## Why this source may matter

This source defines the only price and timestamp that count. For this market, correct interpretation of Binance 1-minute candle timing matters more than broader BTC narratives.

## Possible impact on the question

The contract narrows the event to a single Binance minute close six days ahead. That reduces some ambiguity but increases date/time and venue specificity. Current BTC levels far above 68,000 are relevant only insofar as they imply a cushion against a decline before the target minute.

## Reliability notes

High reliability for resolution mechanics. Independence is limited because both contract interpretation and exchange implementation point back to Binance as the source of truth, but that is acceptable here because Binance is the designated settlement venue.