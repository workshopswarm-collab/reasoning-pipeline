---
type: source_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: spot-market-resolution
entity: ethereum
topic: case-20260409-21554cf3 | base-rate
question: Will the Binance ETH/USDT 1-minute candle for 2026-04-09 12:00 ET close above 2100?
driver: operational-risk
date_created: 2026-04-09
source_name: Binance spot market data docs + live ETHUSDT price endpoints + Polymarket rules
source_type: primary+contextual
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/base-rate.md]
tags: [binance, ethusdt, resolution, timezone, kline]
---

# Summary

This note captures the governing resolution mechanics and a direct live price check relevant to the market. Binance's market-data docs state that `GET /api/v3/klines` and `GET /api/v3/uiKlines` identify candles by open time, support a `timeZone` parameter for interval interpretation, but always interpret `startTime` and `endTime` in UTC. A live Binance ticker endpoint returned ETHUSDT at 2183.69 during this run, putting spot price meaningfully above the 2100 resolution threshold before the noon ET observation window.

## Key facts extracted

- Polymarket rules say this market resolves from the Binance ETH/USDT 1-minute candle for `12:00` in ET on 2026-04-09, using the candle's final `Close` price.
- Binance docs say klines are uniquely identified by their open time.
- Binance docs say `timeZone` changes interval interpretation, but `startTime` and `endTime` are always interpreted in UTC.
- 2026-04-09 12:00 ET converts to 2026-04-09 16:00 UTC.
- During this run, Binance ticker endpoint `GET /api/v3/ticker/price?symbol=ETHUSDT` returned `2183.69000000`.
- Attempts to query the future 16:00 UTC 1-minute kline at run time returned empty arrays, which is expected because the resolution minute had not occurred yet.

## Evidence directly stated by source

- Binance docs directly state the kline endpoint semantics, including open-time identity and UTC handling for request timestamps.
- Binance live ticker endpoint directly stated the current ETHUSDT spot price at the time of checking.
- Polymarket rules directly stated the governing resolution surface and the exact threshold logic.

## What is uncertain

- The Binance website UI may present the candle directly, but the final visible noon ET close was not yet available at run time because the market had not reached resolution time.
- The live ticker is not itself the settlement source; it is contextual evidence about current spot level.
- Intraday crypto volatility between roughly 03:34 ET and 12:00 ET could still push ETH below 2100 by the relevant minute close.

## Why this source may matter

It defines the exact operational mapping from the market's ET wording to Binance's kline mechanics and establishes that ETH was trading with an ~83.69 USDT cushion above the threshold during the research window.

## Possible impact on the question

This source supports a high-but-not-certain probability of YES: ETH was already above the line by nearly 4%, but the market still depends on the exact 12:00 ET / 16:00 UTC 1-minute Binance close rather than current spot.

## Reliability notes

- Source quality is high for contract mechanics because Binance docs and Polymarket rules are direct primary sources.
- Evidence independence is only medium because both mechanics and live price are Binance-linked rather than independent reporting.
- Operational-risk remains relevant because exchange UI/API behavior and exact candle interpretation can matter in narrow-resolution markets.