---
type: assumption_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
research_run_id: 26d4af54-7883-4c21-9bbb-bc4335deca85
analysis_date: 2026-04-16
persona: market-implied
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: highest-temperature-in-seoul-on-april-17-2026-18corhigher
question: "Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher?"
driver:
date_created: 2026-04-16
agent: Orchestrator
status: active
certainty: medium
importance: high
time_horizon: "1 day"
related_entities: []
related_drivers: []
proposed_entities: ["Incheon Intl Airport Station (RKSI)"]
proposed_drivers: ["station microclimate vs city forecast divergence"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/market-implied.md"]
tags: ["weather", "assumption", "station-risk", "threshold"]
---

# Assumption

The market's 71% price is assuming RKSI / Incheon Intl Airport Station will realize a warmer outcome than the most conservative public forecast and finish on the 18°C side of a threshold-centered distribution.

## Why this assumption matters

If RKSI behaves cooler than broader Seoul city forecasts or if the distribution is truly centered at 17°C, then a 71% Yes price is too high. If RKSI is warmer or forecast dispersion is skewed upward, the market price is more defensible.

## What this assumption supports

- A Yes-lean above 50%
- Respect for the market as non-crazy despite one model showing 17°C
- A view that the market may be pricing local/station specifics or warmer forecast tails

## Evidence or logic behind the assumption

- Multiple public forecasts are near or above the threshold, not far below it.
- The adjacent bucket structure on Polymarket (`17°C` around 21%) implies traders see the threshold as close, not certain.
- One model at 17°C and at least one warmer public source is consistent with a distribution straddling the line.

## What would falsify it

- A direct RKSI-targeted forecast cluster clearly centered below 18°C.
- Updated forecast runs converging toward 16-17°C with no meaningful warmer tail.
- Same-day observed temperatures showing the station lagging badly behind needed warming.

## Early warning signs

- New forecast updates cut Apr 17 max temperatures by 1-2°C.
- Cloud/wind regime shifts that suppress daytime heating at the airport station.
- Market price starts sliding materially toward the 17°C bucket.

## What changes if this assumption fails

The fair probability should move closer to a coin flip or below, and the market would look overextended rather than roughly efficient.

## Notes that depend on this assumption

- The main market-implied finding for this run.