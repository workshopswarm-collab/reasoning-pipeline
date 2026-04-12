# Decision-Maker task | case `case-20260411-6669dcdb`

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
- case_key: `case-20260411-6669dcdb`
- dispatch_id: `dispatch-case-20260411-6669dcdb-20260411T003353Z`
- question: Will the price of Bitcoin be above $72,000 on April 11?
- market_title: Will the price of Bitcoin be above $72,000 on April 11?
- market_reference_price: 0.7125

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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will the price of Bitcoin be above $72,000 on April 11?","market_title":"Will the price of Bitcoin be above $72,000 on April 11?","market_reference_price":0.7125,"syndicated_probability_low":0.77,"syndicated_probability_high":0.84,"syndicated_probability_midpoint":0.805,"edge_mid_vs_market_pct_points":9.3,"relation_to_market":"above_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small UI-vs-API/candle-label ambiguity around Binance chart settlement display","freshness_sensitive":"yes","freshness_driver":"BTC intraday volatility before the 12:00 ET / 16:00 UTC settlement minute","decision_blockers":["Exact-minute path risk remains material because the cushion is only about 1.2%","Minor UI-vs-API settlement-display ambiguity remains","Assigned market snapshot appears stale relative to live market pricing"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"strong","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small UI-vs-API/candle-label ambiguity around Binance chart settlement display","verification_gap_summary":"The key unresolved gap is whether current above-threshold spot will survive ordinary intraday volatility into the exact settlement minute.","best_countercase_summary":"A normal ~1% intraday drop could still push the exact noon-ET close below 72,000.","main_reason_for_disagreement":"Most disagreement is about how much weight to give short-horizon path risk versus the current above-threshold cushion.","resolution_mechanics_summary":"Resolution depends on the Binance BTCUSDT 1-minute candle labeled 12:00 ET, using its final close, which should correspond to 16:00 UTC by open-time convention.","freshness_sensitive":"yes","freshness_driver":"BTC intraday volatility before the 12:00 ET / 16:00 UTC settlement minute","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Binance BTCUSDT is the operative pair","12:00 ET on 2026-04-11 maps to 16:00 UTC","Binance docs define klines by open time and include a close field"],"decision_blockers":["Exact-minute path risk remains material because the cushion is only about 1.2%","Minor UI-vs-API settlement-display ambiguity remains"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nThe best post-synthesis view is still Yes: Binance BTCUSDT was already trading materially above 72,000 during the synthesis check, the contract mechanics are mostly clear, and the main surviving risk is an ordinary intraday pullback hitting the exact noon-ET 1-minute close. But the swarm’s implied edge versus the assigned market baseline was large enough that I compress somewhat toward the market because independent verification mainly confirms current above-threshold status and candle mechanics, not immunity from a >1% downside move over the remaining hours.\n\n## Why this may matter now\n\nAssigned market baseline was 71.25%; my final post-synthesis range is 0.77 to 0.84. T …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.82,"w":"medium","thesis":"The market's Yes lean is directionally right because live Binance BTCUSDT was already above 72,000 during the run, making this primarily a short-horizon volatility and settlement-mechanics question.","support":["Live Binance BTCUSDT traded around 72.86k-72.87k during the run."],"disconfirm":["A bit more than a 1% decline from run-time spot would be enough to flip the market to No."],"ambiguity":["Assignment baseline and live page pricing differed materially during the run."],"change":"I would move lower if Binance BTCUSDT fell back below 72k ahead of noon ET or if later verification showed a different candle-boundary inter …"},{"persona":"catalyst-hunter","p":0.88,"w":"high","thesis":"BTCUSDT on Binance was already materially above 72,000 in the final pre-resolution window, so Yes is favored unless a late downside move pushes the exact noon ET minute close below the threshold.","support":["Binance spot ticker showed BTCUSDT at 72877.49, already above the threshold."],"disconfirm":["BTC only needed about a 1.2% downside move from sampled levels to finish below 72,000 at the exact minute."],"ambiguity":["Whether Binance chart UI and API candle values are perfectly identical for settlement purposes in all edge cases."],"change":"A sharp BTCUSDT drop toward or below 72,000 in the final pre-resolution window, or evidence that the relevant candle/timestamp interpretatio …"},{"persona":"risk-manager","p":0.76,"w":"medium","thesis":"Lean Yes because Binance BTCUSDT is already modestly above 72000, but the edge is limited by ordinary intraday volatility and narrow one-minute settlement mechanics.","support":["Binance BTCUSDT traded around 72.89k during the run, already above the 72k threshold."],"disconfirm":["Binance 24h low near 71.43k shows the threshold can be lost within ordinary recent volatility."],"ambiguity":["Whether the Binance website chart labels the noon ET candle exactly as the open-time API interpretation implies."],"change":"I would cut the estimate quickly if BTCUSDT lost 72k and failed to reclaim it into late morning ET, or if evidence showed the noon ET candle …"}],"selected_assumption_snippets":[{"src":"assumptions/catalyst-hunter.md","text":"# Assumption\nThe operative resolution minute is the Binance BTC/USDT 1-minute candle that closes at 12:00 ET / 16:00 UTC on 2026-04-11, and the API-visible candle close should match the Binance chart close referenced in the rules.\n## Why this assumption matters\nThe thesis depends on translating the contract language into the correct minute and reading the correct close field. A one-hour timezone mistake or UI/API mismatch would break the analysis.\n## What this assumption supports\n- The direction …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: BTC intraday volatility before the 12:00 ET / 16:00 UTC settlement minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: small UI-vs-API/candle-label ambiguity around Binance chart settlement display?","Are the current blockers still material to final judgment: Exact-minute path risk remains material because the cushion is only about 1.2%?","Is the main verification gap still decision-material: The key unresolved gap is whether current above-threshold spot will survive ordinary intraday volatility into the exact settlement minute.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The key unresolved gap is whether current above-threshold spot will survive ordinary intraday volatility into the exact settlement minute.","best_countercase_summary":"A normal ~1% intraday drop could still push the exact noon-ET close below 72,000.","freshness_sensitive":"yes","freshness_driver":"BTC intraday volatility before the 12:00 ET / 16:00 UTC settlement minute","decision_blockers":["Exact-minute path risk remains material because the cushion is only about 1.2%","Minor UI-vs-API settlement-display ambiguity remains"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.88,"w":"high","thesis":"BTCUSDT on Binance was already materially above 72,000 in the final pre-resolution window, so Yes is favored unless a late downside move pushes the exact noon ET minute close below the threshold.","logical_chain":["Verify exact contract mechanics: Binance BTC/USDT pair, 1-minute candle, final close price, noon ET timing.","Map noon ET on 2026-04-11 to 16:00 UTC and confirm the target minute had not yet occurred at capture time.","Observe that current Binance BTCUSDT spot and sampled recent 1-minute closes were materially above 72,000."],"supports":["Binance spot ticker showed BTCUSDT at 72877.49, already above the threshold.","Recent Binance 1-minute closes sampled during the run were also above 72,000."],"disconfirmers":["BTC only needed about a 1.2% downside move from sampled levels to finish below 72,000 at the exact minute.","The rules cite the Binance chart UI while verification used Binance API endpoints, leaving a small operational ambiguity."],"ambiguities":["Whether Binance chart UI and API candle values are perfectly identical for settlement purposes in all edge cases.","Whether live market snapshot divergence from assigned current_price reflects rapid repricing or metadata staleness."],"change":"A sharp BTCUSDT drop toward or below 72,000 in the final pre-resolution window, or evidence that the relevant candle/timestamp interpretation differs from the one used here, would …"},"note_deep_dive":{"src":"assumptions/catalyst-hunter.md","text":"# Assumption\nThe operative resolution minute is the Binance BTC/USDT 1-minute candle that closes at 12:00 ET / 16:00 UTC on 2026-04-11, and the API-visible candle close should match the Binance chart close referenced in the rules.\n## Why this assumption matters\nThe thesis depends on translating the contract language into the correct minute and reading the correct close field. A one-hour timezone mistake or UI/API mismatch would break the analysis.\n## What this assumption supports\n- The directional probability estimate.\n- The judgment that the dominant remaining catalyst is intraday downside before noon ET.\n- The view that current spot being above 72,000 is materially informative for the contract.\n## Evidence or logic behind the assumption\n- The rules explicitly reference 12:00 ET, Binance BTC/USDT, 1m candles, and the final close price.\n- April in New York is in daylight saving time, so …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

