---
type: source_note
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
analysis_date: 2026-04-06
persona: base-rate
topic: case-20260406-574ca6af | base-rate
question: Will Ethereum reach $2,200 March 30-April 5?
date_created: 2026-04-06
source_name: Polymarket market page + Binance ETHUSDT 1m klines
source_type: primary + authoritative resolution data
source_url: https://polymarket.com/event/what-price-will-ethereum-hit-march-30-april-5 ; https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&startTime=1774843200000&endTime=1775361599000
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, ethereum, binance, resolution-source, crypto-price-market]
---

# Summary

This source note captures the governing contract mechanics and direct verification of the relevant Binance ETH/USDT 1-minute high during the March 30-April 5 ET window.

## Key facts extracted

- Polymarket states the market resolves YES only if any Binance 1-minute candle for ETH/USDT during the specified ET date range has a final High at or above $2,200.
- Polymarket explicitly states the resolution source is Binance, specifically ETH/USDT on 1m candles.
- Polymarket explicitly states prices from other exchanges, different trading pairs, or spot markets will not be considered.
- A full pull of Binance ETH/USDT 1-minute klines from 2026-03-30 00:00 ET through 2026-04-05 23:59:59 ET yielded 8,640 candles.
- The maximum observed Binance ETH/USDT 1-minute high in that window was 2167.85.
- That maximum occurred in the candle opening 2026-04-01 13:03:00 ET and closing 2026-04-01 13:03:59.999 ET.
- Since 2167.85 < 2200, the direct source-of-truth check supports NO.

## Evidence directly stated by source

Directly from Polymarket market page:
- "This market will immediately resolve to 'Yes' if any Binance 1-minute candle for ETH/USDT during the date range specified in the title ... has a final 'High' price equal to or greater than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance... with the chart settings on '1m' candles selected..."
- "Please note that the outcome of this market depends solely on the price data from the Binance ETH/USDT trading pair. Prices from other exchanges, different trading pairs, or spot markets will not be considered..."

## What is uncertain

- The source note does not independently verify whether Binance later revises historical chart data, though that is not suggested by the evidence reviewed.
- The note does not verify any internal Polymarket dispute/escalation process; it focuses on the stated rule and the referenced source itself.

## Why this source may matter

This is the core resolution source. It is more important than generalized ETH price summaries because the contract is rule-sensitive and excludes non-Binance prints.

## Possible impact on the question

This source is effectively decisive unless the Binance source surface itself is wrong or revised. It strongly supports a NO resolution because the verified max high remained below $2,200.

## Reliability notes

- Reliability is high because the rule language is taken from the market page itself and the verification is drawn from the exact referenced Binance ETH/USDT 1-minute kline endpoint.
- Evidence independence is not high because both rule and data revolve around the same governing ecosystem, but that is acceptable here because the contract is directly settled by that source-of-truth surface.