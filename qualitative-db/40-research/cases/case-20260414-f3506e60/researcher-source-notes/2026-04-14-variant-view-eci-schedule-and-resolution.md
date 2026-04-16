---
type: source_note
case_key: case-20260414-f3506e60
dispatch_id: dispatch-case-20260414-f3506e60-20260414T022039Z
analysis_date: 2026-04-14
persona: variant-view
domain: politics
subdomain: elections
entity: india
topic: tamil-nadu-assembly-election-2026
question: Will the Dravida Munnetra Kazhagam (DMK) win the most seats in the 2026 Tamil Nadu Legislative Assembly election?
driver: elections
date_created: 2026-04-14
source_name: Election schedule and market resolution text
source_type: primary-plus-contract
source_url: https://eci.gov.in
source_date: 2026-03-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [india]
related_drivers: [elections]
upstream_inputs: []
downstream_uses: []
tags: [source-note, eci, resolution, schedule]
---

# Summary
This note captures the governing resolution mechanics and election timing. The market resolves to the political party winning the greatest number of seats in the 2026 Tamil Nadu Legislative Assembly election, with fallback to statewide vote share and then alphabetical order only in the event of a tie for most seats. If consensus reporting is ambiguous, the Election Commission of India (ECI) is the governing official source, specifically the version with the greatest number of Assembly Constituencies covered.

## Key facts extracted
- The market description says the election is scheduled in March-May 2026 and resolves by seat count, not alliance control.
- The market names ECI as the official fallback source of truth if credible reporting is ambiguous.
- A contextual schedule source (Wikipedia summary citing ECI) states ECI announced the election schedule on 15 March 2026.
- That same schedule summary lists polling on 23 April 2026 and counting/results on 4 May 2026.
- The Tamil Nadu Assembly has 234 elected seats; 118 is a majority, but the contract asks only which party wins the most seats.

## Evidence directly stated by source
- Contract wording: resolution is based solely on the number of seats won by the named party in the Tamil Nadu Legislative Assembly.
- Contract wording: if multiple official reports differ, use the report including the greatest number of Assembly Constituencies.
- Schedule summary citing ECI: poll date 23 April 2026; count date 4 May 2026; completion deadline 6 May 2026.

## What is uncertain
- I did not retrieve the original ECI schedule PDF directly through the fetch tool; the precise schedule details are therefore cross-checked via a contextual summary rather than a direct PDF pull.
- The market can still be influenced by late alliance, candidate, or turnout developments before polling.

## Why this source may matter
This source defines what counts for resolution and confirms the event window, which matters because Tamil Nadu politics often centers on alliances while the contract settles at the party level.

## Possible impact on the question
It raises the importance of party-level seat efficiency versus alliance vote share. A coalition can perform well overall while still leaving DMK as the single largest party, which is directly favorable to a DMK YES interpretation.

## Reliability notes
Primary resolution wording is high quality because it comes from the market rules themselves. ECI is the stated official fallback source. The schedule details used here are strong but indirect because they came through a contextual summary citing ECI rather than a directly fetched ECI document.