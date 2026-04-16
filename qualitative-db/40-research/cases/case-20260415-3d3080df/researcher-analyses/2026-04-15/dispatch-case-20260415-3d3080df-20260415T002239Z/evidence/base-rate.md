---
type: evidence_map
case_key: case-20260415-3d3080df
dispatch_id: dispatch-case-20260415-3d3080df-20260415T002239Z
research_run_id: ac95181d-697f-4ec0-844c-dd432b46037f
analysis_date: 2026-04-15
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: reliability
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-3d3080df/researcher-analyses/2026-04-15/dispatch-case-20260415-3d3080df-20260415T002239Z/personas/base-rate.md"]
tags: ["evidence-map", "base-rate", "bitcoin"]
---

# Summary

Base-rate netting favors Yes because BTC is already trading materially above 70k on the governing exchange with only a five-day path to resolution, but the market is probably a bit too confident given BTC's ability to move more than 6% over short windows and the contract's exact-minute settlement sensitivity.

## Question being evaluated

Whether Binance BTC/USDT will have a final close above 70,000 on the 12:00 ET one-minute candle on April 20, 2026.

## Current lean

Yes lean, but less extreme than market pricing.

## Prior / starting view

Starting outside-view prior: once BTC is already ~6% above a threshold with less than a week to go, Yes should be favored; however, crypto short-horizon volatility and exact-minute settlement make sub-90% confidence more appropriate than a near-lock.

## Evidence supporting the claim

- Binance spot is around 74.5k during the research pass.
  - Source: 2026-04-15-base-rate-binance-market-data.md
  - Why it matters causally: current distance from strike is the main structural input.
  - Direct or indirect: direct.
  - Weight: high.

- Recent Binance daily closes show BTC mostly above 70k in the latest stretch.
  - Source: 2026-04-15-base-rate-binance-market-data.md
  - Why it matters causally: suggests the threshold is not a fresh breakout level but a recently occupied zone.
  - Direct or indirect: direct/contextual hybrid.
  - Weight: medium-high.

- The contract resolves on Binance BTC/USDT itself, so there is no cross-exchange basis risk if Binance stays operational.
  - Source: 2026-04-15-base-rate-polymarket-rules.md
  - Why it matters causally: reduces ambiguity around what price matters.
  - Direct or indirect: direct for rules.
  - Weight: medium.

## Evidence against the claim

- BTC is volatile enough that a >6% drop over five days is entirely plausible.
  - Source: implied by recent Binance daily ranges and 24h range in source notes.
  - Why it matters causally: current cushion is meaningful but not huge for crypto.
  - Direct or indirect: contextual.
  - Weight: high.

- Settlement is based on one exact one-minute close at noon ET, not a broader daily average or end-of-day close.
  - Source: 2026-04-15-base-rate-polymarket-rules.md
  - Why it matters causally: a brief downtick at the wrong minute can flip the result even if BTC is above 70k for much of the day.
  - Direct or indirect: direct.
  - Weight: medium-high.

- Market pricing is already at ~85-86%, leaving limited edge unless one thinks short-horizon downside and operational/timing noise are overdiscounted.
  - Source: 2026-04-15-base-rate-polymarket-rules.md
  - Why it matters causally: extreme odds require stronger verification and make overconfidence more likely.
  - Direct or indirect: direct.
  - Weight: medium.

## Ambiguous or mixed evidence

- The recent trend is upward enough to support Yes, but BTC has also shown quick multi-thousand-dollar swings inside the same 30-day sample.
- Binance API documentation improves confidence in how one could verify the relevant candle, but it does not eliminate last-mile UI or exchange-specific operational quirks.

## Conflict between inputs

There is no major factual conflict. The tension is weighting-based: current spot and recent closes support Yes, while volatility and exact-minute rules argue against treating Yes as nearly certain.

## Key assumptions

- No major market shock before April 20 noon ET.
- Binance remains a reliable settlement source without disruptive outage or data ambiguity.
- Recent occupancy above 70k is more informative than isolated downside excursions from late March.

## Key uncertainties

- How much realized BTC volatility persists over the next five days.
- Whether macro or crypto-specific news injects a sharp downside move.
- Whether noon ET on April 20 lands during a transient downtick even if the broader level remains above 70k.

## Disconfirming signals to watch

- BTC losing 72k and then 70k on Binance before the event.
- A visible increase in downside momentum or volatility clustering.
- Any Binance market-data or charting irregularity near the resolution window.

## What would increase confidence

- BTC remaining above 73k-74k into April 18-19.
- Continued Binance daily closes above 70k.
- No exchange-specific operational issues or contract-interpretation disputes.

## Net update logic

The main update from a generic crypto prior is that the threshold is already below current spot on the exact settlement exchange. That strongly favors Yes. The main reason not to simply match the market is that this is still crypto over a five-day window with an exact-minute resolution mechanic, so there remains a real path to a sub-70k print at the decisive minute.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input; no major follow-up investigation appears necessary unless BTC volatility spikes or settlement-source ambiguity emerges.