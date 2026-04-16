---
type: learning_note
learning_type: case_review
learning_scope: resolved_case
case_key: case-20260414-3ce42d6c
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
upstream_inputs: ['qualitative-db/40-research/cases/case-20260414-3ce42d6c/case.md', 'qualitative-db/40-research/cases/case-20260414-3ce42d6c/decision-maker/artifacts/decision-maker-packet.json', 'qualitative-db/40-research/cases/case-20260414-3ce42d6c/synthesizer-agent/syndicated-finding.runtime.json']
downstream_uses: []
promotion_candidates: []
tags: ['learning/case_review', 'evaluator/draft', 'platform/polymarket']
---

# Learning Note

## What was being evaluated

- Case: `case-20260414-3ce42d6c`
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
- Primary crux: BTC being above $70,000 at the April 14 noon ET Binance minute is overwhelmingly likely because the same-venue morning price sat far above the strike, but the market's 99.95% price already assumes away almost all of the exact-minute, single-venue settlement tail that still remains until the resolving candle is actually observed.

## What happened in reality

- Resolution status in packet: resolved
- Resolved outcome: yes
- Resolved value: 1.0
- Resolved at: 2026-04-14T15:44:48-04:00
- This draft is based on the evaluator bridge packet combining qualitative provenance and quant truth.

## Outcome and scoring evidence

- Persona probability range: 0.97 to 0.992
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
- 2026-04-14T11:02:00-04:00 — decision packet generated
- 2026-04-14T11:02:00-04:00 — latest forecast recorded at 0.992
- 2026-04-14T13:09:58.652625+00:00 — prepared analysis `dispatch-case-20260414-3ce42d6c-20260414T130958Z` with summary `qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/summary.md`.
- 2026-04-14T13:09:58.652625+00:00 — synthesis runtime artifact written
- 2026-04-14T13:19:23.337947+00:00 — completed synthesis `dispatch-case-20260414-3ce42d6c-20260414T130958Z` with artifact `qualitative-db/40-research/cases/case-20260414-3ce42d6c/researcher-analyses/2026-04-14/dispatch-case-20260414-3ce42d6c-20260414T130958Z/syndicated-finding.md`.

## Which inputs were high signal

- base-rate: Same-day Binance spot checks showed BTC/USDT around 74.5k-74.6k, well above 70k.
- catalyst-hunter: Polymarket explicitly names Binance BTC/USDT 12:00 ET 1m candle final Close as the source of truth.
- market-implied: Polymarket explicitly defines Binance BTC/USDT 1m 12:00 ET close as the governing source of truth.
- risk-manager: Live Binance ticker during research was about 74544.7, leaving a substantial cushion above 70000.
- variant-view: Polymarket rules explicitly define Binance BTC/USDT 1m 12:00 ET close as the governing source.

## Which inputs were misleading

- base-rate: This is an exact-minute, exchange-specific settlement, so minute-level volatility still matters.
- catalyst-hunter: The contract is governed by a single minute close on a single venue, so sudden liquidation, wick risk, outage, or data irregularity remains a tail risk.
- market-implied: A fast late-morning drawdown of about 6%+ could still push the noon close below 70k.
- risk-manager: The contract resolves on a single one-minute close, so late intraday reversal risk is the main failure mode.
- variant-view: The exact 12:00 ET Binance 1-minute historical close was not directly recovered in this runtime environment.

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
