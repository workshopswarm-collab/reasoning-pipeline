---
type: source_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
analysis_date: 2026-04-16
persona: variant-view
domain: weather
subdomain: airport-temperature-threshold
entity:
topic: Seoul / Incheon airport April 17 temperature threshold
question: Will the highest temperature recorded at Incheon Intl Airport Station be 18°C or higher on April 17, 2026?
driver:
date_created: 2026-04-16
source_name: Open-Meteo and MET Norway location forecast
source_type: forecast aggregation / weather model feed
source_url: https://api.open-meteo.com/v1/forecast?latitude=37.4602&longitude=126.4407&daily=temperature_2m_max&timezone=Asia%2FSeoul&forecast_days=3
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
tags: [weather, forecast, incheon, threshold-market]
---

# Summary

This source note captures the two main forecast checks used for the case: Open-Meteo daily max guidance for both Seoul and Incheon-airport coordinates, and MET Norway hourly forecast for the same locations.

## Key facts extracted

- Open-Meteo forecast for Seoul (37.5665, 126.9780) showed a daily maximum of **17.0°C** for 2026-04-17 local date.
- Open-Meteo forecast for Incheon-airport-like coordinates (37.4602, 126.4407) showed a daily maximum of **13.1°C** for 2026-04-17 local date.
- MET Norway compact forecast for Incheon-airport coordinates showed hourly temperatures on 2026-04-17 UTC reaching **18.9°C at 03:00Z**, which is **12:00 KST on Apr 17**.
- MET Norway compact forecast for Seoul coordinates showed hourly temperatures reaching **18.5°C at 03:00Z** on the same date.
- The market resolves specifically on **Weather Underground history for RKSI / Incheon Intl Airport Station**, not on downtown Seoul temperatures.

## Evidence directly stated by source

- Open-Meteo directly provides `daily.temperature_2m_max` values by local date and timezone.
- MET Norway directly provides hourly `air_temperature` forecast values for the queried coordinates.
- Weather Underground public HTML confirms the named resolution surface exists for `history/daily/kr/incheon/RKSI`, even though the final daily observed high is not yet available before the target date completes.

## What is uncertain

- Open-Meteo and MET Norway are model-based forecasts, not the final governing observation.
- Coordinate matching to the exact Weather Underground station is approximate, though the Incheon-airport coordinate query is close to RKSI.
- Weather Underground may round or process observed station temperatures differently from forecast model fields.

## Why this source may matter

The disagreement in forecast providers is material: one source family points comfortably below 18°C at airport-like coordinates, while another hourly model path briefly clears 18°C around local noon. That creates a real variant view against the market's 71% Yes pricing.

## Possible impact on the question

- Open-Meteo supports a **No-leaning** interpretation for the exact airport-linked resolution surface.
- MET Norway prevents overconfidence in No by showing a plausible path to a brief 18°C+ touch near midday.
- Together they support a sub-market but nontrivial Yes probability rather than an extreme call.

## Reliability notes

- Forecast recency is high because both pulls were made on 2026-04-16, one day before resolution.
- Independence is moderate rather than high because both are weather-model forecast products, though from different services.
- Neither source settles the contract directly; Weather Underground RKSI history remains the governing source of truth.
