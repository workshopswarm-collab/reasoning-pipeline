---
type: source_note
case_key: case-20260416-cc34f737
dispatch_id: dispatch-case-20260416-cc34f737-20260416T162722Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: prediction-markets
entity: ethereum
topic: ethereum-above-2300-on-april-17
question: Will the price of Ethereum be above $2,300 on April 17?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, market-implied-probability, binance]
---

# Summary

This source establishes both the market-implied baseline and the governing contract mechanics. It shows the $2,300 line trading around 71% and states that resolution depends specifically on the Binance ETH/USDT 1-minute candle labeled 12:00 in ET timezone on April 17, 2026.

## Key facts extracted

- The $2,300 April 17 contract was trading around 71% Yes on the market page when checked.
- The market resolves Yes only if the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 has a final close strictly above 2,300.
- The source of truth is Binance ETH/USDT, not other exchanges or USD pairs.
- Price precision is determined by Binance's displayed decimals.

## Evidence directly stated by source

- Contract wording explicitly names Binance ETH/USDT and the 12:00 ET 1-minute candle close as the resolution reference.
- The market page displayed 71% for the 2,300 threshold at the time of review.

## What is uncertain

- The market page does not itself prove what Binance will print tomorrow at noon ET.
- The page does not clarify edge-case handling beyond the general rules text, so practical settlement still depends on the final visible Binance candle data.

## Why this source may matter

This is the governing source for what counts. For a narrow, date-sensitive contract, rule mechanics matter almost as much as directional ETH price context.

## Possible impact on the question

This source narrows the question from a general “Will ETH be above 2,300 tomorrow?” to a stricter “Will Binance ETH/USDT close the noon ET one-minute candle above 2,300?” framing. That makes intraday path dependence and exchange-specific pricing relevant.

## Reliability notes

Useful and necessary as the contract source, but not independent evidence about underlying ETH direction. It is best paired with direct Binance price data and a contextual spot-price source.