---
type: source_note
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
analysis_date: 2026-04-14
persona: variant-view
domain: sports
subdomain: football
entity:
topic: Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club draw market resolution framing
question: What is the governing source of truth and what exactly counts for resolution?
driver:
date_created: 2026-04-14
source_name: Polymarket market page for SPL Qad-Shab 2026-04-23
source_type: market contract / resolution text
source_url: https://polymarket.com/event/spl-qad-sha-2026-04-23
source_date: 2026-04-14
credibility: medium-high
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses: []
tags: [polymarket, resolution, source-of-truth, saudi-pro-league]
---

# Summary

This source note captures the governing market text and resolution logic. It matters because the market title in the assignment references a draw outcome, while the fetched Polymarket contract text says the market resolves YES if Al Qadisiyah wins and NO otherwise.

## Key facts extracted

- The fetched Polymarket page resolves **YES if Al Qadisiyah Saudi Club wins**.
- The page says **otherwise the market resolves NO**.
- It counts only **first 90 minutes of regular play plus stoppage time**.
- If the game is postponed, the market remains open until completion.
- If canceled entirely with no make-up game, the market resolves NO.
- The stated primary resolution source is the **official statistics of the event as recognized by the governing body or event organizers**.
- If no final official statistics are published within 2 hours after conclusion, a **consensus of credible reporting** may be used instead.

## Evidence directly stated by source

Directly fetched contract text from the market page:
- "If Al Qadisiyah Saudi Club wins, this market will resolve to \"Yes\". Otherwise, this market will resolve to \"No\"."
- "This market refers only to the outcome within the first 90 minutes of regular play plus stoppage time."
- "The primary resolution source for this market is the official statistics of the event as recognized by the governing body or event organizers."

## What is uncertain

- The assignment title says the market asks whether the match will **end in a draw**, but the fetched market page text appears to describe a **Qadisiyah win** contract instead.
- It is unclear whether this is a page-label mismatch, a market-routing issue on Polymarket sports pages, or an assignment-layer title mismatch.
- Because of that ambiguity, the operative source-of-truth for the *market question itself* is not perfectly clean from a single fetch.

## Why this source may matter

This is the only directly authoritative resolution text retrieved in the run. It defines what counts (90 minutes + stoppage time) and names the official statistics as the governing source of truth. It also creates the central ambiguity for this run, because the outcome described by the contract text does not match the assignment title.

## Possible impact on the question

This source lowers confidence in any aggressive variant thesis because there is contract-surface ambiguity before even reaching football analysis. It also implies the correct governing source of truth at settlement is official match statistics from the league/governing body, with credible reporting only as fallback.

## Reliability notes

- Strong for resolution mechanics if the fetched page corresponds to the intended market.
- Weaker than ideal for this case because the visible fetched text appears inconsistent with the assignment title, so there is source-of-truth ambiguity at the contract-surface level.
