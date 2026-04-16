---
type: source_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: ethereum
topic: ETH/USDT noon ET Binance candle resolution check
question: Will the Binance ETH/USDT 1-minute candle for 12:00 ET on 2026-04-17 close above 2200?
driver: reliability
date_created: 2026-04-16
source_name: Polymarket rules page + Binance spot API market data docs and live endpoints
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/ethereum-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/base-rate.md]
tags: [source-note, polymarket, binance, resolution]
---

# Summary

This source note checks the contract mechanics and current price context for the ETH > 2200 market resolving on 2026-04-17 at 12:00 ET.

## Key facts extracted

- Polymarket states the market resolves from the Binance ETH/USDT 1-minute candle for 12:00 in the ET timezone, using the final Close price.
- The contract is specifically about Binance ETH/USDT, not other exchanges or other pairs.
- Binance Spot API docs state `/api/v3/klines` returns candlestick bars, including close price, and supports `1m` interval.
- Binance docs also state kline intervals can be interpreted in a supplied timezone, while startTime/endTime are UTC.
- Live Binance spot endpoints on 2026-04-16 showed ETHUSDT trading around 2343-2344, comfortably above 2200.
- A timing sanity check for 2026-04-16 12:00 ET mapped to 16:00 UTC and returned a single 1-minute ETHUSDT kline with close 2340.51, confirming the practical mechanics for querying the target candle window.
- Recent daily closes from Binance show ETH has closed above 2200 on 8 of the last 30 daily candles (~26.7%), but the market is not asking about a generic day-close base rate; it is asking about a noon-next-day level conditional on current spot near 2344.

## Evidence directly stated by source

- Polymarket rules text: market resolves Yes if the Binance 1-minute candle for ETH/USDT at 12:00 ET on the specified date has a final Close price higher than 2200.
- Binance docs: `/api/v3/klines` provides kline/candlestick data and includes close price in the response.

## What is uncertain

- Polymarket references the Binance web chart as the resolution source; API output should match the same underlying exchange data, but the web UI is still the formal governing source of truth if any display discrepancy appears.
- A large crypto move between now and the noon ET resolution window could still flip the outcome despite current spot being well above threshold.

## Why this source may matter

It establishes both the exact settlement mechanics and the current factual buffer above the threshold. For this market, timing and source-of-truth interpretation matter almost as much as directional price view.

## Possible impact on the question

The note strongly supports a Yes leaning because the governing source uses a straightforward observable Binance ETH/USDT 1-minute close and current spot is roughly 6% above the 2200 threshold less than a day before resolution.

## Reliability notes

- Primary settlement mechanics come from Polymarket’s own rules page, which is authoritative for contract interpretation.
- Binance API docs are authoritative for understanding how kline data is structured.
- Live Binance API endpoint responses are direct exchange data but are still a contextual verification layer relative to the formally cited web chart resolution surface.
- Evidence independence is moderate rather than high because both key factual layers ultimately depend on Binance data.