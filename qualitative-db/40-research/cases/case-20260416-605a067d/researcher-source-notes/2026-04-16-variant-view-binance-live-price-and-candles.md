---
type: source_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: threshold-close-markets
entity: ethereum
topic: Binance ETHUSDT live price and recent candle context
question: Will the Binance ETH/USDT 12:00 ET 1-minute candle on April 17 close above 2200?
driver: reliability
date_created: 2026-04-16
source_name: Binance public API ticker and kline endpoints
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/variant-view.md
tags: [source-note, binance, ethereum, kline, ticker]
---

# Summary

Binance public market data showed ETH/USDT around 2297.57-2297.88 during the research window, with recent 1-minute highs up to 2345.68 over the last hour sample and 1-hour highs up to 2385.61 over the last 48-hour sample.

## Key facts extracted

- Binance ticker returned ETHUSDT price 2297.57-2297.88 during the research run.
- Recent 1-minute klines for the last 60 minutes had a maximum high of 2345.68, minimum low of 2285.10, and last close of 2297.57.
- Recent 48 hourly klines had a maximum high of 2385.61, minimum low of 2285.10, and last close of 2297.57.
- The market is therefore currently about 4.4% above the 2200 threshold.
- Recent realized volatility is not trivial: within the sampled 48-hour context, ETH traded roughly a 100-point range.

## Evidence directly stated by source

- Direct primary exchange price and candle data from Binance API.
- Direct evidence that ETH is currently above 2200 by a meaningful margin, but not by an overwhelming distance given crypto volatility.

## What is uncertain

- These are not yet the governing April 17 12:00 ET candle values.
- The API sample used for context is limited to recent intervals; it does not prove what the specific resolution candle will be.
- Binance API data is a strong proxy for the exchange state, but the contract wording points to the Binance trading interface candle as the ultimate source of truth.

## Why this source may matter

This is the strongest direct market-state evidence available before resolution. It shows the line is already in-the-money by nearly $100, which is the main reason the market is heavily priced toward Yes.

## Possible impact on the question

This source supports a high Yes probability. It also supports the variant caveat: because settlement is a single minute-close tomorrow rather than “trades above 2200 anytime,” current price above 2200 does not eliminate overnight selloff risk.

## Reliability notes

High reliability and high recency for current market state. Not by itself sufficient for final settlement because timing and exact governing candle still matter.