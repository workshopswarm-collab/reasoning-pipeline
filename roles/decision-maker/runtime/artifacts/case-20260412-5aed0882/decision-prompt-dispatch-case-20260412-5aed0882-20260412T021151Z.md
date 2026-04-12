# Decision-Maker task | case `case-20260412-5aed0882`

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
- case_key: `case-20260412-5aed0882`
- dispatch_id: `dispatch-case-20260412-5aed0882-20260412T021151Z`
- question: Will the price of Bitcoin be above $62,000 on April 12?
- market_title: Will the price of Bitcoin be above $62,000 on April 12?
- market_reference_price: 0.9595

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
{"verification_mode":"targeted_escalation","verification_triggers":["freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $62,000 on April 12?","market_title":"Will the price of Bitcoin be above $62,000 on April 12?","market_reference_price":0.9595,"syndicated_probability_low":0.94,"syndicated_probability_high":0.98,"syndicated_probability_midpoint":0.96,"edge_mid_vs_market_pct_points":0.0,"relation_to_market":"crosses_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small residual ambiguity around exact noon-ET candle labeling/open-time semantics on Binance UI vs API terminology","freshness_sensitive":"yes","freshness_driver":"the unresolved Binance BTC/USDT noon ET settlement candle on Apr 12","decision_blockers":["The market is not yet settled and the decisive Binance candle has not printed","Single-venue exact-minute settlement leaves residual operational/timing tail risk","No strong independent evidence exists to quantify crash-tail probability beyond current price cushion"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"unclear","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"small residual ambiguity around exact noon-ET candle labeling/open-time semantics on Binance UI vs API terminology","verification_gap_summary":"The actual settlement candle had not printed yet, so exact-minute tail and venue-specific risk cannot be eliminated pre-resolution.","best_countercase_summary":"A fast pre-noon liquidation or Binance-specific print anomaly could still drag the exact settlement minute below 62k despite the large cushion.","main_reason_for_disagreement":"How much residual probability mass to assign to exact-minute single-venue tail risk before settlement.","resolution_mechanics_summary":"Resolves from the Binance BTC/USDT 1-minute candle labeled 12:00 ET on Apr 12 using the final Close, which must be strictly above 62,000.","freshness_sensitive":"yes","freshness_driver":"the unresolved Binance BTC/USDT noon ET settlement candle on Apr 12","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket rules explicitly name Binance BTC/USDT 1-minute 12:00 ET final Close as settlement source","Fresh Binance spot remained around 71.8k during synthesis-stage verification","Fresh recent Binance 1-minute candles were clustered around high-71k, far above 62k"],"decision_blockers":["The market is not yet settled and the decisive Binance candle has not printed","Single-venue exact-minute settlement leaves residual operational/timing tail risk"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBitcoin is still very likely to resolve Yes, but the synthesis should stay a touch below the most aggressive lane because the contract is not settled yet and resolves on one exact future Binance 1-minute close rather than on broad spot consensus. My post-synthesis view is that the noon-ET Binance BTC/USDT close above 62,000 is highly likely, with only tail crash risk and narrow Binance-specific settlement risk left live.\n\n## Why this may matter now\n\nMarket-implied probability is 0.9595. My syndicated range is 0.94 to 0.98. That is broadly in line with market and only marginally actionable at best; the main possible mispricing is that traders may either slightly underweigh …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.985,"w":"high","thesis":"The market's extreme Yes price is justified because Binance BTC/USDT is trading far above 62000 and the remaining live risk is mainly tail-risk or minor settlement-mechanics risk.","support":["Binance API showed BTC/USDT around 71.8k during the run, leaving roughly a 9.8k buffer above the strike."],"disconfirm":["The event remains unresolved until the actual noon ET candle prints."],"ambiguity":["The exact noon ET candle was not yet observable during the run."],"change":"A rapid drop toward 62k, evidence of Binance-specific price dislocation, or a clarified settlement mapping issue would reduce confidence mat …"},{"persona":"risk-manager","p":0.96,"w":"medium","thesis":"BTC is very likely to settle above 62000 on the relevant Binance noon ET one-minute candle, with most remaining risk concentrated in timing and exchange-specific settlement mechanics rather than directional price weaknes …","support":["Binance BTCUSDT was trading around 71.4k to 71.8k during the analysis window."],"disconfirm":["The contract resolves on one exact future Binance one-minute close, not on current broad spot price."],"ambiguity":["Exact price path between analysis time and noon ET."],"change":"A rapid move toward 62000 on Binance, a meaningful Binance-vs-broader-market divergence, or evidence that the noon ET candle interpretation …"},{"persona":"variant-view","p":0.93,"w":"medium","thesis":"Yes is very likely, but the market is slightly overconfident because this is a future exact-minute Binance-specific settlement rather than a generic spot-price question.","support":["Binance spot checked around 71834.96, far above 62000."],"disconfirm":["The market resolves on one exact future minute, so residual timing and venue-specific tail risk remains."],"ambiguity":["How much probability mass to assign to rare but nonzero crash risk before noon ET."],"change":"A fresh pre-noon Binance check showing BTC much closer to 62000, a sharp overnight selloff, or evidence of Binance-specific pricing/operatio …"}],"selected_assumption_snippets":[{"src":"assumptions/market-implied.md","text":"# Assumption\nBTC/USDT on Binance will not suffer a roughly 14% drawdown before the April 12 noon ET settlement minute, and Binance’s displayed 1-minute candle mechanics will behave normally.\n## Why this assumption matters\nThe market’s extreme Yes price only makes sense if the current large distance above the threshold is not erased by an unusually severe overnight-to-noon selloff or by a venue-specific operational anomaly.\n## What this assumption supports\n- A very high Yes probability.\n- A view …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: the unresolved Binance BTC/USDT noon ET settlement candle on Apr 12?","How decision-relevant is the remaining contract/source-of-truth ambiguity: small residual ambiguity around exact noon-ET candle labeling/open-time semantics on Binance UI vs API terminology?","Are the current blockers still material to final judgment: The market is not yet settled and the decisive Binance candle has not printed?","Is the main verification gap still decision-material: The actual settlement candle had not printed yet, so exact-minute tail and venue-specific risk cannot be eliminated pre-resolution.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The actual settlement candle had not printed yet, so exact-minute tail and venue-specific risk cannot be eliminated pre-resolution.","best_countercase_summary":"A fast pre-noon liquidation or Binance-specific print anomaly could still drag the exact settlement minute below 62k despite the large cushion.","freshness_sensitive":"yes","freshness_driver":"the unresolved Binance BTC/USDT noon ET settlement candle on Apr 12","decision_blockers":["The market is not yet settled and the decisive Binance candle has not printed","Single-venue exact-minute settlement leaves residual operational/timing tail risk"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"market-implied","p":0.985,"w":"high","thesis":"The market's extreme Yes price is justified because Binance BTC/USDT is trading far above 62000 and the remaining live risk is mainly tail-risk or minor settlement-mechanics risk.","logical_chain":["The contract settles on a specific Binance BTC/USDT 1-minute close at noon ET.","Current designated-venue price context is around 71.8k, far above 62k.","Therefore ordinary volatility is insufficient to threaten Yes, leaving mainly tail-risk and minor operational/interpretive risk."],"supports":["Binance API showed BTC/USDT around 71.8k during the run, leaving roughly a 9.8k buffer above the strike.","Recent 1-minute Binance candles were clustered in the high-71k range rather than near 62k."],"disconfirmers":["The event remains unresolved until the actual noon ET candle prints.","A large overnight BTC drawdown or Binance-specific dislocation could still flip the result."],"ambiguities":["The exact noon ET candle was not yet observable during the run.","The fetched Polymarket webpage is a less clean probability source than a dedicated market API snapshot."],"change":"A rapid drop toward 62k, evidence of Binance-specific price dislocation, or a clarified settlement mapping issue would reduce confidence materially."},"note_deep_dive":{"src":"assumptions/market-implied.md","text":"# Assumption\nBTC/USDT on Binance will not suffer a roughly 14% drawdown before the April 12 noon ET settlement minute, and Binance’s displayed 1-minute candle mechanics will behave normally.\n## Why this assumption matters\nThe market’s extreme Yes price only makes sense if the current large distance above the threshold is not erased by an unusually severe overnight-to-noon selloff or by a venue-specific operational anomaly.\n## What this assumption supports\n- A very high Yes probability.\n- A view that the market is broadly efficient rather than stale.\n- A conclusion that most remaining risk is tail-risk or settlement-mechanics risk, not ordinary drift.\n## Evidence or logic behind the assumption\n- Binance API data during the run showed BTC/USDT around 71.8k, nearly 10k above the 62k line.\n- Recent 1-minute candles were stable in the high-71k range rather than showing collapse dynamics.\n- Po …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

