---
type: source_note
case_key: case-20260413-9b3e550a
dispatch_id: dispatch-case-20260413-9b3e550a-20260413T191836Z
analysis_date: 2026-04-13
persona: risk-manager
domain: politics
subdomain: elections
entity:
topic: PP-DB third-place contract interpretation
question: Will We Continue the Change – Democratic Bulgaria (PP–DB) finish third in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market page
authority_type: market contract
source_type: market rule / resolution page
source_url: https://polymarket.com/event/bulgarian-parliamentary-election-3rd-place
source_date: 2026-04-13
credibility: medium-high
recency: current
stance: neutral
certainty: medium-high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9b3e550a/researcher-analyses/2026-04-13/dispatch-case-20260413-9b3e550a-20260413T191836Z/personas/risk-manager.md]
tags: [source-note, polymarket, resolution, bulgaria, pp-db]
---

# Summary

This source establishes the market’s exact resolution logic. It says the market resolves to the party or coalition winning the third-greatest number of seats in the 19 April 2026 Bulgarian parliamentary election. If ambiguity remains, final fallback is the official results reported by Bulgaria’s Central Election Commission (CIK).

## Key facts extracted

- Election date in the contract text: 19 April 2026.
- Ranking is by seats won, not raw vote share, with valid-vote totals and then alphabetical abbreviation as tie-breakers.
- If a named coalition dissolves before the election, the market resolves based on the constituent party within that coalition that held the largest number of seats before the election.
- Primary settlement path is consensus of credible reporting; fallback source of truth is the Bulgarian government’s Central Election Commission (CIK).
- If results are not known definitively by 31 October 2026 11:59 PM ET, market resolves to Other.

## Evidence directly stated by source

Direct contract text supports that the core analytical question is not whether PP–DB performs well in votes generally, but whether it finishes exactly third on seats after tie-break logic. This sharply raises the importance of seat-conversion and party-order uncertainty near the cutoff.

## What is uncertain

- The market page itself does not provide the current polling/forecast ranking.
- The contract does not say which specific media outlets would count as the consensus layer before the CIK fallback.
- The dissolution clause creates some tail-interpretation risk if coalition structure changes before election day.

## Why this source may matter

This is the governing source-of-truth surface for what counts. It prevents overfitting to generic “PP–DB competitive” narratives when the actual resolution is a rank-order seat question with explicit fallback logic.

## Possible impact on the question

Because the contract is about exact third place by seats, any situation where PP–DB is clustered with Revival or DPS-like competitors should be treated as fragile rather than safely resolved by broad pro-European coalition reputation.

## Reliability notes

High relevance and near-authoritative for contract interpretation, but not itself an election forecast source. Best paired with a contextual source on current party ordering and election timing.