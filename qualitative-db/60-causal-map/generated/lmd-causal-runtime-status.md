# LMD + causal runtime status

## Summary

- generated_at: `2026-04-16T19:15:02.876257+00:00`
- assignments_by_arm: `{'control': 83, 'treatment': 14}`
- exposures_by_arm: `{'treatment': 46}`
- trial_modes: `{'preview_only': 23, 'treatment_injected': 5}`
- resolved_treatment_case_count: `0`
- pending_treatment_case_count: `10`
- open_graph_violation_count: `0`
- proposal_funnel_total: `15`
- coverage_counts: `{'strong': 11}`
- retry_queue_depth: `0`
- report_timestamps: `{'post_treatment_feedback': '2026-04-16T19:02:27.213144+00:00', 'phase11_retrieval_policy_report': '2026-04-16T19:15:00.140687+00:00', 'reconciliation': '2026-04-16T19:15:01.094177+00:00', 'governance': '2026-04-16T19:02:26.617756+00:00', 'trial_packets': '2026-04-16T19:02:26.923102+00:00', 'shadow_vs_live': '2026-04-16T19:02:27.182626+00:00'}`

## Pending treatment cohort

- `case-20260415-0c8ac7fd` / `dispatch-case-20260415-0c8ac7fd-20260415T190844Z` — status=treatment_ready; selected=0; injected=0
- `case-20260415-5996483c` / `dispatch-case-20260415-5996483c-20260415T193222Z` — status=treatment_ready; selected=0; injected=0
- `case-20260415-0735f476` / `dispatch-case-20260415-0735f476-20260415T201136Z` — status=treatment_ready; selected=0; injected=0
- `case-20260416-a8277fc8` / `dispatch-case-20260416-a8277fc8-20260416T001420Z` — status=treatment_ready; selected=0; injected=0
- `case-20260416-7bf6a6c4` / `dispatch-case-20260416-7bf6a6c4-20260416T025105Z` — status=treatment_ready; selected=0; injected=0
- `case-20260416-f08c3dae` / `dispatch-case-20260416-f08c3dae-20260416T041907Z` — status=treatment_ready; selected=1; injected=1
- `case-20260416-bacb47cd` / `dispatch-case-20260416-bacb47cd-20260416T101708Z` — status=treatment_ready; selected=1; injected=1
- `case-20260416-66f6f47e` / `dispatch-case-20260416-66f6f47e-20260416T141457Z` — status=treatment_ready; selected=1; injected=1
- `case-20260416-605a067d` / `dispatch-case-20260416-605a067d-20260416T142910Z` — status=treatment_ready; selected=1; injected=1
- `case-20260416-8bef05aa` / `dispatch-case-20260416-8bef05aa-20260416T144205Z` — status=treatment_ready; selected=1; injected=1

## Coverage gaps

- none

## Candidate outcome ledger (top)

- `node:verification-state-separation` [source_resolution] — stage=trial_candidate; shadow=40/0; trial=28 injected judged=0
- `edge:verification-caution__conditions__resolution-risk-path-separation` [workflow_pricing] — stage=shadow_candidate; shadow=61/0; trial=0 injected judged=0
- `node:governing-source-proof-capture` [source_resolution] — stage=shadow_candidate; shadow=54/0; trial=0 injected judged=0
- `node:primary-resolution-source-identification` [source_resolution] — stage=shadow_candidate; shadow=54/0; trial=0 injected judged=0
- `node:resolution-risk-path-separation` [workflow_pricing] — stage=shadow_candidate; shadow=39/0; trial=0 injected judged=0
- `edge:time-remaining-nontrivial__increases__path-volatility-pressure` [threshold_touch] — stage=shadow_candidate; shadow=30/0; trial=0 injected judged=0
- `edge:settlement-source-specificity__increases__primary-resolution-source-identification` [source_resolution] — stage=shadow_candidate; shadow=23/0; trial=0 injected judged=0
- `edge:resolution-surface-ambiguity__increases__governing-source-proof-capture` [source_resolution] — stage=shadow_candidate; shadow=9/0; trial=0 injected judged=0
- `edge:price-near-threshold__increases__threshold-distance-scaling` [threshold_touch] — stage=aggregated; shadow=0/0; trial=0 injected judged=0
- `edge:resolution-surface-ambiguity__increases__verification-state-separation` [source_resolution] — stage=aggregated; shadow=0/0; trial=0 injected judged=0
- `node:ex-post-assimilation-labeling` [workflow_pricing] — stage=aggregated; shadow=0/0; trial=0 injected judged=0
- `node:hazard-rate-touch-framing` [threshold_touch] — stage=aggregated; shadow=0/0; trial=0 injected judged=0
- `node:path-volatility-pressure` [threshold_touch] — stage=aggregated; shadow=0/0; trial=0 injected judged=0
- `node:resistance-discount-justification` [workflow_pricing] — stage=aggregated; shadow=0/0; trial=0 injected judged=0
- `node:threshold-distance-scaling` [threshold_touch] — stage=aggregated; shadow=0/0; trial=0 injected judged=0

