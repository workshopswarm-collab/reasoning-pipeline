---
type: evidence_map
case_key: case-20260416-3e035ad7
dispatch_id: dispatch-case-20260416-3e035ad7-20260416T043505Z
research_run_id: 52beb431-4480-452d-995c-b6167dca4b77
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-17
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 close above 70000?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["risk-manager", "threshold-market", "binance"]
---

# Summary

The evidence leans strongly toward Yes, but the main residual risk is narrow timestamp/exchange-specific path risk rather than broad directional uncertainty about Bitcoin.

## Question being evaluated

Will the Binance BTC/USDT 12:00 ET one-minute candle on April 17, 2026 have a final close above 70,000?

## Current lean

Strong Yes lean, with modest residual downside tail from a >6% drop before the exact noon ET close or a Binance-specific anomaly.

## Prior / starting view

Starting view was that a 99.15% market price looked directionally plausible given Bitcoin's level, but possibly too confident for a one-minute single-venue contract that still has a full overnight/intraday path to traverse.

## Evidence supporting the claim

- Polymarket rules define a simple mechanical test tied to Binance BTC/USDT 12:00 ET close.
  - direct
  - high weight
  - matters because lower contract ambiguity reduces interpretive downside.
- Binance public API spot price around 75,010 at the time checked.
  - direct
  - high weight
  - matters because the market currently has about a 5,010-point cushion above the threshold.
- Recent Binance 1-minute klines also closed near 75,000.
  - direct
  - medium-high weight
  - matters because it confirms the exchange/pair named in the contract is presently well above the threshold.
- CoinGecko spot check near 74,961.
  - indirect/contextual
  - low-medium weight
  - matters as an independence check that Binance was not obviously off-market.

## Evidence against the claim

- The contract resolves on one minute at one exact time, not on daily average or multi-exchange consensus.
  - direct contract-interpretation risk
  - medium-high weight
  - matters because a brief sharp drop can invalidate an otherwise bullish thesis.
- BTC can move >5-7% in a day during volatile regimes.
  - contextual
  - medium weight
  - matters because the current cushion is meaningful but not invulnerable.
- Binance-specific operational or market-structure anomalies could matter even if broad BTC remains above 70,000 elsewhere.
  - contextual
  - low-medium weight
  - matters because the source of truth is venue-specific.

## Ambiguous or mixed evidence

- Cross-venue consistency helps, but the settlement source is still Binance only.
- Current price cushion strongly supports Yes, but market confidence near 99% leaves little room for any residual operational or path risk.

## Conflict between inputs

No major factual conflict. The only meaningful tension is between directional spot evidence pointing strongly to Yes and the risk-manager concern that one-minute single-venue contracts can retain more tail risk than extreme prices imply.

## Key assumptions

- BTCUSDT stays above 70,000 into the noon ET settlement minute.
- Binance chart resolution surface behaves consistently with observed API values.
- No material rule reinterpretation emerges.

## Key uncertainties

- Magnitude of possible BTC downside over the next ~35 hours.
- Whether any Binance-specific dislocation appears near settlement.

## Disconfirming signals to watch

- BTCUSDT falls toward 71,000 or below before noon ET April 17.
- Elevated Binance-only volatility or divergence from other major references.
- Any evidence that Binance chart output and API output diverge in a way relevant to final close interpretation.

## What would increase confidence

- Another direct Binance check closer to settlement still showing a large cushion above 70,000.
- Continued cross-venue price consistency.

## Net update logic

The evidence keeps the answer strongly on the Yes side, but not at absolute certainty. The main reason to shade below the market is not a bearish BTC thesis; it is that the contract is a narrow, exact-time, exact-venue threshold event and those retain residual failure modes until the timestamp passes.

## Suggested downstream use

- forecast update
- orchestrator synthesis input
- decision-maker review