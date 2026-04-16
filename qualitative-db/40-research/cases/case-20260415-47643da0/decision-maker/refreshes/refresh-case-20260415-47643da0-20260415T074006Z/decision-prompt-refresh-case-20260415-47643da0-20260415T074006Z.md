# Decision-Maker task | case `case-20260415-47643da0`

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
- case_key: `case-20260415-47643da0`
- dispatch_id: `refresh-case-20260415-47643da0-20260415T074006Z`
- question: Will the price of Bitcoin be above $72,000 on April 17?
- market_title: Will the price of Bitcoin be above $72,000 on April 17?
- market_reference_price: 0.745

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.745,"last_reasoned_price":0.81,"price_delta_pct_points":6.5,"hours_since_last_forecast":6.4,"hours_to_close":56.33,"latest_forecast":{"forecast_id":"dispatch-case-20260415-47643da0-20260415T010752Z","forecast_prob":0.81,"decision_ts":"2026-04-14T21:16:00-04:00","rationale_summary":"Bitcoin is likely to finish above $72,000 on the April 17 noon ET Binance minute because current same-venue pricing remains materially above the strike and recent Binance minute data stayed above it, but the market's 84% …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.745,"max_reference_price":0.78,"avg_reference_price":0.7683333333333333},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.745","0.255"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present"],"core_case":{"question":"Will the price of Bitcoin be above $72,000 on April 17?","market_title":"Will the price of Bitcoin be above $72,000 on April 17?","market_reference_price":0.745,"syndicated_probability_low":0.79,"syndicated_probability_high":0.83,"syndicated_probability_midpoint":0.81,"edge_mid_vs_market_pct_points":6.5,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"minor operational ambiguity around exact Binance ET minute mapping/UI display, though rule text is explicit","freshness_sensitive":"yes","freshness_driver":"BTC short-horizon path volatility into the exact April 17 12:00 ET Binance settlement minute","decision_blockers":["No independently strong estimate of short-horizon downside-tail probability beyond lane heuristics","Single-minute Binance settlement design creates timestamp fragility near resolution","Edge versus market is small after synthesis and may disappear with modest spot movement"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"minor operational ambiguity around exact Binance ET minute mapping/UI display, though rule text is explicit","verification_gap_summary":"No strong independent volatility model or fresh catalyst map verified whether a roughly 3.6% downside move before settlement is over- or underpriced.","best_countercase_summary":"Current Binance cushion and recent above-threshold minute data may mean the market’s 84% Yes price is already fair or slightly conservative.","main_reason_for_disagreement":"how much probability mass to assign to a 3-4% downside move landing exactly at the settlement minute","resolution_mechanics_summary":"Yes requires the Binance BTC/USDT April 17 noon ET 1-minute candle final close to be strictly above 72000.","freshness_sensitive":"yes","freshness_driver":"BTC short-horizon path volatility into the exact April 17 12:00 ET Binance settlement minute","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket-style resolution mechanics center on Binance BTC/USDT 12:00 ET 1-minute final close above 72000","Direct Binance spot remained around 74680 at synthesis check","Fresh Binance 1-minute klines near synthesis time remained comfortably above 72000"],"decision_blockers":["No independently strong estimate of short-horizon downside-tail probability beyond lane heuristics","Single-minute Binance settlement design creates timestamp fragility near resolution"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBitcoin is more likely than not to finish above $72,000 on the relevant April 17 Binance noon ET 1-minute close, but the swarm’s modestly sub-market view remains the best synthesis because the contract is resolved by one exact timestamp on one venue and the independent synthesis-stage verification did not justify trusting a higher-confidence Yes than roughly low-80s.\n\n## Why this may matter now\n\nMarket implied probability is 0.84. My syndicated range is 0.79 to 0.83. That is a marginal-to-unclear edge leaning below market rather than an actionable large one. The only plausible mispricing is that the market may be slightly too comfortable treating a ~3.6% cushion as enough …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.8,"w":"medium","thesis":"The market's 84% Yes price is broadly justified because Binance BTC/USDT is already materially above 72,000, though exact-minute downside volatility keeps the true probability below the market price.","support":["Direct Binance spot check showed BTCUSDT around 74,657, about 2,657 above the threshold."],"disconfirm":["A roughly 3.6% downside move by the exact settlement minute is plausible in BTC over ~35 hours."],"ambiguity":["The main uncertainty is future price path into the settlement minute, not contract wording."],"change":"I would move lower if BTC/USDT trades back near 72,000 or realized downside volatility rises materially before Apr. 17; I would move higher …"},{"persona":"base-rate","p":0.78,"w":"medium","thesis":"YES is favored because Binance BTC/USDT is already materially above $72,000, but the market slightly overstates that edge given normal short-horizon BTC volatility and exact-minute settlement risk.","support":["Binance BTC/USDT spot was about 74,680.51, well above 72,000."],"disconfirm":["BTC often moves 3-4% over a two-to-three-day window, enough to fall below the threshold."],"ambiguity":["Exact practical chart/UI timestamp interpretation remains a minor operational ambiguity until settlement minute observation."],"change":"I would cut YES if BTC starts trading near 72k before settlement, and move closer to or above market if BTC sustains well above 75-76k into …"},{"persona":"catalyst-hunter","p":0.88,"w":"medium","thesis":"BTC is more likely than not to settle above $72,000 on the April 17 noon ET Binance BTC/USDT one-minute close because current spot and recent 1-minute ranges leave a meaningful cushion, with downside shock risk as the ma …","support":["Checked Binance spot was about 74,691.57, roughly 3.6% above the threshold."],"disconfirm":["Bitcoin can move several percent in under two days, and a single bad minute at noon ET is enough for No."],"ambiguity":["No identified scheduled catalyst clearly dominates the next ~39 hours."],"change":"I would reduce the estimate if BTC trades persistently near 72k-73k, if a macro risk-off shock hits, if Binance shows operational issues, or …"}],"selected_assumption_snippets":[{"src":"assumptions/base-rate.md","text":"# Assumption\nBitcoin will remain in roughly the same price regime over the next ~2.5 days, such that a drop of more than about 3.6% by the precise Apr 17 noon ET Binance minute close is less likely than the market's current 84% YES pricing implies, but still materially possible.\n## Why this assumption matters\nThe thesis depends on treating the current price gap above $72,000 as meaningful cushion rather than as noise that can vanish easily before the exact settlement minute.\n## What this assumpt …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: BTC short-horizon path volatility into the exact April 17 12:00 ET Binance settlement minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: minor operational ambiguity around exact Binance ET minute mapping/UI display, though rule text is explicit?","Are the current blockers still material to final judgment: No independently strong estimate of short-horizon downside-tail probability beyond lane heuristics?","Is the main verification gap still decision-material: No strong independent volatility model or fresh catalyst map verified whether a roughly 3.6% downside move before settlement is over- or underpriced.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"No strong independent volatility model or fresh catalyst map verified whether a roughly 3.6% downside move before settlement is over- or underpriced.","best_countercase_summary":"Current Binance cushion and recent above-threshold minute data may mean the market’s 84% Yes price is already fair or slightly conservative.","freshness_sensitive":"yes","freshness_driver":"BTC short-horizon path volatility into the exact April 17 12:00 ET Binance settlement minute","decision_blockers":["No independently strong estimate of short-horizon downside-tail probability beyond lane heuristics","Single-minute Binance settlement design creates timestamp fragility near resolution"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"catalyst-hunter","p":0.88,"w":"medium","thesis":"BTC is more likely than not to settle above $72,000 on the April 17 noon ET Binance BTC/USDT one-minute close because current spot and recent 1-minute ranges leave a meaningful cushion, with downside shock risk as the main threat.","logical_chain":["Verify exact settlement mechanics and timestamp from Polymarket rules.","Check current Binance BTCUSDT spot and recent one-minute close range.","Observe that price is materially above 72,000 and recent range stayed above the threshold."],"supports":["Checked Binance spot was about 74,691.57, roughly 3.6% above the threshold.","A 24-hour Binance 1-minute kline sample stayed above 73,857.55."],"disconfirmers":["Bitcoin can move several percent in under two days, and a single bad minute at noon ET is enough for No.","This contract is timestamp-specific, so temporary downside volatility matters more than broad directional trend."],"ambiguities":["No identified scheduled catalyst clearly dominates the next ~39 hours.","Website UI versus API presentation could differ slightly, though the referenced market surface is the same."],"change":"I would reduce the estimate if BTC trades persistently near 72k-73k, if a macro risk-off shock hits, if Binance shows operational issues, or if settlement-time interpretation chang …"},"note_deep_dive":{"src":"assumptions/base-rate.md","text":"# Assumption\nBitcoin will remain in roughly the same price regime over the next ~2.5 days, such that a drop of more than about 3.6% by the precise Apr 17 noon ET Binance minute close is less likely than the market's current 84% YES pricing implies, but still materially possible.\n## Why this assumption matters\nThe thesis depends on treating the current price gap above $72,000 as meaningful cushion rather than as noise that can vanish easily before the exact settlement minute.\n## What this assumption supports\n- A high but not near-certain YES probability.\n- A modestly bearish adjustment versus the market's 84-85% implied probability.\n- A base-rate framing that short-horizon BTC reversals are common enough to prevent treating current spot > threshold as almost settled.\n## Evidence or logic behind the assumption\n- Current Binance BTC/USDT spot is around 74.68k, well above the threshold.\n- Re …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

