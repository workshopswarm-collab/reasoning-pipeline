---
type: assumption_note
case_key: case-20260413-2d3a41aa
dispatch_id: dispatch-case-20260413-2d3a41aa-20260413T134928Z
research_run_id: 7e91f294-9035-42d7-ac40-708488f6aca4
analysis_date: 2026-04-13
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-13
question: "Will the price of Bitcoin be above $70,000 on April 13?"
driver: operational-risk
date_created: 2026-04-13
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/variant-view.md"]
tags: ["assumption", "btc", "intraday", "resolution"]
---

# Assumption

The most decision-relevant assumption is that BTC/USDT will still be above 70,000 at the exact Binance 12:00 ET one-minute candle close, not just before noon.

## Why this assumption matters

The contract is path-insensitive except at one precise minute close. A market participant can be directionally right about Bitcoin being strong intraday and still lose if a brief drop occurs into the governing close.

## What this assumption supports

- A high but not near-certain Yes probability.
- A modestly more cautious stance than a purely spot-based reading.
- The variant view that intraminute timing risk is the main underweighted residual risk once spot is already above threshold.

## Evidence or logic behind the assumption

- Binance spot at research time was 71,603.23, about 2.3% above the threshold.
- Polymarket rules tie settlement to the exact 12:00 ET Binance 1-minute close.
- Bitcoin can move materially within minutes, so a currently above-threshold spot price is strong but not fully dispositive before the governing candle closes.

## What would falsify it

- A confirmed Binance noon ET candle close at or below 70,000.
- A sharp pre-noon selloff that takes BTC/USDT decisively below the threshold into the governing minute.

## Early warning signs

- Rapid loss of the 71k handle before noon ET.
- Rising short-horizon volatility near the settlement minute.
- Exchange-specific dislocations on Binance versus broader spot markets.

## What changes if this assumption fails

If BTC/USDT falls to or below 70,000 at the governing close, the market resolves No regardless of earlier strength. The correct interpretation would shift from "high-probability Yes with timing caveat" to "timing caveat dominated the outcome."

## Notes that depend on this assumption

- Main finding at `qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-analyses/2026-04-13/dispatch-case-20260413-2d3a41aa-20260413T134928Z/personas/variant-view.md`
- Source note at `qualitative-db/40-research/cases/case-20260413-2d3a41aa/researcher-source-notes/2026-04-13-variant-view-binance-polymarket-resolution-check.md`
