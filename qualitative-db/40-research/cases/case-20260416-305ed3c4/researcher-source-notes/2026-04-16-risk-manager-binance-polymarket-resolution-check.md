---
type: source_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: binance
topic: case-20260416-305ed3c4 | risk-manager
question: Will the price of Ethereum be above $2,200 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance spot API + Polymarket market rules
source_type: primary-plus-resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum, binance]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/risk-manager.md]
tags: [source-note, binance, polymarket, resolution-check, ethusdt]
---

# Summary

This note captures the direct resolution mechanics and the most important live verification for the ETH > 2200 daily threshold market.

## Key facts extracted

- Polymarket states the market resolves from the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17, using the candle's final Close price.
- Polymarket explicitly says the market is about Binance ETH/USDT, not other exchanges or pairs.
- Binance spot API returned ETHUSDT last price around 2343-2345 on 2026-04-16 15:02-15:03 ET.
- Binance 1-minute klines endpoint returned recent 1m candles with closes around 2343.10, 2343.37, 2343.36, 2343.55, and 2343.42.
- Binance 24h ticker returned lastPrice 2344.54, highPrice 2385.61, lowPrice 2285.10, and a 24h window ending around 2026-04-16 15:03 ET.
- Binance developer docs confirm `/api/v3/klines` supports 1m candles and timezone handling; start/end times remain UTC while kline intervals can be interpreted in a provided timezone.

## Evidence directly stated by source

- Polymarket rules: Yes resolves if the Binance 1 minute candle for ETH/USDT at 12:00 ET on the specified date has a final Close price higher than 2200.
- Binance docs: klines are uniquely identified by open time and the endpoint provides close prices for 1m candles.

## What is uncertain

- The exact April 17 12:00 ET candle is not yet available at research time.
- There is still overnight and morning price-path risk before the resolution window.
- Using the website chart manually vs API output could create minor presentation differences, though both point to Binance as source of truth.

## Why this source may matter

This is the governing evidence for both contract interpretation and the current state of the underlying. It constrains what counts, which venue matters, and what exact market condition must hold.

## Possible impact on the question

Because ETH/USDT on Binance is currently roughly 6% above the 2200 threshold and even the verified 24h low is still above 2200, the direct evidence strongly supports Yes. The main remaining risk is not current level uncertainty but adverse path risk before the noon ET settlement candle.

## Reliability notes

- Polymarket is authoritative for contract wording but not for the underlying price outcome itself.
- Binance is the stated resolution source and therefore the most authoritative source for the settlement-relevant price series.
- Binance API documentation is high-quality contextual support for how the relevant kline endpoint works.
- Evidence independence is moderate rather than high because the contextual verification still centers on Binance surfaces.