---
type: source_note
case_key: case-20260406-5e3348e5
dispatch_id: dispatch-case-20260406-5e3348e5-20260406T175635Z
analysis_date: 2026-04-06
persona: base-rate
domain:
subdomain:
entity:
topic: case-20260406-5e3348e5 | base-rate
question: Will "XO, Kitty Season 3" be the top US Netflix show this week?
driver:
date_created: 2026-04-06
source_name: Netflix Tudum Top 10 - United States TV
source_type: authoritative chart / source-of-truth surface
source_url: https://top10.netflix.com/united-states/tv
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [netflix, top10, source-of-truth, us-tv]
---

# Summary

This is the governing source-of-truth surface named by the market description. The page resolves to Netflix Tudum's US TV Top 10 chart and currently displays the week `3/23/26 - 3/29/26`, which is the exact reporting window the market says will be published on Tuesday, April 7, 2026 at 3:00 PM ET.

## Key facts extracted

- The authoritative chart surface is `https://top10.netflix.com/united-states/tv` (redirecting to Netflix Tudum Top 10 US TV).
- The currently visible reporting window is `3/23/26 - 3/29/26`.
- The current #1 title shown on that page is `XO, Kitty Season 3`.
- The page also shows rank #2 as `New York: Season 2`, indicating the page is an ordered US TV chart rather than just a marketing tile.

## Evidence directly stated by source

- Netflix/Tudum lists `XO, Kitty Season 3` as `#1 in Shows` for United States for the week `3/23/26 - 3/29/26`.
- The page is the official Netflix Top 10 surface explicitly cited in the market rules.

## What is uncertain

- The market says the formal update is expected on Tuesday, April 7, 2026, 3:00 PM ET. On April 6 the page already shows the relevant weekly window, so there is a small operational risk that Netflix could still revise presentation or data before the scheduled update.
- The extracted text from the page is noisy, so later reviewers may want a quick manual browser check if disputing exact formatting; however the substance is legible.

## Why this source may matter

This is the source named in the market rules. If the page remains unchanged through the formal update, it should be decisive for resolution.

## Possible impact on the question

This source alone strongly supports a Yes resolution because it already shows `XO, Kitty Season 3` at #1 on the exact US TV reporting window that the contract references.

## Reliability notes

High reliability because it is the official Netflix Top 10 chart surface and matches the market's stated source of truth. The main residual risk is timing/refresh behavior before the scheduled April 7 update, not source credibility.