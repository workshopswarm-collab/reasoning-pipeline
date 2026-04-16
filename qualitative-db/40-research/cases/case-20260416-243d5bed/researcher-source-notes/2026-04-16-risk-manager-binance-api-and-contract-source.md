---
type: source_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: ethereum
topic: case-20260416-243d5bed | risk-manager
question: Will the price of Ethereum be above $2,300 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance ETHUSDT spot API plus Polymarket rules page
source_type: primary_and_contract
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT ; https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=3 ; https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/risk-manager.md
tags: [binance, polymarket, settlement-source, timing-risk]
---

# Summary

This note captures the governing settlement mechanics and a direct Binance reference price snapshot close to the research time.

## Key facts extracted

- Polymarket rules state the market resolves from the Binance ETH/USDT 1 minute candle for **12:00 ET** on **April 17, 2026**.
- The relevant value is the candle's final **Close** price, not a daily close, not another exchange, and not another pair.
- Binance spot API returned ETHUSDT spot prices around **2338.3-2338.7** during this research pass on 2026-04-16.
- Recent 1 minute kline output from Binance showed minute closes around **2337.81**, **2338.31**, and **2338.66** at the time sampled.

## Evidence directly stated by source

- Polymarket rules page directly states: the market resolves to Yes if the Binance 1 minute candle for ETH/USDT at 12:00 ET on the specified date has a final Close price higher than 2300.
- Binance API directly states current ETHUSDT spot price and recent 1 minute kline close values.

## What is uncertain

- The sampled Binance API output is a current snapshot, not the eventual April 17 12:00 ET settlement candle.
- The Polymarket page is a market UI surface rather than an exchange rules PDF, though it is still the direct market contract surface available to traders.
- Binance web UI fetch was not machine-readable here, so API output is being used as the closest direct Binance verification surface.

## Why this source may matter

It is the key direct evidence for both the contract mechanics and the current price distance from the 2300 threshold. The core risk question is whether one more day of ETH volatility can push the final relevant 12:00 ET minute close below 2300.

## Possible impact on the question

This supports a Yes-lean because ETH is currently above 2300, but it also sharpens the main risk-manager point: the contract is fragile to a relatively small adverse move at one exact minute, so current spot above 2300 is supportive but not dispositive.

## Reliability notes

- Binance API is a strong direct source for current ETHUSDT prices and 1 minute kline structure.
- Polymarket rules page is the direct contract-description source-of-truth surface for how the market intends to resolve.
- Evidence independence is only medium because both points concern the same trading venue and contract family; they are complementary rather than strongly independent.
