---
type: source_note
case_key: case-20260416-8fa68833
dispatch_id: dispatch-case-20260416-8fa68833-20260416T163913Z
analysis_date: 2026-04-16
persona: market-implied
domain: sports
subdomain: soccer
entity: barcelona
topic: case-20260416-8fa68833 | market-implied
question: Will FC Barcelona win on 2026-04-22?
date_created: 2026-04-16
source_name: Polymarket contract page
source_type: market contract / platform rules
source_url: https://polymarket.com/event/lal-bar-cel-2026-04-22
source_date: 2026-04-16
credibility: medium-high
recency: current
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: [barcelona]
related_drivers: []
upstream_inputs: []
downstream_uses: [market-implied finding, assumption note]
tags: [source-note, polymarket, contract, resolution]
---

# Summary

This source establishes both the current market-implied probability baseline (0.775 at assignment time) and the exact contract-resolution mechanics.

## Key facts extracted

- Current price supplied in assignment context is 0.775, implying a 77.5% Barcelona win probability.
- The market resolves Yes only if FC Barcelona wins the scheduled La Liga match on April 22, 2026.
- If Barcelona does not win, the market resolves No.
- Resolution is based only on the result within 90 minutes plus stoppage time.
- If the match is postponed, the market stays open until played.
- If canceled with no make-up game, the market resolves No.
- Primary source of truth is the official match statistics recognized by the governing body or event organizers; if those are unavailable within two hours, a consensus of credible reporting may be used.

## Evidence directly stated by source

The page text explicitly states the win/no-win framing, the first-90-minutes-only rule, and the primary resolution source.

## What is uncertain

- The contract page does not itself justify whether 77.5% is efficient; it only states the market baseline and rules.
- The governing body is not named explicitly on-page, so the practical source of truth is likely official La Liga / match organizer statistics, with credible reporting fallback.

## Why this source may matter

This is the governing contract surface. It defines what outcome counts and removes extra-time / penalties ambiguity.

## Possible impact on the question

It means the research should focus strictly on Barcelona's probability of winning in regulation, not advancing or avoiding defeat.

## Reliability notes

High relevance and authoritative for contract interpretation, but not independent evidence about team strength.
