---
type: evidence_map
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
research_run_id: 9ba8ba95-6b51-4d65-8da4-7c7ec7601023
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-9
question: "Will the price of Bitcoin be above $70,000 on April 9?"
driver: operational-risk
date_created: 2026-04-09
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/risk-manager.md"]
tags: ["evidence-map", "settlement-risk", "binance", "btcusdt"]
---

# Summary

The case leans Yes, but the main residual risk is not broad Bitcoin direction; it is single-minute settlement fragility plus minor interpretation risk around the exact Binance candle mapping.

## Question being evaluated

Will Binance BTC/USDT close above 70,000 on the 1-minute candle corresponding to 12:00 PM ET on 2026-04-09?

## Current lean

Lean **Yes**, but with more caution than the market price implies because the contract is a one-minute close market.

## Prior / starting view

Starting view: if spot BTC is materially above 70k with only hours left, Yes is favored; the main question is whether there is any hidden timing/mechanics trap.

## Evidence supporting the claim

- **Current Binance spot above 70k**
  - Source: live Binance ticker endpoint and recent klines.
  - Why it matters causally: if BTC is already trading around 71k, it has some cushion above the threshold.
  - Direct or indirect: indirect for final settlement, but directly relevant to path probability.
  - Weight: high.

- **Polymarket rules clearly anchor settlement to Binance BTC/USDT 1m close**
  - Source: Polymarket market page.
  - Why it matters causally: removes cross-exchange ambiguity and narrows the problem to one exchange/pair/source.
  - Direct or indirect: direct.
  - Weight: high.

- **Binance docs imply candle identification by open time**
  - Source: Binance kline API docs.
  - Why it matters causally: resolves the key ET-to-UTC mapping question in the most standard way.
  - Direct or indirect: direct for mechanics.
  - Weight: medium-high.

## Evidence against the claim

- **Single-minute settlement path risk**
  - Source: contract mechanics themselves.
  - Why it matters causally: BTC can trade above 70k for hours and still finish below 70k on the decisive minute close.
  - Direct or indirect: direct.
  - Weight: high.

- **One-minute interpretation ambiguity risk**
  - Source: mismatch between human-language market wording and technical exchange candle semantics.
  - Why it matters causally: a one-minute offset in interpretation can matter if price is near threshold.
  - Direct or indirect: direct.
  - Weight: medium.

- **Evidence independence is low by design**
  - Source: Binance is both the data source and mechanics source.
  - Why it matters causally: extra verification can validate interpretation but cannot diversify away single-source settlement dependence.
  - Direct or indirect: contextual.
  - Weight: medium.

## Ambiguous or mixed evidence

- BTC being about 1.5% above threshold is supportive, but not enough to eliminate intraday reversal risk in crypto.
- Polymarket’s displayed market price on the fetched page looked somewhat different from assignment metadata, so assignment metadata is the cleaner baseline for current implied probability.

## Conflict between inputs

No major factual conflict. The only meaningful issue is interpretation-based: whether “12:00 in ET” maps to the candle labeled by open time 12:00 ET or the candle finishing at noon. Binance docs favor the open-time interpretation.

## Key assumptions

- Noon ET on 2026-04-09 correctly converts to 16:00 UTC.
- The contract uses the Binance candle identified by open time 16:00 UTC / 12:00 ET.
- No unusual Binance outage, chart revision, or settlement dispute changes practical resolution.

## Key uncertainties

- BTC price level at the exact final close of the settlement minute.
- Whether Polymarket moderation would ever privilege a UI interpretation over Binance’s standard kline semantics if challenged.

## Disconfirming signals to watch

- BTC falling back toward or below 70k shortly before 16:01 UTC.
- Any moderator clarification suggesting a different candle mapping.
- Any Binance chart/API discrepancy for the target minute.

## What would increase confidence

- BTC holding comfortably above 70k closer to the settlement minute.
- A direct Binance UI snapshot or settlement precedent confirming the noon ET candle mapping exactly as open-time 16:00 UTC.

## Net update logic

The main update versus a naive bullish read is that this should not be treated like a broad daily-close market. The evidence still leans Yes because BTC is already above threshold and the source-of-truth mechanics are mostly tractable, but the narrow one-minute close structure keeps tail risk meaningfully alive.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review