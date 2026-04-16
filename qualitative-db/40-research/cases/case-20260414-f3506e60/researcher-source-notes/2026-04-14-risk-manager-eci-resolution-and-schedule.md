---
type: source_note
case_key: case-20260414-f3506e60
dispatch_id: dispatch-case-20260414-f3506e60-20260414T022039Z
analysis_date: 2026-04-14
persona: risk-manager
domain: politics
subdomain: elections
entity: india
topic: tamil-nadu-assembly-election-2026
question: Will the Dravida Munnetra Kazhagam (DMK) win the most seats in the 2026 Tamil Nadu Legislative Assembly election?
driver: elections
date_created: 2026-04-14
source_name: Election Commission of India and contract resolution text
source_type: primary-resolution-source
source_url: https://eci.gov.in
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [india]
related_drivers: [elections]
upstream_inputs: []
downstream_uses: [risk-manager-finding]
tags: [source-note, primary-source, resolution, timing]
---

# Summary
The market contract explicitly names the Election Commission of India (ECI) as the fallback official source of truth if consensus reporting is ambiguous, and specifies that the official report with the greatest number of Assembly Constituencies should control if official reports differ. Independent fetch attempts to ECI during this run were partially blocked (403 / connection refused), so the source-of-truth logic is clear from the contract even though direct retrieval of the current ECI page was not reliable from this environment.

## Key facts extracted
- Market resolves to the party that wins the greatest number of seats in the 2026 Tamil Nadu Legislative Assembly election.
- If credible reporting is ambiguous, fallback is official Indian government reporting, specifically ECI.
- If multiple official reports differ, the one with the greatest number of ACs controls.
- Market close/resolution timestamp in assignment is 2026-04-22 20:00 ET.
- Contextual schedule source used in this run says polling is 23 April 2026 and counting/results declaration is 4 May 2026, so the market appears designed to resolve before polling actually occurs and instead defer final settlement to later official/consensus reporting.

## Evidence directly stated by source
- The assignment/contract text directly states the resolution rule and fallback source.
- The assignment metadata directly states closes_at and resolves_at as 2026-04-22T20:00:00-04:00.

## What is uncertain
- Direct ECI webpage retrieval was blocked from this runtime, so I could not independently quote the schedule from the official site.
- If reporting is delayed or fragmented, there is some operational settlement risk until official counted-seat totals are stable.

## Why this source may matter
The case is date-sensitive and consensus-reporting-dependent. The governing source-of-truth and timing mechanics matter almost as much as the political fundamentals because a misread of poll/count dates or official-vs-media reporting hierarchy could cause analytical overconfidence.

## Possible impact on the question
This source mainly affects confidence calibration and settlement mechanics, not the directional political thesis. It supports treating ECI as the decisive official authority while also flagging that the market deadline precedes the apparent poll date, which raises timing/settlement process risk rather than directly changing which party is likeliest to win the most seats.

## Reliability notes
- Contract text is authoritative for market resolution.
- ECI is the authoritative election authority, but direct access issues during this run reduce direct-verification quality for the schedule itself.
- Because of that access friction, a secondary contextual source was needed to confirm the likely election timetable.