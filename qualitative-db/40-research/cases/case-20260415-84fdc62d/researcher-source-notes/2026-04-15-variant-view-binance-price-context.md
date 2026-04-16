---
type: source_note
case_key: case-20260415-84fdc62d
dispatch_id: dispatch-case-20260415-84fdc62d-20260415T125809Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-20
question: Will the Binance BTC/USDT 12:00 PM ET 1-minute candle close on 2026-04-20 above 70000?
driver: reliability
date_created: 2026-04-15
source_name: Binance API BTCUSDT spot price and recent kline context
source_type: exchange primary market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-84fdc62d/researcher-analyses/2026-04-15/dispatch-case-20260415-84fdc62d-20260415T125809Z/personas/variant-view.md]
tags: [binance, btcusdt, price, primary-data, timing]
---

# Summary

Primary Binance market data on April 15 showed BTC/USDT around 74.3k, meaning the contract strike sat roughly 6% below spot with about five days remaining. Recent daily candles indicate BTC has already been trading materially above 70k for most of the past week, though it remains volatile enough for sharp multi-thousand-dollar swings.

## Key facts extracted

- Binance API ticker returned BTCUSDT at 74,267.11 on April 15, 2026.
- Recent 15-minute candles around the fetch time were clustered around 74.2k-74.4k.
- Recent daily closes / highs / lows from late March to April 14 show:
  - Mar 31 close: 68,113.92
  - Apr 5 high: 70,351.46
  - Apr 6 close: 71,924.22
  - Apr 12 close: 74,417.99 after a low of 70,566.99
  - Apr 13 high: 76,038.00, close: 74,131.55
  - Apr 14 low: 73,514.00, close: 74,267.10
- Since April 6, daily closes have remained above 70,000 despite volatility.

## Evidence directly stated by source

- Direct Binance API response: {"symbol":"BTCUSDT","price":"74267.11000000"}
- Direct Binance API kline responses supplied recent OHLC values used above.

## What is uncertain

- These data do not directly settle the April 20 noon ET close.
- Daily candles are UTC-anchored and therefore only contextual for the specific ET-noon contract.
- Volatility between now and April 20 could still push BTC below 70k at the relevant minute.

## Why this source may matter

This is the closest available primary source to the eventual resolution source. It establishes that the market is currently comfortably above the strike and that Binance itself presently supports the broad bullish baseline.

## Possible impact on the question

Being ~4.3k above the strike with five days to go supports a high Yes probability, but the single-minute resolution design means the relevant question is whether a roughly 6% drawdown occurs by the contract timestamp.

## Reliability notes

High reliability for current and recent Binance pricing because this is direct exchange API data. Moderate limitation for the contract because current spot context is not the same as the specific future noon ET minute close.