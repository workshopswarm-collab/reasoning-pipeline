---
type: source_note
case_key: case-20260414-082b1b3f
dispatch_id: dispatch-case-20260414-082b1b3f-20260414T171716Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: spot-market
entity: sol
topic: case-20260414-082b1b3f | catalyst-hunter
question: Will the Binance SOL/USDT 12:00 ET 1-minute candle close above 80 on April 17, 2026?
driver: operational-risk
date_created: 2026-04-14
source_name: Binance SOL/USDT API timing and recent threshold-risk history
source_type: primary_exchange_data
source_url: https://api.binance.com/api/v3/klines?symbol=SOLUSDT&interval=1d&limit=20
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-082b1b3f/researcher-analyses/2026-04-14/dispatch-case-20260414-082b1b3f-20260414T171716Z/personas/catalyst-hunter.md]
tags: [binance, settlement-timing, threshold-risk, catalyst-calendar]
---

# Summary

This note captures the direct exchange checks most relevant to a catalyst/timing view: current distance above the strike, exact settlement-time conversion, and recent evidence that a move back below 80 is plausible over a short horizon.

## Key facts extracted

- Binance spot on 2026-04-14 checked around 13:24 ET was 85.31 for SOL/USDT.
- Recent 1-minute Binance closes were tightly clustered around 85.23 to 85.31, confirming current trading is comfortably above the 80 threshold but not by an enormous margin.
- The contract’s relevant settlement minute is 2026-04-17 12:00 ET, which converts to 2026-04-17 16:00 UTC for Binance timestamp mapping.
- Recent Binance daily data showed sub-80 downside is not hypothetical: daily close 78.94 on 2026-04-01, lows of 78.85 on 2026-04-02 and 78.38 on 2026-04-06.
- More recent daily closes recovered: 81.53 on 2026-04-11, 86.51 on 2026-04-12, and 85.31 on 2026-04-13.
- The current setup therefore requires roughly a 6.2% downside move from 85.31 to below 80 by the settlement minute to flip the market to No.

## Evidence directly stated by source

- Binance API directly states current spot and recent kline history.
- Timezone conversion directly maps the contract’s ET noon condition to 16:00 UTC.

## What is uncertain

- These checks do not identify a specific scheduled Solana catalyst between now and settlement that is likely to dominate the price path.
- The Binance API is strongly relevant, but the contract cites the Binance trading interface candle as the governing resolution surface.
- A crypto-wide risk-off move, exchange-specific incident, or sharp macro repricing could still overwhelm the current cushion.

## Why this source may matter

For this case, the most material catalyst finding may be the absence of a known positive/negative scheduled event before resolution. That shifts the analysis toward path risk, weekend-style volatility, and whether any shock is likely to produce a >6% drawdown by one specific minute.

## Possible impact on the question

The source supports a high-Yes baseline but argues against near-certainty: there is no need for a fundamental collapse to miss the threshold, only a moderate short-horizon drawdown on the named exchange at the exact settlement minute.

## Reliability notes

- Binance is the named source of truth, so exchange-data relevance is high.
- Independence is medium because both the live state and settlement venue are the same source family.
- Source-of-truth ambiguity remains low rather than zero because the contract points to the Binance UI candle rather than the API endpoint used here.