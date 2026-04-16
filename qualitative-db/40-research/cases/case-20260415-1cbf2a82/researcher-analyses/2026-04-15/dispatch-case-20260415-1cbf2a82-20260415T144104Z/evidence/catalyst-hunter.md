---
type: evidence_map
case_key: case-20260415-1cbf2a82
dispatch_id: dispatch-case-20260415-1cbf2a82-20260415T144104Z
research_run_id: e428ac6f-a3f7-471c-ab8a-dcf33c287429
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-17
question: "Will the price of Bitcoin be above $72,000 on April 17?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["binance-btcusdt-resolution-venue"]
proposed_drivers: ["short-horizon-threshold-volatility"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-1cbf2a82/researcher-analyses/2026-04-15/dispatch-case-20260415T144104Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "bitcoin", "timing", "catalyst"]
---

# Summary

This map nets out a short-dated BTC threshold market where timing and contract mechanics matter more than broad long-run Bitcoin views.

## Question being evaluated

Will Binance BTC/USDT print a 12:00 ET 1-minute candle close above 72,000 on Apr 17, 2026?

## Current lean

Lean Yes, modestly above market.

## Prior / starting view

Starting view was that a threshold already below spot with only ~48 hours remaining should usually be favored, but the exact-noon candle mechanic creates meaningful path risk.

## Evidence supporting the claim

- Binance spot check around 10:45 EDT on Apr 15 showed BTC/USDT at 74,013.45.
  - Direct
  - High weight
  - Matters because the contract is already in the money by about 2.7%.
- Polymarket rules confirm the contract depends only on the Binance noon ET minute close.
  - Direct for contract interpretation
  - High weight
  - Matters because this is a hold-the-line market, not a rally-to-target market.
- Fed calendar check shows no scheduled FOMC meeting before resolution.
  - Contextual
  - Medium-low weight
  - Matters because one obvious high-information macro catalyst is absent from the remaining window.

## Evidence against the claim

- A 2.7% downside move in BTC over ~48 hours is normal enough that the current cushion is real but not large.
  - Indirect / contextual
  - High weight
- The market resolves on one exact minute on one venue; intraday wick or exchange-specific weakness at noon ET can decide it even if BTC is broadly firm.
  - Direct from rules / contextual for trading behavior
  - High weight
- No strong positive scheduled catalyst was identified that should force BTC higher before resolution.
  - Contextual
  - Medium weight

## Ambiguous or mixed evidence

- Absence of a scheduled Fed event reduces one obvious risk, but unscheduled macro or crypto headlines can still dominate a 48-hour BTC market.
- Current market price near 84.5% may already incorporate the above-spot setup and the absence of known near-term catalysts.

## Conflict between inputs

No major source conflict. The main issue is weighting: how much value to assign to current in-the-money spot versus ordinary short-horizon BTC volatility.

## Key assumptions

- No fresh negative shock arrives before Apr 17 noon ET.
- Binance remains a reliable proxy for broader BTC spot at the resolution minute.

## Key uncertainties

- Overnight macro or geopolitical headlines.
- Any crypto-specific stress event.
- How much of the current 84.5% market price already embeds the low-catalyst calendar.

## Disconfirming signals to watch

- BTC loses 72,500 and trades with sustained downside momentum.
- Risk assets sell off sharply ahead of U.S. morning on Apr 17.
- Binance-specific pricing or operational issues.

## What would increase confidence

- BTC holding above roughly 73,500 into Apr 16-17.
- Quiet macro tape with no major risk-off headlines.

## Net update logic

The strongest fact is simple: Binance BTC is already above the threshold and no obvious scheduled macro event forces repricing before the deadline. That pushes the lean to Yes. But the edge is capped because the remaining downside buffer is only about 2.7%, which is not large for BTC over two days.

## Suggested downstream use

Use as synthesis input for short-horizon timing/risk framing, especially to separate terminal directional confidence from exact-minute threshold fragility.
