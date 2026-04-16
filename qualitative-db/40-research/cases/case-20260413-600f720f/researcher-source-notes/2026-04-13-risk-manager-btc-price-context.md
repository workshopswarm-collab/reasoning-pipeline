---
type: source_note
case_key: case-20260413-600f720f
dispatch_id: dispatch-case-20260413-600f720f-20260413T233138Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: market-data
entity: btc
topic: will-bitcoin-reach-76k-april-13-19
question: Will Bitcoin reach $76,000 April 13-19?
date_created: 2026-04-13
source_name: Binance and Coinbase spot/API snapshot
source_type: exchange market data
source_url: https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-600f720f/researcher-analyses/2026-04-13/dispatch-case-20260413T233138Z/personas/risk-manager.md]
tags: [binance, coinbase, btc, price-context]
---

# Summary

This note captures a contemporaneous external price snapshot for BTC, used to assess how far the contract is from being hit and whether the market-implied probability looks too high or too low.

## Key facts extracted

- Binance BTCUSDT API snapshot returned `74815.78`.
- Coinbase BTC-USD spot API snapshot returned `74815.515`.
- The two independent exchange snapshots were effectively identical at retrieval, putting BTC about **$1.18k below** the $76,000 threshold.
- That gap is roughly **1.6%** from the observed spot level.

## Evidence directly stated by source

- BTC was trading materially below the target at the time of observation.
- Cross-exchange spot consistency was high at the snapshot moment, reducing concern that a single API print was stale or anomalous.

## What is uncertain

- These APIs provide current spot snapshots, not the maximum high reached later in the week.
- Coinbase is not the governing resolution venue for this contract; it is contextual confirmation only.
- No volatility or intraday range history was pulled here, so path probability must be inferred conservatively.

## Why this source may matter

The contract only needs a touch, not a sustained break, so distance-to-threshold matters more than closing-level analysis. A ~1.6% move in BTC over nearly a week is plausible, but not trivial enough to justify extreme confidence without more momentum evidence.

## Possible impact on the question

This source supports a moderate-to-high Yes probability while also supporting the risk-manager case that 74-75% may still be somewhat aggressive absent stronger trend evidence. The key downside to the thesis is simple timing/path failure: BTC can stay in the mid-74k range or fade before printing a Binance 1-minute high at 76k.

## Reliability notes

High reliability for contemporaneous spot context. Binance is especially relevant because it is also the contract’s governing resolution venue, though this endpoint is a spot snapshot rather than the actual 1-minute-high resolution record. Coinbase adds useful but not fully independent market confirmation because both venues reflect the same underlying BTC market regime.