---
type: evidence_map
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
research_run_id: 6f74cb87-6f36-43f1-b397-a014d9dfaad5
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: bitcoin-above-70k-on-april-14
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-14 be above 70000?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414T130958Z/personas/risk-manager.md"]
tags: ["evidence-map", "intraday", "settlement", "bitcoin"]
---

# Summary

The evidence strongly favors Yes, but the residual risk is real because this is a narrow one-minute settlement contract on a single venue at a fixed time.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 70,000?

## Current lean

Lean Yes with high probability, but lower confidence than the market’s near-certainty because timing and venue-specific path risk remain.

## Prior / starting view

Starting view: likely Yes because the market was pricing near certainty and adjacent strikes suggested BTC was already well above 70k.

## Evidence supporting the claim

- Polymarket cross-strike surface on the event page showed 70k at about 99.9% and 72k around 99%, while 74k was still materially favored. This implies the market believed spot was comfortably above 70k. Direct to market baseline; medium weight.
- Live Binance spot ticker query returned BTCUSDT around 74,544.7 during research. Direct venue evidence; high weight.
- The gap between live spot and threshold was roughly 4.5k, meaning a substantial move would be required before noon ET to flip the contract. Indirect inference from direct price evidence; medium-high weight.

## Evidence against the claim

- Contract resolves on one exact minute, not a daily average or broad session range. Timing concentration makes intraday reversal risk more important than it looks from a single spot check. Direct contract-mechanics risk; high weight.
- The governing source is Binance chart/UI language, not explicitly the public API. Small operational ambiguity remains if chart labeling or display conventions differ from API expectations. Operational source-risk; low-medium weight.
- BTC is volatile enough that a multi-thousand-dollar intraday move is uncommon but not impossible. Contextual tail-risk; low-medium weight.

## Ambiguous or mixed evidence

- Binance REST kline docs are helpful verification, but they do not fully eliminate UI-vs-API settlement ambiguity because Polymarket names the website chart surface.
- Market pricing itself is informative but not independent from broader trader consensus and may overstate certainty in narrow settlement contracts.

## Conflict between inputs

No major factual conflict found. The tension is between strong directional evidence and the risk-manager view that market confidence may still be slightly too high for a one-minute single-venue settlement.

## Key assumptions

- Binance BTCUSDT remains above 70k into the noon ET settlement minute.
- No exchange-specific anomaly changes the relevant close or its interpretation.
- The working timezone mapping of noon ET to 16:00 UTC on 2026-04-14 is correct.

## Key uncertainties

- Intraday path between research time and settlement.
- Exact final close value for the noon ET minute.
- Whether any UI-specific nuance matters for the named resolution surface.

## Disconfirming signals to watch

- BTCUSDT trading rapidly toward 70k during late morning ET.
- Abnormal Binance volatility, outage, or chart inconsistency near settlement.
- Any clarification from Polymarket implying a different interpretation of the relevant candle.

## What would increase confidence

- A late-morning Binance check showing BTCUSDT still well above 70k.
- A direct screenshot or export of the relevant Binance 12:00 ET candle once formed.

## Net update logic

The evidence moved the view from generic likely-Yes to a more explicit high-probability Yes because direct venue price evidence showed a substantial cushion over the threshold. However, the contract’s one-minute settlement mechanics prevent upgrading all the way to certainty.

## Suggested downstream use

Use as orchestrator synthesis input and as an audit trail for why the run accepted the market direction but still marked residual timing and operational fragility.