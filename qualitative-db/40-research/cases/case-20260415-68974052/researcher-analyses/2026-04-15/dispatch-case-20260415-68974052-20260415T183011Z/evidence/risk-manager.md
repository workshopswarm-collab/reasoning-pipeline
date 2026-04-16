---
type: evidence_map
case_key: case-20260415-68974052
dispatch_id: dispatch-case-20260415-68974052-20260415T183011Z
research_run_id: c04de9ac-e383-46b7-9467-9944b182c6a7
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["short-horizon-price-path-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-68974052/researcher-analyses/2026-04-15/dispatch-case-20260415-68974052-20260415T183011Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "binance", "settlement-risk"]
---

# Summary

The evidence still leans Yes, but the market's confidence likely outruns the true certainty because this is a narrow one-minute, exchange-specific settlement.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 1-minute candle corresponding to Apr 17, 2026 at 12:00 ET?

## Current lean

Lean Yes, but with a lower probability than market.

## Prior / starting view

Starting baseline was that current price being above 74k would make Yes favored, but the market might be too confident given BTC short-horizon volatility and single-minute settlement mechanics.

## Evidence supporting the claim

- **Current Binance spot level is above threshold by about 2.2k**
  - Source: Binance ticker and recent 1-minute klines; captured in source note.
  - Why it matters causally: the contract begins with a real positive cushion rather than needing an upside move.
  - Direct or indirect: direct for current state, indirect for settlement.
  - Weight: high.

- **Governing contract language is simple and explicit**
  - Source: Polymarket market rules page.
  - Why it matters causally: low interpretive ambiguity reduces rule-based downside from misunderstandings.
  - Direct or indirect: direct.
  - Weight: medium.

## Evidence against the claim

- **Settlement is a single future one-minute close on one exchange**
  - Source: Polymarket rules page.
  - Why it matters causally: narrow windows amplify path dependence and microstructure/venue-specific risk.
  - Direct or indirect: direct.
  - Weight: high.

- **BTC can move more than 2k over two days without being surprising**
  - Source: general BTC market behavior inferred from recent minute-level volatility context; no contrary evidence found that this is an unusually stable regime.
  - Why it matters causally: the current cushion is helpful but not decisive versus the time left.
  - Direct or indirect: contextual.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- The market's 0.85 price may be rational if traders expect continued risk-on drift, but it may also embed overconfidence from looking at current spot rather than the exact settlement mechanism.

## Conflict between inputs

No major factual conflict appeared. The key disagreement is weighting-based: how much probability mass should be deducted for short-horizon path risk and exchange-specific settlement risk despite current price being safely above threshold.

## Key assumptions

- Binance remains a usable and clean settlement source at the relevant minute.
- BTC does not suffer a >3% downside move into the settlement window.
- No material contract-interpretation edge case appears beyond the stated rules.

## Key uncertainties

- Near-term BTC volatility between now and Apr 17 noon ET.
- Whether Binance-specific prints deviate from broader spot context at the relevant minute.
- Whether the market is efficiently pricing exact settlement mechanics rather than a looser directional thesis.

## Disconfirming signals to watch

- BTC trading down toward or below 72k on Apr 16-17.
- Binance underperforming other venues into the settlement window.
- Any operational anomalies affecting Binance candles or display.

## What would increase confidence

- BTC holding materially above 73k into the final hours before settlement.
- Consistent Binance pricing near peer venues with no visible operational anomalies.

## Net update logic

Current price location keeps Yes favored, but the risk-manager adjustment comes from recognizing that this contract requires all of the following: BTC stays above threshold, Binance remains the governing venue, and the specific noon ET minute close lands above 72k. The market looks directionally right but somewhat too certain.

## Suggested downstream use

Use as synthesis input and to temper any naive acceptance of the 0.85 market price as if the contract were already nearly settled.