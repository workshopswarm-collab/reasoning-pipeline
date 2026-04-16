---
type: evidence_map
case_key: case-20260415-10579f0a
dispatch_id: dispatch-case-20260415-10579f0a-20260415T184424Z
research_run_id: 624142da-6408-4082-b26d-77fdcd2fb897
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-17
question: "Will the price of Bitcoin be above $70,000 on April 17?"
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
downstream_uses: ["qualitative-db/40-research/cases/case-20260415-10579f0a/researcher-analyses/2026-04-15/dispatch-case-20260415-10579f0a-20260415T184424Z/personas/risk-manager.md"]
tags: ["evidence-map", "bitcoin", "risk-manager"]
---

# Summary

The evidence nets to a clear Yes lean, but the main residual risk is that traders may be pricing this like a nearly settled market when it is still a date-specific exchange-close contract with about two days of path risk left.

## Question being evaluated

Will Binance BTC/USDT print a final 1-minute candle close above 70,000 at 12:00 ET on 2026-04-17?

## Current lean

Lean Yes, high probability but not quite as high as the market.

## Prior / starting view

Starting view was that a 96.5% market price likely reflected BTC already being comfortably above 70k, but needed rule/timing verification because the contract resolves off one exact candle on one venue.

## Evidence supporting the claim

- **Polymarket rules specify a simple threshold test on Binance BTC/USDT 12:00 ET 1m close**  
  - Source: source note on Polymarket rules + Binance verification  
  - Why it matters: narrows the question to one operationally precise condition rather than a broader average-price interpretation  
  - Direct or indirect: direct for contract mechanics  
  - Weight: high

- **Binance public API showed BTCUSDT around 74,290 during the run**  
  - Source: same source note  
  - Why it matters: spot is roughly 5.8% above the threshold, giving material buffer  
  - Direct or indirect: contextual to future resolution, direct to current exchange-specific level  
  - Weight: high

- **Sampled recent 1-minute range stayed above 70,000**  
  - Source: same source note  
  - Why it matters: recent realized trading range does not yet threaten the threshold  
  - Direct or indirect: contextual  
  - Weight: medium

## Evidence against the claim

- **Contract resolves on one exact minute, not on prevailing spot over the next two days**  
  - Source: market rules  
  - Why it matters: path dependency and timing risk are real even when spot is comfortably above threshold  
  - Direct or indirect: direct to contract interpretation  
  - Weight: high

- **BTC can move several percent quickly, especially under liquidation or macro shock**  
  - Source: general market structure inference from short-horizon crypto volatility, not directly quantified in this run  
  - Why it matters: the current 5.8% cushion is meaningful but not unbreakable over ~44 hours  
  - Direct or indirect: contextual  
  - Weight: medium

- **Exchange-specific operational/data risk remains nonzero**  
  - Source: rules dependence on Binance-specific candle  
  - Why it matters: a venue-specific anomaly matters more than broad BTC price consensus because only Binance BTCUSDT counts  
  - Direct or indirect: direct to settlement mechanics  
  - Weight: low-to-medium

## Ambiguous or mixed evidence

- Recent intraday range is supportive, but one day of relatively calm trading does not fully eliminate tail downside over the remaining window.
- The market’s extreme price may partly encode rational confidence from a wide price buffer, but may also underprice the fragility of a single-minute settlement condition.

## Conflict between inputs

There is no major factual conflict between the checked inputs. The main disagreement is weighting-based: whether a ~5.8% buffer with two days left deserves 96.5% confidence or something modestly lower.

## Key assumptions

- Binance remains the operative source and prints normal candles.
- No major crypto-wide drawdown pushes BTCUSDT below 70k into the settlement minute.
- ET-to-UTC mapping is handled correctly, with the relevant candle opening at 16:00:00 UTC on April 17.

## Key uncertainties

- Short-horizon BTC volatility between now and settlement.
- Whether any macro/news catalyst arrives before noon ET April 17.
- Low-probability exchange-specific anomalies.

## Disconfirming signals to watch

- BTCUSDT falling rapidly toward 71k-70k on Binance.
- Abnormal exchange behavior or missing/erratic 1-minute candles.
- Market structure stress suggesting forced selling into the settlement window.

## What would increase confidence

- BTCUSDT holding well above 72k into late April 16 / early April 17.
- Continued normal Binance data behavior.
- Absence of major macro or crypto-specific negative catalyst.

## Net update logic

The key update was not directional so much as mechanical: once the contract was confirmed to depend on a single Binance BTCUSDT 1-minute close at noon ET, the main task became assessing whether the current buffer was large enough to justify the market’s extreme confidence. The answer is mostly yes, but not completely. The market appears directionally right, yet slightly too confident given remaining path and operational risk.

## Suggested downstream use

Use as an orchestrator synthesis input emphasizing that this is a likely Yes but should be treated as a still-live timestamped contract rather than a fully settled one.