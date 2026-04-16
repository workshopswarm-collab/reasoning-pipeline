---
type: evidence_map
case_key: case-20260416-1f25d147
dispatch_id: dispatch-case-20260416-1f25d147-20260416T035120Z
research_run_id: 1ede30cc-9915-4cf7-a5e8-74c4d5684a9c
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: solana
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-1-minute-candle-on-april-19-2026-close-above-80
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle on April 19, 2026 close above 80?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["sol", "solana"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-1f25d147/researcher-analyses/2026-04-16/dispatch-case-20260416-1f25d147-20260416T035120Z/personas/risk-manager.md"]
tags: ["evidence-map", "timing-risk", "crypto"]
---

# Summary

The net evidence supports Yes, but the remaining risk is concentrated in path dependency: a market several dollars above the strike can still miss if a volatile altcoin sells off into the exact Binance noon ET one-minute close on April 19.

## Question being evaluated

Whether the Binance SOL/USDT 12:00 ET one-minute candle on April 19, 2026 closes above 80.

## Current lean

Lean Yes, but less confidently than the 92% market price implies.

## Prior / starting view

Starting view was that a mid-80s current price likely supports Yes, but a risk-manager should discount from near-certainty because the contract is exact-minute and exchange-specific.

## Evidence supporting the claim

- Binance rules/source note: the same exchange named for resolution currently shows SOL around 85.37. Direct evidence. High weight.
- Binance recent daily candles: all reviewed daily closes over the last week were above 80, usually by several dollars. Direct contextual evidence from the governing venue. High weight.
- Binance recent hourly candles: most hourly closes in the last three days were roughly 82.9 to 87.3, indicating a persistent cushion above 80. Direct contextual evidence. Medium-high weight.
- CoinGecko cross-check: broad-market SOL price around 85.29, consistent with Binance. Indirect contextual evidence. Low-medium weight.

## Evidence against the claim

- Exact-minute structure: the contract is not “trade above 80 sometime that day”; it is the final close of one specific 12:00 ET one-minute Binance candle. Direct rule-based downside. High weight.
- SOL is a volatile altcoin: a 5-6% move over several days is plausible, so a current mid-80s price does not justify near-certainty. Indirect but material market-structure consideration. Medium-high weight.
- Venue-specific microstructure risk: even if general SOL pricing stays near the threshold, Binance-specific prints or brief downside into the exact minute could decide the market. Direct contract-mechanics risk. Medium weight.

## Ambiguous or mixed evidence

- Broader crypto market regime between now and April 19: if risk-on continues, the cushion likely holds; if broad crypto weakens, the cushion can disappear quickly.
- Lack of major fresh negative catalyst in the checked sources is supportive, but absence of a catalyst is not strong evidence in a short-horizon crypto market.

## Conflict between inputs

There was no major factual conflict. The main difference is weighting: direct price evidence favors Yes, while risk interpretation argues the residual No path is larger than the market price suggests.

## Key assumptions

- SOL retains a several-dollar buffer above 80 into April 19.
- Binance remains a reliable and representative price venue at the settlement minute.
- No broad crypto drawdown large enough to erase the current cushion occurs before settlement.

## Key uncertainties

- Exact noon ET price on April 19 remains inherently unknown.
- Short-horizon crypto volatility can be nonlinear and catalyst-driven.
- Manual/UI settlement interpretation could still create small operational ambiguity, though not enough to dominate the case.

## Disconfirming signals to watch

- SOL loses the 82 area on repeated hourly closes.
- BTC/ETH lead a sharp market-wide selloff.
- Binance-specific pricing diverges materially from aggregator context.

## What would increase confidence

- Additional days of hourly/daily closes holding above 83-84.
- Stable broad-market crypto sentiment into the weekend.
- A pre-settlement check showing Binance still comfortably above 80 on April 19 morning.

## Net update logic

The evidence moved the starting view to a clear Yes lean because both the governing venue and an independent contextual source show SOL in the mid-80s, and recent Binance candles show sustained cushion above 80. But the current 92% market price appears to compress timing and volatility risk too aggressively for a short-horizon altcoin contract settled on one exact minute.

## Suggested downstream use

Use as orchestrator synthesis input and as a reminder that extreme prices on exact-minute crypto threshold markets may still deserve a modest risk discount.