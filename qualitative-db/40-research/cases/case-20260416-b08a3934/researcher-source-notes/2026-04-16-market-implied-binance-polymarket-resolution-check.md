---
type: source_note
case_key: case-20260416-b08a3934
dispatch_id: dispatch-case-20260416-b08a3934-20260416T023832Z
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance BTC/USDT API and Polymarket rules page
source_type: primary-plus-market-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT ; https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1m&limit=3 ; https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-b08a3934/researcher-analyses/2026-04-16/dispatch-case-20260416-b08a3934-20260416T023832Z/personas/market-implied.md]
tags: [source-note, primary-source, resolution-check, binance, polymarket]
---

# Summary

This source note captures the direct settlement mechanics from Polymarket and a direct Binance BTC/USDT price read plus recent 1-minute klines during the research window.

## Key facts extracted

- Polymarket states the market resolves to Yes if the Binance BTC/USDT 1-minute candle for 12:00 ET on April 17 has a final close strictly higher than 72,000.
- The market is exchange-specific: Binance BTC/USDT, not another exchange or pair.
- Price precision is determined by the source display / reported precision.
- A direct Binance ticker API read during research returned BTCUSDT price 75080.70000000.
- A direct Binance klines API read for the most recent three 1-minute candles during the research window showed closes of 75025.25, 75048.63, and 75077.99 at 2026-04-16 02:38, 02:39, and 02:40 UTC respectively.
- Those timestamps correspond to 2026-04-15 22:38, 22:39, and 22:40 ET, confirming the market was already materially above 72,000 roughly 13 hours before the settlement observation window.

## Evidence directly stated by source

- Polymarket rules explicitly define the governing condition and source of truth.
- Binance API directly reports the current BTCUSDT last price and the recent 1-minute candle closes.

## What is uncertain

- The direct settlement surface named in the contract is the Binance web trading interface with 1m Candles selected, not the public API. The API is highly likely to reflect the same underlying market data, but the contract names the web UI as the explicit source-of-truth surface.
- A price above 72,000 the prior evening does not guarantee the noon ET close will remain above 72,000.
- Crypto can move materially within 13 hours, so path risk remains nonzero.

## Why this source may matter

This is the core source set for a date-sensitive, rule-specific crypto price market. It provides both the governing resolution mechanics and a direct exchange-level spot check relevant to whether a 91% market price is reasonable.

## Possible impact on the question

The source set supports the idea that the market is not pricing a heroic upside move; it is pricing maintenance of an already large cushion above the threshold. That makes a high Yes probability defensible, while still leaving room for a nontrivial No tail if BTC sells off by more than ~4% before the noon ET settlement candle.

## Reliability notes

- Polymarket rules page is authoritative for contract wording but not itself the final price source.
- Binance exchange data is the most relevant direct market data surface available to this run.
- Evidence independence is moderate: the rule source and the exchange source are distinct, but the contract ultimately points back to Binance.
- Operational risk is low-to-moderate rather than zero because the named settlement surface is a UI view and exchange-specific mechanics can occasionally create edge-case ambiguity.