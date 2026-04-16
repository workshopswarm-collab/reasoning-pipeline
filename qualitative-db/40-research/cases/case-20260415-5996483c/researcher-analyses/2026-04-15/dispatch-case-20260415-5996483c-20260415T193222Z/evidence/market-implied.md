---
type: evidence_map
case_key: case-20260415-5996483c
dispatch_id: dispatch-case-20260415-5996483c-20260415T193222Z
research_run_id: f1ccbd6f-5917-4ec2-ac47-1af85f15c3e8
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on 2026-04-20 close above 70000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-5996483c/researcher-source-notes/2026-04-15-market-implied-polymarket-contract-and-market-snapshot.md", "qualitative-db/40-research/cases/case-20260415-5996483c/researcher-source-notes/2026-04-15-market-implied-cnbc-btc-price-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-5996483c/researcher-analyses/2026-04-15/dispatch-case-20260415-5996483c-20260415T193222Z/personas/market-implied.md"]
tags: ["evidence-map", "market-implied", "btc"]
---

# Summary

The evidence currently nets to a high-probability Yes view that is close to, but a bit below, the market’s extreme confidence. The market appears to be pricing the existing buffer above 70,000 as the dominant fact; the main reason not to fully match the market is the narrow exact-minute close mechanism.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for Apr 20, 2026 at 12:00 ET close above 70,000?

## Current lean

Yes, with a high but not near-certain probability.

## Prior / starting view

Start from the live market price of 0.895 as the first serious prior.

## Evidence supporting the claim

- Polymarket market snapshot and rules note: the 70,000 leg trades around 89.5%-93% Yes.
  - Direct for market-implied baseline and contract mechanics.
  - High weight because crowd pricing and exact rules are both visible.
- CNBC BTC quote snapshot shows BTC open around 74.3k, previous close around 74.3k, day low around 73.6k, and day high around 74.9k.
  - Indirect/contextual for settlement, but direct on broad threshold distance.
  - High weight because it shows a material cushion above 70,000 several days ahead of settlement.
- The contract horizon is short.
  - Indirect but meaningful: only a few days remain, reducing the time available for a large downside move.
  - Medium weight.

## Evidence against the claim

- The contract is not a broad "BTC above 70k sometime that day" claim.
  - Direct from rules.
  - High weight against overconfidence because the exact condition is the Binance BTC/USDT noon ET 1-minute close.
- Binance-specific basis, intraminute noise, or a localized drawdown could matter.
  - Indirect but mechanism-relevant.
  - Medium weight.
- No direct verified Binance 1m reference was successfully extracted in-tool during this run.
  - Workflow limitation rather than contrary market evidence.
  - Medium weight because it lowers confidence in matching the market’s most aggressive pricing.

## Ambiguous or mixed evidence

- General BTC bullishness supports Yes, but if sentiment is already crowded it may also mean downside is underpriced.
- A several-thousand-dollar buffer is strong support, but crypto can move fast enough that exact-time close markets are never completely safe.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether a 4k+ buffer with only a few days left justifies something around 90% or closer to the low 80s once the exact-minute-close restriction is respected.

## Key assumptions

- Current BTC levels are a fair guide to the likely Apr 20 noon ET Binance close distribution.
- No major macro or crypto-specific shock arrives before settlement.
- Binance BTC/USDT remains close enough to broader BTC/USD benchmarks for contextual sources to be informative.

## Key uncertainties

- Exact Binance BTC/USDT pricing near settlement.
- Whether BTC remains above 70,000 through normal weekend-style volatility into Apr 20.
- Whether exchange-specific microstructure creates a misleading contextual picture.

## Disconfirming signals to watch

- BTC losing the 72k-73k area before Apr 20.
- Binance-specific weakness versus broader BTC benchmarks.
- New downside catalyst in macro, regulation, or crypto risk sentiment.

## What would increase confidence

- Direct Binance BTC/USDT verification closer to settlement.
- Additional independent price-context reporting still showing BTC materially above 70,000 after another day.

## Net update logic

The market’s high price is largely defensible because BTC appears substantially above the threshold already. I downweight the price slightly because the contract settles on a narrow and exchange-specific exact minute close, so being above the line now is not equivalent to being resolved Yes.

## Suggested downstream use

Use as synthesis input and decision-maker context for why the market should be respected here unless new downside evidence emerges.