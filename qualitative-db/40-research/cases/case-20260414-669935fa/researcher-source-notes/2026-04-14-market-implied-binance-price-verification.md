---
type: source_note
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260414-669935fa | market-implied
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-14
source_name: Binance BTCUSDT klines API verification
source_type: exchange market data / contextual but contract-aligned verification
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=200
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: high
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/market-implied.md]
tags: [binance, klines, verification, btc, price]
---

# Summary

A direct verification pass against Binance BTCUSDT kline data shows the qualifying week already included a price above $76,000: the 2026-04-14 14:00 UTC hourly candle had a high of 76,038. Because the Polymarket contract resolves on any Binance 1-minute high >= 76,000 during Apr 13-19 ET, this strongly supports a Yes resolution.

## Key facts extracted

- Binance BTCUSDT 1-hour kline API returned recent hourly data through Apr 14, 2026.
- In that dataset, the candle beginning 2026-04-14 14:00 UTC showed a high of `76038.00`.
- The same verification pass found the maximum high since the contract window start was `76038.0` and the low was `70566.99`.
- Current Coinbase BTC spot at verification time was about `74621.115`, showing spot had since moved back below $76k even though the threshold had already been hit intraperiod.

## Evidence directly stated by source

- Binance hourly kline print: `2026-04-14T14:00:00 ... high 76038.00000000`
- Computed summary since the start of the relevant window: `since_start_high 76038.0`

## What is uncertain

- The contract specifies 1-minute highs, while this verification used 1-hour klines; however, an hourly high above 76,000 implies at least one included trade and therefore at least one underlying 1-minute candle high at or above that level within the hour.
- This note did not independently archive the exact first 1-minute candle or settlement screenshot.

## Why this source may matter

It is an extra verification pass aligned to the contract's governing exchange. It materially reduces residual doubt that the market price near 100% is stale or purely speculative.

## Possible impact on the question

Given a documented Binance high above the threshold during the valid time window, the market appears correctly priced as essentially certain Yes absent exchange-data correction or contract-administration anomaly.

## Reliability notes

High relevance because it uses the exact exchange/pair named in the rules. Independence from the market page is moderate rather than high because both point back to Binance as the governing source, but it is still a genuine separate data check. Main limitation: hourly rather than 1-minute granularity.