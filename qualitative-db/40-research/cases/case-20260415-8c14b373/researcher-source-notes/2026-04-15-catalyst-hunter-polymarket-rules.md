---
type: source_note
case_key: case-20260415-8c14b373
dispatch_id: dispatch-case-20260415-8c14b373-20260415T130923Z
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: prediction-markets
subdomain: market-rules
entity:
topic: Polymarket contract wording and timing
question: Will claude-opus-4-6-thinking be the best AI model on April 17, 2026?
driver: operational-risk
date_created: 2026-04-15
source_name: Polymarket market page and rules summary
source_type: primary_contract_source
source_url: https://polymarket.com/event/best-ai-model-on-april-17-style-control-off
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: high
novelty: medium
agent: catalyst-hunter
related_entities: []
related_drivers: [operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-8c14b373/researcher-analyses/2026-04-15/dispatch-case-20260415-8c14b373-20260415T130923Z/personas/catalyst-hunter.md]
tags: [contract, rules, timing, source-of-truth]
---

# Summary

This note captures the relevant market mechanics: the market resolves to whichever model is first on the Chatbot Arena Text Arena Overall leaderboard with style control off when checked on April 17, 2026 at 12:00 PM ET, with alphabetical tie-breaking among listed market strings if arena scores tie.

## Key facts extracted

- Resolution uses the Chatbot Arena / Arena AI leaderboard page at `https://lmarena.ai/leaderboard/text`.
- The relevant tab is `Text Arena | Overall` with style control off.
- The check time is April 17, 2026, 12:00 PM ET.
- Primary ranking criterion is arena score.
- If arena scores tie, the listed market strings are broken alphabetically.
- If the source is unavailable at check time, the market remains open until the board comes back and then resolves on the first later check.
- If the resolution source becomes permanently unavailable, another source may be used.

## Evidence directly stated by source

- Resolution timing.
- Resolution source.
- Tie-break rule.
- Fallback behavior if the source is unavailable.

## What is uncertain

- The public FAQ-like readable extract does not reproduce the entire rules block verbatim, but it clearly points to the rules and current leading market outcome pricing.
- The fallback “another resolution source” clause creates some ambiguity only if the leaderboard becomes permanently unavailable.

## Why this source may matter

The market is narrow and timing-sensitive. The exact noon ET check matters because the outcome depends on the leaderboard state at a single future snapshot rather than an average over time. This creates a catalyst-sensitive market where even a late leaderboard update could flip the result.

## Possible impact on the question

The key analytic requirement is to ask whether `claude-opus-4-6-thinking` can become rank 1 by the Apr. 17 noon ET check, not whether it is generally elite or likely to be near the top eventually.

## Reliability notes

- High relevance because this is the governing contract source.
- High certainty on timing and source-of-truth interpretation from the market description provided and page extract.
- Some residual operational ambiguity exists only in the unlikely contingency that the leaderboard is unavailable at check time.