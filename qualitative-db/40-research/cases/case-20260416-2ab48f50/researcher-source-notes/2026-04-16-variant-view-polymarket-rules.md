---
type: source_note
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: market-structure
entity: btc
topic: polymarket-resolution-mechanics
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 74000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and market rules
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/variant-view.md]
tags: [polymarket, resolution, binance, timing]
---

# Summary

The Polymarket rules make this a narrow, time-specific, venue-specific contract: Yes only if the Binance BTC/USDT one-minute candle labeled 12:00 in ET on April 17 has a final close strictly greater than 74,000.

## Key facts extracted

- Governing source of truth is Binance, specifically BTC/USDT with 1m candles.
- Relevant observation time is 12:00 in ET timezone on April 17, 2026.
- Resolution uses the final Close for that one-minute candle, not the day's average, high, or any other exchange.
- The test is strictly higher than 74,000; equal to 74,000 would resolve No.
- Precision is determined by the decimal places shown by the source.

## Evidence directly stated by source

- The event page explicitly states the exact market mechanics and resolution source.
- It also shows the contemporaneous market-implied probability for the 74,000 threshold around 61% at fetch time.

## What is uncertain

- The fetched page is a rendered webpage rather than an API rules endpoint, so there is mild extraction risk, though the language was clear and repeated.
- It does not itself explain whether Binance API and Binance UI candle values could diverge in presentation timing, so exact operational parity remains a small caveat.

## Why this source may matter

The contract is date-sensitive and multi-condition. Knowing exactly that the noon ET one-minute close on Binance is the deciding fact is essential because broad "Bitcoin above 74k tomorrow" narratives can be directionally right while still missing the actual settlement condition.

## Possible impact on the question

This source narrows the question materially. It weakens any overconfident market view based only on daily trend or generic BTC strength because all that matters is one venue-specific close at one minute at one time.

## Reliability notes

High relevance and effectively primary for contract interpretation. Evidence independence versus Binance price data is high enough for this case because it governs rules while Binance governs the actual price observation.