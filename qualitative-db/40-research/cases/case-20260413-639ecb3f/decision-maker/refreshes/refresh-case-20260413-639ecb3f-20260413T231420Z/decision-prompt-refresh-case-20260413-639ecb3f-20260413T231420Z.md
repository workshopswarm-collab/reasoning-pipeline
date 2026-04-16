# Decision-Maker task | case `case-20260413-639ecb3f`

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
- case_key: `case-20260413-639ecb3f`
- dispatch_id: `refresh-case-20260413-639ecb3f-20260413T231420Z`
- question: Will Ethereum reach $2,400 April 13-19?
- market_title: Will Ethereum reach $2,400 April 13-19?
- market_reference_price: 0.79

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.79,"last_reasoned_price":0.71,"price_delta_pct_points":8.0,"hours_since_last_forecast":0.02,"hours_to_close":148.76,"latest_forecast":{"forecast_id":"dispatch-case-20260413-639ecb3f-20260413T225424Z","forecast_prob":0.71,"decision_ts":"2026-04-13T19:13:00-04:00","rationale_summary":"ETH reaching $2,400 during Apr 13-19 remains more likely than not because the level is nearby and the mechanics appear touch-friendly, but the market's 76% price is still slightly rich relative to the bounded evidence, s …"},"snapshot_summary":{"snapshot_count":5,"min_reference_price":0.725,"max_reference_price":0.835,"avg_reference_price":0.774},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.79","0.21"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
- `execution_semantics.price_source`: `market_snapshot_quote | effective_executable_quote`
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will Ethereum reach $2,400 April 13-19?","market_title":"Will Ethereum reach $2,400 April 13-19?","market_reference_price":0.79,"syndicated_probability_low":0.68,"syndicated_probability_high":0.74,"syndicated_probability_midpoint":0.71,"edge_mid_vs_market_pct_points":-8.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Public fetch confirms event framing but not the full rules text directly in this synthesis pass; upstream lanes consistently report Binance 1-minute high mechanics.","freshness_sensitive":"yes","freshness_driver":"Short-dated crypto price path; a single momentum extension or reversal in the next 24-48 hours can move the probability materially.","decision_blockers":["Independent verification of the exact authoritative settlement wording is not perfect in the synthesis pass.","Any sharp crypto-wide risk-off move could quickly invalidate proximity-based bullishness.","The apparent edge versus market is small after compression, so actionability is limited."],"blockers_require_new_research":"no","disagreement_type":"interpretation","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Public fetch confirms event framing but not the full rules text directly in this synthesis pass; upstream lanes consistently report Binance 1-minute high mechanics.","verification_gap_summary":"The main remaining gap is direct first-hand recovery of the full authoritative rules text naming Binance ETH/USDT 1-minute highs in this synthesis pass.","best_countercase_summary":"A visible round-number threshold can still fail despite proximity, and without a fresh forcing catalyst the final 1-2% may not print on Binance.","main_reason_for_disagreement":"Remaining disagreement is mostly about how much weight to put on proximity/touch mechanics versus failed-breakout path risk.","resolution_mechanics_summary":"This is effectively a venue-specific touch market, with Yes favored if the governing Binance threshold-high interpretation is correct.","freshness_sensitive":"yes","freshness_driver":"Short-dated crypto price path; a single momentum extension or reversal in the next 24-48 hours can move the probability materially.","blockers_require_new_research":"no","disagreement_type":"interpretation","independently_verified_points":["ETH was trading in the low-to-mid 2340s at synthesis time, leaving roughly a 2%-plus move to 2400.","Binance 24h high was 2363.94, so the threshold had not yet been reached but was nearby.","Public Polymarket event page confirms the 2400 outcome was priced around 76% and that resolution depends on page rules rather than a weekly …"],"decision_blockers":["Independent verification of the exact authoritative settlement wording is not perfect in the synthesis pass.","Any sharp crypto-wide risk-off move could quickly invalidate proximity-based bullishness."]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nPost-synthesis, ETH reaching $2,400 on Binance ETH/USDT during Apr 13-19 still looks more likely than not, but the market’s 0.76 price appears a bit rich rather than clearly wrong. My final view is 0.68 to 0.74: the contract mechanics are genuinely favorable to Yes because any Binance 1-minute high counts, but the independent verification mostly confirms proximity/mechanics rather than proving a large edge, so I compress modestly toward market while staying slightly below it.\n\n## Why this may matter now\n\nMarket implied probability is 0.76. My syndicated range is 0.68 to 0.74, so the edge is marginal and slightly below market rather than actionable on size. The likely mark …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.72,"w":"medium","thesis":"Market pricing near 76% looks broadly efficient because ETH is already within about 2% of the barrier and the contract resolves on any Binance 1-minute high at or above $2,400.","support":["ETH spot snapshots clustered around $2,356-$2,365, leaving only a modest move to $2,400."],"disconfirm":["ETH had not yet hit $2,400 at research time and a final 1.5%-2% move can still fail."],"ambiguity":["No separate exhaustive realized-volatility study was performed."],"change":"I would move lower if ETH loses the $2,300 area or broader crypto sentiment turns sharply risk-off; higher if ETH repeatedly probes $2,380-$ …"},{"persona":"catalyst-hunter","p":0.64,"w":"medium","thesis":"ETH is close enough to $2,400 that continued momentum could trigger a Binance 1-minute high above the threshold this week, but the market's 76% price looks somewhat rich absent a clear must-happen catalyst.","support":["Polymarket rules make this a Binance 1-minute high threshold-touch contract, which is easier than requiring a close above 2400."],"disconfirm":["There is no clearly identified must-happen catalyst in the Apr 13-19 window that independently forces the final move to 2400."],"ambiguity":["Whether the current rally is durable follow-through or a short-lived squeeze."],"change":"A clean extension through the high-2300s would push the estimate up; failure to retest 2360s followed by reversal toward the low 2200s would …"},{"persona":"base-rate","p":0.79,"w":"medium","thesis":"Ethereum reaching $2,400 during April 13-19 is slightly more likely than the market implies because the threshold is only about 2% above current spot and sits inside recent realized ETH range.","support":["ETH spot was already in the mid-2300s, leaving only about a 2% move to reach 2400."],"disconfirm":["The empirical outside-view calibration is rough and may overstate the true hit probability."],"ambiguity":["Exact Polymarket settlement feed / rule text was not fully visible in the fetched snippet."],"change":"Cleaner restrictive rule text, a sharp ETH selloff away from 2400, or better empirical calibration showing materially lower comparable hit r …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Short-dated crypto price path; a single momentum extension or reversal in the next 24-48 hours can move the probability materially.?","How decision-relevant is the remaining contract/source-of-truth ambiguity: Public fetch confirms event framing but not the full rules text directly in this synthesis pass; upstream lanes consistently report Binance 1-minute high mechanics.?","Are the current blockers still material to final judgment: Independent verification of the exact authoritative settlement wording is not perfect in the synthesis pass.?","Is the main verification gap still decision-material: The main remaining gap is direct first-hand recovery of the full authoritative rules text naming Binance ETH/USDT 1-minute highs in this synthesis pass.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The main remaining gap is direct first-hand recovery of the full authoritative rules text naming Binance ETH/USDT 1-minute highs in this synthesis pass.","best_countercase_summary":"A visible round-number threshold can still fail despite proximity, and without a fresh forcing catalyst the final 1-2% may not print on Binance.","freshness_sensitive":"yes","freshness_driver":"Short-dated crypto price path; a single momentum extension or reversal in the next 24-48 hours can move the probability materially.","decision_blockers":["Independent verification of the exact authoritative settlement wording is not perfect in the synthesis pass.","Any sharp crypto-wide risk-off move could quickly invalidate proximity-based bullishness."]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"base-rate","p":0.79,"w":"medium","thesis":"Ethereum reaching $2,400 during April 13-19 is slightly more likely than the market implies because the threshold is only about 2% above current spot and sits inside recent realized ETH range.","logical_chain":["Start with market-implied probability of 76%.","Check current ETH spot relative to the 2400 threshold and note the hurdle is only about 2%.","Check recent realized ETH history and see that 2400 is inside recent range rather than a fresh breakout level."],"supports":["ETH spot was already in the mid-2300s, leaving only about a 2% move to reach 2400.","Recent realized ETH prices had already reached or exceeded 2400 within the prior month."],"disconfirmers":["The empirical outside-view calibration is rough and may overstate the true hit probability.","If the exact Polymarket settlement rules are more restrictive than a simple touch interpretation, true probability could be lower."],"ambiguities":["Exact Polymarket settlement feed / rule text was not fully visible in the fetched snippet.","How representative recent realized volatility is for the coming week."],"change":"Cleaner restrictive rule text, a sharp ETH selloff away from 2400, or better empirical calibration showing materially lower comparable hit rates would move me down; cleaner permiss …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

