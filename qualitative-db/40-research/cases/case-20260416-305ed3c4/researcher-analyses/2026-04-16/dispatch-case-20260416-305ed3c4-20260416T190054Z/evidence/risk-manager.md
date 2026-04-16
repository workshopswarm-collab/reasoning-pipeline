---
type: evidence_map
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 8adf7e65-044c-4c3f-b33c-1a3dccf75a17
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: exchanges
entity: ethereum
topic: will-the-price-of-ethereum-be-above-2-200-on-april-17
question: "Will the price of Ethereum be above $2,200 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["ethereum", "binance"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["intraday-volatility"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-source-notes/2026-04-16-risk-manager-binance-polymarket-resolution-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/risk-manager.md"]
tags: ["evidence-map", "eth", "binance", "resolution-risk"]
---

# Summary

The evidence strongly favors Yes, but the main residual risk is timestamp-specific downside path risk rather than a dispute over what the contract means.

## Question being evaluated

Will Binance ETH/USDT print a final Close above 2200 on the 12:00 ET 1-minute candle on April 17, 2026?

## Current lean

Lean Yes with high but not absolute confidence.

## Prior / starting view

Given the market price near 97.5%, the starting expectation was that ETH was already comfortably above the strike and that the main task would be checking for timing or contract traps.

## Evidence supporting the claim

- **Direct market-state evidence from Binance API**  
  - Source: source note on Binance + Polymarket resolution check  
  - Why it matters causally: Binance is the named resolution source, and current price around 2344 places ETH about 6.5% above the threshold  
  - Direct or indirect: direct  
  - Weight: high

- **Verified 24h low still above threshold**  
  - Source: Binance 24h ticker data in source note  
  - Why it matters causally: even recent downside excursion did not threaten 2200, suggesting a buffer against ordinary volatility  
  - Direct or indirect: direct/contextual hybrid  
  - Weight: high

- **Polymarket rules are straightforward and venue-specific**  
  - Source: Polymarket market page  
  - Why it matters causally: reduces ambiguity about which exchange, pair, and timestamp decide settlement  
  - Direct or indirect: direct for resolution mechanics  
  - Weight: high

## Evidence against the claim

- **Single-candle timestamp risk**  
  - Source: Polymarket rules  
  - Why it matters causally: a sharp move at exactly noon ET can flip outcome even if ETH spent most of the period above 2200  
  - Direct or indirect: direct for contract risk  
  - Weight: medium-high

- **Crypto can move violently overnight or on macro headlines**  
  - Source: general contextual risk logic, not a case-specific headline  
  - Why it matters causally: the roughly 144-point cushion is meaningful but not impossible to erase in under 24 hours  
  - Direct or indirect: indirect/contextual  
  - Weight: medium

- **Binance-specific operational or pricing anomaly risk**  
  - Source: contract’s exclusive reliance on Binance ETH/USDT  
  - Why it matters causally: exchange-specific dislocation could matter even if broader ETH markets stay stronger  
  - Direct or indirect: contextual  
  - Weight: low-medium

## Ambiguous or mixed evidence

- Extreme market confidence near 97.5% is directionally justified by the buffer, but it may still compress residual timing risk too aggressively.

## Conflict between inputs

There is little factual conflict across the checked inputs. The main disagreement is interpretive: whether a current ~6% cushion plus a 24h low above strike justifies something near market certainty or merely very high confidence.

## Key assumptions

- ETH/USDT remains above 2200 through the exact settlement candle.
- Binance spot remains a reliable representation of the resolution-relevant price at noon ET.
- No late shock creates a gap-down large enough to erase the current cushion.

## Key uncertainties

- Overnight and morning volatility into the settlement window.
- Exchange-specific anomalies on Binance.
- Whether the final noon candle prints a transient downside close despite broader intraday strength.

## Disconfirming signals to watch

- ETH/USDT dropping below the recent 24h low around 2285.
- Spot trading compressing rapidly toward 2250-2220 ahead of noon ET.
- Any Binance-specific outage or market-structure issue.

## What would increase confidence

- ETH still trading comfortably above 2250 on Binance during the U.S. morning of April 17.
- No major macro or crypto-specific shock before the settlement minute.

## Net update logic

The evidence keeps the default Yes lean intact because the named resolution venue currently sits far above the threshold and recent verified trading did not breach it. The main thing downweighted is generic crypto volatility fear without case-specific evidence of immediate stress. The main thing retained as real risk is the narrow timestamp mechanic, which is why the probability remains below market, not because the directional case is weak.

## Suggested downstream use

Use this as an Orchestrator synthesis input emphasizing that the key question is not broad ETH direction but whether residual intraday path risk is being slightly underpriced by an already-extreme Yes market.