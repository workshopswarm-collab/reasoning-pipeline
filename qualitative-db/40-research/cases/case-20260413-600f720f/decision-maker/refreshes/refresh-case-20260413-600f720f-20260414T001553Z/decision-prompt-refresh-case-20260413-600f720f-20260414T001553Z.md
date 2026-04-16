# Decision-Maker task | case `case-20260413-600f720f`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
You may use only web_search, web_fetch in this turn.
Stay within: searches<=5, fetches<=3, min_distinct_source_families=2 when feasible.
Choose sources independently and prefer primary, official, and resolution-relevant sources.
Do not count multiple pages from the same source family as real diversity.

## Case
- case_key: `case-20260413-600f720f`
- dispatch_id: `refresh-case-20260413-600f720f-20260414T001553Z`
- question: Will Bitcoin reach $76,000 April 13-19?
- market_title: Will Bitcoin reach $76,000 April 13-19?
- market_reference_price: 0.72

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.72,"last_reasoned_price":0.665,"price_delta_pct_points":5.5,"hours_since_last_forecast":0.58,"hours_to_close":147.74,"latest_forecast":{"forecast_id":"dispatch-case-20260413-600f720f-20260413T233138Z","forecast_prob":0.665,"decision_ts":"2026-04-13T19:41:00-04:00","rationale_summary":"BTC reaching $76k this week remains more likely than not because only one Binance 1-minute high is needed and spot is already close, but the market's 75% price still looks too rich relative to bounded evidence on momentu …"},"snapshot_summary":{"snapshot_count":6,"min_reference_price":0.72,"max_reference_price":0.765,"avg_reference_price":0.7475},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.69","0.31"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will Bitcoin reach $76,000 April 13-19?","market_title":"Will Bitcoin reach $76,000 April 13-19?","market_reference_price":0.72,"syndicated_probability_low":0.64,"syndicated_probability_high":0.69,"syndicated_probability_midpoint":0.665,"edge_mid_vs_market_pct_points":-5.5,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"none","contract_ambiguity_reason":"","freshness_sensitive":"yes","freshness_driver":"Short-horizon BTC momentum and Binance intrawindow highs can change the forecast quickly over the remaining week.","decision_blockers":["No decisive independent evidence on whether momentum persists strongly enough to finish the final move","Short-dated path dependence means the modest edge versus market could vanish quickly on new price action"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"strong","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"none","verification_gap_summary":"The main remaining gap is fresh evidence on whether near-term momentum is strong enough to complete the final move before week-end.","best_countercase_summary":"Because only one Binance 1-minute spike is needed and BTC is already within roughly 1.5%-1.8%, the market may simply be right that touch odds are near three-in-four.","main_reason_for_disagreement":"Most disagreement is about how much weight to put on proximity-to-strike and touch mechanics versus simple path-failure risk.","resolution_mechanics_summary":"Yes resolves if any Binance BTC/USDT 1-minute candle high is at least $76,000 between Apr 13 00:00 ET and Apr 19 23:59 ET.","freshness_sensitive":"yes","freshness_driver":"Short-horizon BTC momentum and Binance intrawindow highs can change the forecast quickly over the remaining week.","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket rules explicitly use Binance BTC/USDT 1-minute Highs during Apr 13-19 ET","Market snapshot was roughly 0.73-0.75 Yes at research time","Independent contextual price checks put BTC around $74.7k-$74.9k, below but near $76k"],"decision_blockers":["No decisive independent evidence on whether momentum persists strongly enough to finish the final move","Short-dated path dependence means the modest edge versus market could vanish quickly on new price action"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nPost-synthesis view: BTC reaching $76,000 during Apr 13-19 is more likely than not because the contract resolves on any Binance BTC/USDT 1-minute high and BTC was already trading around $74.7k-$74.9k at synthesis time, but the market's 0.75 price still looks somewhat too aggressive absent stronger independent evidence that momentum will complete the final ~1.5%-1.8% move within the week. My final range is 0.64-0.69, a modest under versus market with only medium confidence and limited standalone alpha.\n\n## Why this may matter now\n\nMarket implied probability is 0.75; my syndicated range is 0.64-0.69. That is a modest below-market view, but the edge looks marginal rather tha …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.66,"w":"medium","thesis":"The market is directionally right that a 76k touch is favored because the contract only needs one Binance 1-minute high and BTC is already near the threshold, but 0.75 looks somewhat aggressive; my estimate is 0.66.","support":["Contract resolves Yes on any Binance BTC/USDT 1-minute high >= 76,000 during Apr 13-19."],"disconfirm":["76k had not been hit yet, and a fast reversal from current levels would make the market's optimism look too rich."],"ambiguity":["How much current upside momentum persists over the next several sessions."],"change":"I would move up if BTC quickly challenges fresh highs near 76k, and move down if BTC sells off meaningfully away from the threshold."},{"persona":"base-rate","p":0.61,"w":"medium","thesis":"BTC reaching $76,000 this week is still more likely than not, but the 75% market price looks too aggressive given checked prices remained below the threshold and close is not the same as crossed.","support":["CoinGecko range data showed a max observed price around $74,724, still below $76,000."],"disconfirm":["BTC was already within roughly 1.5%-1.8% of the threshold, a move well within normal crypto volatility over a week."],"ambiguity":["Exact settlement-source text on the Polymarket rules page was not independently captured."],"change":"A verified print at or above $76,000, a sustained breakout above current weekly highs, or direct rule text showing a materially different in …"},{"persona":"variant-view","p":0.68,"w":"medium","thesis":"BTC is close enough to $76k to keep yes favored, but the 75% market price looks slightly too confident because nearby resistance could produce a timed-out near miss.","support":["Binance showed BTC around $74.6k, only about 1.8% below the threshold."],"disconfirm":["A small additional upside move could clear $76k quickly after an already strong day."],"ambiguity":["Exact official Polymarket benchmark/index methodology for 'reach'."],"change":"A clean breakout above the recent highs, especially sustained trade through $75k toward $76k, or cleaner settlement-source evidence that mat …"}],"selected_assumption_snippets":[{"src":"assumptions/base-rate.md","text":"# Assumption\nThe current weekly trading regime that produced a fast move from roughly $70.7k to the mid-$74k area will not automatically extend another roughly 1.5% to 1.8% upward to the $76k threshold within the remaining contract window.\n## Why this assumption matters\nThe final estimate depends on treating the threshold as reachable but not already likely enough to justify the market's 75% implied probability.\n## What this assumption supports\n- A below-market estimate for YES on $76,000.\n- A v …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Short-horizon BTC momentum and Binance intrawindow highs can change the forecast quickly over the remaining week.?","Are the current blockers still material to final judgment: No decisive independent evidence on whether momentum persists strongly enough to finish the final move?","Is the main verification gap still decision-material: The main remaining gap is fresh evidence on whether near-term momentum is strong enough to complete the final move before week-end.?","Does the strongest surviving countercase remain live enough to compress the edge further: Because only one Binance 1-minute spike is needed and BTC is already within roughly 1.5%-1.8%, the market may simply be right that touch odds are near three-in-four.?"],"focus":{"contract_ambiguity_level":"none","verification_gap_summary":"The main remaining gap is fresh evidence on whether near-term momentum is strong enough to complete the final move before week-end.","best_countercase_summary":"Because only one Binance 1-minute spike is needed and BTC is already within roughly 1.5%-1.8%, the market may simply be right that touch odds are near three-in-four.","freshness_sensitive":"yes","freshness_driver":"Short-horizon BTC momentum and Binance intrawindow highs can change the forecast quickly over the remaining week.","decision_blockers":["No decisive independent evidence on whether momentum persists strongly enough to finish the final move","Short-dated path dependence means the modest edge versus market could vanish quickly on new price action"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"variant-view","p":0.68,"w":"medium","thesis":"BTC is close enough to $76k to keep yes favored, but the 75% market price looks slightly too confident because nearby resistance could produce a timed-out near miss.","logical_chain":["Market implies 75% because BTC is already near the target.","Direct price data confirm yes is favored but not settled.","Independent contextual evidence suggests nearby resistance and no confirmed breakout."],"supports":["Binance showed BTC around $74.6k, only about 1.8% below the threshold.","BTC posted a +5.689% 24h move, showing the target is reachable within ordinary crypto volatility."],"disconfirmers":["A small additional upside move could clear $76k quickly after an already strong day.","If BTC breaks above the recent high zone early in the week, the mild-under thesis likely fails."],"ambiguities":["Exact official Polymarket benchmark/index methodology for 'reach'.","How persistent the reported resistance structure will be over the remaining week."],"change":"A clean breakout above the recent highs, especially sustained trade through $75k toward $76k, or cleaner settlement-source evidence that materially changes what counts as a hit."},"note_deep_dive":{"src":"assumptions/base-rate.md","text":"# Assumption\nThe current weekly trading regime that produced a fast move from roughly $70.7k to the mid-$74k area will not automatically extend another roughly 1.5% to 1.8% upward to the $76k threshold within the remaining contract window.\n## Why this assumption matters\nThe final estimate depends on treating the threshold as reachable but not already likely enough to justify the market's 75% implied probability.\n## What this assumption supports\n- A below-market estimate for YES on $76,000.\n- A view that the market may be overweighting momentum and salience from the sharp Apr 13 rebound.\n- A conclusion that the outside-view prior should still discount the chance of one more clean extension leg within days.\n## Evidence or logic behind the assumption\n- Observed contextual pricing shows BTC still below the threshold after a strong daily move.\n- Threshold-touch contracts are nonlinear: gettin …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

