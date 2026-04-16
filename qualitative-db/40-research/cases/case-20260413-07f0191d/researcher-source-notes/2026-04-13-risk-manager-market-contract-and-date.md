---
type: source_note
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: bulgaria-election
entity:
topic: second-place finisher in 2026 Bulgarian parliamentary election
question: Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market page / contract text
source_type: market contract
source_url: https://polymarket.com/event/bulgarian-parliamentary-election-2nd-place
source_date: 2026-04-13
credibility: medium
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [risk-manager finding, risk-manager evidence map, risk-manager assumption note]
tags: [contract, resolution, source-of-truth, timing]
---

# Summary

This source is the governing market contract. It does not answer who will finish second, but it defines what counts, what does not count, tie-break logic, and the source-of-truth fallback.

## Key facts extracted

- Election date in the contract: 19 April 2026.
- Market resolves to the party or coalition with the second-greatest number of seats in the next Bulgarian National Assembly election.
- Primary ranking is by seats won.
- If tied on seats, the tie-breaker is total valid votes received.
- If still tied, alphabetical order of listed party abbreviations breaks the tie.
- If a named coalition dissolves, resolution is based on the seat total of the constituent party within that coalition that held the largest number of seats before the election.
- Resolution is based on consensus of credible reporting; if ambiguous, fallback is official Bulgarian government results from the Central Election Commission of Bulgaria (CIK).
- If results are not known definitively by 2026-10-31 11:59 PM ET, the market resolves to Other.

## Evidence directly stated by source

The contract directly states both the election date and the source-of-truth hierarchy. It also directly limits the resolution metric to parliamentary seats rather than vote share alone.

## What is uncertain

- The market page fetch did not expose a visible candidate list in the extracted text, so the exact set of named answer options was not independently recovered from the fetch output.
- The contract language implies the listed answer is GERB-UDF / GERB-SDS, but the precise naming on the market UI should ideally be cross-checked in a browser.

## Why this source may matter

This case is rule-sensitive. The contract matters because a coalition/party-label ambiguity or tie-break edge case could matter more than ordinary polling narratives.

## Possible impact on the question

The source makes clear that finishing second means second on seats after formal tie-breaks, not second in polls, media expectation, or informal coalition relevance.

## Reliability notes

Primary governing source for resolution mechanics. Reliability is high for contract interpretation, but incomplete for answer-option display because the extracted text omitted the market’s visible selections.