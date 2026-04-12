---
type: evidence_map
case_key: case-20260406-574ca6af
dispatch_id: dispatch-case-20260406-574ca6af-20260406T013239Z
research_run_id: 98f19f60-9ceb-4985-a375-2f6fdff8e994
analysis_date: 2026-04-06
persona: catalyst-hunter
domain: crypto
subdomain: ethereum
entity: Ethereum
topic: whether ETH reached 2200 on the governing venue within the resolution window
question: Will Ethereum reach $2,200 March 30-April 5?
driver: exchange-specific settlement mechanics
date_created: 2026-04-06T01:38:00Z
agent: catalyst-hunter
status: draft
confidence: high
conflict_status: low
action_relevance: high
related_entities: [Ethereum, Binance, Polymarket, Kraken, CoinGecko]
related_drivers: [resolution mechanics, cross-venue basis, expiry timing]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260406-574ca6af/researcher-analyses/2026-04-06/dispatch-case-20260406-574ca6af-20260406T013239Z/personas/catalyst-hunter.md]
tags: [evidence-map, binance, source-of-truth, catalyst]
---

# Summary

This is mostly a contract-mechanics and direct-price-verification case rather than an open-ended catalyst case. Once the governing source is identified as Binance ETH/USDT 1-minute highs, most softer catalysts become non-material unless they can plausibly force a last-minute Binance print through 2200.

## Question being evaluated

Will Ethereum reach $2,200 during Mar 30-Apr 5 under this market’s actual settlement logic?

## Current lean

Lean No with very high confidence by late verification, because the governing Binance ETH/USDT 1-minute high over the full window stayed below 2200.

## Prior / starting view

Starting baseline was market-implied Yes around 74%, suggesting either the market expected a touch of 2200 or was not fully discounting the venue-specific settlement mechanics.

## Evidence supporting the claim

- None on the governing source after direct verification.
- Soft support for a possible late squeeze existed in principle because ETH traded above 2160 during the week, leaving the threshold not impossibly far away. Weight: low after time-window verification.

## Evidence against the claim

- Polymarket rule text says only Binance ETH/USDT 1-minute Highs count. Direct, decisive, very high weight.
- Binance 1-minute kline pull over the full ET window showed max high 2167.85, below 2200. Direct, decisive, very high weight.
- Late contextual prices from Binance ticker, Kraken ticker, and CoinGecko were all around 2116-2118, indicating no hidden cross-venue spike near threshold at verification time. Indirect/contextual, moderate weight.

## Ambiguous or mixed evidence

- General crypto volatility and possible intraday squeezes are always relevant in threshold-touch markets, but once the full historical window is checked they matter only if there is still unresolved time left.
- Cross-venue price differences can matter for trader intuition, but not for this contract’s settlement once Binance-only wording is confirmed.

## Conflict between inputs

Minimal factual conflict. The only meaningful tension is between the market price (0.74 Yes) and the direct governing evidence, implying either stale pricing, late trading inertia, or misunderstanding of settlement mechanics.

## Key assumptions

- Polymarket’s published Binance-only rule is operative without hidden override.
- Binance API historical 1-minute kline highs are faithful to the charted source Polymarket references.

## Key uncertainties

- Small residual implementation risk around UI/API parity or unseen clarification.
- If verification occurred before the final minute of the window, a last-minute spike would remain a residual tail risk. That risk appears low given observed price distance and timing.

## Disconfirming signals to watch

- A verified Binance 1-minute candle at or above 2200 inside the ET window.
- A formal Polymarket clarification broadening the resolution source beyond Binance ETH/USDT 1m highs.

## What would increase confidence

- Visual confirmation from the Binance chart UI for the same historical high.
- Any post-close Polymarket or market resolution notice consistent with the direct kline check.

## Net update logic

The main update was from a moderately open catalyst question to a largely settled mechanics question. The evidence that mattered most was the source-of-truth wording plus the direct 1-minute kline maximum. Contextual venue checks were only a verification pass, not the core mechanism.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- retrospective evaluation for contract-mechanics handling in crypto threshold markets
