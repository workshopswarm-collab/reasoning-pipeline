---
type: source_note
case_key: case-20260415-47643da0
dispatch_id: dispatch-case-20260415-47643da0-20260415T010752Z
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket rules page and Binance API spot/klines
source_type: primary_plus_direct_market_data
source_url: https://polymarket.com/event/bitcoin-above-on-april-17 ; https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=1000
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: variant-view
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-47643da0/researcher-analyses/2026-04-15/dispatch-case-20260415-47643da0-20260415T010752Z/personas/variant-view.md]
tags: [polymarket, binance, settlement, btc-price, direct-evidence]
---

# Summary

This source bundle establishes both the contract mechanics and the immediate price context. Polymarket states the market resolves from the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr. 17, using the final Close value. Binance API checks on Apr. 14 evening ET / Apr. 15 UTC show BTC/USDT trading around 74.65k, with recent 1-minute candles well above 72k.

## Key facts extracted

- Governing source of truth is Binance BTC/USDT, specifically the 1-minute candle labeled 12:00 ET on Apr. 17, 2026, and the deciding field is the final Close.
- Polymarket page displayed the 72,000 line near 84-85% implied probability at fetch time.
- Binance spot API returned BTCUSDT price of 74649.66 at the time checked.
- Binance 1-minute klines over the latest 1,000 minutes had last close around 74665.88, minimum close 73857.55, maximum close 75986.03, and zero closes below 72000.
- Recent 72 hourly closes implied BTC was about 3.6% above the 72k threshold at check time.

## Evidence directly stated by source

- Polymarket directly states: resolve Yes if the Binance 1 minute candle for BTC/USDT at 12:00 ET on the specified date has a final Close price higher than the threshold.
- Binance API directly states current BTCUSDT spot/close values and recent minute-candle closes.

## What is uncertain

- Current spot context is not the settlement print; the relevant value is only the specific Apr. 17 12:00 ET candle close.
- Short-horizon crypto volatility could still move BTC below 72k by settlement.
- Exchange-specific microstructure or a sharp market shock could matter even if broader market consensus stays bullish.

## Why this source may matter

It is the core direct evidence set for this case: one source defines the contract, the other is the actual exchange surface whose print will settle it.

## Possible impact on the question

These sources support a high-probability Yes baseline, but also highlight the main neglected variant mechanism: the market is not asking whether BTC stays generally strong, but whether one exact Binance 1-minute close at a specific timezone-adjusted timestamp clears 72k.

## Reliability notes

- Polymarket rules page is authoritative for contract interpretation but not itself the settlement feed.
- Binance API is direct exchange data and highly relevant, but this check was not the final settlement timestamp.
- Independence is only medium because both items are part of the same market stack rather than fully separate informational channels.