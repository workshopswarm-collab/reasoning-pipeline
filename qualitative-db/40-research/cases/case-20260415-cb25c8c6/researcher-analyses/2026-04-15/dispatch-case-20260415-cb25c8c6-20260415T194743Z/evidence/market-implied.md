---
type: evidence_map
case_key: case-20260415-cb25c8c6
dispatch_id: dispatch-case-20260415-cb25c8c6-20260415T194743Z
research_run_id: e78c1192-5ff3-478c-b293-edbb874e35af
analysis_date: 2026-04-15
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-19
question: "Will the Binance BTC/USDT 12:00 ET 1-minute candle close on 2026-04-19 be above 68000?"
driver: reliability
date_created: 2026-04-15
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-cb25c8c6/researcher-analyses/2026-04-15/dispatch-case-20260415-cb25c8c6-20260415T194743Z/personas/market-implied.md"]
tags: ["evidence-map", "bitcoin", "market-implied"]
---

# Summary

The market's extreme Yes price is mostly justified by a large current spot cushion over the strike plus clear resolution mechanics. The main residual risk is not informational but path risk: a sizeable BTC drawdown or Binance-specific anomaly before the exact settlement minute.

## Question being evaluated

Will Binance BTC/USDT close above 68,000 on the 12:00 ET 1-minute candle on Apr 19, 2026?

## Current lean

Yes, with high probability.

## Prior / starting view

Start from the market prior around 98.1-98.6% because prediction markets often price simple near-dated threshold questions efficiently when the underlying asset is liquid and continuously observed.

## Evidence supporting the claim

- Polymarket rules and displayed pricing: direct for contract mechanics; moderate weight for market consensus. Matters because it defines the exact settlement conditions and shows broad crowd confidence near 98%.
- Binance direct spot/ticker API around 75,023.75: direct and high weight. Matters because Binance is the governing exchange family and current spot is roughly 10% above the strike.
- Binance recent 1-minute klines clustered near 75k: direct and medium-high weight. Matters because the contract resolves from a one-minute close on the same venue and format.
- CoinGecko cross-check near 74,997: indirect for settlement but useful contextual verification; medium weight. Matters because it suggests the Binance read is not obviously anomalous.

## Evidence against the claim

- Four days remain, which is enough time for BTC to move sharply lower; direct path-risk consideration with medium weight.
- The contract is decided by one specific one-minute close, so even temporary stress around settlement matters more than for a daily-close concept; direct rule-sensitive consideration with medium weight.
- Binance-specific operational or market-structure anomalies could matter because other venues do not control settlement; direct but low-probability risk with low-medium weight.

## Ambiguous or mixed evidence

- CoinGecko confirmation is helpful but not independent in a deep causal sense because both sources reflect the same underlying global BTC market.
- The market's own price is informative but partly endogenous; it should not be counted as independent proof of the outcome.

## Conflict between inputs

No meaningful factual conflict found. The main issue is weighting: whether the existing 7k spot cushion is enough to justify a probability as high as the upper-90s.

## Key assumptions

- Current spot cushion remains materially intact into the settlement window.
- No Binance-specific distortion dominates the settlement minute.
- Ordinary BTC volatility over four days is insufficient to force settlement below 68k.

## Key uncertainties

- Magnitude of BTC downside volatility over the next four days.
- Whether macro or crypto-specific news creates a sudden weekend drawdown.
- Whether the exact settlement minute experiences exchange-specific noise.

## Disconfirming signals to watch

- BTC moving into the high-60k to low-70k range before Apr 19.
- Rising venue-specific divergence on Binance versus other spot markets.
- Operational disruptions on Binance near the settlement window.

## What would increase confidence

- BTC remaining comfortably above 72k into Apr 18-19.
- Continued normal Binance market functioning with no unusual spread or candle anomalies.

## Net update logic

The main update is not from discovering hidden information but from confirming that the market's extreme confidence rests on a real and large current price cushion on the exact venue family that governs settlement. That supports staying close to the market prior rather than searching for a contrarian story.

## Suggested downstream use

Use as a synthesis input and as an audit trail showing why this high-probability view was accepted despite the narrow settlement mechanics.