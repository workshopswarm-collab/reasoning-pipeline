# Decision-Maker task | case `case-20260410-1c62ba82`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
You may use only web_search, web_fetch in this turn.
Stay within: searches<=5, fetches<=4, min_distinct_source_families=3 when feasible.
Choose sources independently and prefer primary, official, and resolution-relevant sources.
Do not count multiple pages from the same source family as real diversity.

## Case
- case_key: `case-20260410-1c62ba82`
- dispatch_id: `dispatch-case-20260410-1c62ba82-20260410T002235Z`
- question: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
- market_title: Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?
- market_reference_price: 0.81

## Contract

# Decision-Maker execution contract

You are the final judgment layer for a prediction-market pipeline.

Optimize for:
- predictive accuracy
- long-run expected value
- calibration
- risk discipline
- auditability

## Core rules

- Respect market baselines and base rates.
- Large edges require stronger proof.
- Do not force action because upstream work was expensive.
- Internal agreement is evidence, not authority.
- Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only.
- Form your own final judgment.
- `watch_only`, `risk_reduce_only`, `forbidden`, and `flat` are valid outputs.
- If the case is not decision-ready, say so explicitly.
- Verification is bounded, not open-ended.
- In `targeted_escalation`, bounded `web_search` / `web_fetch` use is allowed only within runtime budgets.
- Return one JSON object only. No fences. No commentary.

## Required top-level keys

Return a single JSON object with:
- `schema_version`
- `generated_at`
- `context`
- `decision`
- `valuation`
- `execution_semantics`
- `risk_controls`
- `bands`
- `invalidation`
- `epistemic_status`
- `audit`

## Critical enums

- `decision.side`: `yes | no | none`
- `decision.trade_authorization`: `authorized | watch_only | risk_reduce_only | forbidden`
- `decision.position_policy`: `enter_or_add | hold_only | reduce_only | exit_only | flat`
- `decision.decision_readiness`: `ready | needs_more_research | needs_market_update`
- `decision.thesis_class`: `edge_present | edge_too_small | price_not_good_enough | not_decision_ready | risk_constraint_binding`
- quality enums: `low | medium | high`
- `epistemic_status.decision_quality`: `clean | good_not_clean | fragile | not_ready`

## Minimum required fields by section

### context
`case_key`, `dispatch_id`, `question`, `market_id`, `market_title`, `source_decision_handoff_path`, `source_syndicated_finding_path`, `decision_maker_agent`

### decision
`side`, `trade_authorization`, `position_policy`, `decision_readiness`, `primary_crux`, `secondary_cruxes`, `thesis_class`

### valuation
`fair_value_low`, `fair_value_high`, `fair_value_mid`, `market_reference_price`, `independent_verification_quality`, `compressed_toward_market_applied`, `compression_reason`

### execution_semantics
Use `price_axis = market_implied_true_prob`.
Include: `price_source`, `rebalance_threshold_fraction`, `allow_auto_reversal`, `valid_until`, `quote_staleness_seconds`, `time_horizon`

### risk_controls
`max_position_size_pct_bankroll`, `max_additional_exposure_pct_bankroll`, `max_single_order_pct_bankroll`, `slippage_tolerance_bps`, `liquidity_min_depth`, `correlation_bucket_limit_pct_bankroll`, `confidence_level`, `portfolio_constraints`, `liquidity_caution`

### bands
Return all five canonical bands with `name`, `min_p`, `max_p`, `target_exposure_fraction`, `notes`.
Required names: `max_enter`, `scaled_enter`, `hold`, `trim`, `exit`.
Rules:
- cover `[0,1]` with no gaps or overlaps
- use the `market_implied_true_prob` axis
- if `side = yes`, exposure should generally fall as price rises
- if `side = no`, exposure should generally rise as price rises
- if `side = none`, use zero-exposure bands

### invalidation
`thesis_breakers`, `market_structure_breakers`, `time_breakers`, `reversal_conditions`

### epistemic_status
`key_uncertainties`, `reasons_to_pass`, `what_would_change_my_mind`, `decision_quality`

### audit
`market_baseline_respected`, `action_bias_check_passed`, `self_preservation_bias_check_passed`, `one_sentence_rationale`, `notes`

## Judgment guidance

- Start from synthesis as upstream compression, not as a verdict.
- Use the compact selected bundle; do not reconstruct the whole case tree unless bounded verification truly requires it.
- You may materially disagree with synthesis when evidence quality, ambiguity, freshness, or actionability justify it.
- In `targeted_escalation`, choose sources independently, prefer primary / official / resolution-relevant sources, and avoid fake diversity from one source family.
- If bounded verification is still insufficient, return a not-ready or non-action packet instead of bluffing.
- If the edge is weak, use `edge_too_small` or `price_not_good_enough`.
- Be explicit about the decisive crux, the main uncertainty, and what would change your mind.
- Keep the rationale economically grounded.

## Deterministic verification mode and bounded-input policy

- The planner/runtime already selected your verification mode and compact evidence bundle programmatically.
- Treat `structured_handoff_primary` as the main synthesis handoff interface.
- Use `prose_fallback` only for additional context on those compact structured fields, not as the default starting point.
- Treat synthesis and researcher material as advisory evidence to evaluate critically, not as a conclusion you are expected to ratify.
- You may materially disagree with upstream synthesis when evidence quality, ambiguity, freshness, or actionability justify that disagreement.
- Do not assume access to the whole case tree is required for a good decision.
- In `targeted_escalation`, independent tool-enabled verification is allowed, but source choice remains your responsibility and budgets remain runtime-enforced.
- If the compact bundle feels too compressed, use the bounded expanded fallback below before assuming broader case access is needed.
- If the compact bundle is insufficient for a responsible decision, express that with `needs_more_research`, `needs_market_update`, `watch_only`, or `forbidden` as appropriate.
- Do not turn this stage into an unbounded second synthesis pass.

## Structured selected-input bundle for this run
```json
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?","market_title":"Will Donald Trump post 100-119 Truth Social posts from April 3 to April 10, 2026?","market_reference_price":0.81,"syndicated_probability_low":0.95,"syndicated_probability_high":0.99,"syndicated_probability_midpoint":0.97,"edge_mid_vs_market_pct_points":16.0,"relation_to_market":"above_market","edge_independent_verification_quality":"high","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Public API still does not fully expose per-item counted/not-counted labels even though the closed-window exact-window result is clearly in-band.","freshness_sensitive":"yes","freshness_driver":"Post-close XTracker refresh materially changed the evidence by resolving the late overshoot tail.","decision_blockers":["Residual opacity in per-item inclusion/exclusion logic"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"no"},"structured_handoff_primary":{"edge_quality":"strong","edge_independent_verification_quality":"high","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Public API still does not fully expose per-item counted/not-counted labels even though the closed-window exact-window result is clearly in-band.","verification_gap_summary":"The remaining gap is that public API surfaces still do not fully label inclusion/exclusion mechanics item by item.","best_countercase_summary":"A settlement-mechanics discrepancy would need to remove enough items from the observed 108 to push the official count outside the band.","main_reason_for_disagreement":"Earlier disagreement was mainly timing-based because personas were pricing live overshoot risk before the window closed.","resolution_mechanics_summary":"XTracker Post Counter is primary resolution source; Truth Social is fallback only if XTracker fails to update correctly.","freshness_sensitive":"yes","freshness_driver":"Post-close XTracker refresh materially changed the evidence by resolving the late overshoot tail.","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Verified XTracker identity for realDonaldTrump on Truth Social","Exact market window remains Apr 3 16:00Z to Apr 10 15:59:59Z","Relevant Apr 3-Apr 10 tracking is now inactive after close"],"decision_blockers":["Residual opacity in per-item inclusion/exclusion logic"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nFresh synthesis-stage verification after the window closed strongly supports Yes. The governing XTracker surface still maps to the correct verified Trump account, the exact April 3-April 10 tracking object is now inactive, and a fresh exact-window query returns 108 in-window posts, which is comfortably inside the 100-119 band. The pre-close disagreement across personas was mostly about live overshoot risk; that timing risk has now resolved in favor of Yes.\n\n## Why this may matter now\n\nMarket-implied probability was 0.81. My final syndicated range is 0.95 to 0.99. The edge now looks actionable on the Yes side because fresh synthesis-stage verification after the window clos …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.72,"w":"high","thesis":"The market is directionally right because XTracker already had Trump at 103 in-window posts, but 0.81 is a bit rich given real overshoot risk before noon ET.","support":["The designated primary resolution source already showed 103 in-window posts."],"disconfirm":["Roughly 11.5 hours remained after the 103-post snapshot, leaving meaningful overshoot risk above 119."],"ambiguity":["How each returned item is classified for replies versus main-feed inclusion."],"change":"A later tracker check showing a sprint toward 120+, or evidence that many counted items are actually excluded replies, would push me down ma …"},{"persona":"catalyst-hunter","p":0.88,"w":"high","thesis":"XTracker already places Trump at 103 counted Truth Social posts in the contract window, so Yes is currently live; the only serious remaining risk is a late burst that pushes the total above 119 before noon ET.","support":["XTracker stats for the exact April 3-April 10 window report totalBetweenStartAndEnd = 103."],"disconfirm":["There were still about 12 hours left after the checked sync, leaving room for a late overshoot above 119."],"ambiguity":["Exact classification of edge-case replies, quote posts, and reposts in the public post output."],"change":"A verified XTracker move to 120+ before noon ET, or strong evidence that part of the current 103 should be excluded, would change the view."},{"persona":"risk-manager","p":0.68,"w":"medium","thesis":"Lean Yes because XTracker, the governing resolution source, currently shows 103 counted Truth Social posts in the exact window, but confidence should be discounted for late-window overshoot risk and counting-rule opacity …","support":["XTracker stats endpoint shows totalBetweenStartAndEnd = 103 for the exact market-linked window."],"disconfirm":["The market is still live, so a late posting burst could push the final official total above 119."],"ambiguity":["Which exact two captured posts were excluded from the official 103 count."],"change":"A tracker update toward or above 120, evidence of tracker malfunction, or proof that several currently counted posts should be excluded woul …"}],"selected_assumption_snippets":[{"src":"assumptions/catalyst-hunter.md","text":"# Assumption\nTrump will not generate 17 or more additional counted Truth Social items between the latest checked sync and the noon ET resolution cutoff.\n## Why this assumption matters\nThe market is already inside the 100-119 bucket at 103 according to the governing tracker. The only realistic path to a No outcome is a late burst that pushes the total to 120 or higher before noon ET.\n## What this assumption supports\n- A Yes-lean probability above the market-implied 81%.\n- The claim that the most …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Post-close XTracker refresh materially changed the evidence by resolving the late overshoot tail.?","How decision-relevant is the remaining contract/source-of-truth ambiguity: Public API still does not fully expose per-item counted/not-counted labels even though the closed-window exact-window result is clearly in-band.?","Are the current blockers still material to final judgment: Residual opacity in per-item inclusion/exclusion logic?","Is the main verification gap still decision-material: The remaining gap is that public API surfaces still do not fully label inclusion/exclusion mechanics item by item.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The remaining gap is that public API surfaces still do not fully label inclusion/exclusion mechanics item by item.","best_countercase_summary":"A settlement-mechanics discrepancy would need to remove enough items from the observed 108 to push the official count outside the band.","freshness_sensitive":"yes","freshness_driver":"Post-close XTracker refresh materially changed the evidence by resolving the late overshoot tail.","decision_blockers":["Residual opacity in per-item inclusion/exclusion logic"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.88,"w":"high","thesis":"XTracker already places Trump at 103 counted Truth Social posts in the contract window, so Yes is currently live; the only serious remaining risk is a late burst that pushes the total above 119 before noon ET.","logical_chain":["The contract resolves to XTracker's post counter unless the tracker fails.","XTracker currently shows 103 counted posts for the exact contract window.","That means the bucket is already in range and the remaining question is overshoot risk, not reach risk."],"supports":["XTracker stats for the exact April 3-April 10 window report totalBetweenStartAndEnd = 103.","Daily cumulative totals show the bucket was already reached by April 9."],"disconfirmers":["There were still about 12 hours left after the checked sync, leaving room for a late overshoot above 119.","Trump already had a 37-post day within this same window, proving upside-burst capacity."],"ambiguities":["Exact classification of edge-case replies, quote posts, and reposts in the public post output.","Whether any deleted posts were captured by XTracker but are no longer visible on secondary surfaces."],"change":"A verified XTracker move to 120+ before noon ET, or strong evidence that part of the current 103 should be excluded, would change the view."},"note_deep_dive":{"src":"assumptions/catalyst-hunter.md","text":"# Assumption\nTrump will not generate 17 or more additional counted Truth Social items between the latest checked sync and the noon ET resolution cutoff.\n## Why this assumption matters\nThe market is already inside the 100-119 bucket at 103 according to the governing tracker. The only realistic path to a No outcome is a late burst that pushes the total to 120 or higher before noon ET.\n## What this assumption supports\n- A Yes-lean probability above the market-implied 81%.\n- The claim that the most important remaining catalyst is simply Trump’s overnight and morning posting pace.\n- The judgment that no other narrative catalyst matters as much as raw intraday posting volume.\n## Evidence or logic behind the assumption\n- XTracker daily counts show the highest day in-window was 37 on April 7, but more recent daily counts were 10 on April 8 and 11 on April 9 through the last sync checked.\n- The c …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

