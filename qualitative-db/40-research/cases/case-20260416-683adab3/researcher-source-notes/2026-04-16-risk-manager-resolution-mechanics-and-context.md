---
type: source_note
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
analysis_date: 2026-04-16
persona: risk-manager
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity:
topic: lee-cronins-the-mummy-opening-weekend-box-office
question: Will "Lee Cronin's The Mummy" opening weekend box office be between 10m and 15m?
driver:
date_created: 2026-04-16
source_name: Contract text plus Box Office Mojo/The Numbers context check
source_type: mixed
source_url: https://polymarket.com/event/lee-cronins-the-mummy-opening-weekend-box-office
source_date: 2026-04-16
credibility: medium
recency: current
stance: neutral
certainty: medium
importance: high
novelty: medium
agent: Orchestrator
related_entities: [the-numbers]
related_drivers: []
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260416-683adab3/researcher-analyses/2026-04-16/dispatch-case-20260416-683adab3-20260416T160048Z/personas/risk-manager.md]
tags: [source-note, resolution-mechanics, contextual-source, contract]
---

# Summary

This note captures the rule-sensitive context around settlement and the limited independent contextual checks available pre-release.

## Key facts extracted

- Market text says settlement uses The Numbers `Box Office` tab value for the `3-day opening weekend (April 17 - April 19)` once the figure is final, not studio estimates.
- If the figure falls exactly on a bracket boundary, the market resolves to the higher range bracket.
- If finality is ambiguous, the market stays open until both The Numbers and Box Office Mojo confirm finalized figures.
- Box Office Mojo weekend page for `2026W16` currently shows `No data available`, which is consistent with the weekend not having occurred yet.
- Box Office Mojo title page fetch for the referenced IMDb title id produced a mismatched title surface and no usable release data, so it is not a reliable pre-release cross-check for this specific title in the current tool environment.
- Deadline tag-page context confirms Lee Cronin’s The Mummy exists as a Blumhouse/Atomic Monster/New Line project and that production reporting existed in 2025, but it did not yield clean pre-release box-office tracking data in this run.

## Evidence directly stated by source

- The market has multi-condition settlement mechanics: correct title mapping, correct weekend window, final not estimate, and possible cross-check with Box Office Mojo if finality is unclear.
- There is no direct public final weekend number yet.

## What is uncertain

- No clean independent pre-release tracking source was recovered in this run that would strongly anchor a 10m-15m estimate.
- Box Office Mojo title linkage appears noisy for this title id in current scraping conditions, so it cannot be treated as a dependable cross-check for the film identity here.
- Because the film has not opened yet, the core numerical question remains forecast-like rather than source-settled.

## Why this source may matter

The main risk in this market is overconfidence before the final The Numbers weekend figure posts. The settlement mechanics are explicit enough that premature reliance on estimates or a mislabeled third-party title page could create avoidable error.

## Possible impact on the question

This source pushes toward humility. The market may be directionally right, but the confidence embedded in a 0.70 price looks high relative to the thin directly observable evidence available before the weekend starts.

## Reliability notes

The contract language is authoritative for resolution mechanics. The contextual source quality for current pre-release tracking in this run is weaker than ideal, which should lower confidence rather than force a stronger claim.