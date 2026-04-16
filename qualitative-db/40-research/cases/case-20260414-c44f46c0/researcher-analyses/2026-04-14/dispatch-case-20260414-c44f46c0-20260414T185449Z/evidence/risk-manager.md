---
type: evidence_map
case_key: case-20260414-c44f46c0
dispatch_id: dispatch-case-20260414-c44f46c0-20260414T185449Z
research_run_id: d646b061-96a7-4dec-baf0-6d8bde9e7f1e
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-19
question: "Will the price of Bitcoin be above $68,000 on April 19?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium-high
conflict_status: "low direct conflict"
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-c44f46c0/researcher-analyses/2026-04-14/dispatch-case-20260414-c44f46c0-20260414T185449Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "threshold-market", "risk-manager"]
---

# Summary

Evidence nets to a strong Yes lean, but the main residual risk is a single-minute timing trap combined with the possibility of a sharp BTC drawdown or Binance-specific settlement anomaly.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-19 close above 68,000?

## Current lean

Yes, with high but not near-certainty confidence.

## Prior / starting view

Starting prior was that a threshold more than 8% below the current BTC level with only five days left would likely resolve Yes, but the market’s 95%+ pricing required checking whether the contract wording or source mechanics introduced hidden fragility.

## Evidence supporting the claim

- **Current Binance level is far above threshold**  
  - source: `2026-04-14-risk-manager-binance-and-market-rules.md`  
  - why it matters: a ~6k buffer is large for a five-day horizon  
  - direct or indirect: direct  
  - weight: high

- **Contract mechanics are relatively simple once pinned down**  
  - source: `2026-04-14-risk-manager-binance-and-market-rules.md`  
  - why it matters: resolution depends on one clear instrument, one venue, one candle, one timestamp  
  - direct or indirect: direct  
  - weight: high

- **Cross-exchange spot context broadly matches Binance**  
  - source: `2026-04-14-risk-manager-cross-exchange-context.md`  
  - why it matters: reduces risk that the live Binance level is an isolated feed error  
  - direct or indirect: indirect/contextual  
  - weight: medium

## Evidence against the claim

- **Single-minute timestamp risk**  
  - source: contract rules from `2026-04-14-risk-manager-binance-and-market-rules.md`  
  - why it matters: settlement depends on one exact minute, not a broader daily average or closing range  
  - direct or indirect: direct  
  - weight: high

- **Extreme market confidence can underprice tail paths**  
  - source: Polymarket market price from `2026-04-14-risk-manager-binance-and-market-rules.md`  
  - why it matters: 95%+ pricing leaves little room for volatility, sudden macro shock, or exchange-specific weirdness  
  - direct or indirect: direct-plus-interpretive  
  - weight: medium-high

- **Settlement source is exchange-specific**  
  - source: contract rules and failed UI fetch challenge noted in source note  
  - why it matters: if Binance has a venue-specific dislocation, other exchanges being above 68k would not save a Yes position  
  - direct or indirect: direct/operational  
  - weight: medium

## Ambiguous or mixed evidence

- Cross-exchange alignment is reassuring, but it is not itself decisive because settlement is Binance-only.
- Small basis differences between BTC-USD and BTC-USDT are immaterial at current distance but could matter if price collapses toward the threshold.

## Conflict between inputs

No major factual conflict across checked sources. The main tension is weighting-based: whether a 6k+ buffer with five days remaining justifies 95%+ confidence, or whether the single-minute rule deserves a larger tail discount.

## Key assumptions

- BTC remains materially above 68,000 into April 19 noon ET.
- Binance’s reported 1-minute close remains a trustworthy reflection of market price.
- No major macro or crypto-specific shock produces an abrupt drop large enough to breach the threshold.

## Key uncertainties

- BTC volatility over the next five days.
- Whether any scheduled or unscheduled catalyst emerges before resolution.
- Whether Binance-specific operational behavior near the resolution minute becomes relevant.

## Disconfirming signals to watch

- BTC falls toward 70k or below before April 19.
- Binance BTCUSDT starts diverging from Coinbase/aggregated spot references.
- Fresh contract interpretation issues emerge around the exact noon ET candle.

## What would increase confidence

- BTC holds above 72k into the final 24-48 hours.
- A direct UI-level confirmation of the Binance 1m candle path near settlement.
- Continued cross-exchange price consistency.

## Net update logic

The net update is that the contract wording is narrower than a casual glance suggests, but not complicated enough to overturn the dominant price-level evidence. That keeps the view Yes-leaning while still discounting the market slightly for timestamp fragility and venue-specific tail risk.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review for whether extreme-confidence crypto threshold markets should receive a standard tail-risk haircut