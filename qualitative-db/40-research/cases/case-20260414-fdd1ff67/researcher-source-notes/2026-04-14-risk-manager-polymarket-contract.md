---
type: source_note
case_key: case-20260414-fdd1ff67
dispatch_id: dispatch-case-20260414-fdd1ff67-20260414T200433Z
analysis_date: 2026-04-14
persona: risk-manager
domain: sports
subdomain: soccer
entity:
topic: case-20260414-fdd1ff67 | risk-manager
question: Will Al Qadisiyah Saudi Club vs. Al Shabab Saudi Club end in a draw?
driver:
date_created: 2026-04-14
source_name: Polymarket market page / contract text
source_type: market_contract
source_url: https://polymarket.com/event/spl-qad-sha-2026-04-23
source_date: 2026-04-14
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
downstream_uses: []
tags: [polymarket, contract, source-of-truth, resolution]
---

# Summary

This source note captures the market contract and explicit resolution logic from Polymarket for the Al Qadisiyah vs Al Shabab Saudi Pro League match market.

## Key facts extracted

- Market concerns the upcoming Saudi Professional League game scheduled for April 23, 2026.
- The market resolves on the match outcome within the first 90 minutes plus stoppage time.
- If the game is postponed, the market stays open until completion.
- If canceled entirely with no make-up game, the market resolves No.
- Primary resolution source is official match statistics recognized by the governing body or event organizers.
- If final official match statistics are unavailable within 2 hours after conclusion, consensus of credible reporting may be used.

## Evidence directly stated by source

Directly stated on the market page:
- "This market refers only to the outcome within the first 90 minutes of regular play plus stoppage time."
- "The primary resolution source for this market is the official statistics of the event as recognized by the governing body or event organizers."
- Fallback to consensus of credible reporting if official final match statistics are not published within 2 hours.

## What is uncertain

- The page fetch available here exposed the general win-market contract wording, not a dedicated draw-market contract page, so care is needed not to overread the Yes/No wording itself.
- The specific governing body surface is not named explicitly on the page; likely league/organizer official match statistics, but the exact settlement surface still needs to be named at a higher level in the finding.

## Why this source may matter

This is the clearest available source for what counts for settlement: regular time only, postponement/cancellation handling, and primary-vs-fallback source hierarchy.

## Possible impact on the question

It sharply reduces contract ambiguity for the draw question. The main residual risk is not wording ambiguity but match-level uncertainty before kickoff and the need to avoid treating contextual odds pages as the settlement source.

## Reliability notes

High reliability for market mechanics because it is the market operator’s own contract text. Lower reliability for team/match evaluation because it does not by itself provide substantive form or strength evidence.