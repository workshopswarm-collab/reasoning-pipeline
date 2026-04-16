---
type: evidence_map
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
research_run_id: 2d9132f2-60e4-4b10-ba84-1d2091e0201c
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: price-threshold-markets
entity: sol
topic: will-solana-reach-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low_direct_conflict_high_timing_uncertainty
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-intraday-wick-risk", "threshold-touch-market-microstructure"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/market-implied.md"]
tags: ["evidence-map", "touch-market", "solana", "binance"]
driver:
---

# Summary

This is a near-threshold crypto touch market where contract mechanics matter almost as much as directional price outlook. The evidence slightly favors Yes, but not as strongly as the 0.74 market price.

## Question being evaluated

Will any Binance SOL/USDT 1-minute candle from April 13 00:00 ET through April 19 23:59 ET print a High of at least 90?

## Current lean

Lean Yes, but only modestly above even odds.

## Prior / starting view

Starting baseline was the market price itself: 0.74 implies traders think one qualifying wick is more likely than not and perhaps fairly likely.

## Evidence supporting the claim

- Polymarket contract wording uses Binance 1-minute highs rather than closes.
  - source: source note on Polymarket resolution source
  - causal relevance: materially lowers the bar versus a sustained-price condition
  - direct or indirect: direct
  - weight: high
- Recent Binance verification pass showed highs reaching 89.15 in sampled data.
  - source: Binance kline source note
  - causal relevance: only a small additional move is needed
  - direct or indirect: direct
  - weight: high
- TradingView contextual page shows current SOL around 87.55 and frames 88 as nearby resistance with upside targets above 90 if cleared.
  - source: TradingView SOLUSD page
  - causal relevance: supports the idea that 90 is within normal short-horizon trading range rather than a distant tail event
  - direct or indirect: contextual
  - weight: medium

## Evidence against the claim

- The direct Binance pass still remained below 90.
  - source: Binance kline source note
  - causal relevance: the event is not already effectively settled
  - direct or indirect: direct
  - weight: high
- The contract is exchange-specific and minute-specific, so non-Binance prints or generalized spot references do not help unless Binance itself tags 90.
  - source: Polymarket resolution source note
  - causal relevance: narrows what counts and increases rule sensitivity
  - direct or indirect: direct
  - weight: medium
- TradingView technical context identifies nearby resistance around 88-88.5, which means 90 still requires follow-through rather than only drift.
  - source: TradingView SOLUSD page
  - causal relevance: highlights that the final move is still nontrivial
  - direct or indirect: contextual
  - weight: medium

## Ambiguous or mixed evidence

- Generic SOL spot references are directionally useful but not settlement-authoritative.
- Older related case files suggest this family of markets often needs explicit governing-source proof, but they do not directly answer this case.

## Conflict between inputs

There is little direct factual conflict. The main disagreement is weighting-based: should a near-threshold crypto asset with several days left be priced as merely possible or as distinctly likely? The market leans distinctly likely; this run leans only modestly likely.

## Key assumptions

- Binance intraday wick probability is high when SOL is already trading in the high-80s.
- No major risk-off shock interrupts the remaining window.

## Key uncertainties

- Full-window Binance highs before and after the sampled verification window were not exhaustively enumerated here.
- Short-horizon crypto volatility can produce fast threshold touches without much warning.

## Disconfirming signals to watch

- Failure to reclaim or extend beyond 89 on repeated attempts.
- Broad crypto downside that pushes SOL away from the threshold.
- Any full-window check showing no meaningful approach to 90 during prior sessions.

## What would increase confidence

- A complete Binance 1-minute audit of the April 13-19 window.
- Evidence that SOL/Binance intraday wicks commonly overshoot spot by enough to clip 90 from similar levels.
- Sustained trading above 88.5-89.

## Net update logic

The market prior deserved respect because the contract is a touch market, not a hold market. Direct rule interpretation and Binance verification keep Yes as the lean. But the same verification also shows the threshold was not yet cleared in the checked window, which restrains conviction and leaves me below the market's 0.74.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis on contract mechanics and governing-source specificity rather than generic crypto sentiment.