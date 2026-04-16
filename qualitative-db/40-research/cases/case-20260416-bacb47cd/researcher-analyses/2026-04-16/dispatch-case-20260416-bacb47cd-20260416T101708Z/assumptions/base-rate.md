---
type: assumption_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
research_run_id: 0c338125-dc6d-434f-85e5-b84e0ad3c09d
analysis_date: 2026-04-16
persona: base-rate
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: seoul-apr-17-high-temperature-threshold
question: "Will the highest temperature in Seoul be 18°C or higher on April 17?"
driver:
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: medium
time_horizon: "1 day"
related_entities: []
related_drivers: []
proposed_entities: ["incheon-intl-airport-station-rksi"]
proposed_drivers: ["station-location-basis-risk"]
upstream_inputs: []
downstream_uses: []
tags: ["assumption", "weather", "station-basis-risk"]
---

# Assumption

The airport station used for settlement will track cool enough relative to Seoul proper that city-forecast highs above 18°C do not automatically imply an easy Yes.

## Why this assumption matters

The main risk in this case is basis mismatch between the market title's plain-language reference to Seoul and the contract's actual governing station at Incheon Intl Airport.

## What this assumption supports

- Holding the estimate below the 0.71 market price.
- Treating the case as a modest Yes lean rather than a near-lock.
- Giving real weight to the airport-area forecast excerpt that sits below the threshold.

## Evidence or logic behind the assumption

- The contract explicitly resolves on Incheon Intl Airport Station.
- Airport/coastal stations often run cooler than inland urban-core sites under spring conditions.
- The collected forecasts split in exactly that direction: Seoul-city pages were 20-22°C while the airport-area monthly page was about 16°C.

## What would falsify it

- A station-specific RKSI forecast or near-term update showing a likely high comfortably above 18°C.
- Late forecast convergence from multiple sources around the airport itself at 19-21°C.
- Early observed warming at RKSI on Apr 17 that already approaches the threshold.

## Early warning signs

- Forecast updates raising airport-area highs faster than city forecasts.
- Marine/cloud constraints weakening in late model cycles.
- Any direct RKSI-oriented forecast page moving from ~16°C toward 18-20°C.

## What changes if this assumption fails

The probability should move up materially, likely toward or above the current market price, because the main bearish base-rate friction would be gone.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/base-rate.md`
