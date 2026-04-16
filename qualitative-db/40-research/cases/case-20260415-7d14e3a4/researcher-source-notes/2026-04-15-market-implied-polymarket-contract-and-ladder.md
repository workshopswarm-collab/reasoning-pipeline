---
type: source_note
case_key: case-20260415-7d14e3a4
dispatch_id: dispatch-case-20260415-7d14e3a4-20260415T231343Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-7d14e3a4 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 19?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket event page and outcome ladder
source_type: market page / contract text / market-implied reference
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-15
credibility: medium-high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-7d14e3a4/researcher-analyses/2026-04-15/dispatch-case-20260415-7d14e3a4-20260415T231343Z/personas/market-implied.md]
tags: [polymarket, contract, market-implied, threshold]
---

# Summary

This source note records the market-implied baseline and the contract mechanics shown on the Polymarket page.

## Key facts extracted

- The assignment states current_price `0.865`, implying an 86.5% market probability for yes.
- The Polymarket page displayed the $72,000 ladder outcome at roughly 87% yes, consistent with the assignment snapshot.
- The page states the market resolves yes if the Binance BTC/USDT 1-minute candle for `12:00` ET on Apr 19 has a final close price strictly higher than $72,000.
- The page explicitly notes this is Binance BTC/USDT, not other exchanges or pairs, and that price precision follows the source.

## Evidence directly stated by source

- Exact settlement condition: final 12:00 ET one-minute candle close on Binance BTC/USDT must be above $72,000.
- Named source of truth: Binance trading page with 1m candles selected.

## What is uncertain

- The Polymarket display is not itself the settlement source.
- Outcome ladder prices can move quickly.
- There may be small interface/API presentation differences, though source family is clearly Binance BTC/USDT.

## Why this source may matter

This is the governing contract text and the direct source for the market-implied probability baseline used in the analysis.

## Possible impact on the question

The contract is narrow and timing-sensitive. A bullish general BTC view is not enough; the relevant question is whether BTC remains above the strike at the exact Binance noon ET one-minute close on Apr 19.

## Reliability notes

High reliability for market wording and baseline pricing. It is authoritative for contract rules but not for the ultimate price observation at resolution.
