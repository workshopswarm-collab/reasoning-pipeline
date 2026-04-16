---
type: source_note
case_key: case-20260415-35855579
dispatch_id: dispatch-case-20260415-35855579-20260415T225312Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket event page and rules
source_type: market_rules_page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-35855579/researcher-analyses/2026-04-15/dispatch-case-20260415-35855579-20260415T225312Z/personas/risk-manager.md]
tags: [polymarket, contract-rules, settlement, market-implied-probability]
---

# Summary

The Polymarket event page states that the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final close strictly higher than 72,000. The same page shows the 72,000 line trading around 97.7% Yes / 2.4% No, implying extreme market confidence.

## Key facts extracted

- Resolution condition is the Binance BTC/USDT 1-minute candle for 12:00 in ET timezone on the specified date.
- The required comparison is the final candle `Close` price, and it must be higher than 72,000.
- Price source is Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the decimals used by the source.
- The 72,000 contract was displayed at roughly 97.7% Yes and 2.4% No at fetch time.

## Evidence directly stated by source

- Governing source of truth is Binance BTC/USDT with 1m candles selected.
- Timing condition is specifically 12:00 PM ET on April 16.
- Threshold test is strictly `Close > 72,000`.

## What is uncertain

- The event page is a secondary presentation of the market rules; the actual resolution data still comes from Binance.
- It does not separately document fallback procedures if Binance UI / feed access becomes impaired.
- Displayed market prices can move after the fetch.

## Why this source may matter

It establishes the exact contract mechanics, timing, and threshold condition. Those mechanics are essential because the question is not about generic bitcoin price levels; it is about a very specific exchange, pair, timeframe, and exact close print.

## Possible impact on the question

This source narrows the relevant risk set to: (1) whether BTCUSDT stays above 72,000 at the exact settlement minute, and (2) whether any Binance-specific data or operational issue affects the observed 1-minute close.

## Reliability notes

- High relevance because it states the contract mechanics.
- Moderate independence because it is the market operator’s own rules page, not a third-party check.
- Strong for interpretation, not sufficient alone for directional pricing confidence.
