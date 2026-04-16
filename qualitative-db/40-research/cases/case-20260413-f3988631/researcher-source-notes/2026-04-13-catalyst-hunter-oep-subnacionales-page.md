---
type: source_note
case_key: case-20260413-f3988631
dispatch_id: dispatch-case-20260413-f3988631-20260413T211840Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: politics
subdomain: bolivia-subnational-elections
entity: bolivia
topic: santa-cruz-governor-election-2026
question: Will Juan Pablo Velasco win the 2026 Santa Cruz gubernatorial election?
driver: elections
date_created: 2026-04-13
source_name: OEP Elecciones Subnacionales 2026 page
source_type: official electoral authority webpage
source_url: https://www.oep.org.bo/elecciones-subnacionales-2026/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [bolivia]
related_drivers: [elections, governance]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-f3988631/researcher-analyses/2026-04-13/dispatch-case-20260413-f3988631-20260413T211840Z/personas/catalyst-hunter.md]
tags: [source-note, official-source, bolivia, santa-cruz, elections]
---

# Summary

This official OEP page is the most important source-of-truth surface for the market because the contract explicitly names the Bolivian electoral authority as the fallback authority if reporting is ambiguous.

## Key facts extracted

- The OEP hosts a dedicated `Elecciones Subnacionales 2026` page.
- The page includes a `Ver Listas` section with downloadable lists of candidacies, including department-specific surfaces for Santa Cruz.
- The OEP front page currently references `RESOLUCIÓN TSE-RSP-ADM N° 0156/2026`, which explicitly mentions prohibitions governing the `segunda vuelta` of the 2026 subnational elections in Santa Cruz and other departments.
- That implies Santa Cruz is in a second-round phase and that the OEP is actively publishing election-administration materials tied to that phase.

## Evidence directly stated by source

- The OEP is actively publishing official 2026 subnational election materials.
- Santa Cruz is explicitly named in the referenced 2026 resolution about election-day prohibitions for the second round.
- Candidate-list and department-level materials exist on the official election page.

## What is uncertain

- The extracted text available through lightweight fetch did not cleanly expose the full Santa Cruz candidate list or vote reporting page.
- The fetched snippet does not by itself verify candidate names, only that Santa Cruz second-round and candidate-list surfaces exist.
- The page extraction is noisy enough that a full official results page URL could not be cleanly recovered from this pass.

## Why this source may matter

This is the governing source of truth for market resolution if media consensus is ambiguous. It also confirms the key timing/mechanism fact that Santa Cruz is in a second-round election process under active official administration.

## Possible impact on the question

The main impact is on resolution mechanics and catalyst timing, not on the horse-race margin directly. The most important catalyst remains official OEP reporting from the Santa Cruz second-round election process.

## Reliability notes

- Official source directly named in the market rules.
- High credibility for administrative timing, official lists, and official results.
- Limited by partial extraction quality in this environment, so best used alongside a contextual reporting source for horse-race interpretation.