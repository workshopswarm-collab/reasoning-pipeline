---
type: source_note
case_key: case-20260413-9c835dfe
dispatch_id: dispatch-case-20260413-9c835dfe-20260413T162509Z
analysis_date: 2026-04-13
persona: risk-manager
domain: crypto
subdomain: prediction-markets
entity: btc
topic: case-20260413-9c835dfe | risk-manager
question: Will MicroStrategy/Strategy announce a purchase of more than 1000 BTC between April 7 and April 13, 2026 ET?
driver: operational-risk
date_created: 2026-04-13
source_name: Polymarket market/rules page
source_type: market page
source_url: https://polymarket.com/event/microstrategy-announces-1000-btc-purchase-april-7-13
source_date: 2026-04-13
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: low
agent: orchestrator
related_entities: [btc]
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260413-9c835dfe/researcher-analyses/2026-04-13/dispatch-case-20260413-9c835dfe-20260413T162509Z/personas/risk-manager.md]
tags: [market-rules, resolution-criteria, polymarket]
---

# Summary

The Polymarket event page confirms the market is date-window and announcement-based rather than purchase-execution-based. That resolution framing is the main risk-management issue here: a purchase could have occurred outside the window, but the market only resolves on whether an official announcement of more than 1000 BTC happened between April 7 12:00 AM ET and April 13 11:59 PM ET.

## Key facts extracted

- The market page showed the market at effectively 100% Yes during this run.
- The market description states the market resolves to Yes if MicroStrategy announces a purchase of more Bitcoin than the threshold in the title within the stated dates.
- The rules state the market resolves based on announcements made within the designated time frame regardless of when the actual purchases were made.
- The governing source is official information from MicroStrategy or Michael Saylor.

## Evidence directly stated by source

- Resolution depends on an official announcement, not just inferred holdings changes.
- Timing and attribution matter directly.

## What is uncertain

- The fetched readable page did not expose a full independent transcript of the rules section beyond summary text.
- The current price shown via the page extraction rounded to 100% rather than the assignment's 0.96 snapshot, so the assignment snapshot is the better baseline for analysis.

## Why this source may matter

- It defines what counts and prevents a common error: treating off-window purchases or non-official commentary as sufficient.
- It highlights the main downside risk in an extreme-probability market: overconfidence from assuming routine MSTR/Strategy BTC accumulation automatically implies a qualifying in-window announcement.

## Possible impact on the question

- Strongly supports a Yes lean only if one trusts that an official company/Saylor announcement already exists or is imminent within the window.
- Leaves residual tail risk around timing, wording, or official-source ambiguity.

## Reliability notes

- Useful and necessary for contract interpretation.
- Not independent evidence of the underlying event itself.
- Best paired with an official company or Saylor source for the actual announcement question.
