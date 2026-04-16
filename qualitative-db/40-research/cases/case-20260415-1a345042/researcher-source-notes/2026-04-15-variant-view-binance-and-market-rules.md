---
type: source_note
case_key: case-20260415-1a345042
dispatch_id: dispatch-case-20260415-1a345042-20260415T223206Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-1a345042 | variant-view
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-21 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market rules page and Binance BTCUSDT API
type: source_note
source_type: primary-plus-direct-context
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-1a345042/researcher-analyses/2026-04-15/dispatch-case-20260415-1a345042-20260415T223206Z/personas/variant-view.md]
tags: [market-rules, binance, btc, resolution-mechanics]
---

# Summary

The market resolves off the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-21, specifically its final Close value, not off any broader daily close, other exchange, or other pair. Current Binance spot context shows BTC/USDT at roughly 75002 on 2026-04-15, meaning the market is asking whether BTC can remain only modestly above a level already exceeded by about 4.2% over the next six days.

## Key facts extracted

- Polymarket rules specify a Yes resolution if the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 21 has a final Close above 72000.
- Resolution source is Binance BTC/USDT with 1m candles selected.
- Binance ticker API returned BTCUSDT price 75002.22 on 2026-04-15 fetch.
- Binance recent daily kline data shows BTC had already traded above 72000 multiple times in the most recent week and closed 75002.22 on the latest daily bar returned.
- Recent daily klines show meaningful realized volatility, including drops into the high-60s/low-70s before recovering into the mid-70s.

## Evidence directly stated by source

- The exact contract mechanic is exchange-specific, pair-specific, timeframe-specific, and minute-close-specific.
- Binance API output directly reports recent BTCUSDT price history and current quoted price.

## What is uncertain

- The Polymarket webpage is not itself the final settlement event; actual settlement depends on the Binance candle as observed at resolution time.
- Daily klines are contextual only and cannot directly answer the noon ET minute-close condition.
- A six-day crypto window remains long enough for a macro or crypto-specific shock to move BTC below 72000 by the relevant minute.

## Why this source may matter

It is the cleanest combination of contract interpretation plus direct exchange context. It establishes both what counts and the current distance from the threshold.

## Possible impact on the question

This source set supports a bullish baseline because spot is currently above threshold, but it also supports a variant caution because the actual contract is narrower than a simple “BTC is above 72k now” claim. A single weak intraday or risk-off move at the wrong time would be enough for No.

## Reliability notes

- Polymarket rules page is the governing market description but should be treated as a contract-summary surface rather than the actual future settlement observation.
- Binance API is a direct source for the relevant exchange/pair and is more authoritative for price context than third-party aggregators.
- Independence between these two is medium: they are different surfaces, but the contract explicitly delegates to Binance as source of truth.