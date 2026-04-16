---
type: source_note
case_key: case-20260416-8bef05aa
dispatch_id: dispatch-case-20260416-8bef05aa-20260416T144205Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: btc
topic: Binance BTC/USDT threshold close above 72000 at noon ET on 2026-04-21
question: Will the Binance BTC/USDT 1-minute candle for 12:00 ET on April 21, 2026 close above 72000?
driver: operational-risk
date_created: 2026-04-16
source_name: Polymarket rules page plus Binance BTCUSDT API context
source_type: primary-plus-contextual
source_url: https://polymarket.com/event/bitcoin-above-on-april-21
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [btc, bitcoin]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-8bef05aa/researcher-analyses/2026-04-16/dispatch-case-20260416-8bef05aa-20260416T144205Z/personas/base-rate.md
tags: [polymarket, binance, btc, source-note, threshold-market]
---

# Summary

This note combines the market's governing contract language from Polymarket with direct Binance BTC/USDT price context gathered from Binance public API endpoints. The Polymarket page is the clearest available source for the exact resolution mechanics; Binance market data is the direct contextual source for whether a >72000 noon close is currently structurally likely.

## Key facts extracted

- Polymarket states the market resolves Yes if the **Binance BTC/USDT 1 minute candle for 12:00 ET on April 21** has a final **Close** price **higher than 72000**.
- The rules explicitly anchor to **Binance BTC/USDT**, not other venues or pairs.
- The rule is a **single-minute close-above** condition, not an intraday high/touch condition.
- Binance public API showed spot BTC/USDT around **73944** during this research run.
- Binance daily candles for April 7-16 all had closes above 72000 except April 12, and the most recent several daily closes were materially above the threshold.
- Binance recent hourly data for April 15-16 also showed BTC trading mostly in the mid-74k area during this run, far above 72000.

## Evidence directly stated by source

From the Polymarket rules page:
- Yes requires the **12:00 ET** Binance **1-minute candle close** on the specified date to be higher than the listed threshold.
- Resolution source is Binance BTC/USDT candles.
- Price precision follows the source.

From Binance API outputs observed during the run:
- Current ticker price was approximately 73943.98.
- Recent daily closes: Apr 13 = 74417.99, Apr 14 = 74131.55, Apr 15 = 74809.99.
- Recent daily highs were also above 72k by a comfortable margin, but that matters less than the close-based rule.

## What is uncertain

- The market will be decided by the **specific 12:00 ET one-minute close on Apr 21**, not by current price, daily close, or intraday highs beforehand.
- Bitcoin can move several percent within days, so being 2k above the threshold now does not settle the question.
- I did not directly capture the final Apr 21 noon ET candle because it has not occurred yet; this is explicitly a forecast, not verification of occurrence.

## Why this source may matter

- The Polymarket rules page is the governing source for what actually counts.
- Binance API market data is the strongest direct contextual source for the current state relative to the threshold.
- Together they prevent a mechanism error: this is not a touch market and not an all-day close market.

## Possible impact on the question

- Because current BTC/USDT is already materially above 72000 and recent closes have mostly held above that level, the base rate for a single specified minute closing above 72000 in five days looks better than even.
- But because the contract is resolved by one exact minute rather than a broad window, there remains meaningful path risk; a several-percent drawdown before Apr 21 noon ET would flip the outcome.

## Reliability notes

- Polymarket page: high relevance and effectively primary for contract interpretation, though web extraction is still a secondary capture of the page.
- Binance API: primary contextual market data for BTC/USDT pricing, highly relevant and recent.
- Independence between the two is medium: they serve different roles (rules vs price context) rather than corroborating the same claim from independent journalism.
- Main residual risk is not source credibility but future price movement and the narrow single-minute settlement mechanic.