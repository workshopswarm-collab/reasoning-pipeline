---
type: source_note
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
analysis_date: 2026-04-15
persona: market-implied
domain: tech-ai
subdomain: prediction-markets
entity:
topic: polymarket-resolution-rules
question: Will claude-opus-4-6-thinking be the best AI model on April 17, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules context
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
tags: [polymarket, resolution-rules, primary-source, contract]
---

# Summary

The Polymarket market page states that resolution will use the Chatbot Arena LLM Leaderboard checked on April 17, 2026 at 12:00 PM ET, specifically the `Score` column under the `Text Arena | Overall` leaderboard tab with style control off. It also specifies alphabetical tiebreaking using the full model strings as listed in the market group.

## Key facts extracted

- Check time: April 17, 2026, 12:00 PM ET.
- Ranking source: Chatbot Arena LLM Leaderboard at `https://lmarena.ai/` / text leaderboard.
- Resolution field: `Score` column under `Text Arena | Overall`, style control off.
- Tiebreak rule: alphabetical order of full model names in the market group if arena scores are tied.
- Availability fallback: if the resolution source is unavailable at the check time, the market stays open until the leaderboard returns; if permanently unavailable, another source may be used.

## Evidence directly stated by source

- The contract is not about general model quality or broad public opinion; it is specifically about occupying first place on the named leaderboard at the precise check time.
- All material conditions must hold for a YES resolution: the listed model must rank first on that specific table at the check time, using the score column and stated tiebreak.

## What is uncertain

- The fetched page context summarizes the rules but does not expose the full market-group list in a structured way through readability extraction.
- Because fallback wording allows an alternate source only if the named source becomes permanently unavailable, there is some low-probability source-of-truth contingency risk.

## Why this source may matter

This source determines how the question resolves. It limits the relevant evidence to leaderboard rank at a specified time and reduces the importance of broader narratives about model quality unless they affect that leaderboard.

## Possible impact on the question

The rules increase confidence in a market-implied view only if the current leaderboard leader is correctly identified and likely to remain leader through the deadline. They also create a nontrivial tiebreak nuance: a tied score would not automatically favor `claude-opus-4-6-thinking` if another listed model sorts earlier alphabetically.

## Reliability notes

High reliability as the contract source. The main residual uncertainty is operational: source availability and whether a tie scenario becomes relevant near the resolution time.