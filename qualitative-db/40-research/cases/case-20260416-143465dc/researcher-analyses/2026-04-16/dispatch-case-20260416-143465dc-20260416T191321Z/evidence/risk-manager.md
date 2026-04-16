---
type: evidence_map
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
research_run_id: c1e9bcf5-9f84-4ad4-ba08-72626c299f68
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: solana-touch-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["binance-microstructure-touch-risk"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/risk-manager.md"]
tags: ["evidence-map", "touch-market", "risk-manager"]
driver:
---

# Summary

The net evidence supports a modest Yes lean, but not as confidently as the market's 74% price implies. The threshold is close enough that a brief wick can settle the market, yet the contract is narrow enough that source-of-truth error and timing/path risk remain the core failure modes.

## Question being evaluated

Will Binance SOL/USDT print any 1-minute candle high at or above $90 between April 13 12:00 AM ET and April 19 11:59 PM ET?

## Current lean

Leaning Yes, but with meaningful fragility.

## Prior / starting view

Starting view: market likely somewhat efficient because the threshold is only modestly above current spot, but confidence should be discounted because touch markets near round numbers often look easier than they are.

## Evidence supporting the claim

- **Binance contract-relevant proximity:** Binance daily data showed a recent high of **89.15** on April 15. That leaves less than 1% additional upside to trigger resolution. Direct evidence. High weight.
- **Current price still near threshold:** Binance 24h ticker and CoinGecko cross-check both placed SOL in the high-88s during analysis. Direct for Binance ticker, contextual for CoinGecko. Medium-high weight.
- **Touch-market structure:** Because this is a touch market rather than a close-above market, a brief wick suffices. This lowers the bar relative to a sustained move. Contract interpretation. High weight.

## Evidence against the claim

- **No verified qualifying print yet in checked data:** The checked Binance highs remained below 90. Direct evidence. High weight.
- **Narrow governing source:** Only Binance SOL/USDT 1m highs count. A move to 90 on another venue, or a broader narrative that SOL was "around 90," is irrelevant. Contract/rule risk. High weight.
- **Timing risk:** The market has only a few remaining days. If momentum fades or volatility compresses, the threshold can remain unhit despite being nearby. Indirect but material. Medium-high weight.

## Ambiguous or mixed evidence

- **Round-number magnet vs resistance:** $90 is close enough to be reachable on noise, but also a psychologically visible level that can produce rejection.
- **Broader crypto beta:** Helpful if the market stays risk-on, but the current artifact set does not independently establish a durable catalyst strong enough to guarantee follow-through.

## Conflict between inputs

No major factual conflict. The main tension is interpretive: whether proximity plus touch-market mechanics justify something as high as 74%, or whether unresolved path/timing risk deserves a larger discount.

## Key assumptions

- Short-horizon SOL volatility remains high enough to generate at least one upward wick.
- Binance remains representative enough that a broader SOL move would likely appear there.
- No adverse regime shift pushes SOL materially away from the threshold before expiry.

## Key uncertainties

- Exact realized intraday momentum over the remaining window
- Whether $90 acts as a quick wick target or a near-term ceiling
- Whether late-week volatility expands or compresses

## Disconfirming signals to watch

- SOL loses the high-88 handle and trades back toward mid-80s
- Repeated Binance highs stall below ~89.2 without improvement
- Broad crypto risk sentiment weakens into the deadline window

## What would increase confidence

- Verified Binance 1-minute highs advancing into the 89.5-89.9 range
- A fresh Binance daily high above the current 89.15 reference
- Independent evidence of broad crypto risk-on continuation

## Net update logic

The contract text narrows the question materially, which prevents overcounting non-Binance or non-touch evidence. Once narrowed, the setup still leans Yes because the remaining move is small and only a wick is required. However, the absence of any verified 90+ print so far and the narrow source-of-truth mechanics keep the estimate below the market price.

## Suggested downstream use

Use as orchestrator synthesis input and as a check against overconfident bullish personas on a near-threshold touch market.