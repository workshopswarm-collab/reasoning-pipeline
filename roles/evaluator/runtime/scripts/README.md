# Evaluator runtime scripts

Place evaluator-side runtime scripts here.

Examples of intended work:
- learning-packet compilation
- case-review drafting / indexing
- structured signal extraction
- intervention registry / application logging / evaluation helpers
- calibration / attribution utilities
- LMD bundle generation support when evaluator-owned

Current Step 1 intervention helpers:
- `upsert_learning_interventions.py`
- `log_learning_intervention_application.py`

Current Step 2 LMD experiment / exposure helpers:
- `assign_lmd_experiment_arm.py`
- `log_lmd_bundle_exposure.py`
- `trigger_post_treatment_feedback_cycle.py` (conditionally reruns the post-treatment feedback cycle after live dispatch logging or evaluator-review resolution updates)

Current Step 3 causal-map substrate helpers:
- `upsert_causal_nodes.py`
- `upsert_causal_edges.py`

Current Step 4 case-projection helpers:
- `project_case_to_causal_map.py`
- `backfill_significant_causal_projections.py`

Current causal-candidate proposal helpers:
- `mine_causal_candidates.py`
- `aggregate_causal_candidate_proposals.py` (now emits trial-gate blocker details, exploratory-trial blocker visibility, and family-level gate counts)

Current Step 7 batch-evaluation / learned-weight helpers:
- `update_lmd_candidate_stats.py`
- `update_causal_edge_stats.py`
- `update_causal_node_stats.py`
- `run_post_treatment_causal_feedback_cycle.py` (audits recent treatment-arm cases, verifies/backfills exposure logging when requested, refreshes proposal/candidate/node/edge stats, relearns the Phase 11 policy, and reruns the comparison report)

Current Step 9 live-graph controller helpers:
- `advance_live_causal_graph_items.py`
- `run_live_causal_graph_cycle.py` (stats -> health scan -> repair -> controller wrapper)

Current Step 10 health / repair helpers:
- `scan_causal_graph_health.py`
- `repair_causal_graph.py`
