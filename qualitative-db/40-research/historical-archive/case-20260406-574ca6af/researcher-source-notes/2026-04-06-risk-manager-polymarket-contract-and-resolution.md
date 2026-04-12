---
type: source_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
analysis_date: 2026-04-06
persona: risk-manager
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260406-574ca6af | risk-manager
question: Will Ethereum reach $2,200 March 30-April 5?
driver: resolution mechanics
date_created: 2026-04-06T01:36:00Z
source_name: Polymarket market page / contract text
source_type: market contract
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-march-30-april-5
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum, binance, polymarket]
related_drivers: [resolution mechanics, source-of-truth ambiguity]
upstream_inputs: []
downstream_uses: [risk-manager finding, assumption note]
tags: [polymarket, binance, resolution-source, cex, no-dex]
---

# Summary

This source is the governing contract text for the market. It directly answers the otherwise ambiguous source-of-truth question.

## Key facts extracted

- Market resolves Yes if **any Binance 1-minute candle for ETH/USDT** during the title window has a final **High** price **>= 2200**.
- Resolution source is explicitly **Binance ETH/USDT** with chart settings on **1m** candles.
- Contract says the outcome depends **solely** on Binance ETH/USDT price data.
- Contract explicitly says prices from **other exchanges, different trading pairs, or spot markets** will **not** be considered.

## Evidence directly stated by source

The page text states that the market will immediately resolve to Yes if any Binance 1-minute candle high during the specified date range reaches the threshold, and that Binance ETH/USDT 1m candles are the resolution source.

## What is uncertain

- The phrase excluding "spot markets" is awkward because ETH/USDT on Binance is itself a spot pair; likely the intended meaning is that non-designated sources do not count.
- The page does not provide any special market-maker attribution or anti-manipulation override beyond the designated Binance source.

## Why this source may matter

This is the authoritative source-of-truth surface. It resolves the main contract-risk question: this is a **CEX-specific** market, not a best-price, DEX, or blended-index market.

## Possible impact on the question

If Binance printed 2200 on any 1m candle high in the window, the market should resolve Yes even if DEXs or other exchanges differed. If Binance never printed it, DEX spikes or other exchange highs should not matter.

## Reliability notes

High reliability for resolution mechanics because it is the contract text itself, fetched from the market page. It is less useful for empirical price verification than Binance data.