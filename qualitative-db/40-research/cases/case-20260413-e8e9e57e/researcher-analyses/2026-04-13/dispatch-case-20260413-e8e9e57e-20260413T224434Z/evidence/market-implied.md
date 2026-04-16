---
type: evidence_map
case_key: case-20260413-e8e9e57e
dispatch_id: dispatch-case-20260413-e8e9e57e-20260413T224434Z
research_run_id: a71a7e05-3ebf-4d05-8e70-91f193956657
analysis_date: 2026-04-13
persona: market-implied
domain: sports
subdomain: hockey
entity: connor-mcdavid
topic: "market efficiency in Art Ross pricing"
question: "Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?"
date_created: 2026-04-13
agent: market-implied
status: draft
confidence: medium-high
conflict_status: low
action_relevance: high
related_entities: ["connor-mcdavid", "nhl"]
related_drivers: []
proposed_entities: []
proposed_drivers: ["award-resolution-mechanics"]
upstream_inputs: []
downstream_uses: ["market-implied.md", "market-implied.sidecar.json"]
tags: ["evidence-map", "art-ross", "sports", "hockey"]
driver:
---

# Summary

The market appears to be pricing a near-closed race based on McDavid’s apparent points lead and the expectation that official NHL award attribution will follow the publicly visible leaderboard. The main residual risk is procedural/source-of-truth risk, not a live on-ice comeback case.

## Question being evaluated

Will Connor McDavid win the 2025–2026 NHL Art Ross Trophy?

## Current lean

Lean `Yes`, with only modest discount versus the market because the public evidence broadly supports the current extreme price.

## Prior / starting view

Starting from the market price, the default prior was that McDavid had likely already separated enough in the scoring race that only official confirmation remained.

## Evidence supporting the claim

- `2026-04-13-market-implied-polymarket-market-page.md`
  - Direct market evidence.
  - Shows McDavid near 96% and nearest rivals far behind.
  - High weight for market baseline, not for settlement truth.
- `2026-04-13-market-implied-hockey-reference-points-leaders.md`
  - Indirect but strong contextual evidence.
  - Shows McDavid leading with 133 points versus Kucherov 128 and MacKinnon 126.
  - High weight because it independently matches the market’s apparent assumption.
- General rule logic of the Art Ross Trophy
  - Contextual mechanism.
  - Trophy is ordinarily awarded to the regular-season points leader.
  - Medium weight because this supports why the market would rationally compress probability toward the current leader.

## Evidence against the claim

- Official NHL confirmation not directly captured in this run
  - This is a source-of-truth gap, not direct contrary evidence.
  - Medium weight because the contract explicitly prioritizes official NHL information.
- Contract wording includes finalist/announcement language
  - Procedural ambiguity could matter if the market wording is imperfectly aligned with how the Art Ross is officially administered.
  - Low-to-medium weight because it is more of a settlement-path concern than a substantive challenge to McDavid’s status.

## Ambiguous or mixed evidence

- The market page is excellent for price discovery but not authoritative for outcome truth.
- Hockey-Reference is excellent for independent leaderboard checking but still secondary to NHL official attribution.

## Conflict between inputs

There is no material factual conflict between the main inputs used here. The only tension is between strong contextual evidence and the absence of directly captured official NHL announcement text.

## Key assumptions

- Public points-leader data will map cleanly to NHL official Art Ross attribution.
- No stat correction or procedural wrinkle is large enough to change the award winner.

## Key uncertainties

- Whether NHL has already formally published the winner in a way directly accessible during this run.
- Whether any fallback consensus-reporting path would ever be needed.

## Disconfirming signals to watch

- NHL naming another player as Art Ross winner.
- Credible reporting of stat corrections or unresolved scoring changes.
- Evidence that the contract’s finalist wording matters in a nonstandard way.

## What would increase confidence

- Direct official NHL page or release explicitly naming McDavid the 2025-26 Art Ross winner.
- Another independent current-season stats source matching the same final leaderboard.

## Net update logic

The evidence did not meaningfully move me away from the market prior. Instead, the verification pass mostly supported the market’s logic: current public data already looks consistent with a nearly decided race. I still shave a few points off the market because I do not have direct official NHL attribution in hand, so the remaining uncertainty is source-of-truth/procedural rather than competitive.

## Suggested downstream use

- Orchestrator synthesis input.
- Decision-maker review.
- Light follow-up only if someone can quickly capture the direct official NHL naming source.