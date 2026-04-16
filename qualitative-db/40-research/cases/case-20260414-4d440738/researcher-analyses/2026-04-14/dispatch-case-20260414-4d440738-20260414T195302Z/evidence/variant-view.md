---
type: evidence_map
case_key: case-20260414-4d440738
research_run_id: 21ed5f76-ad34-464c-a787-1243dd4b6a10
analysis_date: 2026-04-14
persona: variant-view
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68000-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 68000?"
driver: reliability
date_created: 2026-04-14
agent: variant-view
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-4d440738/researcher-analyses/2026-04-14/dispatch-case-20260414-4d440738-20260414T195302Z/personas/variant-view.md"]
tags: ["evidence-map", "btc", "settlement-minute"]
dispatch_id: dispatch-case-20260414-4d440738-20260414T195302Z
---

# Summary

The net evidence supports Yes, but the strongest credible variant view is that a 90%+ market may be a bit too confident because this contract resolves on one exchange-specific future minute close rather than on broad BTC direction alone.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 ET on 2026-04-20 close above 68,000?

## Current lean

Lean Yes, but less strongly than the market.

## Prior / starting view

Starting view was that a 93.5% market is probably directionally right given BTC's current level, but needed explicit timing/rules verification because the contract is narrow and date-sensitive.

## Evidence supporting the claim

- Binance current BTCUSDT spot at 74,233.62. Direct, high weight. This is about 9.17% above the threshold and makes Yes the base case.
- Binance recent daily klines show recent closes above 68,000 across the sampled period. Direct contextual, medium-high weight. This reduces the chance that current spot is a one-off spike.
- CoinGecko current BTC spot near 74,238. Indirect contextual, medium weight. This confirms current BTC level is broadly consistent beyond a single Binance print.
- Polymarket rule text confirms the exact threshold and source. Direct on mechanics, high weight for interpretation.

## Evidence against the claim

- The contract resolves on a single future one-minute Binance close, not on today's spot or a multi-exchange index. Direct on mechanics, medium-high weight.
- Six days remain, which is enough time for BTC to move more than 9% in either direction in a volatile regime. Indirect contextual, medium weight.
- Binance-specific operational or microstructure anomalies could matter because only one venue and one pair count. Direct on contract structure, low-medium weight.

## Ambiguous or mixed evidence

- High current BTC level can support Yes but may also encourage market overconfidence if traders mentally substitute broad bullishness for the exact settlement condition.

## Conflict between inputs

There is little factual conflict. The main disagreement is weighting-based: how much confidence should current >74k spot justify for a single-minute close six days later?

## Key assumptions

- Current cushion above 68,000 is large enough that ordinary six-day volatility still leaves Yes more likely than not.
- No exchange-specific incident will distort the settlement minute on Binance.

## Key uncertainties

- BTC volatility over the next six days.
- Whether a macro or crypto-specific shock arrives before April 20.
- Whether Binance experiences any pricing anomaly near settlement.

## Disconfirming signals to watch

- BTC losing 70k decisively before April 20.
- Large downside volatility shock.
- Evidence of Binance-specific feed or trading irregularity.

## What would increase confidence

- BTC remaining comfortably above 70k into April 19-20.
- Additional exchange and derivatives context showing stable basis / low stress.

## Net update logic

The evidence keeps the lean on Yes because current Binance spot and recent daily closes are materially above the threshold. The variant update is not bearish outright; it is that the market may be pricing too much certainty for a contract with a narrow, exchange-specific, minute-specific settlement rule and six days of remaining volatility.

## Suggested downstream use

Use as orchestrator synthesis input and forecast update context, especially for calibrating whether extreme-probability crypto threshold markets are overconfident versus their actual settlement mechanics.