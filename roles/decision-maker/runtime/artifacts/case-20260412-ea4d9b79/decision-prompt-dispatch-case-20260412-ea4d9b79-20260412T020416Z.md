# Decision-Maker task | case `case-20260412-ea4d9b79`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
Do not use tools for additional research, browsing, or file reads during this decision turn. The runtime inspects the session and will fail the run if tool use occurs.

## Case
- case_key: `case-20260412-ea4d9b79`
- dispatch_id: `dispatch-case-20260412-ea4d9b79-20260412T020416Z`
- question: Will the price of Bitcoin be above $72,000 on April 12?
- market_title: Will the price of Bitcoin be above $72,000 on April 12?
- market_reference_price: 0.76

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
- Do not use tools for additional research or file inspection during this turn; the runtime will treat tool use as a policy violation.
- If the compact bundle feels too compressed, use the bounded expanded fallback below before assuming broader case access is needed.
- If the compact bundle is insufficient for a responsible decision, express that with `needs_more_research`, `needs_market_update`, `watch_only`, or `forbidden` as appropriate.
- Do not turn this stage into an unbounded second synthesis pass.

## Structured selected-input bundle for this run
```json
{"verification_mode":"not_ready_reopen_recommended","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will the price of Bitcoin be above $72,000 on April 12?","market_title":"Will the price of Bitcoin be above $72,000 on April 12?","market_reference_price":0.76,"syndicated_probability_low":0.33,"syndicated_probability_high":0.43,"syndicated_probability_midpoint":0.38,"edge_mid_vs_market_pct_points":-38.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"live assignment baseline 0.76 conflicted with fetched Polymarket 72k line around 0.36","freshness_sensitive":"yes","freshness_driver":"the exact noon ET Binance 1-minute close and late-morning BTC path","decision_blockers":["Assignment market baseline of 0.76 conflicted with live fetched Polymarket pricing near 0.36","Outcome is highly path-dependent in the final hours before noon ET","No synthesis-stage direct check of the actual resolving noon candle was possible yet"],"blockers_require_new_research":"yes","disagreement_type":"market_pricing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"strong","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"live assignment baseline 0.76 conflicted with fetched Polymarket 72k line around 0.36","verification_gap_summary":"The main remaining gap is final-hour path information into the decisive noon ET candle.","best_countercase_summary":"BTC only needed a routine sub-1% move and 72,000 was already within the recent 24h range, so a normal morning rally could still flip Yes.","main_reason_for_disagreement":"Most disagreement came from stale or mismatched market baseline inputs rather than substantive mechanism disagreement.","resolution_mechanics_summary":"Yes requires the final Close of Binance BTC/USDT’s exact 12:00 ET 1-minute candle on April 12 to be strictly above 72,000.","freshness_sensitive":"yes","freshness_driver":"the exact noon ET Binance 1-minute close and late-morning BTC path","blockers_require_new_research":"yes","disagreement_type":"market_pricing","independently_verified_points":["Polymarket rules require Binance BTC/USDT exact 12:00 ET 1-minute Close strictly above 72,000","Fetched Polymarket page showed the 72,000 line around 36% at synthesis time","Fresh Binance BTCUSDT spot during synthesis was about 71,728, still below 72,000"],"decision_blockers":["Assignment market baseline of 0.76 conflicted with live fetched Polymarket pricing near 0.36","Outcome is highly path-dependent in the final hours before noon ET"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{},"selected_persona_sidecars":[{"persona":"market-implied","p":0.32,"w":"medium","thesis":"Market pricing is broadly efficient but slightly optimistic on Yes because Binance BTC/USDT is still below 72000 and the contract requires the exact noon ET 1-minute close to finish above that threshold.","support":["Binance spot was about 71394, below the 72000 threshold."],"disconfirm":["BTC only needs a modest roughly 0.8% move to clear 72000 with many hours remaining."],"ambiguity":["How much intraday volatility will emerge before the noon ET candle."],"change":"I would move up if Binance BTC/USDT reclaims and sustains 72000+ into the morning ET window or if a clear upside catalyst emerges before set …"},{"persona":"catalyst-hunter","p":0.28,"w":"medium","thesis":"The 72k line is a plausible but still sub-even-odds threshold, and without a concrete upside catalyst before noon ET the exact Binance 1-minute close is more likely to finish below than above 72,000.","support":["Rules require the exact Binance BTC/USDT 12:00 ET 1-minute final close to be strictly above 72,000."],"disconfirm":["Only one minute close above 72,000 is needed, so ordinary crypto volatility can still flip the outcome near the threshold."],"ambiguity":["Assignment metadata showed 0.76 while the visible 72k line on the governing page showed about 0.34."],"change":"A direct upside catalyst or sustained Binance trading above 72k before the final hour would raise the estimate materially."}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.28,"w":"medium","thesis":"The 72k line is a plausible but still sub-even-odds threshold, and without a concrete upside catalyst before noon ET the exact Binance 1-minute close is more likely to finish below than above 72,000.","logical_chain":["Interpret the exact contract mechanics and source of truth.","Use the visible 72k ladder price as the market-implied baseline."],"supports":["Rules require the exact Binance BTC/USDT 12:00 ET 1-minute final close to be strictly above 72,000."],"disconfirmers":["Only one minute close above 72,000 is needed, so ordinary crypto volatility can still flip the outcome near the threshold."],"ambiguities":["Assignment metadata showed 0.76 while the visible 72k line on the governing page showed about 0.34."],"change":"A direct upside catalyst or sustained Binance trading above 72k before the final hour would raise the estimate materially."}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

