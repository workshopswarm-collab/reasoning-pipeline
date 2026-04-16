---
type: source_note
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
analysis_date: 2026-04-14
persona: variant-view
domain: sports
subdomain: soccer
entity:
topic: al-qadisiyah-vs-al-shabab-market-rules
question: Will Al Qadisiyah Saudi Club win on 2026-04-23?
driver:
date_created: 2026-04-14
source_name: Polymarket market page
source_type: market-contract
source_url: https://polymarket.com/event/spl-qad-sha-2026-04-23
source_date: 2026-04-14
credibility: medium
recency: high
stance: neutral
certainty: medium
importance: high
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4c35c81d/researcher-analyses/2026-04-14/dispatch-case-20260414-4c35c81d-20260414T204205Z/personas/variant-view.md]
tags: [market-rules, source-of-truth, resolution]
---

# Summary

This source note captures the market wording and settlement mechanics from the Polymarket contract page for Al Qadisiyah vs Al Shabab.

## Key facts extracted

- Current market price supplied in assignment context is 0.83, implying roughly 83% for Al Qadisiyah to win.
- Market resolves Yes only if Al Qadisiyah wins.
- Any non-win outcome resolves No.
- Resolution is based on the outcome in the first 90 minutes plus stoppage time.
- If the match is postponed, the market stays open until completed.
- If the match is canceled entirely with no make-up game, the market resolves No.
- Primary resolution source is official statistics recognized by the governing body or event organizers; if final official match statistics are unavailable within two hours, consensus credible reporting may be used.

## Evidence directly stated by source

The market text directly states the win-only condition, the first-90-minutes scope, and the official-statistics-first settlement rule.

## What is uncertain

- The market page does not itself identify the exact operational governing source (for example SPL site, federation site, or another official competition feed).
- The page does not provide team-strength evidence, form evidence, or lineup evidence.

## Why this source may matter

This is the governing contract source for what counts as a win and what source should settle the market. It anchors both the probability comparison and the source-of-truth discussion.

## Possible impact on the question

It narrows the question to a regulation-time home win and removes ambiguity about extra time or penalties. That matters because high pre-match prices can be overstated if market participants are informally thinking in broader “advance / don’t lose” terms rather than strict regulation-time win.

## Reliability notes

Reliable for contract wording and settlement logic, but not for competitive form or team-news analysis. Independence is low because it is the market itself, not an external evidence source.