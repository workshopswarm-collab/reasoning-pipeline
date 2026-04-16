---
type: evidence_map
case_key: case-20260416-881aa4d0
dispatch_id: dispatch-case-20260416-881aa4d0-20260416T044756Z
research_run_id: 7b8ceace-bb06-4360-8fdd-52a68ad459b4
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-17
question: "Will the price of Bitcoin be above $70,000 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["orchestrator synthesis input"]
tags: ["evidence-map", "threshold-market", "binance", "short-horizon"]
---

# Summary

The evidence mostly supports the market's near-certain Yes pricing, but the right framing is "very likely" rather than "already settled" because the contract depends on one exact future one-minute close.

## Question being evaluated

Whether Binance BTC/USDT will have a final 12:00 ET 1-minute candle close above 70,000 on April 17, 2026.

## Current lean

Lean Yes with very high probability.

## Prior / starting view

Starting prior was the live market price: 99.05% Yes.

## Evidence supporting the claim

- Direct Binance ticker check during the run showed BTCUSDT at 74,735.47.
  - Direct.
  - Causally important because Binance BTC/USDT is the settlement venue and pair.
  - Weight: very high.
- Direct Binance 1-minute kline check showed recent closes in the high-74k / low-75k area.
  - Direct.
  - Confirms the ticker was not a lone stale print.
  - Weight: high.
- Polymarket rules explicitly say the relevant print is the Binance BTC/USDT 12:00 ET candle close.
  - Direct for contract interpretation.
  - Weight: very high.
- Adjacent ladder prices imply a distribution centered materially above 70k (72k 94%, 74k 70%, 76k 29%).
  - Contextual / market-structure evidence.
  - Suggests traders are not pricing a borderline 70k scenario.
  - Weight: medium.

## Evidence against the claim

- The contract is not about today's level; it is about one exact future one-minute close at noon ET on April 17.
  - Direct contract risk.
  - Weight: high.
- BTC can move several percent in less than a day, and the current cushion is meaningful but not impregnable.
  - Contextual market-risk evidence.
  - Weight: medium.
- Exchange-specific operational or data issues at Binance could matter because Binance is both venue and source of truth.
  - Contextual/operational.
  - Weight: low to medium.

## Ambiguous or mixed evidence

- The extreme 99% market price may reflect genuine efficiency, but it can also embed some complacency because a one-minute threshold market is still path-sensitive.

## Conflict between inputs

No material factual conflict found. The main disagreement is interpretive: whether a 6-7% cushion with ~1 day remaining justifies ~99% versus something slightly lower in the mid/high-90s.

## Key assumptions

- Current Binance spot remains a reasonable guide to the likely noon ET April 17 level.
- No major overnight crypto shock or Binance-specific incident occurs.
- Noon ET was correctly mapped as the contract time to check.

## Key uncertainties

- Short-horizon BTC volatility between now and the settlement minute.
- Any exchange-specific anomalies at the exact resolution time.

## Disconfirming signals to watch

- Binance BTC/USDT falling quickly toward 72k or lower ahead of the resolution window.
- Broad crypto risk-off move during US morning hours on April 17.
- Evidence of rule ambiguity around the candle label or timezone mapping.

## What would increase confidence

- Another direct Binance spot/kline verification closer to the resolution window.
- Continued price stability above the low-73k area overnight.

## Net update logic

The evidence kept me close to the market but not fully at the market price. The direct settlement venue check strongly supports Yes, and the extra verification pass did not reveal contract ambiguity large enough to justify a strong discount. I still leave a few points of probability for one-day volatility and exact-minute threshold risk.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review