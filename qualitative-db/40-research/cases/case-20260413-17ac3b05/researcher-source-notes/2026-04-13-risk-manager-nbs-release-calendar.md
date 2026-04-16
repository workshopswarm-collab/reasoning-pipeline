---
type: source_note
case_key: case-20260413-17ac3b05
dispatch_id: dispatch-case-20260413-17ac3b05-20260413T185719Z
analysis_date: 2026-04-13
persona: risk-manager
domain: economics
subdomain: china-macro
entity: china
topic: q1-2026-gdp-resolution-mechanics
question: Will China GDP growth in Q1 2026 be between 5.0% and 5.5%?
driver: operational-risk
date_created: 2026-04-13
source_name: National Bureau of Statistics of China 2026 release calendar
source_type: official release calendar
source_url: https://www.stats.gov.cn/english/PressRelease/ReleaseCalendar/202512/t20251226_1962154.html
source_date: 2025-12-26
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [china]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [risk-manager.md, risk-manager.md]
tags: [source-note, official-source, settlement-mechanics, china-gdp]
---

# Summary

This official NBS release-calendar page is the governing timing/context source for the market’s settlement mechanics. It states that quarterly national economic performance releases occur in April and that release dates are preliminary and subject to adjustment.

## Key facts extracted

- NBS says annual and quarterly national economic performance will be released in January, April, July, and October respectively.
- The calendar explicitly says release dates are preliminary and subject to adjustment.
- NBS notes the national statistical database updates progress-tracking indicators about three working days after the release, implying the press release itself is the first authoritative public surface.

## Evidence directly stated by source

- “Annual and quarterly national economic performance will be released in January, April, July, and October, respectively.”
- “The release dates are preliminary and subject to adjustment.”
- Database updates lag the initial release by about three working days.

## What is uncertain

- The fetched excerpt does not show the exact April day in the readable extract, only the quarterly-in-April cadence and preliminary-status note.
- Whether the English page and Chinese page post simultaneously is not established here.

## Why this source may matter

This source anchors what counts as the expected official release window and supports the contract clause about falling back to the last available quarter if the specified quarter is not released by the next quarter’s scheduled release date.

## Possible impact on the question

It lowers settlement ambiguity somewhat by confirming the official source family and quarterly timing, but it also highlights operational/timing risk because release dates can move. That timing flexibility is a modest disconfirming consideration against overconfidence in any narrow contract interpretation.

## Reliability notes

Official primary source. Strong for release mechanics; weaker for the actual GDP number because it contains no forecast or reported Q1 value.