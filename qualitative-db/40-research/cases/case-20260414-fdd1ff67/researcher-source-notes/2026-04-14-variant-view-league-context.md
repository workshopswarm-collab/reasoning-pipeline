---
type: source_note
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
analysis_date: 2026-04-14
persona: variant-view
domain: sports
subdomain: football
entity:
topic: 2025-26 Saudi Pro League and club-context verification
question: Are Al Qadsiah and Al Shabab current Saudi Pro League participants, and what contextual source verifies the clubs involved?
driver:
date_created: 2026-04-14
source_name: Wikipedia pages for 2025-26 Saudi Pro League, Al Qadsiah FC, and Al Shabab Club
source_type: contextual encyclopedia / team and league pages
source_url: https://en.wikipedia.org/wiki/2025%E2%80%9326_Saudi_Pro_League
source_date: 2026-04-14
credibility: medium
recency: current-enough
stance: neutral
certainty: medium
importance: medium
novelty: low
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [wikipedia, league-context, team-context, saudi-pro-league]
---

# Summary

This source note preserves contextual verification that both Al Qadsiah and Al Shabab are current clubs in the 2025-26 Saudi Pro League ecosystem and that the fixture framing is plausible as a scheduled league match.

## Key facts extracted

- The 2025-26 Saudi Pro League page includes both **Al-Qadsiah** and **Al-Shabab** among league participants.
- Separate club pages exist for **Al Qadsiah FC** and **Al Shabab Club (Riyadh)**.
- The league page did not yield a clean fixture-level extraction for the exact April 23, 2026 match from simple fetch parsing during this run.

## Evidence directly stated by source

- The league season page visibly includes both clubs in the participant set.
- The club pages confirm the identities of the teams referenced by the market.

## What is uncertain

- This source does not directly settle the specific fixture date or current odds.
- The page fetch/parsing quality is limited, so it is contextual rather than dispositive.

## Why this source may matter

It provides an independent contextual check that the assignment refers to real current Saudi Pro League clubs rather than malformed entities, and it supports the conservative conclusion that this is an ordinary 90-minute football-outcome market rather than a rules-heavy special case.

## Possible impact on the question

This source does not materially move the probability by itself. Its main value is to support entity identification and reduce the chance of researching the wrong clubs or competition.

## Reliability notes

- Medium reliability as contextual support.
- Not authoritative for settlement or fixture-level odds.
- Appropriate as the key secondary/contextual source paired with the market contract text.
