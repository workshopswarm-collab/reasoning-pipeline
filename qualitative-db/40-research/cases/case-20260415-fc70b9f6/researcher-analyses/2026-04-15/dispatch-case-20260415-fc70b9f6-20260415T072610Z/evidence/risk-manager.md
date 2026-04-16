---
type: evidence_map
case_key: case-20260415-fc70b9f6
dispatch_id: dispatch-case-20260415-fc70b9f6-20260415T072610Z
research_run_id: 27d30a87-b55a-4dd9-bd93-07de68d357e5
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-72k-on-april-16
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-16 close above 72000?"
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
tags: ["evidence-map", "path-risk", "settlement-mechanics", "btc"]
---

# Summary

Direct Binance price context supports Yes, but the risk-manager view emphasizes that the contract is fragile to one specific minute close rather than the broader trend.

## Question being evaluated

Whether Binance BTC/USDT will have a final 1-minute candle close above 72,000 for the 12:00 ET candle on April 16, 2026.

## Current lean

Lean Yes, but with a modest discount to the market because the market appears to price in high confidence despite narrow timestamp risk.

## Prior / starting view

Starting view from market price: approximately 80% Yes, implying traders see the threshold as safely below spot.

## Evidence supporting the claim

- Binance live ticker and recent 1-minute klines show BTCUSDT around 73.7k during the run, roughly 1.7k above the threshold. Direct evidence. High weight.
- Binance 24h low from the direct ticker pull was 73,592.36, still above 72,000. Direct evidence. High weight.
- Recent daily Binance klines show BTC closed above 72k on most nearby dates, including April 14 and remained above 72k on April 15 during this run. Direct/contextual mix. Medium weight.
- The Polymarket rules explicitly point to Binance BTC/USDT 1-minute close, removing most cross-exchange ambiguity. Direct contract evidence. High weight.

## Evidence against the claim

- The contract resolves on one exact 12:00 ET minute close, not on a daily average or broader trend. A sharp intraday move of only about 2.3% could flip outcome. Direct contract-interpretation risk. High weight.
- Binance is both trading venue and source of truth, so exchange-specific wick, temporary dislocation, or chart/API operational mismatch is a low-probability but real tail risk. Direct/contextual risk. Medium weight.
- BTC had already drifted down from the 24h high near 76k into the 73.7k area, showing that multi-percent moves within a day are feasible. Direct evidence. Medium weight.

## Ambiguous or mixed evidence

- The market being priced near 80-85% could be read as efficient confidence or as slight overconfidence given timestamp fragility.
- Recent trend is mildly downward intraday, but still far enough above threshold that ordinary noise may not matter.

## Conflict between inputs

No major factual conflict. The tension is mostly weighting-based: how much probability mass to put on one-minute path risk despite a comfortable current cushion.

## Key assumptions

- BTC remains above 72k through the settlement window with no sudden downside shock.
- Binance’s settlement surface behaves consistently with its API/documentation.
- No unusual exchange-specific event distorts the exact fixing minute.

## Key uncertainties

- Overnight and next-morning BTC volatility.
- Whether any macro or crypto-specific catalyst emerges before noon ET.
- Whether Binance-specific microstructure produces a sharp wick at the wrong moment.

## Disconfirming signals to watch

- BTCUSDT trading down toward 72.5k or lower ahead of settlement.
- Rising downside volatility during the U.S. morning on April 16.
- Any Binance outage, chart discrepancy, or anomalous candle behavior.

## What would increase confidence

- BTC holding above 73k through the overnight and morning sessions.
- A fresh direct check of Binance 1-minute candles close to settlement time showing continued cushion.
- No operational issues on Binance.

## Net update logic

The direct-source evidence makes Yes the base case, but the risk-manager adjustment is to avoid treating an above-threshold spot price as equivalent to a locked result. The narrow settlement mechanics justify some discount versus the market’s embedded confidence.

## Suggested downstream use

Use as synthesis input and as a check against overconfident consensus. This note is mainly for probability calibration rather than for identifying a different directional thesis.