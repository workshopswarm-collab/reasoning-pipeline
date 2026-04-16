# Proposed causal candidates

- occurrence_count: 15
- proposal_count: 15

## Family policy summary

### `publication_timing`
- enabled: `True` | shadow_budget: `4` | trial_budget: `1` | available_trial_slots: `1` | exploratory_trial_enabled: `False` | exploratory_trial_budget: `0` | available_exploratory_trial_slots: `0` | promotion_ready_budget: `1` | available_promotion_ready_slots: `1`
- proposals: total `0` | shadow `0` | trial `0` (standard `0` / exploratory `0`) | promotion_ready `0`
- live_nodes: total `2` | live_edges: total `1`

### `source_resolution`
- enabled: `True` | shadow_budget: `6` | trial_budget: `2` | available_trial_slots: `2` | exploratory_trial_enabled: `True` | exploratory_trial_budget: `1` | available_exploratory_trial_slots: `0` | promotion_ready_budget: `1` | available_promotion_ready_slots: `1`
- proposals: total `6` | shadow `5` | trial `1` (standard `0` / exploratory `1`) | promotion_ready `0`
- live_nodes: total `2` | live_edges: total `2`
- trial_gate_blocker_counts: `{"below_base_proposal_threshold": 6, "below_family_min_non_intervention_support_cases": 6, "below_family_min_shadow_helpful_count": 6, "below_family_min_shadow_judged_count": 3, "below_family_min_shadow_mean_score": 6, "duplicate_similarity_above_family_trial_limit": 1, "merge_recommended": 1, "no_shadow_matches": 1, "outside_family_shadow_budget": 1}`
- exploratory_trial_gate_blocker_counts: `{"below_exploratory_min_shadow_judged_count": 3, "duplicate_similarity_above_family_trial_limit": 1, "merge_recommended": 1, "no_shadow_matches": 1, "outside_exploratory_trial_budget": 2, "outside_family_shadow_budget": 1}`

### `threshold_touch`
- enabled: `True` | shadow_budget: `6` | trial_budget: `2` | available_trial_slots: `2` | exploratory_trial_enabled: `False` | exploratory_trial_budget: `0` | available_exploratory_trial_slots: `0` | promotion_ready_budget: `1` | available_promotion_ready_slots: `1`
- proposals: total `5` | shadow `1` | trial `0` (standard `0` / exploratory `0`) | promotion_ready `0`
- live_nodes: total `3` | live_edges: total `2`
- trial_gate_blocker_counts: `{"below_base_proposal_threshold": 5, "below_family_min_non_intervention_support_cases": 5, "below_family_min_shadow_helpful_count": 5, "below_family_min_shadow_judged_count": 5, "below_family_min_shadow_mean_score": 5, "no_shadow_matches": 4, "outside_family_shadow_budget": 4}`

### `unassigned`
- enabled: `False` | shadow_budget: `0` | trial_budget: `0` | available_trial_slots: `0` | exploratory_trial_enabled: `False` | exploratory_trial_budget: `0` | available_exploratory_trial_slots: `0` | promotion_ready_budget: `0` | available_promotion_ready_slots: `0`
- proposals: total `0` | shadow `0` | trial `0` (standard `0` / exploratory `0`) | promotion_ready `0`
- live_nodes: total `0` | live_edges: total `0`

### `workflow_pricing`
- enabled: `True` | shadow_budget: `5` | trial_budget: `2` | available_trial_slots: `2` | exploratory_trial_enabled: `False` | exploratory_trial_budget: `0` | available_exploratory_trial_slots: `0` | promotion_ready_budget: `1` | available_promotion_ready_slots: `1`
- proposals: total `4` | shadow `2` | trial `0` (standard `0` / exploratory `0`) | promotion_ready `0`
- live_nodes: total `2` | live_edges: total `1`
- trial_gate_blocker_counts: `{"below_base_proposal_threshold": 4, "below_family_min_non_intervention_support_cases": 4, "below_family_min_shadow_helpful_count": 4, "below_family_min_shadow_judged_count": 2, "below_family_min_shadow_mean_score": 4, "no_shadow_matches": 2, "outside_family_shadow_budget": 2}`

## Node proposals

### `resolution-risk-path-separation`
- status: `insufficient_support` | lifecycle_stage: `shadow_candidate` | family: `workflow_pricing`
- score: `1.351231` | dominant_source: `rule_projection`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.483897-04:00` | last_seen_at: `2026-04-15T14:59:10.024225-04:00`
- shadow: `39` matches | helpful `0` | neutral `0` | harmful `0` | unclear `4`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_mean_score
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.482759, "maximum": 0.86, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.14, "maximum": 0.26, "passed": true}, "mechanism_family_assignment": {"current": "workflow_pricing", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 4, "minimum": 4, "passed": true}, "shadow_matches": {"current": 39, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `verification-state-separation`
- status: `insufficient_support` | lifecycle_stage: `trial_candidate` | family: `source_resolution`
- score: `1.346231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.468214-04:00` | last_seen_at: `2026-04-15T14:59:10.071039-04:00`
- shadow: `40` matches | helpful `0` | neutral `0` | harmful `0` | unclear `4`
- trial: exposures `5` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `True` | trial_eligibility_mode: `exploratory` | exploratory_trial_rank: `1`
- family_promotion_ready_rank: `1` | within_family_promotion_ready_budget: `True` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `0.0`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- standard_trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_mean_score
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.734694, "maximum": 0.88, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.145, "maximum": 0.28, "passed": true}, "mechanism_family_assignment": {"current": "source_resolution", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 4, "minimum": 4, "passed": true}, "shadow_matches": {"current": 40, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility

### `primary-resolution-source-identification`
- status: `insufficient_support` | lifecycle_stage: `shadow_candidate` | family: `source_resolution`
- score: `1.321231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.437309-04:00` | last_seen_at: `2026-04-15T14:59:09.976178-04:00`
- shadow: `54` matches | helpful `0` | neutral `0` | harmful `0` | unclear `4`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `2`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_mean_score
- exploratory_trial_blockers: outside_exploratory_trial_budget
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.558824, "maximum": 0.88, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.17, "maximum": 0.28, "passed": true}, "mechanism_family_assignment": {"current": "source_resolution", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 4, "minimum": 4, "passed": true}, "shadow_matches": {"current": 54, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `threshold-distance-scaling`
- status: `insufficient_support` | lifecycle_stage: `aggregated` | family: `threshold_touch`
- score: `1.321231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T13:41:05.777106-04:00` | last_seen_at: `2026-04-15T14:59:10.048075-04:00`
- shadow: `0` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score, no_shadow_matches, outside_family_shadow_budget
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.518519, "maximum": 0.87, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": false, "passed": false}, "genericity_penalty": {"current": 0.17, "maximum": 0.27, "passed": true}, "mechanism_family_assignment": {"current": "threshold_touch", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 0, "minimum": 1, "passed": false}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `path-volatility-pressure`
- status: `insufficient_support` | lifecycle_stage: `aggregated` | family: `threshold_touch`
- score: `1.311231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T13:41:05.6174-04:00` | last_seen_at: `2026-04-15T14:59:09.953192-04:00`
- shadow: `0` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score, no_shadow_matches, outside_family_shadow_budget
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.545455, "maximum": 0.87, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": false, "passed": false}, "genericity_penalty": {"current": 0.18, "maximum": 0.27, "passed": true}, "mechanism_family_assignment": {"current": "threshold_touch", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 0, "minimum": 1, "passed": false}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `governing-source-proof-capture`
- status: `insufficient_support` | lifecycle_stage: `shadow_candidate` | family: `source_resolution`
- score: `1.293731` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.452615-04:00` | last_seen_at: `2026-04-15T14:59:09.905106-04:00`
- shadow: `54` matches | helpful `0` | neutral `0` | harmful `0` | unclear `4`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `3`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_mean_score
- exploratory_trial_blockers: outside_exploratory_trial_budget
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.474576, "maximum": 0.88, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.1975, "maximum": 0.28, "passed": true}, "mechanism_family_assignment": {"current": "source_resolution", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 4, "minimum": 4, "passed": true}, "shadow_matches": {"current": 54, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `ex-post-assimilation-labeling`
- status: `insufficient_support` | lifecycle_stage: `aggregated` | family: `workflow_pricing`
- score: `1.291231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T13:41:05.502741-04:00` | last_seen_at: `2026-04-15T14:59:09.880983-04:00`
- shadow: `0` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score, no_shadow_matches, outside_family_shadow_budget
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.489796, "maximum": 0.86, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": false, "passed": false}, "genericity_penalty": {"current": 0.2, "maximum": 0.26, "passed": true}, "mechanism_family_assignment": {"current": "workflow_pricing", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 0, "minimum": 1, "passed": false}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `resistance-discount-justification`
- status: `insufficient_support` | lifecycle_stage: `aggregated` | family: `workflow_pricing`
- score: `1.291231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T13:41:05.686955-04:00` | last_seen_at: `2026-04-15T14:59:09.999984-04:00`
- shadow: `0` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score, no_shadow_matches, outside_family_shadow_budget
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.4375, "maximum": 0.86, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": false, "passed": false}, "genericity_penalty": {"current": 0.2, "maximum": 0.26, "passed": true}, "mechanism_family_assignment": {"current": "workflow_pricing", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 0, "minimum": 1, "passed": false}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `hazard-rate-touch-framing`
- status: `insufficient_support` | lifecycle_stage: `aggregated` | family: `threshold_touch`
- score: `1.276231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- reason: below_node_threshold_after_support_filter
- first_seen_at: `2026-04-15T13:41:05.548411-04:00` | last_seen_at: `2026-04-15T14:59:09.929131-04:00`
- shadow: `0` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score, no_shadow_matches, outside_family_shadow_budget
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.428571, "maximum": 0.87, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": false, "passed": false}, "genericity_penalty": {"current": 0.215, "maximum": 0.27, "passed": true}, "mechanism_family_assignment": {"current": "threshold_touch", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 0, "minimum": 1, "passed": false}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

## Edge proposals

### `verification-caution__conditions__resolution-risk-path-separation`
- status: `insufficient_support` | lifecycle_stage: `shadow_candidate` | family: `workflow_pricing`
- score: `1.351231` | dominant_source: `rule_projection`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- edge: `verification-caution` -> `resolution-risk-path-separation`
- reason: below_edge_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.545602-04:00` | last_seen_at: `2026-04-15T14:59:09.857728-04:00`
- shadow: `61` matches | helpful `0` | neutral `0` | harmful `0` | unclear `4`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_mean_score
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.515152, "maximum": 0.86, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.14, "maximum": 0.26, "passed": true}, "mechanism_family_assignment": {"current": "workflow_pricing", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 4, "minimum": 4, "passed": true}, "shadow_matches": {"current": 61, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `resolution-surface-ambiguity__increases__governing-source-proof-capture`
- status: `insufficient_support` | lifecycle_stage: `shadow_candidate` | family: `source_resolution`
- score: `1.331231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- edge: `resolution-surface-ambiguity` -> `governing-source-proof-capture`
- reason: below_edge_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.515032-04:00` | last_seen_at: `2026-04-15T14:59:09.763763-04:00`
- shadow: `9` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score
- exploratory_trial_blockers: below_exploratory_min_shadow_judged_count
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.742424, "maximum": 0.88, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.16, "maximum": 0.28, "passed": true}, "mechanism_family_assignment": {"current": "source_resolution", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 9, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `price-near-threshold__increases__threshold-distance-scaling`
- status: `insufficient_support` | lifecycle_stage: `aggregated` | family: `threshold_touch`
- score: `1.321231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- edge: `price-near-threshold` -> `threshold-distance-scaling`
- reason: below_edge_threshold_after_support_filter
- first_seen_at: `2026-04-15T13:41:05.339589-04:00` | last_seen_at: `2026-04-15T14:59:09.738-04:00`
- shadow: `0` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score, no_shadow_matches, outside_family_shadow_budget
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.733945, "maximum": 0.87, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": false, "passed": false}, "genericity_penalty": {"current": 0.17, "maximum": 0.27, "passed": true}, "mechanism_family_assignment": {"current": "threshold_touch", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 0, "minimum": 1, "passed": false}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `settlement-source-specificity__increases__primary-resolution-source-identification`
- status: `insufficient_support` | lifecycle_stage: `shadow_candidate` | family: `source_resolution`
- score: `1.311231` | dominant_source: `rule_projection`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- edge: `settlement-source-specificity` -> `primary-resolution-source-identification`
- reason: below_edge_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.499677-04:00` | last_seen_at: `2026-04-15T14:59:09.811358-04:00`
- shadow: `23` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score
- exploratory_trial_blockers: below_exploratory_min_shadow_judged_count
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.802632, "maximum": 0.88, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.18, "maximum": 0.28, "passed": true}, "mechanism_family_assignment": {"current": "source_resolution", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 23, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `time-remaining-nontrivial__increases__path-volatility-pressure`
- status: `insufficient_support` | lifecycle_stage: `shadow_candidate` | family: `threshold_touch`
- score: `1.311231` | dominant_source: `case_extractor`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- edge: `time-remaining-nontrivial` -> `path-volatility-pressure`
- reason: below_edge_threshold_after_support_filter
- first_seen_at: `2026-04-15T13:41:05.43335-04:00` | last_seen_at: `2026-04-15T14:59:09.834795-04:00`
- shadow: `30` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score
- exploratory_trial_blockers: exploratory_trial_disabled
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.820513, "maximum": 0.87, "passed": true}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": true, "passed": true}, "genericity_penalty": {"current": 0.18, "maximum": 0.27, "passed": true}, "mechanism_family_assignment": {"current": "threshold_touch", "passed": true}, "merge_recommended": {"current": false, "passed": true}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 30, "minimum": 1, "passed": true}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, not_trial_candidate

### `resolution-surface-ambiguity__increases__verification-state-separation`
- status: `insufficient_support` | lifecycle_stage: `aggregated` | family: `source_resolution`
- score: `0.341231` | dominant_source: `rule_projection`
- cases: `1` | non_intervention_supports: `1` | contests: `0`
- intervention_only_supports: `0` | heuristic_only_supports: `0`
- edge: `resolution-surface-ambiguity` -> `verification-state-separation`
- merge_candidate_key: `resolution-surface-ambiguity__increases__verification-caution` | max_duplicate_similarity: `0.900763`
- reason: below_edge_threshold_after_support_filter
- first_seen_at: `2026-04-15T03:15:18.530945-04:00` | last_seen_at: `2026-04-15T14:59:09.787669-04:00`
- shadow: `0` matches | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- trial: exposures `0` | helpful `0` | neutral `0` | harmful `0` | unclear `0`
- family_trial_rank: `None` | within_family_trial_budget: `False` | trial_eligible: `False` | trial_eligibility_mode: `blocked` | exploratory_trial_rank: `None`
- family_promotion_ready_rank: `None` | within_family_promotion_ready_budget: `False` | promotion_ready_eligible: `False`
- shadow_trial_score: `0.0` | shadow_label_balance: `0` | trial_shrunken_utility: `0.0` | trial_label_balance: `0` | trial_harmful_rate: `None`
- supporting_case_keys: case-20260414-4e668883
- blockers: below_draft_min_cases, below_draft_non_intervention_support_cases, below_proposed_min_cases, merge_recommended
- trial_blockers: below_base_proposal_threshold, below_family_min_non_intervention_support_cases, below_family_min_shadow_helpful_count, below_family_min_shadow_judged_count, below_family_min_shadow_mean_score, duplicate_similarity_above_family_trial_limit, merge_recommended, no_shadow_matches, outside_family_shadow_budget
- exploratory_trial_blockers: below_exploratory_min_shadow_judged_count, duplicate_similarity_above_family_trial_limit, merge_recommended, no_shadow_matches, outside_family_shadow_budget
- trial_gate_details: `{"base_proposal_threshold": {"current": "insufficient_support", "passed": false, "required_any_of": ["proposed", "draft_recommendation"]}, "duplicate_of_live_graph": {"current": false, "passed": true}, "duplicate_similarity": {"current": 0.900763, "maximum": 0.88, "passed": false}, "family_policy_enabled": {"passed": true}, "family_shadow_budget": {"current": false, "passed": false}, "genericity_penalty": {"current": 0.15, "maximum": 0.28, "passed": true}, "mechanism_family_assignment": {"current": "source_resolution", "passed": true}, "merge_recommended": {"current": true, "passed": false}, "non_intervention_support_case_count": {"current": 1, "minimum": 2, "passed": false}, "open_health_violations": {"current": 0, "maximum": 0, "passed": true}, "shadow_helpful_count": {"current": 0, "minimum": 1, "passed": false}, "shadow_judged_count": {"current": 0, "minimum": 4, "passed": false}, "shadow_matches": {"current": 0, "minimum": 1, "passed": false}, "shadow_trial_score": {"current": 0.0, "minimum": 0.5, "passed": false}}`
- promotion_ready_blockers: below_family_min_trial_helpful_count, below_family_min_trial_judged_count, below_family_min_trial_shrunken_utility, merge_recommended, not_trial_candidate

