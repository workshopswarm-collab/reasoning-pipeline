---
type: source_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: btc-usdt-price-level-into-april-20
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT API and market page
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
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
tags: [source-note, binance, btc, price-levels, resolution-source]
---

# Summary

Binance is the governing source of truth for this contract, and current BTC/USDT levels are materially above the 70,000 threshold with five days remaining until the Apr. 20 noon ET resolution minute.

## Key facts extracted

- Polymarket rules specify this market resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on Apr. 20, using the final `Close` price.
- Binance spot API returned BTCUSDT last price `74676.79` on 2026-04-15 during this research run.
- Binance 5-minute average price endpoint returned `74686.08076125`, corroborating spot trading in the mid-74k range.
- Recent daily Binance closes show BTC above 70k on 9 of the last 10 daily closes and above 74k on Apr. 13-15 snapshots gathered in-run.
- From the latest sampled close near 74.6k, BTC would need to fall roughly 6.2% by the relevant Apr. 20 noon ET minute for this market to resolve No.

## Evidence directly stated by source

- Binance API directly states current BTCUSDT spot price and rolling average price.
- Binance daily klines directly state recent open/high/low/close values, including several consecutive days above 70k.
- Polymarket rules directly state Binance BTC/USDT 1-minute candle close is the settlement surface.

## What is uncertain

- The source does not and cannot tell us the exact Apr. 20 noon ET close in advance.
- Web fetch of the Binance trading page itself was not extractable, so verification used Binance public API endpoints rather than rendered page candles.
- Intraday volatility could still produce a temporary or sustained drop below 70k before settlement.

## Why this source may matter

This is the closest thing to an authoritative source before resolution because the contract explicitly names Binance BTC/USDT as the settlement source.

## Possible impact on the question

Current direct exchange data supports a high Yes probability because the threshold sits several thousand dollars below the current market and would require a nontrivial drawdown within a short window.

## Reliability notes

High relevance and high authority for contract interpretation because the market explicitly settles to Binance. Main caveat is that the contract references the rendered 1-minute candle close on the exchange UI; API spot and kline endpoints are strong but still slightly indirect pre-resolution proxies for that exact future displayed candle.