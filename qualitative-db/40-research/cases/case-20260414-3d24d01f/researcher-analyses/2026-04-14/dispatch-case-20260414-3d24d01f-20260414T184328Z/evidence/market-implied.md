---
type: evidence_map
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
research_run_id: 1ece8aaf-3416-4eeb-ac47-c13d6007f59e
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-19
question: "Will the Binance BTC/USDT 1-minute candle closing at 12:00 PM America/New_York on 2026-04-19 close above 70000?"
driver: reliability
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied"]
---

# Summary

The market's high-yes price looks directionally justified by current Binance spot levels and recent same-venue noon closes, but 89% likely embeds a fairly strong persistence assumption for the next five days.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-19 close above 70,000?

## Current lean

Lean yes, with only modest disagreement versus the market because the cushion above strike is real but not so large that a five-day crypto drawdown becomes negligible.

## Prior / starting view

Starting point was the market's 0.89 implied probability.

## Evidence supporting the claim

- Binance ticker price around 74,281 at research time.
  - Source: Binance API source note.
  - Causal relevance: the contract only needs the final relevant minute close to remain above 70,000, and spot is already materially above that line.
  - Direct/indirect: direct contextual evidence from the settlement venue.
  - Weight: high.

- Recent noon ET Binance 1-minute closes were above 70,000 on both Apr 13 and Apr 14.
  - Source: Binance API source note.
  - Causal relevance: directly checks the same venue and same time-of-day framing used by the contract.
  - Direct/indirect: direct contextual evidence.
  - Weight: medium-high.

- Polymarket cross-threshold ladder is internally coherent: 68k 95%, 70k 89%, 72k 75%, 74k 55%.
  - Source: Polymarket rules/pricing source note.
  - Causal relevance: suggests traders are not pricing the 70k leg in isolation; they are expressing a full distribution centered in the low-to-mid 70s.
  - Direct/indirect: indirect evidence via crowd aggregation.
  - Weight: medium.

## Evidence against the claim

- The contract is resolved on one specific minute close on one specific venue, so a short-lived but badly timed selloff can still fail the market even if BTC spends most of the week above 70k.
  - Source: Polymarket rules/pricing source note.
  - Direct/indirect: direct rule risk.
  - Weight: high.

- BTC is only about 6% above the strike, not 15-20% above it.
  - Source: Binance API source note.
  - Causal relevance: crypto can easily move more than that over five days.
  - Direct/indirect: direct contextual evidence.
  - Weight: medium-high.

- Settlement depends on Binance specifically, and UI/API interpretation around the exact noon ET candle required explicit conversion/verification.
  - Source: Binance API source note plus Polymarket rules note.
  - Direct/indirect: direct operational/source-of-truth consideration.
  - Weight: medium.

## Ambiguous or mixed evidence

- Current bullish spot level supports yes, but the same fact may already be fully reflected in the 89% market price.
- The market ladder implies confidence, but it does not by itself prove that traders are correctly pricing tail downside over the remaining five days.

## Conflict between inputs

There is little factual conflict; the main disagreement is weighting. The market appears slightly more confident than this run because it may be leaning heavily on current price persistence.

## Key assumptions

- BTC remains comfortably above 70k into the weekend.
- Binance continues to provide a clean, representative BTCUSDT print.
- Noon ET conversion to the relevant UTC minute is understood correctly for contextual checks.

## Key uncertainties

- Near-term macro or crypto-specific volatility over the remaining five days.
- Whether a fast downside move clusters near the settlement window.
- Whether any Binance-specific disruption affects the exact minute used for resolution.

## Disconfirming signals to watch

- BTC losing 72k and then 70k support before April 19.
- Binance-specific outage, maintenance, or obvious price dislocation.
- Sharp broad-risk-off move in crypto ahead of the weekend.

## What would increase confidence

- BTC remaining above roughly 73k into April 18-19.
- Another same-time Binance noon ET check still showing a strong cushion above 70k.
- No venue-specific operational issues reported by Binance.

## Net update logic

The market prior survived scrutiny. Direct venue-specific price evidence supports a yes lean, and the contract wording is clear enough that the main residual issue is not interpretation but short-horizon price path risk. That leaves only modest room to shade below the market rather than taking a hard contrarian stance.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why this persona remained broadly market-respecting rather than reflexively contrarian.