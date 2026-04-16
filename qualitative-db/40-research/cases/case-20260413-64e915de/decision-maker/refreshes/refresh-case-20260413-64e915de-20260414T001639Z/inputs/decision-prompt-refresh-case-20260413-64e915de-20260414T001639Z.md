# Decision-Maker task | case `case-20260413-64e915de`

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
- case_key: `case-20260413-64e915de`
- dispatch_id: `refresh-case-20260413-64e915de-20260414T001639Z`
- question: Will Ethereum reach $2,400 April 13-19?
- market_title: Will Ethereum reach $2,400 April 13-19?
- market_reference_price: 0.88

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.88,"last_reasoned_price":0.81,"price_delta_pct_points":7.0,"hours_since_last_forecast":0.03,"hours_to_close":147.72,"latest_forecast":{"forecast_id":"dispatch-case-20260413-64e915de-20260413T234340Z","forecast_prob":0.81,"decision_ts":"2026-04-13T20:15:00-04:00","rationale_summary":"ETH is likely to hit $2,400 during Apr 13-19 because Binance touch mechanics and the near-miss around 2395 make Yes genuinely favored, but the market's 90.5% price still overstates how automatic that last few dollars rea …"},"snapshot_summary":{"snapshot_count":11,"min_reference_price":0.725,"max_reference_price":0.92,"avg_reference_price":0.8318181818181818},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.88","0.12"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will Ethereum reach $2,400 April 13-19?","market_title":"Will Ethereum reach $2,400 April 13-19?","market_reference_price":0.88,"syndicated_probability_low":0.78,"syndicated_probability_high":0.84,"syndicated_probability_midpoint":0.81,"edge_mid_vs_market_pct_points":-7.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"none","contract_ambiguity_reason":"","freshness_sensitive":"yes","freshness_driver":"Binance ETH/USDT intraday path and any renewed retest of the 2390s before Apr 19 close","decision_blockers":["Fresh path dependence remains high in a short-dated threshold market","No decisive synthesis-stage evidence that the remaining last-mile move is nearly automatic"],"blockers_require_new_research":"no","disagreement_type":"market_pricing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"strong","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"none","verification_gap_summary":"The key remaining gap is fresh Binance path data proving whether the initial near-touch impulse will convert before Apr 19.","best_countercase_summary":"ETH was already within a few dollars of the threshold on day one, so a brief Binance wick above $2,400 may still deserve near-market odds.","main_reason_for_disagreement":"Remaining disagreement is mostly about how much residual failure risk to assign to a very-near threshold touch market.","resolution_mechanics_summary":"Resolves Yes if any Binance ETH/USDT 1-minute candle during Apr 13-19 ET has High >= 2400.","freshness_sensitive":"yes","freshness_driver":"Binance ETH/USDT intraday path and any renewed retest of the 2390s before Apr 19 close","blockers_require_new_research":"no","disagreement_type":"market_pricing","independently_verified_points":["Polymarket page embeds explicit Binance ETH/USDT 1-minute High resolution rule","Only Binance ETH/USDT highs count; other venues do not govern settlement","Swarm consensus that event is favored but below market is faithful to raw findings"],"decision_blockers":["Fresh path dependence remains high in a short-dated threshold market","No decisive synthesis-stage evidence that the remaining last-mile move is nearly automatic"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nPost-synthesis view: ETH reaching $2,400 during Apr 13-19 is still more likely than not, but the swarm’s below-market stance remains the right synthesis posture after verification. The strongest reason is that the contract is explicitly a Binance ETH/USDT 1-minute high-touch market, and while ETH was already very close to the threshold on day one, the independent synthesis-stage check does not justify treating the last few dollars as nearly automatic. Final view stays below the market’s 90.5% and centers in the low-80s rather than near-certainty.\n\n## Why this may matter now\n\nMarket-implied probability is 0.905. My syndicated range is 0.78 to 0.84. That leaves the edge as …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.82,"w":"medium","thesis":"ETH reaching $2,400 this week is likely because spot is already near $2,374, but the market's 90.5% price looks somewhat too confident relative to still-unmet threshold and partial rules-text ambiguity.","support":["Binance and Coinbase spot checks placed ETH around 2373-2375 during the run."],"disconfirm":["ETH had not yet actually crossed $2,400 in the extra verification pass."],"ambiguity":["Exact Polymarket rules text and qualifying price-source convention were not fully extracted from the event page fetch."],"change":"I would move up on cleaner rules confirmation or a stronger retest near $2,400, and move down on a sharp selloff, verified restrictive rules …"},{"persona":"catalyst-hunter","p":0.72,"w":"medium","thesis":"ETH is favored to touch $2,400 during Apr 13-19 because spot already reached $2,395 on day one, but the market's 90.5% probability still looks too high for a one-week threshold market.","support":["Coinbase spot traded around $2,374 late on Apr 13 and already printed a same-day high of $2,395."],"disconfirm":["ETH already reached $2,395 and still failed to print $2,400 on day one, suggesting real resistance just below the threshold."],"ambiguity":["Exact contract settlement source mechanics if exchange prints diverge."],"change":"I would cut the probability if rules proved more restrictive than expected or if ETH quickly rejected and failed to revisit the $2,370-$2,39 …"},{"persona":"variant-view","p":0.84,"w":"medium","thesis":"ETH is likely to hit $2,400 during April 13-19, but the market is mildly overconfident because a near-miss after a sharp impulse move can still fail in a short-dated threshold market.","support":["Binance verified ETH high of 2394.71 left ETH only $5.29 short of the target."],"disconfirm":["ETH was already extremely close to the threshold, so a yes outcome may still deserve an extreme probability."],"ambiguity":["Exact governing venue/source text for settlement was not independently verified from the live market page."],"change":"A verified print above $2,400 on the governing settlement source, or confirmation that the governing source already crossed that level, woul …"}],"selected_assumption_snippets":[{"src":"assumptions/catalyst-hunter.md","text":"# Assumption\nThe most important assumption is that once ETH trades to within roughly 1% of $2,400 at the start of the window, near-term momentum and liquidity are more likely than not to produce at least one qualifying touch before Apr 19 rather than stall just below the level all week.\n## Why this assumption matters\nThe market resolves on whether the threshold is hit during a narrow period, not on end-of-week close. That makes path dependence crucial. If near-threshold momentum tends to extend …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Binance ETH/USDT intraday path and any renewed retest of the 2390s before Apr 19 close?","Are the current blockers still material to final judgment: Fresh path dependence remains high in a short-dated threshold market?","Is the main verification gap still decision-material: The key remaining gap is fresh Binance path data proving whether the initial near-touch impulse will convert before Apr 19.?","Does the strongest surviving countercase remain live enough to compress the edge further: ETH was already within a few dollars of the threshold on day one, so a brief Binance wick above $2,400 may still deserve near-market odds.?"],"focus":{"contract_ambiguity_level":"none","verification_gap_summary":"The key remaining gap is fresh Binance path data proving whether the initial near-touch impulse will convert before Apr 19.","best_countercase_summary":"ETH was already within a few dollars of the threshold on day one, so a brief Binance wick above $2,400 may still deserve near-market odds.","freshness_sensitive":"yes","freshness_driver":"Binance ETH/USDT intraday path and any renewed retest of the 2390s before Apr 19 close","decision_blockers":["Fresh path dependence remains high in a short-dated threshold market","No decisive synthesis-stage evidence that the remaining last-mile move is nearly automatic"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"variant-view","p":0.84,"w":"medium","thesis":"ETH is likely to hit $2,400 during April 13-19, but the market is mildly overconfident because a near-miss after a sharp impulse move can still fail in a short-dated threshold market.","logical_chain":["Market implies about 90.5% from the current price.","Verified exchange data shows ETH very near but still below $2,400 at this snapshot.","That supports a likely yes outcome but leaves real path-dependent failure risk in a short-dated threshold market."],"supports":["Binance verified ETH high of 2394.71 left ETH only $5.29 short of the target.","ETH 24h change of about +8.4% shows strong momentum entering the window."],"disconfirmers":["ETH was already extremely close to the threshold, so a yes outcome may still deserve an extreme probability.","If broader crypto risk appetite remains strong, the market may be conservative rather than overconfident."],"ambiguities":["Exact governing venue/source text for settlement was not independently verified from the live market page.","Different venues may print slightly different intraday highs."],"change":"A verified print above $2,400 on the governing settlement source, or confirmation that the governing source already crossed that level, would move the estimate toward or above the …"},"note_deep_dive":{"src":"assumptions/catalyst-hunter.md","text":"# Assumption\nThe most important assumption is that once ETH trades to within roughly 1% of $2,400 at the start of the window, near-term momentum and liquidity are more likely than not to produce at least one qualifying touch before Apr 19 rather than stall just below the level all week.\n## Why this assumption matters\nThe market resolves on whether the threshold is hit during a narrow period, not on end-of-week close. That makes path dependence crucial. If near-threshold momentum tends to extend into one more wick, the hit probability is high; if resistance and profit-taking dominate, the market's very high implied probability is too aggressive.\n## What this assumption supports\n- A probability estimate moderately above 50% and potentially in rough agreement with the market.\n- A catalyst framing centered on liquidity continuation and short-dated derivatives behavior rather than a single di …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

