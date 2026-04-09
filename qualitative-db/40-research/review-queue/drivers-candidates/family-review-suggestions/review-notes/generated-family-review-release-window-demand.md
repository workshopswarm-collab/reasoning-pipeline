---
type: proposed_driver_family_review
family_slug: release-window-demand
review_model: qwen3.5:9b
generated_at: 2026-04-07T02:37:38Z
prompt_version: v1
recommended_action: hold
recommended_family_slug: release-window-demand
recommended_family_label: "release-window demand"
merge_target_family_slug: 
merge_target_canonical_driver: 
canon_overlap_status: partial
canon_overlap_driver: 
review_confidence: low
status: active
---

# Family review: release-window-demand

## Recommendation
- action: `hold`
- recommended family slug: `release-window-demand`
- recommended family label: `release-window demand`
- merge target family: ``
- merge target canonical driver: ``

## Canon overlap
- status: `partial`
- canonical driver: ``
- reason: related_canonical_drivers list mentions 'performance' and 'operational-risk' but these are not strong semantic matches for a demand-driven release-window mechanism; evidence is sparse (5 occurrences, 1 distinct case) so no confident merge.

## Family quality
- coherent cluster: `True`
- needs split: `False`
- confidence: `low`

## Rationale
The family contains two candidates from the same case but different personas. The first candidate relates to demand in a release window; the second relates to viewership concentration in a release week. Both are sparse (total 5 occurrences, 1 case). The grouping appears coherent as a cluster of release-window related demand/viewership drivers, but evidence is too thin to promote or split. No strong overlap with existing canon ('performance' or 'operational-risk') justifies merge. Hold is appropriate.

## Raw candidate assignments
- `release-window-demand` -> family `release-window-demand` | notes: primary candidate, risk-manager persona, 3 occurrences
- `release-week-viewership-concentration` -> family `release-window-demand` | notes: variant-view persona, 2 occurrences, same case; semantic link to release-window demand plausible but evidence sparse

## Suggested follow-up


## Normalization notes
- none

## Source candidate notes
- none

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/family-review-suggestions/inputs/generated-family-review-input-release-window-demand.json`
