---
type: source_note
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
analysis_date: 2026-04-13
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-15
question: Will the price of Bitcoin be above $70,000 on April 15?
driver: reliability
date_created: 2026-04-13
source_name: Binance spot API with Coinbase and CoinGecko context check
source_type: exchange API / market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-analyses/2026-04-13/dispatch-case-20260413-e2ee488e-20260413T222544Z/personas/market-implied.md]
tags: [binance, coinbase, coingecko, spot-price, verification]
---

# Summary

A direct Binance API check on 2026-04-13 showed BTCUSDT around 74.2k, comfortably above 70k. A verification pass using CoinGecko and Coinbase showed roughly consistent spot pricing around 74.3k.

## Key facts extracted

- Binance ticker endpoint returned BTCUSDT price 74197.36.
- Recent Binance 1-minute klines were clustered around roughly 74.19k to 74.33k.
- CoinGecko simple price returned bitcoin at 74,284 USD.
- Coinbase spot returned BTC-USD at 74,299.995.
- Cross-venue/context prices were all roughly 4.2k above the 70,000 threshold.

## Evidence directly stated by source

- Binance ticker API: `{\"symbol\":\"BTCUSDT\",\"price\":\"74197.36000000\"}`
- Binance 1m klines for the most recent five candles all closed above 74,000.
- CoinGecko: `{\"bitcoin\":{\"usd\":74284}}`
- Coinbase: `{\"data\":{\"amount\":\"74299.995\",\"base\":\"BTC\",\"currency\":\"USD\"}}`

## What is uncertain

- These checks are a snapshot from Apr 13, not the resolving Apr 15 noon ET candle.
- Cross-venue checks are contextual only because the contract resolves solely to Binance BTC/USDT.
- Crypto can move several percent in less than two days, so current distance above threshold does not guarantee settlement.

## Why this source may matter

This is the best direct evidence for the market's current logic: the governing exchange price is already materially above the threshold, so a 94.5% market price mostly reflects the need to avoid a ~5.7% drawdown by settlement.

## Possible impact on the question

This supports the market-implied view that `Yes` is favored. The margin above 70k is large enough that only a fairly sharp short-horizon selloff, or an exchange-specific pricing anomaly at noon ET, would flip the contract to `No`.

## Reliability notes

Binance is the authoritative source for settlement, so its direct price API is high-value primary evidence. Coinbase and CoinGecko are useful contextual verification sources and moderately independent checks that the Binance print is not an obvious outlier.