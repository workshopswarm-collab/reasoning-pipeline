---
type: source_note
case_key: case-20260415-572502e1
dispatch_id: dispatch-case-20260415-572502e1-20260415T124520Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 1-minute candle at 12:00 ET on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market_contract
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
downstream_uses: []
tags: [polymarket, contract, market-implied-probability, resolution-rules]
---

# Summary

This source establishes both the market-implied baseline and the governing contract mechanics. It says the 72,000 line is trading around 90% Yes and that resolution depends specifically on the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16, using the final Close price.

## Key facts extracted

- The displayed market price for the 72,000 threshold was about 90% Yes at capture time.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 16 has a final Close strictly higher than 72,000.
- The source of truth is Binance spot BTC/USDT with 1m candles selected.
- Exchange choice, pair choice, exact minute, timezone, and strict-greater-than condition all matter.
- Price precision is determined by Binance source decimals.

## Evidence directly stated by source

- Polymarket lists the Apr 16 BTC-above ladder and shows the 72,000 bracket around 90%.
- Rules text explicitly names Binance BTC/USDT, the 12:00 ET 1-minute candle, and the final Close field.

## What is uncertain

- The page itself does not provide the future resolving candle; it only provides contract mechanics and current market pricing.
- The page text does not independently validate whether Binance data access could become operationally impaired near resolution.

## Why this source may matter

This is the direct contract source. For a date-specific, rule-sensitive market, the exact settlement wording is part of the substance, not background.

## Possible impact on the question

It fixes the relevant benchmark: not generic BTC price, not another exchange, and not an intraday high. The position is effectively a question about whether Binance spot BTC/USDT stays above 72,000 exactly at noon ET on Apr 16.

## Reliability notes

Useful as the authoritative contract/rules surface for Polymarket, but not independent evidence for the underlying BTC level. It should be paired with a direct Binance data source for context and verification.