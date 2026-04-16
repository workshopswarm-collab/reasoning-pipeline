---
type: source_note
case_key: case-20260416-97839980
dispatch_id: dispatch-case-20260416-97839980-20260416T040518Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-price
entity: sol
topic: case-20260416-97839980 | base-rate
question: Will the price of Solana be above $80 on April 19?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance SOL/USDT API and Polymarket market rules
source_type: primary_market_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-97839980/researcher-analyses/2026-04-16/dispatch-case-20260416-97839980-20260416T040518Z/personas/base-rate.md]
tags: [binance, polymarket, resolution-source, spot-price]
---

# Summary

Directly checked the governing market rules on Polymarket and live Binance SOL/USDT spot data. The contract resolves on the Binance 1-minute candle for SOL/USDT at 12:00 ET on April 19, 2026, using the final close price. Current spot at research time was about $85.32 on Binance, already above the $80 threshold.

## Key facts extracted

- Polymarket rules say the market resolves to Yes if the Binance SOL/USDT 1-minute candle for 12:00 ET on April 19, 2026 has a final close strictly above 80.
- The contract is specifically about Binance SOL/USDT, not other exchanges or other pairs.
- Price precision is determined by the source display/quote precision.
- Binance public ticker API returned SOLUSDT price `85.32000000` at research time.
- Binance recent 1-minute klines retrieved successfully, confirming the market was trading around the mid-85 area during the verification pass.

## Evidence directly stated by source

- Polymarket contract text directly defines the source of truth and timing condition.
- Binance public API directly reports current SOL/USDT spot price and recent 1-minute candles.

## What is uncertain

- The contract resolves on April 19 at 12:00 ET, so the current spot price is only contextual, not dispositive.
- Short-horizon crypto volatility could still move SOL below $80 by the resolution minute.
- It is still worth confirming timezone handling and the exact candle convention closer to resolution.

## Why this source may matter

This is the key primary evidence pair for the case: one source defines the contract and the other is the explicit underlying market the contract references.

## Possible impact on the question

Since SOL is already about 6.6% above the strike with only a few days left, the outside-view baseline favors Yes unless there is a meaningful market drawdown or idiosyncratic Binance-only dislocation before noon ET on April 19.

## Reliability notes

- High reliability for contract interpretation because the Polymarket rule text is the governing market description.
- High reliability for underlying reference price because Binance is the specified resolution source.
- Main limitation is timing: this is a snapshot several days before resolution, so it supports a base-rate probability rather than a settled answer.
