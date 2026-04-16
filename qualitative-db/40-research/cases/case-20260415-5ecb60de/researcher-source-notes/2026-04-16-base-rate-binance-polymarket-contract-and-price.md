---
type: source_note
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: case-20260415-5ecb60de | base-rate
question: Will the Binance SOL/USDT 1-minute candle close at 12:00 ET on 2026-04-19 be higher than 80?
driver: operational-risk
date_created: 2026-04-16
source_name: Binance API and Polymarket market page
source_type: primary+resolution-context
source_url: https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [sol, solana]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/base-rate.md]
tags: [binance, polymarket, resolution-source, source-note]
---

# Summary

This note captures the governing resolution wording from Polymarket and direct Binance pricing/context used for the base-rate estimate.

## Key facts extracted

- Polymarket says the market resolves "Yes" if the Binance SOL/USDT 1-minute candle for **12:00 ET (noon) on April 19, 2026** has a final **Close** price **higher than 80**.
- The contract is specifically tied to **Binance SOL/USDT**, not other venues or pairs.
- Price precision is determined by Binance source decimals.
- Direct Binance API spot/ticker checks during this run showed SOL/USDT around **84.87-84.92**.
- Direct Binance daily kline data for the prior 29 completed days showed **28/29 daily closes above 80**; the only sub-80 daily close in that sample was **78.94**.
- Recent completed daily closes include **86.51, 83.72, 84.90**, which indicates SOL has recently remained above the threshold despite short-term volatility.

## Evidence directly stated by source

From Polymarket market page:
- Resolution source is Binance.
- Relevant condition is the **1-minute candle close at 12:00 ET** on the specified date.
- "Higher than the price specified" means **strictly greater than 80**, not equal to 80.

From Binance API:
- Current ticker price during run: about **84.87-84.92**.
- Recent 1-minute candles around retrieval time clustered tightly around **84.85-85.00**.
- Recent daily klines imply SOL would need roughly a **5.7%** drop from current spot to finish below the threshold if noon April 19 were near current levels.

## What is uncertain

- The contract resolves on a single future minute, not on current spot or daily close.
- Crypto can move materially over several days, so current price alone does not settle the contract.
- The exact noon ET candle on April 19 is not yet observable.

## Why this source may matter

This is the governing source-of-truth surface plus the closest available direct market data. It is enough to establish the exact contract mechanics and a disciplined outside-view starting point.

## Possible impact on the question

Because the market asks about a threshold materially below current Binance spot and because recent Binance closes have usually stayed above 80, the outside view leans Yes unless there is evidence of an imminent drawdown larger than recent ordinary variation.

## Reliability notes

- Polymarket market page is authoritative for stated contract wording and settlement logic.
- Binance is the named resolution source, making direct Binance price data the highest-value evidence.
- Independence is limited because both direct pricing observations come from Binance-family surfaces, but that is acceptable here because the market is explicitly settled by Binance.