---
type: source_note
case_key: case-20260416-653ab0f8
dispatch_id: dispatch-case-20260416-653ab0f8-20260416T090226Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-653ab0f8 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 18?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket event page and rules
source_type: market page / primary contract source
source_url: https://polymarket.com/event/bitcoin-above-on-april-18
source_date: 2026-04-16
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
downstream_uses: [qualitative-db/40-research/cases/case-20260416-653ab0f8/researcher-analyses/2026-04-16/dispatch-case-20260416-653ab0f8-20260416T090226Z/personas/market-implied.md]
tags: [polymarket, contract-rules, market-implied, binance]
---

# Summary

This source establishes both the live market-implied probability for the $72,000 threshold and the contract mechanics that govern resolution.

## Key facts extracted

- The Apr 18 $72,000 line was trading around 88% Yes at fetch time.
- The market resolves on the Binance BTC/USDT 1-minute candle for 12:00 PM ET on Apr 18, 2026.
- The contract resolves Yes only if the final close is higher than 72,000, not equal to it.
- The resolution source is Binance BTC/USDT with 1m candles selected.
- The market is explicitly about Binance BTC/USDT, not other exchanges or pairs.

## Evidence directly stated by source

- "This market will resolve to 'Yes' if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final 'Close' price higher than the price specified in the title. Otherwise, this market will resolve to 'No'."
- The listed Apr 18 ladder showed 72,000 at about 88% Yes when checked.

## What is uncertain

- The event page does not itself show the future 12:00 PM ET Apr 18 Binance close; it only defines the rule and the current market price.
- The page gives no direct rationale for why traders are pricing 88%.

## Why this source may matter

This is the governing contract source for the prediction market. It defines the exact timestamp, timezone, exchange, pair, and strict inequality condition, all of which are necessary because this is a narrow date-specific crypto contract.

## Possible impact on the question

It anchors the baseline: if Binance BTC/USDT is already around the mid-$74k area two days before resolution, the market's 88% prior implies traders see a modest but meaningful cushion over the $72k threshold, while still leaving room for crypto volatility.

## Reliability notes

High reliability for contract wording and live market-implied pricing on Polymarket. It is not an authoritative source for the eventual answer itself; Binance remains the governing source of truth at resolution.