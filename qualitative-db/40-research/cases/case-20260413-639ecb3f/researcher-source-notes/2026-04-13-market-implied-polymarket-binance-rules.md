---
type: source_note
case_key: case-20260413-639ecb3f
dispatch_id: dispatch-case-20260413-639ecb3f-20260413T225424Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: protocols
entity: ethereum
topic: case-20260413-639ecb3f | market-implied
question: Will Ethereum reach $2,400 April 13-19?
driver:
date_created: 2026-04-13
source_name: Polymarket market page / embedded rules text
source_type: market page / resolution rules
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-april-13-19
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [ethereum]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-639ecb3f/researcher-analyses/2026-04-13/dispatch-case-20260413-639ecb3f-20260413T225424Z/personas/market-implied.md]
tags: [polymarket, resolution-rules, binance, eth]
---

# Summary

The Polymarket page provides both the live market-implied probability for the "$2,400" bucket and, in embedded page text, the contract-resolution logic. The key rule is that the market resolves Yes if any Binance ETH/USDT 1-minute candle during Apr 13-19 ET has a final High at or above $2,400.

## Key facts extracted

- The assigned current price for the "$2,400" outcome is 0.76, implying a 76% market probability.
- The market page text indicates the leading adjacent outcome is "$2,300" at 100%, consistent with ETH already trading above $2,300.
- Embedded rules text says the market resolves Yes if any Binance 1-minute candle for ETH/USDT during the specified ET date range has a final High greater than or equal to $2,400.
- The page identifies Binance ETH/USDT 1-minute candle highs as the governing resolution source, not aggregate spot indices or other exchanges.

## Evidence directly stated by source

- Current odds on the market page for the relevant outcome are 76%.
- Resolution depends on Binance ETH/USDT 1-minute High prices over the stated window.
- A touch on another venue or in another pair would not count unless reflected in the Binance ETH/USDT 1-minute High.

## What is uncertain

- The market page itself is not an official Binance record; it quotes/embeds the rule text.
- The page snapshot is current as fetched, but prices can move rapidly after capture.
- The page does not itself prove that ETH will touch $2,400; it only clarifies what counts.

## Why this source may matter

This is the closest available primary source for both the market-implied probability and the contract mechanics. For a date-bounded hit-level market, exact source-of-truth mechanics materially affect how reachable the target is.

## Possible impact on the question

Because the threshold is checked on Binance 1-minute highs, the bar is easier to satisfy than a sustained close above $2,400. That mechanically supports a relatively high Yes probability when spot is already in the mid-$2,300s and weekly realized range is large enough to allow a brief wick.

## Reliability notes

Useful as the governing contract surface, but still should be paired with an independent contextual source on actual ETH trading levels and volatility. The rules text appears directly in page HTML and is specific enough to audit.