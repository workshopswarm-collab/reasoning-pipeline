---
type: learning_note
learning_type: case_review
learning_scope: resolved_case
case_key: case-20260414-9f18b170
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
upstream_inputs: ['qualitative-db/40-research/cases/case-20260414-9f18b170/case.md', 'qualitative-db/40-research/cases/case-20260414-9f18b170/decision-maker/artifacts/decision-maker-packet.json', 'qualitative-db/40-research/cases/case-20260414-9f18b170/synthesizer-agent/syndicated-finding.runtime.json']
downstream_uses: []
promotion_candidates: []
tags: ['learning/case_review', 'evaluator/draft', 'platform/polymarket']
---

# Learning Note

## What was being evaluated

- Case: `case-20260414-9f18b170`
- Question: Will Bitcoin reach $76,000 April 13-19?
- Platform: polymarket
- Current case status: closed
- Resolution status: resolved

## What the pipeline believed or did

- Decision side: yes
- Trade authorization: watch_only
- Position policy: hold_only
- Decision fair value mid: 0.88
- Market reference price at decision: 0.98
- Primary crux: This now looks like a market repricing toward fair value rather than a factual regime change: BTC reaching $76,000 during Apr 13-19 remains likely because Binance is already trading just below the threshold and only a 1-minute high is needed, but 0.98 is clearly beyond what can be justified without a directly verified qualifying Binance print.

## What happened in reality

- Resolution status in packet: resolved
- Resolved outcome: yes
- Resolved value: 1.0
- Resolved at: 2026-04-14T13:20:02-04:00
- This draft is based on the evaluator bridge packet combining qualitative provenance and quant truth.

## Outcome and scoring evidence

- Persona probability range: 0.82 to 0.93
- Initial forecast probability: 0.665
- Latest forecast probability: 0.995
- Initial Brier component: 0.112225
- Latest Brier component: 2.5e-05
- Decision fair value range: 0.85 to 0.91
- Market reference price: 0.98
- Edge mid vs market pct points: -10.0
- Timeline excerpt:
- unknown-time — research swarm reported 5 completed personas
- 2026-04-13T19:41:00-04:00 — initial forecast recorded at 0.665
- 2026-04-14T10:43:00-04:00 — decision packet generated
- 2026-04-14T13:20:02-04:00 — market resolution recorded as yes
- 2026-04-14T13:38:00-04:00 — latest forecast recorded at 0.995
- 2026-04-14T14:20:57.840760+00:00 — prepared analysis `dispatch-case-20260414-9f18b170-20260414T142057Z` with summary `qualitative-db/40-research/cases/case-20260414-9f18b170/researcher-analyses/2026-04-14/dispatch-case-20260414-9f18b170-20260414T142057Z/summary.md`.
- 2026-04-14T14:20:57.840760+00:00 — synthesis runtime artifact written

## Which inputs were high signal

- base-rate: Binance is the governing source and sampled prices were already near $75.7k.
- catalyst-hunter: Coinbase and Kraken spot were around $75.7k on Apr 14.
- market-implied: Polymarket rules specify any Binance BTC/USDT 1-minute candle high at or above 76,000 resolves Yes.
- risk-manager: Polymarket rules only require any qualifying Binance 1-minute High during the window.
- variant-view: Binance BTCUSDT 24h high was 75715.55, leaving BTC within roughly 0.4% of the threshold.

## Which inputs were misleading

- base-rate: The sampled Binance high was still below $76k at the time checked, so the event had not yet happened.
- catalyst-hunter: The fetched Polymarket page did not cleanly expose full rule text, leaving some settlement-source ambiguity.
- market-implied: Binance had not yet printed 76,000 in the observed data.
- risk-manager: Settlement is Binance-specific, so other venues being near or above 76000 would not guarantee resolution.
- variant-view: The additional verification pass did not directly show a 76000 print yet.

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
