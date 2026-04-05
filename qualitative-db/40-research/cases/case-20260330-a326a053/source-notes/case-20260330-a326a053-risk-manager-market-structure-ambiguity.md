---
type: source_note
domain: geopolitics
subdomain: prediction-market-structure
entity: polymarket-contract
topic: will-russia-capture-all-of-huliaipole-by-april-30
question: Will Russia capture all of Huliaipole by the market deadline under the stated ISW-map resolution rules?
driver: conflicts
date_created: 2026-03-30
source_name: market prompt / dispatch manifest
source_type: primary market metadata
source_url: local dispatch manifest and market description in assignment
source_date: 2026-03-30
credibility: high
recency: high
stance: neutral
certainty: high
importance: very-high
novelty: high
agent: risk-manager
related_entities: [russia, ukraine]
related_drivers: [conflicts]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260330-a326a053/analyses/2026-03-30/dispatch-case-20260330-a326a053-20260330T200831Z/assumptions/risk-manager.md, qualitative-db/40-research/cases/case-20260330-a326a053/analyses/2026-03-30/dispatch-case-20260330-a326a053-20260330T200831Z/evidence/risk-manager.md, qualitative-db/40-research/cases/case-20260330-a326a053/analyses/2026-03-30/dispatch-case-20260330-a326a053-20260330T200831Z/personas/risk-manager.md]
tags: [source-note, market/case-20260330-a326a053, agent/risk-manager, market-structure]
legacy_imported: true
legacy_original_path: qualitative-db/40-research/source-notes/by-market/case-20260330-a326a053-risk-manager-market-structure-ambiguity.md
legacy_original_note_kind: source
imported_by: legacy_40_research_backfill
import_batch: 20260405T225345Z
case_key: case-20260330-a326a053
---

# Summary
The market metadata is internally inconsistent. The title says “Will Russia capture all of Huliaipole by April 30?” but the embedded description repeatedly says resolution is by February 28, 2026, while dispatch metadata also shows close/resolve timestamps on March 30, 2026.

## Key facts extracted
- The market title references April 30.
- The description references February 28 multiple times as the resolution date.
- The dispatch metadata says closes_at and resolves_at are March 30, 2026.
- The contract also requires a very specific ISW map condition and persistence through the next full ISW update cycle.

## Evidence directly stated by source
- Title: “Will Russia capture all of Huliaipole by April 30?”
- Description: resolves YES if Russia captures the entirety of Huliaipole “by February 28, 2026, 11:59 PM ET.”
- Dispatch metadata: closes_at and resolves_at are both “2026-03-30T20:00:00-04:00.”
- The description says map shading must “persist through the next full ISW daily update cycle.”

## What is uncertain
- Which deadline is actually controlling for final market resolution: April 30, February 28, or an administratively updated interpretation.
- Whether traders are pricing battlefield probability, expected administrative correction, or some blend of both.
- Whether the persistence clause creates additional timing risk even if Russia briefly reaches qualifying shading.

## Why this source may matter
This is one of the most important risk-manager observations in the case. A high YES price may partly reflect assumptions about contract interpretation rather than pure battlefield likelihood.

## Possible impact on the question
This introduces material non-battlefield risk. Even a strong military thesis can fail if the market resolves against a different date or stricter map-persistence interpretation than traders assume.

## Reliability notes
Highest reliability available because this comes from the primary market wording/assignment itself, not downstream reporting. The ambiguity is real and should not be smoothed over.