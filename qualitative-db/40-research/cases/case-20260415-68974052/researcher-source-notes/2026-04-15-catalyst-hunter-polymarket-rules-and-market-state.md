---
type: source_note
case_key: case-20260415-68974052
dispatch_id: dispatch-case-20260415-68974052-20260415T183011Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules
source_type: market rules / platform page
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-68974052/researcher-analyses/2026-04-15/dispatch-case-20260415-68974052-20260415T183011Z/personas/catalyst-hunter.md]
tags: [polymarket, rules, resolution, binance, timing]
---

# Summary

The Polymarket event page gives both the current market-implied probability for the $72,000 line and the governing resolution mechanics. For this case, the critical detail is that resolution is not based on a daily close or any exchange average; it is the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 17, and the final close of that specific minute must be strictly above 72,000.

## Key facts extracted

- The $72,000 bracket was trading around 86% on the fetched page, with Yes shown at 87¢ and No at 15¢.
- The market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close price higher than 72,000.
- The rules explicitly point to Binance BTC/USDT with 1m candles selected as the resolution source.
- The rules explicitly say the market is about Binance BTC/USDT, not other exchanges or other pairs.
- Price precision is determined by the number of decimal places in the source.

## Evidence directly stated by source

Directly stated by the page rules: resolution depends on the Binance 1-minute candle at 12:00 ET on the specified date, using the final close, and the threshold must be exceeded rather than merely touched.

## What is uncertain

- The public event page is not itself the final settlement record; it is the rules surface that points to Binance as source of truth.
- The page snapshot is current only at fetch time and can move before resolution.

## Why this source may matter

This is the governing contract source for what counts. It eliminates common mistakes such as using spot price on another venue, daily close, UTC noon, or intraminute highs instead of the exact candle close.

## Possible impact on the question

Because the contract is a narrow time-and-source-specific threshold market, the main catalyst question is not merely whether BTC can remain generally strong through April 17, but whether it is still above 72,000 on Binance specifically at the noon ET 1-minute close.

## Reliability notes

High credibility for contract interpretation because this is the market’s own rules page. Lower utility for independent price discovery because it is not an external market-data source.