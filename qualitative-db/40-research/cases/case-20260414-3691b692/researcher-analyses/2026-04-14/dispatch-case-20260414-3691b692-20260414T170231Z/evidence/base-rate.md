---
type: evidence_map
case_key: case-20260414-3691b692
dispatch_id: dispatch-case-20260414-3691b692-20260414T170231Z
research_run_id: af7fa7dd-08c2-478a-a7a4-873b9c39ca03
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on 2026-04-16 above 72000?"
driver: reliability
date_created: 2026-04-14
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3691b692/researcher-analyses/2026-04-14/dispatch-case-20260414-3691b692-20260414T170231Z/personas/base-rate.md"]
tags: ["evidence-map", "threshold-market", "btc"]
---

# Summary

Net evidence supports Yes because BTC/USDT is currently above the threshold by a few thousand dollars on the source exchange, but the base-rate view is materially less bullish than the market because two-day crypto threshold-hold probabilities are not near certainty even in an improving regime.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on April 16, 2026 above 72,000?

## Current lean

Lean Yes, but less strongly than the market.

## Prior / starting view

Starting outside view: short-horizon crypto threshold markets should rarely trade near 90% unless the underlying is either much farther above the strike or the event is almost mechanically locked in.

## Evidence supporting the claim

- Direct Binance 1-minute data for the matching reference minute on April 14 closed at 75,356.48.
  - Source: Binance kline source note.
  - Why it matters: direct evidence on the correct exchange and pair, with about a 4.7% cushion over the threshold.
  - Direct or indirect: direct.
  - Weight: high.

- Recent daily closes shifted into a stronger regime, with April 10-14 clustered near or above the threshold.
  - Source: Binance kline source note.
  - Why it matters: suggests the market is not relying on a one-off spike.
  - Direct or indirect: direct/contextual.
  - Weight: medium.

- Recent ET-noon-equivalent observations were above 72,000 on April 9, 10, 11, and 14.
  - Source: Binance kline source note.
  - Why it matters: directly relevant to the exact contract timing convention.
  - Direct or indirect: direct.
  - Weight: medium.

## Evidence against the claim

- The same recent noon-ET comparison point fell below 72,000 on April 12 and April 13, showing the threshold is not securely held yet.
  - Source: Binance kline source note.
  - Why it matters: strongest direct disconfirmation against a near-certain Yes view.
  - Direct or indirect: direct.
  - Weight: high.

- Minute-level share above 72,000 across April 1-14 was only about 22.3%, showing how recent and regime-dependent the move is.
  - Source: Binance kline source note.
  - Why it matters: long-enough recent sample argues against complacency.
  - Direct or indirect: direct/contextual.
  - Weight: medium.

- Contract resolves at one exact minute, so path volatility matters more than general bullishness.
  - Source: Polymarket rules note.
  - Why it matters: even a bullish BTC path can still fail at the specified instant.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.

## Ambiguous or mixed evidence

- Current buffer above 72,000 is meaningful but not overwhelming by crypto standards; a routine multi-percent move could erase it.
- The market price may reflect some momentum persistence, but it may also be overweighting the fresh breakout.

## Conflict between inputs

There is no major factual conflict between sources. The main disagreement is between the market's implied confidence and the outside-view interpretation of how often a two-day threshold hold actually survives in a volatile asset.

## Key assumptions

- Binance API data is a valid verification proxy for the Binance chart surface named in the contract.
- The current bullish regime is informative enough to justify a Yes lean but not enough to justify near-certainty.

## Key uncertainties

- Short-horizon BTC volatility over the next roughly 47 hours.
- Any exchange-specific deviation or operational oddity near the exact resolution minute.
- Whether recent breakout momentum persists or mean-reverts.

## Disconfirming signals to watch

- Sustained trade back below 72,000 before April 15 close.
- Repeated failures to defend low-72k on Binance.
- Market-wide risk-off shock.

## What would increase confidence

- Continued Binance trading above 74,000 through April 15.
- Another noon-ET-equivalent reference point above 72,000 on April 15.
- Independent secondary chart source matching the Binance level without discrepancy.

## Net update logic

The outside view starts below the market because a volatile asset clearing a point-in-time threshold two days ahead is rarely a 90% event unless deeply in the money. Direct Binance observations move the estimate above 50% because BTC is already above 72,000 by a noticeable margin and has recently spent more time above that level. But the recent record includes very fresh failures at the same reference time, so the correct update is to Yes with caution, not to near-certainty.

## Suggested downstream use

Use as forecast update and Orchestrator synthesis input; especially useful as a check against overconfident market anchoring.