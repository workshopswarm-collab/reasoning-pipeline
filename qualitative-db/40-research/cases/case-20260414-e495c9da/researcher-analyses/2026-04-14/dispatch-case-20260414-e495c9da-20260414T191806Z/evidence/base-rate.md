---
type: evidence_map
case_key: case-20260414-e495c9da
dispatch_id: dispatch-case-20260414-e495c9da-20260414T191806Z
research_run_id: bb3aa5ae-c532-47e8-a68c-d27624da9881
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-19
question: "Will the price of Bitcoin be above $70,000 on April 19?"
driver: reliability
date_created: 2026-04-14
agent: base-rate
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["base-rate", "bitcoin", "threshold-market"]
---

# Summary
The evidence nets to a high-probability Yes view, but not to certainty. The dominant mechanism is simple regime persistence: BTC is already above the threshold on the governing venue. The main counterweight is that the contract resolves at one exact minute, so short-horizon volatility still matters.

## Question being evaluated
Will the Binance BTC/USDT 12:00 ET one-minute candle on April 19 close above 70,000?

## Current lean
Yes, with a high but sub-market probability.

## Prior / starting view
A generic outside-view prior for a 5-day Bitcoin threshold market near the current spot level would be materially lower than 90% because BTC can move several percent over a few days.

## Evidence supporting the claim
- Binance settlement venue currently around 74k and recent daily closes mostly above 70k.
  - direct
  - high weight
  - matters because the governing venue already sits comfortably above threshold.
- CoinGecko and Yahoo Finance cross-check the same recent 70k+ regime.
  - indirect/contextual
  - medium weight
  - matters because it reduces concern that the Binance picture is a one-feed artifact.
- Short horizon to resolution means absent a catalyst, persistence is a reasonable prior.
  - inferential
  - medium weight
  - matters because many threshold markets over short windows are dominated by regime continuity.

## Evidence against the claim
- BTC was in the mid/high 60ks within the last few weeks, so sub-70k is clearly reachable.
  - contextual
  - medium-high weight
- Contract resolves on one exact minute, not a daily average or weekly close.
  - direct contract interpretation
  - high weight
- Weekend / macro shock risk can produce sharp downside moves larger than the current cushion.
  - indirect
  - medium weight

## Ambiguous or mixed evidence
- The market price near 89.5% may reflect informed traders correctly pricing persistence, or may slightly overstate confidence because thresholds near spot can look safer than they are.

## Conflict between inputs
No major factual conflict. The issue is weighting: direct venue price supports Yes strongly, while recent realized volatility argues against treating Yes as almost locked.

## Key assumptions
- No severe downside shock before Apr 19 noon ET.
- Binance remains a usable and representative settlement venue.
- Recent regime persistence is more informative than the earlier sub-70k prints.

## Key uncertainties
- Exact noon ET print versus surrounding price path.
- Weekend volatility.
- Any exchange-specific operational or liquidity dislocation.

## Disconfirming signals to watch
- BTC/USDT breaking back below 72k, then 70k, before the weekend ends.
- Sudden macro risk-off move.
- Large divergence between Binance and broader BTC spot references.

## What would increase confidence
- Additional days holding above 72k on Binance.
- Lower realized volatility into Apr 18-19.
- Confirmation that the target minute sits well above 70k on other nearby dated threshold markets.

## Net update logic
The outside-view prior starts from Bitcoin being volatile enough that a 5-day binary threshold should not default to certainty. But the current direct evidence is strong: the settlement venue is already ~6% above threshold, and independent sources confirm the same regime. That moves the estimate to a high Yes probability, though not all the way to the market because the exact-minute contract structure leaves meaningful path risk.

## Suggested downstream use
forecast update
