---
type: source_note
case_key: case-20260416-f08c3dae
dispatch_id: dispatch-case-20260416-f08c3dae-20260416T041907Z
analysis_date: 2026-04-16
persona: base-rate
domain: sports
subdomain: soccer
entity:
topic: CD Tolima vs Deportivo Pereira market contract and resolution source
question: Will CD Tolima win on 2026-04-18?
driver:
date_created: 2026-04-16
source_name: Polymarket market page
source_type: market page / contract text
source_url: https://polymarket.com/event/col1-cdt-dep-2026-04-18
source_date: 2026-04-16
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: low
agent: orchestrator
related_entities: []
related_drivers: []
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260416-f08c3dae/researcher-analyses/2026-04-16/dispatch-case-20260416-f08c3dae-20260416T041907Z/personas/base-rate.md
tags: [polymarket, contract, source-of-truth, colombia-primera-a]
---

# Summary

This source establishes the exact market wording, settlement mechanics, and governing source-of-truth hierarchy.

## Key facts extracted

- Market asks whether **CD Tolima wins** the upcoming match scheduled for **April 18, 2026** versus Deportivo Pereira.
- If CD Tolima wins, the market resolves **Yes**; otherwise **No**.
- The market applies only to the result within **first 90 minutes plus stoppage time**.
- If the game is postponed, the market remains open until completed.
- If canceled entirely with no make-up game, the market resolves **No**.
- Primary resolution source is the **official statistics of the event as recognized by the governing body or event organizers**.
- If final match statistics are not published within 2 hours after conclusion, **consensus of credible reporting** may be used instead.

## Evidence directly stated by source

- Contract wording and fallback resolution rule are explicit on the market page.
- The page also showed market volume around **$27.43K** at fetch time.

## What is uncertain

- The market page does not itself specify which exact official competition or organizer feed will be used first in practice.
- It does not provide team-strength context, injury context, or pricing rationale.

## Why this source may matter

- It is the primary contract source for what counts.
- It resolves the biggest mechanical ambiguity: only regulation + stoppage time counts, not extra time or penalties.

## Possible impact on the question

- This source does not answer who is more likely to win, but it anchors the event definition and settlement logic.
- It also clarifies that for final verification, official match statistics are the governing source unless missing after two hours.

## Reliability notes

- High reliability for contract interpretation.
- Not independent evidence on team strength; it is a market-definition source rather than a forecasting source.
