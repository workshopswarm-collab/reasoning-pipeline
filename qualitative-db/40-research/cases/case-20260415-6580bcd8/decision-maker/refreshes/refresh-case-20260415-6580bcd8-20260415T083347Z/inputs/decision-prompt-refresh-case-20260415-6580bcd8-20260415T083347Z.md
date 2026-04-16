# Decision-Maker task | case `case-20260415-6580bcd8`

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
- case_key: `case-20260415-6580bcd8`
- dispatch_id: `refresh-case-20260415-6580bcd8-20260415T083347Z`
- question: Will the price of Bitcoin be above $72,000 on April 17?
- market_title: Will the price of Bitcoin be above $72,000 on April 17?
- market_reference_price: 0.79

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.79,"last_reasoned_price":0.74,"price_delta_pct_points":5.0,"hours_since_last_forecast":0.25,"hours_to_close":55.44,"latest_forecast":{"forecast_id":"dispatch-case-20260415-6580bcd8-20260415T081158Z","forecast_prob":0.74,"decision_ts":"2026-04-15T04:19:00-04:00","rationale_summary":"BTC is still more likely than not to finish above $72,000 on the April 17 Binance noon minute, but with fair value compressed to about 0.74 and the market at 0.77, the right judgment is watch-only because exact-minute pa …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.78,"max_reference_price":0.79,"avg_reference_price":0.7808333333333334},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.78","0.22"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $72,000 on April 17?","market_title":"Will the price of Bitcoin be above $72,000 on April 17?","market_reference_price":0.79,"syndicated_probability_low":0.72,"syndicated_probability_high":0.76,"syndicated_probability_midpoint":0.74,"edge_mid_vs_market_pct_points":-5.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Low residual ambiguity around exact operational mapping of the noon-ET 1-minute Binance bar, but rules are otherwise explicit.","freshness_sensitive":"yes","freshness_driver":"BTC distance from 72,000 and Binance-specific price action in the final hours before Apr 17 12:00 ET.","decision_blockers":["Edge versus market looks marginal after synthesis compression","Exact-minute path dependence cannot be independently verified strongly from current data alone"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Low residual ambiguity around exact operational mapping of the noon-ET 1-minute Binance bar, but rules are otherwise explicit.","verification_gap_summary":"No strong independent way to quantify exact-minute downside risk beyond same-venue Binance history and current spot context.","best_countercase_summary":"A normal 2-3% BTC downdraft or one-minute Binance-specific dip near noon ET can still flip this to No.","main_reason_for_disagreement":"Weighting of narrow settlement-minute fragility versus current cushion above strike.","resolution_mechanics_summary":"Yes resolves only if Binance BTC/USDT’s Apr 17 12:00 ET 1-minute candle final Close is strictly above 72,000.","freshness_sensitive":"yes","freshness_driver":"BTC distance from 72,000 and Binance-specific price action in the final hours before Apr 17 12:00 ET.","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket rules explicitly resolve on Binance BTC/USDT 12:00 ET 1-minute candle final Close","Current Binance BTCUSDT spot remains above 72,000 at about 73.84k during synthesis check","Recent Binance 24h low remained above 72,000 at 73,514"],"decision_blockers":["Edge versus market looks marginal after synthesis compression","Exact-minute path dependence cannot be independently verified strongly from current data alone"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nPost-synthesis view: Yes is still more likely than not, but the swarm’s modestly-bearish-vs-market lean survives verification. The contract is mechanically clear and current Binance BTC/USDT remains comfortably above 72,000, yet the edge against market is small and fragile because resolution depends on one exact Binance 1-minute noon-ET close in a volatile asset. My final estimate is 0.72 to 0.76, slightly below the 0.77 market and compressed toward market because independent verification confirmed the setup but did not strongly justify a larger fade.\n\n## Why this may matter now\n\nMarket implies 0.77 Yes. My post-synthesis range is 0.72 to 0.76. That makes the apparent edg …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.73,"w":"medium","thesis":"Market-implied Yes pricing is broadly reasonable because Binance BTC/USDT is already well above 72k, but the exact noon ET 1-minute close makes 77% slightly rich.","support":["Binance spot snapshot showed BTCUSDT at 73846.60000000 during research."],"disconfirm":["The contract settles on one exact future 1-minute close, so a sharp downside move or resolution-minute noise could still flip the result."],"ambiguity":["How much intraday volatility will increase before the April 17 noon ET window."],"change":"A move back toward or below 72k on Binance before resolution would lower the estimate materially; stable trading well above 74k into late Ap …"},{"persona":"variant-view","p":0.71,"w":"medium","thesis":"BTC is still more likely than not to be above 72k at the April 17 noon ET Binance minute, but the market is slightly overconfident because a single-minute, single-venue settlement window leaves more downside path risk th …","support":["Live Binance BTCUSDT during the run was about 73.8k, already above the 72k threshold."],"disconfirm":["A roughly 2.5% drop is enough to lose, and that is well within normal BTC intraday movement."],"ambiguity":["Whether market participants have already fully priced the narrow timing risk."],"change":"I would move more bullish if BTC holds well above 75k into April 17, and more bearish if price trades back near 72k-73k or if Binance-specif …"},{"persona":"catalyst-hunter","p":0.81,"w":"medium","thesis":"BTC is already above 72k on Binance with a moderate cushion, so absent a short-window shock or settlement-minute dip the April 17 noon ET close is more likely than not to finish above 72k.","support":["Binance BTCUSDT spot was about 73856.76 when checked, roughly 1856.76 above the threshold."],"disconfirm":["The contract settles on one exact Binance 1-minute noon-ET close, so a transient selloff or wick can decide the market."],"ambiguity":["Exact UI/candle-label handling on Binance can matter in narrow time-window markets."],"change":"A move back toward 72.2k-72.5k, a material macro risk-off catalyst, or Binance-specific instability would push the estimate lower."}],"selected_assumption_snippets":[{"src":"assumptions/variant-view.md","text":"# Assumption\nThe market’s 0.77 Yes price is slightly underweighting the chance that a narrow intraday downdraft or Binance-specific print at exactly 12:00 ET can knock BTC/USDT below 72,000 even if broader trend conditions stay constructive.\n## Why this assumption matters\nThe entire variant view depends on separating \"BTC probably remains generally strong\" from \"the contract resolves Yes.\" This market is not about end-of-day or average price; it is about one exchange, one pair, and one minute.\n# …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: BTC distance from 72,000 and Binance-specific price action in the final hours before Apr 17 12:00 ET.?","How decision-relevant is the remaining contract/source-of-truth ambiguity: Low residual ambiguity around exact operational mapping of the noon-ET 1-minute Binance bar, but rules are otherwise explicit.?","Are the current blockers still material to final judgment: Edge versus market looks marginal after synthesis compression?","Is the main verification gap still decision-material: No strong independent way to quantify exact-minute downside risk beyond same-venue Binance history and current spot context.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"No strong independent way to quantify exact-minute downside risk beyond same-venue Binance history and current spot context.","best_countercase_summary":"A normal 2-3% BTC downdraft or one-minute Binance-specific dip near noon ET can still flip this to No.","freshness_sensitive":"yes","freshness_driver":"BTC distance from 72,000 and Binance-specific price action in the final hours before Apr 17 12:00 ET.","decision_blockers":["Edge versus market looks marginal after synthesis compression","Exact-minute path dependence cannot be independently verified strongly from current data alone"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.81,"w":"medium","thesis":"BTC is already above 72k on Binance with a moderate cushion, so absent a short-window shock or settlement-minute dip the April 17 noon ET close is more likely than not to finish above 72k.","logical_chain":["The governing source of truth is the Binance BTC/USDT 1-minute candle close at 12:00 PM ET on April 17.","Current Binance spot is already above 72k by a moderate margin.","With roughly two days left, the base case is persistence unless a bearish catalyst forces a sharp drawdown."],"supports":["Binance BTCUSDT spot was about 73856.76 when checked, roughly 1856.76 above the threshold.","Binance 24h low of 73514 remained above 72000 on the short lookback."],"disconfirmers":["The contract settles on one exact Binance 1-minute noon-ET close, so a transient selloff or wick can decide the market.","BTC can move multiple percentage points within 48 hours on macro or leverage-driven shocks."],"ambiguities":["Exact UI/candle-label handling on Binance can matter in narrow time-window markets.","No specific scheduled high-information catalyst was identified; the key risk is unscheduled shock risk."],"change":"A move back toward 72.2k-72.5k, a material macro risk-off catalyst, or Binance-specific instability would push the estimate lower."},"note_deep_dive":{"src":"assumptions/variant-view.md","text":"# Assumption\nThe market’s 0.77 Yes price is slightly underweighting the chance that a narrow intraday downdraft or Binance-specific print at exactly 12:00 ET can knock BTC/USDT below 72,000 even if broader trend conditions stay constructive.\n## Why this assumption matters\nThe entire variant view depends on separating \"BTC probably remains generally strong\" from \"the contract resolves Yes.\" This market is not about end-of-day or average price; it is about one exchange, one pair, and one minute.\n## What this assumption supports\n- A modestly lower-than-market Yes estimate rather than a strong contrarian No call.\n- Emphasis on timing and venue-specific fragility as the main neglected mechanism.\n- The judgment that market confidence may be a bit too smooth for a narrow-resolution contract.\n## Evidence or logic behind the assumption\n- The threshold is only about 2.5% below live spot during thi …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

