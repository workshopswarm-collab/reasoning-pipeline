---
type: evidence_map
case_key: case-20260416-683adab3
dispatch_id: dispatch-case-20260416-683adab3-20260416T160048Z
research_run_id: 0bf27ace-80d7-41c2-83a1-e68654d514bc
analysis_date: 2026-04-16
persona: variant-view
domain: culture
subdomain: film-box-office-and-ranking-surfaces
entity: the-numbers
topic: lee-cronins-the-mummy-opening-weekend-box-office
question: "Will \"Lee Cronin's The Mummy\" opening weekend domestic box office be between $10m and $15m on The Numbers' final 3-day weekend figure?"
driver:
date_created: 2026-04-16
agent: variant-view
status: draft
confidence: medium
conflict_status: "low-direct-conflict / high-pre-release-uncertainty"
action_relevance: medium
related_entities: ["box-office-mojo", "the-numbers"]
related_drivers: []
proposed_entities: ["warner-bros", "lee-cronins-the-mummy"]
proposed_drivers: ["box-office-range-fragility", "pre-release-tracking-uncertainty"]
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260416-683adab3/researcher-analyses/2026-04-16/dispatch-case-20260416-683adab3-20260416T160048Z/personas/variant-view.md"]
tags: ["evidence-map", "variant-view", "box-office"]
---

# Summary

The current lean is that the market's 70% confidence in the $10m-$15m bucket is too high, even though that bucket is still the single most plausible band.

## Question being evaluated

Will the final The Numbers 3-day opening-weekend figure for Lee Cronin's The Mummy land between $10m and $15m?

## Current lean

Lean **No / below market confidence on Yes**. The $10m-$15m band is plausible, but not plausible enough for 70% without stronger direct tracking evidence.

## Prior / starting view

Starting baseline: a mid-budget wide horror launch often can open somewhere around the low-to-mid teens, so the market's directional intuition is understandable.

## Evidence supporting the claim

- The film is a wide Warner Bros. release and therefore has enough distribution support to make a low-teens opening realistic.
  - Source: The Numbers title page; Box Office Mojo release page.
  - Directness: contextual.
  - Weight: medium.
- Horror / supernatural horror positioning with recognizable Mummy branding creates a straightforward genre-commercial lane for an opening in the target area.
  - Source: The Numbers title page.
  - Directness: contextual.
  - Weight: medium.
- The contract uses the 3-day weekend figure including previews, which can help a front-loaded horror title clear into a middle bracket quickly.
  - Source: Polymarket rule text.
  - Directness: direct for settlement mechanics, indirect for performance.
  - Weight: medium.

## Evidence against the claim

- The market is pricing a **narrow** range outcome at 70%, which is aggressive before opening-weekend data exists.
  - Source: current market price + contract structure.
  - Directness: direct.
  - Weight: high.
- Both downside miss (<$10m) and upside miss (>$15m) defeat the contract, and pre-release evidence here does not yet constrain either tail tightly.
  - Source: contract structure + lack of direct tracking in checked sources.
  - Directness: direct / inferential.
  - Weight: high.
- There is no authoritative current The Numbers weekend performance data yet, so confidence must come from indirect evidence rather than source-of-truth performance evidence.
  - Source: The Numbers title page status.
  - Directness: direct.
  - Weight: medium-high.

## Ambiguous or mixed evidence

- Strong horror producers and familiar IP can cut both ways: they can support a healthy debut, but they can also cause the crowd to cluster too tightly around a familiar low-teens narrative.
- Wide release confirmation raises the floor but also keeps open the possibility of a better-than-expected launch above the bracket.

## Conflict between inputs

There is little factual conflict across sources. The disagreement is mainly **weighting-based** and **uncertainty-based**: the market appears to convert generic release setup into a very high probability for a narrow range, while the evidence collected here only supports that range as plausible, not dominant.

## Key assumptions

- Pre-release uncertainty is still materially wider than the market implies.
- No hidden late tracking evidence exists that would sharply tighten the expected range into the low teens.

## Key uncertainties

- Preview strength and Friday multiple.
- Theater count and marketing conversion quality.
- Whether the film over-indexes on franchise familiarity or under-indexes on audience enthusiasm.

## Disconfirming signals to watch

- Strong Friday estimate that mechanically points to ~$11m-$14m.
- Independent trade tracking clustering tightly around low teens.
- Final weekend reporting showing a very standard horror trajectory.

## What would increase confidence

- Verified preview totals.
- A credible Friday number.
- Independent reporting from trade outlets or trackers on expected opening range.

## Net update logic

The main update is not that the film must miss the bracket; it is that the market's confidence in the bracket looks too high relative to the evidence actually visible. The contract's narrow-range structure matters more than the generic "this looks like a low-teens horror opener" story.

## Suggested downstream use

Use as forecast-update input and as an audit trail for why variant-view pushed back on market confidence without claiming a strong directional alt-range.
