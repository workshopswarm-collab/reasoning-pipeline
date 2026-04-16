---
type: assumption_note
case_key: case-20260416-a8277fc8
dispatch_id: dispatch-case-20260416-a8277fc8-20260416T001420Z
research_run_id: 11a62521-e945-4f29-906d-350ae46533b5
analysis_date: 2026-04-16
persona: variant-view
domain: crypto
subdomain: daily-close-thresholds
entity: sol
topic: "Noon-specific close risk despite current spot cushion"
question: "Will the Binance SOL/USDT 1-minute candle at 12:00 ET on 2026-04-19 close above $80?"
driver: operational-risk
date_created: 2026-04-16
agent: variant-view
status: active
certainty: medium
importance: high
time_horizon: short
related_entities: ["binance", "sol", "solana"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-source-notes/2026-04-16-variant-view-binance-sol-price-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/variant-view.md"]
tags: ["assumption", "noon-close", "binance", "sol"]
---

# Assumption

Even though SOL is currently above $80 on Binance, the probability of finishing above $80 on the specific Apr 19 12:00 ET one-minute close is meaningfully lower than the probability implied by a simple "already above threshold" framing.

## Why this assumption matters

The market is already pricing roughly 88.5% Yes. The variant case depends on the idea that traders may be partially compressing the distinction between being above $80 now and being above $80 at one exact future minute close.

## What this assumption supports

- A modestly lower-than-market Yes estimate rather than matching the market exactly.
- Emphasis on contract interpretation and timing-specific fragility instead of treating current spot as near-settlement proof.

## Evidence or logic behind the assumption

- The rules require a single exact one-minute candle close at noon ET on Apr 19.
- Short-dated crypto prices can move several percent over multi-day windows.
- Current cushion above threshold is material but not enormous: about 5.9% using the 84.74 spot check.
- Near-threshold close markets are less forgiving than touch/high markets, so timing risk is real even when the underlying path is generally favorable.

## What would falsify it

- If SOL materially extends upward, e.g. into the high 80s or 90s, this timing-specific fragility becomes much less important.
- If fresh evidence shows the market historically settles close-above contracts with very low deviation from spot several days out in similar volatility conditions, the assumed haircut would be too conservative.

## Early warning signs

- Sustained price weakness back toward low 80s or below before Apr 19.
- Broader crypto risk-off moves reducing the current cushion.
- Exchange-specific dislocations on Binance SOL/USDT relative to other venues.

## What changes if this assumption fails

If noon-specific close risk is smaller than assumed, the fair Yes probability should move closer to the market or above it.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-a8277fc8/researcher-analyses/2026-04-16/dispatch-case-20260416-a8277fc8-20260416T001420Z/personas/variant-view.md