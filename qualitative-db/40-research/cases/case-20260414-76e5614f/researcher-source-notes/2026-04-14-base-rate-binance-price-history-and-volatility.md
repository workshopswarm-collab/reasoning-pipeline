---
type: source_note
case_key: case-20260414-76e5614f
dispatch_id: dispatch-case-20260414-76e5614f-20260414T182607Z
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: btc
topic: bitcoin-above-72k-on-april-17
question: Will the price of Bitcoin be above $72,000 on April 17?
driver: reliability
date_created: 2026-04-14
source_name: Binance BTCUSDT daily and hourly klines
source_type: exchange historical price series
source_url: https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=365
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium-high
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-76e5614f/researcher-analyses/2026-04-14/dispatch-case-20260414-76e5614f-20260414T182607Z/personas/base-rate.md]
tags: [source-note, binance, history, volatility, base-rate]
---

# Summary

Binance historical price checks show that BTCUSDT has spent only a minority of the last 30-60 days above 72,000, but it has moved back above that level in the most recent week and is currently several percent above the threshold. Recent hourly realized volatility over the last 96 hours suggests that a 3.45% decline into the settlement minute is possible but larger than a typical hour-scale move.

## Key facts extracted

- BTCUSDT daily closes above 72,000:
  - 6 of last 30 days (20.0%)
  - 8 of last 60 days (13.3%)
  - 29 of last 90 days (32.2%)
  - 119 of last 180 days (66.1%)
  - 304 of last 365 days (83.3%)
- Recent closes show BTC regained the threshold area after spending much of late March and early April below it.
- Recent daily closes:
  - 2026-04-07: 71,924.22
  - 2026-04-10: 72,962.70
  - 2026-04-11: 73,043.16
  - 2026-04-12: 70,740.98
  - 2026-04-13: 74,417.99
  - 2026-04-14: 74,573.11 at time checked
- Over the most recent 95 hourly changes, median absolute move was about 0.19%, 90th percentile about 0.63%, 95th percentile about 0.88%, and 99th percentile about 1.97%.
- The gap from live price to the threshold was about -3.45%, meaning BTC would need to fall roughly 3.45% from the checked level to finish below 72,000.

## Evidence directly stated by source

- Binance kline data directly provides the daily and hourly close series used here.

## What is uncertain

- Historical close frequencies are a rough base-rate reference class, not a direct probability for one specific future minute.
- Volatility measured over the most recent 96 hours may understate or overstate moves over the roughly two-and-a-half-day horizon to settlement.
- A single sharp crypto move, macro shock, or exchange-specific deviation could still break the recent distribution.

## Why this source may matter

This is the main outside-view evidence. It shows both that the threshold has not been consistently safe in the recent 30-60 day window and that current price position is meaningfully above 72,000. That combination pushes toward Yes but argues against treating 83% market odds as trivial.

## Possible impact on the question

The base-rate evidence supports a Yes lean because price is currently above the strike by several percent and BTC has recently re-established levels above 72,000. But the short-horizon crypto volatility and the fact that most of the last 30-60 days still closed below 72,000 keep the probability well below certainty.

## Reliability notes

- Binance is the same exchange named in the contract, so this is strongly aligned with the governing price source.
- Evidence independence versus the settlement source is low-to-medium because both the current and historical series come from Binance, but that is appropriate here since the contract is explicitly Binance-specific.
- The main limitation is reference-class choice, not source integrity.