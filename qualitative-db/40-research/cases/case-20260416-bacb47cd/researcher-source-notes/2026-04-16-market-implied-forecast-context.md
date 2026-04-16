---
type: source_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
analysis_date: 2026-04-16
persona: market-implied
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: highest-temperature-in-seoul-on-april-17-2026-18corhigher
question: Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher?
driver:
date_created: 2026-04-16
source_name: Open-Meteo forecast plus contextual public forecasts
source_type: forecast aggregation / contextual forecast
source_url: https://api.open-meteo.com/v1/forecast?latitude=37.5665&longitude=126.9780&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Asia%2FSeoul&forecast_days=3
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
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/market-implied.md
tags: [weather, forecast, threshold, contextual-source]
---

# Summary

Independent forecast context is close to the threshold but does not strongly support a 71% probability of 18°C+ at the settlement station.

## Key facts extracted

- Open-Meteo forecast for Seoul on `2026-04-17` gives a daily max of **17.0°C**.
- Timeanddate extended forecast for Seoul on `Fri Apr 17` lists **22 / 10°C** using Seoul / Gimpo context, which is warmer than Open-Meteo and above the contract threshold.
- Yr long-range table appears to show a next-day max near **20°C**, also above threshold, though the scraped output is less explicit and lower quality.
- Wunderground daily history page for `RKSI` is the final settlement surface, but as of the fetch it shows **no finalized Apr 17 daily observation yet**, which is expected because the day has not occurred / finalized.

## Evidence directly stated by source

- Open-Meteo directly returns a structured forecast with max temperature 17.0°C for Apr 17 at Seoul coordinates.
- Timeanddate directly shows Apr 17 forecast high 22°C for Seoul.
- Wunderground directly identifies RKSI as the relevant station surface, but no final Apr 17 history is available yet.

## What is uncertain

- These contextual forecasts are for Seoul-area locations/models, not necessarily identical to RKSI microclimate.
- Timeanddate and Yr are secondary forecast products, not the settlement source.
- Forecast disagreement around the threshold is material: one notable source prints 17°C while others are warmer.

## Why this source may matter

This is the main external check on whether the market is plausibly efficient. Forecasts cluster around the threshold rather than far above it, suggesting the market may be leaning on warmer-station assumptions, model dispersion, or local knowledge rather than overwhelming public consensus.

## Possible impact on the question

The contextual forecasts support a Yes-lean but with nontrivial threshold risk. They argue against an extremely bearish view, while also making 71% look somewhat rich rather than obviously cheap.

## Reliability notes

Useful for current context and directional calibration, but lower authority than the contract rules and lower relevance than the final RKSI Wunderground history that will settle the market.