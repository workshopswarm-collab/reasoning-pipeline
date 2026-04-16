---
type: source_note
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-cd7fa6c7 | risk-manager
question: Will the price of Bitcoin be above $74,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page for Bitcoin above ___ on April 17
source_type: market rules / resolution source summary
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/risk-manager.md]
tags: [polymarket, resolution-rules, binance, timing-risk]
---

# Summary

This source establishes the contract mechanics that govern resolution. It matters more than generic BTC price discussion because the market resolves on a specific Binance BTC/USDT 1-minute candle close at 12:00 ET on April 17, not on daily close, other exchanges, or BTC/USD composites.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on the specified date has a final Close price higher than 74,000.
- The market resolves No otherwise.
- The stated resolution source is Binance, specifically the BTC/USDT chart with 1m candles.
- Price precision is whatever Binance displays.
- This is explicitly about Binance BTC/USDT, not other exchanges or pairs.

## Evidence directly stated by source

- Resolution depends on one exact minute candle close, not an average or end-of-day print.
- Timezone handling matters: the contract says 12:00 in ET timezone.
- Instrument mapping matters: BTC/USDT on Binance.

## What is uncertain

- The Polymarket page does not itself provide the future resolving candle.
- The page does not clarify operational contingencies beyond the named source.
- The page does not discuss whether intraminute spikes above 74,000 matter; by wording, only the final close matters.

## Why this source may matter

This is the governing source-of-truth surface for the contract logic. It makes the main risk-manager issue a timing/precision problem rather than a broad Bitcoin-thesis problem.

## Possible impact on the question

It raises path risk materially. BTC can trade above 74,000 before or after noon ET and still resolve No if the exact 12:00 ET 1-minute Binance BTC/USDT close is 74,000 or lower.

## Reliability notes

High relevance and high credibility for contract interpretation because it is the market’s own rules page. It is not independent price evidence, so it should be paired with an external price/context source.