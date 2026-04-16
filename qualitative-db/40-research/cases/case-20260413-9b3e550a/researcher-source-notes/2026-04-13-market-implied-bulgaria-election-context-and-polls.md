---
type: source_note
case_key: case-20260413-9b3e550a
dispatch_id: dispatch-case-20260413-9b3e550a-20260413T191836Z
analysis_date: 2026-04-13
persona: market-implied
domain: politics
subdomain: elections
entity:
topic: bulgarian-parliamentary-election-third-place
question: Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Wikipedia 2026 Bulgarian parliamentary election page and Politico Poll of Polls Bulgaria page
source_type: contextual election reference / polling aggregation
source_url: https://en.wikipedia.org/wiki/2026_Bulgarian_parliamentary_election ; https://www.politico.eu/europe-poll-of-polls/bulgaria/
source_date: 2026-04-13
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [market-implied-finding]
tags: [bulgaria, polls, contextual-source, pp-db]
---

# Summary

These contextual sources indicate that PP–DB sits in a crowded cluster for second through fourth place rather than in a clearly dominant or clearly collapsing position. The strongest accessible polling context here places PP–DB around the mid-teens, close to Revival and DPS, while the current-seat baseline from the prior parliament has PP–DB above those rivals.

## Key facts extracted

- Wikipedia's 2026 Bulgarian parliamentary election page states that the next election is scheduled for **19 April 2026** and describes it as another snap election following government collapse and appointment of a caretaker cabinet in February 2026.
- The same page lists current parliamentary seat holdings from the prior assembly as approximately: **GERB–SDS 66, PP–DB 36, Revival 33, DPS 29**, placing PP–DB currently second by seats in the outgoing assembly.
- Politico Poll of Polls Bulgaria shows a recent aggregation with PP–DB around **14.5%**, close to **Revival ~14.0%** and **DPS ~14.7%**, with GERB ahead on **23.6%**.
- That Poll of Polls snapshot implies a very tight contest among the parties plausibly competing for **second and third**, rather than a settled expectation that PP–DB is the clear third-place finisher.

## Evidence directly stated by source

- Election date and snap-election context are directly stated by the Wikipedia page.
- Outgoing parliamentary seat counts are directly stated by the Wikipedia page.
- Politico directly displays a poll aggregation with PP–DB essentially in a statistical cluster with Revival and DPS.

## What is uncertain

- Wikipedia is not an authoritative election source and may contain errors.
- The Poll of Polls page shown here is not a full seat model and does not by itself determine who will rank third in seats under Bulgaria's proportional allocation system.
- Accessible fetches did not produce a clean primary CIK schedule/result page because the site blocked automated access in this environment.
- The coalition structure and party labels around DPS / APS splits could affect interpretation of who the named market options map to if party alignments shift again.

## Why this source may matter

This is the core contextual evidence for why a high market price on PP–DB finishing exactly third may be too confident. Publicly visible aggregation does not show PP–DB in an obvious third-place slot; instead it suggests a three-way cluster behind GERB, where PP–DB could still finish second or third depending on late movement and seat conversion.

## Possible impact on the question

If the accessible polling aggregate is roughly right, PP–DB being a plausible third-place finisher is real, but a **0.78 probability** looks high because the public evidence also leaves substantial room for PP–DB to finish second. The market may be pricing in additional tacit information or structural seat-conversion expectations, but the visible evidence alone does not strongly justify near-80% confidence.

## Reliability notes

- Useful as contextual, not authoritative, evidence.
- Independence is only moderate because both sources are public summaries rather than raw primary electoral data.
- Adequate for a medium-confidence directional memo when paired with the market contract and explicit acknowledgment of source limits.