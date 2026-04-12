---
type: source_note
case_key: case-20260409-99902b0b
dispatch_id: dispatch-case-20260409-99902b0b-20260409T203957Z
analysis_date: 2026-04-09
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-10
question: Will the price of Bitcoin be above $70,000 on April 10?
driver: reliability
date_created: 2026-04-09
source_name: Binance public API spot check
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-09
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [binance, btcusdt, market-data, source-note]
---

# Summary

A direct public-API spot check from Binance showed BTC/USDT around 72,422.65 at 2026-04-09 20:43 UTC / 16:43 EDT, roughly 19 hours before the noon-ET settlement candle. Recent 1-minute klines in the same pull were clustered around 72.37k-72.44k, leaving about a 2.4k buffer above the 70k threshold.

## Key facts extracted

- Binance server time responded normally.
- Binance ticker endpoint returned BTCUSDT at 72,422.65.
- Recent 1-minute candle closes in the sample were all above 72,000.
- The observed spot level implied BTC could fall materially and still remain above the 70,000 line at settlement.

## Evidence directly stated by source

- Ticker response: `{\"symbol\":\"BTCUSDT\",\"price\":\"72422.65000000\"}`
- Kline sample included minute closes such as 72436.32, 72411.31, 72392.38, 72387.18, 72374.99, 72383.78, 72373.45, 72367.13, 72426.90, and 72422.66.
- Server time response: `{\"serverTime\":1775767425671}`

## What is uncertain

- This is a snapshot, not a forecast. It does not by itself establish the noon ET April 10 close.
- BTC is volatile enough that a 2.4k cushion is meaningful but not invulnerable over ~19 hours.
- The API snapshot does not explain what catalyst would cause a sharp downward move before the settlement minute.

## Why this source may matter

This is the most direct contextual source for current distance from the strike and the timing problem. For a short-horizon threshold market, distance-to-barrier and realized minute-level stability are highly decision-relevant.

## Possible impact on the question

With BTC/USDT trading materially above 70k shortly before the deadline, the market only fails if BTC sells off by roughly 3.3% from the observed level into the exact settlement minute. That makes bearish near-term catalysts or operational settlement quirks the only obvious routes to No.

## Reliability notes

High reliability as a direct Binance public API pull from the named exchange and pair. Still only a partial input because the contract settles on one future minute close rather than the current spot price.