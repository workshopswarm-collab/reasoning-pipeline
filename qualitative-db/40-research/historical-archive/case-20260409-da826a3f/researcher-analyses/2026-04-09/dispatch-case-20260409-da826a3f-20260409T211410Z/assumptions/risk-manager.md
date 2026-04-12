---
type: assumption_note
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
research_run_id: 6c6dae63-899b-4d33-8486-50f3bb80d911
analysis_date: 2026-04-09
persona: risk-manager
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: will-the-price-of-bitcoin-be-above-68-000-on-april-10
question: "Will the price of Bitcoin be above $68,000 on April 10?"
driver: operational-risk
date_created: 2026-04-09
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-10 12:00 ET"
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["timing", "binance", "settlement", "assumption"]
---

# Assumption

The Binance website candle used by Polymarket for settlement will align with Binance spot API 1-minute BTCUSDT klines such that the relevant settlement bar is the 12:00 ET / 16:00 UTC minute on 2026-04-10.

## Why this assumption matters

The directional view is easy only if the contract is interpreted on the correct minute boundary. A timezone or bar-label mismatch is one of the few realistic ways to make a nearly certain-looking trade operationally wrong.

## What this assumption supports

- The conclusion that current spot around 72.3k implies a very high probability of finishing above 68k.
- The claim that the most important residual risk is path/timing risk rather than contract ambiguity.
- The use of Binance API documentation as meaningful verification for the website-based settlement source.

## Evidence or logic behind the assumption

- Polymarket rules explicitly say the relevant source is Binance BTC/USDT with 1m candles selected.
- Binance docs state that klines are uniquely identified by open time and can be interpreted in a provided timezone.
- April 10, 2026 in New York is during daylight saving time, so noon ET is 16:00 UTC.
- Live kline timestamp checks during this run mapped correctly between UTC and ET.

## What would falsify it

- Evidence that Binance website chart labels the noon ET candle differently from the API's `timeZone=-4` interpretation.
- A Polymarket clarification or prior precedent showing that "12:00 ET" refers to a different bar labeling convention than the open-time minute.
- Visible discrepancy between the website candle close and API close for the same displayed minute.

## Early warning signs

- Inconsistent timestamps between Binance web chart and API output.
- Trader confusion or public dispute over which exact minute counts.
- Binance UI showing local-browser-time formatting that obscures the actual settlement bar.

## What changes if this assumption fails

Confidence should drop materially and the case would require direct capture of the Binance website candle display at the relevant time rather than relying on API interpretation as a proxy.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260409-da826a3f/researcher-analyses/2026-04-09/dispatch-case-20260409-da826a3f-20260409T211410Z/personas/risk-manager.md`
- `qualitative-db/40-research/cases/case-20260409-da826a3f/researcher-analyses/2026-04-09/dispatch-case-20260409-da826a3f-20260409T211410Z/evidence/risk-manager.md`