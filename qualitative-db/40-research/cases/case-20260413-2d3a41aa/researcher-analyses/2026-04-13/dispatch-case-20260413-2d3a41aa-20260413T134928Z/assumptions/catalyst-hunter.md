---
type: assumption_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
research_run_id: 9d65b404-2833-4335-9cf4-b4e8281e1a41
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-13
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-13 close above 70000?"
driver: operational-risk
date_created: 2026-04-13
agent: catalyst-hunter
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/catalyst-hunter.md"]
tags: ["assumption-note", "intraday", "timing", "bitcoin"]
---

# Assumption

BTC can avoid a greater-than-roughly-2 percent intraday selloff before the Binance BTC/USDT 12:00 ET candle closes.

## Why this assumption matters

The research view depends less on long-run Bitcoin fundamentals than on whether there is enough short-horizon path stability to preserve an already-above-threshold price into the exact settlement minute.

## What this assumption supports

- A Yes-leaning probability above the market-implied 71%
- The claim that the dominant catalyst is absence of a sharp negative shock, not discovery of a new bullish catalyst
- The view that contract mechanics and timing matter more than broad directional Bitcoin conviction here

## Evidence or logic behind the assumption

- BTC was trading around 71.4k during research, leaving roughly 1.4k of buffer above the threshold.
- Recent 240-minute Binance data showed modest average one-minute realized movement and no evidence in this sample of a sustained collapse larger than the required threshold.
- No specific imminent scheduled event was identified in the brief contextual pass that would obviously force a repricing larger than the buffer before noon ET.

## What would falsify it

- A macro headline, exchange shock, liquidation cascade, or correlated risk-off move that pushes BTC below 70k into the noon ET minute
- Evidence of a scheduled market-moving release before noon ET that was missed in the initial pass
- Binance-specific trading disruption that affects the reported candle or contract interpretation

## Early warning signs

- BTC losing the 71k handle decisively and failing to recover
- Abrupt rise in one-minute realized volatility or liquidation-driven wicks
- Material divergence between Binance BTCUSDT and broader crypto tape suggesting venue-specific stress

## What changes if this assumption fails

The probability should move sharply toward No, because this contract is threshold-and-minute specific rather than based on any average or end-of-day recovery.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/catalyst-hunter.md
- qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-source-notes/2026-04-13-catalyst-hunter-binance-polymarket.md