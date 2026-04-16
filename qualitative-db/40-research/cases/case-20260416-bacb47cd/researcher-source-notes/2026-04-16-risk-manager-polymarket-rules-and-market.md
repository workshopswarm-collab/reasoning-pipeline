---
type: source_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
analysis_date: 2026-04-16
persona: risk-manager
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: highest-temperature-in-seoul-on-april-17-2026
question: Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher?
driver:
date_created: 2026-04-16
source_name: Polymarket market page and rules
source_type: market_rules
source_url: https://polymarket.com/event/highest-temperature-in-seoul-on-april-17-2026
source_date: 2026-04-16
credibility: medium
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/risk-manager.md
tags: [source-note, polymarket, weather, resolution-rules]
---

# Summary

The Polymarket market page establishes that this is not actually a generic Seoul-city forecast market. It resolves using the highest temperature recorded at **Incheon Intl Airport Station** on **17 Apr 2026**, using the Wunderground daily history surface once finalized, with whole-degree Celsius resolution.

## Key facts extracted

- Current market pricing on the fetched page showed `18°C or higher` around **71%**.
- The market resolves to the temperature range containing the **highest temperature recorded at the Incheon Intl Airport Station** on **17 Apr 2026**.
- The named resolution source is **Wunderground daily history** for station `RKSI`.
- The market explicitly says it **cannot resolve until data for the date has been finalized**.
- Resolution uses **whole degrees Celsius**.
- Revisions after data is finalized are not considered.

## Evidence directly stated by source

- The source of truth is not a citywide Seoul average or the Seoul/Kimpo station; it is the **Incheon Intl Airport Station** history page on Wunderground.
- Timing matters: the relevant reporting window is all times on **2026-04-17 local date** for that station.
- Whole-degree Celsius matters because a forecast near 17.x vs 18.x has threshold significance.

## What is uncertain

- The market page itself does not provide a direct forecast for the station; it only gives rules and current market odds.
- The page does not clarify how Wunderground rounding is implemented beyond saying the source measures to whole degrees Celsius.
- It does not prove what the realized high will be, only what will count.

## Why this source may matter

This is the governing contract surface. It determines the exact station, date window, source of truth, and whole-degree resolution mechanic.

## Possible impact on the question

This source sharply limits a common failure mode: using Seoul-city forecasts or Seoul/Kimpo airport forecasts as if they directly settle the contract. That could materially overstate the chance of 18°C or higher if Incheon airport is cooler.

## Reliability notes

- Good for contract interpretation and current implied odds.
- Not independent evidence on the weather outcome itself.
- Needs at least one strong contextual weather source and ideally one source tied more closely to the governing station or nearby coordinates.
