---
type: source_note
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules for bitcoin-above-on-april-17
source_type: market rules / market state
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/variant-view.md]
tags: [polymarket, rules, resolution, binance, timing]
---

# Summary

This source establishes both the market-implied probability baseline and the contract mechanics. It states that the market resolves on the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 17, using the final Close price, and shows the current market price for the 72,000 line at roughly 84% Yes.

## Key facts extracted

- Current market-implied probability for BTC above 72,000 on April 17 is about 84% Yes on the Polymarket page.
- Resolution is based on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17, 2026.
- The relevant value is the final candle Close, not the high, low, midpoint, or another exchange print.
- Price precision is determined by the source display.
- The market is explicitly about Binance BTC/USDT, not BTC/USD or other exchanges.

## Evidence directly stated by source

- The rules directly name Binance as the source of truth.
- The rules directly name the 12:00 ET 1-minute candle and its final Close as the settlement mechanism.
- The market page directly shows the 72,000 contract trading around 84 cents Yes at time of review.

## What is uncertain

- The fetched page is not itself an exchange API and should not be treated as the final settlement print.
- The market page does not itself provide the future April 17 noon candle value.
- Polymarket page extraction is enough for rules and baseline, but the authoritative settlement value still must come from Binance.

## Why this source may matter

This is the governing contract surface. It determines what counts, what does not count, and where a variant view can exist: not in abstract Bitcoin direction, but in the risk that a sub-48-hour horizon and one-minute Binance close leave more downside variance than the 84% market price implies.

## Possible impact on the question

This source narrows the analysis to a specific, date-sensitive, exchange-specific, one-minute settlement event. That makes timing and microstructure more important than a general bullish BTC narrative.

## Reliability notes

Strong for market rules and current market state; not sufficient alone for actual settlement because Binance remains the source of truth for the final April 17 noon ET close.