---
type: evidence_map
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
research_run_id: df85adea-03ee-4d2a-9fad-82f5faa62887
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: daily-close-threshold
entity: bitcoin
topic: "Evidence net for BTC > 74000 at Apr. 17 noon ET Binance close"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close be above 74000 on April 17?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: ["threshold persistence risk"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-market-implied-polymarket-rules-and-market-state.md", "qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-market-implied-binance-spot-and-1m-context.md", "qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/assumptions/market-implied.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "polymarket", "binance"]
---

# Summary

The market has a reasonable case for pricing Yes above 50% because BTC is already above the threshold on Binance. The main remaining issue is whether that level persists into the exact Apr. 17 12:00 ET settlement minute.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on Apr. 17 close above 74,000?

## Current lean

Lean Yes, but not as strongly as the assignment price of 0.71.

## Prior / starting view

Started from the market-implied baseline of 71% and asked what would make that price reasonable.

## Evidence supporting the claim

- Binance spot/ticker context shows BTCUSDT at 74888.89.
  - Direct source from governing venue.
  - Matters because the strike is already exceeded.
  - Weight: high.
- Recent Binance 1-minute closes in fetched sample all remained above 74,000.
  - Direct but contextual, since timing is not the settlement minute.
  - Matters because it suggests near-term persistence rather than one-off overshoot.
  - Weight: medium-high.
- Polymarket rules clearly define a single later close on Binance BTC/USDT, not an average or multi-venue print.
  - Direct primary contract evidence.
  - Matters because it reduces source ambiguity and frames the right risk.
  - Weight: high.

## Evidence against the claim

- The contract settles on one exact later candle close, not current spot.
  - Direct rules-based objection.
  - Matters because sub-threshold reversion into noon ET tomorrow is sufficient for No.
  - Weight: high.
- Only a short recent Binance sample was checked.
  - Direct workflow limitation.
  - Matters because a narrow window may overstate stability.
  - Weight: medium.
- Crypto remains volatile overnight and into U.S. morning sessions.
  - Contextual rather than directly measured here.
  - Matters because BTC only needs to slip about 1.2% from the observed 74888.89 level to lose the contract.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Polymarket page snapshot displayed the 74,000 outcome at about 66%, while assignment context gave 71%.
  - This is not substantive disagreement on mechanism, just evidence the live market may have moved within a moderate band.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much confidence should current above-threshold trading get when the resolution is a single later minute close.

## Key assumptions

- Current above-threshold Binance trading is informative about next-day noon persistence.
- No venue-specific resolution anomaly is likely.

## Key uncertainties

- Overnight and morning BTC volatility before settlement.
- Whether 74,000 remains firm support versus a recently reclaimed level.

## Disconfirming signals to watch

- BTC/USDT falling materially back below 74,000 on Binance before the U.S. morning.
- Increasing downside momentum near settlement time.

## What would increase confidence

- Additional Binance checks later in the night or morning showing repeated 1-minute closes above 74,000.
- Evidence of sustained support above the threshold rather than oscillation around it.

## Net update logic

The market prior deserves respect because current Binance pricing already sits above the strike and the governing rules are clean. I still shade below the market because the contract is a one-minute later close, and only a modest drawdown is needed to flip the outcome.

## Suggested downstream use

Use as synthesis input and as an auditable rationale for a modest Yes lean that is close to, but slightly less confident than, the market.