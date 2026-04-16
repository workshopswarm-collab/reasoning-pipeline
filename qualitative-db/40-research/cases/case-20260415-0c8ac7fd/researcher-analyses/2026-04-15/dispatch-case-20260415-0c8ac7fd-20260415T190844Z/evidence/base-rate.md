---
type: evidence_map
case_key: case-20260415-0c8ac7fd
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
research_run_id: 50fa720d-a864-40e4-8184-6a9f5b56bbba
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "April 17 noon ET BTC close-above-72000 evidence netting"
question: "Will Binance BTC/USDT close above 72000 on the 12:00 ET one-minute candle on April 17, 2026?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: "forecast update"
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-base-rate-binance-polymarket-resolution-and-price.md", "qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/assumptions/base-rate.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/base-rate.md"]
tags: ["evidence-map", "btc", "threshold-close"]
---

# Summary

The evidence leans Yes because BTC is already trading comfortably above 72,000 and has done so repeatedly in recent Binance trading, but the contract is a precise close-above event at a single minute rather than a touch market, so short-horizon volatility still matters.

## Question being evaluated

Will Binance BTC/USDT close above 72,000 on the 12:00 ET one-minute candle on April 17, 2026?

## Current lean

Lean Yes, but less aggressively than the market.

## Prior / starting view

Starting outside view: if BTC were already several percent above a nearby threshold with only two days left, Yes should be favored, but a close-specific rule should trade below a touch-style contract with the same threshold.

## Evidence supporting the claim

- **Current Binance price is above threshold by ~3.7% to 3.8%**
  - Source: direct Binance API price and avgPrice checks
  - Why it matters: the event does not require a rally from below; it requires persistence
  - Direct/indirect: direct contextual evidence, not direct settlement evidence
  - Weight: high

- **Recent Binance daily trading repeatedly exceeded 72,000 and closed above it on several days**
  - Source: Binance daily klines for recent sessions
  - Why it matters: above-threshold trading appears persistent rather than momentary
  - Direct/indirect: contextual
  - Weight: medium-high

- **Contract threshold is not far below current spot**
  - Source: Polymarket rules plus Binance price context
  - Why it matters: only a moderate pullback is needed for No, but no upward breakout is needed for Yes
  - Direct/indirect: mixed
  - Weight: medium

## Evidence against the claim

- **The contract is about one exact one-minute close, not a touch/high or daily close**
  - Source: Polymarket rules page
  - Why it matters: precision raises failure probability relative to a looser threshold market
  - Direct/indirect: direct contract-mechanics evidence
  - Weight: high

- **BTC short-horizon volatility can erase a 3% to 4% cushion in two days**
  - Source: generic BTC outside view plus recent daily ranges in Binance data
  - Why it matters: the current cushion is meaningful but not enormous for BTC
  - Direct/indirect: contextual
  - Weight: medium-high

## Ambiguous or mixed evidence

- **Recent strong BTC level around 74k-76k** is supportive, but if this is a temporary momentum burst, the current level may overstate persistence odds.
- **Market price at 87%** could reflect informed traders correctly pricing short-dated persistence; it could also modestly overstate confidence in a close-specific setup.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much to discount from current above-threshold price because settlement depends on one precise minute.

## Key assumptions

- Current above-threshold trading is reasonably persistent through April 17 noon ET.
- No major negative shock hits BTC before the governing minute.
- Binance remains the relevant and usable resolution surface.

## Key uncertainties

- Exact intraday BTC path into April 17 noon ET
- Whether market participants are underpricing close-specific fragility
- Whether any sudden risk-off move occurs before settlement

## Disconfirming signals to watch

- BTC/USDT breaks back below 72,000 on Binance before April 17
- Sharp deterioration in crypto risk sentiment on April 16-17
- Meaningful basis or venue-specific dislocation on Binance

## What would increase confidence

- A fresh direct Binance check late on April 16 or morning of April 17 still showing BTC comfortably above 72,000
- Continued multi-hour stability above the threshold

## Net update logic

The outside-view prior begins with "already above threshold, short horizon, so Yes favored." The main downward adjustment is contract precision: a single-minute close is stricter than a touch market. That leaves a Yes probability meaningfully above 50% but somewhat below the market's 87%.

## Suggested downstream use

Use this as a forecast input for synthesis, with special attention to the distinction between current above-threshold state and final governing-minute close risk.