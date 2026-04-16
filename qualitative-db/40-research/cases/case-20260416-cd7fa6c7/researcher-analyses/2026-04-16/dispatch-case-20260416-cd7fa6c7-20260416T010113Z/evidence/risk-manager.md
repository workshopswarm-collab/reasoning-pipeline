---
type: evidence_map
case_key: case-20260416-cd7fa6c7
dispatch_id: dispatch-case-20260416-cd7fa6c7-20260416T010113Z
research_run_id: 28b38a3e-2a52-41ef-9594-d25010be2fee
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
conflict_status: "low factual conflict, medium interpretive fragility"
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-cd7fa6c7/researcher-analyses/2026-04-16/dispatch-case-20260416-cd7fa6c7-20260416T010113Z/personas/risk-manager.md"]
tags: ["evidence-map", "timing-risk", "threshold-market", "binance"]
---

# Summary

The evidence nets to a modest Yes lean with meaningful fragility because the contract resolves on one exact Binance minute close rather than a broader daily or cross-exchange measure.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 17 be above 74,000?

## Current lean

Slight Yes lean, but less confident than the market.

## Prior / starting view

Starting baseline was the market price of 0.65, which implies a meaningful but not overwhelming Yes edge.

## Evidence supporting the claim

- Binance spot around 74,472 during the research window.
  - source: 2026-04-16-risk-manager-binance-coinbase-price-context.md
  - why it matters causally: the contract resolves on Binance BTC/USDT, so current Binance level is the most relevant direct evidence
  - direct or indirect: direct contextual evidence, but not direct settlement evidence
  - weight: high

- Coinbase BTC-USD around 74,559 at the same time.
  - source: 2026-04-16-risk-manager-binance-coinbase-price-context.md
  - why it matters causally: corroborates that BTC broadly was trading above the threshold, reducing concern that Binance was a one-off outlier during the check
  - direct or indirect: indirect/contextual
  - weight: medium

## Evidence against the claim

- Contract resolves on one exact minute close at 12:00 ET, not on whether BTC trades above 74k generally during the day.
  - source: 2026-04-16-risk-manager-polymarket-rules-binance-resolution.md
  - why it matters causally: creates substantial timing/path risk and raises the chance of a false broad narrative about being “above 74k” while still resolving No
  - direct or indirect: direct contract evidence
  - weight: very high

- Current spot margin over the threshold is small, only a few hundred dollars.
  - source: 2026-04-16-risk-manager-binance-coinbase-price-context.md
  - why it matters causally: ordinary BTC intraday volatility can erase that edge by the designated minute
  - direct or indirect: direct contextual evidence
  - weight: high

## Ambiguous or mixed evidence

- Cross-exchange agreement is directionally supportive for Yes, but the contract ignores non-Binance venues at settlement.
- Lack of a visible major dislocation at research time helps, but one-day crypto volatility remains large relative to the narrow threshold buffer.

## Conflict between inputs

There is little factual conflict. The tension is interpretive: current spot above the threshold supports Yes, while contract precision and small margin argue against high confidence.

## Key assumptions

- Current Binance spot context carries predictive value into the exact resolving minute.
- No large overnight or morning shock materially changes BTC direction before noon ET.
- Binance-specific microstructure does not diverge unusually from the broader market near settlement.

## Key uncertainties

- Overnight and morning macro/crypto volatility before April 17 noon ET.
- Whether BTC remains comfortably above 74k or drifts back into the threshold zone.
- Exchange-specific print behavior on Binance during the resolving minute.

## Disconfirming signals to watch

- BTC losing 74k and failing to reclaim it during the U.S. morning.
- Increased short-horizon volatility or sharp risk-off move before noon ET.
- Binance trading below peers into the resolving window.

## What would increase confidence

- BTC holding well above 74k, ideally with a wider cushion, into the morning of April 17.
- Additional pre-resolution Binance checks showing stable trading above threshold.
- Absence of event-driven volatility catalysts into the settlement window.

## Net update logic

The main update is not about long-term BTC direction but about contract mechanics. Because the resolving source is a single Binance minute close, broad bullishness should be discounted relative to a daily-close framing. Current spot above the threshold still matters enough to keep a Yes lean, but the path-dependent structure warrants shaving probability below the market.

## Suggested downstream use

Use this as an orchestrator synthesis input and as a warning against overweighting generic “BTC is above 74k” commentary without checking the exact noon ET Binance print risk.