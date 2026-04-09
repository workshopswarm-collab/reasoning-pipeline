---
type: evidence_map
case_key: case-20260406-5e3348e5
dispatch_id: dispatch-case-20260406-5e3348e5-20260406T175635Z
research_run_id: 77bfa70c-7514-40fa-83f1-9aff691acd70
analysis_date: 2026-04-06
persona: market-implied
domain: entertainment
subdomain: streaming
entity:
topic: xo-kitty-netflix-us-top10-week-2026-03-23
question: "Will \"XO, Kitty Season 3\" be the top US Netflix show this week?"
driver:
date_created: 2026-04-06
agent: orchestrator
related_entities: []
related_drivers: []
proposed_entities: ["xo-kitty", "netflix-top-10-us-tv-chart"]
proposed_drivers: ["chart-label-resolution-mapping"]
tags: ["evidence-map", "netflix", "resolution", "market-implied"]
---

# Evidence map

## Net assessment

The evidence set supports a high-confidence yes-leaning interpretation because the governing source-of-truth surface appears to already show the relevant US weekly window and its #1 show. The main nontrivial risk is not chart leadership but contract-label ambiguity: the market title says `XO, Kitty Season 3`, while the available Netflix weekly chart extraction shows a top-ranked `Season 2` entry.

## Direct evidence for the market price

1. **Netflix Tudum US TV Top 10 page**
   - Governing source named by the contract.
   - Visible selected week: `3/23/26 - 3/29/26`.
   - Visible page context: `United States | 3/23/26 - 3/29/26`.
   - Extracted ranking text indicates `Season 2` is `#1 in Shows`.
   - For a simple official-chart market, this is the strongest reason the market is at 95%.

2. **Contract timing mechanics match the page week**
   - Market description says the Tuesday April 7 update reflects the previous Monday-Sunday week.
   - Monday-Sunday immediately preceding April 7 is indeed March 23-March 29, 2026.
   - This reduces date-window uncertainty materially.

## Contextual evidence / interpretation

1. **Extreme market price as an information prior**
   - At 0.95, the market is probably assuming the official page already effectively settles the issue or that traders have verified the chart mapping manually.
   - Given this is a low-difficulty official-chart market, that assumption is plausible.

## Disconfirming evidence / residual risks

1. **Season-number mismatch in market title**
   - The contract asks about `XO, Kitty Season 3`.
   - The Netflix extraction points to `Season 2` at #1, not `Season 3`.
   - If the market title is interpreted literally and not as a franchise/clerical mismatch, this could matter.

2. **Lossy text extraction**
   - The fetched page does not cleanly preserve the title name adjacent to the `Season 2` label.
   - This is a real but limited verification weakness.

## Why the market may be efficient

The market likely recognizes that the official Netflix surface is the only thing that really matters here, and that once the correct week is visible, chart interpretation dominates over speculative alternative mechanisms. In other words, the market appears to be pricing the settlement mechanics, not trying to forecast demand from scratch.

## What would most change the evidence balance

- A cleaner official Netflix extract or screenshot showing a different #1 title for the same week.
- Rules guidance indicating the season-number wording is binding enough to override the apparent intended subject.
- Any official Netflix update changing the displayed week or top-ranked title before resolution.