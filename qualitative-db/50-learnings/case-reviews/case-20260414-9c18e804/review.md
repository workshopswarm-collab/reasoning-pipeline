---
type: learning_note
learning_type: case_review
learning_scope: resolved_case
case_key: case-20260414-9c18e804
market_category: polymarket-discovery
domain: 
subdomain: 
entity: 
topic: 
question: Will Bitcoin reach $76,000 April 13-19?
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
upstream_inputs: ['qualitative-db/40-research/cases/case-20260414-9c18e804/case.md', 'qualitative-db/40-research/cases/case-20260414-9c18e804/decision-maker/artifacts/decision-maker-packet.json', 'qualitative-db/40-research/cases/case-20260414-9c18e804/synthesizer-agent/syndicated-finding.runtime.json']
downstream_uses: []
promotion_candidates: []
tags: ['learning/case_review', 'evaluator/draft', 'platform/polymarket']
---

# Learning Note

## What was being evaluated

- Case: `case-20260414-9c18e804`
- Question: Will Bitcoin reach $76,000 April 13-19?
- Platform: polymarket
- Current case status: closed
- Resolution status: resolved

## What the pipeline believed or did

- Decision side: yes
- Trade authorization: watch_only
- Position policy: hold_only
- Decision fair value mid: 0.69
- Market reference price at decision: 0.75
- Primary crux: BTC reaching $76,000 this week is still more likely than not because the contract is a Binance 1-minute high touch market and BTC is already trading within roughly 1% of the threshold, but the market's 75% price remains somewhat too rich without a verified qualifying $76,000 Binance print yet.

## What happened in reality

- Resolution status in packet: resolved
- Resolved outcome: yes
- Resolved value: 1.0
- Resolved at: 2026-04-14T13:20:02-04:00
- This draft is based on the evaluator bridge packet combining qualitative provenance and quant truth.

## Outcome and scoring evidence

- Persona probability range: 0.62 to 0.76
- Initial forecast probability: 0.665
- Latest forecast probability: 0.995
- Initial Brier component: 0.112225
- Latest Brier component: 2.5e-05
- Decision fair value range: 0.66 to 0.72
- Market reference price: 0.75
- Edge mid vs market pct points: -6.0
- Timeline excerpt:
- unknown-time — research swarm reported 5 completed personas
- 2026-04-13T19:41:00-04:00 — initial forecast recorded at 0.665
- 2026-04-14T10:03:00-04:00 — decision packet generated
- 2026-04-14T13:20:02-04:00 — market resolution recorded as yes
- 2026-04-14T13:38:00-04:00 — latest forecast recorded at 0.995
- 2026-04-14T13:51:45.772567+00:00 — prepared analysis `dispatch-case-20260414-9c18e804-20260414T135145Z` with summary `qualitative-db/40-research/cases/case-20260414-9c18e804/researcher-analyses/2026-04-14/dispatch-case-20260414-9c18e804-20260414T135145Z/summary.md`.
- 2026-04-14T13:51:45.772567+00:00 — synthesis runtime artifact written

## Which inputs were high signal

- base-rate: Polymarket rules settle on any Binance BTC/USDT 1-minute high at or above 76000.
- catalyst-hunter: CoinGecko showed BTC around $75,409, only about $591 below the threshold.
- market-implied: Binance, Kraken, and Coinbase all showed BTC around $75.3k-$75.4k, less than 1% below the threshold.
- risk-manager: Binance direct data showed highs of 74,900 on Apr 13 UTC and about 75,430 on Apr 14 UTC, leaving only a small gap to 76k.
- variant-view: Polymarket rules only require any Binance BTC/USDT 1-minute high at or above $76,000 during Apr 13-19.

## Which inputs were misleading

- base-rate: BTC had not yet clearly touched 76000 in the current window when checked despite already trading near it.
- catalyst-hunter: The market may be over-crediting proximity alone while underweighting mean-reversion risk.
- market-implied: No verified source in this run showed an actual $76k print yet.
- risk-manager: Checked evidence did not yet show an actual 76,000 print.
- variant-view: The actual qualifying Binance high had not happened yet despite the strong move.

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
