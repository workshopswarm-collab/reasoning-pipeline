---
type: source_note
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-3691b692 | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket market page and resolution rules
source_type: market rules page
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: market-implied
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3691b692/researcher-analyses/2026-04-14/dispatch-case-20260414-3691b692-20260414T170231Z/personas/market-implied.md]
tags: [polymarket, rules, resolution, btc]
---

# Summary

The Polymarket rules page states that the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 in ET on April 16 has a final close price above 72,000; otherwise No. The same page shows the 72,000 line trading around 90-91% Yes.

## Key facts extracted

- Market title: Bitcoin above ___ on April 16?
- The 72,000 strike is the relevant sub-market for this case.
- The displayed market price on the page is about 90-91% Yes for 72,000.
- Resolution condition is the Binance BTC/USDT 1-minute candle at `12:00` ET on the specified date.
- The relevant value is the candle’s final `Close` price.
- The source is specifically Binance BTC/USDT, not another exchange or pair.
- Precision is determined by the decimal places in the source.

## Evidence directly stated by source

- The contract mechanics and governing source-of-truth surface are explicitly stated.
- The contemporaneous market-implied probability is approximately 0.90-0.91.

## What is uncertain

- The page does not itself explain whether the Binance website candle and Binance API kline endpoint could ever diverge in edge presentation.
- The page does not give historical volatility context, only current odds and resolution mechanics.

## Why this source may matter

This is the governing market contract text. It determines what conditions must all hold for a Yes resolution and therefore is essential for any audit-ready interpretation.

## Possible impact on the question

It anchors both the market-implied baseline and the exact settlement mechanics. Any substantive view has to be expressed relative to these rules rather than generic BTC spot commentary.

## Reliability notes

High credibility for contract interpretation because it is the market operator’s own rules page. Not sufficient by itself for a price-direction estimate, so it needs live/contextual verification.
