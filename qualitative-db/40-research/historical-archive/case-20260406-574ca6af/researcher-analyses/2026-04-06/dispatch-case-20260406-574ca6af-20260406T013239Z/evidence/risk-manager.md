---
type: evidence_map
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 53b2f3c6-cb4c-4c59-80a6-9924143d9ad2
analysis_date: 2026-04-06
persona: risk-manager
domain: crypto
subdomain: ethereum
entity: ethereum
topic: case-20260406-574ca6af | risk-manager
question: Will Ethereum reach $2,200 March 30-April 5?
driver: threshold reach vs settlement mechanics
date_created: 2026-04-06T01:37:20Z
agent: Orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: [ethereum, binance, polymarket]
related_drivers: [resolution mechanics, threshold path, source-of-truth ambiguity]
upstream_inputs: [contract text, binance klines]
downstream_uses: [risk-manager finding, orchestrator synthesis]
tags: [evidence-map, crypto, cex, threshold]
---

# Summary

This case is mostly a resolution-mechanics and direct-price-check problem, not a broad ETH thesis problem. The core risk question is whether the market's 0.74 price reflected underappreciated contract ambiguity or simply stale confidence.

## Question being evaluated

Will Ethereum reach $2,200 March 30-April 5 under this market's actual settlement rules?

## Current lean

Lean **No**, strongly; estimated Yes probability ~8% at the time of review.

## Prior / starting view

Starting from the market price, the implied Yes probability was 74%, suggesting either market expectation that Binance had already printed 2200 or confidence that a qualifying wick existed.

## Evidence supporting the claim

- Broad crypto price action during the week plausibly made 2200 seem reachable.
  - indirect/contextual
  - limited weight because the contract is not best-price across venues.
- Market itself priced Yes at 0.74.
  - indirect
  - some informational weight but downweighted because this case is source-of-truth sensitive and may be mispriced by rule confusion.

## Evidence against the claim

- Polymarket contract text says only **Binance ETH/USDT 1m candle highs** count.
  - direct, authoritative for mechanics
  - very high weight.
- Binance ETH/USDT 1m kline check across the full window found max high **2167.85**, below 2200.
  - direct empirical check against designated venue/symbol/interval
  - very high weight.
- Contract excludes other exchanges / pairs / generalized price references.
  - direct
  - high weight because it kills DEX or alternate-CEX rescue arguments.

## Ambiguous or mixed evidence

- The contract phrase excluding "spot markets" is slightly awkward and could confuse traders, but it does not materially overturn the explicit Binance ETH/USDT instruction.
- Binance API vs Binance GUI chart is a small implementation-level ambiguity, but likely low importance unless a discrepancy is documented.

## Conflict between inputs

Main conflict is weighting-based: market price suggested high confidence in Yes, while direct contract-plus-Binance evidence suggests No. This looks more like trader/rules confusion or stale pricing than a factual tie.

## Key assumptions

- Binance API and Binance chart data are materially aligned for settlement purposes.
- The ET date-window conversion used in the API check matches the contract window.

## Key uncertainties

- Whether Polymarket or traders used any hidden settlement override or moderator clarification not visible on the fetched page.
- Whether there was a one-off chart/API discrepancy.

## Disconfirming signals to watch

- Any screenshot or archived Binance 1m chart showing a wick >= 2200 in-window.
- Any Polymarket clarification naming a different source hierarchy.
- Any dispute centered on a specific timestamped candle.

## What would increase confidence

- Direct GUI confirmation from Binance chart archives.
- Final Polymarket resolution consistent with the No interpretation.

## Net update logic

The direct source-of-truth audit dominates. Once the contract is read carefully, generic ETH bullishness and DEX/other-venue possibilities lose most of their relevance. The market price therefore looked too confident relative to the actual designated venue check.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis on source-of-truth sensitivity and on market-pricing errors caused by contract-mechanics confusion.