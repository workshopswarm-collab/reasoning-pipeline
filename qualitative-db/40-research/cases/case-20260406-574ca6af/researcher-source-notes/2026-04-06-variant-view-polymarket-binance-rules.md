---
type: source_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
analysis_date: 2026-04-06
persona: variant-view
topic: case-20260406-574ca6af | variant-view
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
source_name: Polymarket market page resolution text
source_type: market rules / resolution source
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-march-30-april-5
source_date: 2026-04-06
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: high
agent: Orchestrator
related_entities: [ethereum, binance, polymarket]
related_drivers: []
upstream_inputs: []
downstream_uses: [variant-view finding, variant-view assumption]
tags: [resolution-rules, source-of-truth, binance, eth]
---

# Summary

This source establishes the governing contract mechanics and source of truth for the market. It materially reduces ambiguity because the market does **not** use a broad crypto price composite, DEX print, or cross-exchange best price standard.

## Key facts extracted

- The market resolves Yes if **any Binance 1-minute candle** for **ETH/USDT** during the stated ET date window has a final **High** price **>= $2,200**.
- The stated resolution source is **Binance**, specifically the ETH/USDT chart with **1m candles** selected.
- The page states that prices from **other exchanges**, **different trading pairs**, or **spot markets** will **not** be considered.

## Evidence directly stated by source

Direct rule text from the market page states that the market resolves immediately to Yes if any Binance 1-minute ETH/USDT candle in the window has a final High at or above the threshold, and otherwise resolves No. It further states the resolution source is Binance ETH/USDT 1m candles and that prices from other exchanges, different pairs, or spot markets are excluded.

## What is uncertain

- The phrase excluding “spot markets” is awkward because ETH/USDT on Binance is itself a spot pair; likely this is templated language intended to exclude non-designated venues/pairs rather than Binance spot itself.
- The market page does not mention any special market-maker attribution carveout beyond the standard candle-high rule.

## Why this source may matter

This source is the primary settlement authority. It means a DEX wick, CoinGecko composite print, or another exchange trading above $2,200 would not settle the market Yes unless Binance ETH/USDT 1m High also printed >= $2,200.

## Possible impact on the question

This pushes the analysis away from generic “did ETH broadly trade near/through $2,200 somewhere?” framing and toward the narrower question: did **Binance ETH/USDT 1m High** hit $2,200 in the specified window? That narrowing is the main place a variant view could have emerged, but once checked directly it becomes decisive.

## Reliability notes

High reliability as the governing contract text directly on the market page. Low independence because it is the market’s own rules, but that is appropriate here because source-of-truth interpretation is the core issue.
