---
type: evidence_map
case_key: case-20260416-5baa54ee
dispatch_id: dispatch-case-20260416-5baa54ee-20260416T032738Z
research_run_id: e77911a4-52ee-430b-9843-39f3332b8371
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-12-00-et-1-minute-candle-close-on-2026-04-20-above-70000
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-20 above 70000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-5baa54ee/researcher-analyses/2026-04-16/dispatch-case-20260416-5baa54ee-20260416T032738Z/personas/risk-manager.md"]
tags: ["evidence-map", "btc", "risk-manager"]
---

# Summary

The evidence supports Yes, but the market's 94% pricing still compresses meaningful exact-minute timing and exchange-specific failure risk.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET 1-minute candle close on April 20, 2026 above 70,000?

## Current lean

Lean Yes at high but not extreme confidence.

## Prior / starting view

Starting view was that a 94% market price might be slightly too confident for a narrow, exact-minute crypto contract unless BTC were far above the strike.

## Evidence supporting the claim

- Binance spot at research time was about 75,029.99, roughly 7% above the threshold. Direct source, high weight.
- Recent Binance daily closes in the fetched sample were all above 70,000. Direct but lower-frequency evidence, medium weight.
- BTC is a deep, highly liquid benchmark asset, reducing thin-market print risk. Contextual source, low-to-medium weight.

## Evidence against the claim

- Contract resolution depends on one exact 1-minute candle close at 12:00 ET on April 20; this creates timing fragility even if the broader price trend stays healthy. Direct contract interpretation, high weight.
- A ~7% cushion is good but not unbreakable in crypto over multiple days, especially through a weekend. Contextual risk analysis, medium weight.
- The governing source is Binance specifically, so venue-specific operational or print anomalies matter more than in a broad-index contract. Direct contract interpretation, medium weight.

## Ambiguous or mixed evidence

- CoinGecko and other broad references support that BTC is a liquid benchmark, but they do not materially reduce the exact-minute resolution risk.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: whether the current cushion justifies a probability in the mid-90s versus high-80s/low-90s.

## Key assumptions

- BTC remains above 70,000 into the specific noon ET reference minute.
- Binance produces a normal market print without disruptive anomaly.
- No major macro or crypto shock occurs before resolution.

## Key uncertainties

- Intraday volatility at the exact minute.
- Weekend/event headline risk before April 20.
- Binance-specific market-structure or data-surface issues.

## Disconfirming signals to watch

- BTC falling below 72,000 before April 20.
- Sharp risk-off move in crypto majors.
- Binance outage, unusual premium/discount, or wick behavior.

## What would increase confidence

- BTC holding comfortably above 73k-74k into late April 19 / early April 20.
- Additional direct verification of Binance minute-candle behavior near the deadline.

## Net update logic

Direct exchange evidence supports Yes, but the case is not as clean as a settled official statistic because all conditions must hold simultaneously: correct exchange, correct pair, correct minute, correct timezone, and close strictly above 70,000. That bundle of conditions keeps me below the market.

## Suggested downstream use

Use as orchestrator synthesis input and as a caution against over-reading a 94% price as near-certainty.