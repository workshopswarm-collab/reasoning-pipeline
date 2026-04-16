---
type: source_note
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: politics
subdomain: market-contract
entity:
topic: Polymarket Bulgaria parliamentary election winner contract
question: Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market page
source_type: market contract / resolution rules
source_url: https://polymarket.com/event/bulgaria-parliamentary-election-winner
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: catalyst-hunter
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-analyses/2026-04-13/dispatch-case-20260413-1fcb4925-20260413T212655Z/personas/catalyst-hunter.md]
tags: [contract, resolution, source-of-truth, polymarket]
---

# Summary

This is the governing contract language for what counts. It makes seat count, not coalition formation after the vote or broad narrative victory, the operative metric.

## Key facts extracted

- The election is scheduled for 19 April 2026.
- The market resolves to the listed party or coalition that wins the greatest number of seats in the National Assembly.
- If results are not known definitively by 31 October 2026, the market resolves to Other.
- In a tie on seats, valid votes break the tie; if still tied, alphabetical order of abbreviation/name breaks the tie.
- Resolution is based on consensus of credible reporting, but if there is ambiguity, the fallback source of truth is the official results reported by Bulgaria's Central Election Commission (CIK).

## Evidence directly stated by source

- Seat total is the only metric that counts for settlement.
- Official CIK results are the ultimate fallback if reporting consensus is ambiguous.
- Timing matters because the market closes before election day but resolves from post-election reporting.

## What is uncertain

- The contract does not define which media outlets count as a sufficient reporting consensus.
- The contract does not itself provide current polling or party strength.
- Official CIK pages were not directly accessible from this environment due Cloudflare blocking, so the CIK role is known from the contract text rather than direct page inspection in this run.

## Why this source may matter

This source narrows the analytical task. Arguments about who can form a government are secondary unless they correlate with seat plurality. It also means late poll or exit-poll catalysts matter because the market can reprice rapidly once credible reporting converges on seat leader.

## Possible impact on the question

The contract favors whichever bloc is most likely to top the seat table, not necessarily the bloc with the strongest coalition prospects. That distinction slightly weakens any thesis built mainly on Radev's broader popularity if district-level seat conversion still favors GERB–SDS.

## Reliability notes

Primary and authoritative for market interpretation. Not authoritative for the election result itself, but authoritative for how the market should be read.