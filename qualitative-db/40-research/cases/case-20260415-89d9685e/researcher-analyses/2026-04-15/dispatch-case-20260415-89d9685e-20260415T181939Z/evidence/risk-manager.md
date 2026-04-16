---
type: evidence_map
case_key: case-20260415-89d9685e
dispatch_id: dispatch-case-20260415-89d9685e-20260415T181939Z
research_run_id: 5da10d14-5e35-4aca-b3c2-87262ddef2b8
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: exchange-market-data
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-72-000-on-april-16
question: "Will the price of Bitcoin be above $72,000 on April 16?"
driver: operational-risk
date_created: 2026-04-15
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
tags: ["evidence-map", "bitcoin", "binance", "timing-risk"]
---

# Summary

Evidence nets to a clear "Yes" lean, but the main reason to stay below the market's confidence is that this contract settles on one exact Binance minute close and crypto can move several percent in a day.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for April 16 at 12:00 ET have a final close above 72,000?

## Current lean

Yes is more likely than not and likely materially favored, but not as close to certain as a 94% market price suggests.

## Prior / starting view

Starting view was that a 94% market price might be too confident unless the current Binance level sat far enough above 72,000 and the contract mechanics were straightforward.

## Evidence supporting the claim

- Binance API and Binance data API both showed recent BTC/USDT 1-minute closes around 74.3k.
  - Direct evidence.
  - High weight because the contract settles on Binance BTC/USDT 1-minute close data.
- The current level is about 3.1% above the threshold.
  - Derived from direct source data.
  - Medium-high weight because it frames how much downside is required to lose.
- Recent sampled 1-minute closes in the collected window stayed above 72,000.
  - Direct but time-limited evidence.
  - Medium weight because it reduces immediate concern about the threshold being marginal.
- Polymarket's rules clearly define the settlement source and the condition as a strict close above 72,000.
  - Direct contract evidence.
  - High weight for interpretation, not direction.

## Evidence against the claim

- The contract settles on one exact minute close tomorrow, not today's level.
  - Direct structural risk.
  - High weight because a one-minute contract is vulnerable to timing/path variance.
- BTC only needs about a 3.1% decline from sampled current levels to lose.
  - Derived risk metric.
  - High weight because that size move is plausible over a day in crypto.
- Both current-state price checks come from Binance-controlled surfaces.
  - Source-quality limitation.
  - Medium weight because it limits independence even while improving direct relevance.

## Ambiguous or mixed evidence

- The Binance website UI was not directly readable in this environment, while the APIs were. That is not a contradiction, but it means operational verification leaned on API surfaces rather than the visible chart UI.

## Conflict between inputs

There was no meaningful factual conflict between the Polymarket rules page and Binance API data. The real disagreement is interpretive: whether a current ~74.3k level justifies a confidence estimate near 94% for a single-minute settlement tomorrow.

## Key assumptions

- Current Binance BTC/USDT level is a useful anchor for the settlement minute.
- No exchange-specific dislocation or sharp downside move occurs by noon ET on April 16.
- The relevant candle labeled for 12:00 ET maps to the expected UTC-converted minute.

## Key uncertainties

- Overnight/intraday volatility before settlement.
- Exchange-specific operational or pricing anomalies on Binance.
- Residual minute-label interpretation risk, though the ET conversion itself is straightforward.

## Disconfirming signals to watch

- BTC moving down toward or below 72k during the hours before noon ET.
- Rising Binance-specific basis or operational instability.
- Any clarification suggesting a different exact candle than assumed.

## What would increase confidence

- Fresh Binance verification closer to the settlement minute still showing BTC comfortably above 72k.
- Evidence of subdued volatility into the settlement window.

## Net update logic

The contract is mechanically simple once source-of-truth is pinned down: Binance BTC/USDT, 1-minute close, noon ET. Current direct-source pricing well above 72k supports Yes, but the remaining gap is not enormous for crypto, so risk-adjusted confidence should be lower than the market's current extreme reading.

## Suggested downstream use

Use as synthesis input and as an audit trail for why the risk-manager view is "Yes, but with less confidence than the market price implies."