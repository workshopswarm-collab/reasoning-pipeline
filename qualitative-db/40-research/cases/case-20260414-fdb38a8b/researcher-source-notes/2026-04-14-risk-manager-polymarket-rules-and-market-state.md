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
driver: operational-risk
date_created: 2026-04-14
source_name: Polymarket market page and rules
source_type: market page / contract rules
source_url: https://polymarket.com/event/bitcoin-above-on-april-17
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [bitcoin, btc]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-fdb38a8b/researcher-analyses/2026-04-14/dispatch-case-20260414-fdb38a8b-20260414T180238Z/personas/risk-manager.md]
tags: [polymarket, contract-rules, resolution-source, market-implied-probability]
---

# Summary

The Polymarket market page establishes both the current market-implied probability (~0.81 from the assigned current_price 0.815 and page display around 81¢) and the governing settlement rule: resolution depends specifically on the Binance BTC/USDT 1-minute candle labeled 12:00 in ET on April 17, using the final Close price.

## Key facts extracted

- The market resolves Yes if the Binance BTC/USDT 1-minute candle for 12:00 PM ET on April 17 has a final Close price above 72,000.
- The source of truth is Binance, not other exchanges and not other BTC pairs.
- The contract is a multi-condition rule: correct date, ET noon timing, Binance venue, BTC/USDT pair, 1-minute candle, and final Close field all matter.
- The market page displayed the 72,000 line around 81¢ at fetch time, consistent with the assignment's current_price of 0.815.

## Evidence directly stated by source

- "This market will resolve to \"Yes\" if the Binance 1 minute candle for BTC/USDT 12:00 in the ET timezone (noon) on the date specified in the title has a final \"Close\" price higher than the price specified in the title. Otherwise, this market will resolve to \"No\"."
- "The resolution source for this market is Binance... BTC/USDT ... with \"1m\" and \"Candles\" selected."
- "Please note that this market is about the price according to Binance BTC/USDT, not according to other exchanges or trading pairs."

## What is uncertain

- The market page itself does not provide a robust time-series or volatility context for whether BTC is likely to remain above 72,000 by April 17 noon ET.
- It does not spell out DST conversion mechanics explicitly beyond saying ET, so the researcher still needs to map noon ET to the relevant Binance candle time convention operationally.

## Why this source may matter

This is the governing resolution surface. For a narrow date-and-time crypto market, contract mechanics are as important as price direction. Misreading venue, pair, or candle timing would create a false forecast even with a correct macro BTC view.

## Possible impact on the question

This source makes the case more favorable to a current-above-threshold Yes view because BTC is already materially above 72,000, but it also introduces path and microstructure risk: a single specific Binance minute close at noon ET can fail even if broader BTC sentiment stays bullish.

## Reliability notes

Primary source for contract interpretation and market state. High reliability for rules, but not sufficient alone for estimating the probability of the future noon ET close.