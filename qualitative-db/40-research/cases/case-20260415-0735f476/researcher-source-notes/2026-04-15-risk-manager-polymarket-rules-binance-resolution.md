---
type: source_note
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin-threshold-market
entity: btc
topic: Binance noon ET close threshold resolution mechanics
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page rules for Bitcoin above ___ on April 20
source_type: market_rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/risk-manager.md
tags: [polymarket, binance, rules, resolution-source, noon-close]
---

# Summary

This source establishes the governing resolution mechanics. The contract resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026 has a final Close strictly above 70,000.

## Key facts extracted

- The governing source of truth is Binance, specifically BTC/USDT with 1m Candles selected.
- The relevant observation is the 12:00 ET candle on the date in the title.
- The relevant field is the final Close, not the high, low, midpoint, or another exchange price.
- The threshold is strictly higher than 70,000, not equal to 70,000.
- Price precision follows the source's displayed decimal precision.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- "The resolution source for this market is Binance, specifically the BTC/USDT 'Close' prices currently available at https://www.binance.com/en/trade/BTC_USDT with '1m' and 'Candles' selected on the top bar."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The exact Binance UI presentation on April 20 cannot yet be captured because the relevant future candle does not exist.
- The source note does not itself provide historical or forecasted probabilities for BTC being above 70,000 at the deadline.

## Why this source may matter

This is the primary contract interpretation source. The case is date-sensitive and rule-sensitive, so distinguishing close-versus-touch and Binance-versus-other-exchange is essential.

## Possible impact on the question

This source narrows the mechanism sharply: for a Yes resolution, all material conditions must hold simultaneously:
1. the relevant date is April 20, 2026,
2. the relevant time is 12:00 ET,
3. the relevant instrument is Binance BTC/USDT,
4. the relevant bar is the 1-minute candle at that timestamp,
5. the relevant field is the final Close,
6. that Close must be strictly greater than 70,000.

## Reliability notes

Primary resolution source. High credibility for contract mechanics. It does not answer the market directly, but it defines exactly what will count.