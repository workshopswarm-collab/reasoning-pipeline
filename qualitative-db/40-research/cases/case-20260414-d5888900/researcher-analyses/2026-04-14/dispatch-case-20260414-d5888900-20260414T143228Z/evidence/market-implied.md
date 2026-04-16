---
type: evidence_map
case_key: case-20260414-d5888900
dispatch_id: dispatch-case-20260414-d5888900-20260414T143228Z
research_run_id: 50382375-b500-45da-b4ab-19c8d27d0820
analysis_date: 2026-04-14
persona: market-implied
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-70-000-on-april-14
question: "Will the price of Bitcoin be above $70,000 on April 14?"
driver: reliability
date_created: 2026-04-14
agent: orchestrator
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["bitcoin"]
related_drivers: ["reliability", "operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260414-d5888900/researcher-analyses/2026-04-14/dispatch-case-20260414-d5888900-20260414T143228Z/personas/market-implied.md"]
tags: ["evidence-map", "binance", "threshold-market"]
---

# Summary

The evidence nets to a strong Yes lean because both the contract source and current Binance exchange context line up with the market's extreme pricing. The main residual risk is not trend-level thesis error but a narrow point-in-time print risk at the exact resolving minute.

## Question being evaluated

Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-14 close above 70,000?

## Current lean

Strong Yes.

## Prior / starting view

Start from market price as prior: 0.9995 implies about 99.95% Yes.

## Evidence supporting the claim

- Polymarket rules specify a simple, exchange-specific threshold test on Binance BTC/USDT.
  - Source: source note on Polymarket rules.
  - Why it matters causally: narrows the problem to one exact observable.
  - Direct or indirect: direct for resolution mechanics.
  - Weight: high.

- Binance spot ticker shortly before resolution was around 75,635, far above 70,000.
  - Source: Binance API check note.
  - Why it matters causally: shows the market only fails if BTC drops more than about 7% before the resolving minute.
  - Direct or indirect: contextual but exchange-direct.
  - Weight: high.

- Recent Binance 1-minute and 1-hour candles on the same day were also above 70,000.
  - Source: Binance API check note.
  - Why it matters causally: supports that being above 70k is not a one-tick anomaly.
  - Direct or indirect: contextual.
  - Weight: medium-high.

## Evidence against the claim

- The contract settles on one exact minute close at noon ET, not on current price or daily average.
  - Source: Polymarket rules note.
  - Why it matters causally: introduces point-in-time path dependence.
  - Direct or indirect: direct.
  - Weight: medium.

- Exact 16:00 UTC 1-minute candle could not be directly verified before it occurred.
  - Source: Binance API check note.
  - Why it matters causally: prevents direct settlement-level confirmation during the run.
  - Direct or indirect: direct process limitation.
  - Weight: medium.

- Binance-specific wick, outage, or unusual microstructure event could still create a losing print.
  - Source: assumption note plus contract design.
  - Why it matters causally: exchange-specific operational anomalies matter for these contracts.
  - Direct or indirect: indirect risk.
  - Weight: low-medium.

## Ambiguous or mixed evidence

- CoinGecko daily history showed BTC around 74.5k on the date, which is supportive context but not relevant for settlement because the contract is Binance-specific and minute-specific.

## Conflict between inputs

No meaningful factual conflict across checked sources. The main issue is scope: contextual sources support the market strongly, but only the exact Binance noon candle can settle it.

## Key assumptions

- No >7% selloff into the noon ET minute.
- No Binance-specific print anomaly at the exact resolution minute.
- The contract wording maps cleanly to the noon ET / 16:00 UTC candle.

## Key uncertainties

- Final exact 12:00 ET close value before the minute is complete.
- Whether any exchange-specific operational irregularity appears at the resolving minute.

## Disconfirming signals to watch

- Sudden BTC drawdown during the last pre-noon hour.
- Binance-only price dislocation.
- Resolution interpretation dispute over timestamp labeling.

## What would increase confidence

- Direct observation of the completed Binance 12:00 ET 1-minute candle close.
- Independent archival capture of the same Binance minute print.

## Net update logic

The market started at an extreme Yes prior and the evidence failed to uncover a serious reason to fade it. The most important update was verifying that Binance itself still had BTC/USDT in the mid-75k area shortly before noon ET, making the remaining No path mostly a narrow operational or crash-path tail risk rather than a broad informational disagreement.

## Suggested downstream use

- orchestrator synthesis input
- retrospective evaluation of extreme same-day threshold markets
- source collection gap note: archive final resolving candle when available