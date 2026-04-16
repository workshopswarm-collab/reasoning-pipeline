---
type: assumption_note
case_key: case-20260416-605a067d
dispatch_id: dispatch-case-20260416-605a067d-20260416T142910Z
research_run_id: 462a53a5-a84b-4046-b50b-38278daf2730
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: daily-threshold-close
entity: ethereum
topic: "Cushion persistence into exact noon ET Binance close"
question: "Will the Binance ETH/USDT 1-minute candle for 12:00 ET on April 17 close above 2200?"
driver: reliability
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "< 24h"
related_entities: ["binance", "ethereum"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules.md", "qualitative-db/40-research/cases/case-20260416-605a067d/researcher-source-notes/2026-04-16-risk-manager-binance-spot-check.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-605a067d/researcher-analyses/2026-04-16/dispatch-case-20260416-605a067d-20260416T142910Z/personas/risk-manager.md"]
tags: ["assumption-note", "timing-risk", "noon-close", "ethereum"]
---

# Assumption

ETH/USDT will retain enough of its current cushion above 2200 that the specific Binance 12:00 ET one-minute close on April 17 still prints above 2200.

## Why this assumption matters

The case is not about broad daily direction or whether ETH trades above 2200 at some point; it is about one exact exchange-specific minute. The entire bullish view depends on the current price cushion surviving into that minute.

## What this assumption supports

- A high but not near-certain Yes probability.
- The judgment that current market confidence is directionally reasonable.
- The conclusion that the main residual risk is timing/path dependence, not contract interpretation.

## Evidence or logic behind the assumption

- Direct Binance spot check showed ETH/USDT near 2298-2299, comfortably above 2200.
- Binance 24-hour low was still 2285.10, also above 2200.
- This means ETH could fall materially and still resolve Yes, so the threshold is not knife-edge at the time of analysis.

## What would falsify it

- A sustained selloff that pushes Binance ETH/USDT below 2200 before noon ET on April 17.
- Evidence of exchange-specific dislocation on Binance versus broader ETH markets.
- New Binance operational issues affecting the integrity or availability of the governing minute-close surface.

## Early warning signs

- ETH trading down toward the low 2200s overnight.
- Elevated intraday volatility concentrated near the U.S. morning session.
- A sharp negative crypto macro move that narrows the cushion well before the governing timestamp.

## What changes if this assumption fails

The Yes thesis deteriorates quickly because the contract is exact-minute sensitive. If ETH approaches or dips below 2200 before settlement, the market should be treated more like a coin-flip or worse rather than a high-confidence hold-above setup.

## Notes that depend on this assumption

- Main finding for risk-manager persona.
- Evidence map for support versus fragility netting.