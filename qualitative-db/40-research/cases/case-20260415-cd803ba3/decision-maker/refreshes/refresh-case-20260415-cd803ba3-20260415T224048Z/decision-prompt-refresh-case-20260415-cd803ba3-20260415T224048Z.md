# Decision-Maker task | case `case-20260415-cd803ba3`

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
- case_key: `case-20260415-cd803ba3`
- dispatch_id: `refresh-case-20260415-cd803ba3-20260415T224048Z`
- question: Will the price of Bitcoin be above $74,000 on April 17?
- market_title: Will the price of Bitcoin be above $74,000 on April 17?
- market_reference_price: 0.705

## Lightweight refresh brief for this run
```json
{"recommended_mode":"light","reasons":["material_price_move"],"current_price":0.705,"last_reasoned_price":0.65,"price_delta_pct_points":5.5,"hours_since_last_forecast":1.86,"hours_to_close":41.32,"latest_forecast":{"forecast_id":"dispatch-case-20260415-cd803ba3-20260415T203927Z","forecast_prob":0.65,"decision_ts":"2026-04-15T16:49:00-04:00","rationale_summary":"BTC is only modestly more likely than not to finish above $74,000 on the April 17 Binance noon minute, but with fair value closer to 0.65 than the 0.70 assignment price and meaningful exact-minute downside fragility stil …"},"snapshot_summary":{"snapshot_count":12,"min_reference_price":0.68,"max_reference_price":0.705,"avg_reference_price":0.69},"live_market_probe":{"closed":false,"archived":false,"acceptingOrders":true,"umaResolutionStatus":"","outcomePrices":["0.69","0.31"]},"focused_questions":["Did the market move invalidate the prior crux, or is this mainly repricing without new information?","Does the new price imply the previous edge has materially compressed or inverted?","Has time-to-close changed the appropriate confidence or action threshold?","Can we update priors responsibly using prior synthesis plus current market state without rerunning the full swarm?"]}
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
{"verification_mode":"targeted_escalation","verification_triggers":["large_apparent_edge_vs_market","freshness_sensitive_catalyst","decision_blockers_present","internal_inconsistency_in_package"],"core_case":{"question":"Will the price of Bitcoin be above $74,000 on April 17?","market_title":"Will the price of Bitcoin be above $74,000 on April 17?","market_reference_price":0.705,"syndicated_probability_low":0.62,"syndicated_probability_high":0.68,"syndicated_probability_midpoint":0.65,"edge_mid_vs_market_pct_points":-5.5,"relation_to_market":"below_market","edge_independent_verification_quality":"medium","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Binance UI candle named as source while verification used Binance API proxy","freshness_sensitive":"yes","freshness_driver":"BTC level relative to 74000 heading into the Apr 17 noon ET settlement minute","decision_blockers":["Exact-minute timing fragility with only a modest price cushion above 74000","No strong independent verification that the current cushion will persist through settlement","Minor operational ambiguity between Binance UI settlement surface and API-based verification"],"blockers_require_new_research":"no","disagreement_type":"timing","follow_up_needed":"yes"},"structured_handoff_primary":{"edge_quality":"moderate","edge_independent_verification_quality":"medium","compressed_toward_market_due_to_verification":"no","contract_ambiguity_level":"minor","contract_ambiguity_reason":"Binance UI candle named as source while verification used Binance API proxy","verification_gap_summary":"The main remaining gap is not contract wording but whether BTC can retain a small above-strike cushion into one exact future minute.","best_countercase_summary":"A routine sub-1.5% selloff into the settlement minute would still flip this to No despite current above-strike spot.","main_reason_for_disagreement":"Remaining disagreement is mostly about how much weight to place on exact-minute volatility versus the fact that the strike is already cleared.","resolution_mechanics_summary":"Yes resolves only if the Binance BTC/USDT 12:00 ET Apr 17 1-minute candle final close is strictly above 74000.","freshness_sensitive":"yes","freshness_driver":"BTC level relative to 74000 heading into the Apr 17 noon ET settlement minute","blockers_require_new_research":"no","disagreement_type":"timing","independently_verified_points":["Polymarket rules resolve from Binance BTC/USDT 12:00 ET Apr 17 1m candle close","Live Polymarket page showed the 74k line around 65% during synthesis","Binance BTCUSDT spot remained above 74000 during synthesis-stage checks"],"decision_blockers":["Exact-minute timing fragility with only a modest price cushion above 74000","No strong independent verification that the current cushion will persist through settlement"]},"structured_handoff_policy":{"structured_handoff_is_primary_starting_point":true,"prose_is_fallback_only":true},"prose_fallback":{"included":true,"text":"# Decision summary\n\nBitcoin is more likely than not to close above $74,000 on the April 17 Binance 12:00 ET 1-minute candle, but the edge is only modest and more fragile than a casual spot-level reading suggests. My post-synthesis view is a narrow Yes lean below the 0.70 market baseline because independent verification confirms BTC is currently above the strike and broadly aligned across venues, yet does not strongly overcome the exact-minute settlement fragility or the small cushion above the threshold.\n\n## Why this may matter now\n\nMarket baseline is 0.70 from assignment metadata, while live synthesis-stage verification found the Polymarket 74k line around 0.65. My syndicated range is 0.62- …"},"selected_persona_sidecars":[{"persona":"market-implied","p":0.66,"w":"medium","thesis":"The market is broadly efficient: BTC is already above 74000 on Binance, so Yes is reasonably favored, but the exact-minute settlement keeps confidence below the market's roughly 70% level.","support":["Binance BTCUSDT 1m prices were already above 74000 during the verification pass."],"disconfirm":["The contract settles on one exact future minute, so a routine ~1% BTC pullback could flip the outcome to No."],"ambiguity":["Polymarket page scrape showed 63% while assignment metadata gave 70%, so live price should be treated as a mid-60s to 70% range."],"change":"I would cut the estimate if BTC loses 74000 across Binance and major spot venues and fails to reclaim it before noon ET April 17; I would ra …"},{"persona":"base-rate","p":0.58,"w":"medium","thesis":"Bitcoin being modestly above $74,000 supports a Yes lean, but the exact-minute Binance close and recent volatility make the edge only moderate.","support":["Current Binance BTCUSDT spot was about 74,853, above the 74,000 strike"],"disconfirm":["Recent realized volatility shows BTC can move back below 74,000 within the remaining window"],"ambiguity":["Assignment snapshot market price was 0.70 while fetched live display was closer to 0.63"],"change":"A larger sustained cushion above 74,000 before April 17 noon ET would raise the estimate; a move back below 74,000 or volatility expansion w …"},{"persona":"variant-view","p":0.72,"w":"medium","thesis":"BTC is already modestly above the 74k strike, so this is mainly a hold-the-line settlement-minute question rather than a breakout question; that supports a slight Yes edge.","support":["Binance BTCUSDT traded around 74.7k during the run, already above the strike."],"disconfirm":["Settlement depends on one exact 1-minute Binance close at 12:00 PM ET, so ordinary intraday volatility could still flip the result below 74k …"],"ambiguity":["How much intraday volatility will compress or expand before Friday noon ET."],"change":"I would move toward No if BTC fell back below 74k and failed to reclaim it across several hourly closes, if a risk-off shock pushed it into …"}],"selected_assumption_snippets":[{"src":"assumptions/base-rate.md","text":"# Assumption\nThe best outside-view approximation is that, absent a new major catalyst, Bitcoin will remain within its recent short-horizon trading regime through the April 17 noon ET resolution window.\n## Why this assumption matters\nThe probability of finishing above 74,000 depends less on long-run Bitcoin fundamentals than on whether the next roughly 44 hours resemble recent realized volatility and level behavior.\n## What this assumption supports\n- A moderate Yes lean rather than an extreme con …"}],"selected_evidence_snippets":[],"selected_supporting_note_snippets":[]}
```

## Targeted verification scaffold for this run
```json
{"verification_questions":["Does the latest available information materially change the decision, given: BTC level relative to 74000 heading into the Apr 17 noon ET settlement minute?","How decision-relevant is the remaining contract/source-of-truth ambiguity: Binance UI candle named as source while verification used Binance API proxy?","Are the current blockers still material to final judgment: Exact-minute timing fragility with only a modest price cushion above 74000?","Is the main verification gap still decision-material: The main remaining gap is not contract wording but whether BTC can retain a small above-strike cushion into one exact future minute.?"],"focus":{"contract_ambiguity_level":"minor","verification_gap_summary":"The main remaining gap is not contract wording but whether BTC can retain a small above-strike cushion into one exact future minute.","best_countercase_summary":"A routine sub-1.5% selloff into the settlement minute would still flip this to No despite current above-strike spot.","freshness_sensitive":"yes","freshness_driver":"BTC level relative to 74000 heading into the Apr 17 noon ET settlement minute","decision_blockers":["Exact-minute timing fragility with only a modest price cushion above 74000","No strong independent verification that the current cushion will persist through settlement"]}}
```

## Bounded expanded reasoning fallback (use only if needed)
```json
{"persona_deep_dive":{"persona":"variant-view","p":0.72,"w":"medium","thesis":"BTC is already modestly above the 74k strike, so this is mainly a hold-the-line settlement-minute question rather than a breakout question; that supports a slight Yes edge.","logical_chain":["The market implies 70% Yes.","Direct Binance checks show BTC already above 74k, so additional upside is not required.","Because the contract is decided by one future noon ET minute close, the main residual risk is timing-specific volatility rather than general trend direction."],"supports":["Binance BTCUSDT traded around 74.7k during the run, already above the strike.","Recent Binance hourly and daily candles show BTC has been operating near and above 74k."],"disconfirmers":["Settlement depends on one exact 1-minute Binance close at 12:00 PM ET, so ordinary intraday volatility could still flip the result below 74k.","Recent Binance ranges were wide enough that a sub-74k print is plausible before Friday noon ET."],"ambiguities":["How much intraday volatility will compress or expand before Friday noon ET.","Whether Binance-specific microstructure diverges from broader BTC references at settlement."],"change":"I would move toward No if BTC fell back below 74k and failed to reclaim it across several hourly closes, if a risk-off shock pushed it into the low-73k area before settlement, or i …"},"note_deep_dive":{"src":"assumptions/base-rate.md","text":"# Assumption\nThe best outside-view approximation is that, absent a new major catalyst, Bitcoin will remain within its recent short-horizon trading regime through the April 17 noon ET resolution window.\n## Why this assumption matters\nThe probability of finishing above 74,000 depends less on long-run Bitcoin fundamentals than on whether the next roughly 44 hours resemble recent realized volatility and level behavior.\n## What this assumption supports\n- A moderate Yes lean rather than an extreme conviction view.\n- Treating recent Binance price distribution around the threshold as more informative than narrative headlines.\n- Discounting vivid but unsupported stories that imply a very large directional move before resolution.\n## Evidence or logic behind the assumption\nRecent Binance daily data show BTC repeatedly moving through the upper-60k to mid-70k region, with current price modestly above …"}}
```

## Final reminder
Return one JSON object only. No markdown fences. No commentary before or after the JSON.

