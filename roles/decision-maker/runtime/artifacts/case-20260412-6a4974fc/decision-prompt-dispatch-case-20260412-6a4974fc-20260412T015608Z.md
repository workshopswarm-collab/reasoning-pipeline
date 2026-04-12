# Decision-Maker task | case `case-20260412-6a4974fc`

You are the separate `decision-maker` agent. Return the final decision packet JSON only.
Do not wrap the JSON in markdown fences. Do not prepend explanation.
The runtime will persist artifacts and post visible Telegram markers; you should focus on judgment quality and packet correctness.
The runtime has already deterministically bounded your verification context. Use the compact selected bundle below rather than trying to reconstruct the whole case tree.
Treat `structured_handoff_primary` as the main starting point for synthesis->decision transfer. Treat `prose_fallback` only as fallback context on those compact fields.
Synthesis, researcher findings, sidecars, and handoff prose are advisory inputs only. They are not determinative of the final decision.
Your job is to critically evaluate those upstream materials, decide how much weight they deserve, and form your own final judgment.
You may use only web_search, web_fetch in this turn.
Stay within: searches<=4, fetches<=3, min_distinct_source_families=2 when feasible.
Choose sources independently and prefer primary, official, and resolution-relevant sources.
Do not count multiple pages from the same source family as real diversity.

## Case
- case_key: `case-20260412-6a4974fc`
- dispatch_id: `dispatch-case-20260412-6a4974fc-20260412T015608Z`
- question: Will the price of Bitcoin be above $66,000 on April 12?
- market_title: Will the price of Bitcoin be above $66,000 on April 12?
- market_reference_price: 0.953

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
{"verification_mode":"targeted_escalation","verification_triggers":["freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $66,000 on April 12?","market_title":"Will the price of Bitcoin be above $66,000 on April 12?","market_reference_price":0.953,"syndicated_probability_low":0.93,"syndicated_probability_high":0.97,"syndicated_probability_midpoint":0.95,"edge_mid_vs_market_pct_points":-0.3,"relation_to_market":"crosses_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small Binance web-UI versus API interpretation residual despite clear rule text","freshness_sensitive":"yes","freshness_driver":"BTC intraday volatility before the exact 12:00 ET / 16:00 UTC settlement minute","decision_blockers":["The final settling candle was still in the future at analysis time","Residual single-minute path dependence and Binance-specific operational risk remain"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"unclear","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small Binance web-UI versus API interpretation residual despite clear rule text","verification_gap_summary":"The exact settling 16:00 UTC candle had not yet occurred, so residual path risk could not be eliminated.","best_countercase_summary":"A sharp pre-noon selloff or Binance-specific settlement-surface anomaly could still flip an otherwise comfortable Yes.","main_reason_for_disagreement":"Remaining disagreement is mostly about how much tail risk to assign to a narrow one-minute crypto settlement.","resolution_mechanics_summary":"Resolve from the Binance BTC/USDT candle opening at 12:00 ET / 16:00 UTC using that candle's final Close.","freshness_sensitive":"yes","freshness_driver":"BTC intraday volatility before the exact 12:00 ET / 16:00 UTC settlement minute","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket rules explicitly use Binance BTC/USDT 12:00 ET 1m candle final Close","12:00 ET on 2026-04-12 maps to 16:00 UTC","Binance BTCUSDT remained around 71.6k during synthesis checks, far above 66k"],"decision_blockers":["The final settling candle was still in the future at analysis time","Residual single-minute path dependence and Binance-specific operational risk remain"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBTC is still very likely to resolve Yes on the Binance BTC/USDT 12:00 ET one-minute close above 66,000, but the synthesis view remains modestly below the most aggressive market pricing because this is an exact-minute, single-venue settlement and the final candle had not yet printed at analysis time.\n\n## Why this may matter now\n\nMarket-implied baseline was 95.3% from the assignment snapshot, while live Polymarket surface during verification showed the 66k line near 99.8% Yes. My final synthesis range is 0.93 to 0.97. That makes the edge marginal to unclear rather than strongly actionable: directionally Yes still dominates, but the contract's exact-minute Binance settlement …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.98,"w":"high","thesis":"The market is directionally right: Binance BTC/USDT is far enough above 66,000 that Yes is very likely, though single-minute close mechanics keep the probability a bit below literal certainty.","support":["Polymarket rules explicitly define Binance BTC/USDT 1m 12:00 ET final Close as the settlement mechanism."],"disconfirm":["This is a single exact-minute close contract, so a sharp late selloff could still flip the result."],"ambiguity":["Exact final noon ET candle had not printed at analysis time."],"change":"A fast BTC drop toward 66k before noon ET, a Binance outage, or direct evidence that the Binance web candle differs from API interpretation …"},{"persona":"catalyst-hunter","p":0.97,"w":"high","thesis":"The decisive catalyst is the exact Binance BTC/USDT 12:00 ET one-minute close, and direct exchange checks showing BTC materially above 66,000 make Yes highly likely absent a sharp pre-settlement selloff or source-of-trut …","support":["Polymarket rules explicitly define the Binance BTC/USDT 12:00 ET 1m candle Close as the source of truth."],"disconfirm":["This is a single-minute settlement market, so a sharp overnight or late-morning selloff could still flip the outcome."],"ambiguity":["Whether the Binance web UI display could differ in any meaningful way from API-derived interpretation at settlement."],"change":"I would cut confidence if BTC/USDT trades near 66,000 before noon ET, if the actual 16:00 UTC candle closes near/below the line, or if Binan …"},{"persona":"base-rate","p":0.91,"w":"medium","thesis":"Yes is likely because BTC/USDT is trading far above 66,000, but the market is slightly too confident for a one-minute Binance-specific settlement.","support":["Binance BTCUSDT was around 71.5k during the run, leaving a ~7.7% cushion over 66k."],"disconfirm":["BTC can still fall 7-8% intraday or overnight, especially during weekend liquidation cascades."],"ambiguity":["Minor residual ambiguity remains around UI presentation versus API indexing, though Binance docs indicate the candle is identified by open t …"],"change":"A sharp move toward 66k before noon ET, a macro/geopolitical shock, or Binance-specific pricing/candle anomalies would reduce the Yes probab …"}],"selected_assumption_snippets":[{"src":"assumptions/market-implied.md","text":"# Assumption\nThe market’s near-certainty pricing is rational because Binance BTC/USDT is far enough above 66,000 shortly before the deadline that a drop below the threshold by the exact noon ET 1-minute close is unlikely.\n## Why this assumption matters\nThe market-implied thesis depends less on exotic hidden information than on the simple premise that the threshold is already deeply in the money and the remaining time window is short.\n## What this assumption supports\n- A high own probability esti …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: BTC intraday volatility before the exact 12:00 ET / 16:00 UTC settlement minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: small Binance web-UI versus API interpretation residual despite clear rule text?","Are the current blockers still material to final judgment: The final settling candle was still in the future at analysis time?","Is the main verification gap still decision-material: The exact settling 16:00 UTC candle had not yet occurred, so residual path risk could not be eliminated.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The exact settling 16:00 UTC candle had not yet occurred, so residual path risk could not be eliminated.","best_countercase_summary":"A sharp pre-noon selloff or Binance-specific settlement-surface anomaly could still flip an otherwise comfortable Yes.","freshness_sensitive":"yes","freshness_driver":"BTC intraday volatility before the exact 12:00 ET / 16:00 UTC settlement minute","decision_blockers":["The final settling candle was still in the future at analysis time","Residual single-minute path dependence and Binance-specific operational risk remain"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.98,"w":"high","thesis":"The market is directionally right: Binance BTC/USDT is far enough above 66,000 that Yes is very likely, though single-minute close mechanics keep the probability a bit below literal certainty.","logical_chain":["Start from the market prior: assignment snapshot 95.3%, live page effectively 99.9% Yes.","Verify the contract mechanics: Binance BTC/USDT, 1m candle, ET noon, final Close.","Verify current Binance spot on the specified pair and interval: around 71.5k during the run."],"supports":["Polymarket rules explicitly define Binance BTC/USDT 1m 12:00 ET final Close as the settlement mechanism.","Live Polymarket page showed the 66k line trading near certainty at 99.9¢ Yes."],"disconfirmers":["This is a single exact-minute close contract, so a sharp late selloff could still flip the result.","Polymarket cites the Binance web candle as source of truth, while verification here used the API as proxy."],"ambiguities":["Exact final noon ET candle had not printed at analysis time.","The assignment snapshot price differed from the near-expiry live page price."],"change":"A fast BTC drop toward 66k before noon ET, a Binance outage, or direct evidence that the Binance web candle differs from API interpretation would reduce confidence."},"note_deep_dive":{"src":"assumptions/market-implied.md","text":"# Assumption\nThe market’s near-certainty pricing is rational because Binance BTC/USDT is far enough above 66,000 shortly before the deadline that a drop below the threshold by the exact noon ET 1-minute close is unlikely.\n## Why this assumption matters\nThe market-implied thesis depends less on exotic hidden information than on the simple premise that the threshold is already deeply in the money and the remaining time window is short.\n## What this assumption supports\n- A high own probability estimate for Yes.\n- Rough agreement with the market’s direction.\n- Interpreting the market as mostly efficient rather than stale or overextended.\n## Evidence or logic behind the assumption\n- Polymarket shows the 66k line at 99.9¢ Yes.\n- Binance BTCUSDT 1-minute spot data was trading around 71.5k at the time checked.\n- The distance to threshold is more than 5k, which is large for a short remaining wind …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

