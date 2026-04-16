---
type: evidence_map
case_key: case-20260414-1b10f4b2
dispatch_id: dispatch-case-20260414-1b10f4b2-20260414T201759Z
research_run_id: 5e806b7a-4c64-46ed-89de-158fa54d80c5
analysis_date: 2026-04-14
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-68k-on-april-20
question: "Will the price of Bitcoin be above $68,000 on April 20?"
driver: operational-risk
date_created: 2026-04-14
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
tags: ["evidence-map", "btc", "polymarket", "binance", "timing-risk"]
---

# Summary

The evidence supports a Yes lean, but with less confidence than the market price implies because settlement depends on one exact Binance one-minute close six days from now.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle at 12:00 PM ET on April 20, 2026 close above 68,000?

## Current lean

Yes, but not as confidently as the market's ~93.5% suggests.

## Prior / starting view

Starting view: likely Yes given current BTC spot level, but extreme pricing requires a contract-interpretation and timing-risk audit.

## Evidence supporting the claim

- Current Binance BTCUSDT around 74.3k; direct price context; high weight.
- Recent 24h Binance range around 73.0k-76.0k, meaning current spot is well above the threshold; direct/contextual; medium-high weight.
- Governing rule is simple conditional logic once the correct minute candle is identified; direct contract evidence; high weight.

## Evidence against the claim

- Contract is narrow: one exact minute close at 12:00 PM ET, not average daily price or broad weekly level; direct rule-based downside; high weight.
- Time to resolution is still about six days; BTC can move >8-10% over that horizon during volatile periods; contextual risk; medium-high weight.
- Settlement is Binance-specific, so exchange microstructure or idiosyncratic wick behavior matters even if cross-venue BTC stays stronger; contextual but structurally important; medium weight.

## Ambiguous or mixed evidence

- Binance API/docs strongly suggest how the candle can be retrieved, but Polymarket points to the UI chart as the settlement surface.
- Current high spot level is supportive, but may itself explain why the market is overconfident.

## Conflict between inputs

There is no major factual conflict in the checked sources. The main issue is weighting: whether current cushion above 68k justifies a probability in the mid-90s versus high-80s/low-90s.

## Key assumptions

- Binance remains the relevant and operationally reliable settlement source.
- No major BTC drawdown pushes spot near or below 68k by Apr 20 noon ET.
- The noon ET candle can be interpreted cleanly as the 16:00 UTC minute for settlement.

## Key uncertainties

- Near-term BTC volatility over the next six days.
- Any macro or crypto-specific catalyst before resolution.
- Whether Binance-specific print behavior introduces a small but nontrivial tail risk.

## Disconfirming signals to watch

- BTCUSDT losing 70k decisively.
- Sharp weekend or overnight selloff into Apr 20.
- Exchange incidents or unusual BTCUSDT wicks on Binance.

## What would increase confidence

- BTC remaining comfortably above 70k into Apr 19-20.
- Additional evidence of stable Binance BTCUSDT trading with no operational anomalies.
- A narrowing of realized volatility before settlement.

## Net update logic

The evidence keeps the base direction at Yes because spot is materially above the threshold and the contract is mechanically straightforward. The risk adjustment comes from timing specificity, exchange specificity, and the fact that market confidence is already extreme.

## Suggested downstream use

Use as orchestrator synthesis input and as a caution against treating this as a trivial near-certainty despite the current cushion above the threshold.
