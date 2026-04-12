---
type: source_note
case_key: case-20260409-746679d3
dispatch_id: dispatch-case-20260409-746679d3-20260409T205932Z
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: market-structure
entity: ethereum
topic: case-20260409-746679d3 | base-rate
question: Will the price of Ethereum be above $2,100 on April 10?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance spot API plus Polymarket rules page
source_type: primary-plus-contract-context
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=5
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-746679d3/researcher-analyses/2026-04-09/dispatch-case-20260409-746679d3-20260409T205932Z/personas/base-rate.md]
tags: [binance, polymarket, resolution, klines, ethusdt]
---

# Summary

The governing settlement surface is Polymarket's market rules pointing to Binance ETH/USDT 1-minute candles, and the strongest direct verification surface available in-run is Binance's public spot API for ETHUSDT klines, exchange metadata, and server time.

## Key facts extracted

- Polymarket rules say the market resolves "Yes" if the Binance ETH/USDT 1-minute candle for 12:00 ET on April 10 has a final close above 2100.
- Binance spot API `exchangeInfo` reports exchange timezone as `UTC` and `serverTime` in Unix milliseconds.
- Binance spot API `klines` for `ETHUSDT` returns arrays with open time and close time in UTC milliseconds, with the close price in the fifth position.
- Current spot ticker during the check was about 2213.08, already above the 2100 threshold by roughly $113.
- Querying the exact target minute converted from 2026-04-10 12:00 ET to 2026-04-10 16:00 UTC returned no data yet, which is consistent with the event still being in the future and also validates the ET-to-UTC conversion logic.

## Evidence directly stated by source

- `exchangeInfo`: timezone is UTC.
- `time`: Binance server time is provided directly in Unix milliseconds.
- `klines`: 1-minute bars include explicit open time, close time, and final close.
- Recent 1-minute ETHUSDT bars showed closes around 2211-2214 at the time checked.
- Polymarket rules explicitly designate Binance ETH/USDT 1-minute candle close as the source of truth.

## What is uncertain

- The Binance website chart UI wording could differ slightly from API field naming, though the underlying close values should align.
- Polymarket rules say "12:00 in the ET timezone"; the operational interpretation is that the relevant minute begins at 12:00:00 ET and ends at 12:00:59 ET, with the final close recorded at the minute end. That is very likely but still worth stating explicitly.

## Why this source may matter

This is the direct settlement and verification layer. For a narrow, time-specific crypto price market, contract mechanics and timestamp interpretation matter almost as much as the spot price level itself.

## Possible impact on the question

Because ETHUSDT is already comfortably above 2100 and the governing source is a single Binance minute close, the main live risk is not broad narrative error but last-day price movement or a timestamp/interpretation mismatch. The source strongly supports a high-probability Yes baseline while also clarifying the specific operational checks needed.

## Reliability notes

- Binance API is the most authoritative accessible source checked in-run because the market explicitly keys off Binance ETH/USDT pricing.
- Polymarket rules are authoritative for contract interpretation but not for the price value itself.
- Evidence independence is limited because both the website chart and API depend on Binance data, so secondary sources are mainly contextual rather than independent settlement evidence.