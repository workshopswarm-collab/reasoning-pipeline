---
type: source_note
case_key: case-20260415-35855579
dispatch_id: dispatch-case-20260415-35855579-20260415T225312Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-35855579 | catalyst-hunter
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT price surfaces and Polymarket market rules
source_type: primary_market_rule + direct_exchange_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-16 ; https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=5
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-35855579/researcher-analyses/2026-04-15/dispatch-case-20260415-35855579-20260415T225312Z/personas/catalyst-hunter.md]
tags: [source-note, binance, polymarket, resolution-source, timing]
---

# Summary

This source note captures the governing market rule and a direct check of current Binance BTC/USDT pricing surfaces relevant to a short-dated threshold market.

## Key facts extracted

- Polymarket states this market resolves from the Binance BTC/USDT 1-minute candle for **12:00 ET on April 16, 2026**, using the candle's final **Close** price.
- The threshold condition is strict: the close must be **higher than 72,000**.
- Binance spot API check on 2026-04-15 showed BTCUSDT at **74912.06** at retrieval time.
- Recent Binance 1-minute klines retrieved during the same pass showed closes around **75.1k -> 74.9k**, all comfortably above 72k.

## Evidence directly stated by source

- Direct rule text from the market page: resolution uses Binance BTC/USDT, 1m candle, 12:00 ET, and final close price.
- Direct exchange data from Binance public API showed spot price and recent 1m candle closes above the target threshold.

## What is uncertain

- The market does not settle on current spot; it settles on one specific future 1-minute close at noon ET on Apr 16.
- Binance web UI is the named resolution surface; API data are highly relevant contextual verification but may not be the literal settlement surface if display discrepancies occur.
- A severe overnight selloff, exchange incident, or market-wide shock could still move BTC below 72k by the observation minute.

## Why this source may matter

This is the highest-value source set for a narrow, date-specific BTC threshold market because it combines the contract mechanics with the exchange price source named in the rules.

## Possible impact on the question

At check time, BTC was roughly 4% above the strike, implying the market only fails if BTC falls materially before the noon ET observation window or if a Binance-specific pricing/operational issue affects the measured close.

## Reliability notes

- Polymarket rules are authoritative for contract interpretation.
- Binance is the authoritative economic source named for settlement.
- API checks are useful direct verification of current conditions and timeframe mechanics, but the exact settlement source remains the Binance surface specified by Polymarket (web candles / close display).
