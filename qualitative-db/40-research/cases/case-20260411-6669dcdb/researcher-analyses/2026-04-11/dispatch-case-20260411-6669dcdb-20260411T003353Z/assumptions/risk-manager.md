---
type: assumption_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
research_run_id: b1bd99f0-882e-480f-929a-51b75f160793
analysis_date: 2026-04-11
persona: risk-manager
domain: crypto
subdomain: bitcoin
entity: bitcoin
topic: will-the-binance-btc-usdt-1m-candle-for-2026-04-11-12-00-et-close-above-72000
question: "Will the Binance BTC/USDT 1m candle for 2026-04-11 12:00 ET close above 72000?"
driver: operational-risk
date_created: 2026-04-10
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["risk-manager finding", "risk-manager evidence map"]
tags: ["resolution-assumption", "timezone", "candle"]
---

# Assumption

The Polymarket contract will effectively map to the Binance BTCUSDT 1-minute candle whose interval begins at 2026-04-11 12:00:00 ET (16:00:00 UTC), and the decisive value is that candle's final close field.

## Why this assumption matters

The market is narrow and date-specific, so a one-minute timing or chart-interpretation mismatch could flip resolution even if the broader directional BTC thesis is right.

## What this assumption supports

- The conclusion that the contract is mostly a short-horizon BTC spot-level question rather than a broader Bitcoin sentiment question.
- The estimate that current spot trading modestly above 72k makes Yes more likely than No.
- The decision to treat exchange-specific operational interpretation as the main residual risk after price direction.

## Evidence or logic behind the assumption

- Polymarket rules explicitly name Binance BTC/USDT, 1m candles, and the candle for 12:00 in ET.
- Binance kline documentation says candles are uniquely identified by open time and field 4 is the close price.
- Time-zone conversion from 12:00 ET on 2026-04-11 lands at 16:00 UTC because the date is in daylight saving time.

## What would falsify it

- Evidence from the Binance chart UI or Polymarket resolution guidance showing they instead use the minute ending at 12:00 ET rather than the minute beginning at 12:00 ET.
- A chart/UI convention or late edit that causes the displayed noon ET candle to correspond to a different UTC slice.
- A Binance chart anomaly where UI close differs from the API close used for the same minute.

## Early warning signs

- Inconsistent labeling between Binance API timestamps and the website candle displayed for noon ET.
- Polymarket comments or prior resolutions showing ambiguity around whether the 12:00 candle refers to open-time or close-time labeling.
- Unusual Binance UI refresh lag near the resolution minute.

## What changes if this assumption fails

If the noon ET candle is interpreted differently, the directional price thesis may still be right but the exact contract estimate could move several points because the wrong minute may be materially above or below 72k.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/risk-manager.md`
- `qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/evidence/risk-manager.md`