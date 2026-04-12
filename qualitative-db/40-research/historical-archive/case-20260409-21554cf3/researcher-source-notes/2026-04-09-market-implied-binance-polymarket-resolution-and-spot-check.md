---
type: source_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
analysis_date: 2026-04-09
persona: market-implied
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260409-21554cf3 | market-implied
question: Will the price of Ethereum be above $2,100 on April 9?
driver: reliability
date_created: 2026-04-09T03:35:00-04:00
source_name: Binance ETHUSDT API + Polymarket market rules page
source_type: primary_resolution_plus_market_rules
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&startTime=1775750400000&endTime=1775750460000&limit=1
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/market-implied.md]
tags: [binance, polymarket, resolution-source, exact-candle, timezone-check]
---

# Summary

This note records the governing source-of-truth mechanics and a direct Binance spot check relevant to the market pricing.

## Key facts extracted

- Polymarket rules explicitly state this market resolves from the Binance ETH/USDT 1-minute candle for **12:00 in ET timezone (noon)** on 2026-04-09, using the candle's final **Close** price.
- The rules explicitly say the market is about **Binance ETH/USDT**, not another exchange or pair.
- Session time check confirms 2026-04-09 12:00 ET = **2026-04-09 16:00:00 UTC**.
- A direct Binance API spot check at approximately 03:34 ET / 07:34 UTC returned ETHUSDT around **2183.68**, already above the 2100 strike by roughly **$83.68**.
- Recent Binance 1m klines around the observation time were clustered around **2181-2184**, indicating price was not merely a one-tick print near the threshold but comfortably above it at the time checked.
- Querying Binance for the future settlement minute (16:00 UTC) returned an empty result at research time, which is expected because that candle had not occurred yet.

## Evidence directly stated by source

- Polymarket page rules: settle from Binance ETH/USDT 1m candle, 12:00 ET, final close, exact pair specified.
- Binance ticker endpoint: ETHUSDT price 2183.68000000 at fetch time.
- Binance 1m kline endpoint: last several candles around 07:30-07:34 UTC had closes in the 2181-2184 range.

## What is uncertain

- The actual settlement candle close at 12:00 ET / 16:00 UTC was still in the future during this run.
- Crypto can move sharply intra-day, so being above 2100 several hours before settlement does not by itself guarantee a Yes resolution.
- I did not obtain the Binance web UI candle directly through rendered HTML; the API is a direct Binance surface but not the exact UI surface cited in the rules.

## Why this source may matter

This is the most important evidence set because the market is a narrow, source-defined numeric contract. Exact source-of-truth mechanics and correct timezone conversion are central to assessing whether current pricing is efficient.

## Possible impact on the question

This source strongly supports the market's high Yes probability. If ETHUSDT is already ~4% above the strike with only hours remaining, a Yes outcome is naturally favored unless there is a material intraday selloff before the exact settlement minute.

## Reliability notes

- Binance API is a direct exchange-operated surface and therefore strong for contextual verification.
- Polymarket rules page is the contract-definition surface and therefore authoritative for resolution mechanics.
- Independence is limited because both points are about the same market mechanism rather than separate causal evidence streams, but that is acceptable here because this is primarily a source-defined price-threshold market.