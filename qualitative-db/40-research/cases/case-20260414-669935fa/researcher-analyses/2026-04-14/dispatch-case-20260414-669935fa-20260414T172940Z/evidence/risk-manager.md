---
type: evidence_map
case_key: case-20260414-669935fa
dispatch_id: dispatch-case-20260414-669935fa-20260414T172940Z
research_run_id: 591764aa-483b-4dd8-b2ab-48ab921b4a9b
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: tokens
entity: bitcoin
topic: will-bitcoin-reach-76k-april-13-19
question: "Will Bitcoin reach $76,000 April 13-19?"
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: []
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "binance", "settlement"]
driver:
---

# Summary

This map nets out a simple but audit-sensitive case. Once a direct Binance 1-minute high above $76,000 is observed inside the contract window, ordinary path risk mostly disappears and the residual uncertainty collapses into source-of-truth implementation risk.

## Question being evaluated

Will Bitcoin reach $76,000 at least once during Apr 13-19 under the contract’s stated Binance BTC/USDT 1-minute-high rules?

## Current lean

Very strong Yes lean; effectively already satisfied unless there is an unexpected settlement-source mismatch.

## Prior / starting view

Starting view from assignment metadata alone: Yes was already priced near certainty by the market at 99.95%, but that extreme confidence required an extra verification pass because the event is still a narrow threshold-touch contract.

## Evidence supporting the claim

- `2026-04-14-risk-manager-binance-1m-threshold-check.md`
  - Direct evidence from the named venue and timeframe.
  - Shows a 1-minute BTCUSDT high of 76038.0 at 2026-04-14 14:32 UTC / 10:32 ET.
  - Weight: very high.
- `2026-04-14-risk-manager-polymarket-rules-and-live-market.md`
  - Direct contract mechanics showing that any qualifying Binance 1-minute high is sufficient for Yes.
  - Weight: very high.
- `2026-04-14-risk-manager-coingecko-context.md`
  - Contextual cross-check showing BTC was already trading close enough to make a touch plausible even before the direct qualifying print check.
  - Weight: medium.

## Evidence against the claim

- The rules reference Binance chart highs, and this run verified via Binance public API rather than manually confirming the exact chart UI high.
  - This is not evidence against the underlying event, but it is the main residual implementation risk.
  - Weight: low to medium.
- Polymarket had not yet mechanically resolved the outcome at the time of research.
  - That lag can create apparent uncertainty even after the factual condition is met.
  - Weight: low.

## Ambiguous or mixed evidence

- CoinGecko and other contextual feeds are directionally supportive but not contract-settling.
- A near-certain market price can reflect either genuine factual near-resolution or herd overconfidence; without direct venue verification it would be ambiguous, but the Binance check largely resolves that ambiguity.

## Conflict between inputs

No meaningful factual conflict after the Binance 1-minute check. Remaining uncertainty is mostly about source implementation, not directional evidence.

## Key assumptions

- The Binance public 1-minute kline data is consistent with the source the market operator will use for settlement.
- The retrieved qualifying candle remains valid and is not later revised away.

## Key uncertainties

- Whether the settlement process relies on a chart rendering or data path that could differ from the public API.
- Whether any hidden contract nuance overrides the plain-language rule excerpt.

## Disconfirming signals to watch

- A documented Binance chart/UI check that fails to show the 76038.0 high.
- Polymarket or UMA-style resolution discussion indicating a source discrepancy.
- Unexpected continued non-resolution combined with informed market repricing lower.

## What would increase confidence

- Manual confirmation on the exact Binance web chart with 1m candles selected.
- Formal market resolution or public settlement confirmation.

## Net update logic

The run started with skepticism toward a 99.95% market price because extreme prices can overstate certainty in narrow threshold-touch contracts. The decisive update was direct Binance 1-minute data showing a high above the threshold during the relevant window. That transformed the problem from future path forecasting into settlement-implementation validation.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review
- retrospective evaluation