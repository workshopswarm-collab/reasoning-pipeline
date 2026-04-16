---
type: assumption_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
research_run_id: b6946fa3-6d35-4298-b268-0379edeab30e
analysis_date: 2026-04-16
persona: variant-view
domain: weather
subdomain: airport-temperature-threshold
entity:
topic: "Airport-vs-city temperature gap matters more than city headline forecast"
question: "Will the highest temperature recorded at Incheon Intl Airport Station be 18°C or higher on April 17, 2026?"
driver:
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: 1d
related_entities: []
related_drivers: ["reliability"]
proposed_entities: ["Incheon Intl Airport Station RKSI", "Seoul"]
proposed_drivers: ["microclimate / airport-vs-city forecast divergence"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-variant-view-weather-sources.md"]
downstream_uses: []
tags: ["weather", "airport-station", "forecast-gap"]
---

# Assumption

The market is more likely to misprice this case by anchoring on headline Seoul warmth than on the colder airport-specific station path that actually governs settlement.

## Why this assumption matters

If airport-specific temperatures run several degrees cooler than central Seoul, then city-level intuition can overstate the probability of clearing an 18°C threshold at the governing station.

## What this assumption supports

- A below-market probability estimate.
- A variant view focused on location mismatch rather than broad regional weather direction.
- Skepticism toward a simple “Seoul should be warm enough” consensus narrative.

## Evidence or logic behind the assumption

- The contract resolves on Weather Underground history for RKSI / Incheon Intl Airport Station, not downtown Seoul.
- Open-Meteo shows a large gap between Seoul daily max (**17.0°C**) and airport-like coordinates (**13.1°C**) for the relevant date.
- Airports near the coast often run cooler than inland urban cores, especially if marine influence is present.

## What would falsify it

- Updated airport-specific forecast guidance clustering near or above 18°C.
- Observed intra-day warming at RKSI reaching 18°C despite cooler daily guidance.
- Evidence that current coordinate choice badly mismatches the station used by the contract.

## Early warning signs

- Multiple provider updates lift airport highs materially while Seoul stays warm.
- Hourly forecast paths show several midday readings above 18°C at airport coordinates.
- Weather Underground forecast surfaces for the station itself imply a higher ceiling than the off-platform models.

## What changes if this assumption fails

The variant view weakens sharply and the fair probability should move closer to or above the market because the main disagreement mechanism would be gone.

## Notes that depend on this assumption

- qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/variant-view.md
