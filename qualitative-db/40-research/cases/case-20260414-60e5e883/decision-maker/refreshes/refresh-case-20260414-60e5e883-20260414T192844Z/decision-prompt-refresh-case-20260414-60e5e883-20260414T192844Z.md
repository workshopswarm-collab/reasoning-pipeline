# Decision-Maker task | case `case-20260414-60e5e883`

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
- case_key: `case-20260414-60e5e883`
- dispatch_id: `refresh-case-20260414-60e5e883-20260414T192844Z`
- question: Will the price of Bitcoin be above $70,000 on April 17?
- market_title: Will the price of Bitcoin be above $70,000 on April 17?
- market_reference_price: 0.9365

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.9365,"last_reasoned_price":0.885,"price_delta_pct_points":5.1,"hours_since_last_forecast":0.25,"hours_to_close":68.52,"latest_forecast":{"forecast_id":"dispatch-case-20260414-60e5e883-20260414T190542Z","forecast_prob":0.885,"decision_ts":"2026-04-14T15:14:00-04:00","rationale_summary":"Bitcoin is likely to finish above $70,000 on the April 17 noon ET Binance minute because current same-venue pricing remains materially above the strike, but the market's 92.5% price is still modestly too confident for a …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.9285,"max_reference_price":0.9365,"avg_reference_price":0.9291666666666667},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.936","0.064"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $70,000 on April 17?","market_title":"Will the price of Bitcoin be above $70,000 on April 17?","market_reference_price":0.9365,"syndicated_probability_low":0.87,"syndicated_probability_high":0.9,"syndicated_probability_midpoint":0.885,"edge_mid_vs_market_pct_points":-5.1,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"narrow minute-close/timezone/venue mechanics create small operational interpretation risk but rules are mostly explicit","freshness_sensitive":"yes","freshness_driver":"BTC can reprice several percent in under three days and the contract resolves on one exact Apr 17 noon ET minute","decision_blockers":["No fresh synthesis-stage live price/ladder refresh beyond upstream checks","Exact-minute Binance settlement structure leaves residual path and venue-specific risk","Apparent edge versus market is modest and not strongly independently verified"],"blockers_require_new_research":"no","disagreement_type":"market_pricing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"narrow minute-close/timezone/venue mechanics create small operational interpretation risk but rules are mostly explicit","verification_gap_summary":"No fresh independent live market or volatility check beyond upstream lane verification was obtained in synthesis.","best_countercase_summary":"A normal crypto selloff or badly timed noon-minute wick on Binance can still flip this narrow contract despite spot being comfortably above 70k now.","main_reason_for_disagreement":"how much probability discount to apply for exact-minute Binance settlement and ordinary 3-day BTC volatility","resolution_mechanics_summary":"Yes requires the Binance BTC/USDT 1-minute candle closing at 12:00 PM ET on Apr 17 to finish strictly above 70000.","freshness_sensitive":"yes","freshness_driver":"BTC can reprice several percent in under three days and the contract resolves on one exact Apr 17 noon ET minute","blockers_require_new_research":"no","disagreement_type":"market_pricing","independently_verified_points":["Polymarket-style contract mechanics are consistently described as Binance BTC/USDT 12:00 PM ET 1-minute close above 70000","All five raw persona findings support Yes as the base case and center only modestly below market","Upstream direct checks consistently placed Binance BTC/USDT around 74.2k-74.3k on Apr 14, about 6% above strike"],"decision_blockers":["No fresh synthesis-stage live price/ladder refresh beyond upstream checks","Exact-minute Binance settlement structure leaves residual path and venue-specific risk"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBTC being above $70,000 on the April 17 settlement print is still the base case, but the market’s 92.5% Yes price looks modestly too confident for a contract that resolves on one exact Binance BTC/USDT 1-minute close at 12:00 PM ET; my post-synthesis view is 0.87 to 0.90 Yes, with only medium independent verification and a mild compression back toward the market relative to the swarm’s more bearish center.\n\n## Why this may matter now\n\nMarket implies 92.5% Yes. My synthesized estimate is 0.87 to 0.90 Yes. That is a small below-market edge at most, not a strong actionable dislocation. The likely mispricing, if any, is that the market slightly underweights ordinary BTC drawd …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.89,"w":"high","thesis":"The market's high-probability Yes view is broadly efficient because Binance BTC/USDT is currently well above 70k, but the 93% price is slightly rich once short-horizon volatility and the single-minute settlement rule are …","support":["Binance BTCUSDT spot was about 74293.57, roughly 6.1% above the 70000 threshold."],"disconfirm":["BTC can fall more than 6% in three days."],"ambiguity":["Whether short-horizon macro or crypto-specific news hits before the Apr 17 noon ET settlement window."],"change":"I would move materially lower if Binance BTCUSDT fell back toward or below 72k, if neighboring strikes repriced sharply lower, or if Binance …"},{"persona":"variant-view","p":0.84,"w":"medium","thesis":"BTC above 70k on Binance at settlement is still more likely than not, but the market is somewhat overconfident because the contract resolves on one exact Binance BTCUSDT noon-ET minute close rather than a broader spot or …","support":["Binance BTCUSDT was trading around 74.3k on 2026-04-14, already above the 70k strike."],"disconfirm":["A 6% cushion with less than three days left is substantial, so the market's high Yes pricing is not irrational."],"ambiguity":["The contract wording is specific, but timezone-to-candle mapping must still be handled carefully at resolution time."],"change":"I would move closer to the market if BTC remains well above the strike into late April 16 / early April 17 with lower volatility, and more b …"},{"persona":"risk-manager","p":0.88,"w":"medium","thesis":"Yes is still the base case, but the 92.5%-93% market price looks slightly too confident for a narrow Binance-specific noon ET minute-close contract; 88% is a better estimate.","support":["Binance direct ticker check showed BTCUSDT around 74,163, comfortably above 70,000."],"disconfirm":["The contract resolves on one exact Binance minute close, so a brief but badly timed drawdown could still settle No."],"ambiguity":["Whether any close-to-settlement Binance display/finalization quirk could matter in practice."],"change":"I would move toward the market if BTC stays comfortably above the mid-74k area into late April 16 with clean Binance prints; I would move lo …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: BTC can reprice several percent in under three days and the contract resolves on one exact Apr 17 noon ET minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: narrow minute-close/timezone/venue mechanics create small operational interpretation risk but rules are mostly explicit?","Are the current blockers still material to final judgment: No fresh synthesis-stage live price/ladder refresh beyond upstream checks?","Is the main verification gap still decision-material: No fresh independent live market or volatility check beyond upstream lane verification was obtained in synthesis.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"No fresh independent live market or volatility check beyond upstream lane verification was obtained in synthesis.","best_countercase_summary":"A normal crypto selloff or badly timed noon-minute wick on Binance can still flip this narrow contract despite spot being comfortably above 70k now.","freshness_sensitive":"yes","freshness_driver":"BTC can reprice several percent in under three days and the contract resolves on one exact Apr 17 noon ET minute","decision_blockers":["No fresh synthesis-stage live price/ladder refresh beyond upstream checks","Exact-minute Binance settlement structure leaves residual path and venue-specific risk"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.89,"w":"high","thesis":"The market's high-probability Yes view is broadly efficient because Binance BTC/USDT is currently well above 70k, but the 93% price is slightly rich once short-horizon volatility and the single-minute settlement rule are fully accounted for.","logical_chain":["Start from the market's 92.5%-93% Yes prior because the strike ladder contains information about the expected BTC distribution.","Check the governing source directly: Binance spot and recent klines show BTC materially above 70000 and trading in a regime where 70000 is below the recent center of price action.","Apply a modest discount for ordinary crypto volatility and the narrow single-minute settlement mechanic, yielding an 89% Yes estimate rather than the full market price."],"supports":["Binance BTCUSDT spot was about 74293.57, roughly 6.1% above the 70000 threshold.","Recent Binance daily closes were mostly above 70000, with recent highs above 76000."],"disconfirmers":["BTC can fall more than 6% in three days.","The contract settles on a single Binance 1-minute close at noon ET, adding timing/path risk."],"ambiguities":["Whether short-horizon macro or crypto-specific news hits before the Apr 17 noon ET settlement window.","How much extra probability mass the market is assigning to current regime persistence versus pure spot anchoring."],"change":"I would move materially lower if Binance BTCUSDT fell back toward or below 72k, if neighboring strikes repriced sharply lower, or if Binance-specific settlement-risk issues emerged …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

