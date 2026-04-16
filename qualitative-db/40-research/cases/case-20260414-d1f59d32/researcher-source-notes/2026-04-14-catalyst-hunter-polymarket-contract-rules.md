---
type: source_note
case_key: case-20260414-d1f59d32
dispatch_id: dispatch-case-20260414-d1f59d32-20260414T144613Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-74k-on-april-15
question: Will the price of Bitcoin be above $74,000 on April 15?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket market page and rules for Bitcoin above 74000 on April 15
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-15
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract-rules, resolution-source, source-note]
---

# Summary

The Polymarket rules define a narrow, date-sensitive contract: settlement depends specifically on the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-15, and the final close must be higher than $74,000 for Yes to resolve.

## Key facts extracted

- The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for `12:00` in ET timezone on the target date has a final `Close` above the threshold.
- The named resolution source is Binance, with `1m` and `Candles` selected on the BTC/USDT chart.
- The contract is about Binance BTC/USDT specifically, not other exchanges or other BTC pairs.
- Precision is determined by the decimals shown by the source.
- The market page showed current market-implied probability around 78% for the 74,000 strike at fetch time.

## Evidence directly stated by source

- Exact wording of the market condition and settlement source.
- Exact exchange/pair/timeframe requirements.
- Current market pricing on the relevant strike.

## What is uncertain

- The page does not explain edge-case handling if Binance UI/API temporarily diverge or if the chart later revises a candle.
- The market page itself is not the governing price source; it only points to Binance.

## Why this source may matter

This is the governing contract interpretation layer. It determines that timing precision, exchange specificity, and the noon ET one-minute close matter more than daily close, other venues, or broader crypto sentiment alone.

## Possible impact on the question

The contract structure makes this a catalyst-timing problem: the relevant question is whether BTC can stay above $74,000 at one very specific minute tomorrow rather than whether Bitcoin is generally strong over the full day.

## Reliability notes

High reliability for contract wording and source-of-truth definition. Residual ambiguity is low but not zero because human resolution depends on a visual Binance source surface that can have small operational edge cases.