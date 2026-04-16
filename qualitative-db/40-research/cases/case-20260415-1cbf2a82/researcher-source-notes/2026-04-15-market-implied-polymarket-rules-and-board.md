---
type: source_note
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-1cbf2a82 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market page / resolution rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/market-implied.md]
tags: [polymarket, rules, market-pricing, resolution-source]
---

# Summary

This source provides the contract wording, governing source of truth, and the contemporaneous Polymarket board prices for the April 17 BTC threshold ladder.

## Key facts extracted

- The assigned market is the "$72,000" rung for April 17 and was trading around 84 cents Yes / 18 cents No on fetch, broadly consistent with the assignment current_price of 0.845.
- The market resolves Yes if the Binance BTC/USDT 1 minute candle for 12:00 ET on April 17 has a final Close above 72,000.
- The source of truth is specifically Binance BTC/USDT, not another exchange or another pair.
- Price precision is determined by the precision displayed in the source.
- Neighboring rungs on the same board were materially lower at higher thresholds (roughly 56% at 74k and 24% at 76k), implying a market distribution centered in the low-to-mid 70s rather than far above 72k.

## Evidence directly stated by source

- Exact contract wording and resolution mechanics.
- The same-day ladder prices across multiple April 17 BTC thresholds.
- The date-specific noon ET observation window.

## What is uncertain

- The web page itself is not the final settlement artifact; it points to Binance as the governing settlement source.
- The fetched page does not explain why traders hold this view, only what they are pricing.

## Why this source may matter

It is the best source for what the market is currently implying and for the exact conditions that all must hold for a Yes resolution.

## Possible impact on the question

The ladder shape supports the idea that the market is not pricing an extreme upside blowoff; it is pricing BTC as likely above 72k but far from certain to clear materially higher thresholds by the same deadline.

## Reliability notes

Useful and necessary for contract interpretation and market-implied odds, but not independent evidence about BTC fundamentals. It should be paired with Binance data or other contextual market evidence.