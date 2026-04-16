---
type: proposed_driver_provisional_synthesis_review
family_slug: opposition-fragmentation
review_model: qwen3.5:9b
generated_at: 2026-04-13T19:28:11Z
prompt_version: v1
recommended_action: merge_provisional_buckets
target_family_slug: coalition-fragmentation
target_family_label: "coalition-fragmentation"
target_canonical_driver: elections
review_confidence: low
status: active
---

# Provisional synthesis review: opposition-fragmentation

## Recommendation
- action: `merge_provisional_buckets`
- target family slug: `coalition-fragmentation`
- target family label: `coalition-fragmentation`
- target canonical driver: `elections`
- confidence: `low`

## Rationale
The focal bucket 'opposition-fragmentation' and neighbor 'coalition-fragmentation' share the same canonical driver 'elections' and exhibit strong neighbor_overlap (1.75). Both describe fragmentation mechanisms within the electoral context. The other neighbors ('anti-incumbent-vote-splitting', 'coalition-brand-decay') have lower overlap scores (0.75) and distinct labels suggesting different mechanisms. Merging 'opposition-fragmentation' into 'coalition-fragmentation' consolidates evidence around the shared driver while preserving the broader fragmentation mechanism.

## Suggested follow-up
Review merged bucket for additional cases or canonical driver refinements.

## Normalization notes
- `confidence_defaulted`

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/provisional-family-synthesis/inputs/generated-provisional-synthesis-input-opposition-fragmentation.json`
