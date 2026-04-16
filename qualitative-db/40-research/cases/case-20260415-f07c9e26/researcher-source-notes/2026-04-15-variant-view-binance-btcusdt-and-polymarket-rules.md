---
type: source_note
case_key: case-20260415-f07c9e26
dispatch_id: dispatch-case-20260415-f07c9e26-20260415T013036Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-16 be above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTC/USDT API and Polymarket market rules page
source_type: primary_plus_resolution_context
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT ; https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-f07c9e26/researcher-analyses/2026-04-15/dispatch-case-20260415-f07c9e26-20260415T013036Z/personas/variant-view.md]
tags: [binance, polymarket, resolution-rules, source-note]
---

# Summary

This note captures the direct market-resolution mechanics from Polymarket and contemporaneous Binance BTC/USDT spot data relevant to the April 16 noon ET resolution window.

## Key facts extracted

- Polymarket states the market resolves from the Binance BTC/USDT **1 minute candle for 12:00 in the ET timezone (noon)** on the specified date.
- The contract resolves to Yes only if the candle's final **Close** is **higher than 72,000**.
- Resolution source is Binance BTC/USDT with 1m candles; not another exchange or pair.
- ET noon on 2026-04-16 converts to **2026-04-16 16:00:00 UTC**.
- On 2026-04-15 during this research run, Binance spot BTC/USDT was around **74.66k**.
- Binance 24h stats during this check showed roughly **76.04k high / 73.80k low / 74.67k last**, implying BTC was already materially above the threshold but still capable of >2k intraday moves.

## Evidence directly stated by source

From Polymarket rules page:
- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance, specifically the BTC/USDT \"Close\" prices... with \"1m\" and \"Candles\" selected..."

From Binance API during run:
- ticker price: 74663.59
- 24h lastPrice: 74668.32
- 24h highPrice: 76038.00
- 24h lowPrice: 73795.47
- 24h priceChangePercent: 0.564

## What is uncertain

- Current price is not itself the settlement price; the relevant datapoint is the final close of the specific 12:00 ET one-minute candle on 2026-04-16.
- Intraday BTC volatility remains large enough that a >72k price can still fail if a sharp move occurs before the exact settlement minute.
- Binance UI/API presentation mechanics could matter at the margin if a data glitch or temporary display discrepancy emerged, though the contract language points to Binance as source of truth.

## Why this source may matter

This is the core direct evidence set for both contract interpretation and current state. It establishes exactly what must happen for resolution and shows the market is being priced from a level already comfortably above the threshold.

## Possible impact on the question

These sources support a high Yes probability, but they also reveal the strongest variant caution: a market at ~90% is implicitly assuming not just "BTC remains above 72k generally" but "BTC specifically closes above 72k on the exact Binance minute at noon ET tomorrow," which is a narrower condition than casual spot-level intuition may imply.

## Reliability notes

- Polymarket rules page is the governing contract-context source and highly relevant for resolution mechanics.
- Binance API is a direct source for current BTC/USDT prices and recent realized range.
- Evidence independence is only moderate because both sources are part of the same market/settlement ecosystem rather than independent causal evidence about future price direction.