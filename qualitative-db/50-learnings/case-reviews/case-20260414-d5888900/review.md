---
type: learning_note
learning_type: case_review
learning_scope: resolved_case
case_key: case-20260414-d5888900
market_category: polymarket-discovery
domain: 
subdomain: 
entity: 
topic: 
question: Will the price of Bitcoin be above $70,000 on April 14?
date_created: 
resolution_date: 2026-04-14T15:44:48-04:00
evaluation_scope: resolved_case
evaluation_target: pipeline_case
outcome_observed: 1.0
decision_taken: watch_only
error_pattern: resolved_case_review_pending
intervention_status: candidate
related_entities: []
related_drivers: []
upstream_inputs: ['qualitative-db/40-research/cases/case-20260414-d5888900/case.md', 'qualitative-db/40-research/cases/case-20260414-d5888900/decision-maker/artifacts/decision-maker-packet.json', 'qualitative-db/40-research/cases/case-20260414-d5888900/synthesizer-agent/syndicated-finding.runtime.json']
downstream_uses: []
promotion_candidates: []
tags: ['learning/case_review', 'evaluator/draft', 'platform/polymarket']
---

# Learning Note

## What was being evaluated

- Case: `case-20260414-d5888900`
- Question: Will the price of Bitcoin be above $70,000 on April 14?
- Platform: polymarket
- Current case status: closed
- Resolution status: resolved

## What the pipeline believed or did

- Decision side: yes
- Trade authorization: watch_only
- Position policy: hold_only
- Decision fair value mid: 0.992
- Market reference price at decision: 0.9995
- Primary crux: Yes is overwhelmingly likely because Binance BTC/USDT was still trading far above $70,000 shortly before the governing noon ET minute, but the market's 99.95% price already leaves essentially no room for the remaining exact-minute, single-venue settlement tail.

## What happened in reality

- Resolution status in packet: resolved
- Resolved outcome: yes
- Resolved value: 1.0
- Resolved at: 2026-04-14T15:44:48-04:00
- This draft is based on the evaluator bridge packet combining qualitative provenance and quant truth.

## Outcome and scoring evidence

- Persona probability range: 0.985 to 0.993
- Initial forecast probability: 0.87
- Latest forecast probability: 0.992
- Initial Brier component: 0.0169
- Latest Brier component: 6.4e-05
- Decision fair value range: 0.989 to 0.995
- Market reference price: 0.9995
- Edge mid vs market pct points: -0.8
- Timeline excerpt:
- unknown-time — research swarm reported 5 completed personas
- 2026-04-13T12:57:00-04:00 — initial forecast recorded at 0.87
- 2026-04-14T10:42:00-04:00 — decision packet generated
- 2026-04-14T11:02:00-04:00 — latest forecast recorded at 0.992
- 2026-04-14T14:32:28.207212+00:00 — prepared analysis `dispatch-case-20260414-d5888900-20260414T143228Z` with summary `qualitative-db/40-research/cases/case-20260414-d5888900/researcher-analyses/2026-04-14/dispatch-case-20260414-d5888900-20260414T143228Z/summary.md`.
- 2026-04-14T14:32:28.207212+00:00 — synthesis runtime artifact written
- 2026-04-14T14:41:59.562091+00:00 — completed synthesis `dispatch-case-20260414-d5888900-20260414T143228Z` with artifact `qualitative-db/40-research/cases/case-20260414-d5888900/researcher-analyses/2026-04-14/dispatch-case-20260414-d5888900-20260414T143228Z/syndicated-finding.md`.

## Which inputs were high signal

- base-rate: Binance BTCUSDT spot was around 75.6k, leaving a large cushion above 70k.
- catalyst-hunter: Direct Binance ticker showed BTCUSDT around 75553, well above 70000.
- market-implied: Polymarket rules clearly define Binance BTC/USDT 12:00 ET 1-minute close as the source of truth.
- risk-manager: Polymarket rules explicitly define the governing source as the Binance BTC/USDT 1-minute close at 12:00 ET.
- variant-view: Assignment market price implies 99.95% Yes.

## Which inputs were misleading

- base-rate: The contract resolves on one exact Binance 1-minute close, so a sudden selloff, wick, or venue-specific issue could still flip the result.
- catalyst-hunter: Single-minute settlement creates residual path risk.
- market-implied: The contract settles on one exact minute close, so a sharp intraday selloff or Binance-specific anomaly could still flip the result.
- risk-manager: The final noon ET candle was not directly observed during the run.
- variant-view: Single-exchange single-minute settlement leaves small operational and interpretation risk.

## What was missing

- No obvious missing inputs recorded yet.

## Error-pattern classification

- Initial draft classification: settlement_or_path_review_pending
- This should be updated after structured resolution outcome and score are available.

## Driver and mechanism takeaways

- Keep source-of-truth mechanics and path dependence separate from generic directional thesis quality.
- Use this note to evaluate whether threshold-touch / settlement-mechanics logic materially influenced the case.

## Source / input / workflow takeaways

- Persona sidecars appear available and usable for structured evaluator extraction.
- The learning packet bridge is now sufficient for a first-pass review, but still needs richer structured market-path and resolution ingestion.

## Proposed intervention or hold decision

- If quant truth is present, compare the initial/latest forecast path against the resolved value before deciding whether the miss was directional, calibration-related, timing-related, or execution-policy-related.
- Decide whether a verification-rule, retrieval-rule, or workflow guardrail intervention is warranted.

## Promotion candidates for stable layers

- None yet. Promotion should wait for reviewed resolved-case evidence.

## How this should be reused later

- Re-open this note after resolution and scoring data are populated.
- Use it as the evaluator-facing bridge between upstream provenance, decision behavior, and future intervention candidates.
