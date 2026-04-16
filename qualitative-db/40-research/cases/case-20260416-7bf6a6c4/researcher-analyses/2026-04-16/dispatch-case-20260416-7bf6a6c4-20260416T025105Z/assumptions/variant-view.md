---
type: assumption_note
case_key: case-20260416-7bf6a6c4
dispatch_id: dispatch-case-20260416-7bf6a6c4-20260416T025105Z
research_run_id: d9390331-d5ea-4393-9f6e-c636a3f328c3
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close
entity: bitcoin
topic: "noon-close path dependence is tighter than a generic above-threshold framing suggests"
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle on April 17 close above 74000?"
driver: reliability
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "<24h"
related_entities: ["bitcoin"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: ["threshold-proximity", "timestamp-close-fragility"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-variant-view-polymarket-rules-and-market-snapshot.md", "qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-source-notes/2026-04-16-variant-view-binance-api-spot-and-recent-1m-context.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/variant-view.md"]
tags: ["assumption", "noon-close", "path-dependence", "btc"]
---

# Assumption

The market is slightly overpricing Yes because traders may be anchoring to BTC being currently above 74,000 while underweighting the stricter requirement of staying above that line on the exact Binance 12:00 ET 1-minute close tomorrow.

## Why this assumption matters

The whole variant case depends on the distinction between a broad directional bullish stance and a precise timestamp-close requirement. If that distinction does not deserve a discount, then the market's Yes price is probably fair or even cheap.

## What this assumption supports

- A modestly lower-than-market Yes probability.
- A view that the contract is more fragile than a generic “BTC above 74k tomorrow” framing implies.
- Emphasis on exact resolution mechanics rather than narrative momentum alone.

## Evidence or logic behind the assumption

- The Polymarket rules explicitly require the **final Close** of the **12:00 ET** Binance 1-minute candle, not a touch or session-wide average.
- Recent Binance 1-minute data shows BTC above the threshold but drifting lower over several consecutive minutes at snapshot time.
- Short-dated crypto prices can move hundreds of dollars intraday, so an ~860-point cushion is helpful but not overwhelming over the remaining time window.

## What would falsify it

- Strong evidence that BTC has held comfortably and persistently above 74k through the U.S. morning on April 17.
- A materially larger cushion above 74k with low realized volatility into the settlement window.
- New information showing the market already incorporated the exact close-vs-touch distinction correctly.

## Early warning signs

- BTC extends well above 75k and holds there overnight.
- Market probability rises while venue-specific data shows stable support rather than mean reversion risk.
- Correlated crypto/macro conditions turn decisively risk-on into the settlement window.

## What changes if this assumption fails

The variant edge largely disappears. The correct stance would move toward agreeing with or even slightly exceeding the market-implied probability.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-7bf6a6c4/researcher-analyses/2026-04-16/dispatch-case-20260416-7bf6a6c4-20260416T025105Z/personas/variant-view.md