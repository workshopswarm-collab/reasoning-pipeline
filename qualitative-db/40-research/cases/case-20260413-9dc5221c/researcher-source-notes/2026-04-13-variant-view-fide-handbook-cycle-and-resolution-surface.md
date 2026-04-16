---
type: source_note
case_key: case-20260413-9dc5221c
dispatch_id: dispatch-case-20260413-9dc5221c-20260413T190728Z
analysis_date: 2026-04-13
persona: variant-view
domain: sports
subdomain: chess
entity:
topic: 2026 FIDE Candidates Tournament resolution and governing rules
question: Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?
driver: operational-risk
date_created: 2026-04-13
source_name: FIDE Handbook / World Championship cycle surface
source_type: primary
source_url: https://handbook.fide.com/chapter/worldchampcycle2026
source_date: 2026-04-13
credibility: high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [fide, rules, source-of-truth, candidates]
---

# Summary

This source note captures the primary governing surface for how the 2026 FIDE world championship cycle is documented by FIDE and why official FIDE information is the governing source of truth for the market.

## Key facts extracted

- The FIDE Handbook contains the governing competition framework for the world championship cycle.
- The Polymarket contract explicitly says the primary resolution source will be official information from FIDE, with consensus credible reporting as fallback.
- For this market, official FIDE competition information is therefore the key source-of-truth surface, even if easier-to-read standings pages come from secondary outlets.

## Evidence directly stated by source

- The handbook page is the official FIDE rules/documentation surface for the world championship cycle area.
- The market description directly points to official FIDE information as primary resolution source.

## What is uncertain

- The handbook fetch here exposed the handbook index rather than the full detailed regulations text, so this note is more useful for source-of-truth hierarchy than for detailed tiebreak parsing.
- Additional official event pages or FIDE announcements would be stronger for live standings than the handbook landing page alone.

## Why this source may matter

The market is extreme (~95%), so source-of-truth discipline matters. Even if secondary reporting says Sindarov is nearly home, the contract resolves on official FIDE information first.

## Possible impact on the question

This source does not itself settle whether Sindarov wins, but it lowers confidence in over-relying on media summaries and frames the right verification logic: check official FIDE first, then use credible independent reporting only as contextual or fallback evidence.

## Reliability notes

High credibility for governance/source-of-truth hierarchy; only medium usefulness for live-result details in this run because the extracted page was an index rather than a full live tournament page.
