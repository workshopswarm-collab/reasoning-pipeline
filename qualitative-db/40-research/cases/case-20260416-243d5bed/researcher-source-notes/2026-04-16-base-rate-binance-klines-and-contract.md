---
type: source_note
case_key: case-20260416-243d5bed
dispatch_id: dispatch-case-20260416-243d5bed-20260416T161511Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: exchange-market-structure
entity: ethereum
topic: ETH/USDT Binance noon ET resolution mechanics and current price context
question: Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 close above 2300?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket market rules page plus Binance spot API market-data docs / recent klines
source_type: mixed-primary
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-243d5bed/researcher-analyses/2026-04-16/dispatch-case-20260416-243d5bed-20260416T161511Z/personas/base-rate.md]
tags: [source-note, polymarket-rules, binance, klines, resolution]
---

# Summary

This note captures the direct resolution mechanics and current spot context for the ETH > 2300 noon-ET market. The contract resolves using Binance ETH/USDT 1-minute candle data, specifically the final close of the candle labeled 12:00 ET on April 17. Binance spot API docs confirm the kline endpoint returns the close price field and supports 1-minute candles. A direct spot pull on 2026-04-16 around 12:16 ET showed ETH/USDT trading around 2337-2345, modestly above the threshold.

## Key facts extracted

- Polymarket rules say the market resolves Yes if the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 has a final close price strictly higher than 2300.
- The rules explicitly say Binance ETH/USDT, not another exchange or pair, is the governing source of truth.
- Binance spot API documentation for `/api/v3/klines` identifies the returned close field as the candle close price and supports interval `1m`.
- A direct Binance API check on 2026-04-16 around 16:16 UTC / 12:16 ET returned recent ETHUSDT 1-minute closes around 2336-2345, with the latest close near 2337.74.

## Evidence directly stated by source

- Polymarket directly states the governing condition: Binance ETH/USDT, 1-minute candle, 12:00 ET, final close price higher than 2300.
- Binance docs directly state that `GET /api/v3/klines` returns kline/candlestick bars and that the fifth field in each row is the close price.

## What is uncertain

- The exact April 17 12:00 ET closing print is not yet observable because the market has not resolved.
- Polymarket references the Binance UI chart as settlement source; while the API should match the same underlying spot market data, there is still small operational ambiguity around final displayed chart data versus programmatic retrieval if Binance revises or displays differently.

## Why this source may matter

This is the core contract-mechanics source. It establishes both the exact all-conditions-needed resolution path and the exchange/pair/timeframe specificity that prevents substitution with broader ETH/USD spot data.

## Possible impact on the question

The threshold is close enough to current spot that the market is primarily about whether ETH remains above 2300 at one precise minute tomorrow, not about broad long-run Ethereum fundamentals. Because the current spot check is above 2300, the immediate base rate is favorable to Yes, but the one-minute/time-specific structure leaves meaningful path risk.

## Reliability notes

- Polymarket rules page is the most important direct source for contract interpretation, though it is still a market-hosted source rather than an external regulator or exchange notice.
- Binance developer docs are authoritative for API field meaning and timing mechanics.
- Direct Binance spot API output is high-value contextual evidence for current level, but not itself the final settlement observation yet.
- Evidence independence is medium: contract wording and Binance data are separate sources, but both ultimately point back to the same settlement mechanism.