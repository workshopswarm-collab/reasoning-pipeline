---
type: source_note
case_key: case-20260414-625be8a3
dispatch_id: dispatch-case-20260414-625be8a3-20260414T002740Z
analysis_date: 2026-04-14
persona: variant-view
domain: politics
subdomain: ballot-measures
entity:
topic: virginia-redistricting-referendum
question: Will the Virginia redistricting referendum pass?
driver: elections
date_created: 2026-04-13
source_name: Virginia Department of Elections — Proposed Amendment for April 2026 Special Election
source_type: official election authority page
source_url: https://www.elections.virginia.gov/election-law/proposed-amendment-for-april-2026-special-election/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [elections, legal]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260414-625be8a3/researcher-analyses/2026-04-14/dispatch-case-20260414-625be8a3-20260414T002740Z/personas/variant-view.md
  - qualitative-db/40-research/cases/case-20260414-625be8a3/researcher-analyses/2026-04-14/dispatch-case-20260414-625be8a3-20260414T002740Z/evidence/variant-view.md
tags: [official-source, ballot-question, source-of-truth-context]
---

# Summary

This official Virginia Department of Elections page is the primary source for the existence, scheduled timing, and wording of the April 21, 2026 special-election constitutional amendment. It does not itself prove passage likelihood, but it sharply reduces ambiguity about what the referendum is and confirms the event is officially scheduled despite the contract's note about pending legal challenges.

## Key facts extracted

- Virginia lists an "Explanation for Proposed Constitutional Amendment to Be Voted On at the April 21, 2026, Special Election."
- The ballot question asks whether the Constitution of Virginia should be amended to allow the General Assembly to temporarily adopt new congressional districts to "restore fairness in the upcoming elections," with normal process resuming after the 2030 census.
- The page confirms the referendum is framed as a statewide voter-facing constitutional amendment at a special election on April 21, 2026.

## Evidence directly stated by source

- The election authority page explicitly states the referendum date as April 21, 2026.
- The page explicitly provides the ballot question text and explanatory framing.
- The source is directly relevant to the market's fallback source-of-truth logic because Polymarket specifies the Virginia Department of Elections as the official source in case of ambiguity.

## What is uncertain

- The page does not provide polling, turnout expectations, campaign spending, or elite support/opposition balance.
- The page does not resolve the referenced legal challenges or indicate their probability of materially affecting the vote before November 3, 2026.
- The page does not provide actual results until after voting occurs.

## Why this source may matter

This is the governing administrative source confirming that the referendum is real, scheduled, and officially described in a way likely to influence voters. It is the cleanest authority for what counts and for timing verification.

## Possible impact on the question

This source supports a high baseline probability that the vote will occur and that a majority-approval standard will govern. It does not alone justify a very high pass probability, but it weakens the strongest mechanical bear case that the referendum might be fictive, misdescribed, or already off-calendar.

## Reliability notes

High reliability for scheduling, wording, and official election administration context. Low usefulness by itself for estimating voter approval probability beyond confirming the event and ballot language.