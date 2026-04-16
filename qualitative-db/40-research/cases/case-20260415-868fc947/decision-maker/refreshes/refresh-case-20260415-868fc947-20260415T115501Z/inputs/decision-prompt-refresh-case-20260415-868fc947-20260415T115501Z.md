# Decision-Maker task | case `case-20260415-868fc947`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Important: the runtime hydrates many metadata / execution / risk / audit defaults after parsing. Focus your output effort on judgment-bearing fields rather than boilerplate runtime-owned fields.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
Do not use tools for additional research, browsing, or file reads during this decision turn. The runtime inspects the session and will fail the run if tool use occurs.

## Case
- case_key: `case-20260415-868fc947`
- dispatch_id: `refresh-case-20260415-868fc947-20260415T115501Z`
- question: Will the price of Bitcoin be above $72,000 on April 16?
- market_title: Will the price of Bitcoin be above $72,000 on April 16?
- market_reference_price: 0.885

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.885,"last_reasoned_price":0.83,"price_delta_pct_points":5.5,"hours_since_last_forecast":2.77,"hours_to_close":28.08,"latest_forecast":{"forecast_id":"dispatch-case-20260415-868fc947-20260415T090047Z","forecast_prob":0.83,"decision_ts":"2026-04-15T05:09:00-04:00","rationale_summary":"BTC is still more likely than not to finish above $72,000 on the April 16 Binance noon minute, but with fair value centered near 0.83 and the market at 0.875, the disciplined output remains watch-only because exact-minut …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.865,"max_reference_price":0.885,"avg_reference_price":0.8683333333333333},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.885","0.115"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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

Return a single JSON object.

The final persisted decision packet will contain these keys:
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

Important runtime behavior:
- the runtime deterministically hydrates / overrides many metadata and policy fields after your response is parsed
- you do **not** need to spend tokens recreating runtime-owned metadata perfectly
- it is acceptable to keep runtime-owned sections minimal when you have no meaningful override to provide

## Critical enums

- `decision.side`: `yes | no | none`
- `decision.trade_authorization`: `authorized | watch_only | risk_reduce_only | forbidden`
- `decision.position_policy`: `enter_or_add | hold_only | reduce_only | exit_only | flat`
- `decision.decision_readiness`: `ready | needs_more_research | needs_market_update`
- `decision.thesis_class`: `edge_present | edge_too_small | price_not_good_enough | not_decision_ready | risk_constraint_binding`
- `execution_semantics.price_source`: `market_snapshot_quote | effective_executable_quote`
- quality enums: `low | medium | high`
- `epistemic_status.decision_quality`: `clean | good_not_clean | fragile | not_ready`

## Minimum model-owned fields by section

### context
Focus on the judgment-bearing identifiers only:
`case_key`, `dispatch_id`, `question`

The runtime will fill market identifiers, canonical output paths, source artifact paths, and agent metadata.

### decision
These are the most important fields to get right:
`side`, `trade_authorization`, `position_policy`, `decision_readiness`, `primary_crux`

Useful when available:
`secondary_cruxes`, `thesis_class`

### valuation
Model-owned core valuation fields:
`fair_value_low`, `fair_value_high`

Helpful when you have a clean estimate:
`fair_value_mid`, `independent_verification_quality`, `compressed_toward_market_applied`, `compression_reason`

The runtime will fill / normalize `market_reference_price` and recompute `edge_mid_vs_market_pct_points`.

### execution_semantics
You may keep this section minimal unless you have a meaningful override.
The runtime will enforce / hydrate:
- `price_axis = market_implied_true_prob`
- `price_source`
- `rebalance_threshold_fraction`
- `allow_auto_reversal`
- `valid_until`
- `quote_staleness_seconds`

### risk_controls
You may keep this section minimal unless you have a meaningful override.
The runtime hydrates default bankroll/risk fields and confidence metadata.

### bands
If you have a deliberate exposure schedule, return all five canonical bands with `name`, `min_p`, `max_p`, `target_exposure_fraction`, `notes`.
Otherwise the runtime can hydrate a deterministic default band shape from your chosen side.

### invalidation
Provide concise lists for:
`thesis_breakers`, `time_breakers`

Useful when available:
`market_structure_breakers`, `reversal_conditions`

### epistemic_status
Prefer concise lists for:
`key_uncertainties`, `what_would_change_my_mind`

Useful when available:
`reasons_to_pass`, `decision_quality`

### audit
Model-owned must-have:
`one_sentence_rationale`

Helpful when available:
`notes`

The runtime hydrates most audit booleans and verification bookkeeping.

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
{"verification_mode":"not_ready_reopen_recommended","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will the price of Bitcoin be above $72,000 on April 16?","market_title":"Will the price of Bitcoin be above $72,000 on April 16?","market_reference_price":0.885,"syndicated_probability_low":0.8,"syndicated_probability_high":0.86,"syndicated_probability_midpoint":0.83,"edge_mid_vs_market_pct_points":-5.5,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"mild Binance UI-versus-API implementation ambiguity despite otherwise clear venue/time/close rules","freshness_sensitive":"yes","freshness_driver":"Binance BTC/USDT price path and minute-level volatility into the Apr. 16 12:00 ET settlement window","decision_blockers":["Freshness risk: a one-day crypto contract can reprice materially before settlement","Exact-minute Binance wick/path dependence is still not independently quantified","No stronger volatility-based verification beyond spot/candle checks was added at synthesis stage"],"blockers_require_new_research":"yes","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"mild Binance UI-versus-API implementation ambiguity despite otherwise clear venue/time/close rules","verification_gap_summary":"The main unresolved gap is how much downside volatility or wick risk arrives in the final pre-settlement hours.","best_countercase_summary":"BTC is already >$2k above the strike and recent Binance lows stayed above 72k, so the market’s high-Yes pricing may simply be correct.","main_reason_for_disagreement":"Different weighting of exact-minute path risk versus the current cushion above 72k.","resolution_mechanics_summary":"Yes resolves only if the Binance BTC/USDT 1-minute candle at Apr. 16 12:00 ET closes strictly above 72,000.","freshness_sensitive":"yes","freshness_driver":"Binance BTC/USDT price path and minute-level volatility into the Apr. 16 12:00 ET settlement window","blockers_require_new_research":"yes","disagreement_type":"timing","independently_verified_points":["Binance BTC/USDT remains the governing settlement venue and pair","Resolution is the Apr. 16 12:00 ET Binance 1-minute candle close, equivalent to 16:00 UTC","Current Binance spot is around 74.03k, leaving roughly a 2.0k cushion above 72k"],"decision_blockers":["Freshness risk: a one-day crypto contract can reprice materially before settlement","Exact-minute Binance wick/path dependence is still not independently quantified"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{},"selected_persona_sidecars":[{"persona":"market-implied","p":0.84,"w":"high","thesis":"Market's high-Yes view is broadly justified by Binance BTC/USDT trading around 74.1k, but the exact noon ET 1-minute close condition makes 87.5% slightly too aggressive; estimate 84% Yes.","support":["Binance BTCUSDT spot and recent candles were around 74.1k during the run"],"disconfirm":["The contract settles on one exact Binance 1-minute close at 12:00 ET, so normal BTC volatility could still flip the result"],"ambiguity":["How much normal BTC intraday volatility should discount a high current spot cushion in this exact-minute format"],"change":"A move back toward or below 73k, a material negative catalyst before noon ET, or Binance-specific weakness would make the view more bearish; …"},{"persona":"risk-manager","p":0.78,"w":"medium","thesis":"BTC is currently above 72k on Binance, so Yes is favored, but the market is too confident for a one-minute tomorrow settlement and timing risk is underpriced.","support":["Binance spot was around 74,034 at review time, roughly 2,034 above strike."],"disconfirm":["The market resolves on one exact Binance 1m close tomorrow, not on broad daily price conditions."],"ambiguity":["How much intraday volatility arrives before 2026-04-16 16:00 UTC."],"change":"I would move toward market if a later verification closer to resolution still showed a comfortable cushion with subdued volatility; I would …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.84,"w":"high","thesis":"Market's high-Yes view is broadly justified by Binance BTC/USDT trading around 74.1k, but the exact noon ET 1-minute close condition makes 87.5% slightly too aggressive; estimate 84% Yes.","logical_chain":["Start from the live 87.5% market prior and verify the exact contract mechanics","Check Binance, the settlement venue, and confirm BTC is currently trading materially above 72k","Perform an extra contextual verification pass with CoinGecko and recent Binance history"],"supports":["Binance BTCUSDT spot and recent candles were around 74.1k during the run","Polymarket market price and order book centered near 87.5% Yes"],"disconfirmers":["The contract settles on one exact Binance 1-minute close at 12:00 ET, so normal BTC volatility could still flip the result","A ~2.1k cushion is meaningful but not huge on a one-day Bitcoin horizon"],"ambiguities":["How much normal BTC intraday volatility should discount a high current spot cushion in this exact-minute format"],"change":"A move back toward or below 73k, a material negative catalyst before noon ET, or Binance-specific weakness would make the view more bearish; sustained stability above 74k into sett …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

