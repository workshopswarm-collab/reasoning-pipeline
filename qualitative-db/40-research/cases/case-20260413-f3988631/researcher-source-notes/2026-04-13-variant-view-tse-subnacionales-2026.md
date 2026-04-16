---
type: source_note
case_key: case-20260413-f3988631
dispatch_id: dispatch-case-20260413-f3988631-20260413T211840Z
analysis_date: 2026-04-13
persona: variant-view
domain: geopolitics
subdomain: elections
entity: bolivia
topic: santa-cruz-governor-election-2026
question: Will Juan Pablo Velasco win the 2026 Santa Cruz gubernatorial election?
driver: reliability
date_created: 2026-04-13
source_name: Órgano Electoral Plurinacional (OEP/TSE) Elecciones Subnacionales 2026 hub
source_type: official electoral authority website
source_url: https://www.oep.org.bo/elecciones-subnacionales-2026/
source_date: 2026-04-13 accessed
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities:
  - bolivia
related_drivers:
  - reliability
  - operational-risk
upstream_inputs: []
downstream_uses: []
tags: [source-note, official-source, elections, bolivia, santa-cruz]
---

# Summary

This official TSE/OEP surface is the governing source-of-truth family for the market. It confirms the Subnacionales 2026 process is live, provides the election hub and departmental pages, and links to official candidate habilitation/inhabilitation lists.

## Key facts extracted

- The market’s named fallback authority, the Bolivian electoral authority / Tribunal Supremo Electoral (via OEP), is active and publishing the Subnacionales 2026 election materials.
- The OEP election hub links to Santa Cruz’s departmental election page and to consolidated candidate-list documents, including habilitated and inhabilitated candidacies.
- The OEP homepage surfaced a 2026 resolution referencing second-round prohibitions for Santa Cruz among other departments, indicating the electoral process is active and ongoing beyond the initial vote date.

## Evidence directly stated by source

- OEP Subnacionales 2026 hub exists and links to:
  - departmental election pages including Santa Cruz
  - "Lista de Candidaturas Habilitadas"
  - "Lista de Candidaturas Inhabilitadas"
- OEP homepage displayed: "RESOLUCIÓN TSE-RSP-ADM N° 0156/2026 ... segunda vuelta ... en los departamentos de ... Santa Cruz"

## What is uncertain

- The fetched text extractor did not cleanly parse the candidate PDF contents, so this note does not independently verify Velasco’s exact line item from the PDF.
- The hub confirms the authoritative surfaces and process state, but not by itself the current race balance or Velasco’s probability of winning.

## Why this source may matter

This is the explicit governing authority named in the market rules. For a date-sensitive, consensus-reporting-dependent market, confirming the source-of-truth and live election process matters as much as directional horse-race commentary.

## Possible impact on the question

- Supports confidence that the market should ultimately resolve off credible reporting with TSE/OEP official results as fallback.
- Also supports a modest variant caution: if traders are leaning heavily on media consensus without repeated cross-checks to the TSE/OEP process, they may be underpricing operational/timing ambiguity.

## Reliability notes

- Very high authority for resolution mechanics and official results.
- Lower utility for current win probability absent readable extracted candidate/result data from the linked documents.
- Independent from market chatter, but not an independent horse-race estimator.