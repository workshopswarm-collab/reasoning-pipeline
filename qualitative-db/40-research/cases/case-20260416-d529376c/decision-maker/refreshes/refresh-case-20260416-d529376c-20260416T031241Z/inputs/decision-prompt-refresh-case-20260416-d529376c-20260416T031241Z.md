# Decision-Maker task | case `case-20260416-d529376c`

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
- case_key: `case-20260416-d529376c`
- dispatch_id: `refresh-case-20260416-d529376c-20260416T031241Z`
- question: Will the price of Solana be above $80 on April 19?
- market_title: Will the price of Solana be above $80 on April 19?
- market_reference_price: 0.92

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.92,"last_reasoned_price":0.85,"price_delta_pct_points":7.0,"hours_since_last_forecast":0.01,"hours_to_close":84.79,"latest_forecast":{"forecast_id":"dispatch-case-20260416-d529376c-20260416T030247Z","forecast_prob":0.85,"decision_ts":"2026-04-15T23:12:00-04:00","rationale_summary":"SOL above $80 on April 19 is still the directional base case, but because this bounded package explicitly requires more research on volatility calibration and near-settlement confirmation, the correct output is forbidden …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.89,"max_reference_price":0.92,"avg_reference_price":0.8979166666666667},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.92","0.08"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"not_ready_reopen_recommended","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will the price of Solana be above $80 on April 19?","market_title":"Will the price of Solana be above $80 on April 19?","market_reference_price":0.92,"syndicated_probability_low":0.82,"syndicated_probability_high":0.88,"syndicated_probability_midpoint":0.85,"edge_mid_vs_market_pct_points":-7.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"minor implementation risk around exact Binance ET-noon minute/UI-vs-API mapping, though core rules are clear","freshness_sensitive":"yes","freshness_driver":"SOL distance from 80 and any crypto-wide risk-off move before the Apr 19 12:00 ET settlement minute","decision_blockers":["Single-minute settlement makes ordinary path volatility more important than current spot","Independent verification of the large below-market edge is only medium strength","Final confidence is highly sensitive to a fresh Binance check closer to settlement"],"blockers_require_new_research":"yes","disagreement_type":"market_pricing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"minor implementation risk around exact Binance ET-noon minute/UI-vs-API mapping, though core rules are clear","verification_gap_summary":"The main remaining gap is direct empirical calibration of downside probability for the exact settlement minute over the next ~3 days.","best_countercase_summary":"A normal crypto selloff or brief wick into the exact noon ET minute could still push SOL below 80 despite current mid-85s spot.","main_reason_for_disagreement":"The main disagreement is volatility calibration for a single-minute settlement given a roughly 6% cushion above strike.","resolution_mechanics_summary":"Yes resolves only if the Binance SOL/USDT 12:00 ET one-minute candle on April 19 closes strictly above 80.","freshness_sensitive":"yes","freshness_driver":"SOL distance from 80 and any crypto-wide risk-off move before the Apr 19 12:00 ET settlement minute","blockers_require_new_research":"yes","disagreement_type":"market_pricing","independently_verified_points":["Polymarket rules specify Binance SOL/USDT 12:00 ET one-minute close with strict greater-than-80 condition","Direct Binance spot remained around 85.2 at synthesis time","Direct Binance recent one-minute data still showed SOL trading in the mid-85s"],"decision_blockers":["Single-minute settlement makes ordinary path volatility more important than current spot","Independent verification of the large below-market edge is only medium strength"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{},"selected_persona_sidecars":[{"persona":"market-implied","p":0.86,"w":"high","thesis":"The market is directionally right because Binance already has SOL materially above 80, but exact-minute settlement and normal crypto volatility justify a modest haircut versus the 91.5% market price.","support":["Direct Binance SOL/USDT read was about 85.27, already roughly $5.27 above strike."],"disconfirm":["A ~6% drawdown over several days is plausible in crypto."],"ambiguity":["How much realized volatility SOL will see between now and April 19."],"change":"I would move lower if SOL loses the 82-83 area or if a fresh Binance check near expiry shows the cushion over 80 has mostly vanished; I woul …"},{"persona":"base-rate","p":0.68,"w":"medium","thesis":"Yes is more likely than No because recent Binance SOL/USDT trading has mostly been above $80, but the market's 91.5% price overstates confidence for a single-minute noon ET threshold contract.","support":["Binance daily closes were above $80 on 13 of 15 completed days in the Apr 1-15 sample."],"disconfirm":["The contract resolves on one exact 12:00 ET one-minute close, so timing noise matters more than daily-level intuition."],"ambiguity":["Exact Binance UI candle labeling at the ET noon mapping was not independently verified beyond the contract rules."],"change":"I would move up if SOL carries a larger cushion above $80 near settlement or if direct intraday noon-window evidence shows limited downside …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.86,"w":"high","thesis":"The market is directionally right because Binance already has SOL materially above 80, but exact-minute settlement and normal crypto volatility justify a modest haircut versus the 91.5% market price.","logical_chain":["Start from the 91.5% market-implied prior.","Check the governing venue and contract mechanics directly on Binance / Polymarket rules.","Observe that SOL is already comfortably above 80, so persistence is the main requirement."],"supports":["Direct Binance SOL/USDT read was about 85.27, already roughly $5.27 above strike.","Recent Binance 1-minute closes were clustered in the mid-85s rather than barely above 80."],"disconfirmers":["A ~6% drawdown over several days is plausible in crypto.","The contract settles on one exact 1-minute Binance close, not a daily average."],"ambiguities":["How much realized volatility SOL will see between now and April 19.","Whether any weekend-style or event-driven move hits the exact settlement minute."],"change":"I would move lower if SOL loses the 82-83 area or if a fresh Binance check near expiry shows the cushion over 80 has mostly vanished; I would move toward the market if SOL remains …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

