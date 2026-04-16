---
type: evidence_map
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
status: draft
confidence: medium
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: []
proposed_entities: ["incheon-intl-airport-station-rksi"]
proposed_drivers: ["station-mapping-risk", "source-of-truth-location-basis"]
upstream_inputs: ["qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-risk-manager-polymarket-rules-and-market.md", "qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-source-notes/2026-04-16-risk-manager-open-meteo-and-timeanddate-forecast.md"]
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-bacb47cd/researcher-analyses/2026-04-16/dispatch-case-20260416-bacb47cd-20260416T101708Z/personas/risk-manager.md"]
tags: ["evidence-map", "weather", "threshold-market", "station-mapping"]
---

# Summary

This evidence map shows a market whose label encourages a warm Seoul-city interpretation, while the rules point to a cooler airport station. That mismatch is the main downside risk to the bullish 18°C-or-higher thesis.

## Question being evaluated

Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher?

## Current lean

Lean **No / below threshold** relative to market pricing, though not with extreme conviction because this remains a short-dated weather forecast.

## Prior / starting view

Starting baseline was the market-implied **71% Yes**, which looked high for a one-day threshold before station-specific verification.

## Evidence supporting the claim

- **Polymarket current price is 71% Yes**
  - Source: market page/rules note
  - Why it matters causally: the crowd may be incorporating recent forecast updates not captured elsewhere
  - Direct or indirect: indirect on outcome, direct on consensus
  - Weight: medium

- **Timeanddate Seoul forecast shows 22°C high for Apr 17**
  - Source: forecast note
  - Why it matters causally: suggests broader Seoul region could be warm enough that some traders see 18°C as comfortably reachable
  - Direct or indirect: indirect/contextual, because it is not the governing station
  - Weight: low-to-medium

## Evidence against the claim

- **Contract resolves on Incheon Intl Airport Station, not generic Seoul forecast pages**
  - Source: market rules note
  - Why it matters causally: wrong-location anchoring is a direct resolution-mechanic risk
  - Direct or indirect: direct on mechanism
  - Weight: high

- **Open-Meteo at Incheon-airport coordinates forecasts only 13.1°C for Apr 17**
  - Source: forecast note
  - Why it matters causally: this is the strongest available station-proximate forecast in the run and it sits far below threshold
  - Direct or indirect: contextual but geographically relevant
  - Weight: high

- **Open-Meteo central Seoul forecast is only 17.0°C, still below threshold**
  - Source: forecast note
  - Why it matters causally: even central Seoul forecast is not above 18°C in this source, reducing confidence in a Yes outcome
  - Direct or indirect: contextual
  - Weight: medium

## Ambiguous or mixed evidence

- The large gap between Timeanddate Seoul at 22°C and Open-Meteo central Seoul at 17°C is mixed evidence.
- It could mean one forecast provider is off, or simply that different forecast systems and station bases are producing very different outputs.
- That ambiguity raises uncertainty, but it does not clearly rescue the Yes case because neither source is the governing RKSI Wunderground final history surface.

## Conflict between inputs

- Main disagreement is **location-based and source-based**, not factual resolution conflict.
- The market label and some city-level forecast surfaces suggest warmth, while the contract's actual station mapping points to a potentially cooler site.
- Evidence needed to resolve this best: direct RKSI forecast/history signal on Wunderground or another high-quality station-specific surface near the airport.

## Key assumptions

- The Incheon airport station will be materially cooler than generic Seoul-city forecasts.
- Open-Meteo's station-proximate forecast is directionally informative even if not the governing source.
- The market may be over-anchoring to the city label rather than the exact station.

## Key uncertainties

- Exact Wunderground forecast signal for RKSI ahead of the event.
- Whether Open-Meteo is materially too cool for the airport site.
- How much intraday upside tail remains in a one-day spring temperature forecast.

## Disconfirming signals to watch

- Any direct RKSI/Wunderground forecast moving to 18°C or above.
- Additional station-specific models clustering near or above threshold.
- A late warm-shift forecast update with stronger site alignment.

## What would increase confidence

- A readable RKSI forecast or pre-event Wunderground station page for Apr 17.
- Another independent airport-proximate model agreeing with Open-Meteo's low-teens view.
- Historical evidence that Incheon airport commonly runs several degrees cooler than central Seoul under similar setups.

## Net update logic

The decisive update is not generic weather optimism or pessimism; it is the realization that the contract is governed by a specific airport station, while the public label says Seoul. That creates a meaningful risk that the market price is too confident because it is anchored on the wrong temperature surface.

## Suggested downstream use

- Forecast update
- Orchestrator synthesis input
- Source collection gap
