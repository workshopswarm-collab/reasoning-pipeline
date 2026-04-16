---
type: evidence_map
case_key: case-20260415-75a50190
dispatch_id: dispatch-case-20260415-75a50190-20260415T205116Z
research_run_id: c7169e08-0c23-4d70-bf66-da4e6120c82d
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-21
question: "Will the price of Bitcoin be above $72,000 on April 21?"
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
proposed_drivers: ["intraday-volatility"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-75a50190/researcher-analyses/2026-04-15/dispatch-case-20260415-75a50190-20260415T205116Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "timing-risk", "contract-interpretation"]
---

# Summary

The evidence nets to a moderate Yes lean because BTC is currently materially above the threshold and the contract wording is clean, but the risk-manager view discounts confidence because settlement depends on one exact Binance minute-close several days away.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 ET on April 21, 2026 close above $72,000?

## Current lean

Lean Yes, but with lower confidence than the market price suggests.

## Prior / starting view

Starting view was that a market at 0.78 likely reflected BTC already trading above the threshold, but that short-horizon crypto path risk and exact-minute settlement mechanics could make the market modestly overconfident.

## Evidence supporting the claim

- **Current Binance spot context above threshold**
  - Source: direct Binance API check + source note
  - Why it matters causally: price is already around 74.9k, so no large upward move is required
  - Direct or indirect: direct contextual evidence from the exact exchange/pair
  - Weight: high

- **Contract wording is straightforward and source-of-truth ambiguity is low**
  - Source: Polymarket rules page + source note
  - Why it matters causally: lowers the chance that a technical interpretation surprise invalidates a plain reading
  - Direct or indirect: direct evidence on market mechanics
  - Weight: medium

- **Market baseline itself implies broad trader agreement that threshold is presently favorable**
  - Source: assignment current_price 0.78 and Polymarket page showing about 80-81%
  - Why it matters causally: suggests threshold is not obviously mispriced versus live market conditions
  - Direct or indirect: indirect consensus signal
  - Weight: medium

## Evidence against the claim

- **Settlement is one exact minute close, not average price or end-of-day level**
  - Source: Polymarket rules page
  - Why it matters causally: makes path/timing risk much more important than general BTC trend
  - Direct or indirect: direct contract evidence
  - Weight: high

- **Current cushion above threshold is meaningful but not huge for BTC over a six-day horizon**
  - Source: direct Binance API check versus 72k threshold
  - Why it matters causally: a ~3.8% move can erase the cushion in a volatile asset
  - Direct or indirect: direct contextual evidence
  - Weight: high

- **Single-venue dependence introduces venue-specific print risk**
  - Source: Polymarket rules page naming Binance BTC/USDT only
  - Why it matters causally: even if broader BTC references are firm, Binance-specific minute close is the actual resolver
  - Direct or indirect: direct contract evidence
  - Weight: medium

## Ambiguous or mixed evidence

- Lack of independent macro/contextual source collection in this run slightly limits confidence. It does not break the lean, but it means the estimate rests heavily on direct contract mechanics plus current price context rather than a deeper catalyst map.

## Conflict between inputs

No major factual conflict. The tension is weighting-based: spot is currently above threshold, but the market may be underpricing exact-minute volatility and settlement-timing fragility.

## Key assumptions

- BTC remains above 72k at the exact April 21 noon ET Binance minute close.
- Binance operational continuity and data presentation remain normal.
- No sudden macro or crypto-specific shock drives BTC below the threshold into settlement.

## Key uncertainties

- Near-term BTC realized volatility between now and settlement.
- Whether macro/news catalysts emerge before April 21.
- Whether the current 74.9k area remains durable support.

## Disconfirming signals to watch

- BTC decisively losing 74k and drifting into the 72k handle ahead of settlement.
- Volatility spike or risk-off move that compresses the threshold buffer.
- Binance-specific anomalies around pricing or minute-candle interpretation.

## What would increase confidence

- BTC holding comfortably above 74k into April 20-21.
- A wider threshold cushion, e.g. sustained trade above 75k.
- Additional independent evidence on supportive flow/macro backdrop.

## Net update logic

The main update is not about discovering a hidden rule edge; the rules are clear. The net comes from balancing a currently favorable spot level against a narrow settlement mechanic. That pushes the probability above 50% and keeps a Yes lean, but below the market's 78-81% confidence because one-minute settlement risk is more fragile than a generic spot-above-threshold story.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review