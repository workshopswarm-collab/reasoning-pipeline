---
type: assumption_note
case_key: case-20260409-21554cf3
dispatch_id: dispatch-case-20260409-21554cf3-20260409T073402Z
research_run_id: 35ef18d5-29cb-4cda-9899-ee727930a784
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: spot-market-resolution
entity: ethereum
topic: will-the-binance-eth-usdt-1-minute-candle-for-2026-04-09-12-00-et-close-above-2100
question: "Will the Binance ETH/USDT 1-minute candle for 2026-04-09 12:00 ET close above 2100?"
driver: operational-risk
date_created: 2026-04-09
agent: Orchestrator
status: active
certainty: medium
importance: medium
time_horizon: intraday
related_entities: ["ethereum"]
related_drivers: ["operational-risk"]
proposed_entities: ["binance-global"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/base-rate.md"]
tags: ["assumption", "timezone", "binance", "intraday"]
---

# Assumption

The market's `12:00 ET` resolution minute can be cleanly operationalized as the Binance ETHUSDT 1-minute candle opening at 2026-04-09 16:00:00 UTC and closing at 16:00:59.999 UTC.

## Why this assumption matters

The directional call depends on matching Polymarket's ET wording to Binance's candle mechanics correctly; a bad timezone or candle-boundary interpretation could flip a seemingly simple market.

## What this assumption supports

- treating the contract as narrow but operationally clear rather than ambiguous
- using current ETHUSDT level versus 2100 as meaningful contextual evidence
- framing the remaining uncertainty as market volatility into noon rather than contract interpretation risk

## Evidence or logic behind the assumption

Polymarket rules explicitly specify Binance ETH/USDT, `1m`, and `12:00` in ET. Binance docs say klines are uniquely identified by open time and that request timestamps are interpreted in UTC. Converting 2026-04-09 12:00 ET yields 2026-04-09 16:00 UTC, so the noon ET candle should be the 16:00 UTC 1-minute bar.

## What would falsify it

- Binance or Polymarket clarifies that the relevant candle is labeled by close time rather than open time
- Binance UI for the specified surface shows a different minute labeling convention for ET noon
- contract clarifications specify a different operational mapping

## Early warning signs

- mismatch between Binance UI candle label and API kline open-time convention
- visible community dispute over which minute counts
- a later settlement note using a different timestamp than 16:00 UTC

## What changes if this assumption fails

If the minute mapping is wrong, the current estimate becomes less reliable and the settlement risk shifts from mostly price-path uncertainty to rules/ops uncertainty.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-21554cf3/researcher-analyses/2026-04-09/dispatch-case-20260409-21554cf3-20260409T073402Z/personas/base-rate.md