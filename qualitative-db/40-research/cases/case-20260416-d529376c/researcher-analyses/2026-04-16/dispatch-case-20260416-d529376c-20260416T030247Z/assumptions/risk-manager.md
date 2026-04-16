---
type: assumption_note
case_key: case-20260416-d529376c
dispatch_id: dispatch-case-20260416-d529376c-20260416T030247Z
research_run_id: 15023e2f-188e-41f3-af65-e46f04fd7220
analysis_date: 2026-04-16
persona: risk-manager
domain: crypto
subdomain: markets
entity: sol
topic: will-the-binance-sol-usdt-12-00-et-1-minute-candle-on-2026-04-19-close-above-80
question: "Will the Binance SOL/USDT 12:00 ET 1-minute candle on 2026-04-19 close above 80?"
driver: operational-risk
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-19 12:00 ET"
related_entities: ["sol"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/personas/risk-manager.md", "qualitative-db/40-research/cases/case-20260416-d529376c/researcher-analyses/2026-04-16/dispatch-case-20260416-d529376c-20260416T030247Z/evidence/risk-manager.md"]
tags: ["assumption", "volatility-buffer", "timing-risk"]
---

# Assumption

SOL will retain enough cushion above 80 over the next ~3.5 days that ordinary crypto volatility does not push the specific Apr 19 noon ET Binance one-minute close below the threshold.

## Why this assumption matters

The bullish case is not that SOL is merely strong in general, but that it stays above a fixed strike at one exact minute. If the buffer over 80 is not durable, the market can resolve No even if the broader trend still looks healthy.

## What this assumption supports

- A probability estimate above 50%
- A view that current spot above 85 is meaningful rather than illusory
- A view that recent trading range gives some margin over the 80 threshold

## Evidence or logic behind the assumption

- Binance daily candles for the last 10 days all closed above 80.
- Recent hourly closes stayed in an approximately 81.7 to 87.3 band over the last 72 hours.
- Current Binance and Coinbase spot readings were both around 85.3, suggesting no obvious exchange-specific distortion at review time.

## What would falsify it

- A sharp crypto-wide risk-off move that takes SOL back near or below 80 before Apr 19 noon ET.
- Exchange-specific stress, listing anomaly, or sudden venue dislocation on Binance SOL/USDT.
- Repeated failure to hold the low-80s region in the next 1-2 days.

## Early warning signs

- SOL losing the recent 82-83 support area on Binance.
- A broad altcoin selloff led by BTC/ETH weakness or macro risk sentiment.
- Binance-specific operational issues or unusual basis divergence versus other major exchanges.

## What changes if this assumption fails

The probability should move materially lower because the contract depends on a single minute. Once SOL trades near the strike shortly before resolution, path risk becomes much more important than the current directional backdrop.

## Notes that depend on this assumption

- Main finding: risk-manager persona note for this dispatch
- Evidence map: risk-manager evidence netting for this dispatch