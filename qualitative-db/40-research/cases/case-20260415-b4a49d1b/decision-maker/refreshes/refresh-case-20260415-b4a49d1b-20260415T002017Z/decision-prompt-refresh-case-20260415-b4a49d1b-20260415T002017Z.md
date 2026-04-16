# Decision-Maker task | case `case-20260415-b4a49d1b`

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
- case_key: `case-20260415-b4a49d1b`
- dispatch_id: `refresh-case-20260415-b4a49d1b-20260415T002017Z`
- question: Will the price of Bitcoin be above $70,000 on April 20?
- market_title: Will the price of Bitcoin be above $70,000 on April 20?
- market_reference_price: 0.875

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.875,"last_reasoned_price":0.825,"price_delta_pct_points":5.0,"hours_since_last_forecast":0.04,"hours_to_close":135.66,"latest_forecast":{"forecast_id":"dispatch-case-20260415-b4a49d1b-20260415T000939Z","forecast_prob":0.825,"decision_ts":"2026-04-14T20:18:00-04:00","rationale_summary":"Bitcoin is likely to finish above $70,000 on the April 20 noon ET Binance minute because current same-venue pricing remains materially above the strike and no top-tier scheduled macro catalyst lands before resolution, bu …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.855,"max_reference_price":0.875,"avg_reference_price":0.8604166666666667},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.875","0.125"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $70,000 on April 20?","market_title":"Will the price of Bitcoin be above $70,000 on April 20?","market_reference_price":0.875,"syndicated_probability_low":0.8,"syndicated_probability_high":0.85,"syndicated_probability_midpoint":0.825,"edge_mid_vs_market_pct_points":-5.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Binance 1m candle/open-time implementation details are narrow but not materially outcome-changing","freshness_sensitive":"yes","freshness_driver":"Live BTC cushion versus 70000 can change materially before the Apr 20 noon ET settlement minute.","decision_blockers":["No fully independent short-horizon volatility model for the exact settlement-minute condition","Edge versus market is modest and partly rests on judgment about path-risk discounting"],"blockers_require_new_research":"no","disagreement_type":"interpretation","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Binance 1m candle/open-time implementation details are narrow but not materially outcome-changing","verification_gap_summary":"No independent volatility-based estimate was built for odds of a >6% downside move by the exact settlement minute.","best_countercase_summary":"A normal crypto drawdown or localized Binance noon-minute dip could still push the exact close below 70k despite current cushion.","main_reason_for_disagreement":"Different weighting of narrow timestamp/path risk versus current spot cushion and lack of scheduled catalysts.","resolution_mechanics_summary":"Yes requires the Binance BTC/USDT 12:00 ET Apr 20 one-minute candle final close to be strictly above 70000.","freshness_sensitive":"yes","freshness_driver":"Live BTC cushion versus 70000 can change materially before the Apr 20 noon ET settlement minute.","blockers_require_new_research":"no","disagreement_type":"interpretation","independently_verified_points":["Binance BTCUSDT spot remained around 74.5k during synthesis-stage check","Fed calendar shows next 2026 FOMC meeting is Apr 28-29, after resolution","BLS CPI schedule shows March 2026 CPI was released Apr 10, before resolution"],"decision_blockers":["No fully independent short-horizon volatility model for the exact settlement-minute condition","Edge versus market is modest and partly rests on judgment about path-risk discounting"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBTC being above 70,000 on the April 20 Polymarket contract remains more likely than not, but the best post-synthesis read is slightly below the market’s 0.86 implied probability because the contract resolves on one exact Binance BTC/USDT 12:00 ET 1-minute close and the independent truth-finding pass mostly confirmed current cushion and catalyst absence rather than proving that a sub-70k print is remote.\n\n## Why this may matter now\n\nMarket implies 0.86. My final syndicated range is 0.80-0.85. That makes the edge versus market marginal-to-modest and probably not robust enough to call strong alpha. The likely mispricing, if any, is that the market may still be a bit too comf …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.82,"w":"medium","thesis":"The market's 86% Yes price is broadly justified by BTC trading well above 70k, but I discount slightly for narrow timestamp risk and normal five-day crypto volatility.","support":["Binance BTCUSDT spot during research was around 74.5k, materially above the 70k threshold."],"disconfirm":["The contract settles on one exact one-minute close, so a >6% downside move before noon ET April 20 is enough to flip the result."],"ambiguity":["Whether realized volatility between now and April 20 is low enough to fully justify an 86% price rather than a slightly lower one."],"change":"I would cut the estimate if BTC loses most of its cushion toward 70k, if downside volatility spikes, or if Binance-specific issues emerge; I …"},{"persona":"variant-view","p":0.78,"w":"medium","thesis":"Yes remains more likely than No, but the market likely overprices confidence because this resolves on one exact Binance BTC/USDT 1-minute close at noon ET and current cushion above 70k is meaningful but not huge for BTC …","support":["Direct Binance checks during the run showed BTC/USDT around 74.6k, above 70k."],"disconfirm":["Even the recent 24-hour Binance low remained above 70k, which supports the market's high Yes probability."],"ambiguity":["Operational details of the exact Binance display surface at settlement are narrow but not materially ambiguous after the rule/API check."],"change":"I would move toward or above market if BTC retains a large cushion above 70k with declining volatility into April 20, and more bearish if BT …"},{"persona":"catalyst-hunter","p":0.89,"w":"medium","thesis":"BTC is already materially above 70,000 on the named Binance venue, and with no obvious top-tier scheduled macro catalyst left before Apr 20 noon ET, the most likely path is simply staying above the threshold unless an un …","support":["Binance BTC/USDT was around 74.5k during the run, roughly 6% above the 70k threshold."],"disconfirm":["The contract settles on one exact Binance 12:00 ET 1-minute close, so a localized dip below 70k is enough for No."],"ambiguity":["Whether noon ET specifically could coincide with localized liquidity weakness on Binance."],"change":"A decisive break below 72k on Binance, a new risk-off macro/geopolitical shock, or evidence of Binance-specific operational/pricing instabil …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Live BTC cushion versus 70000 can change materially before the Apr 20 noon ET settlement minute.?","How decision-relevant is the remaining contract/source-of-truth ambiguity: Binance 1m candle/open-time implementation details are narrow but not materially outcome-changing?","Are the current blockers still material to final judgment: No fully independent short-horizon volatility model for the exact settlement-minute condition?","Is the main verification gap still decision-material: No independent volatility-based estimate was built for odds of a >6% downside move by the exact settlement minute.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"No independent volatility-based estimate was built for odds of a >6% downside move by the exact settlement minute.","best_countercase_summary":"A normal crypto drawdown or localized Binance noon-minute dip could still push the exact close below 70k despite current cushion.","freshness_sensitive":"yes","freshness_driver":"Live BTC cushion versus 70000 can change materially before the Apr 20 noon ET settlement minute.","decision_blockers":["No fully independent short-horizon volatility model for the exact settlement-minute condition","Edge versus market is modest and partly rests on judgment about path-risk discounting"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.89,"w":"medium","thesis":"BTC is already materially above 70,000 on the named Binance venue, and with no obvious top-tier scheduled macro catalyst left before Apr 20 noon ET, the most likely path is simply staying above the threshold unless an unscheduled downside shock hits.","logical_chain":["Check the contract mechanics and confirm the governing source is Binance BTC/USDT 12:00 ET 1-minute close above 70,000.","Verify that current Binance spot is materially above 70,000 and recent closes have mostly held above that threshold.","Check whether any top-tier scheduled macro catalyst remains before resolution; official calendars suggest not."],"supports":["Binance BTC/USDT was around 74.5k during the run, roughly 6% above the 70k threshold.","Recent Binance daily closes in the sampled output were above 70k for Apr 10-14."],"disconfirmers":["The contract settles on one exact Binance 12:00 ET 1-minute close, so a localized dip below 70k is enough for No.","A 6% BTC move over five days is plausible in crypto."],"ambiguities":["Whether noon ET specifically could coincide with localized liquidity weakness on Binance.","Whether any missed or unscheduled catalyst emerges before Apr 20."],"change":"A decisive break below 72k on Binance, a new risk-off macro/geopolitical shock, or evidence of Binance-specific operational/pricing instability would lower the estimate."}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

