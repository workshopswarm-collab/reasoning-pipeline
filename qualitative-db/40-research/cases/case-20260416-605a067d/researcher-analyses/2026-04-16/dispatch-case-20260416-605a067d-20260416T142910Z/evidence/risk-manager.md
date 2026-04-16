---
type: evidence_map
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: 462a53a5-a84b-4046-b50b-38278daf2730
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: daily-threshold-close
entity: ethereum
topic: "Netting current cushion versus exact-minute settlement risk"
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-risk-manager-binance-spot-check.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/assumptions/risk-manager.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/risk-manager.md"]
tags: ["evidence-map", "ethereum", "binance", "settlement-risk"]
---

# Summary

Evidence nets to a high-probability Yes lean, but the main reason to avoid near-certainty is that the contract depends on one exact future Binance minute close rather than current spot or full-day average levels.

## Question being evaluated

Will the Binance ETH/USDT 1-minute candle corresponding to April 17, 2026 12:00 ET have a final close above 2200?

## Current lean

Lean Yes with meaningful but bounded timing risk.

## Prior / starting view

Starting baseline from market price was about 87.1% Yes, implying traders already see this as likely.

## Evidence supporting the claim

- **Current Binance spot is well above threshold**  
  - source: Binance spot-check note  
  - direct evidence  
  - ETH/USDT was around 2298-2299, giving roughly a 4.5% cushion over 2200  
  - high weight

- **Recent 24-hour Binance low remained above threshold**  
  - source: Binance 24hr stats note  
  - direct evidence  
  - 24h low of 2285.10 suggests price has not recently been threatening 2200  
  - medium-high weight

- **Contract uses a single noon close, not a harder full-day condition**  
  - source: Polymarket rules note  
  - direct evidence on mechanism  
  - only one specific minute must finish above threshold; if price stays roughly in current range, Yes resolves cleanly  
  - medium weight

## Evidence against the claim

- **Exact-minute timing risk remains the key failure mode**  
  - source: Polymarket rules + assumption note  
  - direct mechanism risk  
  - even if ETH is above 2200 most of the time, a selloff into the precise noon ET minute would still resolve No  
  - high weight

- **Crypto can move several percent within a day**  
  - source: Binance 24hr range itself  
  - direct/contextual mixed evidence  
  - the market already moved about 100 points high-to-low over 24 hours, so a 98-point drop from current levels to sub-2200 is not impossible  
  - medium weight

- **Binance-specific source dependence**  
  - source: Polymarket rules note  
  - direct contract risk  
  - other exchanges being above 2200 would not matter if Binance alone printed below 2200  
  - medium weight

## Ambiguous or mixed evidence

- The market is pricing Yes very high, which is informative but not independent proof.
- Current price cushion is strong, but high cushion today can still decay materially by tomorrow noon in crypto.

## Conflict between inputs

No major factual conflict in the checked sources. The tension is weighting-based: how much probability discount should be applied for overnight volatility and exact-minute settlement risk.

## Key assumptions

- Current cushion persists into the governing minute.
- Binance data surface remains a reliable proxy for the chart-based settlement source.
- No exchange-specific anomaly materially distorts the noon close.

## Key uncertainties

- Overnight and morning price path before settlement.
- Whether U.S. morning volatility narrows the cushion more than recent range suggests.
- Small residual ambiguity from chart-interface settlement wording versus API-based precheck.

## Disconfirming signals to watch

- ETH/USDT trading near or below 2225 ahead of noon ET.
- Sudden crypto-wide risk-off move.
- Binance-specific outage, wick, or pricing anomaly near settlement.

## What would increase confidence

- A fresh Binance check closer to settlement still showing a substantial cushion.
- Independent confirmation that Binance chart values align with API values at the target minute.

## Net update logic

The evidence keeps the view bullish because direct Binance price evidence is comfortably above threshold. But the risk-manager discount remains meaningful because the market resolves on one exact future minute close. That means the main uncertainty is not whether ETH is generally strong enough; it is whether timing/path dependence or exchange-specific noise can still produce a losing print.

## Suggested downstream use

Use as a synthesis input emphasizing that this should not be treated like a touch market or broad directional ETH call. The main decision variable is whether current cushion is enough to survive exact-minute settlement risk.