---
type: source_note
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
analysis_date: 2026-04-15
persona: base-rate
domain: prediction-markets
subdomain: contract-resolution
entity:
topic: polymarket-contract-rules
question: Will claude-opus-4-6-thinking be the best AI model on April 17, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market description and rules page
source_type: primary
source_url: https://polymarket.com/event/best-ai-model-on-april-17-style-control-off
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: Orchestrator
related_entities: []
related_drivers: [operational-risk, reliability]
upstream_inputs: []
downstream_uses: []
tags: [polymarket, contract, rules, resolution]
---

# Summary

This source defines the contract mechanics. The market resolves to whichever model has the highest arena score on the Chatbot Arena LLM Leaderboard under the `Text Arena | Overall` leaderboard with style control off when checked on April 17, 2026 at 12:00 PM ET. If scores tie, alphabetical order of model names as listed in the market group breaks the tie.

## Key facts extracted

- Resolution check time: April 17, 2026, 12:00 PM ET.
- Resolution source: Chatbot Arena / Arena AI leaderboard at `https://lmarena.ai/` / `https://lmarena.ai/leaderboard/text`.
- Relevant table slice: `Score` column under `Text Arena | Overall` with style control off.
- Primary ranking criterion: highest arena score at check time.
- Tiebreaker: alphabetical order of model names as listed in the market group, including suffixes such as `-thinking`.
- If the resolution source is unavailable at check time, the market stays open until the leaderboard becomes available again and resolves on the first later check.
- If the source becomes permanently unavailable, the market may resolve from another source.

## Evidence directly stated by source

- The market is not about subjective model quality in general; it is specifically about first place on one named leaderboard at one named time.
- All material conditions that must hold for YES are explicit: the model must be first under the specified score table at the check time, with tie handling as specified.

## What is uncertain

- The fallback path if the source becomes permanently unavailable is underspecified beyond `another resolution source`.
- The exact market group listing order for tie-breaking was not independently recovered from page structure in this pass, but the contract gives the governing rule.
- The current odds on the page excerpt were visible as roughly 90% for this outcome, while assignment metadata gave current price 0.931.

## Why this source may matter

This is the contract source that defines what counts. It narrows the question to a date-specific leaderboard snapshot and makes timing/source-availability operational risks relevant.

## Possible impact on the question

The contract mechanics make current first-place status highly relevant but not sufficient by itself. The path to failure is mainly leaderboard movement before the check or source-of-truth complications, not broader debates about overall model quality.

## Reliability notes

- High reliability for contract interpretation because this is the market operator's own rules page.
- It is authoritative for what counts, but not for predicting future leaderboard stability.
- Some source-of-truth ambiguity remains only in the unlikely fallback case where the named source is permanently unavailable.
