# Decision-Maker task | case `case-20260413-9dc5221c`

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
- case_key: `case-20260413-9dc5221c`
- dispatch_id: `refresh-case-20260413-9dc5221c-20260413T193340Z`
- question: Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?
- market_title: Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?
- market_reference_price: 0.9905

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.9905,"last_reasoned_price":0.925,"price_delta_pct_points":6.6,"hours_since_last_forecast":0.31,"hours_to_close":76.44,"latest_forecast":{"forecast_id":"dispatch-case-20260413-9dc5221c-20260413T190728Z","forecast_prob":0.925,"decision_ts":"2026-04-13T15:15:00-04:00","rationale_summary":"Sindarov still looks very likely to win because credible late-stage reporting says he leads by two points with two rounds left and has at least a playoff guaranteed, but without a clean official FIDE standings capture th …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.8935,"max_reference_price":0.9905,"avg_reference_price":0.9317916666666667},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.9905","0.0095"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
```

Use this brief as a bounded update layer on top of the prior synthesis package. Do not rerun broad synthesis mentally unless the refresh brief indicates a true regime change.

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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?","market_title":"Will Javokhir Sindarov win the 2026 FIDE Candidates Tournament?","market_reference_price":0.9905,"syndicated_probability_low":0.89,"syndicated_probability_high":0.94,"syndicated_probability_midpoint":0.915,"edge_mid_vs_market_pct_points":-7.6,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"official winner not yet declared; current confidence relies partly on contextual live-standings reporting rather than a clean official standings capture","freshness_sensitive":"yes","freshness_driver":"Round 13 and any official FIDE standings/result update can move the probability materially.","decision_blockers":["No clean official FIDE standings/clinch page was captured directly in the synthesis pass","The tournament was not yet officially finished at analysis time"],"blockers_require_new_research":"no","disagreement_type":"mixed","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"official winner not yet declared; current confidence relies partly on contextual live-standings reporting rather than a clean official standings capture","verification_gap_summary":"I did not obtain a clean official FIDE live standings or clinch page directly in the synthesis pass.","best_countercase_summary":"If the live-state interpretation is overstated or Sindarov loses round 13, the race can reopen quickly and 95% was too high.","main_reason_for_disagreement":"Different weighting of missing direct official standings verification versus strong contextual late-stage lead evidence.","resolution_mechanics_summary":"Resolve to the official FIDE-declared winner, with consensus credible reporting only as fallback.","freshness_sensitive":"yes","freshness_driver":"Round 13 and any official FIDE standings/result update can move the probability materially.","blockers_require_new_research":"no","disagreement_type":"mixed","independently_verified_points":["FIDE is the governing resolution source","Sindarov was reported two points clear after round 12 with two rounds left","Chess.com reported Sindarov was guaranteed at least a playoff"],"decision_blockers":["No clean official FIDE standings/clinch page was captured directly in the synthesis pass","The tournament was not yet officially finished at analysis time"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nJavokhir Sindarov is very likely to win the 2026 FIDE Candidates Tournament, but the best post-synthesis estimate is still slightly below the 95.05% market because the strongest independently checked evidence supports an overwhelming late lead rather than a fully settled official result.\n\n## Why this may matter now\n\nMarket-implied probability is 0.9505. My syndicated range is 0.89 to 0.94. That is still a strong yes view, but the edge versus market is marginal-to-negative rather than actionable. The market may be a touch rich because it is pricing a near-converted lead almost like an already-declared win.\n\n## Shift versus swarm baseline\n\nThis is not a large move from the …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.91,"w":"medium","thesis":"The market is directionally right because Sindarov appears to have an almost decisive late-stage lead, but 95.05% is slightly too high given residual two-round, tiebreak, and official-live-verification risk.","support":["Contextual live standings show Sindarov leading by two points with two rounds left."],"disconfirm":["Two rounds plus possible tie-breaks still leave a nonzero failure path."],"ambiguity":["Exact official live standings were not directly captured from a clean FIDE page in this run."],"change":"A clean official FIDE standings/result update showing a smaller lead, a round-13 stumble, or any procedural dispute would push the estimate …"},{"persona":"risk-manager","p":0.58,"w":"medium","thesis":"Sindarov is a real contender, but the visible evidence does not justify the market's 95.05% near-certainty absent hidden live-state context.","support":["FIDE officially lists Sindarov in the 2026 Candidates field and as 2025 World Cup winner."],"disconfirm":["The same FIDE page shows a full elite eight-player double round-robin, which is hard to square with 95% for one player absent hidden context …"],"ambiguity":["Whether the market snapshot reflects late-event state not visible in fetched sources."],"change":"Official FIDE standings showing Sindarov with a commanding late lead, rival ineligibility, or strong independent odds near 95% would move me …"},{"persona":"variant-view","p":0.92,"w":"medium","thesis":"Sindarov is very likely to win, but the market is slightly overconfident because the tournament is not yet officially settled and residual tiebreak/admin tails still exist.","support":["Contextual standings show Sindarov leading 9/12 by two points with two rounds left."],"disconfirm":["A two-point lead with two rounds left in this format may make 95% entirely fair or even slightly low if standings are accurate."],"ambiguity":["Exact official live standings/tiebreak math were not reconstructed from a primary FIDE event page."],"change":"An official FIDE confirmation that Sindarov has clinched or clean official standings with no complications would push the estimate up; contr …"}],"selected_assumption_snippets":[{"src":"assumptions/risk-manager.md","text":"# Assumption\nThe market's 95.05% price is implicitly assuming either that Javokhir Sindarov is an overwhelming pre-tournament favorite versus seven elite qualifiers or that substantial contract/listing context outside the visible rules makes his victory close to settled.\n## Why this assumption matters\nWithout that assumption, a pre-event price above 95% in an eight-player double round-robin is extremely hard to justify. The whole risk-manager view turns on whether this confidence comes from real …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Round 13 and any official FIDE standings/result update can move the probability materially.?","How decision-relevant is the remaining contract/source-of-truth ambiguity: official winner not yet declared; current confidence relies partly on contextual live-standings reporting rather than a clean official standings capture?","Are the current blockers still material to final judgment: No clean official FIDE standings/clinch page was captured directly in the synthesis pass?","Is the main verification gap still decision-material: I did not obtain a clean official FIDE live standings or clinch page directly in the synthesis pass.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"I did not obtain a clean official FIDE live standings or clinch page directly in the synthesis pass.","best_countercase_summary":"If the live-state interpretation is overstated or Sindarov loses round 13, the race can reopen quickly and 95% was too high.","freshness_sensitive":"yes","freshness_driver":"Round 13 and any official FIDE standings/result update can move the probability materially.","decision_blockers":["No clean official FIDE standings/clinch page was captured directly in the synthesis pass","The tournament was not yet officially finished at analysis time"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"variant-view","p":0.92,"w":"medium","thesis":"Sindarov is very likely to win, but the market is slightly overconfident because the tournament is not yet officially settled and residual tiebreak/admin tails still exist.","logical_chain":["The contract resolves on an actual FIDE-declared winner, not merely on a dominant in-progress position.","Secondary sources indicate Sindarov is in a hugely favorable late-stage position.","Because two rounds and possible tiebreaks still remain, residual competitive and administrative tails are not zero."],"supports":["Contextual standings show Sindarov leading 9/12 by two points with two rounds left.","Chess.com round-12 coverage says he is guaranteed at least a playoff."],"disconfirmers":["A two-point lead with two rounds left in this format may make 95% entirely fair or even slightly low if standings are accurate.","The bearish case is mostly about tail-risk pricing rather than a plausible mainline loss narrative."],"ambiguities":["Exact official live standings/tiebreak math were not reconstructed from a primary FIDE event page.","Low-probability off-board complications remain hard to rule out completely."],"change":"An official FIDE confirmation that Sindarov has clinched or clean official standings with no complications would push the estimate up; contradictory official reporting or a sharply …"},"note_deep_dive":{"src":"assumptions/risk-manager.md","text":"# Assumption\nThe market's 95.05% price is implicitly assuming either that Javokhir Sindarov is an overwhelming pre-tournament favorite versus seven elite qualifiers or that substantial contract/listing context outside the visible rules makes his victory close to settled.\n## Why this assumption matters\nWithout that assumption, a pre-event price above 95% in an eight-player double round-robin is extremely hard to justify. The whole risk-manager view turns on whether this confidence comes from real hidden information or from market mispricing / market-structure distortion.\n## What this assumption supports\n- A view that the displayed market price is likely too confident.\n- A probability estimate materially below the market-implied baseline.\n- Elevated concern about hidden assumptions, field-strength underweighting, or book-structure issues.\n## Evidence or logic behind the assumption\n- Offici …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

