---
type: source_note
case_key: case-20260407-be55ad2f
dispatch_id: dispatch-case-20260407-be55ad2f-20260407T193635Z
analysis_date: 2026-04-07
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: btc
topic: case-20260407-be55ad2f | risk-manager
question: Will the Binance BTC/USDT 1 minute candle for 12:00 ET on 2026-04-08 close above 66000?
driver: operational-risk
date_created: 2026-04-07T19:39:30Z
source_name: Binance Spot API market data docs and live BTCUSDT endpoints
source_type: primary
source_url: https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints
source_date: 2026-04-07
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260407-be55ad2f/researcher-analyses/2026-04-07/dispatch-case-20260407-be55ad2f-20260407T193635Z/personas/risk-manager.md]
tags: [binance, resolution-source, candle-definition, timezone]
---

# Summary

Binance's own spot market-data documentation confirms that klines are identified by their open time and that the `timeZone` parameter defaults to UTC unless explicitly overridden. That matters because the Polymarket contract specifies the Binance BTC/USDT 1-minute candle for `12:00` in ET, not simply noon UTC. A direct live endpoint check also showed the current BTCUSDT spot price around 68.5k on 2026-04-07, comfortably above the 66k strike, but the actual resolving candle has not occurred yet.

## Key facts extracted

- Binance spot docs expose both `/api/v3/klines` and `/api/v3/uiKlines`.
- Binance documents that `Klines are uniquely identified by their open time`.
- Binance documents a `timeZone` parameter for kline queries, with default `0 (UTC)`.
- Binance documents 1-minute intervals as valid.
- Direct API query to `https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT` returned `68509.18000000` on 2026-04-07T19:39Z.
- Direct API query for the future resolving timestamp (`startTime=1775664000000`, which is 2026-04-08 12:00 ET / 16:00 UTC) returned an empty array on 2026-04-07, confirming the candle had not yet printed.

## Evidence directly stated by source

- The docs explicitly state that the kline/candlestick bars are for a symbol and are uniquely identified by open time.
- The docs explicitly state that `timeZone` is optional and defaults to UTC, which means ET alignment must be handled deliberately rather than assumed from exchange server time.
- The docs explicitly show `1m` as a supported interval.

## What is uncertain

- The public docs do not themselves settle whether Polymarket resolvers will use a direct API pull with `timeZone=-4` or the Binance web UI candle display, only that the Binance source of truth is the Binance BTC/USDT 1m candle.
- The exact decimal precision visible in the Binance UI at settlement time still needs a final manual check at resolution.
- A direct pre-resolution API check cannot provide the future closing print.

## Why this source may matter

This is the governing mechanics source for how Binance defines and retrieves the candle underlying the market. It directly addresses the assignment's required checks on exchange timezone, candle time definition, and exact close-value handling.

## Possible impact on the question

The source reduces mechanical ambiguity: the relevant candle should be the one opened at 12:00 ET, and ET must be translated correctly because Binance kline defaults are UTC unless overridden. It does not by itself answer the market direction, but it supports a cleaner interpretation of what would invalidate or confirm a Yes outcome.

## Reliability notes

This is a high-credibility primary source because it is Binance's own API documentation plus live Binance API responses. Evidence independence is limited because both pieces are Binance-controlled, but that is acceptable here because Binance is also the contract's governing source of truth.