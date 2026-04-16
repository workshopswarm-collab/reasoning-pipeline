---
type: evidence_map
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
research_run_id: f6f42fe2-b2d9-4818-842e-60d900aec762
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-bitcoin-reach-76-000-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
driver: liquidity
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["liquidity", "macro", "sentiment"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-669935fa/researcher-analyses/2026-04-14/dispatch-case-20260414-669935fa-20260414T172940Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalysts", "bitcoin", "threshold"]
---

# Summary

This evidence map nets out a low-complexity but audit-sensitive timing case. The central question is not broad BTC direction but whether the contract-triggering price event has already happened on the governing venue.

## Question being evaluated

Will Bitcoin reach $76,000 April 13-19 under the Polymarket rule that keys off Binance BTC/USDT 1-minute highs?

## Current lean

Strong lean Yes; the key catalyst appears to have already occurred.

## Prior / starting view

Starting from the market price alone, the baseline was that the market considered Yes nearly certain. The main task was to verify whether the extreme probability reflected an already-triggered event versus mere expectation.

## Evidence supporting the claim

- Polymarket rule note indicates any Binance BTC/USDT 1-minute high >= $76,000 during Apr 13-19 ET resolves Yes.
  - directness: direct on resolution mechanics
  - weight: very high
- Binance 24-hour ticker recorded `highPrice = 76038.00` on Apr 14.
  - directness: direct contract-aligned market data
  - weight: very high
- Binance hourly kline note found a 2026-04-14 14:00 UTC high of `76038.00`.
  - directness: direct contract-aligned market data, though not minute-level archived
  - weight: high

## Evidence against the claim

- CoinGecko sampled series remained below $76,000 in sampled observations.
  - why it matters: suggests the move may have been brief, exchange-specific, or easy to miss in aggregated data
  - directness: indirect/contextual
  - weight: medium-low
- The exact qualifying 1-minute candle was not independently archived in this run.
  - why it matters: leaves a small residual transcript / data-correction risk
  - directness: direct limitation of the evidence set
  - weight: medium

## Ambiguous or mixed evidence

- Current BTC spot has already moved back below $76,000, which is irrelevant for contract resolution if the threshold was already touched, but can create superficial doubt for anyone thinking in end-of-week-close terms rather than hit-any-time terms.
- Macro and sentiment catalysts still matter for broad BTC path, but they matter much less for this contract once the threshold-trigger event has likely already occurred.

## Conflict between inputs

There is no major factual conflict. The mild tension is between Binance-specific threshold evidence and broader aggregator samples that do not clearly show the touch. This is primarily a source-granularity issue, not a true contradiction.

## Key assumptions

- The captured Polymarket rule note accurately reflects the governing settlement rule.
- The Binance >$76k print is valid and maps down to at least one qualifying 1-minute candle.

## Key uncertainties

- Exact archived minute of the first qualifying touch.
- Residual possibility of data correction or a rule-interpretation wrinkle not visible in the public fetch path.

## Disconfirming signals to watch

- A later Binance minute-candle archive showing no qualifying 1-minute high.
- Polymarket settlement delay accompanied by rule clarification.
- Exchange data correction below the threshold.

## What would increase confidence

- Archiving the exact Binance 1-minute candle that first printed >= $76,000.
- Final Polymarket settlement or explicit admin confirmation.

## Net update logic

The main update is from a generic extreme-price baseline to a catalyst-specific interpretation: the market is near 100% not because traders merely expect a future rally, but because the decisive trigger has likely already happened. That makes this much more of a settlement-verification case than a forward macro forecasting case.

## Suggested downstream use

- orchestrator synthesis input
- retrospective evaluation of how to handle exchange-specific hit markets at extreme probabilities