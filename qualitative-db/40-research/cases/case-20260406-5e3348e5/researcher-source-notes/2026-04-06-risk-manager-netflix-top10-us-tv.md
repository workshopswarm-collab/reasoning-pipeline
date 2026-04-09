---
type: source_note
case_key: case-20260406-5e3348e5
dispatch_id: dispatch-case-20260406-5e3348e5-20260406T175635Z
analysis_date: 2026-04-06
persona: risk-manager
domain: culture
subdomain: streaming
entity: netflix
topic: will-xo-kitty-season-3-be-the-top-us-netflix-show-this-week
question: Will "XO, Kitty Season 3" be the top US Netflix show this week?
driver: performance
date_created: 2026-04-06
source_name: Netflix Tudum Top 10 — United States TV
source_type: authoritative ranking page
source_url: https://www.netflix.com/tudum/top10/united-states/tv
source_date: 2026-04-06
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: risk-manager
related_entities: [netflix]
related_drivers: [performance]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260406-5e3348e5/researcher-analyses/2026-04-06/dispatch-case-20260406-5e3348e5-20260406T175635Z/personas/risk-manager.md]
tags: [netflix-top10, authoritative-source, us-tv-chart]
---

# Summary

Netflix's Tudum Top 10 page for United States TV is the governing source-of-truth surface named by the market description. On retrieval during this run, the current visible completed weekly ranking is for **3/23/26 - 3/29/26**, not yet the target week that would settle this market. The page shows the reporting window selector and current US TV ranking cards, with the #1 card visible and a separate embedded Tudum video/article reference confirming that **XO, Kitty Season 3** exists and is current Netflix editorial content.

## Key facts extracted

- The market description points to Netflix's Top 10 TV list on `top10.netflix.com`, which currently redirects to Netflix Tudum's Top 10 pages.
- The fetched United States TV page displays **3/23/26 - 3/29/26** as the current completed week at time of research.
- The visible ranking page shows a current #1 card for that prior week, meaning the decisive update for the market's target week has **not yet posted**.
- The page contains Netflix-controlled content referencing `xo-kitty` / `XO, Kitty Season 3`, which helps confirm the title is an active Netflix title rather than a malformed market label.

## Evidence directly stated by source

- The US TV Top 10 page exists and is the operative ranking surface.
- The current visible week is **3/23/26 - 3/29/26**.
- The market's relevant update is described as arriving Tuesday, April 7, 2026 at 3:00 PM ET for the previous Monday-Sunday window, so the current page is still one cycle early.

## What is uncertain

- The page fetch path available here does not expose a clean machine-readable table for the not-yet-published target week.
- The exact rank of XO, Kitty for **3/30/26 - 4/5/26** cannot be observed yet from this source during this run.
- The current extracted page text does not cleanly enumerate every ranking slot with titles in plain text, so manual HTML signals are used for verification rather than a pristine table dump.

## Why this source may matter

This is the authoritative source because the market description explicitly says resolution is based on which show the Netflix Top 10 update ranks #1 in the United States.

## Possible impact on the question

This source does not yet settle the market, but it strongly constrains the answer format: the correct decision should be based on the next Netflix-authored US TV Top 10 weekly update, not on third-party popularity chatter or partial daily app rankings.

## Reliability notes

High reliability for resolution mechanics and eventual settlement because this is the named Netflix-controlled source-of-truth surface. Lower utility for immediate prediction because the decisive week has not posted yet at research time.