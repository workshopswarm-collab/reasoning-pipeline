---
type: proposed_driver_family_review
family_slug: release-window-demand
review_model: qwen3.5:9b
generated_at: 2026-04-09T07:41:59Z
prompt_version: v1
recommended_action: hold
recommended_family_slug: release-window-demand
recommended_family_label: "release-window demand"
merge_target_family_slug: 
merge_target_canonical_driver: 
canon_overlap_status: none
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
- status: `none`
- canonical driver: ``
- reason: family marked as novel with no canonical driver coverage; related drivers (performance, operational-risk) are distinct mechanisms.

## Family quality
- coherent cluster: `True`
- needs split: `False`
- confidence: `low`

## Rationale
The family contains two candidates from the same case but different personas. Evidence is sparse (5 total occurrences, 1 distinct case). The candidates are not clearly materially different mechanisms (one is demand, one is viewership concentration) but are co-mentioned and adjacent. Given the lack of clear mechanistic distinction and sparse evidence, hold rather than split or promote. No strong overlap with existing canon.

## Raw candidate assignments
- `release-window-demand` -> family `release-window-demand` | notes: primary candidate, risk-manager persona, 3 occurrences.
- `release-week-viewership-concentration` -> family `release-window-demand` | notes: variant-view persona, 2 occurrences, co-occurring in same case; mechanism distinction unclear, keep grouped.

## Suggested follow-up
gather more cases to determine if the two candidates represent distinct mechanisms or a single coherent concept.

## Normalization notes
- `canon_overlap_status_defaulted_to_none`

## Source candidate notes
- `release-window-demand` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-release-window-demand.md`
- `release-week-viewership-concentration` -> `qualitative-db/40-research/review-queue/drivers-candidates/candidate-notes/generated-driver-candidate-release-week-viewership-concentration.md`

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/surfaced-family-review/inputs/generated-family-review-input-release-window-demand.json`
