---
type: source_note
case_key: case-20260413-1fcb4925
dispatch_id: dispatch-case-20260413-1fcb4925-20260413T212655Z
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: Polymarket contract wording for Bulgaria parliamentary election winner market
question: Will Progressive Bulgaria (PB) win the most seats in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market page - Bulgaria Parliamentary Election Winner
source_type: market contract / resolution source
source_url: https://polymarket.com/event/bulgaria-parliamentary-election-winner
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
downstream_uses: [qualitative-db/40-research/cases/case-20260413-1fcb4925/researcher-analyses/2026-04-13/dispatch-case-20260413-1fcb4925-20260413T212655Z/personas/base-rate.md]
tags: [contract, source-of-truth, polymarket, elections, bulgaria]
---

# Summary

This source governs what counts for market resolution: election date, rank metric, tie-breakers, coalition-dissolution handling, reporting hierarchy, and the official fallback source of truth.

## Key facts extracted

- The election date in the contract is **19 April 2026**.
- The market resolves to the listed party or coalition that wins the **greatest number of seats** in the Bulgarian National Assembly.
- If results are not known definitively by **31 October 2026, 11:59 PM ET**, the market resolves to **Other**.
- Parties or coalitions are ranked primarily by **number of seats won**.
- If seat totals tie, the tiebreak is **valid votes**; if still tied, **alphabetical order of the listed abbreviation** is used.
- If a named coalition dissolves, resolution uses the **constituent party within that coalition with the largest number of seats before the election**.
- Resolution is based on a **consensus of credible reporting**, with fallback to the **Central Election Commission of Bulgaria (CIK)** if there is ambiguity.

## Evidence directly stated by source

- What counts is seat rank, not merely vote share.
- The primary governing official fallback source is the **Central Election Commission of Bulgaria (CIK)**.
- The market has explicit timing and tiebreak rules.

## What is uncertain

- The contract does not answer the empirical question of whether PB is actually likely to finish first.
- The coalition-dissolution clause matters only if coalition structure changes before the election or before settlement.

## Why this source may matter

This is the core source-of-truth surface for the question. Because the market is about exact first place on seats, not general momentum, any empirical view must be interpreted through these rules.

## Possible impact on the question

The contract narrows the relevant issue to whether PB finishes **first on seats**. A new coalition can be electorally important without being the modal first-place seat winner, so contract interpretation pushes against over-reading general salience.

## Reliability notes

This is the primary resolution-governing source for what counts. It is highly reliable for contract interpretation but not sufficient by itself to estimate probability.
