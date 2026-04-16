---
type: source_note
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: politics
subdomain: elections
entity:
topic: Bulgarian 2026 parliamentary election timing and resolution source
question: Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: 2026 Bulgarian parliamentary election Wikipedia raw page + Polymarket market description
source_type: secondary plus market contract
source_url: https://en.wikipedia.org/w/index.php?title=2026_Bulgarian_parliamentary_election&action=raw
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-ac4c8995/researcher-analyses/2026-04-13/dispatch-case-20260413-ac4c8995-20260413T204806Z/personas/catalyst-hunter.md]
tags: [bulgaria, election-date, threshold, resolution]
---

# Summary

This note captures the timing and rule surfaces most directly relevant to the market: election date, threshold mechanics, and the market's governing source-of-truth language.

## Key facts extracted

- The Bulgarian parliamentary election is scheduled for **19 April 2026**.
- The National Assembly has **240 seats**.
- The electoral threshold is listed as **4% for parties or electoral coalitions**.
- The market resolves based on a **consensus of credible reporting**, with fallback to the **Central Election Commission of Bulgaria (CIK)** if ambiguity remains.
- The market has an `Other` condition only if results are not known definitively by **31 October 2026 11:59 PM ET**.

## Evidence directly stated by source

- Wikipedia raw page states the election date as 19 April 2026 and describes a 4% threshold in the electoral system section.
- Polymarket market description states that "Yes" resolves if the listed party wins at least one seat and names the Bulgarian CIK as the official fallback source of truth.

## What is uncertain

- Wikipedia is not itself an authoritative election source.
- Direct access to CIK pages was blocked by 403 during this run, so the CIK fallback was verified from market language rather than from live CIK content.
- This note does not independently confirm current polling.

## Why this source may matter

The market is date-sensitive and threshold-sensitive. Confirming the election date and the 4% threshold is necessary to frame the key catalyst: whether BSP–United Left remains safely above the line into election day.

## Possible impact on the question

If BSP–United Left is credibly above the threshold near election day, the path to at least one seat is straightforward under proportional representation. If it slips below the threshold, the contract flips to likely "No". This makes late polling, registration confirmation, and official reporting cadence the highest-value catalysts.

## Reliability notes

- Polymarket contract language is high-reliability for resolution mechanics.
- Wikipedia is only medium reliability, but acceptable as contextual support for election date and threshold when paired with the contract and other contextual sources.
- Direct CIK verification would be superior but was not technically accessible from this environment.