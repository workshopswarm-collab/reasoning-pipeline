---
type: assumption_note
case_key: case-20260414-3ce42d6c
research_run_id: 59deb394-7128-406b-8ea8-467e8851fb0c
analysis_date: 2026-04-14
persona: base-rate
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: bitcoin-above-70k-on-april-14
question: "Will the price of Bitcoin be above $70,000 on April 14?"
driver: operational-risk
date_created: 2026-04-14
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "binance", "intraday", "resolution"]
dispatch_id: dispatch-case-20260414-3ce42d6c-20260414T130958Z
---

# Assumption

BTC/USDT on Binance will remain above 70,000 through the specific noon ET 1-minute close, and the Binance UI candle used for settlement will align with Binance public market data surfaces.

## Why this assumption matters

The bullish base-rate view is not about long-run Bitcoin strength alone; it depends on the price staying above the threshold at one exact intraday timestamp and on no material mismatch between data surfaces.

## What this assumption supports

- A very high Yes probability despite the still-open clock.
- A view that the remaining risk is mostly short-horizon volatility or settlement-surface mismatch rather than broad directional uncertainty.

## Evidence or logic behind the assumption

- Same-day Binance spot price and 5-minute average were both around 74.5k to 74.6k, leaving a margin of roughly 6% above the 70k threshold.
- Polymarket market pricing at 0.9995 implies near-consensus that the threshold is comfortably in the money.
- Intraday moves of more than 6% over a few hours are possible in crypto but are not the default base rate absent a catalyst.

## What would falsify it

- Binance BTC/USDT trades down below 70,000 by the 12:00 ET candle close.
- A Binance outage, data anomaly, or UI/API discrepancy causes the settlement candle to print differently from expected.
- A sudden market-wide shock produces an unusually large intraday drawdown before noon ET.

## Early warning signs

- Rapid acceleration downward toward 72k or lower in the late morning ET window.
- Exchange instability or abnormal Binance market-data behavior.
- Conflicting candle values across Binance surfaces close to the resolution minute.

## What changes if this assumption fails

The market could resolve No despite BTC having spent most of the day above 70k, and the research conclusion would have materially overstated effective certainty.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/personas/base-rate.md