---
type: evidence_map
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
research_run_id: 188bb629-19bf-4aa1-bb8c-69e64b1d1a67
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-13
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close above 70000?"
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "timing-risk"]
---

# Summary

The evidence leans Yes, but the main residual risk is not directional BTC weakness in general; it is the narrow contract structure around one exact Binance minute close.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-13 close strictly above 70,000?

## Current lean

Lean Yes, with modest haircut versus market because the market appears slightly too confident relative to timestamp risk.

## Prior / starting view

Starting view was that a 71% market price likely understated the large pre-noon cushion if spot was already well above 70,000, but this had to be checked against actual contract mechanics and exact timing.

## Evidence supporting the claim

- Polymarket page showed the 70,000 line around 94% Yes at fetch time.
  - Source: source note on Polymarket rules and market state.
  - Why it matters: market participants were pricing a high likelihood of holding above 70,000.
  - Direct or indirect: indirect on outcome, direct on consensus baseline.
  - Weight: medium.
- Binance API around 09:46-09:50 ET showed BTC/USDT closes roughly from 70,964 to 71,609.
  - Source: Binance API verification note.
  - Why it matters: direct exchange data showed a cushion above the strike with only about 2h10m left.
  - Direct or indirect: direct on contemporaneous price state, indirect on final noon close.
  - Weight: high.

## Evidence against the claim

- Contract resolves on one exact 12:00 ET minute close, not on earlier trading, daily close, average price, or other exchanges.
  - Source: Polymarket rules note.
  - Why it matters causally: narrow timestamp markets can fail on brief intraday reversals.
  - Direct or indirect: direct on mechanics.
  - Weight: high.
- Binance verification could not yet access the future noon ET candle.
  - Source: Binance API verification note.
  - Why it matters causally: pre-resolution research cannot eliminate late path risk.
  - Direct or indirect: direct on unresolved timing uncertainty.
  - Weight: medium.

## Ambiguous or mixed evidence

- The high market price may reflect justified confidence from a large spot cushion, but it also may embed too much certainty for a single-minute binary event.

## Conflict between inputs

There is no material factual conflict between the sources. The main tension is weighting-based: whether a roughly 1.4k+ cushion with 2h10m to go deserves a mid-90s probability or something slightly lower.

## Key assumptions

- BTC stays above 70,000 through the exact resolving minute on Binance.
- No exchange-specific pricing anomaly on Binance breaks cross-venue intuition.

## Key uncertainties

- Late-morning crypto volatility before noon ET.
- Whether the spot cushion compresses materially into the resolving minute.

## Disconfirming signals to watch

- BTC/USDT losing the 70,500-70,000 area during late morning ET.
- Sharp macro or crypto headline shock before noon.
- Exchange-specific Binance dislocation.

## What would increase confidence

- A fresh Binance spot check closer to 11:30-11:55 ET still showing a strong cushion above 70,000.
- Lower realized volatility into the noon window.

## Net update logic

Contract-mechanics review raised the importance of timing risk, but direct Binance spot checks still left the balance clearly on Yes because BTC was materially above the strike fairly close to resolution. The result is a high-Yes view with a modest risk haircut relative to a very confident market.

## Suggested downstream use

Use as orchestrator synthesis input and as a stress-test note on why narrow timestamp crypto contracts should not be treated as equivalent to broad daily directional views.