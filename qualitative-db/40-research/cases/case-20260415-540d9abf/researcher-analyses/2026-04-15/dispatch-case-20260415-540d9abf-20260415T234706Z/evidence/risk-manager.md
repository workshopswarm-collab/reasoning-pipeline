---
type: evidence_map
case_key: case-20260415-540d9abf
dispatch_id: dispatch-case-20260415-540d9abf-20260415T234706Z
research_run_id: 501666b7-5dc7-4a91-a291-52a63a6408e7
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: sol
topic: solana-above-80-on-april-19
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 80?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-540d9abf/researcher-analyses/2026-04-15/dispatch-case-20260415-540d9abf-20260415T234706Z/personas/risk-manager.md"]
tags: ["evidence-map", "sol", "binance", "settlement"]
---

# Summary

Current evidence favors Yes because SOL is already above 80 on Binance, but the main risk-manager adjustment is against overconfidence: the contract resolves on one exact noon ET minute close several days out.

## Question being evaluated

Will the Binance SOL/USDT 1-minute candle labeled 12:00 ET on 2026-04-19 have a final close price above 80?

## Current lean

Lean Yes, but with lower confidence than the 90% market-implied probability suggests.

## Prior / starting view

Starting baseline was the market-implied probability from Polymarket: roughly 90% Yes.

## Evidence supporting the claim

- Current Binance SOLUSDT spot observed in-run was about 84.93.
  - Direct source: Binance live ticker endpoint.
  - Why it matters: price is already above the threshold with a nontrivial cushion.
  - Direct or indirect: direct for current state, indirect for final settlement.
  - Weight: high.

- Recent Binance 24h range observed in-run was 82.65 to 85.83.
  - Direct source: Binance 24hr ticker endpoint.
  - Why it matters: threshold is below current market and even below recent 24h lows only by a modest amount; no immediate evidence that 80 is far out of reach downward.
  - Direct or indirect: direct for current context.
  - Weight: medium.

- Contract language is mechanically straightforward once mapped: Binance SOL/USDT, 1-minute candle, noon ET, final close higher than 80.
  - Direct source: Polymarket market page and rules text.
  - Why it matters: no hidden multi-source averaging or end-of-day ambiguity after rules review.
  - Direct or indirect: direct for settlement mechanics.
  - Weight: high.

## Evidence against the claim

- The market resolves on one exact minute close several days in the future, not on current spot or daily average.
  - Source: contract wording itself.
  - Why it matters causally: single-minute settlement increases path dependence and makes short-term volatility more important.
  - Direct or indirect: direct.
  - Weight: high.

- SOL is only about 6% above the threshold, which is meaningful but still within plausible crypto weekend move size.
  - Source: netting current Binance price against threshold.
  - Why it matters causally: a modest risk-off move can flip the result even if the broader uptrend remains intact.
  - Direct or indirect: derived from direct data.
  - Weight: high.

- Current market price around 90% may embed confidence that is too high relative to the evidence base used here.
  - Source: Polymarket outcome price and risk-manager judgment.
  - Why it matters causally: extreme market confidence requires stronger verification than merely being currently above strike.
  - Direct or indirect: interpretive.
  - Weight: medium.

## Ambiguous or mixed evidence

- Binance API documentation supports the kline mechanics, but Polymarket points to the Binance UI chart as the resolution surface. That is probably operationally equivalent, yet slight implementation ambiguity remains.
- Lack of broader independent market context in this run cuts both ways: there is no obvious bearish catalyst identified, but source coverage is not broad enough to dismiss one.

## Conflict between inputs

No major factual conflict across sources. The main disagreement is weighting-based: whether current spot above 80 should justify something close to 90% or something more conservative.

## Key assumptions

- Current spot level is informative for the noon ET close three-plus days ahead.
- No material Solana-specific or crypto-wide negative shock occurs before settlement.
- Binance settlement display and API kline interpretation remain aligned enough to avoid contract confusion.

## Key uncertainties

- Weekend crypto volatility before April 19 noon ET
- Potential exchange-specific anomalies on Binance near settlement
- Whether macro/crypto sentiment changes sharply over the next few days

## Disconfirming signals to watch

- SOL losing 82 and especially 80 on Binance before April 19
- Broad crypto selloff led by BTC/ETH weakness
- Any Binance charting/API irregularity that creates settlement ambiguity

## What would increase confidence

- Additional verification closer to settlement showing SOL still holding comfortably above 80
- Independent exchange/context checks showing no emerging Solana-specific weakness
- Continued Binance trading well above 80 through the weekend

## Net update logic

The evidence moved the view from an agnostic prior toward Yes because the governing source currently shows SOL above 80. But the risk-manager net adjustment is to cut confidence below the market because the case is date-specific, single-minute, and still exposed to normal crypto volatility. The key insight is not a directional reversal; it is that the market may be pricing too little path risk.

## Suggested downstream use

Use as orchestrator synthesis input and forecast calibration input, especially for confidence discounting rather than directional reversal.