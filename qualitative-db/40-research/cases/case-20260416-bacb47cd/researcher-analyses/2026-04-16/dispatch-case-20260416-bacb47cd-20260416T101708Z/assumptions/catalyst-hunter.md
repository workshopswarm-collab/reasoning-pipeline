---
type: assumption_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
research_run_id: 70e33f05-5b05-4a8b-a54b-94c67284f7cb
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: "Geographic mismatch between market title and governing station"
question: "Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher once finalized on Wunderground?"
driver:
date_created: 2026-04-16
agent: catalyst-hunter
status: active
certainty: medium
importance: high
time_horizon: "through 2026-04-17 settlement"
related_entities: ["polymarket"]
related_drivers: []
proposed_entities: ["incheon-intl-airport-station"]
proposed_drivers: ["airport-vs-city forecast divergence"]
upstream_inputs: []
downstream_uses: []
tags: ["weather", "assumption", "location-mismatch"]
---

# Assumption

The relevant forecast edge comes from treating **Incheon Intl Airport Station** as materially cooler than generic Seoul city forecasts, because that is the settlement location actually named in the contract rules.

## Why this assumption matters

If airport and city temperatures are effectively interchangeable, the market's 71% pricing for `18°C or higher` looks much more defensible. If they diverge meaningfully, then Seoul headline forecasts are a misleading catalyst and the market may be overpricing the warm bucket.

## What this assumption supports

- A below-market probability estimate for `18°C or higher`.
- The thesis that the most important near-term catalyst is not a new weather headline but whether station-specific forecast surfaces converge upward toward the threshold.
- The view that downtown-Seoul forecast summaries should be discounted unless they are reconciled to the airport station.

## Evidence or logic behind the assumption

- Polymarket rules explicitly settle on Wunderground data for Incheon Intl Airport Station rather than central Seoul.
- Open-Meteo showed a sizable gap between Incheon airport max forecast (14.7°C) and central Seoul max forecast (17.0°C).
- Timeanddate's Seoul city forecast was even warmer at 22°C, reinforcing that city-level weather pages can overstate the relevant station outcome.

## What would falsify it

- Station-specific forecast updates from independent providers converging clearly above 18°C.
- Evidence that the airport station historically tracks city highs tightly enough on this setup that the current divergence is noise.
- A Wunderground forecast surface for RKSI clearly indicating a finalized or near-final expectation at/above 18°C.

## Early warning signs

- Multiple station-specific forecast providers move upward together.
- Overnight / early-morning hourly forecasts increase instead of flatten.
- The market reprices higher after station-aware participants reconcile the geography issue.

## What changes if this assumption fails

My below-market stance weakens materially, and the fair probability would move closer to or above the market if airport-specific evidence starts supporting an 18°C print.

## Notes that depend on this assumption

- `qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/catalyst-hunter.md`
- `qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-catalyst-hunter-wunderground-polymarket-rules.md`
- `qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-catalyst-hunter-open-meteo-metno.md`