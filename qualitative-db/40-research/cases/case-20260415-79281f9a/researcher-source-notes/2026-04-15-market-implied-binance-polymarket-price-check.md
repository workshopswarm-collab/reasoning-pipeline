---
type: source_note
case_key: case-20260415-79281f9a
dispatch_id: dispatch-case-20260415-79281f9a-20260415T202526Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-79281f9a | market-implied
question: Will the price of Bitcoin be above $68,000 on April 20?
driver:
date_created: 2026-04-15
source_name: Binance BTCUSDT API and Polymarket contract page
source_type: primary_market_and_resolution_source
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: market-implied
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-79281f9a/researcher-analyses/2026-04-15/dispatch-case-20260415-79281f9a-20260415T202526Z/personas/market-implied.md]
tags: [source-note, binance, polymarket, btc]
---

# Summary

This note records the direct contract and price-level checks most relevant to the case. The contract resolves using the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20, 2026, specifically the final Close price for that minute. On 2026-04-15, Binance spot BTCUSDT was approximately 74.6k, well above the 68k strike.

## Key facts extracted

- Polymarket contract page states the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 20 has a final Close above 68,000.
- The listed source of truth is Binance BTC/USDT with 1m Candles selected.
- Binance API spot price check returned BTCUSDT at 74,626.57 on 2026-04-15.
- Binance 1-minute klines check around the observation time showed closes around 74.54k-74.64k.
- Polymarket market page displayed the 68,000 line at roughly 97% Yes, consistent with the assignment current_price 0.9715.

## Evidence directly stated by source

- Contract wording directly specifies all material conditions: exchange, pair, candle interval, relevant minute, timezone, and close-price comparison threshold.
- Binance market data directly states current BTCUSDT price and recent 1-minute candle closes.

## What is uncertain

- Spot price on April 15 does not directly settle price on April 20 noon ET.
- The market could still move materially over ~4.5 days.
- Binance UI and API are not literally the same presentation layer, though they refer to the same BTCUSDT market and 1-minute candle series.

## Why this source may matter

This is the governing resolution source plus a same-venue current price check. It is the cleanest way to assess whether the market’s extreme probability is directionally justified and whether contract interpretation risk is low or high.

## Possible impact on the question

Because Binance BTCUSDT is already roughly 6.6k above the strike, the market only needs BTC to avoid a drawdown of roughly 8.9% by the relevant minute. That strongly supports a high Yes probability, though not necessarily one as high as 97% absent stronger path/stability evidence.

## Reliability notes

- Resolution-source quality is high because Polymarket explicitly names Binance BTC/USDT 1-minute candle close as the governing source of truth.
- Current-price evidence quality is high for present state but only medium for forecasting several days ahead.
- Binance and Polymarket are not fully independent sources; they are linked by contract design. Independence improves when paired with an outside contextual source.