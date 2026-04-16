---
type: evidence_map
case_key: case-20260416-bac9c8f2
dispatch_id: dispatch-case-20260416-bac9c8f2-20260416T033803Z
research_run_id: b4a267a7-cce5-49d8-9c6b-235f7330313f
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-bac9c8f2/researcher-analyses/2026-04-16/dispatch-case-20260416-bac9c8f2-20260416T033803Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "timing-risk"]
---

# Summary

This market currently leans YES, but the risk-manager case is mainly about whether a modest current cushion above 74,000 is enough to survive to one exact noon ET candle close tomorrow.

## Question being evaluated

Will Binance BTC/USDT's 1-minute candle at 12:00 ET on Apr. 17 close above 74,000?

## Current lean

Lean YES, but less confidently than a casual glance at spot-above-threshold might suggest.

## Prior / starting view

Starting baseline was roughly aligned with market pricing because BTC was already trading above the threshold, but with explicit concern that date-specific single-minute settlement creates more fragility than a plain daily-close style market.

## Evidence supporting the claim

- **Current Binance spot above threshold**
  - Source: Binance API / source note.
  - Why it matters: direct evidence that BTCUSDT is currently above 74,000.
  - Direct or indirect: direct.
  - Weight: high.

- **Recent 1-minute Binance closes sampled above threshold**
  - Source: Binance API / source note.
  - Why it matters: shows the market is not just one transient print above 74,000.
  - Direct or indirect: direct.
  - Weight: medium.

- **CoinGecko cross-check broadly consistent with Binance**
  - Source: CoinGecko via direct API check.
  - Why it matters: reduces concern about immediate Binance-only anomaly.
  - Direct or indirect: contextual.
  - Weight: low-to-medium.

## Evidence against the claim

- **Settlement is one exact minute, not a broad daily condition**
  - Source: Polymarket rules / source note.
  - Why it matters: narrow timing increases path dependence and fragility.
  - Direct or indirect: direct for contract interpretation.
  - Weight: high.

- **Current cushion is modest in BTC terms**
  - Source: netting current spot against threshold.
  - Why it matters: roughly ~1.3% headroom can disappear in routine crypto volatility.
  - Direct or indirect: direct arithmetic plus contextual volatility logic.
  - Weight: high.

- **Binance-specific settlement source creates exchange-specific risk**
  - Source: Polymarket rules.
  - Why it matters: even if broader BTC spot is fine, the contract keys off Binance BTCUSDT specifically.
  - Direct or indirect: direct for mechanism, indirect for probability.
  - Weight: medium.

## Ambiguous or mixed evidence

- Market price near 0.71 suggests the crowd sees clear but not overwhelming odds of YES. That is informative, but it may also reflect underweighted timing/path risk or simply efficient pricing.

## Conflict between inputs

There is little factual conflict. The main tension is interpretive: whether current spot-above-threshold should be treated as strong enough evidence for a high-probability YES, or whether single-minute timing risk should compress confidence.

## Key assumptions

- BTC does not suffer a >1.3% adverse move into the settlement minute.
- Binance BTCUSDT remains a reasonable reference without settlement-specific anomaly.
- No material contract-interpretation surprise emerges beyond the explicit rules.

## Key uncertainties

- Overnight and morning volatility into noon ET.
- Sensitivity of BTC to macro or crypto-specific flow between now and settlement.
- Whether a brief settlement-window dip could dominate an otherwise bullish path.

## Disconfirming signals to watch

- BTCUSDT moving back toward or below 74,200 well before settlement.
- Sharp risk-off move in crypto overnight.
- Binance prints diverging unusually from other spot references.

## What would increase confidence

- Continued trade above ~75,000 into the morning.
- Evidence of lower realized volatility into the settlement window.
- Additional direct Binance checks closer to noon ET still comfortably above threshold.

## Net update logic

The direct evidence supports YES because current Binance price is above threshold, but the contract design prevents this from being treated as a near-lock. The main risk-manager adjustment is to haircut confidence for narrow timing and exchange-specific settlement mechanics.

## Suggested downstream use

Use this as synthesis input for probability calibration and for keeping the final decision-maker from over-reading current spot-above-threshold as if the market were already settled.