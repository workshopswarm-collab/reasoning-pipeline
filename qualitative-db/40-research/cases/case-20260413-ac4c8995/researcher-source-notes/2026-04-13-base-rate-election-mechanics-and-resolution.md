---
type: source_note
case_key: case-20260413-ac4c8995
dispatch_id: dispatch-case-20260413-ac4c8995-20260413T204806Z
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: elections
entity:
topic: Bulgarian parliamentary election 2026 resolution mechanics and seat threshold
question: Will United Left (BSP) win at least one seat in the 2026 Bulgarian parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Polymarket market description plus accessible public election context
source_type: market rule text plus contextual public reference
source_url: https://polymarket.com/event/bulgarian-parliamentary-election-which-parties-enter-parliament
source_date: 2026-04-13
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [elections]
upstream_inputs: []
downstream_uses: []
tags: [source-note, resolution, elections, bulgaria]
---

# Summary

This note captures the operative contract mechanics and accessible public election-structure context for the BSP/United Left seat market.

## Key facts extracted

- The market resolves Yes if the listed political party wins at least one seat in the next Bulgarian National Assembly as a result of the 19 April 2026 election.
- If results are not known definitively by 31 October 2026 11:59 PM ET, the market resolves Other.
- The market description says resolution is based on consensus of credible reporting, with fallback to official Bulgarian government results from the Central Election Commission of Bulgaria (CIK) if ambiguity remains.
- Accessible public election-context material indicates the Bulgarian parliamentary election is scheduled for 19 April 2026.
- Accessible public election-context material also states Bulgaria uses proportional representation with a 4% threshold for parties or coalitions to win seats in the National Assembly.

## Evidence directly stated by source

- Polymarket rule text directly states the market question, resolution deadline, primary reporting standard, and official fallback source of truth.
- Public contextual election summaries directly state the 19 April 2026 election date and 4% parliamentary threshold mechanics.

## What is uncertain

- I could not directly access CIK in this environment because the site returned Cloudflare challenge pages, so I did not independently pull the official Bulgarian election page here.
- Because of that, the authoritative source-of-truth layer is known from the market rules, but not directly re-opened from the official site during this run.

## Why this source may matter

- This market is date-sensitive and reporting-dependent, so the source-of-truth logic matters.
- For a seat-entry question, the 4% threshold is the core structural mechanism for a base-rate estimate.

## Possible impact on the question

- If BSP–United Left is clearly above 4%, base-rate odds of winning at least one seat are high.
- If it drifts near or below 4%, risk rises sharply because Bulgarian threshold rules can convert small vote-share changes into zero seats.

## Reliability notes

- The market rule text is authoritative for how this contract resolves.
- The election-structure context is useful but secondary; ideally it would be cross-checked against directly accessible official CIK material when possible.
- CIK remains the governing official fallback source even though it was not directly reachable from this environment during the run.
