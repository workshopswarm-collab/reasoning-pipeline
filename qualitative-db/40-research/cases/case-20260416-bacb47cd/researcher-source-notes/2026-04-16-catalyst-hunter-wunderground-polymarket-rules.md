---
type: source_note
case_key: case-20260416-bacb47cd
dispatch_id: dispatch-case-20260416-bacb47cd-20260416T101708Z
analysis_date: 2026-04-16
persona: catalyst-hunter
domain: weather
subdomain: daily-temperature-threshold
entity:
topic: Incheon Intl Airport Station governing source and resolution mechanics
question: Will the highest temperature recorded at Incheon Intl Airport Station on 2026-04-17 be 18°C or higher once finalized on Wunderground?
driver:
date_created: 2026-04-16
source_name: Polymarket market page and referenced Wunderground history page
source_type: market rules + governing source page
source_url: https://polymarket.com/event/highest-temperature-in-seoul-on-april-17-2026
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: ["polymarket"]
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["weather", "resolution-source", "wunderground", "incheon-airport"]
---

# Summary

This source establishes the contract mechanics: despite the market title saying Seoul, the actual resolution source is the highest temperature recorded at **Incheon Intl Airport Station** on 2026-04-17, using Wunderground's daily history page once finalized and rounded/recorded in whole °C.

## Key facts extracted

- Market resolves to the temperature range containing the highest temperature recorded at Incheon Intl Airport Station on 17 Apr 2026.
- Governing source is Wunderground daily history for station `RKSI`: `https://www.wunderground.com/history/daily/kr/incheon/RKSI`.
- Market cannot resolve Yes until all data for that day is finalized.
- Resolution precision is whole degrees Celsius.
- Any later revisions after data is finalized do not count.
- Current market-implied probability on the `18°C or higher` bucket was about 71% / 72¢ at fetch time.
- At fetch time, the Wunderground history page for the future date did not provide finalized Apr 17 data; it only showed the station surface and no daily observations yet, so this is explicitly **not yet verified**, not evidence that the event cannot happen.

## Evidence directly stated by source

- The contract wording directly names Incheon Intl Airport Station and Wunderground as source of truth.
- The market page directly displays `18°C or higher` as the leading outcome around 71%.
- The Wunderground history page exists for station `RKSI`, but future-day finalized observations were not yet available at research time.

## What is uncertain

- Wunderground's displayed future history/forecast UX is messy and not itself a clean forecast artifact.
- The exact finalized whole-degree high for Apr 17 is unavailable before the day completes.
- The market title references Seoul while the rules settle on Incheon airport; that geographic mismatch matters for forecast interpretation.

## Why this source may matter

This is the governing resolution source, so it matters more than generic Seoul forecasts. It also forces the analysis to separate `not yet verified on Wunderground` from `not yet occurred`.

## Possible impact on the question

The source shifts focus from downtown Seoul forecasts toward the cooler airport/coastal station actually used for settlement. That lowers the plausibility of `18°C or higher` relative to city-center forecasts.

## Reliability notes

- High reliability for contract interpretation because this is the market's own rules page.
- Wunderground is authoritative here only because the market explicitly designates it as the settlement source.
- This source is not enough by itself to estimate probability; it needs contextual forecast evidence for the station/location.