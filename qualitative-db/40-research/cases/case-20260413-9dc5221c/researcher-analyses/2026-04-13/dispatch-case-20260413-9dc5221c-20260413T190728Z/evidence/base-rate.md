---
type: evidence_map
case_key: case-20260413-9dc5221c
dispatch_id: dispatch-case-20260413-9dc5221c-20260413T190728Z
research_run_id: b78bf0f9-ef38-4738-95fb-6216e973fcaf
analysis_date: 2026-04-13
persona: base-rate
domain: chess
subdomain: tournament-state
entity:
topic: sindarov-candidates-win-probability
question: "Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?"
driver: reliability
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium
conflict_status: "low-direct-conflict high-source-gap"
action_relevance: high
related_entities: []
related_drivers: ["reliability", "operational-risk"]
proposed_entities: ["javokhir-sindarov", "fide"]
proposed_drivers: ["live-standings-state"]
upstream_inputs: []
downstream_uses: []
tags: ["evidence-map", "candidates", "chess"]
---

# Summary

The current lean is that Sindarov is a strong favorite only if the live standings state is already close to decisive; absent that, the market's 95% price looks too high relative to the outside view.

## Question being evaluated

Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?

## Current lean

Lean yes, but at materially below the market price.

## Prior / starting view

Starting outside-view prior for one player in an 8-player elite double round robin is far below 50%, with only modest uplift for a player ranked around world No. 11.

## Evidence supporting the claim

- Sindarov is not a random entrant; he is the 2025 World Cup winner and around 2745 / world No. 11. Weight: meaningful contextual support.
- Available contextual reporting indicates he has been undefeated deep into the event (six wins, six draws through twelve games). Weight: large, but not authoritative here because the source is secondary.
- The market itself is at 95.05%, which suggests informed traders believe the live standings are highly favorable. Weight: moderate, but not enough to replace direct verification.

## Evidence against the claim

- The field is elite and only eight players; structurally, these events are hard to dominate and near-certainty prices require exceptional current standings. Weight: high base-rate constraint.
- Sindarov's rating/rank profile is world-class but not Magnus-level dominance. Weight: high against a generic 95% prior.
- I did not obtain a clean official FIDE standings/winner page in this run. Weight: high source-of-truth gap for endorsing extreme certainty.

## Ambiguous or mixed evidence

- Wikipedia appears to imply Sindarov is leading late, which could justify a high probability, but this is not enough to fully accept 95% without direct FIDE confirmation.

## Conflict between inputs

There is no strong factual conflict. The main issue is weighting and source hierarchy: contextual sources and market pricing point strongly toward Sindarov, while the outside view and incomplete direct verification argue against treating the position as nearly locked.

## Key assumptions

- Official FIDE standings have not already made the outcome effectively certain in a way my direct evidence failed to capture.
- The market may be somewhat overconfident because it is pricing a late-stage leader as if the event is nearly resolved.

## Key uncertainties

- Exact live standings and remaining pairings as of 2026-04-13.
- Whether tiebreak or clinching conditions materially reduce remaining variance.

## Disconfirming signals to watch

- Official FIDE standings showing a commanding lead with only one or two rounds left.
- FIDE or broad credible consensus reporting that Sindarov has already clinched or is overwhelmingly likely via tiebreaks.

## What would increase confidence

- Direct FIDE standings table or official tournament report.
- Independent high-quality chess coverage with the exact points table and remaining schedule.

## Net update logic

The outside view starts low because one player rarely deserves near-certainty in this format. Current contextual evidence moves Sindarov well above a flat prior, but not all the way to the market because the strongest justification for 95% would have to be direct live standings evidence, which remained under-verified in this run.

## Suggested downstream use

Use as an orchestrator synthesis input with emphasis on source-of-truth gap and the need for one authoritative standings check before heavy reliance on an extreme price.