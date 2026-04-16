# Decision-Maker task | case `case-20260415-0c8ac7fd`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Important: the runtime hydrates many metadata / execution / risk / audit defaults after parsing. Focus your output effort on judgment-bearing fields rather than boilerplate runtime-owned fields.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
You may use only web_search, web_fetch in this turn.
Stay within: searches<=5, fetches<=3, min_distinct_source_families=2 when feasible.
Choose sources independently and prefer primary, official, and resolution-relevant sources.
Do not count multiple pages from the same source family as real diversity.

## Case
- case_key: `case-20260415-0c8ac7fd`
- dispatch_id: `refresh-case-20260415-0c8ac7fd-20260415T194458Z`
- question: Will the price of Bitcoin be above $72,000 on April 17?
- market_title: Will the price of Bitcoin be above $72,000 on April 17?
- market_reference_price: 0.925

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.925,"last_reasoned_price":0.845,"price_delta_pct_points":8.0,"hours_since_last_forecast":0.05,"hours_to_close":44.25,"latest_forecast":{"forecast_id":"refresh-case-20260415-0c8ac7fd-20260415T194223Z","forecast_prob":0.845,"decision_ts":"2026-04-15T15:42:00-04:00","rationale_summary":"BTC is still more likely than not by a wide margin to finish above $72,000 on the April 17 Binance noon minute, but the market's move to 0.895 pushes price above fair value centered near 0.845, so the disciplined output …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.89,"max_reference_price":0.925,"avg_reference_price":0.8933333333333333},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.91","0.09"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
- In `targeted_escalation`, independent tool-enabled verification is allowed, but source choice remains your responsibility and budgets remain runtime-enforced.
- If the compact bundle feels too compressed, use the bounded expanded fallback below before assuming broader case access is needed.
- If the compact bundle is insufficient for a responsible decision, express that with `needs_more_research`, `needs_market_update`, `watch_only`, or `forbidden` as appropriate.
- Do not turn this stage into an unbounded second synthesis pass.

## Structured selected-input bundle for this run
```json
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $72,000 on April 17?","market_title":"Will the price of Bitcoin be above $72,000 on April 17?","market_reference_price":0.925,"syndicated_probability_low":0.82,"syndicated_probability_high":0.87,"syndicated_probability_midpoint":0.845,"edge_mid_vs_market_pct_points":-8.0,"relation_to_market":"crosses_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small Binance UI-versus-API verification gap before final resolving candle exists","freshness_sensitive":"yes","freshness_driver":"Binance BTC/USDT price path into the exact Apr 17 12:00 ET resolving minute","decision_blockers":["Outcome depends on one future exact-minute Binance close that has not yet occurred","Independent verification of the apparent market-vs-swarm gap is only moderate because evidence is concentrated in Binance/Polymarket source family","A sharp crypto selloff before noon ET Apr 17 could erase the current cushion quickly"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"unclear","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small Binance UI-versus-API verification gap before final resolving candle exists","verification_gap_summary":"No independent estimate strongly quantified the odds of a 3% to 4% selloff into the exact resolving minute.","best_countercase_summary":"Current cushion is large enough that ordinary short-horizon BTC noise may still leave the noon close above 72000, making market pricing fair or slightly cheap.","main_reason_for_disagreement":"How much exact-minute path risk should discount a currently comfortable cushion above strike.","resolution_mechanics_summary":"Yes resolves only if the Binance BTC/USDT 12:00 ET Apr 17 one-minute candle final close is strictly above 72000.","freshness_sensitive":"yes","freshness_driver":"Binance BTC/USDT price path into the exact Apr 17 12:00 ET resolving minute","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket rules explicitly resolve from Binance BTC/USDT 1-minute 12:00 ET candle close","Current Binance BTCUSDT spot remained materially above 72000 during synthesis-stage check","Recent Binance 1-minute closes remained clustered well above 72000"],"decision_blockers":["Outcome depends on one future exact-minute Binance close that has not yet occurred","Independent verification of the apparent market-vs-swarm gap is only moderate because evidence is concentrated in Binance/Polymarket source …"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBTC being above 72,000 on the relevant Apr 17 Binance noon ET 1-minute close still looks more likely than not by a wide margin, but the market’s 0.87 Yes price already captures most of that advantage; the residual edge appears small-to-negative after accounting for exact-minute close risk and limited independent verification beyond the same governing source family.\n\n## Why this may matter now\n\nMarket-implied probability is 0.87. My syndicated range is 0.82 to 0.87. That makes the edge unclear to marginal and slightly negative versus market after synthesis. The likely mispricing, if any, is that some traders may treat this as a broad BTC-above-threshold bet rather than a s …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.84,"w":"high","thesis":"The market's 0.87 Yes price is broadly justified because Binance BTC/USDT is already trading materially above 72000, though exact-minute close mechanics justify a modest discount from near-certainty.","support":["Direct Binance ticker check showed BTCUSDT at 74646.66 during the run."],"disconfirm":["This is a specific-minute close market, not a touch market, so a selloff into the exact noon ET minute could still produce No."],"ambiguity":["Exact final UI-state proof cannot be captured yet because the resolving candle is still in the future."],"change":"I would mark down Yes materially if Binance BTCUSDT trades near or below 72000 before the deadline or if clearer source-surface interpretati …"},{"persona":"catalyst-hunter","p":0.91,"w":"high","thesis":"BTC is already trading materially above 72,000 on Binance, so this market is more about preserving cushion into the Apr 17 noon ET close than needing a new upside catalyst.","support":["Direct Binance ticker check showed BTCUSDT at 74,704."],"disconfirm":["This is a specific Apr 17 12:00 ET one-minute close, not a touch market."],"ambiguity":["No strong independent macro-news catalyst source was obtained in this run due fetch limits."],"change":"A decisive Binance move back toward or below 72k before the Apr 17 noon ET close, or new evidence of unusual fixing-minute/operational risk, …"},{"persona":"risk-manager","p":0.82,"w":"medium","thesis":"BTC is currently comfortably above 72000 on Binance, so Yes is favored, but the market is slightly overconfident because settlement depends on one exact Binance BTC/USDT 12:00 ET 1-minute close on April 17.","support":["Recent Binance 1-minute closes were around 74.6k-74.7k, leaving a meaningful cushion above 72k."],"disconfirm":["This is a precise timestamp close market, so a sharp selloff into the exact noon ET minute can still produce No."],"ambiguity":["No major rule ambiguity remains; the main uncertainty is future price path into settlement."],"change":"A fresh check closer to settlement showing BTC still comfortably above 74k would move me toward market; a selloff back toward or below 72k, …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Binance BTC/USDT price path into the exact Apr 17 12:00 ET resolving minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: small Binance UI-versus-API verification gap before final resolving candle exists?","Are the current blockers still material to final judgment: Outcome depends on one future exact-minute Binance close that has not yet occurred?","Is the main verification gap still decision-material: No independent estimate strongly quantified the odds of a 3% to 4% selloff into the exact resolving minute.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"No independent estimate strongly quantified the odds of a 3% to 4% selloff into the exact resolving minute.","best_countercase_summary":"Current cushion is large enough that ordinary short-horizon BTC noise may still leave the noon close above 72000, making market pricing fair or slightly cheap.","freshness_sensitive":"yes","freshness_driver":"Binance BTC/USDT price path into the exact Apr 17 12:00 ET resolving minute","decision_blockers":["Outcome depends on one future exact-minute Binance close that has not yet occurred","Independent verification of the apparent market-vs-swarm gap is only moderate because evidence is concentrated in Binance/Polymarket source …"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.91,"w":"high","thesis":"BTC is already trading materially above 72,000 on Binance, so this market is more about preserving cushion into the Apr 17 noon ET close than needing a new upside catalyst.","logical_chain":["The contract resolves on the Binance BTC/USDT 12:00 ET one-minute close on Apr 17.","BTC is currently around 74.7k on Binance, materially above the 72k threshold.","That leaves a meaningful cushion, so absent a negative shock the default path favors Yes."],"supports":["Direct Binance ticker check showed BTCUSDT at 74,704.","Recent Binance 1-minute klines were clustered in the mid-74k range."],"disconfirmers":["This is a specific Apr 17 12:00 ET one-minute close, not a touch market.","BTC can move several percent in 48 hours on macro or crypto-specific shocks."],"ambiguities":["No strong independent macro-news catalyst source was obtained in this run due fetch limits.","Need rerun-time confirmation if BTC compresses close to 72k before settlement."],"change":"A decisive Binance move back toward or below 72k before the Apr 17 noon ET close, or new evidence of unusual fixing-minute/operational risk, would cut the estimate materially."}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

