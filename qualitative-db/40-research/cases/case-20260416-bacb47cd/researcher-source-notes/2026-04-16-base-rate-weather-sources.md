---
type: source_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
analysis_date: 2026-04-16
persona: base-rate
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: seoul-apr-17-high-temperature-threshold
question: Will the highest temperature in Seoul be 18°C or higher on April 17?
driver:
date_created: 2026-04-16
source_name: Wunderground RKSI history page; Timeanddate Seoul extended forecast; Weather.com Seoul 10-day and Incheon airport monthly forecast
source_type: mixed-primary-and-contextual
source_url: https://www.wunderground.com/history/daily/kr/incheon/RKSI
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [weather, forecast, source-note, polymarket]
---

# Summary

This note captures the key forecast and resolution-source surfaces for a low-difficulty temperature-threshold market tied to Wunderground's RKSI daily history page.

## Key facts extracted

- The market resolves using the highest temperature recorded at **Incheon Intl Airport Station** on **17 Apr 2026**, not central Seoul city observations.
- The governing resolution page is Wunderground's RKSI daily history page, which on 2026-04-16 still showed **"No data recorded"** for the current day and therefore did not yet verify the Apr 17 outcome.
- Timeanddate's Seoul extended forecast listed **Fri Apr 17: 22 / 10 °C**.
- Weather.com's Seoul 10-day page listed **Fri 17: high around 20°C**.
- Weather.com's Incheon airport monthly page displayed **Apr 17: 60°F / 49°F**, implying roughly **16°C / 9°C** for the airport area, with Apr 16 showing no finalized high yet on that page excerpt.

## Evidence directly stated by source

- Wunderground RKSI page: source-of-truth surface exists and is station-specific; current-day page excerpt said "No data recorded," so the event is **not yet verified**, not resolved.
- Timeanddate Seoul forecast: Apr 17 expected high **22°C**.
- Weather.com Seoul forecast: Apr 17 expected high **20°C**.
- Weather.com Incheon-airport-area monthly forecast: Apr 17 expected high **60°F (~16°C)**.

## What is uncertain

- The market title says Seoul, but the contract resolves on **Incheon Intl Airport Station**; airport/coastal temperatures can run cooler than Seoul proper.
- Web extraction quality for consumer weather sites is uneven; some pages expose limited structured text.
- Forecast disagreement remains material because Seoul-city forecasts are above 18°C while the airport-area forecast excerpt is below.

## Why this source may matter

- Wunderground is the explicit governing source of truth, so capturing its role is mandatory even before the event occurs.
- The split between Seoul-city forecasts and airport-area forecasts is the main base-rate caution against blindly following the market title.

## Possible impact on the question

- If one anchored only on Seoul-city weather pages, Yes looks comfortably favored.
- If one respects the actual resolution station at Incheon airport, the threshold becomes closer to a coin flip or modest Yes rather than an obvious Yes.
- The source set therefore supports a tempered positive lean, not a high-confidence chase of the 0.71 market price.

## Reliability notes

- Wunderground is primary for settlement but not yet probative on the actual Apr 17 high because the date had not occurred / been finalized.
- Timeanddate and Weather.com are secondary/contextual forecast providers; they are reasonably useful but not independent in a strict meteorological-model sense.
- Independence is medium-low overall because consumer weather services may share overlapping NWP inputs, though the airport-vs-city distinction is still genuinely informative.
