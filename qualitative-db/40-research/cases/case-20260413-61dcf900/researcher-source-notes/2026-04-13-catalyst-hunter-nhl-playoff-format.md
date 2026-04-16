---
type: source_note
case_key: case-20260413-61dcf900
dispatch_id: dispatch-case-20260413-61dcf900-20260413T184628Z
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: sports
subdomain: hockey
entity: nhl
topic: playoff qualification rules
question: Will the Los Angeles Kings make the NHL Playoffs?
driver: reliability
date_created: 2026-04-13
source_name: NHL standings page playoff-format reference
source_type: official league rules/context
source_url: https://www.nhl.com/info/standings-info/playoff-format
source_date: 2026-04-13
credibility: high
recency: medium
stance: neutral
certainty: high
importance: high
novelty: low
agent: Orchestrator
related_entities:
  - nhl
related_drivers:
  - reliability
upstream_inputs: []
downstream_uses: []
tags:
  - source-note
  - nhl
  - playoff-format
---

# Summary

The NHL playoff format counts the top three teams in each division plus two wild cards in each conference. The Los Angeles Kings market resolves Yes if LAK qualifies for the postseason bracket under official NHL rules, including a wild-card berth.

## Key facts extracted

- Qualification is conference-based with division slots plus two wild cards.
- Wild-card qualification is explicitly relevant to this market.
- The official standings surface is the natural source-of-truth context because it links directly to playoff-format and tie-breaking procedure pages.

## Evidence directly stated by source

- The official playoff-format description defines what counts as making the playoffs.
- The standings page explicitly presents an "If Playoffs Started Today" structure tied to playoff qualification logic.

## What is uncertain

- This source is about rules structure, not live standings status.
- It does not itself settle whether LAK has clinched on 2026-04-13.

## Why this source may matter

The market is rule-sensitive at the margin because the Kings need not finish top three in the Pacific; a wild-card berth is sufficient. This source removes ambiguity about what counts.

## Possible impact on the question

It narrows the question to whether LAK finishes in one of the conference's eight playoff spots, not whether it wins a division slot.

## Reliability notes

High-quality official contextual source. It is authoritative on resolution mechanics but only contextual on current probability.