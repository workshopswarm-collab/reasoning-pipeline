---
type: source_note
case_key: case-20260415-894d4fca
dispatch_id: dispatch-case-20260415-894d4fca-20260415T021731Z
analysis_date: 2026-04-15
persona: risk-manager
domain: politics
subdomain: surveillance-law
entity: united-states
topic: case-20260415-894d4fca | risk-manager
question: FISA Section 702 reauthorized before it expires?
driver: reliability
date_created: 2026-04-15
source_name: Polymarket market description and resolution criteria
source_type: primary_market_rule
source_url: https://polymarket.com/event/fisa-section-702-reauthorized-before-it-expires
source_date: 2026-04-15
credibility: high
recency: high
stance: neutral
certainty: high
importance: very-high
novelty: high
agent: Orchestrator
related_entities: [united-states]
related_drivers: [reliability, operational-risk]
upstream_inputs: []
downstream_uses: [qualitative-db/40-research/cases/case-20260415-894d4fca/researcher-analyses/2026-04-15/dispatch-case-20260415-894d4fca-20260415T021731Z/personas/risk-manager.md]
tags: [market-rules, source-of-truth, polymarket, fisa, section-702]
---

# Summary
This is the governing contract text available to the researcher. It explicitly states that qualifying legislation includes Public Law 118-49 and that the primary resolution sources are Congress.gov and other official U.S. government information, with credible consensus reporting as fallback.

## Key facts extracted
- The market resolves Yes if legislation reauthorizing FISA Title VII including Section 702 is passed by both chambers and signed into law by April 19, 2026 11:59 PM ET.
- Qualifying legislation includes Public Law 118-49.
- Joint resolutions can qualify if they satisfy the passage-and-becoming-law conditions.
- Primary resolution sources are Congress.gov / Library of Congress and other official U.S. government information.
- Consensus credible reporting is fallback, not primary.

## Evidence directly stated by source
- The market itself names Public Law 118-49 as qualifying legislation.
- The market gives an explicit deadline in Eastern Time and requires all material legislative conditions to hold.

## What is uncertain
- The contract text alone does not show whether the market creator intended this to mean the condition was already satisfied before current trading.
- The market text points to Congress.gov H.R. 22 as primary tracker, but direct fetch access to Congress.gov was blocked during this run, limiting independent confirmation from the official tracker.

## Why this source may matter
This is the highest-value source because the main risk-manager question is not generic legislative odds but the exact contract interpretation and whether previously enacted qualifying legislation already covers the event.

## Possible impact on the question
If Public Law 118-49 is indeed an enacted reauthorization of Section 702, then the market should be overwhelmingly Yes already, and the main downside is operational or interpretive error rather than congressional failure before April 2026.

## Reliability notes
Highest relevance and highest authority for contract interpretation short of direct official government confirmation of the referenced law. The remaining fragility is source-of-truth execution, not the wording itself.