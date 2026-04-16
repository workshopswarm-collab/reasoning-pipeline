---
type: source_note
case_key: case-20260415-89d9685e
dispatch_id: dispatch-case-20260415-89d9685e-20260415T181939Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: binance
topic: btc-usdt-resolution-and-spot-check
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-16 close above 72000?
driver: liquidity
date_created: 2026-04-15
source_name: Binance API and trading surface
source_type: primary_market_data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: [binance, btc, usdt]
related_drivers: [liquidity, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-89d9685e/researcher-analyses/2026-04-15/dispatch-case-20260415-89d9685e-20260415T181939Z/personas/catalyst-hunter.md]
tags: [binance, btcusdt, resolution-source, spot-check]
---

# Summary

This note captures the direct source-of-truth surface named by the market rules and a live spot check of BTC/USDT well above the 72,000 threshold roughly 24 hours before resolution.

## Key facts extracted

- The market rules specify Binance BTC/USDT with 1m candles as the governing source.
- A direct Binance API spot query on 2026-04-15 returned BTCUSDT price 74297.73.
- Binance exchange metadata confirms BTCUSDT is an active trading symbol on the venue and that price precision includes two decimals via tickSize 0.01.
- Recent 1-minute kline output shows BTCUSDT trading in the 74.25k-74.33k area during the spot check window.
- The assignment resolves at 2026-04-16 12:00 ET, which converts to 2026-04-16 16:00 UTC.

## Evidence directly stated by source

- Binance ticker endpoint returned: {"symbol":"BTCUSDT","price":"74297.73000000"}.
- Binance exchangeInfo for BTCUSDT returned status TRADING and PRICE_FILTER tickSize 0.01000000.
- Binance 1m klines returned recent closes including 74257.54, 74300.00, 74329.02, 74291.43, and 74297.65.

## What is uncertain

- The direct settlement candle is tomorrow's 12:00 ET candle, not today's spot price or today's nearby candles.
- Overnight macro, policy, or crypto-specific shocks could still move BTC/USDT more than 2,300 points lower before the settlement minute.
- I was not able to fetch a clean readable Binance webpage snapshot through the standard web fetcher, so this note relies on Binance public API endpoints plus the Polymarket rules text.

## Why this source may matter

The contract explicitly settles on Binance BTC/USDT, so Binance is the authoritative source rather than a general crypto price index or another exchange.

## Possible impact on the question

Because BTC/USDT is already ~3.2% above the threshold with less than a day to go, the default lean is Yes unless a meaningful negative catalyst hits before the settlement minute.

## Reliability notes

This is the highest-quality source available for this contract because it comes from the named venue and directly exposes the symbol, last price, and 1-minute kline structure relevant to settlement. The main limitation is temporal: it does not directly settle tomorrow's noon candle yet.