---
type: source_note
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
analysis_date: 2026-04-13
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the price of Bitcoin be above $70,000 on April 15?
driver: operational-risk
date_created: 2026-04-13
source_name: Binance Spot API plus Polymarket market rules page
source_type: primary_and_contextual_market_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13T22:28:13.249000+00:00
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, polymarket, resolution-source, btc]
---

# Summary

This source note captures the direct settlement surface and the immediate price context for the April 15 BTC>$70k noon-ET market.

## Key facts extracted

- Binance spot API returned BTCUSDT last price 74,122.08 at 2026-04-13T18:28:13.249000-04:00.
- Binance server time confirms the exchange time surface is active and queryable.
- BTCUSDT is currently in TRADING status on Binance spot.
- Binance exchange metadata shows `PRICE_FILTER.tickSize` of 0.01, so settlement precision should naturally resolve to cents if the Polymarket rule uses Binance's displayed close value.
- Polymarket rules specify this market resolves on the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-15, using the candle's final `Close` price, and requires that close to be strictly higher than 70,000.
- Recent Binance daily data show BTC has closed above 70,000 on 5 of the last 7 completed daily candles in the fetched sample, and the most recent spot is materially above the threshold.

## Evidence directly stated by source

- Direct/authoritative settlement source: Binance BTCUSDT 1m candle close for 12:00 ET on Apr 15.
- Contract condition is strict inequality: the final close must be higher than 70,000; 70,000.00 exactly would be a No.
- Pair specificity matters: Binance BTC/USDT, not BTC/USD or another exchange.
- Timezone specificity matters: noon ET, not UTC noon.

## What is uncertain

- The direct API pulls used here are not the exact future 12:00 ET minute candle, so they only establish current context and mechanics, not settlement itself.
- Binance web UI language on the market page does not spell out daylight-saving translation, but ET on Apr 15, 2026 implies EDT (UTC-4).
- Short-horizon BTC volatility could still push price below 70,000 by the settlement minute.

## Why this source may matter

It is the governing settlement surface and the best available direct reference for both contract mechanics and current distance-from-threshold.

## Possible impact on the question

With spot around 74,122.08, BTC is roughly 4,122.08 above the threshold about 41.5 hours before resolution. That makes the base-rate question mostly about whether BTC typically gives back more than ~5.6% within that time window, not about requiring fresh upside.

## Reliability notes

- Binance is the explicit source of truth in the contract, so source-of-truth ambiguity is low once the ET/noon mapping is understood.
- Polymarket's rule page is contextual rather than authoritative for the actual price print, but it is authoritative for the contract wording viewed by traders.
- Evidence independence is only medium because both pieces revolve around the same market stack; I compensated by separately verifying exchange status, server time, current spot, and recent klines from Binance endpoints.
