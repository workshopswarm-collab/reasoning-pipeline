---
type: source_note
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 72000?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT market data and CoinGecko BTC context
authority: mixed
source_type: exchange data + market data aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [binance, coingecko, price, volatility]
---

# Summary

Direct Binance data and secondary CoinGecko context show BTC already trading meaningfully above 72,000 on April 14, but with enough recent volatility that a three-day horizon to a specific one-minute resolving candle is not trivial.

## Key facts extracted

- Binance spot ticker during research was about 74.8k BTC/USDT.
- The Binance 1-minute candle for 2026-04-14 12:00 ET (16:00 UTC) closed around 75,356.48.
- Recent Binance daily closes showed sharp swings: about 73,043 on Apr 10, about 70,741 on Apr 13, and about 74,418 on Apr 14 before further intraday strength.
- CoinGecko daily context over the last week showed BTC moving from roughly 71.1k to roughly 74.5k-74.8k, with a notable dip near 70.8k on Apr 13.

## Evidence directly stated by source

- Binance API directly gives current BTCUSDT spot price and candle close values.
- CoinGecko directly gives recent BTC/USD daily market history.

## What is uncertain

- CoinGecko is contextual rather than the settlement source.
- Current spot levels do not guarantee the exact 12:00 ET Friday candle close.
- Near-threshold contracts remain sensitive to macro headlines and crypto-specific volatility over a three-day window.

## Why this source may matter

It anchors the case in current distance-from-threshold and realized volatility. Being roughly 3-4% above the strike makes Yes favored, but recent multi-day swings show the threshold is still reachable on the downside before the resolving minute.

## Possible impact on the question

This evidence supports a Yes lean while also supporting the variant view that 81.5% may be slightly rich because recent realized movement has been large enough to threaten a specific-timestamp threshold even without a full trend reversal.

## Reliability notes

Binance is the best direct source for settlement-relevant pricing. CoinGecko adds useful independent context on recent BTC path and volatility but is not the governing source for resolution.