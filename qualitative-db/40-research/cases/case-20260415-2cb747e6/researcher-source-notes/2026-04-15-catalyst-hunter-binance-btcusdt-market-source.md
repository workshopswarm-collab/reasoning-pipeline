---
type: source_note
case_key: case-20260415-2cb747e6
dispatch_id: dispatch-case-20260415-2cb747e6-20260415T122916Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-16 close above 72000?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance spot/API market data and contract resolution source
source_type: exchange_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: intraday
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, resolution-source, intraday-price]
---

# Summary

Binance is the governing source of truth for this contract. Direct API checks on 2026-04-15 show BTC/USDT trading around 74.2k, comfortably above the 72k strike roughly 24 hours before the noon ET resolution candle.

## Key facts extracted

- Binance ticker endpoint returned `{"symbol":"BTCUSDT","price":"74231.14000000"}` during this run.
- Binance 24h ticker stats returned `lastPrice 74228.29000000`, `highPrice 76038.00000000`, `lowPrice 73514.00000000`, and `priceChangePercent -0.167`.
- Recent 1h candles for 2026-04-15 show BTC/USDT holding above 73.5k throughout the sampled 24h range and trading back above 74.2k by the time of the check.
- The most recent sampled 1m candles also printed closes around 74.18k-74.23k.

## Evidence directly stated by source

- Current Binance spot price is above 72,000 by more than 2,200 points.
- Recent intraday low in the checked 24h stats was 73,514, still above 72,000.
- Binance supports the exact resolution instrument and candle framework referenced by Polymarket rules.

## What is uncertain

- This source does not settle the market yet because the resolution candle is specifically the 12:00 ET one-minute candle on 2026-04-16, not the current spot price on 2026-04-15.
- A sharp overnight or morning selloff could still move BTC/USDT below the strike by the relevant minute close.
- API availability now does not guarantee a totally frictionless settlement workflow tomorrow, though Binance remains the stated source of truth.

## Why this source may matter

This is both the most important market-state source and the governing resolution source. It directly answers the relevant exchange/pair question and removes cross-exchange basis ambiguity.

## Possible impact on the question

Because Binance BTC/USDT is already materially above the strike and even the checked 24h low stayed above 72k, the base rate strongly favors Yes unless a meaningful downside catalyst hits before noon ET on April 16.

## Reliability notes

- Highest relevance because Polymarket explicitly names Binance BTC/USDT 1m candle close as the resolution source.
- Exchange API output is direct and machine-readable.
- Remaining risk is timing/path risk, not source relevance.