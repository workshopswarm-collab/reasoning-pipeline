---
type: evidence_map
case_key: case-20260416-e5b42460
dispatch_id: dispatch-case-20260416-e5b42460-20260416T051736Z
research_run_id: ea07da7a-027e-42fa-b3d7-608de40816ea
analysis_date: 2026-04-16
persona: market-implied
domain: sports
subdomain: soccer
entity:
topic: fenerbahce-vs-caykur-rizespor
question: "Will Fenerbahçe SK win on 2026-04-17?"
driver: performance
date_created: 2026-04-16
agent: market-implied
status: draft
confidence: medium
conflict_status: low
action_relevance: medium
related_entities: []
related_drivers: ["performance"]
proposed_entities: ["fenerbahce-sk", "caykur-rizespor", "super-lig"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: []
tags: ["sports", "soccer", "super-lig", "market-implied"]
---

# Summary

The evidence nets to a straightforward view: Fenerbahçe deserve to be strong home favorites, and the market price around 74.5% looks broadly reasonable, though perhaps a touch rich rather than obviously wrong.

## Question being evaluated

Will Fenerbahçe SK win their Süper Lig match against Çaykur Rizespor on 2026-04-17, under 90-minute settlement rules?

## Current lean

Lean Yes; market roughly efficient.

## Prior / starting view

Starting baseline was the market price of 0.745, treated as an information-rich prior.

## Evidence supporting the claim

- Polymarket rules page: direct contract interpretation confirms Yes resolves only on a Fenerbahçe regulation win. This removes ambiguity about extra time or postponement handling. Weight: high for resolution mechanics, not for probability.
- Transfermarkt Fenerbahçe schedule/record page: unbeaten home league record (10-4-0, 32:13) supports a strong home-favorite prior. Direct contextual evidence. Weight: high.
- Transfermarkt Rizespor schedule/record page: weak away league record (2-7-5) supports the market's pro-Fenerbahçe tilt. Direct contextual evidence. Weight: medium-high.
- Transfermarkt form table: Fenerbahçe's recent form is better than Rizespor's, though both are respectable. Indirect contextual evidence. Weight: medium.
- Transfermarkt squad pages: Fenerbahçe roster quality appears materially stronger. Indirect contextual evidence. Weight: medium.

## Evidence against the claim

- Rizespor's recent form is not poor; they are 3-0-2 over the last five league matches, so this is not an obviously soft opponent arriving in collapse. Weight: medium.
- Soccer is inherently draw-heavy, and even strong favorites often fail to convert superiority into a regulation win. Weight: medium.
- No clean official lineup/injury confirmation was obtained in the reviewed sources, leaving room for hidden negative team news. Weight: medium.

## Ambiguous or mixed evidence

- Market values and squad profiles support Fenerbahçe on paper, but paper quality does not always translate cleanly into single-match win probability.
- Recent form favors Fenerbahçe, but not by enough to alone justify an extremely aggressive price.

## Conflict between inputs

No strong factual conflict across reviewed inputs. The main issue is weighting: whether strong home/quality context deserves a number as high as 74.5% versus something a few points lower.

## Key assumptions

- Public team-strength and venue information explain most of the market price.
- No late injury/rotation news materially undermines the home-favorite case.
- Transfermarkt context is directionally accurate even if not authoritative.

## Key uncertainties

- Confirmed lineups and last-minute absences.
- Whether the market is incorporating sharper bookmaker or local-information signals not visible in reviewed sources.

## Disconfirming signals to watch

- Credible reports of major Fenerbahçe absences.
- Sharp pre-kickoff price drop for Fenerbahçe.
- Multiple independent previews downgrading the home side for tactical or availability reasons.

## What would increase confidence

- Confirmed lineups close to full strength for Fenerbahçe.
- Independent odds or preview consensus also clustering around mid-70s home-win probability.
- Official league or club pre-match reporting without adverse team news.

## Net update logic

Starting from the market prior, the public evidence reviewed mostly validates the direction and much of the magnitude. The evidence does not strongly justify a large contrarian cut, but it does leave enough uncertainty to keep my estimate slightly below market rather than fully matching it.

## Suggested downstream use

Use as an input for orchestrator synthesis: the market-implied lane finds little basis for a strong anti-market stance and suggests any edge here is likely small unless another persona uncovers materially stronger team-news evidence.