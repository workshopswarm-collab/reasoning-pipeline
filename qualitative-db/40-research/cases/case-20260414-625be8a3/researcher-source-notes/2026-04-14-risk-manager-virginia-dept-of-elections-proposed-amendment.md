---
type: source_note
case_key: case-20260414-625be8a3
dispatch_id: dispatch-case-20260414-625be8a3-20260414T002740Z
analysis_date: 2026-04-14
persona: risk-manager
domain: politics
subdomain: ballot-measure
entity:
topic: virginia-redistricting-referendum
question: Will the Virginia redistricting referendum pass?
driver: elections
date_created: 2026-04-14
source_name: Virginia Department of Elections — Proposed Amendment for April 2026 Special Election
source_type: official_government_page
source_url: https://www.elections.virginia.gov/election-law/proposed-amendment-for-april-2026-special-election/
source_date: 2026-04-14
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [elections, legal]
upstream_inputs: []
downstream_uses: []
tags: [official-source, source-of-truth, ballot-language, resolution-relevant]
---

# Summary

This is the primary authoritative source for the existence, timing, and substance of the April 21, 2026 Virginia constitutional amendment vote referenced by the market.

## Key facts extracted

- The Virginia Department of Elections hosts an official page titled **"Proposed Amendment for April 2026 Special Election."**
- The page states the amendment is to be voted on at the **April 21, 2026 special election**.
- The ballot question asks whether the Virginia Constitution should be amended to allow the **General Assembly to temporarily adopt new congressional districts** to restore fairness in upcoming elections while the standard process resumes after the 2030 census.
- The page says the proposed district map has already been **approved by the General Assembly** and would take effect **only if the constitutional amendment is approved by voters**.
- The explanation says a yes vote would allow redraws because **other states have done so**, and a no vote would leave authority with the **Virginia Redistricting Commission** and leave current districts in place.
- The page further specifies the trigger condition: another state must redraw its own congressional districts before 2031 **without being ordered by a court to do so**.
- The page says the General Assembly's temporary power would continue until **October 31, 2030**, with the Virginia Redistricting Commission resuming responsibility in 2031.

## Evidence directly stated by source

Directly stated on the page:
- official scheduling of the vote for April 21, 2026
- exact ballot-question framing
- yes/no explanatory summaries
- operative trigger language tied to another state's non-court-ordered redraw
- statement that the proposed map has been approved by the General Assembly and is contingent on voter approval

## What is uncertain

- The page does not itself provide polling, campaign strength, turnout expectations, or forecast odds.
- The page is authoritative on the official election setup and ballot wording, but not on whether the amendment is likely to pass.
- The page does not resolve whether pending legal challenges could postpone or cancel the vote; it only confirms the scheduled election and measure content.

## Why this source may matter

This is the market's explicit fallback source of truth and the cleanest direct evidence that the referendum is real, date-specific, statewide, and tied to a clearly defined amendment text.

## Possible impact on the question

It raises confidence that the referendum currently exists as described, but it also highlights an underappreciated contract-risk feature: passage requires not just voter approval, but an actual statewide vote occurring by the contract deadline if any postponement or legal challenge emerges.

## Reliability notes

Official Virginia government election-law page. High credibility for ballot existence, date, and wording. Not sufficient by itself for passage probability because it is not evidence of voter intent or of legal stability.