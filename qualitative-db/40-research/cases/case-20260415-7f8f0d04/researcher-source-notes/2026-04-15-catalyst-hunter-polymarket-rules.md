---
type: source_note
case_key: case-20260415-7f8f0d04
dispatch_id: dispatch-case-20260415-7f8f0d04-20260415T104754Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: tech-ai
subdomain: model-benchmarks
entity:
topic: polymarket-resolution-rules
question: Will claude-opus-4-6-thinking be the top AI model on April 17, 2026 (Style Control On)?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market description
source_type: market-rule-page
source_url: https://polymarket.com/event/top-ai-model-on-april-17-style-control-on
source_date: 2026-04-15
credibility: high
recency: current
stance: neutral
certainty: high
importance: high
novelty: medium
agent: orchestrator
related_entities: []
related_drivers: [reliability]
upstream_inputs: []
downstream_uses: [catalyst-hunter.md, catalyst-hunter.md]
tags: [polymarket, rules, resolution, style-control-on, chatbot-arena]
---

# Summary

This source defines the governing resolution logic for the market. It says the winner is the model with the highest arena score under the "Text Arena | Overall" leaderboard with style control on at the April 17, 2026 12:00 PM ET check time, using alphabetical order as the tiebreaker if scores are tied.

## Key facts extracted

- Resolution checks the Chatbot Arena LLM Leaderboard under the "Leaderboard" tab on April 17, 2026 at 12:00 PM ET.
- The relevant metric is the "Score" column in the "Text Arena | Overall" leaderboard with style control on.
- The contract is multi-condition: the cited model must still be present, must be first by score at the check time, and must also survive any tie by alphabetical ordering of full model names as listed in the market group.
- If the resolution source is unavailable at check time, the market stays open until the first later check when the leaderboard becomes available again.
- If the source becomes permanently unavailable, another resolution source may be used.

## Evidence directly stated by source

- Exact check time and timezone are explicitly stated.
- Exact leaderboard tab and score column are explicitly stated.
- Tiebreaking rule is explicitly stated and is adverse to any "-thinking" suffix if tied with a base name that sorts earlier.

## What is uncertain

- The market page does not itself show the live leaderboard snapshot that will matter on April 17.
- It does not define what alternate resolution source would be used if Chatbot Arena becomes permanently unavailable.

## Why this source may matter

This is the governing source of truth for how the contract resolves, so it matters more than any narrative about which lab has momentum. It also introduces a nontrivial tie-risk for a "-thinking" labeled model because alphabetical order can break against it.

## Possible impact on the question

This source makes timing and exact naming materially important. A model can be broadly perceived as elite yet still fail to resolve YES if it is no longer first on the precise leaderboard/table at the check time or if it ties and loses the alphabetical tiebreak.

## Reliability notes

High reliability for contract interpretation because this is the market’s own rule text. It is not sufficient alone for the terminal answer because it does not establish the live April 17 leaderboard state.