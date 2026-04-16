# Decision-Maker task | case `case-20260415-c8d6e83e`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Important: the runtime hydrates many metadata / execution / risk / audit defaults after parsing. Focus your output effort on judgment-bearing fields rather than boilerplate runtime-owned fields.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
Do not use tools for additional research, browsing, or file reads during this decision turn. The runtime inspects the session and will fail the run if tool use occurs.

## Case
- case_key: `case-20260415-c8d6e83e`
- dispatch_id: `refresh-case-20260415-c8d6e83e-20260415T202231Z`
- question: Will the price of Bitcoin be above $68,000 on April 20?
- market_title: Will the price of Bitcoin be above $68,000 on April 20?
- market_reference_price: 0.9715

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.9715,"last_reasoned_price":0.92,"price_delta_pct_points":5.1,"hours_since_last_forecast":4.91,"hours_to_close":115.62,"latest_forecast":{"forecast_id":"dispatch-case-20260415-c8d6e83e-20260415T151858Z","forecast_prob":0.92,"decision_ts":"2026-04-15T11:28:00-04:00","rationale_summary":"BTC is still highly likely to finish above $68,000 on the April 20 Binance noon minute, but with fair value closer to 0.92 than the 0.955 market and exact-minute downside-path risk still nonzero, the disciplined output r …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.963,"max_reference_price":0.9715,"avg_reference_price":0.966375},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.9745","0.0255"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
- Do not use tools for additional research or file inspection during this turn; the runtime will treat tool use as a policy violation.
- If the compact bundle feels too compressed, use the bounded expanded fallback below before assuming broader case access is needed.
- If the compact bundle is insufficient for a responsible decision, express that with `needs_more_research`, `needs_market_update`, `watch_only`, or `forbidden` as appropriate.
- Do not turn this stage into an unbounded second synthesis pass.

## Structured selected-input bundle for this run
```json
{"verification_mode":"not_ready_reopen_recommended","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $68,000 on April 20?","market_title":"Will the price of Bitcoin be above $68,000 on April 20?","market_reference_price":0.9715,"syndicated_probability_low":0.9,"syndicated_probability_high":0.94,"syndicated_probability_midpoint":0.92,"edge_mid_vs_market_pct_points":-5.1,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Residual Binance website candle vs API/operational minute-mapping sensitivity, though wording is otherwise clear.","freshness_sensitive":"yes","freshness_driver":"BTC can reprice materially within five days, and the contract depends on one exact April 20 noon ET Binance minute.","decision_blockers":["No strong independently verified basis for a large edge versus the market.","Outcome remains sensitive to short-horizon BTC downside volatility and one-minute settlement mechanics.","Need fresher pre-settlement spot/volatility check if acting materially closer to resolution."],"blockers_require_new_research":"yes","disagreement_type":"market_pricing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"yes","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Residual Binance website candle vs API/operational minute-mapping sensitivity, though wording is otherwise clear.","verification_gap_summary":"The key remaining gap is fresh independent evidence on short-horizon downside-tail risk between now and the exact April 20 noon ET settlement minute.","best_countercase_summary":"An ordinary crypto risk-off move or settlement-minute downtick could still erase the current cushion and make 95%+ too confident.","main_reason_for_disagreement":"The main disagreement is how much single-minute settlement and short-horizon BTC tail risk should discount a large current spot cushion.","resolution_mechanics_summary":"Yes resolves only if Binance BTC/USDT's April 20 12:00 ET one-minute candle final Close is strictly above 68,000.","freshness_sensitive":"yes","freshness_driver":"BTC can reprice materially within five days, and the contract depends on one exact April 20 noon ET Binance minute.","blockers_require_new_research":"yes","disagreement_type":"market_pricing","independently_verified_points":["Polymarket rules explicitly use the Binance BTC/USDT 12:00 ET one-minute candle final Close.","Current Binance BTC/USDT spot is about 74,038-74,044, leaving roughly a 6k cushion over 68,000.","The live market strip still prices the 68k line around 96% Yes."],"decision_blockers":["No strong independently verified basis for a large edge versus the market.","Outcome remains sensitive to short-horizon BTC downside volatility and one-minute settlement mechanics."]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{},"selected_persona_sidecars":[{"persona":"market-implied","p":0.93,"w":"high","thesis":"Market is directionally right: Binance BTC/USDT is comfortably above 68000, but single-minute settlement and crypto downside tails justify a small discount to the market's near-certainty.","support":["Binance spot was about 74044 on April 15, leaving roughly a 6000-point cushion above the strike."],"disconfirm":["The contract resolves on one exact Binance one-minute close, so a sharp intraday downtick or wick could still flip it."],"ambiguity":["How much short-horizon downside volatility will emerge over the next five days."],"change":"A sharp move toward 70k or below, a new macro/crypto shock, or Binance operational irregularities near resolution would lower the estimate m …"},{"persona":"base-rate","p":0.89,"w":"medium","thesis":"Yes is still highly likely because BTC is materially above 68k with only about five days left, but the market is a bit too close to certainty for an exact-minute crypto threshold contract.","support":["Binance BTCUSDT spot was about 74,044 when checked, leaving about a 6k cushion above 68,000."],"disconfirm":["Crypto can still realize sharp multi-day drawdowns, and this contract settles on one exact minute."],"ambiguity":["How much additional downside volatility emerges between now and the final 24 hours."],"change":"I would move higher if BTC stays comfortably above 72k-73k into the final 24-48 hours with lower volatility, and lower if BTC loses 70k or i …"}],"selected_assumption_snippets":[],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.93,"w":"high","thesis":"Market is directionally right: Binance BTC/USDT is comfortably above 68000, but single-minute settlement and crypto downside tails justify a small discount to the market's near-certainty.","logical_chain":["Start from the market-implied probability of about 95.5%.","Check the governing venue directly: Binance BTC/USDT is around 74044, well above 68000.","Verify recent realized context including ET-noon timing; recent comparable closes are also well above the strike."],"supports":["Binance spot was about 74044 on April 15, leaving roughly a 6000-point cushion above the strike.","Recent sampled Binance daily closes and ET-noon context were all above 68000."],"disconfirmers":["The contract resolves on one exact Binance one-minute close, so a sharp intraday downtick or wick could still flip it.","BTC can move more than 8% over a few days during risk-off episodes."],"ambiguities":["How much short-horizon downside volatility will emerge over the next five days.","Whether the final noon ET minute could be unusually noisy relative to surrounding trade."],"change":"A sharp move toward 70k or below, a new macro/crypto shock, or Binance operational irregularities near resolution would lower the estimate materially."}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

