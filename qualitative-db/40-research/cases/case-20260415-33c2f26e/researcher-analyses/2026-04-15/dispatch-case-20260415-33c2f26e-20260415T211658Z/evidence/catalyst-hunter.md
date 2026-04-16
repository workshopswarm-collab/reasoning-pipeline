---
type: evidence_map
case_key: case-20260415-33c2f26e
dispatch_id: dispatch-case-20260415-33c2f26e-20260415T211658Z
research_run_id: e49fac67-b4e8-4d35-afb3-f3fea0bd5a51
analysis_date: 2026-04-15
persona: catalyst-hunter
domain: sports
subdomain: soccer
entity:
topic: catalyst and repricing map for Al Nassr vs Al Ettifaq
question: Will Al Nassr Saudi Club win on 2026-04-24?
driver:
date_created: 2026-04-15
agent: orchestrator
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: []
related_drivers: []
proposed_entities:
  - al-nassr-fc
  - al-ettifaq-fc
  - saudi-pro-league
proposed_drivers:
  - lineup-availability-shock
  - matchday-team-news
upstream_inputs: []
downstream_uses:
  - qualitative-db/40-research/cases/case-20260415-33c2f26e/researcher-analyses/2026-04-15/dispatch-case-20260415-33c2f26e-20260415T211658Z/personas/catalyst-hunter.md
tags: [evidence-map, catalyst, soccer, match-pricing]
---

# Summary

This evidence map nets a simple conclusion: the match itself is the governing event, and the only clearly material pre-match repricing catalyst identified in this pass is lineup / availability news.

## Question being evaluated

Will Al Nassr Saudi Club win its Saudi Pro League match against Al Ettifaq on 2026-04-24, within 90 minutes plus stoppage time?

## Current lean

Lean yes, with Al Nassr a strong favorite but not so overwhelming that lineup shocks are irrelevant.

## Prior / starting view

Starting baseline was the market price of 0.915, implying a very heavy favorite.

## Evidence supporting the claim

- Polymarket contract page defines a simple 90-minute win condition with low settlement ambiguity; this removes many rule-risk complications.
- Transfermarkt contextual snapshot suggests Al Nassr is top of the league while Al Ettifaq is materially lower in the table, supporting a strong baseline class gap.
- Al Nassr roster context indicates substantially higher-end attacking talent than Al Ettifaq's currently visible context pages.

## Evidence against the claim

- A 91.5% market price is already extreme for a single soccer match, so even a clearly stronger team still faces draw/upset risk.
- Exact pre-match lineups, injuries, suspensions, and rotation plans were not available in a clean authoritative source during this pass.
- Secondary contextual sources are not independent of the broader public soccer-information ecosystem and may not fully capture late changes.

## Ambiguous or mixed evidence

- The April 24 fixture page itself was not cleanly retrievable from common public score sites in this pass, which limits catalyst-specific granularity.
- Transfermarkt retrieval for Al Ettifaq was noisy on this tool stack, reducing confidence in exact comparative table and roster details unless separately cross-checked.

## Conflict between inputs

There was no substantive factual conflict about the basic setup. The main issue was source cleanliness and completeness rather than contradiction.

## Key assumptions

- No major Al Nassr lineup deterioration before kickoff.
- Match is played on schedule and settled under ordinary 90-minute rules.

## Key uncertainties

- Late injuries, suspensions, or deliberate rotation.
- Whether the market is slightly overconfident in a league-match favorite because of brand and roster prestige.

## Disconfirming signals to watch

- Official squad omissions for key Al Nassr attackers or midfield anchors.
- Sudden price weakness before kickoff without a clear public explanation.
- Credible reporting of travel, venue, or postponement disruption.

## What would increase confidence

- Official league fixture page with confirmed schedule and venue.
- Official club or league pre-match squad news.
- A clean independent stats source confirming the comparative league positions and recent performance.

## Net update logic

The evidence did not justify a large move away from the market. It did justify a slight discount from 91.5% because the available support is more contextual than directly fixture-specific, and soccer match outcomes retain nontrivial upset/draw risk even when one side is materially stronger.

## Suggested downstream use

Use as synthesis input and as a reminder to treat late lineup news as the main remaining catalyst rather than continuing broad generic form research.
