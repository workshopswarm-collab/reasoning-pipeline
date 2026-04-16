---
type: evidence_map
case_key: case-20260416-969f7c01
dispatch_id: dispatch-case-20260416-969f7c01-20260416T013210Z
research_run_id: 810c1ece-82f1-479d-9fb3-d4c2b39fb0eb
analysis_date: 2026-04-16
persona: base-rate
domain: crypto
subdomain: spot-price-threshold-markets
entity: ethereum
topic: ethereum-above-2200-on-april-17
question: "Will the Binance ETH/USDT 12:00 ET one-minute candle on 2026-04-17 close above 2200?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "eth", "binance", "threshold-market"]
---

# Summary

This case is mostly a short-horizon spot-threshold problem with narrow settlement mechanics. The base-rate lean is Yes because ETH/USDT is currently trading well above 2200 and the remaining window is short, but the one-minute Binance-close structure prevents certainty.

## Question being evaluated

Will Binance's ETH/USDT 1-minute candle for 12:00 ET on Apr 17, 2026 close above 2200?

## Current lean

Lean Yes, high but not near-certain.

## Prior / starting view

Before current-source checking, the outside-view prior for a major crypto asset already trading materially above a strike less than a day before a single-minute threshold check is favorable to Yes, but not equivalent to the current spot percentage cushion because crypto intraday volatility can be large.

## Evidence supporting the claim

- Polymarket contract rules define a simple threshold: strict close above 2200 on Binance ETH/USDT at the specified minute.
  - Source: case source note on rules.
  - Why it matters: removes many alternative interpretations and says the event is fundamentally a price-level question.
  - Direct or indirect: direct.
  - Weight: high.

- Contextual price checks place ETH/USDT around 2350+ during the research window.
  - Source: Binance search result snippet and CoinMarketCap live converter/history page.
  - Why it matters: gives a cushion of roughly 150 points, around 6-7%, above the strike with less than a day to go.
  - Direct or indirect: indirect for settlement, direct for current market state.
  - Weight: high.

- Recent daily ETH/USDT context is mostly above 2200 over the preceding week.
  - Source: CoinMarketCap daily history table.
  - Why it matters: suggests the strike is not at the edge of the recent distribution.
  - Direct or indirect: indirect.
  - Weight: medium.

## Evidence against the claim

- One listed recent daily close from Apr 12 was below 2200 at roughly 2192.47.
  - Source: CoinMarketCap history table.
  - Why it matters: shows that sub-2200 prints are still inside the nearby realized range; a sharp move is not absurd.
  - Direct or indirect: indirect.
  - Weight: medium.

- The contract resolves on a single one-minute close, not a daily average or broad market composite.
  - Source: Polymarket rules.
  - Why it matters: a temporary selloff exactly into the resolution minute is sufficient for No.
  - Direct or indirect: direct.
  - Weight: medium-high.

- Clean live extraction from Binance was not available through the fetch tool.
  - Source: research process limitation.
  - Why it matters: increases operational/verification uncertainty slightly.
  - Direct or indirect: indirect.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- Market price of 94.5% is itself evidence of crowd confidence, but it may also slightly overstate certainty for a volatile asset and a single-minute condition.

## Conflict between inputs

There was no major factual conflict. The main tension is between current spot cushion favoring Yes and the narrow single-minute settlement structure preserving tail risk.

## Key assumptions

- Binance ETH/USDT remains normally functioning through settlement.
- Noon ET maps to the intended Binance one-minute candle without rule surprise.
- No large downside catalyst hits ETH before the resolution window.

## Key uncertainties

- Exact realized volatility between now and noon ET Apr 17.
- Whether any venue-specific issue appears on Binance near the decision minute.
- Whether the current premium above 2200 narrows sharply overnight.

## Disconfirming signals to watch

- ETH/USDT falling toward the low-2200s or below before the morning of Apr 17.
- Broad crypto risk-off move led by BTC or macro shock.
- Binance-specific operational irregularity.

## What would increase confidence

- A fresh Binance or independent aggregator check on Apr 17 morning still showing ETH comfortably above 2200.
- Continued market stability with no exchange-specific disruptions.

## Net update logic

The prior started favorable because the asset was already above the strike close to resolution. Current-source checks kept that lean and strengthened it somewhat by showing a substantial cushion and mostly above-threshold recent context. I downweighted the near-certainty implied by the market because crypto can move several percent quickly and the contract only needs one bad minute.

## Suggested downstream use

Use as an orchestrator synthesis input and forecast update input. Low need for broad follow-up unless the price approaches the threshold before noon ET on Apr 17.
