---
type: evidence_map
case_key: case-20260416-04100395
dispatch_id: dispatch-case-20260416-04100395-20260416T154804Z
research_run_id: 5d28a326-6ea4-49d7-ab83-b240db3558aa
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: price-markets
entity: ethereum
topic: will-the-binance-eth-usdt-12-00-et-1-minute-candle-on-2026-04-17-close-above-2300
question: "Will the Binance ETH/USDT 12:00 ET 1-minute candle on 2026-04-17 close above 2300?"
driver: operational-risk
date_created: 2026-04-16
agent: orchestrator
status: draft
confidence: medium
conflict_status: low-explicit-conflict
action_relevance: high
related_entities: ["binance", "ethereum"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-04100395/researcher-analyses/2026-04-16/dispatch-case-20260416-04100395-20260416T154804Z/personas/risk-manager.md"]
tags: ["stress-test", "evidence-netting", "minute-resolution"]
---

# Summary

The evidence nets to a modest Yes lean, but with lower confidence than the market price appears to embed because this is a narrow minute-level settlement contract rather than a broad directional ETH call.

## Question being evaluated

Will the Binance ETH/USDT 1-minute candle labeled 12:00 ET on 2026-04-17 have a final close strictly above 2300?

## Current lean

Lean Yes, but only modestly above the market baseline after accounting for timing and path fragility.

## Prior / starting view

Starting view: ETH being above 2300 the day before resolution would usually make Yes more likely than not, but the exact-minute contract structure should cap confidence unless price has a large cushion.

## Evidence supporting the claim

- Binance spot price during the run was about 2333.19.
  - Source: source note `2026-04-16-risk-manager-binance-market-context.md`
  - Why it matters: direct exchange-specific evidence from the settlement venue.
  - Direct or indirect: direct.
  - Weight: high.

- Recent Binance 1-minute candles fetched during the run closed in the mid-2330s to high-2330s.
  - Source: same Binance source note.
  - Why it matters: suggests price was not merely touching 2300 but holding some cushion during sampled minutes.
  - Direct or indirect: direct.
  - Weight: medium-high.

- CoinGecko contextual snapshot also showed ETH around 2338 with positive 7d and 14d momentum.
  - Source: source note `2026-04-16-risk-manager-coingecko-context.md`
  - Why it matters: reduces concern that Binance was showing an idiosyncratically high print.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The contract resolves on one exact 1-minute close tomorrow at 12:00 ET, not on current price or daily close.
  - Source: Polymarket rule text captured in the Binance/rules source note.
  - Why it matters: narrow timing creates path dependence and minute-volatility risk.
  - Direct or indirect: direct contract interpretation.
  - Weight: high.

- Current cushion above 2300 is only around 30-40 dollars, which is not huge for ETH over a roughly 20-hour horizon.
  - Source: netting of current Binance and CoinGecko price context.
  - Why it matters: modest drawdown is enough to flip the outcome.
  - Direct or indirect: inferential but grounded in direct price observations.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Recent positive multi-day ETH performance helps the Yes case, but momentum evidence is weakly transferable to a single-minute settlement.
- Cross-source price agreement is reassuring, but both sources still ultimately reflect market data rather than a causal reason price must stay above 2300 tomorrow.

## Conflict between inputs

No strong factual conflict across sources. The main issue is weighting: broad market context points toward Yes, while the contract design argues for discounting confidence.

## Key assumptions

- ETH retains enough cushion above 2300 into the settlement minute that ordinary volatility does not break the threshold.
- Binance spot remains a representative venue rather than showing a special dislocation at resolution time.

## Key uncertainties

- Overnight and morning crypto volatility before the 12:00 ET settlement minute.
- Whether U.S. morning order flow produces a brief dip through 2300 even if the broader trend remains constructive.

## Disconfirming signals to watch

- ETH moving back toward 2300 before the final hours.
- Binance 1-minute candles repeatedly printing near or below 2300 ahead of noon ET.
- Exchange-specific divergence on Binance versus broader ETH market pricing.

## What would increase confidence

- ETH trading materially higher, e.g. comfortably above the low-2330s, into the final morning.
- Additional exchange-specific evidence showing stable support above 2300 during the U.S. session.

## Net update logic

The direct exchange evidence is enough to justify a Yes lean because the current level is above the threshold and not by a trivial amount. But the risk-manager adjustment is to avoid treating current spot as equivalent to settlement probability. A one-minute, one-exchange, one-time contract should trade with more humility than a generic “ETH above 2300 tomorrow” proposition.

## Suggested downstream use

Use as an orchestrator synthesis input emphasizing that the right disagreement question is confidence calibration, not a strong directional contrarian call.