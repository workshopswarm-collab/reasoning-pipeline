---
type: source_note
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: crypto
subdomain: exchange-market-data
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: Will the price of Ethereum be above $2,200 on April 17?
driver: reliability
date_created: 2026-04-16
source_name: Binance spot API recent ETHUSDT 1m klines and 24h ticker
source_type: exchange-api
source_url: https://api.binance.com/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=60
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.md]
tags: [source-note, binance, kline, ethusdt]
---

# Summary

A direct Binance spot API pull showed ETH/USDT recent 1-minute closes materially above 2200 on Apr. 16, with the last 60 one-minute closes ranging roughly from 2320.92 to 2343.74 and the latest sampled close at 2341.63. The 24h ticker showed a daily range of 2285.10 to 2385.61 and a 24h change of about -0.99%.

## Key facts extracted

- Recent sampled Binance ETH/USDT 1-minute closes were all above 2200.
- In the sampled last 60 minutes, close prices ranged from 2320.92 to 2343.74.
- Latest sampled close was 2341.63.
- Binance 24h high/low from the same direct exchange surface were 2385.61 / 2285.10.
- This leaves an approximately 85-point cushion above the 2200 threshold even versus the 24h low.

## Evidence directly stated by source

- The Binance spot kline endpoint returned one-minute candle arrays for ETHUSDT including open time, OHLC, and close time.
- The Binance 24h ticker endpoint returned priceChangePercent, highPrice, and lowPrice for ETHUSDT.

## What is uncertain

- This is not the final Apr. 17 noon ET candle, only a near-resolution-state snapshot.
- A broad crypto risk-off move before noon ET on Apr. 17 could still push ETH below 2200.

## Why this source may matter

It is the closest available direct source to the contract’s actual resolution surface and materially reduces uncertainty about current distance from the strike.

## Possible impact on the question

Because the contract resolves off a single Binance 1-minute close, current distance from strike matters a lot. With ETH trading well above 2200 shortly before resolution, the burden shifts to identifying a plausible near-term catalyst large enough to erase that cushion.

## Reliability notes

High reliability as a direct Binance market-data surface, though the exact final contract source is the Binance chart/display for the specified minute. API-vs-UI formatting differences seem low-risk here because the question is simply whether the close is above 2200, not a fine-grained value comparison.