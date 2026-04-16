---
type: source_note
case_key: case-20260416-e5b42460
dispatch_id: dispatch-case-20260416-e5b42460-20260416T051736Z
analysis_date: 2026-04-16
persona: base-rate
domain: sports
subdomain: soccer
entity:
topic: Fenerbahçe vs Çaykur Rizespor market and fixture context
question: Will Fenerbahçe SK win on 2026-04-17?
driver: performance
date_created: 2026-04-16
source_name: Polymarket market page; Sofascore fixture page; Soccerway fixture page
source_type: mixed_primary_and_secondary
source_url: https://polymarket.com/event/tur-fen-riz-2026-04-17
source_date: 2026-04-16
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities:
  - turkey
related_drivers:
  - performance
upstream_inputs: []
downstream_uses: []
tags: [polymarket, super-lig, fixture, standings, source-note]
---

# Summary

This source note captures the main directly checked surfaces for this low-difficulty soccer match market: the market's own resolution rules and independent match-context pages confirming the fixture and league positions.

## Key facts extracted

- Polymarket states the market resolves Yes if Fenerbahçe wins the scheduled Süper Lig game on 2026-04-17, otherwise No.
- Polymarket explicitly limits the market to the first 90 minutes plus stoppage time; postponement keeps the market open until completed, while full cancellation with no make-up game resolves No.
- Polymarket says the primary resolution source is official statistics recognized by the governing body or event organizers, with credible reporting only as a fallback if official final match statistics are not published within 2 hours after the event.
- Sofascore lists Fenerbahçe vs Çaykur Rizespor for 17 Apr 2026 at 17:00 UTC in Istanbul, in the Trendyol Süper Lig.
- Sofascore lists Fenerbahçe 2nd and Çaykur Rizespor 8th at time of access.
- Soccerway independently lists the same fixture/match page for Fenerbahce v Rizespor on 17/04/2026.

## Evidence directly stated by source

- Direct resolution mechanics come from Polymarket's own market page.
- Direct fixture timing and competition context come from Sofascore and Soccerway match pages.
- Relative table position comes from Sofascore.

## What is uncertain

- No official club or league page was fetched successfully in this run, so fixture confirmation relies on two large secondary match-data sites rather than league/club primary pages.
- The fetched pages did not expose a clean bookmaker odds table or detailed recent-form splits through readable extraction.
- Team news, injuries, and lineups remain unverified here.

## Why this source may matter

The market is date-specific and resolution-sensitive, so the exact settlement language matters. For base-rate analysis, the main contextual value is that this is a normal league fixture with Fenerbahçe at home and materially higher in the table than Rizespor.

## Possible impact on the question

These sources support a prior that Fenerbahçe should be favored, but they do not by themselves justify an extreme probability above the low-to-mid 70s without stronger team-strength or lineup evidence. They also clarify that only regulation-time outcome counts, which slightly matters because a postponed match would not immediately settle and a cancellation without replay would resolve No.

## Reliability notes

- Polymarket is the primary source for market wording and resolution mechanics.
- Sofascore and Soccerway are useful contextual secondary sources with broad match coverage, but they are not the governing source of truth for settlement.
- Evidence independence is moderate: Sofascore and Soccerway are separate outlets, though both are downstream aggregators rather than official league publications.
