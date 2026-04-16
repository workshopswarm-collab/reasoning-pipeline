---
type: evidence_map
case_key: case-20260413-07f0191d
dispatch_id: dispatch-case-20260413-07f0191d-20260413T201947Z
research_run_id: 68c87da3-0cf0-4813-8848-9ec81e8daa2b
analysis_date: 2026-04-13
persona: catalyst-hunter
domain: politics
subdomain: bulgarian-parliamentary-election
entity:
topic: "exact-rank risk for GERB-SDS"
governing_source:
question: "Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?"
driver: elections
date_created: 2026-04-13
agent: Orchestrator
status: draft
confidence: medium-low
conflict_status: moderate
action_relevance: high
related_entities: []
related_drivers: ["elections", "polling"]
proposed_entities: ["GERB-SDS", "Revival", "PP-DB", "DPS", "Central Election Commission of Bulgaria"]
proposed_drivers: []
upstream_inputs: []
downstream_uses: ["qualitative-db/40-research/cases/case-20260413-07f0191d/researcher-analyses/2026-04-13/dispatch-case-20260413-07f0191d-20260413T201947Z/personas/catalyst-hunter.md"]
tags: ["auditability", "rank-order", "market-extreme"]
---

# Summary

The evidence does not support treating GERB–SDS finishing exactly second as a ~96% event. GERB–SDS appears more like a top-tier contender whose most likely rival paths are first or second, making the exact-second contract meaningfully less certain than the market price implies.

## Question being evaluated

Will GERB-UDF (GERB-SDS) finish second in the 2026 Bulgarian parliamentary election?

## Current lean

Lean NO versus the market price, while still acknowledging GERB–SDS could finish second.

## Prior / starting view

Starting view was that a 0.96 market price likely embeds either strong late polling consensus or a settlement-mechanics nuance. The available evidence did not validate such an extreme exact-rank confidence level.

## Evidence supporting the claim

- Wikipedia election overview indicates GERB–SDS is the current largest parliamentary bloc, so it is clearly a top-tier actor and could still plausibly land second if another rival overtakes it by election day. Weight: medium. Directness: contextual.
- POLITICO poll-of-polls extract still includes GERB-linked coalition among top Bulgarian parties. Weight: low-to-medium. Directness: contextual.
- Fragmented Bulgarian party competition makes exact second place plausible for several major blocs if late momentum shifts. Weight: medium. Directness: indirect structural logic.

## Evidence against the claim

- If GERB–SDS remains the modal first-place finisher, then YES is structurally overconfident because exact second excludes first. Weight: high. Directness: direct contract logic.
- No strong accessible source in this run showed a durable consensus that GERB–SDS had already settled into second place specifically. Weight: high. Directness: direct negative evidence.
- The market is at an extreme 96%, so the burden of proof is high; available evidence did not clear that bar. Weight: high. Directness: direct market-vs-evidence comparison.

## Ambiguous or mixed evidence

- Accessible polling context was incomplete and may be stale.
- Wikipedia is recent enough for schedule/context but not strong enough for exact-rank forecasting.
- CIK was identified as the governing source of truth in the contract, but direct fetch access was blocked during the run.

## Conflict between inputs

The main conflict is not source-vs-source but market-vs-evidence. The market implies near-certainty on exact second place, while the accessible evidence supports only a broad top-tier view with unresolved first-vs-second ordering.

## Key assumptions

- GERB–SDS remains competitive for first, not locked into second.
- No hidden settlement nuance overrides normal seat-ranking logic.
- Consensus reporting before official finalization will broadly track eventual CIK seat totals.

## Key uncertainties

- Current late-cycle polling median.
- Whether one rival bloc has recently consolidated into clear first place.
- Whether Bulgarian credible-reporting consensus is already stronger than what was accessible in this run.

## Disconfirming signals to watch

- Multiple independent late polls showing GERB–SDS consistently second.
- Election-night exit polls with another party clearly ahead and GERB–SDS clearly next.
- Credible Bulgarian media consensus converging on GERB–SDS as second before official seat allocation finalizes.

## What would increase confidence

- Direct CIK pre-election schedule and result-publication pages.
- At least two recent independent Bulgarian poll releases or a transparent polling aggregator.
- Reuters/AP or another high-quality international report summarizing the late race.

## Net update logic

What mattered most was the mismatch between an exact-rank market at 96% and evidence that only clearly established GERB–SDS as a major contender, not as a near-certain second-place finisher. I downweighted compromised or partial polling access and treated source-access limitations as a confidence reducer rather than a reason to force agreement with the market.

## Suggested downstream use

Use this as an audit trail for why the catalyst-hunter lane came in below market and flagged late polling / election-night reporting as the only truly high-information catalysts.