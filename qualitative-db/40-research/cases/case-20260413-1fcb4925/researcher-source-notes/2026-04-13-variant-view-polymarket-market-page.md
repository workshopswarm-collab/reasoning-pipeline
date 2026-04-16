---
type: source_note
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
analysis_date: 2026-04-13
persona: variant-view
domain: prediction-markets
subdomain: contract
entity:
topic: Polymarket contract language for Bulgaria parliamentary election winner
question: Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market page
source_type: primary_market_contract
source_url: https://polymarket.com/event/bulgaria-parliamentary-election-winner
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: variant-view
related_entities: []
related_drivers:
  - elections
upstream_inputs: []
downstream_uses: []
tags:
  - contract
  - resolution
  - polymarket
---

# Summary

Primary contract source for what counts. The market resolves on which listed party or coalition wins the greatest number of seats in the National Assembly from the 19 April 2026 election, with a consensus-of-credible-reporting rule and an explicit official fallback to Bulgaria's Central Election Commission (CIK).

## Key facts extracted

- The contract asks which listed party or coalition wins the greatest number of seats.
- Tie-breaks are valid votes first, then alphabetical order of abbreviation/name if still tied.
- If a named coalition dissolves, resolution falls to the constituent party with the largest prior seat count.
- If ambiguity remains, the official results reported by the Bulgarian Central Election Commission are controlling.
- If results are not definitively known by 31 October 2026 11:59 PM ET, market resolves to Other.

## Evidence directly stated by source

- The governing source of truth is consensus of credible reporting, with official CIK fallback when ambiguous.
- Seat count matters, not raw vote share alone.
- The relevant election is the Bulgarian parliamentary election scheduled for 19 April 2026.

## What is uncertain

- The contract text alone does not tell us current polling or who is favored.
- "Consensus of credible reporting" can introduce short-run ambiguity before final official tabulation.

## Why this source may matter

This source defines the actual proposition. A variant view cannot just ask whether PB has momentum; it must ask whether PB is more likely than all other listed entities to finish with the most seats under the contract's seat-count logic.

## Possible impact on the question

Because seats, not just excitement or presidential alignment, decide the contract, a challenger like PB must plausibly outrun GERB and other blocs in final seat conversion. That is a higher bar than merely entering parliament strongly.

## Reliability notes

Highest relevance for resolution mechanics. Needs to be paired with election reporting and ballot/polling context to infer probability.