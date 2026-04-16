# Evaluator

This role is the home for the pipeline's evaluation, recursive-learning, and bounded self-improvement work.

Use `roles/evaluator/` for implementation related to:
- resolved-case evaluation
- calibration and attribution surfaces
- recursive learning / improvement workflows
- learning-packet compilation
- case-review generation and aggregation
- intervention tracking and evaluation
- runtime learning retrieval (for example LMD-style injection)
- other scripts, schemas, and runtime logic that belong to the evaluation / learning loop

Current status:
- initial scaffold plus first evaluator vertical-slice implementation
- concrete target architecture currently documented in `qualitative-db/00-system/methodology/recursive-learning-system-spec.md`
- implemented files now include path helpers, case-artifact discovery, event-timeline compilation, learning-packet compilation, deterministic case-review drafting, agent-backed evaluator review execution, importance-gated evaluator memory-upgrade proposals/writeback, deterministic indexing/signal extraction, SQL-backed persistence scaffolds, one-command canonical case-review bundle materialization under `runtime/`, the first intervention-registry / intervention-application logging surfaces, live LMD assignment/exposure scaffolds, the first causal-map substrate with canonical node/edge registry helpers, a first deterministic case-to-causal-map projection path, a first causal-candidate mining + proposal-aggregation layer with occurrence indexing and promotion thresholds, proposal-side trial blocker reporting plus a bounded exploratory trial lane in `aggregate_causal_candidate_proposals.py`, the planner-side first slice of mechanism-aware `lmd-bundle.json` generation, the first batch-evaluation / learned-weight update layer for LMD candidates and causal edges, a generated Phase 11 learned-policy surface (`runtime/scripts/learn_phase11_retrieval_policy.py`), a real-case default-vs-learned comparison/reporting surface (`runtime/scripts/report_phase11_retrieval_policy.py`) that writes report artifacts under `qualitative-db/60-causal-map/generated/`, a post-treatment closed-loop runner (`runtime/scripts/run_post_treatment_causal_feedback_cycle.py`) that audits recent treatment-arm cases, verifies exposure completeness, and then refreshes proposal/candidate/node/edge stats before relearning/reporting Phase 11, and an automatic feedback trigger surface (`runtime/scripts/trigger_post_treatment_feedback_cycle.py`) that lets live dispatch logging and evaluator-review completion rerun that feedback loop without waiting for manual operator intervention

Default rule:
- if work is primarily about evaluating outcomes, extracting lessons, measuring pipeline performance, or turning reviewed lessons into bounded future behavior, it belongs in `roles/evaluator/`
- if work is primarily about live research dispatch / synthesis / decision generation, it belongs in the existing upstream role folders instead
