---
type: source_note
case_key: case-20260414-3ae5a275
dispatch_id: dispatch-case-20260414-3ae5a275-20260414T202946Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 be above 70000?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
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
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3ae5a275/researcher-analyses/2026-04-14/dispatch-case-20260414-3ae5a275-20260414T202946Z/personas/risk-manager.md]
tags: [polymarket, contract, source-of-truth, resolution]
---

# Summary

This source note isolates the contract wording and visible market pricing relevant to the risk-manager memo.

## Key facts extracted

- Resolution is based on Binance BTC/USDT, not other exchanges or other BTC pairs.
- The relevant candle is the 1-minute candle for `12:00` in ET on Apr. 20, 2026.
- The trigger is the final candle `Close` price, and the condition is strictly `higher than` 70,000.
- The visible market price for the 70,000 threshold was about 85-86% at review time.

## Evidence directly stated by source

- The contract language directly identifies the exchange, pair, timeframe, timestamp convention, and price field.
- The market page directly displays the market-implied probability used as baseline.

## What is uncertain

- The page does not itself provide the final resolving candle in advance.
- The phrase `12:00 in the ET timezone (noon)` still leaves a practical implementation dependency on Binance candle timestamps and ET conversion, so explicit timing verification remains important.

## Why this source may matter

For a date-sensitive and multi-condition contract, exact wording matters as much as price direction.

## Possible impact on the question

This source raises confidence that the correct question is not merely `BTC sometime around Apr. 20 above 70k`, but specifically `Binance BTC/USDT noon ET 1-minute close above 70k`.

## Reliability notes

High reliability for contract mechanics. Lower value for directional forecasting by itself; it must be paired with current price and volatility context.