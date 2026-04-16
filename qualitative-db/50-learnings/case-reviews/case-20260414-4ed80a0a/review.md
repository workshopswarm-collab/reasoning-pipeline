---
type: learning_note
learning_type: case_review
learning_scope: resolved_case
case_key: case-20260414-4ed80a0a
market_category: polymarket-discovery
domain: 
subdomain: 
entity: 
topic: 
question: Will Ethereum reach $2,400 April 13-19?
date_created: 
resolution_date: 2026-04-14T13:20:02-04:00
evaluation_scope: resolved_case
evaluation_target: pipeline_case
outcome_observed: 1.0
decision_taken: watch_only
error_pattern: resolved_case_review_pending
intervention_status: candidate
related_entities: []
related_drivers: []
upstream_inputs: ['qualitative-db/40-research/cases/case-20260414-4ed80a0a/case.md', 'qualitative-db/40-research/cases/case-20260414-4ed80a0a/decision-maker/artifacts/decision-maker-packet.json', 'qualitative-db/40-research/cases/case-20260414-4ed80a0a/synthesizer-agent/syndicated-finding.runtime.json']
downstream_uses: []
promotion_candidates: []
tags: ['learning/case_review', 'evaluator/draft', 'platform/polymarket']
---

# Learning Note

## What was being evaluated

- Case: `case-20260414-4ed80a0a`
- Question: Will Ethereum reach $2,400 April 13-19?
- Platform: polymarket
- Current case status: closed
- Resolution status: resolved

## What the pipeline believed or did

- Decision side: yes
- Trade authorization: watch_only
- Position policy: hold_only
- Decision fair value mid: 0.9825
- Market reference price at decision: 0.916
- Primary crux: This contract appears effectively already satisfied because bundled Binance ETH/USDT data showed an in-window high of 2415.5 above the 2400 threshold, but the market's 0.916 price no longer offers a clean executable edge once the remaining uncertainty is mostly about settlement-surface parity and archival proof rather than ETH direction.

## What happened in reality

- Resolution status in packet: resolved
- Resolved outcome: yes
- Resolved value: 1.0
- Resolved at: 2026-04-14T13:20:02-04:00
- This draft is based on the evaluator bridge packet combining qualitative provenance and quant truth.

## Outcome and scoring evidence

- Persona probability range: 0.84 to 0.995
- Initial forecast probability: 0.71
- Latest forecast probability: 0.9825
- Initial Brier component: 0.0841
- Latest Brier component: 0.00030625
- Decision fair value range: 0.97 to 0.995
- Market reference price: 0.916
- Edge mid vs market pct points: 6.7
- Timeline excerpt:
- unknown-time — research swarm reported 5 completed personas
- 2026-04-13T19:13:00-04:00 — initial forecast recorded at 0.71
- 2026-04-14T13:20:02-04:00 — market resolution recorded as yes
- 2026-04-14T13:50:00-04:00 — decision packet generated
- 2026-04-14T13:50:00-04:00 — latest forecast recorded at 0.9825
- 2026-04-14T17:40:40.292461+00:00 — prepared analysis `dispatch-case-20260414-4ed80a0a-20260414T174040Z` with summary `qualitative-db/40-research/cases/case-20260414-4ed80a0a/researcher-analyses/2026-04-14/dispatch-case-20260414-4ed80a0a-20260414T174040Z/summary.md`.
- 2026-04-14T17:40:40.292461+00:00 — synthesis runtime artifact written

## Which inputs were high signal

- base-rate: Polymarket metadata explicitly defines the source of truth as Binance ETH/USDT 1-minute candle High and showed the market resolved Yes.
- catalyst-hunter: Polymarket embedded rules specify Binance ETH/USDT 1-minute Highs as the sole resolution source.
- market-implied: Polymarket rules explicitly name Binance ETH/USDT 1m candle highs as the settlement source.
- risk-manager: Polymarket rules say any Binance ETH/USDT 1-minute candle high >= 2400 in the Apr 13-19 ET window resolves Yes.
- variant-view: Binance ETHUSDT 24h high printed 2415.50, above the $2,400 threshold.

## Which inputs were misleading

- base-rate: The extra verification used Binance's 24-hour summary ticker rather than the exact 1-minute candle table named in the rules.
- catalyst-hunter: I did not independently retrieve the exact Binance historical 1-minute candle that crossed $2,400.
- market-implied: The saved verification artifact used Binance 1h candles rather than directly archived 1m candles.
- risk-manager: Residual risk that Binance API output differs from the exact chart/UI Polymarket expects.
- variant-view: The exact Polymarket rules and named official data source were not recoverable in-tool, so Binance alone is not fully dispositive.

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
