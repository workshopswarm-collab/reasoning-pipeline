---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, rules, resolution, contract]
---

# Summary

The Polymarket rules page defines the contract narrowly: the market resolves Yes only if the Binance BTC/USDT one-minute candle labeled 12:00 in ET on 2026-04-16 has a final close strictly greater than 72,000.

## Key facts extracted

- The event page showed the 72,000 line trading around 90% at fetch time, matching the assignment `current_price: 0.895` closely enough for market-implied probability reference.
- Rules specify Binance BTC/USDT, not other exchanges or BTC/USD references.
- Rules specify the one-minute candle for 12:00 ET (noon) on the date in the title.
- Rules specify the final `Close` price must be higher than the strike; equality would resolve No.
- Price precision is determined by the source’s decimal precision.

## Evidence directly stated by source

- Governing source of truth is Binance spot market data for BTC/USDT.
- Material conditions are pair specificity, timestamp specificity, one-minute candle specificity, and strict-greater-than threshold.

## What is uncertain

- The event page fetch is not an exchange price source; it only defines rules and displayed market pricing.
- The page text does not itself provide the future resolution candle, so it must be combined with Binance data.

## Why this source may matter

This is the definitive contract-interpretation source. The case is date-sensitive and multi-condition, so resolution mechanics matter as much as directional price intuition.

## Possible impact on the question

This source narrows the relevant risk: the bet is not “is BTC generally above 72k tomorrow” across all venues, but whether Binance BTC/USDT specifically remains above 72k at the exact noon ET minute close.

## Reliability notes

- Primary source for contract wording.
- Strong for settlement interpretation, but not sufficient alone for forecasting the outcome.