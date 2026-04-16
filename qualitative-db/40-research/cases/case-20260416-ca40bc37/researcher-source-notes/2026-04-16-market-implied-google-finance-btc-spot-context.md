---
type: source_note
case_key: case-20260416-ca40bc37
dispatch_id: dispatch-case-20260416-ca40bc37-20260416T053546Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-20
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: reliability
date_created: 2026-04-16
source_name: Google Finance BTC/USD quote page
source_type: secondary contextual price source
source_url: https://www.google.com/finance/quote/BTC-USD
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-ca40bc37/researcher-analyses/2026-04-16/dispatch-case-20260416-ca40bc37-20260416T053546Z/personas/market-implied.md]
tags: [google-finance, btcusd, context-price]
---

# Summary

This source provides an independent, recent contextual BTC spot reference to test whether the market's 84.5% probability for staying above $72,000 looks directionally sensible.

## Key facts extracted

- Google Finance showed BTC/USD around **$74,039.75** at fetch time.
- It listed a previous close around **$74,182.03**.
- The page timestamp in the fetch was **Apr 15, 10:00:36 UTC**.

## Evidence directly stated by source

The page directly reports a live BTC/USD quote near $74.0k, which is about $2k above the contract threshold.

## What is uncertain

- This is BTC/USD, not Binance BTC/USDT.
- The page does not provide the exact Binance noon-ET April 20 candle that will settle the market.
- Quote timing in the fetched page may lag the exact present moment of the run.

## Why this source may matter

It is a reasonably independent contextual check that BTC is currently trading above the strike by a meaningful but not enormous margin. That supports the market's positive baseline but also shows the buffer is not so large that downside volatility is irrelevant.

## Possible impact on the question

A current spot level around $74k makes an above-$72k resolution plausible and helps explain why the market is strongly Yes-leaning. At the same time, the gap to threshold is modest enough that a few percent drawdown over four days could still flip the outcome.

## Reliability notes

Useful as a secondary context source, but not authoritative for settlement because the contract is tied specifically to Binance BTC/USDT 1-minute close data at noon ET on April 20.