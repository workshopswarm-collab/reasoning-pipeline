---
type: source_note
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page + Binance BTCUSDT API spot data
source_type: market rules plus exchange data
source_url: https://polymarket.com/event/bitcoin-above-on-april-16
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, binance, resolution-source, timing, catalyst]
---

# Summary

This source note combines the contract language visible on the Polymarket event page with direct Binance BTCUSDT spot-market data pulled from Binance's public API. Together they establish the governing source of truth, the relevant timestamp, and the current distance of spot price from the $72,000 threshold.

## Key facts extracted

- Polymarket states the market resolves **Yes** if the Binance BTC/USDT **1 minute candle for 12:00 ET on April 16, 2026** has a final **Close** price above 72,000.
- The source-of-truth surface is Binance BTC/USDT with **1m Candles**; other exchanges and pairs do not count.
- Because the date is in April and ET is on EDT, the relevant candle timestamp is **16:00 UTC**.
- Binance spot API data on 2026-04-14 showed BTCUSDT around **74.7k** at the time checked.
- The Binance **16:00 UTC / 12:00 ET** one-minute candle on 2026-04-14 closed at **75,356.48**, which is already comfortably above the 72k line and provides a same-time-of-day reference point.
- Recent Binance daily candles show BTC closed:
  - 2026-04-12: **70,740.98**
  - 2026-04-13: **74,417.99**
  - 2026-04-14 intraday check: about **74,716.75**
- In the prior 72 hours sampled from hourly Binance data, BTCUSDT traded above 72k in **34 of 72 hours**, with a high around **76,038** and low around **70,505.88**.

## Evidence directly stated by source

From Polymarket rules:
- Resolution depends on the Binance BTC/USDT **1-minute candle** for **12:00 ET** on the specified date.
- The deciding field is the candle's final **Close** price.
- Price precision is determined by the source.

From Binance API market data:
- Current BTCUSDT spot price is mid-74k on 2026-04-14.
- Same-time reference candle on 2026-04-14 16:00 UTC closed materially above 72k.

## What is uncertain

- The market resolves on a single minute close, so even if BTC trades above 72k most of the time, a sharp intraday selloff into the exact resolution minute could still flip the result.
- Binance API spot checks are current-state evidence, not a guarantee about the April 16 noon ET close.

## Why this source may matter

This is the most decision-relevant source set because it directly defines the contract mechanics and provides the live exchange reference that the contract will use. For a narrow time-specific crypto threshold market, this matters more than broader narrative commentary.

## Possible impact on the question

These sources support a high probability of **Yes** because the contract only needs one specific Binance minute close above 72k and current spot is already several thousand dollars above that level. They also highlight the main remaining risk: a fast drawdown into exactly the noon ET minute.

## Reliability notes

- Polymarket rules are authoritative for contract interpretation.
- Binance is the explicit settlement source, so direct Binance data is the highest-value market evidence available short of the final settlement print itself.
- Evidence independence is moderate rather than high because the pricing evidence and settlement source both point back to Binance, but that is acceptable here because Binance is explicitly the governing source of truth.
- Operationally, the main residual risk is exchange/source handling or single-minute timing sensitivity rather than uncertainty about which data source counts.
