---
type: source_note
case_key: case-20260416-989964fe
dispatch_id: dispatch-case-20260416-989964fe-20260416T020418Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-market
entity: ethereum
topic: case-20260416-989964fe | base-rate
question: Will the price of Ethereum be above $2,200 on April 17?
driver: reliability
date_created: 2026-04-16
source_name: Binance public API ETHUSDT spot, 24h ticker, and recent klines
source_type: exchange API
source_url: https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [ethereum]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-989964fe/researcher-analyses/2026-04-16/dispatch-case-20260416-989964fe-20260416T020418Z/personas/base-rate.md]
tags: [binance, api, ethusdt, spot-price, verification]
---

# Summary

Direct Binance API checks show ETH/USDT trading materially above 2200 during the research window, with recent daily closes also above 2200 on most nearby dates. This does not settle the market but materially supports a high Yes prior for the next day's noon ET close.

## Key facts extracted

- Binance ticker price returned about 2355.61 at approximately 2026-04-16T02:05:00Z.
- Recent 1-minute klines around the fetch time showed closes clustered around 2353-2356.
- Binance 24h ticker showed ETHUSDT last price about 2355.35, 24h high about 2385.61, low about 2308.50, and positive 24h change.
- Recent daily klines show multiple nearby closes above 2200, including around 2240.01, 2245.05, 2284.99, 2369.46, 2322.44, and 2359.95; one nearby close at 2191.65 shows the threshold is not impossible to lose.

## Evidence directly stated by source

- Current ETHUSDT price on Binance.
- Recent intraday and daily realized trading range.
- Nearby historical daily closes on the same exchange/pair that governs settlement.

## What is uncertain

- The market settles on the final close of the 12:00 PM ET one-minute candle on April 17, not the current spot price on April 15/16.
- Public API access confirms the relevant venue and pair but not the exact future settlement candle.
- Daily closes are contextual, not identical to the contract's noon ET minute-close condition.

## Why this source may matter

This is the closest direct contextual evidence available before settlement because the same venue and pair named in the contract are already trading comfortably above the strike.

## Possible impact on the question

This substantially raises the outside-view probability that ETH remains above 2200 at the relevant settlement minute, while preserving some room for crypto volatility and exchange-specific price swings.

## Reliability notes

High credibility for current price context because it is the named exchange's own public API. Independence relative to the Polymarket page is reasonably good. Limitation: this is contextual evidence for a future minute close rather than direct settlement evidence.