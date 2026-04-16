---
type: assumption_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
research_run_id: d196eba0-72ee-4489-95b7-e90d4234fe00
analysis_date: 2026-04-16
persona: risk-manager
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: highest-temperature-in-seoul-on-april-17-2026
question: "Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher?"
driver:
date_created: 2026-04-16
agent: orchestrator
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-17 resolution window"
related_entities: []
related_drivers: []
proposed_entities: ["incheon-intl-airport-station-rksi"]
proposed_drivers: ["station-mapping-risk"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules-and-market.md", "qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-risk-manager-open-meteo-and-timeanddate-forecast.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/risk-manager.md"]
tags: ["assumption-note", "weather", "station-mapping", "threshold-risk"]
---

# Assumption

The core assumption is that the governing **Incheon Intl Airport Station** will run materially cooler than generic Seoul-city forecast surfaces, so the market's 18°C-or-higher pricing is overstating the chance of crossing the threshold.

## Why this assumption matters

The whole case turns on station mapping. If traders are anchoring on warmer Seoul forecasts rather than the governing airport station, then the market price can be too high even if city-level Seoul weather looks mild or warm.

## What this assumption supports

- A below-market probability estimate for `18°C or higher`.
- The conclusion that the biggest risk is mis-specified location, not a lack of upside tail weather paths.
- The view that the market may be embedding too much confidence for a one-day weather threshold with station ambiguity.

## Evidence or logic behind the assumption

- The market rules explicitly name Wunderground history for **Incheon Intl Airport Station** as the source of truth.
- Open-Meteo forecast at coordinates near Incheon airport is much cooler than Open-Meteo central Seoul.
- Timeanddate's warmer Seoul forecast further shows how a city-labeled weather page can diverge from the governing station outcome.

## What would falsify it

- A direct Wunderground forecast/history surface for RKSI showing a forecast max of 18°C or above for Apr 17.
- Another credible station-specific forecast near RKSI that clusters around or above 18°C.
- Evidence that the market is already clearly pricing the cooler airport station rather than generic Seoul city weather.

## Early warning signs

- Updated station-specific forecasts begin moving sharply warmer.
- Multiple independent weather surfaces converge on 18°C or above at Incheon airport.
- Synoptic changes increase sunshine or warm advection enough to narrow the Seoul-airport gap.

## What changes if this assumption fails

If the airport station is not meaningfully cooler than city-level Seoul forecasts, then my current below-market lean weakens and the fair probability should move closer to market, potentially above 60% depending on the station-specific evidence.

## Notes that depend on this assumption

- Main risk-manager finding for this dispatch.
- Evidence netting around station-mapping risk versus generic city-forecast anchoring.
