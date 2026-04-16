---
type: source_note
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-70k-on-april-19
question: Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 19, 2026?
driver: reliability
date_created: 2026-04-14
source_name: Polymarket event page and rules
source_type: primary-contract
source_url: https://polymarket.com/event/bitcoin-above-on-april-19
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/base-rate.md]
tags: [polymarket, contract, rules, settlement]
---

# Summary

The Polymarket contract specifies a narrow and date-sensitive settlement condition: the Binance BTC/USDT 1-minute candle for 12:00 ET on April 19, 2026 must have a final close price above 70000.

## Key facts extracted

- Market title: Will the price of Bitcoin be above 70000 on April 19?
- Current market-implied probability shown in assignment context is 0.89.
- Contract resolves Yes only if the Binance BTC/USDT 12:00 ET 1-minute candle close is higher than 70000.
- Exchange and pair are fixed: Binance BTC/USDT, not other exchanges or pairs.
- Precision is determined by the decimal places in the source.

## Evidence directly stated by source

- The rules explicitly define the relevant candle, time, exchange, pair, and comparison operator.
- The event page lists the 70000 line around 89-90% Yes during this run, matching the assignment's current price.

## What is uncertain

- The page text does not itself explain whether traders should use the website UI or API if the UI presentation differs, though both should point to the same underlying Binance data.
- The contract is sensitive to a single minute close several days in the future, so otherwise bullish market structure can still fail via short-term volatility.

## Why this source may matter

It is the governing contract source for what counts, what does not count, and how to interpret the threshold.

## Possible impact on the question

This narrows the forecast from a broad weekly BTC direction question into a specific single-minute settlement event. That tight wording makes extreme certainty slightly less justified than a simple spot-above-threshold question would be.

## Reliability notes

High-quality primary contract source. Main limitation is that it defines rules but not the future value, so it must be paired with Binance data for actual probability assessment.