# Decision-Maker task | case `case-20260416-969f7c01`

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
- case_key: `case-20260416-969f7c01`
- dispatch_id: `refresh-case-20260416-969f7c01-20260416T020025Z`
- question: Will the price of Ethereum be above $2,200 on April 17?
- market_title: Will the price of Ethereum be above $2,200 on April 17?
- market_reference_price: 0.955

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.955,"last_reasoned_price":0.905,"price_delta_pct_points":5.0,"hours_since_last_forecast":0.32,"hours_to_close":37.99,"latest_forecast":{"forecast_id":"dispatch-case-20260416-969f7c01-20260416T013210Z","forecast_prob":0.905,"decision_ts":"2026-04-15T21:41:00-04:00","rationale_summary":"ETH above $2,200 on the April 17 Binance noon minute is still the clear base case, but with fair value around 0.905 and the market already at 0.945, the disciplined output remains watch-only because near-certainty pricin …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.945,"max_reference_price":0.955,"avg_reference_price":0.9466666666666667},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.955","0.045"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Ethereum be above $2,200 on April 17?","market_title":"Will the price of Ethereum be above $2,200 on April 17?","market_reference_price":0.955,"syndicated_probability_low":0.89,"syndicated_probability_high":0.92,"syndicated_probability_midpoint":0.905,"edge_mid_vs_market_pct_points":-5.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small residual UI-versus-API and exact candle-label interpretation risk, but rules are explicit enough for practical use","freshness_sensitive":"yes","freshness_driver":"ETH can still move materially before the Apr 17 12:00 ET resolving minute, so a morning Binance check would meaningfully update odds.","decision_blockers":["No major contract blocker; main blocker is unverified near-settlement price path risk.","Residual minor ambiguity about Binance UI-versus-API representation is not zero.","Actionability is limited because final view remains below market only modestly."],"blockers_require_new_research":"no","disagreement_type":"market_pricing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small residual UI-versus-API and exact candle-label interpretation risk, but rules are explicit enough for practical use","verification_gap_summary":"No near-settlement Apr 17 morning verification yet, so overnight shock risk remains only partially checked.","best_countercase_summary":"A fast overnight or U.S.-morning selloff or Binance-specific wick into the exact noon ET minute could still flip this to No.","main_reason_for_disagreement":"Remaining disagreement is mostly about how much probability to charge for exact-minute crypto tail risk versus treating the current cushion as nearly dispositive.","resolution_mechanics_summary":"Yes resolves only if Binance ETH/USDT's 12:00 ET Apr 17 one-minute candle final close is strictly above 2200.","freshness_sensitive":"yes","freshness_driver":"ETH can still move materially before the Apr 17 12:00 ET resolving minute, so a morning Binance check would meaningfully update odds.","blockers_require_new_research":"no","disagreement_type":"market_pricing","independently_verified_points":["Polymarket rules explicitly resolve on Binance ETH/USDT 12:00 ET 1m final close","Live Binance ETHUSDT remained around 2353 during synthesis-stage check","Binance 24h low was still above 2200 at 2308.5"],"decision_blockers":["No major contract blocker; main blocker is unverified near-settlement price path risk.","Residual minor ambiguity about Binance UI-versus-API representation is not zero."]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nETH resolving above 2200 on the specified April 17 Binance noon-ET 1-minute close remains the clear base case, but the swarm’s mild below-market view survives synthesis: current Binance price context strongly supports Yes, yet a 94.5% market price still looks a bit too aggressive for a venue-specific single-minute crypto close with sub-24h tail risk still live.\n\n## Why this may matter now\n\nMarket implied probability is 0.945. My post-synthesis range is 0.89 to 0.92 Yes. That leaves only a modest below-market edge, not a large one. The likely mispricing is that the market is treating a roughly 6-7% cushion as almost sufficient for near-certainty even though settlement depe …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.9,"w":"high","thesis":"The market is broadly right that Yes is the base case because Binance ETH/USDT is comfortably above 2200, but 94.5% looks slightly too high for a venue-specific one-minute crypto close that is still nearly a day away.","support":["Direct Binance ETHUSDT checks were around 2352.5-2352.6, well above 2200."],"disconfirm":["Crypto can still move more than 6% in less than a day."],"ambiguity":["Whether Binance website chart presentation and public API would ever diverge in a way that matters for settlement."],"change":"I would cut the estimate if Binance ETH/USDT moved materially closer to 2200, if Binance underperformed other spot references, or if an exch …"},{"persona":"base-rate","p":0.88,"w":"medium","thesis":"Yes is still the right side because ETH/USDT is materially above 2200 close to resolution, but the market slightly overstates certainty for a one-minute Binance-close contract.","support":["ETH/USDT contextual spot was around the mid-2300s during research, leaving a roughly 6-7% cushion above 2200."],"disconfirm":["Settlement depends on a single Binance one-minute close at noon ET, so a brief downside move is enough for No."],"ambiguity":["Direct live extraction from Binance was limited, leaving small residual ET-to-candle mapping uncertainty."],"change":"A fresh check showing ETH/USDT near or below 2200 on Apr 17 morning, or Binance-specific operational problems near settlement, would move th …"},{"persona":"catalyst-hunter","p":0.91,"w":"medium","thesis":"ETH is likely to stay above 2200 at the Binance noon ET resolving minute, but the single-minute close mechanic keeps residual downside timing risk nontrivial.","support":["Binance ETH/USDT last price sampled at 2353.84, well above 2200."],"disconfirm":["Single-minute resolution creates path-sensitive downside risk even if ETH trades above 2200 most of the time."],"ambiguity":["Whether any unscheduled macro or crypto headline emerges before the resolving window."],"change":"A decisive break toward/below 2300, a new bearish catalyst, or Binance-specific instability near resolution would cut the Yes probability ma …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: ETH can still move materially before the Apr 17 12:00 ET resolving minute, so a morning Binance check would meaningfully update odds.?","How decision-relevant is the remaining contract/source-of-truth ambiguity: small residual UI-versus-API and exact candle-label interpretation risk, but rules are explicit enough for practical use?","Are the current blockers still material to final judgment: No major contract blocker; main blocker is unverified near-settlement price path risk.?","Is the main verification gap still decision-material: No near-settlement Apr 17 morning verification yet, so overnight shock risk remains only partially checked.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"No near-settlement Apr 17 morning verification yet, so overnight shock risk remains only partially checked.","best_countercase_summary":"A fast overnight or U.S.-morning selloff or Binance-specific wick into the exact noon ET minute could still flip this to No.","freshness_sensitive":"yes","freshness_driver":"ETH can still move materially before the Apr 17 12:00 ET resolving minute, so a morning Binance check would meaningfully update odds.","decision_blockers":["No major contract blocker; main blocker is unverified near-settlement price path risk.","Residual minor ambiguity about Binance UI-versus-API representation is not zero."]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.9,"w":"high","thesis":"The market is broadly right that Yes is the base case because Binance ETH/USDT is comfortably above 2200, but 94.5% looks slightly too high for a venue-specific one-minute crypto close that is still nearly a day away.","logical_chain":["Start from the market prior of 94.5% Yes.","Check the governing source of truth and exact settlement mechanics on Polymarket rules.","Verify current Binance ETH/USDT level and short-horizon context directly on Binance data."],"supports":["Direct Binance ETHUSDT checks were around 2352.5-2352.6, well above 2200.","Binance 24h low in the check was 2308.5, still above the threshold."],"disconfirmers":["Crypto can still move more than 6% in less than a day.","Settlement is venue-specific and minute-specific, so a Binance-only wick or operational anomaly could matter."],"ambiguities":["Whether Binance website chart presentation and public API would ever diverge in a way that matters for settlement.","How much tail-risk should be charged over the remaining sub-24h window."],"change":"I would cut the estimate if Binance ETH/USDT moved materially closer to 2200, if Binance underperformed other spot references, or if an exchange-specific operational/data issue app …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

