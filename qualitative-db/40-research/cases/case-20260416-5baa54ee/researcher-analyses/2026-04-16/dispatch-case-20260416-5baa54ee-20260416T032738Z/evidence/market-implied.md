---
type: evidence_map
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
research_run_id: d30938f4-aed6-4194-8db0-0f62386de149
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-pm-et-one-minute-candle-on-2026-04-20-close-above-70000
question: "Will the Binance BTC/USDT 12:00 PM ET one-minute candle on 2026-04-20 close above 70000?"
driver: reliability
date_created: 2026-04-15T23:30:00-04:00
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-5baa54ee/researcher-analyses/2026-04-16/dispatch-case-20260416-5baa54ee-20260416T032738Z/personas/market-implied.md"]
tags: ["evidence-map", "threshold", "binance"]
---

# Summary

Evidence currently nets to a high-probability Yes view, with the market probably directionally right but slightly overconfident at 94% because crypto can still move violently over four days and the contract settles on one exact minute.

## Question being evaluated

Will the Binance BTC/USDT 12:00 PM ET one-minute candle on April 20, 2026 have a final close above 70,000?

## Current lean

Lean Yes.

## Prior / starting view

Starting view was to respect the 94% market price unless direct settlement mechanics or current Binance pricing suggested hidden fragility.

## Evidence supporting the claim

- Binance ticker API showed BTCUSDT at 75,029.99 during the run.
  - direct source
  - matters because the named settlement venue/instrument is currently about 7% above the threshold
  - weight: high
- Binance 1-minute kline API showed the latest three closes at 75,068.50, 75,032.91, and 75,029.99.
  - direct source
  - matters because the contract resolves on a 1-minute close, so recent minute-level data is more relevant than broad daily commentary
  - weight: high
- Polymarket rules page confirms a narrow mechanical contract: Binance BTC/USDT, 12:00 ET, final 1-minute candle close, strictly greater than 70,000.
  - primary resolution-context source
  - matters because it removes ambiguity about exchange, pair, interval, and comparison operator
  - weight: high
- Market price at 0.94 likely reflects that the strike is materially below spot with short time left.
  - indirect source
  - matters because crowd aggregation is often efficient on simple short-horizon threshold markets unless there is rule confusion
  - weight: medium

## Evidence against the claim

- BTC can move more than 7% within four days, especially over a weekend, so the current cushion is meaningful but not dispositive.
  - contextual evidence
  - matters because the market settles on one exact minute rather than a range or average
  - weight: medium
- The contract is venue-specific to Binance spot BTC/USDT.
  - direct contract feature
  - matters because exchange-specific dislocations, outages, or temporary pricing divergence could matter even if broader BTC stays firm
  - weight: low-to-medium
- Web verification of the exact Binance chart UI named in the rules failed, leaving the direct exchange check dependent on API endpoints instead of the visible chart surface.
  - procedural limitation
  - matters because it is a slight source-of-truth surface mismatch, though still within the same primary exchange family
  - weight: low

## Ambiguous or mixed evidence

- Extreme market confidence itself cuts both ways: it may reflect efficient pricing, or it may reflect overcompression in a market where tail risk is still real.

## Conflict between inputs

No major factual conflict found. The main tension is weighting-based: whether ~7% cushion with four days left deserves something like 90%+ or something slightly lower.

## Key assumptions

- Recent Binance spot and minute-candle levels are a reasonable proxy for settlement risk over the next four days.
- No major negative catalyst or venue-specific disruption occurs before noon ET on April 20.
- The Polymarket rules page accurately describes how the final settlement check will be applied.

## Key uncertainties

- Short-horizon BTC volatility into the exact resolving minute.
- Weekend/event-driven downside shock risk.
- Any Binance-specific operational or price-feed issue near settlement.

## Disconfirming signals to watch

- BTCUSDT loses the mid-74k to low-73k region with momentum.
- Material exchange-specific stress at Binance.
- Updated market structure showing sustained downside rather than noise.

## What would increase confidence

- Another later Binance check still showing BTC comfortably above 70,000.
- No new macro/crypto-specific shock heading into the weekend.
- Continued tight alignment between Binance spot prints and broader BTC reference venues.

## Net update logic

The key evidence did not overturn the market prior; it mostly validated it. The narrow contract mechanics were checked directly, and current Binance prices are far enough above the strike that the default view should remain Yes. The only meaningful subtraction is that 94% leaves limited room for still-real short-horizon crypto tail risk.

## Suggested downstream use

Use as orchestrator synthesis input and as a compact audit trail for why the market-implied lane stayed close to the live price rather than forcing contrarianism.
