---
type: source_note
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
analysis_date: 2026-04-13
persona: risk-manager
domain: sports
subdomain: hockey
entity: nhl
topic: los-angeles-kings-playoff-status
question: Will the Los Angeles Kings make the 2025-26 NHL Playoffs?
driver: reliability
date_created: 2026-04-13
source_name: NHL standings / official resolution source surface
source_type: official league standings
source_url: https://www.nhl.com/standings/2025-2026/wildcard
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities: [nhl]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-61dcf900/researcher-analyses/2026-04-13/dispatch-case-20260413-61dcf900-20260413T184628Z/personas/risk-manager.md]
tags: [source-note, nhl, standings, playoffs, official-source]
---

# Summary

The official NHL standings page is the governing source-of-truth surface for whether a team has clinched or been eliminated for this market. The fetch output was sparse in readability mode, but it confirms NHL.com as the authoritative official league surface and aligns with the contract language naming official NHL information as the resolution source.

## Key facts extracted

- NHL.com is the official website of the National Hockey League.
- The assigned market resolves based on whether the team qualifies under official NHL playoff rules.
- Official NHL information is explicitly named as the market's resolution source.

## Evidence directly stated by source

- The fetched page identifies NHL.com as the official NHL website.
- The page title is the NHL standings surface for the 2025-26 season wildcard view.

## What is uncertain

- The readability extraction did not preserve the standings table rows cleanly from NHL.com, so this source is stronger for source-of-truth authority than for conveniently extracted table detail in this run.

## Why this source may matter

This is the primary resolution authority. Even if contextual sources are easier to parse, the market is ultimately governed by official NHL qualification status.

## Possible impact on the question

If the Kings were marked clinched or eliminated on NHL official standings, that would dominate interpretation. In this run, the official source mainly anchors the source-of-truth logic, while ESPN provides cleaner extracted context.

## Reliability notes

Very high authority for settlement. Lower extraction convenience in this tooling pass. Best used as the governing source, with contextual verification from an independent standings page.