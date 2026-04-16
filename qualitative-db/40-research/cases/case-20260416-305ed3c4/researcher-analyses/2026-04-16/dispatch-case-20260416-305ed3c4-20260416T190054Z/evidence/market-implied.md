---
type: evidence_map
case_key: case-20260416-305ed3c4
dispatch_id: dispatch-case-20260416-305ed3c4-20260416T190054Z
research_run_id: 19e691be-89c6-4aca-a941-a51c15bcecb3
analysis_date: 2026-04-16
persona: market-implied
domain: crypto
subdomain: spot-market-structure
entity: ethereum
topic: will-the-binance-eth-usdt-12-00-et-1-minute-candle-on-2026-04-17-close-above-2200
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance exchange"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-305ed3c4/researcher-analyses/2026-04-16/dispatch-case-20260416-305ed3c4-20260416T190054Z/personas/market-implied.md"]
tags: ["evidence-map", "ethusdt", "binance", "market-implied"]
---

# Summary

The market is pricing a very high probability because ETH is already materially above the strike on the named venue, and the remaining question is mostly short-horizon downside risk into a single settlement minute.

## Question being evaluated

Will Binance ETH/USDT close above 2200 on the 1-minute candle labeled 12:00 ET on Apr 17, 2026?

## Current lean

Lean Yes, with high but not near-certain confidence.

## Prior / starting view

Starting view was that a 97.5% market implied probability looked extreme and required verification of both contract mechanics and current spot cushion.

## Evidence supporting the claim

- **Direct venue check: Binance spot price about 2343.56.**
  - Source: direct API pull from `/api/v3/ticker/price`
  - Why it matters: the underlying is already about 6.5% above the strike on the exact venue/pair named in the rules
  - Direct or indirect: direct
  - Weight: high

- **Recent Binance 1-minute klines show closes around 2343.1 to 2343.56.**
  - Source: direct API pull from `/api/v3/klines?symbol=ETHUSDT&interval=1m`
  - Why it matters: confirms that the relevant 1-minute close concept is currently comfortably above 2200, not just a stale last price artifact
  - Direct or indirect: direct
  - Weight: high

- **Contract wording is straightforward and exchange-specific.**
  - Source: Polymarket event page
  - Why it matters: reduces interpretive ambiguity; this is not about broad ETH price consensus, only Binance ETH/USDT 1m close at the specified minute
  - Direct or indirect: direct for mechanics
  - Weight: high

- **Binance docs describe the kline endpoint and close field clearly.**
  - Source: Binance Spot API market-data docs
  - Why it matters: helps verify the mechanics of the settlement object and the meaning of the 1-minute close
  - Direct or indirect: contextual/technical verification
  - Weight: medium

## Evidence against the claim

- **Single-minute threshold markets remain vulnerable to short-horizon volatility.**
  - Source: contract structure and general crypto microstructure
  - Why it matters: a rapid move or wick at the exact resolution minute can decide the outcome
  - Direct or indirect: indirect/contextual
  - Weight: medium

- **The market is already at an extreme probability.**
  - Source: Polymarket current price 0.975
  - Why it matters: little room for error; even modest overlooked risks can matter when a market is priced this high
  - Direct or indirect: contextual
  - Weight: medium

## Ambiguous or mixed evidence

- Binance website chart is the formal reference surface in the rules, while API verification is a practical but slightly different access surface. Usually these should align, but the distinction is worth noting.

## Conflict between inputs

There was no major factual conflict. The main tension is weighting-based: whether a ~6.5% cushion with <24h left justifies ~97.5% implied odds, or whether that still slightly overstates certainty because crypto can move fast.

## Key assumptions

- Binance spot remains broadly orderly through settlement.
- No major market shock pushes ETH down more than about 6% before noon ET.
- The website chart close and API-observed close correspond as expected.

## Key uncertainties

- Overnight/morning crypto volatility into the resolution window
- Exchange-specific disruptions or unusual wick behavior at the exact minute
- Residual ambiguity between website UI presentation and public API presentation

## Disconfirming signals to watch

- ETHUSDT breaking below 2300 and accelerating lower
- Broad crypto risk-off move before noon ET
- Binance-specific operational issues near the settlement minute

## What would increase confidence

- A fresh Binance check closer to settlement still showing ETH comfortably above 2200
- Confirmation that the Binance website chart and API kline values align on 1-minute closes

## Net update logic

Verification moved the initial impression from "maybe the market is too confident" to "the market is directionally right and only modestly aggressive." What mattered most was not generic ETH bullishness but the large current gap versus the strike on the named exchange. I downweighted generic macro commentary because this contract resolves on a specific minute print, so direct venue state matters more than broader narratives.

## Suggested downstream use

- Orchestrator synthesis input
- decision-maker review
- possible near-settlement refresh if timing permits