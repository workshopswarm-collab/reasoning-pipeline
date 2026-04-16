---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on April 16, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and stated rules
source_type: market-rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-572502e1/researcher-analyses/2026-04-15/dispatch-case-20260415-572502e1-20260415T124520Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, contract, resolution]
---

# Summary

This source establishes the market structure, the market-implied baseline, and the exact resolution mechanics. It is not itself the governing source of truth for settlement, but it points directly to Binance BTC/USDT 1-minute candles as the governing source.

## Key facts extracted

- The April 16 market's 72,000 line was trading around 90% on the Polymarket page at capture time.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 16 has a final close strictly higher than 72,000.
- The contract is exchange-specific: Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by the source display.
- Other nearby strikes on the same page implied a local ladder centered around roughly 74k spot, with 74,000 near the mid-50s and 76,000 much lower.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title."
- "The resolution source for this market is Binance..."
- Current displayed probability for 72,000 was approximately 90%.

## What is uncertain

- The fetched Polymarket page is a rendered web page rather than a formal rulebook API response.
- The page does not itself provide the future 12:00 ET candle; it only states how the market will settle.
- It does not specify whether Binance later revises displayed candles, though the language implies the final close shown on Binance controls.

## Why this source may matter

This is the key contract-interpretation source. For a narrow, date-specific market with extreme pricing, the exact candle timing, timezone, exchange, pair, and strict-greater-than condition are all material.

## Possible impact on the question

It raises the importance of timing and exchange-specific operational details. A BTC price above 72k on other exchanges or before noon ET is insufficient if Binance BTC/USDT is below 72k on the specific 12:00 ET one-minute candle close.

## Reliability notes

Useful as the market's own rules page, but not fully independent. Reliability is strongest for contract wording and current implied price, weaker for any broader market narrative. The actual governing settlement value still comes from Binance.