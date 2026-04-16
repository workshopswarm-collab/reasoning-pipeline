---
type: source_note
case_key: case-20260415-35855579
dispatch_id: dispatch-case-20260415-35855579-20260415T225312Z
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: markets
entity: btc
topic: bitcoin-above-72k-on-april-16
question: Will the price of Bitcoin be above $72,000 on April 16?
driver: operational-risk
date_created: 2026-04-15
source_name: Binance BTCUSDT spot API check
source_type: exchange_api
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-15T22:55:00Z
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
downstream_uses: [qualitative-db/40-research/cases/case-20260415-35855579/researcher-analyses/2026-04-15/dispatch-case-20260415-35855579-20260415T225312Z/personas/risk-manager.md]
tags: [binance, btcusdt, spot-price, resolution-source]
---

# Summary

Direct Binance API spot check shows BTCUSDT at 75,088.01 around 2026-04-15 22:55:00Z, comfortably above the 72,000 threshold one day before the noon-ET settlement print. This is not itself the settling candle, but it materially informs how much adverse move would be required for a No resolution.

## Key facts extracted

- Binance ticker endpoint returned `{"symbol":"BTCUSDT","price":"75088.01000000"}`.
- This spot level is 3,088.01 points above 72,000.
- That is about 4.29% above the threshold.
- Timestamp of collection was 2026-04-15T22:55:00Z, which is 18:55 ET on April 15.

## Evidence directly stated by source

- BTCUSDT spot price on Binance was 75,088.01 at fetch time.

## What is uncertain

- The API ticker is not the exact contract settlement surface; the contract resolves on the Binance 1-minute candle close for 12:00 ET on April 16.
- The source note does not by itself establish whether the market will still be above 72,000 at the precise settlement minute.
- It does not rule out exchange-specific outage, display differences, or a fast drawdown into the relevant minute.

## Why this source may matter

This is the direct exchange family named in the market rules, so it is the best available current-state anchor for the path to resolution. It quantifies the size of the downside move needed for No.

## Possible impact on the question

A current Binance level around 75.1k means the market can be wrong only if BTCUSDT falls more than roughly 4.3% by the exact noon-ET settlement minute or if contract mechanics / exchange-surface issues create an unexpected resolution outcome.

## Reliability notes

- High relevance because Binance is the named resolution source.
- High recency because the data is live.
- Moderate evidentiary completeness because the contract settles on a future one-minute close rather than the current spot price.
