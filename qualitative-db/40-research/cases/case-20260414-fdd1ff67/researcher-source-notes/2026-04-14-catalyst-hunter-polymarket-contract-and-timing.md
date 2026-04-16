---
type: source_note
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
analysis_date: 2026-04-14
persona: catalyst-hunter
domain: sports
subdomain: soccer
entity:
topic: case-20260414-fdd1ff67 | catalyst-hunter
question: Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?
driver:
date_created: 2026-04-14
source_name: Polymarket event page / contract timing and resolution text
source_type: primary_market_contract
source_url: https://polymarket.com/sports/spl/spl-qad-sha-2026-04-23
source_date: 2026-04-14
credibility: medium-high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, timing, catalyst, source-of-truth, soccer]
---

# Summary

This source is primary for the market clock, current pricing context, and settlement mechanics. For a catalyst-hunter lane, the important takeaway is that there is no known major information release between now and kickoff embedded in the contract itself; the dominant catalyst is simply the match being played on 2026-04-23, with any repricing before then likely driven by team-news or independent odds movement rather than contract interpretation.

## Key facts extracted

- The market closes/resolves on 2026-04-23 around the scheduled match time.
- The current market-implied probability from the assignment context is 0.76.
- The market counts only first 90 minutes plus stoppage time.
- If the game is postponed, the market remains open until completion.
- If the game is canceled entirely with no make-up game, the market resolves No.
- The stated primary source of truth is official match statistics recognized by the governing body or event organizers, with credible reporting as fallback if final official statistics are unavailable within 2 hours.

## Evidence directly stated by source

- Timing of the match and market close.
- Resolution mechanics for regulation-time only.
- Source-of-truth hierarchy.

## What is uncertain

- One fetch of the Polymarket surface produced generic winner-market text inconsistent with the assignment title, so there is mild contract-surface ambiguity even though the assignment and embedded metadata identify this as a draw market.
- The market page itself does not provide the team-news or lineup catalysts that would justify a large pre-match repricing.

## Why this source may matter

This source identifies the only hard catalyst that is definitely scheduled: the match itself. It also clarifies that there is no extra-time/penalty ambiguity and that postponement extends the time window rather than immediately resolving the market.

## Possible impact on the question

The main repricing path before settlement is likely to run through ordinary pre-match catalysts such as injuries, suspensions, or lineups. If no such catalysts emerge, the market is mostly waiting for kickoff and the final official result.

## Reliability notes

Strong for timing and settlement mechanics. Weak for football-probability estimation by itself.