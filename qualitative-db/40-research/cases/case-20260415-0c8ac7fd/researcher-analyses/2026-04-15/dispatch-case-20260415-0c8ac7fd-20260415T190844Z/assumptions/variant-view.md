---
type: assumption_note
case_key: case-20260415-0c8ac7fd
research_run_id: 6657a49e-464e-43a5-bd73-34022327a92c
analysis_date: 2026-04-15
persona: variant-view
domain: crypto
subdomain: bitcoin-threshold-close-market
entity: bitcoin
topic: "single-minute timestamp risk remains material even when BTC trades above threshold beforehand"
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: variant-view
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-17T12:00:00-04:00"
related_entities: ["bitcoin"]
related_drivers: ["reliability"]
proposed_entities: []
proposed_drivers: ["threshold-close timing risk"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-variant-view-polymarket-rules-and-market.md", "qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-source-notes/2026-04-15-variant-view-binance-direct-price-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/variant-view.md"]
tags: ["assumption", "noon-close", "path-risk", "bitcoin"]
dispatch_id: dispatch-case-20260415-0c8ac7fd-20260415T190844Z
---

# Assumption

Even with BTC currently above 72,000, the probability of finishing above that threshold at the exact Binance BTC/USDT 12:00 ET one-minute close on Apr 17 is meaningfully lower than a naive trend-following read would imply.

## Why this assumption matters

The entire variant thesis depends on the contract being a **timestamped close** market rather than a generic bullish-BTC market. If exact-minute timing risk is small enough to ignore, then the market’s 87% price is probably fair or even conservative.

## What this assumption supports

- A modestly lower probability estimate than the market.
- Emphasis on timing/path dependency rather than broad directional BTC conviction.
- The claim that the market may be slightly overconfident because traders can blur “currently above threshold” with “will be above threshold at the exact governing minute.”

## Evidence or logic behind the assumption

- Polymarket’s rules explicitly use a single Binance BTC/USDT 1-minute candle close at **Apr 17 12:00 ET**.
- Direct Binance data shows BTC is above threshold now, but also that intraday movement of hundreds of dollars is routine.
- The threshold buffer versus current spot is only around **3% to 3.7%**, which is comfortable but not so large that a two-day reversal is implausible in BTC.
- The prior case review on similar crypto threshold markets warns against confusing mechanism types; touch-style and exact-close markets should not be priced the same way.

## What would falsify it

- Evidence that BTC remains persistently far above 72k into Apr 17 morning with a much larger safety buffer, reducing noon-close risk to a very low level.
- A strong new macro/crypto catalyst that materially lowers near-term downside risk before the deadline.
- Historical/contextual evidence showing noon-close deviations of this magnitude are rarer than assumed under current volatility conditions.

## Early warning signs

- BTC extends materially above 75k-76k and holds there through multiple sessions.
- Realized volatility compresses sharply while spot remains well above 72k.
- Market structure or flows show strong support specifically into US midday trading hours.

## What changes if this assumption fails

If exact-minute timing risk is smaller than assumed, the fair probability should move up toward the market or above it, and the disagreement case largely disappears.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260415-0c8ac7fd/researcher-analyses/2026-04-15/dispatch-case-20260415-0c8ac7fd-20260415T190844Z/personas/variant-view.md