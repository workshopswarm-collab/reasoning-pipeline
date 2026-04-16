# Decision-Maker task | case `case-20260415-540d9abf`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Important: the runtime hydrates many metadata / execution / risk / audit defaults after parsing. Focus your output effort on judgment-bearing fields rather than boilerplate runtime-owned fields.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
You may use only web_search, web_fetch in this turn.
Stay within: searches<=5, fetches<=4, min_distinct_source_families=3 when feasible.
Choose sources independently and prefer primary, official, and resolution-relevant sources.
Do not count multiple pages from the same source family as real diversity.

## Case
- case_key: `case-20260415-540d9abf`
- dispatch_id: `refresh-case-20260415-540d9abf-20260415T235725Z`
- question: Will the price of Solana be above $80 on April 19?
- market_title: Will the price of Solana be above $80 on April 19?
- market_reference_price: 0.9

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.9,"last_reasoned_price":0.835,"price_delta_pct_points":6.5,"hours_since_last_forecast":0.04,"hours_to_close":88.04,"latest_forecast":{"forecast_id":"dispatch-case-20260415-540d9abf-20260415T234706Z","forecast_prob":0.835,"decision_ts":"2026-04-15T19:55:00-04:00","rationale_summary":"SOL is still more likely than not to finish above $80 on the April 19 Binance noon minute, but with fair value closer to 0.835 than the 0.90 market and meaningful exact-minute downside tail still live, the disciplined ou …"},"snapshot_summary":{"snapshot_count":2,"min_reference_price":0.9,"max_reference_price":0.9,"avg_reference_price":0.9},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.9","0.1"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will the price of Solana be above $80 on April 19?","market_title":"Will the price of Solana be above $80 on April 19?","market_reference_price":0.9,"syndicated_probability_low":0.8,"syndicated_probability_high":0.87,"syndicated_probability_midpoint":0.835,"edge_mid_vs_market_pct_points":-6.5,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small residual Binance UI vs API candle-mapping ambiguity","freshness_sensitive":"yes","freshness_driver":"Binance SOL/USDT price path into the exact Apr 19 noon ET settlement minute","decision_blockers":["Single-minute settlement makes ordinary crypto volatility materially relevant","Verification is strong on mechanics but only medium on independent edge confirmation","Minor UI-versus-API implementation ambiguity remains"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small residual Binance UI vs API candle-mapping ambiguity","verification_gap_summary":"The key remaining gap is short-horizon downside/timestamp volatility into the exact Apr 19 noon ET minute.","best_countercase_summary":"A normal crypto selloff or brief noon-minute dip can still push a single-print settlement below 80 despite current spot above strike.","main_reason_for_disagreement":"Remaining disagreement is mostly about how much to discount confidence for single-minute path risk versus current cushion.","resolution_mechanics_summary":"Yes resolves only if Binance SOL/USDT's Apr 19 12:00 ET 1-minute candle final close is strictly above 80.","freshness_sensitive":"yes","freshness_driver":"Binance SOL/USDT price path into the exact Apr 19 noon ET settlement minute","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket rules explicitly resolve on Binance SOL/USDT 1-minute 12:00 ET close","Current Binance SOLUSDT spot is about 84.92, above the 80 threshold","Recent Binance 24h low was about 82.65, still above 80"],"decision_blockers":["Single-minute settlement makes ordinary crypto volatility materially relevant","Verification is strong on mechanics but only medium on independent edge confirmation"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nSOL > $80 on the April 19 noon-ET Binance 1-minute close is still more likely than not, but the market’s ~90% Yes price looks somewhat rich for a single-minute settlement several days out in a volatile asset; my post-synthesis view is a modestly compressed Yes range centered below market.\n\n## Why this may matter now\n\nMarket-implied probability is about 0.90. My syndicated probability range is 0.80 to 0.87. That is a modest bearish-to-market compression, so the edge versus market looks marginal rather than actionable. The likely mispricing is overconfidence in translating a mid-80s current spot price into near-certainty for a single future one-minute Binance close.\n\n## Shi …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.84,"w":"medium","thesis":"The market is directionally right that SOL > 80 on Apr 19 noon ET is likely, but ~90% looks somewhat rich for a single Binance one-minute close several days out; 84% Yes is a better estimate.","support":["Binance SOLUSDT spot was around 84.86-84.87 at analysis time."],"disconfirm":["The contract resolves on a single one-minute Binance close several days away, so a 6% downside move is still plausible."],"ambiguity":["No separate Binance documentation source was found in-run to restate the ET mapping in Polymarket's terms."],"change":"A move back toward 80, a broader crypto selloff, or evidence of unusual Binance/noon-print behavior would make me less bullish; continued tr …"},{"persona":"risk-manager","p":0.78,"w":"medium","thesis":"SOL above 80 on April 19 is more likely than not because Binance spot is already above 80, but the market is overconfident given single-minute settlement and short-horizon crypto volatility.","support":["Live Binance SOLUSDT spot checked in-run around 84.93, already above 80."],"disconfirm":["The contract resolves on one exact future minute close, so path risk is materially higher than a broad daily-price framing suggests."],"ambiguity":["Minor ambiguity remains between Binance UI candle labeling and API open-time representation."],"change":"A move back toward or below 80 on Binance, broader crypto weakness, or any Binance settlement-surface irregularity would push the estimate d …"},{"persona":"base-rate","p":0.93,"w":"medium","thesis":"SOL is already trading comfortably above 80 on Binance with only a short horizon remaining, so the outside-view favors a Yes resolution unless a meaningful downside shock hits before the exact noon-ET settlement minute.","support":["Direct Binance checks during the run showed SOLUSDT around 84.84, several dollars above the 80 threshold."],"disconfirm":["A roughly 5% crypto drawdown before the exact settlement minute would put the contract at risk."],"ambiguity":["Whether Binance UI presentation could differ in any edge case from API-verified kline data, though no such divergence was found."],"change":"A move of SOL back near or below 80 before settlement, SOL-specific negative news, or evidence of meaningful Binance UI/API divergence would …"}],"selected_assumption_snippets":[{"src":"assumptions/risk-manager.md","text":"# Assumption\nThe current ~6% cushion above 80 on Binance SOL/USDT is large enough that ordinary short-horizon volatility is more likely than not to leave the 2026-04-19 12:00 ET close above 80.\n## Why this assumption matters\nThe market is pricing Yes around 90%, which implies not just directional bullishness but confidence that path risk over the next few days is modest. If the volatility buffer assumption is wrong, the market may be overconfident even if SOL is currently above 80.\n## What this …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: Binance SOL/USDT price path into the exact Apr 19 noon ET settlement minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: small residual Binance UI vs API candle-mapping ambiguity?","Are the current blockers still material to final judgment: Single-minute settlement makes ordinary crypto volatility materially relevant?","Is the main verification gap still decision-material: The key remaining gap is short-horizon downside/timestamp volatility into the exact Apr 19 noon ET minute.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The key remaining gap is short-horizon downside/timestamp volatility into the exact Apr 19 noon ET minute.","best_countercase_summary":"A normal crypto selloff or brief noon-minute dip can still push a single-print settlement below 80 despite current spot above strike.","freshness_sensitive":"yes","freshness_driver":"Binance SOL/USDT price path into the exact Apr 19 noon ET settlement minute","decision_blockers":["Single-minute settlement makes ordinary crypto volatility materially relevant","Verification is strong on mechanics but only medium on independent edge confirmation"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"base-rate","p":0.93,"w":"medium","thesis":"SOL is already trading comfortably above 80 on Binance with only a short horizon remaining, so the outside-view favors a Yes resolution unless a meaningful downside shock hits before the exact noon-ET settlement minute.","logical_chain":["Polymarket rules define the outcome by the Binance SOL/USDT 12:00 ET one-minute close on April 19.","Current Binance price context shows SOL already above 80 by a meaningful cushion.","For a short-dated threshold market already in the money, base rates favor persistence unless a specific downside catalyst appears."],"supports":["Direct Binance checks during the run showed SOLUSDT around 84.84, several dollars above the 80 threshold.","Recent observed Binance daily closes were all above 80."],"disconfirmers":["A roughly 5% crypto drawdown before the exact settlement minute would put the contract at risk.","The market resolves on one exact Binance one-minute close, so transient timing volatility matters."],"ambiguities":["Whether Binance UI presentation could differ in any edge case from API-verified kline data, though no such divergence was found.","How much short-horizon crypto volatility will materialize before April 19 noon ET."],"change":"A move of SOL back near or below 80 before settlement, SOL-specific negative news, or evidence of meaningful Binance UI/API divergence would reduce confidence materially."},"note_deep_dive":{"src":"assumptions/risk-manager.md","text":"# Assumption\nThe current ~6% cushion above 80 on Binance SOL/USDT is large enough that ordinary short-horizon volatility is more likely than not to leave the 2026-04-19 12:00 ET close above 80.\n## Why this assumption matters\nThe market is pricing Yes around 90%, which implies not just directional bullishness but confidence that path risk over the next few days is modest. If the volatility buffer assumption is wrong, the market may be overconfident even if SOL is currently above 80.\n## What this assumption supports\n- A Yes-leaning probability estimate above 50%\n- A view that current spot level contains meaningful information for the final noon ET candle\n- A view that the right disagreement, if any, is about confidence calibration rather than direction\n## Evidence or logic behind the assumption\n- Current Binance SOLUSDT spot observed in-run was about 84.93, already above the threshold.\n- R …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

