---
type: source_note
case_key: case-20260415-9a9c8ea3
dispatch_id: dispatch-case-20260415-9a9c8ea3-20260415T192028Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-9a9c8ea3 | risk-manager
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Binance public API checks
source_type: exchange direct data / verification
source_url: https://api.binance.com/api/v3/
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager finding, risk-manager assumption note, risk-manager evidence map]
tags: [binance, api, btcusdt, candle, verification]
---

# Summary

Direct Binance API checks confirm BTCUSDT is an actively trading spot symbol, that 1-minute kline data is exposed with explicit close prices, and that current spot is materially above the 72,000 threshold.

## Key facts extracted

- `ticker/price` returned BTCUSDT spot around 74,656 at check time.
- `ticker/24hr` returned BTCUSDT last price around 74,661.82, 24h high around 74,786.72, and 24h low around 73,514.00.
- `exchangeInfo` confirmed BTCUSDT is trading and uses a price tick size of 0.01.
- `klines?interval=1m` returned recent one-minute candles with open, high, low, close structure and close timestamps in Unix milliseconds.
- Recent sampled 1-minute closes were above 74.6k, which is comfortably above the 72k threshold.

## Evidence directly stated by source

The API responses directly provided:
- the live BTCUSDT spot price
- recent 24h trading range
- the availability and structure of 1-minute candle closes
- trading status and price precision information

## What is uncertain

- This check does not itself prove where BTC will trade at the exact April 16 12:00 ET resolution minute.
- The Polymarket rule refers to the Binance UI candles surface; the public API is best treated as strong contextual verification of the same market mechanics, not an explicit contractual substitute unless settlement practice confirms equivalence.

## Why this source may matter

This is the best direct verification pass for operational mechanics and current distance from threshold. It reduces risk of relying only on Polymarket paraphrase or on third-party BTC prices from other venues.

## Possible impact on the question

Because BTCUSDT is currently about 2.6k above the threshold and the last 24h low is still above 72k, the base case favors Yes. The remaining risk is mainly path/timing risk: a selloff of roughly 2%+ into the exact settlement minute, or an exchange-specific print anomaly.

## Reliability notes

High reliability for current market-state verification because Binance is the named underlying venue and the API is first-party exchange data. Independence versus the Polymarket rules source is only medium because both still point back to Binance for the actual underlying market.