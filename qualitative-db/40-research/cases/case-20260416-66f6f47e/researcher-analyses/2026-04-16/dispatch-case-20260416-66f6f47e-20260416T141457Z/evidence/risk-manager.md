---
type: evidence_map
case_key: case-20260416-66f6f47e
dispatch_id: dispatch-case-20260416-66f6f47e-20260416T141457Z
research_run_id: c675a0cb-3861-460c-8378-abeff2057be0
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: threshold-close-markets
entity: bitcoin
topic: "Risk framing for Bitcoin above 72000 on Apr 21 noon ET"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 72000 on Apr 21, 2026?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["threshold-close-timing-risk"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-66f6f47e/researcher-source-notes/2026-04-16-risk-manager-binance-governing-source.md", "qualitative-db/40-research/cases/case-20260416-66f6f47e/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260416-66f6f47e/researcher-analyses/2026-04-16/dispatch-case-20260416-66f6f47e-20260416T141457Z/assumptions/risk-manager.md"]
downstream_uses: []
tags: ["evidence-map", "btc", "risk-manager"]
---

# Summary

Current evidence leans Yes because Binance BTC/USDT is already above 72k, but the contract remains fragile to a single future timestamp and close-only mechanics.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on Apr 21, 2026 close above 72,000?

## Current lean

Lean Yes, but with meaningful timing-risk discount versus a simple spot-based read.

## Prior / starting view

Starting baseline was the market-implied probability of about 70.5% from the current price input.

## Evidence supporting the claim

- **Current Binance spot is above threshold by ~2.4%**
  - Source: Binance API source note
  - Why it matters causally: the market only needs BTC to maintain a level it has already exceeded
  - Direct vs indirect: indirect/contextual for settlement, but directly relevant for state
  - Weight: high

- **Recent 24h Binance low remained above 73.3k**
  - Source: Binance API source note
  - Why it matters causally: recent trading range still leaves cushion above 72k
  - Direct vs indirect: indirect/contextual
  - Weight: medium

- **Contract mechanics are operationally clear**
  - Source: Polymarket rules note
  - Why it matters causally: lowers ambiguity risk versus more interpretive markets
  - Direct vs indirect: direct for contract interpretation
  - Weight: medium

## Evidence against the claim

- **This is a single future one-minute close, not a touch market**
  - Source: Polymarket rules note
  - Why it matters causally: BTC can trade above 72k repeatedly and still resolve No
  - Direct vs indirect: direct for mechanism
  - Weight: high

- **Five days is enough time for a 2% to 3% drawdown in BTC**
  - Source: inference from contract timing plus recent 24h volatility band
  - Why it matters causally: crypto can easily move this much before a fixed timestamp
  - Direct vs indirect: contextual
  - Weight: high

- **Current 24h change is mildly negative**
  - Source: Binance API source note
  - Why it matters causally: confirms there is active downside movement even while still above threshold
  - Direct vs indirect: contextual
  - Weight: low to medium

## Ambiguous or mixed evidence

- **Market price around 70.5%**
  - Useful as aggregate signal, but may embed both genuine information and overconfidence from spot anchoring.

## Conflict between inputs

- No factual source conflict.
- Main tension is weighting-based: how much confidence current spot cushion should receive versus close-only timing risk.

## Key assumptions

- BTC does not suffer a meaningful risk-off drawdown before Apr 21 noon ET.
- Binance remains a clean operational settlement surface.

## Key uncertainties

- What macro or crypto-specific catalysts hit before Apr 21 noon ET.
- Whether noon ET on Apr 21 coincides with heightened volatility.

## Disconfirming signals to watch

- BTC breaks below 73k and especially below 72k on Binance before Apr 21.
- Any exchange-specific dislocation affecting Binance BTC/USDT pricing.

## What would increase confidence

- Continued multi-session holding above 73k on Binance.
- A higher market level with spot support that is not solely driven by thin momentum.

## Net update logic

The contract-mechanics check kept me from treating this as a trivial Yes, but current Binance level being already above the line still leaves Yes as the base case. The risk discount is mostly about single-timestamp fragility rather than uncertainty about what the market means.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input, with emphasis on underappreciated close-only timing risk.