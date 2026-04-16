---
type: evidence_map
case_key: case-20260414-c44f46c0
dispatch_id: dispatch-case-20260414-c44f46c0-20260414T185449Z
research_run_id: e7a751d8-e426-483c-af72-ad2f67b5487d
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-19
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 PM ET on 2026-04-19 close above 68000?"
driver: operational-risk
date_created: 2026-04-14
agent: variant-view
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["variant-view.md"]
tags: ["evidence-map", "bitcoin", "binance", "contract-interpretation"]
---

# Summary

The market’s Yes lean is directionally justified by current Binance price distance above the strike, but the variant edge is that a 95%+ price may still underweight exact-minute settlement mechanics and the nontrivial possibility of a sharp multi-day drawdown in a volatile asset.

## Question being evaluated

Whether Binance BTC/USDT will print a final close above 68,000 on the 1-minute candle corresponding to 12:00 PM ET on 2026-04-19.

## Current lean

Lean Yes, but slightly less confidently than the market.

## Prior / starting view

Starting view was that 95.75% looked high enough to deserve contract-mechanics verification and an explicit check of how much price buffer currently exists.

## Evidence supporting the claim

- Binance live ticker showed BTCUSDT around 74,298 during the run.
  - Source: Binance live endpoint note.
  - Why it matters: implies an approximately 6.3k buffer above the strike, meaning price can fall materially and still resolve Yes.
  - Direct vs indirect: direct current exchange data, indirect for final settlement.
  - Weight: high.

- Recent Binance 1-minute klines during the run were also clustered around 74k+.
  - Source: Binance live endpoint note.
  - Why it matters: confirms the ticker was not a stale or isolated print.
  - Direct vs indirect: direct current exchange data, indirect for April 19 noon close.
  - Weight: medium-high.

- Polymarket rules are straightforward on source and pair selection.
  - Source: Polymarket rules note.
  - Why it matters: narrows away cross-exchange ambiguity and supports using Binance-specific context rather than blended BTC prices.
  - Direct vs indirect: direct contract evidence.
  - Weight: high.

## Evidence against the claim

- The contract settles on one exact minute close, not broad daily trading range.
  - Source: Polymarket rules note.
  - Why it matters: even if BTC trades above 68k most of the week, a sharp move into noon ET on Sunday could still produce No.
  - Direct vs indirect: direct contract evidence.
  - Weight: medium.

- Bitcoin can move more than 8% over a few days, especially around weekends or macro shocks.
  - Source: inference from asset class behavior, not directly quantified in this run.
  - Why it matters: current cushion is meaningful but not invulnerable.
  - Direct vs indirect: contextual.
  - Weight: medium.

- The contract points to Binance chart output, while this run used Binance API docs and endpoints for verification.
  - Source: comparison between rule wording and Binance documentation.
  - Why it matters: introduces small but real mechanics risk if UI/API mapping is not perfectly clean.
  - Direct vs indirect: interpretive.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- CoinGecko provides broad BTC context, but for this market it adds little beyond confirming that BTC is a large, liquid, widely tracked asset; it is less relevant than Binance-specific data.

## Conflict between inputs

There was no major factual conflict. The main tension is weighting-based: whether a 95%+ market is properly accounting for exact-minute and source-specific settlement details versus simply extrapolating current spot distance from the strike.

## Key assumptions

- Binance UI candle selection aligns cleanly with Binance documented kline structure for the relevant minute.
- No exceptional market event produces a large enough drawdown before the exact settlement minute.

## Key uncertainties

- Sunday-noon timing risk.
- Whether BTC remains above the strike after several more days of trading.
- Residual contract mapping ambiguity between named chart UI and API-verifiable kline structure.

## Disconfirming signals to watch

- BTCUSDT losing the 70k-72k area before the weekend.
- Any rule clarification or dispute suggesting non-obvious candle mapping.
- Sharp macro or crypto-specific downside catalyst before settlement.

## What would increase confidence

- A direct check closer to April 19 using Binance UI or API with timezone-matched minute selection.
- Continued BTCUSDT trading several thousand dollars above 68k into the final 24 hours.

## Net update logic

What mattered most was not generic bullishness but the magnitude of current Binance buffer versus the strike. What was downweighted was broad market commentary not tied to Binance settlement mechanics. The current lean is not just headline-following: it rests on direct contract rules plus direct Binance exchange data, while still discounting the market modestly for exact-minute and execution-source risk.

## Suggested downstream use

Use as an orchestrator synthesis input and as a compact audit trail for why the final estimate is slightly below, not equal to, the market price.