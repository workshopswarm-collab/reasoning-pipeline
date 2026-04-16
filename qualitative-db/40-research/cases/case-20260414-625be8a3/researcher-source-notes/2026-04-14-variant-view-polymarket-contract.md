---
type: source_note
case_key: case-20260414-625be8a3
dispatch_id: dispatch-case-20260414-625be8a3-20260414T002740Z
analysis_date: 2026-04-14
persona: variant-view
domain: politics
subdomain: prediction-markets
entity:
topic: virginia-redistricting-referendum
question: Will the Virginia redistricting referendum pass?
driver: legal
date_created: 2026-04-13
source_name: Polymarket market rules — Will the Virginia redistricting referendum pass?
source_type: market contract
source_url: https://polymarket.com/event/will-the-virginia-redistricting-referendum-pass
source_date: 2026-04-13
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [legal, elections]
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260414-625be8a3/researcher-analyses/2026-04-14/dispatch-case-20260414-625be8a3-20260414T002740Z/personas/variant-view.md
  - qualitative-db/40-research/cases/case-20260414-625be8a3/researcher-analyses/2026-04-14/dispatch-case-20260414-625be8a3-20260414T002740Z/assumptions/variant-view.md
tags: [market-rules, resolution-mechanics, source-of-truth]
---

# Summary

The market contract is essential because this case is highly rule-sensitive. Passage by voter majority is not the only path-relevant condition. Timing, postponement, cancellation, and source-of-truth mechanics matter materially.

## Key facts extracted

- The market resolves Yes only if the proposed constitutional amendment is approved by a majority of valid votes cast in a statewide referendum by November 3, 2026 11:59 PM ET.
- If the referendum is postponed prior to that deadline, the market remains open and resolves based on the eventual vote.
- If the referendum is postponed after that deadline, or the vote does not take place by that deadline for any reason, the market resolves No.
- If the referendum is definitively cancelled with no opportunity to be rescheduled, the market resolves immediately No.
- The market resolves by consensus of credible reporting, with official Virginia Department of Elections results as sole fallback in ambiguity.

## Evidence directly stated by source

- The contract explicitly embeds both electoral-outcome risk and procedural/timing risk.
- The contract expressly references pending legal challenges, which keeps process risk live even if the referendum itself appears favored on substance.

## What is uncertain

- The contract does not quantify the size or seriousness of the legal challenges.
- The contract does not define what level of reporting disagreement would trigger fallback to official results, beyond general ambiguity.

## Why this source may matter

This source determines what counts. A pure "will voters approve the substance?" frame is incomplete because the market also carries scheduling and cancellation risk.

## Possible impact on the question

This source creates the main variant-view opening: even if the amendment would probably win if voted on, a 0.89 market price may still be too high if traders are underweighting procedural failure or delay-to-after-deadline risk.

## Reliability notes

Authoritative for market resolution mechanics, but not for real-world probability of substantive voter approval or legal developments.