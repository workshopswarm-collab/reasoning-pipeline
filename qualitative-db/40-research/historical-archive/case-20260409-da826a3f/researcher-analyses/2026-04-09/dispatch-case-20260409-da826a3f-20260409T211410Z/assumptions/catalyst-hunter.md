---
type: assumption_note
case_key: case-20260409-da826a3f
dispatch_id: dispatch-case-20260409-da826a3f-20260409T211410Z
research_run_id: e55d5208-d3ed-470e-b218-d47cfed248d7
analysis_date: 2026-04-09
persona: catalyst-hunter
entity: bitcoin
related_entities: ["bitcoin"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
tags: ["assumption", "timing", "binance", "btc"]
driver:
---

# Assumption
The relevant settlement candle is the Binance BTC/USDT 1-minute candle that opens at 12:00 ET on 2026-04-10, which corresponds to 16:00 UTC because New York is on EDT.

## Why this assumption is needed
The contract wording references the Binance 1-minute candle for 12:00 in the ET timezone, and this case is flagged for timezone and candle-timing ambiguity. A clean operational mapping is necessary before estimating probability.

## Evidence supporting the assumption
- Polymarket rules explicitly specify the Binance 1-minute candle for 12:00 ET.
- Binance docs state klines are uniquely identified by open time.
- Binance docs state `timeZone` changes interval interpretation, but `startTime` and `endTime` stay UTC.
- Adjacent-day live verification showed 2026-04-09 16:00 UTC is the ET-noon 1-minute candle during EDT.

## Evidence against / ambiguity
- Binance website chart UI, which Polymarket names as the resolution source surface, was not directly inspected in-browser here.
- Some chart UIs visually label candles by close boundary or local display conventions, which can create superficial confusion even when API semantics are clear.

## Impact on the case if wrong
If the relevant candle were interpreted as a different minute than the 12:00 ET open minute, settlement could hinge on a neighboring 1-minute close and slightly alter probability near the threshold. In this case, the threshold is ~4.3k below spot, so minute-label ambiguity is unlikely to dominate unless BTC crashes toward 68k near settlement.

## Confidence in assumption
Medium-high.

## What would reduce uncertainty
A direct Binance chart UI check at or near the target time, or an explicit Polymarket clarification that the candle is keyed to the minute opening at 12:00 ET.
