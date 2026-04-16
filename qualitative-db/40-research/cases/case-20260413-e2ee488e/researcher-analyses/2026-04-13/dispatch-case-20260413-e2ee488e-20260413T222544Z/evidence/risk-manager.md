---
type: evidence_map
case_key: case-20260413-e2ee488e
dispatch_id: dispatch-case-20260413-e2ee488e-20260413T222544Z
research_run_id: f0696ff9-18f0-4400-9273-f04e041148ab
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-15
question: "Will the Binance BTC/USDT 12:00 ET 1m candle close on 2026-04-15 be above 70000?"
driver: operational-risk
date_created: 2026-04-13
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-e2ee488e/researcher-analyses/2026-04-13/dispatch-case-20260413-e2ee488e-20260413T222544Z/personas/risk-manager.md"]
tags: ["threshold-market", "timing-risk", "resolution-check"]
---

# Summary

Current evidence nets to a clear Yes lean, but the risk-manager adjustment is to discount the near-certainty tone implied by a 94.5% market because this is a narrow timestamp contract with meaningful path risk over ~42 remaining hours.

## Question being evaluated

Whether the Binance BTC/USDT 1-minute candle labeled 12:00 ET on April 15, 2026 closes above 70,000.

## Current lean

Lean Yes.

## Prior / starting view

Starting view from market price was that Yes was highly likely given a 0.945 contract price, but this required verification because the market is both extreme-probability and timing-sensitive.

## Evidence supporting the claim

- **Current Binance spot level is well above threshold**
  - Source: Binance API / source note
  - Why it matters causally: price at ~74.2k leaves ~4.2k cushion above 70k
  - Direct or indirect: direct contextual price evidence, though not final settlement
  - Weight: high

- **24h Binance low remained above threshold**
  - Source: Binance 24h ticker / source note
  - Why it matters causally: suggests recent realized downside has not pierced 70k even during intraday weakness
  - Direct or indirect: contextual
  - Weight: medium

- **Resolution mechanics are simple and explicit**
  - Source: Polymarket rules page / source note
  - Why it matters causally: low ambiguity about exchange, pair, candle interval, and decisive field (close)
  - Direct or indirect: direct contract interpretation evidence
  - Weight: high

## Evidence against the claim

- **Single-minute, single-venue timestamp risk**
  - Source: Polymarket rules plus market structure logic
  - Why it matters causally: the contract can fail even if BTC stays broadly strong but dips at the exact noon minute on Binance
  - Direct or indirect: direct contract-mechanics risk
  - Weight: high

- **Current cushion is meaningful but not enormous for BTC over ~42 hours**
  - Source: Binance spot and 24h range
  - Why it matters causally: a ~5.7% drawdown from ~74.2k would be enough to miss
  - Direct or indirect: contextual
  - Weight: medium-high

- **Exchange-specific operational or microstructure tail**
  - Source: Binance-as-governing-source rule plus operational-risk driver
  - Why it matters causally: Binance-specific dislocation or wick can matter even if broader BTC prints differ
  - Direct or indirect: contextual/tail-risk
  - Weight: low-medium

## Ambiguous or mixed evidence

- The 24h weighted average around 72.0k is comfortably above 70k, but also shows the market is not trading absurdly far from the threshold; both comfort and residual fragility are true.

## Conflict between inputs

No major factual conflict found. The main issue is weighting: how much probability to assign to path/timing failure despite currently favorable spot conditions.

## Key assumptions

- BTC retains most of its current cushion into Apr 15 noon ET.
- Binance spot remains a clean reflection of broader BTC pricing near settlement.
- No sharp risk-off move erases more than ~4.2k before the relevant close.

## Key uncertainties

- BTC volatility over the remaining ~42 hours.
- Whether any macro or crypto-specific shock hits before settlement.
- Whether Binance shows exchange-specific noise near the resolution minute.

## Disconfirming signals to watch

- BTC trading near or below 71k before Apr 15.
- High realized volatility on Binance into the settlement window.
- Any sign of Binance-specific pricing irregularity.

## What would increase confidence

- BTC still trading materially above 72k shortly before Apr 15 noon ET.
- Another verification pass closer to settlement showing continued cushion.
- No exchange-specific anomalies on Binance.

## Net update logic

The main update is not directional but calibration-based: direct rule verification and Binance price checks support Yes, but they do not justify treating the outcome as virtually certain. The evidence supports a high-probability bullish view while preserving a nontrivial residual No tail due to narrow timestamp mechanics.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review