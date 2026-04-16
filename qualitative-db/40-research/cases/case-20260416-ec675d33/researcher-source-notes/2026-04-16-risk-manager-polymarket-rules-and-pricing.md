---
type: source_note
case_key: case-20260416-ec675d33
dispatch_id: dispatch-case-20260416-ec675d33-20260416T073538Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on 2026-04-20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market rules / market pricing page
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ec675d33/researcher-analyses/2026-04-16/dispatch-case-20260416-ec675d33-20260416T073538Z/personas/risk-manager.md]
tags: [polymarket, rules, pricing, resolution]
---

# Summary

The Polymarket market page provides the direct contract wording, the named resolution source, and the contemporaneous market price for the $72,000 threshold leg. It is the key direct source for contract mechanics but not itself the settlement source.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026 has a final close price strictly higher than 72,000.
- The market resolves No otherwise.
- The named resolution source is Binance BTC/USDT with 1m candles selected.
- The rule explicitly says the contract is about Binance BTC/USDT, not other exchanges or pairs.
- Price precision is determined by Binance source decimals.
- The visible market price for the 72,000 leg was about 84-85% at time of review, consistent with assignment current_price 0.845.

## Evidence directly stated by source

- Exact settlement condition: Binance BTC/USDT 12:00 ET 1-minute candle close must be higher than 72,000.
- Exact source-of-truth surface: Binance BTC/USDT candles.
- Multi-condition detail: exchange, pair, timeframe, local ET timestamp, and strict-greater-than threshold all matter.

## What is uncertain

- The Polymarket page does not itself provide the future April 20 settlement candle.
- The page does not independently verify how Binance UI labels ET versus local/browser timezone, so a timing check still matters.
- The page is not independent evidence about whether BTC will actually remain above 72,000 by settlement.

## Why this source may matter

This source governs the contract interpretation. For a date-specific crypto threshold market, wording and timing risk matter almost as much as spot direction.

## Possible impact on the question

The rules narrow the relevant outcome to one exchange, one pair, one minute, and one ET timestamp. That makes path risk and exchange-specific print risk more relevant than a looser question like daily average price or broad market spot level.

## Reliability notes

Useful as the contract source and market-pricing surface, but not authoritative for the final answer beyond rules and current implied odds. It should be paired with a direct Binance source for price context and eventual settlement logic.