---
type: evidence_map
case_key: case-20260416-143465dc
dispatch_id: dispatch-case-20260416-143465dc-20260416T191321Z
research_run_id: 6d25cb26-798a-4d9e-8725-d5c2a662051b
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: prediction-markets
entity: sol
topic: will-solana-reach-90-april-13-19
question: "Will Solana reach $90 April 13-19?"
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["crypto-short-horizon-momentum-threshold-touch"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-base-rate-binance-resolution-source.md", "qualitative-db/40-research/cases/case-20260416-143465dc/researcher-source-notes/2026-04-16-base-rate-binance-price-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-143465dc/researcher-analyses/2026-04-16/dispatch-case-20260416-143465dc-20260416T191321Z/personas/base-rate.md"]
tags: ["evidence-map", "base-rate", "touch-market"]
driver:
---

# Summary

This is a narrow touch-market with explicit exchange and candle rules. The net evidence says the market is still unresolved but structurally live: SOL has not yet touched 90 on the governing Binance 1-minute High series, yet it is already trading close enough that a short-horizon wick remains plausible.

## Question being evaluated

Will Binance SOL/USDT print any 1-minute candle High of at least 90.00 between April 13 00:00 ET and April 19 23:59 ET?

## Current lean

Moderate lean Yes, but not as high as the market price implies.

## Prior / starting view

Outside-view prior for a round-number touch market a few days out should be lower than a vivid momentum narrative suggests unless the asset is already very close to the threshold.

## Evidence supporting the claim

- `2026-04-16-base-rate-binance-price-check.md`: direct Binance check shows the market only ~1.2% below the threshold at research time; high weight, direct.
- Same source note: recent daily highs rose from 86.81 to 89.15 during the live window, showing active upward pressure; medium weight, direct/contextual.
- Contract design from `2026-04-16-base-rate-binance-resolution-source.md`: only a brief wick is needed, not a persistent close above 90; high causal relevance.

## Evidence against the claim

- Direct Binance check also shows no touch yet in the observed April 13-16 window; high weight, direct.
- The last 14 daily candles contained zero highs at or above 90, which weakens a claim that 90 is routinely breached in the current regime; medium weight, contextual.
- A touch market can look easy when price is near the barrier, but repeated failures below a round number can signal real resistance; medium weight, contextual.

## Ambiguous or mixed evidence

- The last 30 daily candles included 8 highs at or above 90, but none in the last 14. That suggests 90 is reachable in the broader recent regime, but current local momentum has only recently rebuilt.
- Current market price of 0.74 may contain information about trader expectations, but it can also overreact to the vividness of a same-week near-touch.

## Conflict between inputs

There is little factual conflict. The tension is weighting-based: the same direct evidence supports both "no touch yet" and "threshold is close enough for a plausible wick." More future path dependence than source disagreement drives uncertainty.

## Key assumptions

- Short-horizon SOL volatility remains high enough to generate a 1-2% upside extension.
- No contract-interpretation edge case invalidates the Binance API-based read of the same underlying market.

## Key uncertainties

- Whether remaining April 17-19 price action is risk-on or risk-off.
- Whether 89.xx acts as a staging area for a quick breakout or as a rejection zone.
- Whether a qualifying wick occurs even if end-of-day closes remain sub-90.

## Disconfirming signals to watch

- A reversal into the low 80s.
- Repeated rejection below 89 with shrinking intraday range.
- A fresh verification pass showing a touch already happened or that the checked time-window logic was wrong.

## What would increase confidence

- Another direct Binance verification closer to the end of the window.
- Continued trading above roughly 88.5 with expanding intraday highs.
- Evidence of broad crypto beta strength rather than isolated SOL-specific weakness.

## Net update logic

The main update versus a generic base-rate prior is not a new narrative catalyst; it is proximity. A touch market becomes materially more live when the asset is already within about 1-2% of the threshold and several days remain. But the market's 74% price still looks somewhat aggressive because the direct governing data also says the event has not happened yet and recent local history has repeatedly stalled below 90.

## Suggested downstream use

Use as an orchestrator synthesis input and as an audit trail for why the base-rate lane stayed slightly below the market rather than fading the contract outright.