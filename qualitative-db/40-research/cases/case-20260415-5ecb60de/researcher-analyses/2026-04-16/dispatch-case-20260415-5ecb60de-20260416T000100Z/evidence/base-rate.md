---
type: evidence_map
case_key: case-20260415-5ecb60de
dispatch_id: dispatch-case-20260415-5ecb60de-20260416T000100Z
research_run_id: db877a35-6693-42a2-b221-258519522004
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: market-structure
entity: sol
topic: will-the-binance-sol-usdt-1-minute-candle-close-at-12-00-et-on-2026-04-19-be-higher-than-80
question: "Will the Binance SOL/USDT 1-minute candle close at 12:00 ET on 2026-04-19 be higher than 80?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-5ecb60de/researcher-analyses/2026-04-16/dispatch-case-20260415-5ecb60de-20260416T000100Z/personas/base-rate.md"]
tags: ["evidence-map", "base-rate", "binance"]
---

# Summary

The net evidence supports Yes, but not at the 90% confidence implied by the market. The outside view is strong because SOL is already above 80 and has usually remained above 80 recently, yet the contract is still a single future minute on a volatile crypto asset.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle close at 12:00 ET on April 19, 2026 above 80?

## Current lean

Lean Yes.

## Prior / starting view

Given current spot above 80 and a low threshold relative to recent trading range, the starting outside-view prior was that Yes should be favored unless the market had misread the contract timing or there was strong evidence of imminent downside.

## Evidence supporting the claim

- **Direct Binance spot above threshold**  
  - Source: Binance ticker / recent 1-minute klines  
  - Why it matters: the contract only needs a future noon close above 80, and current spot was around 84.9  
  - Directness: direct  
  - Weight: high

- **Recent daily frequency mostly above 80**  
  - Source: Binance 1-day klines, prior 29 completed days  
  - Why it matters: base-rate sample shows 28/29 daily closes above 80  
  - Directness: direct contextual proxy, not settlement-minute direct  
  - Weight: high

- **Required downside is meaningful but not tiny**  
  - Source: calculation from direct price data  
  - Why it matters: SOL would need about a 5.7% drop from current spot to be below threshold  
  - Directness: derived from direct source  
  - Weight: medium

## Evidence against the claim

- **Single-minute future settlement**  
  - Source: Polymarket contract wording  
  - Why it matters: even if broader trend is above 80, a volatile asset can print below 80 at one specific minute  
  - Directness: direct contract interpretation  
  - Weight: high

- **Recent sample includes sub-80 close**  
  - Source: Binance 1-day klines  
  - Why it matters: threshold breach is not hypothetical; a 78.94 close occurred in the recent window  
  - Directness: direct contextual  
  - Weight: medium

- **Market may reflect superior near-term flow information**  
  - Source: Polymarket pricing at ~90%  
  - Why it matters: market participants may have information or positioning about short-horizon crypto conditions not captured by a simple base-rate lens  
  - Directness: indirect  
  - Weight: medium

## Ambiguous or mixed evidence

- The market is extreme but not absurd: 90% may be too high from a base-rate perspective, but current spot and recent frequency clearly justify a strong Yes lean.

## Conflict between inputs

There is limited factual conflict. The main disagreement is weighting-based: whether current spot plus recent frequency justify something near 90%, or whether crypto short-horizon volatility should keep the estimate materially lower.

## Key assumptions

- No broad crypto shock before settlement
- No Binance-specific settlement anomaly
- Recent above-80 behavior is informative for the next several days

## Key uncertainties

- How much short-term crypto volatility to expect by April 19 noon ET
- Whether the noon ET minute could be unusually noisy relative to daily-close base rates

## Disconfirming signals to watch

- SOL loses 80 ahead of settlement
- Sharp crypto beta selloff into April 19
- Binance-specific disruption or unusual dislocation near the settlement minute

## What would increase confidence

- SOL holding above 83-85 into the day before settlement
- Additional intraday evidence showing noon ET prints have recently stayed comfortably above 80

## Net update logic

The base-rate prior already leaned Yes because the threshold is below current spot. Direct Binance data strengthened that lean: recent closes are mostly above 80, so the modal path remains Yes. But because this resolves on one future minute and crypto can swing quickly, the estimate should remain below the market's 90% confidence.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review