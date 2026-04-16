---
type: source_note
case_key: case-20260416-2ab48f50
dispatch_id: dispatch-case-20260416-2ab48f50-20260416T002737Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-17 close above 74000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market rules / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-2ab48f50/researcher-analyses/2026-04-16/dispatch-case-20260416-2ab48f50-20260416T002737Z/personas/catalyst-hunter.md]
tags: [polymarket, contract-rules, binance, resolution]
---

# Summary

This source establishes the governing source of truth and the exact resolution mechanics. The market resolves on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, 2026, using the final Close price, with a strict threshold of higher than 74,000.

## Key facts extracted

- Resolution depends on Binance BTC/USDT, not other exchanges or other BTC pairs.
- The relevant candle is the 12:00 ET one-minute candle on April 17, 2026.
- The winning condition is that the final Close is strictly higher than 74,000.
- Price precision is determined by the decimals shown by the Binance source.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT... with \"1m\" and \"Candles\" selected."

## What is uncertain

- The page does not itself provide the future resolved candle value; it only defines the settlement method.
- The page does not clarify how Binance labels the candle internally versus the user-facing ET conversion, so the analyst still needs to be careful about timezone mapping when checking the live reference data.

## Why this source may matter

This is the primary source for contract interpretation. It determines what data counts and excludes alternative spot references that may differ slightly from Binance.

## Possible impact on the question

Because the contract is a narrow one-minute Binance print at noon ET, short-horizon volatility and exchange-specific price differences matter more than broad end-of-day Bitcoin direction. That makes catalyst timing and intraday path more important than a generic bullish or bearish Bitcoin thesis.

## Reliability notes

High reliability for resolution mechanics because it is the market's own governing rules surface. It is not independent evidence about the likely price outcome, only about what counts for settlement.
