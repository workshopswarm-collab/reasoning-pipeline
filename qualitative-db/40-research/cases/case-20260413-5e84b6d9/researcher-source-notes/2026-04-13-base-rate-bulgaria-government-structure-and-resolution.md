---
type: source_note
case_key: case-20260413-5e84b6d9
dispatch_id: dispatch-case-20260413-5e84b6d9-20260413T210605Z
analysis_date: 2026-04-13
persona: base-rate
domain: politics
subdomain: bulgaria
entity:
topic: next prime minister of Bulgaria after the 2026 parliamentary election
question: Will Rumen Radev be the next prime minister of Bulgaria after the 2026 parliamentary election?
driver: elections
date_created: 2026-04-13
source_name: Government of Bulgaria / Council of Ministers site and market contract wording
source_type: primary_government_plus_contract
source_url: https://www.gov.bg/en
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers:
  - elections
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260413-5e84b6d9/researcher-analyses/2026-04-13/dispatch-case-20260413-5e84b6d9-20260413T210605Z/personas/base-rate.md
  - qualitative-db/40-research/cases/case-20260413-5e84b6d9/researcher-analyses/2026-04-13/dispatch-case-20260413-5e84b6d9-20260413T210605Z/evidence/base-rate.md
tags: [source-note, bulgaria, resolution, government]
---

# Summary

This source note records the governing source-of-truth surface and the main resolution mechanics relevant to the market.

## Key facts extracted

- The market contract says the market resolves to the next individual officially sworn in as Prime Minister of Bulgaria following the 19 April 2026 parliamentary election.
- Interim or caretaker prime ministers do not count.
- If no such prime minister is appointed by 31 March 2027 11:59 PM ET, the market resolves to Other.
- The primary resolution source is official information from the Government of Bulgaria, with consensus credible reporting as fallback.
- The Bulgarian government site is the natural official surface for sworn-in prime minister status.

## Evidence directly stated by source

- Official government information is designated as the primary resolution source by the contract.
- The Council of Ministers site is the official government surface.

## What is uncertain

- The exact page/path that will announce the eventual swearing-in was not identified during this run.
- The government English pages fetched cleanly, but not all subpages were easily discoverable through the fetch tool.

## Why this source may matter

This market is rule-sensitive and explicitly excludes caretaker prime ministers. That makes the official government source and the contract wording central to analysis.

## Possible impact on the question

The exclusion of caretaker prime ministers materially lowers the chance that a currently visible interim officeholder resolves the market. It also means any high probability on a named candidate must rest on a genuine post-election coalition/sworn-in path, not temporary incumbency.

## Reliability notes

High reliability on the source-of-truth issue because the market contract itself specifies the hierarchy and the government site is the official state surface. Lower reliability for broader political interpretation because this source does not on its own identify the most likely post-election coalition.