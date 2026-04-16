---
type: source_note
case_key: case-20260415-90641eba
dispatch_id: dispatch-case-20260415-90641eba-20260415T174326Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: daily-close-threshold
entity: btc
topic: Spot price context across Binance, CoinGecko, and Coinbase
question: Will the price of Bitcoin be above $70,000 on April 20?
driver: liquidity
date_created: 2026-04-15
source_name: Binance API with CoinGecko and Coinbase spot cross-check
source_type: exchange/API spot data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc]
related_drivers: [liquidity]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-90641eba/researcher-analyses/2026-04-15/dispatch-case-20260415-90641eba-20260415T174326Z/personas/risk-manager.md
tags: [source-note, btc, binance, coingecko, coinbase, price-context]
---

# Summary

Current cross-venue context shows BTC already trading materially above 70000 on April 15, but the contract is about a specific Binance 1-minute close five days later. That supports a Yes baseline but does not remove timing risk.

## Key facts extracted

- Binance BTCUSDT spot API returned 73999.38 during this run.
- Recent Binance 1-minute candles in the same pull showed closes clustered around 73931 to 73999 with highs up to 74027.46.
- CoinGecko simple price returned 73982 USD for bitcoin.
- Coinbase BTC-USD spot returned 74044.655.
- Cross-source spot levels are directionally consistent: BTC is about 5.7% above the 70000 threshold today.

## Evidence directly stated by source

- Binance ticker endpoint returned `{\"symbol\":\"BTCUSDT\",\"price\":\"73999.38000000\"}`.
- Binance 1-minute kline endpoint returned recent candles including a last close of `73999.38000000` and a recent high of `74027.46000000`.
- CoinGecko returned `{\"bitcoin\":{\"usd\":73982}}`.
- Coinbase returned `{\"data\":{\"amount\":\"74044.655\",\"base\":\"BTC\",\"currency\":\"USD\"}}`.

## What is uncertain

- These are current spot references, not the contract-settling April 20 12:00 ET close.
- Cross-venue confirmation improves confidence that BTC is broadly above 70k now, but only Binance BTC/USDT matters for settlement.
- No volatility model or event schedule was checked in depth; this is contextual price state, not a path forecast.

## Why this source may matter

It shows the market is not pricing an obviously out-of-the-money event. The main remaining issue is maintenance of price above the threshold at a precise timestamp, not whether BTC can trade above 70k at all.

## Possible impact on the question

The fact pattern supports Yes as the base case, but also highlights the key fragility: short-dated crypto can easily swing several percent, so a 5-6% cushion with five days left is meaningful but not lock-tight.

## Reliability notes

Binance is highly relevant because it is the settlement venue. CoinGecko and Coinbase are useful secondary/contextual checks with moderate independence. None of these sources alone forecasts the April 20 noon close.