---
type: evidence_map
case_key: case-20260407-b3dc16a7
dispatch_id: dispatch-case-20260407-b3dc16a7-20260407T031152Z
research_run_id: d153b911-9902-4c82-ab9e-22887a2a6d05
analysis_date: 2026-04-07
persona: catalyst-hunter
domain: politics
subdomain: social-media
entity: donald-trump
topic: will-donald-trump-post-80-99-truth-social-posts-from-march-31-to-april-7-2026
question: "Will Donald Trump post 80-99 Truth Social posts from March 31 to April 7, 2026?"
driver: operational-risk
date_created: 2026-04-07
agent: catalyst-hunter
status: draft
confidence: medium
conflict_status: low
action_relevance: high
related_entities: ["donald-trump"]
related_drivers: ["operational-risk", "reliability"]
proposed_entities: []
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260407-b3dc16a7/researcher-analyses/2026-04-07/dispatch-case-20260407-b3dc16a7-20260407T031152Z/personas/catalyst-hunter.md"]
tags: ["evidence-netting", "catalyst-calendar", "resolution-audit"]
---

# Summary

The market is now mostly an intraday threshold-crossing question. XTracker already shows 77 counted posts, so the relevant catalyst is whether Trump produces 3 or more additional qualifying posts before noon ET. Evidence is supportive but not overwhelming because an independent archive counted 79 rather than 77, and rule-sensitive tracker mechanics remain slightly opaque.

## Question being evaluated

Will Donald Trump finish the March 31 noon ET to April 7 noon ET window with 80-99 counted Truth Social posts under Polymarket's XTracker-based rules?

## Current lean

Slight lean toward YES / 80-99, but only modestly above a coin flip.

## Prior / starting view

Starting view was that the band looked plausible because Trump's weekly posting base rate is high, but the narrow wording and tracker-rule quirks meant the real question was live count integrity plus the final-hours posting cadence.

## Evidence supporting the claim

- **Governing tracker already at 77** — source note: `2026-04-07-catalyst-hunter-xtracker-final-window-audit.md`. Direct and high weight. Only 3 more counted posts are needed to enter the band.
- **Underlying XTracker export matched the headline total exactly** — same source note. Direct and high weight. Reduces concern that the visible counter is stale or detached from export data.
- **Trump often posts in bursts and repost-like items count** — same source note plus `2026-04-07-base-rate-truth-archive-and-base-rate.md`. Indirect-to-direct and medium weight. The export includes quote/repost-like and blank/media items, so the hurdle is operationally easier than requiring 3 long original text posts.
- **Prior week reached 99** — XTracker contextual comparison in catalyst source note. Indirect and medium weight. Shows recent output regime has been high enough that a 3-post final push is ordinary rather than exceptional.

## Evidence against the claim

- **Independent archive count was 79, not 77, highlighting source mismatch risk** — source note: `2026-04-07-base-rate-truth-archive-and-base-rate.md`. Directly relevant but medium weight because archive is not the settlement source.
- **No posts yet in the queried final-hours sub-window at audit time** — source note: `2026-04-07-catalyst-hunter-xtracker-final-window-audit.md`. Direct and medium weight. The needed catalyst had not started yet.
- **Rule wording around replies-on-main-feed and deleted posts is implementation-dependent** — source note: `2026-04-07-market-implied-polymarket-rules.md`. Direct for rules, medium weight for outcome. Narrow markets can swing on edge-case classification.
- **Current week pace trails prior week materially** — catalyst source note. Indirect and medium weight. Cooling pace raises risk that the final 3 never arrive.

## Ambiguous or mixed evidence

- **Truth Social profile identity page confirms `@realDonaldTrump` but is poor for manual counting** — source note: `2026-04-07-variant-view-truthsocial-identity-and-access.md`. Useful for identity verification, weak for direct count reconstruction.
- **Blank-body/media posts** can count, but public lightweight fetches do not always make their type obvious. This supports tracker dependence while also making external audit harder.

## Conflict between inputs

The main disagreement is not factual about identity; it is measurement-based between the governing tracker count (77) and the independent archive count (79). This is partly operational and partly rules-based. The tracker wins for settlement unless clearly broken, but the mismatch is enough to cap confidence.

## Key assumptions

- Trump still posts at least 3 more qualifying items before noon ET.
- XTracker continues updating normally through the close.
- The current 77 baseline is not later revised downward by a rule-sensitive audit.

## Key uncertainties

- Whether the final-hours posting burst materializes.
- Whether any deleted or edge-case reply/main-feed items meaningfully change the terminal total.
- Whether tracker-vs-archive mismatch reflects harmless methodology differences or a more material counting issue.

## Disconfirming signals to watch

- Continued zero-post morning on XTracker.
- Tracker sync problems or stale timestamps.
- Manual export evidence that currently counted items are misclassified non-qualifiers.

## What would increase confidence

- Even one fresh posting burst in the morning hours.
- Another verification pass showing the tracker and export remain aligned.
- Better transparency on whether any edge-case counted items are replies versus reposts/quotes.

## Net update logic

The live 77 count did most of the work. That moved the question from an abstract weekly-base-rate exercise to a concrete final-threshold exercise. I downweighted the independent 79-row archive because it is not the source of truth, but I did not ignore it because the mismatch shows nontrivial measurement ambiguity.

## Suggested downstream use

Use this as forecast-update and orchestrator-synthesis input, with emphasis on the late repricing trigger: the next 3 qualifying XTracker posts matter far more than broad narrative commentary.