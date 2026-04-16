---
type: evidence_map
case_key: case-20260416-b80742d2
dispatch_id: dispatch-case-20260416-b80742d2-20260416T014833Z
research_run_id: 2e8b6169-d24a-4eb0-8935-07aac6fa87ce
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchange-market-structure
entity: xrp
topic: xrp-above-1pt3-on-april-19
question: "Will the Binance XRP/USDT 1-minute candle for 12:00 PM ET on 2026-04-19 close above 1.30?"
driver: operational-risk
date_created: 2026-04-15T21:54:00-04:00
agent: orchestrator
status: draft
confidence: medium
conflict_status: low_explicit_conflict_but_nontrivial_path_risk
action_relevance: high
related_entities: ["binance", "xrp"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-b80742d2/researcher-analyses/2026-04-16/dispatch-case-20260416-b80742d2-20260416T014833Z/personas/risk-manager.md"]
tags: ["evidence-map", "path-risk", "timing-risk", "crypto"]
---

# Summary

Current evidence favors Yes because Binance XRP/USDT is already materially above 1.30, but the risk-manager adjustment is that the contract is resolved by a single minute at a single venue, so confidence should be discounted for path dependence and exchange-specific timing risk.

## Question being evaluated

Will the Binance XRP/USDT 1-minute candle corresponding to 12:00 PM ET on 2026-04-19 have a final close above 1.30?

## Current lean

Lean Yes, but with less confidence than the market price suggests.

## Prior / starting view

Starting view: likely Yes given current price baseline, but needed explicit check on settlement mechanics, timezone handling, and whether recent Binance price behavior left enough buffer over 1.30.

## Evidence supporting the claim

- Binance spot price around 1.4013 at research time.
  - source: Binance ticker API
  - causal relevance: gives direct current distance from threshold
  - direct or indirect: direct
  - weight: high

- Binance 24h range of roughly 1.3503 to 1.4086, all still above 1.30.
  - source: Binance 24h ticker API
  - causal relevance: recent realized volatility still left a nontrivial margin above threshold
  - direct or indirect: direct
  - weight: high

- Last 10 sampled daily closes all above 1.32.
  - source: Binance daily klines
  - causal relevance: suggests current regime has held for multiple sessions
  - direct or indirect: direct historical context
  - weight: medium

- Last 1000 sampled 5-minute closes had zero closes at or below 1.30; minimum close about 1.3221.
  - source: Binance 5m klines
  - causal relevance: recent intraday path stayed above threshold even during fluctuations
  - direct or indirect: direct historical context
  - weight: medium

## Evidence against the claim

- Contract resolves on one exact 1-minute candle rather than a daily close or broader average.
  - source: Polymarket rules
  - causal relevance: creates narrow timing/path risk
  - direct or indirect: direct contract mechanics
  - weight: high

- Settlement depends on Binance XRP/USDT specifically, so exchange-specific anomalies matter even if broader XRP pricing is fine elsewhere.
  - source: Polymarket rules plus Binance-source dependence
  - causal relevance: venue-specific operational and microstructure risk can create a bad minute
  - direct or indirect: direct mechanics, indirect risk translation
  - weight: medium-high

- Search tool limitations reduced retrieval of independent contextual sources about upcoming catalysts or event risk.
  - source: workflow limitation this run
  - causal relevance: lowers confidence in ruling out surprise downside catalysts
  - direct or indirect: contextual confidence limitation
  - weight: medium

## Ambiguous or mixed evidence

- Binance API docs support timezone interpretation for klines, which helps operationalize the noon ET candle, but the contract points users to the Binance front-end candlestick display. That is probably aligned, but there is still some implementation ambiguity around exactly how a reviewer will inspect the final candle.

## Conflict between inputs

No major factual conflict was found. The main issue is weighting: current price regime strongly supports Yes, while contract narrowness argues for discounting extreme confidence.

## Key assumptions

- Binance spot remains in roughly the current regime through April 19.
- No sharp crypto-wide drawdown or XRP-specific negative catalyst hits before settlement.
- Binance venue behavior at noon ET is representative and operationally normal.

## Key uncertainties

- Magnitude of short-horizon XRP volatility over the next ~3 days.
- Whether any idiosyncratic catalyst could compress the price buffer quickly.
- Exact practical settlement inspection method on Binance front-end versus API data.

## Disconfirming signals to watch

- Spot falling back toward 1.33-1.35 with elevated volatility.
- Binance-specific outages, odd spreads, or liquidity anomalies in XRP/USDT.
- Material negative XRP or crypto market news before April 19 noon ET.

## What would increase confidence

- Continued maintenance of a >1.35 buffer into April 18-19.
- Additional independent contextual evidence showing no known adverse catalyst risk.
- A pre-resolution check confirming Binance front-end/API alignment on the relevant noon ET minute.

## Net update logic

The direct price evidence supports Yes clearly enough to exceed the ordinary evidence floor. The risk-manager update is not to flip bearish, but to resist the market's near-certainty because a single-minute, single-venue contract can fail through path dependence faster than a broad daily narrative would suggest.

## Suggested downstream use

Use as an orchestrator synthesis input and as a confidence-discount note: directionally supportive of Yes, but useful mainly for tempering overconfidence and highlighting what to verify closer to resolution.