---
type: source_note
case_key: case-20260415-2ce6159e
dispatch_id: dispatch-case-20260415-2ce6159e-20260415T142913Z
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: btc
topic: case-20260415-2ce6159e | market-implied
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: reliability
date_created: 2026-04-15
source_name: Binance BTCUSDT API spot and 1m klines cross-checked with CoinGecko spot
source_type: exchange API plus market data aggregator
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-2ce6159e/researcher-analyses/2026-04-15/dispatch-case-20260415-2ce6159e-20260415T142913Z/personas/market-implied.md]
tags: [binance, coingecko, spot-price, bitcoin, verification]
---

# Summary

This source note captures the direct factual price verification used to test whether the market's 93% Yes price is broadly sensible.

## Key facts extracted

- Binance BTCUSDT spot fetched at 74,405.16.
- Recent Binance 1-minute closes around the fetch window were 74,473.06, 74,467.09, 74,408.63, 74,429.99, and 74,408.96.
- Those kline timestamps convert to 10:26-10:30 ET on April 15, confirming the API timestamps line up as expected with ET conversion.
- CoinGecko simple price showed Bitcoin around 74,438 USD at nearly the same time.
- The spot level was therefore roughly 2.4k above the 72,000 threshold with about 25.5 hours remaining until the relevant noon ET candle.

## Evidence directly stated by source

- Binance directly states the live BTCUSDT spot price and minute-level OHLC closes.
- CoinGecko independently reports a very similar spot level, supporting that Binance was not an obvious outlier at the time checked.

## What is uncertain

- A one-time price check does not prove the contract will resolve Yes; BTC can move materially in a day.
- CoinGecko is contextual rather than the settlement source.

## Why this source may matter

This is the strongest direct evidence for the market's current confidence: the asset is already materially above the target on the same venue/pair family that matters for settlement.

## Possible impact on the question

If BTC remains near current levels, the market's 93% price is reasonable. The main remaining risk is adverse price volatility large enough to push the specific Binance noon ET close below 72,000 tomorrow.

## Reliability notes

High relevance because Binance is the governing source of truth for settlement. CoinGecko adds a useful independent contextual cross-check but is not itself dispositive.