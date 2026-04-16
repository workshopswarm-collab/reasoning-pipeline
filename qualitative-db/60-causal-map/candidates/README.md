---
type: system_guide
domain: causal_map
status: active
last_updated: 2026-04-15
owner: evaluator
tags: [causal-map/candidates, qualitative-db/60-causal-map, recursive-improvement]
---

# Proposed causal candidates

This folder documents the **proposal layer** for future causal-map topology growth.

Hard rule:
- proposal generation may be automatic
- promotion to live reviewed graph topology should remain lifecycle-gated

Lifecycle policy:
- `qualitative-db/00-system/methodology/causal-lifecycle-policy.md`

## Current first-slice mechanism

The first slice mines proposed node/edge occurrences from existing `causal-projection.json` files.

Current runtime helpers:
- `roles/evaluator/runtime/scripts/extract_case_causal_suggestions.py`
- `roles/evaluator/runtime/scripts/canonicalize_causal_suggestions.py`
- `roles/evaluator/runtime/scripts/mine_causal_candidates.py`
- `roles/evaluator/runtime/scripts/aggregate_causal_candidate_proposals.py`
- `roles/evaluator/runtime/scripts/log_proposed_causal_shadow_matches.py`
- `roles/evaluator/runtime/scripts/score_proposed_causal_shadow_outcomes.py`
- `roles/evaluator/runtime/scripts/log_proposed_causal_trial_exposure.py`
- `roles/evaluator/runtime/scripts/score_proposed_causal_trial_outcomes.py`
- `roles/evaluator/runtime/scripts/materialize_promoted_causal_candidates.py`

Current DB schema:
- `roles/evaluator/sql/024_proposed_causal_candidate_occurrences.sql`
- `roles/evaluator/sql/025_proposed_causal_candidate_stats.sql`
- `roles/evaluator/sql/031_proposed_causal_shadow_matches.sql`
- `roles/evaluator/sql/034_proposed_causal_shadow_outcome_labels.sql`
- `roles/evaluator/sql/035_causal_family_policies.sql`
- `roles/evaluator/sql/036_proposed_causal_trial_exposures.sql`
- `roles/evaluator/sql/037_proposed_causal_trial_outcome_labels.sql`
- `roles/evaluator/sql/038_extend_causal_family_policies_for_promotion.sql`

Family-policy control surface:
- canonical config file: `qualitative-db/60-causal-map/family-policies.json`
- DB sync helper: `roles/evaluator/runtime/scripts/upsert_causal_family_policies.py`
- aggregation now emits per-family budgets, live occupancy, per-proposal family ranks, shrunken `shadow_trial_score`, and `trial_readiness` blockers.
- explicit advancement entrypoint: `roles/evaluator/runtime/scripts/advance_proposed_causal_candidates.py`
- trial-overlay selector: `roles/evaluator/runtime/lib/proposed_causal_trial_selection.py`

Current Phase 3 / Phase 4 / Phase 5 / Phase 6 / Phase 7 substrate:
- every LMD bundle build can now compute a `trial_overlay` block
- trial overlay selection is deterministic and only considers proposals already at `trial_candidate`
- treatment bundles can mark the overlay as `used=true` / `overlay_mode=treatment_injected`; control bundles remain preview-only
- dispatch runtime can persist trial exposures into `public.proposed_causal_trial_exposures`, including whether they were previewed or actually injected
- prompt injection is bounded to a separate `## Trial mechanism checks (experimental)` section and is only rendered when the bundle marks the overlay as used
- injected trial exposures can now be labeled deterministically as `helpful`, `neutral`, `harmful`, or `unclear` via `score_proposed_causal_trial_outcomes.py`
- proposal summaries now expose trial counts and conservative `trial_shrunken_utility = trial_score_sum / (trial_exposure_count + 6.0)`
- the promotion-ready controller is now active in `advance_proposed_causal_candidates.py` / `aggregate_causal_candidate_proposals.py`, using trial utility, contestation, genericity, open health violations, merge/duplicate blockers, and family-local promotion budgets to determine `promotion_ready`
- `materialize_promoted_causal_candidates.py` can now turn `promotion_ready` proposals into live graph `draft` node/edge notes with preserved provenance and lifecycle event logging, then refresh proposal summaries so those proposals can fall out of the pending-candidate path on the next aggregate pass

Current Phase 2 advancement rule:
- proposal must first clear the base proposal thresholds (`promotion_status in {proposed, draft_recommendation}`)
- then it must clear family-policy thresholds for:
  - shadow judged count
  - helpful shadow count
  - shrunken `shadow_trial_score`
  - non-intervention support case count
  - genericity ceiling
  - duplicate-similarity ceiling
- then it must rank inside the family trial budget (`max_trial_candidates`)
- only then does lifecycle stage advance to `trial_candidate`

`shadow_trial_score` is intentionally conservative:
- current formula = `shadow_score_sum / (shadow_judged_count + 4.0)`
- that is a zero-centered prior with prior sample size 4, so thin early evidence does not immediately promote a proposal.

Generated summaries live under:
- `qualitative-db/60-causal-map/generated/proposed-causal-candidates-summary.json`
- `qualitative-db/60-causal-map/generated/proposed-causal-candidates-index.md`
- `qualitative-db/60-causal-map/generated/canonical-causal-suggestions-summary.json`
- `qualitative-db/60-causal-map/generated/canonical-causal-suggestions-index.md`

Reviewed-case suggestion artifacts live under each case review:
- `case-reviews/<case-key>/causal-suggestions.json`
- `case-reviews/<case-key>/causal-suggestions-canonical.json`

## Proposal lifecycle

Proposal-layer candidates may move through:
- `observed`
- `aggregated`
- `shadow_candidate`
- `trial_candidate`
- `promotion_ready`
- `rejected`
- `duplicate_of_live_graph`

Proposal-layer items are **not** prompt-time LMD canon.
They exist to accumulate evidence, shadow performance, and promotion metadata before any live graph promotion occurs.

Phase 3 broadens candidate generation by extracting and canonicalizing reviewed-case suggestions before proposal mining. Those suggestion artifacts should inform proposal occurrences only when the underlying case projection still clears the stricter Phase-2 significance gate.

Shadow evaluation now sits between proposal accumulation and any future automated promotion:
- every LMD bundle build can compute `shadow_evaluation.top_matches`
- dispatch runtime can persist those matches into `public.proposed_causal_shadow_matches`
- `score_proposed_causal_shadow_outcomes.py` deterministically labels each shadow row as `helpful`, `neutral`, `harmful`, or `unclear`
- shadow matches are evaluated in parallel and logged, but they are not injected as live graph canon

### Phase 1 deterministic shadow-outcome thresholds

The first shadow-outcome scorer is intentionally conservative.
It uses only deterministic downstream evidence from:
- same-case proposal occurrences in `public.proposed_causal_candidate_occurrences`
- same-case canonical reviewed suggestions in `case-reviews/<case-key>/causal-suggestions-canonical.json`
- same-case final projection overlap from `case-reviews/<case-key>/causal-projection.json`

Current weighting / gating logic:
- `+3.0` for same-case non-intervention proposal support
- `+2.25` for same-case mixed/intervention support
- `+1.0` for same-case weak-only support
- `-4.0` for same-case explicit contest / weakening
- `+1.4` per exact canonical suggestion match (capped)
- `+0.6` per canonical merge-candidate match (capped)
- `+0.9` per required-check overlap with final projection (capped)
- `+0.25` per active-node overlap with final projection (capped)
- `+0.35` per edge overlap with final projection (capped)
- `-1.25` penalty when the final case is significant, the candidate would have injected, and no downstream support materialized
- `-0.35` merge-ambiguity penalty when the proposal already looks like a near-duplicate / merge candidate

Current labels:
- `helpful` if score `>= 3.0` **and** the row clears a strong-support gate
  - strong-support gate = same-case non-intervention support, or same-case support plus canonical/projection reinforcement
- `neutral` if reviewed downstream artifacts exist and score `>= 1.0`, but the row does not clear the helpful gate
- `harmful` if same-case contestation exists or total score `<= -2.0`
- `unclear` otherwise, including when no downstream reviewed artifacts exist yet

## Promotion policy

Automatic mining should only produce:
- occurrences
- recurrence stats
- lifecycle metadata
- support-provenance metadata
- duplicate / merge hints
- promotion recommendations

It should not directly create active graph topology.

## Enriched evidence-accounting metadata

Proposal occurrences should now preserve:
- `mechanism_family`
- `proposal_source`
- `evidence_channels`
- `intervention_dependency`
- `normalized_cluster_key`
- `context_snapshot`

Aggregated proposal stats should now preserve:
- source mixes and dominant proposal source
- non-intervention vs intervention-only support counts
- draft-intervention vs active-intervention support counts
- heuristic-only support counts
- review-text / signal-packet / frontmatter support counts
- near-duplicate and near-live-graph keys
- merge recommendation metadata
- context breadth / distribution metadata

Current deterministic recommendation thresholds remain:

### Node proposals
- `proposed` if:
  - `distinct_case_count >= 2`
  - `genericity_penalty <= 0.35`
- `draft_recommendation` if:
  - `distinct_case_count >= 3`
  - `support_case_count >= 2`
  - `genericity_penalty <= 0.25`

### Edge proposals
- `proposed` if:
  - `distinct_case_count >= 2`
  - `support_case_count >= 2`
  - `genericity_penalty <= 0.35`
- `draft_recommendation` if:
  - `distinct_case_count >= 3`
  - `support_case_count >= 3`
  - `support_case_count / max(contest_case_count, 1) >= 2.0`
  - `genericity_penalty <= 0.25`

These thresholds are recommendation gates, not final live-graph promotion authority.

## Additional bounded-promotion requirements

Before a proposal can later become live graph topology, it should also have:
- explicit `mechanism_family`
- duplicate / merge review against live graph
- bounded contestation
- non-trivial non-intervention support
- family-budget availability
- shadow or trial evidence when available

### Duplicate guard
If a proposal key already exists in the live graph, mark it `duplicate_of_live_graph` rather than promoting it.
