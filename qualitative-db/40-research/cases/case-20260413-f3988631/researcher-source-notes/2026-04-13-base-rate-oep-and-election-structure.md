---
type: source_note
case_key: case-20260413-f3988631
dispatch_id: dispatch-case-20260413-f3988631-20260413T211840Z
analysis_date: 2026-04-13
persona: base-rate
domain: geopolitics
subdomain: elections
entity: bolivia
topic: case-20260413-f3988631 | base-rate
question: Will Juan Pablo Velasco win the 2026 Santa Cruz gubernatorial election?
driver: elections
date_created: 2026-04-13
source_name: Órgano Electoral Plurinacional (OEP/TSE) subnational elections 2026 pages
source_type: official election authority
source_url: https://www.oep.org.bo/elecciones-subnacionales-2026/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [bolivia]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-f3988631/researcher-analyses/2026-04-13/dispatch-case-20260413-f3988631-20260413T211840Z/personas/base-rate.md]
tags: [source-note, elections, bolivia, santa-cruz, official-source]
---

# Summary

Official OEP/TSE pages confirm that the 2026 Bolivian subnational election process is the governing source of truth for candidate eligibility and official results, and that Santa Cruz is part of the second-round election process.

## Key facts extracted

- The market rules point to the Bolivian electoral authority, Tribunal Supremo Electoral / OEP, as the official fallback source of truth if consensus reporting is ambiguous.
- The OEP subnational election page for 2026 links directly to Santa Cruz election materials and lists Santa Cruz among the departments covered by the 2026 subnational process.
- The OEP homepage on 2026-04-13 displayed a resolution covering prohibitions during the second round for subnational elections in several departments including Santa Cruz.
- The public OEP pages available through lightweight fetch are strong for process confirmation, but weak for clean candidate-level extraction in this environment.

## Evidence directly stated by source

- OEP homepage text references: "Elecciones Subnacionales 2026" and a resolution for the "segunda vuelta" including Santa Cruz.
- OEP election portal links Santa Cruz under the 2026 subnational election materials and links candidate habilitation/inhabilitation resources.

## What is uncertain

- The fetched OEP pages did not cleanly expose candidate-level Santa Cruz runoff names or vote shares through the available extractor.
- Because the exact candidate pair was not cleanly visible from OEP fetch output, candidate-level corroboration had to come from contextual secondary sources.

## Why this source may matter

This is the highest-quality source for resolution mechanics, official timing, and final fallback settlement logic.

## Possible impact on the question

It materially reduces uncertainty about what counts for settlement and confirms that a second-round Santa Cruz result should be the decisive official outcome if consensus reporting becomes messy.

## Reliability notes

High reliability for process and official result authority. Lower usability here for candidate-level detail because the extractor did not surface all structured content cleanly.