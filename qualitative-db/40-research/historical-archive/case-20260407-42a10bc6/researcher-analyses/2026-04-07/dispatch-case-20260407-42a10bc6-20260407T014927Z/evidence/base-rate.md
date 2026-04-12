---
type: evidence_map
case_key: case-20260407-42a10bc6
dispatch_id: dispatch-case-20260407-42a10bc6-20260407T014927Z
research_run_id: 57bcf933-ab20-444e-9cb2-073348dc6477
analysis_date: 2026-04-07
persona: base-rate
domain: crypto
subdomain: exchange-market-structure
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-7
question: "Will the price of Bitcoin be above $68,000 on April 7?"
driver: reliability
date_created: 2026-04-06
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin", "binance"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-42a10bc6/researcher-analyses/2026-04-07/dispatch-case-20260407-42a10bc6-20260407T014927Z/personas/base-rate.md"]
tags: ["base-rate", "threshold-market", "intraday-volatility"]
---

# Summary

This market is a narrow threshold question on a single Binance 1-minute candle at noon ET. The base-rate issue is whether being modestly above the line hours before settlement should be priced as strong favorite or only moderate favorite.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-07 have a final close above 68000?

## Current lean

Lean Yes, but not as strongly as the market.

## Prior / starting view

Before checking live price context, a generic outside view for a same-day noon threshold market would start near 50% unless spot was materially far from the threshold.

## Evidence supporting the claim

- Direct current Binance spot was 68485.64, already above the threshold.
  - direct source
  - matters because the market only needs price to remain above 68000 at one specific minute close
  - deserves high weight
- Binance 24h high was 70351.46.
  - direct source
  - matters because it shows the threshold is not an extreme upside target for the current regime
  - deserves medium weight
- Polymarket market price around 70% indicates other traders also see above-threshold persistence as more likely than not.
  - contextual source
  - not independent from market sentiment, so moderate weight only

## Evidence against the claim

- The edge above threshold is small: about 485.64 dollars or roughly 0.71%.
  - direct arithmetic from current price and threshold
  - matters because BTC can easily move that much intraday
  - deserves high weight
- Binance 24h low was 68300.00, only about 300 dollars above the threshold.
  - direct source
  - matters because it shows the market has already been near the line and could plausibly trade below it before noon ET
  - deserves medium-high weight
- Settlement depends on one exact minute close rather than average trading over a window.
  - direct contract mechanic
  - matters because it increases path sensitivity and noise
  - deserves high weight

## Ambiguous or mixed evidence

- The market-implied probability itself is informative but not independent; it may aggregate real information or may overstate persistence from current spot.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much should current spot above threshold dominate versus ordinary intraday volatility for a one-minute close several hours away?

## Key assumptions

- Noon ET correctly maps to 16:00 UTC on this date.
- The relevant candle is the Binance BTCUSDT 1m candle associated with 16:00 UTC.
- No Binance data/presentation anomaly changes the visible final close used for settlement.

## Key uncertainties

- Short-horizon BTC path from late evening ET to noon ET
- Whether overnight/morning macro or crypto-specific flow pushes BTC decisively above or below the threshold

## Disconfirming signals to watch

- Sustained move below 68000 before the morning ET session
- Repeated rejection near 68500-69000 without reclaim
- Any sign that Polymarket or Binance interface interpretation of the noon candle differs from the straightforward UTC conversion

## What would increase confidence

- Additional Binance price action showing persistent holding above 68000 into the morning ET session
- A verified screenshot or direct interface check at settlement time confirming the exact candle mapping

## Net update logic

Starting from a near-even same-day threshold prior, current spot above 68000 shifts the probability above 50%. But because the gap is small and the settlement is a single 1-minute close hours ahead, the market’s 70% Yes price looks somewhat rich versus a disciplined outside-view estimate.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- retrospective evaluation of how much same-day threshold markets should discount spot-above-line conditions