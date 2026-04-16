---
type: source_note
case_key: case-20260413-f3988631
dispatch_id: dispatch-case-20260413-f3988631-20260413T211840Z
analysis_date: 2026-04-13
persona: market-implied
domain: geopolitics
subdomain: bolivia-subnational-politics
entity: bolivia
topic: santa-cruz-governor-election-2026
question: Will Juan Pablo Velasco win the 2026 Santa Cruz gubernatorial election?
driver: reliability
date_created: 2026-04-13
source_name: OEP/TSE election authority pages and published resolution logic
source_type: official-election-authority
source_url: https://www.oep.org.bo/
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: market-implied
related_entities: [bolivia]
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: []
tags: [oep, tse, santa-cruz, runoff, source-of-truth]
---

# Summary

The Bolivian electoral authority (OEP/TSE) is the governing source of truth for this market if consensus reporting is ambiguous. OEP also shows election materials for the 2026 subnational elections and a resolution referring to second-round voting in Santa Cruz, confirming that a runoff process exists and is active.

## Key facts extracted

- The market contract explicitly names the Tribunal Supremo Electoral / OEP as the fallback official source of truth if consensus reporting is ambiguous.
- The OEP homepage on 2026-04-13 surfaced a resolution titled `TSE-RSP-ADM N° 0156/2026` referring to prohibitions during the second-round departmental election in Santa Cruz and other departments.
- This is consistent with a live second-round electoral process rather than a settled race.

## Evidence directly stated by source

- OEP is the official Bolivian electoral authority.
- A formal 2026 resolution exists specifically mentioning `segunda vuelta` and Santa Cruz.

## What is uncertain

- The fetched OEP election page was not very readable in this environment, so this note does not extract vote totals or candidate-level official runoff data directly from OEP.
- This source alone does not establish which candidate is ahead right now; it mainly establishes source-of-truth and confirms the runoff timing/process.

## Why this source may matter

This source is essential because the market is date-sensitive and resolves by consensus reporting with explicit fallback to OEP/TSE. Any market view must be anchored to that resolution logic.

## Possible impact on the question

This source increases confidence in the contract interpretation and timing window, but it does not by itself justify an 80% probability for Velasco. It mainly supports the view that the market is being asked about a real, imminent runoff governed by a clear official authority.

## Reliability notes

Official and authoritative for resolution mechanics. Limited here by fetch readability, so it is strongest on source-of-truth and timing, weaker on candidate standing without supplemental reporting.
