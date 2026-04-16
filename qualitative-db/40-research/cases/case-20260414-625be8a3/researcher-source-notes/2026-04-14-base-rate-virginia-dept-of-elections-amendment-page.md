---
type: source_note
case_key: case-20260414-625be8a3
dispatch_id: dispatch-case-20260414-625be8a3-20260414T002740Z
analysis_date: 2026-04-14
persona: base-rate
domain: politics
subdomain: ballot-measures
entity:
topic: virginia-redistricting-referendum
question: Will the Virginia redistricting referendum pass?
driver: elections
date_created: 2026-04-14
source_name: Virginia Department of Elections proposed amendment page
source_type: official election authority page
source_url: https://www.elections.virginia.gov/election-law/proposed-amendment-for-april-2026-special-election/
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: base-rate
related_entities: []
related_drivers: [elections, legal]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-625be8a3/researcher-analyses/2026-04-14/dispatch-case-20260414-625be8a3-20260414T002740Z/personas/base-rate.md]
tags: [official-source, resolution-source, virginia, referendum]
---

# Summary

The Virginia Department of Elections page is the contract's named fallback source of truth and confirms the referendum is scheduled for the April 21, 2026 special election, with legal challenges still relevant context.

## Key facts extracted

- The state has a dedicated Department of Elections page for the proposed amendment tied to the April 2026 special election.
- The market description itself points to this page as the relevant official reference for the amendment.
- The contract says ambiguity resolves solely by official referendum results reported by the Virginia Department of Elections.

## Evidence directly stated by source

- The page exists on the official Virginia Department of Elections domain and is specifically for the proposed amendment for the April 2026 special election.
- The official elections domain is the authoritative reporting surface named in the contract fallback logic.

## What is uncertain

- The fetched page content was sparse in the extraction tool, so the exact amendment text and any procedural detail are not fully visible in this note.
- This page alone does not prove passage odds; it mainly anchors existence, timing, and source-of-truth authority.
- Pending legal challenges remain a live condition in the market description and require contextual handling rather than being fully settled by this page snapshot.

## Why this source may matter

It is the governing authority for official reporting if public reporting becomes contested, and it confirms that the referendum is not purely hypothetical at this stage.

## Possible impact on the question

This source raises confidence that the referendum is officially scheduled and that, if the vote occurs, resolution should ultimately track Virginia election reporting rather than rumor or commentary.

## Reliability notes

High institutional credibility and directly named in the market rules. Weakness: the fetch extraction was thin, so this source is best used as an authoritative anchor combined with contextual reporting and a contract-reading pass.
