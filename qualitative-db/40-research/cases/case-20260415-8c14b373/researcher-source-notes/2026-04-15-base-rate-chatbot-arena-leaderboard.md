---
type: source_note
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
analysis_date: 2026-04-15
persona: base-rate
domain: tech-ai
subdomain: model-rankings
entity:
topic: chatbot-arena-text-overall-leaderboard
question: Will claude-opus-4-6-thinking be the best AI model on April 17, 2026?
driver: reliability
date_created: 2026-04-15
source_name: Arena AI / Chatbot Arena Text Arena Overall leaderboard
source_type: primary
source_url: https://arena.ai/leaderboard/text
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: medium
importance: high
novelty: high
agent: Orchestrator
related_entities: [anthropic, claude]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: []
tags: [chatbot-arena, leaderboard, primary-source, resolution-source]
---

# Summary

This is the governing source of truth named in the contract. A direct scrape of the page on 2026-04-15 showed `claude-opus-4-6-thinking` in first place on the Text Arena Overall leaderboard with score 1502±5, ahead of `gpt-5.4-high` at 1481±6 and `gemini-2.5-pro` at 1448±3.

## Key facts extracted

- The page header includes `Text Arena` and `Overall`, matching the contract's relevant tab and score column framing.
- `claude-opus-4-6-thinking` appeared as the top listed model in the captured HTML.
- Nearby extracted values in the same row were score `1502` with uncertainty `±5`.
- `gpt-5.4-high` appeared lower in the ranking with score `1481±6`.
- `gemini-2.5-pro` appeared lower still with score `1448±3`.
- The top-vs-nearest-rival gap visible in this pass was about 21 Elo points versus the named nearest market rival used here (`gpt-5.4-high`).

## Evidence directly stated by source

- The relevant leaderboard exists at `https://arena.ai/leaderboard/text`.
- The live ranking currently places `claude-opus-4-6-thinking` first in the captured page state.
- The source is the named resolution source in the market rules unless unavailable at check time.

## What is uncertain

- The page is dynamic and could change before the 2026-04-17 12:00 PM ET check time.
- This scrape confirms the current ordering, not the future snapshot at resolution time.
- The page extraction method is not a formal API, so there is some parsing fragility, though the model names and scores were visible in raw HTML.

## Why this source may matter

It is the explicit governing source of truth for market resolution. Current first-place status is the strongest direct evidence in favor of a YES interpretation for this outcome.

## Possible impact on the question

If the leaderboard remains materially similar through the check time, `claude-opus-4-6-thinking` resolves YES. The main residual risk is not current rank confusion but leaderboard movement, methodology/display changes, or source-availability complications before the check.

## Reliability notes

- Highest relevance because this is the contract-named resolution source.
- Moderate extraction fragility because the site is dynamic and the read was via HTML/page extraction rather than a dedicated API.
- Still strong enough for this case because model names and scores were directly visible in the raw page HTML and aligned with the leaderboard text page URL specified by the contract.
