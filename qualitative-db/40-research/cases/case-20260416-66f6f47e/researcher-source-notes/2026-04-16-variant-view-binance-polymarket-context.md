---
type: source_note
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance noon close rule and current BTC/USDT distance from 72000
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 72000 on April 21, 2026?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket market page and Binance public market data
source_type: primary-rule-plus-contextual-market-data
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [source-note, polymarket, binance, btc, noon-close]
---

# Summary

This note captures the governing rule text from the Polymarket market page and the contemporaneous Binance BTC/USDT market context available via Binance public endpoints on 2026-04-16.

## Key facts extracted

- The Polymarket rule text says the market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21 has a final Close price higher than 72,000.
- The rule explicitly says the governing source is Binance BTC/USDT with 1m candles, not other exchanges or pairs.
- Current market-implied probability for 72,000 on the fetched Polymarket page was about 79% to 80%.
- Binance spot context during this run showed BTC/USDT trading around 73,763 to 73,777.
- Recent Binance daily candles showed BTC/USDT closing above 72,000 for multiple recent days, but also with intraday swings of roughly 1,500 to 4,300 dollars.
- Binance 24h stats during the run showed a daily low of 73,309.85 and high of 75,425.00.

## Evidence directly stated by source

Primary rule text from Polymarket market page:
- Yes if the Binance 1 minute candle for BTC/USDT at 12:00 ET on the specified date has a final Close above the threshold.
- Resolution source is Binance BTC/USDT.
- Price precision is determined by the source.

Contextual market data from Binance public endpoints:
- ticker/price returned BTCUSDT around 73,777.05 during the run.
- ticker/24hr returned lastPrice around 73,762.63, highPrice 75,425.00, lowPrice 73,309.85.
- recent daily candles showed closes at or above roughly 70,741, 74,417.99, 74,131.55, 74,809.99, and 73,762.61 depending on day.

## What is uncertain

- The final resolving candle is specifically the Binance 1-minute close at 12:00 ET on April 21, which has not occurred yet.
- A direct Binance API query for the exact 2026-04-16 12:00 ET 1-minute candle returned an empty result in this environment, so this run does not treat Binance API klines here as a verified direct retrieval path for the eventual settling minute.
- Because the contract is close-based, not touch-based, temporary trading above 72,000 earlier in the day is not sufficient by itself.

## Why this source may matter

- It establishes the exact governing source and mechanism.
- It shows the market is currently pricing the threshold as likely, while live BTC/USDT context suggests the threshold is only modestly above current spot rather than deeply out of reach.

## Possible impact on the question

- The rule structure makes this more fragile than a touch market: the relevant condition is the precise noon ET close on Binance.
- Current spot above 73.7k supports a Yes-leaning baseline, but recent daily and 24h volatility show that a sub-72k noon print on April 21 is still plausible if momentum weakens.

## Reliability notes

- Rule text on the market page is the primary source for contract interpretation.
- Binance ticker and daily candle endpoints are strong contextual market data sources for current price and volatility, but they are not direct proof of the future resolving candle.
- Independence is limited because both the contract and contextual analysis revolve around Binance pricing; CoinGecko can help corroborate broader BTC spot context but not settlement.