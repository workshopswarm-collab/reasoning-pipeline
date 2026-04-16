# Decision-Maker task | case `case-20260414-e15c72fe`

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
- case_key: `case-20260414-e15c72fe`
- dispatch_id: `refresh-case-20260414-e15c72fe-20260414T201353Z`
- question: Will the price of Bitcoin be above $70,000 on April 20?
- market_title: Will the price of Bitcoin be above $70,000 on April 20?
- market_reference_price: 0.855

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.855,"last_reasoned_price":0.805,"price_delta_pct_points":5.0,"hours_since_last_forecast":0.58,"hours_to_close":139.77,"latest_forecast":{"forecast_id":"dispatch-case-20260414-e15c72fe-20260414T193100Z","forecast_prob":0.805,"decision_ts":"2026-04-14T15:39:00-04:00","rationale_summary":"Bitcoin is likely to finish above $70,000 on the April 20 noon ET Binance minute because current same-venue pricing remains materially above the strike, but the market's 84.5% price is still somewhat too confident for a …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.85,"max_reference_price":0.855,"avg_reference_price":0.8504166666666667},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.855","0.145"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $70,000 on April 20?","market_title":"Will the price of Bitcoin be above $70,000 on April 20?","market_reference_price":0.855,"syndicated_probability_low":0.78,"syndicated_probability_high":0.83,"syndicated_probability_midpoint":0.805,"edge_mid_vs_market_pct_points":-5.0,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Binance website/display-surface implementation at the exact resolving minute is not fully specified beyond rules text","freshness_sensitive":"yes","freshness_driver":"BTC can move several percent in days and the contract resolves on one exact minute on April 20.","decision_blockers":["No strong independent verification of short-horizon downside probability beyond spot-distance reasoning","Single-minute Binance-only settlement leaves residual operational and path-risk fragility","Any meaningful move back toward 71k-70k before April 20 would quickly change the estimate"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Binance website/display-surface implementation at the exact resolving minute is not fully specified beyond rules text","verification_gap_summary":"No independent volatility study or same-day minute-fragility evidence was added beyond spot/rules verification.","best_countercase_summary":"A plausible 5-6% downside move or Binance-specific dislocation into the exact resolving minute could still flip the market to No.","main_reason_for_disagreement":"How much to discount current spot cushion for exact-minute settlement fragility.","resolution_mechanics_summary":"Yes requires the Binance BTC/USDT 12:00 PM ET 1-minute candle on April 20 to have a final Close strictly above 70,000.","freshness_sensitive":"yes","freshness_driver":"BTC can move several percent in days and the contract resolves on one exact minute on April 20.","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Contract resolves on Binance BTC/USDT 1-minute candle final Close at 12:00 PM ET on April 20","12:00 PM ET on 2026-04-20 maps to 16:00 UTC","Fresh Binance BTCUSDT spot remained around 74,038 during synthesis-stage check, still materially above 70,000"],"decision_blockers":["No strong independent verification of short-horizon downside probability beyond spot-distance reasoning","Single-minute Binance-only settlement leaves residual operational and path-risk fragility"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBitcoin is still more likely than not to settle above $70,000 on the April 20 Binance noon-ET minute close, but the swarm’s below-market skepticism survives synthesis: the current spot cushion supports Yes, while the single-minute single-venue settlement mechanic keeps confidence below the market’s 84.5% baseline.\n\n## Why this may matter now\n\nMarket implied is 0.845; my post-synthesis range is 0.78 to 0.83. That leaves no clean actionable edge versus market after verification; at most it is a marginal below-market lean. Main possible mispricing is that traders may be slightly underweighting the fragility of a single Binance noon-ET minute close, but the current spot cushi …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.82,"w":"high","thesis":"The market is mostly efficient: Binance BTC/USDT is currently comfortably above 70k, so Yes should be favored, but the exact noon-ET one-minute-close mechanic merits a small discount versus the market's mid/high-80s conf …","support":["Direct Binance spot check showed BTCUSDT around 74,258, materially above the 70,000 threshold."],"disconfirm":["The contract settles on one exact Binance 1-minute close at noon ET, so a single volatile minute can flip the result."],"ambiguity":["How volatile the exact noon ET minute is likely to be on April 20."],"change":"I would move lower if BTC falls back toward the low-71k/high-70k area, if Binance-specific risks emerge, or if closer-to-resolution minute-l …"},{"persona":"base-rate","p":0.76,"w":"medium","thesis":"Yes is more likely than not because BTC is currently well above 70k on Binance and the horizon is short, but the market overstates confidence because settlement depends on a single 12:00 ET one-minute close.","support":["Binance BTC/USDT spot was about 74.25k during research, leaving roughly a 4.25k cushion above the threshold."],"disconfirm":["The contract resolves on one exact future minute, not on a daily close or average price."],"ambiguity":["Whether Binance website presentation could matter in edge cases differently from API retrieval."],"change":"I would cut the estimate if BTC loses the 70k regime before settlement or if contract-specific timing/source interpretation risk proves larg …"},{"persona":"risk-manager","p":0.79,"w":"medium","thesis":"Yes is favored because Binance BTC/USDT is currently comfortably above 70000, but the market is slightly overconfident for a single-minute timestamp-specific contract.","support":["Binance is the named settlement venue and BTC/USDT the named pair."],"disconfirm":["Recent BTC daily ranges on Binance were still large enough that a sub-70k noon print remains plausible."],"ambiguity":["No stronger independent causal catalyst review was obtained beyond direct price and contract checks."],"change":"I would cut the estimate if BTC trades persistently near 71k/70k before April 20 or if Binance shows venue-specific anomalies; I would move …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: BTC can move several percent in days and the contract resolves on one exact minute on April 20.?","How decision-relevant is the remaining contract/source-of-truth ambiguity: Binance website/display-surface implementation at the exact resolving minute is not fully specified beyond rules text?","Are the current blockers still material to final judgment: No strong independent verification of short-horizon downside probability beyond spot-distance reasoning?","Is the main verification gap still decision-material: No independent volatility study or same-day minute-fragility evidence was added beyond spot/rules verification.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"No independent volatility study or same-day minute-fragility evidence was added beyond spot/rules verification.","best_countercase_summary":"A plausible 5-6% downside move or Binance-specific dislocation into the exact resolving minute could still flip the market to No.","freshness_sensitive":"yes","freshness_driver":"BTC can move several percent in days and the contract resolves on one exact minute on April 20.","decision_blockers":["No strong independent verification of short-horizon downside probability beyond spot-distance reasoning","Single-minute Binance-only settlement leaves residual operational and path-risk fragility"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.82,"w":"high","thesis":"The market is mostly efficient: Binance BTC/USDT is currently comfortably above 70k, so Yes should be favored, but the exact noon-ET one-minute-close mechanic merits a small discount versus the market's mid/high-80s confidence.","logical_chain":["Start from the market's 84.5% prior and take it seriously because short-dated threshold markets often encode useful strike-distance information.","Verify the governing rules and exact settlement source: Binance BTC/USDT 1-minute candle at 12:00 PM ET on April 20.","Check the exact venue's current price and recent context; Binance spot is comfortably above 70k and recent closes are above the threshold."],"supports":["Direct Binance spot check showed BTCUSDT around 74,258, materially above the 70,000 threshold.","Recent Binance daily closes in the sampled window were all above 70,000."],"disconfirmers":["The contract settles on one exact Binance 1-minute close at noon ET, so a single volatile minute can flip the result.","A roughly 6% drawdown from current spot would be enough to settle No and is plausible over six days in BTC."],"ambiguities":["How volatile the exact noon ET minute is likely to be on April 20.","Whether any Binance UI/data-surface quirks could matter for practical settlement interpretation."],"change":"I would move lower if BTC falls back toward the low-71k/high-70k area, if Binance-specific risks emerge, or if closer-to-resolution minute-level checks show materially higher noon- …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

