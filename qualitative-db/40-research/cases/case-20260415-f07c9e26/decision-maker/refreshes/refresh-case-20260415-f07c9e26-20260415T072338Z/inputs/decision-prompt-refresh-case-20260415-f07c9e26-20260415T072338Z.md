# Decision-Maker task | case `case-20260415-f07c9e26`

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
- case_key: `case-20260415-f07c9e26`
- dispatch_id: `refresh-case-20260415-f07c9e26-20260415T072338Z`
- question: Will the price of Bitcoin be above $72,000 on April 16?
- market_title: Will the price of Bitcoin be above $72,000 on April 16?
- market_reference_price: 0.805

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.805,"last_reasoned_price":0.875,"price_delta_pct_points":7.0,"hours_since_last_forecast":5.76,"hours_to_close":32.61,"latest_forecast":{"forecast_id":"dispatch-case-20260415-f07c9e26-20260415T013036Z","forecast_prob":0.875,"decision_ts":"2026-04-14T21:38:00-04:00","rationale_summary":"Bitcoin is likely to finish above $72,000 on the April 16 noon ET Binance minute because current same-venue pricing remains materially above the strike and recent Binance minute data stayed well above it, but the market' …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.805,"max_reference_price":0.845,"avg_reference_price":0.8408333333333333},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.805","0.195"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $72,000 on April 16?","market_title":"Will the price of Bitcoin be above $72,000 on April 16?","market_reference_price":0.805,"syndicated_probability_low":0.86,"syndicated_probability_high":0.89,"syndicated_probability_midpoint":0.875,"edge_mid_vs_market_pct_points":7.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small practical UI/API settlement-surface ambiguity on Binance despite clear venue/time/close rules","freshness_sensitive":"yes","freshness_driver":"Live Binance BTCUSDT level and realized volatility into the Apr 16 12:00 ET settlement minute","decision_blockers":["Single-minute settlement path dependence leaves meaningful late-move risk","No independent way to verify absence of an overnight or US-morning crypto selloff catalyst","Minor Binance UI-versus-API implementation ambiguity remains"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small practical UI/API settlement-surface ambiguity on Binance despite clear venue/time/close rules","verification_gap_summary":"The main unverified gap is whether any sharp selloff arrives before the exact noon-ET settlement minute.","best_countercase_summary":"The current cushion may simply be large enough that a 90%+ Yes price is fair if BTC stays above 74k into late morning ET.","main_reason_for_disagreement":"Remaining disagreement is mostly about how much one-minute settlement path risk should discount an otherwise favorable spot cushion.","resolution_mechanics_summary":"Yes requires the Binance BTC/USDT 1-minute candle labeled 12:00 ET on Apr 16 to have a final close strictly above 72,000.","freshness_sensitive":"yes","freshness_driver":"Live Binance BTCUSDT level and realized volatility into the Apr 16 12:00 ET settlement minute","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket contract resolves on Binance BTC/USDT 12:00 ET 1-minute candle close","12:00 ET on Apr 16 maps cleanly to 16:00 UTC","Fresh Binance BTCUSDT remained around 74.54k at synthesis time, still materially above 72k"],"decision_blockers":["Single-minute settlement path dependence leaves meaningful late-move risk","No independent way to verify absence of an overnight or US-morning crypto selloff catalyst"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBitcoin is still more likely than not to be above $72,000 at the April 16 settlement minute, but the swarm's mild below-market view survives synthesis: current Binance BTC/USDT is comfortably above the threshold and contract mechanics are mostly clean, yet a single-minute Binance close with less than a 4% cushion still leaves enough path risk that 90.5% looks somewhat rich rather than obviously cheap.\n\n## Why this may matter now\n\nMarket implies 0.905. My post-synthesis range is 0.86 to 0.89. That is a modest below-market view, so any edge is marginal rather than dramatic. The likely mispricing, if any, is that the market may be slightly underweighting single-minute settle …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.87,"w":"high","thesis":"The market's ~90.5% Yes price is broadly reasonable because BTC/USDT is comfortably above $72k, but I shade lower because a one-minute noon-ET Binance settlement still leaves path and timing risk.","support":["Binance BTCUSDT spot was about 74663.59 during research, materially above the threshold."],"disconfirm":["A roughly 3.5% downside move before the exact settlement minute could still flip the result."],"ambiguity":["Whether any UI/API display nuance could matter at the exact settlement moment."],"change":"A drop toward the low-72k to 73k area before settlement, evidence of elevated event risk, or proof that the settlement-facing Binance surfac …"},{"persona":"base-rate","p":0.86,"w":"medium","thesis":"Binance BTC/USDT is currently well above 72,000, so outside-view short-horizon persistence supports Yes, but 90.5% looks slightly too confident for a one-minute crypto checkpoint still half a day away.","support":["Binance BTC/USDT was about 74,663.59 at research time, roughly 2.7% above the threshold."],"disconfirm":["Crypto can move more than 3% in under a day, and this contract only needs one bad minute at the wrong time."],"ambiguity":["The exact chart UI candle used at settlement is exchange-native but not directly observable from the fetched Polymarket page output here."],"change":"I would cut the estimate if Binance BTC/USDT falls toward 72k, if a sharp risk-off move hits crypto before resolution, or if Binance-specifi …"},{"persona":"catalyst-hunter","p":0.89,"w":"high","thesis":"BTC/USDT is already materially above 72,000 on Binance, so Yes remains likely unless a sharp selloff hits before the exact noon ET settlement minute.","support":["Binance ticker during the run showed BTCUSDT around 74,620, roughly 3.6% above the threshold."],"disconfirm":["A single one-minute settlement rule leaves real path risk if BTC sells off sharply at the wrong time."],"ambiguity":["No scheduled binary catalyst was identified, so residual risk is mostly unscheduled volatility."],"change":"A sharp drawdown toward 72k before noon ET, a clear macro/crypto selloff catalyst, or Binance instability near settlement would make me mate …"}],"selected_assumption_snippets":[{"src":"assumptions/base-rate.md","text":"# Assumption\nBTC will remain within its recent short-horizon trading regime through the April 16 noon ET resolution minute, rather than experiencing a sharp downside break of more than roughly 3% before that time.\n## Why this assumption matters\nThe base-rate case for Yes depends less on a fresh bullish catalyst and more on the tendency for a benchmark asset already trading materially above a threshold to remain above it over a one-day horizon.\n## What this assumption supports\n- A high-probabilit …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Live Binance BTCUSDT level and realized volatility into the Apr 16 12:00 ET settlement minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: small practical UI/API settlement-surface ambiguity on Binance despite clear venue/time/close rules?","Are the current blockers still material to final judgment: Single-minute settlement path dependence leaves meaningful late-move risk?","Is the main verification gap still decision-material: The main unverified gap is whether any sharp selloff arrives before the exact noon-ET settlement minute.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The main unverified gap is whether any sharp selloff arrives before the exact noon-ET settlement minute.","best_countercase_summary":"The current cushion may simply be large enough that a 90%+ Yes price is fair if BTC stays above 74k into late morning ET.","freshness_sensitive":"yes","freshness_driver":"Live Binance BTCUSDT level and realized volatility into the Apr 16 12:00 ET settlement minute","decision_blockers":["Single-minute settlement path dependence leaves meaningful late-move risk","No independent way to verify absence of an overnight or US-morning crypto selloff catalyst"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.89,"w":"high","thesis":"BTC/USDT is already materially above 72,000 on Binance, so Yes remains likely unless a sharp selloff hits before the exact noon ET settlement minute.","logical_chain":["Verify the contract resolves on the Binance BTC/USDT 12:00 ET 1-minute close above 72,000.","Check direct Binance pricing and recent 1-minute candles to measure current cushion over the threshold.","Assess whether any identified near-term catalyst is likely to erase that cushion before settlement."],"supports":["Binance ticker during the run showed BTCUSDT around 74,620, roughly 3.6% above the threshold.","Recent Binance 1-minute closes were clustered around 74.6k-74.7k, not near 72k."],"disconfirmers":["A single one-minute settlement rule leaves real path risk if BTC sells off sharply at the wrong time.","A sudden overnight or US-morning risk-off move could still push the exact settlement candle below 72,000."],"ambiguities":["No scheduled binary catalyst was identified, so residual risk is mostly unscheduled volatility.","The exact settlement candle had not occurred yet at research time."],"change":"A sharp drawdown toward 72k before noon ET, a clear macro/crypto selloff catalyst, or Binance instability near settlement would make me materially less confident."},"note_deep_dive":{"src":"assumptions/base-rate.md","text":"# Assumption\nBTC will remain within its recent short-horizon trading regime through the April 16 noon ET resolution minute, rather than experiencing a sharp downside break of more than roughly 3% before that time.\n## Why this assumption matters\nThe base-rate case for Yes depends less on a fresh bullish catalyst and more on the tendency for a benchmark asset already trading materially above a threshold to remain above it over a one-day horizon.\n## What this assumption supports\n- A high-probability Yes estimate.\n- A view that the market's 90.5% pricing is broadly reasonable.\n- Reliance on outside-view persistence rather than narrative-driven upside arguments.\n## Evidence or logic behind the assumption\n- Current Binance BTC/USDT is in the mid-74k range, above the 72k threshold by about 2.7%.\n- Recent Binance daily-close analogs show high next-day persistence once BTC is already above 72k.\n- …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

