---
type: source_note
case_key: case-20260416-e0b8c17c
dispatch_id: dispatch-case-20260416-e0b8c17c-20260416T050131Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260416-e0b8c17c | catalyst-hunter
question: Will the price of Bitcoin be above $72,000 on April 20?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules plus direct Binance kline/API verification
source_type: contract rules + exchange API
source_url: https://polymarket.com/event/bitcoin-above-on-april-20
source_date: 2026-04-16
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-e0b8c17c/researcher-analyses/2026-04-16/dispatch-case-20260416-e0b8c17c-20260416T050131Z/personas/catalyst-hunter.md]
tags: [polymarket, binance, catalyst-calendar, settlement, timing]
---

# Summary

This source note captures the key near-term catalyst structure for the case: there is no scheduled macro release embedded in the contract itself; the decisive catalyst is the exact Binance BTC/USDT 1-minute noon ET close on April 20. Current Binance pricing is materially above the threshold, but the contract is path-sensitive because one adverse move into the settlement minute can flip the outcome.

## Key facts extracted

- Polymarket rules say the market resolves Yes only if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 20 has a final Close strictly higher than 72,000.
- Binance documentation confirms `/api/v3/klines` returns 1-minute candlestick bars and that the close price is an explicit field in the returned bar.
- Noon ET on April 20, 2026 corresponds to 16:00 UTC because New York is on EDT.
- Direct Binance API checks during the run showed BTC/USDT around 75,000, about 4.1% above the strike.
- Recent daily Binance closes: Apr 13 ~74,418; Apr 14 ~74,132; Apr 15 ~74,810; current Apr 16 partial ~74,991.
- In a 14-day hourly Binance sample ending during this run, 111 of 336 hourly closes were above 72,000, showing that the threshold is currently favorable but not invulnerable.

## Evidence directly stated by source

- Contract source-of-truth is Binance BTC/USDT 1-minute candle close at the named time.
- Binance API docs state klines are uniquely identified by open time and include the close price field.
- Recent Binance BTCUSDT prices are above the 72,000 strike.

## What is uncertain

- This source set does not identify a single scheduled exogenous event that is likely to dominate BTC before April 20.
- The exact settlement minute could still land below 72,000 despite surrounding hours or days staying above it.
- Binance browser-display settlement and Binance API verification are highly related, so independence is limited.

## Why this source may matter

For this short-dated market, the core catalyst is timing itself: the resolution window is one minute at a fixed exchange and clock time. That makes catalyst analysis mostly about whether any upcoming event is likely to cause a repricing large enough to erase a ~3,000-point cushion before noon ET on April 20.

## Possible impact on the question

This evidence supports a high Yes probability, but it also says the market should not be treated like a simple "BTC above 72k sometime that day" contract. The main watch item is any weekend or Monday-morning volatility strong enough to push Binance BTC/USDT below 72,000 into the 12:00 ET candle.

## Reliability notes

Strong for contract interpretation and direct venue context. Evidence independence is only medium because both the contract rules and price verification ultimately point back to Binance as the governing source family.