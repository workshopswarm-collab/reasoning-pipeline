---
type: source_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: Independent forecast context for Incheon Intl Airport Station and Seoul
question: Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher once finalized on Wunderground?
driver:
date_created: 2026-04-16
source_name: Open-Meteo forecast API and MET Norway location forecast
source_type: forecast models / contextual forecast
source_url: https://api.open-meteo.com/v1/forecast?latitude=37.4943&longitude=126.4905&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=Asia%2FSeoul&forecast_days=3
source_date: 2026-04-16
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["weather", "forecast-model", "open-meteo", "metno", "incheon-airport"]
---

# Summary

Two contextual forecast sources pointed to a materially cooler outcome at the settlement location than the market implies. Open-Meteo forecast the Apr 17 high near **14.7°C** for Incheon airport coordinates and **17.0°C** for central Seoul. MET Norway hourly forecast for the same airport coordinates showed the warmest hour around **19.0°C**, which if rounded/truncated into the Wunderground whole-degree high framework keeps `18°C or higher` live but not dominant.

## Key facts extracted

- Open-Meteo for Incheon airport coordinates (37.4943, 126.4905) forecast Apr 17 max temperature **14.7°C** with low precip chance.
- Open-Meteo for central Seoul (37.5665, 126.9780) forecast Apr 17 max temperature **17.0°C**.
- The airport forecast is materially cooler than city-center Seoul, consistent with a coastal / airport moderation effect.
- MET Norway hourly forecast for Incheon airport coordinates reached about **18.9-19.0°C** during the warmest hours on Apr 17 local daytime, before cooling quickly.
- Timeanddate's Seoul city forecast showed **22°C** for Apr 17, again suggesting city forecasts can overstate the relevant settlement location.

## Evidence directly stated by source

- Open-Meteo directly outputs daily max forecast values for the requested coordinates.
- MET Norway directly outputs hourly temperatures, permitting a check of the forecast intraday peak.

## What is uncertain

- Model disagreement is meaningful: one contextual source is clearly below threshold while another briefly touches around 19°C.
- These are forecast/model surfaces, not the governing finalized Wunderground observations.
- It remains uncertain how Wunderground's displayed whole-degree daily max will map from any sub-hourly or hourly modeled path.

## Why this source may matter

This is the main independent contextual evidence set for probability estimation. It shows that the contract's use of Incheon airport rather than downtown Seoul is the key repricing driver and that forecast disagreement is centered near the 18°C threshold itself.

## Possible impact on the question

Because the station-specific contextual forecasts are mixed but skew cooler than the market, the fair probability for `18°C or higher` likely sits below 71%, though not near zero because at least one model briefly peaks around 19°C.

## Reliability notes

- Medium-high reliability as contextual evidence; these are legitimate forecast providers but not the settlement source.
- Independence is moderate rather than high because weather products may share upstream model inputs.
- Best use is directional/contextual calibration, not settlement proof.