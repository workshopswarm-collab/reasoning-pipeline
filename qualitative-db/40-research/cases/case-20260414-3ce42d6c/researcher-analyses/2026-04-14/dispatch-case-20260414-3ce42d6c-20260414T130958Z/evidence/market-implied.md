---
type: evidence_map
case_key: case-20260414-3ce42d6c
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
research_run_id: cb7302c4-4ea6-41dd-a9b0-7dcf4c25710e
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-14
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-14 close above 70000?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/personas/market-implied.md"]
tags: ["evidence-map", "btc", "polymarket", "binance"]
---

# Summary

The evidence nets strongly toward Yes. The market appears to be efficiently pricing a large cushion over the strike, a short remaining time window, and a clearly specified exchange/pair source of truth.

## Question being evaluated

Will the Binance BTC/USDT one-minute candle for 12:00 ET on 2026-04-14 have a final close above 70,000?

## Current lean

Strong Yes lean; near-certainty but not literal certainty.

## Prior / starting view

Starting from the market at 99.95%, the main question was whether that extreme confidence ignored any meaningful rule/timing/venue risk.

## Evidence supporting the claim

- Polymarket rule text explicitly defines the relevant venue, pair, time, and metric.
  - Source: case source note on Polymarket and Binance resolution context.
  - Why it matters causally: removes most interpretation ambiguity.
  - Direct or indirect: direct for contract mechanics.
  - Weight: high.

- Direct Binance BTCUSDT 1m klines check shortly after 09:07 ET showed spot around 74.55k-74.58k.
  - Source: same source note.
  - Why it matters causally: the underlying specified by contract was already about 4.5k above the threshold with only hours left.
  - Direct or indirect: direct contextual evidence on the exact venue/pair.
  - Weight: very high.

- Polymarket threshold strip was internally coherent: 70k almost certain, 72k still very high, 74k materially lower, 76k very unlikely.
  - Source: market page fetch.
  - Why it matters causally: suggests traders are anchoring to a spot level in the mid-74k area rather than mispricing this one line in isolation.
  - Direct or indirect: indirect but market-structure contextual.
  - Weight: medium.

## Evidence against the claim

- The direct Binance check was not the exact noon candle.
  - Why it matters causally: a large late-morning move could still change the outcome.
  - Direct or indirect: direct limitation.
  - Weight: medium.

- The contract is venue-specific and candle-specific.
  - Why it matters causally: a Binance-specific anomaly, outage, bad print, or timestamp misunderstanding could matter even if broader BTC markets stay above 70k.
  - Direct or indirect: direct rule-sensitive risk.
  - Weight: low-to-medium.

## Ambiguous or mixed evidence

- Generic BTC price pages and broad market trackers are directionally consistent but not decisive because the contract is about Binance BTC/USDT specifically.

## Conflict between inputs

There was no meaningful source conflict. The only real tension is between ordinary price-continuity reasoning and the residual tail risk of a venue-specific noon-candle issue.

## Key assumptions

- Binance time labeling and ET conversion are straightforward for the noon candle.
- No intraday move of roughly 6%+ downward occurs before the final resolution minute.
- Binance provides a normal final close for the relevant candle.

## Key uncertainties

- Exact noon-candle close remains unobserved at research time.
- Tail operational anomalies cannot be reduced to zero.

## Disconfirming signals to watch

- Spot deterioration toward 70k during the late morning ET window.
- Binance front-end/API inconsistency or exchange incident reports.
- Sudden repricing of nearby threshold markets inconsistent with current cushion.

## What would increase confidence

- A second direct Binance check closer to noon ET still showing a large cushion.
- Confirmation from Binance front-end candle display matching the API context.

## Net update logic

The market started at near certainty. After checking rules and a direct Binance context source, that extreme pricing still looked justified. The extra verification did not overturn the market prior; it mostly confirmed that the market's confidence is driven by a substantial distance-to-strike cushion and low remaining time, with only modest residual venue/timestamp risk.

## Suggested downstream use

Use this as a high-confidence synthesis input supporting a Yes interpretation while preserving that the residual risk is mostly operational/timing rather than fundamental BTC directionality.