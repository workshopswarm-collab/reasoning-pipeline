---
type: evidence_map
case_key: case-20260414-fdb38a8b
dispatch_id: dispatch-case-20260414-fdb38a8b-20260414T180238Z
research_run_id: ac95f9bf-a014-453d-b503-1cd0cce205cc
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: btc-price
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the Binance BTC/USDT 12:00 PM ET 1-minute candle close on 2026-04-17 be above 72000?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-fdb38a8b/researcher-analyses/2026-04-14/dispatch-case-20260414-fdb38a8b-20260414T180238Z/personas/risk-manager.md"]
tags: ["evidence-map", "threshold", "path-risk", "resolution-logic"]
---

# Summary

Current evidence leans Yes because Binance BTC/USDT is already materially above 72,000, but the edge is weaker than the market's ~81% confidence suggests because the contract is a narrow single-minute threshold check with meaningful path risk over the next ~3 days.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 PM ET on April 17, 2026 have a final Close price above 72,000?

## Current lean

Lean Yes, but with a meaningful haircut to market confidence.

## Prior / starting view

Starting baseline was the market-implied probability of 81.5%, which embeds a strong expectation that BTC remains safely above the threshold through the exact resolution minute.

## Evidence supporting the claim

- **Current Binance spot materially above threshold**  
  - source: `2026-04-14-risk-manager-binance-price-context.md`  
  - why it matters: direct evidence from the relevant venue/pair shows BTC already trading near 74.76k-74.78k  
  - direct or indirect: direct  
  - weight: high

- **Recent 24h low still slightly above threshold**  
  - source: `2026-04-14-risk-manager-binance-price-context.md`  
  - why it matters: shows the threshold has recently held despite normal intraday movement  
  - direct or indirect: direct  
  - weight: medium

- **Contract only asks for one minute close, not sustained settlement above threshold**  
  - source: `2026-04-14-risk-manager-polymarket-rules-and-market-state.md`  
  - why it matters causally: if BTC remains generally above threshold into resolution, only the final close of that specific minute matters  
  - direct or indirect: direct contract interpretation  
  - weight: medium

## Evidence against the claim

- **The cushion is only about 3.8%-3.9% over threshold**  
  - source: `2026-04-14-risk-manager-binance-price-context.md`  
  - why it matters causally: this is small enough for ordinary crypto volatility to erase over ~3 days  
  - direct or indirect: direct  
  - weight: high

- **The contract is a narrow time-specific, venue-specific, field-specific resolution rule**  
  - source: `2026-04-14-risk-manager-polymarket-rules-and-market-state.md`  
  - why it matters causally: a brief downside move into the exact noon ET minute can resolve No even if broader BTC sentiment stays constructive  
  - direct or indirect: direct contract interpretation  
  - weight: high

- **The market-implied confidence may be overstating certainty relative to evidence depth**  
  - source: combined reading of rules plus current price context  
  - why it matters causally: current state evidence is strong, but not strong enough to eliminate event-window volatility and microstructure risk  
  - direct or indirect: interpretive  
  - weight: medium

## Ambiguous or mixed evidence

- The recent 24h low being just above 72,000 is supportive because support held, but also negative because it shows the threshold is already within ordinary trading range.
- Strong short-term momentum helps Yes, but momentum-driven crypto can mean-revert sharply.

## Conflict between inputs

No major factual conflict between sources. The tension is mainly weighting-based: whether current spot and recent range justify something close to 81% or something more conservative.

## Key assumptions

- BTC avoids a ~4% downside move into the exact resolution minute.
- No exchange-specific Binance dislocation meaningfully distorts the relevant close.
- Noon ET on April 17 is interpreted operationally via the Binance minute candle that corresponds to that time window.

## Key uncertainties

- Short-horizon BTC volatility over the next ~3 days.
- Any catalyst or macro/news shock before resolution.
- Whether the exact resolution minute catches a temporary dip even if the broader day remains above 72k.

## Disconfirming signals to watch

- BTC trading back toward 72k before April 17.
- Repeated failures to hold above 74k.
- Rising intraday volatility or sharp macro-led risk-off moves.

## What would increase confidence

- Another 24-48 hours with Binance BTC/USDT holding comfortably above ~73.5k-74k.
- Continued distance between spot price and the 72k threshold.
- Reduced intraday downside volatility heading into resolution.

## Net update logic

The market starts from a strong Yes baseline because spot is already above the threshold. I keep a Yes lean because that direct evidence matters most. But I downweight confidence versus the market because this is not a broad weekly average or end-of-day settle; it is a single specific minute close on one exchange, and the remaining cushion is well within normal crypto movement.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input, especially for calibrating whether the market is slightly overconfident on short-horizon path risk.