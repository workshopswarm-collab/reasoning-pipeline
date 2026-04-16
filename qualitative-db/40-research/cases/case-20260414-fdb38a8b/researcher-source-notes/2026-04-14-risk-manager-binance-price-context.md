---
type: source_note
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: btc-price
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 PM ET 1-minute candle close on 2026-04-17 be above 72000?
driver: reliability
date_created: 2026-04-14
source_name: Binance public API spot price, 1m klines, and 24h ticker
source_type: exchange API / primary market data
source_url: https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: mildly supportive
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [bitcoin, btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-fdb38a8b/researcher-analyses/2026-04-14/dispatch-case-20260414-fdb38a8b-20260414T180238Z/personas/risk-manager.md]
tags: [binance, primary-market-data, btcusdt, 1m-candles, date-sensitive]
---

# Summary

Binance primary market data shows BTC/USDT currently trading around 74.76k-74.78k, well above the 72k threshold, with a 24h range of roughly 72.05k to 76.04k and a positive 24h change of about +3.6%.

## Key facts extracted

- Spot price query returned BTCUSDT around 74,781.32.
- Recent 1-minute klines were closing in the 74,758-74,795 area at capture time.
- Binance 24h ticker reported:
  - lastPrice: 74,758.49
  - openPrice: 72,160.65
  - lowPrice: 72,053.78
  - highPrice: 76,038.00
  - priceChangePercent: +3.600%
- The 24h low remained slightly above 72,000, but only by a narrow margin (~53.78).

## Evidence directly stated by source

- Public Binance API spot price and recent klines provide direct exchange-level evidence of where the relevant market is trading now.
- The 24h ticker gives a recent realized range showing both upside cushion above 72k and the proximity of the recent floor to the threshold.

## What is uncertain

- This source does not answer whether BTC will still be above 72k specifically at noon ET on April 17.
- The current cushion above threshold (~3.8%-3.9%) is meaningful but not large enough to eliminate ordinary crypto volatility risk over the next ~2.9 days.
- The API endpoints are not the exact front-end candle view named in the contract, though they are Binance primary data and directionally aligned with it.

## Why this source may matter

This is the strongest direct evidence for the current state of the relevant instrument and venue. It materially supports a Yes lean because the contract asks about Binance BTC/USDT and the current Binance price is already above threshold.

## Possible impact on the question

The data supports a majority Yes probability, but from a risk-manager perspective it also highlights fragility: the market can fail on an otherwise bullish setup if BTC gives back only a few percent or briefly trades below threshold into the exact noon ET minute.

## Reliability notes

High-quality primary source for current exchange pricing. Independence versus the Polymarket rules source is medium: both point to the same venue, but one is contract interpretation and the other is live market data, so they answer different pieces of the problem.