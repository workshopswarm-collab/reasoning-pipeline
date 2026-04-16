---
type: source_note
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-15
source_name: Binance public price and kline endpoints plus ET-to-UTC timing check
source_type: exchange API / timing verification
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415-1cbf2a82-20260415T144104Z/personas/variant-view.md]
tags: [binance, api, spot, klines, timezone]
---

# Summary

This source note records the direct exchange context used for the estimate. Binance public endpoints returned BTCUSDT spot around 73,988.94 at time of review and recent 1-minute candles clustered near 74k. A separate timezone conversion verified that the relevant settlement minute is 2026-04-17 12:00 ET = 2026-04-17 16:00 UTC.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price 73,988.94 at review time.
- Recent Binance 1-minute klines showed trading in the high-73k / low-74k range, confirming BTC was already above the 72k strike by roughly 2.7% at review time.
- The settlement candle specified in ET converts to 16:00 UTC on April 17, 2026.
- Because settlement uses a single 1-minute candle Close, the key practical question is whether BTC can remain above 72k at that specific minute, not whether it trades above 72k at any point before then.

## Evidence directly stated by source

- Binance API directly returned the current BTCUSDT price.
- Binance API directly returned recent 1-minute kline data.
- Timezone conversion directly established the UTC timestamp corresponding to noon ET on April 17.

## What is uncertain

- Current spot price does not guarantee the future settlement minute close.
- This note does not establish realized volatility or expected path distribution by itself.
- Public Binance API availability today does not remove residual operational / display risk at settlement time, though the contract points to the Binance trading interface rather than an API endpoint.

## Why this source may matter

It provides the primary non-Polymarket evidence: BTC is currently above the strike, but not by an extreme margin for crypto over a roughly two-day horizon. That opens room for a variant view that the crowd may be slightly overconfident at 84% because the event is a precise one-minute close, not a broad directional monthly call.

## Possible impact on the question

This source supports a bullish baseline but also limits confidence. Being only about 2.7% above strike with nearly two days left is supportive of Yes, but not obviously supportive of an 84% probability once short-horizon volatility and one-minute-close mechanics are respected.

## Reliability notes

High reliability for current exchange price context and timing conversion. It is a direct source for current BTCUSDT state, though still only contextual for a future settlement minute.