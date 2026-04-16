---
type: evidence_map
case_key: case-20260414-3d24d01f
dispatch_id: dispatch-case-20260414-3d24d01f-20260414T184328Z
research_run_id: 5b5364e2-e3e1-46e8-9324-e7b529b98197
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-19
question: "Will the price of Bitcoin be above $70,000 on April 19?"
driver: operational-risk
date_created: 2026-04-14
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: ["weekend-macro-catalysts"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3d24d01f/researcher-analyses/2026-04-14/dispatch-case-20260414-3d24d01f-20260414T184328Z/personas/catalyst-hunter.md"]
tags: ["evidence-map", "catalyst", "btc", "timing"]
---

# Summary

This evidence map nets the direct settlement mechanics against the remaining timing risk over the next ~4.9 days.

## Question being evaluated

Will Binance BTC/USDT print a final 1-minute candle close above 70,000 for the 12:00 ET candle on 2026-04-19?

## Current lean

Lean Yes, with high but not near-certain probability.

## Prior / starting view

Starting view was that a market at 89% might be slightly complacent unless BTC had a very comfortable cushion and clean rule interpretation.

## Evidence supporting the claim

- Binance spot during this run was ~74.0k to 74.3k, giving a roughly 4k cushion versus the threshold. Direct, high weight.
- Binance 24h stats showed a low of 72,298.93 and high of 76,038, meaning even a volatile recent day stayed above the threshold. Direct, medium-high weight.
- Prior 7 daily Binance closes were all above 70k. Direct/contextual, medium weight.
- Contract wording is operationally simple once the source-of-truth is checked: only one minute on one named venue/pair matters. Direct, medium weight.

## Evidence against the claim

- The market resolves on one exact minute, not a daily close or weekend average, so path and timing risk remain real. Direct to contract mechanics, high weight.
- BTC can move several thousand dollars in a day; recent 24h range was wide enough to show nontrivial volatility. Direct/contextual, medium weight.
- Weekend macro or crypto-specific negative catalyst before Sunday noon ET could still force a repricing lower. Indirect, medium weight.

## Ambiguous or mixed evidence

- Strong recent price levels can mean either durable support or an overextended setup vulnerable to a fast unwind.
- The lack of a known scheduled catalyst is itself mixed: fewer obvious bearish events, but also less identifiable positive flow to defend the level if risk sentiment sours.

## Conflict between inputs

No major factual conflict. The main disagreement is weighting-based: whether the current ~4k cushion deserves something closer to 90%+ or whether one-minute resolution mechanics should keep the estimate lower.

## Key assumptions

- Current price cushion is large enough to absorb ordinary noise through the deadline.
- No major negative weekend catalyst lands before the noon ET resolution minute.

## Key uncertainties

- Near-term macro tape and weekend risk sentiment.
- Whether BTC remains comfortably above 72k into the final 24 hours.

## Disconfirming signals to watch

- BTC breaks below 72k and cannot recover.
- Broad risk assets weaken sharply ahead of Sunday.
- Exchange-specific disruption or data ambiguity around the Binance candle.

## What would increase confidence

- BTC holding above 73k-74k into late April 18 / early April 19.
- Additional confirmation that Polymarket settlement practice aligns cleanly with Binance API/UI candle data for this contract format.

## Net update logic

What mattered most was the direct combination of exact settlement mechanics plus current Binance price cushion. I downweighted broad crypto commentary because it did not improve the answer by much versus direct exchange data. The current lean is not just “BTC is high”; it is “BTC is materially above the threshold and the remaining risk is concentrated in timing-specific downside catalysts.”

## Suggested downstream use

Use as forecast update input and as an audit trail for why this persona viewed timing risk as the only serious remaining challenge to a Yes outcome.
