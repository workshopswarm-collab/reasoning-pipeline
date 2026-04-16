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
source_name: Open-Meteo forecast plus Timeanddate Seoul extended forecast
source_type: forecast_context
source_url: https://api.open-meteo.com/v1/forecast?latitude=37.4602&longitude=126.4407&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FSeoul&forecast_days=3 ; https://www.timeanddate.com/weather/south-korea/seoul/ext
source_date: 2026-04-16
credibility: medium
recency: current
stance: leans-no
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/risk-manager.md
tags: [source-note, weather, forecast, open-meteo, timeanddate]
---

# Summary

The strongest contextual weather evidence available in this run points to a cooler station outcome than the market price implies. Open-Meteo forecast data for coordinates near **Incheon Intl Airport** shows a **13.1°C** forecast high for 2026-04-17, while Open-Meteo for central Seoul shows **17.0°C**. Timeanddate shows **22°C** for Seoul, highlighting a large station-location spread and reinforcing that the contract's station mapping matters more than generic "Seoul" weather pages.

## Key facts extracted

- Open-Meteo forecast for approximately Incheon airport coordinates (`37.4602, 126.4407`) returned daily max temperature **13.1°C** for **2026-04-17**.
- The same API for central Seoul coordinates (`37.5665, 126.9780`) returned daily max temperature **17.0°C** for **2026-04-17**.
- Timeanddate extended forecast for Seoul showed **22 / 10°C** for **Fri Apr 17**.
- Timeanddate page notes its current-weather station is **Seoul / Kimp'O International Airport**, not the contract station.

## Evidence directly stated by source

- There is material geographic forecast dispersion between central Seoul and the governing Incheon airport area.
- The contract threshold of **18°C** is above the Open-Meteo central Seoul forecast and far above the Open-Meteo Incheon-airport forecast.
- Generic Seoul forecast pages can overstate the chance of the contract resolving Yes because they do not map cleanly to the governing station.

## What is uncertain

- Open-Meteo is not the named settlement source and may not match Wunderground exactly.
- Timeanddate is a city-level contextual forecast, not a governing-station forecast.
- The unusually wide gap between Seoul city forecasts and Incheon-airport forecast could reflect model differences, location effects, or data-surface limitations.

## Why this source may matter

This source set is useful precisely because it stress-tests the optimistic market thesis. It shows that the market label "Seoul" may invite traders to anchor on warmer city forecasts, while the governing station could be materially cooler.

## Possible impact on the question

If the Incheon airport area forecast is directionally right, the Yes side at 71% is too rich. Even if Open-Meteo is somewhat cool-biased here, the evidence suggests substantial risk that the true high finishes in the mid-to-high teens rather than 18°C or above.

## Reliability notes

- Open-Meteo is a strong contextual numerical source and directly available via API, but still secondary to the contract's Wunderground governing source.
- Timeanddate adds an independent contextual signal that "Seoul" can look much warmer than the governing station, though it is also secondary.
- The two sources are not fully independent in the deep meteorological sense because both depend on weather-modeling pipelines, but they are operationally distinct surfaces.
