---
type: evidence_map
case_key: case-20260416-f29db686
dispatch_id: dispatch-case-20260416-f29db686-20260416T004058Z
research_run_id: 98495dac-9c0c-499a-8239-ecb00277f89b
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-74-000-on-april-17
question: "Will the price of Bitcoin be above $74,000 on April 17?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low-direct-conflict
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-f29db686/researcher-analyses/2026-04-16/dispatch-case-20260416-f29db686-20260416T004058Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "timing-risk", "binance"]
---

# Summary

Evidence nets to a modest Yes lean, but the contract is fragile because it settles on one exact Binance minute close tomorrow at noon ET rather than on a broader daily close.

## Question being evaluated

Whether the Binance BTC/USDT 1-minute candle for 12:00 ET on Apr 17 closes above 74,000.

## Current lean

Lean Yes, but with meaningful path and timing risk.

## Prior / starting view

Starting baseline is the market-implied probability of about 60.5% from the assignment.

## Evidence supporting the claim

- **Current Binance spot is above strike**
  - source: Binance public API captured during run; source note
  - why it matters: the market is currently starting from the right side of the threshold
  - direct or indirect: direct contextual evidence on the exact venue/pair
  - weight: medium-high

- **Recent 1-minute Binance closes in sampled window were above 74,000**
  - source: Binance public API klines captured during run; source note
  - why it matters: confirms the immediate local regime is above strike on the relevant venue and timeframe
  - direct or indirect: direct contextual evidence
  - weight: medium

- **Polymarket pricing also centers this contract as a modest favorite**
  - source: assignment current_price and fetched market page
  - why it matters: useful crowd baseline and check against overreacting
  - direct or indirect: indirect market-structure evidence
  - weight: low-medium

## Evidence against the claim

- **Single-minute settlement design creates large timing risk**
  - source: Polymarket rules; source note
  - why it matters causally: the contract can fail on a brief dip at exactly noon ET even if BTC is generally firm
  - direct or indirect: direct rule evidence
  - weight: high

- **Spot cushion over strike is only about 1% at time of review**
  - source: Binance API and arithmetic from current spot versus strike
  - why it matters causally: a small cushion is easily erased in BTC over ~15 hours
  - direct or indirect: direct contextual evidence
  - weight: high

- **Settlement is tomorrow, not now**
  - source: contract date/time from assignment and rules
  - why it matters causally: overnight and US-session volatility still has time to matter
  - direct or indirect: direct rule/timing evidence
  - weight: high

## Ambiguous or mixed evidence

- The Binance front-end candle widget named in the rules was not directly extracted through web fetch, but Binance public API supplied relevant same-venue spot and kline context. Usually that alignment is fine, but the contractual source is the front-end chart interface.

## Conflict between inputs

There is no major factual conflict. The main issue is weighting: current spot above strike argues Yes, while the narrow timing mechanics argue for lower confidence than a generic daily directional bet would justify.

## Key assumptions

- Current above-strike trading remains informative into tomorrow's noon ET settlement minute.
- Binance public API and chart-surface close values will align in ordinary conditions.
- No exchange-specific incident or sudden volatility shock dominates the settlement window.

## Key uncertainties

- BTC path over the next ~15 hours.
- Whether noon ET prints a transient dip below strike even if broader price remains constructive.
- Whether US-session volatility materially increases before settlement.

## Disconfirming signals to watch

- Sustained loss of 74,500 before settlement.
- Any move back below 74,000 on Binance with momentum.
- Exchange-specific data or execution irregularities.

## What would increase confidence

- Sustained Binance trading materially above strike, especially above 75,500.
- Lower realized volatility into the settlement window.
- Continued Binance 1-minute closes above strike through late morning ET on Apr 17.

## Net update logic

The evidence does not justify a strong deviation from market. Current venue-specific spot above strike supports a Yes lean, but the narrow one-minute settlement mechanics sharply limit confidence. The risk-manager update is therefore to keep probability only modestly above 50 rather than treating current spot as near-settling evidence.

## Suggested downstream use

Use as an orchestrator synthesis input emphasizing that the main underpriced risk is not broad crypto thesis failure but single-minute timing fragility on the exact Binance settlement surface.