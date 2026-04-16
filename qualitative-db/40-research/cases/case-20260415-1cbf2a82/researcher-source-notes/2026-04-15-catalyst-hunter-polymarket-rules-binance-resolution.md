---
type: source_note
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and embedded rules
source_type: market-rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-15
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, resolution, timing, source-note]
---

# Summary

This source defines the contract mechanics that govern the market. It is the key source for timing, venue, and exact condition interpretation.

## Key facts extracted

- The market resolves to "Yes" if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 17 has a final close strictly higher than 72,000.
- The relevant source is Binance, specifically BTC/USDT with 1m candles selected.
- This is not a cross-exchange or aggregate-price market.
- Price precision is whatever Binance shows.
- On the market page at capture time, the 72,000 outcome was trading around 84¢, implying roughly 84-85%.

## Evidence directly stated by source

Directly stated on the page: resolution depends on the Binance 1-minute BTC/USDT candle at 12:00 ET on the date in the title, and the close must be higher than the threshold.

## What is uncertain

- The public page is authoritative for market rules but not itself the final Binance candle print.
- It does not specify any fallback if Binance display behavior changes, so operational interpretation still depends on Binance availability and the displayed candle data.

## Why this source may matter

This is the governing source-of-truth for what counts. A broad Bitcoin rally that leaves Binance BTC/USDT below 72,000 at the exact noon ET minute would still resolve "No."

## Possible impact on the question

This source makes the market highly timing-sensitive. Intraday drift, exchange-specific basis, and the exact noon ET candle matter more than end-of-day direction. It also means the main catalyst is simply whether BTC can avoid a >~2.7% drawdown from the current Binance price before the cutoff.

## Reliability notes

Useful and necessary for contract interpretation, but not independent market evidence. It should be paired with direct Binance price checks or other contextual market sources.
