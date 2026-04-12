---
type: assumption_note
case_key: case-20260409-a6f5ffd8
dispatch_id: dispatch-case-20260409-a6f5ffd8-20260409T071326Z
research_run_id: b64b792e-f7f1-456e-9388-296ac223bc91
analysis_date: 2026-04-09
persona: base-rate
domain: crypto
subdomain: market-structure
entity: bitcoin
topic: will-the-binance-btc-usdt-1-minute-candle-for-12-00-et-on-2026-04-09-close-above-70000
question: "Will the Binance BTC/USDT 1-minute candle for 12:00 ET on 2026-04-09 close above 70000?"
driver: operational-risk
date_created: 2026-04-09
agent: base-rate
status: active
certainty: medium
importance: high
time_horizon: intraday
related_entities: ["bitcoin"]
related_drivers: ["operational-risk"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/base-rate.md"]
tags: ["assumption", "timestamp", "resolution", "binance"]
---

# Assumption

The relevant resolving candle is the Binance BTC/USDT 1-minute candle that opens at 12:00:00 ET on 2026-04-09, which corresponds to 16:00:00 UTC because New York is on EDT (UTC-4).

## Why this assumption matters

The market resolves on a single minute close, so using the wrong timestamped candle would flip the answer in edge cases and make the estimate meaningless.

## What this assumption supports

- The timing conversion used in the final finding.
- The view that the market is mostly an intraday threshold-holding problem rather than a longer-horizon directional crypto thesis.
- The operational conclusion that timestamp interpretation is the main non-price risk to the analysis.

## Evidence or logic behind the assumption

- The market description explicitly says `12:00 in the ET timezone (noon)`.
- April 9 in New York is daylight saving time, so ET is EDT = UTC-4.
- Binance kline documentation says klines are identified by open time and defaults are UTC unless a timezone override is supplied.
- Therefore the noon ET candle maps cleanly to the candle opening at 16:00:00 UTC.

## What would falsify it

- A clarified resolution rule from Polymarket indicating a different timestamp convention.
- Binance UI behavior showing the cited 12:00 ET candle corresponds to a different underlying UTC open time.
- Evidence that the market intends the minute ending at noon ET rather than the minute beginning at noon ET.

## Early warning signs

- Conflicting interpretations in related market comments or rule clarifications.
- UI/API mismatch between Binance chart labels and API kline indexing.
- Settlement examples from similar contracts showing an unexpected candle-selection convention.

## What changes if this assumption fails

The main probability estimate would need reassessment because the target minute could shift by one candle, making the live pre-noon price path and microstructure more important than the broader outside view.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260409-a6f5ffd8/researcher-analyses/2026-04-09/dispatch-case-20260409-a6f5ffd8-20260409T071326Z/personas/base-rate.md