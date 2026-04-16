---
type: proposed_driver_provisional_synthesis_review
family_slug: coalition-fragmentation
review_model: qwen3.5:9b
generated_at: 2026-04-13T21:15:51Z
prompt_version: v1
recommended_action: merge_provisional_buckets
target_family_slug: coalition-formation-fragility
target_family_label: "coalition-formation-fragility"
target_canonical_driver: elections
review_confidence: low
status: active
---

# Provisional synthesis review: coalition-fragmentation

## Recommendation
- action: `merge_provisional_buckets`
- target family slug: `coalition-formation-fragility`
- target family label: `coalition-formation-fragility`
- target canonical driver: `elections`
- confidence: `low`

## Rationale
The focal bucket 'coalition-fragmentation' and neighbor 'coalition-formation-fragility' share the same canonical driver 'elections' and high overlap scores (1.75). Both describe mechanisms where coalition dynamics (fragmentation vs formation fragility) are driven by electoral mechanics. The term 'coalition' is the shared semantic core, while 'fragmentation' and 'formation-fragility' describe related but potentially overlapping states of coalition instability. Given the instruction to prefer conservative judgments, merging with 'coalition-formation-fragility' is safer than merging with 'opposition-fragmentation' (different semantic core) or 'coalition-brand-decay' (different outcome). However, evidence is sparse (total occurrences 3 vs 3 vs 2), so confidence is moderate.

## Suggested follow-up
Review the raw candidate notes for 'coalition-fragmentation' and 'coalition-formation-fragility' to determine if the distinction between 'fragmentation' and 'formation-fragility' is substantive or merely semantic variation.

## Normalization notes
- `confidence_defaulted`

## Source input
- `qualitative-db/40-research/review-queue/drivers-candidates/provisional-family-synthesis/inputs/generated-provisional-synthesis-input-coalition-fragmentation.json`
