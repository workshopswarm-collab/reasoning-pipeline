---
type: source_note
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-f29db686 | base-rate
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: primary_market_rule
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, market-state, binance, settlement]
---

# Summary

This source defines the contract mechanics and provides the live market-implied probability. It is the governing market/rules source for what must happen for a Yes resolution.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for **12:00 ET on April 17, 2026** has a final **Close** price **higher than 74,000**.
- The resolution source is explicitly Binance BTC/USDT with 1m candles.
- The market is not about other exchanges or other trading pairs.
- The visible market price for the 74,000 threshold was about **61% Yes** at fetch time, consistent with the assignment `current_price: 0.605`.

## Evidence directly stated by source

- Contract wording identifies the exact settlement test: Binance, BTC/USDT, 1-minute candle, 12:00 ET, close price, threshold above 74,000.
- Market page displayed 74,000 outcome near 61%.

## What is uncertain

- The fetched page is a rendered market page, not a Binance historical candle endpoint.
- The page does not itself provide the future resolution value; it only defines the rule and current odds.

## Why this source may matter

The contract is narrow and date-sensitive. Correct interpretation depends on checking the exact source of truth, exchange, pair, timeframe, and timezone.

## Possible impact on the question

This source anchors both the implied baseline and the operational constraints. Any price evidence from non-Binance venues is only contextual unless it tracks Binance closely enough to inform the prior.

## Reliability notes

Primary for contract interpretation and market state, but not primary for the eventual resolved price itself. Because the contract is mechanically precise, resolution ambiguity is low once the exact timestamp mapping is understood.