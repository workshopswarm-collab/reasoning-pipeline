---
type: evidence_map
case_key: case-20260414-b6293fe0
dispatch_id: dispatch-case-20260414-b6293fe0-20260414T001837Z
research_run_id: 38eb6f92-1ed9-4121-9c0c-4daf22c0fafe
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin-weekly-hit-price
entity: bitcoin
topic: will-bitcoin-reach-74-000-april-13-19
question: "Will Bitcoin reach $74,000 April 13-19?"
driver: operational-risk
date_created: 2026-04-14
agent: Orchestrator
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin", "polymarket"]
related_drivers: ["operational-risk", "liquidity", "macro"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "threshold-market", "resolution"]
---

# Summary

This case is mostly about whether the threshold touch already happened under the exact contract rules. Once that is established, remaining risk is small and mainly operational.

## Question being evaluated

Will Bitcoin reach $74,000 April 13-19 under Polymarket's stated resolution criteria?

## Current lean

Strong lean to `Yes`; effectively already happened unless a narrow source-of-truth issue emerges.

## Prior / starting view

Starting baseline from the market was extreme confidence (`~89%` from assignment price, and the live event page showed even higher confidence near certainty at extraction time), so the main task was stress-testing whether that confidence was overclaiming certainty.

## Evidence supporting the claim

- Polymarket rules and embedded market state: the contract is a simple touch market on Binance BTC/USDT 1-minute highs, and the live state priced `Yes` around 99.95%. Direct for contract interpretation; high weight.
- Embedded event JSON showed the sibling 72k weekly threshold already resolved `Yes`, consistent with upward threshold progression having been reached. Indirect but supportive; medium weight.
- Independent market-data verification via CoinGecko and Binance hourly path showed BTC trading above 74k in the relevant period, making a qualifying Binance 1-minute high highly likely. Contextual verification; high weight.

## Evidence against the claim

- The contract is narrow: only Binance BTC/USDT 1-minute highs count. A broad BTC/USD print elsewhere would not settle the market. Direct contract fragility; medium weight.
- The independent verification used hourly / aggregated data, not a directly archived Binance 1-minute candle export. That leaves small but nonzero operational ambiguity. Indirect methodological limitation; medium weight.
- After the spike, BTC traded back in the low 70ks, reminding that this was a touch event rather than sustained acceptance above 74k. Relevant only if the earlier touch evidence were wrong; low weight.

## Ambiguous or mixed evidence

- The market page appeared to include a proposed resolution object consistent with `Yes`. That is supportive, but the safer framing is still that the core source of truth is the rules plus the underlying Binance print.

## Conflict between inputs

No major factual conflict across sources. The difference is mostly between direct contract-governing evidence and secondary verification quality.

## Key assumptions

- A qualifying Binance BTC/USDT 1-minute high >= 74,000 already occurred in the ET window.
- No hidden rules nuance or dispute prevents normal settlement.

## Key uncertainties

- Whether one wants a literal 1-minute Binance candle capture in hand before calling the residual risk de minimis.
- Whether there is any live dispute process that could temporarily delay or complicate settlement despite the apparent hit.

## Disconfirming signals to watch

- Direct Binance 1-minute data showing no qualifying 74k high.
- Material repricing lower on the contract.
- A dispute or correction to the apparent proposed resolution state.

## What would increase confidence

- A direct Binance 1-minute candle screenshot/export covering the qualifying minute.
- Final market resolution status moving from proposed/active to resolved `Yes`.

## Net update logic

The market started already very confident. The extra verification pass did not uncover a hidden flaw; instead it reinforced that the market's confidence is broadly justified. The only meaningful residual risk is contract-specific operational ambiguity, not a macro or directional BTC thesis failure.

## Suggested downstream use

Use as forecast update and orchestrator synthesis input, with emphasis that this is a narrow contract-interpretation / source-of-truth case rather than a broad BTC call.