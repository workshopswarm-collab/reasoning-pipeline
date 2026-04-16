---
type: evidence_map
case_key: case-20260414-e15c72fe
dispatch_id: dispatch-case-20260414-e15c72fe-20260414T193100Z
research_run_id: c958fe5d-a1eb-47f0-b106-8df07f8d1ea2
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the price of Bitcoin be above $70,000 on April 20?"
driver: reliability
date_created: 2026-04-14
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["market-implied-finding"]
tags: ["evidence-map", "btc", "market-implied"]
---

# Summary

The evidence nets to a high-probability Yes view that is close to, but slightly below, the market's confidence. The market appears mostly efficient because current Binance BTC/USDT pricing is materially above the threshold and the remaining risk is mainly short-horizon volatility plus the exact minute-close contract mechanic.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle labeled 12:00 PM ET on April 20, 2026 have a final Close price strictly above 70,000?

## Current lean

Lean Yes, high probability but not near-certainty.

## Prior / starting view

The starting baseline was the market price from the assignment, 0.845, implying 84.5% Yes before fresh verification.

## Evidence supporting the claim

- Binance spot at research time was 74,258.35.
  - Source: 2026-04-14-market-implied-binance-and-coingecko-price-context.md
  - Why it matters: direct venue-level evidence on the exact exchange and pair named in the contract.
  - Direct or indirect: direct.
  - Weight: high.

- Recent Binance daily closes in the sampled 7-day window all printed above 70,000.
  - Source: 2026-04-14-market-implied-binance-and-coingecko-price-context.md
  - Why it matters: shows the threshold has been maintained across recent closes despite ordinary volatility.
  - Direct or indirect: direct to exchange context, indirect to the exact resolving minute.
  - Weight: medium-high.

- Polymarket's own ladder was internally coherent: 70k around 89%-90%, 72k around 79%, 74k around 62%.
  - Source: 2026-04-14-market-implied-polymarket-rules-and-curve.md
  - Why it matters: suggests traders are not blindly assuming endless upside; they are pricing a sensible downside distribution around the current spot.
  - Direct or indirect: indirect/contextual.
  - Weight: medium.

## Evidence against the claim

- The contract resolves on one exact 1-minute Binance close at noon ET, not on daily close, intraday high, or cross-exchange consensus.
  - Source: 2026-04-14-market-implied-polymarket-rules-and-curve.md
  - Why it matters: this introduces path dependence and a venue-specific tail risk.
  - Direct or indirect: direct to contract interpretation.
  - Weight: high.

- A roughly 6% drawdown from current spot would be enough to flip the outcome.
  - Source: derived from direct Binance spot versus threshold, documented in the assumption note.
  - Why it matters: BTC can move that far over several days without requiring an extreme regime change.
  - Direct or indirect: indirect/scenario logic.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- CoinGecko matched Binance spot context closely, which supports broad price coherence, but it is not the settlement source and therefore does not reduce contract-specific minute-close risk very much.

## Conflict between inputs

There was little factual conflict. The main tension is weighting-based: whether current spot being comfortably above 70k should dominate, or whether minute-specific and exchange-specific settlement mechanics deserve a larger discount.

## Key assumptions

- BTC remains in the current mid-70k trading regime through April 20.
- Binance BTC/USDT remains a reliable and representative price venue at the resolving minute.
- No sudden macro or crypto-specific shock produces a >6% selloff into the deadline.

## Key uncertainties

- Short-horizon realized volatility over the next six days.
- Whether noon ET on April 20 coincides with unusual volatility.
- Any Binance-specific operational or pricing irregularity.

## Disconfirming signals to watch

- BTC slipping back toward low-71k or sub-71k before April 20.
- Binance-specific issues or price dislocations.
- Market repricing in nearby ladder outcomes suggesting increased downside fear.

## What would increase confidence

- Continued BTC trading above 72k into the weekend.
- Additional direct Binance minute-level stability checks closer to resolution.
- No adverse exchange-operational headlines.

## Net update logic

The fresh direct-exchange pass supports the market's broad stance: a threshold sitting about 4.3k below current Binance spot with only six days left should be favored. The main reason not to fully match the market's highest prints is contract specificity: a single minute-close on one exchange deserves a residual volatility/operational discount.

## Suggested downstream use

Use this as orchestrator synthesis input and as a check against overly contrarian researchers. The main actionable takeaway is that market confidence looks mostly justified, but not so justified that minute-close mechanics can be ignored.