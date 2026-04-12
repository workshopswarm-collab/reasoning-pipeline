---
type: assumption_note
case_key: case-20260411-6669dcdb
dispatch_id: dispatch-case-20260411-6669dcdb-20260411T003353Z
research_run_id: 58a350f1-0abd-4473-8de6-51e9f9eb54d4
analysis_date: 2026-04-11
persona: catalyst-hunter
domain: crypto
subdomain: intraday-market-structure
entity: bitcoin
topic: bitcoin-above-72k-on-april-11
question: "Will the price of Bitcoin be above $72,000 on April 11?"
driver: operational-risk
date_created: 2026-04-11
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/catalyst-hunter.md"]
tags: ["timing", "timezone", "candle-close"]
---

# Assumption

The operative resolution minute is the Binance BTC/USDT 1-minute candle that closes at 12:00 ET / 16:00 UTC on 2026-04-11, and the API-visible candle close should match the Binance chart close referenced in the rules.

## Why this assumption matters

The thesis depends on translating the contract language into the correct minute and reading the correct close field. A one-hour timezone mistake or UI/API mismatch would break the analysis.

## What this assumption supports

- The directional probability estimate.
- The judgment that the dominant remaining catalyst is intraday downside before noon ET.
- The view that current spot being above 72,000 is materially informative for the contract.

## Evidence or logic behind the assumption

- The rules explicitly reference 12:00 ET, Binance BTC/USDT, 1m candles, and the final close price.
- April in New York is in daylight saving time, so noon ET maps to 16:00 UTC.
- Binance API 1-minute kline queries behaved as expected on a control timestamp, supporting that the endpoint can be used to sanity-check the relevant minute.

## What would falsify it

- Evidence that Polymarket or Binance interprets the relevant candle differently, such as the candle opening at 12:00 ET rather than closing then.
- Evidence that Binance chart display used for settlement diverges from the API candle close.
- Evidence that the market intended EST rather than ET/DST-aware Eastern Time.

## Early warning signs

- Community dispute over which exact minute counts.
- Binance UI showing a close that differs from API-derived close for the same minute.
- Documentation or market comments indicating alternative timestamp handling.

## What changes if this assumption fails

The current estimate would need review, and contract-interpretation risk would move from secondary caveat to primary driver.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260411-6669dcdb/researcher-analyses/2026-04-11/dispatch-case-20260411-6669dcdb-20260411T003353Z/personas/catalyst-hunter.md