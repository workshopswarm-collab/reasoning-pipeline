---
type: evidence_map
case_key: case-20260415-0735f476
dispatch_id: dispatch-case-20260415-0735f476-20260415T201136Z
research_run_id: 9ee1999a-f097-4354-b2b9-6b4c0ca257df
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "evidence net for BTC above 70000 noon ET close on April 20"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close above 70000 on April 20, 2026?"
date_created: 2026-04-15
agent: market-implied
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["binance", "bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["threshold-proximity", "resolution-surface-ambiguity"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-market-implied-polymarket-rules-and-price.md", "qualitative-db/40-research/cases/case-20260415-0735f476/researcher-source-notes/2026-04-15-market-implied-binance-live-price-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0735f476/researcher-analyses/2026-04-15/dispatch-case-20260415-0735f476-20260415T201136Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "binance", "market-implied"]
driver:
---

# Summary

The evidence net is straightforward: the contract is a single future minute-close on Binance, and current Binance BTCUSDT is materially above the threshold. That strongly supports Yes, but because the market is close-based and several days remain, the evidence is not fully dispositive.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 20, 2026 close above 70,000?

## Current lean

Lean Yes with high but not near-certain confidence.

## Prior / starting view

Starting from the market price, the implied probability was about 93% Yes.

## Evidence supporting the claim

- Live Binance BTCUSDT price around 74,621.
  - Source: Binance API source note.
  - Why it matters: Binance is the governing venue, and spot is ~6.6% above threshold.
  - Direct vs indirect: direct current-state evidence, indirect for the future resolution minute.
  - Weight: high.

- Recent Binance 1m closes all sampled well above 70,000.
  - Source: Binance API source note.
  - Why it matters: shows the governing venue is not just briefly wicking above the threshold; recent minute closes are comfortably above it.
  - Direct vs indirect: direct current-state evidence, indirect for final outcome.
  - Weight: medium-high.

- Polymarket contract wording specifies a simple close-above rule on a single venue/pair/time.
  - Source: Polymarket rules source note.
  - Why it matters: removes ambiguity about touch versus close, venue, and pair.
  - Direct vs indirect: direct rule evidence.
  - Weight: high.

- Market price near 93-94% Yes.
  - Source: Polymarket rules source note.
  - Why it matters: suggests the crowd broadly agrees that current cushion is substantial.
  - Direct vs indirect: indirect aggregation evidence.
  - Weight: medium.

## Evidence against the claim

- Resolution is still several days away and depends on one exact future minute close.
  - Why it matters causally: BTC can move several percent in days, so a 6-7% cushion is strong but not invulnerable.
  - Direct vs indirect: structural/contract evidence.
  - Weight: high.

- The market is close-based, not touch-based.
  - Why it matters causally: being above 70,000 now does not cash the contract; the exact noon ET close matters.
  - Direct vs indirect: direct rule evidence.
  - Weight: medium-high.

- Exchange-specific or reporting-surface ambiguity remains small but nonzero.
  - Why it matters causally: the contract references the Binance interface candle specifically.
  - Direct vs indirect: mechanism/rule caution.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- The market price itself is helpful as an aggregated prior, but not independent from publicly visible price levels and trader positioning.

## Conflict between inputs

There is little factual conflict. The main issue is weighting: whether the current 6-7% cushion deserves a probability in the low 90s or slightly lower.

## Key assumptions

- Current Binance cushion remains meaningful through April 20 noon ET.
- No major BTC selloff or Binance-specific anomaly occurs before resolution.

## Key uncertainties

- Short-horizon BTC volatility over the next several days.
- Whether macro or crypto-specific catalysts emerge before the resolution minute.

## Disconfirming signals to watch

- BTCUSDT falling rapidly toward 72,000 and below.
- Binance-specific pricing irregularities.
- New evidence that the contract interface/source behaves differently than the API proxy used here.

## What would increase confidence

- Additional Binance checks closer to resolution still showing BTC materially above 70,000.
- Independent contextual price coverage also showing no meaningful stress toward the threshold.

## Net update logic

The market starts at an extreme Yes price because BTC is already well above the line on the governing venue. I mostly accept that logic. The main downward adjustment from market is that the event is a future close at one specific minute, not a touch already satisfied.

## Suggested downstream use

Use this as forecast-update and orchestrator-synthesis input.
