---
type: source_note
case_key: case-20260414-4c35c81d
dispatch_id: dispatch-case-20260414-4c35c81d-20260414T204205Z
analysis_date: 2026-04-14
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: al-qadisiyah-vs-al-shabab
question: Will Al Qadisiyah Saudi Club win on 2026-04-23?
driver: performance
date_created: 2026-04-14
source_name: ESPN Saudi Pro League fixtures and standings
source_type: secondary aggregator
source_url: https://www.espn.com/soccer/fixtures/_/league/ksa.1
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: orchestrator
related_entities: [saudi-arabia]
related_drivers: [performance]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260414-4c35c81d/researcher-analyses/2026-04-14/dispatch-case-20260414-4c35c81d-20260414T204205Z/personas/risk-manager.md]
tags: [sports, soccer, saudi-pro-league, fixture, standings]
---

# Summary

ESPN's 2025-26 Saudi Pro League standings page showed Al Qadsiah 4th and Al Shabab 12th as of 2026-04-14, while the fixtures page for the same date showed the match finishing 2-2 rather than as a Qadsiah win.

## Key facts extracted

- ESPN standings page listed Al Qadsiah with an 18-8-3 record, +36 goal difference, and 62 points; Al Shabab with a 7-10-11 record, -6 goal difference, and 31 points.
- ESPN fixtures page for Tuesday, April 14, 2026 showed: `Al Qadsiah 2 - 2 Al Shabab FT`.
- The fixture page location was Prince Mohammed Bin Fahd Stadium, Dammam, Saudi Arabia.

## Evidence directly stated by source

- Direct result evidence: full-time result was a draw, 2-2.
- Direct contextual evidence: league-table gap strongly favored Al Qadsiah pre-match on season quality.

## What is uncertain

- ESPN is an aggregator rather than the league's official competition site.
- The assignment prompt references 2026-04-23, while both ESPN and Polymarket page metadata point to a match already played on 2026-04-14.
- I did not rely on ESPN for official settlement rules; only for independent contextual confirmation and a scoreboard check.

## Why this source may matter

This source is useful because it independently supplies both the market-relevant contextual baseline (Qadsiah much stronger on standings) and the key disconfirming outcome (the favorite did not win).

## Possible impact on the question

If the contract truly asks whether Al Qadisiyah would win this matchup, ESPN's fixture result implies the answer is no because the match finished 2-2.

## Reliability notes

Reasonably reliable as a mainstream sports-data aggregator, but still secondary rather than governing. Good for contextual verification and useful as a cross-check against Polymarket metadata.