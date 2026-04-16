---
type: evidence_map
case_key: case-20260413-64e915de
dispatch_id: dispatch-case-20260413-64e915de-20260413T234340Z
research_run_id: 9896dbb7-9ea3-45ec-a1a5-b7d2cf4dee3f
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: protocols
entity: ethereum
topic: will-ethereum-reach-2-400-april-13-19
question: "Will Ethereum reach $2,400 April 13-19?"
date_created: 2026-04-13
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["short-horizon-crypto-touch-probability"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-64e915de/researcher-analyses/2026-04-13/dispatch-case-20260413-64e915de-20260413T234340Z/personas/risk-manager.md"]
tags: ["evidence-map", "risk-manager", "path-risk"]
driver:
---

# Summary
The case leans Yes because the contract is a weekly touch market on Binance and ETH is already extremely close to the threshold, but the main risk-manager objection is that the market may be overconfident about converting proximity into an actual qualifying 1-minute high.

## Question being evaluated
Will Ethereum reach $2,400 at any point on Binance ETH/USDT between Apr 13 12:00 AM ET and Apr 19 11:59 PM ET?

## Current lean
Lean Yes, but at a slightly lower probability than the market implies.

## Prior / starting view
Starting view was that a 90%+ market likely required explicit rule verification and at least one independent contextual check before accepting it.

## Evidence supporting the claim
- Binance is the explicit resolution source and already printed a 24h high of 2394.71 on Apr 13.
  - source: 2026-04-13-risk-manager-binance-ethusdt-resolution-source.md
  - why it matters causally: only about $5.29 more is needed.
  - direct or indirect: direct for path proximity, direct for resolution source.
  - weight: very high.
- The market has nearly a full week remaining after the first near-touch.
  - source: Polymarket rule text in the same source note.
  - why it matters causally: touch markets need one wick, not sustained trade above threshold.
  - direct or indirect: direct.
  - weight: high.
- CoinGecko historical context shows ETH is already in the low-2200s regime on the relevant date, so 2400 is nearby in percentage terms.
  - source: 2026-04-13-risk-manager-coingecko-history-context.md
  - why it matters causally: the threshold is within ordinary crypto weekly volatility rather than an outlier regime jump.
  - direct or indirect: indirect/contextual.
  - weight: medium.

## Evidence against the claim
- The market still requires a literal Binance 1-minute high at or above 2400; near misses do not count.
  - source: Binance/Polymarket rules note.
  - why it matters causally: resolution is binary and narrow.
  - direct or indirect: direct.
  - weight: high.
- ETH can fail repeatedly just under round-number resistance even in strong conditions.
  - source: inferred from structure of the threshold market and current distance-to-target.
  - why it matters causally: round-number levels often matter most when the market gets complacent about a touch.
  - direct or indirect: indirect.
  - weight: medium.
- Extreme 92% pricing may overstate confidence versus evidence depth because no source here directly proves the next six days will include another higher wick.
  - source: market price plus current evidence set.
  - why it matters causally: confidence can be too high even when direction is right.
  - direct or indirect: interpretive.
  - weight: medium.

## Ambiguous or mixed evidence
- CoinGecko date snapshot is directionally supportive but imprecise for this exact contract.
- Strong current momentum helps the Yes case but also means some of the easy move may already have happened.

## Conflict between inputs
There is little factual conflict. The main disagreement is weighting-based: whether current nearness to 2400 should justify a 90%+ probability rather than something modestly lower.

## Key assumptions
- Near-threshold proximity persists long enough to generate at least one qualifying wick.
- Binance remains a reasonable proxy for broad ETH strength during the window.
- No sudden risk-off shock removes the opportunity set.

## Key uncertainties
- Whether 2394.71 was effectively the week's best impulse already.
- Whether Binance-specific prints will differ meaningfully from other venues.
- Whether resistance just below 2400 is stronger than the market is pricing.

## Disconfirming signals to watch
- Repeated rejection in the high-2380s to 2390s.
- Rapid loss of crypto market momentum.
- ETH falling materially back toward the low-2200s or below.

## What would increase confidence
- A fresh Binance test into the 2390s with sustained momentum.
- Higher realized volatility while holding above recent pullback zones.
- Additional venue-independent context showing broad crypto risk-on continuation.

## Net update logic
Rule verification plus Binance proximity made the case clearly more likely than not. The extra verification pass did not break the Yes thesis, but it reinforced that the residual risk is mostly path-conversion risk rather than deep uncertainty about what the contract means.

## Suggested downstream use
Use as forecast update and Orchestrator synthesis input, especially to distinguish directional agreement from confidence disagreement.
