---
type: evidence_map
domain: culture
subdomain: streaming
entity: War Machine
topic: case-20260401-2fad20ad | risk-manager
question: Will "War Machine" be the #2 global Netflix movie this week?
driver: operational-risk
date_created: 2026-04-01
agent: risk-manager
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: [Netflix, War Machine]
related_drivers: [operational-risk, seasonality, media-narratives]
upstream_inputs: [qualitative-db/40-research/source-notes/by-market/case-20260401-2fad20ad-risk-manager-netflix-top10-page.md, qualitative-db/40-research/source-notes/by-market/case-20260401-2fad20ad-risk-manager-war-machine-page.md, qualitative-db/40-research/assumption-notes/case-20260401-2fad20ad-risk-manager-assumptions.md]
downstream_uses: [qualitative-db/40-research/agent-findings/risk-manager/case-20260401-2fad20ad-will-war-machine-be-the-2-global-netflix-movie-this-week-794.md]
tags: [evidence-map, case-20260401-2fad20ad, risk-manager, netflix, war-machine]
---

# Summary

## Question being evaluated

Will War Machine be the #2 global Netflix movie for the 3/23/26 - 3/29/26 weekly update used by market resolution?

## Current lean

Lean yes at high probability, but with meaningful residual operational/extraction risk that keeps this below certainty.

## Prior / starting view

Starting from the market price of 0.9585, the baseline implied probability is 95.85%. The risk-manager question is whether that confidence is too high for the evidence quality.

## Evidence supporting the claim

- Netflix's official Tudum Top 10 page is live for the exact relevant week and shows a defined #2 slot at 10.3M views.
  - Source: qualitative-db/40-research/source-notes/by-market/case-20260401-2fad20ad-risk-manager-netflix-top10-page.md
  - Why it matters: this is the governing source class for market resolution.
  - Directness: direct on chart existence and rank structure; indirect on title mapping in this scrape.
  - Weight: very high.

- The #2 to #3 gap in the chart extract is large: 10.3M vs 7.9M.
  - Source: same as above.
  - Why it matters: if War Machine is the #2 title, ordinary minor revisions are unlikely to flip the rank.
  - Directness: direct on gap size.
  - Weight: high.

- The same official Netflix page includes a direct link to `/tudum/war-machine`, and War Machine has an active current Tudum page with March 2026 coverage.
  - Sources: the two source notes above.
  - Why it matters: reduces object-identity risk and supports that War Machine is one of the active chart-relevant movie titles in this snapshot.
  - Directness: indirect on exact rank, but supportive on title relevance.
  - Weight: medium.

## Evidence against the claim

- The readable extraction of the official Top 10 page does not clearly pair the title names with the rank rows.
  - Source: netflix-top10-page source note.
  - Why it matters: the strongest remaining risk is that the 10.3M #2 row belongs to a different movie.
  - Directness: direct on extraction weakness.
  - Weight: very high as a confidence discount.

- The War Machine title page does not itself report the movie's exact weekly ranking.
  - Source: war-machine-page source note.
  - Why it matters: title existence/promotion is not the same as resolution-proof rank evidence.
  - Directness: direct.
  - Weight: medium.

- Because the market was priced near certainty already, any title-mapping error would mean the market is not slightly off but sharply wrong.
  - Source: market metadata plus assumption note.
  - Why it matters: downside is discontinuous.
  - Directness: interpretive.
  - Weight: medium.

## Ambiguous or mixed evidence

- The War Machine link on the Top 10 page is supportive, but not dispositive, because the page also contains editorial/promotional material outside the strict ranking table.
- The absence of a cleaner machine-readable extraction could be a scraper problem rather than an evidence problem.

## Conflict between inputs

There is no major factual conflict across the sources used. The main issue is not disagreement but incomplete title-to-rank mapping from the readable extraction layer.

## Key assumptions

- The 10.3M #2 row belongs to War Machine.
- Netflix will not materially revise the relevant weekly chart after publication.
- The market resolves against the official chart rather than a malformed third-party rendering.

## Key uncertainties

- Whether a cleaner direct rendering would explicitly show War Machine as #2.
- Whether any late correction or alternative official presentation changes the title mapping.

## Disconfirming signals to watch

- A screenshot or scrape of the official chart showing another movie at #2.
- A post-publication Netflix correction.
- Market resolution text pointing to a different title than the inference here.

## What would increase confidence

- Any direct official or screenshot-based pairing of War Machine with the #2 row and 10.3M views.
- Another independent extraction of the same official page preserving the title labels.

## Net update logic

The official chart makes it very likely the market is broadly right. The reason not to go all the way to the market's 95.85% is that the available extraction leaves the core title-to-row mapping partially inferred rather than perfectly explicit. So the main risk is operational/extraction risk, not competitive-ranking risk.

## Suggested downstream use

Use as decision-maker review input and as an auditable explanation for why a high-probability yes view still deserves a modest confidence haircut versus near-certainty market pricing.