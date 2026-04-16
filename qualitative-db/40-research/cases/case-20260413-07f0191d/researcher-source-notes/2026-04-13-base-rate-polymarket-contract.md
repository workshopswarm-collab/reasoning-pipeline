---
type: source_note
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: Polymarket contract wording for Bulgarian parliamentary election second-place market
question: Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market page - Bulgarian Parliamentary Election: 2nd Place
source_type: market contract / resolution source
source_url: https://polymarket.com/event/bulgarian-parliamentary-election-2nd-place
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-analyses/2026-04-13/dispatch-case-20260413-07f0191d-20260413T201947Z/personas/base-rate.md]
tags: [contract, source-of-truth, polymarket, elections]
---

# Summary

This source governs what counts for market resolution, including ranking logic, tie-breakers, treatment of coalition dissolution, and fallback to the Bulgarian Central Election Commission if consensus reporting is ambiguous.

## Key facts extracted

- The election date in the contract is 19 April 2026.
- The market resolves to the party or coalition that wins the second-greatest number of seats in the next Bulgarian National Assembly election.
- Parties are ranked primarily by seats won.
- If seats are tied, the tiebreak is higher valid vote total; if still tied, alphabetical order of the listed abbreviations.
- If a named coalition dissolves, resolution uses the seat total of the constituent party within that coalition that held the largest number of seats before the election.
- Resolution is based on a consensus of credible reporting, with fallback to official Bulgarian government reporting, specifically the Central Election Commission (CIK), if there is ambiguity.
- If results are not known definitively by 31 October 2026, 11:59 PM ET, the market resolves to Other.

## Evidence directly stated by source

- Ranking is by seats, not merely vote share.
- Ties are broken first by valid votes, then alphabetically.
- CIK is the governing fallback source of truth in case of ambiguity.

## What is uncertain

- The market page itself does not state current polling or who is most likely to win first or second.
- The coalition-dissolution clause could matter only if coalition structure changes before or around the election.

## Why this source may matter

This contract wording is essential because the question is about second place specifically, and because seat ranking can differ from simple vote-share impressions under Bulgaria's electoral system.

## Possible impact on the question

The contract narrows the relevant analysis to seat-based ranking. A party that looks likely to finish first should usually have low probability to finish exactly second absent evidence of a close three-way race or major late shock.

## Reliability notes

This is the primary resolution-governing source for what counts. It is highly reliable for contract interpretation but does not itself answer the empirical likelihood question.