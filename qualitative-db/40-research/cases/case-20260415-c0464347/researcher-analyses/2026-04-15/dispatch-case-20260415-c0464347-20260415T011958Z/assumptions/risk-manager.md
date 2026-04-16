---
type: assumption_note
case_key: case-20260415-c0464347
dispatch_id: dispatch-case-20260415-c0464347-20260415T011958Z
research_run_id: 8357c265-76f4-4779-9bdb-36852971e867
analysis_date: 2026-04-15
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-20
question: "Will the Binance BTC/USDT 12:00 ET one-minute candle on 2026-04-20 close above 70000?"
driver: operational-risk
date_created: 2026-04-15
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-20 12:00 ET"
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "threshold-distance", "timing-risk"]
---

# Assumption

BTC can absorb normal five-day volatility and still remain above 70000 specifically at the Binance 12:00 ET one-minute close on 2026-04-20.

## Why this assumption matters

The bullish case is not just that BTC is currently above 70000, but that the cushion is large enough to survive path risk into one exact minute that determines settlement.

## What this assumption supports

- A Yes probability still above the already-high market baseline.
- The view that current spot distance from 70000 matters more than near-term narrative noise.
- The conclusion that contract/timing risk is the main residual downside rather than fundamental directional bearishness.

## Evidence or logic behind the assumption

- Live Binance price during the run is around 74632-74643, about 4630 above the threshold.
- Binance 24hr low is around 73795, still comfortably above 70000.
- That implies BTC could fall roughly 6.2%-6.6% from current levels and still resolve Yes.

## What would falsify it

- BTC loses the current cushion and starts trading near or below 71000 ahead of Apr 20.
- A volatility shock or macro/crypto-specific selloff pushes Binance BTC/USDT under 70000 near the target window.
- Evidence that ET/noon candle interpretation differs from the assumed Binance API/UI candle mapping.

## Early warning signs

- Daily range expands downward toward the threshold.
- Weekend liquidity deterioration or exchange-specific dislocation on Binance.
- Repricing in neighboring Polymarket strike markets implying a much fatter downside tail.

## What changes if this assumption fails

The market should be treated as materially less certain than 88-89%, and the edge shifts from "high but not perfect" toward a genuinely contested threshold event.

## Notes that depend on this assumption

- Main persona finding at `personas/risk-manager.md`
- Evidence map at `evidence/risk-manager.md`
